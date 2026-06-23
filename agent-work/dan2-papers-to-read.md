# Top 5 Research Papers to Read — v40
**Author:** Dan2
**Date:** 2026-06-23
**For:** somdipto + the Danlab team

> **v40 change:** Replaces v39 #1 (HeLa-Mem) with **HRM-Text (Sapient)** as the #1 read. v40 #2 is **SIA (Hexo Labs)** with the verified W+H numbers. v40 #3-5 cover the new memory architecture stack (Infini Memory, MemVerse, CMA) and the wearable power reference (OpenGlass).

> If you read only one, read #1. If you read only two, read #1 and #2.

## #1. HRM-Text: Efficient Pretraining Beyond Scaling (Sapient)
**arXiv:** 2605.20613 (May 2026)
**GitHub:** https://github.com/sapientinc/HRM-Text (MIT-licensed)
**HuggingFace:** sapientinc/HRM-Text-1B
**Why this matters:** This is the first credible demonstration that **a 1B model trained for $1,500 can match 2-7B open models on reasoning benchmarks**. The implication for Danlab is enormous: we can own our reasoning stack instead of renting it from a U.S. foundation-model lab. The model is fully open-source, the training recipe is public, and the architecture (hierarchical recurrent with two timescales: slow high-level + fast low-level) is well-suited to wearable compute. HuggingFace CEO publicly endorsed it; Yoshua Bengio's team linked GRAM to HRM in a separate paper.

**Key ideas to extract:**
- The H/L two-time-scale architecture. A slow strategic layer + a fast execution layer. Iterative H_cycles × L_cycles forward passes yield deep effective computation.
- The sample efficiency story: 40B tokens (vs trillions for typical small models) and ~$1,500 training cost.
- The benchmark parity: GSM8K 84.5%, MATH 56.2%, DROP 82.2%, MMLU 60.7%, ARC-C 81.9%.
- The limits: weak on coding (no code-heavy training data), weak on knowledge benchmarks vs. much larger models.
- The Latent Reasoning thesis: HRM-Text operates in latent space, not in token stream. This is a quiet rebuke to chain-of-thought.
- The fine-tuning behavior: improvements on some benchmarks (GSM8K, BoolQ) and regressions on others (MMLU, ARC-C) due to formatting changes. v1.5 must characterize this on our domain.

**Direct application:** This is the reasoning model for Dan Glasses v1.5. We adopt HRM-Text-1B as the base, fine-tune on our domain (voice transcripts + memory schemas + salience decisions + tool-call traces), and ship. The v40 roadmap allocates 2-3 months for this work. The training cost is well within our budget.

**Reading time:** 2-3 hours for the paper, 1 day to understand the architecture, 1 week to design our fine-tuning pipeline.

## #2. SIA: Self-Improving AI with Harness & Weight Updates (Hexo Labs)
**arXiv:** 2605.27276
**GitHub:** https://github.com/hexo-ai/sia (MIT-licensed)
**Why this matters:** This is the canonical open-source self-improving agent framework. The SIA-W+H (harness + weights) numbers are real and verified:
- **LawBench (191-class Chinese legal classification):** baseline 13.5% → SIA-H 50.0% → SIA-W+H **70.1%** (vs prior SOTA 45%, **+25.1pp**).
- **TriMul CUDA kernel:** SIA-W+H **1,017 μs** (vs prior SOTA 1,161 μs, **-12.4%**).
- **scRNA-seq denoising:** SIA-W+H mse_norm **0.289** (vs prior SOTA 0.240, **+20.4%**).

The lesson: **harness-only plateaus around 50% on LawBench; weight updates add another +20pp.** This is the empirical justification for our v1.5 weight-update loop.

**Key ideas to extract:**
- The three-agent pattern: Meta-Agent generates the initial Target Agent; Feedback Agent analyzes logs and updates the Target Agent.
- The "harness" concept: scaffold around the model (prompts, tools, retry logic, search). Updated in v1.
- The "weights" concept: LoRA on a 120B model (GPT-OSS-120B, LoRA rank 32). Updated in v2 with opt-in federated training.
- The reward algorithm selector: PPO+GAE for dense step-level rewards, GRPO for sparse, EAW for right-skewed. This is a real research contribution.
- The per-generation artifact pattern: `target_agent.py`, `agent_execution.json`, `improvement.md` for each generation. We can inspect what changed and roll back.
- The CLI: `sia run` and `sia web` (visualizer for runs).

**Direct application:** Adopt the harness loop in v1 (SIA-H pattern). Add weight updates in v2 (SIA-W+H pattern) on our own HRM-Text-1B. This is the blueprint for our self-improvement roadmap.

**Reading time:** 2 hours for the paper, 1 day to understand the code, 1 week to integrate the pattern.

## #3. Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory
**arXiv:** 2606.10677v1 (Jun 2026)
**Why this matters:** The cleanest practical memory architecture for a personal AI agent. Topic-structured documents as the storage primitive. Each topic document is a semantic unit that collects related evidence, preserves metadata, and revises facts over time. Agentic retrieval at inference time via iterative tool calls (not a single retrieval step). This is exactly the v40 pivot for memoryd v2.

**Key ideas to extract:**
- The topic-document storage primitive. Replaces the flat vector store.
- The iterative retrieval procedure: the LLM reads memory through multiple tool calls. This is a more flexible pattern than single-shot RAG.
- The topic-structured maintenance: related facts live in the same document, with explicit revision history.
- The ablations: topic-structured maintenance + iterative evidence inspection improve complementary aspects of long-term memory.

**Direct application:** This is the architecture for memoryd v2 (Dec 2026). The topic-document primitive + agentic retrieval replaces the flat vector store. We can build on this directly.

**Reading time:** 2 hours for the paper, 1-2 days to implement the core pattern.

## #4. OpenGlass: Ultra-Low-Power On-Device AI Eyewear with Event-based Vision
**arXiv:** 2606.07431v2 (Jun 2026)
**Why this matters:** The canonical academic reference for on-device AI eyewear. The power/performance numbers (67.4 mW continuous, 11.5 hours on 200 mAh) are exactly the targets we should be aiming for. The hardware-software co-design pattern (GAP9 RISC-V + event camera) is the right reference for our wearable design.

**Key ideas to extract:**
- The two-domain architecture: offload BLE to a secondary MCU (nRF5340) to save >3x power during data transmission. We should do the same — offload the always-on wake word to a tiny secondary chip.
- The phase-based power trace: cold start (~14.6 mW), camera bring-up (~180 mW), continuous inference (~67.4 mW, bursts up to ~96 mW). This is the kind of instrumentation we need.
- The runtime estimate: 5.2 mJ per inference cycle. This is the per-call energy budget we should target.
- The modular interposer pattern: support rapid prototyping of sensors and embedded ML.

**Direct application:** Reference design for Dan Glasses hardware integration. The power numbers are the targets. The architecture pattern is the template. The instrumentation approach is what we should copy.

**Reading time:** 1.5 hours for the paper, 1 day to internalize the power budget.

## #5. MemVerse: Multimodal Memory for Lifelong Learning Agents
**arXiv:** 2512.03627v2 (Dec 2025, updated 2026)
**Why this matters:** The first framework that combines fast parametric recall with hierarchical retrieval for multimodal lifelong learning. Two ideas we should adopt: (1) the **periodic distillation** mechanism that compresses essential knowledge from the cognitive graph into the parametric model, providing fast and differentiable recall while preserving interpretability; (2) the **hierarchical retrieval** pattern that combines short-term and long-term memory.

**Key ideas to extract:**
- The two-memory architecture: short-term memory for recent context + long-term memory graph.
- The periodic distillation: compress graph → parametric memory. This is the missing piece for our memoryd v3.
- The continuous learning mechanism: short-term → long-term → distilled to parametric, in a loop.
- The multimodal support: vision + text + audio memory in one framework.

**Direct application:** MemVerse's periodic distillation is the v40 spec for memoryd v3 (Jun 2027). The "compress long-term memory to parametric" pattern is what makes on-device retrieval fast and private.

**Reading time:** 1.5 hours for the paper, 1 day to internalize the architecture.

---

## Bonus reads (read these if you have time)

- **SIA** (arXiv 2605.27276) — already #2. The code is the real reference.
- **HRM-Text** (arXiv 2605.20613) — already #1. HuggingFace model card is the shortest read.
- **Sakana RSI Lab launch** — the broader context. Worth a 30-min read.
- **HeLa-Mem** (arXiv 2604.16839) — the v39 #1 read. Still relevant; the Hebbian learning idea maps to our memoryd v2.
- **CMA: Continuum Memory Architectures** (arXiv 2601.09913) — the v39 #2 read. The four-stage lifecycle is the operational spec.
- **MEMO: Memory as a Model** (May 2026) — Qwen2.5-14B trained as a dedicated memory model + Gemini-3-Flash executive. 54.22% on BrowseComp-Plus. The "train a small model to BE memory" pattern.
- **Nanomind** (arXiv 2510.05109v6) — 0.375W continuous VLM on 2000 mAh = 18.8h. The wearable VLM power reference.
- **TinyissimoYOLO** (arXiv 2311.01057) — 62.9 mW wearable detection. The salience pre-filter reference.
- **Anthropic Mythos Fable 5** (Jun 2026) — the new safety-tier model. Read the safety docs, not the marketing.
- **Meta Ray-Ban Display coverage** (Jun 2026) — the competitive anchor.

## Reading order

If you have one week, read in this order:
1. HRM-Text paper and HuggingFace card (#1) — 1 day, understand the new economics.
2. SIA paper and code (#2) — 1 day, understand the self-improvement pattern.
3. OpenGlass paper (#4) — 1 day, understand the hardware-software co-design.
4. Infini Memory paper (#3) — 1 day, understand the memory architecture.
5. MemVerse paper (#5) — 1 day, internalize the multimodal lifelong learning framework.

If you have one day, read in this order:
1. HRM-Text HuggingFace card (#1) — 1 hour.
2. SIA GitHub README (#2) — 2 hours.
3. OpenGlass paper (#4) — 2 hours.

If you have one hour, read:
1. This document's TL;DR.
2. HRM-Text HuggingFace card.
3. SIA GitHub README.

---

*Dan2 research agent, 2026-06-23 v40. Top 5 papers selected for highest leverage on Danlab's roadmap.*
