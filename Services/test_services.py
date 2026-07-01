"""Tests for memoryd service."""
import pytest
import httpx
import asyncio


MEMORYD_URL = "http://localhost:8741"
TOOLD_URL = "http://localhost:8742"


@pytest.mark.asyncio
async def test_memoryd_health():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{MEMORYD_URL}/health")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"
        assert "all-MiniLM" in data["model"]


@pytest.mark.asyncio
async def test_memoryd_store_episodic():
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{MEMORYD_URL}/memories",
            json={"type": "episodic", "content": "test episodic memory", "metadata": {}}
        )
        assert resp.status_code == 200
        data = resp.json()
        assert "id" in data


@pytest.mark.asyncio
async def test_memoryd_store_semantic():
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{MEMORYD_URL}/memories",
            json={"type": "semantic", "content": "test semantic fact", "metadata": {}}
        )
        assert resp.status_code == 200
        data = resp.json()
        assert "id" in data


@pytest.mark.asyncio
async def test_memoryd_store_procedural():
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{MEMORYD_URL}/memories",
            json={"type": "procedural", "content": "how to build a sandwich", "metadata": {}}
        )
        assert resp.status_code == 200


@pytest.mark.asyncio
async def test_memoryd_invalid_type():
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{MEMORYD_URL}/memories",
            json={"type": "invalid", "content": "test"}
        )
        assert resp.status_code == 400


@pytest.mark.asyncio
async def test_memoryd_query():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{MEMORYD_URL}/query?text=sandwich&top_k=5")
        assert resp.status_code == 200
        results = resp.json()
        assert isinstance(results, list)


@pytest.mark.asyncio
async def test_memoryd_query_filtered():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{MEMORYD_URL}/query?text=test&top_k=5&memory_type=semantic")
        assert resp.status_code == 200
        results = resp.json()
        for r in results:
            assert r["type"] == "semantic"


@pytest.mark.asyncio
async def test_memoryd_conversation_store():
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{MEMORYD_URL}/conversations",
            json={"role": "user", "content": "hello dan", "session_id": "test-session-1"}
        )
        assert resp.status_code == 200
        data = resp.json()
        assert "id" in data


@pytest.mark.asyncio
async def test_toold_health():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{TOOLD_URL}/health")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"


@pytest.mark.asyncio
async def test_toold_shell_exec():
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{TOOLD_URL}/exec",
            json={"command": "echo hello from toold", "timeout": 5}
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] == True
        assert "hello from toold" in data["stdout"]


@pytest.mark.asyncio
async def test_toold_python_exec():
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{TOOLD_URL}/exec/python",
            json={"code": "print('python works')", "timeout": 5}
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] == True
        assert "python works" in data["stdout"]


@pytest.mark.asyncio
async def test_toold_invalid_chars():
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{TOOLD_URL}/exec",
            json={"command": "echo hello; rm -rf /", "timeout": 5}
        )
        assert resp.status_code == 400


@pytest.mark.asyncio
async def test_toold_registry():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{TOOLD_URL}/registry")
        assert resp.status_code == 200
        data = resp.json()
        assert "tools" in data
        assert len(data["tools"]) >= 3
        names = [t["name"] for t in data["tools"]]
        assert "shell" in names
        assert "python" in names