"""End-to-end smoke test for the perceptiond vision stream.

This is the dan-glasses-app equivalent of the wizard roundtrip smoke for
audiod. It boots a minimal handler (no real socket server) and verifies
that the proxy path returns perceptiond's actual /status and
/descriptions JSON. Optionally exercises /frame.jpg and confirms JPEG.

What this proves:
  1. perceptiond is alive on :8092 (skip otherwise).
  2. The dan-glasses-app proxy correctly forwards HTTP and preserves JSON.
  3. /frame.jpg comes back as a real JPEG (SOI marker + >100 bytes).

Run:
    cd /home/workspace/dan-glasses/Services/dan-glasses-app
    python3 test_perceptiond_roundtrip.py
"""
import io
import json
import os
import socket
import sys
import time
import urllib.request
import urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import server as srv  # noqa: E402


def _make_pair():
    srv_sock, cli_sock = socket.socketpair()
    return cli_sock, srv_sock


def _drive(handler_cls, method, path, body=b"", headers=None):
    cli, srv_sock = _make_pair()
    headers = headers or {}
    req_lines = [f"{method} {path} HTTP/1.1", "Host: localhost"]
    for k, v in headers.items():
        req_lines.append(f"{k}: {v}")
    if body:
        req_lines.append(f"Content-Length: {len(body)}")
    req_lines.append("")
    if body:
        req_lines.append("")
    raw = ("\r\n".join(req_lines) + (body.decode("latin-1") if isinstance(body, bytes) else body)).encode("latin-1")
    cli.sendall(raw)
    cli.shutdown(socket.SHUT_WR)

    handler = handler_cls.__new__(handler_cls)
    handler.request = srv_sock
    handler.client_address = ("127.0.0.1", 0)
    handler.server = None
    handler.setup()
    handler.directory = srv.DIST
    # parse_request() reads self.raw_requestline, which is normally set by
    # handle_one_request(). Drive it manually here so we can dispatch directly.
    handler.raw_requestline = handler.rfile.readline(65537)
    if not handler.raw_requestline:
        srv_sock.close()
        cli.close()
        return 0, {}, b""
    handler.parse_request()
    try:
        if method == "GET":
            handler.do_GET()
        elif method == "POST":
            handler.do_POST()
    except BrokenPipeError:
        pass

    srv_sock.close()
    chunks = []
    while True:
        try:
            chunk = cli.recv(65536)
        except OSError:
            break
        if not chunk:
            break
        chunks.append(chunk)
    cli.close()
    raw = b"".join(chunks)
    if b"\r\n\r\n" not in raw:
        return 0, {}, b""
    head, _, body = raw.partition(b"\r\n\r\n")
    lines = head.split(b"\r\n")
    status = int(lines[0].split(b" ")[1]) if len(lines) > 1 else 0
    hdrs = {}
    for line in lines[1:]:
        if b":" in line:
            k, _, v = line.partition(b":")
            hdrs[k.decode().strip().lower()] = v.decode().strip()
    return status, hdrs, body


def _perceptiond_up():
    try:
        with urllib.request.urlopen("http://127.0.0.1:8092/health", timeout=0.5) as r:
            return json.loads(r.read()).get("status") == "ok"
    except (urllib.error.URLError, ConnectionError, OSError, json.JSONDecodeError):
        return False


def main() -> int:
    t0 = time.time()
    print("\n=== perceptiond → dan-glasses-app proxy roundtrip ===\n")

    if not _perceptiond_up():
        print("SKIP: perceptiond not running on :8092")
        return 0

    print("[1/5] /api/perceptiond/health via proxy")
    status, _, body = _drive(srv.SPAHandler, "GET", "/api/perceptiond/health")
    assert status == 200, f"health expected 200, got {status}"
    obj = json.loads(body)
    assert obj.get("status") == "ok", f"health payload: {obj}"
    print(f"      OK ({len(body)} bytes)")

    print("[2/5] /api/perceptiond/status via proxy")
    status, _, body = _drive(srv.SPAHandler, "GET", "/api/perceptiond/status")
    assert status == 200, f"status expected 200, got {status}"
    obj = json.loads(body)
    assert obj.get("running") is True, f"status payload: {obj}"
    fp = obj.get("frames_processed", 0)
    ds = obj.get("descriptions", 0)
    print(f"      OK (frames_processed={fp}, descriptions={ds}, mode={obj.get('mode')})")

    print("[3/5] /api/perceptiond/descriptions?count=3 via proxy")
    status, _, body = _drive(srv.SPAHandler, "GET", "/api/perceptiond/descriptions?count=3")
    assert status == 200, f"descriptions expected 200, got {status}"
    obj = json.loads(body)
    assert obj.get("count", 0) >= 0, f"descriptions payload: {obj}"
    assert isinstance(obj.get("descriptions"), list)
    n = obj["count"]
    if n > 0:
        d = obj["descriptions"][0]
        assert d.get("description"), f"first description empty: {d}"
        sample = d["description"][:80]
        print(f"      OK ({n} descriptions, latest: \"{sample}{'...' if len(d['description']) > 80 else ''}\")")
    else:
        print(f"      OK ({n} descriptions — VLM still warming up)")

    print("[4/5] /api/perceptiond/frame.jpg via proxy (real JPEG)")
    status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/perceptiond/frame.jpg")
    assert status == 200, f"frame expected 200, got {status}"
    assert b"\xff\xd8" in body[:4], f"no JPEG SOI, got {body[:4].hex()}"
    assert len(body) > 200, f"JPEG too small: {len(body)} bytes"
    print(f"      OK ({len(body)} bytes, content-type={hdrs.get('content-type', '?')})")

    print("[5/5] POST /api/perceptiond/mode (re-affirm watchful)")
    status, _, body = _drive(
        srv.SPAHandler, "POST", "/api/perceptiond/mode",
        body=b'{"mode": "watchful"}',
        headers={"Content-Type": "application/json"},
    )
    assert status in (200, 400), f"mode expected 200/400, got {status} body={body[:120]!r}"
    print(f"      OK (status={status})")

    dt = time.time() - t0
    print(f"\n=== ROUNDTRIP OK in {dt:.2f}s ===\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
