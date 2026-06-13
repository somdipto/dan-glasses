# Dan2 — Danlab AGI Roadmap (v42 Final)
**2026-06-13 08:40 IST (03:10 UTC) · 7/7 daemons live re-verified · 12-month plan with locked focal models, locked memoryd v2 architecture, locked 4-path form-factor decision window, 90-day window to ship before Apple Siri AI public GA (Sept 2026) · Live re-verification of SIA architecture (3 LLMs not 2), Harness Updating Is Not Harness Benefit, Microsoft Scout "Autopilot" announcement (Omar Shahine CVP, Microsoft 365 Blog June 2 2026), Apple Siri AI 12GB hardware gate, BitNet b1.58 2B4T model-card numbers (0.4GB mem / 29ms latency / 0.028J energy / 9.2× lower than LLaMA 3.2 1B), LFM2.5-VL-450M (bbox-prompt JSON output, function calling, 765,623 HF downloads)**

## The Bet (v42, 1 line)

**Ship the only local-first, open-source, memory-first, self-improving wearable agent stack on a <50g glasses form factor before Apple Siri AI public GA (Sept 2026) and before Microsoft Scout GA (Oct 2026). The wedge is open-source governance compliance + local-first privacy in a window where Microsoft Scout is cracked ("addicted users" leak, June 4-9 2026), Anthropic Fable 5 is closed (Mythos class, GA June 9 2026), and Apple Siri AI is 12GB-gated (iPhone 17 8GB misses the full feature set). memoryd v2 v1.0 in September 2026 is the single highest-ROI investment for AGI direction AND the deployment deadline.**

## The 24-Month Bet (v42, locked)

| Window | What ships | Why it matters |
|---|---|---|
| **3 months (Sept 2026)** | **memoryd v2 v1.0 OPEN-SOURCE RELEASE** (6-core stack: Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output) + Weaviate Engram). SIA-H forked into danlab-multimodal. BitNet b1.58 spike in perceptiond. | **Apple Siri AI public GA counter.** First open-source memory layer for always-on agents. The bet. |
| **6 months (Dec 2026)** | **memoryd v2 v2.0** (11-component stack: + AEL + vstash + HeLa-Mem + Decagon Proactive + VisualMem). **Microsoft Scout GA counter** (os-toold v2 with ACS + Agent 365 + OWASP v2.01 + Microsoft IQ + Apple Core AI compliance). **Form factor locked** (Redax vs Monako Glass vs Halo vs Project Solara MDEP). Apple Core AI extension skeleton. | **Ship before Apple N50 in late 2027.** Compliance is the differentiator. |
| **12 months (June 2027)** | **Wearable form factor shipped.** BitNet b1.58 + Litespark + GAP9 RISC-V + event camera path concrete. **Sub-1W wearable validated.** Open agent standard v1 (ACS + Agent 365 + OWASP + Microsoft IQ + Apple Core AI compliant). | **First local-first always-on consumer wearable instance.** Counter to Apple Vision Pro M5 + N50 (late 2027) and Microsoft Scout + Solara. |
| **18-24 months (Q4 2027 - Q1 2028)** | **Apple Glasses N50 ship counter.** 100K+ MAU on desktop companion (Brilliant Labs Halo + Monako Glass + Project Solara as OEM distribution). **memoryd v2 v3.0** (3-tier: Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + CraniMem + Memora + APEX-MEM + AEL + Meta-Harness + TRACE + HeLa-Mem + HMO). **Open agent standard v1 GA.** | **The local-first Project Solara memory layer becomes the open-source standard.** |

## The Three Convictions (v42)

1. **The wearable window is 18-24 months wide and now validated by capital + product.** Microsoft Scout (Build 2026 June 2, "Autopilot" #1, OpenClaw in M365, Omar Shahine CVP), Anthropic Fable 5 (Mythos class GA, June 9 2026, 80.3% SWE-bench Pro, Stripe's 50M-line migration in a day), Apple Siri AI (iOS 27 dev beta, public GA Sept 2026, **12GB RAM gate**), Brilliant Labs Halo (shipped, LFM2-VL on device), Monako Glass (Aug 2026, 48g Linux, $399), OpenGlass (arXiv 2606.07431, GAP9 RISC-V + event camera, 11.5h on 200mAh). **5-front competitive landscape + concrete ship dates.** Ship the wearable before Apple N50 in late 2027.

2. **memoryd v2 v1.0 in September 2026 is the single highest-ROI investment for AGI direction.** 6-core stack. $0 of compute. 12-16 weeks for 1 ML engineer. Open-sourced. **The Anthropic Fable 5 + Decagon DuetBench + Recursive Superintelligence $650M + Microsoft Scout "Autopilot" + Microsoft SkillOpt + Anthropic SkillOpt events in the same 2-week window validate the bet.** Every meaningful self-improving system in 2026 has a memory layer that is the moat. **The wearable is the body; memoryd v2 is the soul.** Target LongMemEval: >70% (Hindsight 91.4% with scale is the ceiling; SuperLocalMemory V3.3 70.4% zero-LLM is the credible open-source target). **v42 live-state baseline: v1 is functional (id:1 score 0.5357 verified this run). v2 builds on top, not from scratch.**

3. **Ship the only open-source self-improving agent stack** (SIA-H + memoryd v2 + openclaw-gateway with AHE + Self-Harness + HarnessForge + Anthropic SkillOpt + Microsoft SkillOpt + ACS + Agent 365 + OWASP v2.01 + Microsoft IQ + Apple Core AI compliance) **before Microsoft Scout GA (October 2026) AND before Apple Siri AI public GA (Sept 2026).** The Anthropic brake-pedal plea + Microsoft Scout "addicted users" memo leak (June 4-9 2026) = the regulatory + governance wedge is wide open. **Open-source is the only way to win it.** **v42 sharpening: Microsoft SkillOpt (Build 2026 June 2 2026) and Anthropic SkillOpt (with Fable 5, June 9 2026) ship skill-document evolution as a first-class primitive. Our P1-39 (treat Dan1/Dan2/Dan3/Dan4 as trainable parameters) is now aligned with the SOTA.**

## The 12-Month Plan (v42, locked)

### Month 1 — Foundation + memoryd v2 + SIA-H + Open Standards (July 2026)

**Goals:**
- **Week 1 (immediate):** Read SIA (arXiv 2605.27276) + Harness Updating Is Not Harness Benefit (arXiv 2605.30621) + Mem0 (arXiv 2504.19413). **Begin SIA-H fork for danlab-multimodal (2-week experiment).** **SIA live-verified: 1,594 stars, 179 forks, last push 2026-06-11. CLI: `pip install sia-agent` + `sia run` + `sia web`.**
- **Week 1 (immediate):** **`register_user_service` for all 7 daemons** (openclaw-gateway + audiod + memoryd + perceptiond + ttsd + toold + os-toold). **5-min fix. Solves the recurring os-toold regression (v20→v28→v29).**
- **Week 1 (immediate):** Read OpenGlass (arXiv 2606.07431) + BitNet b1.58 (arXiv 2504.12285 + HF model card 2026-06-13). **Buy GAP9 dev kit + Prophesee GENX320 + Snapdragon X Elite + Monako Glass silicon teardown.**
- **Week 1-2:** Replace SmolVLM-256M with **Gemma 4 12B Q4_K_M** in perceptiond (laptop prototype VLM lock).
- **Week 1-2:** Spike **Gemma 4 E4B vs LFM2.5-VL-450M Q4_0** in perceptiond (wearable VLM lock by end of Month 3).
- **Week 1-2:** **Anthropic SkillOpt + Microsoft SkillOpt** integration for Dan1/Dan2/Dan3/Dan4 skill document evolution. Treat as trainable parameters. **Both are now SOTA-validated as first-class primitives (v42).**
- **Week 3-4:** Spike LFM2.5-Audio-1.5B in audiod + ttsd (end-to-end audio-language, Apache 2.0-equivalent). If quality holds, eliminates audiod + ttsd stack.
- **Week 3-4:** Begin AHE + Self-Harness + HarnessForge integration for openclaw-gateway.
- **Week 3-4:** Begin HeLa-Mem Hebbian distillation study in memoryd v2 (hub detection + spreading activation).
- **Week 3-4:** Microsoft IQ integration design (Work IQ GA June 16, 2026) as context layer for memoryd v2.
- **Week 3-4:** Apple AFM 3 Core Advanced NAND-MoE architecture study for memoryd v2 (NAND-backed memory + IFP per-channel pruning + per-prompt routing).
- **Week 3-4:** **memoryd v2 v1.0 design — 6-core stack, single-process with 3 internal modules (ingest / retrieve / consolidate). LFM2.5-VL-450M (bbox-prompt JSON output) as the ingestion endpoint (v42 correction).**
- **Reaffirm carry from Dan1 punchlist:** Push danlab-multimodal public, fix GitHub bio, record 60s demo, post origin story thread.

**Success criteria:**
- SIA-H forked and running first 3-cycle experiment
- Gemma 4 12B Q4_K_M integrated in perceptiond
- LFM2.5-Audio-1.5B spike result documented
- Anthropic SkillOpt + Microsoft SkillOpt production-shipped for Dan skill evolution
- All 7 daemons supervised via `register_user_service`

### Month 2 — VLM Speedup + memoryd v2 Cognitive Consolidation + BitNet (August 2026)

**Goals:**
- **SpecVLM 2.5-2.9× + ViSpec 3.22× + EAGLE-2 3.05-4.26× + VLMCache 1.4-3.8× (ACM 2026)** in perceptiond. **Combined with BitNet b1.58 (live-verified 0.4GB mem / 29ms latency / 0.028J energy / 9.2× lower than LLaMA 3.2 1B, HF model card 2026-06-13) = 50-150× total VLM energy reduction path.** **v42 sharpening: BitNet b1.58 2B4T is text-only; the VLM path needs BitNet-VLM (2027 target) OR GAP9 RISC-V + event camera (OpenGlass pattern) for 2026 wearable.**
- **Gemma 4 QAT** variant spike (72% VRAM reduction, 26B-A4B in 15GB).
- **vstash adaptive RRF** in memoryd v2 (IDF-weighted fusion, +21.4% NDCG@10 on ArguAna).
- **AEL two-timescale evolution** in memoryd v2 (Thompson Sampling fast + LLM reflection slow, Sharpe +27%).
- **Salience CNN** spike in perceptiond (replace EMA + Haar cascade, biggest power lever for the wearable).
- **HMO 3-tier memory** in memoryd v2 (Primary Cache + Secondary + Archive with persona-driven promotion).
- **HeLa-Mem Hebbian distillation** in memoryd v2 (hub detection threshold + spreading activation + dual-path retrieval).
- **Apple Core AI extension skeleton (Xcode 27).** Apple Intelligence Extensions API distribution path.
- **Monako Glass silicon teardown** (Aug 2026 ship). The 48g form-factor reference arrives.

**Success criteria:**
- BitNet b1.58 integrated in perceptiond
- Salience CNN running at 5 FPS with <50ms latency
- VLMCache-style visual caching integrated
- AEL + vstash + HMO + HeLa-Mem in memoryd v2 dev branch
- Monako Glass teardown analysis documented

### Month 3 — memoryd v2 v1.0 OPEN-SOURCE RELEASE + SIA-W+H spike + iOS 27 GA counter (September 2026)

**Goals:**
- **memoryd v2 v1.0 OPEN-SOURCE RELEASE on GitHub public.** 6-core stack. **This is the single highest-ROI action in the entire 12-month plan.** Wedge against Apple Siri AI public GA in Sept 2026 (and the 12GB hardware gate).
- **SIA-W+H spike** (harness + weights). Build on SIA-H from Month 1-2. Target: LawBench 70.1% held-out, TriMul 14.02×. **Open-source the SIA-W+H fork for danlab-multimodal.** Per "Harness Updating Is Not Harness Benefit" (arXiv 2605.30621): train the 1.2B focal model to load and follow its own harness artifacts. Don't use a 4.6 evolver.
- **PopuLoRA populations** (TrueSkill cross-eval) in danlab-multimodal.
- **Apple Vision Pro M5 visionOS 27 "see what you see" pattern study** for perceptiond proactive loop. **The production reference.**
- **HarnessForge joint harness+policy co-evolution** in openclaw-gateway.
- **Continuous Harness reset-free online refinement** in openclaw-gateway.
- **os-toold v2** GA with ACS + Agent 365 + MXC + OWASP AIUC-1 + OWASP Agentic AI Security Maturity Model v2.01 + Microsoft IQ + Apple Core AI compliance. **Wedge against Microsoft Scout "Autopilot" + "addicted users" memo leak (June 4-9 2026).** **v42 sharpening: Microsoft Scout runs on OpenClaw (the same gateway we use), so we are explicitly building the open-source compliance wedge on top of the same runtime.**
- **Brilliant Labs Halo integration or reference** (Halo ships July 2026 with LFM2-VL-450M).
- **Microsoft IQ (Work IQ GA June 16) integration** as context layer for memoryd v2.
- **Microsoft SkillOpt + Anthropic SkillOpt** for Dan skill document evolution (Dan1/Dan2/Dan3/Dan4 = trainable parameters).

**Success criteria:**
- memoryd v2 v1.0 GitHub repo public, 100+ stars in first week
- SIA-W+H spike published
- os-toold v2 ACS + Agent 365 + OWASP + Microsoft IQ compliant
- Apple Siri AI GA → our open-source memory layer is the alternative

### Months 4-6 — Production Scale + Microsoft Scout GA Counter + memoryd v2 v2.0 (October-December 2026)

**Goals:**
- **memoryd v2 v2.0 PRODUCTION-SHIPPED. Full 11-component stack.** + AEL + vstash + HeLa-Mem + Decagon Proactive + VisualMem (uses LFM2.5-VL-450M bbox JSON output, v42).
- **Microsoft Scout GA (October 2026) — our ACS/Agent 365/IQ compliance on the platform.** Lean into the "addicted users" leak as the differentiator.
- **Brilliant Labs Halo integration or reference** as the LFM-on-wearables production reference.
- **Sub-1W wearable path concrete:** BitNet b1.58 + Litespark + SpecVLM + GAP9 RISC-V + Prophesee GENX320.
- **Salience CNN (replace EMA + Haar cascade) — biggest power lever.** Productionized.
- **AEL two-timescale memory retrieval evolution (Thompson Sampling fast + LLM reflection slow)** in memoryd v2 v2.0.
- **Monako Glass / Halo / Redax / Project Solara form factor decision locked.** Spike all four in parallel; pick the one that ships the wearable before Apple N50 in late 2027.
- **EvoTrainer policy + training-harness co-evolution.**
- **SIA-H + SIA-W+H production deployment in danlab-multimodal.** Target: 3-cycle self-improvement on a Dan Glasses-relevant task. **Beats the DuetBench 93% bar.**

**Success criteria:**
- memoryd v2 v2.0 GitHub release v2.0.0 with 11 components
- Microsoft Scout GA → our compliance wedge is public
- Form factor locked (4-path decision made)
- BitNet b1.58 + Salience CNN in production on laptop prototype

### Months 7-12 — Wearable + Sub-1W Path + Apple Counter + Harness Evolution (Q1-Q2 2027)

**Goals:**
- **Wearable form factor shipped** (Redax, Monako Glass, Project Solara, or Brilliant Labs Halo — locked Month 6).
- **Sub-1W wearable validated** on GAP9 RISC-V + event camera + BitNet b1.58.
- **Apple Core AI extension shipped** (Xcode 27 distribution).
- **visionOS 27 "see what you see" pattern as the perceptiond proactive loop inspiration.**
- **Meta-Harness search spike** (7.7-pt gain on online text classification as benchmark).
- **TRACE per-channel LoRA + MoE for memoryd v2** (capability-targeted retrieval, +14.1pt on τ 2-Bench).
- **HERO hindsight self-distillation for danlab-multimodal.**
- **SGM safety wrapper for SIA-H.**
- **IndiaAI Summit 2027 talk submitted.**
- **Harness-1 RL search agent integration** in memoryd v2 retrieval layer (stateful harness).
- **Decagon DuetBench-style benchmark** for Dan Glasses self-improvement (e.g., "find a person the user met, given 8 hours of memory"). **Target: 93%+ acceptance.**
- **Re-evaluate LFM2.5-1.2B-Thinking focal model** in Month 12. If "harness evolution > base-model capability" finding holds, lock the harness engineering investment for 2027-2028.

**Success criteria:**
- Wearable form factor on somdipto's face
- Sub-1W wearable validated on GAP9 RISC-V + event camera
- Decagon DuetBench-style benchmark published
- Apple N50 reactive content deployed

## Critical Open Questions for somdipto (v42)

1. **Redax vs Monako Glass vs Brilliant Labs Halo vs Project Solara MDEP form factor decision?** 🔴 Critical — four paths now, not three. Monako Glass ships August 2026 at $399 (48g, ARM Linux, runs Claude Code + Codex). Brilliant Labs Halo shipped July 2026 with LFM2-VL-450M. Project Solara MDEP OS is the off-the-shelf badge alternative (Microsoft Build 2026 May 19). **Decision by end of Q3 2026.**

2. **Liquid AI partnership — yes or no by end of June?** 🔴 Critical. Brilliant Labs Halo shipped with LFM2-VL-450M. We use LFM2.5 models. The window is closing.

3. **memoryd v2 v1.0 open source release in Month 3** (September 2026) is the #1 priority. 6-core stack. $0 of compute. **Apple Siri AI public GA in Sept 2026 (with 12GB RAM gate that excludes iPhone 17) is the trigger.** Block 12-16 weeks of ML engineer time on somdipto's calendar now.

4. **~16 RSI/harness architectures, 12-month roadmap.** Start Week 3-4 of Month 1 with SIA-H fork + DGM-H study. Per "Harness Updating Is Not Harness Benefit," invest in the task-solving agent, not the evolver.

5. **LFM2.5-Audio-1.5B decision by end of Month 2** — if quality holds for English, eliminates audiod + ttsd stack. Live-verified: 7.53 avg WER on English ASR benchmarks, Q5_K 1.6GB.

6. **Encoder-free vs encoder-based lock-in decision (Month 3)?** LFM2.5-VL-450M Apache 2.0-equivalent confirmed. Gemma 4 E4B Apache 2.0. Apple AFM 3 confirms encoder-free at scale.

7. **Open Standards target: Agent 365 + ACS + MXC + OWASP AIUC-1 + OWASP Agentic AI Security Maturity Model v2.01 + Lloyds "12th bet" + Microsoft IQ (Work IQ GA June 16) + Anthropic SkillOpt + Microsoft SkillOpt + Apple Core AI** (Month 3-5)? **v42 sharpening: Microsoft Scout "addicted users" memo leak (June 4-9 2026, 404 Media → NY Post + WIRED + MediaPost + Kotaku) is the differentiator — we ship the only ACS/OWASP/MIQ-compliant open-source self-improving agent stack.** Microsoft Scout "Autopilot" GA October 2026 is the trigger. **Microsoft SkillOpt (Build 2026 June 2 2026) and Anthropic SkillOpt (Fable 5 GA June 9 2026) ship skill-document evolution as a first-class primitive — our P1-39 (treat Dan1/Dan2/Dan3/Dan4 as trainable parameters) is now SOTA-aligned.**

8. **Buy Monako Glass silicon teardown + GAP9 dev kit + Prophesee GENX320 + Microsoft Surface RTX Spark + Snapdragon X Elite** THIS WEEK. The single most important measurement in the project.

9. **Apple AFM 3 Core Advanced NAND-stored 20B architecture study** for memoryd v2. Month 1 study.

10. **Microsoft IQ integration design (Month 1-2)?** Work IQ GA June 16, 2026. Context layer reference for memoryd v2.

11. **Microsoft SkillOpt + Anthropic SkillOpt integration (Month 1)?** Dan skill document evolution. Treat Dan1/Dan2/Dan3/Dan4 as trainable parameters. **v42: both are SOTA-validated as first-class primitives.**

12. **Anthropic Fable 5 architecture study (Month 1).** 80.3% SWE-bench Pro. Stripe migrated 50M-line codebase in a day. Ships with Anthropic SkillOpt. What did they get right? What can we copy? What can we open-source better?

13. **Decagon DuetBench-style benchmark for Dan Glasses (Month 9-12).** First industry benchmark for self-improving agents is public (93% acceptance, June 9 2026). **Our target: 93%+ acceptance on a Dan Glasses-relevant task.**

14. **SIA-H fork for danlab-multimodal (Month 1-2).** SIA is MIT, June 9 2026, 1,594 stars, 179 forks, last push 2026-06-11. First open-source SOTA with full architecture public. 2-week integration. **LFM2.5-1.2B-Thinking as Meta-Agent. 3 LLMs not 2 (Meta + Task + Feedback).** Per "Harness Updating Is Not Harness Benefit," train the 1.2B to load and follow its own harness.

15. **Relabel danlab-multimodal "RL feedback loop" → "Heuristic feedback loop — pre-RL scaffold" within 7 days.** (Carry from v26.) "RL" is industry-toxic. Anthropic / Decagon / Sakana frame as "self-improving" or "recursive self-improvement."

16. **Carry from Dan1 punchlist (50+ days unfixed):** Push danlab-multimodal public, fix GitHub bio, record 60s demo, post origin story thread, ship IndiaAI Summit talk abstract.

17. **register_user_service for all 7 daemons — Week 1 of Month 1.** 5-min fix. Solves the recurring os-toold regression. The cheapest single ROI action in the project.

18. **Apple Siri AI 12GB hardware gate response (Month 1).** MacRumors June 10 2026. iPhone 17 (8GB) and 16 Pro miss the full feature set. **The local-first wearable is the architectural case.** Open a public issue / blog post framing Dan Glasses as the always-on, always-local alternative.

## Top 3 Recommendations for Danlab's AGI Direction (v42)

1. **memoryd v2 v1.0 in September 2026 is the single highest-ROI investment for AGI direction.** 6-core stack (Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output, v42 correction) + Weaviate Engram), $0 of compute, 12-16 weeks for 1 ML engineer, open-sourced. The Anthropic Fable 5 + Decagon DuetBench + Recursive Superintelligence $650M + Microsoft Scout "Autopilot" + Microsoft SkillOpt + Anthropic SkillOpt events in the same 2-week window validate the bet. **The wearable is the body; memoryd v2 is the soul.** **v42 baseline: memoryd v1 is live and functional (id:1 score 0.5357 this run). v2 builds on top, not from scratch.**

2. **Form factor decision by end of Q3 2026.** Four paths: Redax (locked by somdipto's hardware team), Monako Glass (Aug 2026, 48g, $399, ARM Linux), Brilliant Labs Halo (July 2026, LFM2 on glasses, open source), Project Solara MDEP OS (Microsoft's off-the-shelf badge, AOSP-based, OpenClaw agent runtime). The window is 18-24 months; pick the path that ships the wearable before Apple N50 in late 2027.

3. **Ship the only open-source self-improving agent stack** (SIA-H + memoryd v2 + openclaw-gateway with AHE + Self-Harness + HarnessForge + Anthropic SkillOpt + Microsoft SkillOpt + ACS + Agent 365 + OWASP v2.01 + Microsoft IQ + Apple Core AI compliance) **before Apple Siri AI public GA (September 2026) AND before Microsoft Scout "Autopilot" GA (October 2026).** The Anthropic brake-pedal plea + Microsoft Scout "addicted users" memo leak (June 4-9 2026) = the regulatory + governance wedge is wide open. **Open-source is the only way to win it.** **v42 sharpening: Microsoft Scout runs on OpenClaw. Our compliance wedge (ACS + Agent 365 + OWASP v2.01 + Microsoft IQ + Apple Core AI) is the open-source alternative to Scout's Entra + Purview + MXC + Work IQ.**

---

*Last updated: 2026-06-13 08:40 IST (03:10 UTC) — v42 final.*
*Status: 12-month plan with locked focal models, locked memoryd v2 architecture, locked 4-path form-factor decision window, 90-day window to ship before Apple Siri AI public GA. The bet is locked.*
