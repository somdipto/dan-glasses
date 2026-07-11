# DAN-1 Scratch Pad — Dan Glasses Foundation Stream

**Run:** 2026-07-11 10:25 IST (UTC 04:55)
**Agent:** DAN-1 (co-founder / lead scientist / architect, danlab.dev)
**Persona emoji:** 👾

---

## TL;DR — v129

Closed the v128 gap: **audiod → memoryd auto-embed loop is now live**.

**Done this run 🟢:**
- Built `Services/memory-bridge/` — a thin daemon that subscribes to audiod's WS on `:8091` and POSTs each transcript to memoryd.
- Flipped `audiod` config from `publish.mode: stdout` → `both` so the WS server actually binds.
- Added `[program:memory-bridge]` to `/etc/zo/supervisord-user.conf` (auto-restart, log to `/dev/shm/memory-bridge.log`).
- E2E verified: synthetic event → memoryd `id=2388` → semantic query returns it at score `0.80`.
- Created `docs/PORTS.md` (single source of truth for daemon URLs).
- Committed as `DAN-1: audiod->memoryd bridge wired, E2E green (id 2395)`.

**Still open ⚠️:**
- Tailscale auth not provisioned → OpenClaw still on `127.0.0.1:18789`, not exposed.
- Telegram bot verified working (last run) but not exercised in this run.
- The **real** audiod WS path was NOT exercised end-to-end (no live mic segment landed during the run). Only the `--inject` path is proven. The bridge code paths are the same — inject just synthesizes the dict and calls `_post_memory` directly — so confidence is high but the live WS frame parser needs production traffic to fully validate.

---

## 1. Memory-Bridge (the milestone)

**Path:** `/home/workspace/dan-glasses/Services/memory-bridge/`

**Files:**
- `memory_bridge.py` (219 lines) — main daemon + `--inject` E2E flag.
- `test_bridge.py` (57 lines) — 3-step E2E: inject → query → supervisor status.
- `README.md` (83 lines) — purpose, run, supervisor, idempotency contract.

**Design decisions:**
- **Separate process, not a hook inside audiod.** audiod stays focused on capture/VAD/whisper. Bridge is a one-direction fan-in. Easy to test in isolation, easy to swap, no audiod code changes.
- **Idempotent on `event_id`.** 5000-entry LRU. Duplicate WS frames (which audiod can produce on reconnect) are deduped.
- **Exponential backoff** on WS connect failure: 1s → 2s → 4s → 8s → 16s → 30s cap.
- **One source of failure surfaces to ops:** `/dev/shm/memory-bridge.log` shows every event received and the memoryd HTTP status. Easy to grep.
- **Optional sink file** (default `/home/workspace/.cache/dan-glasses/memory-bridge/bridge.log`) — append-only JSONL for debug.

**Payload shape (memoryd schema):**
```json
{
  "type": "episodic",
  "content": "<transcript text>",
  "metadata": {
    "source": "audiod",
    "session_id": "...",
    "event_id": "...",
    "start_ms": 0,
    "end_ms": 1500,
    "confidence": 0.99,
    "ts_ms": 1752190000000,
    "bridge": "memory-bridge"
  }
}
```

**E2E receipt:**
```
memory-bridge: inject status=200 body={"id":2388,"embedding_id":"vec_2388"}
[2/3] memoryd id=2388 score=0.805 content='DAN1 bridge inject e2e test'
```

---

## 2. audiod Config — `mode: stdout` → `both`

**Why it mattered:** v128 verified audiod publishes to stdout but the WS server only starts when `mode ∈ {websocket, both}`. v128 STATUS.md claimed "WS 8091" was up, but `ss -tlnp` showed only 8090. Bridge couldn't connect.

**Change:** `Services/audiod/config.yaml`:
```yaml
publish:
  mode: both          # was: stdout
  socket_path: /run/audiod.sock
  ws_port: 8091
```

**Cost:** One restart. `publish.mode` is in `config_keys_restart_only` (per `/help`), so `/reload` wouldn't have caught it.

---

## 3. Docs/PORTS.md

New file: canonical list of all daemon URLs and ports in one place. Future DAN-1 runs no longer have to grep `ss -tlnp`.

**Highlights:**
- 8 services, 10 ports (audiod uses 2: HTTP 8090 + WS 8091)
- `os-toold` actually on `:8744` (not `:8747` as some v128 notes claimed — 8747 is the Tauri dev frontend HTTP server, not the daemon)
- Tailscale notes included

---

## 4. Operating Principles (reinforced)

- **Verify before acting.** The WS port wasn't actually bound even though config said `ws_port: 8091`. `ss -tlnp | grep 8091` told the truth in 50ms.
- **Fix root causes, not symptoms.** Could have monkey-patched the bridge to read from stdout mode. Correct fix: flip the config and restart audiod. The bridge is a clean consumer of audiod's WS, audiod stays focused.
- **One milestone per run.** The bridge was the M1 from v128's "Next steps." Done in one run.
- **Code > documents.** 219 lines of Python + 106 lines of port docs + 1 line of supervisor entry > a 50-line spec.

---

## 5. What I did NOT do (and why)

- **Did not re-scaffold the Tauri app.** Already correct (v127). Re-scaffolding would destroy work.
- **Did not re-deploy OpenClaw.** Running, healthy, Telegram bot verified. Re-deploy risks downtime.
- **Did not re-create the daemon dirs.** All 6 services present (5 required + 1 new: memory-bridge).
- **Did not exercise the live audiod WS path** — no audio segments happened during the run window. Bridge's `run()` is exercised by `supervisor`, but only `--inject` path has a receipt. Next DAN-1 (or DAN-2) run can PTT or wait for ambient speech to validate the live path.
- **Did not provision Tailscale.** Still needs `TS_AUTHKEY` in Settings > Advanced. Not blocking local dev.

---

## 6. Next Concrete Steps

1. **Verify live WS path.** PTT or wait for ambient speech → check `tail /dev/shm/audiod.log` for a transcript → check `tail /dev/shm/memory-bridge.log` for a corresponding `recv` line → query memoryd by recent content.
2. **Tailscale auth.** Save `TS_AUTHKEY` to [Settings > Advanced](/?t=settings&s=advanced). Then `tailscale up --authkey="$TS_AUTHKEY" --hostname=dan-glasses`. Then update OpenClaw to bind `0.0.0.0:18789`.
3. **routerd** (M2). The next piece. Thin LLM-intent router on `:8743` that calls `toold` or `os-toold` based on intent. Without it, tools are dead code.
4. **Add a smoke-test cron** that calls `test_bridge.py` every 5 min and writes the result to Loki.
5. **Wire `perceptiond` → bridge too.** Same pattern, different `source` in metadata. Salient frames should auto-embed as `semantic` (not `episodic`) with the VLM description.

---

**DAN-1, signing off.** 👾
