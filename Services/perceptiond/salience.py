"""Salience detection via motion + face detection cascade.

Algorithm:
- Maintain background frame (updated every N frames via EMA)
- Compute absolute pixel difference → motion score
- Also run Haar cascade face detection → face score
- Frame is salient if motion OR face threshold exceeded
- Salience mode: "motion" | "face" | "any" (default "any")

v7.0: expose SalienceResult with motion_score / face_count / trigger_kind
so the pipeline can record telemetry for the /status and /stats endpoints.
"""

from dataclasses import dataclass
import numpy as np
from typing import Optional

CV2_AVAILABLE = False
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    pass


# Trigger kind constants — surfaced in the pipeline status so operators
# can see *why* VLM fired (motion, face, both) on a given frame.
TRIGGER_NONE = "none"
TRIGGER_MOTION = "motion"
TRIGGER_FACE = "face"
TRIGGER_BOTH = "both"


@dataclass
class SalienceResult:
    """Result of evaluating a single frame.

    `salient` is the boolean verdict. `motion_score` and `face_count` are
    the raw signals that drove the verdict. `kind` is one of TRIGGER_*
    so the pipeline can report WHY it considered the frame interesting.
    """

    salient: bool
    motion_score: float
    face_count: int
    kind: str

    def to_dict(self) -> dict:
        return {
            "salient": self.salient,
            "motion_score": round(self.motion_score, 6),
            "face_count": self.face_count,
            "kind": self.kind,
        }


class SalienceDetector:
    """Detect salient frames using motion and/or face detection."""

    def __init__(
        self,
        motion_threshold: float = 0.15,
        pixel_delta_threshold: int = 30,
        background_update_interval: int = 30,
        width: int = 640,
        height: int = 480,
        mode: str = "any",  # "motion" | "face" | "any"
        face_scale_factor: float = 1.1,
        face_min_neighbors: int = 5,
        face_min_size: int = 30,
    ):
        self.motion_threshold = motion_threshold
        self.pixel_delta_threshold = pixel_delta_threshold
        self.background_update_interval = background_update_interval
        self.width = width
        self.height = height
        self.mode = mode
        self.face_scale_factor = face_scale_factor
        self.face_min_neighbors = face_min_neighbors
        self.face_min_size = face_min_size

        self._background: Optional[np.ndarray] = None
        self._frame_count = 0
        self._face_cascade: Optional[object] = None

        if CV2_AVAILABLE and mode in ("face", "any"):
            cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            self._face_cascade = cv2.CascadeClassifier(cascade_path)

    def is_salient(self, frame: np.ndarray) -> bool:
        """Return True if frame is salient (interesting). Thin wrapper over evaluate()."""
        return self.evaluate(frame).salient

    def evaluate(self, frame: np.ndarray) -> SalienceResult:
        """Run salience analysis and return a structured SalienceResult.

        Always computes motion_score so callers can route through the
        SceneGate even on non-salient frames (the gate consumes the raw
        score, not just the boolean).
        """
        motion_score = self._motion_score(frame)
        face_count = int(self._face_score(frame))

        motion_hit = motion_score > self.motion_threshold
        face_hit = face_count > 0

        if self.mode == "motion":
            salient = motion_hit
        elif self.mode == "face":
            salient = face_hit
        else:  # "any" — either motion or face
            salient = motion_hit or face_hit

        if salient:
            if motion_hit and face_hit:
                kind = TRIGGER_BOTH
            elif motion_hit:
                kind = TRIGGER_MOTION
            else:
                kind = TRIGGER_FACE
        else:
            kind = TRIGGER_NONE

        return SalienceResult(
            salient=salient,
            motion_score=motion_score,
            face_count=face_count,
            kind=kind,
        )

    def _motion_score(self, frame: np.ndarray) -> float:
        """Compute motion score (0.0 to 1.0)."""
        gray = self._to_grayscale(frame)

        if self._background is None:
            self._background = gray.astype(np.float32)
            self._frame_count = 0
            return 0.0

        if self._frame_count > 0 and self._frame_count % self.background_update_interval == 0:
            self._background = 0.95 * self._background + 0.05 * gray.astype(np.float32)

        diff = np.abs(gray.astype(np.float32) - self._background)
        changed_pixels = diff > self.pixel_delta_threshold
        self._frame_count += 1

        return float(np.mean(changed_pixels))

    def _face_score(self, frame: np.ndarray) -> float:
        """Compute face score (number of faces detected)."""
        if not CV2_AVAILABLE or self._face_cascade is None:
            return 0.0

        try:
            gray = self._to_grayscale(frame)
            gray_small = cv2.resize(gray, (320, 240))
            faces = self._face_cascade.detectMultiScale(
                gray_small,
                scaleFactor=self.face_scale_factor,
                minNeighbors=self.face_min_neighbors,
                minSize=(self.face_min_size, self.face_min_size),
            )
            return float(len(faces))
        except Exception:
            return 0.0

    def _to_grayscale(self, frame: np.ndarray) -> np.ndarray:
        """Convert RGB/BGR frame to grayscale."""
        if len(frame.shape) == 2:
            return frame
        if frame.shape[2] == 3:
            return (frame[:, :, 0] * 0.299 + frame[:, :, 1] * 0.587 + frame[:, :, 2] * 0.114).astype(np.uint8)
        return frame[:, :, 0]

    def reset_background(self):
        """Manually reset background frame."""
        self._background = None
        self._frame_count = 0
