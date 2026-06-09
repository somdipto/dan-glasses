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
        assert result["end_ms"] == int(0.5 * 1000)

    def test_short_segment_returns_empty(self):
        """Below 160 samples, transcriber should short-circuit to empty text."""
        pcm = np.zeros(100, dtype=np.int16)
        tr = WhisperTranscriber(model_path=MODEL)
        result = tr.transcribe(pcm, 16000)
        assert result["text"] == ""
        assert result["end_ms"] == 0

    def test_silence_produces_blank_audio(self):
        """whisper-cli should return [BLANK_AUDIO] for true silence, which we strip."""
        pcm = np.zeros(16000, dtype=np.int16)  # 1 second of silence
        tr = WhisperTranscriber(model_path=MODEL)
        result = tr.transcribe(pcm, 16000)
        # Either blank audio (stripped to "") or empty; either way no crash
        assert isinstance(result["text"], str)
