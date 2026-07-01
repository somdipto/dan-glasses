"""ttsd — KittenTTS service daemon using Python API."""

import asyncio
import os
import tempfile
from typing import Optional

import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import Response

try:
    from kittentts import KittenTTS
    KITTENTTS_AVAILABLE = True
except ImportError:
    KITTENTTS_AVAILABLE = False

SUPPORTED_VOICES = [
    "expr-voice-2-m", "expr-voice-2-f",
    "expr-voice-3-m", "expr-voice-3-f",
    "expr-voice-4-m", "expr-voice-4-f",
    "expr-voice-5-m", "expr-voice-5-f",
]
TTS_MODEL = "medium"
TTS_VOICE = os.getenv("TTS_VOICE", "expr-voice-2-m")

app = FastAPI()
_kittentts: Optional[KittenTTS] = None


def get_tts() -> KittenTTS:
    global _kittentts
    if _kittentts is None:
        if not KITTENTTS_AVAILABLE:
            raise HTTPException(503, "KittenTTS not installed")
        _kittentts = KittenTTS()
    return _kittentts


class SpeakRequest(BaseModel):
    text: str
    voice: str = "expr-voice-2-m"
    model: str = "medium"


@app.get("/health")
async def health():
    return {
        "status": "ok" if KITTENTTS_AVAILABLE else "degraded",
        "model": TTS_MODEL,
        "voice": TTS_VOICE,
        "kittentts_available": KITTENTTS_AVAILABLE
    }


@app.get("/voices")
async def voices():
    return SUPPORTED_VOICES


@app.get("/models")
async def models():
    return ["medium"]


@app.post("/speak")
async def speak(req: SpeakRequest):
    if req.voice not in SUPPORTED_VOICES:
        raise HTTPException(400, f"Unsupported voice: {req.voice}")

    tts = get_tts()
    try:
        audio: np.ndarray = tts.generate(req.text, voice=req.voice)
    except Exception as e:
        raise HTTPException(500, f"TTS generation failed: {e}")

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        out_path = f.name

    try:
        import scipy.io.wavfile as wavfile
        wavfile.write(out_path, 24000, audio)
        with open(out_path, "rb") as f:
            audio_data = f.read()
        return Response(content=audio_data, media_type="audio/wav")
    finally:
        if os.path.exists(out_path):
            os.unlink(out_path)


@app.post("/play")
async def play(req: SpeakRequest):
    """Synthesize and play immediately via aplay."""
    if req.voice not in SUPPORTED_VOICES:
        raise HTTPException(400, f"Unsupported voice: {req.voice}")

    tts = get_tts()
    try:
        audio: np.ndarray = tts.generate(req.text, voice=req.voice)
    except Exception as e:
        raise HTTPException(500, f"TTS generation failed: {e}")

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        out_path = f.name

    try:
        import scipy.io.wavfile as wavfile
        wavfile.write(out_path, 24000, audio)
    finally:
        pass

    proc = await asyncio.create_subprocess_exec(
        "aplay", out_path,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    await proc.communicate()

    if os.path.exists(out_path):
        os.unlink(out_path)

    return {"status": "played", "text": req.text[:50]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8743)