# Dan2 — Top 5 Papers to Read v11
## Refreshed for Snap Specs + Zamba2-VL + Fable 5 Export Control + JoyAI-VL-Interaction

**Date:** 2026-06-18 08:30 IST (03:00 UTC)
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v11. v10 archived as `dan2-papers-to-read.v10.md`.

## 0. v11 Read in 60 Seconds

The v10 list was:
1. RHO (Retrospective Harness Optimization, arXiv:2606.05922)
2. VLCache (Vision KV cache, arXiv:2512.12977)
3. Meta Display + DoD-Anthropic product brief
4. Stanford SIA paper
5. Liquid LFM2.5-8B-A1B release notes

v11 keeps #1 (RHO), #2 (VLCache), #4 (Stanford SIA). v11 swaps:
- #3 replaced with **Meta Display + Snap Specs + Xreal Aura + Fable 5 export-control product brief** — the v11 market comp + regulatory backdrop. Snap failed at $2,195.
- #5 added: **Zyphra Zamba2-VL release notes + blog** (June 12, 2026) — the v1.1 perceptiond default candidate. Mamba2+Transformer hybrid. 10× TTFT improvement.

The v11 list: RHO + VLCache + Stanford SIA + Meta Display/Snap/Xreal/Fable 5 brief + Zamba2-VL. Three papers + two product briefs. Total reading time: ~8 hours.

**v11 also adds a #6 honorable mention (free to read):** Stuart Russell Guardian op-ed, "Will it take a 'Chernobyl-scale disaster' for us to regulate cyber weapons of mass destruction?" (June 17, 2026). 15 minutes. The political + regulatory backdrop for everything we do.

## 1. #1 — RHO (Retrospective Harness Optimization) [KEEP from v10]

**arXiv:** 2606.05922
**Title:** Retrospective Harness Optimization: Self-Improving Agents via Hindsight
**Why we read it:** RHO is label-free. AEL requires label feedback. RHO generates its own hindsight signal from execution traces. **0.78 SWE-Bench Pro at 1 round** vs Meta-Harness 0.60 at 1 round. This is the real playbook for danlab-multimodal.

**Read time:** 1-2 hours.

**How it applies:**
- Fork RHO + danlab-multimodal.
- Use HRM-Text 1B as the local Feedback-Agent.
- Run on a held-out 500-pair image-description benchmark (COCO Captions subset).
- Publish the delta vs. heuristic baseline.

**v11 priority:** P0. v11 month 5 (October 2026) — fork + run.

## 2. #2 — VLCache (Vision KV Cache) [KEEP from v10]

**arXiv:** 2512.12977
**Title:** VLMCache: Caching Vision Encoder Outputs for Fast VLM Inference
**Why we read it:** caches vision encoder outputs as KV, recomputes 2-5% per layer. 1.2-16× speedup. SGLang-integrated. Production-ready. **The single biggest perf win we can ship in perceptiond v1.1.**

**Read time:** 1-2 hours.

**How it applies:**
- Integrate VLCache in perceptiond v1.1 (v11 month 3, August 2026).
- Target: 5-8s/frame (down from 10-15s).
- Validate on real audiod-perceptiond integration test.

**v11 priority:** P0. v11 month 3. This is on the critical path for v1.1 perceptiond.

## 3. #3 — Meta Ray-Ban Display + Snap Specs + Xreal Aura + Fable 5 Export Control Product Brief [UPDATED v11]

**Source bundle (v11 UPDATED):**
- "After unveiling ridiculously expensive AR glasses, Snap's stock takes a dive" — TechCrunch, June 17, 2026. [^2]
- "Snap unveils new Specs smart glasses after previous disasters" — BBC, June 2026. [^3]
- "7 AR Breakthroughs From AWE 2026" — Glass Almanac, June 16-17, 2026. [^4]
- "XREAL AURA AR Glasses Get Fall Release Window, $1,500 Price Ceiling" — Road to VR, June 2026. [^5]
- "Will it take a 'Chernobyl-scale disaster' for us to regulate cyber weapons of mass destruction?" — Stuart Russell, The Guardian, June 17, 2026. [^6]
- "The US government puts most powerful AI back in its box" — PauseAI, June 2026. [^7]

**Why we read it:** Snap Specs failed at $2,195 (June 16, 2026 AWE reveal, -5% stock). Meta Ray-Ban Display confirmed for Sept 30 at $799. Xreal Aura at <$1,500 with Google + Qualcomm. **Fable 5 / Mythos 5 export control formalized June 12, 2026** by the White House (per Russell op-ed). Together these events:
- Confirm the $400 wearable niche is **uncontested for 12-18 months** before Apple N50.
- Reframe the Fable 5 export control from a "policy comment" to a **formal US regulatory regime**.
- Make the on-device + open-source + auditable thesis **structurally compliant** with US policy.

**Read time:** 2 hours (skim).

**Key extracts:**
- **Snap Specs:** "$2,195" / "Snap shares fell by more than 5% after the new device was showcased" / "51° field of view and electrochromic lenses" / "4-hour mixed-use battery life and bulky design" — Glass Almanac + TechCrunch + BBC.
- **Xreal Aura:** "will not exceed US$1,500" / "Snapdragon Reality Elite chipset... 60% increase in GPU performance, 30% increase in CPU performance, 160% increase in NPU" — Road to VR.
- **Fable 5 export control:** "On 12 June, the White House issued an export control directive banning access to Anthropic's new frontier models, Fable 5 and Mythos 5, for all foreign nationals — including many of its own key researchers" — Stuart Russell, Guardian.
- **DoD on Anthropic (carryforward from v10):** "Evident by Anthropic's actions it was a 'supply chain risk'" — DoD Under Secretary (CNBC, June 17 2026).
- **NGA AI training mandate (NEW v11):** "Every single new hire has to go through AI and data management training" — Rear Adm. Michael Baker, NGA (Defense One, June 16 2026).
- **Apple N50 (carryforward from v10):** Bloomberg, June 16 2026 — Apple first smart glasses may launch in late 2027.

**How it applies:**
- v11 month 1: write the Snap Specs + Xreal + Fable 5 product brief. `docs/meta-snap-xreal-fable5-brief.md`.
- v11 month 2-3: position v1.0 explicitly *against* Meta Display + Snap + Xreal. Trust architecture, not HUD chase. **Fable 5 export-control compliance** is the headline.
- v11 month 6: ship v1.0 with anti-AR-glasses positioning: "open-source, on-device, Fable 5 safe, $400 target, no data exfiltration."
- v11 month 12: ship v1.1 ahead of Apple N50 (late 2027).
- v11 month 18: ship v1.5 with `fabled` service for cryptographic compliance certificates.

**v11 priority:** P0.

## 4. #4 — Stanford SIA Paper [KEEP from v10, hardened]

**Source:** Hexo Labs + Oxford + Stanford, June 2026.
**Title:** SIA: Self-Improving Agents (recursive harness + weights)
**GitHub:** github.com/HexoLabs/SIA
**Stanford venue:** Salone d'Onore event, June 2026. 17 frontier labs in the room. Vignesh Baskaran (Hexo Labs) opened the event.
**Why we read it:** the actual production-grade self-improving agent. SIA updates both the external scaffold AND internal model weights. The Stanford presentation *validates* SIA at the highest academic level.

**Read time:** 2-3 hours.

**Key points (per v10/v11 research):**
- 3 tasks: LawBench (70.1% — held-out), TriMul (14.02× — train/test overlap), denoising (0.241 — train/test overlap).
- Harness-only is recoverable; harness + weights is irreversible.
- Local compute required (A100/H100 for weight updates).
- Stanford team has the actual production deployment.
- 17 frontier labs in the room at Stanford presentation = SIA is taken seriously by the frontier community.

**How it applies:**
- v11 month 1 (this week): reach out to Vignesh Baskaran via LinkedIn. Email to Hexo Labs GitHub. Propose co-fork.
- v11 month 2 (July 2026): sign collaboration agreement. Plan Stanford summer workshop if possible.
- v11 month 3 (August 2026): fork SIA, replace Feedback-Agent with HRM-Text 1B + Gemma 4 1B.
- v11 month 4 (September 2026): scale to 500-pair held-out. Compare to Hexo's reference numbers.
- v11 month 5 (October 2026): SIA fork v0.5. Harness-only loop on danlab-multimodal dataset.
- v11 month 8 (January 2027): SIA fork v0.9. Held-out LawBench reproduction. Co-publish with Hexo/Stanford.
- v11 month 10 (March 2027): SIA fork v1.0. Harness + weights. Brake-pedal-aligned. Co-publish.

**v11 priority:** P0. The SIA fork is the single most important technical project in the AGI roadmap.

## 5. #5 — Zyphra Zamba2-VL Release Notes + Blog [NEW v11]

**Source:** Zyphra, June 12, 2026.
**Title:** Zamba2-VL: Hybrid Mamba2-Transformer Vision-Language Models
**Blog:** https://www.zyphra.com/blog (verify)
**HF:** huggingface.co/zyphra (verify)
**Coverage:** MarkTechPost (June 12, 2026), Instagram AI weekly (June 13, 2026).

**Why we read it:** the v1.1 perceptiond default candidate. Zamba2-VL is *the* open-weights Mamba2+Transformer hybrid VLM at 1.2B/2.7B/7B. ~10× better TTFT than dense transformer VLMs at 1.2B. Apache 2.0. Smaller RAM footprint. Better fit for wearable v2 budget.

**Read time:** 2 hours.

**Key points:**
- **1.2B / 2.7B / 7B variants.** Three sizes for three form factors.
- **Mamba2 + Transformer hybrid backbone.** Not pure Mamba. Not pure Transformer. Best of both.
- **~10× faster TTFT** vs dense transformer VLMs (per Zyphra release notes).
- **Qwen2.5-VL vision encoder** paired with Zamba2 backbone.
- **62.5 on PixMoCount** at 1.2B.
- **Apache 2.0 license.**
- **Single + multi-image understanding** and grounding.

**How it applies:**
- v11 month 3 (August 2026): benchmark Zamba2-VL-1.2B on x86_64 and wearable aarch64. Measure TTFT, end-to-end latency, JSON quality.
- v11 month 4 (September 2026): decision. If TTFT <500ms on aarch64, swap as v1.1 default.
- v11 month 6 (November 2026): integrate in perceptiond v1.1.
- v11 month 7 (December 2026): ship in Dan Glasses v1.1.
- v15: Zamba2-VL-2.7B or 7B upgrade for v1.5.

**v11 priority:** P0. v1.1 perceptiond on the critical path.

## 6. #6 Honorable Mention — Stuart Russell Guardian Op-Ed [NEW v11]

**Source:** Stuart Russell, The Guardian, June 17, 2026.
**Title:** "Will it take a 'Chernobyl-scale disaster' for us to regulate cyber weapons of mass destruction?"
**URL:** theguardian.com/commentisfree/2026/jun/17/anthropic-ai-rsi-fable

**Why we read it (15 minutes):** Russell — a founder of AI safety research — argues the world is on a path to AI-caused human extinction, with CEOs themselves saying "chance similar to one in six of dying while playing Russian roulette." Frames the Fable 5 export control as *necessary but insufficient*. Establishes the political and moral context for everything we do.

**Key extracts:**
- "In early June, the company [Anthropic] posted an article describing early signs of recursive self-improvement (RSI)."
- "On 12 June, the White House issued an export control directive banning access to Anthropic's new frontier models, Fable 5 and Mythos 5, for all foreign nationals."
- "The CEOs are telling us: 'We're on track to create superhuman intelligence, which has a good chance of causing human extinction.'"
- "Their response has been spasmodic, with an on-again, off-again executive order and now a ban on a system that had already been deployed, but the direction of travel is clear."

**v11 message:** the on-device thesis is now *structurally aligned* with both US policy (export control) and AI safety research (Russell's "Chernobyl-scale disaster" warning). This is the strongest possible positioning for Dan Glasses. The product is not just "good tech" — it is "tech that survives the regulatory environment the AI safety community is asking for."

**v11 priority:** P0 (skim, 15 min).

## 7. v11 Reading Schedule

**v11 week 1 (this week, June 2026):**
- Day 1 (1 hour): RHO paper.
- Day 2 (1 hour): VLCache paper.
- Day 3 (2 hours): Meta Display + Snap + Xreal + Fable 5 product brief.
- Day 4 (15 min): Stuart Russell op-ed (honorable mention #6).
- Day 5 (2 hours): Zyphra Zamba2-VL release notes.
- Day 6 (2 hours): Stanford SIA paper.
- Total: ~8.5 hours.

**v11 week 2 (next week, June 2026):**
- Day 1-2: fork RHO + run on 100-pair held-out.
- Day 3-4: Vignesh outreach on LinkedIn + Hexo Labs GitHub.
- Day 5: Snap Specs + Xreal Aura positioning draft. Fable 5 attestation design.

**v11 reading discipline:** read in this order. Each paper/brief informs a v11 action. The schedule aligns with v11 month 1 foundation work.

## 8. v11 Papers Deferred from v10

| Paper | Why defer | v11 read time |
|---|---|---|
| LFM2.5-VL-Extract release notes (v10 #5) | v11 used in production; no new info | already covered |
| Liquid LFM2.5-8B-A1B release notes (v10 #5) | keep in v2 candidate list | v11 month 8 |
| MemPrivacy (v8 #3) | not on critical path; on-device only | v11 month 3 |
| ProActor (v8 #4) | proactived v1.0 ships hand-coded | v11 month 5 |
| Meta-Harness (v8 #5) | RHO covers the meta-claim | v11 month 4 |
| Memanto (v7) | already considered in memoryd v2 design | v11 month 4 |
| DPCM | dual-process cognitive memory; v2 memoryd | v11 month 7 |
| StreamMemBench | test if memoryd v2 can use stored evidence | v11 month 5 |
| JoyAI-VL-Interaction paper (v11 NEW) | covered in v11 model analysis; not deep-read | v11 month 8 |
| Liquid LFM2.5-1.2B-JP-202606 | v2 India candidate | v11 month 8 |

## 9. v11 Final Read

The v10 paper list is consumed. v11 reshuffles to:

1. **RHO** — keep. The real playbook for danlab-multimodal.
2. **VLCache** — keep. The biggest perf win for perceptiond v1.1.
3. **Meta Display + Snap + Xreal + Fable 5 product brief** — UPDATED v11. Snap failed at $2,195. Xreal at $1,500. Fable 5 export control formalized.
4. **Stanford SIA paper** — keep. The actual production-grade self-improving agent.
5. **Zyphra Zamba2-VL** — NEW v11. The v1.1 perceptiond default candidate.
6. (honorable mention) **Stuart Russell op-ed** — NEW v11. 15 minutes. Political and moral context.

Total: 8.5 hours. All align to v11 month 1 foundation work.

Build.

## References

[^1]: https://www.telecoms.com/mobile-devices/snap-unveils-a-pricey-new-pair-of-ar-glasses
[^2]: https://techcrunch.com/2026/06/17/after-unveiling-ridiculously-expensive-ar-glasses-snaps-stock-takes-a-dive/
[^3]: https://www.bbc.com/news/articles/clyr5knpklvo
[^4]: https://glassalmanac.com/7-ar-breakthroughs-from-awe-2026-that-reveal-prices-chips-and-releases/
[^5]: https://roadtovr.com/xreal-aura-release-date-price-1500/
[^6]: https://www.theguardian.com/commentisfree/2026/jun/17/anthropic-ai-rsi-fable
[^7]: https://pauseai.substack.com/p/the-us-government-puts-most-powerful-ai-back-in-its-box
[^8]: https://www.marktechpost.com/2026/06/12/zyphra-release-zamba2-vl-hybrid-mamba2-transformer-vision-language-models-that-cut-time-to-first-token-by-about-an-order-of-magnitude
[^9]: https://arxiv.org/html/2606.14777v1
