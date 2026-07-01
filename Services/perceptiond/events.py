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
                    else:
                        self._send_json(404, {"error": "not found", "path": path})
                except Exception as e:
                    try:
                        self._send_json(500, {"error": str(e)})
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
