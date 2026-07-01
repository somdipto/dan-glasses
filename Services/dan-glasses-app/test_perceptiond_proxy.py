"""Tests for the /api/perceptiond proxy in dan-glasses-app server.py.

Mirrors test_proxy.py but covers perceptiond. Same strategy: import
SPAHandler, drive it against a socketpair, assert on the response bytes.
No real network except for the upstream-unreachable test (127.0.0.1:1).

Covers:
- /api/perceptiond/help returns the route catalog
- /api/perceptiond/health proxies to the daemon
- /api/perceptiond/status proxies
- /api/perceptiond/descriptions?count=N proxies
- /api/perceptiond/frame.jpg proxies and returns image/jpeg bytes
- 502 on daemon-down (mock upstream port)
- CORS preflight
- unknown path: 404 (proxied) or 502 -- both acceptable, must be JSON
"""
import io
import json
import os
import socket
import sys
import unittest
from unittest import mock

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
        if method == "OPTIONS":
            handler.do_OPTIONS()
        elif method == "GET":
            handler.do_GET()
        elif method == "POST":
            handler.do_POST()
        else:
            handler.send_error(405)
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
    import urllib.request
    import urllib.error
    try:
        urllib.request.urlopen("http://127.0.0.1:8092/health", timeout=0.5)
        return True
    except (urllib.error.URLError, ConnectionError, OSError):
        return False


class PerceptiondProxyTests(unittest.TestCase):
    def test_help_endpoint(self):
        status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/perceptiond/help")
        self.assertEqual(status, 200)
        self.assertIn("application/json", hdrs.get("content-type", ""))
        obj = json.loads(body)
        self.assertIn("routes", obj)
        self.assertIn("GET /api/perceptiond/health", obj["routes"])
        self.assertIn("GET /api/perceptiond/descriptions?count=N", obj["routes"])
        self.assertIn("GET /api/perceptiond/frame.jpg", obj["routes"])
        self.assertIn("POST /api/perceptiond/mode", obj["routes"])
        self.assertEqual(obj["http_upstream"], srv.PERCEPTIOND_HTTP)

    def test_health_proxy_when_perceptiond_up(self):
        if not _perceptiond_up():
            self.skipTest("perceptiond daemon not running on :8092")
        status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/perceptiond/health")
        self.assertEqual(status, 200)
        obj = json.loads(body)
        self.assertEqual(obj.get("status"), "ok")

    def test_status_proxy_when_perceptiond_up(self):
        if not _perceptiond_up():
            self.skipTest("perceptiond daemon not running on :8092")
        status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/perceptiond/status")
        self.assertEqual(status, 200)
        obj = json.loads(body)
        self.assertIn("running", obj)
        self.assertIn("frames_processed", obj)
        self.assertIn("descriptions", obj)
        self.assertIn("mode", obj)

    def test_descriptions_proxy_when_perceptiond_up(self):
        if not _perceptiond_up():
            self.skipTest("perceptiond daemon not running on :8092")
        status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/perceptiond/descriptions?count=2")
        self.assertEqual(status, 200)
        obj = json.loads(body)
        self.assertIn("count", obj)
        self.assertIsInstance(obj.get("descriptions"), list)
        self.assertEqual(obj["count"], len(obj["descriptions"]))
        if obj["count"] > 0:
            d = obj["descriptions"][0]
            self.assertIn("description", d)
            self.assertIn("image_id", d)
            self.assertIn("timestamp", d)

    def test_frame_jpeg_proxy_when_perceptiond_up(self):
        if not _perceptiond_up():
            self.skipTest("perceptiond daemon not running on :8092")
        status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/perceptiond/frame.jpg")
        self.assertEqual(status, 200)
        ctype = hdrs.get("content-type", "").split(";")[0].strip()
        self.assertEqual(ctype, "image/jpeg")
        self.assertGreater(len(body), 200)
        self.assertEqual(body[:2], b"\xff\xd8", "no JPEG SOI")

    def test_502_when_perceptiond_down(self):
        with mock.patch.object(srv, "PERCEPTIOND_HTTP", "http://127.0.0.1:1"):
            status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/perceptiond/health")
        self.assertEqual(status, 502)
        obj = json.loads(body)
        self.assertEqual(obj.get("error"), "upstream unreachable")
        self.assertIn("upstream", obj)

    def test_post_mode_proxies(self):
        if not _perceptiond_up():
            self.skipTest("perceptiond daemon not running on :8092")
        status, hdrs, body = _drive(
            srv.SPAHandler, "POST", "/api/perceptiond/mode",
            body=b'{"mode": "watchful"}',
            headers={"Content-Type": "application/json"},
        )
        # perceptiond accepts watchful|idle|active; watchful is current.
        self.assertIn(status, (200, 400))

    def test_cors_preflight(self):
        status, hdrs, body = _drive(srv.SPAHandler, "OPTIONS", "/api/perceptiond/health")
        self.assertEqual(status, 204)
        self.assertEqual(hdrs.get("access-control-allow-origin"), "*")
        self.assertIn("POST", hdrs.get("access-control-allow-methods", ""))

    def test_unknown_api_path_returns_json(self):
        status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/perceptiond/nonexistent")
        self.assertIn(status, (404, 502))
        ctype = hdrs.get("content-type", "").split(";")[0]
        self.assertEqual(ctype, "application/json")

    def test_cors_header_on_proxied_response(self):
        if not _perceptiond_up():
            self.skipTest("perceptiond daemon not running on :8092")
        status, hdrs, body = _drive(srv.SPAHandler, "GET", "/api/perceptiond/health")
        self.assertEqual(hdrs.get("access-control-allow-origin"), "*")


if __name__ == "__main__":
    unittest.main()
