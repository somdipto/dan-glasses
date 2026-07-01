"""Tests for the /health startup-probe refactor.

The P0 bug fixed in 2026-06-28 (see dan2.md / dan2-architecture-review.md):
/health returned {"status":"ok"} unconditionally. memoryd was observed
returning 200 ok while its model was still loading (process alive, port
not bound). audiod had the same shape. These tests pin the new contract:

  /health 200 + status:ok          — pipeline fully ready
  /health 503 + status:loading     — any required component not ready
  /health body includes a readiness breakdown

Tests run in-process against a HealthHandler bound to an ephemeral port,
no live audiod required.
"""
from __future__ import annotations

import http.client
import json
import os
import socket
import threading
import time

import pytest

# Import the handler + pipeline factory
from audiod import HealthHandler, start_health_server, _build_pipeline_from_config


def _free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def _wait_for_port(port: int, timeout: float = 2.0) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        with socket.socket() as s:
            s.settimeout(0.1)
            try:
                s.connect(("127.0.0.1", port))
                return True
            except OSError:
                time.sleep(0.05)
    return False


def _get(port: int, path: str) -> tuple[int, dict]:
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=2.0)
    try:
        conn.request("GET", path)
        r = conn.getresponse()
        body = r.read().decode()
        return r.status, json.loads(body)
    finally:
        conn.close()


@pytest.fixture
def empty_handler_port():
    """Bind HealthHandler with pipeline=None; tear down after the test."""
    port = _free_port()
    HealthHandler.pipeline = None
    server = start_health_server(port=port)
    assert _wait_for_port(port)
    try:
        yield port
    finally:
        server.shutdown()
        server.server_close()
        HealthHandler.pipeline = None


def _make_pipeline_with_config(cfg: dict, config_path: str | None = None):
    """Build an AudioPipeline from an in-memory dict (no config.yaml)."""
    return _build_pipeline_from_config(cfg, config_path=config_path)


def _tiny_config(model_path: str) -> dict:
    return {
        "audio": {"device": "default", "sample_rate": 16000, "channels": 1,
                  "period_size": 512, "buffer_periods": 8},
        "vad": {"threshold": 0.5, "min_speech_ms": 250, "min_silence_ms": 200,
                "max_segment_ms": 10000},
        "whisper": {"model": model_path, "language": "auto", "threads": 1},
        "publish": {"mode": "stdout", "ws_port": 0, "socket_path": "/tmp/_audiod_test.sock"},
        "push_to_talk": {"enabled": False, "hotkey": "space"},
    }


class TestHealthStartupProbe:
    """The new /health contract."""

    def test_no_pipeline_returns_503(self, empty_handler_port):
        """With pipeline=None (process just started, model not loaded),
        /health must return 503 with status:loading. NOT a green ok."""
        status, body = _get(empty_handler_port, "/health")
        assert status == 503
        assert body["status"] == "loading"
        assert body["service"] == "audiod"
        # Body must surface a readiness breakdown so operators can debug
        assert "readiness" in body

    def test_no_pipeline_body_has_reason(self, empty_handler_port):
        status, body = _get(empty_handler_port, "/health")
        assert status == 503
        assert "reason" in body
        assert isinstance(body["reason"], str)
        assert len(body["reason"]) > 0

    def test_missing_model_returns_503(self):
        """If whisper model file doesn't exist, /health must be loading."""
        port = _free_port()
        cfg = _tiny_config(model_path="/nonexistent/ggml-base.bin")
        # pipeline init should not raise (binary lookup is lazy)
        HealthHandler.pipeline = _make_pipeline_with_config(cfg, config_path=None)
        server = start_health_server(port=port)
        assert _wait_for_port(port)
        try:
            status, body = _get(port, "/health")
            assert status == 503
            assert body["status"] == "loading"
            readiness = body["readiness"]
            assert readiness["whisper_binary"] is True   # whisper-cli is installed
            assert readiness["whisper_model"] is False  # but the model file is missing
            assert body["reason"]
        finally:
            server.shutdown()
            server.server_close()
            HealthHandler.pipeline = None

    def test_ready_pipeline_returns_200(self):
        """When everything is present, /health returns 200 ok with full breakdown."""
        port = _free_port()
        cfg = _tiny_config(model_path="/home/workspace/dan-glasses/models/ggml-base.bin")
        # If the model file is actually missing on this host, skip rather than fail.
        if not os.path.exists(cfg["whisper"]["model"]):
            pytest.skip("whisper model not present on this host")
        HealthHandler.pipeline = _make_pipeline_with_config(cfg, config_path=None)
        # The transcriber does NOT load the model eagerly; readiness only
        # checks binary + model-file existence, which is the contract.
        server = start_health_server(port=port)
        assert _wait_for_port(port)
        try:
            status, body = _get(port, "/health")
            assert status == 200, body
            assert body["status"] == "ok"
            assert body["service"] == "audiod"
            readiness = body["readiness"]
            assert readiness["vad"] is True
            assert readiness["whisper_binary"] is True
            assert readiness["whisper_model"] is True
            assert readiness["publisher"] is True
        finally:
            server.shutdown()
            server.server_close()
            HealthHandler.pipeline = None


class TestHealthTranscriberReady:
    """WhisperTranscriber.is_ready() contract."""

    def test_binary_resolved_and_model_exists(self):
        from transcription import WhisperTranscriber
        path = "/home/workspace/dan-glasses/models/ggml-base.bin"
        if not os.path.exists(path):
            pytest.skip("whisper model not present on this host")
        t = WhisperTranscriber(model_path=path)
        ready, breakdown = t.is_ready()
        assert ready is True
        assert breakdown["binary"] is True
        assert breakdown["model"] is True

    def test_model_missing_makes_not_ready(self):
        from transcription import WhisperTranscriber
        t = WhisperTranscriber(model_path="/nonexistent/ggml-base.bin")
        ready, breakdown = t.is_ready()
        assert ready is False
        assert breakdown["model"] is False


class TestHealthPublisherReady:
    """TranscriptPublisher.is_ready() contract."""

    def test_stdout_mode_is_ready(self):
        from publish import TranscriptPublisher
        p = TranscriptPublisher(mode="stdout")
        ready, breakdown = p.is_ready()
        assert ready is True
        assert breakdown["mode"] == "stdout"
