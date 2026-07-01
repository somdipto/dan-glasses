# TTS Service — `ttsd` (KittenTTS via Python API)

## Purpose
Text-to-speech output for Dan Glasses. Wraps KittenTTS Python bindings with a stable HTTP surface so the wizard and `dan-glasses-app` can stream audio without subprocess fragility.

## Architecture
```
text → KittenTTS Python API → numpy float32 → scipy.io.wavfile (24kHz mono) → audio/wav Response
```

The service is bound to localhost on `:8743` and fronts the global KittenTTS model handle lazily on first request.

## Service Endpoint

- **Health:** `GET http://localhost:8743/health`
- **Speak:** `POST http://localhost:8743/speak` (returns `audio/wav` binary)
- **Play:**  `POST http://localhost:8743/play`  (synth + `aplay` on local speaker)
- **Voices:** `GET http://localhost:8743/voices`
- **Models:** `GET http://localhost:8743/models`

## API Endpoints

### GET /health
Returns:
```json
{"status":"ok","model":"medium","voice":"expr-voice-2-m","kittentts_available":true}
```

### GET /voices
Returns array of voice IDs. Actual set:
```
["expr-voice-2-m","expr-voice-2-f",
 "expr-voice-3-m","expr-voice-3-f",
 "expr-voice-4-m","expr-voice-4-f",
 "expr-voice-5-m","expr-voice-5-f"]
```

### GET /models
Returns: `["medium"]`

### POST /speak
Body: `{"text": "Hello world", "voice": "expr-voice-2-m", "model": "medium"}`
Returns: `audio/wav` — RIFF, 24 kHz mono IEEE Float, ~290 KB for short sentences, ~3.8 s synthesis latency on cold path.
- Latency on warm path: <1 s.
- Caches the KittenTTS model after first request.

### POST /play
Same body as `/speak`. Synthesizes, writes WAV, plays via `aplay` immediately. Used by audiod for live TTS.

## Configuration

- `TTS_VOICE` env (default `expr-voice-2-m`) — used by `/health.voice`.
- `KITTEN_CLI` env — path to `kittentts` CLI fallback (unused by current Python-binding path).

## Constraints

- Single in-process model, single worker. First request after startup pays load cost.
- Audio segment is unmelodic-only — KittenTTS does not currently sing.
- TTS speaks respond with standard WAV (not Opus/MP3) so `<audio>` in the browser can decode natively.

## Port
- `8743`

## Dependencies
- `kittentts` (Python bindings, installed via `pip install kittentts`)
- `numpy`
- `scipy`
- `fastapi`, `uvicorn`
- For `/play`: `aplay` (alsa-utils)

## Wizard / App Integration

- `BootstrapWizard.tsx` polls `/health` for live status. When healthy, fetches `/voices` and posts to `/speak`. The returned blob is wrapped in `URL.createObjectURL` and played via `<audio controls>`.
- `TtsPanel.tsx` exposes ongoing TTS controls (voice pick, sentence typing, play/stop).

## Failure Modes

- `ImportError` for kittentts at startup → `KITTENTTS_AVAILABLE=False`, `/health` returns `status=degraded`, `/speak` returns 503.
- Unsupported `voice` → 400.
- Model generation exception → 500.
