"""audiod client — HTTP control plane + dataclass wiring.

These tests hit the live audiod on 127.0.0.1:8090. The audiod daemon
runs as a background process; if it is down, integration tests are
skipped rather than failed (CI may run without a live audiod).

The dataclass + URL-construction tests are pure unit tests and always run.
"""
from __future__ import annotations

import socket

import pytest

from client import (
    AudiodClient,
    AudiodConfig,
    AudiodError,
    AudiodStream,
    DEFAULT_HTTP_PORT,
)


def _port_open(host: str, port: int, timeout: float = 0.25) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


@pytest.fixture(scope="module")
def live_client():
    """Yield an AudiodClient pointed at the live daemon, or skip if down."""
    if not _port_open("127.0.0.1", DEFAULT_HTTP_PORT):
        pytest.skip(f"audiod not running on :{DEFAULT_HTTP_PORT}")
    return AudiodClient()


# --- pure unit tests --------------------------------------------------------


class TestAudiodConfig:
    def test_defaults(self):
        c = AudiodConfig()
        assert c.host == "127.0.0.1"
        assert c.http_port == 8090
        assert c.ws_port == 8091
        assert c.timeout_s == 5.0

    def test_http_base_url(self):
        c = AudiodConfig(host="10.0.0.5", http_port=9000)
        assert c.http_base == "http://10.0.0.5:9000"

    def test_ws_url(self):
        c = AudiodConfig(host="dan.local", ws_port=18091)
        assert c.ws_url == "ws://dan.local:18091/"


class TestAudiodError:
    def test_message_truncates_body(self):
        e = AudiodError(500, "X" * 1000, "http://x/y")
        assert "audiod HTTP 500" in str(e)
        assert "on http://x/y" in str(e)
        # body should not be a literal substring of the message; truncation is fine
        assert len(str(e)) < 400


class TestClientConstruction:
    def test_default_uses_local_daemon(self):
        c = AudiodClient()
        assert c.cfg.http_port == DEFAULT_HTTP_PORT
        assert c.cfg.host == "127.0.0.1"


# --- integration tests (require live audiod) --------------------------------


class TestClientHTTPIntegration:
    def test_health_returns_ok(self, live_client):
        result = live_client.health()
        assert result["status"] == "ok"
        assert result["service"] == "audiod"

    def test_is_healthy_returns_true(self, live_client):
        assert live_client.is_healthy() is True

    def test_status_has_running_field(self, live_client):
        s = live_client.status()
        assert "running" in s
        assert isinstance(s["running"], bool)
        # Other fields audiod exposes
        for k in ("pid", "vad_ready", "device", "sample_rate", "whisper_model"):
            assert k in s, f"/status missing key {k}"

    def test_config_returns_sections(self, live_client):
        cfg = live_client.config()
        for k in ("audio", "vad", "whisper", "publish"):
            assert k in cfg, f"/config missing section {k}"

    def test_ptt_returns_ok(self, live_client):
        # PTT may be disabled; either way it returns {"ok": true}
        assert live_client.ptt() == {"ok": True}

    def test_start_stop_roundtrip(self, live_client):
        # The daemon starts running in the background. Stop then start should
        # both succeed. After start, is_running should be True.
        live_client.stop()
        assert live_client.is_running() is False
        live_client.start()
        assert live_client.is_running() is True

    def test_restart_preserves_health(self, live_client):
        r = live_client.restart()
        assert r.get("ok") is True
        # Give the pipeline a beat to come back up
        import time
        for _ in range(20):
            if live_client.is_running():
                break
            time.sleep(0.05)
        assert live_client.is_running() is True

    def test_reload_returns_ok(self, live_client):
        r = live_client.reload()
        assert r.get("ok") is True

    def test_unknown_route_raises(self, live_client):
        with pytest.raises(AudiodError) as ei:
            live_client._request("GET", "/does-not-exist")
        assert ei.value.status == 404


class TestClientOffline:
    """The client must surface a clean error when audiod is unreachable."""

    def test_unreachable_host_raises(self):
        # 127.0.0.1:1 is reserved and unbound; connection refused fast.
        c = AudiodClient(AudiodConfig(host="127.0.0.1", http_port=1, timeout_s=0.25))
        with pytest.raises(AudiodError) as ei:
            c.health()
        assert ei.value.status == 0  # connection-level failure

    def test_is_healthy_returns_false_when_down(self):
        c = AudiodClient(AudiodConfig(host="127.0.0.1", http_port=1, timeout_s=0.25))
        assert c.is_healthy() is False
        assert c.is_running() is False


class TestStreamConfig:
    """AudiodStream configuration wiring (no actual WS connection)."""

    def test_default_ws_url(self):
        s = AudiodStream()
        assert s.cfg.ws_url == "ws://127.0.0.1:8091/"

    def test_custom_host(self):
        s = AudiodStream(AudiodConfig(host="dan.local", ws_port=18091))
        assert s.cfg.ws_url == "ws://dan.local:18091/"

    def test_stop_sets_event(self):
        s = AudiodStream()
        assert not s._stop.is_set()
        s.stop()
        assert s._stop.is_set()