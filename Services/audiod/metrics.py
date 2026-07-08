"""Loki push client for audiod metrics.

Ship histograms and counters to the local Loki push endpoint as
structured log lines. The host runs Loki on :3100 with the push API
mounted at /loki/api/v1/push, auto-configured to scrape any process
log under /dev/shm/ that matches the configured filename labels.

audiod does not write its own /dev/shm log via Promtail — the
supervisor already symlinks /dev/shm/audiod.log to stdout/stderr.
We can't easily inject extra metric lines into that stream without
racing the supervisor, and we don't want to fork Promtail config
just for one histogram.

So we use the direct push endpoint: POST a JSON envelope of one
or more streams, each stream is {stream: {labels}, values:
[[ns_ts, line]]}. The lines themselves are the metric values,
formatted as a stable, scrape-friendly schema:

    audiod_metric{service="audiod", kind="segment_timing", unit="ms"}
        p50_ms=123 p95_ms=456 count=10

The query becomes:

    sum by (kind) (rate({service="audiod", kind="segment_timing"} [1m]))

This is intentionally the same shape other daemons will use, so
Loki query templates can stay daemon-agnostic.

Failure mode: any push error is swallowed and logged to stderr.
We never let a metrics hiccup break transcription.
"""
from __future__ import annotations

import json
import logging
import os
import threading
import time
import urllib.error
import urllib.request
from typing import Dict, Optional

log = logging.getLogger("audiod.metrics")

DEFAULT_LOKI_URL = "http://localhost:3100/loki/api/v1/push"
DEFAULT_PUSH_INTERVAL_S = 10.0
DEFAULT_TIMEOUT_S = 2.0
# Cap a single push payload. Loki accepts up to ~100MB; we want a
# fraction of that since we're only emitting a handful of metric
# lines per cycle.
MAX_BODY_BYTES = 64 * 1024


class LokiMetricsSink:
    """Periodic push of structured metric lines to the local Loki.

    Lifecycle:
        sink = LokiMetricsSink(service="audiod", interval_s=10.0)
        sink.start()
        # ... main loop, calls sink.observe(kind="segment_timing", fields={...})
        sink.stop()

    The sink runs a daemon thread that drains the pending payload
    every `interval_s` and POSTs it. If the push fails it logs the
    error and tries again next cycle. Pending payloads are bounded
    so a wedged Loki cannot OOM the daemon.
    """

    def __init__(
        self,
        service: str = "audiod",
        loki_url: str = DEFAULT_LOKI_URL,
        interval_s: float = DEFAULT_PUSH_INTERVAL_S,
        timeout_s: float = DEFAULT_TIMEOUT_S,
        max_buffer: int = 256,
        enabled: Optional[bool] = None,
    ) -> None:
        if interval_s <= 0:
            raise ValueError("interval_s must be > 0")
        if max_buffer <= 0:
            raise ValueError("max_buffer must be > 0")
        # env override for tests / staging: AUDIOD_METRICS=0 disables
        # the entire sink, AUDIOD_LOKI_URL overrides the push target.
        env_flag = os.environ.get("AUDIOD_METRICS", "1").lower()
        if enabled is None:
            enabled = env_flag not in ("0", "false", "no", "off")
        self._service = service
        self._loki_url = os.environ.get("AUDIOD_LOKI_URL", loki_url)
        self._interval_s = float(interval_s)
        self._timeout_s = float(timeout_s)
        self._max_buffer = int(max_buffer)
        self._enabled = bool(enabled)

        # Pending values: list of (kind, line) tuples. The HTTP body
        # is built on flush from this buffer. _buf_lock guards
        # append + drain.
        self._buf_lock = threading.Lock()
        self._pending: list = []
        self._wake = threading.Event()  # set by observe(); cleared in flush
        self._stop = threading.Event()
        self._thread: Optional[threading.Thread] = None
        # Track distinct kinds that have been observed this cycle so
        # the Loki stream labels stay stable across calls.
        self._active_kinds: set = set()
        # Last successful push (epoch seconds). 0 until first push.
        self._last_push_ts: float = 0.0
        # Total successful pushes (counter for /status).
        self._pushes_ok: int = 0
        # Total failed pushes (counter for /status).
        self._pushes_failed: int = 0
        # Total dropped observations because buffer was full.
        self._drops: int = 0

    # -- lifecycle ----------------------------------------------------

    def start(self) -> None:
        if not self._enabled:
            log.info("metrics sink disabled (AUDIOD_METRICS=0)")
            return
        if self._thread is not None:
            return
        self._stop.clear()
        self._thread = threading.Thread(
            target=self._run, name="audiod-metrics-sink", daemon=True
        )
        self._thread.start()

    def stop(self, timeout_s: float = 2.0) -> None:
        self._stop.set()
        self._wake.set()
        t = self._thread
        if t is not None:
            t.join(timeout=timeout_s)
        self._thread = None
        # Best-effort final flush so a clean shutdown still ships a
        # final observation.
        if self._enabled:
            try:
                self._flush()
            except Exception as exc:  # noqa: BLE001
                log.warning("final metrics flush failed: %s", exc)

    # -- public API ---------------------------------------------------

    def observe(self, kind: str, fields: Dict[str, object], unit: str = "ms") -> None:
        """Queue a single metric observation for the next push.

        kind:    short label for the metric (e.g. "segment_timing")
        fields:  numeric fields to record (e.g. {"p50_ms": 123,
                 "p95_ms": 456, "count": 10})
        unit:    unit suffix for the metric kind label; not appended
                 to field names.

        Format produced (one per call):
            audiod_metric{kind=<kind>} <field1>=<v1> <field2>=<v2> ...

        The line is stable enough to grep / query directly:
            {service="audiod"} |~ "audiod_metric"
        """
        if not self._enabled or not kind:
            return
        line = self._format_line(kind, fields, unit)
        with self._buf_lock:
            if len(self._pending) >= self._max_buffer:
                # Drop oldest to make room. We never want a metrics
                # blip to wedge the audio pipeline.
                self._pending.pop(0)
                self._drops += 1
            self._pending.append((kind, line))
            self._active_kinds.add(kind)
        self._wake.set()

    def snapshot(self) -> Dict[str, object]:
        """Return a JSON-serializable view of sink state for /status."""
        with self._buf_lock:
            pending = len(self._pending)
            active_kinds = sorted(self._active_kinds)
        return {
            "enabled": self._enabled,
            "loki_url": self._loki_url,
            "interval_s": self._interval_s,
            "pending": pending,
            "active_kinds": active_kinds,
            "last_push_ts": self._last_push_ts,
            "pushes_ok": self._pushes_ok,
            "pushes_failed": self._pushes_failed,
            "drops": self._drops,
        }

    # -- internals ----------------------------------------------------

    @staticmethod
    def _format_line(kind: str, fields: Dict[str, object], unit: str) -> str:
        # Sort fields for deterministic line order — easier to diff
        # across pushes, and Loki doesn't care about field order.
        head = (
            "audiod_metric{"
            f"service=\\\"audiod\\\",kind=\\\"{kind}\\\",unit=\\\"{unit}\\\""
            "}"
        )
        body = " ".join(f"{k}={_format_value(v)}" for k, v in sorted(fields.items()))
        return f"{head} {body}" if body else head

    def _run(self) -> None:
        while not self._stop.is_set():
            # Wait for either a wake (new data) or the periodic
            # interval — whichever comes first. This means a quiet
            # daemon still pushes "no data" nothing (skipped), but
            # a busy daemon flushes fast.
            got = self._wake.wait(timeout=self._interval_s)
            self._wake.clear()
            if self._stop.is_set():
                break
            if got:
                # Drain quickly so successive observations in the
                # same window collapse into one push.
                try:
                    self._flush()
                except Exception as exc:  # noqa: BLE001
                    log.warning("metrics flush raised: %s", exc)
            else:
                # Idle tick: still flush whatever is buffered. With
                # our observe() pattern this is usually empty, but
                # the periodic heartbeat makes "no pushes" itself
                # a signal in Loki.
                try:
                    self._flush()
                except Exception as exc:  # noqa: BLE001
                    log.warning("metrics heartbeat flush raised: %s", exc)

    def _flush(self) -> None:
        with self._buf_lock:
            if not self._pending:
                return
            # One stream per (service) — Loki stream labels are the
            # high-cardinality axis and we want kind to be inside
            # the line so it's queryable as a structured field
            # (e.g. |~ "kind=\"segment_timing\"").
            now_ns = int(time.time() * 1_000_000_000)
            values = [[str(now_ns), line] for _kind, line in self._pending]
            body_dict = {
                "streams": [
                    {
                        "stream": {"service": self._service, "job": "audiod"},
                        "values": values,
                    }
                ]
            }
            self._pending = []
            self._active_kinds = set()
        body = json.dumps(body_dict).encode("utf-8")
        if len(body) > MAX_BODY_BYTES:
            log.warning(
                "metrics body too large: %d bytes (max %d); dropping",
                len(body),
                MAX_BODY_BYTES,
            )
            with self._buf_lock:
                self._drops += 1
            return
        req = urllib.request.Request(
            self._loki_url,
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=self._timeout_s) as resp:
                if 200 <= resp.status < 300:
                    self._last_push_ts = time.time()
                    self._pushes_ok += 1
                else:
                    self._pushes_failed += 1
                    log.warning(
                        "loki push non-2xx: %s (body=%d bytes)",
                        resp.status,
                        len(body),
                    )
        except (urllib.error.URLError, urllib.error.HTTPError, OSError) as exc:
            self._pushes_failed += 1
            log.warning("loki push failed: %s", exc)


def _format_value(v: object) -> str:
    """Format a metric field value for the line.

    Integers and floats get stable reprs. Strings are quoted so a
    string-valued field cannot break line parsing. None becomes "".
    Booleans become 1/0 so they can flow into PromQL-style
    arithmetic.
    """
    if isinstance(v, bool):
        return "1" if v else "0"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, float):
        # Loki line format is line-protocol-ish; fixed precision
        # keeps pushes diff-friendly.
        if v.is_integer():
            return f"{v:.1f}"
        return f"{v:.4f}"
    if v is None:
        return '""'
    s = str(v)
    if any(c in s for c in " \"\n\r\t"):
        return json.dumps(s)
    return s
