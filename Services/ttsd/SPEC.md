# ttsd — KittenTTS Service (v113)

## Purpose
Text-to-speech output for Dan Glasses. Wraps KittenTTS Python bindings with a stable HTTP surface so the BootstrapWizard and `dan-glasses-app` can preview/stream audio without subprocess fragility.

## Architecture
```
text → KittenTTS Python API (lazy, first request) → numpy float32 → scipy.io.wavfile.write (24kHz mono) → audio/wav Response
```

The service is bound to localhost on `:8743` and instantiates the global KittenTTS model handle lazily on the first `/speak` (or `/play`) call. Single in-process model, single worker.

## Service Endpoints (localhost:8743)
- **Health:** `GET  http://localhost:8743/health`
- **Speak:**  `POST http://localhost:8743/speak`  (returns `audio/wav` binary)
- **Play:**   `POST http://localhost:8743/play`   (synth + `aplay` on local speaker)
- **Voices:** `GET  http://localhost:8743/voices`
- **Models:** `GET  http://localhost:8743/models`

## API Endpoints

### `GET /health`
```json
{"status":"ok","model":"medium","voice":"expr-voice-2-m","kittentts_available":true}
```
- `status="degraded"` when KittenTTS is not installed (ImportError at startup)
- `kittentts_available=false` in that case

### `GET /voices`
```json
["expr-voice-2-m","expr-voice-2-f","expr-voice-3-m","expr-voice-3-f","expr-voice-4-m","expr-voice-4-f","expr-voice-5-m","expr-voice-5-f"]
```

### `GET /models`
```json
["medium"]
```

### `POST /speak`
Body: `{text, voice?, model?}` (defaults: `expr-voice-2-m`, `medium`).
- Returns `audio/wav` — RIFF, 24kHz mono IEEE Float
- ~290KB for a short sentence
- Cold path: ~3s synthesis + ~25s model load
- Warm path: <1s
- 400 on unsupported voice
- 503 on KittenTTS unavailable
- 500 on generation exception

### `POST /play`
Same body as `/speak`. Synthesizes, writes WAV, plays via `aplay` immediately. Used by audiod for live TTS.
- 200 on success with `{status: "played", text: "…"}`

## Configuration
- `TTS_VOICE` env (default `expr-voice-2-m`) — surfaced via `/health.voice`
- `KITTEN_CLI` env — path to `kittentts` CLI fallback (unused by current Python-binding path)

## Constraints
- Single in-process model, single worker
- Audio output is non-melodic — KittenTTS does not currently sing
- WAV (not Opus/MP3) so `<audio>` in the browser can decode natively

## Port
- `8743`

## Dependencies
- `kittentts` (Python bindings, `pip install kittentts`)
- `numpy`
- `scipy`
- `fastapi`, `uvicorn`
- `pydantic`
- `aplay` (alsa-utils) — only required for `/play`

## Tests (6) — `test_ttsd.py`
- `/health` returns 200 with `status` in {ok, degraded}
- `/voices` returns a non-empty list of strings
- `/models` returns list containing `"medium"`
- `/speak` returns 200 with `content-type: audio/wav` and a valid RIFF/WAVE header
- `/speak` with invalid voice returns 400
- `/play` returns 200 with `{status: "played"}`

## Failure Modes
- `ImportError` for kittentts at startup → `KITTENTTS_AVAILABLE=False`, `/health.status=degraded`, `/speak` returns 503
- Unsupported `voice` → 400
- Model generation exception → 500

## Integration
- **BootstrapWizard** polls `/api/services/health` for live status; on the TTS step it calls `/voices` and `/speak` via the dan-glasses-app proxy at `:8747`, wraps the returned blob in `URL.createObjectURL`, and plays via `<audio controls>`. The wizard also runs a self-probe (`probeKittenTTS`) that exercises voices+models+sample bytes and reports the round-trip duration.
- **audiod** can call `/play` for live TTS through the local speaker.
- **Public surface** (via dan-glasses-app proxy) — public, no auth, intended for local LAN.
