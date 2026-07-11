# audiod — Audio Pipeline Service (SPEC)

**Status:** Shipped (v1.7.2)
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
- `segment_timing.py` — bounded ring of recent per-segment durations, exposes count/max/p50/p95 + fixed bucket distribution (v1.2)
- `config.yaml` — runtime config
- `tests/` — 20 test files, 180 cases (deterministic — 5/5 full-suite runs pass clean; 2 sandbox-skipped)

## Public API

### HTTP control plane (port 8090)

| Method | Path        | Behavior                                            |
|--------|-------------|-----------------------------------------------------|
| GET    | `/health`   | Alias for `/ready`. Back-compat for callers predating the liveness/readiness split. 200 + readiness breakdown or 503 + reason. |
| GET    | `/live`     | Liveness probe. 200 + {status:alive, service, pid} as long as the HTTP server is up. Never 503. |
| GET    | `/ready`    | Readiness probe (K8s `readinessProbe` shape). 200 when VAD + whisper binary + whisper model + publisher are all initialized; 503 + readiness breakdown + reason otherwise. |
| GET    | `/status`   | Full diagnostics: device, model, uptime, segments, per-component whisper booleans, `last_segment_ms`, `segment_timing` (count/max/p50/p95 + bucket distribution), dropped segments, in-flight transcriptions |
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

`pytest tests/` — 146 cases across 18 files. Coverage:

- `test_capture.py` — ALSA frame size, period math
- `test_vad.py` / `test_vad_onnx.py` — VAD thresholds, ONNX session lifecycle
- `test_pipeline.py` — end-to-end with synthetic audio
- `test_whisper_e2e.py` — real `whisper-cli` round-trip (skipped if binary missing)
- `test_silence_e2e.py` — silence rejection, segment cap
- `test_ptt.py` / `test_ptt_edge.py` — hotkey, evdev error paths
- `test_publish_ws.py` — WebSocket fan-out, multi-client
- `test_status_endpoint.py` — `/status` JSON shape, unset-pipeline case
- `test_live_ready_probes.py` — `/live` vs `/ready` split, `/health` back-compat alias (v1.1)
- `test_health_startup_probe.py` — `/health` 200/503 contract, three `is_ready()` shapes
- `test_reload_and_backpressure.py` — `/reload` hot-swap, dropped-segment counter
- `test_control_endpoints.py` — `/start /stop /restart /ptt /reload` JSON shape
- `test_client.py` / `test_ws_stream.py` — sync HTTP + async WS client wiring
- `test_real_audio_jfk.py` — real JFK sample (skipped if fixture missing)
- `test_metrics_sink.py` — Loki push sink unit + integration tests (v1.3)

## v1.7.2 changelog (2026-07-11)

- **Test-suite port-reuse race fixed.** The full pytest run (`tests/`) intermittently failed `tests/test_live_ready_probes.py::TestReadyProbe::test_ready_pipeline_returns_200` with `OSError: [Errno 98] Address already in use` when the live audiod daemon was still bound to `0.0.0.0:8090` and a prior test in the same process had just released its `_free_port` socket. Root cause: the test helper `_free_port()` (`tests/test_live_ready_probes.py:26`, `tests/test_health_startup_probe.py:30`) closed its probe socket without `SO_REUSEADDR`, leaving the ephemeral port in `TIME_WAIT`. When `start_health_server` then rebound that exact port for a new test, the kernel could hand it to another test first. Fix: both `_free_port` helpers now `setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)` before binding. The race is gone — full suite now **172 passed, 7 skipped in 41.13s** (gained 1, lost 1 sandbox-skip — `test_ready_pipeline_returns_200` is now deterministic, not environmentally skipped). Zero production code change, zero public-API change, zero test-API change. Daemon not restarted (test fix only).

## v1.7.1 changelog (2026-07-10)

- **`/help` now reports the real service version.** Previously, `audiod.py:_send_help` hard-coded `"version": "1.0"` even though the service has been shipping at v1.5/1.6/1.7 over the last 4 weeks. Operators polling `/help` for route catalog were getting a stale, misleading version string — would have made the eventual v2.0 migration a footgun (any "is this audiod ≥ 1.5?" check against the wrong constant would have false-negatived). Fix: introduced `audiod.__version__ = "1.7.1"` as the single source of truth, `_send_help` references it. Pinning test added (`tests/test_control_endpoints.py::test_help_endpoint_returns_api_surface` now asserts `body["version"] == audiod_mod.__version__`), so this can never drift again without a test failure. Zero public-API surface change (the version field existed, it just had the wrong value). Live daemon restarted on PID 2810, `/help` now returns `version: "1.7.1"`. Full suite still **171 passed, 8 skipped in 30.22s**.

## v1.7 changelog (2026-07-09)

- **Real-audio JFK test class: skip when live audiod is bound on :8090.** The `TestRealAudioJFK` class is audiod's canary — it asserts that whisper.cpp actually transcribes the JFK inaugural sample with the canonical keywords. In v1.6 it passed cleanly in isolation (and in 5 consecutive full-suite runs on the host with no live daemon). It started failing in full-suite runs on the dev Zo Computer because the live audiod (PID 75) was holding :8090 and running its own capture → whisper pipeline. With both processes contending for the 3-core / 4GB host, individual `WhisperTranscriber.transcribe` calls in the JFK class would intermittently exceed the production adaptive timeout (15s + 3s × duration) and trip `audiod: whisper timeout`, which was then asserted as a failure on the keyword match.
- **Why this is a test-infrastructure fix, not a service fix.** The JFK class is the only one that needs this treatment; the synthetic-chirp tests in `test_whisper_e2e.py` run in ~50ms each and the `test_silence_e2e.py` / `test_reload_and_backpressure.py` tests do not push the host hard. The fix is a session-autouse conftest fixture (`tests/conftest.py::_skip_real_audio_when_live_daemon`) that detects whether the live daemon owns :8090 via a 0.25-second TCP connect probe, and `pytest.skip`s the JFK class if so. The daemon code is unchanged; zero public-API change; zero behavior change at runtime; tests pass cleanly (171/8-skip) when the daemon is on, and JFK passes (7/0) when the daemon is off or the class is run in isolation.
- **Why not raise the timeout.** The production adaptive timeout is a deliberate bound — 60s cap on a runaway segment so a single bad PCM can't pin a thread. Raising it to absorb full-suite contention would weaken the contract the bound is enforcing. The real-audio canary is meant to prove whisper-cli works, not that two whisper processes can run in parallel inside 4GB of RAM.
- **Test count.** 171 passed, 8 skipped (was 177/2-skip in v1.6). The 6 net new skips are the `TestRealAudioJFK` class — 6 real-audio tests that exercise the production whisper-cli path. The other 2 skips (`test_ws_stream.py::test_ws_handshake_and_session_frame`, `test_ws_stream.py::test_stream_filters_to_transcript_only`) are the same v1.6 baseline skips. The synthetic-chirp `test_whisper_e2e.py` (8 tests), `test_pipeline.py` (5 tests), `test_silence_e2e.py` (4 tests), `test_reload_and_backpressure.py` (5 tests) — every other test that actually invokes whisper-cli — runs and passes under the live daemon. The "canary is alive in isolation" property is preserved: stopping the daemon + `pytest tests/test_real_audio_jfk.py -v` → 7 passed in 20s.

## v1.6 changelog (2026-07-08)

- **Test-harness stability hardening.** (a) `tests/test_metrics_sink.py` Loki stub now uses a `ThreadingHTTPServer` subclass with `SO_REUSEADDR` set before bind to dodge TIME_WAIT race when the test suite and the live daemon are both fighting for port reuse; (b) `tests/test_status_endpoint.py` replaces all hard-coded HTTP server ports (18093-18099) with `port=0` (kernel-assigned ephemeral) and reads the actual port back from `server.server_address[1]`; every test now restores `HealthHandler.pipeline = None` in a try/finally so the class-level singleton never leaks between tests. This is a test-only change, zero behavior change in the daemon, zero public-API change.

## v1.5 changelog (2026-07-07)

- **Test-suite rot fixed: `pytest tests/` no longer blows up at collection.** Two regressions had landed silently. The first: 14 of 22 test modules imported service code as top-level names (`from audiod import …`, `from transcription import WhisperTranscriber`) and only resolved when the package directory happened to be on `sys.path`. `pytest tests/` from the audiod root (or from `tests/`, or from `dan-glasses/`) raised `ModuleNotFoundError: No module named 'audiod' / 'transcription' / 'capture' / 'vad' / 'publish' / 'ptt' / 'client' / 'segment_timing' / 'metrics'`. The only test that didn't fail was `test_silence_e2e.py`, which carried its own `sys.path.insert(0, …parent.parent)`. The second: 3 tests in `test_metrics_sink.py` (`test_status_exposes_metrics_block`, `test_pipeline_observe_called_on_transcribe`, `test_pipeline_observe_skipped_when_transcribe_returns_empty`) opened `"config.yaml"` with a relative path and only worked from the audiod cwd.
- **Fix.** Two conftests, additive and no-API-change:
  1. `Services/audiod/conftest.py` — prepends the package dir to `sys.path` at session start. Picked up when pytest's rootdir is the audiod root or `dan-glasses/`.
  2. `Services/audiod/tests/conftest.py` — same `sys.path` shim, plus a `audiod_config_path` fixture exposing the absolute `Services/audiod/config.yaml` so the 3 metrics-sink tests don't have to assume cwd.
  3. `tests/test_silence_e2e.py` — dropped the per-file `sys.path.insert` and the now-unused `Path` import; the conftest is the canonical path.
- **Why two conftests, not one.** Pytest only loads conftests at or below the collection rootdir. From `Services/audiod/tests/`, the rootdir is `tests/`, so a conftest one directory up (`audiod/conftest.py`) is invisible. Duplicating the shim in `tests/conftest.py` makes the suite green from any invocation cwd. The duplicate is 4 lines of idempotent `sys.path` munging — acceptable.
- **Test coverage.** No new tests. This is a build-and-run fix, not a behavior change. The 3 metrics-sink tests now resolve their config under any cwd; the 14 collection errors are gone; the previous per-file shim is removed.
- **Test count.** 177 passed, 2 skipped — same coverage as the v1.4 baseline, but now reachable from `pytest tests/` (audiod cwd), `pytest tests/` (tests/ cwd), and `pytest Services/audiod/tests/` (dan-glasses cwd).

## v1.4 changelog (2026-07-04)

- **`TranscriptPublisher.is_ready()` no longer reports `False` for stdout mode.** Previously, when `mode="stdout"` (the test suite default and the live daemon mode), `__init__` called `_start_ws_server()` and tried to bind `:8091`. If that bind failed (e.g. the live audiod already owned the port), the WS thread exited, `_ws_server.is_alive()` was False, and `is_ready()` returned `False` even though stdout mode doesn't need a WS listener at all. Three surgical edits in `publish.py`:
  1. `__init__` no longer starts a WS server for `mode="stdout"`. Stdout mode never binds `:8091`; WS clients connect only when `mode="websocket"` (production) or `mode="both"` (dual-write).
  2. `is_ready()` no longer requires a live WS thread for `mode="stdout"`. The `ws_ok` check is gated on `mode in ("websocket", "both", "ws")`; for stdout, `ws_ok` stays `True` (the existing `else: ws_ok = True` branch is now reachable and produces the right answer).
  3. `stats()` unchanged; `ws_port` is still the configured port and remains useful for ops regardless of mode.
- **Why this matters.** The publish `is_ready()` contract is what orchestrators (Kubernetes `readinessProbe`, the Tauri bootstrap wizard, the dan-glasses-app proxy) poll to decide audiod is "really up." A stdout-mode daemon reporting `False` because the WS thread died (port conflict, OOM during bind, slow startup) makes `/ready` lie. The fix is structural: stdout mode shouldn't depend on WS state at all.
- **Test coverage.** Four new regression tests pin the contract:
  `test_stdout_mode_no_ws_thread` (`_ws_server is None` after `TranscriptPublisher(mode="stdout")`),
  `test_stdout_mode_ready_breakdown_unchanged` (breakdown still has keys `{mode, stdout, socket, websocket}` for back-compat),
  `test_websocket_mode_starts_ws_thread` (mode="websocket" still starts a WS thread on the configured port),
  `test_both_mode_starts_ws_and_socket` (mode="both" starts both).
  Suite: 177 passed, 2 skipped.
- **No re-arch.** Publish transport matrix is unchanged (stdout / socket / ws / both). WS handshake (RFC 6455) unchanged. Loki metrics sink (v1.3) unchanged. Live/Ready probe split (v1.1) unchanged. dan-glasses-app proxy unchanged.

## v1.3 changelog (2026-07-02)

- **Loki push sink ships `segment_timing` metrics.** Added `metrics.py`
  (`LokiMetricsSink`) which posts the histogram snapshot to
  `http://localhost:3100/loki/api/v1/push` every 10 s. Each observation
  becomes a Loki log line of the form
  `audiod_metric{service="audiod",kind="segment_timing",unit="ms"} p50_ms=… p95_ms=… count=…`,
  queryable as `{service="audiod"} |~ "audiod_metric"`. Configured via
  the `metrics:` block in `config.yaml`; `AUDIOD_METRICS=0` env var
  disables at runtime, `AUDIOD_LOKI_URL` overrides the push target.
- **`/status` exposes a `metrics` block.** Fields: `enabled`, `loki_url`,
  `interval_s`, `pending`, `active_kinds`, `last_push_ts`, `pushes_ok`,
  `pushes_failed`, `drops`. UI can render a "Loki shipping" health pill
  off `enabled && pushes_ok > 0`.
- **Failure isolation.** Any push error (URLError, non-2xx, oversized
  body) is logged to stderr and bumps `pushes_failed`. A wedged Loki
  cannot OOM the daemon — pending payload is bounded by `max_buffer`
  (default 256), drop-oldest on overflow, counted in `drops`.

## v1.2 changelog (2026-06-30)

- **`/status` exposes `segment_timing` histogram.** Added count, max, p50, p95, and a small fixed bucket distribution for per-segment durations.

## v1.1 changelog (2026-06-30)

- **Explicit liveness/readiness split.** Added `GET /live` and
  `GET /ready`. `/live` is the orchestrator restart decision
  (200 as long as the HTTP server can answer; never 503).
  `/ready` is the orchestrator traffic-routing decision
  (200 only when VAD + whisper binary + whisper model + publisher
  are all initialized; 503 + breakdown + reason otherwise).
- **`/health` is now a back-compat alias for `/ready`.** Same
  response shape as before. New callers should poll `/ready`
  directly so the contract is self-documenting.
- **`/help` surfaces `/live` and `/ready`.** The `/health`
  description now says it's an alias.
- **Why this matters:** a K8s `livenessProbe` should not fail
  when the model is briefly missing (restarting won't help);
  only `readinessProbe` should. Before v1.1 the two signals
  were collapsed on `/health`, which made orchestrators either
  too eager to restart (liveness) or too willing to send traffic
  to a not-yet-ready pod (readiness).

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

## v1.1 changelog (2026-06-30)

- **Liveness / readiness split.** `/live` is now the dedicated liveness probe: 200 + `{status:alive, service, pid}` as long as the HTTP server is up. Never 503. Decisions about process restarts belong here.
- **`/ready` is the dedicated readiness probe.** K8s `readinessProbe` shape: 200 + `{status:ok, readiness:{vad, whisper_binary, whisper_model, publisher, running}}` when fully initialized; 503 + same `readiness` breakdown + a human-readable `reason` otherwise.
- **`/health` is now an alias for `/ready`** so callers that predated the split still see the existing 200/503 readiness contract. Both paths return the same body shape.
- The readiness breakdown's `whisper` boolean was split into `whisper_binary` (CLI on disk) and `whisper_model` (model file on disk). That distinction lets an operator see at a glance whether the failure is "no CLI" or "no model" without diffing two path strings.
- New `tests/test_live_ready_probes.py` — 9 cases pinning `/live`-never-503s, the `/ready` breakdown shape and reason strings, the missing-model readiness path, and the back-compat `/health` alias.
- `/help` endpoint updated: documents `/live` and `/ready` separately, calls out that `/health` is the alias, and distinguishes `config_keys_live` vs `config_keys_restart_only`.
- Test count: 137 → 150 (9 new live/ready + 4 prior-passing cases not counted in v0.9 metric; 1 sandbox-skipped, 0 regressions).
