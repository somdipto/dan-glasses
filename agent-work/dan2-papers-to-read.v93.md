# Top 5 Papers the Danlab Team Should Read

**Author:** Dan2
**Date:** 2026-06-26
**Status:** v93 — delta on v12 (refreshed for May–Jun 2026 papers, Liquid AI retrievers, NPU benchmarks, memory architectures)

---

## v93 update note

v12's Top 5 (SIA, LFM2.5-VL-450M report, SemanticXR, Sakana RSI, MetaAI/DGM) remain relevant. **v93 rotates three out** for papers that better match our Q3 2026 action items — specifically the memory architecture decisions (Liquid AI retrievers shipped Jun 18) and the edge VLM NPU benchmarks (AMD Ryzen AI published May 2026).

**The v93 top 5 reads are more action-oriented than v12's.** Each one ties to a concrete next-30-day decision.

---

## 1. **SIA: Self Improving AI with Harness & Weight Updates** *(kept from v12 — still #1)*
*Hebbar et al., arXiv:2605.27276, Hexo Labs (MIT), 28 May 2026*

**Why this is still #1.** The path from danlab-multimodal's "pre-RL scaffold" to real RL.

**What it does.** A language-model Feedback-Agent updates *both* the harness (prompts, tools, retry logic) **and** the model weights. **25.1% over prior SOTA** on legal classification, GPU kernels, RNA denoising.

**v93 action update:** v12 said "fork SIA, swap Claude Sonnet 4.6 → LFM2.5-1.2B-Thinking." **v93 confirms and adds: wrap in SGM-style e-value gate for safety.** (SGM = Statistical Gödel Machine, arXiv:2510.10232, the safety wrapper around arbitrary self-modification proposers.) This makes the SIA fork risk-aware before we let it touch weights in production.

**Action:** Dan3 + Dan2 to fork `hexo-ai/sia`, replace Feedback-Agent with LFM2.5-1.2B-Thinking, run a 10-generation loop on danlab-multimodal's screen-description benchmark, wrap in SGM gate, publish results.

**Read it:** https://arxiv.org/abs/2605.27276

---

## 2. **LFM2.5 Retrievers: Embedding-350M + ColBERT-350M** *(NEW for v93)*
*Liquid AI, 18 June 2026*

**Why this is #2.** This is the paper/blog that **unlocks memoryd v2 as a fork-and-ship**, not a research project. v12 hedged; v93 commits.

**What they are.** Two open-weight retrieval models under LFM Open License v1.0 (Apache 2.0-equivalent):
- **LFM2.5-Embedding-350M** — 1024-dim embeddings, 100+ languages including **22 Indic languages**. Replaces `all-MiniLM-L6-v2` (384-dim, English-tilted).
- **LFM2.5-ColBERT-350M** — late-interaction reranker. Pairs with the embedding model for two-stage retrieval.

**Why this matters to us specifically:**
- **1024-dim is 2.7× richer than our current 384-dim.** Retrieval precision boost at minimal storage cost (4.5KB per embedding for 350M).
- **22 Indic languages.** This is the India-origin wedge. Out-of-the-box Hindi, Bengali, Tamil, Telugu, Marathi support for memoryd queries.
- **Same Liquid AI stack as our VLM and Reasoning models.** Single-vendor alignment reduces compatibility risk.
- **Apache-2.0-equivalent.** No licensing concerns for commercialization.

**Action:** Dan4 to fork LFM2.5-Embedding-350M into memoryd v2 in Q3 2026. Add ColBERT reranker in Q4 2026. **2-week effort to ship.**

**Read it:** https://www.liquid.ai/blog/lfm2-5-retrievers

---

## 3. **Mapping Gemma3 onto an Edge Dataflow Architecture** *(NEW for v93)*
*arXiv:2602.06063, AMD + academic partners, May 2026*

**Why this is #3.** This is the **first paper to publish measured NPU benchmarks for a frontier-grade VLM**. It directly informs our hardware decision for v1 wearable.

**What it reports.**
- Gemma3 deployed on AMD Ryzen AI NPU (tiled dataflow architecture)
- **5.2× faster prefill vs iGPU, 33.5× faster vs CPU**
- **4.8× faster decoding vs iGPU, 2.2× faster vs CPU**
- **67.2× more power-efficient than iGPU, 222.9× more than CPU**
- Compact Q4NX 4-bit quantization format

**Why this matters to us specifically.**
- The PRD's biggest risk is "LFM2.5-VL-450M power draw uncharacterized." This paper gives us the **measured NPU numbers** for a comparable VLM. **67× more power-efficient than iGPU** means we can hit the PRD's 4h battery target without compromise.
- The Q4NX quantization format is novel — worth investigating whether our LFM2.5-VL-450M can be re-quantized to this format.
- The "tiled dataflow architecture" suggests we should target **AMD Ryzen AI Max+ 395** as our v1 SoC (it's on the LFM2.5 launch partner list per v12).

**Action:** Dan3 + Dan2 to study the Q4NX format and tiled dataflow paper. Decide: AMD Ryzen AI Max+ 395 vs Qualcomm SA8295P for the v1 SoC. (AutoNeural, paper #5, validates the Qualcomm path.)

**Read it:** http://arxiv.org/abs/2602.06063

---

## 4. **MAGMA: Multi-Graph Agentic Memory Architecture** *(NEW for v93)*
*arXiv:2601.03236, January 2026*

**Why this is #4.** This is the **best reference architecture for memoryd v3** — our 2027 memory layer that goes beyond vectors into typed relational memory.

**What it does.** Represents each memory across **four orthogonal relational graphs**: semantic, temporal, causal, entity. Retrieval is policy-guided multi-stage graph traversal with a Router that decomposes queries into structured signals. Memory evolves via a dual-stream process that separates latency-sensitive ingestion from compute-intensive consolidation.

**Why this matters to us specifically.**
- **v93's memoryd v2 (Q3-Q4 2026)** is vector + HNSW + ColBERT. Vector-only. **memoryd v3 (H1 2027) needs relational memory** for "you met Priya yesterday at the conference, she mentioned photography" queries — these require entity + temporal + causal reasoning, not just cosine similarity.
- **MAGMA's four-graph design** is the cleanest abstraction we've seen. Beats Mem0 (single graph), Zep (proprietary), GraphRAG (entity-only).
- The **dual-stream ingestion** (fast write path + slow consolidation path) maps directly to our episodic→semantic consolidation cron.
- The **Router + multi-stage traversal** pattern is exactly what `awarenessd` needs for proactive recall.

**Action:** Dan4 + Dan2 to study the MAGMA paper, design memoryd v3 around the four-graph model, defer implementation to H1 2027 (after memoryd v2 ships and we have 30-day real user data).

**Read it:** https://arxiv.org/pdf/2601.03236v1

---

## 5. **AutoNeural: Co-Designing Vision–Language Models for NPU Inference** *(NEW for v93)*
*arXiv:2512.02924, December 2025 + Qualcomm SA8295P validation*

**Why this is #5.** This is the **counterpoint to #3** — if we pick Qualcomm over AMD for the SoC, this is the blueprint.

**What it does.**
- Co-designs vision + language backbones specifically for NPU integer-only inference
- Vision encoder: MobileNetV5-style depthwise separable convolutions (replaces ViT for quantization robustness)
- Language backbone: SSM (State-Space Model) + Transformer hybrid with efficient gated convolutions
- Validated on **Qualcomm SA8295P** (the automotive cockpit NPU)
- **Up to 7× lower quantization error, 14× lower end-to-end latency** vs baselines
- **3× faster decoding, 4× longer context window**
- 6 visual tokens from 16×16 grid with 2048-dim features (token budgeting)

**Why this matters to us specifically.**
- The automotive validation is directly relevant — wearables and automotive cockpits share thermal, power, and latency constraints.
- The SSM+Transformer hybrid is a credible alternative to vanilla transformer attention for the wearable VLM — potentially lower power.
- The 6-visual-token pattern is a hint for our perceptiond: we may not need 256 tokens per frame; 6 may suffice for "describe this scene" tasks.

**Action:** Dan3 to benchmark LFM2.5-VL-450M with SSM-augmented projector on the AMD Ryzen AI (paper #3) vs the Qualcomm SA8295P (paper #5) in Q3 2026. **Pick the SoC in Q3 2026. Hardware procurement in Q4 2026.**

**Read it:** https://arxiv.org/html/2512.02924v2

---

## v93 honorable mentions (would've made v12's list)

- **SEAL: Self-Adapting Language Models** (OpenReview) — the RL-on-self-edit-generation-policy school. Useful template for our SIA-loop "should I update weights?" decision.
- **SGM: Statistical Gödel Machine** (arXiv:2510.10232) — the safety wrapper around arbitrary self-modification. **Use directly with our SIA fork.**
- **Proactive Systems in HCI and AI** (arXiv:2606.25149, June 2026) — the foundational paper for `awarenessd` UX. The 5-pillar framework (timing, appropriateness, user control, transparency, trust) is the design checklist.
- **SPEED-Q** (arXiv:2511.08914) — 2-bit VLM quantization. Worth tracking if we hit thermal wall.
- **LiteVLA on Raspberry Pi 4** (arXiv:2511.05642) — the first published CPU-only wearable VLM benchmark. Use as a power-budget sanity check.

## v93 drops (from v12's list)

- **SemanticXR** (arXiv:2606.12849) — kept as honorable mention; deferred. The object-level mapping concept is good but we don't need it for v1 wearable.
- **MetaAI Recursive Self-Design** (arXiv:2606.09663) — covered indirectly via SIA + SEAL + SGM.
- **Sakana RSI Lab launch materials** — covered by Huxley-Gödel Machine (paper in honorable mentions) + Darwin Gödel Machine.

---

## Reading order for Dan2 / Dan3 / Dan4 (this week)

1. **Liquid AI retrievers blog** (Jun 18) — 30 min read → greenlight memoryd v2 fork
2. **SIA paper** (arXiv:2605.27276) — 2 hours → finalize SIA-on-danlab-multimodal fork plan
3. **MAGMA paper** (arXiv:2601.03236) — 1.5 hours → memoryd v3 design notes
4. **AMD Ryzen AI Gemma3 paper** (arXiv:2602.06063) — 1 hour → Q4 2026 hardware decision
5. **AutoNeural** (arXiv:2512.02924) — 1 hour → SSM-augmented projector spike plan

**Total: 6 hours of reading → 5 concrete Q3 2026 decisions.**

---

## Why the rotation

v12's list was foundational. v93's list is **action-oriented for Q3 2026**. Specifically:
- **SIA** stayed because the danlab-multimodal → SIA fork is still the headline AGI roadmap item.
- **LFM2.5 Retrievers** replaced SemanticXR because the timing is now (shipped Jun 18, 8 days ago).
- **Gemma3 + AMD Ryzen AI** replaced Sakana RSI launch because hardware NPU benchmarks are now published, which directly unblocks the wearable power question.
- **MAGMA** is a memory architecture upgrade — needed for memoryd v3 design.
- **AutoNeural** is the Qualcomm counterpart to AMD's Gemma3 paper — needed for SoC decision.

**The throughline:** v12's reads were about *understanding the landscape*. v93's reads are about *making the next 90 days of decisions concrete*. 👾