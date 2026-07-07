"""Live smoke test for the BootstrapWizard's REAL path: through the app server
proxy on :8747, not direct to the daemons.

The React component calls `fetch('/api/memoryd/...')` etc. and the SPA
server (Services/dan-glasses-app/server.py) forwards those to the local
daemons. If the proxy layer is broken (502s, missing CORS, wrong path
rewriting, content-type munging), the wizard breaks in the browser even
though the daemons themselves are healthy.

These tests verify the end-to-end proxy path the wizard actually uses.

Run: pytest test_wizard_proxy_roundtrip.py -v
Requires: daemons up on 8741/8742/8743 AND app server up on 8747.
"""

import httpx
import pytest


APP = "http://localhost:8747"


# --- 1. App server is up -------------------------------------------------


@pytest.mark.asyncio
async def test_app_server_health():
    async with httpx.AsyncClient(timeout=5) as c:
        r = await c.get(f"{APP}/health")
        assert r.status_code == 200


@pytest.mark.asyncio
async def test_app_serves_index_html():
    async with httpx.AsyncClient(timeout=5) as c:
        r = await c.get(f"{APP}/")
        assert r.status_code == 200
        assert "text/html" in r.headers.get("content-type", "")
        body = r.text
        assert "<html" in body.lower()
        assert "vite" in body.lower() or "dan" in body.lower()


# --- 2. /api/<service>/help docs are exposed (proxy is wired) -----------


@pytest.mark.asyncio
@pytest.mark.parametrize("service", ["memoryd", "toold", "ttsd", "audiod", "perceptiond"])
async def test_proxy_help_endpoints(service: str):
    async with httpx.AsyncClient(timeout=5) as c:
        r = await c.get(f"{APP}/api/{service}/help")
        assert r.status_code == 200, f"{service} /help failed: {r.status_code} {r.text[:200]}"
        data = r.json()
        assert "routes" in data, f"{service} /help missing routes: {data}"
        assert isinstance(data["routes"], dict)
        assert len(data["routes"]) >= 3, f"{service} /help too few routes: {data['routes']}"


# --- 3. memoryd roundtrip through the proxy ------------------------------


@pytest.mark.asyncio
async def test_memoryd_health_through_proxy():
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.get(f"{APP}/api/memoryd/health")
        assert r.status_code == 200
        data = r.json()
        assert data["status"] == "ok"
        assert data.get("db_persistent") is True


@pytest.mark.asyncio
async def test_memoryd_store_and_query_through_proxy():
    marker = f"proxy-roundtrip-{__import__('time').time()}"
    async with httpx.AsyncClient(timeout=15) as c:
        # Store
        r = await c.post(
            f"{APP}/api/memoryd/memories",
            json={"type": "semantic", "content": marker, "metadata": {"via": "proxy"}},
        )
        assert r.status_code == 200, f"store failed: {r.status_code} {r.text[:200]}"
        mid = r.json()["id"]

        # Query
        r = await c.get(f"{APP}/api/memoryd/query", params={"text": marker, "top_k": 3})
        assert r.status_code == 200
        hits = r.json()
        assert isinstance(hits, list) and len(hits) >= 1
        # The exact marker should be the top hit
        assert marker in hits[0]["content"], f"top hit mismatch: {hits[0]}"
        assert hits[0]["id"] == mid

        # Cleanup
        await c.delete(f"{APP}/api/memoryd/memories/{mid}")


@pytest.mark.asyncio
async def test_memoryd_stats_through_proxy():
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.get(f"{APP}/api/memoryd/stats")
        assert r.status_code == 200
        data = r.json()
        assert data["total_memories"] >= 0
        assert "by_type" in data
        assert data.get("model_loaded") is True


# --- 4. toold roundtrip through the proxy --------------------------------


@pytest.mark.asyncio
async def test_toold_health_through_proxy():
    async with httpx.AsyncClient(timeout=5) as c:
        r = await c.get(f"{APP}/api/toold/health")
        assert r.status_code == 200
        data = r.json()
        assert data["status"] == "ok"


@pytest.mark.asyncio
async def test_toold_self_test_through_proxy():
    async with httpx.AsyncClient(timeout=15) as c:
        r = await c.get(f"{APP}/api/toold/test")
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is True
        results = data["results"]
        assert results["shell"]["ok"] is True
        assert results["python"]["ok"] is True
        assert results["registry"]["ok"] is True
        assert results["file"]["ok"] is True
        assert data["duration_ms"] < 5000


@pytest.mark.asyncio
async def test_toold_exec_through_proxy():
    async with httpx.AsyncClient(timeout=15) as c:
        r = await c.post(
            f"{APP}/api/toold/exec",
            json={"command": "echo proxy-ok", "timeout": 10},
        )
        assert r.status_code == 200, f"exec failed: {r.status_code} {r.text[:200]}"
        data = r.json()
        assert data["success"] is True
        assert "proxy-ok" in data["stdout"]


# --- 5. ttsd roundtrip through the proxy ---------------------------------


@pytest.mark.asyncio
async def test_ttsd_health_through_proxy():
    async with httpx.AsyncClient(timeout=15) as c:
        r = await c.get(f"{APP}/api/ttsd/health")
        assert r.status_code == 200
        data = r.json()
        assert data["status"] in ("ok", "degraded")


@pytest.mark.asyncio
async def test_ttsd_voices_through_proxy():
    async with httpx.AsyncClient(timeout=10) as c:
        r = await c.get(f"{APP}/api/ttsd/voices")
        assert r.status_code == 200
        voices = r.json()
        assert isinstance(voices, list) and len(voices) >= 2
        # All KittenTTS voice ids
        assert all(v.startswith("expr-voice-") for v in voices)


@pytest.mark.asyncio
async def test_ttsd_speak_through_proxy():
    async with httpx.AsyncClient(timeout=30) as c:
        r = await c.post(
            f"{APP}/api/ttsd/speak",
            json={"text": "Proxy chain test", "voice": "expr-voice-2-m"},
        )
        assert r.status_code == 200, f"speak failed: {r.status_code} {r.text[:200]}"
        ctype = r.headers.get("content-type", "")
        assert "audio" in ctype, f"bad content-type: {ctype}"
        # RIFF WAV header
        assert r.content[:4] == b"RIFF", f"not a WAV: {r.content[:8]!r}"
        assert r.content[8:12] == b"WAVE", f"not a WAV: {r.content[8:16]!r}"
        assert len(r.content) > 1000, f"WAV too small: {len(r.content)} bytes"


# --- 6. CORS is open (browser requirement) -------------------------------


@pytest.mark.asyncio
async def test_proxy_cors_headers():
    async with httpx.AsyncClient(timeout=5) as c:
        r = await c.get(f"{APP}/api/memoryd/health")
        assert r.headers.get("access-control-allow-origin") == "*"
        r = await c.get(f"{APP}/api/toold/health")
        assert r.headers.get("access-control-allow-origin") == "*"
        r = await c.get(f"{APP}/api/ttsd/health")
        assert r.headers.get("access-control-allow-origin") == "*"


# --- 7. Wizard React bundle is built and served --------------------------


@pytest.mark.asyncio
async def test_wizard_bundle_served():
    async with httpx.AsyncClient(timeout=5) as c:
        r = await c.get(f"{APP}/")
        assert r.status_code == 200
        # Vite injects the JS bundle via a script tag
        assert "/assets/" in r.text or "src=" in r.text
