"""Event publishing via stdout and HTTP ring buffer.

DescriptionPublisher: thread-safe, fixed-capacity ring buffer + stdout.
PerceptiondServer: HTTP API on TCP 8092 + Unix socket, with /descriptions GET.
"""

import json
import socket
import os
import threading
import http.server
import socketserver
import time
import uuid
from collections import deque
from typing import Optional, List, Deque


RING_BUFFER_SIZE = 200  # max descriptions held in memory
FRAME_BUFFER_SIZE = 50   # max per-event JPEGs (thumbnails) kept for /frames/<id>.jpg

# v7.0 — SSE /events pub-sub
EVENT_BUS_REPLAY = 20         # last N descriptions replayed to a new subscriber
EVENT_BUS_PER_SUBSCRIBER = 64 # per-subscriber bounded queue (overwrite-on-full)


class EventBus:
    """In-process pub/sub for live description streaming.

    Each subscriber gets a private bounded deque. On attach, the bus replays
    the last N events from the publisher's ring buffer so the new client
    renders history immediately. New events from `publish()` are fanned out
    synchronously under a short lock; if a subscriber's queue is full, the
    oldest entry is dropped to keep the publisher's hot path non-blocking.
    """

    def __init__(self, replay: int = EVENT_BUS_REPLAY, per_subscriber_cap: int = EVENT_BUS_PER_SUBSCRIBER):
        self._lock = threading.Lock()
        self._subscribers: List[deque] = []
        self._replay = max(0, replay)
        self._per_subscriber_cap = max(1, per_subscriber_cap)

    def attach(self, ring) -> tuple:
        """Register a new subscriber; return (queue, replay_count)."""
        q: Deque[dict] = deque(maxlen=self._per_subscriber_cap)
        with self._lock:
            self._subscribers.append(q)
            replay_items = list(ring)[-self._replay:]
        for item in replay_items:
            q.append(item)
        return q, len(replay_items)

    def detach(self, q) -> None:
        with self._lock:
            try:
                self._subscribers.remove(q)
            except ValueError:
                pass

    def publish(self, event: dict) -> None:
        """Fan out an event to every live subscriber; non-blocking."""
        with self._lock:
            subs = list(self._subscribers)
        for q in subs:
            # Bounded queue drops oldest when full, so we never block here.
            q.append(dict(event))

    def subscriber_count(self) -> int:
        with self._lock:
            return len(self._subscribers)


class FrameStore:
    """Thread-safe ring buffer of per-event JPEG bytes keyed by image_id.

    Bounded by FRAME_BUFFER_SIZE (insertion-ordered; oldest evicted first).
    Used to back GET /frames/<image_id>.jpg so the UI can show what the VLM saw.
    """

    def __init__(self, capacity: int = FRAME_BUFFER_SIZE):
        self._capacity = capacity
        self._lock = threading.Lock()
        # Python 3.7+ dict preserves insertion order - used as ordered map.
        self._frames = {}

    def put(self, image_id: str, jpeg: bytes) -> None:
        """Store a JPEG under image_id; evict oldest if over capacity.

        Validates JPEG SOI marker (0xFFD8) so consumers can trust GET output.
        Rejects empty image_id, None bytes, and non-JPEG payloads.
        """
        if not image_id or jpeg is None or len(jpeg) < 2 or jpeg[:2] != b"\xff\xd8":
            return
        with self._lock:
            # If image_id already present, remove first to re-insert at tail.
            self._frames.pop(image_id, None)
            self._frames[image_id] = jpeg
            while len(self._frames) > self._capacity:
                # FIFO eviction: pop oldest inserted key.
                # Note: dict.popitem() has no `last` kwarg (that's OrderedDict).
                oldest = next(iter(self._frames))
                self._frames.pop(oldest, None)

    def get(self, image_id: str):
        """Return JPEG bytes for image_id or None."""
        with self._lock:
            return self._frames.get(image_id)

    def __len__(self) -> int:
        with self._lock:
            return len(self._frames)

    def clear(self) -> None:
        with self._lock:
            self._frames.clear()


class DescriptionPublisher:
    """Publish description events to stdout AND a thread-safe ring buffer."""

    def __init__(
        self,
        mode: str = "stdout",
        socket_path: str = "/var/run/perceptiond.sock",
        ring_size: int = RING_BUFFER_SIZE,
    ):
        self.mode = mode
        self.socket_path = socket_path
        self._sock: Optional[socket.socket] = None
        self._event_count = 0
        self._lock = threading.Lock()
        self._ring: Deque[dict] = deque(maxlen=ring_size)
        # v7.0: in-process pub/sub for the /events SSE stream
        self.event_bus = EventBus()

        if mode == "socket":
            self._setup_socket()

    def _setup_socket(self):
        """Create Unix socket server."""
        if os.path.exists(self.socket_path):
            os.unlink(self.socket_path)
        self._sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind(self.socket_path)
        self._sock.listen(1)

    def publish(self, event: dict):
        """Publish a description event (stdout + ring buffer)."""
        with self._lock:
            self._event_count += 1
            event["event_id"] = self._event_count
            if "timestamp" not in event:
                event["timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            if "image_id" not in event:
                event["image_id"] = uuid.uuid4().hex[:8]
            self._ring.append(dict(event))  # copy to prevent aliasing

        line = json.dumps(event) + "\n"

        if self.mode in ("stdout", "both"):
            print(line, flush=True)

        if self.mode == "socket" and self._sock:
            try:
                conn, _ = self._sock.accept()
                conn.sendall(line.encode())
                conn.close()
            except Exception:
                pass

    def recent(self, count: int = 10) -> List[dict]:
        """Return last N descriptions (oldest first)."""
        with self._lock:
            n = max(0, min(count, len(self._ring)))
            return list(self._ring)[-n:]

    def clear(self):
        """Clear the ring buffer."""
        with self._lock:
            self._ring.clear()

    def __len__(self) -> int:
        with self._lock:
            return len(self._ring)

    def close(self):
        """Close socket."""
        if self._sock:
            self._sock.close()
            self._sock = None
            if os.path.exists(self.socket_path):
                try:
                    os.unlink(self.socket_path)
                except Exception:
                    pass


class PerceptiondServer:
    """HTTP server for perceptiond API on TCP 8092 (and Unix socket)."""

    def __init__(self, socket_path: str = "/var/run/perceptiond.sock", tcp_port: int = 8092):
        self.socket_path = socket_path
        self.tcp_port = tcp_port
        self._unix_sock: Optional[socket.socket] = None
        self._tcp_server: Optional[socketserver.TCPServer] = None
        self._thread_unix: Optional[threading.Thread] = None
        self._thread_tcp: Optional[threading.Thread] = None
        self._running = False
        self._pipeline = None

    def set_pipeline(self, pipeline):
        """Set pipeline reference for status queries."""
        self._pipeline = pipeline
        if self._tcp_server and hasattr(self._tcp_server, "pipeline"):
            self._tcp_server.pipeline = pipeline

    def set_capture(self, capture):
        """Set capture reference for /stream and /frame.jpg endpoints."""
        self._capture = capture
        if self._tcp_server is not None:
            self._tcp_server.capture = capture
        else:
            # TCP thread not started yet — will be wired in _serve_tcp
            self._pending_capture = capture

    def set_frame_store(self, frame_store):
        """Set FrameStore reference for /frames/<image_id>.jpg endpoint."""
        self._frame_store = frame_store
        if self._tcp_server is not None:
            self._tcp_server.frame_store = frame_store
        else:
            self._pending_frame_store = frame_store

    def _resolve_frame_store(self):
        """Return FrameStore from server, falling back to pending."""
        fs = getattr(self, "_frame_store", None)
        if fs is not None:
            return fs
        return getattr(self, "_pending_frame_store", None)

    def start(self):
        """Start HTTP servers."""
        self._running = True
        self._thread_unix = threading.Thread(target=self._serve_unix, daemon=True)
        self._thread_unix.start()
        self._thread_tcp = threading.Thread(target=self._serve_tcp, daemon=True)
        self._thread_tcp.start()

    def _serve_tcp(self):
        """Serve HTTP on TCP port."""
        class ReuseAddrTCPServer(socketserver.TCPServer):
            allow_reuse_address = True
            daemon_threads = True

        class HTTPHandler(http.server.BaseHTTPRequestHandler):
            server: socketserver.TCPServer

            def _send_json(self, code: int, body: dict):
                data = json.dumps(body).encode()
                self.send_response(code)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(data)

            def _parse_query(self, path: str) -> dict:
                if "?" not in path:
                    return {}
                from urllib.parse import parse_qs, urlparse
                qs = parse_qs(urlparse(path).query)
                return {k: v[0] for k, v in qs.items() if v}

            def do_GET(self):
                try:
                    path = self.path.split("?")[0]
                    qs = self._parse_query(self.path)
                    if path == "/health":
                        self._send_json(200, {"status": "ok"})
                    elif path == "/frame.jpg":
                        capture = getattr(self.server, "capture", None)
                        if capture is None:
                            server_obj = getattr(self.server, "_server_ref", None)
                            if server_obj is not None:
                                capture = getattr(server_obj, "_capture", None) or getattr(server_obj, "_pending_capture", None)
                        if capture is None:
                            self._send_json(503, {"error": "no capture"})
                        else:
                            jpeg, ts, w, h = capture.get_latest_jpeg()
                            if jpeg is None:
                                self._send_json(503, {"error": "no frame yet"})
                            else:
                                self.send_response(200)
                                self.send_header("Content-Type", "image/jpeg")
                                self.send_header("Content-Length", str(len(jpeg)))
                                self.send_header("Cache-Control", "no-store")
                                self.send_header("X-Frame-Width", str(w))
                                self.send_header("X-Frame-Height", str(h))
                                self.send_header("X-Frame-Timestamp", str(ts))
                                self.send_header("Access-Control-Allow-Origin", "*")
                                self.end_headers()
                                self.wfile.write(jpeg)
                    elif path.startswith("/frames/") and path.endswith(".jpg"):
                        # /frames/<image_id>.jpg - per-event thumbnail
                        image_id = path[len("/frames/"):-len(".jpg")]
                        if not image_id or not all(c in "0123456789abcdef" for c in image_id):
                            self._send_json(400, {"error": "invalid image_id"})
                        else:
                            frame_store = getattr(self.server, "frame_store", None)
                            if frame_store is None:
                                server_obj = getattr(self.server, "_server_ref", None)
                                if server_obj is not None:
                                    frame_store = server_obj._resolve_frame_store()
                            if frame_store is None:
                                self._send_json(503, {"error": "no frame store"})
                            else:
                                jpeg = frame_store.get(image_id)
                                if jpeg is None:
                                    self._send_json(404, {"error": "frame not found", "image_id": image_id})
                                else:
                                    self.send_response(200)
                                    self.send_header("Content-Type", "image/jpeg")
                                    self.send_header("Content-Length", str(len(jpeg)))
                                    self.send_header("Cache-Control", "public, max-age=3600")
                                    self.send_header("Access-Control-Allow-Origin", "*")
                                    self.end_headers()
                                    self.wfile.write(jpeg)
                    elif path == "/stream":
                        self._serve_mjpeg_stream()
                    elif path == "/status":
                        pipeline = getattr(self.server, "pipeline", None)
                        if pipeline is None:
                            server_obj = getattr(self.server, "_server_ref", None)
                            if server_obj is not None:
                                pipeline = getattr(server_obj, "_pipeline", None)
                        if pipeline:
                            self._send_json(200, pipeline.get_status())
                        else:
                            self._send_json(503, {"status": "initializing"})
                    elif path == "/descriptions":
                        pipeline = getattr(self.server, "pipeline", None)
                        if pipeline is None:
                            server_obj = getattr(self.server, "_server_ref", None)
                            if server_obj is not None:
                                pipeline = getattr(server_obj, "_pipeline", None)
                        count = int(qs.get("count", "20"))
                        if pipeline and pipeline.publisher:
                            items = pipeline.publisher.recent(count)
                            self._send_json(200, {
                                "count": len(items),
                                "descriptions": items,
                            })
                        else:
                            self._send_json(200, {"count": 0, "descriptions": []})
                    elif path == "/events":
                        # v7.0: Server-Sent Events stream of new descriptions.
                        self._serve_sse_stream()
                    elif path == "/stats":
                        # v7.0: Cumulative telemetry summary. Delegates to
                        # pipeline.get_detailed_status() so /stats always
                        # stays in lockstep with /status fields.
                        pipeline = getattr(self.server, "pipeline", None)
                        if pipeline is None:
                            server_obj = getattr(self.server, "_server_ref", None)
                            if server_obj is not None:
                                pipeline = getattr(server_obj, "_pipeline", None)
                        if pipeline is None:
                            self._send_json(503, {"error": "no pipeline"})
                        else:
                            # Prefer get_detailed_status() for full v7.0
                            # telemetry; fall back to get_status() for mocks
                            # and older pipelines. CRITICAL: call the method
                            # to get the dict — get_detailed_status exists
                            # on the live pipeline but the bound method is
                            # not callable via .get() and would 500.
                            st_getter = getattr(pipeline, "get_detailed_status", None) or pipeline.get_status
                            st = st_getter()
                            frames = st.get("frames_processed", 0)
                            salient = st.get("salient_frames", 0)
                            descs = st.get("descriptions", 0)
                            vlm_invoc = st.get("vlm_invocations", 0)
                            scene_skips = st.get("scene_skips", 0)
                            publisher = getattr(pipeline, "publisher", None)
                            ring_size = len(publisher) if publisher is not None else 0
                            self._send_json(200, {
                                "frames_processed": frames,
                                "salient_frames": salient,
                                "descriptions": descs,
                                "vlm_invocations": vlm_invoc,
                                "scene_skips": scene_skips,
                                "scene_threshold": st.get("scene_threshold", 0.02),
                                "motion_score": st.get("motion_score", 0.0),
                                "face_count": st.get("face_count", 0),
                                "last_trigger_kind": st.get("last_trigger_kind", "none"),
                                "deduped_count": st.get("deduped_count", 0),
                                "dedup_skip_count": st.get("dedup_skip_count", 0),
                                "vlm_busy": st.get("vlm_busy", False),
                                "vlm_queue_depth": st.get("vlm_queue_depth", 0),
                                "scene_gate": st.get("scene_gate", {}),
                                "sse_subscribers": st.get("sse_subscribers", 0),
                                "salience_ratio": (salient / frames) if frames > 0 else 0.0,
                                "vlm_pass_rate": (vlm_invoc / frames) if frames > 0 else 0.0,
                                "skip_rate": (scene_skips / salient) if salient > 0 else 0.0,
                                "ring_buffer_size": ring_size,
                                "ring_buffer_cap": RING_BUFFER_SIZE,
                            })
                    else:
                        self._send_json(404, {"error": "not found", "path": path})
                except Exception as e:
                    try:
                        self._send_json(500, {"error": str(e)})
                    except Exception:
                        pass

            def _serve_stats_summary(self):
                """v7.0 — aggregate stats snapshot for dashboards / healthchecks."""
                pipeline = getattr(self.server, "pipeline", None)
                if pipeline is None:
                    server_obj = getattr(self.server, "_server_ref", None)
                    if server_obj is not None:
                        pipeline = getattr(server_obj, "_pipeline", None)
                if pipeline is None:
                    self._send_json(503, {"error": "no pipeline"})
                    return
                st = pipeline.get_status()
                subs = 0
                try:
                    subs = pipeline.publisher.event_bus.subscriber_count()
                except Exception:
                    pass
                vlm_invoc = st.get("vlm_invocations", 0)
                frames = st.get("frames_processed", 0)
                descs = st.get("descriptions", 0)
                scene_skips = st.get("scene_skips", 0)
                self._send_json(200, {
                    "mode": st.get("mode"),
                    "running": st.get("running"),
                    "frames": frames,
                    "salient": st.get("salient_frames", 0),
                    "descriptions": descs,
                    "vlm_invocations": vlm_invoc,
                    "vlm_skip_rate": (
                        1.0 - (vlm_invoc / max(1, frames)) if frames else 0.0
                    ),
                    "scene_skips": scene_skips,
                    "vlm_busy": st.get("vlm_busy", False),
                    "vlm_queue_depth": st.get("vlm_queue_depth", 0),
                    "scene_gate": st.get("scene_gate", {}),
                    "sse_subscribers": subs,
                    "ring_buffer_size": RING_BUFFER_SIZE,
                })

            def _serve_sse_stream(self):
                """v7.0 — Server-Sent Events stream of new descriptions.

                On subscribe, replays the last N descriptions so the client
                renders history immediately. Then streams new events as they
                arrive, one per `data:` frame, until the client disconnects.
                Heartbeat `:` comments every 15s keep proxies from killing
                the idle connection.
                """
                pipeline = getattr(self.server, "pipeline", None)
                if pipeline is None:
                    server_obj = getattr(self.server, "_server_ref", None)
                    if server_obj is not None:
                        pipeline = getattr(server_obj, "_pipeline", None)
                if pipeline is None or not pipeline.publisher:
                    self._send_json(503, {"error": "no pipeline"})
                    return
                pub = pipeline.publisher
                # attach() returns (queue, replay_count). The queue is
                # pre-populated with the last N ring-buffer events; the
                # count is informational. We use the SAME queue for both
                # the replay and the live stream — new events are appended
                # to it by publish() via the EventBus fan-out.
                my_q, replay_n = pub.event_bus.attach(pub._ring)
                # Track for cleanup. List of (handler, queue) tuples so
                # multiple concurrent SSE clients can coexist.
                if not hasattr(self.server, "_sse_subscriber_queues"):
                    self.server._sse_subscriber_queues = []
                self.server._sse_subscriber_queues.append((self, my_q))
                try:
                    self.send_response(200)
                    self.send_header("Content-Type", "text/event-stream")
                    self.send_header("Cache-Control", "no-store")
                    self.send_header("Connection", "close")
                    self.send_header("X-Accel-Buffering", "no")
                    self.send_header("Access-Control-Allow-Origin", "*")
                    self.end_headers()
                    # Drain replay: items already on my_q from attach().
                    # Emit `event: description\nid: <id>\ndata: <json>\n\n`.
                    sent_ids = set()
                    while my_q:
                        item = my_q.popleft()
                        eid = item.get("event_id", 0)
                        if eid and eid in sent_ids:
                            continue
                        if eid:
                            sent_ids.add(eid)
                        payload = json.dumps(item)
                        block = f"event: description\nid: {eid}\ndata: {payload}\n\n".encode("utf-8")
                        self.wfile.write(block)
                        self.wfile.flush()
                    last_seen_id = max(sent_ids) if sent_ids else 0
                    last_heartbeat = time.time()
                    while True:
                        # Drain any new items on the live queue
                        while my_q:
                            item = my_q.popleft()
                            eid = item.get("event_id", 0)
                            if eid and eid == last_seen_id:
                                continue
                            if eid:
                                last_seen_id = eid
                            payload = json.dumps(item)
                            block = f"event: description\nid: {eid}\ndata: {payload}\n\n".encode("utf-8")
                            self.wfile.write(block)
                            self.wfile.flush()
                        # Heartbeat
                        now = time.time()
                        if now - last_heartbeat > 15.0:
                            self.wfile.write(b": ping\n\n")
                            self.wfile.flush()
                            last_heartbeat = now
                        time.sleep(0.25)
                except (BrokenPipeError, ConnectionResetError):
                    return
                except Exception:
                    return
                finally:
                    try:
                        pub.event_bus.detach(my_q)
                    except Exception:
                        pass
                    try:
                        self.server._sse_subscriber_queues.remove((self, my_q))
                    except Exception:
                        pass

            def _serve_mjpeg_stream(self):
                """Serve a multipart/x-mixed-replace MJPEG stream of the latest frame."""
                capture = getattr(self.server, "capture", None)
                if capture is None:
                    server_obj = getattr(self.server, "_server_ref", None)
                    if server_obj is not None:
                        capture = getattr(server_obj, "_capture", None) or getattr(server_obj, "_pending_capture", None)
                if capture is None:
                    self._send_json(503, {"error": "no capture"})
                    return
                pipeline = getattr(self.server, "pipeline", None)
                fps = 5
                if pipeline is not None and hasattr(pipeline, "capture"):
                    try:
                        fps = max(1, int(getattr(pipeline.capture, "fps", 5)))
                    except Exception:
                        fps = 5
                frame_interval = 1.0 / fps
                boundary = "danvision"
                self.send_response(200)
                self.send_header("Content-Type", f"multipart/x-mixed-replace; boundary={boundary}")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Connection", "close")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                last_ts = 0.0
                try:
                    while True:
                        jpeg, ts, w, h = capture.get_latest_jpeg()
                        if jpeg is None or ts == last_ts:
                            time.sleep(frame_interval)
                            continue
                        last_ts = ts
                        header = (
                            f"--{boundary}\r\n"
                            f"Content-Type: image/jpeg\r\n"
                            f"Content-Length: {len(jpeg)}\r\n"
                            f"X-Frame-Timestamp: {ts:.3f}\r\n"
                            f"X-Frame-Width: {w}\r\n"
                            f"X-Frame-Height: {h}\r\n"
                            f"\r\n"
                        ).encode("ascii")
                        self.wfile.write(header)
                        self.wfile.write(jpeg)
                        self.wfile.write(b"\r\n")
                        self.wfile.flush()
                        time.sleep(frame_interval)
                except (BrokenPipeError, ConnectionResetError):
                    return
                except Exception:
                    return

            def do_POST(self):
                try:
                    path = self.path.split("?")[0]
                    if path == "/mode":
                        length = int(self.headers.get("Content-Length", 0))
                        raw = self.rfile.read(length).decode("utf-8", errors="ignore")
                        try:
                            data = json.loads(raw) if raw else {}
                        except Exception:
                            data = {}
                        mode = data.get("mode", "")
                        valid = mode in ("idle", "watchful", "active")
                        pipeline = getattr(self.server, "pipeline", None)
                        if valid and pipeline:
                            pipeline.set_mode(mode)
                            self._send_json(200, {"status": "ok", "mode": mode})
                        else:
                            self._send_json(400, {"status": "error", "reason": "invalid mode"})
                    else:
                        self._send_json(404, {"error": "not found", "path": path})
                except Exception as e:
                    try:
                        self._send_json(500, {"error": str(e)})
                    except Exception:
                        pass

            def log_message(self, format, *args):
                pass

        try:
            self._tcp_server = ReuseAddrTCPServer(("0.0.0.0", self.tcp_port), HTTPHandler)
            # Wire back-references so HTTP handlers can find parent server state
            self._tcp_server._server_ref = self
            self._tcp_server.pipeline = self._pipeline
            self._tcp_server.capture = getattr(self, "_capture", None) or getattr(self, "_pending_capture", None)
            self._tcp_server.frame_store = getattr(self, "_frame_store", None) or getattr(self, "_pending_frame_store", None)
            self._tcp_server.serve_forever()
        except Exception as e:
            print(f"perceptiond: TCP server error: {e}", flush=True)

    def _serve_unix(self):
        """Serve HTTP on Unix socket (subset of TCP API)."""
        if os.path.exists(self.socket_path):
            os.unlink(self.socket_path)
        self._unix_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._unix_sock.bind(self.socket_path)
        self._unix_sock.listen(1)

        while self._running:
            try:
                conn, _ = self._unix_sock.accept()
                self._handle_unix(conn)
                conn.close()
            except Exception:
                if self._running:
                    continue
                break

    def _handle_unix(self, conn):
        try:
            req = conn.recv(4096)
            if not req:
                return
            lines = req.decode("utf-8", errors="ignore").split("\r\n")
            if not lines:
                return
            parts = lines[0].split(" ")
            if len(parts) < 2:
                return
            method, path = parts[0], parts[1].split("?")[0]
            if path == "/health" and method == "GET":
                body = b'{"status":"ok"}'
                response = (b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: "
                            + str(len(body)).encode() + b"\r\n\r\n" + body)
            elif path == "/descriptions" and method == "GET":
                if self._pipeline and self._pipeline.publisher:
                    items = self._pipeline.publisher.recent(20)
                    payload = json.dumps({"count": len(items), "descriptions": items}).encode()
                else:
                    payload = b'{"count":0,"descriptions":[]}'
                response = (b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: "
                            + str(len(payload)).encode() + b"\r\n\r\n" + payload)
            else:
                response = b"HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n"
            conn.sendall(response)
        except Exception:
            pass

    def stop(self):
        self._running = False
        if self._tcp_server:
            self._tcp_server.shutdown()
            self._tcp_server = None
        if self._unix_sock:
            try:
                self._unix_sock.close()
            except Exception:
                pass
            self._unix_sock = None
        if os.path.exists(self.socket_path):
            try:
                os.unlink(self.socket_path)
            except Exception:
                pass


def publish_description(image_id: str, timestamp: str, description: str, confidence: float = 1.0):
    """Convenience function to publish a description event to stdout."""
    event = {
        "type": "description",
        "image_id": image_id,
        "timestamp": timestamp,
        "description": description,
        "confidence": confidence,
    }
    print(json.dumps(event), flush=True)