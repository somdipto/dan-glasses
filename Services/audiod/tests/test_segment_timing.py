"""Tests for the SegmentTimingHistogram and its /status integration."""

import json
import threading
import time
from http.client import HTTPConnection

import pytest

import audiod as audiod_mod
from audiod import AudioPipeline, HealthHandler, start_health_server
from segment_timing import SegmentTimingHistogram, BUCKET_BOUNDS_MS


# ---------- histogram unit tests ---------- #

def test_empty_snapshot_is_zero():
    h = SegmentTimingHistogram(capacity=8)
    snap = h.snapshot()
    assert snap["count"] == 0
    assert snap["max_ms"] == 0
    assert snap["p50_ms"] == 0
    assert snap["p95_ms"] == 0
    for b in snap["buckets"]:
        assert b["count"] == 0


def test_record_increments_count_and_buckets():
    h = SegmentTimingHistogram(capacity=32)
    h.record(120)   # bucket 0 (≤250)
    h.record(800)   # bucket 2 (≤1000)
    h.record(3000)  # bucket 4 (≤5000)
    h.record(9000)  # bucket 5 (>5000)
    snap = h.snapshot()
    assert snap["count"] == 4
    assert snap["max_ms"] == 9000
    by_label = {b["label"]: b["count"] for b in snap["buckets"]}
    assert by_label["≤250ms"] == 1
    assert by_label["≤500ms"] == 0
    assert by_label["≤1000ms"] == 1
    assert by_label["≤2000ms"] == 0
    assert by_label["≤5000ms"] == 1
    assert by_label[">5000ms"] == 1


def test_capacity_bounds_retained_samples():
    cap = 4
    h = SegmentTimingHistogram(capacity=cap)
    for v in [100, 200, 300, 400, 5000, 6000, 7000]:
        h.record(v)
    snap = h.snapshot()
    # Only the last `cap` values are retained: [400, 5000, 6000, 7000]
    assert snap["count"] == cap
    assert snap["max_ms"] == 7000
    by_label = {b["label"]: b["count"] for b in snap["buckets"]}
    # 400 → ≤500ms, 5000 → ≤5000ms, 6000 → >5000ms, 7000 → >5000ms
    assert by_label["≤500ms"] == 1
    assert by_label["≤5000ms"] == 1
    assert by_label[">5000ms"] == 2
    assert by_label["≤250ms"] == 0


def test_percentiles_nearest_rank():
    h = SegmentTimingHistogram(capacity=100)
    samples = [100, 200, 300, 400, 500, 600, 700, 800, 900, 900, 1000]
    for v in samples:
        h.record(v)
    snap = h.snapshot()
    # 11 samples; ceil(0.5 * 11) - 1 = 5 → 600
    assert snap["p50_ms"] == 600
    # ceil(0.95 * 11) - 1 = 10 → 1000
    assert snap["p95_ms"] == 1000


def test_reset_zeroes_everything():
    h = SegmentTimingHistogram(capacity=8)
    for v in [100, 200, 300]:
        h.record(v)
    h.reset()
    snap = h.snapshot()
    assert snap["count"] == 0
    assert snap["max_ms"] == 0
    for b in snap["buckets"]:
        assert b["count"] == 0


def test_record_clamps_negative_to_zero():
    h = SegmentTimingHistogram(capacity=4)
    h.record(-50)
    snap = h.snapshot()
    assert snap["count"] == 1
    assert snap["max_ms"] == 0
    assert snap["buckets"][0]["count"] == 1


def test_bucket_bounds_cover_boundary_values():
    """Ensure the published bucket edges are inclusive of the upper bound."""
    h = SegmentTimingHistogram(capacity=16)
    for v in [250, 500, 1000, 2000, 5000]:
        h.record(v)
    by_label = {b["label"]: b["count"] for b in h.snapshot()["buckets"]}
    # Boundary values fall into the matching "≤X" bucket, not the next one.
    assert by_label["≤250ms"] == 1
    assert by_label["≤500ms"] == 1
    assert by_label["≤1000ms"] == 1
    assert by_label["≤2000ms"] == 1
    assert by_label["≤5000ms"] == 1
    assert by_label[">5000ms"] == 0


def test_thread_safe_record_and_snapshot():
    """Bounded ring: capacity is respected (FIFO eviction) and snapshot
    is consistent across concurrent recorders.
    """
    cap = 2048
    h = SegmentTimingHistogram(capacity=cap)
    n_threads = 4
    n_per_thread = 500

    def worker(start: int):
        for v in range(start, start + n_per_thread):
            h.record(v)

    threads = [threading.Thread(target=worker, args=(i * 10000,)) for i in range(n_threads)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    snap = h.snapshot()
    # capacity fits every sample, so all are retained
    assert snap["count"] == n_threads * n_per_thread
    # max is the last value in the last thread (3 * 10000 + 499)
    assert snap["max_ms"] == 3 * 10000 + (n_per_thread - 1)
    # min is the first value of the first thread
    assert snap["min_ms"] == 0


# ---------- /status integration ---------- #

def _load_minimal_config():
    return {
        "audio": {
            "device": "default",
            "sample_rate": 16000,
            "channels": 1,
            "period_size": 512,
            "buffer_periods": 8,
        },
        "vad": {"threshold": 0.5, "min_speech_ms": 250, "min_silence_ms": 200},
        "whisper": {"model": "/tmp/fake-ggml-base.bin", "language": "auto", "threads": 2},
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


def test_status_includes_segment_timing_block_by_default():
    cfg = _load_minimal_config()
    pipeline = AudioPipeline(cfg)
    HealthHandler.pipeline = pipeline

    server = start_health_server(18101)
    try:
        time.sleep(0.1)
        body = _get_status(18101)
        assert "segment_timing" in body
        st = body["segment_timing"]
        assert st["count"] == 0
        assert st["max_ms"] == 0
        assert st["p50_ms"] == 0
        assert st["p95_ms"] == 0
        # Bucket schema: each bucket has label + count.
        labels = [b["label"] for b in st["buckets"]]
        assert labels == [b[0] for b in BUCKET_BOUNDS_MS]
    finally:
        server.shutdown()


def test_status_segment_timing_reflects_recorded_segments():
    cfg = _load_minimal_config()
    pipeline = AudioPipeline(cfg)
    HealthHandler.pipeline = pipeline

    for v in [120, 450, 1200, 3400, 7200]:
        pipeline._timing.record(v)

    server = start_health_server(18102)
    try:
        time.sleep(0.1)
        st = _get_status(18102)["segment_timing"]
        assert st["count"] == 5
        assert st["max_ms"] == 7200
        by_label = {b["label"]: b["count"] for b in st["buckets"]}
        assert by_label["≤250ms"] == 1
        assert by_label["≤500ms"] == 1
        assert by_label["≤1000ms"] == 0
        assert by_label["≤2000ms"] == 1
        assert by_label["≤5000ms"] == 1
        assert by_label[">5000ms"] == 1
    finally:
        server.shutdown()


def test_reset_counters_clears_segment_timing():
    cfg = _load_minimal_config()
    pipeline = AudioPipeline(cfg)
    HealthHandler.pipeline = pipeline

    for v in [100, 200, 300, 400]:
        pipeline._timing.record(v)
    assert pipeline._timing.snapshot()["count"] == 4

    # _reset_counters is what /start calls; it should drop histogram state.
    pipeline._reset_counters()
    assert pipeline._timing.snapshot()["count"] == 0

    server = start_health_server(18103)
    try:
        time.sleep(0.1)
        st = _get_status(18103)["segment_timing"]
        assert st["count"] == 0
    finally:
        server.shutdown()
