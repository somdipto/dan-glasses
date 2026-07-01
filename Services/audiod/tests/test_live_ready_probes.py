"""Tests for /live and /ready probes (v1.1).

Contract:
  GET /live  -> 200 always (when HTTP server up). Never 503.
  GET /ready -> 200 + breakdown when pipeline fully ready.
                 503 + status:loading + readiness breakdown + reason otherwise.

The K8s pattern is:
  livenessProbe  -> /live   (restart when dead)
  readinessProbe -> /ready  (route traffic only when ready)
"""
from __future__ import annotations

import http.client
import json
import os
import socket
import threading
import time

import pytest

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
    """HealthHandler with pipeline=None. /ready must say loading."""
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


class TestLiveProbe:
    """/live is the orchestrator restart decision. Must NEVER 503."""

    def test_live_no_pipeline_returns_200(self, empty_handler_port):
        """Even when pipeline is None (process just started), /live is 200.

        Liveness means "is the process responsive?" — not "is it ready
        for traffic?". That's /ready's job.
        """
        status, body = _get(empty_handler_port, "/live")
        assert status == 200
        assert body["status"] == "alive"
        assert body["service"] == "audiod"
        assert "pid" in body

    def test_live_returns_pid(self, empty_handler_port):
        _, body = _get(empty_handler_port, "/live")
        assert isinstance(body["pid"], int)
        assert body["pid"] > 0


class TestReadyProbe:
    """/ready is the orchestrator traffic-routing decision."""

    def test_ready_no_pipeline_returns_503(self, empty_handler_port):
        status, body = _get(empty_handler_port, "/ready")
        assert status == 503
        assert body["status"] == "loading"
        assert body["service"] == "audiod"
        assert "readiness" in body
        readiness = body["readiness"]
        assert readiness["vad"] is False
        assert readiness["publisher"] is False
        assert readiness["running"] is False

    def test_ready_no_pipeline_has_reason(self, empty_handler_port):
        status, body = _get(empty_handler_port, "/ready")
        assert status == 503
        assert "reason" in body
        assert isinstance(body["reason"], str)
        assert "pipeline not initialized" in body["reason"]

    def test_ready_missing_model_returns_503(self):
        port = _free_port()
        cfg = _tiny_config(model_path="/nonexistent/ggml-base.bin")
        HealthHandler.pipeline = _build_pipeline_from_config(cfg, config_path=None)
        server = start_health_server(port=port)
        assert _wait_for_port(port)
        try:
            status, body = _get(port, "/ready")
            assert status == 503
            assert body["status"] == "loading"
            readiness = body["readiness"]
            assert readiness["whisper_binary"] is True
            assert readiness["whisper_model"] is False
            assert body["reason"]
        finally:
            server.shutdown()
            server.server_close()
            HealthHandler.pipeline = None

    def test_ready_pipeline_returns_200(self):
        port = _free_port()
        cfg = _tiny_config(model_path="/home/workspace/dan-glasses/models/ggml-base.bin")
        if not os.path.exists(cfg["whisper"]["model"]):
            pytest.skip("whisper model not present on this host")
        HealthHandler.pipeline = _build_pipeline_from_config(cfg, config_path=None)
        server = start_health_server(port=port)
        assert _wait_for_port(port)
        try:
            status, body = _get(port, "/ready")
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


class TestHealthBackcompatAlias:
    """/health must still work — it's the back-compat alias for /ready."""

    def test_health_no_pipeline_returns_503(self, empty_handler_port):
        """Old contract: /health 503 with status:loading when not ready."""
        status, body = _get(empty_handler_port, "/health")
        assert status == 503
        assert body["status"] == "loading"
        assert "readiness" in body

    def test_health_ready_returns_200(self):
        port = _free_port()
        cfg = _tiny_config(model_path="/home/workspace/dan-glasses/models/ggml-base.bin")
        if not os.path.exists(cfg["whisper"]["model"]):
            pytest.skip("whisper model not present on this host")
        HealthHandler.pipeline = _build_pipeline_from_config(cfg, config_path=None)
        server = start_health_server(port=port)
        assert _wait_for_port(port)
        try:
            status, body = _get(port, "/health")
            assert status == 200
            assert body["status"] == "ok"
            assert "readiness" in body
        finally:
            server.shutdown()
            server.server_close()
            HealthHandler.pipeline = None

    def test_health_and_ready_return_same_shape(self, empty_handler_port):
        """The /health alias must return the same body as /ready."""
        _, h_body = _get(empty_handler_port, "/health")
        _, r_body = _get(empty_handler_port, "/ready")
        # Same status, status, service, readiness. /ready has reason
        # only when not ready, but the shape otherwise mirrors /health.
        assert h_body["status"] == r_body["status"]
        assert h_body["service"] == r_body["service"]
        assert h_body["readiness"] == r_body["readiness"]