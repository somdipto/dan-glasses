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
import time
import os
from pathlib import Path
from typing import Optional
import queue

from capture import ALSACapture
from vad import VADSpeechDetector
from transcription import WhisperTranscriber
from ptt import PTTTrigger
from publish import TranscriptPublisher
from segment_timing import SegmentTimingHistogram

import http.server


class HealthHandler(http.server.BaseHTTPRequestHandler):
    """HTTP health + control plane for audiod.

    GET  /health    — liveness probe
    GET  /status    — full deployment diagnostics
    GET  /config    — current effective config
    POST /start     — start capture loop (idempotent)
    POST /stop      — stop capture loop, keep WS clients connected
    POST /restart   — stop + start
    POST /ptt       — fire push-to-talk trigger
    POST /reload    — re-read config.yaml from disk
    """
    pipeline = None

    def do_GET(self):
        if self.path == "/health":
            # Back-compat alias for /ready. Keep the existing
            # 200/503 + readiness breakdown contract.
            self._send_ready()
        elif self.path == "/live":
            # Liveness probe: 200 as long as the HTTP server is up.
            # Never 503 here — that's what restart decisions should
            # look at (process died / port unreachable), not /ready.
            self._send_live()
        elif self.path == "/ready":
            # Readiness probe: 200 if pipeline fully ready, 503 with
            # breakdown + reason otherwise. K8s readinessProbe shape.
            self._send_ready()
        elif self.path == "/status":
            self._send_status()
        elif self.path == "/config":
            self._send_config()
        elif self.path == "/help":
            self._send_help()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        import json as _json
        if self.path == "/start":
            self._control(lambda p: p._cmd_start())
        elif self.path == "/stop":
            self._control(lambda p: p._cmd_stop())
        elif self.path == "/restart":
            self._control(lambda p: p._cmd_restart())
        elif self.path == "/ptt":
            self._control(lambda p: p._on_ptt_trigger())
        elif self.path == "/reload":
            self._control(lambda p: p._cmd_reload())
        else:
            self.send_response(404)
            self.end_headers()

    def _control(self, fn):
        import json as _json
        if HealthHandler.pipeline is None:
            self._json_resp(503, {"error": "pipeline not ready"})
            return
        try:
            result = fn(HealthHandler.pipeline) or {"ok": True}
            self._json_resp(200, result)
        except Exception as e:
            self._json_resp(500, {"error": str(e)})

    def _send_live(self):
        """Liveness probe — 200 as long as the HTTP server is up.

        Used by orchestrators (Kubernetes livenessProbe, systemd
        Watchdog, etc.) to decide "restart the process?". Never 503
        here — readiness gaps (model still loading, VAD not bound)
        are surfaced by /ready, not /live.
        """
        import json as _json
        self._json_resp(200, {
            "status": "alive",
            "service": "audiod",
            "pid": os.getpid(),
        })

    def _send_ready(self):
        """Readiness probe + back-compat /health alias.

        200 + {"status":"ok", "service":"audiod", "readiness":{...}}
            when VAD, whisper binary+model, and publisher are all
            initialized.

        503 + {"status":"loading", "service":"audiod",
            "readiness":{...}, "reason":str}
            otherwise. The breakdown lets an operator see exactly which
            component is not yet ready (e.g. whisper model file missing
            vs publisher listener dead).

        Backward compatible with callers that parse {status, service}.
        """
        import json as _json
        if HealthHandler.pipeline is None:
            self._json_resp(503, {
                "status": "loading",
                "service": "audiod",
                "reason": "pipeline not initialized",
                "readiness": {"vad": False, "whisper": False, "publisher": False, "running": False},
            })
            return
        ready, breakdown = HealthHandler.pipeline.is_ready()
        if ready:
            self._json_resp(200, {
                "status": "ok",
                "service": "audiod",
                "readiness": breakdown,
            })
            return
        # Identify the most likely culprit for the not-ready state.
        reason_bits = []
        if not breakdown["vad"]:
            reason_bits.append("vad not initialized")
        if not breakdown["whisper_binary"]:
            reason_bits.append("whisper binary not ready")
        if not breakdown["whisper_model"]:
            reason_bits.append("whisper model not ready")
        if not breakdown["publisher"]:
            reason_bits.append("publisher not initialized")
        self._json_resp(503, {
            "status": "loading",
            "service": "audiod",
            "reason": "; ".join(reason_bits) or "not ready",
            "readiness": breakdown,
        })

    def _send_status(self):
        import json as _json
        base = {
            "status": "ok",
            "service": "audiod",
            "running": False,
            "vad_ready": False,
            "device": None,
            "sample_rate": None,
            "channels": None,
            "whisper_model": None,
            "whisper_threads": None,
            "ptt_enabled": False,
            "ptt_hotkey": None,
            "started_at_ms": 0,
            "uptime_ms": 0,
            "pid": os.getpid(),
            "segments_transcribed": 0,
            "publisher": {"mode": None, "ws_port": None},
        }
        if HealthHandler.pipeline is None:
            self._json_resp(200, base)
            return
        try:
            extras = HealthHandler.pipeline.stats()
            base.update(extras)
            self._json_resp(200, base)
        except Exception as e:
            self._json_resp(500, {"error": str(e)})

    def _send_config(self):
        import json as _json
        if HealthHandler.pipeline is None:
            self._json_resp(200, {})
            return
        self._json_resp(200, HealthHandler.pipeline.config)

    def _send_help(self):
        """Return the audiod HTTP API surface as JSON.

        Surfaced through /api/audiod/help by the dan-glasses-app proxy.
        """
        import json as _json
        # Use the actual bound port so tests on alternate ports see
        # the correct number.
        http_port = self.server.server_address[1] if self.server else 8090
        ws_port = 8091
        if HealthHandler.pipeline is not None:
            cfg = HealthHandler.pipeline.config or {}
            ws_port = cfg.get("publish", {}).get("ws_port", ws_port)
        body = {
            "service": "audiod",
            "version": "1.0",
            "http_port": http_port,
            "ws_port": ws_port,
            "endpoints": [
                {"method": "GET",  "path": "/health",  "desc": "Liveness + readiness alias. Back-compat for callers predating /live + /ready. Returns {status:ok,service:audiod,readiness:{...}} or 503 + status:loading + reason when any component is not ready."},
                {"method": "GET",  "path": "/live",    "desc": "Liveness probe. 200 + {status:alive,service:audiod,pid} as long as the HTTP server is up. Never 503 — readiness gaps go to /ready."},
                {"method": "GET",  "path": "/ready",   "desc": "Readiness probe. 200 when VAD + whisper binary + whisper model + publisher are all initialized; 503 + readiness breakdown + reason otherwise. K8s readinessProbe shape."},
                {"method": "GET",  "path": "/status",  "desc": "Full diagnostics: running flag, VAD ready, whisper_binary_ok / whisper_model_ok booleans (distinguish missing CLI from missing model), whisper model/threads, PTT, publisher, dropped segments, in-flight transcriptions, last_segment_ms, segment_timing (count/max/p50/p95/buckets), uptime."},
                {"method": "GET",  "path": "/config",  "desc": "Current effective config (merged from config.yaml)."},
                {"method": "GET",  "path": "/help",    "desc": "This surface."},
                {"method": "POST", "path": "/start",   "desc": "Begin capture loop. Idempotent."},
                {"method": "POST", "path": "/stop",    "desc": "Stop capture loop. Idempotent."},
                {"method": "POST", "path": "/restart", "desc": "Stop then start. Recovers from bad state."},
                {"method": "POST", "path": "/ptt",     "desc": "Trigger a push-to-talk segment boundary. Body: {duration_ms?: int}."},
                {"method": "POST", "path": "/reload",  "desc": "Re-read config.yaml. Hot-swaps VAD threshold and whisper model/threads/language. Returns pending_restart_for keys that still need /restart."},
            ],
            "ws": [
                {"path": "/stream", "desc": "Transcript event fan-out. One event per transcribed segment. See publish.py for schema."},
            ],
            "config_keys_live": ["vad.threshold", "whisper.model", "whisper.threads", "whisper.language"],
            "config_keys_restart_only": ["audio.device", "audio.sample_rate", "audio.channels", "publish.mode", "publish.ws_port", "push_to_talk.hotkey"],
        }
        self._json_resp(200, body)

    def _json_resp(self, code: int, body: dict):
        import json as _json
        data = _json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

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
    """Main audio pipeline orchestrating capture → VAD → transcription.

    Lifecycle is controlled by the HTTP control plane (/start, /stop,
    /restart, /reload) AND the legacy entry-point (CLI). start() is
    non-blocking — the process loop runs on a dedicated thread so the
    control plane and HTTP server remain responsive.
    """

    def __init__(self, config: dict, config_path: Optional[str] = None):
        self.config = config
        self._config_path = config_path or "config.yaml"
        self.sample_rate = config["audio"]["sample_rate"]
        self._running = False
        self._lock = threading.Lock()
        self._started_at_ms = int(time.time() * 1000)
        self._segments_transcribed = 0
        self._dropped_segments = 0
        self._transcribe_inflight = 0
        # Duration of the most recently transcribed segment, in ms.
        # 0 when no segment has been transcribed yet in this lifetime.
        # Updated under _lock in _run_transcribe, reset by _reset_counters.
        self._last_segment_ms = 0
        # Bounded ring of recent per-segment durations. Powers the
        # `segment_timing` block in /status (count, max, p50, p95, buckets).
        self._timing = SegmentTimingHistogram(capacity=256)
        self._process_thread: Optional[threading.Thread] = None

        # Cap on a single speech segment length. Prevents a stuck VAD
        # from buffering unbounded audio, and bounds the size of any
        # one whisper.cpp invocation.
        self._max_segment_ms = config.get("vad", {}).get("max_segment_ms", 10_000)

        # Bounded segment queue. Size 2: holds the current and one
        # backlog segment. drop-oldest on overflow (see _enqueue_segment).
        self._segment_queue: queue.Queue = queue.Queue(maxsize=2)
        self._transcription_thread: Optional[threading.Thread] = None

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
        """Called when VAD detects speech start.

        Capture a fresh wall-clock-aligned timestamp; the segment length is
        computed downstream from the buffer, but the start anchor must be
        set when the segment begins, not derived from already-stored samples.
        """
        with self._lock:
            self._segment_start_ms = int(time.time() * 1000) - self._started_at_ms
        print(f"audiod: speech start @ {self._segment_start_ms}ms", flush=True)

    def _on_speech_end(self, segment: np.ndarray):
        """Called when VAD detects speech end. Enqueues for transcription."""
        if len(segment) < self.sample_rate * 0.1:
            return
        self._enqueue_segment(segment, self._segment_start_ms)

    def _enqueue_segment(self, segment: np.ndarray, start_ms: int) -> None:
        """Enqueue a segment for transcription.

        Backpressure: queue is bounded (size 2). If it's full we drop
        the OLDEST item to make room — preserves the user's most
        recent utterance at the cost of an earlier backlog segment.
        Previous behavior was drop-newest, which lost active speech
        when whisper was still busy on a long segment.
        """
        if len(segment) < 160:
            return
        try:
            self._segment_queue.put_nowait((segment, start_ms))
        except queue.Full:
            try:
                dropped, _ = self._segment_queue.get_nowait()
                self._dropped_segments += 1
                del dropped
            except queue.Empty:
                pass
            try:
                self._segment_queue.put_nowait((segment, start_ms))
            except queue.Full:
                self._dropped_segments += 1

    def _transcribe_segment(self, segment: np.ndarray, start_ms: int) -> None:
        """Synchronous transcription. Called from the worker thread.

        Kept as a private method (not a callback target) so tests can
        exercise it directly.
        """
        if len(segment) < 160:
            return
        with self._lock:
            self._transcribe_inflight += 1
        try:
            result = self.transcriber.transcribe(segment, self.sample_rate)
            if result["text"]:
                result["start_ms"] = start_ms
                self.publisher.publish(result)
                with self._lock:
                    self._segments_transcribed += 1
        finally:
            with self._lock:
                self._transcribe_inflight -= 1

    def _transcription_worker(self) -> None:
        """Worker thread: pull (segment, start_ms) from queue, transcribe, publish.

        Stops when _running flips to False. Processes one segment at a
        time — the queue is bounded so backpressure is handled upstream.
        """
        while True:
            try:
                segment, start_ms = self._segment_queue.get(timeout=0.1)
            except queue.Empty:
                if not self._running:
                    # One more drain pass for anything that arrived
                    # between the timeout and the running flip.
                    while True:
                        try:
                            segment, start_ms = self._segment_queue.get_nowait()
                        except queue.Empty:
                            return
                        self._run_transcribe(segment, start_ms)
                continue
            self._run_transcribe(segment, start_ms)

    def _run_transcribe(self, segment: np.ndarray, start_ms: int) -> None:
        """Single transcription pass; called only by the worker thread."""
        try:
            result = self.transcriber.transcribe(segment, self.sample_rate)
            if result["text"]:
                result["start_ms"] = start_ms
                self.publisher.publish(result)
                duration_ms = int(len(segment) * 1000 / self.sample_rate)
                with self._lock:
                    self._segments_transcribed += 1
                    self._last_segment_ms = duration_ms
                # Record outside the counter lock — the histogram has its
                # own lock and we don't want a slow /status read to
                # briefly hold up transcription.
                self._timing.record(duration_ms)
        except Exception as e:
            print(f"audiod: transcribe error: {e}", flush=True)

    def _on_ptt_trigger(self):
        """Handle push-to-talk trigger. Enqueues whatever's buffered."""
        with self._lock:
            segment = self.vad.force_flush()
        if len(segment) > 0:
            self._enqueue_segment(segment, self._segment_start_ms)
        print("audiod: PTT triggered", flush=True)

    def _cmd_ptt(self) -> dict:
        """Force-flush the current VAD segment and enqueue it."""
        segment = self.vad.force_flush()
        if len(segment) == 0:
            return {"ok": True, "flushed_samples": 0, "transcribed": False}
        self._enqueue_segment(segment, self._segment_start_ms)
        return {
            "ok": True,
            "flushed_samples": int(len(segment)),
            "transcribed": True,
        }

    def _reset_counters(self) -> None:
        """Reset lifetime counters to zero.

        Called on every transition to a running state so /status
        reflects only the current lifetime — not a stale history from
        a prior /start. Guarded by the same lock that protects the
        counter reads in stats() so a concurrent /status can't observe
        a half-reset state.
        """
        with self._lock:
            self._segments_transcribed = 0
            self._dropped_segments = 0
            self._transcribe_inflight = 0
            self._last_segment_ms = 0
            self._started_at_ms = int(time.time() * 1000)
        self._timing.reset()

    def _cmd_start(self) -> dict:
        """Start the capture loop (idempotent)."""
        with self._lock:
            if self._running:
                return {"ok": True, "already_running": True}
        self._reset_counters()
        with self._lock:
            self._running = True
        self.capture.start()
        if self._ptt_trigger:
            self._ptt_trigger.start()
        self._process_thread = threading.Thread(
            target=self._process_loop, name="audiod-process", daemon=True,
        )
        self._process_thread.start()
        self._transcription_thread = threading.Thread(
            target=self._transcription_worker, name="audiod-transcribe", daemon=True,
        )
        self._transcription_thread.start()
        return {"ok": True, "started_at_ms": self._started_at_ms}

    def _cmd_stop(self) -> dict:
        """Stop the capture loop (idempotent, keeps publisher open)."""
        with self._lock:
            if not self._running:
                return {"ok": True, "already_stopped": True}
            self._running = False
        self.capture.stop()
        if self._ptt_trigger:
            self._ptt_trigger.stop()
        if self._process_thread is not None:
            self._process_thread.join(timeout=2.0)
            self._process_thread = None
        if self._transcription_thread is not None:
            # Worker exits on its own when _running flips False. Give
            # it a moment to drain whatever was already queued.
            self._transcription_thread.join(timeout=2.0)
            self._transcription_thread = None
        # Drain any straggler segments (counted as dropped since we're
        # shutting down — the operator asked us to stop).
        drained = 0
        while not self._segment_queue.empty():
            try:
                self._segment_queue.get_nowait()
                drained += 1
            except queue.Empty:
                break
        if drained:
            self._dropped_segments += drained
        return {"ok": True, "drained_on_stop": drained}

    def _cmd_restart(self) -> dict:
        """Stop, then start. Used for recovering from bad state."""
        self._cmd_stop()
        return self._cmd_start()

    def _cmd_reload(self) -> dict:
        """Reload config from disk.

        Hot-swap what we can without dropping the capture loop:
          - VAD threshold flips live.
          - Whisper model path swaps live (re-binds the binary).
        What still needs /restart: ALSA device, sample rate, channels,
        publisher mode, PTT hotkey. Those are surfaced in the response
        as `pending_restart_for` so the operator knows.
        """
        try:
            new_cfg = load_config(self._config_path)
        except Exception as e:
            return {"ok": False, "error": f"config parse error: {e}"}

        old_cfg = self.config
        self.config = new_cfg

        # VAD threshold flips live.
        if self.vad is not None and getattr(self.vad, "vad", None) is not None:
            inner = self.vad.vad
            if hasattr(inner, "threshold"):
                inner.threshold = new_cfg.get("vad", {}).get("threshold", inner.threshold)

        # Whisper model_path hot-swap.
        new_model = new_cfg.get("whisper", {}).get("model", self.transcriber.model_path)
        new_threads = new_cfg.get("whisper", {}).get("threads", self.transcriber.threads)
        new_language = new_cfg.get("whisper", {}).get("language", self.transcriber.language)
        reload_error = None
        if (new_model != self.transcriber.model_path
                or new_threads != self.transcriber.threads
                or new_language != self.transcriber.language):
            try:
                self.transcriber.reload(
                    model_path=new_model,
                    threads=new_threads,
                    language=new_language,
                )
            except Exception as e:
                # Roll back: keep the old model in place. Self-heal on
                # the next /restart.
                reload_error = f"whisper reload failed ({e}); kept previous model"
                self.config = old_cfg

        # Surface what still needs a /restart to take effect.
        pending = []
        new_audio = new_cfg.get("audio", {})
        old_audio = old_cfg.get("audio", {})
        for key in ("device", "sample_rate", "channels", "period_size", "buffer_periods"):
            if new_audio.get(key) != old_audio.get(key):
                pending.append(f"audio.{key}")
        new_pub = new_cfg.get("publish", {})
        old_pub = old_cfg.get("publish", {})
        for key in ("mode", "socket_path", "ws_port"):
            if new_pub.get(key) != old_pub.get(key):
                pending.append(f"publish.{key}")
        new_ptt = new_cfg.get("push_to_talk", {})
        old_ptt = old_cfg.get("push_to_talk", {})
        if new_ptt.get("hotkey") != old_ptt.get("hotkey"):
            pending.append("push_to_talk.hotkey")

        result = {
            "ok": reload_error is None,
            "reloaded": True,
            "whisper_model": self.transcriber.model_path,
            "whisper_threads": self.transcriber.threads,
            "whisper_language": self.transcriber.language,
            "vad_threshold": self.vad.vad.threshold if self.vad else None,
            "pending_restart_for": pending,
        }
        if reload_error:
            result["error"] = reload_error
        return result

    def is_ready(self) -> tuple[bool, dict]:
        """Aggregate readiness probe used by GET /health.

        Returns (ready: bool, breakdown: dict). The breakdown is
        surfaced in the response body of /health so operators can see
        exactly which component is not yet ready (e.g. whisper model
        file missing vs publisher listener dead).

        Readiness = VAD initialized AND whisper-cli binary resolved
        AND model file exists on disk AND publisher initialized.
        Running state is NOT part of readiness: a freshly started
        pipeline that has not yet received /start is still "ready"
        (i.e. /health returns 200 with running=false). Running only
        gates transcription throughput, not liveness.
        """
        vad_ok = self.vad is not None and self.vad.is_ready()
        whisper_ready, whisper_breakdown = self.transcriber.is_ready()
        publisher_ok, _publisher_breakdown = self.publisher.is_ready()
        breakdown = {
            "vad": vad_ok,
            "whisper_binary": whisper_breakdown.get("binary", False),
            "whisper_model": whisper_breakdown.get("model", False),
            "publisher": publisher_ok,
            "running": self._running,
        }
        return (vad_ok and whisper_ready and publisher_ok, breakdown)

    def stats(self) -> dict:
        """Return a deployment diagnostics snapshot for /status."""
        # Reuse the same per-component breakdown that powers /health so
        # operators get one source of truth for readiness across both
        # endpoints. whisper_binary distinguishes a missing CLI from a
        # missing model file, which the path strings alone don't show.
        whisper_breakdown = self.transcriber.is_ready()
        with self._lock:
            return {
                "running": self._running,
                "vad_ready": self.vad is not None and self.vad.is_ready(),
                "device": self.capture.device,
                "sample_rate": self.sample_rate,
                "channels": self.capture.channels,
                "whisper_model": self.transcriber.model_path,
                "whisper_binary": self.transcriber._bin,
                "whisper_binary_ok": whisper_breakdown[1].get("binary", False),
                "whisper_model_ok": whisper_breakdown[1].get("model", False),
                "whisper_threads": self.transcriber.threads,
                "segments_transcribed": self._segments_transcribed,
                "dropped_segments": self._dropped_segments,
                "transcribe_inflight": self._transcribe_inflight,
                "last_segment_ms": self._last_segment_ms,
                "max_segment_ms": self._max_segment_ms,
                "segment_timing": self._timing.snapshot(),
                "ptt_enabled": self._ptt_enabled,
                "ptt_hotkey": self.config.get("push_to_talk", {}).get("hotkey", "space"),
                "started_at_ms": self._started_at_ms,
                "uptime_ms": int(time.time() * 1000) - self._started_at_ms,
                "pid": os.getpid(),
                "config_path": self._config_path,
                "publisher": self.publisher.stats(),
                "queue_size": self._segment_queue.qsize(),
            }

    def _process_loop(self):
        """Main processing loop reading from capture buffer.

        Runs on its own thread so the HTTP control plane remains
        responsive. Exits when _running flips to False.
        """
        chunk_size = 512  # 32ms at 16kHz
        max_segment_samples = int(self.sample_rate * self._max_segment_ms / 1000)

        while self._running:
            chunk = self.capture.read(chunk_size)
            if len(chunk) == 0:
                continue
            self.vad.process(chunk)

            # Watchdog: if VAD has been in speech state for longer than
            # _max_segment_ms without a silence boundary, force-flush and
            # enqueue for transcription. Prevents runaway buffers from
            # a stuck VAD.
            if self.vad.is_speaking():
                held = self.vad.speech_duration_ms()
                if held > self._max_segment_ms:
                    with self._lock:
                        segment = self.vad.force_flush()
                        start_ms = self._segment_start_ms
                    if len(segment) > 0:
                        print(
                            f"audiod: force-flushing {held}ms segment "
                            f"({len(segment)} samples)",
                            flush=True,
                        )
                        self._enqueue_segment(segment, start_ms)

    def start(self):
        """Start the audio pipeline (non-blocking).

        Spawns a worker thread for the process loop and returns. Use
        stop() to halt it. The legacy CLI path used to block here; the
        HTTP control plane depends on the non-blocking behavior.
        """
        return self._cmd_start()

    def stop(self):
        """Stop the audio pipeline and close the publisher."""
        self._cmd_stop()
        self.publisher.close()


def load_config(config_path: str = "config.yaml") -> dict:
    """Load configuration from YAML file."""
    with open(config_path) as f:
        return yaml.safe_load(f)


def _build_pipeline_from_config(
    config: dict, config_path: Optional[str] = None
) -> "AudioPipeline":
    """Build an AudioPipeline from a config dict.

    Single source of truth for pipeline construction. Used by main()
    and by tests that need to build a pipeline in-process from an
    in-memory config (no config.yaml on disk).
    """
    pipeline = AudioPipeline(config, config_path=config_path)
    HealthHandler.pipeline = pipeline
    return pipeline


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
    pipeline = _build_pipeline_from_config(config, config_path=args.config)

    # Start HTTP health + control server
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

    # Block main thread on a signal-driven event. The HTTP health server
    # runs in a daemon thread, so main must stay alive or the process
    # exits and the daemon dies with it.
    _shutdown_event = threading.Event()
    def _signal_shutdown(sig, frame):
        print(f"\naudiod: received signal {sig}, stopping", flush=True)
        _shutdown_event.set()
    signal.signal(signal.SIGINT, _signal_shutdown)
    signal.signal(signal.SIGTERM, _signal_shutdown)
    _shutdown_event.wait()
    pipeline.stop()
    sys.exit(0)


if __name__ == "__main__":
    main()