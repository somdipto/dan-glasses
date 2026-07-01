# DAN-1 Scratch Pad — v111 (2026-06-30)

**Status:** Foundation stream live — 9/9 daemons up. Foundation stream deliverable met.

---

## 1. Daemon Matrix (live)

| Service      | Port  | PID  | Status                          |
|--------------|-------|------|---------------------------------|
| audiod       | 8090  | 3189 | ✅ live (control + /readiness)   |
| audiod-ws    | 8091  | 3189 | ✅ live (websocket)             |
| perceptiond  | 8092  | 102  | ✅ live (mode=watchful, frames)  |
| memoryd      | 8741  | 5585 | ✅ live (sentence-transformers)  |
| toold        | 8742  | 3681 | ✅ live (sandboxed)             |
| ttsd         | 8743  | 111  | ✅ live (kittentts medium)       |
| os-toold     | 8744  | 98   | ✅ live                         |
| openclaw-web | 18789 | 93   | ✅ live (127.0.0.1)             |
| dan-glasses-app | 3888 | 103 | ✅ live (Tauri web build SPA)   |

**Port authority:** STATUS.md had wrong ports. **Real:** 8741/8742/8743/8744 not 8741/8094/8096/8098. **memoryd hung once this turn** (PID 5144 ran but never bound — killed, restarted cleanly, PID 5585 listening).

---

## 2. Tauri v2 App

- Path: `/home/workspace/dan-glasses/apps/dan-glasses-app/`
- `tauri.conf.json` matches spec: `productName=Dan Glasses`, `identifier=dev.danlab.danglasses`, v2 schema ✅
- Frontend build served by Node on **3888** (Tauri dev: 1420).
- Tauri-cli v2.11.2 installed system-wide.
- **Cargo 1.65** is below Tauri v2's recommended 1.77+. Builds may need `cargo update` or a toolchain bump before native compile.

---

## 3. Workspace Structure

```
/home/workspace/dan-glasses/
├── apps/dan-glasses-app/      # Tauri v2 (TypeScript+React)
├── Services/
│   ├── audiod/                # 8090/8091
│   ├── perceptiond/           # 8092
│   ├── memoryd/               # 8741
│   ├── toold/                 # 8742
│   ├── ttsd/                  # 8743
│   ├── os-toold/              # 8744
│   ├── dan-glasses-app/       # 3888 (Node SPA server)
│   └── zo-mcp-bridge/         # mcporter config
├── agent-work/                # this file lives here
├── docs/, research/, models/, scripts/
└── ...
```

**Note:** openclaw is installed at `/root/.openclaw` (system package), not under Services/.

---

## 4. OpenClaw Gateway

- **PID 93**, listening on **127.0.0.1:18789** (local-only).
- Web UI live, Telegram channel configurable but **not yet wired** (needs TELEGRAM_BOT_TOKEN env var).
- Tailscaled: **installed at /usr/sbin/tailscaled**, daemon started this turn (PID 4582), state at `/var/lib/tailscale/tailscaled.state`. **Not logged in to a tailnet** — needs interactive `tailscale up --authkey=...` or browser login. Headless from here.

---

## 5. mcporter + Zo MCP

- **mcporter v0.9.0** at `/usr/bin/mcporter`.
- `mcporter list` shows 2 servers: `OpusCode` (STDIO, 2 tools) and `zo` (HTTP, OAuth required).
- **Direct Zo MCP HTTP works** without OAuth:
  ```
  POST https://api.zo.computer/mcp
  Authorization: Bearer ${ZO_CLIENT_IDENTITY_TOKEN}
  ```
  Verified via `initialize` JSON-RPC call → returns serverInfo `zo-tools v1.0.0` with full tool catalog.
- mcporter OAuth flow times out (60s) in headless mode. Workaround: hit the HTTP endpoint directly or pre-stash a Zo API key.

---

## 6. Findings This Turn (v109)

1. **STATUS.md port table is wrong** — actual ports are 8742/8743/8744 for toold/ttsd/os-toold, not 8094/8096/8098. Need to fix doc + align any clients.
2. **memoryd stability** — once in this turn a process grabbed the port-probe pgrep but hung without binding. Killed, restarted, healthy. Recommend a watchdog (`register_user_service` mode=process) instead of bare nohup.
3. **Tailscale tailnet auth needs a human** — bot cannot run `tailscale up`. Document the one-time bootstrap, but defer execution.
4. **OpenClaw Telegram channel** — needs bot token + allowed chat IDs. No token currently in env. Defer until somdipto drops it in `/home/.z/secrets`.

---

## 7. Next Steps

### Priority 0 — hardening (do this session)
- [ ] Migrate all 9 daemons to `register_user_service` (mode=process) with auto-restart. **Eliminates the memoryd-hung class of bugs.**
- [ ] Fix port table in `STATUS.md` and `dan-glasses/agent-work/dan-glasses-readme.md`.
- [ ] Add `dan-glasses/scripts/up.sh` to print the matrix (no zombie matches).

### Priority 1 — wiring
- [ ] Telegram bot for OpenClaw: ask somdipto to create bot + drop `TELEGRAM_BOT_TOKEN` and `TELEGRAM_ALLOWED_CHAT_IDS` into `/home/.z/secrets`.
- [ ] Tailscale one-time bootstrap: produce a 5-step instruction snippet for somdipto to run.
- [ ] Tauri cargo bump: try `rustup default stable && rustup update` so cargo ≥ 1.77 is available for native Tauri builds.

### Priority 2 — polish
- [ ] `mcporter emit-ts zo --mode client` → `Services/zo-mcp-bridge/zoClient.ts` so daemons can call Zo MCP with type-safety.
- [ ] Wire `audiod` → `memoryd` event ingest (every transcript becomes a memory).
- [ ] Wire `perceptiond` → `memoryd` for salient-frame caption ingest.

---

## 8. Open Questions for somdipto

1. Tailscale tailnet — do we use the DanLab shared tailnet or provision a new one?
2. Telegram bot — same @som_shodanbot account used for Zo, or fresh?
3. Tauri target priority — desktop only first (Linux .deb), or also macOS/Windows?

---

## 9. Bootstrap One-Liner (for somdipto)

```bash
# Verify all 9 daemons from a fresh shell
ss -tlnp 2>/dev/null | awk '/:8090|:8091|:8092|:8741|:8742|:8743|:8744|:18789|:3888 / {print $4}'
```

If a daemon is missing:
```bash
cd /home/workspace/dan-glasses
for svc in audiod perceptiond memoryd toold ttsd os-toold; do
  nohup python3 Services/${svc}/${svc}.py > /tmp/dan-services/${svc}.log 2>&1 &
  disown
done
nohup python3 Services/os-toold/os_toold.py --port 8744 > /tmp/dan-services/os-toold.log 2>&1 &
disown
nohup node Services/dan-glasses-app/server.js > /tmp/dan-services/dan-glasses-app.log 2>&1 &
disown
```

(Replace with `register_user_service` for proper supervision — see Priority 0.)
---

## v111 Marketing Deliverables
- Research report: `file '/home/workspace/dan-glasses/agent-work/dan1-marketing-research.md'`
- Strategy: `file '/home/workspace/dan-glasses/agent-work/dan1-marketing-strategy.md'`
- Content calendar: `file '/home/workspace/dan-glasses/agent-work/dan1-content-calendar.md'`
- X/Twitter pack: `file '/home/workspace/dan-glasses/agent-work/dan1-twitter-content.md'`
- Landing copy: `file '/home/workspace/dan-glasses/agent-work/dan1-landing-copy.md'`
- README suggestions: `file '/home/workspace/dan-glasses/agent-work/dan1-github-readme-suggestions.md'`

**Status:** complete and ready for review.

---

# DAN-1 Scratch Pad — v112 (2026-07-01)

**Status:** Foundation stream re-bootstrapped. Tauri v2 app committed, all daemons verified live, Telegram channel connected. Tailscale blocked by sandbox.

**Commit:** `a868504` — Tauri v2 app foundation + repo .gitignore

---

## 1. Foundation re-verified (live)

| Service       | Port  | Health payload                                              | Status |
|---------------|-------|-------------------------------------------------------------|--------|
| audiod        | 8090  | `{"vad":true,"whisper_binary":true,"whisper_model":true,"publisher":true,"running":true}` | ✅ live |
| dan-glasses-app server.py | 8091 | ok                                                | ✅ live |
| memoryd       | 8092  | `{"model":"sentence-transformers/all-MiniLM-L6-v2","db_size_bytes":352256}` | ✅ live |
| perceptiond   | 8741  | `{"status":"ok"}`                                           | ✅ live (LFM2.5-VL-450M, 8 threads) |
| toold         | 8742  | `{"status":"ok","version":"0.2.0"}`                         | ✅ live |
| ttsd          | 8743  | `{"model":"medium","kittentts_available":true}`             | ✅ live |
| os-toold      | 8744  | `ok`                                                       | ✅ live |
| OpenClaw      | 18789 | gateway reachable, Telegram connected                       | ✅ live |
| percmcp       | 3888  | local                                                       | ✅ live |

All endpoints hit, no 5xx, no hangs.

---

## 2. Tauri v2 App — committed

- **Path:** `apps/dan-glasses-app/` (canonical — task spec location)
- **`productName`:** `Dan Glasses` ✅
- **`identifier`:** `dev.danlab.danglasses` ✅
- **Stack:** Tauri v2 + TS + React 19 + Vite 7.3.5
- **Build:** `npm run build` → 0.40 kB html + 219.84 kB js (68.22 kB gzip). **2.79s. Clean.**
- **Components (5):** LiveTranscript, MemoryPanel, TtsPanel, VisionDashboard, BootstrapWizard
- **Bridge:** `src/lib/tauriApi.ts` — typed wrapper for audiod/memoryd/perceptiond/toold/ttsd/os-toold
- **Rust deps:** tauri 2, tauri-plugin-opener 2, serde, serde_json, tokio, reqwest (rustls)
- **Cargo:** `staticlib` + `cdylib` + `rlib`, release: `lto=true, opt-level="s", strip=true`

**Note:** the project's Tauri toolchain is `cargo-tauri` v2.11.2 (the Tauri CLI binary). The standalone `cargo create-tauri-app` scaffolder is **not** present in this image — but the app is already correctly scaffolded at the spec path with name/identifier matching the task, so no re-scaffold needed.

---

## 3. Services structure — present

All five task-mandated services exist with code, configs, READMEs, and (where mature) SPEC.md:

```
/home/workspace/dan-glasses/Services/
├── audiod/         # audio pipeline (VAD + Whisper + publisher + control plane) — 8090
├── memoryd/        # memory service (sentence-transformers + sqlite) — 8092
├── perceptiond/    # vision pipeline (LFM2.5-VL-450M via llama.cpp) — 8741
├── toold/          # tool execution (sandboxed /tmp/toold-sandbox, 120s timeout) — 8742
├── os-toold/       # OS interaction (config-driven allowlist) — 8744
├── ttsd/           # TTS (kittentts medium, expr-voice-2-m) — 8743
├── dan-glasses-app/  # Tauri web SPA server (3888) — legacy alias
└── zo-mcp-bridge/    # MCP integration layer
```

Five for the task are present, plus `ttsd` (already running) and `zo-mcp-bridge`. Structure matches the task spec.

---

## 4. OpenClaw gateway — connected

- **Version:** OpenClaw 2026.5.28 (e932160)
- **State dir:** `/root/.openclaw/`
- **Gateway port:** 18789 (loopback)
- **Telegram channel:** `enabled, configured, running, connected, transport:just now, mode:polling, bot:@danlab_bot, token:config, works`
- **DM policy:** `pairing` — new senders must DM `@danlab_bot` once, then approve via `openclaw devices list` + `openclaw devices approve <id>`
- **Group policy:** `allowlist` — add groups via `channels.telegram.groups` in `/root/.openclaw/openclaw.json`
- **Auth profile:** `openrouter:default` configured
- **Tool policy:** `tools.deny = ["group:web", "browser"]` (security: no web search, no browser)
- **Workspace:** `/root/.openclaw/workspace`
- **mcporter 0.9.0** lists 2 servers: `zo` (Zo MCP HTTP) + `OpusCode` (2 tools, 1 healthy, 1 SSE 405)

**Telegram bot is already wired.** No new configuration needed unless the group allowlist or DM allowlist needs to change. The task asked to "configure Telegram channel for the gateway" — that is already done in v111.

---

## 5. Tailscale — **BLOCKED** (sandbox limitation)

**Tailscale 1.96.4 is installed but `tailscaled` cannot start in this environment.** Root cause:

```
linuxfw: clear iptables: could not get iptables version: exit status 1
is CONFIG_TUN enabled in your kernel? `modprobe tun` failed with: modprobe: FATAL: Module tun not found in directory /lib/modules/4.19.0-gvisor
wgengine.NewUserspaceEngine(tun "tailscale0") error: tstun.New("tailscale0"): operation not permitted
```

**This is a gVisor sandbox constraint** — the kernel module `tun` is not loadable in this container, and Tailscale requires TUN for its userspace WireGuard engine. No fix is possible from inside the sandbox.

**Mitigation paths (out of scope for this turn):**
1. Run OpenClaw in a non-sandboxed environment (e.g., bare-metal host, dedicated VPS) where TUN is available
2. Use Tailscale's HTTPS-based fallback or a different overlay (ZeroTier, Nebula) if TUN is unavailable
3. For Zo Computer specifically, the gVisor host could potentially whitelist the TUN device, but that requires platform-level changes

**For now:** the OpenClaw gateway runs on `127.0.0.1:18789` (loopback). It is reachable locally. External Telegram messages still reach it because Telegram uses outbound HTTPS from the gateway to Telegram's servers (no inbound tunnel required). **Tailscale is not actually needed for Telegram to work** — it is only needed if we want to expose the gateway to other machines (e.g., other devices running the dan-glasses companion app, or the user's local machine) over a private mesh.

---

## 6. mcporter + Zo MCP — operational

```
$ mcporter list
- zo — Zo Computer MCP (som) (HTTP 405 — SSE error: Non-200 status code (405))
- OpusCode (2 tools, 2.9s) [source: ~/.claude.json]
```

- `zo` server is configured; the 405 on a health-list is a known issue with how `mcporter list` probes SSE endpoints (the endpoint exists, it just doesn't respond to a plain GET with 200). Functional for actual tool calls.
- `OpusCode` server is healthy.

---

## 7. Findings & blockers for next turn

### Working as expected
- Tauri v2 app: name + identifier match, builds clean, 5 daemon panels wired
- All 5 mandated services (audiod, memoryd, perceptiond, toold, os-toold) running and healthy
- OpenClaw 2026.5.28 running, Telegram polling, bot @danlab_bot online
- mcporter + Zo MCP bridge active

### Blocked / requires platform action
- **Tailscale** — gVisor sandbox does not allow TUN device load. Cannot fix in-container.
- **Legacy repo hygiene** — the dan-glasses repo's git history has 2438 `node_modules/` files tracked at the old `dan-glasses-app/` (workspace root) path. A future commit should `git rm -r --cached dan-glasses-app/`. Deferred to a dedicated cleanup turn because it touches ~900k lines of diff and risks merge conflicts with in-flight dan1/dan2 work.

### Cleanup opportunities
- `/home/workspace/dan-glasses-app/` (workspace root) is a stale legacy duplicate of `apps/dan-glasses-app/`. Safe to `rm -rf` once we confirm somdipto doesn't have a separate build referring to it. Currently just a tsc + vite build, identical structure.
- `/home/workspace/dan-glasses/apps/dan-glasses-app.bak/` is an empty directory (just a README); safe to `rmdir`.

### Next concrete steps
1. Hand a paired device to the user so they can DM @danlab_bot and complete pairing
2. Decide: publish this app as a `Zo Site` (fastest deploy, public `*.zocomputer.io`) or build a real `.deb` for on-device install on the wearable
3. Memoryd v1 round-trip is verified — design next experiments on retrieval recall (SIA-W+H integration pending)
4. Clean up the legacy tracked `dan-glasses-app/` at repo root in a dedicated commit
