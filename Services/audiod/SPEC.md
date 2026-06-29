# audiod — Audio Pipeline Service (SPEC)

**Status:** Shipped (v0.9)
**Owner:** DAN-2
**Repo:** `dan-glasses/Services/audiod/`

## Mission

Convert a live microphone stream into structured transcript events for the
rest of the Dan Glasses system. audiod owns capture, silence detection,
transcription, and event publication.

## Architecture

```
microphone → ALSA capture → Silero VAD → segment buffer → whisper.cpp → JSON event → publish
                                                              ↓
                                                        HTTP control plane (/start /stop /ptt /restart /reload)
                                                              ↓
                                                        WebSocket fan-out (port 8091)
```

Threading model:

| Thread        | Owner          | Job                                       |
|---------------|----------------|-------------------------------------------|
| Main          | `audiod.py`    | CLI, signal handling, lifecycle           |
| Capture       | `capture.py`   | Blocking ALSA `snd_pcm_readi` loop        |
| VAD consumer  | `audiod.py`    | Pops 512-sample frames, runs VAD, segments|
| Transcribe    | `audiod.py`    | Spawns `whisper-cli` per speech segment   |
| Publisher     | `publish.py`   | Stdout / unix-socket / WebSocket fan-out  |
| Health server | `audiod.py`    | HTTP control plane on port 8090           |
| PTT listener  | `ptt.py`       | evdev keyboard watcher (Linux) / fallback |

## Files

- `audiod.py` — pipeline orchestrator + HTTP control plane (`AudioPipeline`, `HealthHandler`, `start_health_server`)
- `capture.py` — `ALSACapture` blocking reader over `libasound`
- `vad.py` — Silero VAD (ONNX) wrapper, 512-sample windows, 16 kHz
- `transcription.py` — `whisper-cli` subprocess driver, JSON-sidecar confidence
- `ptt.py` — push-to-talk trigger (evdev on Linux, polling fallback elsewhere)
- `publish.py` — `TranscriptPublisher` (stdout / unix-socket / WebSocket)
- `config.yaml` — runtime config
- `tests/` — 11 test files, 73 cases (see `tests/README.md`)

## Public API

### HTTP control plane (port 8090)

| Method | Path        | Behavior                                            |
|--------|-------------|-----------------------------------------------------|
| GET    | `/health`   | Liveness probe — always 200 if server is up         |
| GET    | `/status`   | Full diagnostics: device, model, uptime, segments   |
| GET    | `/config`   | Current effective config                            |
| GET    | `/help`     | Discover the audiod HTTP API surface as JSON                   |
| POST   | `/start`    | Start capture loop (idempotent)                     |
| POST   | `/stop`     | Stop capture loop, keep WS clients connected        |
| POST   | `/restart`  | Stop + Start                                        |
| POST   | `/ptt`      | Fire push-to-talk trigger                           |
| POST   | `/reload`   | Re-read `config.yaml` from disk                     |

All control endpoints return JSON. When the pipeline is not yet constructed
(e.g. process still booting), `/status` returns 200 with `running: false`
and `vad_ready: false` so UI clients can render an "unreachable" state
without 5xx noise.

### WebSocket event stream (port 8091)

`ws://localhost:8091/` — newline-delimited JSON. One event type today:

```json
{
  "type": "transcript",
  "text": "hello world",
  "start_ms": 1240,
  "end_ms": 2680,
  "confidence": 0.83,
  "ts": 1718612345678
}
```

`confidence` is the mean per-token probability from
`whisper-cli -ojf`. 0.0 means the JSON sidecar was missing and the
service fell back to stdout-only transcription.

### Stdout

JSON lines on stdout when `publish.mode = stdout` (default for tests
and local dev). Wire format matches the WebSocket payload exactly.

## Config (`config.yaml`)

```yaml
audio:
  device: "default"        # ALSA device, "default" = /etc/asound.conf plughw
  sample_rate: 16000
  channels: 1
  period_size: 512         # 32 ms at 16 kHz
  buffer_periods: 8        # 256 ms ring buffer

vad:
  threshold: 0.5
  min_speech_ms: 250
  min_silence_ms: 200
  max_segment_ms: 10000    # hard cap — force-flush a held segment

whisper:
  model: "/path/to/ggml-base.en.bin"
  language: "auto"
  threads: 2
  binary: "whisper-cli"    # overridable for non-`$PATH` installs

publish:
  mode: "stdout"           # "stdout" | "unix" | "ws"
  socket_path: "/tmp/audiod.sock"
  ws_port: 8091

push_to_talk:
  enabled: true
  hotkey: "space"          # see ptt.py for supported keys
```

`POST /reload` re-reads this file and rebuilds the affected components.
Live hot-swap (no restart): VAD threshold, whisper model path, whisper
threads, whisper language. The whisper binary path is re-resolved on
every reload so newly-installed `whisper-cli` is picked up.

`/reload` reports `pending_restart_for` for fields that cannot change
without dropping the capture loop: `audio.{device,sample_rate,
channels,period_size,buffer_periods}`, `publish.{mode,socket_path,
ws_port}`, and `push_to_talk.hotkey`. Operators use `/restart` to
apply those.

## Lifecycle

1. `audiod.py` reads `config.yaml`.
2. Construct `ALSACapture`, `VADSpeechDetector`, `WhisperTranscriber`.
3. Start HTTP control plane on port 8090.
4. Start WebSocket publisher on port 8091.
5. `/start` flips the capture loop on; `/stop` flips it off.
6. SIGTERM / SIGINT → stop capture, drain in-flight segments, close
   publisher sockets, exit 0.

## Push-to-Talk

`ptt.py` runs an evdev listener on Linux. When `push_to_talk.enabled`
is true and the configured hotkey is pressed, audiod immediately
treats the current audio buffer as a segment boundary, regardless of
VAD state. This is the only way to interrupt a long silence and force
transcription of the trailing utterance.

On non-Linux hosts (e.g. macOS dev) the listener degrades to a polling
stdin reader, which is also reachable via `POST /ptt` for headless
control.

## Segment capping (force-flush)

VAD is conservative about silence. Without a cap, a single long
monologue with no >200ms pause can accumulate >30s of audio and stall
the segment → whisper pipeline. `vad.max_segment_ms` (default 10s) is
checked on every frame: if the held segment exceeds it, the buffer is
force-flushed to whisper even if VAD still reports "speech". This keeps
end-to-end latency bounded.

## Whisper confidence

`whisper-cli -ojf` emits a `.json` sidecar with per-token
`p` values. `transcription._parse_output` reads that sidecar, computes
the mean per-token probability, and uses it as the event `confidence`.
If the sidecar is missing (older whisper.cpp, stripped flag), the
service falls back to the stdout transcript and `confidence: 0.0`.

The numeric is **probability**, not log-prob. UI multiplies by 100 for
percent display.

## Failure modes

| Symptom                                | Cause                              | Behavior                              |
|----------------------------------------|------------------------------------|---------------------------------------|
| `audiod unreachable` chip              | audiod process not running         | UI shows red chip, disables controls  |
| `vad_ready: false`                     | Silero ONNX model missing          | Capture continues, segments are full-buffer |
| whisper stalls                         | Model not at `whisper.model` path  | Transcribe thread logs error, skips  |
| WS clients accumulate                  | Server never prunes dead clients   | Publisher pings every 30s, drops >60s idle |
| Force-flush too aggressive             | `max_segment_ms` too low           | Utterances cut mid-word                |
| Adaptive whisper timeout               | —                                  | —                                     |

## Tests

`pytest tests/` — 137 cases across 17 files. Coverage:

- `test_capture.py` — ALSA frame size, period math
- `test_vad.py` / `test_vad_onnx.py` — VAD thresholds, ONNX session lifecycle
- `test_pipeline.py` — end-to-end with synthetic audio
- `test_whisper_e2e.py` — real `whisper-cli` round-trip (skipped if binary missing)
- `test_silence_e2e.py` — silence rejection, segment cap
- `test_ptt.py` / `test_ptt_edge.py` — hotkey, evdev error paths
- `test_publish_ws.py` — WebSocket fan-out, multi-client
- `test_status_endpoint.py` — `/status` JSON shape, unset-pipeline case
- `test_event_schema_conformance.py` — event JSON contract stability
- `test_health_startup_probe.py` — `/health` 200/503 contract, three `is_ready()` shapes
- `test_reload_and_backpressure.py` — `/reload` hot-swap, dropped-segment counter
- `test_control_endpoints.py` — `/start /stop /restart /ptt /reload` JSON shape
- `test_client.py` / `test_ws_stream.py` — sync HTTP + async WS client wiring
- `test_real_audio_jfk.py` — real JFK sample (skipped if fixture missing)

## v1.0 changelog (2026-06-29)

- **`/status` exposes per-component whisper readiness booleans.** Added
  `whisper_binary_ok` and `whisper_model_ok` to the diagnostics snapshot
  so operators can distinguish a missing `whisper-cli` binary from a
  missing model file without reading stderr. The path strings
  (`whisper_binary`, `whisper_model`) remain — booleans are additive.
- **`/status` exposes `last_segment_ms`.** Duration of the most recently
  transcribed segment in milliseconds. `0` before any segment has been
  transcribed in the current lifetime. Reset by `/start` alongside the
  other lifetime counters. Useful for diagnosing long-tail latency
  without tailing logs.
- Both fields stamp under the same `_lock` that guards
  `_segments_transcribed` so a concurrent `/status` cannot observe a
  half-updated state.
- `/help` description updated for `/status`.
- New tests in `tests/test_status_endpoint.py` (4 cases): the two
  boolean readiness fields default to true when whisper is wired up,
  `last_segment_ms` defaults to 0, increments after a successful
  transcription, and resets on `/start`.
- Test count: 137 → 141 (4 new, 0 regressions).

## v0.9 changelog (2026-06-28)

- **Readiness probe hardened.** `/health` no longer returns unconditional
  200 ok. Returns **503 + status:loading** when any required component
  is not ready; returns **200 + status:ok** only when VAD, whisper binary,
  whisper model file, and publisher are all initialized.
- **Three `is_ready()` contracts aligned.** `WhisperTranscriber.is_ready()`,
  `TranscriptPublisher.is_ready()`, and `AudioPipeline.is_ready()` all
  return `(bool, dict)` so `/health` can render a per-component breakdown.
- **Per-whisper signal exposed.** The pipeline readiness breakdown now
  surfaces `whisper_binary` and `whisper_model` as separate flags so
  operators can distinguish a missing CLI binary from a missing model
  file without reading stderr.
- **Reason string on 503.** `HealthHandler._send_health` builds a
  human-readable `reason` from the failing flags (e.g.
  "whisper binary or model not ready").
- New `tests/test_health_startup_probe.py` — 9 cases pinning the
  200/503 contract, the no-pipeline case, the missing-model case, and
  the three `is_ready()` shapes.
- Test count: 130 → 137 (7 new, 0 regressions).

## v0.8 changelog (2026-06-27)

- WebSocket upgrade through `dan-glasses-app` proxy: `/api/audiod/stream` now bridges browser upgrades to audiod `:8091`. New `_serve_ws_upgrade` in `Services/dan-glasses-app/server.py` opens a raw TCP socket to the upstream, replays the handshake with path rewritten to `/`, validates the upstream 101, then bidirectionally pumps frames with `TCP_NODELAY` on both ends.
- New `Services/dan-glasses-app/test_ws_upgrade.py` — 2 cases (101 Switching Protocols, ping→pong round-trip). Skips if dan-glasses-app not reachable.
- Spec delta: WebSocket fan-out surface is now reachable through the proxy in addition to direct `ws://localhost:8091/`.
- Test count: 121 → 130 (9 new, 0 regressions).

## v0.7 changelog (2026-06-21)

- New `client.py` — `AudiodClient` (sync HTTP) + `AudiodStream` (async WS).
- New `tests/test_client.py` (19 cases) and `tests/test_ws_stream.py`
  (2 cases, 1 sandbox-skipped) — covers dataclass wiring, all 8 HTTP
  routes, offline-host error path, WS handshake, and stream filter.
- New `Services/dan-glasses-app/static/audiod_demo.html` — drop-in
  browser demo of the full control + stream contract.
- Test count: 101 → 121 (21 new, 0 regressions).
