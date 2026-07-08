# Dan Glasses Architecture Review — Dan2 v38 (2026-06-22 11:30 IST)

> **Scope.** Re-audit the 5-service Dan Glasses daemon topology, the OpenClaw gateway, the perception/memory/power paths, and the wearable silicon pivot. v38 introduces **one new layer (DanClaw proxy)** and **two changes to the canonical plan** (memoryd embedding model swap, perceptiond cascade adoption). Read with `dan2-research-report.v38.md`.

---

## TL;DR

The 5-service decomposition (audiod, perceptiond, memoryd, toold, os-toold + ttsd + openclaw-gateway) is **the right shape** for a desktop prototype and ships. v38 adds **DanClaw proxy** as a thin (~500 LOC TypeScript) control-plane shim because upstream OpenClaw has **documented production failure modes that map 1:1 to the Dan Glasses critical path**. v38 also swaps the memoryd embedding model to **LFM2.5-Embedding-350M** (Jun 18, Apache 2.0-equivalent) and pre-plans **Nanomind-style cascade scheduling** for perceptiond v1.5 to hit sub-1W wearable power. **The 8 critical PRD risks (canonical analysis v1) are now re-prioritized** — the OpenClaw gap moves to #1, Redax is deprioritized to "evaluate alongside GAP9 / Qualcomm AR1 / Alif B1" rather than "block on."

---

## 1. What the live system actually is (re-audited 11:30 IST)

| # | Component | Implementation | Tests | Status |
|---|-----------|----------------|-------|--------|
| 1 | audiod v0.7 | Python daemon, ALSA capture, Silero VAD, whisper.cpp base.en, RFC 6455 WS fan-out | 121/121 | ✅ live on :8090 + :8091 |
| 2 | perceptiond v1.3 | Python daemon, V4L2 capture + mock fallback, SalienceDetector (motion+face), llama-mtmd-cli + LFM2.5-VL-450M Q4_0 | 8/8 | ✅ live on :8092 |
| 3 | memoryd v1 | FastAPI + aiosqlite, all-MiniLM-L6-v2 (384d) embeddings, episodic/semantic/procedural types | 16/16 | ✅ live on :8741 |
| 4 | toold v1 | FastAPI, shell + python + exec_file, `/tmp/toold-sandbox` workdir, 120s timeout | 18/18 | ✅ live on :8742 |
| 5 | ttsd v0.6 | FastAPI, KittenTTS medium Python bindings, 8 voices, 24 kHz mono WAV | 6/6 | ✅ live on :8743 |
| 6 | os-toold v1 | Python, command execution with path guard | manual | ✅ live on :8744 |
| 7 | openclaw-gateway | TypeScript/Node, Telegram @danlab_bot, Zo MCP bridge | TS suite | ⚠ down (gVisor kills + unhandled-rejection bug) |
| 8 | dan-glasses-app | Tauri v2 + React 19 + Vite 7 | build clean | ✅ live on :8747 |

**All HTTP daemons healthy. OpenClaw is the only flapping component, and the cause is upstream-documented.** This is the central problem v38 addresses.

---

## 2. The OpenClaw reliability problem (NEW v38, top priority)

### 2.1 What fails, in production, today

| Issue | Symptom | Dan Glasses impact | Status |
|-------|---------|---------------------|--------|
| #3715, #13463, #11952, #23441 | Unhandled promise rejection → `process.exit()` | Telegram channel down + memoryd state writes lost | Open in upstream |
| #52725 | 3 Maps grow unbounded → OOM at ~1k sessions | Multi-user / multi-day sessions crash silently | Open in upstream |
| #52092 (resolved) | Cron replay heap growth → OOM | Recurring job scheduler crashes | Fixed in main 2026.5.22, not in tagged release |
| #73861 | sessions_send routing table goes stale | Cross-agent coordination fails silently | Open in upstream |
| PR #21944 (blocked) | Escalating crash-loop backoff | CPU/disk exhaustion on bad config | **Unresolved merge conflicts** |
| Rate-limit failover (#24424) | Doesn't exhaust profile list before next model | Anthropic outage stalls 10+ min | Open in upstream |
| Workspace deps crash (#24424) | Missing node_modules crash exec tool | Tool call cascade fail | Open in upstream |

**v38 read:** **OpenClaw as shipped is a developer-grade gateway with documented production failure modes.** It is the right *ecosystem* choice (TypeScript/Node agent framework, MCP-native, multi-channel) but the *runtime* needs hardening for always-on wearable use. **DanClaw proxy is the hardening layer.**

### 2.2 DanClaw proxy design (~500 LOC TypeScript, v1 deliverable)

**Responsibilities:**
1. **Health fanout.** Poll each daemon's `/health` every 5s. Expose `GET /dandlaw/healthz` returning aggregate `{audiod, perceptiond, memoryd, toold, ttsd, os_toold, openclaw}` status. **Fail open** if OpenClaw is down but daemons are healthy.
2. **Crash suppression.** When OpenClaw restarts (signal 143, exit 1, OOM), proxy holds inbound requests for up to 30s with exponential backoff, returns 503 to UI, retries once OpenClaw's `/health` is OK. **No user-facing 5xx storm during restart.**
3. **State mirroring.** Every OpenClaw-bound message (Telegram send, MCP tool call) is mirrored to `memoryd/conversations` with `session_id` + payload + intent. On OpenClaw restart, proxy replays pending sends from `memoryd`.
4. **MCP tool allowlist.** Only registered tools (perception, memory, os-toold, tts). Argument hashing + audit log. This is the **Sentry-key hijack mitigation** (Jun 21, 2026, develeap.com): an exposed Sentry key in any MCP-server config can be used to hijack agent tool calls; DanClaw's allowlist is the second line of defense after toold/os-toold's existing guardrails.
5. **Crash-loop backoff mirror.** Independent of PR #21944. After 3 gateway crashes in 15 min, proxy stops trying to restart and surfaces `DanClawState.CrashLoop`.
6. **State preservation on SIGTERM.** Proxy writes its own state snapshot to memoryd on SIGTERM. Replays on boot.

**Dependencies:** `axios`, `ws`, `pino`, `lru-cache`, `node:fs/promises`. No new framework. ~12 package deps total. **Deployable as `register_user_service` with mode=http on :18790** (separate port from OpenClaw's :18789).

**v38 ask to somdipto:** approve DanClaw proxy as a v1 deliverable. **Cost:** 1 week of Dan1 + Dan2 + Dan4 time. **Risk:** low (it's a passthrough, not a replacement).

### 2.3 What DanClaw proxy is NOT

- **Not a replacement for OpenClaw.** OpenClaw is the agent runtime. DanClaw is the network shim.
- **Not a security boundary.** The real security boundary is `toold` and `os-toold`. DanClaw is defense-in-depth.
- **Not a stateful store.** `memoryd` is the source of truth. DanClaw mirrors to it, doesn't own state.

---

## 3. The 5-service decomposition is correct (re-confirmed)

| Service | Single responsibility | Failure mode | Recovery | Verdict |
|---------|----------------------|--------------|----------|---------|
| audiod | Mic → VAD → STT → transcript events | No audio, no VAD, whisper stalls | Re-init components, fall back to bare ALSA | ✅ correct |
| perceptiond | Camera → VAD → VLM → description events | Camera fail, VLM fail, OOM | Mock fallback, ring buffer (200 events), restart on OOM | ✅ correct |
| memoryd | Store, embed, retrieve memories | SQLite corruption, embed model crash | WAL mode, periodic VACUUM, model reload from disk | ✅ correct |
| toold | Execute shell/python with guardrails | Subprocess hang, sandbox escape | Timeout 120s, workdir constraint, argument denylist | ✅ correct |
| ttsd | Synthesize speech | Model not loaded, voice invalid | Lazy model load, voice whitelist, 503 on init | ✅ correct |
| os-toold | Execute OS commands with path guard | Path traversal, subprocess leak | Path allowlist, Popen cleanup | ✅ correct |

**No decomposition changes in v38.** The service boundaries are clean. The transport is HTTP loopback + FastAPI which is correct for desktop prototype and Tailscale Serve-ready for wearable (no need to switch to Unix sockets or gRPC).

**One sharpening:** the canonical PRD says "Rust binaries" — these are actually Python daemons. **The PRD narrative is wrong; the code is right.** v38 confirms: keep Python for v1 (faster iteration, all bindings work, OpenClaw already talks HTTP). **Rust rewrite is a v2+ concern, only if we hit performance walls on the wearable (we won't — LFM2.5-VL-450M inference is the bottleneck, not the daemon).**

---

## 4. Power & thermal (v38 update)

### 4.1 Desktop prototype: not a concern (AC-powered)

Current draw on x86_64 laptop: audiod ~0.3W, perceptiond ~5W when VLM active, ttsd ~2W spike, memoryd ~0.3W, toold ~0.1W. **Total idle ~1W, active ~10W peak.** Wall-powered. **No power budget to defend.**

### 4.2 Wearable (v1.5): Nanomind anchor (NEW v38)

The closest published wearable VLM benchmark is **Nanomind (arXiv:2510.05109v6)**: LLaVA-OneVision-Qwen2-0.5B + camera at 0.375W continuous, 18.8h on 2000 mAh.

| Component | OpenGlass (arXiv:2606.07431) | Nanomind | Dan Glasses v1.5 target |
|-----------|------------------------------|----------|-------------------------|
| SoC | GAP9 RISC-V + NE16 | Modular NPU/GPU/DSP | GAP9 OR Qualcomm AR1 OR Alif B1 |
| VLM size | Object detect only (Tinyissimo) | LLaVA-OV-0.5B | LFM2.5-VL-450M Q4_0 + cascade |
| Continuous power | 67.4 mW (detect) | 375 mW (VLM) | **~400 mW target** |
| Battery | 200 mAh (11.5h detect) | 2000 mAh (18.8h VLM) | 2000 mAh (18h+ target) |
| Weight | research frame | research frame | **<80g total** |

**v38 plan:**
- **v1** (desktop): current LFM2.5-VL-450M Q4_0 CPU. 10s/frame. No power concern.
- **v1.5** (wearable): Nanomind-style cascade. Light VFM (e.g., YOLO/CLIP-small) on-device always-on. Full VLM only on salience + ~3 events/minute average. **Hit <1W continuous. Hit 18h battery. Hit <80g weight.**

This is a **form-factor revolution**: 18h battery, not 4h like Snap, is the differentiator.

### 4.3 Thermal (carry from canonical analysis)

40°C surface temp max (skin contact). 42°C → thermal throttle (drop to Gemma3-2B fallback per PRD §5.3, but v38 sharpens: drop to *light VFM only, defer VLM to next idle slot*). **The cascade architecture makes thermal events rarer** because VLM isn't called continuously.

---

## 5. Form factor & silicon (v38 update)

### 5.1 The silicon decision tree (binary, with v38 sharpening)

| Option | Timeline | Risk | Sovereign | Danlab path |
|--------|----------|------|-----------|-------------|
| **Redax** | 12+ months | High (moving target) | Depends | Defer — don't block on this |
| **Qualcomm AR1 / Reality Elite** | 6 months | Low (shipping silicon) | No (US) | Spike Month 1-2 |
| **GAP9 + event cam** (OpenGlass/Nanomind pattern) | 4-6 months | Medium (dev kit only, no commercial module) | Yes (EU RISC-V) | **Spike Month 1 — buy $300 dev kit** |
| **Alif B1** (Brilliant Labs Halo reference) | 4 months | Low (shipping in Halo, $349 retail) | No (US) | Spike Month 2 — buy Halo for teardown |
| **BitNet-VLM** | 12+ months | High (paper, no silicon) | Yes | **Track only, do not wait for v1.5** |
| **Project Solara MDEP** (Microsoft) | Unknown | High (announced, no silicon) | No (US) | Track, don't bet |

**v38 recommendation:** **Buy a GAP9 dev kit + Brilliant Labs Halo in Month 1.** Run LFM2.5-VL-450M on GAP9 in Month 2. Decide silicon by end of Month 3. This collapses the v37 "decide this week" pressure (we don't have dev kits yet — we can't decide what we haven't measured).

### 5.2 Weight target — <80g is achievable

| Component | Estimated weight |
|-----------|------------------|
| Frame + hinges (Brilliant Labs Halo reference) | 30g |
| Camera + mic (event-cam + bone-conduction mic) | 8g |
| GAP9 module + LFM2.5-VL-450M (in flash) | 12g |
| 2× 2000 mAh Lipo (distributed, one per temple) | 30g (15g each) |
| **Total** | **80g** |

**2-day battery life on a 80g device. Snap is 4h on whatever-grams. The form factor is the moat.**

---

## 6. Model selection — same stack, smarter deployment (v38 minor updates)

| Slot | Current | v38 verdict | Change |
|------|---------|-------------|--------|
| Vision | LFM2.5-VL-450M Q4_0 | ✅ Keep | Add cascade (light VFM + on-demand VLM) for v1.5 |
| STT | whisper.cpp base.en | ✅ Keep | None |
| TTS | KittenTTS medium | ✅ Keep | None — v37 spike of Kokoro/Orpheus not necessary |
| **Embedding (memoryd)** | all-MiniLM-L6-v2 (384d) | ⚠ **Swap to LFM2.5-Embedding-350M (1024d)** | **Yes — sovereignty moat strengthens** |
| **Reranker (memoryd v2 v2.0)** | None | 🆕 **Add LFM2.5-ColBERT-350M** | **Late-interaction rerank, Dec 2026** |

See `dan2-model-analysis.v38.md` for full reasoning.

---

## 7. Memory architecture (v38 update)

### 7.1 v1 (current): SQLite + 384d vectors + 3 types. **Working.**

memoryd v1 is shipped. 16/16 tests. all-MiniLM-L6-v2 is fine for v1 because (a) it ships now, (b) the eval hasn't shown it's insufficient yet, (c) the sovereignty argument is real but not blocking for prototype.

### 7.2 v2 v1.0 (Sept 2026): 6-core stack

Per v37 roadmap. **Update v38:** swap the 384d embedding to LFM2.5-Embedding-350M. Add the LFM2.5-Embedding-350M migration to the 6-core scope.

| Component | Provider | License | Status |
|-----------|----------|---------|--------|
| Vector store (embeddings) | LFM2.5-Embedding-350M | Apache 2.0-eq | ✅ shipped Jun 18 |
| Temporal KG (events over time) | Zep | Apache 2.0 | ✅ shipped |
| Memory ops (extract/contradict/update) | Mem0 | Apache 2.0 | ✅ shipped |
| Multi-channel RRF (zero-LLM) | SuperLocalMemory V3.3 | Apache 2.0 | ✅ shipped |
| 4-lever memory (recent/relational/...) | Hindsight | MIT | ✅ shipped |
| Visual memory | VisualMem (uses LFM2.5-VL-450M) | TBD | spike Month 1 |

### 7.3 v2 v2.0 (Dec 2026): add ColBERT reranker + proactive triggering

- LFM2.5-ColBERT-350M as late-interaction reranker (top-100 → top-10)
- MemCog-style proactive memory triggering (arXiv:2605.28046)
- 2× longer context (768d → 1536d via ColBERT)

### 7.4 v3 (Q4 2027+): DCPM dual-process + CogniFold

- System 1 (sync, fast): current memoryd path
- System 2 (async, slow): DCPM/CogniFold schema induction
- Graph-topology self-organization (CogniFold)
- v3 is the path to "memory-as-cognition" but requires 12+ months of stable v2 data to train on

---

## 8. Proactive AI (v38 reclaim the wedge)

### 8.1 The architecture (NEW v38)

| Service | Role | Pattern source |
|---------|------|----------------|
| `audiod` | Demand signal (VAD, ambient noise, conversation patterns) | Carried |
| `memoryd` | Memory retrieval (semantic + episodic + proactive triggering) | MemCog pattern |
| **`proactived`** (NEW v1.5) | Intent classification + proactive suggestion generation + TTS/Telegram fan-out | PASK IntentFlow + ProAct |
| `ttsd` | Output (TTS or Telegram text) | Carried |
| `openclaw` | Channels (Telegram primary, terminal debug) | Carried |

### 8.2 v1.5 proactived spike (Month 1, 2 weeks)

1. Wrap `audiod` VAD events into a `DemandSignal` stream.
2. For each `DemandSignal`, query `memoryd` for "unfinished items related to current location/activity/context."
3. If confidence > 0.7, generate proactive suggestion (e.g., "You walked past the pharmacy 3 times this week; do you want to add a stop?").
4. Output via `ttsd` (TTS) or Telegram (text).
5. Eval against ProActEval-style 5 tasks. **Target: out-eval Snap (no published eval) within 90 days of v1.5 GA.**

### 8.3 The defensive moat

Snap claimed "Proactive AI" with no eval. **dglabs-eval v1 publishes a proactive subset.** This is the auditable, open-source, on-device, safety-gated counter. **The category is reclaimable.**

---

## 9. Safety architecture (v38 sharpening)

| Layer | Defense | Status |
|-------|---------|--------|
| 1. Camera/audio capture | audiod/perceptiond VAD/salience gating | ✅ shipped |
| 2. VLM/STT output | TBD — adversarial-prompt detection in v1.5 | Carry from v37 |
| 3. `toold` | Argument denylist + workdir sandbox + 120s timeout | ✅ shipped |
| 4. `os-toold` | Path allowlist + Popen cleanup | ✅ shipped |
| 5. **DanClaw proxy MCP allowlist (NEW v38)** | Only registered tools, argument hashing, audit log | **v1 deliverable** |
| 6. `dglabs-eval` safety subset (5+3+1 = 9 tasks) | Weight-update gate, harness-edit log | v1.5 |
| 7. Human-in-the-loop (toold `/test` self-check) | Mandatory self-test before first tool use | ✅ shipped (toold `/test`) |

The Sentry-key hijack (Jun 21, 2026) shows that **a single exposed secret in a workspace can be used to hijack tool calls.** DanClaw proxy is the L5 layer that mitigates this. **`toold` + `os-toold` are the L3-L4 layers.** Together: defense in depth.

---

## 10. PRD risk re-prioritization (Δ from canonical analysis v1)

| Rank | Risk (canonical v1) | v38 verdict |
|------|---------------------|-------------|
| 1 | Adaptive FPS throttles capture, not inference | **RESOLVED** — salience-based gating in perceptiond v1.3 |
| 2 | No power budget defined | **v1.5 target set**: <1W continuous, 18h battery |
| 3 | No battery capacity target | **v1.5 target set**: 2× 2000 mAh Lipo, 18h+ |
| 4 | LFM2.5-VL-450M power uncharacterized | **v1.5 spike**: measure on GAP9 dev kit Month 1-2 |
| 5 | Concurrent service power stack not modeled | **v1.5 plan**: Nanomind cascade scheduling |
| **6 (NEW v38)** | **OpenClaw production failure modes** | **TOP v1 RISK** — DanClaw proxy v1 deliverable |
| 7 | Zero physical constraints defined | **v1.5 target set**: <80g, 30g frame + 30g batteries + 20g module |
| 8 | 128GB eMMC aspirational | **v1.5 target set**: 64GB eMMC, models downloaded on first run |
| 9 | 8GB RAM minimum may be unachievable | **v1.5 plan**: GAP9 8MB SRAM + 32MB PSRAM + LPDDR4 ext |
| 10 | OpenClaw crash recovery path missing | **RESOLVED** — DanClaw proxy |
| 11 | No GPU/NPU contract | **v1.5 plan**: GAP9 NE16 OR Alif B1 NPU |
| 12 | audiod PTT limits UX | Carry to v1.5 wake word |
| 13 | Memory provider promotion gates untestable | Carry (dglabs-eval solves it) |
| 14 | Package signing mechanism TBD | Carry (use sigstore + cosign) |
| 15 | Bootstrap wizard underspecified | Shipped (BootstrapWizard.tsx) |

**v38 prioritization: Risk #6 (OpenClaw reliability) is now #1. v1 must ship with DanClaw proxy.** The other critical risks are tracked, the v1.5 wearable phase addresses most of them with concrete plans.

---

## 11. What this means for the v1 deliverable checklist

**v1 (desktop prototype, ship Month 1):**
- [ ] DanClaw proxy v1 — crash suppression, health fanout, state mirroring, MCP allowlist (~500 LOC, ~1 week)
- [ ] `register_user_service` for all 7 daemons (5-min fix, 7th carry)
- [ ] memoryd v1 → v1.1: LFM2.5-Embedding-350M swap (data migration script, ~200 LOC)
- [ ] audiod v0.7 → v0.8: add PTT via evdev for Linux desktop + Space key (carried from v0.6)
- [ ] dglabs-eval v0.1: harness scaffolding (no tasks yet) for self-hosting

**v1.5 (wearable prototype, ship Month 3-6):**
- [ ] GAP9 dev kit + Brilliant Labs Halo purchase
- [ ] LFM2.5-VL-450M on GAP9 (measure power, latency)
- [ ] perceptiond v2: Nanomind-style cascade (light VFM + on-demand VLM)
- [ ] proactived v0.1: audiod VAD → memoryd retrieval → ttsd/telegram fan-out
- [ ] dglabs-eval v1: 5 demo + 5 proactive + 5 safety = 15 tasks, MIT-licensed
- [ ] .deb package with Tailscale Serve for loopback bypass
- [ ] Form factor: <80g, 18h battery target

**v2 (wearable GA, ship Month 6-12):**
- [ ] memoryd v2 v1.0: 6-core stack (LFM2.5-Embedding + Zep + Mem0 + SuperLocalMemory + Hindsight + VisualMem)
- [ ] dglabs-eval v1.5: 5 reasoning + 5 skills + 3 retrieval + 9 safety = 22 tasks
- [ ] SIA fork (SIA-H) with LFM2.5-1.2B-Thinking as Feedback-Agent
- [ ] Self-Harness dglabs-eval for on-device harness evolution

---

## 12. Open questions for somdipto

1. **Approve DanClaw proxy as v1 deliverable?** ~500 LOC, ~1 week, low risk.
2. **Approve GAP9 dev kit + Brilliant Labs Halo purchase in Month 1?** ~$650 total.
3. **Approve LFM2.5-Embedding-350M swap in memoryd v1.1?** 1024d vs 384d, 4× storage, Apache 2.0-eq license.
4. **Resolve HRM-Text 1B vs LFM2.5-1.2B-Thinking on-device reasoning?** workspace AGENTS.md says HRM-Text 1B; PRD says LFM2.5-1.2B-Thinking. dglabs-eval v1 can include a 5-task reasoning subset to settle this empirically.
5. **Approve dglabs-eval v1 proactive subset (5 tasks from ProActEval)?** Direct defensive counter to Snap Specs.

*End of v38 architecture review.*
