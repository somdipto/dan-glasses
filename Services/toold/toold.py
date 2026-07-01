"""toold — Tool Execution Service with shell + python execution (v109)."""

import asyncio
import json
import logging
import os
import time
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO, format="[toold] %(message)s")
log = logging.getLogger("toold")

DEFAULT_PERSISTENT_DIR = Path("/home/workspace/.cache/dan-glasses/toold")
PERSISTENT_REGISTRY = DEFAULT_PERSISTENT_DIR / "registry.json"
FALLBACK_REGISTRY = Path("/tmp/toold_registry.json")

WORKDIR = Path(os.getenv("TOOLD_WORKDIR", "/tmp/toold-sandbox"))
WORKDIR.mkdir(parents=True, exist_ok=True)
MAX_TIMEOUT = 120

VERSION = "0.2.0"
_start_ts = time.time()


def _resolve_registry_path() -> Path:
    """Pick the persistent path if writable, else fall back to /tmp."""
    try:
        DEFAULT_PERSISTENT_DIR.mkdir(parents=True, exist_ok=True)
        # Probe writability with a touch + unlink.
        probe = DEFAULT_PERSISTENT_DIR / ".writeprobe"
        probe.write_text("ok")
        probe.unlink()
        return PERSISTENT_REGISTRY
    except OSError as e:
        log.warning("persistent registry dir unwritable (%s) — falling back to /tmp", e)
        return FALLBACK_REGISTRY


REGISTRY_PATH = _resolve_registry_path()
log.info("registry path: %s", REGISTRY_PATH)


app = FastAPI()


def load_registry() -> dict:
    if REGISTRY_PATH.exists():
        try:
            with REGISTRY_PATH.open() as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            log.warning("registry load failed (%s) — reseeding defaults", e)
    reg = {
        "tools": [
            {"name": "shell", "description": "run shell commands", "enabled": True},
            {"name": "python", "description": "run inline python", "enabled": True},
            {"name": "exec_file", "description": "execute saved script files", "enabled": True},
        ]
    }
    save_registry(reg)
    return reg


def save_registry(reg: dict) -> None:
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = REGISTRY_PATH.with_suffix(".tmp")
    with tmp.open("w") as f:
        json.dump(reg, f, indent=2)
    tmp.replace(REGISTRY_PATH)  # atomic on POSIX


def validate_shell_command(cmd: str) -> bool:
    blocked = [";", "&", "|", "`", "$(", ">", "<", "\n", "\r", "&&", "||"]
    return all(p not in cmd for p in blocked)


class ShellExec(BaseModel):
    command: str
    timeout: int = 30


class PythonExec(BaseModel):
    code: str
    timeout: int = 30


class ExecFile(BaseModel):
    filepath: str
    args: list[str] = []


class ToolInput(BaseModel):
    name: str
    description: str
    enabled: bool = True
    kind: str = "shell"
    command_template: Optional[str] = None


class ToolWithExec(BaseModel):
    name: str
    args: list[str] = []
    timeout: int = 30


@app.on_event("startup")
async def _seed_registry():
    """Make sure the registry file exists on first boot."""
    load_registry()


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "workdir": str(WORKDIR),
        "max_timeout": MAX_TIMEOUT,
        "registry_path": str(REGISTRY_PATH),
        "version": VERSION,
    }


@app.get("/ready")
async def ready():
    try:
        reg = load_registry()
        ok = "tools" in reg and isinstance(reg["tools"], list)
        return {"ready": ok, "tool_count": len(reg.get("tools", []))}
    except Exception as e:
        return {"ready": False, "error": str(e)}


@app.get("/version")
async def version():
    return {
        "version": VERSION,
        "registry_path": str(REGISTRY_PATH),
        "workdir": str(WORKDIR),
        "uptime_seconds": round(time.time() - _start_ts, 2),
    }


@app.get("/test")
async def test():
    """Self-test: exercise shell + python + file + registry end-to-end."""
    results = {}
    start = time.time()

    try:
        proc = await asyncio.create_subprocess_shell(
            "echo tool-ready",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=str(WORKDIR),
        )
        so, se = await asyncio.wait_for(proc.communicate(), timeout=10)
        results["shell"] = {
            "ok": proc.returncode == 0 and so.decode().strip() == "tool-ready",
            "stdout": so.decode().strip(),
        }
    except Exception as e:
        results["shell"] = {"ok": False, "error": str(e)}

    try:
        proc = await asyncio.create_subprocess_exec(
            "python3", "-c", "print('py-ready')",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=str(WORKDIR),
        )
        so, se = await asyncio.wait_for(proc.communicate(), timeout=10)
        results["python"] = {
            "ok": proc.returncode == 0 and so.decode().strip() == "py-ready",
            "stdout": so.decode().strip(),
        }
    except Exception as e:
        results["python"] = {"ok": False, "error": str(e)}

    try:
        reg = load_registry()
        results["registry"] = {
            "ok": len(reg.get("tools", [])) > 0,
            "tool_count": len(reg.get("tools", [])),
        }
    except Exception as e:
        results["registry"] = {"ok": False, "error": str(e)}

    tmp_path = WORKDIR / ".toold_selftest.sh"
    try:
        tmp_path.write_text("#!/bin/bash\necho file-ready\n")
        tmp_path.chmod(0o755)
        proc = await asyncio.create_subprocess_exec(
            "bash", str(tmp_path),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=str(WORKDIR),
        )
        so, se = await asyncio.wait_for(proc.communicate(), timeout=10)
        results["file"] = {
            "ok": proc.returncode == 0 and so.decode().strip() == "file-ready",
            "stdout": so.decode().strip(),
        }
    except Exception as e:
        results["file"] = {"ok": False, "error": str(e)}
    finally:
        try:
            tmp_path.unlink()
        except OSError:
            pass

    all_ok = all(v.get("ok") for v in results.values())
    return {
        "success": all_ok,
        "results": results,
        "duration_ms": int((time.time() - start) * 1000),
    }


async def _run_subprocess(cmd, timeout: int, cwd: str) -> dict:
    """Shared subprocess runner with structured result format."""
    start = time.time()
    try:
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=cwd,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        return {
            "success": proc.returncode == 0,
            "stdout": stdout.decode(),
            "stderr": stderr.decode(),
            "exit_code": proc.returncode,
            "duration_ms": int((time.time() - start) * 1000),
        }
    except asyncio.TimeoutError:
        try:
            proc.kill()
        except ProcessLookupError:
            pass
        return {
            "success": False,
            "stdout": "",
            "stderr": f"Timed out after {timeout}s",
            "exit_code": -1,
            "duration_ms": int((time.time() - start) * 1000),
        }


@app.post("/exec")
async def exec_shell(req: ShellExec):
    if not validate_shell_command(req.command):
        raise HTTPException(400, "Command contains disallowed characters")
    timeout = min(req.timeout, MAX_TIMEOUT)
    return await _run_subprocess(
        ["bash", "-c", req.command], timeout, str(WORKDIR),
    )


@app.post("/exec/python")
async def exec_python(req: PythonExec):
    timeout = min(req.timeout, MAX_TIMEOUT)
    return await _run_subprocess(
        ["python3", "-c", req.code], timeout, str(WORKDIR),
    )


@app.post("/exec/file")
async def exec_file(req: ExecFile):
    if not os.path.exists(req.filepath):
        raise HTTPException(404, f"File not found: {req.filepath}")
    ext = os.path.splitext(req.filepath)[1]
    if ext == ".py":
        cmd = ["python3", req.filepath] + req.args
    elif ext == ".sh":
        cmd = ["bash", req.filepath] + req.args
    else:
        cmd = [req.filepath] + req.args
    return await _run_subprocess(cmd, MAX_TIMEOUT, str(WORKDIR))


@app.get("/registry")
async def get_registry():
    return load_registry()


@app.post("/registry/{name}/enable")
async def enable_tool(name: str):
    reg = load_registry()
    for tool in reg["tools"]:
        if tool["name"] == name:
            tool["enabled"] = True
            save_registry(reg)
            return {"updated": name, "enabled": True}
    raise HTTPException(404, f"Tool not found: {name}")


@app.post("/registry/{name}/disable")
async def disable_tool(name: str):
    reg = load_registry()
    for tool in reg["tools"]:
        if tool["name"] == name:
            tool["enabled"] = False
            save_registry(reg)
            return {"updated": name, "enabled": False}
    raise HTTPException(404, f"Tool not found: {name}")


@app.post("/registry/tools")
async def register_tool(tool: ToolInput):
    reg = load_registry()
    for existing in reg["tools"]:
        if existing["name"] == tool.name:
            raise HTTPException(409, f"Tool already exists: {tool.name}")
    reg["tools"].append(tool.model_dump())
    save_registry(reg)
    return {"registered": tool.name}


@app.post("/exec/with-tool")
async def exec_with_tool(req: ToolWithExec):
    reg = load_registry()
    tool = next((t for t in reg["tools"] if t["name"] == req.name), None)
    if tool is None:
        raise HTTPException(404, f"Tool not found: {req.name}")
    if not tool.get("enabled", False):
        raise HTTPException(403, f"Tool disabled: {req.name}")
    template = tool.get("command_template")
    if not template:
        raise HTTPException(400, f"Tool has no command_template: {req.name}")
    if not validate_shell_command(template):
        raise HTTPException(400, "Tool template contains disallowed characters")
    timeout = min(req.timeout, MAX_TIMEOUT)
    return await _run_subprocess(["bash", "-c", template], timeout, str(WORKDIR))


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("TOOLD_PORT", "8742"))
    uvicorn.run(app, host="0.0.0.0", port=port)