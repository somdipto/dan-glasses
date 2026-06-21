# Dan2 — Top 5 Papers to Read v9
## Refreshed for the Fable 5 / Apple Window / SIA-Stanford Delta

**Date:** 2026-06-18 06:30 IST (01:00 UTC)
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v9. v8 archived as `dan2-papers-to-read.v8.md`.

## 0. v9 Read in 60 Seconds

The v8 list was:
1. RHO (Retrospective Harness Optimization, arXiv:2606.05922)
2. VLCache (Vision KV cache, arXiv:2512.12977)
3. MemPrivacy (edge-cloud reversible pseudonymization, May 2026)
4. ProActor (RL-trained proactive agent, ACL 2026)
5. Meta-Harness (harness post-training beats weights, ICML 2026)

v9 keeps #1 (RHO) and #2 (VLCache). v9 swaps:

- #3 replaced with **Apple N50 + Fable 5 product brief** (not a paper — a product brief tying together the Apple-window and the Fable 5 moat).
- #4 replaced with **Stanford SIA paper** (Hexo Labs + Oxford + Stanford, June 2026) — the actual production-grade self-improving agent.
- #5 replaced with **Liquid LFM2.5-VL-1.6B-Extract release notes** (Liquid AI, June 2026) — the v1.1 vision upgrade candidate.

The v9 reading list is shorter and tighter. Three papers + two product briefs. Total reading time: ~6 hours.

---

## 1. #1 — RHO (Retrospective Harness Optimization) [KEEP from v8]

**arXiv:** 2606.05922
**Title:** Retrospective Harness Optimization: Self-Improving Agents via Hindsight
**Why we read it:** RHO is label-free. AEL requires label feedback. RHO generates its own hindsight signal from execution traces. **0.78 SWE-Bench Pro at 1 round** vs Meta-Harness 0.60 at 1 round (0.80 at 10 rounds with 3x compute). This is the real playbook for danlab-multimodal.

**Read time:** 1-2 hours.

**How it applies:**
- Fork RHO + danlab-multimodal.
- Use HRM-Text 1B as the local Feedback-Agent.
- Run on a held-out 500-pair image-description benchmark (COCO Captions subset).
- Publish the delta vs. heuristic baseline.

**v9 priority:** P0. v9 month 5 (October 2026) — fork + run.

---

## 2. #2 — VLCache (Vision KV Cache) [KEEP from v8]

**arXiv:** 2512.12977
**Title:** VLMCache: Caching Vision Encoder Outputs for Fast VLM Inference (or VLCache variant)
**Why we read it:** caches vision encoder outputs as KV, recomputes 2-5% per layer. 1.2-16× speedup. SGLang-integrated. Production-ready. **The single biggest perf win we can ship in perceptiond v1.1.**

**Read time:** 1-2 hours.

**How it applies:**
- Integrate VLCache in perceptiond v1.1 (v9 month 3, August 2026).
- Target: 5-8s/frame (down from 10-15s).
- Validate on real audiod-perceptiond integration test.

**v9 priority:** P0. v9 month 3. This is on the critical path for v1.1 perceptiond.

---

## 3. #3 — Apple N50 + Fable 5 Product Brief [NEW v9]

**Source:** Bloomberg (June 16 2026), Fortune (June 13 2026), TechCrunch (June 12 + 15 2026), Wired.
**Title bundle:** "Apple plans camera AirPods alongside upgraded foldable iPhone in 2027" (Bloomberg) + "Anthropic's safety warnings may have just backfired — the government has pulled the plug on its most powerful AI" (TechCrunch, June 12 2026) + "The US government's Anthropic models ban was never about an AI jailbreak" (TechCrunch, June 15 2026).

**Why we read it:** the two events together constrain our AGI roadmap. Apple N50 (late 2027) closes the window. Fable 5 (June 12 2026) makes on-device the new norm.

**Read time:** 1 hour (skim).

**Key extracts:**
- **Apple N50:** "Apple Inc.'s upcoming camera-equipped AirPods, a product meant to vault the company into the AI device market, is scheduled to launch in late 2027. ... Apple's first smart glasses as early as the tail end of next year. ... The N50 glasses could have two cameras, one for pictures and videos, the other for multimodal AI input and hand-gesture control."
- **Fable 5 trigger:** "We have reviewed a report that we believe is the basis of the government's directive and validated that the level of capability displayed there is widely available from other models (including OpenAI's GPT-5.5)."
- **TechCrunch (June 15 2026):** "The US government's Anthropic models ban was never about an AI jailbreak." (Strong implication: it's about competition, not security.)

**How it applies:**
- v9 month 1: write the Apple-window + Fable 5 product brief. `docs/apple-window-fable5-brief.md`.
- v9 month 6: ship v1.0 with Fable 5 safe claim.
- v9 month 12: ship v1.1 ahead of Apple N50.

**v9 priority:** P0.

---

## 4. #4 — Stanford SIA Paper [NEW v9]

**Source:** Hexo Labs + Oxford + Stanford, June 2026.
**Title:** SIA: Self-Improving Agents (recursive harness + weights)
**GitHub:** github.com/HexoLabs/SIA
**Why we read it:** the actual production-grade self-improving agent. SIA updates both the external scaffold AND internal model weights. We need to read the paper (not just the README) and understand the trade-offs.

**Read time:** 2-3 hours.

**Key points (per v9 research):**
- 3 tasks: LawBench (70.1% — held-out), TriMul (14.02× — train/test overlap), denoising (0.241 — train/test overlap).
- Harness-only is recoverable; harness + weights is irreversible.
- Local compute required (A100/H100 for weight updates).
- Stanford team has the actual production deployment.

**How it applies:**
- v9 month 1: outreach to Stanford SIA team. Email GitHub issue on HexoLabs/SIA.
- v9 month 3: fork SIA, replace Feedback-Agent with HRM-Text 1B + Gemma 4 1B.
- v9 month 5: SIA fork v0.5 on danlab-multimodal dataset.
- v9 month 8: SIA fork v0.9 with LawBench reproduction.
- v9 month 12: SIA fork v1.0 with held-out generalization.

**v9 priority:** P0. The SIA fork is the single most important technical project in the AGI roadmap.

---

## 5. #5 — Liquid LFM2.5-VL-1.6B-Extract Release Notes [NEW v9]

**Source:** Liquid AI, June 2026.
**Title:** LFM2.5-VL-1.6B-Extract release notes
**BenchLM:** liquidExtractSchemaF1, scored 99.6% (vs 98.8% for 450M-Extract)
**Why we read it:** the v1.1 vision upgrade candidate. We need to understand the size/quality tradeoff before integrating.

**Read time:** 1 hour.

**Key points:**
- 1.6B params. Q4_0 ~700MB.
- Image-to-JSON extraction: 99.6% F1 on the Liquid Extract F1 benchmark.
- Same Liquid architecture family as LFM2.5-VL-450M.
- GGUF + ONNX available.

**How it applies:**
- v9 month 3: benchmark LFM2.5-VL-1.6B-Extract on x86_64.
- v9 month 4: decide v1.1 swap. If <5s/frame, ship as default. If 5-10s, ship as pro mode.
- v9 month 7: integrate in perceptiond v1.1.

**v9 priority:** P1. Not blocking v1.0. Blocking v1.1.

---

## 6. v9 Reading Schedule

**Week 1 (this week, June 2026):**
- Day 1 (1 hour): RHO paper.
- Day 2 (1 hour): VLCache paper.
- Day 3 (1 hour): Apple N50 + Fable 5 product brief.
- Day 4 (2 hours): Stanford SIA paper.
- Day 5 (1 hour): Liquid LFM2.5-VL-1.6B-Extract release notes.
- Total: 6 hours.

**v9 reading discipline:** read in this order. Each paper informs a v9 action. The schedule aligns with the v9 month 1 foundation work.

---

## 7. v9 Papers to Read but Defer

These were on v8 list and are still relevant, but **deferred to v9 month 2+** because the v9 month 1 priority is the SIA fork, Fable 5, and Apple positioning.

| Paper | Why defer | v9 read time |
|---|---|---|
| MemPrivacy (v8 #3) | nice-to-have for cloud-sync; we are on-device only, so not on critical path | v9 month 3 |
| ProActor (v8 #4) | proactived v1.0 ships hand-coded; v1.1 learns from ProActor | v9 month 5 |
| Meta-Harness (v8 #5) | the meta-claim (harness > weights) is validated by RHO already | v9 month 4 |
| Memanto (v7) | memoryd v2 is on critical path; counter-argument already considered in v9 memoryd v2 design | v9 month 4 |
| DPCM | dual-process cognitive memory; v2 memoryd | v9 month 7 |
| StreamMemBench | test if our memoryd v2 can use stored evidence for future help | v9 month 5 |

---

## 8. v9 Final Read

The v8 paper list is consumed. v9 reshuffles to:

1. **RHO** — keep. The real playbook for danlab-multimodal.
2. **VLCache** — keep. The biggest perf win for perceptiond v1.1.
3. **Apple N50 + Fable 5 brief** — NEW. Constrains v9.
4. **Stanford SIA paper** — NEW. The actual production-grade self-improving agent.
5. **Liquid LFM2.5-VL-1.6B-Extract** — NEW. The v1.1 vision upgrade.

Total: 6 hours. All align to v9 month 1 foundation work.

Build.

---

*End of v9 papers to read. Total: ~200 lines / ~12KB. Companion: `dan2-research-report.md` (the deep-dive evidence), `dan2-architecture-review.md` (concrete fixes), `dan2-model-analysis.md` (model selection), `dan2-agi-roadmap.md` (the plan). v8 archived as `dan2-papers-to-read.v8.md`.*
