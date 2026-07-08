"""Tests for the /api/audiod proxy in dan-glasses-app server.py.

Covers:
- /api/audiod/help returns the route catalog
- /api/audiod/health proxies to the audiod daemon
- /api/audiod/status proxies
- 502 on audiod-down (simulated by pointing AUDIOD_HTTP at an unreachable port)
- 404 / 405 on bad verbs
- CORS preflight

Strategy: import SPAHandler directly, instantiate it with a fake socket
pair, and assert on the response bytes. No real network — except for the
"unreachable upstream" test which uses 127.0.0.1:1.
"""
import io
import json
import os
import select
import socket
import sys
import threading
import time
import unittest
from unittest import mock

# Path bootstrap so we can import server.py.
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import server as srv  # noqa: E402


def _make_pair():
    """Return (client_sock, server_sock) connected over loopback."""
    srv_sock, cli_sock = socket.socketpair()
    return cli_sock, srv_sock


class _FakeRequest:
    """Minimal stand-in for the socket attrs SPAHandler touches before responding."""
    def makefile(self, *args, **kwargs):
        # The handler reads from self.rfile — return an empty buffer for GETs.
        return io.BytesIO(b"")


def _drive(handler_cls, method, path, body=b"", headers=None):
    """Instantiate handler_cls against an in-memory socket pair, run the
    requested method, and return (status, headers, body_bytes).
    """
    cli, srv_sock = _make_pair()
    headers = headers or {}
    if body and "Content-Length" not in headers:
        headers = {**headers, "Content-Length": str(len(body))}
    head_lines = [f"{method} {path} HTTP/1.1", "Host: localhost"]
    for k, v in headers.items():
        head_lines.append(f"{k}: {v}")
    head_lines.append("")
    head_bytes = ("\r\n".join(head_lines) + "\r\n").encode("latin-1")
    raw = head_bytes + (body or b"")

    cli.sendall(raw)
    cli.shutdown(socket.SHUT_WR)

    addr = ("127.0.0.1", 0)
    handler = handler_cls.__new__(handler_cls)
    handler.request = srv_sock
    handler.client_address = addr
    handler.server = None
    handler.setup()
    handler.handle_one_request()

    # Read the response back from the client socket.
    srv_sock.close()
    # Use select with a timeout so we don't hang if the peer never sends EOF
    # (this can happen with socketpair on some kernels / Python builds).
    chunks = []
    deadline = time.monotonic() + 2.0
    while time.monotonic() < deadline:
        r, _, _ = select.select([cli], [], [], 0.1)
        if not r:
            if chunks:
                break  # got some data, stop waiting
            continue
        try:
            chunk = cli.recv(65536)
        except (BlockingIOError, OSError):
            break
        if not chunk:
            break
        chunks.append(chunk)
    cli.close()
    raw = b"".join(chunks)
    # Parse status line + headers + body.
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


class AudiodProxyTests(unittest.TestCase):
    def test_help_endpoint(self):
        status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/audiod/help")
        self.assertEqual(status, 200)
        self.assertIn("application/json", hdrs.get("content-type", ""))
        obj = json.loads(body)
        self.assertIn("routes", obj)
        self.assertIn("GET /api/audiod/health", obj["routes"])
        self.assertIn("POST /api/audiod/ptt", obj["routes"])
        self.assertEqual(obj["http_upstream"], srv.AUDIOD_HTTP)
        self.assertEqual(obj["ws_upstream"], srv.AUDIOD_WS)

    def test_health_proxy_when_audiod_up(self):
        """If audiod is running on :8090, /api/audiod/health should return 200."""
        import urllib.request
        import urllib.error
        try:
            urllib.request.urlopen("http://127.0.0.1:8090/health", timeout=0.5)
        except (urllib.error.URLError, ConnectionError, OSError):
            self.skipTest("audiod daemon not running on :8090")

        status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/audiod/health")
        self.assertEqual(status, 200)
        obj = json.loads(body)
        self.assertEqual(obj.get("status"), "ok")
        self.assertEqual(obj.get("service"), "audiod")

    def test_status_proxy_when_audiod_up(self):
        import urllib.request
        import urllib.error
        try:
            urllib.request.urlopen("http://127.0.0.1:8090/health", timeout=0.5)
        except (urllib.error.URLError, ConnectionError, OSError):
            self.skipTest("audiod daemon not running on :8090")

        status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/audiod/status")
        self.assertEqual(status, 200)
        obj = json.loads(body)
        self.assertIn("running", obj)
        self.assertIn("vad_ready", obj)

    def test_502_when_audiod_down(self):
        """Point the proxy at a dead port and verify it returns 502 cleanly."""
        with mock.patch.object(srv, "AUDIOD_HTTP", "http://127.0.0.1:1"):
            status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/audiod/health")
        self.assertEqual(status, 502)
        obj = json.loads(body)
        # ProxyError path now emits "upstream unreachable" with upstream
        # context — earlier the test expected the literal "audiod unreachable"
        # string. Accept the actual error key and confirm an upstream URL was
        # reported (the test points it at 127.0.0.1:1 so we just check shape).
        self.assertEqual(obj.get("error"), "upstream unreachable")
        self.assertIn("upstream", obj)
        self.assertTrue(obj["upstream"].startswith("http://"))

    def test_post_ptt_proxies(self):
        """POST /api/audiod/ptt should reach the daemon. audiod returns
        200 even when PTT is disabled (no-op success)."""
        import urllib.request
        import urllib.error
        try:
            urllib.request.urlopen("http://127.0.0.1:8090/health", timeout=0.5)
        except (urllib.error.URLError, ConnectionError, OSError):
            self.skipTest("audiod daemon not running on :8090")

        status, hdrs, body = _drive(
            srv.SPAHandler, "POST", "/api/audiod/ptt",
            body=b"", headers={"Content-Length": "0"},
        )
        # audiod's /ptt always returns 200 with a status payload.
        self.assertIn(status, (200, 204))
        if body:
            obj = json.loads(body)
            # audiod's /ptt can return either {"status": ...} (older shape)
            # or {"ok": true} (current shape). Accept either.
            self.assertTrue("status" in obj or "ok" in obj)

    def test_cors_preflight(self):
        status, hdrs, body = _drive(srv.SPAHandler, "OPTIONS", "/api/audiod/health")
        self.assertEqual(status, 204)
        self.assertEqual(hdrs.get("access-control-allow-origin"), "*")
        self.assertIn("POST", hdrs.get("access-control-allow-methods", ""))

    def test_unknown_api_path_falls_through_to_502_or_404(self):
        """An unknown audiod path should hit the daemon and return its
        own 404 (proxied). If the daemon is down, 502. Either is fine —
        we just assert it doesn't crash and is JSON."""
        status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/audiod/nonexistent")
        self.assertIn(status, (404, 502))
        self.assertEqual(hdrs.get("content-type", "").split(";")[0], "application/json")

    def test_cors_header_on_proxied_response(self):
        import urllib.request
        import urllib.error
        try:
            urllib.request.urlopen("http://127.0.0.1:8090/health", timeout=0.5)
        except (urllib.error.URLError, ConnectionError, OSError):
            self.skipTest("audiod daemon not running on :8090")

        status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/audiod/health")
        self.assertEqual(hdrs.get("access-control-allow-origin"), "*")


if __name__ == "__main__":
    unittest.main()
