"""Audio capture using sounddevice (PortAudio) with ring buffer."""

import threading
import numpy as np
from typing import Callable, Optional


class RingBuffer:
    """Lock-free single-producer single-consumer ring buffer for PCM frames."""

    def __init__(self, size: int):
        self.size = size
        self.buffer = np.zeros(size, dtype=np.int16)
        self._write_idx = 0  # absolute write index
        self._read_idx = 0   # absolute read index

    def write(self, data: np.ndarray):
        n = len(data)
        for i in range(n):
            self.buffer[self._write_idx % self.size] = data[i]
            self._write_idx += 1
            # Overwrite oldest if needed
            if self._write_idx - self._read_idx > self.size:
                self._read_idx += 1

    def read(self, n: int) -> np.ndarray:
        available = self.count()
        if available == 0:
            return np.array([], dtype=np.int16)
        n = min(n, available)
        result = np.empty(n, dtype=np.int16)
        for i in range(n):
            result[i] = self.buffer[self._read_idx % self.size]
            self._read_idx += 1
        return result

    def read_all(self) -> np.ndarray:
        return self.read(self.count())

    def available(self) -> int:
        return self.count()

    def count(self) -> int:
        return self._write_idx - self._read_idx


class ALSACapture:
    """Capture audio from PortAudio/ALSA device."""

    def __init__(
        self,
        device: str = "default",
        sample_rate: int = 16000,
        channels: int = 1,
        period_size: int = 512,
        buffer_periods: int = 8,
    ):
        self.device = device
        self.sample_rate = sample_rate
        self.channels = channels
        self.period_size = period_size
        self.buffer_periods = buffer_periods
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._buffer = RingBuffer(sample_rate * 60)
        self._callbacks: list[Callable[[np.ndarray], None]] = []

    def _get_device_index(self):
        """Get device index from name."""
        try:
            import sounddevice as sd
            if self.device == "default":
                return sd.query_devices(kind="input")
            devices = sd.query_devices()
            if isinstance(devices, dict):
                devices = [devices]
            for i, dev in enumerate(devices):
                if self.device in str(dev.get("name", "")):
                    return i
            return sd.query_devices(kind="input")
        except Exception:
            return None

    def _capture_loop(self):
        import sounddevice as sd

        device_idx = self._get_device_index()

        def callback(indata, frames, time, status):
            if status:
                print(f"audiod: capture status {status}", flush=True)
            pcm = indata[:, 0].astype(np.int16)
            self._buffer.write(pcm)
            for cb in self._callbacks:
                cb(pcm)

        try:
            with sd.InputStream(
                device=device_idx,
                channels=self.channels,
                samplerate=self.sample_rate,
                dtype="int16",
                blocksize=self.period_size,
                callback=callback,
            ):
                while self._running:
                    threading.Event().wait(0.05)
        except Exception as e:
            print(f"audiod: capture error {e}", flush=True)
            self._mock_capture_loop()

    def _mock_capture_loop(self):
        """Mock capture when no audio device available."""
        import time
        while self._running:
            silence = np.zeros(self.period_size, dtype=np.int16)
            self._buffer.write(silence)
            for cb in self._callbacks:
                cb(silence)
            time.sleep(self.period_size / self.sample_rate)

    def start(self):
        """Start capture in background thread."""
        self._running = True
        self._thread = threading.Thread(target=self._capture_loop, daemon=True)
        self._thread.start()

    def stop(self):
        """Stop capture."""
        self._running = False
        if self._thread:
            self._thread.join(timeout=2)

    def read(self, n_frames: int) -> np.ndarray:
        """Read n_frames from buffer."""
        return self._buffer.read(n_frames)

    def read_all(self) -> np.ndarray:
        """Read all available audio."""
        return self._buffer.read_all()

    def available(self) -> int:
        """Return number of frames available."""
        return self._buffer.available()

    def on_audio(self, callback: Callable[[np.ndarray], None]):
        """Register callback for each audio chunk."""
        self._callbacks.append(callback)