"""Tests for the WebSocket publisher (frame encoding + handshake parsing)."""

import base64
import hashlib
import json
import socket
import struct
import threading
import time

import pytest

from publish import (
    TranscriptPublisher,
    WS_GUID,
    _accept_key,
    _frame,
    _parse_client_frame,
    _parse_headers,
    frame_text,
)


class TestFrameEncoding:
    def test_frame_text_small(self):
        f = frame_text(b"hi")
        # FIN=1, opcode=1 (text) → 0x81
        assert f[0] == 0x81
        # length 2, unmasked → 0x02
        assert f[1] == 0x02
        assert f[2:] == b"hi"

    def test_frame_text_125(self):
        payload = b"x" * 125
        f = frame_text(payload)
        assert f[1] == 125
        assert f[2:] == payload

    def test_frame_text_126(self):
        payload = b"x" * 200
        f = frame_text(payload)
        # length 126, 2-byte extended length follows
        assert f[1] == 126
        assert struct.unpack(">H", f[2:4])[0] == 200
        assert f[4:] == payload

    def test_frame_text_127(self):
        payload = b"x" * 70000
        f = frame_text(payload)
        assert f[1] == 127
        assert struct.unpack(">Q", f[2:10])[0] == 70000
        assert f[10:] == payload

    def test_frame_rejects_bad_opcode(self):
        with pytest.raises(ValueError):
            _frame(99, b"x")

    def test_frame_masks_payload(self):
        f = _frame(0x1, b"hello", mask=True)
        # mask bit set on byte 1
        assert f[1] & 0x80
        # unmask → "hello"
        masked = f[2 + 4 :]
        assert len(masked) == 5
        key = f[2:6]
        unmasked = bytes(b ^ key[i & 3] for i, b in enumerate(masked))
        assert unmasked == b"hello"


class TestClientFrameParse:
    def test_parse_unmasked_text_rejected(self):
        # Client→server must be masked; unmasked frames are protocol violations
        f = b"\x81\x05hello"
        assert _parse_client_frame(f) is None

    def test_parse_masked_text(self):
        key = b"\x01\x02\x03\x04"
        payload = b"hello"
        masked = bytes(b ^ key[i & 3] for i, b in enumerate(payload))
        f = b"\x81" + bytes([0x80 | len(payload)]) + key + masked
        parsed = _parse_client_frame(f)
        assert parsed is not None
        data, opcode, frame_size = parsed
        assert opcode == 0x1
        assert data == payload
        assert frame_size == len(f)

    def test_parse_close(self):
        key = b"\x00" * 4
        payload = b""
        f = b"\x88" + bytes([0x80]) + key
        parsed = _parse_client_frame(f)
        assert parsed is not None
        _, opcode, _ = parsed
        assert opcode == 0x8

    def test_parse_truncated(self):
        # Single byte: header incomplete
        assert _parse_client_frame(b"\x81") is None
        # Header ok, length=0, but mask key missing (only 4 bytes total, no length)
        # b"\x81\x80" + no mask key → can't parse
        assert _parse_client_frame(b"\x81\x80") is None
        # Header ok, declared length 0x05, but only mask key (no payload)
        assert _parse_client_frame(b"\x81\x85\x00\x00\x00\x00") is None

    def test_parse_empty_masked_frame_is_valid(self):
        # A masked frame with zero payload is a valid empty text frame
        f = b"\x81\x80" + b"\x00\x00\x00\x00"
        parsed = _parse_client_frame(f)
        assert parsed is not None
        payload, opcode, frame_size = parsed
        assert payload == b""
        assert opcode == 0x1
        assert frame_size == len(f)


class TestHeaders:
    def test_parse_simple(self):
        text = "GET / HTTP/1.1\r\nHost: localhost:8091\r\nUpgrade: websocket\r\n\r\n"
        h = _parse_headers(text)
        assert h["host"] == "localhost:8091"
        assert h["upgrade"] == "websocket"

    def test_parse_case_insensitive(self):
        text = "POST /chat HTTP/1.1\r\nContent-Type: text/plain\r\n\r\n"
        h = _parse_headers(text)
        assert h["content-type"] == "text/plain"


class TestAcceptKey:
    def test_rfc_example(self):
        # RFC 6455 §1.3 example
        key = "dGhlIHNhbXBsZSBub25jZQ=="
        accept = _accept_key(key)
        assert accept == "s3pPLMBiTxaQ9kYGzzhZRbK+xOo="


def _ws_handshake(sock, key):
    req = (
        "GET / HTTP/1.1\r\n"
        "Host: localhost\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        f"Sec-WebSocket-Key: {key}\r\n"
        "Sec-WebSocket-Version: 13\r\n"
        "\r\n"
    )
    sock.sendall(req.encode("ascii"))


def _read_until_double_crlf(sock, timeout=2.0):
    sock.settimeout(timeout)
    buf = b""
    while b"\r\n\r\n" not in buf:
        chunk = sock.recv(4096)
        if not chunk:
            break
        buf += chunk
    return buf


def _encode_client_text_frame(payload: bytes) -> bytes:
    key = b"\x01\x02\x03\x04"
    masked = bytes(b ^ key[i & 3] for i, b in enumerate(payload))
    return b"\x81" + bytes([0x80 | len(payload)]) + key + masked


def _encode_client_close_frame() -> bytes:
    key = b"\x00" * 4
    return b"\x88\x80" + key


class TestPublisherWebSocket:
    """End-to-end WS server test using raw sockets (no ws client lib)."""

    @staticmethod
    def _free_port() -> int:
        s = socket.socket()
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
        s.close()
        return port

    def test_ws_client_receives_event(self):
        port = self._free_port()
        pub = TranscriptPublisher(mode="websocket", ws_port=port)
        try:
            # Give the accept loop a moment to bind
            time.sleep(0.3)

            sock = socket.socket()
            sock.settimeout(5)
            sock.connect(("127.0.0.1", port))
            key = base64.b64encode(b"0123456789abcdef").decode()
            _ws_handshake(sock, key)
            resp = _read_until_double_crlf(sock)
            assert b"101 Switching Protocols" in resp
            accept = hashlib.sha1((key + WS_GUID).encode()).digest()
            assert base64.b64encode(accept).decode().encode() in resp

            # Wait until the publisher has registered the client in its list
            # (the handshake handler appends after the 101 is sent).
            deadline = time.time() + 2.0
            while time.time() < deadline:
                with pub._ws_lock:
                    if pub._ws_clients:
                        break
                time.sleep(0.01)

            # Publish an event; client should receive a text frame
            pub.publish(
                {
                    "type": "transcript",
                    "text": "ws hello",
                    "start_ms": 0,
                    "end_ms": 100,
                    "confidence": 0.9,
                }
            )

            # First frame should be FIN + text opcode with our payload
            sock.settimeout(3.0)
            frame = sock.recv(4096)
            assert frame[0] == 0x81  # FIN + text
            length = frame[1] & 0x7F
            if length < 126:
                body = frame[2 : 2 + length]
            elif length == 126:
                length = struct.unpack(">H", frame[2:4])[0]
                body = frame[4 : 4 + length]
            else:
                length = struct.unpack(">Q", frame[2:10])[0]
                body = frame[10 : 10 + length]
            event = json.loads(body.decode("utf-8"))
            assert event["text"] == "ws hello"

            # Clean close
            sock.sendall(_encode_client_close_frame())
        finally:
            pub.close()
            try:
                sock.close()
            except OSError:
                pass

    def test_ws_handshake_rejects_non_upgrade(self):
        port = self._free_port()
        pub = TranscriptPublisher(mode="websocket", ws_port=port)
        try:
            time.sleep(0.2)
            sock = socket.socket()
            sock.settimeout(3)
            sock.connect(("127.0.0.1", port))
            sock.sendall(b"GET / HTTP/1.1\r\nHost: x\r\n\r\n")
            resp = _read_until_double_crlf(sock)
            assert b"400" in resp
        finally:
            pub.close()
            try:
                sock.close()
            except OSError:
                pass

    def test_ws_handshake_rejects_missing_key(self):
        port = self._free_port()
        pub = TranscriptPublisher(mode="websocket", ws_port=port)
        try:
            time.sleep(0.2)
            sock = socket.socket()
            sock.settimeout(3)
            sock.connect(("127.0.0.1", port))
            sock.sendall(
                b"GET / HTTP/1.1\r\nHost: x\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n\r\n"
            )
            resp = _read_until_double_crlf(sock)
            assert b"400" in resp
        finally:
            pub.close()
            try:
                sock.close()
            except OSError:
                pass

    def test_ws_handshake_echoes_ping_with_pong(self):
        port = self._free_port()
        pub = TranscriptPublisher(mode="websocket", ws_port=port)
        try:
            time.sleep(0.2)
            sock = socket.socket()
            sock.settimeout(3)
            sock.connect(("127.0.0.1", port))
            key = base64.b64encode(b"pingpongkey12345").decode()
            _ws_handshake(sock, key)
            _read_until_double_crlf(sock)
            # Send masked ping
            ping_payload = b"ping"
            sock.sendall(_encode_client_text_frame(ping_payload).replace(b"\x81", b"\x89"))
            # Should receive pong with same payload
            frame = sock.recv(4096)
            opcode = frame[0] & 0x0F
            assert opcode == 0xA  # pong
            length = frame[1] & 0x7F
            assert frame[2 : 2 + length] == ping_payload
            # Clean close
            sock.sendall(_encode_client_close_frame())
        finally:
            pub.close()
            try:
                sock.close()
            except OSError:
                pass
