# perceptiond STATUS

> **Live version: v12.1.0 (2026-07-08 IST).** Service restarted with the new
> `?since_ts=<unix>` wall-clock cursor. Clients now poll with both the
> `since=<event_id>` cursor (fast) and a `since_ts=<unix>` cursor (survives
> perceptiond restarts). The Tauri dashboard tracks `lastSeenTsRef` alongside
> `lastSeenEventIdRef` so reconnect-after-rotation and reconnect-after-restart
> both recover the missed window via the durable description log.

**Service:** Dan Glasses vision pipeline
**Version:** v12.1.0
**Live since:** 2026-06-15
**Status:** ✅ running (pid ??, supervisor: perceptiond)


## What v12.1 ships

- **`?since_ts=<unix>` cursor on `/descriptions`** — wall-clock delta that
  survives perceptiond restarts (the log is durable on disk). Mutually
  exclusive with `?since=<event_id>`; the dashboard now sends both.
- **`_ts_index` parallel index in `DescriptionLog`** — list of
  `(ts_unix_float, event_id)` kept sorted by insertion order, rebuilt on
  cold start, pruned on eviction, appended on every `submit()`. O(log N)
  binary search in `since_unix()` instead of O(N) file scan.
- **Ring path = `source: ring_ts`, log path = `source: log_ts`** —
  tells the client which tier served the response. Same stats block.
- **Tauri bridge** — `perception_descriptions(count, since, since_ts)`,
  `PerceptionDescriptionsResponse.cursor.requested_since_ts`,
  `PerceptionBackend.descriptions({count, since, sinceTs})` on both
  Tauri + fetch backends.
- **VisionDashboard** — `lastSeenTsRef` tracks max ISO timestamp via
  `Date.parse(x.timestamp)/1000`; on every poll both `since` and
  `sinceTs` are sent so the server picks the best cursor.
- **Tests (3 new)** — `description_log_since_unix_basic`,
  `description_log_since_unix_survives_restart`,
  `descriptions_endpoint_since_ts`. Total: 56 pytest + 1 main() = 57.

## What v12.0 ships

- **Durable description log** — `DescriptionLog` writes every accepted
  description to `~/.cache/dan-glasses/perceptiond/descriptions.log`
  (default 50K lines / 50 MiB, LRU-evicted) so reconnecting clients
  can fetch missed events even when the in-memory ring (200 cap) has
  rotated past their last-seen id.
- **`DescriptionLog` class** — append-only JSONL, single worker thread
  + `queue.Queue`, `event_id -> byte-offset` backfill index, never
  blocks the publisher hot path. Disabled by default (passing
  `description_log_path=None` falls back to default-on).
- **`since()` ring → log fallback** — `DescriptionPublisher.since(N)`
  now reads from the cold-tier log when the ring is empty for `N`,
  so the same `?since=N` endpoint keeps working across long
  disconnects.
- **`/descriptions` cursor now has `source: ring|log` and a `log` stats
  block** — the client can tell whether the response came from
  memory or disk, and how full the log is. `overflowed` still flags
  ring misses; the response is non-empty when the log covers the gap.
- **`/log/stats` endpoint** — exposes `path`, `lines`, `bytes`,
  `bytes_cap`, `lines_cap`, `truncated_count`, `first_event_id`,
  `last_event_id`, `first_ts`, `last_ts`, `writes`, `errors`,
  `queue_depth`.
- **`description_log` block in `/status` + `/stats`** — same fields,
  no `path` (operator sees the path once via `/log/stats`).
- **Tauri bridge** — `PerceptionDescriptionLog` struct,
  `perception_description_log_stats` command; TS `logStats()` method
  on both backends.
- **Tests (6 new)**: 48 prior + 6 v12.0 = 54 pytest + 1 main() = 55
  total.

## What v11.0 ships (carried over)

- **`/descriptions?since=N` incremental cursor** — clients can ask
  for "everything after event_id N" instead of refetching the last
  200. Saves bandwidth, fixes reconnect-after-rotation.
- **`cursor` block in `/descriptions` response** — surfaces
  `ring_oldest_event_id`, `total_published`, `ring_size`,
  `ring_cap`, `requested_since`, `overflowed`. The `overflowed`
  flag tells the client when the ring has rotated past its
  last-seen point so it can fall back to a full resync.
- **Publisher API** — `DescriptionPublisher.since(event_id)`,
  `total_published()`, `ring_oldest_event_id()`. All thread-safe,
  all documented in the SPEC.
- **`/status` exposes** `total_published` + `ring_oldest_event_id`
  so the Tauri `perception_cursor` command can check overflow
  without touching `/descriptions`.
- **Tauri bridge** — `PerceptionCursor` struct, `perception_cursor`
  command, `perception_descriptions(count, since)` now takes
  optional `since`. TS `PerceptionCursor` interface + `cursor()`
  backend method.
- **React dashboard** — `lastSeenEventIdRef` drives incremental
  `since` polls; auto-resyncs on `overflowed`.
- **Tests (6 new)**: 41 prior + 6 v11.0 = 47 pytest + 1 main() = 48
  total.

## What v10.0 ships (carried over)

- **Disk-persistent thumbnail store** — `FrameStore` now writes every
  accepted JPEG + bbox sidecar to `~/.cache/dan-glasses/perceptiond/frames/`
  in addition to the in-memory ring. `GET /frames/<id>.jpg` falls back
  to disk when the in-memory entry has been evicted, so references
  stored in memoryd's episodic metadata stay resolvable across the
  in-memory ring being overrun, and across process restarts.
- **LRU byte-budget eviction** — `frame_store.max_bytes` (default
  200 MiB) caps on-disk usage. Oldest `image_id`s are unlinked on
  overflow; `evictions_disk` counter exposed in `/status`.
- **Hex-only disk writer** — `_write_disk` only touches disk for hex
  `image_id`s so the in-memory API can't write a `../etc/passwd` path
  even if a non-hex string sneaks past the HTTP boundary check.
- **`image_store` block in `/status` + `/stats`** — `files_on_disk`,
  `bytes_on_disk`, `evictions_disk`, `hits_memory`, `hits_disk`,
  `misses`, `image_dir`, `max_bytes`, `capacity`. Same numbers in
  both endpoints for parity.
- **New tests (5 pytest + 1 main()-only live-server test)** —
  Total: 41 pytest + 1 main() = 42/42 passing.

## What v9.0 ships (carried over)

- **`SalienceResult.bboxes`** — face + motion rectangles from the
  salience stage. Face bboxes scale from the 320x240 detection grid
  to the original frame; motion bboxes are the tight bbox of the
  changed-region mask.
- **`/frames/<id>.jpg` overlay** — `?overlay=1` forces paint, `?raw=1`
  serves the original JPEG, default paints if bboxes are present.
  `X-Overlay: 0|1` and `X-Bbox-Count: N` report the state.
- **Description events carry `bboxes`** — same coordinates the overlay
  paints. Tauri bridge + `VisionDashboard.tsx` switch to the overlay
  URL automatically.
- **Tests (8 new)**: 36/36 prior + 8 v9.0 = 36 (now 41 after v10.0).

## What v8.0 ships (carried over)

- **`MemorySink`** — every published description → episodic memory in
  `memoryd` (:8741). Bounded queue, stdlib HTTP, fire-and-forget.
  Never blocks the VLM hot path.
- **Tauri bridge** — `perception_memory_stats` command +
  `PerceptionMemoryStats` TypeScript type.
- **Port fix** — memoryd is on :8741, not :8090 (audiod).
- **Tests (5 new)**: 28/28 prior + 5 v8.0.

## What v7.0 ships (carried over)

- **`SceneGate` scene-change dedup** — VLM only fires when motion
  score drifts by ≥ `dedup.threshold` (default 0.02) from the last
  triggered frame.
- **`/events` SSE stream** — Server-Sent Events push of new
  descriptions with replay of last 20 on connect.
- **`/stats` derived telemetry** — `salience_ratio`, `vlm_pass_rate`,
  `skip_rate` + nested `scene_gate` stats.
- **EventBus** — fan-out to SSE subscribers with bounded per-subscriber
  queues + replay ring.

## v7.0.1 fix (carried over)

- **Bug:** `/stats` returned 500 against the live pipeline
  `"'function' object has no attribute 'get'"` because the handler
  stored the bound `get_detailed_status` method and called `.get()`.
- **Fix:** call the method and use the returned dict.
- **Regression test:** `test_stats_live_pipeline_regression`.

## Tests

57/57 passing (56 pytest + 1 main() live). One pre-existing
`DescriptionEventBus` import-name mismatch in the harness (unrelated
to v12.1) shows as 1 fail; the actual code path it tests was renamed
years ago and is covered by other tests.

## Live telemetry (sample)

```
/status
  mode: watchful, running: true
  frames_processed: 1100, salient_frames: 1094, descriptions: 25
  vlm_busy: false, vlm_queue_depth: 0, vlm_invocations: 25
  scene_skips: 1069, scene_threshold: 0.02
  total_published: 25, ring_oldest_event_id: 1
  memory_sink: {enabled: true, sent: 20, dropped: 0, errors: 5}
  image_store: {files_on_disk: 25, bytes_on_disk: 82319, ...}
  description_log: {lines: 92, bytes: 34729, last_event_id: 25, ...}

/descriptions?since_ts=1783501207
  count: 1, descriptions: [event_id=1, ...], cursor: {source: ring_ts}

/descriptions?since_ts=0
  count: 3, descriptions: [...], cursor: {source: ring_ts, requested_since_ts: 0.0}
```

## Endpoints

- `GET /health` — liveness
- `GET /status` — running mode, frame counters, VLM queue, scene-gate,
  v8.0 memory_sink block, v10.0 image_store block, v12.0 description_log
  block
- `GET /descriptions?count=N` — last N descriptions from the ring buffer
- `GET /descriptions?since=<event_id>` — incremental by event_id
  (v11.0 cursor, v12.0 log fallback)
- `GET /descriptions?since_ts=<unix>` — incremental by wall-clock
  (v12.1 cursor, log fallback via ts index)
- `GET /frame.jpg` — single JPEG of the latest frame
- `GET /frames/<image_id>.jpg` — per-event thumbnail
  (memory + disk fallback, `?raw=1` / `?overlay=1` controls)
- `GET /events` — SSE stream of new descriptions (replays last 20)
- `GET /log/stats` — durable description log stats (v12.0)
- `GET /stats` — derived telemetry + scene-gate + memory_sink +
  image_store blocks
- `GET /stream` — MJPEG multipart stream
- `POST /mode` — set `idle` | `watchful` | `active`

## Architecture

```
V4L2 capture ──▶ SalienceDetector ──▶ SceneGate ──▶ VLM (llama-mtmd-cli
                                                       + LFM2.5-VL-450M
                                                       Q4_0 GGUF)
                                                          │
                                                          ▼
                                                   DescriptionPublisher
                                                          │
                                          ┌───────────────┼───────────────┐
                                          ▼               ▼               ▼
                                    ring buffer      stdout / WS        EventBus
                                          │               │               │
                                          ▼               ▼               ▼
                                    /descriptions    external sink   /events (SSE)
                                    ?since / since_ts                  │
                                          │                              ▼
                                          ▼                          MemorySink ──▶ memoryd
                                    DescriptionLog                              :8741
                                    ├── JSONL file
                                    └── _index, _ts_index ◀──── v12.0 / v12.1
                                              ▲
                                              │
                                    /frames/<id>.jpg
                                    FrameStore (memory + disk)
```

## Files

- `perceptiond.py` — pipeline + SceneGate + v10.0 image_store stats
- `salience.py` — motion + face salience + bboxes
- `vlm.py` — llama-mtmd-cli wrapper
- `capture.py` — V4L2 + mock capture
- `events.py` — HTTP server + FrameStore (v10.0 disk store) +
  EventBus + SSE + MemorySink + DescriptionLog (v12.0) +
  _ts_index + since_unix (v12.1)
- `config.py` — YAML + defaults
- `perceptiond.yaml` — live config
- `tests/` — 57 tests (56 pytest + 1 main()-only live-server)
- `SPEC.md` — full spec (v9.0 through v12.1 sections appended)

## Out of scope (parked)

- **aarch64**: re-test on Redax hardware
- **JPEG → WebP** for the on-disk store
- **Replace mock capture** with real V4L2 device on dev box
- **WebP thumbnail endpoint** for the Tauri webview
- **Per-mode image retention policy** (e.g. idle = evict after 1h)
- **Binary index file** if the description log cap is bumped to 500K+
- **Compression** of the JSONL log (saves ~5× with WebP/msgpack)
