# Service Ports & Endpoints — Dan Glasses

**Last updated:** 2026-07-11 (DAN-1 v129)
**Status:** All 8 canonical daemons live, supervised by supervisord (`/etc/zo/supervisord-user.conf`).

## TL;DR

| Service        | Port(s)         | Protocol          | Health        | Owner supervisor entry        |
|----------------|-----------------|-------------------|---------------|-------------------------------|
| `audiod`       | 8090 + 8091     | HTTP + WebSocket  | `/health`     | `[program:audiod]`            |
| `perceptiond`  | 8092            | HTTP              | `/status`     | `[program:perceptiond]`       |
| `memoryd`      | 8741            | HTTP (FastAPI)    | `/health`     | `[program:memoryd]`           |
| `toold`        | 8742            | HTTP (FastAPI)    | `/health`     | `[program:toold]`             |
| `ttsd`         | 8743            | HTTP              | `/health`     | `[program:ttsd]`              |
| `os-toold`     | 8744            | HTTP              | `/health`     | `[program:os-toold]`          |
| `openclaw`     | 18789 (loopback)| HTTP              | `/health`     | `[program:openclaw-gateway]`  |
| `memory-bridge`| — (fan-in only) | —                 | log + supervisor | `[program:memory-bridge]` |

## Quick probes

```bash
curl http://127.0.0.1:8090/health       # audiod → {status:ok, readiness:{...}}
curl http://127.0.0.1:8092/status       # perceptiond
curl http://127.0.0.1:8741/health       # memoryd (returns db_persistent flag)
curl http://127.0.0.1:8742/health       # toold
curl http://127.0.0.1:8743/health       # ttsd
curl http://127.0.0.1:8744/health       # os-toold
curl http://127.0.0.1:18789/health      # openclaw (loopback only — Tailscale needed for remote)
```

## Endpoints that matter

### audiod (8090)
- `GET /help` — full route catalog + restart-only config keys
- `GET /live` `/ready` `/status` — k8s-style probes
- `POST /start` `/stop` `/restart` — capture loop control
- `POST /ptt` — push-to-talk trigger
- `POST /reload` — hot-reload config (publish.mode requires full `/restart`)
- `WS /stream` (port 8091) — broadcast transcript events. Schema: `{type, session_id, event_id, seq, text, start_ms, end_ms, confidence, ts_ms}`

### memoryd (8741)
- `POST /memories` — body `{type: "episodic"|"semantic"|"procedural", content: str, metadata?: dict}`
- `GET /query?text=...&top_k=N` — semantic + lexical recall
- `GET /memories` `/memories/{id}` `/memories/by-type/{type}` — browse
- `DELETE /memories/{id}`
- `GET /stats`
- `POST /v1/embeddings` — direct MiniLM-L6-v2 access
- `POST /conversations` — store conversation turn

### toold (8742)
- `GET /health` `GET /test` — self-test (shell + python + file + registry)
- `POST /shell` `/python` `/exec_file` — sandboxed execution
- `POST /tools/{name}` — named tool exec (registry-backed)

### ttsd (8743)
- `GET /voices` — list 8 voices
- `POST /speak` — body `{text, voice}` → audio/wav blob

### os-toold (8744)
- `POST /command` — restricted OS commands (path guard + allowlist)
- See `Services/os-toold/SCHEMA.json` for the full shape

### perceptiond (8092)
- `GET /status` — frame counter, salient count, VLM busy state
- Modes: `watchful` (default) | `triggered` | `paused`
- Sends its own `episodic` memories to memoryd on salient frames

### openclaw (18789, loopback)
- `GET /health`
- Telegram bot `@danlab_bot` — polling mode, no webhook
- Auth: bearer token in `OPENCLAW_GATEWAY_TOKEN` env var
- `dmPolicy: pairing`, `groupPolicy: allowlist`, `streaming: partial`

## Data flow

```
                    ┌──────────────┐
  mic → audiod ──→  │  WS 8091     │
                    │ /stream      │
                    └──────┬───────┘
                           │ broadcast (events)
                           ↓
                    ┌──────────────┐
                    │memory-bridge │  ← NEW v129
                    │  (fan-in)    │
                    └──────┬───────┘
                           │ POST /memories
                           ↓
                    ┌──────────────┐
                    │  memoryd     │  ← persistent SQLite + MiniLM
                    │  :8741       │
                    └──────────────┘
                           ↑
                           │ POST /memories (perceptiond writes salient frames directly)
                           │
                    ┌──────────────┐
   camera → perceptiond │
                    :8092         │
                    └──────────────┘
```

## Notes

- **Tailscale is logged out** on this host. OpenClaw binds 127.0.0.1 only. To expose remotely: add `TS_AUTHKEY` to [Settings > Advanced](/?t=settings&s=advanced), then `tailscale up --authkey=$TS_AUTHKEY --hostname=dan-glasses`, then update openclaw config to `0.0.0.0`.
- **memory-bridge** is a DAN-1 v129 addition: zero-dep Python WS client, ~220 LOC, supervised, idempotent on `event_id`. See `Services/memory-bridge/README.md`.
- All supervisor entries live in `/etc/zo/supervisord-user.conf`. Reapply with `supervisorctl -c /etc/zo/supervisord-user.conf reread && update`.
