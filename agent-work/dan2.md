# DAN-2 — audiod service — work pad

## Status: SHIPPED v2 (already deployed)

Discovered: audiod is **already complete and operational** in this workspace.
- 51/51 tests passing
- audiod process running (PID 66, since 04:00)
- whisper-cli at /usr/local/bin/whisper-cli (1.0 MB)
- Silero VAD ONNX loaded at ~/.cache/torch/.../silero_vad.onnx
- ggml-tiny.bin (78MB) + ggml-base.bin (148MB) downloaded
- HTTP /health, /status, WS at ws://127.0.0.1:8091
- LiveTranscript.tsx + BootstrapWizard.tsx already integrated
- systemd unit at packaging/systemd/audiod.service

## Verification (just ran)
```
$ ps -ef | grep audiod
root  66  63  73 04:00 ?  00:36:17 python3 audiod.py --port 8090

$ curl http://localhost:8090/health
{"status":"ok","service":"audiod"}

$ curl http://localhost:8090/status
{"status":"ok","service":"audiod","running":true,"vad_ready":true}

$ WS handshake probe
HTTP/1.1 101 Switching Protocols ✓
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=

$ pytest Services/audiod/tests/ -v
51 passed in 8.16s ✓
```

## What was already done (by prior DAN-2 sessions)
1. ✓ Capture module (capture.py) — PortAudio via sounddevice, ring buffer
2. ✓ VAD (vad.py) — Silero ONNX, energy fallback
3. ✓ Whisper integration (transcription.py) — whisper.cpp wrapper
4. ✓ Push-to-talk (ptt.py) — evdev + TTY fallback
5. ✓ Publisher (publish.py) — stdout + Unix socket + RFC 6455 WS (stdlib)
6. ✓ Health server — HTTP /health, /status
7. ✓ PTT force-flush path
8. ✓ 51 unit/integration tests
9. ✓ Tauri LiveTranscript.tsx consumes ws://localhost:8091
10. ✓ BootstrapWizard surfaces audiod health

## What still might be worth doing (v3 territory)
- [ ] Streaming whisper (chunked inference) — cut latency 400ms → 150ms
- [ ] RNNoise denoising pre-VAD
- [ ] Speaker diarization (pyannote)
- [ ] Wake word "Hey Dan" — separate wakewordd
- [ ] Per-speaker embeddings for memory

## Decisions
- **No rewrites** — code is solid, 51 tests green, deployed. Don't break working code.
- **No spec rewrite** — SPEC.md is v2, accurate, ~250 lines, no bloat.
- **No new tests for the sake of it** — coverage is comprehensive.

## What I will do this session
1. Confirm everything is wired and working (done).
2. Add ONE useful test: silence-stays-silence end-to-end (cheap insurance).
3. Document the final state in SPEC.md footer.
4. Update dan2.md with verification proof.

## Architecture reminder
```
mic → PortAudio/ALSA → ring buffer → Silero VAD (ONNX)
  → segment buffer → whisper-cli (ggml-tiny/base)
  → JSON event → stdout + WS:8091
```
