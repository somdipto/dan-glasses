"""Tests for toold service."""

import asyncio
import os
import sys
import pytest
import httpx

sys.path.insert(0, os.path.dirname(__file__))

TOOLD_PORT = 8742
BASE_URL = f"http://localhost:{TOOLD_PORT}"


@pytest.mark.asyncio
async def test_health():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.get("/health")
        assert r.status_code == 200
        data = r.json()
        assert data["status"] == "ok"
        assert "workdir" in data
        assert "max_timeout" in data


@pytest.mark.asyncio
async def test_exec_shell_success():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/exec", json={
            "command": "echo hello",
            "timeout": 10
        })
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is True
        assert "hello" in data["stdout"]
        assert data["exit_code"] == 0


@pytest.mark.asyncio
async def test_exec_shell_with_args():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/exec", json={
            "command": "pwd",
            "timeout": 10
        })
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is True
        assert data["exit_code"] == 0


@pytest.mark.asyncio
async def test_exec_shell_failure():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/exec", json={
            "command": "exit 1",
            "timeout": 10
        })
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is False
        assert data["exit_code"] == 1


@pytest.mark.asyncio
async def test_exec_shell_blocked_chars():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/exec", json={
            "command": "echo hello; rm -rf /",
            "timeout": 10
        })
        assert r.status_code == 400


@pytest.mark.asyncio
async def test_exec_python_success():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/exec/python", json={
            "code": "print('hello from python')",
            "timeout": 10
        })
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is True
        assert "hello from python" in data["stdout"]


@pytest.mark.asyncio
async def test_exec_python_math():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/exec/python", json={
            "code": "print(42 * 2)",
            "timeout": 10
        })
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is True
        assert "84" in data["stdout"]


@pytest.mark.asyncio
async def test_exec_python_failure():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/exec/python", json={
            "code": "raise Exception('test error')",
            "timeout": 10
        })
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is False
        assert "Traceback" in data["stderr"]


@pytest.mark.asyncio
async def test_exec_python_timeout():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/exec/python", json={
            "code": "import time; time.sleep(10)",
            "timeout": 2
        })
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is False
        assert "Timed out" in data["stderr"]


@pytest.mark.asyncio
async def test_get_registry():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.get("/registry")
        assert r.status_code == 200
        data = r.json()
        assert "tools" in data
        assert len(data["tools"]) > 0


@pytest.mark.asyncio
async def test_registry_disable_tool():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/registry/shell/disable")
        assert r.status_code == 200
        data = r.json()
        assert data["enabled"] is False


@pytest.mark.asyncio
async def test_registry_enable_tool():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/registry/shell/enable")
        assert r.status_code == 200
        data = r.json()
        assert data["enabled"] is True


@pytest.mark.asyncio
async def test_registry_nonexistent_tool():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/registry/nonexistent/enable")
        assert r.status_code == 404


@pytest.mark.asyncio
async def test_exec_file_not_found():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/exec/file", json={
            "filepath": "/nonexistent/file.py"
        })
        assert r.status_code == 404


@pytest.mark.asyncio
async def test_duration_reported():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        r = await c.post("/exec", json={
            "command": "echo test",
            "timeout": 10
        })
        data = r.json()
        assert "duration_ms" in data
        assert data["duration_ms"] >= 0


@pytest.mark.asyncio
async def test_register_tool():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        # Idempotent across re-runs: if the tool already exists from a prior
        # test run, treat that as the success case rather than failing.
        r = await c.post("/registry/tools", json={
            "name": "test_register_echo",
            "description": "test echo",
            "enabled": True,
            "kind": "shell",
            "command_template": "echo registered"
        })
        if r.status_code == 409:
            reg = (await c.get("/registry")).json()
            assert any(t["name"] == "test_register_echo" for t in reg.get("tools", []))
            return
        assert r.status_code == 200
        assert r.json()["registered"] == "test_register_echo"


@pytest.mark.asyncio
async def test_exec_with_tool_success():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        # ensure enabled
        await c.post("/registry/test_register_echo/enable")
        r = await c.post("/exec/with-tool", json={
            "name": "test_register_echo",
            "args": [],
            "timeout": 10
        })
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is True
        assert "registered" in data["stdout"]


@pytest.mark.asyncio
async def test_exec_with_tool_disabled_rejected():
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as c:
        await c.post("/registry/test_register_echo/disable")
        r = await c.post("/exec/with-tool", json={
            "name": "test_register_echo",
            "args": [],
            "timeout": 10
        })
        assert r.status_code == 403
        await c.post("/registry/test_register_echo/enable")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])