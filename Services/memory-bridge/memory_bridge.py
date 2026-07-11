#!/usr/bin/env python3
"""memory-bridge: subscribe to audiod /stream WS, POST each transcript to memoryd.

One-direction fan-in. Idempotent on audiod event_id. Reconnects on failure.
Optional sink: also publishes to a local file for debug.

Run: python3 memory_bridge.py [--audiod ws://127.0.0.1:8091/stream]
                              [--memoryd http://127.0.0.1:8741]
                              [--sink /home/workspace/.cache/dan-glasses/memory-bridge/bridge.log]
"""
import argparse
import json
import os
import socket
import sys
import threading
import time
import urllib.request
import urllib.error
import base64
import hashlib
import struct
from typing import Optional

WS_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"


def _ws_handshake(sock: socket.socket, host: str, port: int, path: str) -> None:
    key = base64.b64encode(os.urandom(16)).decode("ascii")
    req = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host}:{port}\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        f"Sec-WebSocket-Key: {key}\r\n"
        "Sec-WebSocket-Version: 13\r\n"
        f"User-Agent: memory-bridge/0.1\r\n"
        "\r\n"
    )
    sock.sendall(req.encode("ascii"))
    buf = b""
    sock.settimeout(5.0)
    while b"\r\n\r\n" not in buf:
        chunk = sock.recv(4096)
        if not chunk:
            raise RuntimeError("ws: handshake closed early")
        buf += chunk
    head, _, _ = buf.partition(b"\r\n\r\n")
    if b" 101 " not in head.split(b"\r\n", 1)[0]:
        raise RuntimeError(f"ws: handshake failed: {head[:120]!r}")
    accept_expected = base64.b64encode(
        hashlib.sha1((key + WS_GUID).encode("ascii")).digest()
    ).decode("ascii")
    if accept_expected.encode("ascii") not in head:
        raise RuntimeError("ws: bad Sec-WebSocket-Accept")


def _ws_read_frame(sock: socket.socket) -> Optional[dict]:
    """Read one server→client frame (must be unmasked). Returns parsed JSON dict or None on close."""
    def _recv_n(n: int) -> bytes:
        out = b""
        while len(out) < n:
            chunk = sock.recv(n - len(out))
            if not chunk:
                raise ConnectionError("ws: socket closed mid-frame")
            out += chunk
        return out

    hdr = _recv_n(2)
    fin = hdr[0] & 0x80
    opcode = hdr[0] & 0x0F
    masked = hdr[1] & 0x80
    length = hdr[1] & 0x7F
    if length == 126:
        length = struct.unpack(">H", _recv_n(2))[0]
    elif length == 127:
        length = struct.unpack(">Q", _recv_n(8))[0]
    if masked:
        mask_key = _recv_n(4)
        payload = bytearray(_recv_n(length))
        for i in range(length):
            payload[i] ^= mask_key[i & 3]
        payload = bytes(payload)
    else:
        payload = _recv_n(length)

    if opcode == 0x8:  # close
        return None
    if opcode == 0x9:  # ping — ignore
        return _ws_read_frame(sock)
    if opcode not in (0x1,):  # only text frames
        return _ws_read_frame(sock)
    return json.loads(payload.decode("utf-8"))


def _build_memory_payload(event: dict) -> dict:
    """Map an audiod transcript event into a memoryd POST body.

    memoryd schema: {type, content, metadata?}
    VALID_TYPES = ("episodic", "semantic", "procedural")
    """
    text = (event.get("text") or "").strip()
    meta = {
        "source": "audiod",
        "session_id": event.get("session_id"),
        "event_id": event.get("event_id"),
        "seq": event.get("seq"),
        "start_ms": event.get("start_ms"),
        "end_ms": event.get("end_ms"),
        "confidence": event.get("confidence"),
        "ts_ms": event.get("ts_ms"),
        "bridge": "memory-bridge",
    }
    # Drop keys whose value is None to keep the audit row tight.
    meta = {k: v for k, v in meta.items() if v is not None}
    return {"type": "episodic", "content": text, "metadata": meta}


def _post_memory(memoryd: str, payload: dict) -> tuple[int, str]:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{memoryd}/memories",
        data=body,
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status, resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")
    except Exception as e:
        return 0, f"bridge-error: {e}"


def _append_sink(path: Optional[str], line: str) -> None:
    if not path:
        return
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass


def run(audiod_url: str, memoryd: str, sink: Optional[str]) -> int:
    # audiod_url like ws://127.0.0.1:8091/stream
    assert audiod_url.startswith("ws://"), audiod_url
    rest = audiod_url[len("ws://"):]
    host_port, _, path = rest.partition("/")
    host, _, port_s = host_port.partition(":")
    port = int(port_s or "80")
    if not path.startswith("/"):
        path = "/" + path
    if not path:
        path = "/"

    print(f"memory-bridge: audiod={audiod_url} memoryd={memoryd} sink={sink}", flush=True)
    seen_event_ids: set[str] = set()
    backoff = 1.0
    while True:
        sock: Optional[socket.socket] = None
        try:
            sock = socket.create_connection((host, port), timeout=5.0)
            _ws_handshake(sock, host, port, path)
            print("memory-bridge: ws connected", flush=True)
            backoff = 1.0
            sock.settimeout(60.0)
            while True:
                event = _ws_read_frame(sock)
                if event is None:
                    raise ConnectionError("ws: closed by server")
                text = (event.get("text") or "").strip()
                if not text:
                    continue
                eid = event.get("event_id") or event.get("id")
                if eid and eid in seen_event_ids:
                    continue
                if eid:
                    seen_event_ids.add(eid)
                if len(seen_event_ids) > 5000:
                    seen_event_ids = set(list(seen_event_ids)[-1000:])

                print(f"memory-bridge: recv event_id={event.get('event_id')} text={text[:80]!r}", flush=True)
                payload = _build_memory_payload(event)
                status, body = _post_memory(memoryd, payload)
                if 200 <= status < 300:
                    log(f"stored: id-from-memoryd seq={event.get('seq')} text={text[:80]!r}")
                else:
                    log(f"memoryd POST failed: {status} {body[:200]}")
        except Exception as e:
            log(f"forward error: {e!r}")
        except (ConnectionError, OSError, RuntimeError) as e:
            print(f"memory-bridge: connection error: {e}; retry in {backoff:.1f}s", flush=True)
            time.sleep(backoff)
            backoff = min(backoff * 2, 30.0)
        finally:
            if sock is not None:
                try:
                    sock.close()
                except Exception:
                    pass


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--audiod", default=os.environ.get("AUDIOD_WS", "ws://127.0.0.1:8091/stream"))
    p.add_argument("--memoryd", default=os.environ.get("MEMORYD_URL", "http://127.0.0.1:8741"))
    p.add_argument("--sink", default=os.environ.get("BRIDGE_SINK", "/home/workspace/.cache/dan-glasses/memory-bridge/bridge.log"))
    p.add_argument("--inject", action="store_true", help="Synthesize one audiod event and POST to memoryd, then exit. For E2E verification.")
    args = p.parse_args()
    if args.inject:
        event = {
            "type": "transcript",
            "event_id": "inject-dan1-001",
            "session_id": "synth",
            "seq": 0,
            "text": "DAN1 bridge inject e2e test",
            "start_ms": 0,
            "end_ms": 1500,
            "confidence": 0.99,
            "ts_ms": int(time.time() * 1000),
        }
        payload = _build_memory_payload(event)
        status, body = _post_memory(args.memoryd, payload)
        print(f"memory-bridge: inject status={status} body={body[:200]}")
        return 0 if 200 <= status < 300 else 1
    try:
        return run(args.audiod, args.memoryd, args.sink) or 0
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    sys.exit(main())
