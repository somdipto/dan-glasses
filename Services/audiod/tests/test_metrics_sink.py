"""Tests for the LokiMetricsSink (v1.3: structured-metric push to Loki).

Covers:
- Disabled sink (AUDIOD_METRICS=0 or enabled=False): no thread, no push,
  observe() is a no-op, snapshot reports enabled=False.
- Enabled sink: observe() formats stable lines, flush() builds a valid
  Loki push payload, HTTP 2xx counts as push_ok, non-2xx counts as
  push_failed, URLError counts as push_failed, drops counter increments
  when buffer is full.
- /status exposes a metrics block with all counters.
- AudioPipeline calls sink.observe() after each successful transcription.

These tests use a local HTTP server (loki stub) to receive pushes
without depending on a real Loki at :3100.
"""

from __future__ import annotations

import json
import os
import threading
import time
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

# Ensure no inherited env flag from a parent shell turns the sink on.
os.environ.pop("AUDIOD_METRICS", None)
os.environ.pop("AUDIOD_LOKI_URL", None)

from metrics import LokiMetricsSink  # noqa: E402


# ---------- helpers ---------- #


class _LokiStub:
    """Tiny in-process Loki push endpoint.

    Captures every POST it receives, exposes the latest one for
    assertions, and can be configured to return arbitrary status codes
    or raise URLErrors to exercise the sink's error path.
    """

    def __init__(self, status: int = 204, raise_on_post: bool = False):
        self.status = status
        self.raise_on_post = raise_on_post
        self.received: list[dict] = []
        self._lock = threading.Lock()
        self._server: HTTPServer | None = None
        self._thread: threading.Thread | None = None

    @property
    def url(self) -> str:
        assert self._server is not None, "loki stub not started"
        host, port = self._server.server_address
        return f"http://{host}:{port}/loki/api/v1/push"

    def received_count(self) -> int:
        with self._lock:
            return len(self.received)

    def __enter__(self) -> "_LokiStub":
        outer = self

        class _Server(HTTPServer):
            # Reuse the listening socket across test boundaries so a prior
            # _LokiStub's TIME_WAIT doesn't block the next bind on a flaky
            # kernel. Same pattern used by audiod's health server in tests.
            allow_reuse_address = True

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):  # noqa: N802
                length = int(self.headers.get("Content-Length", "0"))
                raw = self.rfile.read(length) if length else b""
                if outer.raise_on_post:
                    self.send_response(500)
                    self.end_headers()
                    return
                try:
                    payload = json.loads(raw.decode("utf-8"))
                except Exception:  # noqa: BLE001
                    payload = {"_raw": raw.decode("utf-8", "replace")}
                with outer._lock:
                    outer.received.append(payload)
                self.send_response(outer.status)
                self.end_headers()

            def log_message(self, *_a, **_kw):  # silence
                return

        self._server = _Server(("127.0.0.1", 0), Handler)
        self._thread = threading.Thread(
            target=self._server.serve_forever, daemon=True
        )
        self._thread.start()
        # Give the kernel a beat to actually bind. Without this, a
        # follow-up test that re-creates the stub can race a TIME_WAIT
        # and hit EADDRINUSE on a slow CI host.
        time.sleep(0.01)
        return self

    def __exit__(self, *_a) -> None:
        if self._server is not None:
            self._server.shutdown()
            self._server.server_close()
        if self._thread is not None:
            self._thread.join(timeout=1.0)


def _wait_until(predicate, timeout: float = 2.0, interval: float = 0.01) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if predicate():
            return True
        time.sleep(interval)
    return predicate()


# ---------- constructor / disabled ---------- #


def test_disabled_via_explicit_arg():
    sink = LokiMetricsSink(service="audiod", enabled=False)
    assert sink.snapshot()["enabled"] is False
    # observe() is a no-op when disabled.
    sink.observe("segment_timing", {"p50_ms": 100})
    assert sink.snapshot()["pending"] == 0
    # start() with disabled should NOT spawn a thread.
    sink.start()
    assert sink._thread is None
    sink.stop()  # safe to call when never started


def test_disabled_via_env_var(monkeypatch):
    monkeypatch.setenv("AUDIOD_METRICS", "0")
    sink = LokiMetricsSink(service="audiod")
    assert sink.snapshot()["enabled"] is False
    sink.start()
    assert sink._thread is None
    sink.stop()


def test_env_var_truthy_values_enable(monkeypatch):
    for v in ("1", "true", "yes", "on", "TRUE"):
        monkeypatch.setenv("AUDIOD_METRICS", v)
        sink = LokiMetricsSink(service="audiod")
        assert sink.snapshot()["enabled"] is True, f"env={v}"


def test_explicit_enabled_overrides_env(monkeypatch):
    monkeypatch.setenv("AUDIOD_METRICS", "1")
    sink = LokiMetricsSink(service="audiod", enabled=False)
    assert sink.snapshot()["enabled"] is False


def test_constructor_rejects_bad_args():
    with pytest.raises(ValueError):
        LokiMetricsSink(interval_s=0)
    with pytest.raises(ValueError):
        LokiMetricsSink(interval_s=-1)
    with pytest.raises(ValueError):
        LokiMetricsSink(max_buffer=0)


def test_constructor_accepts_env_url_override(monkeypatch):
    monkeypatch.setenv("AUDIOD_LOKI_URL", "http://override.example/push")
    sink = LokiMetricsSink(service="audiod")
    assert sink.snapshot()["loki_url"] == "http://override.example/push"


# ---------- formatting ---------- #


def test_format_line_stable_for_segment_timing():
    line = LokiMetricsSink._format_line(
        "segment_timing",
        {"p50_ms": 250, "p95_ms": 1100, "count": 42},
        "ms",
    )
    # The line is JSON-encoded into the push payload, so the in-memory
    # string contains JSON-escaped quotes (\\\" in raw form). Decode
    # for readability before asserting on the labels.
    assert line.startswith("audiod_metric{")
    decoded = line.encode().decode("unicode_escape")
    assert 'service="audiod"' in decoded
    assert 'kind="segment_timing"' in decoded
    assert 'unit="ms"' in decoded
    # Fields are sorted by key (stable for diffs).
    assert "count=42" in line
    assert "p50_ms=250" in line
    assert "p95_ms=1100" in line


def test_format_line_handles_empty_fields():
    line = LokiMetricsSink._format_line("noop", {}, "ms")
    assert line.endswith("}")
    # With no fields the body is the head alone.
    assert " " not in line.rstrip("}")


def test_format_line_value_types():
    """Booleans → 1/0, ints/floats stable, strings quoted."""
    line = LokiMetricsSink._format_line(
        "x",
        {"b": True, "i": 7, "f": 1.5, "s": "hi", "n": None},
        "ms",
    )
    assert "b=1" in line
    assert "i=7" in line
    assert "f=1.5000" in line
    assert "s=hi" in line  # "hi" has no special chars, unquoted
    assert 'n=""' in line


# ---------- push behavior ---------- #


def test_observe_then_flush_pushes_to_loki():
    with _LokiStub(status=204) as loki:
        sink = LokiMetricsSink(
            service="audiod",
            loki_url=loki.url,
            interval_s=0.05,
            timeout_s=1.0,
        )
        sink.start()
        try:
            sink.observe("segment_timing", {"p50_ms": 250, "p95_ms": 1100, "count": 5})
            assert _wait_until(lambda: loki.received_count() >= 1)
            payload = loki.received[0]
            assert "streams" in payload
            stream = payload["streams"][0]
            assert stream["stream"]["service"] == "audiod"
            assert stream["stream"]["job"] == "audiod"
            values = stream["values"]
            assert len(values) == 1
            ts, line = values[0]
            assert int(ts) > 0
            decoded = line.encode().decode("unicode_escape")
            assert 'kind="segment_timing"' in decoded
            assert "p50_ms=250" in line
            assert "p95_ms=1100" in line
            assert "count=5" in line
            # Counters reflect one successful push.
            assert sink.snapshot()["pushes_ok"] == 1
            assert sink.snapshot()["pushes_failed"] == 0
        finally:
            sink.stop()


def test_non_2xx_counts_as_push_failed():
    with _LokiStub(status=500) as loki:
        sink = LokiMetricsSink(
            service="audiod",
            loki_url=loki.url,
            interval_s=0.05,
            timeout_s=1.0,
        )
        sink.start()
        try:
            sink.observe("segment_timing", {"p50_ms": 100})
            assert _wait_until(lambda: loki.received_count() >= 1)
            assert _wait_until(lambda: sink.snapshot()["pushes_failed"] >= 1)
            assert sink.snapshot()["pushes_ok"] == 0
        finally:
            sink.stop()


def test_network_error_counts_as_push_failed():
    """If the URL is unreachable the sink must keep going and tally
    the failure without crashing the pipeline."""
    sink = LokiMetricsSink(
        service="audiod",
        loki_url="http://127.0.0.1:1/loki/api/v1/push",  # unbound
        interval_s=0.05,
        timeout_s=0.2,
    )
    sink.start()
    try:
        sink.observe("segment_timing", {"p50_ms": 100})
        assert _wait_until(lambda: sink.snapshot()["pushes_failed"] >= 1)
        assert sink.snapshot()["pushes_ok"] == 0
        # Subsequent observations must still be accepted (no thread death).
        sink.observe("segment_timing", {"p50_ms": 200})
    finally:
        sink.stop()


def test_buffer_full_drops_oldest_and_increments_counter():
    """When the buffer is saturated the sink drops the oldest entry
    (never blocks the caller) and increments the drops counter."""
    sink = LokiMetricsSink(
        service="audiod",
        loki_url="http://127.0.0.1:1/loki/api/v1/push",  # fails fast
        interval_s=10.0,  # don't auto-flush
        max_buffer=3,
        timeout_s=0.1,
    )
    sink.start()
    try:
        for i in range(10):
            sink.observe("segment_timing", {"i": i})
        snap = sink.snapshot()
        # The buffer was capped at 3; once full each new observe() drops
        # the oldest, so we should have 3 pending and 7 drops.
        assert snap["pending"] == 3
        assert snap["drops"] == 7
    finally:
        sink.stop()


def test_active_kinds_tracks_distinct_kinds():
    """snapshot()'s active_kinds reflects the distinct kinds currently
    buffered (or last buffered, post-flush)."""
    sink = LokiMetricsSink(
        service="audiod",
        loki_url="http://127.0.0.1:1/loki/api/v1/push",  # ignore
        interval_s=10.0,  # don't auto-flush
        enabled=True,
    )
    sink.observe("segment_timing", {"a": 1})
    sink.observe("segment_timing", {"a": 2})
    sink.observe("other_metric", {"b": 1})
    snap = sink.snapshot()
    assert sorted(snap["active_kinds"]) == ["other_metric", "segment_timing"]
    assert snap["pending"] == 3
    sink.stop()


# ---------- /status integration ---------- #


def test_status_exposes_metrics_block(monkeypatch, audiod_config_path):
    """The /status endpoint must surface the metrics block with the
    full set of counters (pushes_ok, pushes_failed, drops, etc) so the
    UI can render a 'Loki shipping' health pill."""
    monkeypatch.delenv("AUDIOD_METRICS", raising=False)
    import yaml

    from audiod import AudioPipeline, HealthHandler, start_health_server

    with open(audiod_config_path, "r") as f:
        cfg = yaml.safe_load(f)
    cfg.setdefault("metrics", {})["enabled"] = False  # sink in-process
    cfg["publish"] = {"mode": "stdout", "ws_port": 0}

    pipeline = AudioPipeline(config=cfg)
    HealthHandler.pipeline = pipeline

    srv = start_health_server(0)
    try:
        # Discover the actual bound port.
        port = srv.server_address[1]
        conn = HTTPConnection("127.0.0.1", port, timeout=2)
        conn.request("GET", "/status")
        resp = conn.getresponse()
        assert resp.status == 200
        body = json.loads(resp.read().decode("utf-8"))
        assert "metrics" in body, f"missing metrics block in /status: keys={list(body)}"
        m = body["metrics"]
        for k in (
            "enabled",
            "loki_url",
            "interval_s",
            "pending",
            "active_kinds",
            "last_push_ts",
            "pushes_ok",
            "pushes_failed",
            "drops",
        ):
            assert k in m, f"missing metrics key: {k}"
        assert m["enabled"] is False
    finally:
        srv.shutdown()
        try:
            srv.server_close()
        except Exception:  # noqa: BLE001
            pass


# ---------- pipeline integration ---------- #


def test_pipeline_observe_called_on_transcribe(monkeypatch, audiod_config_path):
    """The pipeline must call self._metrics.observe() with the
    segment_timing snapshot after a successful transcription. We
    bypass VAD + whisper by stubbing the publisher and the
    transcriber, then drive a synthetic segment through
    _run_transcribe directly."""
    monkeypatch.delenv("AUDIOD_METRICS", raising=False)
    import yaml

    from audiod import AudioPipeline

    with open(audiod_config_path, "r") as f:
        cfg = yaml.safe_load(f)
    cfg.setdefault("metrics", {})["enabled"] = False
    cfg["publish"] = {"mode": "stdout", "ws_port": 0}

    pipeline = AudioPipeline(config=cfg)
    pipeline.publisher.publish = lambda *_a, **_kw: None  # type: ignore[assignment]

    captured: list[tuple[str, dict, str]] = []
    pipeline._metrics.observe = (  # type: ignore[assignment]
        lambda kind, fields, unit="ms": captured.append((kind, fields, unit))
    )

    import numpy as np

    segment = np.zeros(16000, dtype=np.int16)  # 1 second of silence
    pipeline.transcriber.transcribe = lambda *_a, **_kw: {  # type: ignore[assignment]
        "text": "hello",
        "confidence": 0.9,
    }

    pipeline._run_transcribe(segment, start_ms=0)

    assert captured, "expected at least one metrics observe() call"
    kind, fields, unit = captured[0]
    assert kind == "segment_timing"
    assert unit == "ms"
    assert fields["count"] >= 1
    assert fields["p50_ms"] >= 0
    assert fields["p95_ms"] >= fields["p50_ms"]
    # The segment we passed is 1 second @ 16 kHz => 1000 ms.
    assert fields["max_ms"] >= 1000


def test_pipeline_observe_skipped_when_transcribe_returns_empty(monkeypatch, audiod_config_path):
    """No observe() call when the transcriber produces no text. This
    keeps the Loki stream clean of empty segments and reflects the
    intent: histograms are a property of *real* speech."""
    monkeypatch.delenv("AUDIOD_METRICS", raising=False)
    import yaml

    from audiod import AudioPipeline

    with open(audiod_config_path, "r") as f:
        cfg = yaml.safe_load(f)
    cfg.setdefault("metrics", {})["enabled"] = False
    cfg["publish"] = {"mode": "stdout", "ws_port": 0}

    pipeline = AudioPipeline(config=cfg)
    pipeline.publisher.publish = lambda *_a, **_kw: None  # type: ignore[assignment]

    captured: list = []
    pipeline._metrics.observe = (  # type: ignore[assignment]
        lambda *a, **kw: captured.append((a, kw))
    )

    import numpy as np

    segment = np.zeros(16000, dtype=np.int16)
    pipeline.transcriber.transcribe = lambda *_a, **_kw: {  # type: ignore[assignment]
        "text": "",
        "confidence": 0.0,
    }

    pipeline._run_transcribe(segment, start_ms=0)
    assert captured == []
