# toold — Tool Execution Service

## Purpose
Execute shell commands and Python scripts with safety guardrails and structured JSON results. Tool registry for enable/disable.

## Architecture
```
request → validate → execute (asyncio subprocess) → structured response
```

## Security Model
- Blocked shell chars: `; & | \` $( ) > < \n \r && ||`
- Workdir sandbox: `/tmp/toold-sandbox` (configurable via `TOOLD_WORKDIR`)
- Max timeout: 120s (configurable via `MAX_TIMEOUT`)

## Tool Registry
JSON file at `/tmp/toold_registry.json`:
```json
{
  "tools": [
    {"name": "shell", "description": "run shell commands", "enabled": true},
    {"name": "python", "description": "run inline python", "enabled": true},
    {"name": "exec_file", "description": "execute saved script files", "enabled": true}
  ]
}
```

## API Endpoints

### GET /health
Returns: `{"status": "ok", "workdir": "/tmp/toold-sandbox", "max_timeout": 120}`

### GET /test
Self-test: exercises shell + python + file + registry end-to-end. Used by the bootstrap wizard to verify the full tool pipeline.
Returns:
```json
{
  "success": true,
  "results": {
    "shell": {"ok": true, "stdout": "tool-ready"},
    "python": {"ok": true, "stdout": "py-ready"},
    "registry": {"ok": true, "tool_count": 3},
    "file": {"ok": true, "stdout": "file-ready"}
  },
  "duration_ms": 56
}
```

### POST /exec
Execute shell command.
```json
{"command": "ls -la", "timeout": 30}
```
Returns: `{"success": bool, "stdout": str, "stderr": str, "exit_code": int, "duration_ms": int}`

### POST /exec/python
Execute inline Python.
```json
{"code": "print('hello world')", "timeout": 30}
```

### POST /exec/file
Execute script file.
```json
{"filepath": "/tmp/script.py", "args": ["arg1", "arg2"]}
```
- `.py` → python3
- `.sh` → bash
- others → direct exec

### GET /registry
Returns full registry JSON.

### POST /registry/{name}/enable
Enable a tool. Returns: `{"updated": "toolname", "enabled": true}`

### POST /registry/{name}/disable
Disable a tool. Returns: `{"updated": "toolname", "enabled": false}`

## Response Format
All exec endpoints return:
```json
{
  "success": true,
  "stdout": "...",
  "stderr": "",
  "exit_code": 0,
  "duration_ms": 45
}
```

On timeout: `success=false`, `stderr="Timed out after Ns"`, `exit_code=-1`

## Port
- 8742

## Dependencies
- FastAPI
- uvicorn
- Python 3