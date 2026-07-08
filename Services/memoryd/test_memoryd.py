"""Tests for memoryd service."""

import asyncio
import os
import sys
import tempfile
import pytest
import httpx

sys.path.insert(0, os.path.dirname(__file__))

MEMORYD_PORT = 8741
BASE_URL = f"http://127.0.0.1:{MEMORYD_PORT}"
TEST_DB = tempfile.mktemp(suffix=".db")


@pytest.fixture(scope="module")
def setup_env():
    os.environ["MEMORYD_DB"] = TEST_DB
    import memoryd
    memoryd.DB_PATH = TEST_DB
    yield


@pytest.fixture
async def client(setup_env):
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        yield c


@pytest.mark.asyncio
async def test_health():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.get("/health")
        assert r.status_code == 200
        data = r.json()
        assert data["status"] == "ok"
        assert "model" in data


@pytest.mark.asyncio
async def test_store_episodic_memory():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/memories", json={
            "type": "episodic",
            "content": "test episodic memory",
            "metadata": {"source": "test"}
        })
        assert r.status_code == 200
        data = r.json()
        assert "id" in data
        assert data["id"] > 0


@pytest.mark.asyncio
async def test_store_semantic_memory():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/memories", json={
            "type": "semantic",
            "content": "test semantic memory",
        })
        assert r.status_code == 200
        data = r.json()
        assert "id" in data


@pytest.mark.asyncio
async def test_store_procedural_memory():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/memories", json={
            "type": "procedural",
            "content": "how to do something",
        })
        assert r.status_code == 200
        data = r.json()
        assert "id" in data


@pytest.mark.asyncio
async def test_store_invalid_type():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/memories", json={
            "type": "invalid",
            "content": "test"
        })
        assert r.status_code == 400


@pytest.mark.asyncio
async def test_store_conversation():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/conversations", json={
            "role": "user",
            "content": "hello world",
            "session_id": "test-session-1"
        })
        assert r.status_code == 200
        data = r.json()
        assert "id" in data


@pytest.mark.asyncio
async def test_query_memory():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/memories", json={
            "type": "semantic",
            "content": "I like pizza and pasta"
        })
        data = r.json()
        mem_id = data["id"]

        r = await c.get("/query", params={"text": "food preferences", "top_k": 5})
        assert r.status_code == 200
        results = r.json()
        assert isinstance(results, list)
        assert len(results) > 0
        assert all("score" in m for m in results)
        assert all("content" in m for m in results)


@pytest.mark.asyncio
async def test_query_with_type_filter():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.get("/query", params={"text": "test", "top_k": 5, "memory_type": "episodic"})
        assert r.status_code == 200
        results = r.json()
        for m in results:
            assert m["type"] == "episodic"


@pytest.mark.asyncio
async def test_list_memories():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.get("/memories", params={"limit": 10})
        assert r.status_code == 200


@pytest.mark.asyncio
async def test_list_memories_by_type():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.get("/memories", params={"type": "semantic", "limit": 5})
        assert r.status_code == 200


@pytest.mark.asyncio
async def test_delete_memory():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/memories", json={
            "type": "episodic",
            "content": "memory to delete"
        })
        data = r.json()
        mem_id = data["id"]

        r = await c.delete(f"/memories/{mem_id}")
        assert r.status_code == 200
        assert r.json()["deleted"] == mem_id


@pytest.mark.asyncio
async def test_list_by_type():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.get("/memories/by-type/episodic", params={"limit": 10})
        assert r.status_code == 200
        items = r.json()
        assert isinstance(items, list)
        for m in items:
            assert m["type"] == "episodic"


@pytest.mark.asyncio
async def test_list_by_type_invalid():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.get("/memories/by-type/bogus", params={"limit": 5})
        assert r.status_code == 400


@pytest.mark.asyncio
async def test_get_memory_by_id():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/memories", json={
            "type": "procedural",
            "content": "first step: open editor",
            "metadata": {"steps": 3}
        })
        mem_id = r.json()["id"]

        r = await c.get(f"/memories/{mem_id}")
        assert r.status_code == 200
        data = r.json()
        assert data["id"] == mem_id
        assert data["type"] == "procedural"
        assert data["content"] == "first step: open editor"


@pytest.mark.asyncio
async def test_get_memory_404():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.get("/memories/99999999")
        assert r.status_code == 404


@pytest.mark.asyncio
async def test_stats():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.get("/stats")
        assert r.status_code == 200
        data = r.json()
        assert "total_memories" in data
        assert "by_type" in data
        assert "episodic" in data["by_type"]
        assert "semantic" in data["by_type"]
        assert "procedural" in data["by_type"]
        assert "conversations" in data
        assert "dim" in data
        assert data["dim"] == 384


@pytest.mark.asyncio
async def test_v1_embeddings():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/v1/embeddings", json={
            "input": ["alpha", "beta", "gamma"],
            "model": "all-MiniLM-L6-v2"
        })
        assert r.status_code == 200
        data = r.json()
        assert data["object"] == "list"
        assert len(data["data"]) == 3
        for i, item in enumerate(data["data"]):
            assert item["object"] == "embedding"
            assert isinstance(item["embedding"], list)
            assert len(item["embedding"]) == 384
            assert item["index"] == i


if __name__ == "__main__":
    pytest.main([__file__, "-v"])