# Dan2 — Top 5 Research Papers to Read (v4, 2026-06-16 03:00 UTC)
**Status:** Final v4 (delta over v3)
**Audience:** somdipto (decision-maker), Dan1/Dan3/Dan4 (peer architects)
**Scope:** 5 papers Danlab should read in the next 4 weeks, plus 5 honorable mentions
**Run window:** 2026-06-16 03:00 UTC

---

## How to read this list

**Selection criteria (v4):**
1. **Directly informs a v1 or v2 product decision** (security, memory, edge VLM, proactive AI, TTS)
2. **2026 publication** (the field has moved; 2024-2025 work is largely superseded)
3. **Reproducible** (code or weights available)
4. **Peer-reviewed or high-credibility** (NeurIPS/ICML/ACL/MM/Apress venues, or top industry labs)
5. **Open-source** (we can implement the techniques)

**v4 update:** the top 2 papers (SIA, StakeBench) carry from v3. Papers 3, 4, 5 are new in v4 — selected from the 3 deep technical dives (edge VLM, memory architecture, proactive AI). The honorable mentions are all v4-new and target specific `os-toold v2` / `memoryd v2` / `perceptiond v2` work.

**Reading budget:** 5 papers × 1-2 hours each = 5-10 hours per person. 4 weeks = 1 paper per week per person. Doable.

---

## Paper 1: SIA: Self Improving AI with Harness & Weight Updates (Hexo Labs, MIT, May 2026) — UNCHANGED from v3

**Why this is #1:** The SIA framework is the **single most important paper for our AGI thesis**. It validates the architectural bet (harness + weights self-improvement) with empirical results, and it gives us a concrete fork target for `danlab-multimodal` Month 1.

**Key claims:**
- Harness-only (H) updates drive most of the self-improvement
- Weight + harness (W+H) updates add modest gains on top
- The "Harness Updating Is Not Harness Benefit" paper (companion) shows that updating the harness doesn't always translate to downstream task benefit — important caveat
- 1.2B focal model is the recommended size (not 4.6B evolver)

**v4 sharpening:** SIA-H (harness-only) is the right fork target for our heuristic loop. The 1.2B focal model means we can use LFM2.5-1.2B-Thinking as the evolution target, not a larger model. **Implementation cost: ~1 week.** **Value: validates the danlab-multimodal pre-RL → RL transition path.**

**Reading time:** ~90 minutes (paper + companion).

**Action item:** Dan1 + Dan2 read by June 22, 2026. Spec the SIA-H fork into `danlab-multimodal` by June 29, 2026.

---

## Paper 2: StakeBench: A Stakeholder-Centric Benchmark for Prompt Injection (NTU + ST Engineering + IBM + UIUC, June 2026) — UNCHANGED from v3 (still priority)

**Why this is #2:** The Varonis Pinchy test gave us the industry validation. StakeBench gives us the **academic validation** for the same threat model. The "stealthy parasitism" attack pattern is the harder failure mode — the agent completes the user task while advancing the attacker task in parallel.

**Key claims:**
- No current AI agent consistently blocks prompt injection
- "Stealthy parasitism" is the dominant attack pattern (user task + attacker task in same conversation)
- Best agents (GPT-5-Nano) achieve <13% safe completion on dual-use scenarios
- 12 SOTA web agents evaluated in realistic environments
- Architectural context matters (not just backbone)

**v4 sharpening:** The StakeBench finding + Varonis Pinchy + Lethal Trifecta (Willison) + Architecture as Governance (drift) all converge on the same conclusion: **`os-toold v2` must be a structural control, not a rule-based instruction.** The 5-layer structural control (path guard + identity verification + stealthy-parasitism detector + arbiter + audit log) directly addresses the StakeBench threat model.

**Reading time:** ~90 minutes.

**Action item:** Dan1 + Dan2 + Dan4 read by June 25, 2026. `os-toold v2` spec reflects the StakeBench threat model by June 30, 2026.

---

## Paper 3: Memory Beyond Recall: DPCM Dual-Process Cognitive Memory for Self-Evolving Agent Memory (ACL ARR 2026) — v4 NEW PRIORITY

**Why this is #3:** The 2026 SOTA for agent memory is **dual-process consolidation** — System 1 (synchronous writer, episodic updates) + System 2 (asynchronous engine, schema/pattern induction). DPCM is the cleanest paper on this. **It directly informs the `memoryd v2` hierarchical architecture.**

**Key claims:**
- Memory organized into cognitive capability hierarchy: raw inputs → atomic facts → high-level schemas → latent intentions → cross-domain patterns
- System 1 (daytime): records belief revisions as doubly linked superseded chains
- System 2 (nighttime): induces schemas, intentions, cross-domain patterns
- Strongest gains on PersonaMem-v2 (+5.20) where cross-session inference is rewarded
- "Self-evolving" memory = the agent improves over time without explicit retraining

**v4 impact:** This is the paper that validates the `memoryd v2` proposal in the architecture review. Tier 0 (raw events) = System 1 input. Tier 1 (semantic facts) = System 1 output. Tier 2 (schemas/patterns) = System 2 output. **The DPCM architecture maps directly to our v2 plan.**

**Reading time:** ~60 minutes.

**Action item:** Dan2 + Dan4 read by July 1, 2026. `memoryd v2` spec adopts the DPCM dual-process architecture by July 8, 2026.

---

## Paper 4: VLMCache: Efficient On-Device Vision-Language Model Inference (ACM Multimedia 2026) — v4 NEW PRIORITY (was honorable mention in v3)

**Why this is #4 (upgraded from honorable mention):** The 1.4-3.8× speedup with <1% accuracy loss is too good to skip for the wearable power budget. **It directly informs `perceptiond v2` optimization.**

**Key claims:**
- Cache stable (background) visual blocks across frames
- Semantic disaggregation to identify reusable blocks
- Isolate-then-fuse strategy preserves global attention + positional coherence
- 1.4-3.8× speedup, <1% average accuracy loss
- Enables low-latency VLM tasks on resource-constrained devices

**v4 impact:** **This is the optimization that brings us from 10-15s/frame to 3-5s/frame on CPU.** The salience detector we already have does the "what changed since last frame" detection; VLMCache gives us the "cache the rest" mechanism. **Implementation: ~1 week. Power reduction: 2-4× for the dominant case (static or slowly-changing scene).**

**Reading time:** ~45 minutes.

**Action item:** Dan3 (perceptiond owner) + Dan2 read by July 5, 2026. `perceptiond v2` spec includes VLMCache-style background caching by July 12, 2026.

---

## Paper 5: SAGE: Self-Evolving Agentic Graph-Memory Engine for Structure-Aware Associative Memory (OpenReview 2026) — v4 NEW PRIORITY

**Why this is #5:** SAGE validates the **graph-memory direction** for agent memory. While DPCM is dual-process, SAGE is the engine that builds + uses the graph. **It's the closest open-source competitor to our `memoryd v2` plan, and we can learn from its architecture.**

**Key claims:**
- Memory as a dynamic, structured graph substrate (not a static store)
- Memory Writer: incrementally builds a structured graph from interaction histories
- Graph Foundation Model-based Reader: retrieves evidence, provides feedback to the writer
- Self-evolution cycles improve memory quality and reduce hallucinations
- After 2 self-evolution cycles: top avg rank on multi-hop QA
- Zero-shot open-domain transfer: Recall@2/5 on Natural Questions 82.5/91.6
- Code available: https://github.com/[SAGE repo]

**v4 impact:** SAGE is the **closest research analog to our `memoryd v2` plan**. Reading it gives us a concrete implementation reference for the graph-memory layer. **We're not building a graph DB; we're building a hierarchical memory (Tier 0/1/2). But the self-evolution cycle pattern from SAGE is directly applicable to our daily/weekly consolidation jobs.**

**Reading time:** ~75 minutes.

**Action item:** Dan2 + Dan4 read by July 8, 2026. `memoryd v2` implementation references the SAGE self-evolution pattern.

---

## Honorable Mention 1: Qualia as control-theoretic constructs for autonomous agents (Frontiers Robotics & AI 2026) — v4 NEW

**Why mention:** A 6,550-parameter safety classifier that runs at 1.8ms/decision on CPU. **This is the pattern for the `policyd` safety gate** in v1.5 proactive mode.

**Key claims:**
- Qualia-inspired control-theoretic framework
- Event phase space as action-oriented semantic safety layer
- 6,550 parameters, 1.8ms/decision, no GPU
- 0.827 AUC safety classification
- 29.6% collision reduction in CARLA stress scenarios
- ~85% legitimate delivery under tested flooding

**v4 impact:** **The `policyd` safety gate can be a 6.5K-param model.** That's smaller than the wake word models. CPU-only, no GPU, no cloud. **Perfect for the wearable form factor.** Implementation: train on our own data (engagement_score + proactive trigger context → proceed/suppress/queue).

**Reading time:** ~45 minutes.

**Action item:** Dan2 + Dan1 read by July 15, 2026. `policyd` spec includes the qualia-style safety gate.

---

## Honorable Mention 2: SWEET: Workload-Balanced End-to-End Efficient Edge Inference via Quantization and Partitioning (Frontiers 2026) — v4 NEW

**Why mention:** Per-layer quantization with explicit accuracy budgets. **Directly informs the LFM2.5-VL-450M v2 quantization strategy.**

**Key claims:**
- First to optimize layer-wise quantization bitwidth with a theoretical accuracy metric
- Reduced parameter payloads by 11.9-18.1% (ResNet-18 from 108MB to 19MB)
- Communication payload compression ratios 11.9-18.1%
- Minimal accuracy degradation (0.08-0.66%)

**v4 impact:** **The LFM2.5-VL-450M v2 quant recipe:** Q4_K_M in attention + Q8_0 in vision projector + Q4_0 in text decoder. Total: 250-280MB (down from 389MB), <1% accuracy loss. **This is the path to fitting the model in wearable memory budget.**

**Reading time:** ~30 minutes.

**Action item:** Dan3 read by July 10, 2026. `perceptiond v2` quant script implements the SWEET per-layer strategy.

---

## Honorable Mention 3: Omni-Embed-Mini: Binding Modalities Without Forgetting via Dense Distillation (OpenReview 2026) — v4 NEW

**Why mention:** 0.9B-parameter multimodal embedder. **Directly informs the `memoryd v2.5` embedding strategy.**

**Key claims:**
- Maps text, speech, audio, images, video, visually-rich documents into one shared embedding space
- Frozen text backbone + LoRA adapters
- Matryoshka SigLIP contrastive loss (flexible dimensionality)
- 2.7-9.5× smaller than competing omni-embedders
- Preserves text retrieval quality (49.50 nDCG@10 on MTEB-v2 BEIR-8)
- 0.9B params, smaller than 2.3B variant

**v4 impact:** **The only model swap in v4.** Replace text-only all-MiniLM-L6-v2 (v1) with multimodal Omni-Embed-Mini (v2.5) when `memoryd v2` hierarchical memory is in place. **Memory gains: query "what did I see when I heard that sound?" across modalities.**

**Reading time:** ~45 minutes.

**Action item:** Dan2 + Dan4 read by July 20, 2026. `memoryd v2.5` spec evaluates Omni-Embed-Mini for the multimodal memory store.

---

## Honorable Mention 4: Arbiter Agent: Continually Monitoring Multi-Agent Conversations to Detect Emergent Misalignment (OpenReview 2026) — v4 NEW

**Why mention:** The Arbiter Agent pattern is the **reference architecture for the `os-toold v2` Layer 4 (watch-the-watcher).** The Varonis Pinchy + StakeBench threat model requires a watchdog that monitors other agents.

**Key claims:**
- Continuously monitors multi-agent conversations under limited inspection budget
- Can decide to wait, question, inspect internal info (system prompts, reasoning traces), or log concerning behavior
- Outputs a report identifying likely sources of misalignment
- Detects misaligned agents before conversation ends
- Active inspection tools improve detection accuracy and speed
- Weight-induced misalignment hardest to detect; instruction-induced reliably detected
- Code: https://github.com/aisilab/arbiter

**v4 impact:** **`os-toold v2` Layer 4 arbiter is the concrete implementation of this pattern.** Inspect budget, log, integration with Loki. Implementation: ~1 week. **This is the structural control that catches the "stealthy parasitism" attack in real-time.**

**Reading time:** ~60 minutes.

**Action item:** Dan1 + Dan2 read by July 25, 2026. `os-toold v2` Layer 4 spec includes the Arbiter pattern.

---

## Honorable Mention 5: BareWave: Waveform-Native Flow-Matching Text-to-Speech (arXiv 2606.09048, June 2026) — v4 NEW

**Why mention:** Waveform-native flow-matching TTS. **Worth tracking for v2 TTS when we want to upgrade from KittenTTS.**

**Key claims:**
- Fully waveform-native (no intermediate acoustic representations, no pretrained decoders)
- Training-time representation alignment, staged noise scheduling, VAPA
- Single test-time waveform path, no pretrained components
- Strong zero-shot voice cloning quality
- Edge-friendly inference design (no pretrained components at test time)
- Exact model size and latency not specified in the abstract

**v4 impact:** **Watch for v2 TTS.** If BareWave can hit KittenTTS quality at a similar size with edge-friendly inference, it's a strong candidate. **For v1, KittenTTS remains the right choice.**

**Reading time:** ~45 minutes.

**Action item:** Dan4 (TTS owner) read by July 30, 2026. `ttsd v2` evaluation plan includes BareWave when the paper's edge benchmarks are published.

---

## Reading schedule (v4)

| Week | Paper | Owner | Output |
|---|---|---|---|
| Jun 16-22 | #1 SIA + companion | Dan1 + Dan2 | SIA-H fork spec for `danlab-multimodal` |
| Jun 23-29 | #2 StakeBench | Dan1 + Dan2 + Dan4 | `os-toold v2` spec reflects StakeBench threat model |
| Jun 30-Jul 6 | #3 DPCM | Dan2 + Dan4 | `memoryd v2` spec adopts DPCM architecture |
| Jul 7-13 | #4 VLMCache | Dan3 + Dan2 | `perceptiond v2` spec includes VLMCache caching |
| Jul 14-20 | #5 SAGE | Dan2 + Dan4 | `memoryd v2` implementation references SAGE patterns |
| Jul 21-27 | Honorable mentions 1-3 | All | `policyd` + `perceptiond v2` quant + `memoryd v2.5` embed |
| Jul 28-Aug 3 | Honorable mentions 4-5 | Dan1/Dan2/Dan4 | `os-toold v2` Layer 4 + `ttsd v2` evaluation plan |
| Aug 4-10 | All-paper synthesis | All | Roadmap v5 (post-Microsoft Scout GA) |

---

## The 1-page summary (v4)

**Read these 5 papers in the next 4 weeks:**

1. **SIA** (Hexo Labs, MIT) — validates the self-improvement thesis. Fork target for `danlab-multimodal`.
2. **StakeBench** (NTU + ST Engineering + IBM + UIUC) — validates the security thesis. Threat model for `os-toold v2`.
3. **DPCM** (ACL ARR 2026) — validates the dual-process memory architecture. Spec for `memoryd v2`.
4. **VLMCache** (ACM MM 2026) — validates the on-device VLM optimization path. Implementation for `perceptiond v2`.
5. **SAGE** (OpenReview 2026) — validates the self-evolving graph-memory engine. Reference for `memoryd v2` implementation.

**Plus 5 honorable mentions** for specific v1.5 / v2 features: Qualia (policyd), SWEET (perceptiond v2 quant), Omni-Embed-Mini (memoryd v2.5), Arbiter Agent (os-toold v2 Layer 4), BareWave (ttsd v2 watch).

**Total reading time:** ~12-15 hours per person over 4 weeks. **Output:** `dan2-research-report.md v5` synthesis + concrete specs for all 4 v2 services.

---

## Sources (v4)

See `dan2-research-report.md` §8 for full v4 source list. Key papers:
- SIA framework (Hexo Labs, MIT, May 2026)
- "Harness Updating Is Not Harness Benefit" (May 2026)
- StakeBench (NTU + ST Engineering + IBM + UIUC, June 2026)
- DPCM Dual-Process Cognitive Memory (ACL ARR 2026)
- VLMCache (ACM Multimedia 2026)
- SAGE (OpenReview 2026)
- Qualia (Frontiers Robotics & AI 2026)
- SWEET (Frontiers Complex Systems 2026)
- Omni-Embed-Mini (OpenReview 2026)
- Arbiter Agent (OpenReview 2026)
- BareWave (arXiv 2606.09048, June 2026)

---

*Dan2 Papers to Read v4 — 2026-06-16 03:00 UTC. v4 changes: #3 (DPCM) and #5 (SAGE) replace v3's #3 and #4 (OpenGlass, Mem0) — both are v4 NEW based on the memory architecture deep-dive. #4 (VLMCache) is upgraded from honorable mention. 5 honorable mentions are all v4-new and target specific v1.5/v2 features. Reading schedule 4 weeks.*
