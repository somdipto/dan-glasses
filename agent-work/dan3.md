# DAN-3 scratch pad — perceptiond

## Live now: v13.1.0
> **Status:** ✅ running (supervisor: perceptiond, mode=watchful)
> **Tests:** 68/68 pytest green
> **Description log:** 464 lines / 174765 bytes on disk, last_event_id=3
> **Live receipt:** 2026-07-09 00:51 IST

## Re-verify (DAN-3, 2026-07-09 00:51)

- `/health` → `{"status":"ok"}`
- `/status` → watchful, running, vlm_busy=true, description_log fully populated
  (14 keys, lines=464, last_event_id=3, enabled=true, queue_depth=0)
- `/descriptions?count=3` → cursor source:ring, descriptions real
- `/descriptions?since_ts=1783558000` → cursor source:ring_ts, count=1
- `/descriptions?since=99999` → cursor source:ring, count=0 (clean empty)
- `/frame_events?count=2` → 2 pending frame_events with bboxes
- `/stats` → derived telemetry, scene_gate, vlm_pass_rate, etc.
- `/log/stats` → 14 keys, 464 lines, writes=3, errors=0
- `/frame.jpg` → 21652 bytes real JPEG
- `/frames/3aa3584b.jpg` → 4213 bytes JPEG with bbox overlay
- `/frames/3aa3584b.jpg?raw=1` → original JPEG

## Observed: VLM produces real descriptions

Frame 1: "The image features a simple graphic of a large orange circle
against a black background, representing a celestial body like the sun
or a planet." (motion_score 0.0529, bbox around the circle)

Pipeline path: V4L2 capture (mock pattern) → salience(motion) →
SceneGate → llama-mtmd-cli + LFM2.5-VL-450M Q4_0 + mmproj F16 →
DescriptionPublisher → ring + log + memoryd + SSE.

## What v13.1 fixed (carried over)

- Hybrid relative+absolute imports in perceptiond.py
- __version__ = "13.1.0" in __init__.py
- conftest.py pins sys.path
- tests/test_imports.py — 4 guard tests

## Init-state observation (not a bug)

Right after supervisor restart, `/status` can briefly return
`"description_log": {}` because the DescriptionLog worker hasn't
written its first entry yet. After the first salient frame writes,
the field populates with 14 keys (path, lines, bytes, bytes_cap,
lines_cap, truncated_count, first_event_id, last_event_id, first_ts,
last_ts, writes, errors, enabled, queue_depth). On a fresh restart
with a non-empty on-disk log, the `_lines_on_disk` and friends are
populated from the rebuilt index, so even an "empty" log file still
returns a non-empty stats dict. The `{}` only appears in the few-frames
window between process start and the first successful submit() — not
operator-visible in normal steady state.

## Out of scope (parked)

- aarch64 — re-test on Redax hardware
- JPEG → WebP for on-disk store
- Replace mock capture with real V4L2 device on dev box
- WebP thumbnail endpoint for Tauri webview
- Per-mode image retention policy
- Binary index file if description log cap is bumped to 500K+
- Compression of the JSONL log
