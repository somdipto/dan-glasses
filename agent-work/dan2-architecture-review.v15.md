# DAN-2 Architecture Review — v14
**Date:** 2026-06-19 (companion to `dan2-research-report.md`)
**Scope:** Dan Glasses v1.0 daemon topology + wearable v2 power architecture + RSI integration points

---

## TL;DR

The v13 daemon topology (7 services + OpenClaw) is **structurally correct**. The blocker for v1.0 .deb is not architecture — it is **Mnemosyne swap**, **OpenClaw signed-skill infra**, **proactive service**, and a **documented power state machine**. Wearable v2 cannot ship without target wattage per component and an NPU plan.

---

## 1. Service decomposition — what works, what's missing

### Keep as-is (verified, 131/131 tests green)

| Service | Port | Owner | Status |
|---|---|---|---|
| audiod | 8090 + 8091 WS | DAN-2 | ✅ v0.5 |
| perceptiond | 8092 | DAN-3 | ✅ v6 |
| memoryd | 8741 | DAN-4 | ✅ v1 (will swap to Mnemosyne) |
| toold | 8742 | DAN-4 | ✅ v1 |
| ttsd | 8743 | DAN-4 | ✅ v1 |
| os-toold | 8744 | DAN-4 | ✅ v1 |
| zo-mcp-bridge | stdio MCP | DAN-1 | ✅ live |
| openclaw | 18789 | DAN-1 | ✅ live |

### Add for v1.0 (blockers)

| New service | Purpose | Effort | Owner |
|---|---|---|---|
| **proactived** | Initiates, doesn't just respond | 2 weeks | TBD (DAN-2 candidate) |
| **privacyd** | Sigstore Rekor attestation, Fable-5-safe compliance | 3 weeks | TBD |
| **reasond** | Planning layer (HRM-Text 1B integration in v1.5; placeholder for v1.0) | 6 weeks | TBD |

### Add for v1.5

| New service | Purpose |
|---|---|
| **fabled** | B2B compliance customer pipeline ($99 / $999) |
| **SIA-fork harness** | Harness + LoRA co-evolution on danlab traces |
| **distilled ProActor** | 1-2B proactive model |

---

## 2. v1.0 service-by-service review

### audiod — ship as-is

- 98/98 tests, live with whisper-cli at `/usr/local/bin/whisper-cli`, Silero VAD ONNX, base.en model, evdev PTT, WS publisher on 8091, HTTP control on 8090. **[audiod/SPEC.md](../Services/audiod/SPEC.md) v0.5 is the spec of record.**
- **Open work** (non-blocking): whisper binary hot-reload on `/reload`; bounded transcribe queue with drop-oldest; ALSA device hot-swap; UDP/WebRTC transport for phone-relay mode.
- **v1.1 plan:** benchmark Zamba2-Audio-1.5B and Stability Audio 3.0 small as collapse candidate (audiod + ttsd in one model). Don't ship until benchmark holds.

### perceptiond — ship as-is, bench Zamba2-VL

- 8/8 tests, live with LFM2.5-VL-450M Q4_0 (209MB) + mmproj-F16 (180MB) at `/home/workspace/danlab-multimodal/llama.cpp/build/bin/llama-mtmd-cli`. Salience-gated (motion OR face), watchful 5 FPS, MAX_QUEUE_DEPTH=2. **[perceptiond/SPEC.md](../Services/perceptiond/SPEC.md) v5 is the spec of record.**
- **Open work:** power draw on Redax aarch64 is uncharacterized. ~10-15s/frame on x86_64 CPU. Wearable v2 measurement plan needed.
- **v1.1 plan:** benchmark Zamba2-VL-1.2B (Zyphra) on perceptiond workloads. 10× TTFT claim is from Zyphra's own silicon — measure on ours before swapping. LFM2.5-VL-Extract (June 4 2026) for structured JSON output, useful for tool-calling from perception.

### memoryd — swap to Mnemosyne before v1.0 .deb

- Currently uses `sentence-transformers/all-MiniLM-L6-v2` (384-dim). Works, but Mnemosyne is the 2026 SOTA. **[memoryd/SPEC.md](../Services/memoryd/SPEC.md) v1 is the spec of record — must be revised.**
- **Plan:**
  1. `pip install mnemosyne-memory[openclaw]`
  2. Set `plugins.slots.memory = "memory-core"` in `/root/.openclaw/openclaw.json` (community gotcha — avoids OpenClaw auto-loading wrong memory plugin)
  3. Migrate `/memories` and `/query` endpoints to Mnemosyne API (drops-in; SQLite-backed)
  4. Evaluate LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M as the embedding layer (Liquid AI, June 18 2026, 4.4× smaller than MiniLM with higher retrieval quality)
  5. Validate ≥98% Recall@All@5 on the danlab-multimodal screenshot set (we have ground-truth LFM2.5 captions)
- **6-week workstream. Blocks v1.0 .deb.**

### toold + os-toold — ship as-is

- 33 tests total, sandboxed `/tmp/toold-sandbox`, 120s timeout, shell + python + exec_file. os-toold enforces path guard. **[toold/SPEC.md](../Services/toold/SPEC.md) is the spec of record.**
- **Open work:** per-user isolation (currently single-user dev mode), sysctl/seccomp hardening for production, audit log shipping to Loki.

### ttsd — ship as-is, watch KittenTTS licensing

- 6 tests, KittenTTS medium variant, expr-voice-2-m voice, 24kHz mono IEEE Float WAV, ~3.8s cold / <1s warm. **[ttsd/SPEC.md](../Services/ttsd/SPEC.md) is the spec of record.**
- **Open work:** confirm KittenTTS commercial-use license (the [README](../Services/ttsd/SPEC.md) flags this as unverified). If non-commercial, swap to F5-TTS or Piper-TTS for v1.0. The 218-309 KB WAV payload is fine for desktop; optimize for streaming on wearable v2.

### zo-mcp-bridge — ship as-is

- stdio MCP server shimming `https://api.zo.computer/zo/ask` for OpenClaw. Auth via `ZO_CLIENT_IDENTITY_TOKEN` env. Avoids the `mcporter` 405 problem.
- **Why it exists:** the Zo MCP endpoint at `https://api.zo.computer/mcp` returns 405 on mcporter's `tools/list`. Bridge is the production path.
- **Open work:** none — this is the working primitive.

### OpenClaw — harden before v1.0 .deb

- Live at `/usr/lib/node_modules/openclaw`, PID 72, port 18789. Telegram channel enabled, `dmPolicy=pairing`, `groupPolicy=allowlist`, streaming=partial. **[zopenclaw SKILL.md](../../Skills/zopenclaw/SKILL.md) is the install procedure.**
- **Required hardening (P0):**
  - `cosign` sign every danlab OpenClaw skill, commit signatures to Sigstore Rekor
  - Default-deny policy for unsigned skills
  - `plugins.slots.memory = "memory-core"` explicit pin
  - `systemd Restart=always` unit with `WatchdogSec=30`
  - Document in `docs/openclaw-signed-skill-policy.md`
- **Reason:** `cline@2.3.0` (June 2026) silently installed OpenClaw via npm. Skill supply-chain is now a real attack surface.

---

## 3. Memoryd → Mnemosyne swap (detailed plan)

This is the highest-leverage change in the v1.0 cycle.

### Step 1 (Day 1-2): install + validate

```bash
pip install mnemosyne-memory[openclaw]
# Update /root/.openclaw/openclaw.json
# plugins.slots.memory = "memory-core"
```

### Step 2 (Day 3-7): schema mapping

Current memoryd schema (per SPEC.md v1):
- `memories` table: id, type (episodic|semantic|procedural), content, embedding (384-dim BLOB), created_at, metadata (JSON)
- `conversations` table: id, role, content, embedding, timestamp, session_id

Mnemosyne schema:
- Single SQLite file, 6-layer framework, dual reasoning
- BEAM (ICLR 2026) and LongMemEval (ICLR 2025) optimized
- Hermes-first but framework-agnostic

### Step 3 (Day 8-14): API surface

Keep `memoryd.py`'s HTTP API stable (Tauri bridge depends on it). Internally rewrite to call Mnemosyne. Endpoints preserved:
- `GET /health`, `POST /memories`, `POST /conversations`, `GET /query`, `GET /memories`, `GET /memories/by-type/{type}`, `GET /memories/{id}`, `DELETE /memories/{id}`, `GET /stats`, `POST /v1/embeddings`

### Step 4 (Day 15-21): eval

Build a held-out test from the danlab-multimodal screenshot set. Ground truth = existing LFM2.5-VL-450M captions. Run Mnemosyne + bge-small-en-v1.5, measure Recall@All@5. **Target: ≥98%.**

### Step 5 (Day 22-28): LFM2.5-Embedding swap

If LFM2.5-Embedding-350M matches Mnemosyne quality with bge-small, swap. If not, keep bge-small.

### Step 6 (Day 29-42): production cutover

Co-deploy memoryd (old) + memoryd-mnemo (new) on different ports. Run shadow writes for 7 days. Compare queries on the live UI. Cut over. Deprecate old.

**Risk:** Mnemosyne is a 6-layer framework with "dual reasoning" — if our use cases are mostly simple episodic recall (which they are), we are paying complexity tax. **Mitigation:** use Mnemosyne in dense mode (default), ignore the framework layers we don't need.

---

## 4. Power state machine (the wearable v2 blocker)

The canonical analysis (April 2026) flagged this. As of June 19 2026, it is still undocumented.

### Proposed state machine (v2 spec candidate)

```
States:
  BOOT         → powers up, init services, ready in <5s
  IDLE         → camera off, mic low-power (1mA), wake-word detection only
  WATCHFUL     → camera 2 FPS, no VLM, motion + face detection only
  ACTIVE       → camera 5 FPS, VLM on salient frames, max queue depth 2
  BURST        → camera 10 FPS, VLM continuous (only on user PTT or proactive fire)
  THROTTLED    → dropped to Gemma 2B or LFM2-VL-300M (thermal/power cap hit)
  SLEEP        → camera off, mic off, wake on RTC + push from paired phone
  SHUTDOWN     → graceful, drain OpenClaw session, flush memoryd, persist
```

### Power budget (planning estimates, NOT measured)

| Component | IDLE | WATCHFUL | ACTIVE | BURST |
|---|---|---|---|---|
| Redax SoC (CPU only) | 0.3W | 0.8W | 1.5W | 2.0W |
| Camera (V4L2 + ISP) | 0W | 0.3W | 0.5W | 0.8W |
| LFM2.5-VL-450M Q4_0 (CPU) | 0W | 0W | 3-5W | 5-8W |
| Zamba2-VL-1.2B Q4 (NPU) | 0W | 0W | 1-2W | 2-3W |
| whisper.cpp base.en | 0.05W | 0.1W | 0.4W | 0.5W |
| KittenTTS base spike | 0W | 0W | 0W | 1-2W |
| OpenClaw + daemons | 0.3W | 0.4W | 0.5W | 0.6W |
| **Total (CPU VLM path)** | **0.65W** | **1.6W** | **6-8W** | **9-12W** |
| **Total (NPU VLM path)** | **0.65W** | **1.6W** | **3.5-5W** | **5-7W** |

### Battery math

- 2× 200mAh LiPo at 3.7V = 1.48Wh per cell = 2.96Wh total
- At 2W average (idle-dominant mix, CPU VLM): ~1.5h — unacceptable
- At 2W average (idle-dominant mix, NPU VLM): ~1.5h — same
- **Either we get bigger batteries or we hit <1W average**

### Form factor constraints (still undecided)

The canonical analysis flagged that **target weight, dimensions, temple/arm thickness, nose bridge fit, and display type are all undefined**. Without these, the v2 product spec is a software architecture, not a wearable product spec. **Hard ask:** somdipto to lock the form-factor envelope this month.

---

## 5. SIA integration architecture

Forks `hexo-ai/sia` (MIT). Replace the default Feedback-Agent with LFM2.5-1.2B-Thinking (open, MIT). Replace the default target agent with our task-specific agents.

### Component layout

```
┌──────────────────────────────────────────────────────────────────┐
│                       danlab-sia-fork                            │
│                                                                  │
│  ┌─────────────────┐     ┌─────────────────┐                     │
│  │  Meta-Agent     │ ──► │  Target Agent   │ ──► task execution │
│  │  (writes initial│     │  (SmolVLM-256M  │     on danlab-     │
│  │   harness from  │     │   for vision,   │     multimodal     │
│  │   task spec)    │     │   Whisper for   │     screenshot set │
│  │                 │     │   audio, etc.)  │                     │
│  └─────────────────┘     └────────┬────────┘                     │
│                                   │ trajectory                   │
│                                   ▼                              │
│                          ┌─────────────────┐                     │
│                          │  Feedback-Agent │                     │
│                          │  (LFM2.5-1.2B-  │                     │
│                          │   Thinking, MIT)│                     │
│                          │                 │                     │
│                          │  Decides:       │                     │
│                          │   - rewrite     │                     │
│                          │     harness?    │                     │
│                          │   - LoRA update?│                     │
│                          │   - both?       │                     │
│                          └────────┬────────┘                     │
│                                   │                              │
│                                   ▼                              │
│                          LoRA weights +                         │
│                          harness patches ──► Target Agent        │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Where it lives in Dan Glasses

- **`danlab-sia-fork` is a new service in the daemon set** (port 8760, internal-only).
- Subscribes to memoryd events + OpenClaw session store.
- Runs nightly on the day's worth of trajectories.
- LoRA updates committed to `/var/lib/danlab/lora/` and versioned in git.
- Harness rewrites committed as patches to `services/{target_agent}/`.

### Safety gates (REQUIRED before any LoRA update is loaded)

1. Held-out evaluation ≥ baseline + ε (ε = 0.5% on task benchmark).
2. Catastrophic-forgetting check on the canonical 100-pair seed set.
3. Replay-buffer integrity check (no duplicate / corrupted trajectories).
4. Human-in-the-loop approval for the first 10 updates.
5. After update 10: every 10th update requires approval; rest are auto-applied.

**Open question:** do we publish the LoRA updates publicly, or keep them private? Public = credibility for "open RSI" thesis. Private = IP protection. Recommendation: publish with a `danlab-lora-v{N}` tag and a 7-day public review window before auto-merge.

---

## 6. Critical risks (re-categorized for v14)

| Risk | Severity | Owner | Mitigation |
|---|---|---|---|
| Redax hardware slipping | High | somdipto | Pi 5 proxy benchmarks; lock form-factor envelope this month |
| Memoryd < Mnemosyne quality | Med | DAN-4 | 6-week swap, blocked only on schedule |
| OpenClaw skill malware | High | DAN-1 | Signed-skill infra before v1.0 .deb |
| "Pre-RL scaffold" claim drift | Med | somdipto | SIA-fork in v1.0; drop the "pre-RL" label by v1.5 |
| Fable 5 export-control disruption | Med | somdipto | "Fable 5 safe by construction" attestation in privacyd |
| Apple N50 quality bar (2027) | High | n/a | Compete on trust architecture, not form factor |
| Power budget unmeasured | High | somdipto + hardware partner | Pi 5 proxy benchmarks this quarter |
| Rust toolchain 1.63 < 1.74 | Low | somdipto | Bump rustc on container; doesn't block v1.0 frontend |
| Cline/OpenClaw npm supply-chain | High | DAN-1 | cosign+Rekor+default-deny |
| Illinois HB4843 spillover (12-24mo) | Low | somdipto | Driver-mode behavior in v2 |

---

## 7. What we should change RIGHT NOW (before v1.0 .deb)

1. `pip install mnemosyne-memory[openclaw]` + pin `plugins.slots.memory = "memory-core"`. **1 day.**
2. Open GitHub issue on `hexo-ai/sia` proposing co-fork collaboration. **1 day.**
3. Send LinkedIn DM to Vignesh Baskaran (Hexo Labs). **1 day.**
4. Update `models/download.sh` to fetch LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M. **1 day.**
5. Write `docs/openclaw-signed-skill-policy.md` (cosign + Rekor + default-deny). **3 days.**
6. Write `docs/fable-5-compliance-narrative.md`. **3 days.**
7. Write `docs/proactived-design.md` (the v1.0 cheap-proactive plan). **2 days.**
8. Add power-state-machine to `docs/dan-glasses-architecture-v2.md` (new section). **2 days.**

**Total: 2 engineer-weeks. All 8 items are pre-v1.0 .deb unblockers.**

---

## 8. What should NOT change in v1.0

- **Service topology** (7 daemons + OpenClaw). Production-grade, no reason to re-architect.
- **Tauri v2 + .deb + systemd.** Right call.
- **LFM2.5-VL-450M Q4_0 for desktop v1.0.** No swap until Zamba2-VL benchmarked.
- **whisper.cpp + KittenTTS.** Right until collapse candidate measured.
- **OpenClaw as sole orchestrator.** No dual-runtime.

---

*Half-life of useful architecture review is now ~6 hours. v14 reads in 90 seconds. v13 archived.*
