"""Live smoke test for the BootstrapWizard's exact HTTP sequence.

Runs the same calls the React component makes against memoryd + toold + ttsd.
If these tests pass and `npm run build` passes, the wizard should work in the
browser.

Real pytest module — collected by `pytest test_wizard_roundtrip.py -v`.
"""

import pytest
import httpx


MEMORYD = "http://127.0.0.1:8741"
TOOLD = "http://127.0.0.1:8742"
TTSD = "http://127.0.0.1:8743"


# --- 1. Health checks for the three services the wizard exercises ---------


@pytest.mark.asyncio
async def test_memoryd_health():
    async with httpx.AsyncClient(timeout=5) as c:
        r = await c.get(f"{MEMORYD}/health")
        assert r.status_code == 200
        data = r.json()
        assert data["status"] == "ok"
        assert "model" in data
        assert data.get("db_persistent") is True


@pytest.mark.asyncio
async def test_toold_health():
    async with httpx.AsyncClient(timeout=5) as c:
        r = await c.get(f"{TOOLD}/health")
        assert r.status_code == 200
        data = r.json()
        assert data["status"] == "ok"
        assert "workdir" in data
        assert "max_timeout" in data


@pytest.mark.asyncio
async def test_ttsd_health():
    async with httpx.AsyncClient(timeout=15) as c:
        r = await c.get(f"{TTSD}/health")
        assert r.status_code == 200
        data = r.json()
        assert data["status"] in ("ok", "degraded")
        assert data.get("kittentts_available") is True


# --- 2. memoryd roundtrip (the wizard's exact 4-type store + query) -------


@pytest.mark.asyncio
async def test_wizard_memory_roundtrip_stores_all_three_types():
    """Wizard stores 1 episodic + 2 semantic + 1 procedural memory."""
    types_and_content = [
        ("episodic", "wizard pytest bootstrap run"),
        ("semantic", "User display name: pytest-wizard"),
        ("semantic", "Preferred TTS voice: expr-voice-2-f"),
        (
            "procedural",
            "To run a Dan Glasses bootstrap: check services, prompt for name+voice, exercise memoryd + toold + ttsd.",
        ),
    ]
    async with httpx.AsyncClient(timeout=30) as c:
        for mem_type, content in types_and_content:
            r = await c.post(
                f"{MEMORYD}/memories",
                json={"type": mem_type, "content": content},
            )
            assert r.status_code == 200, f"{mem_type} store failed: {r.text}"
            data = r.json()
            assert "id" in data
            assert data["id"] > 0


@pytest.mark.asyncio
async def test_wizard_memory_query_returns_hits():
    """After storing wizard memories, /query must return ≥1 hit."""
    async with httpx.AsyncClient(timeout=30) as c:
        # seed one more so this test is independent of store order
        await c.post(
            f"{MEMORYD}/memories",
            json={
                "type": "procedural",
                "content": "Wizard query seed: bootstrap+setup keywords.",
            },
        )
        r = await c.get(f"{MEMORYD}/query", params={"text": "bootstrap setup", "top_k": 5})
        assert r.status_code == 200
        results = r.json()
        assert isinstance(results, list)
        assert len(results) > 0
        for hit in results:
            assert "score" in hit
            assert "content" in hit
            assert "type" in hit
            assert 0.0 <= hit["score"] <= 1.0


# --- 3. toold /test (wizard uses this verbatim) ----------------------------


@pytest.mark.asyncio
async def test_wizard_toold_test_passes():
    async with httpx.AsyncClient(timeout=15) as c:
        r = await c.get(f"{TOOLD}/test")
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is True
        for channel in ("shell", "python", "registry", "file"):
            assert channel in data["results"], f"missing channel: {channel}"
            assert data["results"][channel]["ok"] is True, f"{channel} failed"
        assert data["duration_ms"] >= 0


# --- 4. ttsd /speak — the wizard's TTS sample step -------------------------


@pytest.mark.asyncio
async def test_wizard_tts_speak_returns_wav():
    """Wizard's `speakText` calls /speak with a sentence and voice. Must
    return audio/wav ≥ a few KB. Cold-loads KittenTTS (~20s first time)."""
    async with httpx.AsyncClient(timeout=60) as c:
        r = await c.post(
            f"{TTSD}/speak",
            json={"text": "DAN-4 wizard pytest live smoke", "voice": "expr-voice-2-m"},
        )
        assert r.status_code == 200
        assert r.headers.get("content-type") == "audio/wav"
        # WAV magic
        assert r.content[:4] == b"RIFF"
        assert r.content[8:12] == b"WAVE"
        # A few seconds of 24kHz mono is hundreds of KB; <1KB is suspicious
        assert len(r.content) > 1000, f"tts WAV too small: {len(r.content)} bytes"


@pytest.mark.asyncio
async def test_wizard_tts_voices_listed():
    """Wizard populates voice dropdown from /voices."""
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.get(f"{TTSD}/voices")
        assert r.status_code == 200
        voices = r.json()
        assert isinstance(voices, list)
        assert "expr-voice-2-m" in voices
        assert "expr-voice-2-f" in voices


# --- 5. /v1/embeddings — used by OpenClaw memory-core ----------------------


@pytest.mark.asyncio
async def test_v1_embeddings_openai_compat():
    async with httpx.AsyncClient(timeout=15) as c:
        r = await c.post(
            f"{MEMORYD}/v1/embeddings",
            json={"input": ["hello world", "goodbye world"], "model": "all-MiniLM-L6-v2"},
        )
        assert r.status_code == 200
        data = r.json()
        assert data["object"] == "list"
        assert len(data["data"]) == 2
        for i, item in enumerate(data["data"]):
            assert item["object"] == "embedding"
            assert isinstance(item["embedding"], list)
            assert len(item["embedding"]) == 384
            assert item["index"] == i


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


# --- 6. Regression: the wizard must not use http://localhost:PORT ----------
#
# Why: the service supervisors bind 0.0.0.0 (IPv4 only). A browser that
# resolves `localhost` to `::1` first will hit ECONNREFUSED, even though
# `127.0.0.1` works. Catching this in code review is fine; catching it
# when the user opens the wizard is not.

import os
import re

WIZARD_SRC = "/home/workspace/dan-glasses/apps/dan-glasses-app/src/components"

_LOCALHOST_URL = re.compile(r"http://localhost:\d+")


@pytest.mark.parametrize(
    "component",
    ["BootstrapWizard.tsx", "MemoryPanel.tsx", "VisionDashboard.tsx", "TtsPanel.tsx", "LiveTranscript.tsx"],
)
def test_no_localhost_urls_in_component(component):
    """No live http://localhost:PORT URL in a component file."""
    path = os.path.join(WIZARD_SRC, component)
    if not os.path.exists(path):
        pytest.skip(f"{component} not found")
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            stripped = line.lstrip()
            if stripped.startswith("//") or stripped.startswith("*"):
                continue
            assert not _LOCALHOST_URL.search(line), (
                f"{component}:{lineno} uses {line.strip()!r}. "
                "Service supervisors bind 0.0.0.0 only — use 127.0.0.1."
            )


# --- 7. Live IPv6 probe ----------------------------------------------------
# Sanity-check: ensure we are not silently shipping a service that
# responds to `localhost` over IPv6 (which would mask the bug above).


@pytest.mark.asyncio
async def test_localhost_ipv6_must_be_refused():
    """If this fails, the supervisors started binding ::1 too and the
    localhost→127.0.0.1 contract is broken — relax the regression test."""
    import socket

    for port in (8741, 8742, 8743):
        try:
            with socket.create_connection(("::1", port), timeout=1):
                pytest.fail(
                    f"port {port} accepted an IPv6 connection; "
                    "the localhost→127.0.0.1 contract is broken — review "
                    "test_no_localhost_urls_in_component."
                )
        except OSError:
            pass  # expected: ::1:PORT refused
