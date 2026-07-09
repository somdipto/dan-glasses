# toold — Tool Execution Service (v113)

## Purpose
Executes shell commands and Python scripts under an allowlist sanitizer, with structured results, a persistent tool registry, and a self-test endpoint used by the bootstrap wizard.

## Architecture
```
request → validate_shell_command (allowlist) → asyncio.create_subprocess_exec → structured JSON response
python/file routes bypass shell validation
```

## Security Model
- **Block:** `;`, single `|`, `` ` ``, `$(`, `>`, `<`, `\n`, `\r`
- **Allow:** `&&`, `||` (chained commands), spaces, all other chars
- Python `/exec/python` and `/exec/file` routes are not shell-string-validated (the Python interpreter is the boundary; the file route's argv is fixed by the dispatcher)
- Workdir: `/tmp/toold-sandbox` (override via `TOOLD_WORKDIR`)
- Max timeout: 120s (configurable via `MAX_TIMEOUT`)

## Tool Registry
- Default path: `/home/workspace/.cache/dan-glasses/toold/registry.json` (atomic `tmp + replace` writes)
- Fallback path: `/tmp/toold_registry.json` (when persistent dir is unwritable)
- Resolved on first call to `_resolve_registry_path()`
- Seeded on startup via `_seed_registry` event

### Default tools
```json
{
  "tools": [
    {"name": "shell", "description": "run shell commands", "enabled": true},
    {"name": "python", "description": "run inline python", "enabled": true},
    {"name": "exec_file", "description": "execute saved script files", "enabled": true}
  ]
}
```

Custom tools can be registered with `POST /registry/tools`:
```json
{"name": "git_status", "description": "git status", "kind": "shell", "command_template": "git status --short", "enabled": true}
```

## API Endpoints

### `GET /health`
Liveness.
```json
{"status":"ok","workdir":"/tmp/toold-sandbox","max_timeout":120,"registry_path":"/home/workspace/.cache/dan-glasses/toold/registry.json","version":"0.2.0"}
```

### `GET /ready`
Readiness — checks registry is loadable and non-empty.
```json
{"ready":true,"tool_count":3}
```

### `GET /version`
Service version + uptime.
```json
{"version":"0.2.0","registry_path":"…","workdir":"…","uptime_seconds":1234.56}
```

### `GET /test`
Self-test exercising shell + python + file + registry end-to-end. Used by BootstrapWizard.
```json
{
  "success": true,
  "results": {
    "shell":    {"ok": true, "stdout": "tool-ready"},
    "python":   {"ok": true, "stdout": "py-ready"},
    "registry": {"ok": true, "tool_count": 4},
    "file":     {"ok": true, "stdout": "file-ready"}
  },
  "duration_ms": 23
}
```

### `POST /exec`
Run a shell command. Body: `{command, timeout?}`. Validates with `validate_shell_command`. 400 on disallowed chars.
Response:
```json
{"success":true,"stdout":"…","stderr":"","exit_code":0,"duration_ms":45}
```
On timeout: `success=false`, `stderr="Timed out after Ns"`, `exit_code=-1`.

### `POST /exec/python`
Run inline Python via `python3 -c <code>`. Body: `{code, timeout?}`.

### `POST /exec/file`
Run a saved script. Body: `{filepath, args?}`.
- `.py` → `python3 <file> <args>`
- `.sh` → `bash <file> <args>`
- other → direct `<file> <args>`
- 404 if file missing

### `GET /registry`
Return full registry JSON.

### `POST /registry/tools`
Register a new tool. Body: `{name, description, kind, command_template?, enabled?}`.
- 409 on duplicate name.

### `POST /registry/{name}/enable` / `POST /registry/{name}/disable`
Toggle a tool. 404 if name unknown.

### `POST /exec/with-tool`
Execute a registered tool by name. Body: `{name, args?, timeout?}`.
- 404 if tool not in registry
- 403 if tool is disabled
- 400 if tool has no `command_template` or template fails the shell sanitizer

## Response Format (all exec endpoints)
```json
{
  "success": true,
  "stdout": "…",
  "stderr": "",
  "exit_code": 0,
  "duration_ms": 45
}
```

## Port
- `8742` (override via `TOOLD_PORT`)

## Dependencies
- `fastapi`
- `uvicorn`
- `pydantic`
- Python 3 stdlib: `asyncio`, `subprocess`, `os`, `re`, `json`, `time`, `pathlib`

## Tests (21) — `test_toold.py`
- health, exec shell success/failure, blocked chars (semicolon, pipe, redirect, backtick, `$()`, newline)
- exec python success, math, failure, timeout
- exec file 404
- registry: get, enable, disable, none-existent
- duration_ms reported
- register tool (idempotent across re-runs)
- exec-with-tool success, disabled-rejected
- chained `&&` allowed, chained `||` allowed, full injection vector list still rejected

## Failure Modes
- **Disallowed shell char** → 400 with "Command contains disallowed characters"
- **Tool disabled** → 403
- **Timeout** → subprocess killed, structured `{success: false, stderr: "Timed out after Ns", exit_code: -1}`
- **Registry dir unwritable** → falls back to `/tmp/toold_registry.json` and logs a warning; service still starts

## Integration
- BootstrapWizard calls `/test` for one-shot "Tools" step
- dan-glasses-app's `/api/services/test` aggregates with the rest
- Custom tools registered here become invokable by `/exec/with-tool` from any service that proxies to `:8742`
