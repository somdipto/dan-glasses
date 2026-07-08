"""Tests for ttsd service."""

import pytest
import httpx


TTSD_URL = "http://127.0.0.1:8743"


@pytest.mark.asyncio
async def test_ttsd_health():
    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.get(f"{TTSD_URL}/health")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] in ("ok", "degraded")
        assert "model" in data
        assert "voice" in data


@pytest.mark.asyncio
async def test_ttsd_voices():
    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.get(f"{TTSD_URL}/voices")
        assert resp.status_code == 200
        voices = resp.json()
        assert isinstance(voices, list)
        assert len(voices) >= 1
        assert all(isinstance(v, str) for v in voices)


@pytest.mark.asyncio
async def test_ttsd_models():
    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.get(f"{TTSD_URL}/models")
        assert resp.status_code == 200
        models = resp.json()
        assert isinstance(models, list)
        assert "medium" in models


@pytest.mark.asyncio
async def test_ttsd_speak_returns_wav():
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(
            f"{TTSD_URL}/speak",
            json={"text": "test synthesis", "voice": "expr-voice-2-m"},
        )
        assert resp.status_code == 200
        assert resp.headers["content-type"] == "audio/wav"
        # WAV header magic: RIFF....WAVE
        assert resp.content[:4] == b"RIFF"
        assert resp.content[8:12] == b"WAVE"


@pytest.mark.asyncio
async def test_ttsd_speak_invalid_voice():
    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.post(
            f"{TTSD_URL}/speak",
            json={"text": "test", "voice": "nonexistent-voice"},
        )
        assert resp.status_code == 400


@pytest.mark.asyncio
async def test_ttsd_play_runs():
    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(
            f"{TTSD_URL}/play",
            json={"text": "test playback", "voice": "expr-voice-2-m"},
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "played"
