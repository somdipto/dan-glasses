"""V4L2 camera capture with fallback to periodic mock capture.

Note: v4l2py is unmaintained — migrated to linuxpy.video.
API: Device(path).open() → VideoCapture(device) → set_format → start → dequeue/enqueue
"""

import threading
import time
import os
import io
import numpy as np
from typing import Optional, Callable

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

JPEG_QUALITY = 70
LATEST_FRAME_JPEG_MAX = 5 * 1024 * 1024  # 5MB cap for latest frame JPEG

V4L2_AVAILABLE = False
try:
    from linuxpy.video.device import Device, VideoCapture, PixelFormat
    from linuxpy.video.device import ImageFormat
    V4L2_AVAILABLE = os.path.exists("/dev/video0")
except ImportError:
    pass


class V4L2Capture:
    """Capture frames from V4L2 camera."""

    def __init__(
        self,
        device: str = "/dev/video0",
        width: int = 640,
        height: int = 480,
        fps: int = 5,
    ):
        self.device_path = device
        self.width = width
        self.height = height
        self.fps = fps
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._callbacks: list[Callable[[np.ndarray], None]] = []
        self._capture: Optional[VideoCapture] = None
        self._frame_count = 0

        # Latest-frame JPEG buffer (single-slot, thread-safe).
        # Consumers: GET /stream (multipart), GET /frame.jpg
        self._latest_lock = threading.Lock()
        self._latest_jpeg: Optional[bytes] = None
        self._latest_jpeg_ts: float = 0.0
        self._latest_w: int = 0
        self._latest_h: int = 0

    def _update_latest(self, frame: np.ndarray) -> None:
        """Encode frame as JPEG and store it as the latest frame snapshot."""
        if not PIL_AVAILABLE or frame is None:
            return
        try:
            if frame.dtype != np.uint8:
                frame = frame.astype(np.uint8)
            if frame.ndim == 2:
                frame = np.stack([frame, frame, frame], axis=-1)
            elif frame.ndim == 3 and frame.shape[2] == 4:
                frame = frame[:, :, :3]
            img = Image.fromarray(frame)
            buf = io.BytesIO()
            img.save(buf, format="JPEG", quality=JPEG_QUALITY)
            data = buf.getvalue()
            if len(data) > LATEST_FRAME_JPEG_MAX:
                return  # safety: don't blow up memory on huge frames
            with self._latest_lock:
                self._latest_jpeg = data
                self._latest_jpeg_ts = time.time()
                self._latest_w = frame.shape[1]
                self._latest_h = frame.shape[0]
        except Exception:
            return

    def get_latest_jpeg(self) -> tuple[Optional[bytes], float, int, int]:
        """Return (jpeg_bytes, timestamp, width, height) — thread-safe."""
        with self._latest_lock:
            return (
                self._latest_jpeg,
                self._latest_jpeg_ts,
                self._latest_w,
                self._latest_h,
            )

    def _open_camera(self):
        """Open V4L2 device and configure capture."""
        if not V4L2_AVAILABLE:
            return None
        try:
            dev = Device(self.device_path)
            dev.open()
            vc = VideoCapture(dev, size=4)
            # Try MJPG first (most reliable on USB cams), fall back to YUYV
            try:
                vc.set_format(self.width, self.height, PixelFormat.MJPEG)
            except Exception:
                try:
                    vc.set_format(self.width, self.height, PixelFormat.YUYV)
                except Exception:
                    pass
            vc.set_fps(self.fps)
            vc.start()
            return vc
        except Exception as e:
            print(f"perceptiond: V4L2 open failed: {e}", flush=True)
            return None

    def _capture_loop(self):
        """Main capture loop reading frames from camera."""
        vc = self._open_camera()

        if vc is None:
            print("perceptiond: no camera, using mock capture", flush=True)
            self._mock_capture_loop()
            return

        print(f"perceptiond: camera opened {self.device_path}", flush=True)
        self._capture = vc
        dev = vc.device

        while self._running:
            try:
                buf = vc.dequeue_buffer()
                if buf is None:
                    time.sleep(0.01)
                    continue

                frame = self._convert_buffer(buf, vc)
                if frame is not None:
                    self._frame_count += 1
                    self._update_latest(frame)
                    for cb in self._callbacks:
                        cb(frame)

                vc.enqueue_buffer(buf)

            except Exception as e:
                print(f"perceptiond: capture error: {e}", flush=True)
                time.sleep(0.5)
                continue

            time.sleep(1.0 / self.fps)

        vc.stop()
        vc.disarm()
        dev.close()

    def _convert_buffer(self, buf, vc) -> Optional[np.ndarray]:
        """Convert V4L2 buffer to RGB numpy array."""
        try:
            import cv2
            data = buf.planes[0].to_bytes()
            if buf.format == PixelFormat.MJPEG:
                # Decode MJPEG to BGR
                bgr = cv2.imdecode(np.frombuffer(data, dtype=np.uint8), cv2.IMREAD_COLOR)
                if bgr is None:
                    return None
                rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
                return rgb
            elif buf.format == PixelFormat.YUYV:
                # YUYV → RGB
                yuyv = np.frombuffer(data, dtype=np.uint8).reshape(self.height, self.width, 2)
                rgb = cv2.cvtColor(yuyv, cv2.COLOR_YUV2RGB_YUYV)
                return rgb
            return None
        except ImportError:
            # Fallback without cv2 — return grayscale from raw bytes
            try:
                data = buf.planes[0].to_bytes()
                gray = np.frombuffer(data, dtype=np.uint8).reshape(self.height, self.width)
                return np.stack([gray, gray, gray], axis=-1)
            except Exception:
                return None
        except Exception as e:
            print(f"perceptiond: buffer convert error: {e}", flush=True)
            return None

    def _mock_capture_loop(self):
        """Generate synthetic frames with deliberate motion when no camera available."""
        import random
        t_offset = 0.0
        while self._running:
            t = time.time() + t_offset
            frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)

            # Deliberate motion: large stable blob well away from edges
            cx = int((np.sin(t * 0.3) + 1) * 0.5 * (self.width - 160)) + 80  # [80, width-80]
            cy = int((np.cos(t * 0.2) + 1) * 0.5 * (self.height - 160)) + 80  # [80, height-80]
            radius = 90  # area ≈ 25447px / 307200 ≈ 8.3% (above 0.15 threshold)

            y, x = np.ogrid[:self.height, :self.width]
            mask = (x - cx) ** 2 + (y - cy) ** 2 <= radius ** 2

            # Drifting blue-white blob on dark background — high contrast for motion detection
            frame[mask] = [200, 80, 30]  # RGB: reddish blob (high delta from dark background)
            frame[~mask] = [10, 12, 15]   # near-black background

            # Add noise for texture
            noise = np.random.randint(0, 20, (self.height, self.width, 3), dtype=np.uint8)
            frame = np.clip(frame.astype(np.int16) + noise, 0, 255).astype(np.uint8)

            self._frame_count += 1
            self._update_latest(frame)
            for cb in self._callbacks:
                cb(frame)

            t_offset += 0.001  # slight time drift to ensure motion detection fires
            time.sleep(1.0 / self.fps)

    def start(self):
        """Start capture in background thread."""
        self._running = True
        self._thread = threading.Thread(target=self._capture_loop, daemon=True)
        self._thread.start()

    def stop(self):
        """Stop capture."""
        self._running = False
        if self._thread:
            self._thread.join(timeout=5)

    def on_frame(self, callback: Callable[[np.ndarray], None]):
        """Register callback for each frame."""
        self._callbacks.append(callback)

    @property
    def frame_count(self) -> int:
        return self._frame_count
