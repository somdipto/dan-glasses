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
from urllib import request as _urlrequest
from urllib.error import URLError, HTTPError


RING_BUFFER_SIZE = 200  # max descriptions held in memory
FRAME_BUFFER_SIZE = 50   # max per-event JPEGs (thumbnails) kept for /frames/<id>.jpg

# v7.0 — SSE /events pub-sub
EVENT_BUS_REPLAY = 20         # last N descriptions replayed to a new subscriber
EVENT_BUS_PER_SUBSCRIBER = 64 # per-subscriber bounded queue (overwrite-on-full)

# v8.0 — memoryd ingest hook
MEMORY_SINK_QUEUE_CAP = 256   # bounded cross-daemon queue (overwrite-on-full)
MEMORY_SINK_TIMEOUT = 2.0     # per-request HTTP timeout (seconds) — tight, daemon must stay live


class MemorySink:
    """v8.0 — fire-and-forget HTTP forwarder to memoryd.

    Each published description is also POSTed to `memoryd_url` (e.g.
    `http://127.0.0.1:8090/memories`) as an `episodic` memory. Runs on a
    background thread with a bounded queue so the VLM/publisher hot path
    is never blocked by an unhealthy or slow memoryd. Counters exposed
    via `stats()` and `/status` for observability.
    """

    def __init__(
        self,
        url: Optional[str] = None,
        queue_cap: int = MEMORY_SINK_QUEUE_CAP,
        timeout: float = MEMORY_SINK_TIMEOUT,
    ):
        self._url = url
        self._queue_cap = max(1, queue_cap)
        self._timeout = max(0.1, float(timeout))
        self._queue: Deque[dict] = deque(maxlen=self._queue_cap)
        self._lock = threading.Lock()
        self._sent = 0
        self._dropped = 0
        self._errors = 0
        self._enabled = bool(url)
        self._stop = threading.Event()
        self._thread: Optional[threading.Thread] = None
        if self._enabled:
            self._thread = threading.Thread(
                target=self._run, name="perceptiond-memory-sink", daemon=True
            )
            self._thread.start()

    @property
    def enabled(self) -> bool:
        return self._enabled

    def submit(self, event: dict) -> None:
        """Enqueue an event for delivery. Non-blocking, overwrites oldest on overflow."""
        if not self._enabled:
            return
        with self._lock:
            # Bounded queue — if full, drop oldest and count it.
            if len(self._queue) >= self._queue_cap:
                self._dropped += 1
            self._queue.append(dict(event))

    def _drain_one(self) -> Optional[dict]:
        with self._lock:
            if not self._queue:
                return None
            return self._queue.popleft()

    def _post(self, payload: dict) -> bool:
        if not self._url:
            return False
        try:
            data = json.dumps(payload).encode("utf-8")
            req = _urlrequest.Request(
                self._url,
                data=data,
                method="POST",
                headers={"Content-Type": "application/json", "Accept": "application/json"},
            )
            with _urlrequest.urlopen(req, timeout=self._timeout) as resp:
                # memoryd returns 200 on /memories POST; anything in [200,300) is OK.
                if 200 <= resp.status < 300:
                    return True
                with self._lock:
                    self._errors += 1
                return False
        except (HTTPError, URLError, TimeoutError, OSError):
            with self._lock:
                self._errors += 1
            return False

    def _run(self) -> None:
        # Single consumer thread. Polls the queue on a short interval so we
        # exit promptly on shutdown but don't busy-spin when idle.
        while not self._stop.is_set():
            event = self._drain_one()
            if event is None:
                self._stop.wait(0.1)
                continue
            if self._post(event):
                with self._lock:
                    self._sent += 1
            else:
                with self._lock:
                    # _post already incremented _errors; nothing else to do.
                    pass

    def stats(self) -> dict:
        with self._lock:
            return {
                "enabled": self._enabled,
                "url": self._url,
                "queued": len(self._queue),
                "queue_cap": self._queue_cap,
                "sent": self._sent,
                "dropped": self._dropped,
                "errors": self._errors,
            }

    def close(self) -> None:
        self._stop.set()
        if self._thread and self._thread.is_alive() and self._thread is not threading.current_thread():
            self._thread.join(timeout=2.0)


class EventBus:
    """In-process pub/sub for live description streaming.

    Each subscriber gets a private bounded deque. On attach, the bus replays
    the last N events from the publisher's ring buffer so the new client
    renders history immediately. New events from `publish()` are fanned out
    synchronously under a short lock; if a subscriber's queue is full, the
    oldest entry is dropped to keep the publisher's hot path non-blocking.
    """

    def __init__(self, replay: int = EVENT_BUS_REPLAY, per_subscriber_cap: int = EVENT_BUS_PER_SUBSCRIBER):
        self._lock = threading.Lock()
        self._subscribers: List[deque] = []
        self._replay = max(0, replay)
        self._per_subscriber_cap = max(1, per_subscriber_cap)

    def attach(self, ring) -> tuple:
        """Register a new subscriber; return (queue, replay_count)."""
        q: Deque[dict] = deque(maxlen=self._per_subscriber_cap)
        with self._lock:
            self._subscribers.append(q)
            replay_items = list(ring)[-self._replay:]
        for item in replay_items:
            q.append(item)
        return q, len(replay_items)

    def detach(self, q) -> None:
        with self._lock:
            try:
                self._subscribers.remove(q)
            except ValueError:
                pass

    def publish(self, event: dict) -> None:
        """Fan out an event to every live subscriber; non-blocking."""
        with self._lock:
            subs = list(self._subscribers)
        for q in subs:
            # Bounded queue drops oldest when full, so we never block here.
            q.append(dict(event))

    def subscriber_count(self) -> int:
        with self._lock:
            return len(self._subscribers)


class FrameStore:
    """Thread-safe ring buffer of per-event JPEG bytes keyed by image_id.

    Bounded by FRAME_BUFFER_SIZE (insertion-ordered; oldest evicted first)
    in memory, and by `max_bytes` on disk (LRU eviction). Used to back
    GET /frames/<image_id>.jpg so the UI can show what the VLM saw.

    v9.0: also tracks the per-event salience bboxes (list of
    [x, y, w, h, kind]) alongside each JPEG so the GET handler can paint
    the rectangles onto the thumbnail on demand. Old `put()` callers
    that omit bboxes still work — the entry is stored with bboxes=[].

    v10.0: optional disk persistence. When `image_dir` is set, every
    accepted put also writes `<image_id>.jpg` and `<image_id>.json`
    (bboxes) under that directory. `get()` falls back to the disk copy
    when the in-memory entry has been evicted, so memoryd's image_id
    references stay resolvable across process restarts and across the
    in-memory ring being overrun. Disk is bounded by `max_bytes`; oldest
    files are deleted (LRU) when the budget is exceeded. All disk I/O
    is best-effort: a failed write must NOT fail the in-memory put.
    """

    def __init__(
        self,
        capacity: int = FRAME_BUFFER_SIZE,
        image_dir: "str | os.PathLike | None" = None,
        max_bytes: int = 200 * 1024 * 1024,  # 200 MiB
    ):
        self._capacity = capacity
        self._image_dir = None
        self._max_bytes = max(0, int(max_bytes))
        self._lock = threading.Lock()
        # Python 3.7+ dict preserves insertion order - used as ordered map.
        self._frames = {}  # image_id -> jpeg bytes
        self._bboxes = {}  # image_id -> list of [x, y, w, h, kind]
        # Disk bookkeeping
        self._disk_bytes = 0
        self._disk_index: "dict[str, float]" = {}  # image_id -> mtime (LRU)
        self._disk_sizes: "dict[str, int]" = {}    # image_id -> total on-disk bytes (jpg + sidecar)
        self._evictions_disk = 0
        self._hits_memory = 0
        self._hits_disk = 0
        self._misses = 0
        if image_dir is not None:
            try:
                p = os.fspath(image_dir)
                os.makedirs(p, exist_ok=True)
                self._image_dir = p
            except OSError:
                # Disk persistence is opt-in best-effort; fall back to
                # in-memory only if we can't create the directory.
                self._image_dir = None
        # v10.0: when image_dir is None, max_bytes is forced to 0 so the
        # disk-write code path is a complete no-op. When image_dir is
        # provided, the caller's value is respected.
        if self._image_dir is None:
            self._max_bytes = 0

    # ---------- internal helpers ----------

    def _disk_path(self, image_id: str, suffix: str) -> str:
        assert self._image_dir is not None
        return os.path.join(self._image_dir, f"{image_id}{suffix}")

    def _normalize_bboxes(self, bboxes) -> list:
        """Return [[x, y, w, h, kind], ...] or []."""
        norm: list = []
        if not bboxes:
            return norm
        for bb in bboxes:
            try:
                if isinstance(bb, dict):
                    x = int(bb["x"]); y = int(bb["y"])
                    w = int(bb["w"]); h = int(bb["h"])
                    kind = str(bb.get("kind", "region"))
                elif len(bb) >= 4:
                    x, y, w, h = (int(v) for v in bb[:4])
                    kind = str(bb[4]) if len(bb) >= 5 else "region"
                else:
                    continue
                if w > 0 and h > 0:
                    norm.append([x, y, w, h, kind])
            except (TypeError, ValueError, KeyError):
                continue
        return norm

    def _validate(self, image_id: str, jpeg: bytes) -> bool:
        if not image_id or jpeg is None or len(jpeg) < 2 or jpeg[:2] != b"\xff\xd8":
            return False
        # Hex-safety is enforced at the HTTP boundary (handler's regex
        # check). The in-memory API accepts any non-empty string so
        # tests can use descriptive keys.
        return True

    def _evict_inmem(self) -> None:
        if len(self._frames) > self._capacity:
            oldest = next(iter(self._frames))
            self._frames.pop(oldest, None)
            self._bboxes.pop(oldest, None)

    def _write_disk(self, image_id: str, jpeg: bytes, bboxes: list) -> None:
        """Best-effort write of JPEG + sidecar. Updates index + byte count.
        Enforces `max_bytes` via LRU eviction. Never raises."""
        if self._image_dir is None or self._max_bytes == 0:
            return
        # v10.0: only hex image_ids touch disk so we never write a path
        # like `../etc/passwd` if the in-memory API is called with a
        # non-hex string. (The HTTP /frames/<id>.jpg handler validates
        # hex too, but the disk path is an additional safety net.)
        if not image_id or not all(c in "0123456789abcdef" for c in image_id):
            return
        try:
            jpg_path = self._disk_path(image_id, ".jpg")
            json_path = self._disk_path(image_id, ".json")
            with open(jpg_path, "wb") as f:
                f.write(jpeg)
            with open(json_path, "w") as f:
                json.dump(bboxes, f)
            sidecar_size = os.path.getsize(json_path)
            size = len(jpeg) + sidecar_size
            with self._lock:
                prev = self._disk_sizes.get(image_id)
                if prev is not None:
                    self._disk_bytes = max(0, self._disk_bytes - prev)
                self._disk_sizes[image_id] = size
                self._disk_bytes += size
                self._disk_index[image_id] = time.time()
                self._enforce_budget_locked()
        except OSError:
            # Disk full, permission denied, race with another writer — ignore.
            pass

    def _enforce_budget_locked(self) -> None:
        """LRU-evict disk entries until `_disk_bytes <= _max_bytes`."""
        guard = 0
        while self._disk_bytes > self._max_bytes and self._disk_index and guard < 10_000:
            guard += 1
            oldest_id = next(iter(self._disk_index))
            popped_size = self._disk_sizes.pop(oldest_id, 0)
            self._disk_index.pop(oldest_id, None)
            try:
                os.unlink(self._disk_path(oldest_id, ".jpg"))
            except OSError:
                pass
            try:
                os.unlink(self._disk_path(oldest_id, ".json"))
            except OSError:
                pass
            # Subtract from the running byte count so the loop terminates
            # once the budget is satisfied, not when the index is empty.
            self._disk_bytes = max(0, self._disk_bytes - popped_size)
            self._evictions_disk += 1

    def _read_disk(self, image_id: str):
        """Return (jpeg_bytes, bboxes) or (None, None) on miss / error."""
        if self._image_dir is None:
            return None, None
        jpg_path = self._disk_path(image_id, ".jpg")
        json_path = self._disk_path(image_id, ".json")
        try:
            with open(jpg_path, "rb") as f:
                jpeg = f.read()
            bboxes = []
            try:
                with open(json_path, "r") as f:
                    bboxes = json.load(f)
            except (OSError, ValueError):
                bboxes = []
            return jpeg, bboxes
        except OSError:
            return None, None

    # ---------- public API ----------

    def put(self, image_id: str, jpeg: bytes) -> None:
        """Store a JPEG under image_id; evict oldest in-memory if over capacity.
        Also writes to disk (if image_dir is set) so the image survives eviction."""
        if not self._validate(image_id, jpeg):
            return
        with self._lock:
            self._frames.pop(image_id, None)
            self._bboxes.pop(image_id, None)
            self._frames[image_id] = jpeg
            self._evict_inmem()
        # Disk write outside the in-memory critical section (slow I/O).
        self._write_disk(image_id, jpeg, [])

    def put_with_bboxes(
        self, image_id: str, jpeg: bytes, bboxes: Optional[list]
    ) -> None:
        """Store a JPEG + optional salience bboxes under image_id.

        Bboxes are normalised to a flat list of [x, y, w, h, kind] so the
        overlay renderer can iterate without special-casing the legacy
        "face rectangles" format. None / empty bboxes are stored as [].
        """
        if not self._validate(image_id, jpeg):
            return
        norm = self._normalize_bboxes(bboxes)
        with self._lock:
            self._frames.pop(image_id, None)
            self._bboxes.pop(image_id, None)
            self._frames[image_id] = jpeg
            self._bboxes[image_id] = norm
            self._evict_inmem()
        self._write_disk(image_id, jpeg, norm)

    def get(self, image_id: str):
        """Return JPEG bytes for image_id or None. Checks memory first,
        then falls back to disk (v10.0)."""
        with self._lock:
            data = self._frames.get(image_id)
        if data is not None:
            self._hits_memory += 1
            return data
        # Disk fallback
        if self._image_dir is not None:
            jpg_path = self._disk_path(image_id, ".jpg")
            try:
                with open(jpg_path, "rb") as f:
                    data = f.read()
                if data[:2] == b"\xff\xd8":
                    # Touch LRU mtime so a hit doesn't immediately get evicted.
                    self._disk_index[image_id] = time.time()
                    self._hits_disk += 1
                    return data
            except OSError:
                pass
        self._misses += 1
        return None

    def get_bboxes(self, image_id: str):
        """Return salience bboxes for image_id, or None if not stored.

        None is a sentinel meaning the entry was never tagged with
        bboxes (e.g. inserted via plain put()). Use this to distinguish
        from an empty list (an entry with zero detections).
        """
        with self._lock:
            if image_id in self._bboxes:
                return list(self._bboxes[image_id])
        # Disk fallback (v10.0): read sidecar JSON
        if self._image_dir is not None:
            json_path = self._disk_path(image_id, ".json")
            try:
                with open(json_path, "r") as f:
                    return json.load(f)
            except (OSError, json.JSONDecodeError):
                return None
        return None

    def __len__(self) -> int:
        with self._lock:
            return len(self._frames)

    def clear(self) -> None:
        with self._lock:
            self._frames.clear()
            self._bboxes.clear()

    def stats(self) -> dict:
        with self._lock:
            return {
                "files_on_disk": len(self._disk_index),
                "bytes_on_disk": self._disk_bytes,
                "evictions_disk": self._evictions_disk,
                "hits_memory": self._hits_memory,
                "hits_disk": self._hits_disk,
                "misses": self._misses,
                "image_dir": self._image_dir,
                "max_bytes": self._max_bytes,
                "capacity": self._capacity,
            }


# v9.0 — bounding-box overlay constants + helper
BBOX_KIND_COLOR = {
    "face": (0, 220, 60),       # green
    "motion": (255, 180, 0),    # amber
    "region": (255, 180, 0),    # amber (alias of motion)
}
BBOX_DEFAULT_COLOR = (0, 200, 255)  # cyan, used for unknown kinds


def _paint_bboxes(jpeg_bytes: bytes, bboxes: list, thumbnail_w: int = 320, thumbnail_h: int = 240) -> Optional[bytes]:
    """Return a new JPEG with salience rectangles drawn on the thumbnail.

    `jpeg_bytes` is the per-event thumbnail the pipeline already stores.
    `bboxes` may be either a dict (`{x, y, w, h, kind}`) or a list/tuple
    (`[x, y, w, h, kind]`); both shapes are produced by the salience
    detector and the legacy face list. Coordinates are in the *original*
    capture resolution and are scaled to the thumbnail before drawing.
    Returns None if PIL is unavailable or any frame-decode / draw step
    fails — the caller should fall back to the raw JPEG in that case.
    """
    try:
        from PIL import Image, ImageDraw  # noqa: F401
    except ImportError:
        return None
    try:
        from io import BytesIO

        img = Image.open(BytesIO(jpeg_bytes)).convert("RGB")
        scale_x = img.width / float(max(1, thumbnail_w))
        scale_y = img.height / float(max(1, thumbnail_h))
        if not bboxes:
            # No annotations — re-encode and ship the original thumbnail
            # untouched (Cache-Control, etc. unaffected).
            buf = BytesIO()
            img.save(buf, format="JPEG", quality=80)
            return buf.getvalue()
        draw = ImageDraw.Draw(img)
        for bb in bboxes:
            try:
                if isinstance(bb, dict):
                    x = int(bb.get("x", 0)); y = int(bb.get("y", 0))
                    w = int(bb.get("w", 0)); h = int(bb.get("h", 0))
                    kind = str(bb.get("kind", "region"))
                else:
                    x, y, w, h = (int(v) for v in bb[:4])
                    kind = str(bb[4]) if len(bb) >= 5 else "region"
            except (TypeError, ValueError):
                continue
            if w <= 0 or h <= 0:
                continue
            color = BBOX_KIND_COLOR.get(kind, BBOX_DEFAULT_COLOR)
            x0 = max(0, int(round(x * scale_x)))
            y0 = max(0, int(round(y * scale_y)))
            x1 = min(img.width - 1, int(round((x + w) * scale_x)))
            y1 = min(img.height - 1, int(round((y + h) * scale_y)))
            if x1 <= x0 or y1 <= y0:
                continue
            # Two-stroke outline for visibility on noisy frames.
            draw.rectangle([x0, y0, x1, y1], outline=color, width=2)
            draw.rectangle(
                [max(0, x0 - 1), max(0, y0 - 1), min(img.width - 1, x1 + 1), min(img.height - 1, y1 + 1)],
                outline=color,
                width=1,
            )
            # Small label badge in the top-left of the box.
            label = kind
            try:
                draw.text((x0 + 2, max(0, y0 - 11)), label, fill=color)
            except Exception:
                pass
        buf = BytesIO()
        img.save(buf, format="JPEG", quality=80)
        return buf.getvalue()
    except Exception as e:
        print(f"perceptiond: bbox overlay render error: {e}", flush=True)
        return None


class DescriptionPublisher:
    """Publish description events to stdout AND a thread-safe ring buffer."""

    def __init__(
        self,
        mode: str = "stdout",
        socket_path: str = "/var/run/perceptiond.sock",
        ring_size: int = RING_BUFFER_SIZE,
        memory_sink_url: Optional[str] = None,
        memory_sink_timeout: float = MEMORY_SINK_TIMEOUT,
        memory_sink_queue_cap: int = MEMORY_SINK_QUEUE_CAP,
    ):
        self.mode = mode
        self.socket_path = socket_path
        self._sock: Optional[socket.socket] = None
        self._event_count = 0
        self._lock = threading.Lock()
        self._ring: Deque[dict] = deque(maxlen=ring_size)
        # v7.0: in-process pub/sub for the /events SSE stream
        self.event_bus = EventBus()
        # v8.0: cross-daemon memoryd ingest hook (fire-and-forget)
        self.memory_sink = MemorySink(
            url=memory_sink_url,
            queue_cap=memory_sink_queue_cap,
            timeout=memory_sink_timeout,
        )

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
        """Publish a description event (stdout + ring buffer + memoryd sink)."""
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

        # v8.0: fan out to EventBus (SSE subscribers) AFTER stdout so a
        # broken sink can't delay the publish path; memoryd is also
        # non-blocking via its own bounded queue.
        self.event_bus.publish(event)
        if event.get("type") == "description" and event.get("description"):
            self.memory_sink.submit({
                "type": "episodic",
                "content": event["description"],
                "metadata": {
                    "source": "perceptiond",
                    "image_id": event.get("image_id"),
                    "trigger_kind": event.get("trigger_kind"),
                    "motion_score": event.get("motion_score"),
                    "timestamp": event.get("timestamp"),
                    "event_id": event.get("event_id"),
                },
            })

    def recent(self, count: int = 10) -> List[dict]:
        """Return last N descriptions (oldest first)."""
        with self._lock:
            n = max(0, min(count, len(self._ring)))
            return list(self._ring)[-n:]

    def since(self, last_event_id: int) -> List[dict]:
        """v11.0 — return all ring entries with event_id > last_event_id.

        Used by `/descriptions?since=<id>` so a reconnecting client can
        ask only for the events it has not yet seen without paying for
        the full replay-on-connect window. If the ring has rolled past
        `last_event_id` (oldest ring event_id > last_event_id), returns
        an empty list — the caller should detect this via
        `ring_oldest_event_id()` and fall back to `recent()`.
        """
        with self._lock:
            return [e for e in self._ring if e.get("event_id", 0) > last_event_id]

    def ring_oldest_event_id(self) -> int:
        """v11.0 — event_id of the oldest entry in the ring (0 if empty).

        Clients can compare this to their last_seen_id: if their id is
        below the ring floor, they've been disconnected too long and
        should fall back to a full `recent()` replay.
        """
        with self._lock:
            if not self._ring:
                return 0
            return self._ring[0].get("event_id", 0)

    def total_published(self) -> int:
        """v11.0 — monotonic counter of all descriptions ever published.

        Monotonically increasing across ring-buffer rotations so clients
        can detect that they missed events (by comparing their
        last_seen_id to total_published - len(ring)).
        """
        with self._lock:
            return self._event_count

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

    def set_frame_store(self, frame_store):
        """Set FrameStore reference for /frames/<image_id>.jpg endpoint."""
        self._frame_store = frame_store
        if self._tcp_server is not None:
            self._tcp_server.frame_store = frame_store
        else:
            self._pending_frame_store = frame_store

    def _resolve_frame_store(self):
        """Return FrameStore from server, falling back to pending."""
        fs = getattr(self, "_frame_store", None)
        if fs is not None:
            return fs
        return getattr(self, "_pending_frame_store", None)

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
                    elif path.startswith("/frames/") and path.endswith(".jpg"):
                        # /frames/<image_id>.jpg - per-event thumbnail
                        # v9.0: ?raw=1 → serve the original JPEG untouched.
                        #        ?overlay=1 → force annotated even if no bboxes.
                        #        default → annotate if bboxes are present, else raw.
                        image_id = path[len("/frames/"):-len(".jpg")]
                        if not image_id or not all(c in "0123456789abcdefABCDEF" for c in image_id):
                            self._send_json(400, {"error": "invalid image_id"})
                        else:
                            frame_store = getattr(self.server, "frame_store", None)
                            if frame_store is None:
                                server_obj = getattr(self.server, "_server_ref", None)
                                if server_obj is not None:
                                    frame_store = server_obj._resolve_frame_store()
                            if frame_store is None:
                                self._send_json(503, {"error": "no frame store"})
                            else:
                                jpeg = frame_store.get(image_id)
                                if jpeg is None:
                                    self._send_json(404, {"error": "frame not found", "image_id": image_id})
                                else:
                                    bboxes = frame_store.get_bboxes(image_id) or []
                                    want_raw = qs.get("raw") == "1"
                                    want_overlay = qs.get("overlay") == "1"
                                    # X-Bbox-Count reports the stored count regardless
                                    # of overlay mode so clients can decide whether
                                    # to show a "(N regions)" badge. X-Overlay=1
                                    # only when the body was actually re-rendered.
                                    x_count = str(len(bboxes))
                                    if want_raw or (not bboxes and not want_overlay):
                                        body = jpeg
                                        x_overlay = "0"
                                    else:
                                        body = _paint_bboxes(jpeg, bboxes) or jpeg
                                        x_overlay = "1" if body is not jpeg else "0"
                                    self.send_response(200)
                                    self.send_header("Content-Type", "image/jpeg")
                                    self.send_header("Content-Length", str(len(body)))
                                    self.send_header("Cache-Control", "public, max-age=3600")
                                    self.send_header("Access-Control-Allow-Origin", "*")
                                    self.send_header("X-Bbox-Count", x_count)
                                    self.send_header("X-Overlay", x_overlay)
                                    self.end_headers()
                                    self.wfile.write(body)
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
                        # v11.0: supports both `?count=N` (last N) and
                        # `?since=<event_id>` (everything newer than that
                        # id). The two are mutually exclusive — `since`
                        # wins if both are present. Response now also
                        # includes a `cursor` block with ring_oldest_event_id,
                        # total_published, and the request's effective
                        # last_event_id, so the caller can detect a
                        # ring-buffer overflow (their last_seen_id is
                        # below ring_oldest_event_id and the `since`
                        # filter dropped some events).
                        pipeline = getattr(self.server, "pipeline", None)
                        if pipeline is None:
                            server_obj = getattr(self.server, "_server_ref", None)
                            if server_obj is not None:
                                pipeline = getattr(server_obj, "_pipeline", None)
                        qs = self._parse_query(self.path)
                        if pipeline and pipeline.publisher:
                            pub = pipeline.publisher
                            cursor = {
                                "ring_oldest_event_id": pub.ring_oldest_event_id(),
                                "total_published": pub.total_published(),
                                "ring_size": len(pub),
                                "ring_cap": pub._ring.maxlen,
                            }
                            since_raw = qs.get("since")
                            if since_raw is not None:
                                try:
                                    last_id = int(since_raw)
                                except ValueError:
                                    self._send_json(400, {
                                        "error": "since must be an integer event_id",
                                    })
                                    return
                                items = pub.since(last_id)
                                cursor["requested_since"] = last_id
                                # If the ring has rolled past the client's
                                # last id, the `since` filter returned []
                                # but the client may have actually missed
                                # events. Flag it so the UI can fall back
                                # to a full /descriptions?count=N replay.
                                cursor["overflowed"] = (
                                    last_id > 0
                                    and cursor["ring_oldest_event_id"] > 0
                                    and last_id < cursor["ring_oldest_event_id"]
                                )
                            else:
                                count = int(qs.get("count", "20"))
                                items = pub.recent(count)
                                cursor["requested_count"] = count
                            self._send_json(200, {
                                "count": len(items),
                                "descriptions": items,
                                "cursor": cursor,
                            })
                        else:
                            self._send_json(200, {
                                "count": 0,
                                "descriptions": [],
                                "cursor": {
                                    "ring_oldest_event_id": 0,
                                    "total_published": 0,
                                    "ring_size": 0,
                                    "ring_cap": 200,
                                },
                            })
                    elif path == "/events":
                        # v7.0: Server-Sent Events stream of new descriptions.
                        self._serve_sse_stream()
                    elif path == "/stats":
                        # v7.0: Cumulative telemetry summary. Delegates to
                        # pipeline.get_detailed_status() so /stats always
                        # stays in lockstep with /status fields.
                        pipeline = getattr(self.server, "pipeline", None)
                        if pipeline is None:
                            server_obj = getattr(self.server, "_server_ref", None)
                            if server_obj is not None:
                                pipeline = getattr(server_obj, "_pipeline", None)
                        if pipeline is None:
                            self._send_json(503, {"error": "no pipeline"})
                        else:
                            # Prefer get_detailed_status() for full v7.0
                            # telemetry; fall back to get_status() for mocks
                            # and older pipelines. CRITICAL: call the method
                            # to get the dict — get_detailed_status exists
                            # on the live pipeline but the bound method is
                            # not callable via .get() and would 500.
                            st_getter = getattr(pipeline, "get_detailed_status", None) or pipeline.get_status
                            st = st_getter()
                            frames = st.get("frames_processed", 0)
                            salient = st.get("salient_frames", 0)
                            descs = st.get("descriptions", 0)
                            vlm_invoc = st.get("vlm_invocations", 0)
                            scene_skips = st.get("scene_skips", 0)
                            publisher = getattr(pipeline, "publisher", None)
                            ring_size = len(publisher) if publisher is not None else 0
                            self._send_json(200, {
                                "frames_processed": frames,
                                "salient_frames": salient,
                                "descriptions": descs,
                                "vlm_invocations": vlm_invoc,
                                "scene_skips": scene_skips,
                                "scene_threshold": st.get("scene_threshold", 0.02),
                                "motion_score": st.get("motion_score", 0.0),
                                "face_count": st.get("face_count", 0),
                                "last_trigger_kind": st.get("last_trigger_kind", "none"),
                                "deduped_count": st.get("deduped_count", 0),
                                "dedup_skip_count": st.get("dedup_skip_count", 0),
                                "vlm_busy": st.get("vlm_busy", False),
                                "vlm_queue_depth": st.get("vlm_queue_depth", 0),
                                "scene_gate": st.get("scene_gate", {}),
                                "sse_subscribers": st.get("sse_subscribers", 0),
                                "salience_ratio": (salient / frames) if frames > 0 else 0.0,
                                "vlm_pass_rate": (vlm_invoc / frames) if frames > 0 else 0.0,
                                "skip_rate": (scene_skips / salient) if salient > 0 else 0.0,
                                "ring_buffer_size": ring_size,
                                "ring_buffer_cap": RING_BUFFER_SIZE,
                            })
                    else:
                        self._send_json(404, {"error": "not found", "path": path})
                except Exception as e:
                    try:
                        self._send_json(500, {"error": str(e)})
                    except Exception:
                        pass

            def _serve_stats_summary(self):
                """v7.0 — aggregate stats snapshot for dashboards / healthchecks."""
                pipeline = getattr(self.server, "pipeline", None)
                if pipeline is None:
                    server_obj = getattr(self.server, "_server_ref", None)
                    if server_obj is not None:
                        pipeline = getattr(server_obj, "_pipeline", None)
                if pipeline is None:
                    self._send_json(503, {"error": "no pipeline"})
                    return
                st = pipeline.get_status()
                subs = 0
                try:
                    subs = pipeline.publisher.event_bus.subscriber_count()
                except Exception:
                    pass
                vlm_invoc = st.get("vlm_invocations", 0)
                frames = st.get("frames_processed", 0)
                descs = st.get("descriptions", 0)
                scene_skips = st.get("scene_skips", 0)
                self._send_json(200, {
                    "mode": st.get("mode"),
                    "running": st.get("running"),
                    "frames": frames,
                    "salient": st.get("salient_frames", 0),
                    "descriptions": descs,
                    "vlm_invocations": vlm_invoc,
                    "vlm_skip_rate": (
                        1.0 - (vlm_invoc / max(1, frames)) if frames else 0.0
                    ),
                    "scene_skips": scene_skips,
                    "vlm_busy": st.get("vlm_busy", False),
                    "vlm_queue_depth": st.get("vlm_queue_depth", 0),
                    "scene_gate": st.get("scene_gate", {}),
                    "sse_subscribers": subs,
                    "ring_buffer_size": RING_BUFFER_SIZE,
                })

            def _serve_sse_stream(self):
                """v7.0 — Server-Sent Events stream of new descriptions.

                On subscribe, replays the last N descriptions so the client
                renders history immediately. Then streams new events as they
                arrive, one per `data:` frame, until the client disconnects.
                Heartbeat `:` comments every 15s keep proxies from killing
                the idle connection.
                """
                pipeline = getattr(self.server, "pipeline", None)
                if pipeline is None:
                    server_obj = getattr(self.server, "_server_ref", None)
                    if server_obj is not None:
                        pipeline = getattr(server_obj, "_pipeline", None)
                if pipeline is None or not pipeline.publisher:
                    self._send_json(503, {"error": "no pipeline"})
                    return
                pub = pipeline.publisher
                # attach() returns (queue, replay_count). The queue is
                # pre-populated with the last N ring-buffer events; the
                # count is informational. We use the SAME queue for both
                # the replay and the live stream — new events are appended
                # to it by publish() via the EventBus fan-out.
                my_q, replay_n = pub.event_bus.attach(pub._ring)
                # Track for cleanup. List of (handler, queue) tuples so
                # multiple concurrent SSE clients can coexist.
                if not hasattr(self.server, "_sse_subscriber_queues"):
                    self.server._sse_subscriber_queues = []
                self.server._sse_subscriber_queues.append((self, my_q))
                try:
                    self.send_response(200)
                    self.send_header("Content-Type", "text/event-stream")
                    self.send_header("Cache-Control", "no-store")
                    self.send_header("Connection", "close")
                    self.send_header("X-Accel-Buffering", "no")
                    self.send_header("Access-Control-Allow-Origin", "*")
                    self.end_headers()
                    # Drain replay: items already on my_q from attach().
                    # Emit `event: description\nid: <id>\ndata: <json>\n\n`.
                    sent_ids = set()
                    while my_q:
                        item = my_q.popleft()
                        eid = item.get("event_id", 0)
                        if eid and eid in sent_ids:
                            continue
                        if eid:
                            sent_ids.add(eid)
                        payload = json.dumps(item)
                        block = f"event: description\nid: {eid}\ndata: {payload}\n\n".encode("utf-8")
                        self.wfile.write(block)
                        self.wfile.flush()
                    last_seen_id = max(sent_ids) if sent_ids else 0
                    last_heartbeat = time.time()
                    while True:
                        # Drain any new items on the live queue
                        while my_q:
                            item = my_q.popleft()
                            eid = item.get("event_id", 0)
                            if eid and eid == last_seen_id:
                                continue
                            if eid:
                                last_seen_id = eid
                            payload = json.dumps(item)
                            block = f"event: description\nid: {eid}\ndata: {payload}\n\n".encode("utf-8")
                            self.wfile.write(block)
                            self.wfile.flush()
                        # Heartbeat
                        now = time.time()
                        if now - last_heartbeat > 15.0:
                            self.wfile.write(b": ping\n\n")
                            self.wfile.flush()
                            last_heartbeat = now
                        time.sleep(0.25)
                except (BrokenPipeError, ConnectionResetError):
                    return
                except Exception:
                    return
                finally:
                    try:
                        pub.event_bus.detach(my_q)
                    except Exception:
                        pass
                    try:
                        self.server._sse_subscriber_queues.remove((self, my_q))
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
            self._tcp_server.frame_store = getattr(self, "_frame_store", None) or getattr(self, "_pending_frame_store", None)
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