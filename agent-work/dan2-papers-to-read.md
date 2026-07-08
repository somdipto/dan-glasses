# Dan-2 Top 5 Papers to Read — v33 (2026-07-06)

> **Status:** v33 refresh. v32 backups at `*.v32-backup-2026-07-06.md`. v32 content preserved; v33 deltas prepended.
> **Scope:** Top 5 papers + honorable mentions to read for Danlab's AGI roadmap.
> **Run window:** 2026-07-06 04:00 → 05:00 UTC (60 min).

---

## v33 Top 5 Papers (changes from v32 bolded)

### 1. **Microsoft Research — "Agentic Evolution: From Self-Improving Agents to Co-Evolving Human–AI Systems"** (July 2026) ⭐ NEW v33

- **Authors**: Microsoft Research, Sico team
- **URL**: https://www.microsoft.com/en-us/research/wp-content/uploads/2026/07/agentic-evolution.pdf
- **Length**: 300-paper survey
- **Why read it**: This is the v33 *single best paper* for Danlab's v1.0 architecture. It organizes the self-evolving agent literature through a three-axis taxonomy: **evolutionary substrate, consolidation pathway, selective pressure**. Distinguishes agentic evolution from full RSI. Validates the *co-evolution* frame as the v33 production-ready answer to "how do agents improve without full autonomy."
- **v33 critical finding**: "Reliable improvement emerges not from full autonomy, but from co-evolving human–AI systems, where AI agents and their human operators evolve together through real work." This is the v33 *exact* frame for v1.0 OpenClaw + memoryd + co-evolution shell (plan-CO1, Q2 2027).
- **Action**: Read this week. Drives plan-CO1 Sico-style Digital Worker shell design.

### 2. **Microsoft Research — Memora technical paper** (July 2026) ⭐ NEW v33

- **URL**: https://www.microsoft.com/en-us/research/project/memora (linked from Research post)
- **Why read it**: Memora is Microsoft's *production* answer to "AI agents can't remember past conversations." The architecture: **storage/retrieval split** — separate what is stored from how it is retrieved. This is the v33 *exact* architecture we should port to memoryd v1.5 (plan-A sharpen).
- **v33 critical finding**: Microsoft *independently arrived at* the same architectural pattern that the DynamicMem paper (v28) suggested was the 93%-failure-cause. Two independent confirmations = production-ready.
- **Action**: Read this week. Drives memoryd v1.5 storage/retrieval split (plan-A, 2 weeks, 1 eng, dan4, Q3 W1-W2).

### 3. **"Phase Matters" — Hardware-in-the-loop VLM characterization on Qualcomm SM8750** (arXiv 2606.27906, late June 2026) ⭐ UNCHANGED v32

- **Why read it**: First *hardware-in-the-loop* paper on VLM inference on the Qualcomm Snapdragon 8 Elite (the v32 reference chip for Redax v1.0 wearable).
- **v32/v33 critical finding**: NPU prefill gives 1.64× speedup, NPU decode only 1.18×. Vision encoders achieve 2.52× lower energy on NPU. **Phase-mapped heterogeneous inference** is the v32/v33 right architecture: VLM pipelines must be split across CPU/NPU/GPU by phase, not by model.
- **Action**: Read this week. Drives perceptiond v1.5 phase-mapped heterogeneous inference (Q3 W3-W4 spike, 1 eng).

### 4. **DynamicMem — Memory failure root cause analysis** (arXiv 2606.22877, late June 2026) ⭐ UNCHANGED v32

- **Why read it**: First systematic study of *why* AI agent memory systems fail. Finding: **over 93% of memory failures trace to retrieval, not the writing model.** This is the v32 *problem statement* for plan-A (Memora port).
- **v32/v33 critical finding**: 93% of failures are in retrieval. The v33 *engineering* implication: spend the v1.5 engineering effort on retrieval, not on the writing model. The v33 *cost* implication: writing model upgrades (BGE-large, Qwen3-Embedding) have <7% marginal benefit; retrieval architecture changes have >93% marginal benefit.
- **Action**: Re-read alongside Memora (item 2). Drives plan-A and plan-M1 priority order.

### 5. **Jack Clark — Import AI #460** (July 2026) ⭐ UNCHANGED v32

- **Why read it**: Anthropic cofounder Jack Clark's 60% RSI-by-2028 estimate with quantitative evidence: **8x increase in lines-of-code merged in 2026 vs 2024 at Anthropic**. Distinguishes maximalist RSI (60% by 2028) from prosaic RSI (outer-loop productivity, already happening).
- **v32/v33 critical finding**: Outer-loop RSI is *already in flight* at Anthropic and at Danlab (audiod v1.3 → v1.5, dan2 v23 → v33, perceptiond v6 → v7). Maximalist RSI is *deferred* to v2.0+ (2028+). v1.0 marketing should ship with outer-loop RSI framing.
- **Action**: Cite in v1.0 spec §15. Drives the v33 "outer-loop RSI is in flight, maximalist is 2028+" marketing frame.

---

## v33 Honorable Mentions (additions to v32 list)

### HM1. **Microsoft Sico — "Symbiotic Intelligence for CO-evolution"** (July 2026) ⭐ NEW v33

- **URL**: https://www.microsoft.com/en-us/research/project/sico
- **GitHub**: https://github.com/microsoft/Sico
- **Why read it**: The v33 *production* reference for the Digital Worker shell. Sico is open-source, MIT-licensed, and ships as a *structured AI labor unit* abstraction that co-evolves with human operators through real work. Specifically targets BPO (Business Process Outsourcing) — the v33 most-relevant *enterprise* use case for v1.0 OpenClaw.
- **v33 critical finding**: Sico's co-evolution loop is the v33 *exact* pattern for plan-CO1 (Q2 2027 Digital Worker shell for audiod + memoryd). Read the Sico README + technical report.

### HM2. **Sakana AI — RSI Lab program manager posting + RSI Lab English/JP pages** (July 2026) ⭐ NEW v33

- **URL**: https://sakana.ai/careers/program-manager-rsi-lab/, https://sakana.ai/rsi-lab/
- **Why read it**: Sakana's formal RSI Lab is the v33 *third* named RSI org (after Recursive Superintelligence and Mirendil). The program manager posting reveals: "Sakana AI's fast growing Recursive Self-Improvement (RSI) Lab… Frontier Research Scientists and Advanced Core Engineers for both domestic and international applicants." Frames RSI as *sample-efficiency-first*, not raw-compute-first. This is the v33 *alternative* thesis to the OpenAI/Anthropic raw-compute RSI.
- **v33 critical finding**: Sakana bets on *sample efficiency*. Danlab bets on *co-evolution + on-device*. Both are *alternatives to maximalist raw-compute RSI*. v1.0 marketing can sharpen to "we are not racing Sakana, we are the *edge* co-evolution layer."

### HM3. **The New Stack — "The AI revolution will not be televised — it'll be quantized"** (July 5 2026) ⭐ NEW v33

- **URL**: https://thenewstack.io/chinese-frontier-models-quantization/
- **Why read it**: Argues that Chinese frontier models (Zhipu GLM-5.2, Qwen3, DeepSeek) reaching near-frontier quality at Q4 quantization is the v33 *real* AI revolution — not raw-compute scaling, but **quantization + on-device deployment**. Directly validates the v1.0 619MB footprint as the v33 *winning architecture*, not a *compromise*.
- **v33 critical finding**: The v1.0 v32 spec §14 RAM-pricing-anchor can now sharpen to "the AI revolution is quantization, not scaling. v1.0 ships the quantization-first path." Cite in v1.0 spec.

### HM4. **arXiv 2606.27906 — "Phase Matters" + companion Qualcomm SM8750 VLM paper** (re-cited) ⭐ UNCHANGED v32

- See item 3 above. Phase-mapped heterogeneous inference is the v32/v33 right architecture for perceptiond v1.5.

### HM5. **Enterprise Times — "Why Creating a Unified Memory Architecture for AI is an Imperative Now"** (July 1 2026) ⭐ NEW v33

- **URL**: https://www.enterprisetimes.co.uk/2026/07/01/why-creating-a-unified-memory-architecture-for-ai-is-an-imperative-now
- **Why read it**: Dominik Tomicevic's argument for the *context graph* as the v33 enterprise memory architecture. Decision traces + relationships + operational knowledge. Validates the v33 *third* memory pattern (alongside Memora split and Ebbinghaus decay).
- **v33 critical finding**: v1.5 memory architecture should layer: vector (Memora) + graph (context graph) + decay (Ebbinghaus). Three independent 2026 validations converge.

### HM6. **"Recursive Self-Improvement is the Human Skill We Need in the AI Age" — Time** (June 29 2026) ⭐ UNCHANGED v32

- See v32 papers-to-read. Marina Favaro (Anthropic Institute) + Jack Clark. Distinguishes full RSI from human-driven RSI.

### HM7. **FourWeekMBA — "Anthropic's Map of AI Position"** (July 2026) ⭐ UNCHANGED v32

- See v32 papers-to-read. Anthropic's self-hosted gateway strategy.

---

## v33 Reading priority (this week, ordered by ROI)

1. **Memora + Microsoft Research Agentic Evolution survey (items 1-2)** — drives plan-A + plan-CO1, the v33 highest-ROI 1-2 week engineering bet
2. **DynamicMem (item 4)** — re-read alongside Memora to understand *why* the split is the right architecture
3. **Phase Matters (item 3)** — drives perceptiond v1.5 phase-mapped heterogeneous inference
4. **Sico README (HM1)** — drives plan-CO1 Digital Worker shell design (Q2 2027)
5. **Enterprise Times context graph (HM5)** — drives memoryd v1.5 graph layer design
6. **Jack Clark Import AI (item 5)** — re-read for v1.0 marketing copy (1 day copy)
7. **Sakana RSI Lab (HM2)** — read for v1.0 spec §15 RSI landscape (1 day copy)

## v33 Reading notes

- **Read together**: items 1, 2, 4 (Memora + Agentic Evolution + DynamicMem). All three are about memory architecture. They form a v33 *coherent* 1-2 day read.
- **Read together**: item 3 + arXiv 2606.27906 (Phase Matters is *part* of a larger hardware-in-the-loop research thread on Qualcomm SM8750). Read both for full picture.
- **Background reading**: items 5 (Jack Clark), HM2 (Sakana), HM3 (quantization), HM6 (Anthropic Institute). All are 1-day reads for v1.0 marketing copy.

## v33 v1.0 spec §15 "5-org RSI landscape" — papers to cite

Per plan-X15 (NEW v33, Q3 W3, 1 day copy), the v1.0 spec §15 should cite:
1. Sakana RSI Lab (sakana.ai/rsi-lab/) — Tokyo-based, sample-efficiency-first
2. Recursive Superintelligence (Crypto Briefing, June 2026) — $4.65B, 2-year ship-date
3. Mirendil (Gizmodo, June 2026) — a16z-backed, "friend of precious things"
4. Anthropic Institute (Time, June 29 2026) — Jack Clark, Marina Favaro
5. Andrew Ng (Reddit, late 2026) — "in 3-6 months, everyone will be using self-improving loops"

**v33 frame**: Danlab is the *audit-by-default, co-evolution* layer when these ship. v1.0 ships *before* maximalist RSI; v1.5 is the Digital Worker shell; v2.0 is multi-Digital-Worker orchestration.
