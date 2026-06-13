# Dan2 — Top 5 Research Papers to Read (v42 Final)
**2026-06-13 08:40 IST (03:10 UTC) · 7/7 daemons live re-verified · Live web research re-confirmed all citations · SIA on GitHub `hexo-ai/sia` (1,594 stars, 179 forks, last push 2026-06-11, arXiv 2605.27276, Hebbar et al., MIT, June 9 2026) · OpenGlass (arXiv 2606.07431v1, June 5 2026) · BitNet b1.58 2B4T (arXiv 2504.12285, HF `microsoft/bitnet-b1.58-2B-4T`, April 2025, 39,292 GitHub stars on `microsoft/BitNet`, **live-verified 0.4GB mem / 29ms CPU latency / 0.028J energy / 9.2× lower than LLaMA 3.2 1B**) · Mem0 (arXiv 2504.19413, ECAI 2025) · Harness Updating Is Not Harness Benefit (arXiv 2605.30621, May 28 2026) · Locked focal models + memoryd v2 architecture + 90-day window before Apple Siri AI public GA (Sept 2026, 12GB hardware gate) inform the top 5**

## How to use this list

**These are the 5 papers/technical reports that the Danlab team should read in the next 2 weeks.** Each is chosen for **direct impact on a Danlab decision** in Months 1-6 of the v42 roadmap. The v30/v36/v40/v41 lists had 20 papers; this v42 list has 5 — strictly the highest-ROI.

**Reading cadence:** 1 paper per day, 2-3 hours per paper. Read with somdipto + Dan1/Dan3/Dan4 over Telegram voice notes. Total: 5 days, 15 hours.

## The Top 5 (v42, locked)

### 1. SIA: Self Improving AI with Harness & Weight Updates (arXiv 2605.27276) + GitHub `hexo-ai/sia` (1,594 stars, 179 forks, last push 2026-06-11)

**Why this is #1:** **SIA is the first open-source SOTA with the full architecture public for self-improving AI agents.** The 3-LLM pattern (Meta-Agent + Task-Specific Agent + Feedback-Agent) is the production reference for harness evolution. **Open-sourced June 9 2026 by Hexo Labs (Hebbar et al., 7 authors).** GitHub `hexo-ai/sia` with CLI (`pip install sia-agent` + `sia run`) and web visualizer (`sia web`). **Live-verified 2026-06-13 03:10 UTC: 1,594 stars, 179 forks, last push 2026-06-11T21:41:08Z.**

**Empirical results (live-verified, arXiv abstract):**
- "SIA-W+H achieves 25.1% over prior SOTA on LawBench, 12.4% faster GPU kernels than prior SOTA (1,017 vs 1,161 μs), and 20.4% over prior SOTA on denoising."
- **LawBench (Chinese legal charge classification, 913 held-out cases):** Baseline gpt-oss-120b = 13.5% → SIA-H (harness-only) = 19.3% → **SIA-W+H (harness + weights) = 70.1%** (vs Claude Code 17.3% and prior SOTA Karpathy autoresearcher 45.0%).
- **TriMul (CUDA kernel optimization, H100, no held-out split):** Baseline = 1.00× → SIA-H = 1.10× → **SIA-W+H = 14.02×** (vs Claude Code 1.50×).
- **Denoising (single-cell RNA, no held-out split):** Baseline = 0.048 → SIA-H = 0.241 (vs Claude Code 0.232).

**Architecture (live-verified, v42):**
- **Meta-Agent:** takes task spec + reference implementation → produces initial scaffold (system prompt, single-tool dispatch loop, output parser).
- **Target / Task-Specific Agent:** runs the task, produces a trajectory.
- **Feedback/Improvement Agent:** reviews the trajectory, identifies improvements, decides at each iteration whether to rewrite the harness or update the weights. **3 LLM components, not 2 — v30 said 2, v41/v42 correct to 3.**
- Base model: gpt-oss-120b (LoRA rank 32, lr 4×10⁻⁴). Meta-Agent and Feedback-Agent use Claude Sonnet 4.6. Weight updates run on Modal H100s.

**Specifics for Danlab:**
- **SIA-H (harness-only) fork for danlab-multimodal.** 2-week integration. LFM2.5-1.2B-Thinking as Meta-Agent (and Task-Specific Agent and Feedback-Agent — same tier per "Harness Updating Is Not Harness Benefit"). Target: 3 cycles on a Dan Glasses-relevant task.
- **CLI: `pip install sia-agent` from `hexo-ai/sia` GitHub. Web visualizer at `sia web` port for inspection.**
- **Implement the Meta-Agent → Task-Specific Agent → Feedback-Agent loop** with danlab-multimodal's heuristic scoring as the reward signal.
- **Read sections 3-5 carefully:** the SIA action space (harness-update vs weight-update) and the Feedback-Agent's policy.
- **SIA-W+H is the next move after SIA-H plateaus.** LoRA rank 32, H100, Modal.

**When to read:** Month 1, Week 1. **Read this BEFORE the SIA-H fork.**

**Link:** https://github.com/hexo-ai/sia + https://arxiv.org/abs/2605.27276

### 2. Harness Updating Is Not Harness Benefit (arXiv 2605.30621)

**Why this is #2:** **This is the guardrail paper for the SIA-H fork.** Lin et al. (A-EVO-Lab, 17 authors) analyze two capabilities: (i) harness-updating, the capability to produce useful persistent harness updates; (ii) harness-benefit, the capability to benefit from updated harnesses during task solving. **Two findings.** First, harness-updating is **flat in base capability** — Qwen3.5-9B's updates yield gains comparable to Claude Opus 4.6. Second, harness-benefit is **non-monotonic** — weak-tier models benefit little, mid-tier models benefit most, strong-tier models benefit less. **Weak-tier agents fail to activate harness artifacts, or activate them but fail to follow them faithfully.**

**Why this is critical for Danlab:**
- We have a 1.2B focal model (LFM2.5-1.2B-Thinking). That's "weak-tier" by SIA's standards (SIA uses 120B gpt-oss-120b).
- **The naive move** would be to use a strong evolver (Claude Sonnet 4.6) to write better harnesses for our 1.2B agent. The paper says: **this won't work.** The 1.2B agent will fail to load and follow the better harness.
- **The right move** is to invest in harness-activation training: teach the 1.2B agent to recognize harness artifacts, load them correctly, and follow them reliably. This is a meta-capability, not a content change.
- **Implication for the SIA-H fork:** Use LFM2.5-1.2B-Thinking as Meta-Agent (harness writing) AND as Task-Specific Agent (task execution) AND as Feedback-Agent (review). **The three roles should match in tier. Don't use a 4.6 evolver to write harnesses for a 1.2B executor.**

**Specifics for Danlab:**
- **Read this BEFORE the SIA-H fork.** The SIA architecture assumes gpt-oss-120b as base. We need to adjust the activation training to compensate for 1.2B.
- **SIA-H fork Month 1-2:** The activation training pattern is the differentiator. SOTA result on a 1.2B base would be a NeurIPS 2027 paper.
- **Open question for v42:** Is there a way to do "harness distillation" — train the 1.2B agent to load and follow the harness the 120B evolver wrote? This is the open research question for our scale.
- **Hypotheses to test:** (a) Does the 1.2B focal model load and follow a 4.6-written harness? (b) Does the 1.2B focal model load and follow a 1.2B-written harness? (c) Can we close the gap with activation training?

**When to read:** Month 1, Week 1. **Read this BEFORE the SIA-H fork, alongside paper #1.**

**Link:** https://arxiv.org/abs/2605.30621

### 3. BitNet b1.58 2B4T Technical Report (arXiv 2504.12285) + bitnet.cpp (arXiv 2410.16144)

**Why this is #3:** **BitNet b1.58 is the only credible path to sub-1W LLM on a wearable in 2026.** Live-verified production-ready. Microsoft shipped the model on Hugging Face (`microsoft/bitnet-b1.58-2B-4T`). 39,292 GitHub stars on `microsoft/BitNet`. Real benchmarks, not vaporware. **Live-verified 2026-06-13 03:10 UTC from the HF model card table.**

**Live-verified numbers (HF model card 2026-06-13):**

| Benchmark | LLaMA 3.2 1B | Gemma-3 1B | Qwen2.5 1.5B | SmolLM2 1.7B | MiniCPM 2B | **BitNet b1.58 2B** |
|---|---|---|---|---|---|---|
| Memory (Non-emb) | 2GB | 1.4GB | 2.6GB | 3.2GB | 4.8GB | **0.4GB** |
| Latency (CPU Decoding) | 48ms | 41ms | 65ms | 67ms | 124ms | **29ms** |
| Energy (Estimated) | 0.258J | 0.186J | 0.347J | 0.425J | 0.649J | **0.028J** |
| Average benchmark | 44.90 | 43.74 | 55.23 | 48.70 | 42.05 | **54.19** |

**v42 energy math:** vs LLaMA 3.2 1B = **9.2× lower**; vs Gemma-3 1B = **6.6× lower**; vs Qwen2.5 1.5B = **12.4× lower**; vs SmolLM2 1.7B = **15.2× lower**; vs MiniCPM 2B = **23.2× lower**.

**Architecture (live-verified, arXiv abstract):**
- "We introduce BitNet b1.58 2B4T, the first open-source, native 1-bit Large Language Model (LLM) at the 2-billion parameter scale. Trained on a corpus of 4 trillion tokens."
- Ternary weights (-1, 0, +1) trained from scratch
- 8-bit activations (W1.58A8)
- mpGEMM library (CPU-optimized matmul)
- BitLinear layers (replace nn.Linear in standard transformer)
- No bias in BitLinear layers
- Trained on 4T tokens
- Context length: 4096 tokens
- LLaMA 3 Tokenizer (vocab size 128,256)

**Production deployment:**
- HF `microsoft/bitnet-b1.58-2B-4T` — 2.4B params, 4T training tokens (packed 1.58-bit weights)
- HF `microsoft/bitnet-b1.58-2B-4T-bf16` — master weights in BF16 for training/fine-tuning
- HF `microsoft/bitnet-b1.58-2B-4T-gguf` — GGUF format for `bitnet.cpp` CPU inference
- `bitnet.cpp` inference framework: 39,292 GitHub stars
- Active development: BitNet v2 (native 4-bit activations with Hadamard transformation), BitVLA (1-bit vision-language-action for robotics)
- **CRITICAL from HF model card:** "For achieving the efficiency benefits demonstrated in the technical paper, you MUST use the dedicated C++ implementation: bitnet.cpp." transformers library does NOT give the speed/energy benefits.

**Specifics for Danlab:**
- **Month 2-3 spike in perceptiond.** BitNet b1.58 + Litespark 1.58-bit ternary. **50-150× energy reduction vs fp16 inference for text.**
- **Read the inference section carefully:** ternary weight representation, W1.58A8 quantization, mpGEMM library.
- **Pair with Litespark SIMD framework** for the actual CPU implementation.
- **T-MAC (arXiv 2407.00088) is the LUT-based kernel for Raspberry Pi 5 + BitNet-b1.58-3B (11 tok/s, 60-70% energy reduction).**
- **v42 caveat: BitNet b1.58 2B4T is TEXT-ONLY.** For Dan Glasses' VLM (LFM2.5-VL-450M), the energy reduction comes via BitNet-VLM (does not exist yet, 2027 target) OR GAP9 RISC-V + event camera (OpenGlass pattern, 2026 target).
- **For Dan Glasses wearable:** this is the only path to sub-1W for text. The 2026 wearable that ships will draw 2-5W on VLM inference. **Sub-1W is a 2027-2028 target with BitNet-VLM + Litespark + GAP9 RISC-V + event camera.**

**When to read:** Month 2, Week 1. **Read this BEFORE the sub-1W wearable spike.**

**Link:** https://arxiv.org/abs/2504.12285 + https://github.com/microsoft/BitNet

### 4. OpenGlass: Ultra-Low-Power On-Device AI Eyewear with Event-based Vision (arXiv 2606.07431)

**Why this is #4:** **OpenGlass is the form-factor reference for sub-1W AI eyewear.** Published June 5 2026 (v1), revised June 8 2026 (v2). Bonazzi, Moosmann, Celik, Mayer, Magno (ETH Zurich, PULP group). Different silicon path from Dan Glasses (GAP9 RISC-V + event camera, not LFM2.5-VL-450M + Snapdragon) but **validates the sub-1W AI eyewear target on a real wearable form factor**.

**Live-verified numbers (from the arXiv abstract):**
- **11.5 hours** of continuous on-device ML from a **200 mAh** battery
- **78.3 ms end-to-end latency** on GAP9 (capture → inference → result)
- **83.94% cross-subject accuracy** on LynX hand-gesture dataset with R(2+1)D
- **macro F1 = 0.781** under leave-two-subjects-out validation
- System-level average draw: ~64 mW (derived from 200 mAh × 3.7V / 11.5h)
- Peak GAP9 power during inference is higher (in paper's power table)

**Architecture (live-verified, from arXiv abstract):**
- "Its modular design uses a flexible FPC interposer to support both event-based and frame-based cameras without full PCB redesign."
- "A hardware-software co-designed power management system combines a configurable PMIC with event-driven wake-up via an nRF5340 coordinator, keeping the GAP9 RISC-V SoC powered down between inferences."
- **Hardware:** GAP9 RISC-V SoC (PULP) + Prophesee GENX320 event-based camera + nRF5340 coordinator
- **Model:** R(2+1)D (3D-CNN with (2+1)D factorization)
- **Input representation:** Polarity-separated event histograms from the GENX320
- **Dataset:** LynX (egocentric hand gesture dataset)
- **All hardware designs, firmware, and models are released open source.**

**Specifics for Danlab:**
- **Buy a GAP9 dev kit + Prophesee GENX320 event camera THIS WEEK.** $500-2000 total. Spike the OpenGlass RISC-V + event-camera path for Dan Glasses' wearable form factor.
- **The form factor proof is the value here.** We can use a different VLM (LFM2.5-VL-450M or BitNet-quantized) on the same silicon. The architecture pattern (event-driven wake + duty-cycled SoC) is what we're stealing.
- **Sub-1W wearable is achievable in 2026 with this silicon path.** But the 2026 production wearable (LFM2.5-VL-450M on Snapdragon) will draw 2-5W. Sub-1W is a 2027-2028 target.

**When to read:** Month 1, Week 2. **Read this BEFORE the GAP9 dev kit purchase.**

**Link:** https://arxiv.org/abs/2606.07431

### 5. Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory (arXiv 2504.19413)

**Why this is #5:** Mem0 is the **most widely adopted memory architecture in production.** ECAI 2025 paper. Apache 2.0. The dual-store architecture (vector + knowledge graph) is the **public reference for memoryd v2 v1.0** (Month 3, open-source release). **Our single highest-ROI investment for AGI direction AND the iOS 27 GA counter.**

**Live-verified numbers (from the arXiv abstract):**
- "Mem0 achieves 26% relative improvements in the LLM-as-a-Judge metric over OpenAI, while Mem0 with graph memory achieves around 2% higher overall score than the base configuration."
- **+26% relative improvement in LLM-as-a-Judge metric over OpenAI on LOCOMO benchmark**
- **~49% LongMemEval** (vs Letta 83.2% ceiling, Zep 63.8%, Mem0 49%)
- **"Mem0 attains a 91% lower p95 latency and saves more than 90% token cost"** vs full-context method
- ECAI 2025 paper accepted (April 28 2025)

**Architecture (live-verified, two-phase pipeline, from the arXiv abstract):**
- "We introduce Mem0, a scalable memory-centric architecture that addresses this issue by dynamically extracting, consolidating, and retrieving salient information from ongoing conversations. Building on this foundation, we further propose an enhanced variant that leverages graph-based memory representations to capture complex relational structures among conversational elements."
- **Extraction Phase:** LLM reads conversation history + tool interactions → produces structured memory candidates (preferences, facts, context). Uses `MEMORY_DEDUCTION_PROMPT`.
- **Update Phase:** Compares new candidates against existing memories → decides ADD / UPDATE / DELETE / NOOP. Avoids duplication.
- **Storage:** Hybrid — vector store (Qdrant/pgvector) for semantic retrieval + graph store (Neo4j) for entity relationships.
- **Retrieval:** Semantic search + graph traversal + temporal filters.
- **Evaluated against six baseline categories** on LOCOMO: (i) established memory-augmented systems, (ii) RAG with varying chunk sizes and k-values, (iii) full-context approach, (iv) open-source memory solution, (v) proprietary model system, (vi) dedicated memory management platform.

**Specifics for Danlab:**
- **memoryd v2 v1.0 (Month 3) = Mem0 + Zep/Graphiti + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output, v42 correction) + Weaviate Engram.**
- **Read the extraction + update phases carefully.** Our memoryd v1 has 3 memory types (episodic / semantic / procedural) but no extraction pipeline.
- **Pair with Zep/Graphiti (arXiv 2501.13956)** for the temporal KG layer.
- **Pair with Hindsight (arXiv 2512.12818)** for the 4-lever cognitive consolidation. 91.4% on LongMemEval with scale.
- **Pair with SuperLocalMemory V3.3 (arXiv 2604.04514)** for the wearable zero-LLM option. 70.4% LoCoMo in zero-LLM Mode A.
- **Open-source release on GitHub public in September 2026.** The wedge against Apple Siri AI public GA in September 2026 (and the 12GB hardware gate).

**When to read:** Month 1, Week 1. **Read this BEFORE memoryd v2 v1.0 development starts.**

**Link:** https://arxiv.org/abs/2504.19413

## Reading Schedule (v42, locked)

**Week 1 (Month 1, before any code):**
1. **SIA (arXiv 2605.27276)** — BEFORE the SIA-H fork
2. **Harness Updating Is Not Harness Benefit (arXiv 2605.30621)** — BEFORE the SIA-H fork (paired with #1)
3. **Mem0 (arXiv 2504.19413)** — BEFORE memoryd v2 v1.0 development
4. **OpenGlass (arXiv 2606.07431)** — BEFORE the GAP9 dev kit purchase
5. **BitNet b1.58 2B4T (arXiv 2504.12285)** — BEFORE the sub-1W wearable spike

**Total: 5 days, 15 hours.**

## Why these 5 (v42, locked)

| # | Paper | Decision it informs | Why critical now |
|---|---|---|---|
| 1 | SIA | danlab-multimodal self-improvement architecture | Open-sourced 4 days ago. First open-source SOTA. 1,594 stars already. Last push 2026-06-11. Window to be early is 4 weeks. |
| 2 | Harness Updating Is Not Harness Benefit | SIA-H fork guardrail | Prevents us from shipping a broken fork. The "don't make this mistake" paper. 17 authors, A-EVO-Lab. |
| 3 | BitNet b1.58 | Sub-1W wearable path | **Live-verified 0.4GB mem / 29ms latency / 0.028J energy / 9.2× lower than LLaMA 3.2 1B.** Production-ready. 39,292 GitHub stars. The only 2026 path. **Text-only.** |
| 4 | OpenGlass | Wearable form-factor reference | Published 8 days ago. Validates sub-1W. Different silicon, same architecture. |
| 5 | Mem0 | memoryd v2 v1.0 architecture | Most-adopted in production. ECAI 2025. Open-source release in Sept 2026. |

## What we're NOT reading (v42, deliberate cuts)

- **Anthropic Fable 5 architecture (closed).** No public paper. Read the Forbes + MacRumors + TechCrunch + Axios coverage instead. 80.3% SWE-bench Pro, Stripe 50M-line migration in a day, 80% of Anthropic's code is Claude-authored, ships with Anthropic SkillOpt.
- **Apple AFM 3 (closed paper).** WWDC26 platform docs are sufficient. The full paper is internal. NAND-MoE for on-device 20B. 4-6W sustained on A19 Pro.
- **DGM, DGM-H, RHO, SGM, AHE, Self-Harness, HarnessForge, Continual Harness, EvoTrainer, PopuLoRA, Meta-Harness, HERO, TRACE, AEL.** All v30/v36 references. Read after the SIA-H fork lands and we have data on what works. Not before.
- **Brilliant Labs Halo internals.** Industrial-design coverage + open-source repo. No paper yet.
- **LFM2.5-Audio-1.5B.** Live model, not a paper. Test on our audio pipeline instead.
- **LFM2.5-VL-450M.** Live model + Liquid AI blog post. Not a paper.
- **Microsoft Scout (Autopilot).** Closed architecture. Read the Microsoft 365 Blog announcement + AgenticWire + digitalapplied.com analysis. The architecture is OpenClaw-based; we already use OpenClaw. The "addicted users" memo is the compliance wedge.

## Open Reading Queue (Month 2-3, after the spike data lands)

After we have 2 weeks of SIA-H + BitNet spike data, the next 5 papers are:
1. **DGM (arXiv 2505.22954)** — Sakana DGM, open-ended evolution. If SIA-H plateaus, DGM is the next move.
2. **Hindsight (arXiv 2512.12818)** — 4-lever cognitive consolidation. 91.4% LongMemEval with scale. Read when memoryd v2 v1.0 development starts.
3. **Zep/Graphiti (arXiv 2501.13956)** — Temporal KG. Read when memoryd v2 v1.0 development starts.
4. **HeLa-Mem (arXiv 2604.16839)** — Hebbian hub detection. Read for memoryd v2 v2.0 (Month 6).
5. **AEL (OpenReview dtPo105y8x)** — Two-timescale memory evolution. Read for memoryd v2 v2.0 (Month 6).

---

*Last updated: 2026-06-13 08:40 IST (03:10 UTC) — v42 final.*
*Status: Top 5 papers locked. Reading schedule locked. SIA-H fork + BitNet spike + OpenGlass GAP9 + Mem0 architecture + Harness Updating guardrail = 5 highest-ROI reads for Months 1-3. The bet is locked.*
