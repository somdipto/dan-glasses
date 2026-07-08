# audiod v1.1 — Live/Ready Probe Split

**Date:** 2026-06-30
**Author:** DAN-2
**Status:** Shipped

## Why

v0.9 mapped everything onto `/health`. That conflated two orthogonal
orchestrator questions:

- **Liveness** — "is the process responsive? Decide whether to restart it."
- **Readiness** — "is the pipeline usable? Decide whether to route traffic."

For a microphone-capture service this matters twice over:

- During boot, `whisper-cli` is still warming up the ggml graph. A single
  `/health` endpoint that 503s until the model is loaded confuses a liveness
  probe into restarting a perfectly healthy process that's just slow to
  initialize.
- During ALSA re-bind after a USB mic hot-swap, VAD may not be ready but the
  HTTP server still answers. Restarting the process just to recover is
  wasteful when only the capture thread is affected.

The K8s pattern is: split them. `/live` for restart decisions, `/ready` for
traffic routing. Back-compat stays for callers that still hit `/health`.

## What shipped

**`audiod.py` — `HealthHandler`**

- New `do_GET` routes:
  - `/live` → 200 + `{status: alive, service: audiod, pid}`. Never 503.
  - `/ready` → 200 + readiness breakdown OR 503 + breakdown + reason.
  - `/health` → alias for `/ready` (same body, same status). Preserved old
    shape: `{status, service, readiness, ...}`.
- `is_ready()` (existing) factored to drive `/ready` directly.
- `stats()` already returned `whisper_binary_ok` / `whisper_model_ok`; those
  aliases are now first-class in the readiness breakdown too.

**`audiod.py` — `/help`**

- Documents `/live` and `/ready` as separate rows.
- Annotates `/health` as the back-compat alias.
- Splits `config_keys_live` (VAD threshold, whisper model/threads/language) vs
  `config_keys_restart_only` (ALSA device/SR/channels, publisher, PTT hotkey).

**`tests/test_live_ready_probes.py` — 9 cases**

- `/live` never 503s (no-pipeline case, pid check).
- `/ready` 503 with correct breakdown on: no pipeline, missing model file.
- `/ready` 200 with all-true readiness when fully initialized.
- `/health` shape equals `/ready` shape (alias contract).
- Reason strings carry through for operators (`"vad not initialized"; "whisper
  model not ready"`).

## Tests

```
$ python3 -m pytest tests/ -x
150 passed, 1 skipped in 69.87s (0:01:09)
```

The 1 skip is the sandbox-only WS round-trip guard.

## Files

| File                              | Change                              |
|-----------------------------------|-------------------------------------|
| `audiod.py`                       | `/live` + `/ready` + alias `/health` |
| `SPEC.md`                         | v1.1 changelog, probe contract table  |
| `STATUS.md`                       | audiod row + changelog entry         |
| `tests/test_live_ready_probes.py` | 9 new cases                          |

## Risk notes

- All existing tests that hit `/health` still pass — the alias preserves
  shape and status code.
- An orchestrator that previously watched `/health` for readiness sees no
  behavior change; one that watched it for liveness now sees the stricter
  contract (200 always) and might never restart on readiness gaps. That's
  the intended fix.
- No new external surface. The `/help` payload is the only thing that
  mentions `/live` to callers, and a downstream consumer would need to be
  reading it to notice.

## Next

- v1.2: per-segment timing histogram in `/status` (latency p50/p95 under load).
- v1.2: drop `/health` after the dan-glasses-app proxy pins to `/ready`.
