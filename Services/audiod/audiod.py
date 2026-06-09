#!/usr/bin/env python3
"""audiod — Audio pipeline service for Dan Glasses.

ALSA capture → VAD (Silero) → whisper.cpp → transcript events
"""

import sys
import yaml
import signal
import numpy as np
import threading
import argparse
from pathlib import Path

from capture import ALSACapture
from vad import VADSpeechDetector
from transcription import WhisperTranscriber
from ptt import PTTTrigger
from publish import TranscriptPublisher

import http.server


class HealthHandler(http.server.BaseHTTPRequestHandler):
    """HTTP health check handler for audiod."""
    pipeline = None

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status":"ok","service":"audiod"}')
        elif self.path == "/status":
            running = False
            vad_ready = False
            if HealthHandler.pipeline is not None:
                p = HealthHandler.pipeline
                running = p._running
                vad_ready = p.vad is not None and p.vad.is_ready()
            import json
            body = json.dumps({"status": "ok", "service": "audiod", "running": running, "vad_ready": vad_ready})
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # silence HTTP logs


def start_health_server(port: int = 8090):
    """Start HTTP health server in background thread."""
    import socket
    # Allow port reuse to avoid "Address already in use" on restarts
    class ReuseAddrHTTPServer(http.server.HTTPServer):
        def server_bind(self):
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            super().server_bind()
    server = ReuseAddrHTTPServer(("0.0.0.0", port), HealthHandler)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    return server


class AudioPipeline:
    """Main audio pipeline orchestrating capture → VAD → transcription."""

    def __init__(self, config: dict):
        self.config = config
        self.sample_rate = config["audio"]["sample_rate"]
        self._running = False
        self._lock = threading.Lock()

        # Publisher
        pub_cfg = config.get("publish", {})
        self.publisher = TranscriptPublisher(
            mode=pub_cfg.get("mode", "stdout"),
            socket_path=pub_cfg.get("socket_path", "/run/audiod.sock"),
            ws_port=pub_cfg.get("ws_port", 8091),
        )

        # Capture
        cap_cfg = config["audio"]
        self.capture = ALSACapture(
            device=cap_cfg.get("device", "default"),
            sample_rate=cap_cfg.get("sample_rate", 16000),
            channels=cap_cfg.get("channels", 1),
            period_size=cap_cfg.get("period_size", 512),
            buffer_periods=cap_cfg.get("buffer_periods", 8),
        )

        # VAD
        vad_cfg = config["vad"]
        self.vad = VADSpeechDetector(
            threshold=vad_cfg.get("threshold", 0.5),
            min_speech_ms=vad_cfg.get("min_speech_ms", 250),
            min_silence_ms=vad_cfg.get("min_silence_ms", 200),
            sample_rate=self.sample_rate,
            on_speech_start=self._on_speech_start,
            on_speech_end=self._on_speech_end,
        )

        # Transcription
        w_cfg = config["whisper"]
        self.transcriber = WhisperTranscriber(
            model_path=w_cfg.get("model", "ggml-base.bin"),
            language=w_cfg.get("language", "auto"),
            threads=w_cfg.get("threads", 2),
        )

        # PTT
        ptt_cfg = config.get("push_to_talk", {})
        self._ptt_enabled = ptt_cfg.get("enabled", False)
        self._ptt_trigger = None
        if self._ptt_enabled:
            self._ptt_trigger = PTTTrigger(
                hotkey=ptt_cfg.get("hotkey", "space"),
                on_trigger=self._on_ptt_trigger,
            )

        self._segment_start_ms = 0

    def _on_speech_start(self):
        """Called when VAD detects speech start."""
        with self._lock:
            self._segment_start_ms = int(
                sum(len(x) for x in self.vad._speech_buffer) * 1000 // self.sample_rate
                if self.vad._speech_buffer
                else 0
            )
        print(f"audiod: speech start", flush=True)

    def _on_speech_end(self, segment: np.ndarray):
        """Called when VAD detects speech end."""
        if len(segment) < self.sample_rate * 0.1:
            return
        self._transcribe_segment(segment, self._segment_start_ms)

    def _transcribe_segment(self, segment: np.ndarray, start_ms: int):
        """Run transcription on a speech segment."""
        if len(segment) < 160:
            return

        result = self.transcriber.transcribe(segment, self.sample_rate)
        if result["text"]:
            result["start_ms"] = start_ms
            self.publisher.publish(result)

    def _on_ptt_trigger(self):
        """Handle push-to-talk trigger."""
        with self._lock:
            segment = self.vad.force_flush()
            if len(segment) > 0:
                self._transcribe_segment(segment, self._segment_start_ms)
        print("audiod: PTT triggered", flush=True)

    def _process_loop(self):
        """Main processing loop reading from capture buffer."""
        chunk_size = 512  # 32ms at 16kHz

        while self._running:
            chunk = self.capture.read(chunk_size)
            if len(chunk) == 0:
                continue
            self.vad.process(chunk)

    def start(self):
        """Start the audio pipeline."""
        self._running = True
        self.capture.start()

        if self._ptt_trigger:
            self._ptt_trigger.start()

        self._process_loop()

    def stop(self):
        """Stop the audio pipeline."""
        self._running = False
        self.capture.stop()

        if self._ptt_trigger:
            self._ptt_trigger.stop()

        self.publisher.close()


def load_config(config_path: str = "config.yaml") -> dict:
    """Load configuration from YAML file."""
    with open(config_path) as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description="audiod - Dan Glasses audio pipeline")
    parser.add_argument("--config", default="config.yaml", help="Config file path")
    parser.add_argument("--model", help="Override whisper model path")
    parser.add_argument("--device", help="Override ALSA device")
    parser.add_argument("--port", type=int, default=8090, help="Health server port")
    args = parser.parse_args()

    # Load config
    config = load_config(args.config)

    # CLI overrides
    if args.model:
        config["whisper"]["model"] = args.model
    if args.device:
        config["audio"]["device"] = args.device

    # Setup signal handlers
    pipeline = AudioPipeline(config)

    def signal_handler(sig, frame):
        print("\naudiod: stopping", flush=True)
        pipeline.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Start HTTP health server
    HealthHandler.pipeline = pipeline
    health_server = start_health_server(args.port)

    print(f"audiod: starting (config={args.config})", flush=True)
    print(f"audiod: whisper={config['whisper']['model']}", flush=True)
    print(f"audiod: health server on port {args.port}", flush=True)

    try:
        pipeline.start()
    except Exception as e:
        print(f"audiod: error - {e}", flush=True)
        pipeline.stop()
        sys.exit(1)


if __name__ == "__main__":
    main()