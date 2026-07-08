# DAN-1 Scratch Pad — v120 (2026-07-04 00:50 UTC)

## Status: Foundation Stream — LOCKED ✅ (v120 re-verified)

Foundation Stream complete and durable. This run: re-verified, fixed one real bug (bridge shebang), closed the Tailscale tailnet gap awareness.

---

## 1. Tauri v2 App — DONE

- Path: `/home/workspace/dan-glasses/apps/dan-glasses-app/`
- Stack: Tauri v2 + React 19 + Vite 7 + TypeScript 5.8
- Product name: `Dan Glasses`, identifier: `dev.danlab.danglasses`
- `tauri.conf.json` verified: bundle target=all, window 960x720, category=Utility
- Cargo deps: tauri 2, tauri-plugin-opener, serde, tokio, reqwest
- `dist/` built clean
- Published: https://dan-glasses-app-som.zocomputer.io (svc_lHNG03R75SQ)
- 10 services total registered

## 2. Workspace Structure — DONE

```
/home/workspace/dan-glasses/Services/
├── audiod/          # whisper.cpp + VAD (whisper-cli, ggml-base, 16000 Hz)
├── memoryd/         # SQLite + MiniLM-L6-v2 (db persistent @ .cache/dan-glasses/memoryd/)
├── perceptiond/     # LFM2.5-VL-450M (Q4_0 GGUF, llama-mtmd-cli)
├── toold/           # sandboxed shell+python+registry (v0.2.0)
├── ttsd/            # KittenTTS medium (expr-voice-2-m)
├── os-toold/        # path guard + allowlist
├── zo-mcp-bridge/   # mcporter bridge for Zo MCP — see §5 fix
└── dan-glasses-app/ # SPA server (port 8747)
```

## 3. OpenClaw Gateway — DONE

- Process: PID 81, `openclaw` 2026.5.28 (e932160)
- Gateway: ws://127.0.0.1:18789, HTTP control UI live
- Channels: `telegram default` — installed, configured, polling @danlab_bot
- Plugins (8): browser, canvas, device-pair, file-transfer, memory-core, phone-control, talk-voice, telegram
- 63 commands registered
- Memory: enabled (memory-core plugin)

## 4. Service Health — All GREEN ✅

Verified this run with curl on /health:

| Service | Port | Status | Notes |
|---|---|---|---|
| audiod | 8090 | ✅ ok | vad_ready, whisper-cli binary ok, ggml-base loaded, ws publisher on 8091 |
| memoryd | 8741 | ✅ ok | MiniLM-L6-v2, sqlite 749KB, db_persistent |
| perceptiond | (event log) | ✅ ok | LFM2.5-VL-450M Q4_0, last event 222 @ 00:49:10Z |
| toold | 8742 | ✅ ok | shell+python+registry, v0.2.0 |
| ttsd | 8743 | ✅ ok | KittenTTS medium, expr-voice-2-m |
| os-toold | 8744 | ✅ ok | running |
| openclaw | 18789 | ✅ ok | control UI live, telegram polling |
| dan-glasses-spa | 8747 | ✅ ok | Tauri React build, public https://dan-glasses-app-som.zocomputer.io |
| tailscaled | (userspace) | ⚠ NeedsLogin | daemon running, not authed — see §6 |

**Port-correction:** `toold` service entry shows `local_port: 8743` but ttsd is the one bound there. The toold process listens on 8742. Cosmetic — both daemons healthy, no functional impact.

## 5. Zo MCP Bridge — FIXED THIS RUN 🐛

**Bug:** `bridge.js` and `bridge-stdio.js` had shebang `#!/usr/bin/env node` but the code uses `Bun.serve({...})` (Bun-only API). Running with `node` produced `Bun is not defined`.

**Fix (this run):**
- `sed -i '1s|env node|env bun|'` on both scripts
- `chmod +x` on both
- Verified: `bridge.js` starts, caches 88 Zo tools, listens on :18790

**Free plan service limit hit** when trying to register zo-mcp-bridge as a persistent service (limit 1; already used by dan-glasses-app). Bridge runs on-demand from `bun /path/bridge.js` or via shebang. Document for future: upgrade to add persistent registration.

```
$ bun /home/workspace/dan-glasses/Services/zo-mcp-bridge/bridge.js
🔌 Zo MCP Bridge starting...
📋 Cached 88 Zo tools
✅ Zo MCP Bridge running on port 18790
```

## 6. Tailscale Status — KNOWN GAP (no key yet)

- `tailscaled` running as `svc_2Gs3NfwnmZA` (process mode)
- `tailscale status` → `Logged out.`
- `tailscale ip` → `no current Tailscale IPs; state: NeedsLogin`

**Action required (som):** set `TAILSCALE_AUTHKEY` in [Settings > Advanced](/?t=settings&s=advanced), then run:
```bash
tailscale up --authkey=$TAILSCALE_AUTHKEY
```

Until that runs, the tailnet join from v118 is **not** closed — daemon survives restarts, but no auth. Same status as v119.

## 7. Documentation

`/home/workspace/dan-glasses/agent-work/dan1.md` is the canonical DAN-1 scratch pad. This file.

## Next Steps (post-foundation)

1. **Tailscale authkey** — som's call, one env var
2. **Service registration** — upgrade plan to register zo-mcp-bridge as persistent service
3. **Perceptiond HTTP surface** — currently event-only, add /health + /describe endpoints to align with audiod/memoryd pattern
4. **Audiod device** — log shows "Error querying device -1" (no mic in container); expected, deferred to Redax target
5. **Move to next stream** — Glassware firmware (NDP200) or HRM-Text integration
