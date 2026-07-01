"""KittenTTS integration for Dan Glasses.

Text → TTS → audio playback via KittenTTS subprocess.
"""

import asyncio
import os
import subprocess
import tempfile

TTS_MODEL = os.getenv("TTS_MODEL", "medium")
TTS_VOICE = os.getenv("TTS_VOICE", "expr-voice-2-m")
KITTEN_CLI = os.getenv("KITTEN_CLI", "/root/.local/bin/kittentts")

SUPPORTED_VOICES = [
    "expr-voice-2-m", "expr-voice-2-f",
    "expr-voice-3-m", "expr-voice-3-f",
    "expr-voice-4-m", "expr-voice-4-f",
    "expr-voice-5-m", "expr-voice-5-f",
]


def synthesize(text: str, output_path: str, voice: str = "expr-voice-2-m") -> bool:
    """Synchronous TTS synthesis via Kitt en CLI."""
    try:
        cmd = [
            KITTEN_CLI,
            "--text", text,
            "--output", output_path,
            "--voice", voice,
        ]
        result = subprocess.run(cmd, capture_output=True, timeout=60)
        return result.returncode == 0
    except Exception:
        return False


async def synthesize_async(text: str, voice: str = "expr-voice-2-m") -> str:
    """Async TTS: returns path to generated audio file."""
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        out_path = f.name

    loop = asyncio.get_event_loop()
    success = await loop.run_in_executor(None, synthesize, text, out_path, voice)
    if not success:
        os.unlink(out_path)
        raise RuntimeError(f"TTS synthesis failed for: {text[:50]}...")
    return out_path


async def speak(text: str, voice: str = "expr-voice-2-m") -> bool:
    """Synthesize and play audio."""
    audio_path = await synthesize_async(text, voice)
    try:
        proc = await asyncio.create_subprocess_exec(
            "aplay", audio_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        await proc.communicate()
        return True
    finally:
        os.unlink(audio_path)


class TTSClient:
    def __init__(self, base_url: str = "http://localhost:8743"):
        self.base_url = base_url

    async def speak(self, text: str, voice: str = "expr-voice-2-m") -> dict:
        """POST /speak — synthesize and stream audio."""
        import aiohttp
        async with aiohttp.ClientSession() as sess:
            async with sess.post(
                f"{self.base_url}/speak",
                json={"text": text, "voice": voice},
                timeout=aiohttp.ClientTimeout(total=30)
            ) as resp:
                return await resp.json()

    async def voices(self) -> list:
        import aiohttp
        async with aiohttp.ClientSession() as sess:
            async with sess.get(f"{self.base_url}/voices") as resp:
                return await resp.json()

    async def health(self) -> dict:
        import aiohttp
        async with aiohttp.ClientSession() as sess:
            async with sess.get(f"{self.base_url}/health") as resp:
                return await resp.json()
