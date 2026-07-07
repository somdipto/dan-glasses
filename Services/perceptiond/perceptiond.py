#!/usr/bin/env python3
"""perceptiond — Vision pipeline service for Dan Glasses.

Camera → V4L2 capture → motion salience → [if salient] → VLM (llama.cpp) → description → publish
"""

import sys
import time
import uuid
import signal
import argparse
import threading
import json
import os
from collections import deque
from pathlib import Path
from typing import Optional
import numpy as np

from capture import V4L2Capture
from salience import SalienceDetector
from vlm import VLMInference
from events import DescriptionPublisher, FrameStore, PerceptiondServer
from config import load_config


class SceneGate:
    """v7.0 — scene-change deduplication.

    Tracks the last triggered motion score and a rolling baseline. A new
    salient frame is allowed to invoke VLM only if the current motion score
    differs from the last triggered score by >= `threshold`, OR if the
    rolling-baseline std-dev has spiked (catches content changes that
    happen to land near the same score as the last frame).

    Thread-safe; the same gate instance is touched from the frame callback
    thread and read from the publisher.
    """

    def __init__(self, threshold: float = 0.02, window: int = 5):
        self.threshold = float(threshold)
        self.window = max(2, int(window))
        self._lock = threading.Lock()
        self._last_triggered_score: Optional[float] = None
        self._baseline: deque = deque(maxlen=self.window)
        self._total_evaluations = 0
        self._total_skips = 0

    def should_run(self, motion_score: float) -> bool:
        """Return True if VLM should run on a salient frame.

        Disabled (always True) when threshold == 0.0. Otherwise require
        the current score to differ from the last triggered score by at
        least `threshold`, or to be a clear outlier vs. the rolling
        baseline.
        """
        with self._lock:
            self._total_evaluations += 1
            if self.threshold <= 0.0:
                self._last_triggered_score = motion_score
                return True
            if self._last_triggered_score is None:
                self._last_triggered_score = motion_score
                self._baseline.append(motion_score)
                return True
            delta = abs(motion_score - self._last_triggered_score)
            if delta >= self.threshold:
                self._last_triggered_score = motion_score
                self._baseline.append(motion_score)
                return True
            # Outlier check: if baseline is non-empty and current score
            # is more than 3x std-dev away from the mean, scene changed
            # even if delta from last trigger is small.
            if len(self._baseline) >= 3:
                arr = np.fromiter(self._baseline, dtype=np.float32)
                mean = float(arr.mean())
                std = float(arr.std()) if len(arr) > 1 else 0.0
                if std > 0 and abs(motion_score - mean) > 3.0 * std:
                    self._last_triggered_score = motion_score
                    self._baseline.append(motion_score)
                    return True
            self._total_skips += 1
            return False

    def reset(self) -> None:
        with self._lock:
            self._last_triggered_score = None
            self._baseline.clear()
            self._total_evaluations = 0
            self._total_skips = 0

    def stats(self) -> dict:
        with self._lock:
            return {
                "threshold": self.threshold,
                "window": self.window,
                "evaluations": self._total_evaluations,
                "skips": self._total_skips,
                "last_triggered_score": self._last_triggered_score,
                "baseline_size": len(self._baseline),
            }


class PerceptionPipeline:
    """Main vision pipeline orchestrating capture → salience → VLM → publish."""

    # Max VLM queue depth before skipping frames (prevents unbounded lag)
    MAX_QUEUE_DEPTH = 2

    def __init__(self, config: dict):
        self.config = config
        self._running = False
        self._lock = threading.Lock()
        self._vlm_busy = False
        self._vlm_queue_depth = 0  # Track outstanding VLM calls

        # Publisher
        pub_cfg = config.get("server", {})
        # v8.0: memoryd sink is opt-in. Disabled if `memory_sink.enabled`
        # is False or `url` is empty.
        sink_cfg = config.get("memory_sink", {}) or {}
        sink_enabled = bool(sink_cfg.get("enabled", True)) and bool(sink_cfg.get("url"))
        self.publisher = DescriptionPublisher(
            mode=pub_cfg.get("mode", "stdout"),
            socket_path=pub_cfg.get("socket_path", "/var/run/perceptiond.sock"),
            memory_sink_url=sink_cfg.get("url") if sink_enabled else None,
            memory_sink_timeout=float(sink_cfg.get("timeout", 2.0)),
            memory_sink_queue_cap=int(sink_cfg.get("queue_cap", 256)),
        )

        # HTTP server (for health/status checks) - TCP on 8092 + Unix socket
        self.server = PerceptiondServer(
            socket_path=pub_cfg.get("socket_path", "/var/run/perceptiond.sock"),
            tcp_port=8092,
        )
        # Give server reference to pipeline for status queries
        self.server.set_pipeline(self)

        # Per-event thumbnail ring (for /frames/<image_id>.jpg)
        # v10.0: opt-in persistent frame store. When enabled, the
        # FrameStore writes JPEGs to disk so memoryd's image_id refs
        # stay resolvable across the in-memory ring being overrun.
        img_cfg = config.get("image_store", {}) or {}
        if img_cfg.get("enabled", True):
            raw_dir = img_cfg.get("dir") or "~/.cache/dan-glasses/perceptiond/frames"
            image_dir = os.path.expanduser(raw_dir)
        else:
            image_dir = None
        self.frame_store = FrameStore(
            capacity=int(img_cfg.get("capacity", 50)),
            image_dir=image_dir,
            max_bytes=int(img_cfg.get("max_bytes", 200 * 1024 * 1024)),
        )
        self.server.set_frame_store(self.frame_store)

        # Capture
        cam_cfg = config["camera"]
        self.capture = V4L2Capture(
            device=cam_cfg.get("device", "/dev/video0"),
            width=cam_cfg.get("width", 640),
            height=cam_cfg.get("height", 480),
            fps=cam_cfg.get("fps", 5),
        )

        # Salience detector
        sal_cfg = config["salience"]
        self.salience = SalienceDetector(
            motion_threshold=sal_cfg.get("motion_threshold", 0.15),
            pixel_delta_threshold=sal_cfg.get("pixel_delta_threshold", 30),
            background_update_interval=sal_cfg.get("background_update_interval", 30),
            width=cam_cfg.get("width", 640),
            height=cam_cfg.get("height", 480),
            mode=sal_cfg.get("mode", "any"),
            face_scale_factor=sal_cfg.get("face_scale_factor", 1.1),
            face_min_neighbors=sal_cfg.get("face_min_neighbors", 5),
            face_min_size=sal_cfg.get("face_min_size", 30),
        )

        # VLM
        vlm_cfg = config["vlm"]
        self.vlm = VLMInference(
            model_path=vlm_cfg.get("model_path", ""),
            mmproj_path=vlm_cfg.get("mmproj_path", ""),
            llama_cli_path=vlm_cfg.get("llama_cli_path", "/home/workspace/danlab-multimodal/llama.cpp/build/bin/llama-mtmd-cli"),
            prompt=vlm_cfg.get("prompt", "Describe this image briefly. Focus on: people, objects, text, activities."),
            max_tokens=vlm_cfg.get("max_tokens", 100),
            timeout=vlm_cfg.get("timeout", 30),
        )

        # Power mode
        self._mode = config.get("power", {}).get("mode", "watchful")
        self._fps_map = {"idle": 0, "watchful": 5, "active": 10}

        # v7.0: scene-change gate (suppresses VLM on near-duplicate motion)
        dedup_cfg = config.get("dedup", {}) or {}
        self.scene_gate = SceneGate(
            threshold=dedup_cfg.get("threshold", 0.02),
            window=dedup_cfg.get("window", 5),
        )

        # Stats
        self._frames_processed = 0
        self._salient_frames = 0
        self._descriptions = 0
        self._scene_skips = 0       # v7.0: count of frames skipped by SceneGate
        self._vlm_invocations = 0   # v7.0: count of actual VLM subprocess calls
        # v7.0 telemetry — most-recent salience signals, exposed via /status
        self._last_motion_score = 0.0
        self._last_face_count = 0
        self._last_trigger_kind = "none"
        self._deduped_count = 0     # v7.0: frames the gate let through
        self._dedup_skip_count = 0  # v7.0: alias of scene_skips, kept for status clarity

        # Register frame callback
        self.capture.on_frame(self._on_frame)

    def _on_frame(self, frame):
        """Handle each captured frame.

        v7.0: also feeds motion score into SceneGate. If the gate says
        the current frame is too similar to the last triggered frame, we
        skip the expensive VLM call entirely. The skip is counted but the
        frame is still considered processed.

        v9.0: captures the per-frame bboxes from the salience result and
        forwards them to _run_vlm so the description event includes the
        rectangle(s) the VLM actually saw. /frames/<id>.jpg paints them
        back on top of the thumbnail via /frames/<id>.jpg?overlay=1.
        """
        with self._lock:
            if self._mode == "idle":
                return
            if self._vlm_busy:
                return  # Skip if VLM still processing
            if self._vlm_queue_depth >= self.MAX_QUEUE_DEPTH:
                return  # Skip if we're falling behind

        # Salience — capture both the verdict and the raw signals so we
        # can log them and feed motion_score to the SceneGate.
        result = self.salience.evaluate(frame)

        with self._lock:
            self._frames_processed += 1
            self._last_motion_score = result.motion_score
            self._last_face_count = result.face_count
            if result.salient:
                self._salient_frames += 1
                self._last_trigger_kind = result.kind

        if not result.salient and self._mode == "watchful":
            return  # Skip non-salient frames in watchful mode

        # Scene gate: only run VLM when the scene has actually changed.
        # threshold=0.0 disables the gate (always run).
        if not self.scene_gate.should_run(result.motion_score):
            with self._lock:
                self._scene_skips += 1
                self._dedup_skip_count = self._scene_skips
            return

        with self._lock:
            self._deduped_count += 1

        # Run VLM (carry bboxes through so the event and the thumbnail
        # are consistent with what the VLM was asked to describe).
        self._run_vlm(frame, result.bboxes)

    def _encode_thumb(self, frame) -> "Optional[bytes]":
        """Encode a small JPEG thumbnail for the frame (used for /frames/<id>.jpg)."""
        try:
            from PIL import Image
            import io
            if frame is None:
                return None
            if frame.dtype != np.uint8:
                frame = frame.astype(np.uint8)
            if frame.ndim == 2:
                frame = np.stack([frame, frame, frame], axis=-1)
            elif frame.ndim == 3 and frame.shape[2] == 4:
                frame = frame[:, :, :3]
            img = Image.fromarray(frame)
            # Downscale to a reasonable thumb for transport over the wire.
            img.thumbnail((320, 240))
            buf = io.BytesIO()
            img.save(buf, format="JPEG", quality=70)
            return buf.getvalue()
        except Exception as e:
            print(f"perceptiond: thumb encode error: {e}", flush=True)
            return None

    def _run_vlm(self, frame, bboxes: Optional[list] = None):
        """Run VLM on a frame in a background thread.

        v9.0: `bboxes` is the salience result's rectangle list. We pass it
        to DescriptionPublisher so the description event carries the same
        coordinates the /frames/<id>.jpg overlay paints. Defaults to
        None / empty for tests that don't supply a SalienceResult.
        """
        bboxes = bboxes or []

        def _do():
            with self._lock:
                self._vlm_busy = True
                self._vlm_queue_depth += 1

            image_id = str(uuid.uuid4())[:8]
            thumb = self._encode_thumb(frame)
            if thumb:
                # v9.0: stash the bboxes next to the JPEG so the
                # /frames/<id>.jpg handler can paint them on demand
                # without needing a second lookup.
                if bboxes:
                    self.frame_store.put_with_bboxes(image_id, thumb, bboxes)
                else:
                    self.frame_store.put(image_id, thumb)

            try:
                # v7.0: count the VLM invocation before the actual call so
                # /stats can show attempts vs. successful descriptions.
                with self._lock:
                    self._vlm_invocations += 1
                desc = self.vlm.describe(frame)
                if desc:
                    with self._lock:
                        self._descriptions += 1
                    self.publisher.publish({
                        "type": "description",
                        "image_id": image_id,
                        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                        "description": desc,
                        "trigger_kind": self._last_trigger_kind,
                        "motion_score": round(self._last_motion_score, 4),
                        "bboxes": bboxes,
                    })
            except Exception as e:
                print(f"perceptiond: VLM error: {e}", flush=True)
            finally:
                with self._lock:
                    self._vlm_busy = False
                    self._vlm_queue_depth -= 1

        threading.Thread(target=_do, daemon=True).start()

    def set_mode(self, mode: str):
        """Set power mode: idle, watchful, active."""
        if mode not in self._fps_map:
            return
        with self._lock:
            self._mode = mode
            fps = self._fps_map[mode]
            if fps == 0:
                self.capture.stop()
            else:
                if not self.capture._running:
                    self.capture.fps = fps
                    self.capture.start()

    def set_capture(self, capture: V4L2Capture):
        """Set the capture device."""
        self.capture = capture

    def get_status(self) -> dict:
        """Return pipeline status (v7.0 — exposes salience telemetry).

        Includes a live SSE subscriber count so dashboards can render how
        many clients are currently listening to /events. Computed outside
        the pipeline lock (EventBus has its own internal lock).
        """
        with self._lock:
            base = {
                "mode": self._mode,
                "running": self._running,
                "frames_processed": self._frames_processed,
                "salient_frames": self._salient_frames,
                "descriptions": self._descriptions,
                "vlm_busy": self._vlm_busy,
                "vlm_queue_depth": self._vlm_queue_depth,
                # v7.0 telemetry
                "vlm_invocations": self._vlm_invocations,
                "scene_skips": self._scene_skips,
                "scene_threshold": self.scene_gate.threshold,
                "motion_score": round(self._last_motion_score, 4),
                "face_count": self._last_face_count,
                "last_trigger_kind": self._last_trigger_kind,
                "deduped_count": self._deduped_count,
                "dedup_skip_count": self._dedup_skip_count,
                # v11.0: monotonic publish counter + ring-buffer cursor
                # so dashboards can detect missed events and resume
                # cleanly via /descriptions?since=<id>.
                "total_published": self.publisher.total_published() if self.publisher else 0,
                "ring_oldest_event_id": self.publisher.ring_oldest_event_id() if self.publisher else 0,
            }
        try:
            base["sse_subscribers"] = self.publisher.event_bus.subscriber_count()
        except Exception:
            base["sse_subscribers"] = 0
        # v8.0 — memoryd sink counters
        try:
            base["memory_sink"] = self.publisher.memory_sink.stats()
        except Exception:
            pass
        # v10.0 — persistent image-store counters
        try:
            base["image_store"] = self.frame_store.stats()
        except Exception:
            pass
        return base

    def get_detailed_status(self) -> dict:
        """v7.0 — get_status() augmented with scene-gate internals and
        active SSE subscriber count. Used by /stats and dashboards.
        """
        with self._lock:
            base = {
                "mode": self._mode,
                "running": self._running,
                "frames_processed": self._frames_processed,
                "salient_frames": self._salient_frames,
                "descriptions": self._descriptions,
                "vlm_busy": self._vlm_busy,
                "vlm_queue_depth": self._vlm_queue_depth,
                "vlm_invocations": self._vlm_invocations,
                "scene_skips": self._scene_skips,
                "scene_threshold": self.scene_gate.threshold,
                "motion_score": round(self._last_motion_score, 4),
                "face_count": self._last_face_count,
                "last_trigger_kind": self._last_trigger_kind,
                "deduped_count": self._deduped_count,
                "dedup_skip_count": self._dedup_skip_count,
                "scene_gate": self.scene_gate.stats(),
                # v11.0: monotonic publish counter + ring-buffer cursor
                "total_published": self.publisher.total_published() if self.publisher else 0,
                "ring_oldest_event_id": self.publisher.ring_oldest_event_id() if self.publisher else 0,
            }
        # Subscriber count is read without holding self._lock to avoid
        # contending with the publisher hot path; EventBus has its own
        # internal lock.
        try:
            base["sse_subscribers"] = self.publisher.event_bus.subscriber_count()
        except Exception:
            base["sse_subscribers"] = 0
        # v10.0 — persistent image-store counters
        try:
            base["image_store"] = self.frame_store.stats()
        except Exception:
            pass
        return base

    def start(self):
        """Start the vision pipeline."""
        self._running = True
        self.server.start()
        self.server.set_capture(self.capture)

        if self._fps_map.get(self._mode, 0) > 0:
            self.capture.start()

        print(f"perceptiond: started (mode={self._mode})", flush=True)

    def stop(self):
        """Stop the vision pipeline."""
        self._running = False
        self.capture.stop()
        self.server.stop()
        self.vlm.shutdown()
        self.publisher.close()
        print("perceptiond: stopped", flush=True)


def main():
    parser = argparse.ArgumentParser(description="perceptiond - Dan Glasses vision pipeline")
    parser.add_argument("--config", default="/etc/dan-glasses/perceptiond.yaml", help="Config file path")
    parser.add_argument("--mode", choices=["idle", "watchful", "active"], help="Override power mode")
    args = parser.parse_args()

    # Load config
    config = load_config(args.config if Path(args.config).exists() else None)

    # CLI overrides
    if args.mode:
        config["power"]["mode"] = args.mode

    # Create pipeline
    pipeline = PerceptionPipeline(config)

    # Signal handlers
    def signal_handler(sig, frame):
        print("\nperceptiond: stopping", flush=True)
        pipeline.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    print(f"perceptiond: starting (config={args.config}, mode={config['power']['mode']})", flush=True)

    try:
        pipeline.start()

        # Keep main thread alive
        while pipeline._running:
            time.sleep(1)

            # Periodic status log
            status = pipeline.get_status()
            if status["frames_processed"] % 100 == 0 and status["frames_processed"] > 0:
                print(f"perceptiond: {status}", flush=True)

    except Exception as e:
        print(f"perceptiond: error - {e}", flush=True)
        pipeline.stop()
        sys.exit(1)


if __name__ == "__main__":
    main()