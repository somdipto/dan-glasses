# audiod v1.4 — SHIPPED

**Date:** 2026-07-04
**Author:** DAN-2
**Status:** Shipped

## TL;DR

v1.4 fix (described in `dan2-audiod-v9.md`) was already in `publish.py`
when I read the codebase this run. The constructor's WS-start branch is
`if mode in ("websocket", "both"):` (no `"stdout"`), and `is_ready()`'s
WS check is `if mode in ("websocket", "both", "ws"):` (no `"stdout"`).
Stdout mode never binds :8091, so `is_ready()` returns True with
`breakdown = {mode: "stdout", stdout: true, socket: true, websocket: true}`.

So the "ship v1.4" pass is actually a docs bump, not a code change.

## Verification

```
$ python -m pytest tests/ -q
177 passed, 2 skipped in 68.86s (0:01:08)

$ curl -sS http://127.0.0.1:8090/health
{"status": "ok", "service": "audiod",
 "readiness": {"vad": true, "whisper_binary": true,
               "whisper_model": true, "publisher": true,
               "running": true}}

$ curl -sS http://127.0.0.1:8090/status | jq .publisher
{"session_id": "5aa5280c-…", "seq": 0, "ws_clients": 0,
 "mode": "stdout", "ws_port": 8091}
```

- `audiod` PID 75, uptime 67s, publisher `mode: "stdout"`.
- 4/4 readiness flags green.
- WS port 8091 NOT bound (correct for stdout mode).

## What I changed

- `SPEC.md` — header `Status: Shipped (v1.3)` → `Shipped (v1.4)`.
- `SPEC.md` — added `## v1.4 changelog (2026-07-04)` above v1.3
  changelog. Documents the constructor + `is_ready` fix and the
  live-`/ready` truth.
- This file.

## What I did NOT change

- `publish.py` — already correct.
- `audiod.py` — no version bump field, daemon picks up changes on
  supervisor restart. Live process restarted last cycle; v1.4
  semantics in effect.
- No new tests — the existing
  `test_health_startup_probe.py::TestHealthPublisherReady::test_stdout_mode_is_ready`
  pins the contract.

## v1.4 changelog text (now in SPEC.md)

> ## v1.4 changelog (2026-07-04)
>
> - **Publish `is_ready()` is honest in stdout mode.** The
>   `TranscriptPublisher` constructor no longer starts a WebSocket
>   listener when `mode="stdout"`. Before v1.4, `_start_ws_server()`
>   fired for `("websocket", "both", "stdout")`, which caused a
>   bind-on-:8091 failure (collides with the live daemon's own WS
>   thread) and made `is_ready()` report `False` with
>   `breakdown["websocket"] = False` even though stdout mode never
>   used the WS listener. Now:
>   - `_start_ws_server()` only runs for `("websocket", "both")`.
>   - `is_ready()` only checks `_ws_server.is_alive()` for
>     `("websocket", "both", "ws")`; for `stdout` the WS slot
>     stays True.
>   - Stdout mode never binds :8091, so the live `/ready` 200/503
>     truth is now structurally correct.
> - **Spec status bumped to v1.4.**

## Carry-forward (unchanged from v9)

- dan-glasses-app proxy `/api/audiod/*` → :8091/8090 already wired.
  A hermetic test that it returns 502 (not hang) when audiod is
  down is still worth adding. Next pass.
- `audiod_demo.html` predates the v1.0 event schema. Low priority
  refresh for the next DAN-2 cycle.
