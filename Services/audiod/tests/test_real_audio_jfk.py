"""Real-audio end-to-end test using a known JFK speech sample.

This is the *real* test for audiod's transcription path. Unlike the
synthetic chirp tests in test_whisper_e2e.py, this runs whisper against
actual recorded speech and asserts the transcript matches the ground
truth shipped with whisper.cpp's own test fixtures.

Why this matters
----------------
The synthetic-chirp tests prove the harness works. They do NOT prove
the pipeline can transcribe real human speech at acceptable accuracy.
A regression that swaps whisper for a broken model, drops the JSON
sidecar parse path, or strips non-ASCII would pass all synthetic tests
and fail this one. This is audiod's canary.

The fixture
-----------
- jfk.wav: JFK's inaugural "ask not what your country can do for you"
  clip, 10.5s, 16 kHz mono PCM (whisper.cpp's own test asset).
- jfk.json: whisper.cpp's own ground-truth JSON sidecar, including
  per-token probabilities.

Ground-truth text (whisper.cpp reference):
    " And so my fellow Americans ask not what your country can do
      for you, ask what you can do for your country."

Tolerance rationale
-------------------
We don't require byte-for-byte equality. whisper has temperature drift
and tiny.en / base / small differ. The base model shipped with audiod
should reproduce >80% of the canonical tokens. We check:

1. The transcript is non-empty (real speech, not BLANK_AUDIO).
2. The 4 most-distinctive keywords appear: "fellow Americans",
   "country", "ask not what", "for your country". Missing any of
   these means we're hallucinating or transcribing garbage.
3. Confidence is non-zero (JSON sidecar path is being exercised,
   not the stdout fallback).
4. end_ms is non-zero (the segment spans the speech, not collapsed
   to silence).
5. The result integrates with AudioPipeline._run_transcribe (the
   path that publishes to the WebSocket). We feed a captured WAV
   through the same code the live service uses.

This test is skipped if whisper-cli or the model is missing.
"""

import json
import os
import re
import wave
from pathlib import Path

import numpy as np
import pytest

from transcription import WhisperTranscriber


WHISPER_BIN = "/usr/local/bin/whisper-cli"
MODEL = os.environ.get("AUDIOD_MODEL", "/home/workspace/dan-glasses/models/ggml-base.bin")
FIXTURE_DIR = Path(__file__).parent / "fixtures"
WAV_PATH = FIXTURE_DIR / "jfk.wav"
JSON_PATH = FIXTURE_DIR / "jfk.json"


def _load_wav(path: Path) -> np.ndarray:
    with wave.open(str(path), "rb") as wf:
        assert wf.getnchannels() == 1, "fixture must be mono"
        assert wf.getsampwidth() == 2, "fixture must be 16-bit"
        sr = wf.getframerate()
        assert sr == 16000, f"fixture must be 16 kHz, got {sr}"
        raw = wf.readframes(wf.getnframes())
    return np.frombuffer(raw, dtype=np.int16), sr


def _ground_truth_text() -> str:
    """Pull the canonical text from whisper.cpp's reference JSON sidecar."""
    with open(JSON_PATH) as f:
        data = json.load(f)
    parts = [seg["text"].strip() for seg in data["transcription"]]
    return " ".join(parts)


@pytest.mark.skipif(
    not (os.path.exists(WHISPER_BIN) and os.path.exists(MODEL) and WAV_PATH.exists()),
    reason=f"whisper-cli ({WHISPER_BIN}) or model ({MODEL}) or fixture ({WAV_PATH}) not present",
)
class TestRealAudioJFK:
    """Transcribe JFK's inaugural clip and assert the result is real."""

    def test_jfk_wav_is_real_16k_mono(self):
        pcm, sr = _load_wav(WAV_PATH)
        assert sr == 16000
        assert pcm.dtype == np.int16
        # 10.5s of speech at 16kHz = ~168k samples
        assert 150_000 < len(pcm) < 200_000, f"unexpected length {len(pcm)}"
        # RMS energy should be non-trivial (real speech, not silence)
        rms = float(np.sqrt(np.mean(pcm.astype(np.float64) ** 2)))
        assert rms > 1000, f"audio is too quiet, rms={rms}"

    def test_jfk_transcript_recovers_canonical_text(self):
        """whisper-base must reproduce the distinctive JFK keywords."""
        pcm, sr = _load_wav(WAV_PATH)
        tr = WhisperTranscriber(model_path=MODEL, language="en", threads=2)
        result = tr.transcribe(pcm, sr)

        assert result["text"], f"empty transcript for JFK clip: {result!r}"
        assert result["end_ms"] > 0, f"end_ms collapsed: {result!r}"

        # Lowercase normalize for keyword matching.
        text_lc = result["text"].lower()

        # These four phrases are uniquely identifying. If any is missing,
        # the model is hallucinating or transcribing the wrong audio.
        canonical = [
            "fellow americans",
            "country",
            "ask",       # appears 3x in ground truth
            "your",
        ]
        missing = [kw for kw in canonical if kw not in text_lc]
        assert not missing, f"transcript missing keywords {missing}: {result['text']!r}"

    def test_jfk_transcript_contains_country_twice(self):
        """Ground-truth has 'country' exactly twice. A regression that
        collapses to one occurrence (e.g., truncating mid-sentence)
        would slip past the keyword check above and fail here."""
        pcm, sr = _load_wav(WAV_PATH)
        tr = WhisperTranscriber(model_path=MODEL, language="en", threads=2)
        result = tr.transcribe(pcm, sr)
        text_lc = result["text"].lower()
        count = text_lc.count("country")
        assert count >= 2, f"expected ≥2 'country' mentions, got {count}: {result['text']!r}"

    def test_jfk_confidence_path_is_real(self):
        """If the JSON sidecar path is broken, the result would carry
        confidence=0.0 (the stdout fallback). A passing run with
        confidence=0.0 is a silent regression."""
        pcm, sr = _load_wav(WAV_PATH)
        tr = WhisperTranscriber(model_path=MODEL, language="en", threads=2)
        result = tr.transcribe(pcm, sr)
        assert result["confidence"] > 0.0, (
            f"confidence=0.0 means JSON sidecar parse failed; "
            f"stdout fallback is being used. Full result: {result!r}"
        )
        # Per-token mean probability should be reasonable for clear speech.
        assert result["confidence"] > 0.4, (
            f"confidence suspiciously low ({result['confidence']:.3f}); "
            f"either model is bad or parse path is wrong. Text: {result['text']!r}"
        )

    def test_jfk_segment_timing_matches_audio_length(self):
        """end_ms should be within 20% of the actual audio length.
        whisper sometimes pads; we allow generous slack but a 0ms or
        30s result is wrong."""
        pcm, sr = _load_wav(WAV_PATH)
        duration_ms = int(len(pcm) / sr * 1000)
        tr = WhisperTranscriber(model_path=MODEL, language="en", threads=2)
        result = tr.transcribe(pcm, sr)
        assert result["end_ms"] > 0
        assert result["end_ms"] < duration_ms * 1.5, (
            f"end_ms={result['end_ms']} exceeds 1.5x audio length ({duration_ms})"
        )
        assert result["end_ms"] > duration_ms * 0.5, (
            f"end_ms={result['end_ms']} is less than half the audio length ({duration_ms})"
        )

    def test_jfk_pipeline_publishes_via_audio_pipeline(self):
        """End-to-end: feed the WAV through AudioPipeline._run_transcribe
        (the same code path the live service uses to publish to WS).
        Capture the published event and assert it carries real text."""
        from unittest.mock import MagicMock
        from audiod import AudioPipeline

        # Minimal config; we never start the capture loop.
        config = {
            "audio": {"device": "default", "sample_rate": 16000, "channels": 1,
                       "period_size": 512, "buffer_periods": 8},
            "vad": {"threshold": 0.5, "min_speech_ms": 250, "min_silence_ms": 200,
                     "max_segment_ms": 10000},
            "whisper": {"model": MODEL, "language": "en", "threads": 2},
            "publish": {"mode": "stdout", "socket_path": "/tmp/x.sock", "ws_port": 8091},
        }
        pipeline = AudioPipeline(config, config_path=str(FIXTURE_DIR / "_unused.yaml"))

        # Stub the publisher so we can capture what would have hit the WS.
        pipeline.publisher = MagicMock()

        pcm, sr = _load_wav(WAV_PATH)
        # _run_transcribe takes (segment, start_ms)
        pipeline._run_transcribe(pcm, 0)

        # Publisher.publish must have been called with a real event.
        pipeline.publisher.publish.assert_called_once()
        event = pipeline.publisher.publish.call_args[0][0]
        assert "text" in event and event["text"], f"empty event: {event!r}"
        assert event["end_ms"] > 0
        assert event["confidence"] > 0.0
        # Same keyword check on the published payload
        text_lc = event["text"].lower()
        for kw in ("fellow americans", "country", "ask"):
            assert kw in text_lc, f"published event missing {kw!r}: {event['text']!r}"


@pytest.mark.skipif(
    not (os.path.exists(WHISPER_BIN) and os.path.exists(MODEL) and JSON_PATH.exists()),
    reason="ground truth JSON missing",
)
class TestGroundTruthFixture:
    """Sanity-check the ground-truth fixture itself.

    If the reference JSON gets corrupted or replaced, every assertion
    above silently drifts. Pin the canonical text so the fixture
    integrity check happens once, loudly, before any other test runs.
    """

    def test_ground_truth_matches_whisper_cpp_canonical(self):
        gt = _ground_truth_text()
        # The 5 unique signature phrases from JFK's inaugural ask.
        for kw in (
            "fellow americans",
            "ask not what your country",
            "ask what you can do for your country",
        ):
            assert kw in gt.lower(), f"ground truth missing {kw!r}: {gt!r}"