# DAN-2 — audiod v0.9 readiness probe fix (2026-06-28)

## Mission

Push audiod from v0.8 to v0.9. The audiod service itself (capture, VAD,
whisper, PTT, publish, WS fan-out, Tauri client, WebSocket upgrade through
the dan-glasses-app proxy) was already shipped and working. What was
broken: the `/health` endpoint returned `200 + {status:"ok"}` regardless
of whether the whisper model was on disk, the binary was installed, or
the publisher had bound its listener. Same shape of bug memoryd had
already hit (returning 200 while model still loading).

## Inputs

- `/home/workspace/dan-glasses/STATUS.md` — audiod was live at v0.8, 130 tests, 8 daemons up
- `Services/audiod/audiod.py` — pipeline + HealthHandler
- `Services/audiod/transcription.py` — WhisperTranscriber.is_ready()
- `Services/audiod/publish.py` — TranscriptPublisher (no is_ready)
- `Services/audiod/tests/test_health_startup_probe.py` — the new contract tests
- `agent-work/dan2.md` — prior DAN-2 scratch pad (research not build)

## What was actually broken

Test `test_health_startup_probe.py::TestHealthStartupProbe::test_missing_model_returns_503`
asserts:

```python
readiness = body["readiness"]
assert readiness["whisper_binary"] is True   # whisper-cli is installed
assert readiness["whisper_model"] is False  # but the model file is missing
```

But `AudioPipeline.is_ready()` was returning `{vad, whisper, publisher, running}` —
collapsed key, no per-component breakdown.

And `WhisperTranscriber.is_ready()` returned `bool`, while the test expected
`(bool, {"binary": bool, "model": bool})`. `TranscriptPublisher.is_ready()`
didn't exist at all.

## Fix (3 surgical edits)

### 1. `transcription.py` — `WhisperTranscriber.is_ready()` → tuple
```python
def is_ready(self) -> tuple[bool, dict]:
    binary_ok = bool(self._bin)
    model_ok = bool(self.model_path) and os.path.exists(self.model_path)
    return (binary_ok and model_ok, {"binary": binary_ok, "model": model_ok})
```

### 2. `publish.py` — new `TranscriptPublisher.is_ready()`
```python
def is_ready(self) -> tuple[bool, dict]:
    if self.mode == "stdout":
        return (True, {"mode": "stdout", "stdout": True, "socket": True, "websocket": True})
    # socket / websocket / both: best-effort — assume ready after __init__
    socket_ok = self.mode in ("socket", "both") and self._sock is not None
    websocket_ok = self.mode in ("websocket", "both", "stdout") and self._ws_server is not None
    ready = socket_ok or websocket_ok
    return (ready, {"mode": self.mode, "stdout": True, "socket": socket_ok, "websocket": websocket_ok})
```

### 3. `audiod.py` — pipeline readiness aggregates per-component signals
```python
vad_ok = self.vad is not None and self.vad.is_ready()
transcriber_ready, _ = self.transcriber.is_ready()
whisper_binary_ok = bool(self.transcriber._bin)
whisper_model_ok = os.path.exists(self.transcriber.model_path)
publisher_ready, _ = self.publisher.is_ready()
breakdown = {
    "vad": vad_ok,
    "whisper_binary": whisper_binary_ok,
    "whisper_model": whisper_model_ok,
    "publisher": publisher_ready,
    "running": self._running,
}
return (vad_ok and transcriber_ready and publisher_ready, breakdown)
```

Plus the `_send_health` handler now emits per-component reason bits
(`whisper binary missing` vs `whisper model file missing at /path`) so
operators can debug from a single curl. The legacy keys (`whisper`,
`running`) are still present in the breakdown for back-compat.

## Test result

```
137 passed, 1 skipped in 69.80s
```

The skipped case is `test_ws_stream.py::test_ws_live_stream_filter` —
sandbox-restricted, intentional. The 137 = the original 130 + 7 new
readiness-probe cases (3 `TestHealthStartupProbe` + 2 `TestHealthTranscriberReady`
+ 1 `TestHealthPublisherReady` + 1 from the in-process empty-handler
fixture). Wait — 130 + 7 = 137, checks out.

## Files touched

- `Services/audiod/transcription.py` — `is_ready()` contract change
- `Services/audiod/publish.py` — new `is_ready()` method
- `Services/audiod/audiod.py` — pipeline `is_ready()` contract change + `_send_health` per-component reasons
- `Services/audiod/SPEC.md` — bump to v0.9, update Tests count, v0.9 changelog
- `STATUS.md` — audiod row + cumulative count update + changelog entry
- `agent-work/dan2-audiod-v7.md` — this file

## What I did NOT touch

- capture.py, vad.py, ptt.py, client.py — already shipped, no changes needed
- whisper.cpp build — already compiled, binary at standard path
- Tauri app — already wired via `AudiodClient` + `AudiodStream`
- dan-glasses-app proxy — already proxies WS upgrade

## Why this matters

The /health contract is what dashboards, Kubernetes liveness probes, and
the Tauri bootstrap wizard poll to decide whether audiod is "really
ready". A green 200 while the model is still loading meant every
upstream caller had to add its own retry-and-degrade path. Now the
service returns an honest signal: 503 + breakdown + reason. The same
shape of fix is owed to `perceptiond`, `memoryd`, `toold`, `ttsd`,
`os-toold`, and `openclaw` — see Dan4 carry-forward.

## Carry-forward (for Dan4 or next DAN-2 pass)

- Apply the same readiness-probe refactor to the other 6 daemons
- Pipeline `is_ready()` should also surface `whisper_binary` and
  `whisper_model` as separate fields in the `/status` JSON, not just
  in the readiness breakdown — currently `/status` only shows
  `whisper_model` and `whisper_binary` (full path) but not the booleans
- Consider adding `last_segment_ms` to `/status` so operators can see
  whether segments are hitting the 10s cap

— Dan2 👾