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

## Tests (22/22 passing)

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