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
from pathlib import Path

from capture import V4L2Capture
from salience import SalienceDetector
from vlm import VLMInference
from events import DescriptionPublisher, PerceptiondServer
from config import load_config


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
        self.publisher = DescriptionPublisher(
            mode=pub_cfg.get("mode", "stdout"),
            socket_path=pub_cfg.get("socket_path", "/var/run/perceptiond.sock"),
        )

        # HTTP server (for health/status checks) - TCP on 8091 + Unix socket
        self.server = PerceptiondServer(
            socket_path=pub_cfg.get("socket_path", "/var/run/perceptiond.sock"),
            tcp_port=8092,
        )
        # Give server reference to pipeline for status queries
        self.server.set_pipeline(self)

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

        # Stats
        self._frames_processed = 0
        self._salient_frames = 0
        self._descriptions = 0

        # Register frame callback
        self.capture.on_frame(self._on_frame)

    def _on_frame(self, frame):
        """Handle each captured frame."""
        with self._lock:
            if self._mode == "idle":
                return
            if self._vlm_busy:
                return  # Skip if VLM still processing
            if self._vlm_queue_depth >= self.MAX_QUEUE_DEPTH:
                return  # Skip if we're falling behind

        # Check salience
        salient = self.salience.is_salient(frame)

        with self._lock:
            self._frames_processed += 1
            if salient:
                self._salient_frames += 1

        if not salient and self._mode == "watchful":
            return  # Skip non-salient frames in watchful mode

        # Run VLM
        self._run_vlm(frame)

    def _run_vlm(self, frame):
        """Run VLM on a frame in a background thread."""
        def _do():
            with self._lock:
                self._vlm_busy = True
                self._vlm_queue_depth += 1

            try:
                desc = self.vlm.describe(frame)
                if desc:
                    with self._lock:
                        self._descriptions += 1
                    self.publisher.publish({
                        "type": "description",
                        "image_id": str(uuid.uuid4())[:8],
                        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                        "description": desc,
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
        """Return pipeline status."""
        with self._lock:
            return {
                "mode": self._mode,
                "running": self._running,
                "frames_processed": self._frames_processed,
                "salient_frames": self._salient_frames,
                "descriptions": self._descriptions,
                "vlm_busy": self._vlm_busy,
                "vlm_queue_depth": self._vlm_queue_depth,
            }

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