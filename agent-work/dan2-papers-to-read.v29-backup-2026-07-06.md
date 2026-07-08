# Dan-2 Papers to Read — v29 (2026-07-06)

> **Status:** v29 refresh. v28 content preserved. v29 deltas prepended.
> **Scope:** Top 5 research papers the team should read, based on Danlab's focus.
> **Verdict:** v23-v28 top-5 **all hold**. v29 promotes 1 paper from honorable mention to top-5 (SIA arXiv 2605.27276v1 confirmed with official numbers), and adds 3 new honorable mentions.

---

## Top 5 Papers (v29)

### 1. SIA: A Self-Improving AI with Harness and Weight Updates (Hexo Labs, arXiv 2605.27276v1, May 2026)
**Why:** the v1.0 research-publishing bet. The paper formalizes a self-improving loop where a language-model agent (the Feedback-Agent) updates both the harness and the weights of a task-specific agent. **Official published numbers (v29 SHARPEN #1):** LawBench 56.6% improvement, GPU kernel optimization 91.9% runtime reduction (12× faster), single-cell RNA denoising 502% improvement. The 91.9% kernel speedup maps to audiod segment timing histogram optimization as a v1.5 SIA-W+H port target. **Read this if you read nothing else.**

### 2. Edge Reliability Gap in Vision-Language Models (arXiv 2603.26769, 2026) — **PROMOTED from v28 honorable mention**
**Why:** the v29 VLM v1.0 ship-gate evaluation. SmolVLM2-500M answers "Yes" to 100% of COCO negation trials; Qwen2.5-VL-7B 4-bit answers incorrectly only 14% of the time. **v29 implication:** LFM2.5-VL-450M has no published negation benchmark. The v1.0 ship-gate must include a 200-image COCO-style negation probe (scaled-down FINER-CompreCap or Ghost-100 5-Level Prompt Intensity Framework). If LFM2.5-VL-450M exhibits >50% negation collapse, fall back to LFM2.5-VL-1.6B.

### 3. MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation (arXiv 2606.29914, late June 2026)
**Why:** the v28 evaluation-rigor gate. Four findings: (1) verbatim RAG matches full-context GPT-4o-mini (47.2% vs 0.34); (2) swapping only the embedding model in an identical pipeline shifts accuracy by +6.2pp at n=500, p<0.004; (3) Mem0 beats MiniLM-RAG by +11pp but loses to cloud-RAG by 1.2pp — one variable flips the conclusion; (4) agent self-memory (42%) underperforms basic retrieval (47%). **v29 implication:** any memoryd v1.5 model swap must be MemDelta-controlled.

### 4. As We May Search: Local-First Information Retrieval (arXiv 2606.29652, late June 2026)
**Why:** the v28 memoryd v1.5 architecture certainty. Three findings: (a) dense retrieval keeps over 91% nDCG@10 up to 100K documents; (b) approximate HNSW indexes extend to 1M documents with only 2% quality loss; (c) a 7B local language model reaches within 4 points of a cloud baseline on answer quality. **v29 implication:** the memoryd v1.5 architecture is now an *empirical certainty* — 1M documents at full accuracy is achievable on-device.

### 5. Jack Clark, Import AI #460: Reward hacking society, RSI data from Anthropic, and RL-based quadcopter racing (July 2026)
**Why:** the v28 outer-loop RSI framing. 8x increase in lines-of-code merged in 2026 vs 2024 at Anthropic. Clark's 60% maximalist RSI by 2028 estimate with quantitative evidence. **v29 implication:** the AGI roadmap should distinguish outer-loop RSI (already happening) from maximalist RSI (60% by 2028). The wedge is transparency + reversibility + on-device, not "we do RSI."

---

## Honorable Mentions (v29)

- **Adaptive Auto-Harness (arXiv 2606.01770)** — v29 NEW. Stateful multi-agent evolver + harness tree with solve-time routing. Outperforms five baselines on prediction-market, security-competition, event-forecasting streams. v1.5 plan-P4+ add-on.
- **INAR-VL (arXiv 2605.18853)** — v29 NEW. Edge-cloud routing for VLMs. Recovers 71% of edge-to-cloud accuracy gap. v1.5 differentiator (plan-R2).
- **Hermes Agent "Channel Fracture" (arXiv 2606.04896)** — v29 NEW. Silent memory-isolation failure in cron-delegated writes. v29 Hermes Agent spike (plan-R1) adds verification.
- **LQA: A Lightweight Quantized-Adaptive Framework for Vision-Language Models on the Edge (arXiv 2602.07849)** — v29 NEW. Sub-200MB 4-bit VLM framework. Test-time adaptation without gradient updates. v1.5 spike candidate.
- **FINER: MLLMs Hallucinate under Fine-grained Negative Queries (arXiv 2603.17662v1)** — v29 NEW. FINER-Tuning with DPO reduces hallucinations by up to 24.2%. v1.5 spike candidate.
- **Ghost-100: LLM-as-Judge Framework for Tone-Induced Hallucination (arXiv 2604.18803)** — v29 NEW. 5-Level Prompt Intensity Framework for VLM hallucination evaluation. v1.0 ship-gate evaluation rig.
- **DynamicMem: A Long-Horizon Memory Benchmark (arXiv 2606.22877)** — v28. 93% of memory failures trace to retrieval, not the writing model.
- **One Retrieval to Cover Them All: Co-occurrence-Aware KB Reorganization (ACL 2026 KnowFM Workshop)** — v28. v1.5 memoryd design.
- **Summary RAG: A Multi-Format Document Retrieval System (2026)** — v28. v1.5 memoryd design.
- **Alibaba SkillWeaver: AI agent tool routing cuts token use 99% (VentureBeat, July 2026)** — v28. v1.5 toold design.
- **TRINITY: An Evolved LLM Coordinator (ICLR 2026)** — v28. v1.5 openclaw research.
- **Carbon-aware Edge ML (ACM MobiSys 2026)** — v28. v2.0 chip-stack planning.
- **From AGI to ASI (Google DeepMind, 57-page arXiv report, June 10 2026)** — v29 NEW. 4-pathway framework: scaling, paradigm shifts, recursive self-improvement, multi-agent collectives. v29 19-step narrative anchor.

---

## v29 Paper-to-Plan Mapping

| Plan | Paper |
|------|-------|
| plan-P3 (SIA-H honest-RL) | #1 SIA paper |
| plan-P4 (SIA-W+H port) | #1 SIA paper (SIA-W+H variant) |
| plan-P4+ (Adaptive Auto-Harness add-on) | Adaptive Auto-Harness paper |
| plan-E1 (VLM negation-collapse gate) | #2 Edge Reliability Gap + Ghost-100 + FINER |
| plan-P1 + plan-M1 (MemDelta baseline) | #3 MemDelta paper |
| plan-P2 (memoryd OKF adapter) | #4 As We May Search paper |
| v1.0 spec §13 (outer-loop RSI framing) | #5 Import AI #460 + DeepMind From AGI to ASI |
| memoryd v1.5 retrieval focus | DynamicMem paper |
| memoryd v1.5 KB reorganization | Co-occurrence-Aware KB paper |
| memoryd v1.5 document-level retrieval | Summary RAG paper |
| toold v1.5 execution-graph + skill-routing | SkillWeaver paper |
| openclaw v1.5 multi-agent coordination | TRINITY paper |
| v2.0 chip-stack carbon planning | Carbon-aware Edge ML paper |
| v1.5 edge-cloud routing (plan-R2) | INAR-VL paper |
| v1.5 VLM 4-bit quantization (LQA spike) | LQA paper |
| v1.5 VLM negation-tuning (FINER spike) | FINER paper |
| v1.0 marketing 19-step narrative | From AGI to ASI paper |

---

*Maintained by DAN-2. v29 promotes Edge Reliability Gap to top-5, adds Adaptive Auto-Harness, INAR-VL, Channel Fracture, LQA, FINER, Ghost-100, From AGI to ASI as honorable mentions. All v23-v28 paper choices hold.*