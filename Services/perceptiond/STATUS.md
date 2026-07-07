# perceptiond STATUS

**Service:** Dan Glasses vision pipeline
**Version:** v11.0.0
**Live since:** 2026-06-15
**Status:** ✅ running (pid ??, supervisor: perceptiond)


## What v11.0 ships

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

## What v10.0 ships

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
  `frame_store_disk_basic`, `frame_store_disk_evicts_when_over_budget`,
  `frame_store_disk_get_falls_back_to_disk`,
  `frame_store_disk_invalid_image_id_rejected`,
  `frame_store_disk_disabled_by_default`, `frames_endpoint_disk_fallback`.
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

48/48 passing (`pytest tests/ -q` collects 47 in ~55s + 1 main()
live-server test `frames_endpoint_disk_fallback`).

## Live telemetry (sample)

```
/status
  mode: watchful, running: true
  frames_processed: 6, salient_frames: 2, descriptions: 1
  vlm_busy: true, vlm_queue_depth: 1, vlm_invocations: 2
  scene_skips: 0, scene_threshold: 0.02
  motion_score: 0.1657, last_trigger_kind: motion
  memory_sink: {enabled: true, sent: 1, dropped: 0, errors: 0}
  image_store: {
    files_on_disk: 2, bytes_on_disk: 6575, evictions_disk: 0,
    hits_memory: 0, hits_disk: 0, misses: 0,
    image_dir: "/root/.cache/dan-glasses/perceptiond/frames",
    max_bytes: 209715200, capacity: 50,
  }

/frames/0c2bee6e.jpg
  200 OK, Content-Type: image/jpeg, 5919 bytes
  X-Bbox-Count: 1, X-Overlay: 1
  Body: valid JPEG 320x240, motion bbox painted

Disk: 2 files (.jpg + .json sidecar) for image_ids 0c2bee6e, b22302d9
```

## Endpoints

- `GET /health` — liveness
- `GET /status` — running mode, frame counters, VLM queue, scene-gate,
  v8.0 memory_sink block, v10.0 image_store block
- `GET /descriptions?count=N` — last N descriptions from the ring buffer
- `GET /frame.jpg` — single JPEG of the latest frame
- `GET /frames/<image_id>.jpg` — per-event thumbnail
  (memory + disk fallback, `?raw=1` / `?overlay=1` controls)
- `GET /events` — SSE stream of new descriptions (replays last 20)
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
                                          │                              │
                                          ▼                              ▼
                                    FrameStore                     MemorySink ──▶ memoryd
                                    ├── in-mem (50 entries)                      :8741
                                    └── disk (200 MiB LRU) ◀──── bboxes / JPEGs
                                          ▲
                                          │
                                    /frames/<id>.jpg
                                    (memory → disk fallback)
```

## Files

- `perceptiond.py` — pipeline + SceneGate + v10.0 image_store stats
- `salience.py` — motion + face salience + bboxes
- `vlm.py` — llama-mtmd-cli wrapper
- `capture.py` — V4L2 + mock capture
- `events.py` — HTTP server + FrameStore (v10.0 disk store) +
  EventBus + SSE + MemorySink
- `config.py` — YAML + defaults (v10.0 `frame_store` block)
- `perceptiond.yaml` — live config (v10.0 `frame_store` block)
- `tests/` — 42 tests (41 pytest + 1 main()-only live-server)
- `SPEC.md` — full spec (v9.0 + v10.0 sections appended)

## Out of scope (parked)

- **aarch64**: re-test on Redax hardware
- **JPEG → WebP** for the on-disk store
- **Replace mock capture** with real V4L2 device on dev box
- **WebP thumbnail endpoint** for the Tauri webview
- **Per-mode image retention policy** (e.g. idle = evict after 1h)
