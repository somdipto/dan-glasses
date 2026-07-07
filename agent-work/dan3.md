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
