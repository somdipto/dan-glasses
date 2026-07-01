"""Bounded per-segment duration histogram for audiod /status.

Tracks the durations (ms) of the last N successfully-transcribed
segments. Exposes count, max, p50, p95, and a small fixed bucket
distribution so the UI can render a quick "are segments normal?"
signal without holding the full sample history.

Thread-safety: all mutations and reads go through a single lock. The
histogram is small (a short deque + a tiny int array) so contention is
a non-issue at audiod's scale (handful of segments per minute).
"""
from __future__ import annotations

import math
import threading
from collections import deque
from typing import Deque, Dict, List, Tuple

# Each entry is (label, upper_bound_ms). The final entry is the
# open-ended overflow bucket — its bound is math.inf and its label is
# ">5000ms". All other buckets are inclusive at the upper bound so a
# sample of exactly N lands in "≤Nms" (the
# test_bucket_bounds_cover_boundary_values contract).
BUCKET_BOUNDS_MS: List[Tuple[str, float]] = [
    ("≤250ms", 250),
    ("≤500ms", 500),
    ("≤1000ms", 1000),
    ("≤2000ms", 2000),
    ("≤5000ms", 5000),
    (">5000ms", math.inf),
]


class SegmentTimingHistogram:
    """Fixed-capacity ring of recent segment durations (ms)."""

    def __init__(self, capacity: int = 200) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self._capacity = capacity
        self._samples: Deque[int] = deque(maxlen=capacity)
        self._lock = threading.Lock()

    def record(self, duration_ms: int) -> None:
        """Record a single segment duration. Clamped to >= 0."""
        if duration_ms < 0:
            duration_ms = 0
        with self._lock:
            self._samples.append(int(duration_ms))

    def reset(self) -> None:
        with self._lock:
            self._samples.clear()

    def snapshot(self) -> Dict[str, object]:
        """Return a JSON-serializable snapshot for /status."""
        with self._lock:
            n = len(self._samples)
            if n == 0:
                return self._empty_snapshot()
            samples = sorted(self._samples)
            bucket_counts = [0] * len(BUCKET_BOUNDS_MS)
            for v in samples:
                for i, (_, bound) in enumerate(BUCKET_BOUNDS_MS):
                    if v <= bound:
                        bucket_counts[i] += 1
                        break
            return {
                "count": n,
                "capacity": self._capacity,
                "min_ms": samples[0],
                "max_ms": samples[-1],
                "p50_ms": _percentile(samples, 0.50),
                "p95_ms": _percentile(samples, 0.95),
                "buckets": [
                    {"label": label, "count": bucket_counts[i]}
                    for i, (label, _) in enumerate(BUCKET_BOUNDS_MS)
                ],
            }

    @staticmethod
    def _empty_snapshot() -> Dict[str, object]:
        return {
            "count": 0,
            "capacity": 0,
            "min_ms": 0,
            "max_ms": 0,
            "p50_ms": 0,
            "p95_ms": 0,
            "buckets": [
                {"label": label, "count": 0}
                for label, _ in BUCKET_BOUNDS_MS
            ],
        }


def _percentile(sorted_samples: List[int], q: float) -> int:
    """Nearest-rank percentile. sorted_samples is non-empty."""
    if not sorted_samples:
        return 0
    if q <= 0:
        return int(sorted_samples[0])
    if q >= 1:
        return int(sorted_samples[-1])
    n = len(sorted_samples)
    idx = max(0, min(n - 1, int(math.ceil(q * n)) - 1))
    return int(sorted_samples[idx])
