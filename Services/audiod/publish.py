"""Publish transcription events to stdout, Unix socket, or WebSocket.

Implements RFC 6455 WebSocket (server side) so browsers can connect.
Server-side framing is required for client compatibility; browsers
will not parse raw JSON bytes as WebSocket messages.
"""

import base64
import hashlib
import json
import os
import socket
import struct
import sys
import threading
import time
import uuid
from collections import deque
from typing import Optional


WS_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"


# Lazy singleton used by publish_transcript() so ad-hoc one-liners emit
# the full transcript event schema (type, session_id, event_id, seq,
# text, start_ms, end_ms, confidence, ts_ms) instead of a partial one.
_stdout_publisher: Optional["TranscriptPublisher"] = None


def _accept_key(client_key: str) -> str:
    """Compute Sec-WebSocket-Accept from client's Sec-WebSocket-Key (RFC 6455 §4.2.2)."""
    digest = hashlib.sha1((client_key + WS_GUID).encode("ascii")).digest()
    return base64.b64encode(digest).decode("ascii")


def _frame(opcode: int, payload: bytes, mask: bool = False) -> bytes:
    """Build a single WebSocket frame. Server→client must NOT be masked."""
    if opcode < 0 or opcode > 0xF:
        raise ValueError(f"bad opcode: {opcode}")
    header = bytearray()
    header.append(0x80 | opcode)  # FIN=1

    length = len(payload)
    if mask:
        if length < 126:
            header.append(0x80 | length)
        elif length <= 0xFFFF:
            header.append(0x80 | 126)
            header.extend(struct.pack(">H", length))
        elif length <= 0x7FFFFFFFFFFFFFFF:
            header.append(0x80 | 127)
            header.extend(struct.pack(">Q", length))
        else:
            raise ValueError(f"payload too large: {length}")
        mask_key = os.urandom(4)
        header.extend(mask_key)
        payload = bytes(b ^ mask_key[i & 3] for i, b in enumerate(payload))
    else:
        if length < 126:
            header.append(length)
        elif length <= 0xFFFF:
            header.append(126)
            header.extend(struct.pack(">H", length))
        elif length <= 0x7FFFFFFFFFFFFFFF:
            header.append(127)
            header.extend(struct.pack(">Q", length))
        else:
            raise ValueError(f"payload too large: {length}")

    return bytes(header) + payload


def frame_text(payload: bytes) -> bytes:
    """Wrap a payload as a single unfragmented WebSocket text frame (server→client)."""
    return _frame(0x1, payload, mask=False)


def _parse_client_frame(data: bytes) -> Optional[tuple[bytes, int, int]]:
    """Parse a single client→server frame. Returns (payload, opcode, frame_size) or None.

    Client frames MUST be masked (RFC 6455 §5.1).
    """
    if len(data) < 2:
        return None
    b1, b2 = data[0], data[1]
    fin = bool(b1 & 0x80)
    opcode = b1 & 0x0F
    masked = bool(b2 & 0x80)
    length = b2 & 0x7F

    idx = 2
    if length == 126:
        if len(data) < idx + 2:
            return None
        length = struct.unpack(">H", data[idx:idx + 2])[0]
        idx += 2
    elif length == 127:
        if len(data) < idx + 8:
            return None
        length = struct.unpack(">Q", data[idx:idx + 8])[0]
        idx += 8

    if not masked:
        # Protocol violation; reject by closing
        return None
    if len(data) < idx + 4:
        return None
    mask = data[idx:idx + 4]
    idx += 4

    if len(data) < idx + length:
        return None

    payload = data[idx:idx + length]
    payload = bytes(b ^ mask[i & 3] for i, b in enumerate(payload))
    return payload, opcode, idx + length


def _pong(payload: bytes) -> bytes:
    """Build a pong frame echoing the client's ping payload (RFC 6455 §5.5.3)."""
    return _frame(0xA, payload, mask=False)


def _close(code: int = 1000, reason: str = "") -> bytes:
    """Build a close frame."""
    body = struct.pack(">H", code) + reason.encode("utf-8")
    return _frame(0x8, body, mask=False)


class _WSClient:
    """A single connected WebSocket client with its own send queue (no head-of-line blocking)."""

    def __init__(self, sock: socket.socket, addr, on_close):
        self.sock = sock
        self.addr = addr
        self._on_close = on_close
        self._queue: deque[bytes] = deque(maxlen=512)
        self._lock = threading.Lock()
        self._closed = False
        self._send_thread = threading.Thread(target=self._send_loop, daemon=True)
        self._send_thread.start()

    def enqueue(self, framed: bytes) -> bool:
        """Enqueue a fully-framed message. Returns False if dropped (queue full / closed)."""
        with self._lock:
            if self._closed:
                return False
            if len(self._queue) == self._queue.maxlen:
                return False
            self._queue.append(framed)
            return True

    def close(self):
        with self._lock:
            if self._closed:
                return
            self._closed = True
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        try:
            self.sock.close()
        except OSError:
            pass
        self._on_close(self)

    def _send_loop(self):
        while True:
            with self._lock:
                if self._closed:
                    return
                if not self._queue:
                    frame = None
                else:
                    frame = self._queue.popleft()
            if frame is None:
                time.sleep(0.005)
                continue
            try:
                self.sock.sendall(frame)
            except OSError:
                self.close()
                return


class TranscriptPublisher:
    """Publish transcript events to stdout, Unix socket, and WebSocket clients.

    Event format (all transports):
        {
            "type": "transcript",
            "session_id": "uuid",
            "event_id": "uuid",
            "seq": 42,
            "text": "what was said",
            "start_ms": 1234,
            "end_ms": 5678,
            "confidence": 0.92,
            "ts_ms": 1730000000000
        }
    """

    def __init__(
        self,
        mode: str = "stdout",
        socket_path: str = "/run/audiod.sock",
        ws_port: int = 8091,
    ):
        self.mode = mode
        self.socket_path = socket_path
        self.ws_port = ws_port
        self._sock: Optional[socket.socket] = None
        self._ws_clients: list[_WSClient] = []
        self._ws_lock = threading.Lock()
        self._ws_server: Optional[threading.Thread] = None
        self._session_id = str(uuid.uuid4())
        self._seq = 0
        self._seq_lock = threading.Lock()

        if mode in ("socket", "both"):
            self._setup_socket()

        if mode in ("websocket", "both"):
            self._start_ws_server()

    def _next_seq(self) -> int:
        with self._seq_lock:
            self._seq += 1
            return self._seq

    def _enrich(self, event: dict) -> dict:
        """Attach session_id, event_id, seq, ts_ms to an event."""
        if "session_id" not in event:
            event["session_id"] = self._session_id
        if "event_id" not in event:
            event["event_id"] = str(uuid.uuid4())
        if "seq" not in event:
            event["seq"] = self._next_seq()
        if "ts_ms" not in event:
            event["ts_ms"] = int(time.time() * 1000)
        return event

    def _start_ws_server(self):
        """Start WebSocket server thread for frontend streaming."""

        def ws_loop():
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                server.bind(("127.0.0.1", self.ws_port))
                server.listen(8)
                server.settimeout(1.0)
                if self.ws_port == 0:
                    self.ws_port = server.getsockname()[1]
            except OSError as e:
                print(f"audiod: ws bind failed: {e}", flush=True)
                return

            while getattr(self, "_running", True):
                try:
                    client_sock, addr = server.accept()
                except socket.timeout:
                    continue
                except OSError:
                    break
                threading.Thread(
                    target=self._ws_handshake_and_serve,
                    args=(client_sock, addr),
                    daemon=True,
                ).start()

        self._running = True
        self._ws_server = threading.Thread(target=ws_loop, daemon=True)
        self._ws_server.start()

    def _ws_handshake_and_serve(self, client_sock: socket.socket, addr):
        """Perform RFC 6455 handshake and then serve frames from the client."""
        client_sock.settimeout(5.0)
        try:
            header = b""
            while b"\r\n\r\n" not in header:
                chunk = client_sock.recv(1024)
                if not chunk:
                    client_sock.close()
                    return
                header += chunk
                if len(header) > 16384:
                    client_sock.close()
                    return

            header_text = header.decode("latin-1", errors="replace")
            headers = _parse_headers(header_text)

            if "websocket" not in headers.get("upgrade", "").lower():
                _send_http_error(client_sock, 400, "Expected WebSocket Upgrade")
                return
            client_key = headers.get("sec-websocket-key")
            if not client_key:
                _send_http_error(client_sock, 400, "Missing Sec-WebSocket-Key")
                return

            accept = _accept_key(client_key)
            response = (
                "HTTP/1.1 101 Switching Protocols\r\n"
                "Upgrade: websocket\r\n"
                "Connection: Upgrade\r\n"
                f"Sec-WebSocket-Accept: {accept}\r\n"
                "\r\n"
            )
            client_sock.sendall(response.encode("ascii"))

            leftover = header.split(b"\r\n\r\n", 1)[1]
        except OSError:
            try:
                client_sock.close()
            except OSError:
                pass
            return

        ws_client = _WSClient(client_sock, addr, self._remove_client)
        with self._ws_lock:
            self._ws_clients.append(ws_client)

        # Read loop: parse client frames, respond to pings, drop close
        buf = leftover or b""
        client_sock.settimeout(60.0)
        while not ws_client._closed:
            try:
                chunk = client_sock.recv(4096)
            except OSError:
                break
            if not chunk:
                break
            buf += chunk
            # Parse all complete frames
            while True:
                parsed = _parse_client_frame(buf)
                if parsed is None:
                    break
                payload, opcode, frame_size = parsed
                buf = buf[frame_size:]
                if opcode == 0x8:  # close
                    try:
                        client_sock.sendall(_close(1000, ""))
                    except OSError:
                        pass
                    ws_client.close()
                    return
                elif opcode == 0x9:  # ping
                    try:
                        client_sock.sendall(_pong(payload))
                    except OSError:
                        ws_client.close()
                        return
                # opcode 0x1 (text) / 0x2 (binary) / 0xA (pong): ignored for now

        ws_client.close()

    def _remove_client(self, ws_client: _WSClient):
        with self._ws_lock:
            try:
                self._ws_clients.remove(ws_client)
            except ValueError:
                pass

    def _setup_socket(self):
        """Create Unix socket server."""
        if os.path.exists(self.socket_path):
            os.unlink(self.socket_path)
        self._sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind(self.socket_path)
        self._sock.listen(1)

    def publish(self, event: dict):
        """Publish a transcript event to all configured outputs."""
        event = self._enrich(dict(event))
        line = json.dumps(event) + "\n"
        raw = line.encode("utf-8")

        if self.mode in ("stdout", "both"):
            sys.stdout.write(line)
            sys.stdout.flush()

        if self.mode in ("socket", "both") and self._sock:
            try:
                conn, _ = self._sock.accept()
                conn.sendall(raw)
                conn.close()
            except (BlockingIOError, OSError):
                pass

        if self._ws_clients:
            framed = frame_text(raw.rstrip(b"\n"))
            with self._ws_lock:
                clients = list(self._ws_clients)
            for c in clients:
                if not c.enqueue(framed):
                    c.close()  # backpressure: drop slow client

    def stats(self) -> dict:
        with self._ws_lock:
            n_clients = len(self._ws_clients)
        return {
            "session_id": self._session_id,
            "seq": self._seq,
            "ws_clients": n_clients,
            "mode": self.mode,
            "ws_port": self.ws_port,
        }

    def is_ready(self) -> tuple[bool, dict]:
        """Liveness probe for /health.

        Returns (ready, breakdown) where ready is True iff the
        configured transport(s) are initialized and the WS listener
        thread is alive (for ws modes). For pure-stdout mode the
        publisher is always ready: stdout has no listener state to
        fail. For socket modes the unix listener must be bound. For
        websocket modes the dedicated thread must be alive.
        """
        mode = self.mode
        stdout_ok = mode in ("stdout", "both")
        socket_ok = True
        ws_ok = True
        if mode in ("socket", "both"):
            socket_ok = self._sock is not None
        if mode in ("websocket", "both", "ws"):
            ws_ok = (self._ws_server is not None) and self._ws_server.is_alive()
        ready = stdout_ok and socket_ok and ws_ok
        return (ready, {
            "mode": mode,
            "stdout": stdout_ok,
            "socket": socket_ok,
            "websocket": ws_ok,
        })

    def close(self):
        """Close all publishing channels."""
        self._running = False
        if self._sock:
            try:
                self._sock.close()
            except OSError:
                pass
            self._sock = None
            if os.path.exists(self.socket_path):
                try:
                    os.unlink(self.socket_path)
                except OSError:
                    pass
        with self._ws_lock:
            clients = list(self._ws_clients)
            self._ws_clients.clear()
        for c in clients:
            c.close()


def _parse_headers(text: str) -> dict:
    """Parse RFC 7230 headers (case-insensitive keys, first value wins)."""
    lines = text.split("\r\n")
    headers = {}
    for line in lines[1:]:
        if not line or ":" not in line:
            continue
        k, _, v = line.partition(":")
        headers[k.strip().lower()] = v.strip()
    return headers


def _send_http_error(sock: socket.socket, code: int, msg: str):
    body = f"{code} {msg}\n".encode()
    resp = (
        f"HTTP/1.1 {code} {msg}\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
    ).encode() + body
    try:
        sock.sendall(resp)
        sock.close()
    except OSError:
        pass


def publish_transcript(text: str, start_ms: int, end_ms: int, confidence: float):
    """Convenience function to publish a transcript event to stdout.

    Routes through the same TranscriptPublisher used by the pipeline so the
    emitted event matches the schema pinned by test_event_schema_conformance.py
    (type, session_id, event_id, seq, text, start_ms, end_ms, confidence, ts_ms).

    A module-level lazy singleton keeps the call site a one-liner while
    sharing one session_id and monotonic seq counter across the process.
    """
    global _stdout_publisher
    if _stdout_publisher is None:
        _stdout_publisher = TranscriptPublisher(mode="stdout")
    _stdout_publisher.publish({
        "type": "transcript",
        "text": text,
        "start_ms": start_ms,
        "end_ms": end_ms,
        "confidence": confidence,
    })
