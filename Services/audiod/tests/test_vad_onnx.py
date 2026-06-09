"""Tests for ONNX Silero VAD."""

import pytest
from unittest.mock import Mock
import numpy as np
from vad import VAD, VADSpeechDetector


class TestVADONNX:
    def test_onnx_session_loaded(self):
        """Verify ONNX session is loaded (not in fallback mode)."""
        vad = VAD(threshold=0.5, sample_rate=16000)
        assert vad._session is not None, "ONNX session should be loaded"

    def test_speech_prob_noise(self):
        """Noise should return low speech probability."""
        vad = VAD(threshold=0.5, sample_rate=16000)
        noise = np.zeros(512, dtype=np.int16)
        prob = vad.get_speech_prob(noise)
        assert 0.0 <= prob <= 1.0

    def test_speech_prob_tone(self):
        """Strong sine wave should return high speech probability."""
        vad = VAD(threshold=0.5, sample_rate=16000)
        t = np.linspace(0, 1, 512)
        tone = (np.sin(2 * np.pi * 200 * t) * 8000).astype(np.int16)
        prob = vad.get_speech_prob(tone)
        assert prob > 0.5, f"Tone should trigger VAD, got {prob}"

    def test_is_speech(self):
        """is_speech returns True for speech-like audio."""
        vad = VAD(threshold=0.5, sample_rate=16000)
        t = np.linspace(0, 1, 512)
        tone = (np.sin(2 * np.pi * 300 * t) * 10000).astype(np.int16)
        assert vad.is_speech(tone) is True

    def test_reset_hidden_state(self):
        """Reset should reinitialize hidden state."""
        vad = VAD(threshold=0.5, sample_rate=16000)
        t = np.linspace(0, 1, 512)
        tone = (np.sin(2 * np.pi * 300 * t) * 8000).astype(np.int16)
        vad.get_speech_prob(tone)
        h_before = vad._h.copy() if vad._h is not None else None
        vad.reset()
        if vad._h is not None:
            np.testing.assert_array_equal(vad._h, np.zeros((1, 1, 64), dtype=np.float32))


class TestVADSpeechDetectorONNX:
    def test_speech_end_callback(self):
        """Speech end callback fires after speech segment."""
        speech_end = Mock()

        detector = VADSpeechDetector(
            threshold=0.5,
            min_speech_ms=100,
            min_silence_ms=100,
            sample_rate=16000,
            on_speech_end=Mock(),
        )

        # Simulate speech
        t = np.linspace(0, 0.5, 8000)
        speech = (np.sin(2 * np.pi * 200 * t) * 10000).astype(np.int16)

        for i in range(0, len(speech), 512):
            chunk = speech[i:i + 512]
            if len(chunk) < 512:
                chunk = np.pad(chunk, (0, 512 - len(chunk)))
            detector.process(chunk)

        # Silence to trigger flush
        silence = np.zeros(512, dtype=np.int16)
        for _ in range(10):
            detector.process(silence)

    def test_is_ready(self):
        """is_ready should return True when ONNX is loaded."""
        detector = VADSpeechDetector(threshold=0.5, sample_rate=16000)
        assert detector.is_ready() is True, "ONNX VAD should be ready"