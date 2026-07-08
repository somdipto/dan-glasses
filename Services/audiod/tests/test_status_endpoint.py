"""Tests for /status endpoint diagnostics."""

import json
import threading
import time
from http.client import HTTPConnection

import pytest

import audiod as audiod_mod
from audiod import AudioPipeline, HealthHandler, start_health_server


def _load_minimal_config():
    """Build an in-memory config that doesn't require real audio/whisper hardware."""
    return {
        "audio": {
            "device": "default",
            "sample_rate": 16000,
            "channels": 1,
            "period_size": 512,
            "buffer_periods": 8,
        },
        "vad": {
            "threshold": 0.5,
            "min_speech_ms": 250,
            "min_silence_ms": 200,
        },
        "whisper": {
            "model": "/tmp/fake-ggml-base.bin",
            "language": "auto",
            "threads": 2,
        },
        "publish": {"mode": "stdout", "socket_path": "/tmp/audiod-test.sock", "ws_port": 0},
        "push_to_talk": {"enabled": False, "hotkey": "space"},
    }


def _get_status(port: int) -> dict:
    conn = HTTPConnection("127.0.0.1", port, timeout=2)
    conn.request("GET", "/status")
    resp = conn.getresponse()
    body = resp.read().decode("utf-8")
    conn.close()
    return json.loads(body)


def _spin_pipeline_server(cfg):
    """Start a health server on an ephemeral port; return (server, port, pipeline).

    Always restores HealthHandler.pipeline to None on teardown so the
    class-level singleton cannot leak across tests.
    """
    pipeline = AudioPipeline(cfg)
    prior_pipeline = HealthHandler.pipeline
    HealthHandler.pipeline = pipeline
    server = start_health_server(0)
    port = server.server_address[1]
    return server, port, pipeline, prior_pipeline


def _teardown(server, prior_pipeline):
    try:
        server.shutdown()
        server.server_close()
    finally:
        HealthHandler.pipeline = prior_pipeline


def test_status_returns_extended_diagnostics():
    """The enriched /status should include device, model, sample rate, and uptime."""
    cfg = _load_minimal_config()
    server, port, pipeline, prior = _spin_pipeline_server(cfg)
    try:
        time.sleep(0.1)
        body = _get_status(port)
    finally:
        _teardown(server, prior)

    assert body["service"] == "audiod"
    assert body["vad_ready"] in (True, False)
    assert body["device"] == "default"
    assert body["sample_rate"] == 16000
    assert body["channels"] == 1
    assert body["whisper_model"] == "/tmp/fake-ggml-base.bin"
    assert body["whisper_threads"] == 2
    assert body["ptt_enabled"] is False
    assert body["ptt_hotkey"] == "space"
    assert body["started_at_ms"] > 0
    assert body["uptime_ms"] >= 0
    assert body["pid"] > 0
    assert body["segments_transcribed"] == 0
    assert "publisher" in body
    assert body["publisher"]["mode"] == "stdout"
    assert isinstance(body["publisher"]["ws_port"], int)


def test_status_handles_pipeline_unset():
    """If no pipeline is registered, /status should still return valid JSON."""
    prior = HealthHandler.pipeline
    HealthHandler.pipeline = None
    server = start_health_server(0)
    port = server.server_address[1]
    try:
        time.sleep(0.1)
        body = _get_status(port)
    finally:
        server.shutdown()
        server.server_close()
        HealthHandler.pipeline = prior

    assert body["service"] == "audiod"
    assert body["running"] is False
    assert body["vad_ready"] is False


def test_segments_transcribed_increments():
    """Each published transcript should bump the counter."""
    cfg = _load_minimal_config()
    server, port, pipeline, prior = _spin_pipeline_server(cfg)
    try:
        # Simulate 3 successful publishes
        for _ in range(3):
            with pipeline._lock:
                pipeline._segments_transcribed += 1
        time.sleep(0.1)
        body = _get_status(port)
    finally:
        _teardown(server, prior)

    assert body["segments_transcribed"] == 3


def test_status_exposes_whisper_readiness_booleans():
    """/status must expose whisper_binary_ok and whisper_model_ok as booleans.

    Operators need to distinguish "whisper-cli missing" from "model file
    missing" without reading stderr. The strings whisper_binary /
    whisper_model alone don't make this distinction.
    """
    cfg = _load_minimal_config()
    server, port, pipeline, prior = _spin_pipeline_server(cfg)
    try:
        time.sleep(0.1)
        body = _get_status(port)
    finally:
        _teardown(server, prior)

    # The new boolean fields are present and are real booleans.
    assert "whisper_binary_ok" in body
    assert "whisper_model_ok" in body
    assert isinstance(body["whisper_binary_ok"], bool)
    assert isinstance(body["whisper_model_ok"], bool)
    # The /status strings still exist for backward compatibility.
    assert isinstance(body["whisper_binary"], str)
    assert body["whisper_model"] == "/tmp/fake-ggml-base.bin"


def test_status_last_segment_ms_defaults_to_zero():
    """Before any segment is transcribed, last_segment_ms is 0."""
    cfg = _load_minimal_config()
    server, port, pipeline, prior = _spin_pipeline_server(cfg)
    try:
        time.sleep(0.1)
        body = _get_status(port)
    finally:
        _teardown(server, prior)

    assert body["last_segment_ms"] == 0


def test_status_last_segment_ms_updates_after_transcribe():
    """last_segment_ms reflects the duration of the most recent successful transcription."""
    import numpy as np

    cfg = _load_minimal_config()
    server, port, pipeline, prior = _spin_pipeline_server(cfg)
    try:
        # Stub the transcriber so we don't depend on whisper-cli / a real model.
        pipeline.transcriber.transcribe = lambda segment, sr: {"text": "hello", "confidence": 0.9}

        # Simulate a 1.5s mono segment at 16 kHz being transcribed successfully.
        sr = 16000
        samples = np.zeros(sr * 3 // 2, dtype=np.float32)  # 1.5s
        pipeline._run_transcribe(samples, start_ms=0)

        time.sleep(0.1)
        body = _get_status(port)
    finally:
        _teardown(server, prior)

    # 1.5s = 1500 ms
    assert body["last_segment_ms"] == 1500
    # The transcribe counter advanced too, since _run_transcribe only
    # stamps last_segment_ms on a successful publish.
    assert body["segments_transcribed"] == 1


def test_status_last_segment_ms_resets_on_start():
    """Calling _reset_counters must clear last_segment_ms back to 0."""
    import numpy as np

    cfg = _load_minimal_config()
    server, port, pipeline, prior = _spin_pipeline_server(cfg)
    try:
        # Prime last_segment_ms with a fake value.
        with pipeline._lock:
            pipeline._last_segment_ms = 4242

        # _cmd_start exercises _reset_counters without touching the capture thread.
        pipeline._cmd_start()
        pipeline._cmd_stop()  # don't leave the capture loop running

        time.sleep(0.1)
        body = _get_status(port)
    finally:
        _teardown(server, prior)

    assert body["last_segment_ms"] == 0
