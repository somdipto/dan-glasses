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

## HTTP API (TCP :8092)

| Method | Path                          | Purpose                                     |
| ------ | ----------------------------- | ------------------------------------------- |
| GET    | `/health`                     | `{"status": "ok"}` liveness ping            |
| GET    | `/status`                     | mode, frames, salient, descs, vlm_busy, qd  |
| GET    | `/descriptions?count=N`       | last N (≤ 200) from in-memory ring buffer  |
| POST   | `/mode` body=`{"mode": ...}`  | set power mode (idle/watchful/active)       |

`/descriptions` event shape:
```json
{
  "type": "description",
  "image_id": "8a3b9c12",
  "timestamp": "2026-06-15T00:48:05Z",
  "description": "...",
  "event_id": 1
}
```

## Power modes

| Mode       | FPS | Salience gate | VLM queue cap |
| ---------- | --- | ------------- | ------------- |
| `idle`     | 0   | n/a (off)     | 0             |
| `watchful` | 5   | must be salient | 2           |
| `active`   | 10  | none          | 2             |

Switching to `idle` calls `capture.stop()`; switching back to a non-idle
mode restarts capture at the new FPS.

## Tauri integration

`apps/dan-glasses-app/src-tauri/src/lib.rs` (perceptiond section, ~80 LOC):
- 4 commands: `perception_health`, `perception_status`, `perception_set_mode`, `perception_descriptions`
- HTTP via `reqwest` (5s timeout), error mapping through `Result<_, String>`
- Bridges Rust structs to TypeScript via serde; types match `/status` and `/descriptions` 1:1
- Mode is validated server-side (`idle` | `watchful` | `active`)
- `count` is clamped to 200 to match the ring buffer cap

`apps/dan-glasses-app/src/components/VisionDashboard.tsx`:
- Polls `/health`, `/status`, `/descriptions?count=50` every 2s in one batched tick
- Mode buttons (Idle / Watchful / Active) call `POST /mode`
- New-event counter via `seenIdsRef` Set so additions stand out without scroll-jank
- Tab nav in `App.tsx`: Bootstrap / Vision / Memory / TTS / Live
- Live descriptions feed, newest first, with image_id + timestamp; no image bytes
  (frame preview is Q3 hardware milestone)

## v5 — Live MJPEG viewfinder

- `/frame.jpg` and `/stream` endpoints for live MJPEG viewfinder.
- JPEG buffer in `capture.py` (single-slot, 5MB cap).
- `_server_ref` fallback that fixed the `set_capture` race.
- `dan-glasses-app` server.py proxy added for `/api/perceptiond/{health,status,descriptions,frame.jpg,mode}` with `/stream` intentionally NOT proxied (direct connection from `<img>`).

## Tests (8/8 passing)

```
SalienceDetector: PASS
V4L2Capture: PASS
Mock capture: PASS
Config default: PASS
Publisher: PASS
Publisher ring buffer: PASS
/descriptions endpoint: PASS
VLMInference init: PASS
=== Results: 8 passed, 0 failed ===
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