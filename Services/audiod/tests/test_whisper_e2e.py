"""End-to-end test: synth PCM → write WAV → whisper-cli → assert text.

Requires /usr/local/bin/whisper-cli and the model file. Skipped if either is missing.
"""

import os
import struct
import subprocess
import tempfile
import wave

import numpy as np
import pytest

from transcription import WhisperTranscriber


WHISPER_BIN = "/usr/local/bin/whisper-cli"
MODEL = "/home/workspace/dan-glasses/models/ggml-tiny.bin"


def _synth_speech_like(duration_s: float = 1.0, sample_rate: int = 16000) -> np.ndarray:
    """Synthesize a chirp that resembles a vowel for whisper's encoder.

    We use a stack of harmonics around formant frequencies to give whisper
    something phoneme-like to chew on. Not real speech — this is a smoke test.
    """
    t = np.linspace(0, duration_s, int(sample_rate * duration_s), endpoint=False)
    # Add formants roughly in F1/F2 ranges
    f0 = 130.0
    harmonics = [f0, 2 * f0, 3 * f0, 4 * f0, 5 * f0]
    sig = np.zeros_like(t)
    for i, f in enumerate(harmonics, start=1):
        sig += (np.sin(2 * np.pi * f * t) / i)
    # Add some AM modulation so the segment is non-stationary
    sig *= 0.5 + 0.5 * np.sin(2 * np.pi * 5 * t)
    # Normalize and scale
    sig = sig / (np.max(np.abs(sig)) + 1e-9) * 0.6
    return (sig * 32767).astype(np.int16)


def _write_wav(path: str, pcm: np.ndarray, sample_rate: int = 16000) -> None:
    with wave.open(path, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(pcm.tobytes())


@pytest.mark.skipif(
    not (os.path.exists(WHISPER_BIN) and os.path.exists(MODEL)),
    reason=f"whisper-cli ({WHISPER_BIN}) or model ({MODEL}) not present",
)
class TestWhisperEndToEnd:
    def test_whisper_cli_invocation(self):
        """The transcriber should write a WAV and invoke whisper-cli without errors."""
        pcm = _synth_speech_like(duration_s=0.5)
        tr = WhisperTranscriber(model_path=MODEL, language="en", threads=2)
        assert tr._bin is not None, "whisper-cli not found"

        # Direct call
        result = tr.transcribe(pcm, 16000)
        assert "text" in result
        assert "start_ms" in result
        assert "end_ms" in result
        assert "confidence" in result
        # The 0.5s chirp is not real speech; whisper may either transcribe
        # BLANK_AUDIO (silence hallucination) or hallucinate a token. Accept
        # either outcome: empty text → end_ms==0, non-empty → end_ms==500.
        if result["text"]:
            assert result["end_ms"] == int(0.5 * 1000), (
                f"non-empty transcription should span the full segment, "
                f"got end_ms={result['end_ms']} for text={result['text']!r}"
            )
        else:
            assert result["end_ms"] == 0, (
                f"empty transcription should have end_ms==0, got {result['end_ms']}"
            )

    def test_short_segment_returns_empty(self):
        """Below 160 samples, transcriber should short-circuit to empty text."""
        pcm = np.zeros(100, dtype=np.int16)
        tr = WhisperTranscriber(model_path=MODEL)
        result = tr.transcribe(pcm, 16000)
        assert result["text"] == ""
        assert result["end_ms"] == 0

    def test_silence_produces_blank_audio(self):
        """whisper-cli returns [BLANK_AUDIO] for silence; we must strip it to ''."""
        pcm = np.zeros(16000, dtype=np.int16)  # 1 second of silence
        tr = WhisperTranscriber(model_path=MODEL)
        result = tr.transcribe(pcm, 16000)
        # whisper-tiny emits BLANK_AUDIO as multiple tokens ("BLANK", "_", "AUDIO").
        # The strip path must catch that pattern and return empty text.
        assert result["text"] == "", f"expected empty text for silence, got {result['text']!r}"

    def test_silence_pure_zeros_50ms_above_short_circuit(self):
        """Silence longer than 160 samples should also yield empty text, not crash."""
        pcm = np.zeros(4000, dtype=np.int16)  # 250ms silence
        tr = WhisperTranscriber(model_path=MODEL)
        result = tr.transcribe(pcm, 16000)
        assert result["text"] == ""
        # Empty text → zero timing. We used to return the full duration
        # for silence, but that leaked the input span into the event
        # stream and confused downstream consumers (memoryd indexes
        # empty-but-spanning events as real utterances).
        assert result["end_ms"] == 0


class TestWhisperTimeoutBudget:
    """Regression: the whisper-cli subprocess timeout must be adaptive
    and bounded, not a fixed 10s.

    Bug fixed in v0.6: under sustained CPU pressure (full test suite
    hammering whisper-tiny back-to-back), the fixed 10s timeout fired
    on the first cold-cache call. v0.6 makes the budget
    `15s + 3s/sec_of_audio`, capped at 60s.
    """

    def test_short_audio_meets_floor(self):
        from transcription import WhisperTranscriber
        tr = WhisperTranscriber(model_path=MODEL, threads=2)
        # 500ms of audio → 15 + 3*0.5 = 16.5s budget
        pcm = np.zeros(8000, dtype=np.int16)
        budget = tr._timeout_for(pcm, 16000)
        assert budget >= 15.0, f"floor breached: {budget}"
        assert budget <= 60.0, f"cap breached: {budget}"

    def test_long_audio_capped(self):
        from transcription import WhisperTranscriber
        tr = WhisperTranscriber(model_path=MODEL, threads=2)
        # 30s of audio → 15 + 3*30 = 105s raw, must cap to 60s
        pcm = np.zeros(30 * 16000, dtype=np.int16)
        budget = tr._timeout_for(pcm, 16000)
        assert budget == 60.0, f"expected 60s cap, got {budget}"

    def test_grows_with_length(self):
        from transcription import WhisperTranscriber
        tr = WhisperTranscriber(model_path=MODEL, threads=2)
        b1 = tr._timeout_for(np.zeros(16000, dtype=np.int16), 16000)   # 1s
        b5 = tr._timeout_for(np.zeros(5 * 16000, dtype=np.int16), 16000)  # 5s
        assert b5 > b1, f"expected 5s budget > 1s budget, got {b1} vs {b5}"
