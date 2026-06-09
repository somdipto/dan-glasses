"""Silero VAD integration via ONNX runtime (avoids torch/torchaudio ABI issues)."""

import numpy as np
import onnxruntime as ort
import os
from typing import Callable, Optional


_ONNX_MODEL_PATH = os.path.expanduser(
    "~/.cache/torch/hub/snakers4_silero-vad_master/src/silero_vad/data/silero_vad.onnx"
)


class VAD:
    """Silero VAD via ONNX runtime for voice activity detection."""

    def __init__(
        self,
        threshold: float = 0.5,
        min_speech_ms: int = 250,
        min_silence_ms: int = 200,
        sample_rate: int = 16000,
    ):
        self.threshold = threshold
        self.min_speech_samples = int(sample_rate * min_speech_ms / 1000)
        self.min_silence_samples = int(sample_rate * min_silence_ms / 1000)
        self.sample_rate = sample_rate

        # Try ONNX runtime with cached model
        if os.path.exists(_ONNX_MODEL_PATH):
            try:
                sess_opts = ort.SessionOptions()
                sess_opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
                self._session = ort.InferenceSession(
                    _ONNX_MODEL_PATH, sess_opts, providers=["CPUExecutionProvider"]
                )
                self._input_name = self._session.get_inputs()[0].name
                self._hidden_name = self._session.get_inputs()[1].name if len(self._session.get_inputs()) > 1 else None
                self._h = np.zeros((1, 1, 64), dtype=np.float32) if self._hidden_name else None
            except Exception as e:
                print(f"audiod: ONNX VAD load failed ({e}), using energy fallback")
                self._session = None
                self._hidden_name = None
                self._h = None
        else:
            print("audiod: Silero ONNX not found, using energy fallback")
            self._session = None
            self._hidden_name = None
            self._h = None

    def get_speech_prob(self, pcm: np.ndarray) -> float:
        """Get speech probability for a PCM chunk."""
        if self._session is None:
            return self._energy_vad(pcm)

        try:
            x = pcm.astype(np.float32)
            if len(x) < 512:
                x = np.pad(x, (0, 512 - len(x)))
            elif len(x) > 512:
                x = x[:512]

            # ONNX model: [1, 512] or [1, 1, 512] depending on version
            x = x.reshape(1, -1).astype(np.float32)

            if self._hidden_name:
                out = self._session.run(
                    [self._session.get_outputs()[0].name],
                    {self._session.get_inputs()[0].name: x, self._hidden_name: self._h}
                )
                # VAD output: [prob, hidden_state]
                prob = float(out[0][0, 0]) if len(out[0].shape) > 1 else float(out[0][0])
                # Update hidden state from output[1] if present
                if len(out) > 1:
                    self._h = out[1]
            else:
                out = self._session.run(None, {self._session.get_inputs()[0].name: x})
                prob = float(out[0][0, 0]) if len(out[0].shape) > 1 else float(out[0][0])

            return min(max(prob, 0.0), 1.0)
        except Exception:
            return self._energy_vad(pcm)

    def _energy_vad(self, pcm: np.ndarray) -> float:
        """Energy-based VAD fallback."""
        if len(pcm) == 0:
            return 0.0
        rms = np.sqrt(np.mean(pcm.astype(float) ** 2))
        return min(rms / 2000.0, 1.0)

    def is_speech(self, pcm: np.ndarray) -> bool:
        """Return True if speech detected in chunk."""
        return self.get_speech_prob(pcm) > self.threshold

    def reset(self):
        """Reset internal state."""
        if self._h is not None:
            self._h = np.zeros((1, 1, 64), dtype=np.float32)


class VADSpeechDetector:
    """VAD-based speech segment detection with state machine."""

    def __init__(
        self,
        threshold: float = 0.5,
        min_speech_ms: int = 250,
        min_silence_ms: int = 200,
        sample_rate: int = 16000,
        on_speech_start: Optional[Callable[[], None]] = None,
        on_speech_end: Optional[Callable[[np.ndarray], None]] = None,
    ):
        self.vad = VAD(threshold, min_speech_ms, min_silence_ms, sample_rate)
        self.on_speech_start = on_speech_start or (lambda: None)
        self.on_speech_end = on_speech_end or (lambda _: None)
        self.sample_rate = sample_rate

        self._speech_active = False
        self._speech_buffer: list[np.ndarray] = []
        self._silence_frames = 0
        self._pre_roll_buffer: list[np.ndarray] = []
        self._pre_roll_samples = int(sample_rate * 0.2)

    def process(self, pcm_chunk: np.ndarray) -> bool:
        """Process a PCM chunk. Returns True if in speech segment."""
        is_speech = self.vad.is_speech(pcm_chunk)

        if not self._speech_active:
            self._pre_roll_buffer.append(pcm_chunk)
            total = sum(len(x) for x in self._pre_roll_buffer)
            if total > self._pre_roll_samples:
                self._pre_roll_buffer.pop(0)

        if is_speech:
            self._silence_frames = 0
            if not self._speech_active:
                full_chunk = np.concatenate([*self._pre_roll_buffer, pcm_chunk])
                self._speech_buffer.append(full_chunk)
                self._pre_roll_buffer = []
                self._speech_active = True
                self.on_speech_start()
            else:
                self._speech_buffer.append(pcm_chunk)
        else:
            if self._speech_active:
                self._silence_frames += len(pcm_chunk)
                silence_sec = self._silence_frames / self.sample_rate
                if silence_sec >= self.vad.min_silence_samples / 1000.0:
                    self._flush_segment()
                else:
                    self._speech_buffer.append(pcm_chunk)

        return self._speech_active

    def _flush_segment(self):
        """Flush accumulated speech segment."""
        if self._speech_buffer:
            segment = np.concatenate(self._speech_buffer)
            self.on_speech_end(segment)
        self._reset()

    def _reset(self):
        """Reset speech detection state."""
        self._speech_active = False
        self._speech_buffer = []
        self._silence_frames = 0
        self._pre_roll_buffer = []
        self.vad.reset()

    def is_ready(self) -> bool:
        """Return True if VAD is loaded and ready (not in fallback mode)."""
        return self.vad._session is not None

    def force_flush(self) -> np.ndarray:
        """Force flush current segment (for push-to-talk)."""
        if self._speech_buffer:
            segment = np.concatenate(self._speech_buffer)
            self._reset()
            return segment
        return np.array([], dtype=np.int16)
