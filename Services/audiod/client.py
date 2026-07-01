"""audiod client — sync HTTP control + async WebSocket transcript stream.

Used by the dan-glasses-app (Tauri v2 + React frontend) to drive audiod
without depending on its HTTP server internals.

Two surfaces:

    AudiodClient       sync HTTP, mirrors the audiod control plane
                       (/health /status /config /start /stop /restart /ptt /reload)

    AudiodStream       async WS subscriber on the transcript fan-out port
                       (default :8091). Wraps `websockets` and yields parsed
                       transcript dicts.

Both are pure stdlib + `websockets`. No audiod-internal imports, so this
file can live anywhere on disk and still run against a remote audiod.
"""
from __future__ import annotations

import asyncio
import json
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any, AsyncIterator, Awaitable, Callable, Optional


DEFAULT_HTTP_HOST = "127.0.0.1"
DEFAULT_HTTP_PORT = 8090
DEFAULT_WS_PORT = 8091
HTTP_TIMEOUT_S = 5.0


class AudiodError(RuntimeError):
    """Raised when audiod returns a non-2xx response or the connection fails."""

    def __init__(self, status: int, body: str, url: str):
        super().__init__(f"audiod HTTP {status} on {url}: {body[:200]}")
        self.status = status
        self.body = body
        self.url = url


@dataclass
class AudiodConfig:
    """Connection settings for an audiod deployment."""

    host: str = DEFAULT_HTTP_HOST
    http_port: int = DEFAULT_HTTP_PORT
    ws_port: int = DEFAULT_WS_PORT
    timeout_s: float = HTTP_TIMEOUT_S

    @property
    def http_base(self) -> str:
        return f"http://{self.host}:{self.http_port}"

    @property
    def ws_url(self) -> str:
        return f"ws://{self.host}:{self.ws_port}/"


class AudiodClient:
    """Sync HTTP client over audiod's control plane.

    Designed for use from non-async callers (Tauri command handlers,
    CLI scripts, tests). All methods map 1:1 to an audiod HTTP route.

    Example:

        c = AudiodClient()
        if not c.health()["status"] == "ok":
            raise SystemExit("audiod not running")
        c.start()
        for ev in AudiodStream().events():
            print(ev["text"])
    """

    def __init__(self, config: Optional[AudiodConfig] = None):
        self.cfg = config or AudiodConfig()

    # --- transport ---------------------------------------------------------

    def _request(self, method: str, path: str) -> dict[str, Any]:
        url = f"{self.cfg.http_base}{path}"
        req = urllib.request.Request(url, method=method)
        try:
            with urllib.request.urlopen(req, timeout=self.cfg.timeout_s) as resp:
                raw = resp.read().decode("utf-8")
                if resp.status < 200 or resp.status >= 300:
                    raise AudiodError(resp.status, raw, url)
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            raise AudiodError(e.code, body, url) from None
        except urllib.error.URLError as e:
            raise AudiodError(0, str(e.reason), url) from None

    # --- control plane -----------------------------------------------------

    def health(self) -> dict[str, Any]:
        return self._request("GET", "/health")

    def status(self) -> dict[str, Any]:
        return self._request("GET", "/status")

    def config(self) -> dict[str, Any]:
        return self._request("GET", "/config")

    def start(self) -> dict[str, Any]:
        return self._request("POST", "/start")

    def stop(self) -> dict[str, Any]:
        return self._request("POST", "/stop")

    def restart(self) -> dict[str, Any]:
        return self._request("POST", "/restart")

    def ptt(self) -> dict[str, Any]:
        """Fire the push-to-talk trigger. No-op when PTT is disabled in audiod config."""
        return self._request("POST", "/ptt")

    def reload(self) -> dict[str, Any]:
        """Re-read audiod's config.yaml from disk."""
        return self._request("POST", "/reload")

    # --- convenience -------------------------------------------------------

    def is_healthy(self) -> bool:
        try:
            return self.health().get("status") == "ok"
        except AudiodError:
            return False

    def is_running(self) -> bool:
        try:
            return bool(self.status().get("running"))
        except AudiodError:
            return False


class AudiodStream:
    """Async subscriber for audiod's transcript WebSocket fan-out.

    Yields parsed transcript dicts:

        {
            "type": "transcript",
            "session_id": "...",
            "event_id": "...",
            "seq": 42,
            "text": "what was said",
            "start_ms": 1234,
            "end_ms": 5678,
            "confidence": 0.92,
            "ts_ms": 1730000000000
        }

    Usage:

        async for ev in AudiodStream().events():
            print(ev["text"])

    Or with a callback:

        stream = AudiodStream(on_event=lambda ev: print(ev["text"]))
        await stream.run_forever()
    """

    def __init__(
        self,
        config: Optional[AudiodConfig] = None,
        on_event: Optional[Callable[[dict[str, Any]], None]] = None,
    ):
        self.cfg = config or AudiodConfig()
        self.on_event = on_event
        self._stop = asyncio.Event()

    async def events(self) -> AsyncIterator[dict[str, Any]]:
        """Yield transcript events until the caller cancels or the WS drops."""
        import websockets  # local import — optional dep, only needed for streams

        async with websockets.connect(self.cfg.ws_url) as ws:
            while not self._stop.is_set():
                raw = await ws.recv()
                if isinstance(raw, bytes):
                    raw = raw.decode("utf-8")
                try:
                    ev = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                if ev.get("type") != "transcript":
                    continue
                if self.on_event is not None:
                    try:
                        self.on_event(ev)
                    except Exception:  # pragma: no cover — callback errors must not kill the stream
                        pass
                yield ev

    async def run_forever(self) -> None:
        """Consume events forever; cancel-safe via `stop()`."""
        async for _ in self.events():
            pass

    def stop(self) -> None:
        self._stop.set()


# Convenience top-level handles for ad-hoc scripts ----------------------------

def connect(host: str = DEFAULT_HTTP_HOST, http_port: int = DEFAULT_HTTP_PORT) -> AudiodClient:
    """Build a client aimed at a specific audiod deployment."""
    return AudiodClient(AudiodConfig(host=host, http_port=http_port))


async def stream(
    host: str = DEFAULT_HTTP_HOST,
    ws_port: int = DEFAULT_WS_PORT,
    on_event: Optional[Callable[[dict[str, Any]], None]] = None,
) -> AsyncIterator[dict[str, Any]]:
    """Async generator over transcripts from a specific audiod."""
    cfg = AudiodConfig(host=host, ws_port=ws_port)
    async for ev in AudiodStream(config=cfg, on_event=on_event).events():
        yield ev