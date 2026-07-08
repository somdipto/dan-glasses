"""Regression tests for WebSocket upgrade forwarding in dan-glasses-app.

The /api/audiod/stream endpoint must:
- return 101 Switching Protocols when the browser requests an upgrade
- forward the Sec-WebSocket-Accept back to the client
- hand the bidirectional byte stream off to audiod's :8091

These tests connect to a real dan-glasses-app server on :8747 and
assert on the wire. Skipped if the server is not reachable.
"""
import base64
import os
import socket
import struct
import sys
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

PROXY_HOST = os.environ.get("PROXY_HOST", "127.0.0.1")
PROXY_PORT = int(os.environ.get("PROXY_PORT", "8747"))


def _audiod_ws_listening(host="127.0.0.1", port=8091, timeout=0.5):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _server_reachable(host, port, timeout=1.0):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _ws_handshake(sock, path):
    key = base64.b64encode(os.urandom(16)).decode()
    req = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {PROXY_HOST}:{PROXY_PORT}\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        f"Sec-WebSocket-Key: {key}\r\n"
        "Sec-WebSocket-Version: 13\r\n"
        "\r\n"
    ).encode("ascii")
    sock.sendall(req)
    buf = b""
    while b"\r\n\r\n" not in buf:
        chunk = sock.recv(4096)
        if not chunk:
            raise ConnectionError("closed during handshake")
        buf += chunk
        if len(buf) > 16384:
            raise ConnectionError("handshake too large")
    return buf.split(b"\r\n\r\n", 1)[0], key


def _send_ping(sock, payload=b"ping"):
    """Send a WS ping frame (opcode 0x9)."""
    n = len(payload)
    mask_key = os.urandom(4)
    if n < 126:
        header = bytes([0x89, 0x80 | n])
    elif n < 65536:
        header = bytes([0x89, 0x80 | 126]) + struct.pack(">H", n)
    else:
        header = bytes([0x89, 0x80 | 127]) + struct.pack(">Q", n)
    sock.sendall(header + mask_key + bytes(b ^ mask_key[i % 4] for i, b in enumerate(payload)))


def _read_one_frame(sock, timeout=3.0):
    sock.settimeout(timeout)
    hdr = b""
    while len(hdr) < 2:
        c = sock.recv(2 - len(hdr))
        if not c:
            return None
        hdr += c
    b1, b2 = hdr[0], hdr[1]
    opcode = b1 & 0x0F
    masked = b2 & 0x80
    length = b2 & 0x7F
    if length == 126:
        ext = sock.recv(2)
        length = struct.unpack(">H", ext)[0]
    elif length == 127:
        ext = sock.recv(8)
        length = struct.unpack(">Q", ext)[0]
    mask = sock.recv(4) if masked else b""
    payload = b""
    while len(payload) < length:
        c = sock.recv(length - len(payload))
        if not c:
            break
        payload += c
    if masked and mask:
        payload = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
    return opcode, payload


@unittest.skipUnless(
    _server_reachable(PROXY_HOST, PROXY_PORT),
    f"dan-glasses-app not reachable at {PROXY_HOST}:{PROXY_PORT}",
)
@unittest.skipUnless(
    _audiod_ws_listening(),
    "audiod WS server not listening on :8091 (publish.mode != websocket/both)",
)
class TestWsUpgrade(unittest.TestCase):
    def test_handshake_returns_101(self):
        s = socket.create_connection((PROXY_HOST, PROXY_PORT), timeout=3)
        try:
            head, _ = _ws_handshake(s, "/api/audiod/stream")
        finally:
            s.close()
        text = head.decode("latin-1")
        self.assertIn("101", text.split("\r\n", 1)[0], msg=f"unexpected: {text!r}")
        self.assertIn("Upgrade: websocket", text)
        self.assertIn("Connection: Upgrade", text)
        self.assertIn("Sec-WebSocket-Accept:", text)

    def test_ping_round_trip(self):
        """Send a ping; audiod's WS server must reply with a pong containing
        the same payload. This proves the bidirectional byte bridge works."""
        s = socket.create_connection((PROXY_HOST, PROXY_PORT), timeout=3)
        try:
            head, _ = _ws_handshake(s, "/api/audiod/stream")
            self.assertIn("101", head.decode("latin-1").split("\r\n", 1)[0])
            _send_ping(s, b"hello")
            frame = _read_one_frame(s, timeout=5)
            self.assertIsNotNone(frame, msg="no frame returned")
            opcode, payload = frame
            # 0xA = pong
            self.assertEqual(opcode, 0xA, msg=f"expected pong (0xA), got {hex(opcode)}")
            self.assertEqual(payload, b"hello")
        finally:
            s.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)