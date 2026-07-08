# Dan2 — Danlab AGI Roadmap (v33)
**Date:** 2026-06-20 06:30 UTC (12:00 IST)
**Status:** v33 — sharpened over v15
**Scope:** Where should Danlab focus over the next 6/12/24 months?
**Audience:** somdipto (decision-maker), Dan1/Dan3/Dan4 (peer architects)
**Companion:** `dan2-research-report.v33.md`, `dan2-architecture-review.v33.md`, `dan2-model-analysis.v33.md`, `dan2-papers-to-read.v33.md`

---

## The Bet (1 line)

**Ship the only local-first, open-weights, memory-first, auditable-harness, no-cloud AI companion + open agent standard before the 5+ closed-source wearable competitors lock the consumer narrative — and before the Anthropic-Mythos political precedent forces every non-US enterprise to scramble for an open alternative. memoryd v2 v1.0 in September 2026 is the single highest-ROI action.**

---

## Three Convictions

1. **The wearable window is 14-18 months wide and the consumer narrative is hardening.** Meta Ray-Ban Display ($799, Sept 30 2026), Snap Specs ($2,195 with AR display, AWE June 16), Google Gemini glasses (Fall 2026), Apple N50 (late 2027), Apple Watch + Siri AI (watchOS 27, 2026), Brilliant Labs Halo (open-source, ships July 2026), Monako Glass ($399, 48g, Aug 2026), AI AirPods delayed to 2027. Illinois HB4843 (June 19 2026) is the first state bill to ban smart-glasses driving. Meta NameTag scandal exposed dormant facial-recognition code in Meta AI (WIRED, June 16). Privacy is no longer a niche concern. **Open-weights + on-device + auditable harness is the only credible 2026-2027 wedge.**

2. **memoryd v2 v1.0 in September 2026 is the single highest-ROI investment for AGI direction AND the deployment deadline.** 6-core stack: Mnemosyne (98.9% Recall@All@5) + Mem0 + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output) + Weaviate Engram. Open-sourced. **Salesforce bought Fin for $3.6B (June 15) — a $3.6B vote that agents are now a platform category.** Memory is the moat layer. **The wearable is the body; memoryd v2 is the soul.**

3. **The self-improving tier graduated in the last 30 days.** SIA-H is no longer alone. Meta-Harness (Chelsea Finn group, TerminalBench-2 #1) proves harness search beats weight tuning in production. SEAGym gives us the eval harness. Socratic-SWE reached 50.4% on SWE-bench Verified in 3 self-evolution iterations. POISE autonomously discovered RL algorithms improving AIME25 pass@32 from 26.7% to 43.3%. SkillsVote, AEL, HERO, RefCon, GRAM, GraP-Mem all closed in the same window. **The credible path for danlab-multimodal is no longer "ship SIA-H in Month 1" — it is "ship a SkillOpt + SkillsVote + SIA-H + Meta-Harness + AEL stack in Month 1-3, with verifiable benchmark gains on the danlab-multimodal screenshot set."** **The Dan1/Dan2/Dan3/Dan4 skill documents become the harness. The model weights stay frozen. The verifier gates the writes.**

---

## The 24-Month Roadmap

| Window | What ships | Why it matters |
|---|---|---|
| **3 months (Sept 2026)** | **memoryd v2 v1.0 OPEN-SOURCE RELEASE** + SIA-H fork + Meta-Harness-inspired skill evolution + SkillOpt + SkillsVote | **Apple Siri AI on Apple Watch (watchOS 27) counter.** First open-source memory + auditable-harness stack for always-on agents. **The bet.** |
| **6 months (Dec 2026)** | **memoryd v2 v2.0** (11-component stack: + AEL + GRAM + HeLa-Mem + Decagon Proactive + VisualMem). **Form factor locked** (Halo vs Monako vs Redax vs Project Solara). | **Ship before Apple N50 in late 2027.** Memory depth + harness evolution is the differentiator. |
| **12 months (June 2027)** | **Wearable form factor shipped.** Sub-2W wearable validated. Open agent standard v1. | **First local-first always-on consumer wearable instance.** Counter to Apple Vision Pro M5 + N50 (late 2027). |
| **18-24 months (Q4 2027 - Q1 2028)** | **Apple Glasses N50 ship counter.** 100K+ MAU on desktop companion. **memoryd v2 v3.0** (HMO 3-tier + CraniMem + Memora + APEX-MEM). **Open agent standard v1 GA.** | **The local-first memory layer becomes the open-source standard.** |

---

## The 12-Month Plan

### Month 1 — Foundation + memoryd v2 + SIA-H + Meta-Harness (July 2026)

**Goals:**
- **Week 1 (immediate):** Read Meta-Harness + SIA + SEAGym + Socratic-SWE. **Begin SIA-H fork for `danlab-multimodal` (2-week experiment).** SEAGym-style eval harness for `danlab-multimodal`.
- **Week 1 (immediate):** **`register_user_service` for all 7 daemons** (openclaw-gateway + audiod + memoryd + perceptiond + ttsd + toold + os-toold). **5-min fix. Solves the recurring os-toold regression.**
- **Week 1 (immediate):** Read OpenGlass (arXiv 2606.07431) + BitNet b1.58 (arXiv 2504.12285 + HF model card 2026-06-13). **Buy GAP9 dev kit + Prophesee GENX320 + Snapdragon X Elite + Monako Glass silicon teardown.**
- **Week 1-2:** Spike Zamba2-VL-1.2B + Gemma 4 12B Q4_K_M in perceptiond (laptop prototype VLM lock).
- **Week 1-2:** Spike LFM2.5-Embedding-350M + LFM2.5-ColBERT-350M in memoryd v2.
- **Week 1-2:** Spike LFM2-Audio-1.5B in audiod + ttsd (end-to-end audio-language). If quality holds, **consolidate audiod + ttsd into audiolangd**.
- **Week 3-4:** Begin AEL + Meta-Harness + SkillsVote + SIA-H integration for `danlab-multimodal`.
- **Week 3-4:** Begin HeLa-Mem Hebbian distillation study in memoryd v2.
- **Week 3-4:** **memoryd v2 v1.0 design — 6-core stack, single-process with 3 internal modules (ingest / retrieve / consolidate).**
- **Reaffirm carry from Dan1 punchlist:** Push `danlab-multimodal` public, fix GitHub bio, record 60s demo, post origin story thread.

**Success criteria:**
- Meta-Harness design notes + harness-search spike in `danlab-multimodal`
- SIA-H forked and running first 3-cycle experiment
- SEAGym-style eval harness on `danlab-multimodal` screenshot set
- LFM2.5-Audio-1.5B spike result documented
- All 7 daemons supervised via `register_user_service`

### Month 2 — VLM Speedup + memoryd v2 Cognitive Consolidation (August 2026)

**Goals:**
- **VLMCache 1.4-3.8× + V5e-0 1.89× + ViSpec 3.22× + SFPruner 1.6-3× (ACM 2026 + OpenReview 2026)** in perceptiond. **Combined with BitNet b1.58 (live-verified 0.4 GB mem / 29 ms latency / 0.028 J energy / 9.2× lower than LLaMA 3.2 1B) = 50-150× total VLM energy reduction path.**
- **Gemma 4 QAT** variant spike (72% VRAM reduction, 26B-A4B in 15 GB).
- **AEL two-timescale evolution** in memoryd v2 (Thompson Sampling fast + LLM reflection slow, Sharpe +27%).
- **Mnemosyne spike** in memoryd v2 (98.9% Recall@All@5).
- **Salience CNN** spike in perceptiond (replace EMA + Haar cascade, biggest power lever for the wearable).
- **HMO 3-tier memory** in memoryd v2 (Primary Cache + Secondary + Archive with persona-driven promotion).
- **HeLa-Mem Hebbian distillation** in memoryd v2 (hub detection threshold + spreading activation).
- **Monako Glass silicon teardown** (Aug 2026 ship). The 48g form-factor reference arrives.

**Success criteria:**
- VLMCache-style visual caching integrated
- Salience CNN running at 5 FPS with <50 ms latency
- Mnemosyne + AEL + HMO + HeLa-Mem in memoryd v2 dev branch
- Monako Glass teardown analysis documented

### Month 3 — memoryd v2 v1.0 OPEN-SOURCE RELEASE + Apple Siri AI on Apple Watch GA counter (September 2026)

**Goals:**
- **memoryd v2 v1.0 OPEN-SOURCE RELEASE on GitHub public.** 6-core stack. **This is the single highest-ROI action in the entire 12-month plan.** Counter to Apple Watch + Siri AI (watchOS 27 GA, 2026).
- **SIA-H spike** (harness-only) in `danlab-multimodal`. Publish: harness updates are logged, weight updates deferred, benchmark gains on held-out screenshot set.
- **Apple Vision Pro M5 visionOS 27 "see what you see" pattern study** for perceptiond proactive loop. **The production reference.**
- **os-toold v2** GA with ACS + Agent 365 + OWASP AIUC-1 + OWASP Agentic AI Security Maturity Model v2.01 + Apple Core AI compliance. **Wedge against Microsoft Scout "addicted users" memo leak (June 4-9 2026).**
- **Brilliant Labs Halo integration or reference** (Halo ships July 2026 with LFM2-VL-450M).
- **Microsoft IQ (Work IQ GA June 16) integration** as context layer for memoryd v2.

**Success criteria:**
- memoryd v2 v1.0 GitHub repo public, 100+ stars in first week
- SIA-H spike published with benchmark evidence
- os-toold v2 ACS + Agent 365 + OWASP + Microsoft IQ compliant
- Apple Watch + Siri AI GA → our open-source memory layer is the alternative

### Months 4-6 — Production Scale + memoryd v2 v2.0 (October-December 2026)

**Goals:**
- **memoryd v2 v2.0** (11-component stack): Mnemosyne + Mem0 + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output) + Weaviate Engram + **AEL + GRAM + HeLa-Mem + Decagon Proactive + VisualMem**.
- **Microsoft Scout GA counter:** os-toold v2 + openclaw-gateway with the full compliance stack.
- **Hailo-15H dev kit + LFM2.5-VL-450M** measurement on the wearable silicon path. Sub-1.5W sustained at 4 FPS = wearable path locked.
- **GAP9 dev kit + Prophesee GENX320** OpenGlass path silicon measurement. 11.5h on 200mAh at 78.3ms end-to-end = sub-1W path validated.
- **Form factor decision tree** locked: 4 paths (Redax vs Monako Glass vs Brilliant Labs Halo vs Project Solara MDEP) → pick one and ship.
- **Cognee self-improving "cognify" pipeline** spike (graph+vector+relational hybrid, 14 retrieval modes).

**Success criteria:**
- memoryd v2 v2.0 shipped
- Form factor locked
- Sub-1.5W wearable path measured
- 1000+ stars on memoryd v2 GitHub

### Months 7-9 — Wearable Pilot + memoryd v2 v2.5 (January-March 2027)

**Goals:**
- **Wearable pilot program** (50-100 users) on the locked form factor.
- **memoryd v2 v2.5** with **Hindsight 4-lever consolidation** (World/Experience/Opinion/Observation, 91.4% LongMemEval) + **Apple Intelligence Extensions API** integration.
- **BitNet-VLM** spike (if it ships in 2027).
- **Hailo-15H + LFM2.5-VL-450M Q4_0** production deployment.
- **VisualMem** integration in perceptiond → memoryd v2 (uses LFM2.5-VL-450M bbox JSON output).
- **Open agent standard v1** draft (ACS + Agent 365 + OWASP + Microsoft IQ + Apple Core AI compliant).

**Success criteria:**
- 50-100 wearable pilot users
- 90% pilot user retention at 30 days
- memoryd v2 v2.5 shipped

### Months 10-12 — Production Wearable + Open Agent Standard v1 (April-June 2027)

**Goals:**
- **Production wearable** shipping at scale (10K+ units).
- **Open agent standard v1 GA** (the open-source compliance wedge).
- **memoryd v2 v2.5** with **A-MEM** + **Memora** + **APEX-MEM** + **CraniMem** (Bayesian-credible-region memory).
- **SIA-H** deployed in production (harness updates on user-isolated personal models).
- **100K+ MAU on desktop companion** (free app, optional glasses upgrade).

**Success criteria:**
- 10K+ wearable units shipped
- Open agent standard v1 GA
- memoryd v2 v2.5 shipped
- 100K+ MAU on desktop companion

---

## What NOT to do (anti-recommendations)

1. **Do not rewrite OpenClaw in Rust.** It is correct as TypeScript/Node. The compliance wedge is the differentiator, not the runtime.
2. **Do not call it "RL" until harness+weight modifications are open and auditable.** Stay with "pre-RL scaffold" or "auditable self-improving."
3. **Do not run weight updates in v1.** Meta-Harness proves harness search alone is enough for TerminalBench-2 #1. Save weight updates for v2.
4. **Do not service-ize memoryd v2 prematurely.** One process with 3 internal modules (ingest / retrieve / consolidate). Split only if profiling proves the bottleneck.
5. **Do not try to LoRA-tune the user's brain model in v1.** Context management > weight updates for personal AI.
6. **Do not pick a wearable silicon path without measuring it.** $150-500 in dev kits is the single most important investment in Month 1.
7. **Do not keep the canonical PRD as the source of truth.** Reconcile the PRD, the build plan, the analysis, and the work pads.
8. **Do not bet the wearable path on Snapdragon-class silicon.** It will draw 2-5W sustained. Sub-1W is a GAP9 + event camera (2026) or BitNet-VLM (2027) target.
9. **Do not put OpenClaw on the wearable.** Run it in the user's EigenCloud container (or laptop).
10. **Do not ship a 1-bit VLM.** BitNet b1.58 is text-only. The VLM path needs BitNet-VLM (2027 target) OR GAP9 RISC-V + event camera (OpenGlass pattern) for 2026 wearable.
11. **Do not ship a display on v1.** Snap Specs at $2,195 is the ceiling. v1 should be camera + voice only at $349-399. Display is v2.
12. **Do not bet on a closed-source wearable silicon.** The memory crisis (June 19) shows supply is the new constraint.

---

## Open questions for somdipto

1. **Target battery life for v1 wearable?** PRD says 4h; canonical says 6h. The OpenGlass reference is 11.5h on 200mAh. Need a number.
2. **Target weight for v1 wearable?** PRD says <50g target, <80g minimum. Monako Glass is 48g. Brilliant Labs Halo is 40g. Need a number.
3. **Target BOM for v1 wearable?** PRD says $99-149. Recommend **$349-399** (Halo/Monako class) given memory crisis. The desktop companion stays free.
4. **What is the v1 distribution model?** EigenCloud container vs. local-only vs. hybrid?
5. **Who is the v1 user?** Technical early adopter, productivity knowledge worker, accessibility-first?
6. **What is the v1 success metric?** "100K+ MAU on desktop companion" is 18 months out. What is the v1 demo-ready metric?
7. **What is the v1 ship date?** Wearable is late 2027. What is the desktop prototype ship date?
8. **Liquid AI partnership — yes or no by end of June?** LFM Open License v1.0 is Apache 2.0-equivalent.
9. **Memoryd v2 open-source timing — lock to September 2026?** Or shift if silicon measurements shift?
10. **Open-source the Dan Glasses desktop companion NOW, or wait for wearable?** Brilliant Labs Halo is open-source from day 1.
11. **Open-source the `danlab-multimodal` heuristic loop NOW** (relabeled as "auditable self-improving agent") or wait for SIA-H fork?
12. **Decagon DuetBench-style benchmark for Dan Glasses (Month 9-12).** First industry benchmark for self-improving agents is public. Beat the 93% bar?
13. **Apple Core AI extension for v1.5+ Mac companion app** (Xcode 27 distribution path)?
14. **Buy Monako Glass silicon teardown + GAP9 dev kit + Prophesee GENX320 + Microsoft Surface RTX Spark + Snapdragon X Elite** THIS WEEK?
15. **Sovereign-India silicon path?** MoU with IndiaAI Mission compute for wearable silicon validation?

---

## Risks register

| # | Risk | Severity | Mitigation |
|---|---|---|---|
| 1 | Canonical PRD is stale vs shipped reality | High | Reconcile in Month 1. Pick a track. |
| 2 | VLM power uncharacterized | Critical | Buy dev kits, measure in Week 1. |
| 3 | OpenClaw gateway has no watchdog | High | `register_user_service` 5-min fix. |
| 4 | LFM2.5-VL-450M not yet in production | Medium | Download script in perceptiond. Spike Week 2. |
| 5 | memoryd v1 too weak for prod | Medium | memoryd v2 v1.0 in Month 3. |
| 6 | Microsoft Scout "addicted users" leak opens compliance wedge | Low (opportunity) | os-toold v2 compliance in Month 3. |
| 7 | Anthropic Fable 5 / Mythos 5 suspension opens sovereign wedge | Low (opportunity) | Open-source memoryd v2 in Month 3. |
| 8 | Apple Watch + Siri AI (watchOS 27) GA counters "wearable=glasses" narrative | Medium | Counter with open memoryd v2 + open wearable reference. |
| 9 | Memory crisis raises wearable BOM | Medium | Lock BOM at $349-399 in Month 1. Desktop companion stays free. |
| 10 | BitNet b1.58 is text-only | Medium | Spike GAP9 + event camera. Or wait for BitNet-VLM 2027. |
| 11 | Form factor unknowns (weight, battery, dimensions) | High | Spike in Month 1. Define physical constraints. |
| 12 | memoryd v2 ships late → miss the Sept 2026 window | Critical | 12-16 weeks, 1 ML engineer, $0 compute. Start Week 1 of Month 1. |
| 13 | Meta NameTag scandal / Apple privacy narrative may harden against closed AI glasses | Low (opportunity) | Open-weights + auditable harness positioning. |
| 14 | EU CADA sovereign-tier regulations may require open-source compliance | Low (opportunity) | Open agent standard v1 in Month 3-6. |
| 15 | Salesforce / Fin $3.6B validates agent platform category | Low (opportunity) | memoryd v2 + os-toold v2 as the open-source compliance wedge. |

---

## TL;DR

**The bet is memoryd v2 v1.0 in September 2026.**

A 6-core open-source memory layer (Mnemosyne + Mem0 + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M bbox-prompt + Weaviate Engram) that ships before Apple Siri AI public GA on Apple Watch (watchOS 27) AND before Apple Glasses N50 (late 2027). It is the single highest-ROI investment for AGI direction AND the deployment deadline.

The 7+ front competitive landscape (Meta Ray-Ban Display, Snap Specs, Google Gemini glasses, Apple N50, Apple Watch + Siri AI, Brilliant Labs Halo, Monako Glass) is now validated by capital + product. Ship the wearable before Apple N50 in late 2027. Sub-1W wearable is a 2026 (GAP9 + event camera) or 2027 (BitNet-VLM) target.

The self-improving tier graduated in June 2026. Meta-Harness, SIA-H, SEAGym, Socratic-SWE, SkillsVote, AEL, HERO, RefCon all closed in the same window. The credible path is harness search + skill evolution + verifiers. **Weights stay frozen in v1.** Do not call it "RL" until harness+weight modifications are open and auditable.

The OpenClaw gateway is the right choice for the agent layer. Do not rewrite it in Rust. Stand up a `register_user_service` watchdog unit for it — this is a 5-minute fix.

Microsoft Scout "addicted users" memo leak + Anthropic "brake pedal" plea + EU CADA sovereign-tier + Vembu "globalisation is dead" = the compliance + sovereignty wedge is wide open. **Open-source is the only way to win it.**
