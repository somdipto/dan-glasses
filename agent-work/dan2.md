# DAN-2 — audiod ship notes (v7, 2026-06-17)

**Run window:** 2026-06-17 00:50 UTC
**Task:** Build audiod service — ALSA capture → VAD → whisper.cpp → transcript events.
**Status:** v0.3 shipped. All gaps from v6 closed.

## What this run shipped

- **Bug fix:** `/_send_status` returned 503 when no pipeline was registered.
  Now returns 200 with a `service=audiod, running=False` base envelope,
  merging in `pipeline.stats()` when available. Test
  `test_status_handles_pipeline_unset` now passes.
- **Bug fix:** `_cmd_reload` was