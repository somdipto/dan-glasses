"""Schema conformance tests for audiod transcript events.

The transcript event shape is a public contract spanning three
processes:
  - audiod (Python publisher, publish.py:TranscriptPublisher)
  - Tauri Rust commands (apps/dan-glasses-app/src-tauri/src/audiod.rs
    calls /status, NOT transcript events — but downstream consumers
    of the same shape will)
  - LiveTranscript.tsx (WebSocket consumer, expects TranscriptEvent)

If the schema drifts, the Tauri app, downstream services, and any
external consumer all break. Pin it.

These tests run against the stdlib publisher directly — no
whisper.cpp, no microphone, no WS roundtrip. Cheap, deterministic.
"""

import json
import time
import uuid

import pytest

from publish import TranscriptPublisher, publish_transcript


REQUIRED_KEYS = {
    "type",
    "session_id",
    "event_id",
    "seq",
    "text",
    "start_ms",
    "end_ms",
    "confidence",
    "ts_ms",
}


def _base_event():
    """A fully-formed caller-side event — type is supplied by callers,
    not auto-set by _enrich()."""
    return {"type": "transcript", "text": "hello", "start_ms": 0, "end_ms": 100, "confidence": 0.9}


def test_required_keys_present():
    p = TranscriptPublisher(mode="stdout")
    try:
        enriched = p._enrich(_base_event())
        missing = REQUIRED_KEYS - set(enriched.keys())
        assert not missing, f"missing keys: {missing}"
    finally:
        p.close()


def test_type_is_preserved():
    p = TranscriptPublisher(mode="stdout")
    try:
        enriched = p._enrich(_base_event())
        assert enriched["type"] == "transcript"
    finally:
        p.close()


def test_session_id_is_uuid():
    p = TranscriptPublisher(mode="stdout")
    try:
        enriched = p._enrich(_base_event())
        parsed = uuid.UUID(enriched["session_id"])
        assert str(parsed) == enriched["session_id"]
    finally:
        p.close()


def test_event_id_is_unique_per_event():
    p = TranscriptPublisher(mode="stdout")
    try:
        ids = set()
        for _ in range(20):
            e = p._enrich(_base_event())
            assert e["event_id"] not in ids
            uuid.UUID(e["event_id"])
            ids.add(e["event_id"])
    finally:
        p.close()


def test_seq_is_monotonic():
    p = TranscriptPublisher(mode="stdout")
    try:
        seqs = []
        for i in range(10):
            e = p._enrich({**_base_event(), "text": str(i), "start_ms": i * 100, "end_ms": (i + 1) * 100})
            seqs.append(e["seq"])
        assert seqs == sorted(seqs)
        assert len(set(seqs)) == len(seqs)
    finally:
        p.close()


def test_confidence_is_float_in_unit_interval():
    p = TranscriptPublisher(mode="stdout")
    try:
        for c in [0.0, 0.5, 0.9, 1.0]:
            e = p._enrich({**_base_event(), "confidence": c})
            assert isinstance(e["confidence"], float), f"confidence type {type(e['confidence'])}"
            assert 0.0 <= e["confidence"] <= 1.0, f"confidence out of range: {c}"
    finally:
        p.close()


def test_start_ms_less_than_end_ms():
    p = TranscriptPublisher(mode="stdout")
    try:
        e = p._enrich({**_base_event(), "start_ms": 100, "end_ms": 200})
        assert e["start_ms"] < e["end_ms"]

        # 0-length segments are valid (brief utterance / silence burst)
        e = p._enrich({**_base_event(), "start_ms": 100, "end_ms": 100})
        assert e["start_ms"] == e["end_ms"]
    finally:
        p.close()


def test_ts_ms_is_unix_epoch_ms():
    p = TranscriptPublisher(mode="stdout")
    try:
        before_ms = int(time.time() * 1000)
        e = p._enrich(_base_event())
        after_ms = int(time.time() * 1000)
        assert before_ms - 1 <= e["ts_ms"] <= after_ms + 1
    finally:
        p.close()


def test_text_is_string():
    p = TranscriptPublisher(mode="stdout")
    try:
        for t in ["", "hello", "hello world", "नमस्ते"]:
            e = p._enrich({**_base_event(), "text": t})
            assert isinstance(e["text"], str)
            assert e["text"] == t
    finally:
        p.close()


def test_publish_transcript_helper_shape(capsys):
    """publish_transcript() stdout helper must emit a single JSON line
    with the full schema. Tauri CLI debug runs may tail stdout."""
    publish_transcript("hi there", 100, 200, 0.85)
    captured = capsys.readouterr()
    lines = [ln for ln in captured.out.splitlines() if ln.startswith("{")]
    assert len(lines) == 1
    parsed = json.loads(lines[0])
    missing = REQUIRED_KEYS - set(parsed.keys())
    assert not missing, f"missing keys: {missing}"
    assert parsed["type"] == "transcript"
    assert parsed["text"] == "hi there"
    assert parsed["start_ms"] == 100
    assert parsed["end_ms"] == 200
    assert parsed["confidence"] == 0.85


def test_enrich_idempotent_on_metadata():
    """If the caller pre-sets session_id/event_id/seq, the publisher
    must respect it (don't overwrite with a fresh uuid)."""
    p = TranscriptPublisher(mode="stdout")
    try:
        sid = "test-session-123"
        eid = "test-event-456"
        seq = 99
        e = p._enrich({
            "type": "transcript",
            "session_id": sid,
            "event_id": eid,
            "seq": seq,
            "text": "x",
            "start_ms": 0,
            "end_ms": 1,
            "confidence": 0.5,
        })
        assert e["session_id"] == sid
        assert e["event_id"] == eid
        assert e["seq"] == seq
    finally:
        p.close()
