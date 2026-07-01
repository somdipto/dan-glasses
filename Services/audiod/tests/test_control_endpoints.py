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


def test_help_endpoint_returns_api_surface():
    """GET /help documents the audiod HTTP API as JSON."""
    HealthHandler.pipeline = AudioPipeline(_load_minimal_config())
    port = 18093
    srv = start_health_server(port)
    time.sleep(0.1)
    try:
        code, body = _get(port, "/help")
        assert code == 200
        assert body["service"] == "audiod"
        assert body["http_port"] == 18093
        paths = {ep["path"] for ep in body["endpoints"]}
        assert "/health" in paths
        assert "/status" in paths
        assert "/config" in paths
        assert "/reload" in paths
        assert "/start" in paths
        assert "/stop" in paths
        assert "/restart" in paths
        assert "/ptt" in paths
        # Every endpoint has method+path+desc
        for ep in body["endpoints"]:
            assert "method" in ep and "path" in ep and "desc" in ep
    finally:
        srv.shutdown()
        srv.server_close()


def test_reload_hot_swaps_whisper_model_no_restart():
    """POST /reload swaps whisper model + threads live without restart.

    Verifies the v0.7 SPEC claim: whisper model path is hot-swappable.
    Uses an isolated tmp config file so the test never touches the real
    `Services/audiod/config.yaml`.
    """
    import os
    import tempfile
    import yaml as _yaml

    cfg = _load_minimal_config()
    MODELS = [
        "/home/workspace/dan-glasses/models/ggml-base.bin",
        "/home/workspace/dan-glasses/models/ggml-tiny.bin",
    ]
    cfg["whisper"]["model"] = MODELS[0]
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as tmp:
        _yaml.safe_dump(cfg, tmp)
        cfg_path = tmp.name
    try:
        pipeline = AudioPipeline(cfg, config_path=cfg_path)
        HealthHandler.pipeline = pipeline
        port = 18094
        srv = start_health_server(port)
        time.sleep(0.1)
        try:
            assert pipeline.transcriber.model_path == MODELS[0]
            assert pipeline.transcriber.threads == 2

            # Mutate ONLY the tmp config and trigger reload.
            with open(cfg_path, "r") as f:
                disk_cfg = _yaml.safe_load(f)
            disk_cfg["whisper"]["model"] = MODELS[1]
            disk_cfg["whisper"]["threads"] = 4
            with open(cfg_path, "w") as f:
                _yaml.safe_dump(disk_cfg, f)

            code, body = _post(port, "/reload")
            assert code == 200
            assert body["ok"] is True
            assert body["whisper_model"] == MODELS[1]
            assert body["whisper_threads"] == 4
            # No audio/publish/ptt fields changed → nothing pending restart.
            assert body["pending_restart_for"] == []
            # Verify the transcriber actually picked up the new model.
            assert pipeline.transcriber.model_path == MODELS[1]
            assert pipeline.transcriber.threads == 4
        finally:
            srv.shutdown()
            srv.server_close()
    finally:
        os.unlink(cfg_path)
