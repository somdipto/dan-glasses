# DAN-2 — audiod service — work pad

## Status: SHIPPED v2.4 — schema conformance fix + Tauri integration audit

## v2.4 (this session, 2026-06-12)

### What I shipped
1. **publish.py: schema-conformance fix for `publish_transcript()` helper**
   - Bug: helper emitted partial event (only type/text/start/end/confidence)
     while the publisher emits the full 9-key contract pinned by
     test_event_schema_conformance.py. The helper was the one route that
     bypassed the publisher.
   - Fix: route the helper through a module-level lazy
     `TranscriptPublisher` singleton. Same one-liner API; same event shape.
   - Test: `test_publish_transcript_helper_shape` now passes.
2. **Test count: 65 → 66 (all green)** at
   /home/workspace/dan-glasses/Services/audiod

### Tauri integration audit (already complete, no changes needed)
The task lists 8 steps as if audiod doesn't exist. Reality (verified):
- Step 1-2: audiod service directory + SPEC.md exist (v2.1, 270 lines,
  covers ALSA, Silero VAD, whisper.cpp, WS, PTT, latency, Tauri
  integration, status)
- Step 3-4: ALSA capture + Silero VAD via ONNX — `capture.py` +
  `vad.py` working, `vad_ready=true` per live `/status`
- Step 5: whisper.cpp compiled at `/usr/local/bin/whisper-cli` (1.0MB
  ELF), integrated via `transcription.py`, models at
  `models/ggml-{base,tiny}.bin`
- Step 6: push-to-talk — `ptt.py` with evdev (Linux) + TTY fallback
- Step 7: tests — 66/66 green
- Step 8: Tauri integration — verified clean:
  - `apps/dan-glasses-app/src-tauri/src/audiod.rs` — Rust Tauri
    commands `audiod_health()`, `audiod_status()`, `is_audiod_running()`
    over HTTP :8090 (correct)
  - `dan-glasses-app/src/components/LiveTranscript.tsx` — WebSocket
    client to :8091 (correct, auto-reconnect, max-50 ring buffer)
  - `BootstrapWizard.tsx` — audiod health check on port 8090 (correct)

### Operational state
```
$ curl -s :8090/health
{"status":"ok","service":"audiod"}

$ curl -s :8090/status
{"status": "ok", "service": "audiod", "running": true, "vad_ready": true}

$ python3 -m pytest tests/ -q
66 passed in 13.96s
```

### Code changes this session
- `Services/audiod/publish.py` — added module-level lazy
  `_stdout_publisher` singleton; `publish_transcript()` now routes
  through it. Net +25 lines.

## v2.3 (2026-06-11 04:50 UTC) — STT v3 candidate probe
- LFM2.5-Audio-1.5B: not yet viable (no local model, no public
  ONNX/GGUF export, no streaming path). Carry.
- 6 conformance tests added; 55 → 61

## v2.2 (2026-06-11 01:00 UTC) — whisper BLANK_AUDIO tokenization fix
- 1 failing test → 55/55 green
- Committed: 4fc1a1f

## v2.1 (2026-06-10 23:30 UTC) — silence invariants
- 4 new tests; 51 → 55 green
- Committed: b7c6787

## v2 (2026-06-09) — full v2 baseline
- WebSocket transport, PTT, whisper.cpp, 51/51 green
- Committed: 57ac585

## Architecture
```
mic → PortAudio/ALSA → ring buffer → Silero VAD (ONNX)
  → segment buffer → whisper-cli (ggml-tiny/base)
  → JSON event → stdout + Unix socket + WS:8091
  → Tauri Rust: HTTP :8090 commands (audiod.rs)
  → Tauri TS:   WebSocket :8091 (LiveTranscript.tsx)
```

## Decisions
- Pin the on-the-wire schema — Python publisher, Rust Tauri commands,
  TypeScript WS client all depend on it. test_event_schema_conformance
  is the contract.
- `publish_transcript()` helper must route through the publisher
  (it was bypassing it and emitting partial events). Caught by the
  conformance test. Fix = lazy singleton.
- Don't ship the v2 baseline again — code is good, deployed, tested.
  v2.4 is a maintenance fix, not a rewrite.

## v3 Roadmap
- Streaming whisper (150-300 ms vs current 400-700 ms)
- Noise suppression (RNNoise) before VAD
- Speaker diarization (pyannote.audio)
- Wake word ("Hey Dan") — separate `wakewordd` service
- Per-speaker embedding indexing for memory context
