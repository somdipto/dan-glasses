# perceptiond STATUS

**Service:** Dan Glasses vision pipeline
**Version:** v7.0.1
**Live since:** 2026-06-15
**Status:** ✅ running (pid 107, supervisor: perceptiond)

## What v7.0 ships

- **`SceneGate` scene-change dedup** — VLM only fires when motion score
  drifts by ≥ `dedup.threshold` (default 0.02) from the last triggered
  frame. Cuts ~80–95% of duplicate VLM calls in steady scenes.
- **`/events` SSE stream** — Server-Sent Events push of new descriptions
  with replay of last 20 on connect. Replaces 2s polling.
- **`/stats` derived telemetry** — `salience_ratio`, `vlm_pass_rate`,
  `skip_rate` + nested `scene_gate` stats.
- **Salience telemetry in `/status`** — `motion_score`, `face_count`,
  `last_trigger_kind`, `deduped_count`, `dedup_skip_count`,
  `vlm_invocations`, `scene_skips`, `sse_subscribers`.
- **EventBus** — fan-out to SSE subscribers with bounded per-subscriber
  queues + replay ring.

## v7.0.1 fix (this run)

- **Bug:** `/stats` returned 500
  `"'function' object has no attribute 'get'"` against the live pipeline
  because the handler stored the bound `get_detailed_status` method
  itself and called `.get()` on it.
- **Fix:** call the method and use the returned dict (`events.py`,
  `/stats` branch).
- **Regression test:** `test_stats_live_pipeline_regression` (mocks a
  pipeline exposing both `get_status` and `get_detailed_status`,
  asserts all v7.0 fields and derived ratios).

## Tests

23 / 23 passing (`pytest tests/ -q`, ~40 s).

## Live telemetry (sample)

```
/status
  frames_processed:  23
  salient_frames:    1
  descriptions:      0
  vlm_busy:          true
  vlm_queue_depth:   1
  vlm_invocations:   1
  scene_skips:       0
  scene_threshold:   0.02
  motion_score:      0.0581
  last_trigger_kind: motion
  sse_subscribers:   0

/stats
  salience_ratio:  0.043
  vlm_pass_rate:   0.043
  skip_rate:       0.0
  scene_gate: {threshold: 0.02, window: 5, evaluations: 1, skips: 0,
               last_triggered_score: 0.058, baseline_size: 1}
  ring_buffer_cap: 200
```

## Endpoints

- `GET /health` — liveness
- `GET /status` — running mode, frame counters, VLM queue, v7.0 telemetry
- `GET /descriptions?count=N` — last N descriptions from the ring buffer
- `GET /frame.jpg` — single JPEG of the latest frame
- `GET /frames/<image_id>.jpg` — per-event thumbnail (ring-buffered, may
  be evicted)
- `GET /events` — SSE stream of new descriptions (replays last 20)
- `GET /stats` — v7.0 derived telemetry + scene-gate internals
- `GET /stream` — MJPEG multipart stream (not proxied through
  dan-glasses-app; connect directly)
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
```

## Files

- `perceptiond.py` — pipeline + SceneGate
- `salience.py` — motion + face salience
- `vlm.py` — llama-mtmd-cli wrapper
- `capture.py` — V4L2 + mock capture
- `events.py` — HTTP server + FrameStore + EventBus + SSE
- `config.py` — YAML + defaults
- `perceptiond.yaml` — live config
- `tests/` — 23 pytest cases
- `SPEC.md` — full spec

## Out of scope (parked)

- Cross-daemon: hook memoryd ingest on each description
- aarch64: re-test on Redax hardware
- Bbox overlay on thumbs
- JPEG → WebP
- Replace mock capture with real V4L2 device on dev box
