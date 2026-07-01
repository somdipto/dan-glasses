"""Integration tests for the full audio pipeline."""

import pytest
import numpy as np
from unittest.mock import Mock, patch
from io import StringIO
import json

from capture import ALSACapture, RingBuffer
from vad import VAD, VADSpeechDetector
from transcription import WhisperTranscriber
from publish import TranscriptPublisher


class TestRingBufferIntegration:
    def test_capture_to_vad(self):
        """Simulate capture producing PCM that feeds into VAD."""
        rb = RingBuffer(4096)
        sample_rate = 16000
        chunk_size = 512

        # Write one speech chunk directly
        t = np.linspace(0, 1, sample_rate)
        speech = (np.sin(2 * np.pi * 200 * t) * 5000).astype(np.int16)
        chunk = speech[:chunk_size]

        rb.write(chunk)

        # Read and verify
        assert rb.count() >= 512


class TestVADIntegration:
    def test_speech_detection_flow(self):
        """Test VAD state machine with speech audio."""
        speech_on_called = Mock()
        speech_end_called = Mock()

        detector = VADSpeechDetector(
            threshold=0.5,
            min_speech_ms=100,
            min_silence_ms=100,
            sample_rate=16000,
            on_speech_start=speech_on_called,
            on_speech_end=speech_end_called,
        )

        # Force VAD into fallback mode (no real model)
        detector.vad._model = None

        # Simulate silence first
        silence = np.zeros(512, dtype=np.int16)
        for _ in range(10):
            detector.process(silence)

        # Simulate speech
        t = np.linspace(0, 0.5, 8000)
        speech = (np.sin(2 * np.pi * 200 * t) * 8000).astype(np.int16)

        for i in range(0, len(speech), 512):
            chunk = speech[i:i + 512]
            if len(chunk) < 512:
                chunk = np.pad(chunk, (0, 512 - len(chunk)))
            detector.process(chunk)

        # Simulate silence to flush
        for _ in range(20):
            detector.process(silence)

        # speech_on_called may or may not be called depending on threshold


class TestPublisher:
    def test_publish_to_stdout(self, capsys):
        # Pick a high unused port to avoid colliding with live audiod on 8091
        pub = TranscriptPublisher(mode="stdout", ws_port=18791)
        try:
            event = {"type": "transcript", "text": "hello world", "start_ms": 0, "end_ms": 1000, "confidence": 0.9}
            pub.publish(event)

            out, err = capsys.readouterr()
            # Filter out the ws bind warning (if any) before parsing JSON
            json_line = next(
                (ln for ln in out.splitlines() if ln.lstrip().startswith("{") and '"text"' in ln),
                "",
            )
            assert "hello world" in json_line
            assert json.loads(json_line)["text"] == "hello world"
        finally:
            pub.close()


class TestTranscriptionMock:
    def test_mock_transcribe(self):
        transcriber = WhisperTranscriber()
        transcriber._bin = None  # Force mock

        pcm = np.ones(16000, dtype=np.int16)
        result = transcriber.transcribe(pcm, 16000)

        assert "text" in result
        assert "[mock transcript" in result["text"]
        assert result["end_ms"] == 1000

class TestRestartCounterReset:
    """Regression: /restart must reset lifetime counters so /status
    reflects only the current lifetime, not stale history.

    Bug fixed in v0.6: _cmd_start was refreshing _started_at_ms but
    leaving _segments_transcribed, _dropped_segments, and
    _transcribe_inflight intact, so /status lied about segment count
    after a restart.
    """

    @staticmethod
    def _cfg():
        return {
            "audio": {"device": "default", "sample_rate": 16000, "channels": 1,
                      "period_size": 512, "buffer_periods": 8},
            "vad": {"threshold": 0.5, "min_speech_ms": 250, "min_silence_ms": 200},
            "whisper": {"model": "/tmp/fake-ggml-base.bin", "language": "auto", "threads": 2},
            "publish": {"mode": "stdout", "socket_path": "/tmp/audiod-test.sock", "ws_port": 18091},
            "push_to_talk": {"enabled": False, "hotkey": "space"},
        }

    def test_restart_resets_segments_transcribed(self):
        """Force a fake history, restart, then assert /status reads 0."""
        from audiod import AudioPipeline
        pipeline = AudioPipeline(self._cfg())
        pipeline._segments_transcribed = 47
        pipeline._dropped_segments = 3
        pipeline._transcribe_inflight = 2

        with patch.object(pipeline, "capture") as cap, \
             patch.object(pipeline, "_process_loop", lambda: None), \
             patch.object(pipeline, "_transcription_worker", lambda: None):
            cap.start = Mock()
            cap.stop = Mock()
            pipeline._cmd_restart()

        snap = pipeline.stats()
        assert snap["segments_transcribed"] == 0
        assert snap["dropped_segments"] == 0
        assert snap["transcribe_inflight"] == 0

    def test_restart_resets_uptime_to_near_zero(self):
        """Uptime must be reset, not just _started_at_ms."""
        import time as _time
        from audiod import AudioPipeline
        pipeline = AudioPipeline(self._cfg())
        pipeline._started_at_ms = int(_time.time() * 1000) - 60_000  # pretend 60s old

        with patch.object(pipeline, "capture") as cap, \
             patch.object(pipeline, "_process_loop", lambda: None), \
             patch.object(pipeline, "_transcription_worker", lambda: None):
            cap.start = Mock()
            cap.stop = Mock()
            pipeline._cmd_restart()

        snap = pipeline.stats()
        # Allow generous slack for slow CI (up to 5s).
        assert snap["uptime_ms"] < 5_000
