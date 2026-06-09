# audiod — Audio Pipeline Service (v2)

## Purpose
Always-on audio capture → VAD → transcription for Dan Glasses.
Low-latency STT for the wearable. v2 ships a WebSocket transport and PTT
fallback; same v1 capture/VAD/STT core.

## Architecture
```
mic → PortAudio/ALSA → ring buffer → Silero VAD (ONNX) → speech segment
       → whisper.cpp (ggml-tiny or ggml-base) → JSON event
       → stdout + Unix socket + WebSocket (ws://127.0.0.1:8091)
```

## Pipeline Stages

### 1. ALSA Capture (`capture.py`)
- Library: `sounddevice` (PortAudio bindings)
- Sample rate: 16 kHz mono int16
- Period size: 512 frames (32 ms)
- Ring buffer: 60 s capacity
- Device: `default` or substring match against `sd.query_devices()`
- **Fallback**: `_mock_capture_loop()` emits silence when no audio device
  is available (sandboxed CI, headless hosts). The pipeline stays
  end-to-end runnable even without hardware.

### 2. VAD (`vad.py`)
- Model: **Silero VAD via ONNX Runtime** (no torch dependency, lighter
  wheel than the PyTorch Silero VAD)
- ONNX path: `~/.cache/torch/hub/snakers4_silero-vad_master/src/silero_vad/data/silero_vad.onnx`
- Input shape: `[1, 512]` float32, 16 kHz
- Hidden state: `[1, 1, 64]` float32 — maintained across calls, reset on
  `reset()` (after each flushed segment)
- Threshold: 0.5 (default), exposed via `vad.threshold`
- Min speech: 250 ms; min silence to end: 200 ms
- **Energy fallback**: when ONNX model is missing, `_energy_vad` returns
  RMS/2000. Good enough to keep the pipeline alive, bad enough to flag
  the deployment as degraded via `/status` (`vad_ready=false`).

### 3. Segment Buffer (`vad.py:VADSpeechDetector`)
- Pre-roll: 200 ms of audio before speech onset (gives whisper
  consonant context)
- `_speech_buffer: list[np.ndarray]` accumulates PCM chunks
- `_flush_segment()` runs on min-silence-met
- `force_flush()` is the PTT path — drains the buffer immediately

### 4. Transcription (`transcription.py`)
- Binary: `/usr/local/bin/whisper-cli` (1.0 MB statically-linked, from
  whisper.cpp commit 2025-04-18)
- Model: `ggml-base.bin` (148 MB, default) or `ggml-tiny.bin` (78 MB,
  recommended on Redax aarch64)
- Flags: `-ng` (no GPU), `-ml 1` (max segment length 1, faster first
  result for low-latency mode), `-l auto` or `-l en`
- Input format: 16 kHz mono WAV (whisper-cli does not accept raw PCM,
  we write a tiny WAV header in a tempfile)
- Timeout: 10 s
- Output: stdout, regex-stripped of `[hh:mm:ss.sss --> hh:mm:ss.sss]`
  prefix; `[BLANK_AUDIO]` is mapped to empty text

### 5. Publish (`publish.py`)
- **stdout**: JSON lines, one event per line, flushed immediately
- **Unix socket**: `/run/audiod.sock` (TCP via UDS) — simple socket
  for in-process consumers
- **WebSocket**: `ws://127.0.0.1:8091`, full RFC 6455 server in 200
  lines of pure-stdlib Python (no `websockets` dep at runtime)
  - Per-client send queue (deque, maxlen 512) so a slow client can't
    stall the publisher
  - Backpressure: queue full → drop client (`c.close()`)
  - Ping/pong handled
  - Rejects non-WebSocket upgrades with HTTP 400
- Event schema:
  ```json
  {
    "type": "transcript",
    "session_id": "uuid",
    "event_id": "uuid",
    "seq": 42,
    "text": "what was said",
    "start_ms": 1234,
    "end_ms": 5678,
    "confidence": 0.92,
    "ts_ms": 1780000000000
  }
  ```

### 6. Push-to-Talk (`ptt.py`)
- Linux: `evdev` listening for `EV_KEY` value=1 (keydown)
- Fallback: TTY cbreak + `select` for "press space to flush"
- Configurable hotkey (default: `space`)
- `force_flush()` returns the current segment, transcribed immediately
- Currently off by default (`push_to_talk.enabled: false`); flip when
  the wearable button is wired

### 7. Health Server (`audiod.py:start_health_server`)
- HTTP on `0.0.0.0:8090` (configurable via `--port`)
- `GET /health` → `{"status":"ok","service":"audiod"}`
- `GET /status` → `{"status":"ok","service":"audiod","running":bool,"vad_ready":bool}`
- Used by the Tauri app via fetch

## Configuration (`config.yaml`)
```yaml
audio:
  device: default
  sample_rate: 16000
  channels: 1
  period_size: 512
  buffer_periods: 8

vad:
  threshold: 0.5
  min_speech_ms: 250
  min_silence_ms: 200

whisper:
  model: /home/workspace/dan-glasses/models/ggml-base.bin
  language: auto
  threads: 2

publish:
  mode: stdout            # stdout | socket | websocket | both
  socket_path: /run/audiod.sock
  ws_port: 8091

push_to_talk:
  enabled: false
  hotkey: space
```

CLI overrides: `--model PATH`, `--device NAME`, `--port N`.

## File Structure
```
Services/audiod/
├── SPEC.md
├── README.md
├── config.yaml
├── requirements.txt
├── audiod.py            # main entrypoint + health server
├── capture.py           # PortAudio/ALSA capture + ring buffer
├── vad.py               # Silero VAD via ONNX + energy fallback
├── transcription.py     # whisper.cpp runner
├── ptt.py               # push-to-talk trigger
├── publish.py           # stdout + Unix socket + WebSocket publisher
├── scripts/
│   ├── audiod-launch.sh
│   └── download-model.sh
└── tests/
    ├── test_capture.py          # ring buffer + capture lifecycle
    ├── test_vad.py              # energy fallback
    ├── test_vad_onnx.py         # ONNX Silero VAD
    ├── test_ptt.py              # PTT lifecycle + fallback path
    ├── test_publish_ws.py       # WS frame encoding + handshake + ping/pong
    ├── test_pipeline.py         # integration: capture → VAD → publish
    └── test_whisper_e2e.py      # end-to-end: synth → whisper-cli → text
```

## Dependencies (`requirements.txt`)
- `numpy==2.2.3`
- `sounddevice==0.5.2`
- `onnxruntime==1.24.4`
- `PyYAML==6.0.2`
- `pytest==8.3.5`
- `websockets>=12.0` (test-only — runtime WS is stdlib)
- `evdev>=1.7.0` (Linux only)

## Usage
```bash
# one-time: download model
bash scripts/download-model.sh base

# run
bash scripts/audiod-launch.sh
# or directly
python3 audiod.py --config config.yaml

# verify
curl http://localhost:8090/health
curl http://localhost:8090/status

# stream transcripts from the Tauri app
ws://localhost:8091
```

## Tauri Integration
- `audiod_health()` (lib.rs) → `GET http://localhost:8090/health`
- `is_audiod_running()` (lib.rs) → `GET /status` and check `vad_ready`
- `LiveTranscript.tsx` (dan-glasses-app) → `new WebSocket("ws://localhost:8091")`
  with auto-reconnect, live-dot status indicator, max 50 events ring buffer
- `BootstrapWizard.tsx` (dan-glasses-app) → surfaces audiod health in setup

## Latency Budget (target: <1 s speech-to-text on x86_64 laptop)
| Stage | Latency |
|---|---|
| VAD end-of-segment detection | 200 ms (min silence) |
| whisper-cli first-result (ggml-tiny, 2 threads) | 200-500 ms |
| WS frame send | <5 ms |
| **Total** | **400-700 ms** |

## Tests
- **51 passing** (7 files)
- 6 capture / ring buffer
- 6 VAD (energy fallback)
- 7 VAD (ONNX Silero)
- 7 PTT (lifecycle + fallback)
- 18 publish (frame encode/decode + WS server handshake + ping/pong)
- 4 pipeline integration
- 3 whisper end-to-end (real whisper-cli + ggml-tiny)

## Status: SHIPPED v2 ✅
- 51/51 tests passing
- whisper-cli at /usr/local/bin/whisper-cli (1.0 MB)
- ggml-base.bin (148 MB) + ggml-tiny.bin (78 MB) at /home/workspace/dan-glasses/models/
- Silero VAD ONNX at ~/.cache/torch/hub/.../silero_vad.onnx
- WebSocket streaming on port 8091 (RFC 6455, stdlib)
- Tauri `LiveTranscript.tsx` connects to ws://localhost:8091
- systemd unit at packaging/systemd/audiod.service

## v3 Roadmap
- Streaming whisper (low-latency chunked inference) — currently
  400-700 ms end-to-end; streaming could cut to 150-300 ms
- Noise suppression (RNNoise) before VAD
- Speaker diarization (pyannote.audio) — multi-user wearables
- On-device wake word ("Hey Dan") — separate `wakewordd` service
- Per-speaker embedding indexing for memory context
