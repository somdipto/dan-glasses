# DAN-2 scratchpad

## Run 2026-06-29

audiod v0.9 already shipped & verified live (PID 77, port 8090, 137/137 tests).

Carry-forward from v0.9 changelog:
1. Apply same /health readiness-probe refactor to other 6 daemons
2. Surface whisper_binary + whisper_model booleans in /status JSON  ← **done**
3. Add last_segment_ms to /status  ← **done**

### What I shipped (v1.0)
- `whisper_binary_ok` + `whisper_model_ok` booleans in `/status`
- `last_segment_ms` in `/status`
- Both stamp under `_lock`; reset by `/start`
- 4 new tests in `test_status_endpoint.py`
- SPEC.md v1.0 changelog entry
- 141 passed / 1 skipped / 0 regressions

### Why I didn't do carry-forward #1
Audited all 6 other daemons. Audiod is the only one with multi-component
readiness (binary + model + publisher). Other daemons return unconditional
{status:ok} on /health, but they don't have a binary/model split — a generic
"is loading" check would require per-daemon design (e.g. ttsd: model vs
kittentts availability, perceptiond: vlm queue depth, toold: registry
load state). That's a separate design pass, not a mechanical refactor.
Out of scope for a single DAN-2 run.

### What's left for the next run
- Add explicit `/ready` (or upgrade `/health` to 503-when-loading) on
  ttsd, toold, os-toold, perceptiond, dan-glasses-app. Each needs its
  own "what counts as ready" decision.
- Consider mirroring audiod's `whisper_binary_ok` pattern in ttsd
  (`kittentts_available` is already there but not a structured
  readiness breakdown).