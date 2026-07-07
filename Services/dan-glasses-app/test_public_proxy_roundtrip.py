"""End-to-end smoke test for the public-URL path used by the published SPA.

The dan-glasses-app is published at https://dan-glasses-app-som.zocomputer.io
via a CF → frpc tunnel → dan-glasses-app :8747. The React SPA at the public
URL fetches `/api/<svc>/...` which the local server proxies to the daemons.

These tests verify the public URL roundtrip for each daemon proxy. They are
not a substitute for the local-proxy tests (test_wizard_proxy_roundtrip.py)
— they add CF + tunnel coverage on top.

Run: pytest Services/dan-glasses-app/test_public_proxy_roundtrip.py -v
Network: egress to dan-glasses-app-som.zocomputer.io required.
"""

import os
import struct
import httpx
import pytest


PUBLIC = os.environ.get(
    "DAN_GLASSES_PUBLIC_URL",
    "https://dan-glasses-app-som.zocomputer.io",
)


# --- 1. SPA loads --------------------------------------------------------


@pytest.mark.asyncio
async def test_public_index_loads():
    async with httpx.AsyncClient(timeout=10, follow_redirects=True) as c:
        r = await c.get(f"{PUBLIC}/")
        assert r.status_code == 200
        assert "Dan Glasses" in r.text


# --- 2. Aggregator through CF -------------------------------------------


@pytest.mark.asyncio
async def test_public_aggregator_all_healthy():
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.get(f"{PUBLIC}/api/services/health")
        assert r.status_code == 200
        data = r.json()
        assert data["ok"] is True, f"down services: {data}"
        assert data["up_count"] == data["down_count"] + data["up_count"]
        for name, svc in data["services"].items():
            assert svc["ok"] is True, f"{name} not healthy: {svc}"


# --- 3. memoryd proxy through CF ----------------------------------------


@pytest.mark.asyncio
async def test_public_memoryd_write_and_query():
    async with httpx.AsyncClient(timeout=15) as c:
        marker = "DAN-4-public-proxy-smoke"
        r = await c.post(
            f"{PUBLIC}/api/memoryd/memories",
            json={"type": "episodic", "content": marker},
        )
        assert r.status_code == 200
        mem = r.json()
        assert "id" in mem and mem["id"] > 0

        # The /query endpoint is ratey on CF first-call; allow retries.
        hits = []
        for _ in range(3):
            q = await c.get(
                f"{PUBLIC}/api/memoryd/query",
                params={"text": "DAN-4 public proxy smoke", "top_k": 5},
            )
            if q.status_code == 200:
                hits = q.json() if isinstance(q.json(), list) else []
                break
        assert any(marker in h.get("content", "") for h in hits), (
            f"marker not in top-5 query hits: {hits}"
        )


# --- 4. toold proxy through CF ------------------------------------------


@pytest.mark.asyncio
async def test_public_toold_test():
    async with httpx.AsyncClient(timeout=15) as c:
        r = await c.get(f"{PUBLIC}/api/toold/test")
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is True
        for ch_name, ch in data["results"].items():
            assert ch.get("ok") is True, f"toold channel {ch_name} failed: {ch}"


# --- 5. ttsd proxy through CF (binary path) -----------------------------


def _wav_duration_ms(body: bytes) -> int | None:
    """Best-effort parse a PCM WAV header. Returns total ms or None."""
    if not body.startswith(b"RIFF") or body[8:12] != b"WAVE":
        return None
    # Walk chunks looking for fmt + data.
    i = 12
    sample_rate = channels = bits = 0
    data_size = 0
    while i + 8 <= len(body):
        tag = body[i : i + 4]
        size = struct.unpack("<I", body[i + 4 : i + 8])[0]
        if tag == b"fmt ":
            fmt = body[i + 8 : i + 8 + min(size, 16)]
            if len(fmt) >= 16:
                channels = struct.unpack("<H", fmt[2:4])[0]
                sample_rate = struct.unpack("<I", fmt[4:8])[0]
                bits = struct.unpack("<H", fmt[14:16])[0]
        elif tag == b"data":
            data_size = size
            break
        i += 8 + size + (size & 1)
    if not (sample_rate and channels and bits and data_size):
        return None
    bytes_per_sample = (bits // 8) * channels
    samples = data_size / max(bytes_per_sample, 1)
    return int((samples / sample_rate) * 1000)


@pytest.mark.asyncio
async def test_public_ttsd_speak():
    async with httpx.AsyncClient(timeout=30) as c:
        r = await c.post(
            f"{PUBLIC}/api/ttsd/speak",
            json={"text": "DAN-4 public proxy verify.", "voice": "expr-voice-2-m"},
        )
        assert r.status_code == 200, f"ttsd public proxy failed: {r.status_code} {r.text[:200]}"
        assert r.headers.get("content-type", "").startswith("audio/wav")
        body = r.content
        assert body.startswith(b"RIFF") and b"WAVE" in body[:12]
        assert len(body) > 5000, f"wav suspiciously small: {len(body)} bytes"
        dur_ms = _wav_duration_ms(body)
        assert dur_ms is None or 200 < dur_ms < 30000, f"implausible duration: {dur_ms}ms"
