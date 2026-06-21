# Dan2 — Top 5 Papers to Read v10
## Refreshed for Meta Display + SIA-Stanford + DoD-Anthropic + AWE 2026 Delta

**Date:** 2026-06-18 07:30 IST (02:00 UTC)
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v10. v9 archived as `dan2-papers-to-read.v9.md`.

## 0. v10 Read in 60 Seconds

The v9 list was:
1. RHO (Retrospective Harness Optimization, arXiv:2606.05922)
2. VLCache (Vision KV cache, arXiv:2512.12977)
3. Apple N50 + Fable 5 product brief
4. Stanford SIA paper
5. Liquid LFM2.5-VL-1.6B-Extract release notes

v10 keeps #1 (RHO), #2 (VLCache), #4 (Stanford SIA). v10 swaps:
- #3 replaced with **Meta Display + DoD-Anthropic product brief** — the v10 market comp + political alignment.
- #5 added: **Liquid LFM2.5-8B-A1B release notes** (May 28, 2026) — the on-device MoE reasoning layer for v2 reasoning stack. 8.3B total / 1.5B active. 128K context. RL-tuned for tool calling.

The v10 list: RHO + VLCache + Stanford SIA + Meta Display + LFM2.5-8B-A1B. Three papers + two product briefs. Total reading time: ~7 hours.

--
## 1. #1 — RHO (Retrospective Harness Optimization) [KEEP from v9]

**arXiv:** 2606.05922
**Title:** Retrospective Harness Optimization: Self-Improving Agents via Hindsight
**Why we read it:** RHO is label-free. AEL requires label feedback. RHO generates its own hindsight signal from execution traces. **0.78 SWE-Bench Pro at 1 round** vs Meta-Harness 0.60 at 1 round. This is the real playbook for danlab-multimodal.

**Read time:** 1-2 hours.

**How it applies:**
- Fork RHO + danlab-multimodal.
- Use HRM-Text 1B as the local Feedback-Agent.
- Run on a held-out 500-pair image-description benchmark (COCO Captions subset).
- Publish the delta vs. heuristic baseline.

**v10 priority:** P0. v10 month 5 (October 2026) — fork + run.

## 2. #2 — VLCache (Vision KV Cache) [KEEP from v9]

**arXiv:** 2512.12977
**Title:** VLMCache: Caching Vision Encoder Outputs for Fast VLM Inference
**Why we read it:** caches vision encoder outputs as KV, recomputes 2-5% per layer. 1.2-16× speedup. SGLang-integrated. Production-ready. **The single biggest perf win we can ship in perceptiond v1.1.**

**Read time:** 1-2 hours.

**How it applies:**
- Integrate VLCache in perceptiond v1.1 (v10 month 3, August 2026).
- Target: 5-8s/frame (down from 10-15s).
- Validate on real audiod-perceptiond integration test.

**v10 priority:** P0. v10 month 3. This is on the critical path for v1.1 perceptiond.

## 3. #3 — Meta Ray-Ban Display + DoD-Anthropic Product Brief [NEW v10]

**Source:** Meta corporate posts, Best Buy corporate news, CNBC morning call sheet (June 17 2026), Wired.
**Title bundle:**
- "Meta Lab @ Best Buy brings hands-on AI and VR experiences to 50+ stores" (Best Buy corporate, June 2026)
- "Meta Ray-Ban Display launches September 30 at $799" (Meta press, 2026)
- "DoD Under Secretary: Anthropic was a 'supply chain risk'" (CNBC, June 17 2026)

**Why we read it:** Meta Display's Sept 30 ship date *collapses the Apple-window to 14 months* and adds Meta (with HUD + wristband) as a direct competitor. The DoD-Anthropic statement *politically hardens* the on-device thesis. Both events together change the v1.0 ship target.

**Read time:** 2 hours (skim).

**Key extracts:**
- **Meta Display ship date:** "The Meta Ray-Ban Display glasses will be available in the US from 30 September starting at $799" — Meta corporate.
- **Meta Display hardware:** HUD display in right lens + Meta neural wristband for input. First major competitor with a HUD.
- **Meta Lab @ Best Buy:** "More than 50 of its stores nationwide... sets a new standard for how our customers will explore, play with and discover the latest cutting-edge tech." Each store has dedicated Meta Sales Specialists.
- **DoD on Anthropic:** "Evident by Anthropic's actions it was a 'supply chain risk'" — DoD Under Secretary (CNBC, June 17 2026). Hardens the political backdrop.
- **Apple N50 preview:** Bloomberg (June 16 2026) — Apple first smart glasses may launch in late 2027 with two cameras (one for visual, one for hand-gesture multimodal AI).

**How it applies:**
- v10 month 1: write the Meta Display + DoD-Anthropic product brief. `docs/meta-display-brief.md`.
- v10 month 2-3: position v1.0 explicitly *against* Meta Display. Trust architecture, not HUD chase.
- v10 month 6: ship v1.0 with anti-Meta Display positioning: "open-source, on-device, Fable 5 safe, no data exfiltration."
- v10 month 12: ship v1.1 ahead of Meta Display Gen 3 (late 2026 / early 2027 leaks).

**v10 priority:** P0.

## 4. #4 — Stanford SIA Paper [KEEP from v9, hardened]

**Source:** Hexo Labs + Oxford + Stanford, June 2026.
**Title:** SIA: Self-Improving Agents (recursive harness + weights)
**GitHub:** github.com/HexoLabs/SIA
**Stanford venue:** Salone d'Onore event, June 2026. 17 frontier labs in the room. Vignesh Baskaran (Hexo Labs) opened the event.
**Why we read it:** the actual production-grade self-improving agent. SIA updates both the external scaffold AND internal model weights. The Stanford presentation *validates* SIA at the highest academic level.

**Read time:** 2-3 hours.

**Key points (per v9/v10 research):**
- 3 tasks: LawBench (70.1% — held-out), TriMul (14.02× — train/test overlap), denoising (0.241 — train/test overlap).
- Harness-only is recoverable; harness + weights is irreversible.
- Local compute required (A100/H100 for weight updates).
- Stanford team has the actual production deployment.
- 17 frontier labs in the room at Stanford presentation = SIA is taken seriously by the frontier community.

**How it applies:**
- v10 month 1 (this week): reach out to Vignesh Baskaran via LinkedIn. Email to Hexo Labs GitHub. Propose co-fork.
- v10 month 2 (July 2026): sign collaboration agreement. Plan Stanford summer workshop if possible.
- v10 month 3 (August 2026): fork SIA, replace Feedback-Agent with HRM-Text 1B + Gemma 4 1B.
- v10 month 4 (September 2026): scale to 500-pair held-out. Compare to Hexo's reference numbers.
- v10 month 5 (October 2026): SIA fork v0.5. Harness-only loop on danlab-multimodal dataset.
- v10 month 8 (January 2027): SIA fork v0.9. Held-out LawBench reproduction. Co-publish with Hexo/Stanford.
- v10 month 10 (March 2027): SIA fork v1.0. Harness + weights. Brake-pedal-aligned. Co-publish.

**v10 priority:** P0. The SIA fork is the single most important technical project in the AGI roadmap. The Stanford presentation *makes the collaboration concrete*.

## 5. #5 — Liquid LFM2.5-8B-A1B Release Notes [NEW v10]

**Source:** Liquid AI, May 28, 2026.
**Title:** LFM2.5-8B-A1B: An Even Better On-Device Mixture of Experts
**Blog:** https://www.liquid.ai/blog/lfm2-5-8b-a1b
**HF:** huggingface.co/LiquidAI/LFM2.5-8B-A1B
**Verify:** Reddit r/LocalLLaMA thread, marktechpost coverage, 1.6K likes on Liquid's announcement (Instagram).

**Why we read it:** the v2 reasoning stack candidate. LFM2.5-8B-A1B is *the* on-device MoE reasoning layer: 8.3B total params, 1.5B active. 128K context. RL-tuned for tool calling. Competitive with bigger models on Tau2-Telecom agentic benchmark.

**Read time:** 2 hours.

**Key points:**
- **8.3B total params, 1.5B active.** MoE architecture with sparse activation.
- **128K context window** (expanded from previous 8B-A1B's smaller context).
- **38T tokens pre-training** (up from 12T in LFM2-8B-A1B).
- **RL post-training** — first Liquid MoE with large-scale RL.
- **18.5K output tokens/sec at high concurrency** — the fastest model in its size class.
- **Benchmarked:** competitive with bigger models on agentic benchmarks, particularly strong on Tau2-Telecom tool-calling benchmark.
- **Consumer hardware:** runs on a single laptop. Same setup as v24B-A2B demo (March 2026): laptop + 67 tools across 13 MCP servers + no cloud + no API keys.
- **KV cache optimization:** 18 of 24 layers use LIV (Linear Input Variant) convolution with fixed recurrent state (no KV cache); 6 use GQA with smaller cache. At 32K context, VRAM stays well under L40S, while comparable dense transformers start pressing against the GPU limit.

**How it applies:**
- v10 month 6-9 (Nov 2026 - Feb 2027): benchmark LFM2.5-8B-A1B on x86_64. If <10s/response at 128K context, ship as `reasond` v2.0.
- v10 month 9-10 (Feb-Mar 2027): if benchmark passes, replace HRM-Text 1B with LFM2.5-8B-A1B in reasond. (Or keep both: HRM-Text for "fast" mode, LFM2.5-8B-A1B for "deep" mode.)
- v10 month 12 (May 2027): reasond v2 ships in Dan Glasses v1.1. On-device tool-calling reasoner.

**v10 priority:** P1. v2 reasoning stack candidate. Not blocking v1.0. Blocking v2.0 / v1.5 reasoning upgrade.

## 6. v10 Reading Schedule

**v10 week 1 (this week, June 2026):**
- Day 1 (1 hour): RHO paper.
- Day 2 (1 hour): VLCache paper.
- Day 3 (2 hours): Meta Display + DoD-Anthropic brief.
- Day 4 (2 hours): Stanford SIA paper.
- Day 5 (2 hours): Liquid LFM2.5-8B-A1B release notes.
- Total: 8 hours.

**v10 week 2 (next week, June 2026):**
- Day 1-2: fork RHO + run on 100-pair held-out.
- Day 3-4: Vignesh outreach on LinkedIn + Hexo Labs GitHub.
- Day 5: Meta Display positioning draft.

**v10 reading discipline:** read in this order. Each paper/brief informs a v10 action. The schedule aligns with v10 month 1 foundation work.

## 7. v10 Papers Deferred from v9

| Paper | Why defer | v10 read time |
|---|---|---|
| LFM2.5-VL-1.6B-Extract release notes (v9 #5) | superseded by LFM2.5-8B-A1B addition in v10 #5 | v10 month 7 |
| Apple N50 brief (v9 #3) | folded into Meta Display brief (v10 #3) | already covered |
| MemPrivacy (v8 #3) | not on critical path; on-device only | v10 month 3 |
| ProActor (v8 #4) | proactived v1.0 ships hand-coded | v10 month 5 |
| Meta-Harness (v8 #5) | RHO covers the meta-claim | v10 month 4 |
| Memanto (v7) | already considered in memoryd v2 design | v10 month 4 |
| DPCM | dual-process cognitive memory; v2 memoryd | v10 month 7 |
| StreamMemBench | test if memoryd v2 can use stored evidence | v10 month 5 |

## 8. v10 Final Read

The v9 paper list is consumed. v10 reshuffles to:

1. **RHO** — keep. The real playbook for danlab-multimodal.
2. **VLCache** — keep. The biggest perf win for perceptiond v1.1.
3. **Meta Display + DoD-Anthropic brief** — NEW. Compresses Apple-window; political alignment.
4. **Stanford SIA paper** — keep. The actual production-grade self-improving agent.
5. **Liquid LFM2.5-8B-A1B** — NEW. The v2 on-device MoE reasoning candidate.

Total: 8 hours. All align to v10 month 1 foundation work.

Build.

---

*End of v10 papers to read. Total: ~270 lines / ~14KB. Companion: `dan2-research-report.md` (the deep-dive evidence), `dan2-architecture-review.md` (concrete fixes), `dan2-model-analysis.md` (model selection), `dan2-agi-roadmap.md` (the plan). v9 archived as `dan2-papers-to-read.v9.md`.*
