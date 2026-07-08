# Dan2 — Papers to Read v16 (2026-07-03 11:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-papers-to-read.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v15:** `dan2-papers-to-read.v15-backup-2026-07-03.md`

> **v16 deltas vs v15 (1 Top-5 add, 1 honorable mention add, 1 demotion, 0 retractions):**
> 1. **NEW — Top-5 add: "As We May Search: Local-First Information Retrieval" (arXiv 2606.29652, late June 2026).** v16 Top-5 #5. Academic local-first IR validation. 91% nDCG@10 up to 100K documents, 1M with HNSW at 2% quality loss, 7B local LLM within 4 points of cloud baseline. **The memoryd v1.5 storage/retrieval split is now an empirical certainty.**
> 2. **NEW — Honorable mention: LFM2.5-230M (Liquid AI, June 26 2026) and its technical report.** 230M params, 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5, beats Qwen3.5-0.8B and Gemma 3 1B on instruction following and data extraction. **v1.0 audiod post-processor (displaces v15's HRM-Text-1B as plan-A).** Read alongside HRM-Text-1B, Apertus v1.1 4B, and OpenPhone-3B for the v1.5 audiod post-processor shortlist.
> 3. **NEW — Honorable mention: Hermes Agent technical report (Nous Research, late June 2026).** Mixture-of-agents pattern. 11% higher than GPT-5.5 on hard agentic benchmarks. **v1.0 audiod agent framework plan-A.** Read before the Q3 W2 spike.
> 4. **DEMOTION — HRM-Text-1B from #3 to outside top-5.** v15 had HRM-Text-1B at #3. v16 demotes HRM-Text-1B to honorable mention because LFM2.5-230M is now the v1.0 audiod post-processor and HRM-Text-1B is v1.5 plan-B.

> **v16 retractions of v15:** **none.** The v15 top-5 holds (with the As We May Search add) and HRM-Text-1B is now honorable mention (not top-5).

## TL;DR (one paragraph, v16)

The v15 top-5 holds, with v16 adding "As We May Search" (arXiv 2606.29652) as the academic local-first IR validation paper. **The v16 reading list centers on: (1) Phase Matters + As We May Search for v1.0/v1.5 architecture, (2) SIA + Red Queen for v1.5/v2.0 agent loop, (3) Memora for v1.5 memoryd, (4) Hermes Agent for v1.0 audiod agent framework, (5) LFM2.5-230M technical report for v1.0 audiod post-processor.** HRM-Text-1B demotes from top-5 to honorable mention (v1.5 plan-B). No v15 paper is retracted.

## Top 5 Papers to Read (v16 ranking)

### 1. "Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC" (arXiv 2606.27906, late June 2026) — held from v15 #1

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

### 3. "Red Queen Gödel Machine" (arXiv 2606.26294, June 24 2026) — held from v12 #3

- **Why this paper:** The 2026 strongest paper for self-improving agents. The 1.91× → ~1.0× bias-correction result on the moving-judge pattern.
- **Key takeaway:** The agent can self-improve by changing its own judge. The "moving-judge" pattern is the implementation of the v11 `auto_apply=False` contract.
- **What we will do with it:** Port to danlab-multimodal as the v1.5 plan-A for the agent loop.
- **Effort to read:** 2 hours.
- **Link:** https://arxiv.org/abs/2606.26294.

### 4. "SIA: Self-Improving AI with Harness & Weight Updates" (Hexo Labs, MIT, June 2026) — held from v11

- **Why this paper:** The SIA framework is the open-weights, MIT-licensed self-improving agent pattern. The SIA-W+H (with hindsight) port is the v1.5 publishing bet. SIA-H is the base; SIA-W+H is the open-source counter-narrative to Anthropic Dreaming (closed-source) and Mirendil (a16z, watch).
- **Key takeaway:** Self-improving loop where a Feedback-Agent updates both the harness and the weights. Beats Karpathy's autoresearcher agent by improving itself.
- **What we will do with it:** Q3 W3-Q4 W2 SIA-W+H port. 4 weeks, 1 engineer + $200-500/mo cloud GPU. arXiv draft + ICML/ACL 2027 submission.
- **Effort to read:** 1.5 hours.
- **Link:** https://github.com/HexoLabs/sia.

### 5. "As We May Search: Local-First Information Retrieval" (arXiv 2606.29652, late June 2026) — NEW v16

- **Why this paper:** Academic local-first IR validation. Dense retrieval keeps over 91% nDCG@10 up to 100K documents; approximate HNSW indexes extend to 1M with only 2% quality loss; 7B local language model reaches within 4 points of a cloud baseline on answer quality.
- **Key takeaway:** The on-device memoryd architecture is now an *empirical certainty*. Memora (98% context reduction) + As We May Search (91% nDCG@10) = the storage/retrieval split is the 2026 SOTA. The v1.5 memoryd port is now over-determined.
- **What we will do with it:** Cite in v1.0 marketing as the academic validation of on-device memory. Read before the Q3 W1-W2 Memora port.
- **Effort to read:** 1 hour.
- **Link:** https://arxiv.org/abs/2606.29652.

## Honorable Mentions (v16)

1. **"LFM2.5-230M Technical Report" (Liquid AI, June 26 2026).** 230M params, 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5. Beats Qwen3.5-0.8B and Gemma 3 1B. v1.0 audiod post-processor. **NEW v16.**
2. **"Hermes Agent" (Nous Research, late June 2026).** Mixture-of-agents pattern. 11% higher than GPT-5.5 on hard agentic benchmarks. v1.0 audiod agent framework plan-A. **NEW v16.**
3. **"EPFL MiCRo: Mixture of Cognitive Reasoners" (late June 2026).** Validates the 4-specialized-brain-region pattern. v14 #5, demoted to honorable mention in v16.
4. **"VisualClaw: Self-Evolving Multimodal Agent for AI Glasses" (Mervin Praison, June 2026).** 98% cost reduction + +15.8% accuracy. The cascade-gate pattern. v8 carry.
5. **"Diagnosing the Memory-Update Gap" (arXiv 2606.27472, June 2026).** Frontier models drop 92% → 77% on supersession tasks. v8 carry.
6. **"Ollie: Gaze-Informed Proactive AI" (arXiv 2607.00445, July 1 2026).** The v12 proactived v1 architecture source. v12 carry.
7. **"Apertus v1.1 4B Instruct" (Swiss AI / EPFL, June 29 2026).** EU-provenance open-weights. v1.5 audiod post-processor plan-C.
8. **"OpenPhone-3B" (HKUDS, ACL 2026, late June 2026).** 3B on-device agentic foundation model. v1.5 audiod post-processor plan-D.
9. **"HRM-Text-1B" (Sapient, June 2026).** $1,500 trained, 1B params, Apache-2.0. **v16 demote from top-5 to honorable mention (v1.5 plan-B, was v1.0 plan-A in v15).**
10. **"Anthropic Mythos 5 + Fable 5 export ban lifted" (US Commerce Department, June 30 - July 1 2026).** Industry signal, not a paper. Fable 5 now globally available; Mythos 5 partially open to US Glasswing + ~100 critical-infrastructure organizations. **v16 partial retraction of v15's "$30K catch" framing.**

## v16 Open Questions for somdipto

1. **As We May Search paper — read this week or next?** (recommend: this week, 1 hour, before the Q3 W1-W2 Memora port starts)
2. **LFM2.5-230M technical report — read alongside HRM-Text-1B / Apertus v1.1 4B / OpenPhone-3B / Hermes Agent as the v16 5-way shortlist?** (recommend: yes, 1 hour each)
3. **Hermes Agent — read before the Q3 W2 spike?** (recommend: yes, 1 hour)
4. **Phase Matters paper (v15 #1) — read before the Q3 W1 phase_map spike starts?** (recommend: yes, 30 minutes, before Q3 W1)
5. **Microsoft Frontier Co. + Palantir buy-the-dip + AWS FDE + DoD GenAI.mil + GPT-5.6 + Anthropic Fable 5 — all are analyst/industry signals, not papers; cite in v1.0 marketing but do not add to the top-5?** (recommend: yes, marketing copy only)
6. **Red Queen Gödel Machine (v12 #3) — port to danlab-multimodal in Q4 2026?** (recommend: yes, 4 weeks, 1 engineer)
7. **HRM-Text-1B demotion to honorable mention — confirm?** (recommend: yes, LFM2.5-230M is the v1.0 target)

## Footnotes (v16)

[^1]: https://arxiv.org/abs/2606.29652 — "As We May Search: Local-First Information Retrieval" (NEW v16)
[^2]: https://arxiv.org/html/2606.27906v1 — "Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC" (held from v15)
[^3]: https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity — Microsoft Memora (held from v14)
[^4]: https://arxiv.org/abs/2606.26294 — "Red Queen Gödel Machine" (held from v12)
[^5]: https://github.com/HexoLabs/sia — SIA: Self-Improving AI with Harness & Weight Updates (held from v11)
[^6]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M, Liquid AI (NEW v16)
[^7]: https://www.nousresearch.com/agents/hermes — Hermes Agent, Nous Research (NEW v16)
[^8]: https://github.com/MervinPraison/VisualClaw — VisualClaw (held from v8)
[^9]: https://arxiv.org/abs/2607.00445 — Ollie: Gaze-Informed Proactive AI (held from v12)
[^10]: https://www.sapient.ai/blog/hrm-text-1b — HRM-Text-1B, Sapient (demoted from v15 #3 to honorable mention in v16)

## v15 papers-to-read content (preserved in backup)

The v15 papers-to-read (preserved in `dan2-papers-to-read.v15-backup-2026-07-03.md`) covers: Phase Matters (top-5 #1), Memora (#2), HRM-Text-1B (#3), Red Queen Gödel Machine (#4), MiCRo (#5), plus 10 honorable mentions. **All v15 content is preserved verbatim in the backup. The v16 add is "As We May Search" to the top-5, LFM2.5-230M and Hermes Agent as honorable mentions, and HRM-Text-1B demoted from #3 to honorable mention. The v15 top-5 holds (with As We May Search replacing HRM-Text-1B).**
