# Dan2 — Danlab AGI Roadmap (v1 Final)
**Date:** 2026-06-14
**Status:** FINAL v1
**Scope:** Where should Danlab focus over the next 6/12/24 months?
**Audience:** somdipto (decision-maker), Dan1/Dan3/Dan4 (peer architects)

---

## The Bet (1 line)

**Ship the only local-first, open-source, memory-first, self-improving wearable agent stack before Apple Siri AI public GA (Sept 2026) and Microsoft Scout GA (Oct 2026). The wedge is open-source governance compliance + local-first privacy in a window where Microsoft Scout is cracked ("addicted users" leak, June 4–9 2026), Anthropic Fable 5 is closed (Mythos class, GA June 9 2026), and Apple Siri AI is 12 GB-gated (iPhone 17 8 GB misses the full feature set). memoryd v2 v1.0 in September 2026 is the single highest-ROI investment for AGI direction AND the deployment deadline.**

---

## Three Convictions

1. **The wearable window is 18–24 months wide and now validated by capital + product.** Microsoft Scout (Build 2026 June 2, "Autopilot" #1, OpenClaw in M365, Omar Shahine CVP), Anthropic Fable 5 (Mythos class GA, June 9 2026, 80.3% SWE-bench Pro, Stripe's 50 M-line migration in a day), Apple Siri AI (iOS 27 dev beta, public GA Sept 2026, 12 GB RAM gate), Brilliant Labs Halo (shipping July 2026, LFM2-VL on device), Monako Glass (Aug 2026, 48 g Linux, $399), OpenGlass (arXiv 2606.07431, GAP9 RISC-V + event camera, 11.5 h on 200 mAh). **5-front competitive landscape + concrete ship dates.** Ship the wearable before Apple N50 in late 2027.

2. **memoryd v2 v1.0 in September 2026 is the single highest-ROI investment for AGI direction.** 6-core stack. $0 of compute. 12–16 weeks for 1 ML engineer. Open-sourced. **The Anthropic Fable 5 + Decagon DuetBench + Recursive Superintelligence $650M + Microsoft Scout "Autopilot" + Microsoft SkillOpt + Anthropic SkillOpt events in the same 2-week window validate the bet.** Every meaningful self-improving system in 2026 has a memory layer that is the moat. **The wearable is the body; memoryd v2 is the soul.** Target LongMemEval: >70% (Hindsight 91.4% with scale is the ceiling; SuperLocalMemory V3.3 70.4% zero-LLM is the credible open-source target).

3. **Ship the only open-source self-improving agent stack** (SIA-H + memoryd v2 + openclaw-gateway with AHE + Self-Harness + HarnessForge + Anthropic SkillOpt + Microsoft SkillOpt + ACS + Agent 365 + OWASP v2.01 + Microsoft IQ + Apple Core AI compliance) **before Microsoft Scout GA (Oct 2026) AND before Apple Siri AI public GA (Sept 2026).** The Anthropic brake-pedal plea + Microsoft Scout "addicted users" memo leak (June 4–9 2026) = the regulatory + governance wedge is wide open. **Open-source is the only way to win it.** Microsoft SkillOpt (Build 2026 June 2 2026) and Anthropic SkillOpt (with Fable 5, June 9 2026) ship skill-document evolution as a first-class primitive. **Treat Dan1/Dan2/Dan3/Dan4 as trainable parameters.**

---

## The 24-Month Roadmap

| Window | What ships | Why it matters |
|---|---|---|
| **3 months (Sept 2026)** | **memoryd v2 v1.0 OPEN-SOURCE RELEASE** (6-core stack: Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output) + Weaviate Engram). SIA-H forked into `danlab-multimodal`. BitNet b1.58 spike in perceptiond. | **Apple Siri AI public GA counter.** First open-source memory layer for always-on agents. **The bet.** |
| **6 months (Dec 2026)** | **memoryd v2 v2.0** (11-component stack: + AEL + vstash + HeLa-Mem + Decagon Proactive + VisualMem). **Microsoft Scout GA counter** (os-toold v2 with ACS + Agent 365 + OWASP v2.01 + Microsoft IQ + Apple Core AI compliance). **Form factor locked** (Redax vs Monako Glass vs Halo vs Project Solara MDEP). Apple Core AI extension skeleton. | **Ship before Apple N50 in late 2027.** Compliance is the differentiator. |
| **12 months (June 2027)** | **Wearable form factor shipped.** BitNet b1.58 + Litespark + GAP9 RISC-V + event camera path concrete. **Sub-1 W wearable validated.** Open agent standard v1 (ACS + Agent 365 + OWASP + Microsoft IQ + Apple Core AI compliant). | **First local-first always-on consumer wearable instance.** Counter to Apple Vision Pro M5 + N50 (late 2027) and Microsoft Scout + Solara. |
| **18–24 months (Q4 2027 – Q1 2028)** | **Apple Glasses N50 ship counter.** 100 K+ MAU on desktop companion (Brilliant Labs Halo + Monako Glass + Project Solara as OEM distribution). **memoryd v2 v3.0** (3-tier: Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + CraniMem + Memora + APEX-MEM + AEL + Meta-Harness + TRACE + HeLa-Mem + HMO). **Open agent standard v1 GA.** | **The local-first Project Solara memory layer becomes the open-source standard.** |

---

## The 12-Month Plan

### Month 1 — Foundation + memoryd v2 + SIA-H + Open Standards (July 2026)

**Goals:**
- **Week 1 (immediate):** Read SIA (arXiv 2605.27276) + Harness Updating Is Not Harness Benefit (arXiv 2605.30621) + Mem0 (arXiv 2504.19413). **Begin SIA-H fork for `danlab-multimodal` (2-week experiment).** SIA live-verified: 1,594 stars, 179 forks, last push 2026-06-11. CLI: `pip install sia-agent` + `sia run` + `sia web`.
- **Week 1 (immediate):** **`register_user_service` for all 7 daemons** (openclaw-gateway + audiod + memoryd + perceptiond + ttsd + toold + os-toold). **5-min fix. Solves the recurring os-toold regression.**
- **Week 1 (immediate):** Read OpenGlass (arXiv 2606.07431) + BitNet b1.58 (arXiv 2504.12285 + HF model card 2026-06-13). **Buy GAP9 dev kit + Prophesee GENX320 + Snapdragon X Elite + Monako Glass silicon teardown.**
- **Week 1–2:** Replace SmolVLM-256M with **Gemma 4 12B Q4_K_M** in perceptiond (laptop prototype VLM lock).
- **Week 1–2:** Spike **Gemma 4 E4B vs LFM2.5-VL-450M Q4_0** in perceptiond (wearable VLM lock by end of Month 3).
- **Week 1–2:** **Anthropic SkillOpt + Microsoft SkillOpt** integration for Dan1/Dan2/Dan3/Dan4 skill document evolution. Treat as trainable parameters. **Both are now SOTA-validated as first-class primitives.**
- **Week 3–4:** Spike LFM2.5-Audio-1.5B in audiod + ttsd (end-to-end audio-language, Apache 2.0-equivalent). If quality holds, eliminates audiod + ttsd stack.
- **Week 3–4:** Begin AHE + Self-Harness + HarnessForge integration for openclaw-gateway.
- **Week 3–4:** Begin HeLa-Mem Hebbian distillation study in memoryd v2 (hub detection + spreading activation).
- **Week 3–4:** Microsoft IQ integration design (Work IQ GA June 16, 2026) as context layer for memoryd v2.
- **Week 3–4:** Apple AFM 3 Core Advanced NAND-MoE architecture study for memoryd v2 (NAND-backed memory + IFP per-channel pruning + per-prompt routing).
- **Week 3–4:** **memoryd v2 v1.0 design — 6-core stack, single-process with 3 internal modules (ingest / retrieve / consolidate). LFM2.5-VL-450M (bbox-prompt JSON output) as the ingestion endpoint.**
- **Reaffirm carry from Dan1 punchlist:** Push `danlab-multimodal` public, fix GitHub bio, record 60 s demo, post origin story thread.

**Success criteria:**
- SIA-H forked and running first 3-cycle experiment
- Gemma 4 12B Q4_K_M integrated in perceptiond
- LFM2.5-Audio-1.5B spike result documented
- Anthropic SkillOpt + Microsoft SkillOpt production-shipped for Dan skill evolution
- All 7 daemons supervised via `register_user_service`

### Month 2 — VLM Speedup + memoryd v2 Cognitive Consolidation + BitNet (August 2026)

**Goals:**
- **SpecVLM 2.5–2.9× + ViSpec 3.22× + EAGLE-2 3.05–4.26× + VLMCache 1.4–3.8× (ACM 2026)** in perceptiond. **Combined with BitNet b1.58 (live-verified 0.4 GB mem / 29 ms latency / 0.028 J energy / 9.2× lower than LLaMA 3.2 1B) = 50–150× total VLM energy reduction path.** **Caveat: BitNet b1.58 2B4T is text-only; the VLM path needs BitNet-VLM (2027 target) OR GAP9 RISC-V + event camera (OpenGlass pattern) for 2026 wearable.**
- **Gemma 4 QAT** variant spike (72% VRAM reduction, 26B-A4B in 15 GB).
- **vstash adaptive RRF** in memoryd v2 (IDF-weighted fusion, +21.4% NDCG@10 on ArguAna).
- **AEL two-timescale evolution** in memoryd v2 (Thompson Sampling fast + LLM reflection slow, Sharpe +27%).
- **Salience CNN** spike in perceptiond (replace EMA + Haar cascade, biggest power lever for the wearable).
- **HMO 3-tier memory** in memoryd v2 (Primary Cache + Secondary + Archive with persona-driven promotion).
- **HeLa-Mem Hebbian distillation** in memoryd v2 (hub detection threshold + spreading activation + dual-path retrieval).
- **Apple Core AI extension skeleton (Xcode 27).** Apple Intelligence Extensions API distribution path.
- **Monako Glass silicon teardown** (Aug 2026 ship). The 48 g form-factor reference arrives.

**Success criteria:**
- BitNet b1.58 integrated in perceptiond
- Salience CNN running at 5 FPS with <50 ms latency
- VLMCache-style visual caching integrated
- AEL + vstash + HMO + HeLa-Mem in memoryd v2 dev branch
- Monako Glass teardown analysis documented

### Month 3 — memoryd v2 v1.0 OPEN-SOURCE RELEASE + SIA-W+H spike + iOS 27 GA counter (September 2026)

**Goals:**
- **memoryd v2 v1.0 OPEN-SOURCE RELEASE on GitHub public.** 6-core stack. **This is the single highest-ROI action in the entire 12-month plan.** Wedge against Apple Siri AI public GA in Sept 2026 (and the 12 GB hardware gate).
- **SIA-W+H spike** (harness + weights). Build on SIA-H from Month 1–2. Target: LawBench 70.1% held-out, TriMul 14.02×. **Open-source the SIA-W+H fork for `danlab-multimodal`.** Per "Harness Updating Is Not Harness Benefit": train the 1.2 B focal model to load and follow its own harness artifacts. Don't use a 4.6 evolver.
- **PopuLoRA populations** (TrueSkill cross-eval) in `danlab-multimodal`.
- **Apple Vision Pro M5 visionOS 27 "see what you see" pattern study** for perceptiond proactive loop. **The production reference.**
- **HarnessForge joint harness+policy co-evolution** in openclaw-gateway.
- **Continuous Harness reset-free online refinement** in openclaw-gateway.
- **os-toold v2** GA with ACS + Agent 365 + MXC + OWASP AIUC-1 + OWASP Agentic AI Security Maturity Model v2.01 + Microsoft IQ + Apple Core AI compliance. **Wedge against Microsoft Scout "Autopilot" + "addicted users" memo leak (June 4–9 2026).** Microsoft Scout runs on OpenClaw (the same gateway we use), so we are explicitly building the open-source compliance wedge on top of the same runtime.
- **Brilliant Labs Halo integration or reference** (Halo ships July 2026 with LFM2-VL-450M).
- **Microsoft IQ (Work IQ GA June 16) integration** as context layer for memoryd v2.
- **Microsoft SkillOpt + Anthropic SkillOpt** for Dan skill document evolution (Dan1/Dan2/Dan3/Dan4 = trainable parameters).

**Success criteria:**
- memoryd v2 v1.0 GitHub repo public, 100+ stars in first week
- SIA-W+H spike published
- os-toold v2 ACS + Agent 365 + OWASP + Microsoft IQ compliant
- Apple Siri AI GA → our open-source memory layer is the alternative

### Months 4–6 — Production Scale + Microsoft Scout GA Counter + memoryd v2 v2.0 (October–December 2026)

**Goals:**
- **memoryd v2 v2.0** (11-component stack): Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output) + Weaviate Engram + **AEL + vstash + HeLa-Mem + Decagon Proactive + VisualMem**.
- **Microsoft Scout GA counter:** os-toold v2 + openclaw-gateway with the full compliance stack (ACS + Agent 365 + MXC + OWASP AIUC-1 + OWASP v2.01 + Microsoft IQ + Apple Core AI + Anthropic SkillOpt + Microsoft SkillOpt).
- **Hailo-15H dev kit + LFM2.5-VL-450M** measurement on the wearable silicon path. Sub-1.5 W sustained at 4 FPS = wearable path locked.
- **GAP9 dev kit + Prophesee GENX320** OpenGlass path silicon measurement. 11.5 h on 200 mAh at 78.3 ms end-to-end = sub-1 W path validated.
- **Form factor decision tree** locked: 4 paths (Redax vs Monako Glass vs Brilliant Labs Halo vs Project Solara MDEP) → pick one and ship.
- **TencentDB Agent Memory** OpenClaw plugin (May 2026, MIT) integration for the 4-tier progressive memory pipeline.
- **Cognee self-improving "cognify" pipeline** spike (graph+vector+relational hybrid, 14 retrieval modes, in production at Bayer/Knowunity).
- **Decagon Proactive Agents** pattern in perceptiond → memoryd v2 ("anticipate / remember / initiate" behavior, 93% DuetBench acceptance target).

**Success criteria:**
- memoryd v2 v2.0 shipped
- Form factor locked
- Sub-1.5 W wearable path measured
- 1000+ stars on memoryd v2 GitHub

### Months 7–9 — Wearable Pilot + memoryd v2 v2.5 (January–March 2027)

**Goals:**
- **Wearable pilot program** (50–100 users) on the locked form factor.
- **memoryd v2 v2.5** with **Hindsight 4-lever consolidation** (World/Experience/Opinion/Observation, 91.4% LongMemEval) + **Apple Intelligence Extensions API** integration.
- **BitNet-VLM** spike (if it ships in 2027).
- **BitNet b1.58 + Litespark 1.58-bit ternary** integration for the focal model on the wearable.
- **Hailo-15H + LFM2.5-VL-450M Q4_0** production deployment.
- **VisualMem** integration in perceptiond → memoryd v2 (uses LFM2.5-VL-450M bbox JSON output).
- **Open agent standard v1** draft (ACS + Agent 365 + OWASP + Microsoft IQ + Apple Core AI compliant).

**Success criteria:**
- 50–100 wearable pilot users
- 90% pilot user retention at 30 days
- memoryd v2 v2.5 shipped

### Months 10–12 — Production Wearable + Open Agent Standard v1 (April–June 2027)

**Goals:**
- **Production wearable** shipping at scale (10 K+ units).
- **Open agent standard v1 GA** (the open-source compliance wedge).
- **memoryd v2 v2.5** with **A-MEM** (Zettelkasten-style atomic memory notes) + **Memora** + **APEX-MEM** (skill memory) + **CraniMem** (Bayesian-credible-region memory).
- **SIA-W+H** deployed in production (harness + LoRA weight updates on user-isolated personal models).
- **100 K+ MAU on desktop companion** (free app, optional glasses upgrade).

**Success criteria:**
- 10 K+ wearable units shipped
- Open agent standard v1 GA
- memoryd v2 v2.5 shipped
- 100 K+ MAU on desktop companion

---

## The 24-Month Plan (locked)

| Window | What ships | Why it matters |
|---|---|---|
| **3 months (Sept 2026)** | memoryd v2 v1.0 OPEN-SOURCE RELEASE (6-core stack) + SIA-H fork | **Apple Siri AI public GA counter** |
| **6 months (Dec 2026)** | memoryd v2 v2.0 (11-component stack) + os-toold v2 compliance + form factor locked | **Microsoft Scout GA counter** |
| **12 months (June 2027)** | Production wearable + Open agent standard v1 + sub-1 W path validated | **First local-first always-on consumer wearable** |
| **18–24 months (Q4 2027 – Q1 2028)** | Apple Glasses N50 ship counter + memoryd v2 v3.0 + Open agent standard v1 GA | **The local-first memory layer becomes the open-source standard** |

---

## What NOT to do (anti-recommendations)

1. **Don't rewrite OpenClaw in Rust.** It is correct as TypeScript/Node. The compliance wedge is the differentiator, not the runtime.
2. **Don't call it "RL."** Stay with "pre-RL scaffold" or "self-improving." The semantic war on "RL" labels is real in 2026.
3. **Don't run weight updates in v1.** SIA shows the harness-only path is already +25% on legal, +12% on kernel speed. The "RL" label is earned when (a) harness updates are logged, (b) weight updates are auditable, and (c) both are independently reviewable.
4. **Don't service-ize memoryd v2 prematurely.** One process with 3 internal modules (ingest / retrieve / consolidate). Split only if profiling proves the bottleneck at 10 K+ memories / 10 K+ queries / day.
5. **Don't try to LoRA-tune the user's brain model in v1.** The failure modes are not debuggable. **Context management > weight updates** for personal AI.
6. **Don't pick a wearable silicon path without measuring it.** $150–500 in dev kits is the single most important investment in Month 1. Until we measure LFM2.5-VL-450M on a Hailo-10H or OpenGlass's GAP9 + event camera, we are speculating about the form factor.
7. **Don't keep the canonical PRD as the source of truth.** Reconcile the PRD, the build plan, the analysis, and the work pads. Either update the canonical doc to match reality, or flag the wearable ambition as a separate workstream.
8. **Don't bet the wearable path on Snapdragon-class silicon.** It will draw 2–5 W sustained. Sub-1 W is a GAP9 + event camera (2026) or BitNet-VLM (2027) target.
9. **Don't put OpenClaw on the wearable.** Run it in the user's EigenCloud container. The laptop version is fine because the laptop is AC-powered.
10. **Don't ship a 1-bit VLM.** BitNet b1.58 is text-only. The VLM path needs BitNet-VLM (2027 target) OR GAP9 RISC-V + event camera (OpenGlass pattern) for 2026 wearable.

---

## Open questions for somdipto

1. **What is the target battery life for v1 wearable?** PRD says 4 h; canonical says 6 h. The OpenGlass reference is 11.5 h on 200 mAh (very different power class). Need a number.
2. **What is the target weight for v1 wearable?** PRD says <50 g target, <80 g minimum. Monako Glass is 48 g. Brilliant Labs Halo is <50 g. Need a number.
3. **What is the target BOM for v1 wearable?** PRD says $99–149. That excludes the VLM accelerator. Hailo-10H M.2 is ~$50. Need a BOM.
4. **What is the v1 distribution model?** EigenCloud container (canonical) vs. local-only (no cloud) vs. hybrid? The decision shapes os-toold and memoryd's threat model.
5. **Who is the v1 user?** Technical early adopter, productivity knowledge worker, accessibility-first? The PRD says "all three." Pick one.
6. **What is the v1 success metric?** "100 K+ MAU on desktop companion" is 18 months out. What's the v1 demo-ready metric (Week 4)?
7. **What is the v1 ship date?** "Late 2027" is the wearable. What's the desktop prototype ship date?
8. **Do we open-source the danlab-multimodal heuristic loop now or wait for SIA-H fork?** PRD is unclear. Recommend open-source now with explicit "pre-RL scaffold" framing, then iterate.

---

## Risks register (final)

| # | Risk | Severity | Mitigation |
|---|---|---|---|
| 1 | Canonical PRD is stale; working implementation has diverged | High | Reconcile in Month 1. Pick a track. |
| 2 | VLM power uncharacterized | Critical | Buy dev kits, measure in Week 1. |
| 3 | OpenClaw gateway has no watchdog | High | `register_user_service` 5-min fix. |
| 4 | LFM2.5-VL-450M not yet in production | Medium | Download script in perceptiond. Spike Week 2. |
| 5 | memoryd v1 temporal index is too weak for prod | Medium | memoryd v2 v1.0 in Month 3. |
| 6 | Microsoft Scout "addicted users" leak opens compliance wedge | Low (opportunity) | os-toold v2 compliance in Month 3. |
| 7 | Anthropic Fable 5 GA is closed, not open-source | Low (opportunity) | Open-source memoryd v2 in Month 3. |
| 8 | Apple Siri AI GA 12 GB gate is the wedge | Low (opportunity) | Open-source memoryd v2 in Month 3. |
| 9 | Recursive Superintelligence $650M validates the RSI bet | Low (opportunity) | SIA-H fork in Month 1. |
| 10 | BitNet b1.58 is text-only | Medium | Spike GAP9 + event camera. Or wait for BitNet-VLM 2027. |
| 11 | Form factor unknowns (weight, battery, dimensions) | High | Spike in Month 1. Define physical constraints. |
| 12 | memoryd v2 ships late → miss the Sept 2026 window | Critical | 12–16 weeks, 1 ML engineer, $0 compute. Start Week 1 of Month 1. |

---

## TL;DR

**The bet is memoryd v2 v1.0 in September 2026.**

A 6-core open-source memory layer (Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M bbox-prompt + Weaviate Engram) that ships before Apple Siri AI public GA. It's the single highest-ROI investment for AGI direction AND the deployment deadline.

The 5-front competitive landscape is now validated by capital + product. Ship the wearable before Apple N50 in late 2027. Sub-1 W wearable is a 2026 (GAP9 + event camera) or 2027 (BitNet-VLM) target.

The "RL" label is industry-toxic in 2026. Stay with "pre-RL scaffold" or "self-improving." Do not call it "RL" until the harness+weight modification is open and auditable.

The OpenClaw gateway is the right choice for the agent layer. Don't rewrite it in Rust. Stand up a `register_user_service` watchdog unit for it — this is a 5-minute fix.

Microsoft Scout "addicted users" memo leak + Anthropic "brake pedal" plea = compliance wedge is wide open. Open-source is the only way to win it.
