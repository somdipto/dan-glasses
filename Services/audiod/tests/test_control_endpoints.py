"""Tests for POST /start, /stop, /restart, /ptt, /reload control endpoints."""

import json
import threading
import time
from http.client import HTTPConnection

import pytest

import audiod as audiod_mod
from audiod import AudioPipeline, HealthHandler, start_health_server


def _load_minimal_config():
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


def _post(port: int, path: str) -> tuple[int, dict]:
    conn = HTTPConnection("127.0.0.1", port, timeout=2)
    conn.request("POST", path)
    resp = conn.getresponse()
    body = resp.read().decode("utf-8")
    conn.close()
    try:
        return resp.status, json.loads(body) if body else {}
    except json.JSONDecodeError:
        return resp.status, {"raw": body}


def _get(port: int, path: str) -> tuple[int, dict]:
    conn = HTTPConnection("127.0.0.1", port, timeout=2)
    conn.request("GET", path)
    resp = conn.getresponse()
    body = resp.read().decode("utf-8")
    conn.close()
    try:
        return resp.status, json.loads(body) if body else {}
    except json.JSONDecodeError:
        return resp.status, {"raw": body}


@pytest.fixture
def server():
    cfg = _load_minimal_config()
    pipeline = AudioPipeline(cfg)
    HealthHandler.pipeline = pipeline
    port = 18089
    srv = start_health_server(port)
    time.sleep(0.1)
    try:
        yield port, pipeline
    finally:
        try:
            pipeline._cmd_stop()
        except Exception:
            pass
        srv.shutdown()
        srv.server_close()
        HealthHandler.pipeline = None


def test_start_returns_ok(server):
    port, _ = server
    code, body = _post(port, "/start")
    assert code == 200
    assert body.get("ok") is True


def test_start_is_idempotent(server):
    port, _ = server
    code1, _ = _post(port, "/start")
    code2, _ = _post(port, "/start")
    assert code1 == 200
    assert code2 == 200


def test_stop_returns_ok(server):
    port, _ = server
    _post(port, "/start")
    code, body = _post(port, "/stop")
    assert code == 200
    assert body.get("ok") is True


def test_ptt_returns_ok(server):
    port, _ = server
    code, body = _post(port, "/ptt")
    assert code == 200
    assert body.get("ok") is True


def test_restart_returns_ok(server):
    port, _ = server
    code, _ = _post(port, "/restart")
    assert code == 200


def test_reload_returns_ok(server):
    port, _ = server
    code, body = _post(port, "/reload")
    assert code == 200


def test_unknown_path_returns_404(server):
    port, _ = server
    conn = HTTPConnection("127.0.0.1", port, timeout=2)
    conn.request("POST", "/bogus")
    resp = conn.getresponse()
    resp.read()
    conn.close()
    assert resp.status == 404


def test_pipeline_unset_returns_503():
    HealthHandler.pipeline = None
    port = 18088
    srv = start_health_server(port)
    time.sleep(0.1)
    try:
        code, body = _post(port, "/start")
        assert code == 503
        assert "error" in body
    finally:
        srv.shutdown()
        srv.server_close()
