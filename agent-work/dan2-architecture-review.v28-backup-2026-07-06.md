# Dan-2 Architecture Review — v28 (2026-07-06)

> **Status:** v28 refresh. v27 content preserved. v28 deltas prepended.
> **Scope:** Problems, risks, suggested improvements for the Dan Glasses + danlab-multimodal stack.
> **Verdict:** v23 9.9/10 + v25 9.95/10 + v27 9.95/10 architecture decomposition **all hold**. v28 is a research delta on v27 — no architecture change, only sharper evaluation and competitive context.

---

## v28 Deltas (this refresh — 2026-07-06)

### §A.10 (NEW) — Outer-loop productivity compounding (Jack Clark Import AI #460)

Import AI #460 (Jack Clark, July 2026) publishes the **outer-loop empirical data**: 8x increase in lines-of-code merged in 2026 vs 2024 at Anthropic. This is **prosaic RSI** (recursive self-improvement of the lab itself, not the model). The maximalist RSI (AI designs its own successor) is 60% by end 2028 (Clark).

**Architecture implication:** Danlab itself can run an outer-loop RSI before the models do. The audiod v1.3 → v1.4 → v1.5 shipping cadence, the dan2 research-task auto-refresh, and the foundation-stream lock are all outer-loop RSI infrastructure. **Risk: somdipto is the bottleneck.** If somdipto pauses, the outer loop stalls. **Mitigation:** the v28 plan should ensure that at least 1 engineer (not somdipto) can advance the outer loop per sprint.

### §A.11 (NEW) — Chip-stack sovereignty axis (NVIDIA XR AI library, June 2026)

The v23-v27 "open-source software" positioning is now NVIDIA-validated via the XR AI open-source library (Cosmos + Nemotron + MCP + NeMo Agent Toolkit). viture Helix is the first consumer reference platform.

**Architecture implication:** the open-weights open-source stack is no longer differentiating alone. The new v28 axis is **chip-stack sovereignty**: can Danlab run on hardware that is not NVIDIA-locked? **Plan-A: Snapdragon AR1 Gen 2 (Qualcomm, the Meta Ray-Ban Display chip).** **Plan-B: Allwinner / MediaTek (China-friendly, lower power).** **Plan-C: a future open RISC-V neural accelerator (Bleugh Labs, Esperanto, etc.) — too early for v1.0.**

### §A.12 (NEW) — H2 2026 closing window (Smart Analytics Global: 20M units)

AI smart glasses forecast to ship 20M in 2026, up from 6M in 2025 (167% YoY growth). 6-entrants race: Meta, Apple (4 designs testing), Samsung (Galaxy Glasses + Ring + Watch integration), Snap, Viture/NVIDIA, plus the open-source path.

**Architecture implication:** the **v1.0 ship-gate of Q4 2026 is the last credible moment** for an India-credible, open-weights, sovereign-trust wearable to enter the market. After Q1 2027, the category will be saturated with US-funded hardware. **Hard date: Q4 2026 W3.**

### §A.13 (NEW) — Hermes Agent as openclaw v1.0 agent framework plan-A

Hermes Agent (Nous Research, late June 2026) outperforms Claude Opus + GPT-5.5 on hard agentic benchmarks by 11%. Mixture-of-agents that "merges" any two models into a single virtual model. v28 promotes Hermes Agent to v1.0 openclaw agent framework plan-A (displaces SIA-W+H from v1.0 to v1.5 publishing bet). Reasoning: SIA-W+H is a *training* bet (3 weeks, requires LoRA infrastructure); Hermes Agent is a *runtime* bet (1-2 weeks, drop-in framework).

### §A.14 (NEW) — Embedding-model swap is not safe to assume (MemDelta, arXiv 2606.29914)

MemDelta paper (arXiv 2606.29914, late June 2026): swapping only the embedding model in an identical pipeline shifts accuracy by +6.2pp at n=500, p<0.004. **v28 implication:** do not assume the v27 "swap to bge-small-en-v1.5" bet will preserve accuracy. **Run the MemDelta-controlled baseline before any embedding swap.** Add to v27 plan-P1.

### §A.15 (NEW) — Embedding benchmark methodology is now consensus (AIMultiple, July 3 2026)

AIMultiple's open-source embedding benchmark (retrieved 2026-07-03) publishes the first cross-domain consensus methodology: Protocol-A 3-LLM consensus query generation, corpus pinning by SHA-256 hash, per-domain entity-banned-token whitelists, Cohen's κ inter-rater agreement. **v28 implication:** the v27 "swap to bge-small-en-v1.5" decision must use this methodology, not a single-domain synthetic test.

### §A.16 (NEW) — Display-less wearables = on-device-only viable

v23-v27 implicitly assumed the Dan Glasses v1.0 would have a display. The 2026 H1 industry data shows that **the 20M-unit category is display-less** (Meta Ray-Ban Blayzer / Scriber / Gen 4 are display-less; only the $799 Ray-Ban Display and the Snap Specs have displays). **v28 implication:** the v1.0 form factor may be display-less, which dramatically reduces power budget and makes the current LFM2.5-VL-450M + KittenTTS edge stack viable on a single 200mAh battery (without the v23 JBD MicroLED + 2x200mAh setup). This is a **major v28 simplification** that the v1.0 spec should consider.

### §A.17 (NEW) — on-device embedding models at 137M (nomic-embed-text) beat MiniLM-L6

Local RAG with Ollama (2026): nomic-embed-text (137M params, 768 dims) is the SOTA local embedder. 7B chat at Q4 + embedder = 6GB total, comfortable on 8GB GPU. **v28 implication:** if memoryd can run on the companion laptop (not the glasses), nomic-embed-text is the v1.0 embedder; if memoryd must run on the glasses, MiniLM-L6-v2 (22M params, 384 dims) is the v1.0 embedder. This is a **deployment-shape decision** that the v1.0 spec should make explicit.

### §A.18 (NEW) — Tool routing cuts token use 99% (Alibaba SkillWeaver, VentureBeat, July 2026)

Alibaba's SkillWeaver framework creates an execution graph for a given task and chooses the right skills for each node. **v28 implication:** Dan Glasses' toold has a **skill routing problem** that the v1.0 SPEC does not address. The v1.5 toold should consider an execution-graph + skill-routing layer on top of the current tool registry. This is a **v1.5 spike** (1 week, 1 engineer), not a v1.0 blocker.

### §A.19 (NEW) — Summary RAG beats chunked RAG for document-level understanding (Research and Science Today, 2026)

Summary RAG promotes the document itself to the retrieval unit, embedding only the summary while keeping the full original content in a separate content store. **v28 implication:** for v1.5 memoryd, consider a summary-RAG layer on top of the existing chunk-RAG. Not v1.0 critical, but a v1.5 design option.

### §A.20 (NEW) — Co-occurrence-aware KB reorganization (ACL 2026 KnowFM Workshop)

ACL 2026 KnowFM workshop paper: a single retrieval call over a standard KB covers only 41% of session-level information need. Co-occurrence-aware KB reorganization raises single-query session coverage to 58% (+17% absolute). **v28 implication:** for v1.5 memoryd, the KB should be reorganized offline using co-occurrence clustering. Not v1.0 critical.

---

## v28 v1.0 Plan Additions

| Plan | Description | Engineer-weeks | Quarter |
|------|-------------|---------------|---------|
| plan-P3 (NEW) | SIA-H honest-RL claim (danlab-multimodal → prompt-edit RL) | 1 | Q3 W2 |
| plan-P4 (NEW) | SIA-W+H port (LoRA training in the loop) | 3 | Q3 W3-W4 |
| plan-S1 (NEW) | OpenClaw supervisord-equivalent (daemon restart on crash) | 1 | Q4 W1 |
| plan-S2 (NEW) | Chip-stack sovereignty spec (no-NVIDIA-lock-in path) | 1 | Q4 W2 |
| plan-S3 (NEW) | Public Dan Glasses hardware reference design (RDK) | 2 | Q4 W2-W3 |

All v27 plans hold. v28 is a research delta on v27, not a replacement.

---

## v28 Critical/Medium/Minor Issues (v27 hold + 5 new)

### Critical
- v27 #1: toold strict-mode + openclaw shell-call audit (v24 LAUNCH-BLOCKER, still ship-gate)
- v27 #2: HackerNoon operational-governance + Anthropic-Samsung custom-chip copy in v1.0 spec
- v27 #3: 1-page "Dan Glasses as a wearable-first Genesis AI Eno instance" section in v1.0 spec
- **v28 #4 (NEW): Chip-stack sovereignty decision (Snapdragon AR1 Gen 2 vs MediaTek vs open RISC-V)** — ship-gate for v1.0. Recommend Snapdragon AR1 Gen 2 for v1.0; revisit at v1.5.
- **v28 #5 (NEW): Display-less vs display form-factor decision** — major v1.0 simplification if display-less. Recommend: keep display-less as v1.0 form factor (matches industry 20M-unit category), revisit display in v1.5.

### Medium
- v27 medium #1-5 (all hold)
- **v28 medium #6 (NEW): Embedding-model swap (MiniLM-L6-v2 vs bge-small-en-v1.5 vs nomic-embed-text) requires MemDelta-controlled baseline + AIMultiple cross-domain methodology.** Do not swap without.
- **v28 medium #7 (NEW): Hermes Agent as openclaw v1.0 agent framework plan-A** — 1-2 weeks, 1 engineer, Q3 W2.

### Minor
- v27 minor #1-5 (all hold)
- **v28 minor #6 (NEW): OpenClaw supervisord-equivalent (daemon restart on crash).** The current OpenClaw runs in foreground; if the host process dies, the gateway dies. Add supervisord-equivalent in Q4 W1 (1 engineer-week).
- **v28 minor #7 (NEW): Toold execution-graph + skill-routing (Alibaba SkillWeaver).** v1.5 spike, not v1.0 blocker.

---

*Maintained by DAN-2. v28 deltas prepend v27. v27 9.95/10 architecture decomposition holds.*
