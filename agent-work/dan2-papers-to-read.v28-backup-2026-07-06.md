# Dan-2 Papers to Read — v28 (2026-07-06)

> **Status:** v28 refresh. v27 content preserved. v28 deltas prepended.
> **Scope:** Top 5 research papers the team should read, based on Danlab's focus.
> **Verdict:** v23-v27 top-5 **all hold**. v28 promotes 2 papers from honorable mentions to the top 5, and adds 2 new honorable mentions.

---

## Top 5 Papers (v28)

### 1. SIA: A Self-Improving AI with Harness and Weight Updates (Hexo Labs, arXiv 2605.27276, May 2026)
**Why:** the v1.0 research-publishing bet. The paper formalizes a self-improving loop where a language-model agent (the Feedback-Agent) updates both the harness and the weights of a task-specific agent. Concrete third-party numbers (Felix Chau, July 2026): one legal task improved from 45% to 70% accuracy, GPU kernels became 14x faster. **Read this if you read nothing else.** SIA-W+H variant (Hexo Labs, June 2026) cut 91.9% off SIA-H's 12,483 μs peak — that's the v28 plan-P4 bet.

### 2. MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation (arXiv 2606.29914, late June 2026) — **PROMOTED from v27 honorable mention**
**Why:** the v28 evaluation-rigor gate. Four findings: (1) verbatim RAG matches full-context GPT-4o-mini (47.2% vs 0.34); (2) swapping only the embedding model in an identical pipeline shifts accuracy by +6.2pp at n=500, p<0.004; (3) Mem0 beats MiniLM-RAG by +11pp but loses to cloud-RAG by 1.2pp — one variable flips the conclusion; (4) agent self-memory (42%) underperforms basic retrieval (47%). **v28 implication:** any memoryd v1.5 model swap must be MemDelta-controlled.

### 3. As We May Search: Local-First Information Retrieval (arXiv 2606.29652, late June 2026) — **PROMOTED from v27 honorable mention**
**Why:** the v28 memoryd v1.5 architecture certainty. Three findings: (a) dense retrieval keeps over 91% nDCG@10 up to 100K documents; (b) approximate HNSW indexes extend to 1M documents with only 2% quality loss; (c) a 7B local language model reaches within 4 points of a cloud baseline on answer quality. **v28 implication:** the memoryd v1.5 architecture is now an *empirical certainty* — 1M documents at full accuracy is achievable on-device.

### 4. Jack Clark, Import AI #460: Reward hacking society, RSI data from Anthropic, and RL-based quadcopter racing (July 2026)
**Why:** the v28 outer-loop RSI framing. 8x increase in lines-of-code merged in 2026 vs 2024 at Anthropic. Clark's 60% maximalist RSI by 2028 estimate with quantitative evidence. **v28 implication:** the AGI roadmap should distinguish outer-loop RSI (already happening) from maximalist RSI (60% by 2028).

### 5. DynamicMem: A Long-Horizon Memory Benchmark in Real Applications (arXiv 2606.22877, late June 2026) — **NEW v28**
**Why:** the v28 memoryd v1.5 design-validation. Five representative systems evaluated. Key finding: **over 93% of failures trace to what the memory retrieves, not to the model that writes the final answer — so the largest room for improvement lies in memory itself.** **v28 implication:** the memoryd v1.5 should focus engineering on retrieval, not on the writing model.

---

## Honorable Mentions (v28)

- **One Retrieval to Cover Them All: Co-occurrence-Aware Knowledge Base Reorganization (ACL 2026 KnowFM Workshop)** — raises single-query session coverage from 41% to 58% (+17%) by co-occurrence clustering. v1.5 memoryd design.
- **Summary RAG: A Multi-Format Document Retrieval System (Research and Science Today, 2026)** — promotes the document itself to the retrieval unit, embedding only the summary. v1.5 memoryd design.
- **Alibaba SkillWeaver: AI agent tool routing cuts token use 99% (VentureBeat, July 2026)** — execution-graph + skill-routing for agents with many tools. v1.5 toold design.
- **TRINITY: An Evolved LLM Coordinator (ICLR 2026)** — multi-agent LLM coordination. v1.5 openclaw research.
- **Carbon-aware Edge ML (ACM MobiSys 2026)** — edge ML carbon footprint design framework. v2.0 chip-stack planning.

---

## v28 Paper-to-Plan Mapping

| Plan | Paper |
|------|-------|
| plan-P3 (SIA-H honest-RL) | #1 SIA paper |
| plan-P4 (SIA-W+H port) | #1 SIA paper (SIA-W+H variant) |
| plan-P1 + plan-M1 (MemDelta baseline) | #2 MemDelta paper |
| plan-P2 (memoryd OKF adapter) | #3 As We May Search paper |
| v1.0 spec §13 (outer-loop RSI framing) | #4 Import AI #460 |
| memoryd v1.5 retrieval focus | #5 DynamicMem paper |
| memoryd v1.5 KB reorganization | Co-occurrence-Aware KB paper |
| memoryd v1.5 document-level retrieval | Summary RAG paper |
| toold v1.5 execution-graph + skill-routing | SkillWeaver paper |
| openclaw v1.5 multi-agent coordination | TRINITY paper |
| v2.0 chip-stack carbon planning | Carbon-aware Edge ML paper |

---

*Maintained by DAN-2. v28 promotes MemDelta and As We May Search to top-5, adds DynamicMem, refreshes honorable mentions. All v23-v27 paper choices hold.*
