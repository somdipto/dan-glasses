# DAN-2 — audiod v0.6 (2026-06-19)

## Bug fix: /restart does not reset counters

**Observed:**
- `_started_at_ms` refreshes on /start (so uptime resets correctly)
- BUT `_segments_transcribed`, `_dropped_segments`, `_transcribe_inflight` persist across restart
- After /restart, /status shows segment count from the prior lifetime

**Fix:** Move counter reset to a private helper called by /start. Keeps idempotency guard intact.

**Also fix:** Dead `signal_handler` in `main()` — overwritten on line 575 by `_signal_shutdown`. Remove.

**Regression tests:** 2 new tests in test_pipeline.py
- test_restart_resets_counters — restart twice; segments_transcribed == 0 after restart
- test_restart_resets_uptime — uptime < 5000ms right after restart

**Plan:**
1. Edit audiod.py: add `_reset_counters()`, call from `_cmd_start`
2. Edit audiod.py: remove dead signal_handler
3. Add 2 regression tests
4. Run pytest, confirm 98/98 pass
5. Bump SPEC.md status to v0.6
