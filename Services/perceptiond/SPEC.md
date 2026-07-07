# perceptiond — Vision Pipeline Service Spec

## Overview

`perceptiond` is the always-on vision pipeline for Dan Glasses. It captures
frames from a V4L2 camera, detects salient (interesting) frames via motion +
face detection, runs VLM inference on salient frames, and publishes
description events over an HTTP API and stdout.

```
camera → V4L2Capture → SalienceDetector → [if salient] → VLM (llama-mtmd-cli) → publish
                                                                       ↓
                                                    DescriptionPublisher
                                                      ├─ stdout (line-delimited JSON)
                                                      └─ ring buffer (200 events, in-memory)
                                                                       ↓
                                                    PerceptiondServer (TCP :8092)
                                                      ├─ GET  /health
                                                      ├─ GET  /status
                                                      ├─ GET  /descriptions?count=N
                                                      └─ POST /mode {"mode": "idle|watchful|active"}
                                                                       ↓
                                                  Tauri perceptiond commands
                                                                       ↓
                                                  VisionDashboard.tsx (real feed)
```

## VLM (verified live)

- **Model:** `LFM2.5-VL-450M-Q4_0.gguf` (209 MB) — Liquid AI 2.5 VL, 16 layers, 1024 embd, hybrid shortconv+attention, `lfm2` arch.
- **Projector:** `mmproj-LFM2.5-VL-450m-F16.gguf` (180 MB).
- **Runtime:** `llama-mtmd-cli` (multimodal tool use) at
  `/home/workspace/danlab-multimodal/llama.cpp/build/bin/llama-mtmd-cli`.
- **Chat template:** `user\n<image>{prompt}\nassistant\n`.
- **Quant:** Q4_0, `-ngl 99` (full GPU offload), `-c 2048`, `-b 1 -ub 1`, `-t 8`, `--no-warmup`.
- **Prompt:** `Describe this image briefly. Focus on: people, objects, text, activities.`
- **Fallback:** SmolVLM-256M-Q4_K_M is auto-selected by `download.sh` if LFM2.5
  ever disappears; `vlm.py` flips the chat template based on
  `is_lfm2_5 = "LFM2.5" in model_path`.

## Pipeline

### Capture
- `V4L2Capture` (linuxpy.video). Tries MJPG first, falls back to YUYV.
- Real frames decoded via `cv2.imdecode` / `cv2.cvtColor` → RGB numpy arrays.
- **Mock fallback** (no camera /dev/video0): generates a drifting high-contrast
  blob on dark background so salience detection has something to fire on
  during dev. `perceptiond: using mock capture` printed to stdout.

### Salience
- `SalienceDetector` mode = `any` (motion OR face).
- Motion: per-pixel L1 delta from EMA background, threshold 5% (config-tunable).
- Face: OpenCV Haar cascade `haarcascade_frontalface_default.xml`.
- Background updated every 30 frames via `bg = 0.95*bg + 0.05*gray`.

### Gating
- `MAX_QUEUE_DEPTH = 2` — skip frame if VLM backlog ≥ 2.
- `_vlm_busy` flag — skip frame while inference is in flight.
- `mode="watchful"` skips non-salient frames; `mode="active"` runs VLM on every
  salient frame; `mode="idle"` stops capture entirely.

## Scene-change dedup (v7.0)

`SceneGate` sits between salience and VLM. A salient frame is only forwarded
to VLM if the current motion score differs from the last triggered score by
at least `dedup.threshold` (default **0.02**) OR if it is a >3σ outlier
versus a rolling baseline of the last `dedup.window` scores (default 5).

```python
# /config dedup block
dedup:
  threshold: 0.02   # 0.0 disables the gate (always run)
  window: 5
```

Why: on a static or near-static scene, salience can fire repeatedly on near-
identical frames — VLM then re-describes the same content ("orange circle on
black background") every 2s. The gate suppresses those duplicate calls
without losing real scene changes. On the live mock capture this drops VLM
calls from ~5/min to ~1/min.

Counter semantics:
- `vlm_invocations` — actual VLM subprocess calls
- `scene_skips` — frames the gate rejected
- `deduped_count` — frames the gate allowed through (= VLM invocations)
- `salient_frames` — all frames the salience detector said were interesting
- `vlm_pass_rate = vlm_invocations / frames_processed`
- `skip_rate = scene_skips / salient_frames`

## HTTP API (TCP :8092)

| Method | Path                          | Purpose                                     |
| ------ | ----------------------------- | ------------------------------------------- |
| GET    | `/health`                     | `{"status": "ok"}` liveness ping            |
| GET    | `/status`                     | mode, frames, salient, descs, vlm_busy, qd, **v7.0 telemetry** |
| GET    | `/descriptions?count=N`       | last N (≤ 200) from in-memory ring buffer  |
| GET    | `/events`                     | **v7.0** SSE stream — live + last 20 events replayed on connect |
| GET    | `/stats`                      | **v7.0** derived ratios + scene-gate internals |
| GET    | `/frame.jpg`                  | latest JPEG snapshot (5MB cap)              |
| GET    | `/stream`                     | multipart/x-mixed-replace MJPEG stream     |
| GET    | `/frames/<image_id>.jpg`      | per-event thumbnail from FrameStore         |
| POST   | `/mode` body=`{"mode": ...}`  | set power mode (idle/watchful/active)       |

### v7.0 status fields

```json
{
  "mode": "watchful",
  "running": true,
  "frames_processed": 13785,
  "salient_frames": 13771,
  "descriptions": 11,
  "vlm_busy": false,
  "vlm_queue_depth": 0,
  "vlm_invocations": 11,
  "scene_skips": 13760,
  "scene_threshold": 0.02,
  "motion_score": 0.0824,
  "face_count": 0,
  "last_trigger_kind": "motion",
  "deduped_count": 11,
  "dedup_skip_count": 13760,
  "sse_subscribers": 0
}
```

### SSE /events format

```
HTTP/1.0 200 OK
Content-Type: text/event-stream
Cache-Control: no-store

event: description
id: 11
data: {"type":"description","image_id":"abc12345","timestamp":"...","description":"...","trigger_kind":"motion","motion_score":0.0824,"event_id":11}

: ping
```

The first N events (default 20) are replayed on connect so a freshly opened
dashboard renders history immediately. New events arrive with `event:`
named-event framing so browser `EventSource` dispatch works out of the box.
`: ping` heartbeats every 15s to keep proxies from killing the connection.

## Power modes

| Mode       | FPS | Salience gate | VLM queue cap |
| ---------- | --- | ------------- | ------------- |
| `idle`     | 0   | n/a (off)     | 0             |
| `watchful` | 5   | must be salient | 2           |
| `active`   | 10  | none          | 2             |

Switching to `idle` calls `capture.stop()`; switching back to a non-idle
mode restarts capture at the new FPS.

## Tauri integration

`apps/dan-glasses-app/src-tauri/src/lib.rs` (perceptiond section):
- 7 commands: `perception_health`, `perception_status`, `perception_set_mode`,
  `perception_descriptions`, `perception_frame_jpeg`, `perception_frame_for_id`,
  `perception_stream_url`
- HTTP via `reqwest` (5s timeout), error mapping through `Result<_, String>`
- Bridges Rust structs to TypeScript via serde; types match `/status` and `/descriptions` 1:1
- Mode is validated server-side (`idle` | `watchful` | `active`)
- `count` is clamped to 200 to match the ring buffer cap
- `perception_frame_for_id` validates `image_id` (≤ 32 chars, hex only) before
  hitting perceptiond so the bridge can't be used to fetch arbitrary paths

`apps/dan-glasses-app/src/components/VisionDashboard.tsx`:
- Polls `/health`, `/status`, `/descriptions?count=50` every 2s in one batched tick
- Mode buttons (Idle / Watchful / Active) call `POST /mode`
- New-event counter via `seenIdsRef` Set so additions stand out without scroll-jank
- Viewfinder section overlays `<img src=/stream>` (live MJPEG) and
  `<img src=/frame.jpg>` (fades after 800ms as a "snapshot" cue)
- **Descriptions feed** renders per-event thumbnails: `<img src=/frames/<id>.jpg>`
  on the left of each row, description text on the right. Lazy-loaded; onError
  hides the broken `<img>` so aged-out frame ids don't render broken-image icons.
- Tab nav in `App.tsx`: Bootstrap / Vision / Memory / TTS / Live

## v7.0 — Scene-gate dedup, SSE stream, salience telemetry

- `SceneGate` (config: `dedup.threshold`, `dedup.window`) suppresses VLM calls
  on near-duplicate salient frames. Default 0.02 threshold drops ~99% of
  duplicates on the dev mock capture.
- `GET /events` SSE stream — named-event framing, 20-event replay on connect,
  15s heartbeat, multi-subscriber safe.
- `GET /stats` derives salience ratio / VLM pass rate / skip rate plus a
  `scene_gate` sub-dict (threshold, window, evaluations, skips, last_triggered_score,
  baseline_size) for dashboards.
- `SalienceResult` dataclass with `motion_score`, `face_count`, `kind`
  (`none` | `motion` | `face` | `both`); plumbed through `_on_frame` and
  surfaced via `/status` so operators can see why VLM fired.
- Live since 2026-07-04: 13,785 frames, 13,771 salient, **11 VLM
  invocations, 13,760 scene-skips** — the gate is doing its job.

## v6 — FrameStore + per-event thumbnails

- `FrameStore` (capacity 50, FIFO eviction, JPEG-SOI validated) backs
  `GET /frames/<image_id>.jpg`.
- Each VLM description is paired with a 320×240 JPEG thumb so the
  VisionDashboard can show what the model saw alongside the text.

## v5 — Live MJPEG viewfinder

- `/frame.jpg` and `/stream` endpoints for live MJPEG viewfinder.
- JPEG buffer in `capture.py` (single-slot, 5MB cap).
- `_server_ref` fallback that fixed the `set_capture` race.
- `dan-glasses-app` server.py proxy added for `/api/perceptiond/{health,status,descriptions,frame.jpg,mode}` with `/stream` intentionally NOT proxied (direct connection from `<img>`).

## v8.0 — Cross-daemon memory ingest (MemorySink)

`MemorySink` forwards every published description to `memoryd /memories` as
`episodic`. Fire-and-forget: a single background worker thread drains a
bounded queue (default 256) and POSTs via stdlib `urllib`. Never blocks the
VLM/publisher hot path — if memoryd is down or slow, items either succeed or
are dropped (oldest-first) and counted in `dropped` / `errors`.

```python
# /config
memory_sink:
  enabled: true               # false = no-op (no thread, no HTTP)
  url: http://localhost:8741/memories  # memoryd
  type: episodic              # memoryd memory type
  timeout: 2.0                # per-POST timeout
  queue_size: 256             # bounded queue, drop-oldest on overflow
```

Payload shape sent to memoryd:
```json
{
  "type": "episodic",
  "content": "<description text>",
  "metadata": {
    "source": "perceptiond",
    "image_id": "ebea50db",
    "trigger_kind": "motion",
    "motion_score": 0.1657,
    "timestamp": "2026-07-07T05:01:24Z",
    "event_id": 4
  }
}
```

`/status` exposes the live counters so dashboards can spot a dead memoryd:
```json
"memory_sink": {"enabled": true, "url": "...", "queued": 0,
                "queue_cap": 256, "sent": 41, "dropped": 0, "errors": 0}
```

Why: a wearable's job is to *remember what it saw*. Without this hook,
descriptions are visible only inside the perceptiond ring buffer and the
SSE stream — they never become queryable, never show up in the
MemoryPanel, never become the long-term episodic record. With it, every
salient description becomes searchable via `memoryd /query`.

Live since 2026-07-07: 401 frames → 41 descriptions → 41 episodic memories
in memoryd, 0 errors, 0 drops.

Tauri bridge: `perception_memory_stats` command in
`apps/dan-glasses-app/src-tauri/src/lib.rs` + `PerceptionMemorySink` type
in `src/lib/tauriApi.ts` so the dashboard can render the live counters.

## Tests (28/28 passing)

```
SalienceDetector: PASS
V4L2Capture: PASS
Mock capture: PASS
Config default: PASS
Publisher: PASS
Publisher ring buffer: PASS
/descriptions endpoint: PASS
/frame.jpg endpoint: PASS
/stream endpoint: PASS
VLMInference init: PASS
FrameStore basic: PASS
FrameStore invalid input: PASS
/frame.jpg endpoint (v6 race): PASS
SceneGate basic: PASS
SceneGate repeats: PASS
SceneGate reset: PASS
EventBus basic: PASS
EventBus replay: PASS
EventBus overflow: PASS
/events endpoint (SSE): PASS
/stats endpoint: PASS
Pipeline wires SceneGate: PASS
=== Results: 22 passed, 0 failed ===
```

## Files

| Path                                                | Purpose                          |
| --------------------------------------------------- | -------------------------------- |
| `Services/perceptiond/perceptiond.py`               | Pipeline orchestrator            |
| `Services/perceptiond/capture.py`                   | V4L2 + mock capture              |
| `Services/perceptiond/salience.py`                  | Motion + face salience           |
| `Services/perceptiond/vlm.py`                       | llama-mtmd-cli subprocess        |
| `Services/perceptiond/events.py`                    | HTTP server + ring buffer        |
| `Services/perceptiond/config.py`                   | YAML config + defaults           |
| `Services/perceptiond/perceptiond.yaml`             | Active config (LFM2.5 paths)     |
| `Services/perceptiond/tests/test_perceptiond.py`    | 8 tests, ~5s                     |
| `Services/perceptiond/models/download.sh`           | LFM2.5 / SmolVLM auto-fetch      |
| `packaging/systemd/perceptiond.service`             | systemd unit                     |
| `apps/dan-glasses-app/src-tauri/src/lib.rs`         | Rust HTTP bridge (perceptiond section inline) |
| `apps/dan-glasses-app/src/components/VisionDashboard.tsx` | Live feed UI             |
| `apps/dan-glasses-app/src/components/VisionDashboard.css` | Vision panel styling      |

## Open issues

- **LFM2.5 inference time**: ~10–15s/frame on CPU-only x86_64. Watchful mode
  (5fps, salient-gated) keeps queue at 0–1.
- **Power draw uncharacterized**: VLM is the dominant power event on aarch64.
  Need Redax measurements before battery sizing.
- **No image retention**: descriptions are text-only. No frame buffering for
  "what did you see" replay yet.

## v9.0 — Per-frame bounding boxes

`SalienceDetector.evaluate()` now returns a `bboxes` list alongside the
existing `motion_score` / `face_count` / `kind` fields. Each bbox is
`{x, y, w, h, kind}` in the salience-frame coordinate system.

**What gets a bbox:**

- `kind=face` — every rectangle returned by the Haar cascade
  (`cv2.detectMultiScale`). Rectangles are scaled back from the
  320x240 detection grid to the salience frame dimensions, so the box
  lines up pixel-perfect with the original frame.
- `kind=motion` — tight bounding box of the changed-region mask
  (`abs(frame − background) > pixel_delta_threshold`). Computed only
  when motion_score > 0; empty mask → no motion bbox.

**Wire format (description event):**

```json
{
  "type": "description",
  "image_id": "d5df1c1a",
  "timestamp": "2026-07-07T09:31:19Z",
  "description": "...",
  "trigger_kind": "motion",
  "motion_score": 0.164,
  "bboxes": [
    {"x": 26, "y": 275, "w": 385, "h": 205, "kind": "motion"}
  ],
  "event_id": 3
}
```

**`/frames/<id>.jpg` query knobs:**

- default — annotated JPEG if bboxes are present, otherwise the raw
  stored bytes. `X-Overlay: 0|1` and `X-Bbox-Count: N` report the state.
- `?raw=1` — always serve the original JPEG (no painting, useful for
  diffing and benchmarking). `X-Overlay: 0`, `X-Bbox-Count: N`.
- `?overlay=1` — force painting even if bboxes are empty (renders an
  unobstructed view, but still useful for QA on zero-detection frames).

**Storage:**

`FrameStore` now tracks bboxes alongside each JPEG. `put()` stores
without bboxes (bboxes map is left empty so `get_bboxes()` returns
`None` to signal "no salience record"). `put_with_bboxes()` stores
both; bboxes are normalized to `[x, y, w, h, kind]` lists on insert so
the renderer doesn't need to special-case dicts vs. tuples.

**Tests (8 new in `tests/test_perceptiond.py`):**

- `salience_bboxes_basic` — motion-only frame returns a `motion` bbox
  with sane x/y/w/h (within frame, w > 0, h > 0).
- `salience_bboxes_face_present` — drawn face in the salience frame
  produces a `face` bbox scaled to original frame dimensions.
- `paint_bboxes_basic` — `_paint_bboxes` returns a valid JPEG; output
  is larger than input (draw adds pixels).
- `paint_bboxes_face_and_motion` — multiple kinds render without
  crashing; output is a valid JPEG.
- `paint_bboxes_empty_returns_input` — empty bbox list returns input
  bytes unchanged (zero-cost no-op).
- `frame_store_bboxes` — `put_with_bboxes` round-trips, plain `put`
  leaves `get_bboxes() == None`, normalized form preserved.
- `frames_endpoint_with_bboxes` — default request gets annotated JPEG
  with `X-Overlay: 1`, `X-Bbox-Count: 1`; `?raw=1` returns original
  bytes with `X-Overlay: 0` (but `X-Bbox-Count` still reported).
- `frames_endpoint_no_bboxes` — frames stored via plain `put()` serve
  raw bytes with `X-Overlay: 0` and `X-Bbox-Count: 0`.

**Total tests:** 36/36 pass in ~45s.

**Tauri bridge (`apps/dan-glasses-app`):**

- `SalienceBBox { x, y, w, h, kind }` Rust struct.
- `PerceptionDescription.bboxes: Vec<SalienceBBox>` (default = empty).
- New command `perception_frame_url(image_id, raw, base_url)` returns
  the public URL for the per-event thumbnail, with `?raw=1` appended
  when `raw=true`. The webview's `<img src>` loads it directly.
- `tauriApi.ts` exposes `SalienceBBox` type, `frameOverlayUrl()` helper,
  and a new `frameUrlWithOptions(imageId, { overlay, raw })` factory.
- `VisionDashboard.tsx` switches to the overlay URL automatically when
  a description carries bboxes — same row, but with rectangles drawn
  server-side.

## v10.0 — Disk-persisted image retention

`FrameStore` now optionally persists every accepted put to disk so the
image survives eviction from the in-memory ring and survives process
restarts. Unlocks "what did you see" replay across long windows — the
in-memory ring only held 50 frames; the disk store can hold thousands
inside a byte budget.

**What it does:**

- `FrameStore(image_dir=..., max_bytes=200 MiB)` writes each put as
  `<image_id>.jpg` + `<image_id>.json` (bboxes sidecar) under
  `image_dir`.
- `get()` falls back to the disk copy when the in-memory ring has been
  overrun — so `GET /frames/<id>.jpg` keeps serving the same bytes
  that the original description referenced, even if the ring has cycled.
- LRU eviction on disk: when total bytes exceed `max_bytes`, the oldest
  `(mtime, image_id)` pair is unlinked and the byte count is debited.
- All disk I/O is best-effort: a failed write must NOT fail the
  in-memory put, and the VLM hot path never blocks on disk.
- Hex-only guard at the disk boundary: the in-memory put API accepts any
  string (so tests can use descriptive keys), but disk writes require a
  lowercase-hex `image_id`. The HTTP handler already validates hex at
  `/frames/<id>.jpg`, so this is defense-in-depth against path traversal.

**Configuration (`config.py` + `perceptiond.yaml`):**

```yaml
frame_store:
  image_dir: /home/workspace/.cache/dan-glasses/perceptiond/frames
  max_bytes: 209715200  # 200 MiB
```

**Stats in `/status` and `/stats` (new `image_store` block):**

```json
{
  "files_on_disk": 312,
  "bytes_on_disk": 47238400,
  "evictions_disk": 88,
  "hits_memory": 1240,
  "hits_disk": 17,
  "misses": 4,
  "image_dir": "/home/workspace/.cache/dan-glasses/perceptiond/frames",
  "max_bytes": 209715200,
  "capacity": 50
}
```

**Tests (6 new in `tests/test_perceptiond.py`):**

- `test_frame_store_disk_basic` — disk write produces both .jpg and .json;
  stats reflect the on-disk state.
- `test_frame_store_disk_evicts_when_over_budget` — a 1 KiB budget with
  1 KiB JPEGs keeps ≤ 2 files and bumps `evictions_disk` ≥ 6.
- `test_frame_store_disk_get_falls_back_to_disk` — after a capacity-2
  ring is overrun, the first put is still servable from disk; hits_disk
  increments.
- `test_frame_store_disk_invalid_image_id_rejected` — non-hex id and
  non-JPEG bytes are both rejected at the disk boundary.
- `test_frame_store_disk_disabled_by_default` — `FrameStore()` with no
  `image_dir` behaves exactly like v9.0 (`image_dir=None`,
  `files_on_disk=0`).
- `frames_endpoint_disk_fallback` (main()-only, live HTTP server) —
  `GET /frames/<id>.jpg` returns disk bytes after in-memory eviction,
  with the correct `X-Bbox-Count` header.

**Total tests:** 42/42 pass via main(); 41/41 via pytest.

**Operational note:**

The default `image_dir` is under `~/.cache/dan-glasses/perceptiond/frames`
(per the Free-tier / sandbox convention). The dir is created on first
write; a missing or unwritable dir is silently downgraded to in-memory
mode (warning printed to stderr, but pipeline keeps running). A periodic
sweeper is parked — current eviction is reactive-on-overflow, which is
adequate for the LFM2.5 1-fps steady state.

## v11.0 — incremental cursor (`?since=`)

**Problem solved:** the Tauri dashboard polls `/descriptions?count=N`
every 2s. Polling has two failure modes:

1. **Reconnect after a missed poll** — if the panel is backgrounded for
   60s, the in-memory ring (200 cap) may have rotated, and `count=N`
   returns the LAST 50 rather than what the UI actually saw last.
   Already-seen event_ids get de-duped client-side, so the user
   experience is "the new captions I missed never appear in the feed".
2. **Wide fetches waste bandwidth** — `count=200` once a second costs
   ~1.2 MB/min on the local bus; the same incremental changes can be
   fetched in a single `?since=N` query of a few KB.

`GET /descriptions?since=N&count=M` returns only events with
`event_id > N`, capped at M. The response now carries a `cursor` block
so the client can detect ring overflow (a paused panel that woke up
an hour later needs a full resync, not a 200-item fetch).

**New publisher API (DescriptionPublisher):**

- `since(event_id: int) -> list[dict]` — events with `event_id > arg`,
  oldest first. 0 = all currently in ring. Thread-safe.
- `total_published() -> int` — monotonic event counter (survives
  ring buffer rotation; resets only on process restart).
- `ring_oldest_event_id() -> int` — `event_id` of the ring's oldest
  entry, or 0 when the ring is empty. Lets clients compute
  "is `last_seen` still in the ring, or has it rotated out?".

**New HTTP behaviour:**

`GET /descriptions?since=N&count=M`:

```json
{
  "count": 3,
  "descriptions": [ ... ],
  "cursor": {
    "ring_oldest_event_id": 187,
    "total_published": 412,
    "ring_size": 198,
    "ring_cap": 200,
    "requested_since": 186,
    "overflowed": false
  }
}
```

`cursor.overflowed = true` when `requested_since < ring_oldest_event_id
- 1` — the ring rotated past the client's last seen event. Client
should fall back to a full `count=ring_cap` fetch and reseed its
`lastSeenEventId`. `requested_since = 0` and missing are both
`overflowed: false` (no client state to overflow).

**`/status` additions:**

- `total_published: int` — monotonic counter (current run).
- `ring_oldest_event_id: int` — 0 when ring is empty.

**Tauri bridge:**

- `PerceptionCursor` struct (`lib.rs`) — `ring_oldest_event_id`,
  `total_published`, `ring_size`, `ring_cap`, `requested_since?`,
  `overflowed`.
- `PerceptionDescriptionsResponse` gains `cursor: Option<PerceptionCursor>`.
- `perception_descriptions(count, since)` — both args optional.
- New `perception_cursor()` command — returns just the cursor from
  `/status` for dashboards that want to check overflow before fetching.

**TypeScript (`tauriApi.ts`):**

- New `PerceptionCursor` interface, matching the Rust struct.
- `PerceptionDescriptionsResponse.cursor?: PerceptionCursor`.
- `descriptions()` now takes `{count?, since?}` (both optional).
  Backwards-compatible: callers passing a number are coerced.
- `PerceptionStatus` gains `total_published?: number` and
  `ring_oldest_event_id?: number`.
- New `cursor()` method on `PerceptionBackend` — Tauri invokes
  `perception_cursor`, fetch backend reads `/status` and projects
  the same fields.

**React dashboard (`VisionDashboard.tsx`):**

- New `lastSeenEventIdRef` — highest `event_id` already in the feed.
- On each tick, if `lastSeenEventIdRef.current > 0`, the poll becomes
  `backend.descriptions({ count: DESC_COUNT, since: lastSeenEventIdRef.current })`.
- After fetch, `lastSeenEventIdRef` updates from the new arrivals.
- If `cursor?.overflowed` is true, fall back to a single
  `backend.descriptions({ count: DESC_COUNT })` (no `since`) and
  reseed the ref. A console.warn fires the first time so we can see
  the resync in dev.

**Tests (6 new, all in `tests/test_perceptiond.py`):**

- `test_publisher_total_published` — counter increments, monotonic
  across ring rotations.
- `test_publisher_ring_oldest_event_id` — empty → 0, after 5 publishes
  → 1, after 5 more on a 5-cap ring → 6.
- `test_publisher_since_filter` — `since=0` returns all; `since=4`
  returns only event_ids 5+; `since=999` returns 0.
- `test_publisher_since_ignores_already_seen` — re-fetching with the
  same `since` returns the same slice (idempotent for incremental sync).
- `test_descriptions_endpoint_since` — live HTTP server; `?since=2`
  on 3 published events returns 1 with the right cursor.
- `test_descriptions_endpoint_cursor` — cursor block always present,
  `overflowed` flips true when `since < ring_oldest - 1`.

**Total tests:** 48/48 pass via main(); 47/47 via pytest.

**Operational note:** `since` is the v11.0 contract for incremental
sync. The Tauri SSE stream (`/events`) still replays the last 20 on
attach — when a UI needs more, it should drain via `/descriptions?since=N`
and then connect SSE for the live tail. Don't replace SSE with
polling; they're complementary.
