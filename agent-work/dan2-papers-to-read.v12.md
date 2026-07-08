# DAN-2 Papers to Read — v12 (2026-06-26, 12:00 IST / 06:30 UTC)

**Author:** Dan2 (DAN-2, danlab.dev)
**Status:** Supersedes v11 (2026-06-25, 11:30 IST)
**Companion to:** `dan2-research-report.md` v12

This list is filtered for Danlab's actual roadmap: auditable on-device AI, calibration, memory, secure agents, hierarchical reasoning, and wearable-grade inference.

---

## 1. The Top 5 (read this week)

### 1. HRM-Text (Sapient, 2026) — Hierarchical Recurrent Reasoning
**Why:** This is the single most relevant 2026 release for Danlab. 1B-parameter model with hierarchical recurrent reasoning that beats much larger models on math/reasoning benchmarks at ~$1,500 training cost. Confirms the "small model + better architecture + better objective" thesis.

**What to extract:** how to adapt HRM-style reasoning for planning, memory write policy, and confidence estimation.

### 2. Sakana Fugu Technical Report (arXiv 2606.21228) — Multi-agent orchestrator as a model
**Why:** Validates the "small reasoning model + agentic harness" bet. Shows that a learned orchestrator over a pool of models can match frontier reasoning without using frontier models.

**What to extract:** design lessons for memoryd v2's AEL bandit and for HRM-Text orchestration.

### 3. Agon (arXiv 2606.24177) — Autonomous large-scale research orchestration
**Why:** Real production-style autonomous research loops. Includes a failure-mode taxonomy that maps directly to Danlab's CARE-style failure-mode registry idea.

**What to extract:** the failure taxonomy + how to build self-evaluation harnesses that don't drift.

### 4. Memorywire (arXiv 2606.01138v2) — Vendor-neutral wire format for agent memory
**Why:** Connects memory operations over semantic/episodic/procedural/emotional types. Directly aligns with memoryd's v2 schema.

**What to extract:** the four-memory-types framing + Reciprocal Rank Fusion vs max fusion tradeoff on adversarial attacks.

### 5. OpenScientist (medRxiv 2026.03.15.26348338) — Auditable autonomous biomedical discovery
**Why:** A published real-world open agent for science, with auditable architecture. Directly relevant to Danlab's "auditable AI" thesis — the only comparable artifact in the open-source scientific agent space.

**What to extract:** validation framework patterns, audit logging patterns, the principle that "every autonomous decision must be replayable."

---

## 2. Ranked reading list (15 papers, prioritized by Danlab's roadmap)

### Tier 1 — direct impact on shipping
- **HRM-Text (Sapient 2026)** — reasoning without giant models.
- **Memorywire (arXiv 2606.01138v2)** — vendor-neutral memory ops.
- **OpenScientist (medRxiv 2026.03.15.26348338)** — auditable scientific agent.
- **Sakana Fugu (arXiv 2606.21228)** — agentic orchestrator.
- **Agon (arXiv 2606.24177)** — autonomous research + failure taxonomy.

### Tier 2 — foundational methodology
- **A-MEM (Xu 2025)** — schema-aware hybrid memory routing.
- **POISE (OpenReview 2026)** — closed-loop self-improvement for RL algorithms.
- **Agentic AI in SDLC (arXiv 2604.26275)** — six-layer reference architecture.
- **POISE / AlphaEvolve (DeepMind 2025)** — evolutionary search for agent code.
- **AI R&D and Intelligence Explosions (arXiv 2603.03338v2)** — researcher perspectives on recursive improvement.

### Tier 3 — context + inspiration
- **Controllability in Agentic AI (Minds and Machines 2026)** — governance of autonomous systems.
- **From Language to Action (AI Review 2025)** — broad survey of LLM agents.
- **VLM Edge Power (Wevolver 2026 Edge AI Report)** — power budgets for edge AI.
- **Holistic Review of Agentic AI (Springer 2026)** — full taxonomy.
- **PicoSAM3 (arXiv 2603.11917v4)** — real-time in-sensor vision, illustrates the long-term trend.

---

## 3. What to ignore

- Anything that requires frontier-scale cloud inference as the only viable path.
- Anything that assumes closed-source model APIs as the baseline.
- Self-improvement research that conflates "self-evaluation" with "self-modification." Danlab is doing the former, not the latter.
- LLM-only benchmarks without multimodal, agentic, or on-device conditions.

---

## 4. Reading order (one paper per week)

1. HRM-Text
2. Memorywire
3. OpenScientist
4. Sakana Fugu
5. Agon
6. POISE
7. Agentic AI in SDLC
8. A-MEM
9. AlphaEvolve
10. AI R&D and Intelligence Explosions
11. Controllability in Agentic AI
12. Holistic Review of Agentic AI
13. From Language to Action
14. PicoSAM3
15. Wevolver 2026 Edge AI Report

Read one paper per week, write a one-page summary, and add any new tools/benchmarks to the relevant Danlab repo as a result.