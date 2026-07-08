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

from dataclasses import dataclass, field
import numpy as np
from typing import Optional, List, Tuple

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


# A bounding box in the salience frame coordinate system. (x, y, w, h)
# is the same convention OpenCV's Haar cascade returns: top-left origin,
# width/height in pixels. `kind` says which detector produced it
# ("face" today, "motion" when v9.0 derives a change-region bbox).
BBox = Tuple[int, int, int, int]


@dataclass
class SalienceResult:
    """Result of evaluating a single frame.

    `salient` is the boolean verdict. `motion_score` and `face_count` are
    the raw signals that drove the verdict. `kind` is one of TRIGGER_*
    so the pipeline can report WHY it considered the frame interesting.
    `bboxes` carries the actual face rectangles (and, on motion-triggered
    frames, the changed-region bounding box) so the publisher and the
    /frames endpoint can render annotations on the thumbnail.
    """

    salient: bool
    motion_score: float
    face_count: int
    kind: str
    bboxes: List[dict] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "salient": self.salient,
            "motion_score": round(self.motion_score, 6),
            "face_count": self.face_count,
            "kind": self.kind,
            "bboxes": list(self.bboxes),
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

        v9.0 — also returns `bboxes` for everything that drove the
        verdict: face rectangles from the Haar cascade (in the salience
        frame's coordinate system), and, for motion-triggered frames,
        the bounding box of the changed-region mask. The pipeline stores
        the result on the description event so the UI can draw overlays
        on /frames/<id>.jpg.
        """
        motion_score, face_rects, motion_region = self._compute_signals(frame)
        face_count = len(face_rects)
        bboxes: List[dict] = []
        for (x, y, w, h) in face_rects:
            bboxes.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h), "kind": "face"})
        if motion_region is not None:
            mx, my, mw, mh = motion_region
            bboxes.append({"x": int(mx), "y": int(my), "w": int(mw), "h": int(mh), "kind": "motion"})

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
            bboxes=bboxes,
        )

    # ------------------------------------------------------------------
    # Internals — split out the three signals (motion, faces, region) so
    # tests and the bbox endpoint can call them individually if needed.
    # ------------------------------------------------------------------

    def _compute_signals(self, frame: np.ndarray):
        """Run all three detectors and return (motion_score, face_rects, motion_region)."""
        motion_score, motion_region = self._motion_score_with_region(frame)
        face_rects = self._face_rects(frame)
        return motion_score, face_rects, motion_region

    def _motion_score_with_region(self, frame: np.ndarray):
        """Like _motion_score but also returns the bounding box of the changed pixels.

        Returns (score, None) on the first frame (no background yet) or
        (score, (x, y, w, h)) once a background exists. The bbox is in
        the salience frame coordinate system (i.e. the frame passed in),
        not the grayscale image — both share the same w/h since we never
        resize before differencing.
        """
        gray = self._to_grayscale(frame)

        if self._background is None:
            self._background = gray.astype(np.float32)
            self._frame_count = 0
            return 0.0, None

        if self._frame_count > 0 and self._frame_count % self.background_update_interval == 0:
            self._background = 0.95 * self._background + 0.05 * gray.astype(np.float32)

        diff = np.abs(gray.astype(np.float32) - self._background)
        changed_pixels = diff > self.pixel_delta_threshold
        self._frame_count += 1

        score = float(np.mean(changed_pixels))
        region = _bbox_of_mask(changed_pixels) if changed_pixels.any() else None
        return score, region

    def _face_rects(self, frame: np.ndarray) -> List[BBox]:
        """Return face rectangles in the original frame coordinate system."""
        if not CV2_AVAILABLE or self._face_cascade is None:
            return []

        try:
            gray = self._to_grayscale(frame)
            gray_small = cv2.resize(gray, (320, 240))
            faces = self._face_cascade.detectMultiScale(
                gray_small,
                scaleFactor=self.face_scale_factor,
                minNeighbors=self.face_min_neighbors,
                minSize=(self.face_min_size, self.face_min_size),
            )
            if len(faces) == 0:
                return []
            # Scale rectangles back up from 320x240 to the original frame
            # dimensions. The cascade runs on the downsampled image but
            # we want bboxes in the salience frame space so the overlay
            # lines up pixel-perfect with the thumbnail.
            h, w = gray.shape[:2]
            sx = w / 320.0
            sy = h / 240.0
            out: List[BBox] = []
            for (x, y, fw, fh) in faces:
                out.append((int(round(x * sx)), int(round(y * sy)),
                            int(round(fw * sx)), int(round(fh * sy))))
            return out
        except Exception:
            return []

    def _motion_score(self, frame: np.ndarray) -> float:
        """Backwards-compatible scalar wrapper — kept for tests that
        only want the score, not the region. Calls the unified path."""
        return self._motion_score_with_region(frame)[0]

    def _face_score(self, frame: np.ndarray) -> float:
        """Backwards-compatible face-count wrapper."""
        return float(len(self._face_rects(frame)))

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


def _bbox_of_mask(mask: np.ndarray) -> Optional[BBox]:
    """Tight bounding box around True pixels in a 2D boolean mask.

    Returns (x, y, w, h) in mask coordinates or None if the mask is empty.
    Uses np.argwhere for clarity — masks are 480x640 (≈300k pixels) and
    this is called only on salient frames, so the cost is negligible.
    """
    if not mask.any():
        return None
    ys, xs = np.where(mask)
    x0 = int(xs.min())
    y0 = int(ys.min())
    x1 = int(xs.max()) + 1
    y1 = int(ys.max()) + 1
    return (x0, y0, x1 - x0, y1 - y0)