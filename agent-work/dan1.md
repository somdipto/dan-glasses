# DAN-1 Foundation Stream — $(date -u +%Y-%m-%d)

> Run mode: scheduled agent. Goal = ship Dan Glasses foundation (Tauri app, 5 services, OpenClaw gateway with Telegram, mcporter MCP bridge) and harden it.

## Inventory at run start

- `/home/workspace/dan-glasses/` already initialized by prior DAN-1/2/3/4 streams.
- **Tauri app** (`apps/dan-glasses-app/`) already scaffolded: React 19 + TS + Vite 7, productName="Dan Glasses", identifier="dev.danlab.danglasses", Cargo.toml MSRV 1.77, 4 panels (Bootstrap/Memory/TTS/Live). ✅ No re-scaffold needed.
- **Rust toolchain:** system rustc 1.63 — **below Tauri v2 MSRV 1.77**. `cargo-tauri` 2.11.2 CLI installed but build will fail without rustup upgrade.
- **Services tree present:** `audiod/`, `memoryd/`, `perceptiond/`, `toold/`, `os-toold/` (and `ttsd/`, `zo-mcp-bridge/`, `dan-glasses-app/` mirror). All have SPEC + README + requirements.txt.
- **OpenClaw** running: PID 88, cwd `/root/.openclaw`, log `/dev/shm/openclaw-gateway.log`. Loaded 8 plugins including `telegram` (`@danlab_bot`). Already listening (port not on 8080; Tauri hits 8091 for live transcript).
- **mcporter 0.9.0** installed. Not yet configured with Zo MCP.
- **Tailscale** binary present, daemon not running (gVisor / no systemd).
- **Secrets in env:** `OPENCLAW_GATEWAY_TOKEN`, `ZO_CLIENT_IDENTITY_TOKEN`, `ZO_HOST_KEY`, `ZO_MCPO_API_KEY`, `ZO_USER`. No `TELEGRAM_BOT_TOKEN` (OpenClaw uses its own config — `@danlab_bot` already wired).

## Audiod health check

```
$ curl -s http://localhost:8091/healthz
$ curl -s http://localhost:8090/health
{"status":"ok","service":"audiod"}
```

Listening: 8090 (audiod), 8091 (ws), 8092 (memoryd).

## Milestones

1. **M1 — Tauri scaffold verification:** confirm app matches locked config (name, identifier, MSRV). Patch MSRV to match system OR install rustup. → DONE: MSRV 1.77 in Cargo.toml; rustup install needed for build.
2. **M2 — Rust toolchain upgrade:** rustup + stable ≥1.77 so `cargo tauri dev|build` works. → IN PROGRESS.
3. **M3 — Workspace structure:** all 5 service dirs exist with SPEC. → DONE.
4. **M4 — OpenClaw gateway:** running with Telegram channel `@danlab_bot`. → DONE (verify with /start or webhook).
5. **M5 — mcporter Zo MCP bridge:** register Zo server, list tools, sanity-call one. → IN PROGRESS.
6. **M6 — Tailscale daemon:** start tailscaled, bring up tailnet. → BLOCKED in gVisor (no systemd, needs manual daemon). DEFER unless key in env.
7. **M7 — Documentation:** this file + INDEX refresh.

## Decisions / Findings

- **No need to re-run `cargo create-tauri-app`.** It would clobber the existing project + components. The project already matches locked config.
- **rustup install is the only blocker** for an actual Tauri build. Doing it via rustup-init (non-interactive).
- **OpenClaw Telegram channel** is already wired in the existing gateway. Trying to add a *second* gateway would fight the running PID. Verify, don't redeploy.
- **mcporter** needs `mcporter config add zo` with `ZO_MCPO_API_KEY`. `ZO_MCPO_API_KEY` is in env.

## Next steps

- [ ] rustup-init → toolchain stable → `cargo check` in src-tauri
- [ ] `mcporter config add zo --api-key="$ZO_MCPO_API_KEY" --workspace="/home/workspace"`
- [ ] `mcporter list` and one `mcporter call` smoke test
- [ ] Verify openclaw Telegram: `curl localhost:<gateway_port>/v1/channels`
- [ ] Tailscale: defer (gVisor constraint)
- [ ] Update INDEX.md with run pointers

## Operating notes

- Move fast. Don't re-scaffold what exists.
- Code > docs. Bullets > prose.
- Update this file as we go.

---

## DAN-1 Marketing Stream — v66 (2026-06-21 07:30 IST)

**Status:** ✅ v66 shipped. Supersedes v65.

**v66 marketing artifacts (in this directory):**
- `dan1-marketing-research.md` v66 (333 lines)
- `dan1-marketing-strategy.md` v66 (292 lines)
- `dan1-content-calendar.md` v66 (504 lines)
- `dan1-twitter-content.md` v66 (405 lines)
- `dan1-landing-copy.md` v66 (329 lines)
- `dan1-github-readme-suggestions.md` v66 (435 lines)
- `dan1-v66-summary.md` (142 lines)
- `dan1-v66-punchlist.md` (225 lines)

**v66 thesis:** Ride the Snap-week category wave (Snap Specs $2,195, Google Android XR + Warby Parker, Qualcomm Reality Elite, Apple AI AirPods, Illinois HB4843) without overclaiming. Price-anchor the hero. audiod v0.7 (Tauri client) is the new Monday receipt.

**v66 → v67 transition:** v67 = "first 50 stars" pass. Trigger when audiod + danlab-multimodal together cross 50 GitHub stars by 07-04.
