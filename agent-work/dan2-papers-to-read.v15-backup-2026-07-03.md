# Dan2 — Papers to Read v15 (2026-07-03 10:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-papers-to-read.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v14:** `dan2-papers-to-read.v14-backup-2026-07-03.md`

> **v15 deltas vs v14 (1 CRITICAL add to the top-5, 2 honorable mentions, 0 retractions):**
> 1. **NEW — Top-5 add: "Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC" (arXiv 2606.27906, late June 2026).** v15 CRITICAL #1 paper. The v1.0 wearable execution substrate is now phase-mapped heterogeneous inference (vision encoder → NPU, text decode → CPU, salience gating → low-power DSP). 1.64× NPU prefill, 1.18× NPU decode, 2.52× vision-encoder energy reduction.
> 2. **NEW — Honorable mention: OpenPhone-3B paper (HKUDS, ACL 2026, late June 2026).** Two-layer self-learning memory (Ralph Loop). 3B on-device agentic foundation model. v1.5 audiod post-processor plan-C.
> 3. **NEW — Honorable mention: AI agents threaten research grant awarding (Inside Higher Ed, July 2 2026, citing UCL Rees + Wilsdon).** v15 responsible-AI evidence. Dan Glasses helps the researcher *understand* their data, not auto-generate grant applications.

> **v15 retractions of v14:** **none.** The v14 top-5 holds. The v15 add is the Phase Matters paper to the top-5 and 2 honorable mentions.

---

## TL;DR (one paragraph, v15)

The v14 top-5 holds. **v15 elevates "Phase Matters" (arXiv 2606.27906) to the top-5 as the v1.0 wearable execution substrate paper.** The Dan Glasses 6/12/24-month reading list now centers on: (1) Memora + Phase Matters for v1.0/v1.5 architecture, (2) SIA + Red Queen for v1.5/v2.0 agent loop, (3) HRM-Text-1B + OpenPhone-3B for v1.5 audiod post-processor, (4) Qwen3-TTS + Chatterbox for v1.5 TTS, (5) MiCRo for the multi-daemon decomposition academic citation.

---

## Top 5 Papers to Read (v15 ranking)

### 1. "Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC" (arXiv 2606.27906, late June 2026) — **NEW v15 CRITICAL #1**

- **Why this paper:** The v1.0 wearable execution substrate is now defined. NPU prefill 1.64× faster than CPU, NPU decode 1.18× faster, vision encoders 2.52× lower energy on NPU. Always-on mobile VLM is feasible with careful NPU offload.
- **Key takeaway:** VLM inference on a phone SoC requires phase-mapped heterogeneous NPU/CPU/GPU inference, not "small model on CPU." The 4hr battery target is now reachable.
- **What we will do with it:** 1-week Q3 W1 `perceptiond.phase_map` architecture spike. Vision encoder → NPU (QNN/Hexagon on Snapdragon), text decode → CPU, salience gating → low-power DSP.
- **Effort to read:** 30 minutes.
- **Link:** https://arxiv.org/html/2606.27906v1.

### 2. "Microsoft Memora" (Microsoft Research, July 2026) — held from v14 #1

- **Why this paper:** The v1.5 memoryd architecture target. Decouples "what is stored" from "how it is retrieved." Reduces context token usage by up to 98% while matching or exceeding full-context accuracy.
- **Key takeaway:** Rich procedural memories stored with full embedding vectors; lightweight semantic abstractions stored with indexable keys; retrieval via a 2-stage pipeline.
- **What we will do with it:** 2-week Q3 W1-W2 memoryd v1.5 port. New `/v1/retrieve` endpoint, new `/v1/abstractions` write path. `auto_apply=False` contract still binds.
- **Effort to read:** 1 hour.
- **Link:** https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity.

### 3. "HRM-Text-1B" (Sapient, June 2026) — held from v11 #1

- **Why this paper:** The v1.5 audiod post-processor plan-A. 1B params, Apache-2.0, $1,500 trained from scratch. Hierarchical reasoning model architecture.
- **Key takeaway:** Small-beats-large is now empirically real. $1,500 training cost is the killer story.
- **What we will do with it:** Q1 W1-W2 audiod post-processor upgrade.
- **Effort to read:** 1 hour.
- **Link:** https://www.sapient.ai/blog/hrm-text-1b

### 4. "Red Queen Gödel Machine" (arXiv 2606.26294, June 24 2026) — held from v12 #3

- **Why this paper:** The 2026 strongest paper for self-improving agents. The 1.91× → ~1.0× bias-correction result on the moving-judge pattern.
- **Key takeaway:** The agent can self-improve by changing its own judge. The "moving-judge" pattern is the implementation of the v11 `auto_apply=False` contract.
- **What we will do with it:** Port to danlab-multimodal as the v1.5 plan-A for the agent loop.
- **Effort to read:** 2 hours.
- **Link:** https://arxiv.org/abs/2606.26294

### 5. "EPFL MiCRo: Mixture of Cognitive Reasoners" (late June 2026) — held from v14 #5

- **Why this paper:** Validates the 4-specialized-brain-region pattern in monolithic LLMs. The Dan Glasses 5-daemon split is the engineering analogue.
- **Key takeaway:** The 2026 academic SOTA is "specialized brain regions." We shipped the 5-region split 6 months ago.
- **What we will do with it:** Cite in v1.0 marketing as the academic validation of the decomposition.
- **Effort to read:** 1 hour.
- **Link:** https://www.epfl.ch/research/domains/ai/micro-mixture-of-cognitive-reasoners/

---

## Honorable Mentions (v15)

1. **"Microsoft Memora: A Harmonic Memory Representation Balancing Abstraction and Specificity" (Microsoft Research, July 2026).** The 98% context token reduction at full-context accuracy. The v14 memoryd v1.5 architecture target.
2. **"SIA: Self-Improving Agent" (Hexo Labs, MIT, May 2026).** The SIA-W+H port is the v11/v12 publishing bet. 350x acceleration, 14x GPU kernel speedup, 45% → 70% legal task accuracy.
3. **"Microsoft Scout" (Microsoft Build 2026, June 2 2026).** Microsoft Scout is built on OpenClaw. Validates the agent-OS substrate. v11 carry.
4. **"VisualClaw: Self-Evolving Multimodal Agent for AI Glasses" (Mervin Praison, June 2026).** 98% cost reduction + +15.8% accuracy. The cascade-gate pattern. v8 carry.
5. **"Diagnosing the Memory-Update Gap" (arXiv 2606.27472, June 2026).** Frontier models drop 92% → 77% on supersession tasks. v8 carry.
6. **"Ollie: Gaze-Informed Proactive AI" (arXiv 2607.00445, July 1 2026).** The v12 proactived v1 architecture source. v12 carry.
7. **"Apertus v1.1 4B Instruct" (Swiss AI / EPFL, June 29 2026).** EU-provenance open-weights. v14 plan-B.
8. **"Anthropic Mythos + Mythos 5 Glasswing" (Anthropic, June 2026).** Gated to US Glasswing partners, $30K catch. v9 carry.
9. **"GLM-5.2" (Z.ai, MIT, late June 2026).** Mythos-class open-weights. v13 research bet.
10. **"OpenPhone-3B" (HKUDS, ACL 2026, late June 2026).** 3B on-device agentic foundation model with two-layer self-learning memory. v15 plan-C for v1.5 audiod post-processor.

---

## v15 Open Questions for somdipto

1. **Phase Matters paper — read this week or next?** (recommend: this week, 1 hour, before the Q3 W1 phase_map spike starts)
2. **Memora paper — already at top-5, but read it again with the storage/retrieval split pattern as the v1.5 architecture target?** (recommend: yes, 1 hour, before the Q3 W1-W2 Memora port starts)
3. **OpenPhone-3B — read alongside HRM-Text-1B and Apertus v1.1 4B as the v1.5 audiod post-processor shortlist?** (recommend: yes, 1 hour, before the 2-day evaluation spike)
4. **Microsoft Frontier Co. + Palantir buy-the-dip — both are analyst/industry signals, not papers; cite in v1.0 marketing but do not add to the top-5?** (recommend: yes, marketing copy only)
5. **Red Queen Gödel Machine — already in top-5, port to danlab-multimodal in Q4 2026?** (recommend: yes, 4 weeks, 1 engineer)

---
## Footnotes (v15)

[^1]: https://arxiv.org/html/2606.27906v1 — "Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC"
[^2]: https://www.sapient.ai/blog/hrm-text-1b
[^3]: https://arxiv.org/abs/2606.26294
[^4]: https://www.epfl.ch/research/domains/ai/micro-mixture-of-cognitive-reasoners/
[^5]: https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity
[^6]: https://github.com/HexoLabs/SIA
[^7]: https://github.com/MervinPraison/VisualClaw
[^8]: https://arxiv.org/abs/2607.00445
[^9]: https://huggingface.co/ApertusAI/Apertus-4B-Instruct
[^10]: https://github.com/HKUDS/OpenPhone
