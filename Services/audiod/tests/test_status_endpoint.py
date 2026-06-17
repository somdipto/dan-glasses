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
        "publish": {"mode": "stdout", "socket_path": "/tmp/audiod-test.sock", "ws_port": 18091},
        "push_to_talk": {"enabled": False, "hotkey": "space"},
    }


def _get_status(port: int) -> dict:
    conn = HTTPConnection("127.0.0.1", port, timeout=2)
    conn.request("GET", "/status")
    resp = conn.getresponse()
    body = resp.read().decode("utf-8")
    conn.close()
    return json.loads(body)


def test_status_returns_extended_diagnostics():
    """The enriched /status should include device, model, sample rate, and uptime."""
    cfg = _load_minimal_config()
    pipeline = AudioPipeline(cfg)
    HealthHandler.pipeline = pipeline

    port = 18099
    server = start_health_server(port)
    try:
        time.sleep(0.1)
        body = _get_status(port)
    finally:
        server.shutdown()
        server.server_close()

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
    assert body["publisher"]["ws_port"] == 18091


def test_status_handles_pipeline_unset():
    """If no pipeline is registered, /status should still return valid JSON."""
    HealthHandler.pipeline = None
    port = 18098
    server = start_health_server(port)
    try:
        time.sleep(0.1)
        body = _get_status(port)
    finally:
        server.shutdown()
        server.server_close()

    assert body["service"] == "audiod"
    assert body["running"] is False
    assert body["vad_ready"] is False


def test_segments_transcribed_increments():
    """Each published transcript should bump the counter."""
    cfg = _load_minimal_config()
    pipeline = AudioPipeline(cfg)
    HealthHandler.pipeline = pipeline

    # Simulate 3 successful publishes
    for _ in range(3):
        with pipeline._lock:
            pipeline._segments_transcribed += 1

    port = 18097
    server = start_health_server(port)
    try:
        time.sleep(0.1)
        body = _get_status(port)
    finally:
        server.shutdown()
        server.server_close()

    assert body["segments_transcribed"] == 3
