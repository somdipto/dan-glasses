#!/usr/bin/env python3
"""
Static file server for the dan-glasses-app built UI.
Serves /home/workspace/dan-glasses/apps/dan-glasses-app/dist on PORT.
SPA fallback: any path without an extension and not found in dist
returns index.html so client-side routing works.

Also proxies /api/audiod/* to the audiod daemon (default :8090) and
/api/perceptiond/* to the perceptiond daemon (default :8092) so the
SPA can hit a single origin. WebSocket upgrades to /api/audiod/stream
are forwarded to audiod's :8091 WS endpoint.
"""
import os
import sys
import json
import http.server
import socketserver
import urllib.request
import urllib.error
import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

DIST = os.environ.get("DIST", "/home/workspace/dan-glasses/apps/dan-glasses-app/dist")
STATIC_DIR = os.environ.get("STATIC_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"))
PORT = int(os.environ.get("PORT", "8747"))

AUDIOD_HTTP = os.environ.get("AUDIOD_HTTP", "http://127.0.0.1:8090")
AUDIOD_WS = os.environ.get("AUDIOD_WS", "ws://127.0.0.1:8091")
PERCEPTIOND_HTTP = os.environ.get("PERCEPTIOND_HTTP", "http://127.0.0.1:8092")
MEMORYD_HTTP = os.environ.get("MEMORYD_HTTP", "http://127.0.0.1:8741")
TOOLD_HTTP = os.environ.get("TOOLD_HTTP", "http://127.0.0.1:8742")
TTSD_HTTP = os.environ.get("TTSD_HTTP", "http://127.0.0.1:8743")


def _parse_ws_base(ws_url: str) -> tuple[str, int]:
    """Parse ws://host:port into (host, port). Defaults to 127.0.0.1:8091."""
    s = ws_url
    if s.startswith("ws://"):
        s = s[len("ws://"):]
    if s.startswith("wss://"):
        s = s[len("wss://"):]
    if "/" in s:
        s = s.split("/", 1)[0]
    if ":" in s:
        host, port_s = s.rsplit(":", 1)
        try:
            return host, int(port_s)
        except ValueError:
            return host, 8091
    return s, 8091


AUDIOD_WS_HOST, AUDIOD_WS_PORT = _parse_ws_base(AUDIOD_WS)


class ProxyError(Exception):
    pass


def _proxy_http(method: str, upstream_base: str, upstream_path: str, body: bytes = b"", query: str = "") -> tuple:
    """Forward an HTTP request to an upstream daemon.

    `upstream_base` is the full http://host:port of the target.
    Returns (status_code, response_headers_subset, body_bytes).
    """
    url = upstream_base.rstrip("/") + upstream_path
    if query:
        url = url + "?" + query
    req = urllib.request.Request(url, data=body if body else None, method=method)
    if body:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return (
                resp.status,
                {"content-type": resp.headers.get("Content-Type", "application/json")},
                resp.read(),
            )
    except urllib.error.HTTPError as e:
        return (
            e.code,
            {"content-type": e.headers.get("Content-Type", "application/json") if e.headers else "application/json"},
            e.read() if e.fp else b'{"error":"upstream http error"}',
        )
    except (urllib.error.URLError, ConnectionError, TimeoutError, OSError) as e:
        raise ProxyError(str(e)) from e


def _forward_to_upstream(self: "SPAHandler", upstream_base: str, subpath: str, query: str = "") -> None:
    """Generic /api/<service>/* → upstream HTTP forwarder."""
    body = b""
    if self.command == "POST":
        length = int(self.headers.get("Content-Length", "0") or "0")
        if length:
            body = self.rfile.read(length)
    try:
        status, hdrs, payload = _proxy_http(self.command, upstream_base, subpath, body, query)
    except ProxyError as e:
        self._send_json(502, {"error": "upstream unreachable", "detail": str(e), "upstream": upstream_base})
        return
    self.send_response(status)
    for k, v in hdrs.items():
        # Don't echo upstream CORS — we set our own * below.
        if k.lower() == "access-control-allow-origin":
            continue
        self.send_header(k, v)
    self.send_header("Content-Length", str(len(payload)))
    self.end_headers()
    self.wfile.write(payload)


def _serve_ws_upgrade(self: "SPAHandler", upstream_host: str, upstream_port: int, upstream_path: str) -> None:
    """Bridge a WebSocket upgrade from the client to an upstream TCP socket.

    Forwards the HTTP handshake verbatim (rewriting only the request-line
    target), then pipes bytes in both directions until either side closes.
    Designed for audiod's :8091 `/` endpoint exposed at
    `/api/audiod/stream` so the browser SPA can hit a single origin.
    """
    try:
        upstream = socket.create_connection((upstream_host, upstream_port), timeout=5)
    except OSError as e:
        self._send_json(502, {"error": "upstream unreachable", "detail": str(e), "upstream": f"{upstream_host}:{upstream_port}"})
        return

    # Rebuild the request-line. self.raw_requestline includes the path the
    # browser sent (e.g. b"GET /api/audiod/stream HTTP/1.1\r\n"). Replace
    # just the URI.
    raw = self.raw_requestline
    if not raw:
        upstream.close()
        self._send_json(502, {"error": "malformed request", "detail": "empty request line"})
        return
    try:
        first_line = raw.split(b" ", 2)
        if len(first_line) < 3:
            upstream.close()
            self._send_json(502, {"error": "malformed request", "detail": "bad request line"})
            return
        method = first_line[0]
        version = first_line[2]
        rewritten = b" ".join([method, upstream_path.encode("ascii"), version])
    except Exception as e:
        upstream.close()
        self._send_json(502, {"error": "malformed request", "detail": str(e)})
        return

    try:
        upstream.sendall(rewritten)
        # Replay the rest of the headers verbatim. http.server has already
        # consumed the request line; remaining headers live in self.headers
        # but we want byte-exact replay including any non-ASCII edge cases.
        # For our supported browser clients, reconstructing from self.headers
        # is sufficient and avoids re-reading self.rfile (which the parent
        # handler has not exposed).
        header_lines = []
        for k, v in self.headers.items():
            if k.lower() == "host":
                # Connection-managed: drop because we opened a fresh upstream socket.
                continue
            header_lines.append(f"{k}: {v}".encode("latin-1"))
        upstream.sendall(b"\r\n".join(header_lines) + b"\r\n\r\n")
    except OSError as e:
        upstream.close()
        try:
            self._send_json(502, {"error": "upstream write failed", "detail": str(e)})
        except Exception:
            pass
        return

    # Read the upstream handshake response and relay it to the client.
    try:
        upstream.settimeout(5)
        buf = b""
        while b"\r\n\r\n" not in buf:
            chunk = upstream.recv(4096)
            if not chunk:
                raise ConnectionError("upstream closed during handshake")
            buf += chunk
            if len(buf) > 65536:
                raise ConnectionError("upstream handshake too large")
        head, _, _rest = buf.partition(b"\r\n\r\n")
        head_line = head.split(b"\r\n", 1)[0].decode("latin-1", errors="replace")
        # Reject anything that isn't a 101 Switching Protocols
        if " 101 " not in head_line:
            upstream.close()
            self._send_json(502, {"error": "upstream not a websocket", "detail": head_line})
            return
        # Send the response verbatim to the client
        self.wfile.write(buf)
        self.wfile.flush()
    except Exception as e:
        upstream.close()
        try:
            self._send_json(502, {"error": "upstream handshake failed", "detail": str(e)})
        except Exception:
            pass
        return

    # Bridge bytes both ways. Disable Nagle on both sides for low-latency audio events.
    try:
        upstream.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    except OSError:
        pass
    try:
        self.connection.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    except OSError:
        pass

    client_sock = self.connection
    socks = [client_sock, upstream]

    def _pump(src, dst):
        try:
            while True:
                data = src.recv(4096)
                if not data:
                    break
                dst.sendall(data)
        except OSError:
            pass
        finally:
            try:
                dst.shutdown(socket.SHUT_WR)
            except OSError:
                pass

    t = threading.Thread(target=_pump, args=(upstream, client_sock), daemon=True)
    t.start()
    try:
        _pump(client_sock, upstream)
    finally:
        try:
            client_sock.shutdown(socket.SHUT_WR)
        except OSError:
            pass
        upstream.close()


def _serve_audiod_proxy(self: "SPAHandler") -> None:
    """Handle /api/audiod/<path>. Returns 502 if the daemon is down."""
    parsed = urlparse(self.path)
    subpath = parsed.path[len("/api/audiod"):] or "/"

    if subpath in ("/help", "/"):
        self._send_json(200, {
            "http_upstream": AUDIOD_HTTP,
            "ws_upstream": AUDIOD_WS,
            "routes": {
                "GET /api/audiod/health": "audiod liveness",
                "GET /api/audiod/status": "full diagnostics",
                "GET /api/audiod/config": "effective config",
                "POST /api/audiod/start": "start capture",
                "POST /api/audiod/stop": "stop capture",
                "POST /api/audiod/restart": "stop+start",
                "POST /api/audiod/ptt": "force push-to-talk segment",
                "POST /api/audiod/reload": "re-read config.yaml",
            },
            "ws": "WebSocket upgrade to /api/audiod/stream is proxied to " + AUDIOD_WS,
        })
        return

    if subpath == "/stream":
        return _serve_ws_upgrade(self, AUDIOD_WS_HOST, AUDIOD_WS_PORT, "/stream")

    parsed = urlparse(self.path)
    return _forward_to_upstream(self, AUDIOD_HTTP, subpath, parsed.query)


def _serve_perceptiond_proxy(self: "SPAHandler") -> None:
    """Handle /api/perceptiond/<path>. Returns 502 if the daemon is down.

    Routes forwarded (HTTP):
      GET    /api/perceptiond/health
      GET    /api/perceptiond/status
      GET    /api/perceptiond/descriptions?count=N
      GET    /api/perceptiond/frame.jpg   (single JPEG snapshot)
      GET    /api/perceptiond/frames/<image_id>.jpg  (per-event thumbnail; older ids may be evicted)
      GET    /api/perceptiond/events      (Server-Sent Events stream of new descriptions; replay of last 20)
      GET    /api/perceptiond/stats       (v7.0 telemetry summary: scene_skips, vlm_pass_rate, etc.)
      POST   /api/perceptiond/mode        (body: {"mode": "idle"|"watchful"|"active"})

    Note: /stream is intentionally NOT proxied. MJPEG is a long-lived
    multipart/x-mixed-replace stream; proxying it through this server
    would buffer it and break the live viewfinder. The SPA's <img> tag
    hits PERCEPTIOND_HTTP/stream directly when running outside Tauri.
    Inside the Tauri webview (production) the stream command is exposed
    separately on the Tauri bridge.

    The /events endpoint is a Server-Sent Events stream. It is forwarded
    to the upstream as a regular HTTP GET; SSE works over plain HTTP and
    the proxy does not buffer it (chunked transfer).
    """
    parsed = urlparse(self.path)
    subpath = parsed.path[len("/api/perceptiond"):] or "/"

    if subpath in ("/help", "/"):
        self._send_json(200, {
            "http_upstream": PERCEPTIOND_HTTP,
            "routes": {
                "GET /api/perceptiond/health": "perceptiond liveness",
                "GET /api/perceptiond/status": "running mode, frame counters, VLM queue, scene-gate telemetry",
                "GET /api/perceptiond/descriptions?count=N": "last N descriptions",
                "GET /api/perceptiond/frame.jpg": "single JPEG snapshot of latest frame",
                "GET /api/perceptiond/frames/<image_id>.jpg": "per-event thumbnail (ring-buffered, may be evicted)",
                "GET /api/perceptiond/events": "SSE stream of new descriptions (replays last 20 on connect)",
                "GET /api/perceptiond/stats": "v7.0 telemetry (scene_skips, vlm_pass_rate, skip_rate, scene_gate stats)",
                "POST /api/perceptiond/mode": "set mode (idle|watchful|active)",
            },
            "stream": "Live MJPEG at " + PERCEPTIOND_HTTP + "/stream (not proxied — connect directly)",
        })
        return

    return _forward_to_upstream(self, PERCEPTIOND_HTTP, subpath, parsed.query)


# Upstream base URLs for the /api/services/health aggregator. The order here
# is the order in which results are returned to the client. The wizard's
# `ALL_SERVICES` step list mirrors this set.
HEALTH_AGGREGATOR_SERVICES = (
    ("memoryd", MEMORYD_HTTP),
    ("toold", TOOLD_HTTP),
    ("ttsd", TTSD_HTTP),
    ("audiod", AUDIOD_HTTP),
    ("perceptiond", PERCEPTIOND_HTTP),
)
HEALTH_AGGREGATOR_TIMEOUT_S = 2.0
# Single shared executor for fan-out. 8 workers > 5 daemons so the aggregator
# never queues. Threads exit when the process exits; we don't reuse the
# executor for any other purpose.
_HEALTH_EXECUTOR = ThreadPoolExecutor(
    max_workers=max(8, len(HEALTH_AGGREGATOR_SERVICES) + 3),
    thread_name_prefix="health-agg",
)


def _probe_health(name: str, base: str, timeout: float = HEALTH_AGGREGATOR_TIMEOUT_S) -> dict:
    """Probe a single daemon's /health endpoint. Never raises — always returns a dict.

    Result shape:
      {"service": name, "upstream": base, "ok": bool, "status": int|null,
       "latency_ms": int, "body": dict|None, "error": str|None}
    """
    url = base.rstrip("/") + "/health"
    started = time.monotonic()
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            body_bytes = resp.read()
            latency = int((time.monotonic() - started) * 1000)
            try:
                body = json.loads(body_bytes.decode("utf-8", errors="replace"))
            except (ValueError, UnicodeDecodeError):
                body = None
            return {
                "service": name,
                "upstream": base,
                "ok": 200 <= resp.status < 300,
                "status": resp.status,
                "latency_ms": latency,
                "body": body,
                "error": None,
            }
    except urllib.error.HTTPError as e:
        latency = int((time.monotonic() - started) * 1000)
        try:
            body = json.loads(e.read().decode("utf-8", errors="replace")) if e.fp else None
        except Exception:
            body = None
        return {
            "service": name,
            "upstream": base,
            "ok": False,
            "status": e.code,
            "latency_ms": latency,
            "body": body,
            "error": f"upstream HTTP {e.code}",
        }
    except (urllib.error.URLError, ConnectionError, TimeoutError, OSError) as e:
        latency = int((time.monotonic() - started) * 1000)
        return {
            "service": name,
            "upstream": base,
            "ok": False,
            "status": None,
            "latency_ms": latency,
            "body": None,
            "error": str(e) or type(e).__name__,
        }


def _serve_services_health(self: "SPAHandler") -> None:
    """GET /api/services/health — fan out to every backend's /health concurrently.

    Response shape:
      {
        "ok": bool,                            # true iff every service is up
        "up_count": int,
        "down_count": int,
        "total_latency_ms": int,               # wall-clock from first to last result
        "services": {                          # keyed by service name for fast lookup
          "memoryd":   {"ok": bool, "status": int|null, "latency_ms": int,
                         "body": dict|None, "error": str|None, "upstream": str},
          ...
        },
        "results": [...],                      # same payload in declared order
        "ts": float                            # server time of aggregation (epoch seconds)
      }

    The aggregator always returns 200 — the per-service `ok` fields are
    what callers branch on. Returning 200 even when downstreams are down
    lets a single fetch drive the wizard UI without extra retry logic.
    """
    started = time.monotonic()
    futures = {
        _HEALTH_EXECUTOR.submit(_probe_health, name, base): name
        for name, base in HEALTH_AGGREGATOR_SERVICES
    }
    # Preserve declared order in `results`. Use a dict to dedupe.
    results_by_name: dict[str, dict] = {}
    for fut in as_completed(futures, timeout=HEALTH_AGGREGATOR_TIMEOUT_S + 1.0):
        name = futures[fut]
        try:
            results_by_name[name] = fut.result()
        except Exception as e:  # never expected — _probe_health catches everything
            results_by_name[name] = {
                "service": name,
                "ok": False,
                "status": None,
                "latency_ms": -1,
                "body": None,
                "error": f"probe crashed: {e!r}",
            }
    results = [results_by_name[name] for name, _ in HEALTH_AGGREGATOR_SERVICES if name in results_by_name]
    services = {r["service"]: r for r in results}
    up = sum(1 for r in results if r["ok"])
    down = len(results) - up
    self._send_json(200, {
        "ok": down == 0,
        "up_count": up,
        "down_count": down,
        "total_latency_ms": int((time.monotonic() - started) * 1000),
        "services": services,
        "results": results,
        "ts": time.time(),
    })


def _serve_memoryd_proxy(self: "SPAHandler") -> None:
    """Handle /api/memoryd/<path>. Forwards HTTP to memoryd on :8741."""
    parsed = urlparse(self.path)
    subpath = parsed.path[len("/api/memoryd"):] or "/"
    if subpath in ("/help", "/"):
        self._send_json(200, {
            "http_upstream": MEMORYD_HTTP,
            "routes": {
                "GET /api/memoryd/health": "memoryd liveness",
                "GET /api/memoryd/ready": "memoryd readiness (model loaded + db reachable)",
                "GET /api/memoryd/stats": "counts by memory type + db size",
                "POST /api/memoryd/memories": "store a memory",
                "POST /api/memoryd/conversations": "store a conversation turn",
                "GET /api/memoryd/query?text=...&top_k=5": "semantic similarity search",
                "GET /api/memoryd/memories?type=episodic": "list memories",
                "GET /api/memoryd/memories/by-type/{type}": "list memories by type",
                "GET /api/memoryd/memories/{id}": "fetch one memory",
                "DELETE /api/memoryd/memories/{id}": "delete one memory",
                "POST /api/memoryd/v1/embeddings": "OpenAI-compatible embeddings",
            },
        })
        return
    parsed = urlparse(self.path)
    return _forward_to_upstream(self, MEMORYD_HTTP, subpath, parsed.query)


def _serve_toold_proxy(self: "SPAHandler") -> None:
    """Handle /api/toold/<path>. Forwards HTTP to toold on :8742."""
    parsed = urlparse(self.path)
    subpath = parsed.path[len("/api/toold"):] or "/"
    if subpath in ("/help", "/"):
        self._send_json(200, {
            "http_upstream": TOOLD_HTTP,
            "routes": {
                "GET /api/toold/health": "toold liveness",
                "GET /api/toold/ready": "toold readiness (registry loaded)",
                "GET /api/toold/test": "self-test (shell + python + file + registry)",
                "POST /api/toold/exec": "execute shell command",
                "POST /api/toold/exec/python": "execute inline python",
                "POST /api/toold/exec/file": "execute saved script file",
                "POST /api/toold/exec/with-tool": "execute via named tool from registry",
                "GET /api/toold/registry": "list registered tools",
                "POST /api/toold/registry/tools": "register a new tool",
                "POST /api/toold/registry/{name}/enable": "enable a tool",
                "POST /api/toold/registry/{name}/disable": "disable a tool",
            },
        })
        return
    parsed = urlparse(self.path)
    return _forward_to_upstream(self, TOOLD_HTTP, subpath, parsed.query)


def _serve_ttsd_proxy(self: "SPAHandler") -> None:
    """Handle /api/ttsd/<path>. Forwards HTTP to ttsd on :8743.

    /speak and /play return binary WAV — _forward_to_upstream passes the body
    through with the upstream Content-Type so the browser gets audio/wav.
    """
    parsed = urlparse(self.path)
    subpath = parsed.path[len("/api/ttsd"):] or "/"
    if subpath in ("/help", "/"):
        self._send_json(200, {
            "http_upstream": TTSD_HTTP,
            "routes": {
                "GET /api/ttsd/health": "ttsd liveness",
                "GET /api/ttsd/voices": "list supported KittenTTS voices",
                "GET /api/ttsd/models": "list supported KittenTTS models",
                "POST /api/ttsd/speak": "synthesize → audio/wav body",
                "POST /api/ttsd/play": "synthesize + aplay on server (no body)",
            },
        })
        return
    return _forward_to_upstream(self, TTSD_HTTP, subpath, parsed.query)


def _send_json(self: "SPAHandler", status: int, obj: dict) -> None:
    body = json.dumps(obj).encode()
    self.send_response(status)
    self.send_header("Content-Type", "application/json")
    self.send_header("Content-Length", str(len(body)))
    self.send_header("Access-Control-Allow-Origin", "*")
    self.end_headers()
    self.wfile.write(body)


class SPAHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIST, **kwargs)

    # Bind helper methods onto the class so the proxy handlers can use them.
    _send_json = _send_json

    def do_OPTIONS(self):
        # CORS preflight for the /api/audiod and /api/perceptiond proxies.
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        if self.path.startswith("/api/services/health"):
            return _serve_services_health(self)
        if self.path.startswith("/api/audiod"):
            return _serve_audiod_proxy(self)
        if self.path.startswith("/api/perceptiond"):
            return _serve_perceptiond_proxy(self)
        if self.path.startswith("/api/memoryd"):
            return _serve_memoryd_proxy(self)
        if self.path.startswith("/api/toold"):
            return _serve_toold_proxy(self)
        if self.path.startswith("/api/ttsd"):
            return _serve_ttsd_proxy(self)
        # Serve static/ files (demo pages) when present. Loaded as a sibling
        # of the React dist, this keeps the build output clean while letting
        # us host non-React demos (audiod_demo.html, perceptiond_demo.html)
        # on the same origin.
        static_path = os.path.normpath(os.path.join(STATIC_DIR, self.path.lstrip("/")))
        if (
            static_path.startswith(os.path.normpath(STATIC_DIR))
            and os.path.isfile(static_path)
            and "." in os.path.basename(self.path.split("?")[0])
        ):
            ctype = self.guess_type(static_path)
            try:
                with open(static_path, "rb") as f:
                    data = f.read()
                self.send_response(200)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(data)))
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(data)
                return
            except OSError as e:
                self._send_json(500, {"error": "static read failed", "detail": str(e)})
                return
        # SPA fallback
        path = self.translate_path(self.path)
        if not os.path.exists(path) and "." not in os.path.basename(self.path.split("?")[0]):
            self.path = "/index.html"
        return super().do_GET()

    def do_POST(self):
        if self.path.startswith("/api/audiod"):
            return _serve_audiod_proxy(self)
        if self.path.startswith("/api/perceptiond"):
            return _serve_perceptiond_proxy(self)
        if self.path.startswith("/api/memoryd"):
            return _serve_memoryd_proxy(self)
        if self.path.startswith("/api/toold"):
            return _serve_toold_proxy(self)
        if self.path.startswith("/api/ttsd"):
            return _serve_ttsd_proxy(self)
        self.send_error(404, "POST not supported on static assets")

    def end_headers(self):
        # CORS so the wizard can hit memoryd/toold/ttsd from a different origin
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, format, *args):
        sys.stderr.write(f"[dan-glasses-app] {self.address_string()} {format % args}\n")


def main():
    if not os.path.isdir(DIST):
        print(f"FATAL: dist dir not found: {DIST}", file=sys.stderr)
        sys.exit(1)
    with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), SPAHandler) as httpd:
        httpd.allow_reuse_address = True
        print(f"[dan-glasses-app] serving {DIST} on :{PORT}", flush=True)
        print(f"[dan-glasses-app] audiod proxy: {AUDIOD_HTTP} (ws: {AUDIOD_WS})", flush=True)
        print(f"[dan-glasses-app] perceptiond proxy: {PERCEPTIOND_HTTP}", flush=True)
        print(f"[dan-glasses-app] memoryd proxy: {MEMORYD_HTTP}", flush=True)
        print(f"[dan-glasses-app] toold proxy: {TOOLD_HTTP}", flush=True)
        print(f"[dan-glasses-app] ttsd proxy: {TTSD_HTTP}", flush=True)
        httpd.serve_forever()


if __name__ == "__main__":
    main()