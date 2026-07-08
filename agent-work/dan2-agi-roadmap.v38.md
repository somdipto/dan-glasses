# Danlab AGI Roadmap — Dan2 v38 (2026-06-22 11:30 IST)

> **v38 thesis:** The roadmap is sharpened around **two pivots**: (1) **OpenClaw → DanClaw proxy + 5 daemons** as the v1 production stack, and (2) **memoryd v2 v1.0 in September 2026** as the strategic event (carried from v34-37, now with LFM2.5-Embedding-350M as the embedding model). The 6/12/24-month horizon is unchanged. The **hardware pivot** is now a 3-way decision (GAP9 / Qualcomm AR1 / Alif B1) deferred to end of Month 3, not "this week" as v37 said.

---

## TL;DR

| Horizon | Goal | Headline metric | v38 spec change |
|---------|------|-----------------|-----------------|
| **6 months (by Dec 2026)** | v1.0 desktop + DanClaw proxy + memoryd v1.1 with Liquid embeddings | 100% uptime, 7/7 daemons healthy, dglabs-eval v1 published | Embedding model swap |
| **12 months (by Jun 2027)** | v1.5 wearable (GAP9 or AR1), dglabs-eval v2.0, perceptiond v1.5 cascade | 18h battery, <1s/frame, ProActEval > 70% | Nanomind cascade |
| **24 months (by Jun 2028)** | v2.0 (memoryd v3 cognitive hierarchy + SIA-W weights), open-source moat | LongMemEval > 80%, SIA-fork reproducible | MemCog + DCPM stack |

---

## The two strategic pivots (v38)

### Pivot 1: OpenClaw → DanClaw proxy + 5 daemons

**What:** Add a thin (~500 LOC TypeScript) **DanClaw proxy** between the 5 wearable daemons and OpenClaw-gateway. Proxy hardens OpenClaw's failure surface (unhandled rejections, OOM, sessions_send rot) without replacing the agent runtime.

**Why now:** Upstream OpenClaw has documented production failure modes (#3715, #52725, #73861, #13463, #11952, #23441) that map 1:1 to the Dan Glasses critical path. `register_user_service` watchdog is necessary but not sufficient. **v1 ships with DanClaw proxy as the control plane.**

**Cost:** ~1 week of Dan1 + Dan2 + Dan4 time. ~$0 compute.

**Risk:** Low. Proxy is a passthrough, not a replacement.

### Pivot 2: memoryd v2 v1.0 → LFM2.5-Embedding-350M (Jun 18, 2026 release)

**What:** Swap `all-MiniLM-L6-v2` (384d, US-origin) → `LFM2.5-Embedding-350M` (1024d, Apache 2.0-eq, multilingual, 100+ languages).

**Why now:** Liquid AI released it 4 days ago. Sovereignty (US export-control risk on US-origin models is now structural, cf. Anthropic Fable 5 / Mythos 5 suspension Jun 12). Multilingual (India-first deployment). 1024d aligns with MemCog SOTA.

**Cost:** ~1 week of Dan4 time. Storage grows 4× (15MB → 60MB for 10k memories).

**Risk:** Low. Fallback path to all-MiniLM-L6-v2 stays in the API.

---

## Month-by-month roadmap (v38)

### Month 1 (Jul 2026): Foundation hardening

| Action | Owner | Deliverable |
|--------|-------|-------------|
| **DanClaw proxy v1** | Dan1 + Dan2 + Dan4 | ~500 LOC, deploys on :18790, health fanout + crash suppression + state mirror |
| **memoryd v1.1** | Dan4 | LFM2.5-Embedding-350M integration + migration script + schema migration |
| **SIA-H fork spike** | Dan2 | `pip install 'sia-agent[claude]'`, run `sia run --task danlab-demo --max_gen 3` on 3 demo screens, document results |
| **GAP9 dev kit + Brilliant Labs Halo purchase** | Dan3 | ~$650 total |
| **Liquid AI partnership spike** | somdipto | Email Liquid AI re: Halo integration + retrievers partnership |
| **dglabs-eval v0.5 (private)** | Dan2 | 5 demo + 5 proactive + 5 safety tasks; harness-only Self-Harness loop |

### Month 2 (Aug 2026): Wearable silicon + memoryd v2

| Action | Owner | Deliverable |
|--------|-------|-------------|
| **GAP9 dev kit setup** | Dan3 | OpenGlass reference port; LFM2.5-VL-450M GGUF on GAP9 (if feasible) |
| **Brilliant Labs Halo unboxing + reverse-engineer** | Dan3 | Compare Halo's LFM2-VL-450M integration to ours; document differences |
| **memoryd v2 v0.5** | Dan4 | Add MemCog-style navigable memory store; LoCoMo benchmark baseline |
| **perceptiond v1.4** | Dan3 | Salience-detector v2 with event-camera mode; structured-output prompts (negation-collapse mitigation) |
| **dglabs-eval v1.0 (public)** | Dan2 | 5 demo + 5 proactive + 5 safety + 5 memory = 20 tasks, MIT, on GitHub |
| **Telegram @danlab_bot on DanClaw proxy** | Dan1 | Verify zero message loss over 7 days |

### Month 3 (Sept 2026): memoryd v2 v1.0 GA + hardware pivot

| Action | Owner | Deliverable |
|--------|-------|-------------|
| **memoryd v2 v1.0 (GA)** | Dan4 | 6-core stack (Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M late-interaction reranker); LongMemEval > 70% |
| **Hardware pivot decision** | somdipto + Dan3 | Pick GAP9 / Snapdragon AR1 / Alif B1 for wearable prototype |
| **proactived v0.5 (spike)** | Dan2 | ProAct-pattern on top of audiod VAD + memoryd retrieval; 5 proactive tasks benchmark |
| **SIA-W fork (optional)** | Dan2 | If GPU budget allows, integrate weight-update path with dglabs-eval safety gate |
| **DanClaw proxy v1.0 (GA)** | Dan1 | All crash-suppression + state-mirror features; OOM watchdog; 99.9% uptime target |

### Months 4-6 (Oct-Dec 2026): v1.5 wearable + dglabs-eval v2.0

| Action | Owner | Deliverable |
|--------|-------|-------------|
| **Wearable prototype v0.5** | Dan3 + hardware partner | First 3D-printed frame, 1 sensor module (camera + mic), 2000 mAh battery, 18h endurance |
| **perceptiond v1.5** | Dan3 | LFM2.5-VL-450M + Nanomind-style cascade; sub-1W continuous, sub-1s/frame |
| **memoryd v2 v2.0** | Dan4 | 11-component stack (+ HeLa-Mem, AEL, vstash, Decagon Proactive, VisualMem) |
| **dglabs-eval v2.0** | Dan2 | + reasoning subset (5 tasks, HRM-Text vs LFM2.5-1.2B-Thinking) + skills subset (5 tasks, OpenSkill-derived) |
| **Open-source release** | Dan1 + Dan2 | `dan-glasses` (MIT), `memoryd` (Apache 2.0), `dglabs-eval` (MIT) on GitHub; Reddit + HN launch |

### Months 7-12 (Jan-Jun 2027): v1.0 wearable + open moat

| Action | Owner | Deliverable |
|--------|-------|-------------|
| **Wearable v1.0 (GA)** | Dan3 | <80g total, 18h battery, $349 BOM, open eval, no cloud required for raw camera/audio |
| **Sovereign-India distribution** | somdipto | JioBharat / Airtel partnership for India-first; IndiaAI Mission compute access |
| **ProActEval > 70%** | Dan2 | Proactive subset benchmark target met |
| **LongMemEval > 80%** | Dan4 | memoryd v2 v2.0 ceiling target met |
| **BitNet-VLM watch** | Dan2 | If ships, plan v2.0 wearable upgrade path |

### Months 13-24 (Jul 2027-Jun 2028): v2.0 cognitive hierarchy

| Action | Owner | Deliverable |
|--------|-------|-------------|
| **memoryd v3** | Dan4 | HMO 3-tier + CraniMem + Memora + APEX-MEM + Meta-Harness + TRACE; cognitive graph store |
| **SIA-W+H reproducible** | Dan2 | First open-source reproducible harness+weights self-improvement; SIA-fork GA |
| **perceptiond v2** | Dan3 | BitNet-VLM or 2-bit Liquid model; 50g wearable |
| **Sovereign-India silicon path** | somdipto | If MoU signed, GAP9 / India-designed RISC-V at scale |

---

## Open questions for somdipto (v38)

1. **Approve DanClaw proxy as v1 deliverable.** ~500 LOC, ~1 week, low risk.
2. **Approve GAP9 dev kit + Brilliant Labs Halo purchase in Month 1.** ~$650 total.
3. **Approve LFM2.5-Embedding-350M swap in memoryd v1.1.** 1024d vs 384d, 4× storage, Apache 2.0-eq license.
4. **Approve dglabs-eval v1.0 public release (MIT) in Sept 2026.** Strategic event, not just product launch.
5. **Approve Liquid AI partnership spike.** Email in Month 1.
6. **Resolve HRM-Text 1B vs LFM2.5-1.2B-Thinking on-device reasoning.** dglabs-eval v1 reasoning subset (5 tasks) settles this empirically.
7. **Approve 3-way hardware pivot decision by end of Month 3.** GAP9 / Snapdragon AR1 / Alif B1.
8. **Compute budget.** GPU-hours for SIA-W fork (optional) + dglabs-eval training. Estimate: ~220 GPU-hours. **Still #1 blocker.**

---

## v37 → v38 deltas

| Section | v37 | v38 |
|---------|-----|-----|
| Strategic event | memoryd v2 v1.0 in Sept 2026 | **Same, now with LFM2.5-Embedding-350M swap** |
| Architectural risk | Redax moving target | **OpenClaw reliability (mitigated by DanClaw proxy)** |
| Wedge | v37 said closed (Snap); out-eval | **Same — now with ProAct + MemCog + CogniFold research backing** |
| Hardware pivot | "this week" | **End of Month 3, after buying GAP9 + Halo** |
| Safety | dglabs-eval safety subset | **+ 3 prompt-injection + 1 Sentry-hijack task** |
| Embedding model | all-MiniLM-L6-v2 (open) | **LFM2.5-Embedding-350M (Apache 2.0-eq, 1024d, multilingual)** |
| Reranker | None | **LFM2.5-ColBERT-350M (v1.5)** |
| 24-month | Memoryd v3 | **+ SIA-W+H reproducible, BitNet-VLM watch** |

---

*Dan2 AGI roadmap, 2026-06-22 v38. Companion to dan2-research-report.v38.md, dan2-architecture-review.v38.md, dan2-model-analysis.v38.md, dan2-papers-to-read.v38.md.*
