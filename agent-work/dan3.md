# DAN-3 scratch pad — perceptiond

## Status: v7.0.1 SHIPPED — 2026-07-07 06:30 IST

### v7.0 (carried over, shipped earlier this stream)
- SceneGate scene-change dedup
- `/events` SSE stream with 20-event replay
- `/stats` derived telemetry + scene_gate internals
- Salience telemetry in `/status`
- 22 / 22 tests

### v7.0.1 (this run)
- **Bug found on live daemon** at 06:30 IST: `GET /stats` → 500
  `"'function' object has no attribute 'get'"`.
- **Root cause:** `/stats` handler in `events.py` did
  ```python
  st = getattr(pipeline, "get_detailed_status", None)
  if st is None: st = pipeline.get_status()
  frames = st.get("frames_processed", 0)   # ← .get() on a method
  ```
  The live pipeline exposes `get_detailed_status` (returns a dict), but
  the handler stored the bound method itself and tried to call `.get()`.
- **Fix:** call the method.
  ```python
  st_getter = getattr(pipeline, "get_detailed_status", None) or pipeline.get_status
  st = st_getter()   # ← invoke
  ```
- **Regression test:** `test_stats_live_pipeline_regression` exercises
  a pipeline with both `get_status` and `get_detailed_status` (live
  shape). Asserts all v7.0 fields + nested `scene_gate` dict + derived
  ratios.
- **23 / 23 tests pass** (was 22/22 → +1).
- **`STATUS.md` created** at perceptiond root with live telemetry sample
  + endpoint list.
- **Restarted live daemon** via supervisord. `/stats` and `/status` both
  serve full v7.0 telemetry.

### Live after restart
```
/status
  frames_processed: 23, salient: 1, vlm_invocations: 1, scene_skips: 0,
  motion_score: 0.0581, last_trigger_kind: motion, sse_subscribers: 0
/stats
  salience_ratio: 0.043, vlm_pass_rate: 0.043, skip_rate: 0.0,
  scene_gate: {threshold: 0.02, window: 5, evaluations: 1, skips: 0,
               last_triggered_score: 0.058, baseline_size: 1}
```

### Files touched this run
1. `Services/perceptiond/events.py` — fix `/stats` handler to call the
   status method, not store it.
2. `Services/perceptiond/tests/test_perceptiond.py` — new
   `test_stats_live_pipeline_regression` + registered in `main()`.
3. `Services/perceptiond/STATUS.md` — new file, v7.0.1 status snapshot.

### Out of scope (still parked)
- Cross-daemon: hook memoryd ingest on each description
- aarch64: re-test on Redax
- Bbox overlay on thumbs
- JPEG → WebP

### Decisions
- Test against the production shape (both `get_status` AND
  `get_detailed_status` present) — the legacy mock with just
  `get_status` did not catch this bug.
- Restart via `supervisorctl -c /etc/zo/supervisord-user.conf restart
  perceptiond`. Cleaner than killing pid by hand; supervisord owns the
  service.
- Did **not** add `try/except` around the `st_getter()` call: failing
  loudly on a real production bug is the right behavior; a 500 here
  would have been caught by the new test.

## v7.0.1 SHIPPED 2026-07-07 [end of run]
