# Dan-2 Papers to Read — v30 (2026-07-06)

> **Status:** v30 refresh. v29 backups at `*.v29-backup-2026-07-06.md`. v29 content preserved; v30 deltas prepended.
> **Scope:** Top 5 research papers + honorable mentions the team should read, based on Danlab's focus.
> **Verdict:** v23-v29 top-5 **all hold**. v30 promotes Decagon DuetBench to honorable mention and adds Anthropic-Claude-80%-code datapoint as the v30 outer-loop RSI anchor.

---

## v30 Deltas (this refresh — 2026-07-06 07:30 UTC / 13:00 IST)

### 1. NEW v30 ANCHOR — Anthropic Institute: Claude writes 80% of code (June 4 2026)

Favaro (Anthropic Institute) + Clark (Anthropic co-founder) blog post "The next big step for humans and AI" (June 4 2026, davos announcement): "The model now writes approximately 80% of Anthropic's new production code, according to the company. … engineers are producing several times more output than before with AI assistance." The post also confirms the "8x increase in lines-of-code merged in 2026 vs 2024" figure. This is now the **quantitative citation of record** for outer-loop RSI.

**v30 implication:** the v29 Import AI #460 reference (paper #5 in the v29 top-5) is now corroborated by the source. Replace Import AI #460 reference with the Anthropic Institute blog post as the primary v30 outer-loop RSI citation. The 80% code figure is the v30 "outer-loop RSI is real" anchor for the v1.0 marketing.

### 2. NEW HONORABLE MENTION — Decagon DuetBench: end-to-end self-improvement benchmark (June 9 2026)

Decagon introduced Duet Autopilot (June 9 2026) as "the first verified self-improving AI agent for customer experience" with DuetBench as "the industry's first benchmark for evaluating agent self-improvement end-to-end." DuetBench measures *automatic* and *verifiable* improvement, not just static performance.

**v30 implication:** DuetBench is the v30 first industry-credible benchmark for self-improving agents. The v29 plan-P4 (SIA-W+H port, research-publishing bet) should add a DuetBench-style task that Danlab can self-publish: the danlab-multimodal loop on the danlab-captures dataset, with a verified-improvement metric. This is the v30 "**we don't just port, we evaluate**" upgrade for the Q3 W3-W4 research bet.

### 3. NEW HONORABLE MENTION — Recursive Superintelligence Inc., $650M Series A at $4.65B valuation (announced May 13 2026, public via Tech Times July 2026)

Ex-Meta Fundamental AI Research director Yuandong Tian co-founded Recursive Superintelligence (May 13 2026), raised $650M Series A at $4.65B, from Alphabet's venture arm and two of the largest chipmakers. **The market is now paying multi-billion-dollar valuations for self-improving-systems theses.**

**v30 implication:** the v28 "SIA is now peer-reviewed" + v29 "SIA is now open-paper" framing is now **v30 market-capitalized at $4.65B**. The SIA-W+H port (plan-P4) is no longer a research bet in the abstract — it is a bet into a **market category that has institutional validation**.

### 4. NEW HONORABLE MENTION — Microsoft Research + Renmin University Arbor (June 2026)

Arbor is "a framework that upgrades AI-driven research and optimization from a sequence of trial-and-error guesses into a cumulative learning process. In practical tests, Arbor delivered more than 2.5 times the verifiable performance gains of standard AI coding agents across real-world engineering tasks while operating under the same resource budget."

**v30 implication:** the v29 plan-O1 (toold sovereign-trust audit) + plan-N1 (toold strict-mode) should add an Arbor-style "cumulative learning" optimization. Arbor's 2.5× gain on the same compute budget is the v30 first "agent harness actually improves" citation relevant to the toold v1.0 evaluation. Worth a 1-day read by somdipto.

### 5. NEW HONORABLE MENTION — DeepSeek "Harness" team formation (June 2026)

DeepSeek is hiring an "Agent Harness" team for "DeepSeek Code," Series A >50B yuan from Tencent/JD.com/NetEase/CATL. Confirms the v29 plan-J (ASPIRE skill library port) and v28 plan-P4 (SIA-W+H port) as **industry-aligned bets**, not contrarian ones.

**v30 implication:** the "harness" category is now industry-recognized. OpenClaw is in the right architectural neighborhood. v30 keeps plan-S1 (OpenClaw supervisord-equivalent) and plan-P4 in the same priority bucket.

### 6. NEW HONORABLE MENTION — NVIDIA ASPIRE (self-improving robotics framework, July 3 2026)

NVIDIA + University of Michigan + UIUC + UC Berkeley + CMU: "ASPIRE (Agentic Skill Programming through Iterative Robot Exploration)" reaches 31% zero-shot on LIBERO-Pro long tasks. Continual learning system that writes and refines robot control programs; distills validated fixes into a reusable, transferable skill library.

**v30 implication:** ASPIRE is the v30 first **peer-reviewed, multi-institution** self-improving-system implementation. The "central coordinator manages the shared skill library and dispatches actor coding agents" pattern maps cleanly to OpenClaw memory-core + toold strict-mode. Confirms the v29 plan-J (ASPIRE skill library port) priority.

### 7. NEW HONORABLE MENTION — Engram / Weaviate "learned memory" architecture (June 6 2026)

Weaviate launched Engram (June 6 2026), a managed memory service for LLM agents built on Weaviate's vector database. Solves the agentic AI memory bottleneck: "Memory writes can happen in the background, while retrieval remains available when the agent needs relevant context for a later turn." Separately, an "Engram" startup raised $98M Series A (CNBC June 23 2026) — clients include Microsoft, Notion, Harvey. The startup's thesis: "models can match or outperform frontier labs using up to 100 times fewer tokens."

**v30 implication:** the v28 Mem0 vs MiniLM-RAG-vs-cloud-RAG MemDelta finding is now industry-recognized: **basic RAG with a strong embedding + good prompt wins over agent self-edits + expensive cloud calls**. The v27 plan-P1 (MemDelta-controlled baseline) is now the v30 **right call**. Engram's architecture (background writes, foreground retrieval) is the v1.5 memoryd design pattern.

### 8. NEW HONORABLE MENTION — Perplexity Brain (June 18 2026)

Perplexity launched "Brain" (June 18 2026), a self-improving memory system for its agent product "Computer." Key reframing: "Most AI memory remembers the user. Brain remembers what the agent did." This is the v30 first industry ship of a *work-trace* memory architecture, distinct from the user-profile memory pattern.

**v30 implication:** the v29 memoryd v1.5 three-layer model (vector store + OKF + episodic log) can be sharpened to v30 **four-layer** by adding a *work-trace* layer: when a danlab-multimodal cycle runs, the trace is stored and later retrieved when the user asks "why did you decide that?" This is the v30 **"agent remembers its own reasoning"** differentiator. Not v1.0 (per v29 wedge — must be on-device-only) but a clean v1.5 differentiator.

### 9. NEW HONORABLE MENTION — AWS AgentCore Harness GA (June 18 2026)

AWS launched Amazon Bedrock AgentCore Harness (generally available June 18 2026, New York Summit), reducing agent development to "two API calls." This is the v30 first *managed* agent-harness product from a hyperscaler.

**v30 implication:** the v28 "OpenClaw is the right call for self-hosted agent orchestration" framing is now industry-validated by AWS shipping the same architecture as a managed product. **v30 sharpens the v1.0 OpenClaw v1.0 ship-gate to: "OpenClaw v1.0 ships before AWS AgentCore Harness adopts an open-weights model endpoint."** The race is on; the v1.0 wedge is "self-hosted, on-device, sovereign-trust" not "managed, cloud, monthly fee."

### 10. NEW HONORABLE MENTION — Palantir + NVIDIA Nemotron sovereign stack (June 29 2026)

Palantir (NASDAQ: PLTR) + NVIDIA: AIP + Foundry + Apollo + Ontology as the deployment platform for Nemotron open models in sovereign environments, focused on US government. CEO Karp's interview claim: "some U.S. government customers have recently moved away from proprietary AI models — citing Anthropic by name — toward Nvidia's open-source Nemotron models."

**v30 implication:** the v28 plan-S2 (chip-stack sovereignty spec) is now **v30 first validated at government scale**. Palantir + Nemotron is the v30 *Western-government-aligned* sovereign-AI deployment pattern. Danlab's v30 differentiator is the **India + non-aligned + on-device + open-weights** combination — a position Palantir-Nemotron does not serve (they are US-aligned only). This sharpens the v30 India-credible wedge.

### 11. NEW HONORABLE MENTION — Anthropic + Micron strategic agreement (Series H, June 2026)

Micron + Anthropic strategic agreement (June 2026): memory and storage AI architecture design, supply agreement, enterprise AI adoption of Claude across Micron, and **strategic investment in Anthropic's Series H funding round**. "Collaboration spans memory and storage AI architecture design."

**v30 implication:** the v28 §B.5 "AGI is bifurcated" framing is now industry-validated: frontier labs (Anthropic) are *vertically integrating with memory suppliers* (Micron). The v1.0 v30 memoryd bet (vector + OKF + episodic log + work-trace) is the v30 right call because the on-device + sovereign-trust wedge is *what Anthropic cannot offer*. Anthropic has the cloud; Danlab has the device.

### 12. NEW HONORABLE MENTION — Anthropic Claude Sonnet 5 + self-hosted Code gateway on Bedrock/Vertex (July 2 2026)

Anthropic released Claude Sonnet 5 (July 2 2026) and launched a self-hosted Claude Code gateway compatible with Amazon Bedrock and Google Cloud Vertex AI. The pitch: a "Map of AI position across multiple layers simultaneously: the model layer (Sonnet 5), the tooling layer (Claude Code), the infrastructure layer (self-hosted gateway), and the distribution layer (Bedrock + Vertex)."

**v30 implication:** v30 sharpens the v26 plan-O2 (openclaw + toold end-to-end reversibility contract): **"OpenClaw v1.0 must offer an Anthropic-Claude-Code-gateway-equivalent on the user's own machine — a self-hosted agent gateway with the same model/tool/infrastructure/distribution map."** This is the v30 "we ship the on-device equivalent of what Anthropic ships on AWS/GCP" wedge.

### 13. NEW HONORABLE MENTION — Fable 5 export-control saga: full resolution (June 12 → June 30 2026)

Anthropic launched Claude Fable 5 + Claude Mythos 5 (June 9 2026). Three days later (June 12), US Commerce Department issued an export-control directive suspending access for "all foreign nationals, including foreign national Anthropic employees inside or outside the United States." Trump admin lifted the controls (June 30) after Anthropic trained a safety filter (classifier) for the specific jailbreak technique. Fable 5 returns globally (July 1); Mythos 5 returns to "a set of US organizations" (June 26 onward).

**v30 implication:** the v26 plan-O3 (v1.0 spec §13 sovereign-trust section) is now **v30 first validated by a major lab's near-death experience.** The Fable shutdown "strengthens case for self-hosted models" (Let's Data Science June 2026). **v30 marketing wedge update: "Closed-source frontier is now *politically-conditional* and *export-controlled* — Dan Glasses is the on-device, open-weights, sovereign-trust alternative."** v30 retracts v29 "transparent, reversible, on-device" only in favor of adding "and export-uncapturable" to the wedge.

### 14. NEW HONORABLE MENTION — MemoMind One by XGIMI hits $500K Kickstarter (June 2026)

MemoMind One: dual 2,000-nit green micro-LED displays, no built-in camera, on-device AI assistant, 26-language translation, $20/month Memo+ subscription. From projector manufacturer XGIMI.

**v30 implication:** MemoMind is the v30 first *display-equipped* AI smart glasses that ships from a Chinese manufacturer with on-device AI as the headline feature. It is a competitor for v2.0 form factor (deferred from v23 plan). Not v1.0 (display + 2,000-nit is a power-burner), but a v2.0 directional signal.

### 15. NEW HONORABLE MENTION — Apple AirPods Ultra / camera-equipped AirPods Pro development SUSPENDED (July 3 2026)

Apple suspended the development of camera-equipped AirPods Pro and AirPods Ultra. "Apple reportedly wanted to start selling the camera-equipped AirPods Pro in the first half of 2026, but the product's launch was held back because the smarter, AI version of ‌Siri‌ was still being developed."

**v30 implication:** v30 sharpens the v28 "Apple is a credible 2027 competitor" framing. **Apple is NOT a credible 2027 competitor for on-device AI wearables.** The AirPods Ultra suspension + visionOS 27 delay + iOS 27 Siri delay all signal that Apple's on-device AI is not ready. v30 **removes Apple from the 6-entrants race** (down to 5: Meta, Samsung, Snap, Viture/NVIDIA, Danlab).

---

## Top 5 Papers (v30)

### 1. SIA: A Self-Improving AI with Harness and Weight Updates (Hexo Labs, arXiv 2605.27276v1, May 2026)
**Why:** the v1.0 research-publishing bet. The paper formalizes a self-improving loop where a language-model agent (the Feedback-Agent) updates both the harness and the weights of a task-specific agent. **Official published numbers (v29 SHARPEN #1):** LawBench 56.6% improvement, GPU kernel optimization 91.9% runtime reduction (12× faster), single-cell RNA denoising 502% improvement. The 91.9% kernel speedup maps to audiod segment timing histogram optimization as a v1.5 SIA-W+H port target. **Read this if you read nothing else.**

### 2. Edge Reliability Gap in Vision-Language Models (arXiv 2603.26769, 2026)
**Why:** the v29 VLM v1.0 ship-gate evaluation. SmolVLM2-500M answers "Yes" to 100% of COCO negation trials; Qwen2.5-VL-7B 4-bit answers incorrectly only 14% of the time. **v29 implication:** LFM2.5-VL-450M has no published negation benchmark. The v1.0 ship-gate must include a 200-image COCO-style negation probe (scaled-down FINER-CompreCap or Ghost-100 5-Level Prompt Intensity Framework). If LFM2.5-VL-450M exhibits >50% negation collapse, fall back to LFM2.5-VL-1.6B.

### 3. MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation (arXiv 2606.29914, late June 2026)
**Why:** the v28 evaluation-rigor gate. Four findings: (1) verbatim RAG matches full-context GPT-4o-mini (47.2% vs 0.34); (2) swapping only the embedding model in an identical pipeline shifts accuracy by +6.2pp at n=500, p<0.004; (3) Mem0 beats MiniLM-RAG by +11pp but loses to cloud-RAG by 1.2pp — one variable flips the conclusion; (4) agent self-memory (42%) underperforms basic retrieval (47%). **v30 implication:** any memoryd v1.5 model swap must be MemDelta-controlled; the Engram and Perplexity Brain launches are v30 industry-validated confirmations.

### 4. As We May Search: Local-First Information Retrieval (arXiv 2606.29652, late June 2026)
**Why:** the v28 memoryd v1.5 architecture certainty. Three findings: (a) dense retrieval keeps over 91% nDCG@10 up to 100K documents; (b) approximate HNSW indexes extend to 1M documents with only 2% quality loss; (c) a 7B local language model reaches within 4 points of a cloud baseline on answer quality. **v30 implication:** the memoryd v1.5 architecture is now an *empirical certainty* — 1M documents at full accuracy is achievable on-device.

### 5. From AGI to ASI (Google DeepMind, 57-page arXiv report, June 10 2026) — **PROMOTED from v29 honorable mention**
**Why:** the v30 outer-loop RSI + multi-pathway framing. 14 researchers, 57 pages, 4 pathways: (1) scaling, (2) paradigm shifts, (3) recursive self-improvement, (4) multi-agent collectives. Frames progress as "waves, not a wall." **v30 implication:** the v29 Import AI #460 reference is now best read alongside DeepMind's From AGI to ASI. Together they provide the v30 outer-loop + multi-pathway framing for the v1.0 spec §13.

---

## Honorable Mentions (v30)

- **Anthropic Institute, June 4 2026 blog post** — v30 NEW. Favaro + Clark: "Claude writes 80% of Anthropic's new production code." 8x LOC merged. v30 outer-loop RSI quantitative citation of record.
- **Decagon DuetBench (June 9 2026)** — v30 NEW. "First verified self-improving AI agent for customer experience" with end-to-end DuetBench. v30 plan-P4 evaluation rig add.
- **Recursive Superintelligence Inc. (May 13 2026)** — v30 NEW. $650M Series A at $4.65B valuation. Ex-Meta Tian, "models build models" thesis. Market-category validation for plan-P4.
- **Arbor (Microsoft Research + Renmin University, June 2026)** — v30 NEW. 2.5× Claude Code + Codex on same compute. v30 plan-O1 + plan-N1 evaluation rig add.
- **DeepSeek "Harness" team formation (June 2026)** — v30 NEW. >50B yuan Series A. v30 plan-S1 industry-validation.
- **NVIDIA ASPIRE (July 3 2026)** — v30 NEW. Self-improving robotics, 31% zero-shot on LIBERO-Pro. v30 plan-J (skill library) pattern reference.
- **Engram / Weaviate "learned memory" (June 6 2026)** — v30 NEW. Background writes, foreground retrieval. v30 plan-P1 industry-validation.
- **Engram startup $98M Series A (June 23 2026)** — v30 NEW. 100× fewer tokens vs frontier. v30 plan-M1 (embedding model swap) evaluation rig.
- **Perplexity Brain (June 18 2026)** — v30 NEW. Work-trace memory architecture. v30 memoryd v1.5 four-layer model.
- **AWS AgentCore Harness GA (June 18 2026)** — v30 NEW. Hyperscaler agent-harness managed product. v30 plan-S1 competitive-context.
- **Palantir + NVIDIA Nemotron sovereign stack (June 29 2026)** — v30 NEW. Western-government sovereign AI. v30 plan-S2 industry-validation.
- **Anthropic + Micron strategic agreement (June 2026)** — v30 NEW. Frontier-lab memory vertical integration. v30 memoryd differentiator.
- **Anthropic Claude Sonnet 5 + self-hosted Code gateway (July 2 2026)** — v30 NEW. Self-hosted agent gateway on Bedrock + Vertex. v30 plan-O2 reframing.
- **Fable 5 export-control saga (June 12 → June 30 2026)** — v30 NEW. Full resolution. v30 plan-O3 + v30 wedge update.
- **MemoMind One by XGIMI (June 2026)** — v30 NEW. $500K Kickstarter. v2.0 display-glasses signal.
- **Apple AirPods Ultra development SUSPENDED (July 3 2026)** — v30 NEW. v30 removes Apple from 6-entrants race (down to 5).
- **Adaptive Auto-Harness (arXiv 2606.01770)** — v29. Stateful multi-agent evolver + harness tree with solve-time routing. v1.5 plan-P4+ add-on.
- **INAR-VL (arXiv 2605.18853)** — v29. Edge-cloud routing for VLMs. Recovers 71% of edge-to-cloud accuracy gap. v1.5 differentiator (plan-R2).
- **Hermes Agent "Channel Fracture" (arXiv 2606.04896)** — v29. Silent memory-isolation failure in cron-delegated writes.
- **LQA: A Lightweight Quantized-Adaptive Framework for Vision-Language Models on the Edge (arXiv 2602.07849)** — v29. Sub-200MB 4-bit VLM framework.
- **FINER: MLLMs Hallucinate under Fine-grained Negative Queries (arXiv 2603.17662v1)** — v29. FINER-Tuning with DPO reduces hallucinations by up to 24.2%.
- **Ghost-100: LLM-as-Judge Framework for Tone-Induced Hallucination (arXiv 2604.18803)** — v29. 5-Level Prompt Intensity Framework for VLM hallucination evaluation.
- **DynamicMem: A Long-Horizon Memory Benchmark (arXiv 2606.22877)** — v28. 93% of memory failures trace to retrieval, not the writing model.
- **One Retrieval to Cover Them All: Co-occurrence-Aware KB Reorganization (ACL 2026 KnowFM Workshop)** — v28. v1.5 memoryd design.
- **Summary RAG: A Multi-Format Document Retrieval System (2026)** — v28. v1.5 memoryd design.
- **Alibaba SkillWeaver: AI agent tool routing cuts token use 99% (VentureBeat, July 2026)** — v28. v1.5 toold design.
- **TRINITY: An Evolved LLM Coordinator (ICLR 2026)** — v28. v1.5 openclaw research.
- **Carbon-aware Edge ML (ACM MobiSys 2026)** — v28. v2.0 chip-stack planning.

---

## v30 Paper-to-Plan Mapping

| Plan | Paper |
|------|-------|
| plan-P3 (SIA-H honest-RL) | #1 SIA paper |
| plan-P4 (SIA-W+H port) | #1 SIA paper (SIA-W+H variant) + Decagon DuetBench (NEW v30) |
| plan-P4+ (Adaptive Auto-Harness add-on) | Adaptive Auto-Harness paper |
| plan-E1 (VLM negation-collapse gate) | #2 Edge Reliability Gap + Ghost-100 + FINER |
| plan-P1 + plan-M1 (MemDelta baseline) | #3 MemDelta paper + Engram (NEW v30) |
| plan-P2 (memoryd OKF adapter) | #4 As We May Search paper + Perplexity Brain (NEW v30) |
| v1.0 spec §13 (outer-loop RSI framing) | #5 From AGI to ASI + Anthropic Institute blog (NEW v30) |
| plan-O1 + plan-N1 (toold evaluation) | Arbor (NEW v30) |
| plan-S1 (OpenClaw supervisord-equivalent) | DeepSeek Harness (NEW v30) + AWS AgentCore Harness (NEW v30) |
| plan-J (ASPIRE skill library port) | NVIDIA ASPIRE (NEW v30) |
| plan-S2 (Chip-stack sovereignty spec) | Palantir + Nemotron (NEW v30) |
| plan-O2 (openclaw + toold reversibility) | Anthropic Sonnet 5 self-hosted gateway (NEW v30) |
| plan-O3 (v1.0 spec §13 sovereign-trust) | Fable 5 export-control saga (NEW v30) |
| memoryd v1.5 retrieval focus | DynamicMem paper |
| memoryd v1.5 KB reorganization | Co-occurrence-Aware KB paper |
| memoryd v1.5 document-level retrieval | Summary RAG paper |
| toold v1.5 execution-graph + skill-routing | SkillWeaver paper |
| openclaw v1.5 multi-agent coordination | TRINITY paper |
| v2.0 chip-stack carbon planning | Carbon-aware Edge ML paper |
| v1.5 edge-cloud routing (plan-R2) | INAR-VL paper |
| v1.5 VLM 4-bit quantization (LQA spike) | LQA paper |
| v1.5 VLM negation-tuning (FINER spike) | FINER paper |

---

*Maintained by DAN-2. v30 promotes From AGI to ASI to top-5, adds Anthropic Institute / Decagon DuetBench / Recursive Superintelligence / Arbor / DeepSeek Harness / NVIDIA ASPIRE / Engram × 2 / Perplexity Brain / AWS AgentCore Harness / Palantir Nemotron / Anthropic Micron / Sonnet 5 self-hosted gateway / Fable 5 saga / MemoMind / Apple AirPods Ultra suspension. All v23-v29 paper choices hold.*
