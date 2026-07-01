"""Tests for hot-reload of whisper model + drop-oldest backpressure queue."""

import threading
import time
import pytest
import numpy as np
from unittest.mock import patch, MagicMock

from transcription import WhisperTranscriber
from audiod import AudioPipeline


# ---------- Whisper hot-reload ----------


class TestWhisperHotReload:
    def test_reload_swaps_model_path(self, tmp_path):
        """reload() updates model_path on the transcriber."""
        old_model = tmp_path / "old.bin"
        new_model = tmp_path / "new.bin"
        old_model.write_bytes(b"old")
        new_model.write_bytes(b"new")

        t = WhisperTranscriber(model_path=str(old_model), language="en", threads=2)
        assert t.model_path == str(old_model)

        t.reload(model_path=str(new_model), language="en", threads=4)
        assert t.model_path == str(new_model)
        assert t.threads == 4
        assert t.language == "en"

    def test_reload_raises_on_missing_model(self, tmp_path):
        """reload() raises FileNotFoundError if new model doesn't exist."""
        old = tmp_path / "old.bin"
        old.write_bytes(b"old")
        t = WhisperTranscriber(model_path=str(old))

        with pytest.raises(FileNotFoundError):
            t.reload(model_path=str(tmp_path / "does_not_exist.bin"))

        # Original model path preserved on failure.
        assert t.model_path == str(old)

    def test_reload_optional_args_preserve_existing(self, tmp_path):
        """reload() with no args is a no-op (binary re-lookup only)."""
        old = tmp_path / "m.bin"
        old.write_bytes(b"x")
        t = WhisperTranscriber(model_path=str(old), language="hi", threads=8)
        t.reload()
        assert t.model_path == str(old)
        assert t.language == "hi"
        assert t.threads == 8


# ---------- Pipeline: _cmd_reload hot-swaps whisper ----------


class TestPipelineReload:
    def _make_pipeline(self, tmp_path):
        """Build a pipeline with a mock capture (no ALSA)."""
        model = tmp_path / "ggml-base.bin"
        model.write_bytes(b"fake")
        cfg = {
            "audio": {
                "device": "default",
                "sample_rate": 16000,
                "channels": 1,
                "period_size": 512,
                "buffer_periods": 8,
            },
            "vad": {
                "threshold": 0.5,
                "min_speech_ms": 250,
                "min_silence_ms": 200,
            },
            "whisper": {
                "model": str(model),
                "language": "auto",
                "threads": 2,
            },
            "publish": {"mode": "stdout", "socket_path": "/tmp/x.sock", "ws_port": 8091},
            "push_to_talk": {"enabled": False, "hotkey": "space"},
        }
        config_path = tmp_path / "config.yaml"
        import yaml
        config_path.write_text(yaml.safe_dump(cfg))
        # Patch ALSA so we don't need a real device.
        with patch("audiod.ALSACapture") as mock_cap:
            mock_cap.return_value = MagicMock()
            p = AudioPipeline(cfg, config_path=str(config_path))
        return p, config_path, cfg, model

    def test_reload_updates_whisper_model(self, tmp_path):
        """POST /reload re-binds the whisper transcriber to the new model path."""
        p, config_path, cfg, old_model = self._make_pipeline(tmp_path)
        new_model = tmp_path / "ggml-large.bin"
        new_model.write_bytes(b"large")

        # Simulate operator editing config.yaml: point whisper.model at the new file.
        import yaml
        cfg2 = yaml.safe_load(config_path.read_text())
        cfg2["whisper"]["model"] = str(new_model)
        cfg2["whisper"]["language"] = "en"
        config_path.write_text(yaml.safe_dump(cfg2))

        with patch("audiod.load_config", return_value=cfg2):
            result = p._cmd_reload()

        assert result["ok"] is True
        assert result["reloaded"] is True
        assert p.transcriber.model_path == str(new_model)
        assert p.transcriber.language == "en"

    def test_reload_keeps_old_model_on_failure(self, tmp_path):
        """If new model is missing, the running transcriber is unchanged."""
        p, config_path, cfg, old_model = self._make_pipeline(tmp_path)
        original_model = p.transcriber.model_path

        # Point config at a path that doesn't exist
        import yaml
        cfg2 = yaml.safe_load(config_path.read_text())
        cfg2["whisper"]["model"] = str(tmp_path / "ghost.bin")
        config_path.write_text(yaml.safe_dump(cfg2))

        with patch("audiod.load_config", return_value=cfg2):
            # Should NOT raise — reload returns ok=False, transcriber untouched
            result = p._cmd_reload()

        assert result["ok"] is False
        assert p.transcriber.model_path == original_model

    def test_reload_reports_pending_restart_fields(self, tmp_path):
        """Reload surfaces which fields need /restart (device, sample_rate, etc.)."""
        p, config_path, cfg, _ = self._make_pipeline(tmp_path)
        # First reload: no diff, so pending list should be empty.
        result = p._cmd_reload()
        assert "pending_restart_for" in result
        assert result["pending_restart_for"] == []

        # Now mutate the config on disk: change audio.device, then reload.
        import yaml
        with open(config_path) as f:
            cfg2 = yaml.safe_load(f)
        cfg2["audio"]["device"] = "hw:1,0"
        with open(config_path, "w") as f:
            yaml.safe_dump(cfg2, f)

        result = p._cmd_reload()
        assert "audio.device" in result["pending_restart_for"]


# ---------- Drop-oldest backpressure ----------


class TestDropOldestBackpressure:
    def test_queue_overflow_drops_oldest(self):
        """When the queue is full, enqueue drops the OLDEST item, not the new one."""
        p = AudioPipeline.__new__(AudioPipeline)
        p._lock = threading.Lock()
        p._dropped_segments = 0

        import queue as _q
        p._segment_queue = _q.Queue(maxsize=2)

        # Simulate three enqueues with a transcriber blocked on the first.
        seg = np.zeros(1000, dtype=np.int16)
        p._enqueue_segment(seg, 0)   # slot 1
        p._enqueue_segment(seg, 1)   # slot 2
        p._enqueue_segment(seg, 2)   # should evict slot 1, keep [1, 2]

        assert p._segment_queue.qsize() == 2
        # Drain in order: should be 1 then 2, not 0 then 1.
        a = p._segment_queue.get_nowait()[1]
        b = p._segment_queue.get_nowait()[1]
        assert a == 1
        assert b == 2

    def test_dropped_segments_counter_increments(self):
        """Each dropped-oldest increment shows up in stats."""
        p = AudioPipeline.__new__(AudioPipeline)
        p._lock = threading.Lock()
        p._dropped_segments = 0

        import queue as _q
        p._segment_queue = _q.Queue(maxsize=2)

        seg = np.zeros(1000, dtype=np.int16)
        for i in range(5):
            p._enqueue_segment(seg, i)

        # 5 enqueues, queue holds 2 → 3 drops
        assert p._dropped_segments == 3
        assert p._segment_queue.qsize() == 2

    def test_segment_queue_size_in_stats(self, tmp_path):
        """stats() exposes current queue size for monitoring."""
        p, _, _, _ = TestPipelineReload()._make_pipeline(tmp_path)
        p._started_at_ms = int(time.time() * 1000) - 1000
        s = p.stats()
        assert "queue_size" in s
        assert s["queue_size"] == 0

        # Fill queue: 1 item → size 1.
        segment = np.zeros(3200, dtype=np.int16)
        p._enqueue_segment(segment, 0)
        s = p.stats()
        assert s["queue_size"] == 1

        # Clean up: drain the queue so the worker (if running) doesn't
        # pick it up and run a real whisper call.
        while not p._segment_queue.empty():
            try:
                p._segment_queue.get_nowait()
            except Exception:
                break
