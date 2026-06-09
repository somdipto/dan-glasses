"""Tests for VAD module."""

import pytest
import numpy as np
from vad import VAD, VADSpeechDetector


class TestVAD:
    def test_init(self):
        vad = VAD(threshold=0.5, sample_rate=16000)
        assert vad.threshold == 0.5
        assert vad.sample_rate == 16000

    def test_energy_fallback(self):
        vad = VAD()
        vad._model = None  # Force fallback

        silence = np.zeros(512, dtype=np.int16)
        prob = vad.get_speech_prob(silence)
        assert prob >= 0.0 and prob <= 1.0

        loud = np.ones(512, dtype=np.int16) * 10000
        prob = vad.get_speech_prob(loud)
        assert prob > 0.0

    def test_is_speech(self):
        vad = VAD(threshold=0.5)
        vad._model = None
        silence = np.zeros(512, dtype=np.int16)
        assert not vad.is_speech(silence)


class TestVADSpeechDetector:
    def test_init(self):
        detector = VADSpeechDetector(
            threshold=0.5,
            min_speech_ms=250,
            min_silence_ms=200,
            sample_rate=16000,
        )
        assert detector.vad.threshold == 0.5

    def test_force_flush_empty(self):
        detector = VADSpeechDetector()
        segment = detector.force_flush()
        assert len(segment) == 0

    def test_force_flush_with_data(self):
        detector = VADSpeechDetector()
        detector._speech_buffer = [np.ones(16000, dtype=np.int16)]
        segment = detector.force_flush()
        assert len(segment) == 16000
        assert len(detector._speech_buffer) == 0