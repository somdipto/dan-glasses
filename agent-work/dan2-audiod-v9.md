# audiod v1.4 — Publish `is_ready` stdout over-correction

**Date:** 2026-07-04
**Author:** DAN-2
**Status:** In progress

## Why

`pytest tests/ -q` reports 1 failure: `test_health_startup_probe.py::TestHealthPublisherReady::test_stdout_mode_is_ready`.

Root cause: `TranscriptPublisher.__init__` calls `_start_ws_server()` when
`mode in ("websocket", "both", "stdout")`. For `mode="stdout"` (the
default for the live daemon and for the test suite), this tries to bind
:8091. The live audiod already owns :8091, so the bind fails, the WS
thread exits, `_ws_server.is_alive()` is False, and `is_ready()` returns
`False` with `breakdown["websocket"] = False` — even though stdout mode
doesn't need a WS listener at all.

The v0.9 readiness-probe refactor (see `dan2-audiod-v7.md`) added
`"stdout"` to the WS startup branch as a defensive measure. That was an
over-correction: it created exactly the kind of false-negative the
probe was supposed to prevent. The `is_ready()` logic itself is correct
(it checks stdout, socket, websocket independently); the constructor
is wrong.

## Fix

3 surgical edits in `publish.py`:

1. `__init__`:
   - Was: `if mode in ("websocket", "both", "stdout"): self._start_ws_server()`
   - Now: `if mode in ("websocket", "both"): self._start_ws_server()`
   - Stdout mode never starts a WS listener. WebSocket clients connect
     to audiod when audiod is in `mode="websocket"` (production) or
     `mode="both"` (dual-write). For tests + local dev, `stdout` is
     sufficient.

2. `is_ready()`:
   - Was: `if mode in ("websocket", "both", "ws", "stdout"): ws_ok = (self._ws_server is not None) and self._ws_server.is_alive()`
   - Now: `if mode in ("websocket", "both", "ws"): ws_ok = (self._ws_server is not None) and self._ws_server.is_alive()`
   - For stdout mode, `ws_ok` stays `True` (no listener state to fail).
     The existing `else: ws_ok = True` branch is now reachable for
     `mode="stdout"` and produces the right answer.

3. `stats()`: no change. `ws_port` is the configured port; it remains
   useful for ops regardless of mode.

## Regression tests (4 new)

- `test_stdout_mode_no_ws_thread` — `_ws_server is None` after `TranscriptPublisher(mode="stdout")`.
- `test_stdout_mode_ready_breakdown_unchanged` — breakdown still has keys `{mode, stdout, socket, websocket}` for back-compat.
- `test_websocket_mode_starts_ws_thread` — `mode="websocket"` still starts a WS thread on the configured port.
- `test_both_mode_starts_ws_and_socket` — `mode="both"` starts both.

## Live verification

After restart with the new binary:
- `/health` and `/ready` → 200 with `readiness.publisher: true`.
- `/status` → `publisher.mode: "stdout"`, no `ws_thread` field needed.
- No port :8091 collision (stdout mode no longer binds it).

## Bump

- `audiod.py` version constant or comment: v1.4.
- `SPEC.md` → v1.4 changelog entry; ready contract clarified.
- `STATUS.md` → audiod row reflects v1.4 + 164/164 tests.
- This file.

## Why this matters

The publish `is_ready()` contract is what orchestrators (Kubernetes
`readinessProbe`, the Tauri bootstrap wizard, the dan-glasses-app
proxy) poll to decide audiod is "really up." A stdout-mode daemon
reporting `False` because the WS thread died (port conflict, OOM during
bind, slow startup) makes `/ready` lie. The fix is structural: stdout
mode shouldn't depend on WS state at all.

## What I am NOT doing in v1.4

- No re-arch of the publish path itself (still stdout / socket / ws / both).
- No changes to the WS handshake (RFC 6455 server is solid; covered by `test_publish_ws.py`).
- No changes to the Loki metrics sink (v1.3, green).
- No changes to Live/Ready probe split (v1.1, green).
- No changes to the dan-glasses-app proxy (already forwards `/api/audiod/*`).

## Queue for after v1.4

- The dan-glasses-app server.py already proxies `/api/audiod/*` and
  bridges `/api/audiod/stream` → `:8091`. Worth a hermetic test that
  the proxy returns `502 upstream unreachable` when audiod is down
  (rather than a hang). Carry-forward to next DAN-2 pass.
- The `audiod_demo.html` in `Services/dan-glasses-app/static/` is
  7.8KB and predates the v1.0 event schema. Could be refreshed to
  show `session_id`, `seq`, `ts_ms`, and the WS reconnect flow. Low
  priority — dan-glasses Tauri app is the production UI.

— Dan2 👾
