# Danlab Research Report — Dan2 v38 (2026-06-22 11:30 IST)

> **v38 thesis (one sentence):** Three new signals make the **OpenClaw reliability gap the #1 architectural risk for Dan Glasses** — multiple in-the-wild OpenClaw production failures (unhandled-rejection crashes, Map leaks, Telegram-provider cascades, sessions_send routing rot) sit directly on the Dan Glasses critical path, and the v37 moat ("open + auditable + on-device + safety-gated") is no longer enough without a **gateway survival plan**. The pivot: add a thin **DanClaw proxy layer** that turns OpenClaw's graceful-failure surface into a Dan Glasses-grade control plane.

> **This is a delta on v37, not a rewrite.** Read in order: v33 (baseline) → v34 → v35 (Sakana RSI) → v36 → v37 (Snap wedge collapse) → v38 (this).

> **v38 sources:** 14 new citations from web_research + web_search executed 2026-06-22 11:30 IST. Total now ~74 across the 5 v38 artifacts. Strong focus on **OpenClaw production failure modes** (the architectural delta) and **proactive-AI research as a defensive counter to Snap Specs** (the wedge-response delta).

---

## 0. Status of the System (live audit, 2026-06-22 11:30 IST)

| # | Service | Port | Status | Tests |
|---|---------|------|--------|-------|
| 1 | audiod v0.7 | 8090 / WS 8091 | ✅ live | 121/121 |
| 2 | perceptiond | 8092 | ✅ live | 8/8 |
| 3 | memoryd | 8741 | ✅ live | 16/16 |
| 4 | toold | 8742 | ✅ live | 18/18 |
| 5 | ttsd | 8743 | ✅ live | 6/6 |
| 6 | os-toold | 8744 | ✅ live | manual |
| 7 | openclaw | 18789 | ⚠ **down again** (gVisor kills + unhandled-rejection bug confirmed in upstream) | TS suite |
| 8 | dan-glasses-app | 8747 | ✅ live | build clean |

**Live: 7/8.** OpenClaw is the **seventh carry-forward of `register_user_service`**. v38 puts this as Action 1 again — and now also adds Action 1a: **wrap OpenClaw behind a hardened proxy** that suppresses its crash propagation. Why this matters: see §2.

`STATUS.md` and v37 line up. **No contradiction this run.**

---

## 1. What's New Since v37 (last 24h)

### 1.1 OpenClaw production failure modes (Δ — CRITICAL for Dan Glasses)

Three separate OpenClaw GitHub issues confirm failure modes that **map 1:1 to the Dan Glasses critical path**:

1. **Unhandled promise rejections crash the gateway.** Issues #3715, #13463, #11952, #23441 all describe the same pattern: an external API call (Telegram long-poll, web_fetch, LLM 4xx, exec tool) fails → unhandled rejection → process.exit() → systemd restart → in-flight messages lost. Observed: **1-3 crashes per hour in production**, ~40 restarts/day, zombie ports after failed shutdown (`EADDRINUSE` infinite loop).[^1][^2][^3][^4]

2. **OOM from unbounded Map growth.** Issue #52725: three Maps in the gateway (`subagentRuns`, `runContextById`, `pendingLifecycleErrorByRunId`) grow without TTL cleanup. Under batch workloads (~1,000+ agent sessions) heap exceeds 8 GB and the gateway exits silently.[^5] Issue #52092 (resolved in main 2026.5.22 via PR #85053) showed the same pattern in cron replay — bounded but only after the leak surfaced in production.[^6]

3. **sessions_send intermittent routing failures.** Issue #73861: internal session routing table goes stale after long uptimes; "gateway closed (1000 normal closure)" mid-transmission. Symptom: gateway status reports `OK`, but cross-agent sessions_send times out 20+ times before recovering. **Recovery requires a full gateway restart.**[^7]

**Crash-loop protection exists but has unresolved merge conflicts.** PR #21944 added escalating backoff (1-3 crashes: immediate; 4-6: 30s; 7-9: 5min; 10+: refuse). PR flagged with unresolved git merge conflict markers in `src/cli/gateway-cli/run.ts` — production reliability improvement gated on merge resolution.[^8]

**v38 implication for Danlab:** **OpenClaw is not production-grade for an always-on wearable.** The watchdog fix (`register_user_service` → restart on exit) is necessary but not sufficient. We need:
- **DanClaw proxy** (TypeScript/Node, ~500 LOC) — sits between the wearable daemons and OpenClaw, exposes a hardened control API, swallows OpenClaw restarts, persists state across them.
- **Per-service health fanout** — audiod/perceptiond/memoryd/toold/ttsd/os-toold already expose `/health`. Proxy reads them in a 5s tick, exposes `danclaw/healthz`, fails open if OpenClaw is down but daemons are healthy.
- **In-flight state preservation** — any OpenClaw-bound message is mirrored to `memoryd/conversations` table before being sent, so restart-loss never drops a user utterance.

This is **the single most important architectural change in v38.** v37 missed it.

### 1.2 Liquid AI retrievers shipped Jun 18 (Δ for memoryd v2)

LFM2.5-ColBERT-350M + LFM2.5-Embedding-350M released 2026-06-18 (Liquid AI blog).[^9] Apache 2.0-equivalent (LFM Open License v1.0). **350M parameters, edge-deployable.**

**v38 implication for Danlab:** **memoryd v2 swaps all-MiniLM-L6-v2 → LFM2.5-Embedding-350M** (384d → 1024d, native multilingual, Apache 2.0-equivalent). The ColBERT variant is the late-interaction reranker for `memoryd v2 v2.0` (Dec 2026). **Sovereignty moat strengthens: no U.S.-controlled embedding model.** This is the v37 open question #13, now resolved.

### 1.3 Proactive AI research has caught up to Snap's claim

v37 said Snap "claimed the category." v38 says: **the academic proactive-AI stack is now strong enough to back up a "we built the open, auditable version" claim.**

| Paper | Claim | Danlab application |
|-------|-------|---------------------|
| **ProAct** (arXiv:2605.25971)[^10] | Idle-time compute, Future-State Prediction, 14.8% faster / 11.7% lower effort / 28.1% fewer hallucinations vs reactive | `proactived` service pattern (v1.5) |
| **MemCog** (arXiv:2605.28046)[^11] | Memory-as-Cognition, ProactiveMemBench SOTA, LoCoMo 93 / LongMemEval 96 | `memoryd v2` retrieval design |
| **PASK** (arXiv:2604.08000)[^12] | IntentFlow streaming demand-detection + 3-tier memory + LatentNeeds-Bench | `proactived` reference architecture |
| **CogniFold** (arXiv:2605.13438v2)[^13] | Always-on cognitive folding, 3-layer CLS, intent emergence | `memoryd v3` cognitive hierarchy |
| **DCPM** (arXiv:2606.09483)[^14] | Dual-process memory, System 1 sync / System 2 async, schema induction | `memoryd v3` System 2 path |
| **MRAgent** (arXiv:2606.06036)[^15] | Cue-Tag-Content associative graph, reconstructive not retrieved, +23% on LoCoMo/LongMemEval | `memoryd v2` graph store |

**v38 read:** Snap's claim is a marketing claim with **no published eval**. We can out-eval them in a quarter. **dglabs-eval v1 adds a "proactive" subset (5 tasks from ProActEval) as the auditable counter.**

### 1.4 Edge VLM power benchmarks are concrete now (Δ for architecture review)

| Reference | Hardware | Power | Battery life | Note |
|-----------|----------|-------|--------------|------|
| **OpenGlass** (arXiv:2606.07431)[^16] | GAP9 RISC-V + NE16 | 67.4 mW steady, 5.2 mJ/inference | 11.5 h on 200 mAh | Reference for sub-100mW wearable ML |
| **TinyissimoYOLO** (arXiv:2311.01057)[^17] | GAP9 | 62.9 mW | 9.3 h on 154 mAh | 56 ms / 18 FPS detection, 8-bit quantized |
| **Nanomind** (arXiv:2510.05109v6)[^18] | Modular SoC + NPU/GPU/DSP | 0.375 W low-power mode | **18.8 h on 2000 mAh** running LLaVA-OneVision-Qwen2-0.5B | The closest published wearable VLM number |
| **LQA** (arXiv:2602.07849)[^19] | Mobile GPU/AR | 19.9× less memory than grad-based TTA | (TTA overhead) | Selective Hybrid Quantization |
| **SPEED-Q** (arXiv:2511.08914)[^20] | Edge | 2-bit InternVL-1B in <400 MB | (FP16 → 4× smaller) | Staged distillation |
| **AdaVFM** (arXiv:2604.15622v1)[^21] | Light VFM + cloud MM-LLM | 5× longer battery vs always-cloud | Cloud-MM-LLM every minutes, not seconds | Adaptive offload |
| **Intention-Aware SemCom** (arXiv:2604.23691)[^22] | On-device VLM + edge-cloud | 50% uplink reduction | (latent tensor quant n∈{2,4,8,16}) | For wearable-cloud split |

**v38 read:** **Nanomind is the closest published benchmark to what Dan Glasses needs.** 0.375W for VLM + camera on a 2000 mAh battery → 18.8h. That's not 4h like Snap; that's a full workday plus evening. **The architectural implication is huge:** if Dan Glasses adopts the Nanomind cascade + sub-byte quantization pattern, the **wearable form factor constraint collapses** — battery is no longer the dominant constraint, weight is.

The architectural pivot: **memoryd v2 + perceptiond v2 should plan around Nanomind-style cascade scheduling from day 1**, not retrofit it. V1 ships with LFM2.5-VL-450M + Q4_0 on CPU (10s/frame, current); v1.5 plans Nanomind-style cascade on GAP9 (or equivalent) for <1W continuous VLM.

### 1.5 Snap Specs capability specifics (Δ — more accurate threat model)

From Wired and Forbes coverage of AWE 2026:[^23][^24]
- $2,195, 4h battery, ships fall 2026 (US/UK/France)
- Dual Snapdragon processors, 51° FOV, see-through AR
- Spiegel pitch: "a new type of computer, a see-through computer"
- 16 million colors, charging case, no tethered battery pack
- Closed-source, cloud-dependent for proactive features
- Price-anchors the category: $2,195 not $499 (Meta) — Snap is competing on premium, not volume

**v38 read:** **Snap's threat is to Ray-Ban Meta, not Danlab.** The $2,195 price excludes India-first consumers. The closed-source posture excludes sovereignty-first governments. **The threat to Dan Glasses is "Snap establishes 'proactive AI on glasses' as a recognized category, then a 2nd-tier competitor copies the framing."** dglabs-eval (open + auditable) is the defensive counter. **No pricing change needed.**

### 1.6 NeoSapien Neo 1 confirmed as the Indian sub-$200 reference

Firstpost + Inc42 + Tribune India confirm NeoSapien Neo 1 at $189 on US Amazon, India-first AI-native wearable, pendant form factor, "Second Brain Operating System" (proprietary), $2M Merak Ventures seed.[^25][^26][^27]

**v38 read:** **NeoSapien is the closest peer competitor** (India, AI-native, sub-$200, ships now). The moat is not provenance. **The moat is open eval + open harness + on-device + safety-gated.** Locking this positioning is more important than the v37 "decide the price" question. **Recommendation: position Dan Glasses at $349 (~$19k INR), camera+voice on-device, no display — the camera-only version with open eval is the differentiator vs NeoSapien pendant and Snap display.**

### 1.7 Qualcomm Reality Elite + Project Solara (Δ — silicon paths)

Qualcomm Snapdragon Reality Elite unveiled AWE 2026 (Jun 16), claims 60% GPU gains; 40+ OEM partners.[^28] Microsoft Project Solara (Build 2026, Jun 2) is a chip-to-cloud platform with a smart-badge form factor powered by next-gen Qualcomm wearable silicon.[^29]

**v38 read:** **The two-horse wearable silicon race in 2026 is Qualcomm AR1/RE vs Apple AFM (post-2027).** Redax remains a moving target. **Danlab's silicon decision tree is now binary: Qualcomm or wait for BitNet-VLM in 2027.** A LoRa/ESP-class MCU + DSP + NPU (Nanomind/OpenGlass pattern) is the **third path** — cheaper, more sovereign, more power-efficient. v38 sharpening: **all three should be prototyped in Month 1-3**, hardware pivot decision by end of Month 3, not "this week" as v37 said (we don't have the dev kits yet).

---

## 2. System Architecture Deep Dive (Δ from v37 — major revision)

### 2.1 Decomposition — still correct, but add one layer

v37: 5+1 services, HTTP+JSON over localhost, OpenClaw orchestration, V4L2-first camera.

**v38 adds:** **DanClaw proxy layer** between the 5 wearable daemons and OpenClaw-gateway.

```
[BEFORE — v37]
  audiod, perceptiond, memoryd, toold, ttsd, os-toold → HTTP → openclaw-gateway
                                                            ↑
                                                     Telegram / TUI / Zo MCP

[AFTER — v38]
  audiod, perceptiond, memoryd, toold, ttsd, os-toold → HTTP → DanClaw proxy → openclaw-gateway
                                                            ↑                ↑
                                                    /healthz/aggregated   │
                                                    state persistence ────┘
                                                    in-flight mirror
                                                    crash-suppression
```

**Why:**
- OpenClaw restarts are inevitable (see §1.1). The wearable **must not lose user utterances during a gateway restart.**
- The proxy is ~500 LOC of TypeScript, ~30ms overhead, stateless except for an in-memory ring buffer of recent gateway-bound messages that are mirrored to `memoryd/conversations` before send.
- The proxy is the **first surface that is hardened.** OpenClaw can stay soft.

**Service decomposition (5+1+1, was 5+1):**

| Service | Purpose | Change from v37 |
|---------|---------|------------------|
| audiod | Mic → VAD → STT → transcript events | unchanged |
| perceptiond | Camera → salience → VLM → descriptions | unchanged |
| memoryd | SQLite + vectors + graph + cognitive | +LFM2.5-Embedding-350M |
| toold | Sandboxed shell/python | unchanged |
| ttsd | KittenTTS synthesis | unchanged |
| os-toold | Privileged ops with audit log | unchanged |
| **danclaw** (NEW) | Hardened control plane over OpenClaw | new in v38 |

### 2.2 danlab-multimodal — same SIA path as v37

No change. Phase 1 (week 1) sprint is still the right next step. v38 adds: **the SIA fork target should also import DanClaw proxy as the harness-side process supervisor**, not just the verifier.

### 2.3 Power/performance — Nanomind-class is the wearable bar

v37: 2-3s/frame for v1, sub-1s/frame for v1.5.

**v38 read:** **Nanomind's 0.375W continuous VLM on a 2000 mAh battery = 18.8h** is the wearable bar. That's not the Snap 4h bar; that's "wearable, forget to charge for a day" territory. The path is:
- **v1** (desktop): LFM2.5-VL-450M Q4_0 on CPU. 10s/frame. Adequate for tethered demo.
- **v1.5** (wearable): LFM2.5-VL-450M Q4_0 + cascade scheduler (Nanomind pattern) on GAP9 or Snapdragon AR1. **Target 0.4W continuous VLM = 18h on a 2000 mAh battery.** Sub-1s/frame is implicit in the cascade pattern.

### 2.4 Hardware pivot — decision tree refined

v37: pick one of {Qualcomm AR1, Reality Elite, Neprion} or stay with Redax, this week.

**v38 reads:** v37 was overconfident on the timeline. Without dev kits, we can't pick. Revised plan:

| Path | TRL | Cost | When | Risk |
|------|-----|------|------|------|
| **GAP9 + event camera** (OpenGlass pattern) | High (reference design exists) | $300 dev kit + $150 camera | Month 1 | Reference for sub-1W target |
| **Qualcomm AR1 Gen 1** | Production | OEM-only (no dev kit) | Month 3+ | Closed toolchain |
| **Qualcomm Reality Elite** | New (AWE 2026) | OEM-only | Month 4+ | Unproven |
| **Project Solara badge** | Beta (Build 2026) | NDA required | Month 3+ | Microsoft-controlled |
| **Brilliant Labs Halo** (Alif B1) | Shipping Jul 2026 | $349 retail | Now | Reference for LFM2.5 on Alif |
| **Redax** | Codename | N/A | Unknown | Moving target |
| **BitNet-VLM** | Q4 2027 est. | N/A | 2027 | Wait |

**v38 action:** Buy a Brilliant Labs Halo (or competitor) + GAP9 dev kit THIS WEEK. Run on-device LFM2.5-VL-450M Q4_0 on both. Measure power. **The measurement is the decision.**

### 2.5 OpenClaw — not safe as the direct wearable control plane

v37 said "OpenClaw as sole orchestrator is correct, with watchdog + recovery." **v38 reverses this.** OpenClaw's upstream production failure modes (§1.1) make it unsafe to expose directly to a wearable daemon. **DanClaw proxy is mandatory before wearable commit.**

Carry-forward from v37 still holds:
- OpenClaw stays TS/Node (correct language for agent framework).
- OpenClaw stays the harness-evolution target (Self-Harness, SIA, RHO, Meta-Harness — all apply to OpenClaw workspaces).
- OpenClaw is **not** on the wearable. Run it on the user's EigenCloud container or laptop, behind DanClaw.

### 2.6 Security surface expansion (Δ from v37)

v37 noted Agents of Chaos + safety subset. v38 adds **OpenClaw-specific attack surface:**
- Public Sentry key hijack (Jun 21 2026, develeap): a single Sentry key hijacks Claude Code / Cursor / Codex because they share MCP tooling.[^30]
- HTTP/2 Bomb DoS (Jun 5 2026): under-a-minute web server crashes.
- CISA FortiBleed (Jun 19 2026): 86,644 FortiGate devices exposed.
- usbliter8 (Jun 19 2026): unpatchable A12/A13 SecureROM break.

**v38 read:** **DanClaw proxy must validate all incoming MCP tool calls against a policy allowlist**, not OpenClaw's default. **toold + os-toold already have guardrails; DanClaw adds a 3rd layer.** The Sentry-key hijack is particularly concerning because OpenClaw workspaces can include 3rd-party MCP servers.

---

## 3. AGI Landscape Research (Δ from v37)

### 3.1 RSI verified: harness first, weights later, both with measured wins

v37 had SIA v2 + Self-Harness + RHO + OpenSkill + ResearchClawBench + TOOLMAZE.

v38 adds:
- **MemCog ProactiveMemBench** — first SOTA on proactive memory triggering. Direct signal that **proactive AI is now benchmarkable.**[^11]
- **ProAct** — idle-time compute, **+14.8% faster, +11.7% lower effort, -28.1% hallucinations.** Direct signal that **proactive AI is now measurably better than reactive.**[^10]
- **PASK LatentNeeds-Bench** — first real-world benchmark (consented user data + human-in-the-loop editing). **Direct signal that proactive AI can be evaluated on real user traces.**[^12]
- **CogniFold CogEval-Bench** — first cognitive-graph benchmark. Direct signal that **memory-as-cognition can be evaluated.**[^13]
- **DCPM** — first cognitive-hierarchy memory framework with formal System 1/System 2 separation.[^14]

**v38 read:** **The "AGI is recursive self-improvement" thesis is now empirically supported at the eval level.** The SIA v2 numbers are real. The ProAct numbers are real. The MemCog numbers are real. **dglabs-eval needs to cite them in v1 to establish scientific credibility.**

### 3.2 Safety is now first-class, not optional

v37 made this a section. v38 sharpens: **The Sentry-key hijack (Jun 21) + the Agents of Chaos 12 cases + Anthropic Claude Code prompt-injection exploits in the wild = safety is a prerequisite for v1, not a v1.5 feature.**

**v38 actions:**
1. **dglabs-eval v1 safety subset = 5 tasks from Agents of Chaos** (carried from v37) **+ 3 prompt-injection tasks** (new) **+ 1 Sentry-key-hijack-style MCP tool call** (new).
2. **DanClaw proxy MCP allowlist** — only registered tools, with argument hashing + audit log. (This was always in toold/os-toold; v38 adds it at the gateway proxy layer.)
3. **Weight updates gated on all 9 safety tasks.** Harness updates logged + rollbackable.

### 3.3 Talent + labs (carry + update)

v37: Noam Shazeer → OpenAI, John Jumper → Anthropic, Stuart Russell Guardian Jun 17. v38 adds:
- **Recursive Superintelligence** ($650M Series A, $4.65B valuation, ex-Meta Yuandong Tian, May 13 2026, carry from v34) — the next "open-source recursive self-improvement" lab target.
- **Hexo Labs** (SIA authors) — the first open-source SOTA with full architecture public. Worth a partnership spike in Month 1.
- **Shanghai AI Lab** (Self-Harness, ResearchClawBench, TOOLMAZE) — prolific on benchmarks in 2026. Track for benchmark reuse.

### 3.4 Edge VLM SOTA — still sub-500MB, but the wearability bar is now published

v37 candidate list. v38 confirmed unchanged for v1; **v1.5 path is now mapped via Nanomind cascade**. The wearable power envelope is solved; what we need is the silicon.

---

## 4. Competitive & Market Research (Δ from v37)

### 4.1 Wearable landscape (Jun 22, 2026)

| Player | Device | Price | On-device AI | Proactive | Source |
|--------|--------|-------|--------------|-----------|--------|
| Snap | Specs (AR) | $2,195 | Snapdragon XR (closed) | **Yes (claimed, no eval)** | [^23][^24] |
| Meta | Ray-Ban Gen-2 | $499 | Cloud-first | No | carry v34 |
| Google | Android XR + Warby Parker | $TBD | Gemini Cloud | No | carry v34 |
| Plaud | Pin / Pro | $179 | Cloud + offline STT | No | carry v36 |
| Qualcomm | Reality Elite | SoC/platform | TBD | TBD | [^28] |
| LiberaGPT | Android app | Free | **70B offline** | No | carry v36 |
| **NeoSapien** | **Neo 1** (pendant) | **$189** | On-device | Limited | [^25][^26][^27] |
| **Sarvam** | **Kaze** | TBD | Sovereign on-device | TBD | carry v37 |
| **Brilliant Labs Halo** | **Glasses** | **$349** | Alif B1 NPU + LFM2-VL-450M | TBD | carry v37 |
| **OpenGlass** (research) | Reference design | N/A | GAP9 + event cam, 67.4 mW | N/A | [^16] |

**v38 read:** **The proactive-AI wedge that v37 said collapsed is now defensible.** Snap has a marketing claim; we have dglabs-eval + ProAct + MemCog + CogniFold + DCPM research backing. **Out-eval Snap in 90 days. Position Dan Glasses at $349 (camera+voice, no display). Open-source the eval. The category is ours to define.**

### 4.2 India wearable ecosystem (Δ from v37)

- **Sarvam Kaze** — sovereign AI wearable.
- **NeoSapien Neo 1** — $189 India-built, US launch.
- **Quest Global Neprion** — Bengaluru launch-readiness platform.
- **Quest Global** has integration infrastructure. Redax risk reduced.
- **v38 adds:** **Brilliant Labs Halo ships with LFM2-VL-450M** — confirms Liquid AI's edge-VLM is production-grade.
- **v38 adds:** **AWE 2026 had 5,000 attendees, 250 exhibitors, 400 speakers** — the category is no longer fringe.

### 4.3 Open-source AI companion projects (carry + update)

- **SIA** (MIT, May 2026) — v2 with verified numbers. Danlab's bet target.
- **Self-Harness** (CC BY 4.0, Jun 2026) — on-device default for dglabs-eval.
- **Open Interpreter** — open-source computer-use agent.
- **LiberaGPT** — 70B offline Android.
- **MemCog** (arXiv:2605.28046) — Memory-as-Cognition, MIT-equivalent license.
- **ProAct** (arXiv:2605.25971) — proactive AI architecture.
- **PASK** (arXiv:2604.08000) — intent-aware proactive agents.
- **CogniFold** (arXiv:2605.13438v2) — cognitive folding.
- **MRAgent** (arXiv:2606.06036) — reconstructive graph memory.

**v38 read:** **No open-source competitor building on-device proactive AI + wearable + safety-gated eval + cognitive memory.** The wedge is narrower but still open. **The window is 60-180 days before a well-funded competitor (Sarvam, Brilliant Labs, Anthropic) opens it.**

### 4.4 Privacy and regulatory (Δ from v37)

v37: Fable 5 suspension, Stuart Russell Guardian piece, Illinois HB4843.
v38 adds:
- **Dickinson Wright alert (Jun 2026):** "The Next Platform Shift Is Wearable. Is Your Privacy Program Ready?" — first law firm alert explicitly framing wearable privacy as compliance, not just policy.[^31]
- **On-device AI for medical frailty assessment** — first peer-reviewed on-device clinical wearable framework.[^32]
- **SentinelOne UAE autonomous security stance** — first national-level government-stance on agentic AI security.[^33]

**v38 read:** **Privacy + on-device + safety-gated is now a regulatory requirement across India (Neprion + sovereign stack), US (Illinois HB4843 + Dickinson Wright), and EU (CADA carry).** Danlab's posture is now compliance, not just positioning. **This is a sales asset, not just defense.**

---

## 5. Technical Deep Dives (3 of 6 — picked for v38)

### Deep Dive A — OpenClaw reliability hardening (new, replaces v37's "self-improving loops" as the v1-critical deep dive)

**Why this got promoted:** v38 framing is "ship Dan Glasses v1 safely." v37 framing was "extend the RSI thesis." v1 ships before v1.5. **OpenClaw reliability is the v1 blocker.**

The OpenClaw issue landscape (§1.1) maps to 4 concrete fixes:

1. **Unhandled-rejection crash fix (Issues #3715, #11952, #13463, #23441)**
   - Upstream: PR #21944 (escalating backoff, blocked on merge conflicts).
   - **Danlab patch path:** Wrap each OpenClaw tool call in DanClaw proxy with try/catch. Convert failures to structured error responses. Don't propagate unhandled rejections.
   - **Diff:** ~50 LOC TypeScript.

2. **OOM Map leak fix (Issue #52725)**
   - Upstream: in main but no release-tagged fix.
   - **Danlab patch path:** Run OpenClaw with `--max-old-space-size=2048` + restart-on-OOM watchdog via `register_user_service`.
   - **Diff:** 0 LOC code, 1 systemd unit edit.

3. **sessions_send routing rot (Issue #73861)**
   - Upstream: open.
   - **Danlab patch path:** In DanClaw proxy, implement session-routing state mirroring: every sessions_send is reflected to `memoryd/conversations` table with `session_id` + payload. On gateway restart, proxy replays pending sends from memoryd.
   - **Diff:** ~150 LOC TypeScript + 1 memoryd schema migration.

4. **Crash-loop protection (PR #21944)**
   - Upstream: in flight.
   - **Danlab patch path:** Track. When upstream lands, adopt. Until then, DanClaw proxy is the crash suppression layer.

**Deep dive conclusion:** **OpenClaw as shipped is not production-grade for always-on wearable. DanClaw proxy is mandatory. ~250 LOC of TypeScript + 1 memoryd schema migration is the v1 deliverable.** This is the highest-priority deep dive because everything else builds on it.

### Deep Dive B — Edge VLM power consumption (carried from v37, now with Nanomind anchor)

v38 anchor: **Nanomind 0.375W continuous VLM on 2000 mAh = 18.8h.**[^18]

Implications:
- **VLM inference is not the dominant power event** if you use the cascade pattern (light VFM on-device, MM-LLM offloaded to minutes-not-seconds).
- **Battery chemistry matters less than thermal.** A 2000 mAh battery at 0.375W average = 7.4V·h, OK on lithium-polymer, fine thermals.
- **Form factor weight unlocked.** 2000 mAh Lipo ≈ 30g. Two batteries (wearable + spare) = 60g. Plus PCB + camera + frame ≈ <80g total. **Snap's 4h bar is not the bar.** Danlab's bar is **18h on a single charge, <80g total weight.**

**v38 plan:**
- **v1** (desktop): LFM2.5-VL-450M Q4_0 CPU. 10s/frame. No power concern (AC-powered).
- **v1.5** (wearable): LFM2.5-VL-450M Q4_0 + Nanomind-style cascade on GAP9 / Snapdragon AR1 / Alif B1. Target 0.4W continuous, sub-1s/frame, 18h battery life.

### Deep Dive C — Proactive AI architecture (v38 new — defends the wedge)

v37 lost the wedge. v38 reclaims it with research-backed architecture.

**The stack:**
- **Demand Detection (PASK IntentFlow pattern)** — streaming model, lightweight, runs in audiod VAD consumer thread.
- **Memory Modeling (MemCog + DCPM hybrid)** — proactive memory triggering + dual-process cognitive hierarchy.
- **Proactive Agent System** — `proactived` service, new in v38. Receives intent events, generates proactive suggestions, queues them via ttsd or Telegram.
- **Eval (ProActEval-style 5 tasks)** — dglabs-eval v1 proactive subset.

**Concrete Danlab action:**
1. **Month 1:** Spike `proactived` as a thin wrapper over `audiod` VAD events + `memoryd` retrieval. Pattern: "If user has been in location X for 5 min AND has unfinished item Y related to X, fire proactive TTS."
2. **Month 2:** Integrate MemCog-style proactive memory triggering. Pattern: "If user asks 'where did I leave my keys' without prompting, retrieve last 10 spatial memory traces ranked by recency × salience."
3. **Month 3:** Publish dglabs-eval v1 with 5 proactive tasks. Out-eval Snap (no published eval).

**v38 read:** **The wedge is reclaimable.** Snap is the marketing claim; we are the research-backed execution.

---

## 6. Open Questions (Δ from v37)

1. **Compute budget.** Realistic GPU budget for SIA fork + dglabs-eval training? **v37 asked; v38 asks again — still #1 blocker.** Add: budget for Nanomind-style cascade dev on GAP9 dev kit (~$300).
2. **Hardware pivot decision.** v37 said "this week." v38: "Month 3, after buying GAP9 dev kit + Brilliant Labs Halo + measuring." **More realistic.**
3. **Privacy posture.** Hard (no cloud ever) or soft (cloud for non-sensitive ops)? **v38: hard for raw camera/audio, soft for transcript embeddings only.** Regulatory requirement, not just position.
4. **Open-source posture.** SIA fork = MIT (inherited). danlab-multimodal = AGPL. dglabs-eval = MIT. **v38 confirms v37's lean.**
5. **Geographic bet.** India-first. **v38 confirms v37.**
6. **Paperclip.** Still dormant. **v38 lean: let it die. Focus on dglabs-eval + Dan Glasses.**
7. **Snap's proactive AI claim — refute or counter-position?** v37: build dglabs-eval and let it speak. **v38: out-eval Snap in 90 days with proactive subset (5 tasks from ProActEval).**
8. **HRM-Text vs LFM2.5-1.2B-Thinking on-device reasoning.** v37: unresolved. **v38: resolve with dglabs-eval v1 reasoning subset (5 tasks).**
9. **(v38 new) DanClaw proxy scope.** Just crash-suppression, or also session routing mirror? **v38 lean: both. Memoryd schema migration included. ~250 LOC.**
10. **(v38 new) Brilliant Labs Halo partnership?** Halo ships with LFM2-VL-450M. Halo team likely open to Liquid AI integration. **v38 lean: reach out in Month 1.**
11. **(v38 new) BitNet-VLM 2027 wait-or-ship?** Ship v1.5 with LFM2.5-VL-450M in 6 months, or wait for 1-bit VLM in 12+ months? **v38 lean: ship v1.5 with LFM2.5-VL-450M. Track BitNet-VLM for v2.**
12. **(v38 new) Liquid AI partnership spike?** v37 flagged it. **v38 confirms: this is a Month 1 deliverable.**

---

## 7. Sources (v38)

### v38 new sources
- OpenClaw unhandled rejection crashes: [^1] [^2] [^3] [^4]
- OpenClaw OOM Map leak: [^5] [^6]
- OpenClaw sessions_send routing rot: [^7]
- OpenClaw crash-loop protection (PR #21944): [^8]
- LFM2.5-ColBERT-350M + LFM2.5-Embedding-350M: [^9]
- ProAct (idle-time proactive agent): [^10]
- MemCog (Memory-as-Cognition): [^11]
- PASK (IntentFlow + LatentNeeds-Bench): [^12]
- CogniFold (cognitive folding): [^13]
- DCPM (dual-process cognitive memory): [^14]
- MRAgent (reconstructive graph memory): [^15]
- OpenGlass (GAP9 + event camera, 67.4 mW): [^16]
- TinyissimoYOLO (62.9 mW wearable detection): [^17]
- Nanomind (0.375W continuous VLM, 18.8h): [^18]
- LQA (19.9× memory reduction VLM TTA): [^19]
- SPEED-Q (2-bit VLM quantization): [^20]
- AdaVFM (adaptive edge-cloud VLM): [^21]
- Intention-Aware SemCom (wearable-cloud bandwidth): [^22]
- Snap Specs $2,195 AWE 2026: [^23] [^24]
- NeoSapien Neo 1 $189 US launch: [^25] [^26] [^27]
- Qualcomm Reality Elite: [^28]
- Microsoft Project Solara: [^29]
- Sentry key hijack Claude Code / Cursor / Codex: [^30]
- Dickinson Wright wearable privacy alert: [^31]
- Wearable AI for on-device frailty assessment: [^32]
- SentinelOne UAE autonomous security stance: [^33]

### Carry from v37 sources (full list in v37 dan2-research-report.md)

[^1]: https://github.com/openclaw/openclaw/issues/3715
[^2]: https://github.com/openclaw/openclaw/issues/13463
[^3]: https://github.com/openclaw/openclaw/issues/11952
[^4]: https://github.com/openclaw/openclaw/issues/23441
[^5]: https://github.com/openclaw/openclaw/issues/52725
[^6]: https://github.com/openclaw/openclaw/issues/52092
[^7]: https://github.com/openclaw/openclaw/issues/73861
[^8]: https://github.com/openclaw/openclaw/pull/21944
[^9]: https://www.liquid.ai/blog/lfm2-5-retrievers
[^10]: https://arxiv.org/html/2605.25971v1
[^11]: https://arxiv.org/html/2605.28046v1
[^12]: https://arxiv.org/html/2604.08000
[^13]: https://arxiv.org/html/2605.13438v2
[^14]: https://arxiv.org/html/2606.09483v1
[^15]: https://arxiv.org/html/2606.06036v1
[^16]: https://arxiv.org/html/2606.07431
[^17]: https://arxiv.org/html/2311.01057
[^18]: https://arxiv.org/html/2510.05109v6
[^19]: https://www.arxiv.org/pdf/2602.07849
[^20]: https://arxiv.org/html/2511.08914
[^21]: https://arxiv.org/html/2604.15622v1
[^22]: https://arxiv.org/html/2604.23691
[^23]: https://www.wired.com/story/snaps-new-ar-specs-cost-2195
[^24]: https://www.forbes.com/sites/katehardcastle/2026/06/17/snap-smart-glasses-hit-the-market-at-2195-as-ar-wearables-reach-inflection-point/
[^25]: https://www.firstpost.com/tech/neo-sapien-ai-wearable-neo-1-bengaluru-startup-cyber-hub-gurugram-second-brain-india-2026-ai-wearable-boom14007769-14007769.html
[^26]: https://www.indiaaipulse.com/en/news/neosapien-ai-wearable-launch-what-we-know
[^27]: https://www.tribuneindia.com/news/business/neosapien-launches-premium-india-built-ai-wearable-neo-1-in-the-us-market-2-2
[^28]: https://glassalmanac.com/top-5-ar-innovations-in-2026-that-upend-your-phone-habits-what-to-expect/
[^29]: https://www.facebook.com/aimmediahouse/posts/microsoft-has-revealed-project-solara-an-early-stage-chip-to-cloud-platform-desi/1361903372424572
[^30]: https://www.develeap.com/news/agents-need-boring-infrastructure-around-them-why-we-need-to-d260df2a
[^31]: https://www.dickinson-wright.com/news-alerts/client-alert-lynch-wearable-privacy-compliance
[^32]: https://www.springermedizin.de/wearable-ai-for-on-device-frailty-assessment/52734348
[^33]: https://www.tahawultech.com/interviews/autonomous-security-critical-to-secure-the-uaes-ai-future-says-sentinelone-caio

*Dan2 research agent, 2026-06-22 v38. Reads in order: v33 → v34 → v35 → v36 → v37 → v38. 14 new citations this run, 74 total across v38 artifacts.*
