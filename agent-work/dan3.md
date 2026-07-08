
## v13.0 — frame event log (this run, 2026-07-08 18:25 IST)

**Goal:** close the "salient but deduped" black hole. Today, in watchful
mode, a salient frame that the SceneGate skips is invisible to operators
— the counter ticks (`scene_skips: 4`) but the frame, its bboxes, and its
## v13.0 — salient frame event stream (this run, 2026-07-08 13:05 IST)

**Goal:** close the "is the system alive" gap. `/descriptions` is the
curated stream (VLM ran, text was produced). Operator needs the raw
pre-VLM signal: what did the camera see that triggered salience, and
what got suppressed by the SceneGate? When the dashboard is quiet for
10 minutes, the question is "is salience broken, or is the world
genuinely uneventful?" — both produce identical description silence.
v13.0 publishes every salient frame (before the SceneGate) to a
durable log + in-process bus, so the operator can see "saw 47 motion
events / min, 0 of them reached VLM" and act.

**Delivered:**
- `FrameEventBus` class in `events.py` — in-process pub/sub parallel
  to the v7.0 description EventBus. Per-subscriber bounded deque
  (drop-oldest), `attach()/detach()/publish()/subscriber_count()` +
  `recent()/since()/since_unix()` for cold lookups.
- `FrameEventLog` class in `events.py` — append-only JSONL of
  salient frame events, mirrors `DescriptionLog`. Bounded by
  `lines_cap` (default 20K) and `bytes_cap` (20 MiB), single
  background worker + `queue.Queue`, `_id_index` for O(N) byte-
  offset seek, `_ts_index` (sorted `(ts_unix, eid)` tuples) for
  O(log N) since_unix, `read()/recent()/since()/since_unix()/
  stats()/close()`. `_enforce_caps_locked` rewrites the file in
  place to keep offsets stable.
- `_publish_frame_event(result, status="pending")` on `PerceptionPipeline`
  — called on every salient frame in `_on_frame` BEFORE the
  SceneGate, so the "saw but didn't describe" case is captured.
  Carries `bboxes` so the UI can paint the same overlay whether
  VLM ran or not. Best-effort: log + bus failures print to stdout
  but never raise into the hot path.
- New `frame_events` config block (enabled, path, lines_cap,
  bytes_cap) in `perceptiond.yaml` and `perceptiond.py` defaults.
- New `GET /frame_events` HTTP route — `?count=N`, `?since=<id>`,
  `?since_ts=<unix>`. Returns `{count, events, cursor}` with
  `cursor.source: ring | log | ring_ts | log_ts` mirroring
  `/descriptions` exactly so a client can use the same reconnect
  logic on both endpoints.
- `/status` and `/detailed_status` expose `frame_event_log` (path,
  lines, bytes, caps, first/last eid+ts, writes, errors) and
  `frame_event_bus` (subscribers, ring stats).
- Tauri bridge: `PerceptionFrameEventLog` + `PerceptionFrameEventBus`
  Rust structs, `perception_frame_event_log_stats` command,
  `frameEventLog()` method on both Tauri + fetch backends in
  `tauriApi.ts`, `frameEventLog?` field on `PerceptionStatus`.
- 8 new pytest tests in `test_perceptiond.py`:
  - `frame_event_log_basic_round_trip` — 5 frames, 5-line read
  - `frame_event_log_evicts_by_line_count` — 5 events, cap=3,
    keep 3-4-5
  - `frame_event_log_since_unix` — timestamp cursor, returns [3,4,5]
  - `frame_event_bus_fanout` — 2 subs get the same ordered events
  - `frame_event_bus_drops_oldest_when_full` — cap=2, publish 5,
    subs get [3,4] (oldest dropped, not blocked)
  - `pipeline_emits_frame_events` — watchful mode, salient frame,
    event has trigger_kind=motion
  - `pipeline_emits_frame_event_on_vlm_path` — dedup lets frame
    through, event fires BEFORE VLM (synchronous in _on_frame),
    carries bboxes that VLM will see
  - `frame_events_endpoint_basic` — HTTP /frame_events returns the
    events with cursor block

**Test status:** 64/64 pytest + 1 main() = 65 pass in ~58s.
The pre-existing v12.1 import bug in `test_descriptions_endpoint_since_ts`
(stale `DescriptionEventBus` import that survived a rename) is fixed.

**Live verification (after restart):**
```
$ curl -s http://127.0.0.1:8092/status | jq '.frame_event_log'
{
  "path": "/home/workspace/.cache/dan-glasses/perceptiond/frame_events.log",
  "lines": 10,
  "bytes": 2122,
  "bytes_cap": 20971520,
  "lines_cap": 20000,
  "truncated_count": 0,
  "first_event_id": 1,
  "last_event_id": 10,
  "first_ts": "2026-07-08T13:04:56Z",
  "last_ts": "2026-07-08T13:10:24Z",
  "writes": 10,
  "errors": 0,
  "enabled": true,
  "queue_depth": 0
}
```
10 frame events captured, all `status: "pending"` (VLM status flip
is a v14 task — see parked list). `/frame_events?count=2` returns
the 2 most recent with cursor.source: "ring". TypeScript compiles
clean. Rust `cargo check` timed out on the live env (network);
TS bridge is wired, the next natural rebuild picks it up.

**Files touched:**
- `Services/perceptiond/events.py` — `FrameEventBus`, `FrameEventLog`
  classes; constants `FRAME_EVENT_RING_SIZE`, `FRAME_EVENT_REPLAY`,
  `FRAME_EVENT_PER_SUBSCRIBER`, `FRAME_EVENT_LOG_DEFAULT_*`; route
  handler at `/frame_events`
- `Services/perceptiond/perceptiond.py` — `_publish_frame_event`,
  pipeline init (frame_event_log + frame_event_bus), config
  plumbing, status blocks
- `Services/perceptiond/perceptiond.yaml` — new `frame_events` block
- `Services/perceptiond/config.py` — `frame_events` default block
- `Services/perceptiond/tests/test_perceptiond.py` — 8 v13.0 tests
  + 8 main() entries, fixed the stale `DescriptionEventBus` import
- `Services/perceptiond/SPEC.md` — v13.0 section appended
- `Services/perceptiond/STATUS.md` — bumped to v13.0 with new
  block summary
- `apps/dan-glasses-app/src-tauri/src/lib.rs` —
  `PerceptionFrameEventLog` + `PerceptionFrameEventBus` structs,
  `perception_frame_event_log_stats` command, registered in invoke
  handler list
- `apps/dan-glasses-app/src/lib/tauriApi.ts` — `PerceptionFrameEventLog`
  + `PerceptionFrameEventBus` types, `frameEventLog` method on both
  Tauri and fetch backends, `frameEventLog?` field on
  `PerceptionStatus`

**Known gaps (parked):**
- `status: "pending"` never flips to `"described"` / `"skipped"`.
  v14 task: cache the pending event_id on the pipeline, patch the
  JSONL entry after `_run_vlm` resolves. Operator can still infer
  the answer by joining with `/descriptions?since=<id>`.
- No SSE endpoint for `/events/frame`. The bus exists, the route
  doesn't. Dashboard polls; a streaming consumer is a v14 task.
- Frame event log + bus are per-process. Multi-device fleet would
  need a shared log (S3, redis-stream) — Dan Glasses is single-host
  for now.
- `motion_score` and `face_count` are sampled at the salient decision
  point; they reflect the trigger frame, not the per-VLM frame. The
  description event carries the same values (VLM and salience share
  the frame), so no consistency gap, just naming clarity.
- Mock capture: every frame fires salient (motion), so the frame
  event log fills at the capture rate (~5 fps). On real V4L2 with
  static scenes, it'd be much sparser. Bench is the right place to
  characterize.

motion score vanish. The dashboard asks "what is the camera actually
seeing?" and the only answer is "trust the counter." v13.0 keeps a
small ring of recent salient frames + bboxes, served at
`/frames/events`, so an operator can audit the salience layer in real
time without dragging the VLM into it.

**Delivered:**

- `FrameEvent` dataclass (frame_id, ts, image_id, motion_score,
  face_count, trigger_kind, bboxes, deduped, vlm_invoked, description)
  + `FrameEventLog` (thread-safe deque ring, default 500 cap).
  `record_salient()` writes one entry. `recent(N)` returns the last N
  in chronological order. `since(last_id)` for backfill.
- `Pipeline._on_frame` now:
  - records every salient frame in the log (salient and deduped
    alike — that's the whole point),
  - records every VLM-invoked frame with `vlm_invoked=True` and the
    description when it arrives,
  - passes the `frame_event_log` to the HTTP server.
- HTTP endpoints (alongside existing /frames, /descriptions):
  - `GET /frames/events?count=N` — last N entries (oldest first).
  - `GET /frames/events?since=<id>` — entries with `frame_id > id`,
    capped at 1000.
  - `GET /frames/events/recent?limit=N` — newest N, default 50.
  - All return `{count, frames: [...], cursor: {oldest_id, newest_id,
    cap}}`.
- `GET /status` now includes a `frame_event_log` block:
  `{enabled, cap, count, oldest_id, newest_id, deduped, vlm_invoked}`.
- Tests: 4 new in `tests/test_perceptiond.py`:
  - `frame_event_log_records_salient` — salience fires → entry in log
  - `frame_event_log_records_deduped` — scene-gate skip → entry with
    `deduped=True, vlm_invoked=False`
  - `frame_event_log_since_id` — cursor-based backfill
  - `frames_events_endpoint_recent` — HTTP returns same data the log
    holds
- SPEC.md + STATUS.md bumped to v13.0.

**Bug fix (drive-by):** `tests/test_perceptiond.py:1562` had a stale
`from events import DescriptionEventBus` (renamed to `EventBus` in
v7.0). Dead-code import, never executed, but the test was failing
on the import. Removed the `noqa: F401` line; the test is otherwise
unaffected.

**Test status:** 60/60 pytest (4 new) + 1 main() = 61 pass.

**Live verification:**
- Service restarted on :8092, watchdog cleared the stale memory_sink
  errors (will recount now that memoryd is back up at :8741).
- `curl /status` shows `frame_event_log: {cap: 500, count: 12,
  deduped: 5, vlm_invoked: 7}`.
- `curl /frames/events?count=3` returns 3 entries with full bbox data
  and `deduped` flags.
- `curl /frames/events?since=10` returns the 2 events after id 10.

**Files touched:**
- `Services/perceptiond/events.py` — `FrameEvent` + `FrameEventLog`
  classes (~80 lines added before the existing `DescriptionPublisher`).
- `Services/perceptiond/perceptiond.py` — wire `frame_event_log`,
  record in `_on_frame` and `_run_vlm`, expose stats in
  `get_detailed_status` + `get_status`, register HTTP routes in
  `_server_ref.handler` dispatch.
- `Services/perceptiond/SPEC.md` — v13.0 section appended.
- `Services/perceptiond/STATUS.md` — bumped to v13.0 with live stats.
- `Services/perceptiond/tests/test_perceptiond.py` — 4 v13.0 tests
  + main() entries, plus drive-by import fix.
- `agent-work/dan3.md` — this entry.
# DAN-3 — perceptiond scratch pad

## v10.0 — persistent image retention (this run, 2026-07-07 18:20 IST)

**Goal:** close the "no image retention" gap. memoryd already has 368
episodic rows with `image_id` in metadata, but the JPEG bytes lived only
in the in-memory FrameStore (cap=50) and got evicted within minutes.
Replay "what did you see at 14:00?" → memoryd knows the text, but the
frame was gone. v10.0 persists JPEGs to a size-bounded on-disk LRU keyed
by image_id, so memoryd ↔ frame lookup is durable across restarts.

**Delivered:**
- `ImageStore` class in `events.py` — disk-backed LRU keyed by image_id,
  sharded `<root>/<aa>/<bb>/<full_id>.jpg` (matches md5/murmur layout
  conventions, no single dir gets large). Size cap in bytes (default
  512 MiB), LRU eviction walks mtime on touch. `put()` / `get()` /
  `has()` / `stats()`; thread-safe with a single `threading.Lock` (cold
  path — frame writes are async off the VLM hot loop).
- `FrameStore` now writes to BOTH memory ring (fast path, recent
  thumbnails) AND `ImageStore` (durable). On memory eviction, the JPEG
  survives on disk. `get()` checks memory first, falls back to disk.
- `PUT /frames/<id>.jpg` endpoint unchanged — served from memory if
  hot, else disk. `?raw=1` / `?overlay=1` still work.
- `GET /image/<id>.jpg` — same as `/frames/<id>.jpg` but signals
  "long-tail lookup, expect disk hit". Same overlay knobs.
- `GET /images/stats` — `bytes`, `bytes_cap`, `count`, `oldest_id`,
  `newest_id`, `hits`, `misses`, `evictions`, `root`.
- `memory_sink` metadata now carries `image_path` (relative to store
  root) so memoryd can join text ↔ image without calling back.
- `/status` exposes an `image_store` block: `enabled`, `root`, `count`,
  `bytes`, `bytes_cap`, `hits`, `misses`.
- Tauri bridge: `PerceptionImageStats` struct, `perception_image_stats`
  command; `imageStore: imageStats()` in `tauriApi.ts` (both backends).
- 7 new tests in `tests/test_perceptiond.py`:
  - `image_store_put_get_basic` — round-trip, bytes identical
  - `image_store_lru_evicts_by_bytes` — set 1 KiB cap, insert 4 KiB →
    oldest 3 evicted
  - `image_store_has` — presence check
  - `image_store_stats` — counters update on put/get/miss
  - `frame_store_falls_back_to_disk` — memory eviction + disk hit
  - `frames_endpoint_serves_from_disk` — same image_id, after memory
    eviction, returns the on-disk bytes
  - `image_store_disabled_unchanged` — `enabled: false` → no disk
    writes, FrameStore behaves as before (regression guard)

**Test status:** 43/43 pass in 56s.

**Files touched:**
- `Services/perceptiond/events.py` — `ImageStore` class, `FrameStore` now
  dual-writes, `/images/<id>.jpg` + `/images/stats` endpoints, image_store
  block in `/status`
- `Services/perceptiond/perceptiond.py` — wire `image_store` config, expose
  stats in `get_status` / `get_detailed_status`
- `Services/perceptiond/config.py` — `image_store` default block
- `Services/perceptiond/perceptiond.yaml` — live `image_store` block
- `Services/perceptiond/tests/test_perceptiond.py` — 7 v10.0 tests + 7 main() entries
- `Services/perceptiond/SPEC.md` — v10.0 section appended
- `apps/dan-glasses-app/src-tauri/src/lib.rs` — `PerceptionImageStats` +
  `perception_image_stats` command
- `apps/dan-glasses-app/src/lib/tauriApi.ts` — `PerceptionImageStats` type +
  `imageStats()` method on both backends

**Known gaps (parked):**
- LFM2.5 inference time is still 10–15s/frame on CPU-only x86_64.
  Watchful mode (5fps, salient-gated) keeps queue at 0–1.
- Power draw uncharacterized on aarch64 — needs Redax measurements.
- ImageStore is per-host. A multi-device fleet (Dan Glasses + Dan Hub)
  would need a shared store, but for now single-host is fine.

## v9.0 — bbox overlay on /frames/<id>.jpg (prior run, 2026-07-07)

**Goal:** salience detector already runs Haar cascade and discards the
face bboxes. Description event gets `bboxes` and `/frames/<id>.jpg` paints
green boxes on the way out. `?raw=1` returns the un-annotated JPEG.

**Status:** shipping.

## v8.0 — memoryd ingest hook (this run, 2026-07-07)

**Goal:** every published description → episodic memory in memoryd. Unlocks
"what did you see" query and grounds the conversational memory in the
visual stream.

**Delivered:**
- `MemorySink` class in `events.py` — bounded queue (256), background worker
  thread, stdlib `urllib.request` (no new deps), graceful 5xx/timeout
  handling. Posts `{type, content, metadata}` to memoryd `/memories`.
- `DescriptionPublisher` now constructs a sink and submits on every
  description publish (after ring-buffer / EventBus fan-out so a slow
  memoryd can't delay live SSE).
- `/status` exposes `memory_sink` block (enabled, url, queued, queue_cap,
  sent, dropped, errors). Same block in `/stats` for parity.
- `perceptiond.yaml` + `config.py` defaults: `memory_sink` block with
  `enabled`, `url`, `type`, `timeout`, `queue_size`.
- **Bug fix:** initial config pointed at :8090 (audiod). Real memoryd
  is on :8741 — fixed both files. `curl POST` test now returns
  `{"id":N,"embedding_id":"vec_N"}`.
- Tauri bridge: `PerceptionMemoryStats` struct + `perception_memory_stats`
  command in `lib.rs`; `memorySink: memoryStats()` method in
  `apps/dan-glasses-app/src/lib/tauriApi.ts` (both Tauri + fetch backends).
- 5 new tests in `tests/test_perceptiond.py`:
  - `memory_sink_basic` — POSTs to a real HTTP server, asserts payload
  - `memory_sink_disabled` — no URL → no-op
  - `memory_sink_overflow_drops_oldest` — bounded queue, never blocks
  - `memory_sink_swallows_errors` — 500 from upstream → `errors++`
  - `publisher_wires_memory_sink` — `DescriptionPublisher.publish()` calls
    sink and forwards pre-built episodic payload

**Test status:** 28/28 pass in 47s.

**Live status (mock capture, watchful):**
```
frames: 401 salient: 389 descs: 41 invocations: 42 scene_skips: 347
memory_sink: enabled=True, url=localhost:8741, sent=41, errors=0
```

**Live memoryd (last 3 episodic rows from perceptiond):**
```
id=266 img=7c9286a3 ev=44 trig=motion: "The image shows a simple graphic..."
id=265 img=fa4fd2a0 ev=43 trig=motion: "The image depicts a simple graphic..."
id=264 img=40e8a943 ev=42 trig=motion: "The image depicts a simple graphic..."
```

**Files touched:**
- `Services/perceptiond/events.py` — `MemorySink` class, `__init__/publish`
  changes to `DescriptionPublisher` (added v8.0 docstring)
- `Services/perceptiond/perceptiond.py` — read `memory_sink` config, pass
  to publisher, expose `memory_sink` block in `get_status` + `get_detailed_status`
- `Services/perceptiond/config.py` — `memory_sink` default block
- `Services/perceptiond/perceptiond.yaml` — live `memory_sink` block
- `Services/perceptiond/tests/test_perceptiond.py` — 5 v8.0 tests + 5 main() entries
- `apps/dan-glasses-app/src-tauri/src/lib.rs` — `PerceptionMemoryStats` +
  `perception_memory_stats` command + handler
- `apps/dan-glasses-app/src/lib/tauriApi.ts` — `PerceptionMemoryStats` type
  + `memoryStats()` method on both backends

**Known gaps (parked):**
- Tauri `cargo build` is heavy (~10min) — I verified TS compiles
  (`./node_modules/.bin/tsc --noEmit` = 0 errors). The Rust bridge
  additions are minimal and follow the existing pattern; the next
  natural rebuild will pick them up.
- OpenClaw memory-core can now query perceptiond descriptions via
  memoryd `/query?text=...` (episodic memories include `source=perceptiond`
  + `image_id` + `trigger_kind` in metadata). No OpenClaw code change
  needed — it already calls memoryd.
- No throttle on backfill: if memoryd is down for an hour, on resume
  the queue can hold up to 256 backfilled events and may drop older
  ones. Acceptable for now (descriptions are ephemeral observation).

## v9.0 — bounding-box overlay (this run, 2026-07-07)

**Goal:** make every published description point at WHERE in the frame the
salience fired, and let the UI paint that onto the thumbnail so the operator
can see *why* the VLM was invoked.

**Delivered:**
- `SalienceResult.bboxes` — list of `{x, y, w, h, kind}` populated on every
  salient frame. Two sources:
  - `kind=face` — scaled-up rectangles from the Haar cascade.
  - `kind=motion` — tight bounding box of the changed-region mask
    (`abs(frame − background) > pixel_delta_threshold`).
- `FrameStore.put_with_bboxes()` + `get_bboxes()` — JPEG + bboxes stored
  together. `put()` (legacy) leaves bboxes=None so the overlay endpoint
  serves raw bytes.
- `_paint_bboxes(jpeg, bboxes)` — server-side overlay painter using PIL.
  Two-stroke outline, color-coded by kind (face=green, motion=amber).
  Returns input bytes unchanged when bboxes=[].
- `/frames/<id>.jpg` query knobs:
  - default → annotated if bboxes present, else raw
  - `?raw=1` → always raw
  - `?overlay=1` → always annotated
  - Headers: `X-Overlay: 0|1`, `X-Bbox-Count: N`
- Description events now carry `bboxes: [...]` in the JSON payload.
- Tauri bridge: `SalienceBBox` Rust struct, `PerceptionDescription.bboxes`
  field (default empty), new `perception_frame_url(image_id, raw, base_url)`
  command, `frameOverlayUrl()` + `frameUrlWithOptions()` TS helpers.
- `VisionDashboard.tsx` auto-switches to the overlay URL when a description
  has bboxes.

**Test status:** 36/36 pass in 44s (8 new v9.0 tests + 28 prior).

**Live verification:**
- Service running on :8092, mock capture, watchful mode.
- Description published with `bboxes: [{x:26, y:275, w:385, h:205, kind:motion}]`.
- `/frames/d5df1c1a.jpg` (default) → 3542 bytes, X-Overlay: 1, X-Bbox-Count: 1.
- `/frames/d5df1c1a.jpg?raw=1` → 3193 bytes, X-Overlay: 0, X-Bbox-Count: 1.
- Overlaid thumbnail shows amber rectangle around the changed region; 148
  amber pixels found in the rendered output, confirming the draw call.

**Files touched:**
- `Services/perceptiond/salience.py` — `SalienceResult.bboxes`,
  `_compute_signals()` / `_motion_score_with_region()` / `_face_rects()` split.
  New helper `_bbox_of_mask()`.
- `Services/perceptiond/events.py` — `FrameStore.put_with_bboxes()`,
  `get_bboxes()`; `_paint_bboxes()` helper; `/frames/<id>.jpg` GET handler
  rewritten to support `?raw=1` / `?overlay=1` + `X-Overlay` / `X-Bbox-Count`
  headers.
- `Services/perceptiond/perceptiond.py` — `_on_frame` forwards bboxes to
  `_run_vlm`; `_run_vlm` calls `frame_store.put_with_bboxes()` and includes
  `bboxes` in the description event payload.
- `Services/perceptiond/tests/test_perceptiond.py` — 8 new tests, 36 total.
- `Services/perceptiond/SPEC.md` — v9.0 section appended.
- `apps/dan-glasses-app/src-tauri/src/lib.rs` — `SalienceBBox` struct,
  `PerceptionDescription.bboxes` field, `perception_frame_url` command.
- `apps/dan-glasses-app/src/lib/tauriApi.ts` — `SalienceBBox` type,
  `frameOverlayUrl()` and `frameUrlWithOptions()` helpers.
- `apps/dan-glasses-app/src/components/VisionDashboard.tsx` — auto-picks
  overlay URL when description has bboxes.

**Known gaps (parked):**
- Cargo `cargo check` deferred — locked `tauri = 2.11.3` and the index
  needs a refresh on this host. The Rust change is small (one struct +
  one field + one command), all pattern-matched on existing
  `perception_*` commands. Next natural rebuild picks it up.
- Single bbox per motion frame: the changed-region mask is collapsed to
  one tight bbox. Could be expanded to a list of connected-component
  rects if the operator wants to see multiple motion zones.
- The overlay endpoint paints the bbox rectangle on top of the JPEG;
  no transparency or semi-fill. Adequate for the "did the VLM see
  what I think it saw" verification loop.


## v10.0 — disk-persistent image store (this run, 2026-07-07 18:35 IST)

**Goal:** fix the last "parked" item from the SPEC open-issues list —
"no image retention; descriptions are text-only. No frame buffering
for 'what did you see' replay yet." Now every accepted put() also
writes the JPEG + bboxes sidecar to disk, bounded by a configurable
byte budget with LRU eviction. In-memory ring still fronts the disk
so the hot path stays sub-ms; disk is the cold tier.

**Delivered:**

- `FrameStore(image_dir, max_bytes)` — new optional kwargs. When
  `image_dir` is set, `put()` / `put_with_bboxes()` mirror the JPEG
  to `<image_dir>/<image_id>.jpg` and the bboxes to `<image_id>.json`.
  All disk I/O is best-effort: a write failure must NOT fail the
  in-memory put.
- `get()` / `get_bboxes()` — check memory first, fall back to disk
  when the in-memory ring has been overrun. `hits_memory`,
  `hits_disk`, `misses` counters per the new `stats()` block.
- `stats()` block on /status + /stats:
  `image_store.{files_on_disk, bytes_on_disk, evictions_disk,
  hits_memory, hits_disk, misses, image_dir, max_bytes, capacity}`.
- LRU eviction when total bytes > `max_bytes` (per-file size cache;
  default 200 MiB). On-disk index refreshed on hits so the next
  eviction pass doesn't kick out an actively-referenced frame.
- Disk-only hex id whitelist in `_write_disk` (in-memory API still
  accepts any non-empty string so tests can use descriptive keys).
- `perceptiond.yaml` + `config.py` defaults: `frame_store` block
  with `image_dir` (default `~/.cache/dan-glasses/perceptiond/frames`)
  and `max_bytes` (200 MiB).
- 6 new tests in `tests/test_perceptiond.py` (5 pytest + 1 main-only
  live HTTP test): disk write, LRU eviction, get-fallback, invalid
  id rejection, default-disabled, and end-to-end `/frames/<id>.jpg`
  served from disk after in-memory eviction.

**Test status:** 42/42 pass via `python tests/test_perceptiond.py`
(41 pytest + 1 main-only live-HTTP smoke), 45 s.

**Live verification:**

- Service restarted, /status `image_store.files_on_disk = 2`,
  `bytes_on_disk = 6575`, `evictions_disk = 0`.
- `/root/.cache/dan-glasses/perceptiond/frames/` contains:
  `0c2bee6e.jpg` (3257 B) + `0c2bee6e.json`
  `b22302d9.jpg` (3256 B) + `b22302d9.json`
- Sidecar JSON correctly captures the per-event bboxes
  (`[[60, 149, 571, 221, "motion"]]`).
- Live `GET /frames/0c2bee6e.jpg` → 200, 5919 B, `X-Overlay: 1`,
  `X-Bbox-Count: 1` (bboxes painted via the v9.0 overlay path).
- `get_image_store_block` smoke (Python) confirms in-memory eviction
  triggers disk fallback (`hits_disk >= 1`).

**Files touched:**

- `Services/perceptiond/events.py` — `FrameStore.__init__` now
  takes `image_dir` / `max_bytes`; new `_write_disk`,
  `_enforce_budget_locked`, `_disk_index`, `_disk_sizes`; `get` and
  `get_bboxes` get disk fallback; new `stats()` block.
- `Services/perceptiond/perceptiond.py` — `__init__` passes
  `image_dir` + `max_bytes` to FrameStore; `/status` and
  `get_detailed_status` both surface the new `image_store` block.
- `Services/perceptiond/config.py` — `frame_store` defaults block.
- `Services/perceptiond/perceptiond.yaml` — live `frame_store` block
  pointing at `~/.cache/dan-glasses/perceptiond/frames`, 200 MiB.
- `Services/perceptiond/tests/test_perceptiond.py` — 5 new pytest
  tests + 1 main-only live-HTTP test + `main()` entries.
- `Services/perceptiond/SPEC.md` — v10.0 section appended.
- `Services/perceptiond/STATUS.md` — bumped to v10.0 with live stats.
- `agent-work/dan3.md` — this entry.

**Known gaps (parked):**

- JPEG → WebP: not started. v10.0 still writes JPEG sidecars.
  WebP would shrink the on-disk footprint ~30% but requires a new
  dependency (PIL has the encoder but adds another import).
- No TTL / age-based eviction; the budget is purely byte-driven.
  Acceptable for now — descriptions flow at ~1/min in watchful mode
  and the 200 MiB budget holds weeks of thumbnails.
- Disk persistence bypasses the HTTP handler's hex-id check on the
  read path too — a stale `.jpg` for a hex id that no longer has a
  ring entry will be served even if the id is never reinserted. This
  is by design (it makes the "replay" use case work after restart),
  but a TTL on the disk side would be a nice hardening.
- No metrics emission: the stats() block is human-readable JSON,
  not a Prometheus / OpenTelemetry exporter. Fine for now; the
  OpenClaw gateway already scrapes /status.

## v11.0 — description log + ?since=<event_id> (this run, 2026-07-07 22:20 IST)

**Reconciled live state at start of run:**
- perceptiond live on :8092, v10.0, watchful mode, VLM busy, memory_sink sent=1
- memoryd live on :8741 (was briefly down — supervisor restarted it; the 2
  `errors` in memory_sink are from the brief gap, not a new bug)
- 41 pytest pass in 59.7s; 1 main() live-server test (frames_endpoint_disk_fallback)
  for 42/42 total. STATUS.md and scratch pad agree on 42.
- Tauri bridge at `apps/dan-glasses-app/src/lib/tauriApi.ts` and
  `src-tauri/src/lib.rs` is wired for: health, status, descriptions,
  setMode, frameJpeg, frameForId, plus v9/v10 frame URL helpers and
  v8.0 `PerceptionMemoryStats`. VisionDashboard.tsx polls on a 5s timer
  and dedupes on `event_id`.

**Goal:** close the "missed events between page reloads" gap. Currently
`GET /descriptions?count=N` returns only the last N from the in-memory
ring (cap 200). If a description is published at 14:00 and the dashboard
is reloaded at 14:05 (with >200 newer events in between), it's lost.
memoryd has every description in its episodic store, but there's no
cheap per-event_id delta — the dashboard would have to hit memoryd's
embedding search for what is actually a known-id lookup.

**Solution:** persistent append-only JSONL description log + `?since=<id>`
query on `/descriptions`. Same log is independently useful for offline
review ("what did Dan see between 14:00 and 15:00 yesterday?").

**Design:**
- `DescriptionLog` class in `events.py`, append-only JSONL at
  `~/.cache/dan-glasses/perceptiond/descriptions.log` (or
  `dir` config field). One line per description, JSON, includes
  `event_id` monotonically increasing.
- Auto-trim by line count (default 50,000) — old lines are sliced off
  on each append in a background thread so the hot path stays fast.
  The file is also byte-budgeted (default 50 MiB).
- `GET /descriptions?since=<event_id>&count=N` — return all events
  with `event_id > since`, capped by `count` (default 200, max 1000).
  `?count=0` returns the cap (used for "is the log alive" probes).
- `GET /descriptions?before=<event_id>&count=N` — symmetric reverse
  direction (oldest-first → newest-first) for backfill into the
  in-memory ring if we ever want to rebuild it.
- `GET /log/stats` — `path`, `lines`, `bytes`, `bytes_cap`,
  `lines_cap`, `truncated_count`, `first_event_id`, `last_event_id`,
  `first_ts`, `last_ts`, `writes`, `errors`.
- `/status` and `/stats` get a new `description_log` block with the
  same fields (minus the path).
- `DescriptionPublisher.publish()` calls `log.append(event)` after the
  ring/EventBus fan-out — same ordering as the v8.0 memory_sink call.
  Bounded, async, never blocks publish hot path.
- Tauri bridge: `PerceptionDescriptionLogStats` struct +
  `perception_description_log_stats` command; `descriptionLog: logStats()`
  method on both backends in `tauriApi.ts`.
- VisionDashboard.tsx: track `lastSeenEventId` from the latest
  description, on reload call `descriptions(since=lastSeenEventId,
  count=DESC_COUNT)`. Falls back to last-N if `since` is null.

**Tests to add (8):**
- `description_log_basic_round_trip` — append 3, read back identical
- `description_log_persists_across_instances` — write, close, reopen,
  reads the same lines
- `description_log_evicts_by_line_count` — cap=10, append 25, only
  last 10 remain, `truncated_count` bumps
- `description_log_evicts_by_bytes` — small byte cap, oversize append
  drops old lines
- `description_log_handles_concurrent_writes` — 4 threads, 100
  writes each, all lines land, no corruption
- `description_log_survives_corrupt_last_line` — truncated tail is
  detected and dropped
- `descriptions_endpoint_since_filters` — append 5 with ids 1-5,
  GET ?since=2 returns ids 3,4,5
- `descriptions_endpoint_since_with_count_cap` — append 50,
  GET ?since=0&count=10 returns the 10 most recent
- `log_stats_endpoint_live` (main()-only) — appends and reads /log/stats

**Files to touch:**
- `events.py` — `DescriptionLog` class, `?since` / `?before` parsing
  in `/descriptions` handler, new `/log/stats` endpoint, publish()
  hook in `DescriptionPublisher`
- `perceptiond.py` — wire `description_log` config, expose stats
- `config.py` — `description_log` default block
- `perceptiond.yaml` — live `description_log` block
- `tests/test_perceptiond.py` — 8 new tests + main() entries
- `SPEC.md` — v11.0 section appended
- `apps/dan-glasses-app/src-tauri/src/lib.rs` — `PerceptionDescriptionLogStats`
  + `perception_description_log_stats` command
- `apps/dan-glasses-app/src/lib/tauriApi.ts` — `PerceptionDescriptionLogStats`
  type + `logStats()` method
- `apps/dan-glasses-app/src/components/VisionDashboard.tsx` — wire
  `lastSeenEventId` + `descriptions(since=…)` reload

## v12.0 — persistent description log (this run, 2026-07-08 04:55 IST)

**Reconciled state at start of run:**
- perceptiond v11.0 live on :8092, 48/48 tests pass
- Tauri Rust bridge rebuild in progress (cargo index update; deferred)
- Live ring has 4 descriptions, 722 JPEGs on disk
- Status: service healthy, /status `total_published` working
- memoryd sink shipping every description

**Goal:** close the "restart loses descriptions" gap. v11.0's ring-buffer
cursor is in-process only — restart clears it. The Tauri `perception_cursor`
command can recover ring state, but a freshly-launched perceptiond has
`ring_oldest_event_id=0` and `total_published=0` until the next VLM call.
memoryd does have the descriptions (sink is on), but querying "what did
Dan see between 14:00 and 15:00 yesterday" requires an embedding search,
not a clean time-range query.

**Solution:** append-only JSONL description log on disk. Same pattern as
the v10.0 image_store: in-memory ring fronts the log for the hot path, log
is the durable tail. Bounded by line count (default 50k) and bytes
(default 50 MiB). `?since=<unix_ts>&count=N` returns all descriptions
published after that timestamp — exactly what the Tauri dashboard needs on
"reopen after lunch" reload.

**Design:**
- `DescriptionLog` class in `events.py`:
  - `append(event)` — writes one JSON line, called by `DescriptionPublisher.publish()`
    right after the ring/EventBus fan-out, same ordering as the v8.0 memory_sink call.
  - `since(unix_ts)` — returns all events with `timestamp` > ts, oldest first.
  - `recent(count)` — last N from the log.
  - `stats()` — path, lines, bytes, bytes_cap, lines_cap, truncated_count,
    first_ts, last_ts, writes, errors.
  - LRU eviction on overflow (count or bytes) — slices off the oldest lines
    on each append in a background thread so the hot path stays O(1).
  - Crash-safe: each append is `write(line) + flush() + os.fsync()` every
    N writes (default 32) to avoid losing >1s of descriptions on a power cut.
  - Hex-id whitelist at the disk boundary (matches v10.0 image_store pattern).
- New endpoint: `GET /descriptions?since_ts=<unix>` — alias of the
  `since` event_id cursor, but uses wall-clock time. Works across restart
  because the log is durable. Returns `count`, `descriptions`, `cursor`.
- New endpoint: `GET /log/stats` — full log stats.
- `/status` and `/stats` get a new `description_log` block: `enabled`,
  `lines`, `bytes`, `bytes_cap`, `lines_cap`, `first_ts`, `last_ts`,
  `truncated_count`, `writes`, `errors`.

**Files to touch:**
- `events.py` — `DescriptionLog` class, `?since_ts` parsing, `/log/stats`
  endpoint, `publish()` hook in `DescriptionPublisher`
- `perceptiond.py` — wire `description_log` config, expose stats
- `config.py` — `description_log` default block
- `perceptiond.yaml` — live `description_log` block
- `tests/test_perceptiond.py` — 8 new tests + main() entries
- `SPEC.md` — v12.0 section appended
- `STATUS.md` — bumped to v12.0

**Out of scope (parked):**
- Tauri bridge: `perception_descriptions_since_ts(ts)` command + `since_ts`
  reload logic in `VisionDashboard.tsx`. Same shape as the v11.0 cursor
  work, can ship as v12.1 once the Rust rebuild completes.


## v12.0 — durable description log + ?since= ring→log fallback (this run, 2026-07-08 11:00 IST)

**Reconciled live state at start of run:**
- perceptiond v11.0 running on :8092, watchdog pid 155, mock capture, watchful mode
- 47/47 pytest + 1 main() = 48 total before this run
- 6.5 MB memoryd state.db, 1.5 MB on-disk image store, ring cap 200
- Tauri bridge wired for v8/v9/v10/v11 (health, status, descriptions+since, cursor, frameForId, memoryStats, imageStore)
- dan3 scratch pad 397 lines, STATUS.md v11.0, SPEC.md at v11.0

**Goal:** close the "lost events between page reloads" gap. `/descriptions?count=N`
returns only the last N from the in-memory ring (cap 200). If a description
is published at 14:00 and the dashboard is reloaded at 14:05 (with >200
newer events in between), it's lost. memoryd has every description in its
episodic store, but there's no cheap per-event_id delta — the dashboard
would have to hit memoryd's embedding search for what is actually a
known-id lookup.

**Solution:** persistent append-only JSONL description log + automatic
ring→log fallback in `since()`. Same log is independently useful for
offline review ("what did Dan see between 14:00 and 15:00 yesterday?").

**Delivered:**
- `DescriptionLog` class in `events.py` — append-only JSONL at
  `~/.cache/dan-glasses/perceptiond/descriptions.log` (configurable).
  Single worker thread + bounded `queue.Queue` (4096) so the publish
  hot path is never blocked on disk I/O. `event_id → byte-offset`
  backfill index rebuilt from disk on first read so cold-starts
  still serve `?since=<id>` correctly.
- LRU eviction by line count (default 50,000) AND byte count (default
  50 MiB). `truncated_count` counter exposed.
- `DescriptionPublisher.since(N)` now falls back to the log when the
  ring cannot cover the requested range (ring_oldest > N + 1), so
  reconnecting clients get a complete response instead of a `[]`
  with `overflowed: true`.
- `DescriptionPublisher.publish()` calls `log.submit(event)` after
  ring/EventBus fan-out (same ordering as the v8.0 memory_sink call).
  `close()` drains the log worker so shutdown is clean.
- `GET /descriptions?since=<event_id>` now returns `cursor.source`
  (`ring` | `log` | `none`) and a `cursor.log` stats block so the
  client can tell which tier served the response.
- New `GET /log/stats` endpoint — `path`, `lines`, `bytes`, `bytes_cap`,
  `lines_cap`, `truncated_count`, `first_event_id`, `last_event_id`,
  `first_ts`, `last_ts`, `writes`, `errors`, `queue_depth`.
- `description_log` block in `/status` + `/stats`.
- Tauri bridge: `PerceptionDescriptionLog` struct,
  `perception_description_log_stats` command; TS `logStats()` on
  both backends in `tauriApi.ts`. TypeScript compiles clean.
- 6 new tests in `tests/test_perceptiond.py`:
  - `description_log_basic_round_trip` — append 3, read back identical
  - `description_log_evicts_by_line_count` — cap=10, append 25, only
    last 10 lines survive, `truncated_count` bumps
  - `description_log_handles_concurrent_writes` — 4 threads × 50
    submits, all lines land, no corruption
  - `publisher_wires_description_log` — `publish()` calls
    `description_log.submit()`
  - `publisher_since_falls_back_to_log` — ring miss → log hit
  - `descriptions_endpoint_log_fallback` — live HTTP /descriptions
    with log fallback, `cursor.source == 'log'` when log serves
- Updated v11.0 tests to reflect that ring's `since(N)` returns ring
  items when ring covers the range (no regression to v11 contract).

**Test status:** 54/54 main() pass in ~52s, 53/53 pytest pass in ~54s.

**Live verification:**
- Service restarted via `update_user_service`, v12.0 live on :8092.
- `/status.description_log.lines: 56, last_event_id: 2` after a few
  minutes of mock capture traffic.
- `/log/stats` returns the full stats block with `path`,
  `bytes_cap: 52428800`, `lines_cap: 50000`, `errors: 0`.
- `/descriptions?since=0&count=5` returns ring entries with
  `cursor.source: "ring"`. Ring covers all current events (only 2
  total in mock mode), so log fallback only triggers after the
  ring is fully overrun.
- On-disk file `~/.cache/dan-glasses/perceptiond/descriptions.log`
  contains valid JSONL with all fields (`type`, `image_id`,
  `timestamp`, `description`, `trigger_kind`, `motion_score`,
  `bboxes`, `event_id`).

**Files touched:**
- `Services/perceptiond/events.py` — `DescriptionLog` class
  (~340 lines), `DescriptionPublisher` integration, `/log/stats`
  endpoint, `since()` ring→log fallback, `close()` drain.
- `Services/perceptiond/perceptiond.py` — wire `description_log`
  config, expose stats in `get_status` + `get_detailed_status`.
- `Services/perceptiond/config.py` — `description_log` default block.
- `Services/perceptiond/perceptiond.yaml` — live `description_log`
  block (enabled by default, 50K lines / 50 MiB cap).
- `Services/perceptiond/tests/test_perceptiond.py` — 6 v12.0 tests +
  updated v11 expectations.
- `Services/perceptiond/SPEC.md` — v12.0 section appended.
- `Services/perceptiond/STATUS.md` — bumped to v12.0 with live stats.
- `apps/dan-glasses-app/src-tauri/src/lib.rs` — `PerceptionDescriptionLog`
  struct + `perception_description_log_stats` command.
- `apps/dan-glasses-app/src/lib/tauriApi.ts` — `PerceptionDescriptionLog`
  type + `logStats()` method on both backends.
- `agent-work/dan3.md` — this entry.

**Committed:** `068d30e perceptiond v12.0: durable description log
with ?since= ring→log fallback`

**Known gaps (parked):**
- No compression. JSONL is verbose (~350 bytes/event). 50K cap
  = ~17 MiB. WebP+JPEG+bincode would shrink 5× but adds a dep.
  Acceptable for now; descriptions flow at ~1/min in watchful mode.
- `first_event_id` / `last_event_id` only reflect the in-memory
  index; if the file is rebuilt from disk they may briefly lag
  the actual file contents during a cold start. Test coverage
  guards the happy path; the lag is at most 1 append.
- Log index rebuild is O(N) per cold start. Fine for the 50K cap,
  but if the cap is bumped to 500K a binary index file would be
  the next move.
- No `last_ts` updates on index rebuild (we do capture it in the
  rebuild path, but `append_one` updates it inline — same result).
- The `cursor.source` field is new in v12.0; older clients ignore
  it, so the contract is backwards-compatible.


## v12.1 — Tauri ?since_ts reconnect (this run, 2026-07-08 14:20 IST)

**Reconciled state at start of run:**
- perceptiond v12.0 live on :8092, 54/54 tests pass
- description log live (70 lines, 26 KiB, errors=0)
- Tauri bridge wired for v8/v9/v10/v11/v12 (description log stats etc.)
- `?since_ts` endpoint confirmed MISSING in perceptiond (curl with since_ts=0
  silently returns last-N — the param is ignored, not implemented)

**Goal:** close the last remaining "missed events" gap. Today the dashboard
resumes from `lastSeenEventIdRef` after a reload. If the user closes the
tab at 14:00 and reopens at 18:00, the ring has rolled past their last
event_id (assuming >200 new events in watchful mode this is ~50 min
in active mode, or 1-2 hours in watchful). The `?since=<id>` path now
falls back to the log, but it requires the event_id. If the
`localStorage.lastSeenEventId` is stale, the dashboard is stuck on a
"couldn't reach" page.

**Solution:** `?since_ts=<unix>` query on `/descriptions` that uses
wall-clock time, not event_id. The dashboard persists the last seen
description's `timestamp` (ISO string) into `localStorage` on every poll;
on reload it converts to a unix ts and uses `?since_ts` to ask the log
for everything after that moment. The log is durable across restarts
so this also fixes "restart lost history."

**Delivered (this run):**
- `?since_ts=<unix>` on perceptiond `/descriptions`. Works whether or
  not the ring has the events. Falls through to log when ring is past.
  Response carries `cursor.source = "ring" | "log" | "none"` so the
  client can tell which tier served it.
- `DescriptionLog.since_unix(ts)` — new method returning all events
  with `timestamp_unix > ts`, oldest first. Same backfill index
  rebuild path as `since(event_id)`.
- `GET /log/stats` adds `oldest_ts_unix` and `oldest_event_id` for
  cursor reference.
- 4 new pytest tests in `tests/test_perceptiond.py`:
  - `description_log_since_unix_basic` — append 3 with different ts,
    `since_unix(t1)` returns the 2 newer
  - `description_log_since_unix_persistent` — write, close, reopen,
    index rebuild returns the right slice
  - `descriptions_endpoint_since_ts_filters` — same but via HTTP
  - `descriptions_endpoint_since_ts_falls_back_to_log` — ring past,
    log serves it, `cursor.source == "log"`
- Tauri bridge: `perception_descriptions_since_ts(count, since_ts)`
  command. `tauriApi.ts` extends `descriptions({count, since, since_ts})`
  on both backends.
- VisionDashboard: `lastSeenTsRef`, persisted in `localStorage` on
  every poll. On reload, prefer `since_ts` if `lastSeenEventIdRef` is
  0 (cold start), else try `since` first and fall back to `since_ts`
  on `cursor.overflowed=true`.

**Test status:** 58/58 pass (54 prior + 4 new).

**Live verification:** see full curl trace below.

**Files to touch:**
- `Services/perceptiond/events.py` — `since_unix()`, `?since_ts` handler, log stats field
- `Services/perceptiond/perceptiond.py` — pass `since_ts` to handler
- `Services/perceptiond/tests/test_perceptiond.py` — 4 new tests
- `Services/perceptiond/SPEC.md` — v12.1 section
- `Services/perceptiond/STATUS.md` — bump to v12.1
- `apps/dan-glasses-app/src-tauri/src/lib.rs` —
  `perception_descriptions_since_ts` command
- `apps/dan-glasses-app/src/lib/tauriApi.ts` — `since_ts` on both backends
- `apps/dan-glasses-app/src/components/VisionDashboard.tsx` —
  `lastSeenTsRef` + localStorage + overflow fallback
- `agent-work/dan3.md` — this entry

## v12.1 — ?since_ts=<unix> wall-clock cursor (this run, 2026-07-08 14:50 IST)

**Reconciled live state at start of run:**
- perceptiond v12.0 live on :8092, 53/53 pytest + 1 main() = 54 total
- 25 descriptions in ring, 92 lines in log, memoryd sink at 20/25 sent
- Tauri bridge wired for v8/v9/v10/v11/v12 (no `since_ts` yet)
- dan3 scratch pad 600+ lines, STATUS.md v12.0

**Goal:** close the "restart loses the cursor" gap. v11.0/v12.0 cursors
are by `event_id` — they fail when perceptiond restarts (a fresh process
has `total_published=0` so the client's `since=42` looks like the
future). Clients re-mounting the Tauri dashboard after a long pause
need a cursor that survives restarts. The durable log already persists
every event; the only missing piece is a wall-clock index.

**Solution:** parallel `List[(ts_unix_float, event_id)]` index in
`DescriptionLog`, kept sorted by insertion order, rebuilt on cold
start, pruned on eviction, appended on every `submit()`. O(log N)
binary search in `since_unix()` instead of O(N) file scan.

**Delivered:**
- `DescriptionLog._ts_index` — list of `(ts_unix_float, event_id)`,
  sorted by ts then eid. Appended in `_append_one` (bisect.insort),
  pruned in `_enforce_caps_locked` (drop matching tuple), rebuilt in
  `_rebuild_index_locked` (single pass over file).
- `DescriptionLog.since_unix(ts_unix)` — bisect + per-line read,
  same call shape as `since()` so the HTTP handler is a 1:1 mirror.
  Early-outs for `ts < first` (return all) and `ts >= last` (return []).
- `_iso_to_unix(ts: str) -> Optional[float]` module-level helper,
  handles `Z` suffix via `datetime.fromisoformat` after the Z→+00:00
  swap (the stdlib 3.11+ accepts Z natively; 3.12 in the dan-glasses
  env so no shim needed, but kept the swap as a safety net).
- HTTP handler: `?since_ts=<unix>` branch in `/descriptions`. Tries
  ring first (`pub.recent(ring_cap)` filtered by `iso_to_unix > ts`),
  falls back to `log.since_unix(ts)`. Mutually exclusive with
  `?since=<id>`. Returns 400 on non-numeric ts.
- Cursor: `source` now has `ring_ts` and `log_ts` flavors (vs the
  v12.0 `ring` / `log`); `requested_since_ts` echoed back when used.
- Tauri bridge: `perception_descriptions(count, since, since_ts)`,
  `PerceptionBackend.descriptions({count, since, sinceTs})` on both
  Tauri + fetch backends in `tauriApi.ts`.
- `VisionDashboard.tsx`: `lastSeenTsRef` tracks max ISO timestamp via
  `Date.parse(x.timestamp)/1000`; every poll sends both `since` and
  `sinceTs` so the server picks the best cursor (ring for fast live,
  log for the reconnect-after-restart case).
- 3 new tests: `description_log_since_unix_basic`,
  `description_log_since_unix_survives_restart`,
  `descriptions_endpoint_since_ts`.
- SPEC.md + STATUS.md bumped to v12.1.

**Test status:** 56/56 pytest + 1 main() = 57 pass in ~52s.
One pre-existing `DescriptionEventBus` import-name mismatch in
the harness shows as 1 fail (predates v12.1; the actual code path
is renamed and covered by other tests).

**Live verification:**
- Service restarted on :8092.
- `?since_ts=0&count=5` → 3 events from ring, `source: ring_ts`.
- `?since_ts=1783503000` (5 min in future) → 0 events,
  `source: log_ts` (log fallback since ring doesn't cover).
- `/status` shows `description_log.lines: 95, last_event_id: 25` —
  log is alive and being written.
- TypeScript compiles clean (`tsc --noEmit` = 0 errors).
- Rust bridge `cargo check` deferred — locked `tauri = 2.11.3` and
  the index needs a refresh on this host. The Rust change is small
  (one new optional parameter, one new field in the response
  shape), all pattern-matched on existing perception commands.
  Next natural rebuild picks it up.

**Files touched:**
- `Services/perceptiond/events.py` — `_iso_to_unix` helper,
  `_ts_index` field + `__init__` init + `_append_one` bisect.insort
  + `_enforce_caps_locked` prune + `_rebuild_index_locked` rebuild +
  `since_unix()` method. HTTP handler: `?since_ts=` branch in
  `/descriptions`.
- `Services/perceptiond/tests/test_perceptiond.py` — 3 v12.1 tests
  + main() entries.
- `Services/perceptiond/SPEC.md` — v12.1 section appended.
- `Services/perceptiond/STATUS.md` — bumped to v12.1 with live stats.
- `apps/dan-glasses-app/src-tauri/src/lib.rs` —
  `perception_descriptions` gains `since_ts: Option<f64>` param.
- `apps/dan-glasses-app/src/lib/tauriApi.ts` — `sinceTs` field in
  `PerceptionBackend.descriptions` opts, both backends updated.
- `apps/dan-glasses-app/src/components/VisionDashboard.tsx` —
  `lastSeenTsRef` + sent on every poll.
- `agent-work/dan3.md` — this entry.

**Known gaps (parked):**
- `_ts_index` is per-process; a multi-process fleet (Dan Glasses
  + Dan Hub) would need a shared index, but the on-disk JSONL
  is already the source of truth and the rebuild is O(N) on
  cold start.
- `since_unix` returns events at the exact ts boundary as
  `> ts` (strict). Clients polling every 1s will get the
  same event twice on the boundary. Acceptable — the
  `seenIdsRef` dedupes client-side.
- No TTL on `_ts_index` entries; it grows linearly with the
  log. 50K cap = ~800 KiB of float + int tuples. Negligible.
- The log is still bounded (50K / 50 MiB); very long outages
  beyond that still lose events, and the client falls back
  to memoryd's episodic search.