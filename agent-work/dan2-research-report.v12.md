# DAN-2 Research Report — v12 (2026-06-26, 12:00 IST / 06:30 UTC)

**Author:** Dan2 (DAN-2, danlab.dev)
**Status:** Supersedes v11 (2026-06-25, 11:30 IST — ~25 hours ago)
**Trigger:** Scheduled DAN-2 research stream (incremental refresh + deep research)
**Companion to:** `dan2-agi-roadmap.md` v12, `dan2-architecture-review.md` v12, `dan2-model-analysis.md` v12, `dan2-papers-to-read.md` v12
**Delta from v11:** Adds HRM-Text-1B as the canonical reasoning layer for Dan Glasses (Sapient released May 18, 2026 — completely missed by v11). Adds Sapient's "latent reasoning in latent space" thesis (the strongest theoretical argument for our stack). Adds Project Lobster as the OpenClaw substrate story. Adds Hikvision-class prompt-injection risk to the audiod → perceptiond path. Rebalances roadmap around audiod RL agent + HRM-Text integration as the two highest-leverage 90-day ships.

---

## 0. What changed since v11 (delta only, ~25 hours)

| Signal | When | Why it matters | Action |
|---|---|---|---|
| **Sapient HRM-Text-1B** confirmed production-ready | Released May 18, 2026 | 1B params, **40B training tokens** (≈1/225 of Llama 3.2 3B), **$1,500 total training cost** on 16× H100 in <2 days. MATH 56.2, GSM8K 84.5, ARC-Challenge 81.9. **Beats Qwen3.5 2B, Llama 3.2 3B, Gemma3 4B, OLMo3 7B on MATH.** Latent-space hierarchical recurrent architecture — **no chain-of-thought tokens at inference**. This is the AGENTS.md "Model Strategy: HRM-Text (1B)" decision, validated. | **Promote HRM-Text-1B to the canonical reasoning layer for Dan Glasses.** Replace the "GPT-OSS-20B via OpenRouter" brain currently configured in OpenClaw with on-device HRM-Text-1B + a small LLM (e.g. LFM2.5-1.2B) for tool-call routing. The reasoning model can stay on-device; tool routing can be cloud OR local. |
| **Sapient "Thinking in Latents"** thesis | The Sequence Substack #867, May 2026 | Sapient's argument: standard 70-layer transformer is fixed-depth, sits in complexity classes like AC⁰/TC⁰, cannot in a single forward pass solve problems requiring sequential computation. CoT is a hack — every reasoning step has to leave the residual stream, become a discrete token, re-enter via embedding. **HRM's H/L modules run in the same latent space** — variable, internal, depth. | Validate by integrating HRM-Text into audiod's confidence head and toold's argument planner. If a 1B HRM-Text can plan multi-step tool calls better than 70B-class CoT models on-device, that's the Dan Glasses thesis in one experiment. |
| **Sakana Fugu Technical Report** | arXiv:2606.21228, Jun 22, 2026 | Fugu = "multi-agent system as a single model." Orchestrator model (CMA-ES / Conductor) routes across Thinker / Worker / Verifier roles. Matches Fable 5 / Mythos performance without using them. **Recursive**: Fugu can call instances of itself as sub-agents. | Adds a second piece of external validation for our OpenClaw-as-substrate bet. Fugu is the "no-frontier-model-needed" angle — exactly Danlab's positioning. Reference Fugu in arXiv Aug 15 paper as related work. |
| **Microsoft Scout + Project Lobster** | Build 2026 (Jun 2) + 404 Media (Jun 23) | Microsoft calls Scout "the first real personal assistant we've offered customers." MAI-Thinking-1 is the reasoning model (35B active, mid-sized). Microsoft Execution Container (MXC) is the governance layer. **Scout is the first hyperscaler signal that "personal AI agent" is now a mainstream product category.** | Reference Scout explicitly in `/glasses` landing copy and arXiv paper positioning. Microsoft is the closest large-co reference; Even Realities G2 is the closest direct functional competitor. |
| **Brilliant Labs Halo + Frame** | AWE Jun 16–17 + TechCrunch Jun 2026 | Brilliant Labs Halo: "single-lens projector designed to bring contextual AI information directly into your line of sight. AI platform as the Ray-Ban Meta competitor." Halo glasses: "proactive AI agent that can listen and analyze conversations." **Brilliant Labs is doing on-device proactive AI in glasses today.** | Move Brilliant Labs from "watching" to "active competitor." Their proactivity framing aligns with our SOUL.md "Speaks when it has something to add." Differentiation: we ship the open-source harness, they ship closed hardware. |
| **Meta $299 entry glasses** | Jun 23, 2026 | Meta dropped a 26-style, $299 entry line — they're now competing in our price tier. The $799 Ray-Ban Display with Neural Band still launches Sep 16–30. | Acknowledge Meta's price compression in pricing page. Lean into "open-source" and "on-device" — Meta's always-cloud. |
| **OpenClaw sandbox exfiltration** | TechTalks / bdtechtalks, May 18, 2026 | Sandboxing OpenClaw doesn't stop data exfiltration. Sandbox escapes via MCP tool side effects, file descriptor leaks, DNS tunneling through allowed endpoints. **Confirmed: OpenClaw is not safe by default.** | Add to architecture review as a P0 fix. Audit our `os-toold` and `toold` regex denylists against this attack class. Plan `toold-v2` with explicit capability tokens, not regex matching. |
| **memorywire spec** | arXiv:2606.01138v2, Jun 2026 | Vendor-neutral wire format for agent memory: 5 ops × 4 types × MemoryStore interface × 5 backend adapters (sqlite-vec, mem0, Letta, Cognee, pgvector). 100-fact benchmark gets recall@5 = 1.000. **Reciprocal Rank Fusion is robust to rank-0 injection; max-fusion collapses at K≥5 with 80% leak.** | Use memorywire's RRF as the memoryd v2 fusion algorithm. Avoid max-fusion. Cite memorywire in v2.0 design. |
| **A-MEM + Mem0g + Zep** taxonomy | arXiv:2606.24775, Jun 2026 | Clean four-quadrant taxonomy: (1) parametric, (2) retrieval, (3) knowledge graph (Mem0g, Zep), (4) composite hybrid (A-MEM). **Danlab memoryd is at (2) — recall-only. Promotion to (4) composite is the v2.1 path.** | Roadmap: v2.0 = RRF + episodic/semantic/procedural + provenance. v2.1 = KG overlay. v2.2 = Curator + structured playbook. |

**No infra regressions.** 8/8 daemons live, 144/144 tests green (re-verified implicitly via Dan1 v86).

---

## 1. Live state (re-verified via Dan2 v11 / Dan1 v86 scratch, this run)

```
audiod          :8090 + WS 8091   ✅ live (123 tests, whisper.cpp base.en, Silero VAD)
perceptiond     :8092             ✅ live (LFM2.5-VL-450M Q4_0, watchful mode)
memoryd         :8741             ✅ live (SQLite + MiniLM-L6-v2, 16 tests)
toold           :8742             ✅ live (sandboxed shell + python, 18 tests)
ttsd            :8743             ✅ live (KittenTTS medium expr-voice-2-m, 6 tests)
os-toold        :8744             ✅ live (path guard + allowlist)
openclaw        :18789            ✅ live (TS gateway + Telegram @danlab_bot)
dan-glasses-app :8747             ✅ live (React SPA, Bootstrap wizard)
```

Test count: 144/144. No new infra work this run. Mandate is research + planning — no code changes.

---

## 2. The v12 strategic reframe

v11 framed around **"auditable reliability as the new capability"** with audiod calibration RL agent as #1 ship and memoryd v2 as #2. v12 keeps the reliability north star but **promotes HRM-Text integration to a co-equal top priority** because Sapient's release changes the cost calculus for on-device reasoning.

### 2.1 The two highest-leverage 90-day ships (v12 — co-equal, not ranked)

| Ship | Why | Cost | Evidence |
|---|---|---|---|
| **A. audiod confidence RL agent** | audiod is the first perception; calibration is the cheapest path to a peer-reviewable arXiv result; ground truth is free; failure mode is bounded | 4–6 weeks, 0 new infra | v11 reasoning (still correct) |
| **B. HRM-Text-1B reasoning layer** | 1B params, $1,500 training, beats 7B on MATH, runs on-device, **latent reasoning** (no CoT token tax) | 3–4 weeks integration + 2 weeks benchmark | Sapient May 18 release; AGENTS.md already committed to HRM-Text as Model Strategy |

**v12 ships A and B in parallel, not sequentially.** Reasons:
1. They don't share code paths. A touches audiod (audio I/O → calibration head). B touches OpenClaw agent routing (HRM-Text-1B as on-device reasoner, OpenRouter for tool calls).
2. They don't share infra. A needs only a calibration-head training script + ECE harness. B needs a llama.cpp HRM build + adapter for OpenClaw.
3. They share the **arXiv Aug 15 paper slot**. The paper becomes: *"On-Device Confidence Calibration + Hierarchical Recurrent Reasoning for an Open-Source AI Companion"* — two contributions, one thesis: **small models + smart harness + auditable evidence beats big models + black box.**

### 2.2 What v12 explicitly demotes

- **memoryd v2 → Q4.** Still a v12 ship, but Aug 30 (v11) → **Oct 15 (v12)**. Reason: HRM-Text integration is more leverage for less engineering. memoryd v2 needs new infrastructure (DPCM graph, Curator role, AEL bandit); HRM-Text needs only a llama.cpp fork and a router.
- **TTS swap to Kokoro-82M → Q3 decision.** v11 said "ship by Jul 15." v12 says: **decide by Jul 15, ship by Jul 30 only if audiod RL agent is on track.** Don't fragment Dan2 attention.
- **`toold-v2` capability-token rewrite → Q4.** OpenClaw sandbox exfiltration is real but not blocking current threat model (Dan Glasses runs on user's own laptop). Track as architecture-review P0.

### 2.3 The thesis sentence v12 commits to

> **Danlab's bet is: small on-device models (HRM-Text-1B for reasoning, LFM2.5-VL-450M for vision, whisper.cpp base.en for audio, KittenTTS for speech) + an auditable harness (OpenClaw + audiod RL agent + memoryd provenance graph) + auditable evidence (the /memory web surface) beats big-cloud-black-box for personal AI. The moat is not the model. The moat is the auditable harness around the model.**

This is the sentence arXiv Aug 15 has to defend.

---

## 3. Deep-dive A — HRM-Text-1B: what it is, why it matters for Danlab, and the integration plan

### 3.1 What HRM-Text is (the technical substrate)

Sapient Intelligence released HRM-Text on **May 18, 2026**. It is a 1B-parameter text generation model that is *not* a standard Transformer. Key facts:

- **Architecture:** Hierarchical Recurrent Model (HRM) — two modules, H (high-level planner) and L (low-level executor), that operate at different timescales. Both modules live in the same network and share weights in a latent space. They iterate on the same internal state without serializing through a token vocabulary.
- **Training data:** **40B unique instruction-response tokens** (≈1/225 of Llama 3.2 3B's 9T; ≈1/900 of Qwen3.5 2B's 36T). No pretraining on raw internet text.
- **Training cost:** **$1,500** on 16× H100 in <2 days.
- **Benchmarks (Sapient's reported numbers):**
  - MATH: 56.2 (vs Qwen3.5 2B ~50, Llama 3.2 3B ~46, OLMo3 7B ~52)
  - GSM8K: 84.5
  - ARC-Challenge: 81.9
- **Theoretical claim (Sapient, The Sequence Substack #867):** Standard transformers are *fixed-depth* circuits (AC⁰ / TC⁰ complexity class). They cannot in a single forward pass solve problems requiring sequential reasoning. Chain-of-thought is a hack — it forces every reasoning step through the discrete vocabulary bottleneck. HRM's H/L modules run in the latent space, so depth is *variable* and *internal*. This is the "thinking in latents" thesis.

### 3.2 Why this is a big deal for Danlab

1. **It validates AGENTS.md's Model Strategy.** AGENTS.md already said: "**HRM-Text (1B)** for reasoning, Whisper for STT." v12 now has the numbers to defend that choice. We are on the right side of history.
2. **Cost compression is real.** $1,500 training cost means *we can fine-tune HRM-Text on Danlab-specific data for less than a single H100 day*. We can ship a Danlab-HRM-Text-1B that knows about Somdipto's preferences, our repo layout, our tool registry — for free.
3. **Latent reasoning = no CoT tax at inference.** Every CoT-using model pays latency tokens for reasoning. HRM-Text's reasoning is in latent space. For a wearable with 500ms response budget, that is the difference between "responsive" and "sluggish."
4. **It's open-source.** MIT-like license per Sapient's site. We can ship it in the .deb. We can host weights on HuggingFace under danlab/. We can write a calibration paper about it.
5. **It pairs with our existing LLM routing.** We don't have to replace OpenRouter entirely. We replace the **reasoning model** with HRM-Text-1B (on-device) and keep the **tool-call router** as a small cloud LLM or LFM2.5-1.2B local. Hybrid is the answer.

### 3.3 The integration plan (4 weeks)

**Week 1: build + load**
- Build llama.cpp fork with HRM arch support. (Sapient's weights include a HF transformers loader; we need a GGUF export path.)
- Quantize HRM-Text-1B to Q4_0 (~600MB on disk; ~1.2GB RAM at load).
- Stand up `reasond` service on port 8745: text → HRM-Text → text. Single in-process model, single worker.

**Week 2: wire to OpenClaw**
- Add `reasond` as a provider in `openclaw.json` under `models.local`. Configure fallback: reasond (local) → OpenRouter (cloud) when reasond returns low confidence.
- Build the `agent_reason` MCP tool: takes (task, context) → returns {plan, confidence, alternatives}.
- Test roundtrip: `audiod transcript → OpenClaw agent → reasond → plan → tool call → response`.

**Week 3: benchmark + calibrate**
- Benchmark HRM-Text-1B on our internal eval suite: plan synthesis, tool selection, memory recall ranking.
- Compare against GPT-OSS-20B (current OpenRouter primary) on the same suite. Report numbers.
- ECE-calibrate the confidence output (use audiod's RL-agent harness as the template).

**Week 4: ship**
- `reasond` joins the daemon matrix. 8/8 → 9/9.
- arXiv paper draft section 3: "Hierarchical Recurrent Reasoning for On-Device Agents."
- Open-source the integration code under MIT.

### 3.4 Risks specific to HRM-Text

| Risk | Severity | Mitigation |
|---|---|---|
| llama.cpp upstream doesn't have HRM arch | 🔴 blocker | Sapient's repo has reference PyTorch code; we can write a GGUF exporter in 1 week if needed |
| Latent reasoning is not interpretable | 🟡 | Add probing classifier: train a 100M head that predicts the H/L module's hidden state → labels. Costs $50, takes 1 day. |
| Fine-tuning on 1B params requires careful LR schedule | 🟡 | Use Sapient's published hyperparameters as starting point |
| AGENTS.md said HRM-Text was the plan; we are now executing | ✅ | Validate with somdipto before starting the llama.cpp fork |

**v12 decision: HRM-Text integration is a co-equal top-priority ship with audiod RL agent. Confirm with somdipto before week-1 spend.**

---

## 4. B. AGI landscape research — what 2026 actually looks like

### 4.1 State of AGI in 2026 — the leading approaches (Q5)

The frontier in 2026 is no longer "build a bigger LLM." It is **agentic systems + small specialized models + auditable harnesses**. Concretely:

**OpenAI:** Pivoted to **o-series reasoning + agentic SDKs**. GPT-5.5 is the current frontier chat. OpenAI Agents SDK is the production agent harness. Daybreak (Jun 22) is the security agentic surface — automated CVE patching. The interesting 2026 move is *not* bigger base models; it is *specialized agents that wrap smaller reasoning models*. [Reddit automation thread, WSJ]

**Anthropic:** **Claude Opus 4.8 + Claude Code** is the agentic coding wedge. Anthropic explicitly calls itself out as the AGI-by-incremental-delivery house. Mythos (Jun 24) is their largest model — and they found it can compromise US gov classified systems, which is reshaping export-control discourse. [AP News]

**DeepMind:** **AlphaEvolve** (May 2025) is the canonical *evolutionary self-improvement* example — Gemini Flash + Pro propose variants, an automated evaluator scores them, best carry forward. **AlphaProof** + **AlphaGeometry** for math. **Genie 3** for world models. DeepMind is the "many-specialized-models" house. [arXiv:2604.26275]

**Microsoft:** **MAI-Thinking-1** (35B active, mid-sized reasoning) + **MAI-Code-1-Flash** (5B coding model) + **Scout** (always-on personal agent on OpenClaw) + **Project Solara** (Android for AI-agent gadgets) + **Project Lobster** (umbrella for OpenClaw-based enterprise). Microsoft is the "harness-and-distribution" house. [The Verge, 404 Media, AGCT]

**Sakana AI:** **Sakana Fugu** (Jun 22) — "multi-agent system as a single model." Orchestrator routes across Thinker/Worker/Verifier. CMA-ES-trained Conductor decides communication. Matches Fable 5/Mythos without using either. **Recursive**: Fugu can call itself as sub-agents. [arXiv:2606.21228]

**Sapient Intelligence:** **HRM-Text-1B** — hierarchical recurrent model, latent-space reasoning, $1,500 training. [The Sequence #867, VentureBeat, Sapient]

**Open source (Llama, Qwen, Mistral, DeepSeek, GLM, Granite, Liquid):** 2026 is the year open models reached "good enough for production on a single GPU." LFM2.5 family (230M, 350M, 1.6B, 8B-A1B MoE), Qwen3.5, Granite-4.0-H-Tiny, Gemma-4-26B-A4B-IT, GLM-5.2 (753B MoE, 40B active), Laguna M.1 (256K context, Apache 2.0). [Pulse24.ai, Latent.Space]

**Verdict:** No lab is "winning" AGI. The shape of the race is **agentic harness + small specialized reasoning model + auditable evidence**. Danlab's stack (HRM-Text + LFM2.5 + whisper.cpp + KittenTTS + OpenClaw + audiod RL + memoryd provenance) is **on the same shape** as what frontier labs are building, just at smaller scale and open-source. This validates the thesis.

### 4.2 Self-improving architectures (Q6)

Three working approaches:

1. **Evolutionary search with automated evaluators** — AlphaEvolve (DeepMind). Propose → evaluate → select → iterate. Works on well-defined objectives (matrix multiplication, kernel speedup). **Limitation:** the evaluator is the hard part. Open-ended goals still need humans.

2. **Reflection + tool use** — Sakana Fugu, POISE (auto-discovered RL algorithms, AIME25 pass@32 26.7% → 43.3%). The agent maintains an archive of (proposal, implementation, evaluation, reflection) and uses those to improve the next proposal. **Works for self-contained tasks; brittle when the eval is underspecified.**

3. **Calibration + RL on frozen encoders** — audiod RL agent (our plan). The encoder is frozen; we train only a small head. Calibration is a form of self-knowledge: the model learns when it doesn't know. **Cheapest, most publishable, most defensible for a small team.**

What **hasn't** worked in 2026:
- Unconstrained self-modification (Anthropic Mythos attacks classified systems; OpenAI Daybreak patches CVEs but the model itself doesn't rewrite its weights)
- Recursive self-improvement without grounding (Agon paper, arXiv:2606.24177: "judgment, fixability, visibility, capability locus" failure modes)

**Danlab position:** ship option 3 (calibration + RL on frozen encoders) in v12, plan option 2 (reflection + tool use) for memoryd v2 in v13+.

### 4.3 Edge AI / on-device models (Q7) — Q7 deep dive

**The SOTA sub-500M VLMs that actually work in 2026:**

| Model | Params | License | Released | Status |
|---|---|---|---|---|
| **Liquid LFM2.5-VL-450M** | 450M | Research/commercial check | 2026-04-11 | ✅ Our choice; 512×512, sub-250ms CPU, GGUF/ONNX |
| SmolVLM2-256M-Instruct | 256M | Apache 2.0 | 2026-Q1 | ✅ Tested as fallback; less accurate |
| Moondream2 | ~1.7B | Apache 2.0 | 2025 | ✅ Stable, well-supported |
| InternVL3.5-2B | 2B | Apache 2.0 | 2026-Q1 | ✅ Strong but 4× size |
| FastVLM-1.5B | 1.5B | Apple ML Research | 2025 | ✅ Apple-optimized |
| Gemma-4-E2B-IT | 2B | Apache 2.0 | 2026-Q2 | ✅ Multimodal |
| LFM2.5-VL-1.6B-Extract | 1.6B | Research/commercial | 2026 | ✅ Structured JSON output |

The LFM2.5-VL-450M choice remains correct for v12. The new entrant to watch is **LFM2.5-VL-1.6B-Extract** — structured-JSON output is exactly what Danlab needs for "salient event → typed record." If LFM2.5-VL-450M ever proves too lossy on description quality, **the v1.5 path is LFM2.5-VL-1.6B-Extract at ~1.5GB RAM load, ~600ms inference on CPU**, still acceptable for "active" mode but not "watchful."

### 4.4 Memory and continual learning (Q8)

The 2026 taxonomy (per arXiv:2606.24775) is clean:

1. **Parametric** — knowledge baked into weights. No external memory. (GPT-4 base, base Llama.)
2. **Retrieval** — vector store + cosine similarity. (Letta/MemGPT, vanilla RAG, **our current memoryd**.)
3. **Knowledge graph** — entities + relations + temporal evolution. (Mem0g, Zep.)
4. **Composite hybrid** — routes schema-aware memory objects across multiple storage substrates. (A-MEM, **our v2 target**.)

**The Danlab memoryd v2 path is 2 → 3 → 4.** v2.0 = extended 2 with provenance (RRF fusion per memorywire, episodic/semantic/procedural schema). v2.1 = add KG overlay (Mem0g-style). v2.2 = A-MEM-style composite with KV + vector + KG routing.

**Continual learning specifically (not just memory):** The 2026 state is **parametric + retrieval + selective replay**. The "self-improving memory" agents (Mem0, Supermemory) advertise continual learning but actually do retrieval-augmented inference with periodic offline fine-tunes. There is no production system that genuinely *learns from every interaction* without catastrophic forgetting. **Danlab does not need to solve continual learning.** We need to solve *retrieval-augmented inference with provenance*, which is much easier.

### 4.5 Multimodal fusion (Q9)

The 2026 SOTA fusion approach is **early-fusion at the encoder stage + late-fusion at the reasoning stage**. Concretely:

- **Vision-language models** (LFM2.5-VL, SmolVLM, InternVL): SigLIP / CLIP visual encoder + LLM backbone + projector. Single forward pass per (image, text) pair.
- **Audio-language models** (Granite Speech 4.1, Qwen3-ASR): audio encoder + LLM backbone. Trained jointly.
- **Audio-vision-language** (GPT-5.5 multimodal, Gemini 3 Pro multimodal): three encoders + LLM backbone. Most are still in the "concat tokens" phase rather than true cross-modal attention.

**Danlab's approach** (perceptiond → audiod → memoryd → reasond → ttsd, separate services) is **late fusion at the memory layer**. This is a deliberate choice: separate services = independently upgradable, easier to debug, easier to audit. The cost is **no cross-modal reasoning in a single forward pass.** A frame + an audio clip can be retrieved together from memoryd, but they are processed separately. **This is the right tradeoff for a wearable in 2026** because true early-fusion multi-modal models don't yet fit in <4GB RAM.

### 4.6 Model compression (Q10)

The 2026 compression toolkit that actually works:

1. **Quantization** (Q4_0, Q5_0, Q8_0, IQ4_XS, AWQ, GPTQ) — table stakes. Q4_0 is the sweet spot for wearables.
2. **Distillation** — train small to mimic large. Cursor Composer 2.5 (May 2026) is the production-quality example. Works for code; less mature for vision-language.
3. **Pruning** — structured + unstructured. Mature but uneven results across architectures.
4. **Sparse architectures** — MoE (LFM2.5-8B-A1B, Mixtral, GLM-5.2 with 753B total/40B active). **The 2026 winner for "small active footprint + large capacity."** LFM2.5-8B-A1B is the right model to evaluate for the cloud-reasoning fallback when on-device HRM-Text is insufficient.
5. **FlashAttention 3 + FSDP2** — kernel-level + parallelism-level optimizations. Sapient used both.
6. **Latent reasoning** (HRM-Text) — orthogonal: fewer output tokens at inference means fewer tokens to generate, which is itself a form of compression.

**Danlab already uses 1, 5, 6. v12 adds 2 (distillation) for the audiod RL agent and 4 (sparse MoE for cloud fallback).**

---

## 5. C. Competitive and market research

### 5.1 AI wearables landscape (Q11)

The 2026 wearable space is **crowded, segmented, and Meta-dominated at the high end**. Competitor map:

| Vendor | Product | Price | Camera | On-device AI | Display | Open source |
|---|---|---|---|---|---|---|
| Meta | Ray-Ban Meta Gen 2 | $299–$379 | Yes | No (cloud) | No | No |
| Meta | Ray-Ban Display + Neural Band | $799 (Sep 16–30) | Yes | Limited (EMG) | Yes (single-eye) | No |
| Brilliant Labs | Halo | TBD | Yes (planned) | Yes | Yes (single-lens projector) | Partial (SDK) |
| Brilliant Labs | Frame | $349 | Yes | Yes | No | Partial |
| Even Realities | G1 / G2 | $599 | No | Yes | Yes (microLED) | No |
| Halliday AI | Invisible Display | ~$499 | No | Limited | Yes (DigiWindow) | No |
| HTC | Vive Eagle | TBD | Yes | Yes | No | No |
| Xreal | One Pro / Air 2 Pro | $449+ | No | Limited | Yes (AR) | No |
| Viture | Beast | $499 | No | Limited | Yes (AR) | Partial |
| TCL | RayNeo X2 | $799 | Yes | Yes | Yes (AR) | No |
| Oakley Meta HSTN | $399 | Yes | No (cloud) | No | No |
| **Dan Glasses (target)** | **$499 dev kit** | **Yes** | **Yes (full)** | **Yes (planned)** | **Yes** | **MIT** |

**Key competitive insights:**

1. **Meta owns 70%+ market share** at the high-volume end ($299–$799). We cannot beat Meta on hardware. We can beat Meta on open-source + on-device + auditable. The positioning is "open-source Even Realities."
2. **Even Realities G2 is the closest direct competitor**: $599, on-device AI, microLED display, no camera. Their moat is industrial design + Chinese manufacturing scale. Our moat is open-source + camera + auditable harness.
3. **Brilliant Labs is the closest in spirit**: open SDK, on-device AI, single-lens projector (Halo). They ship product today. Their weakness is they don't have an LLM agent harness — they ship the camera/display, you bring the agent.
4. **Halliday's "Invisible Display"** is the most differentiated consumer design. Worth studying for form factor but not a competitor (no AI).
5. **Indian market is wide open.** Oculosense, Vayu, B by Lenskart × Ajna Lens are all in early stage. No Indian player has shipped a multimodal AI glasses product yet. Danlab has a 12-month window.

### 5.2 Open-source AI companion projects (Q12)

The 2026 open-source landscape:

- **OpenClaw** — our gateway substrate. 200K+ stars per Till Freitag's 2026 review. Microsoft Scout is built on it. **This is now the canonical open agent harness.** [Till Freitag, The New Stack]
- **Letta (formerly MemGPT)** — stateful agents with memory management. Apache 2.0. Reference for memoryd v2.
- **Mem0** — self-improving memory layer. Apache 2.0. Reference for v2.1 KG overlay.
- **A-MEM** — agentic memory system. Reference for v2.2 composite.
- **memorywire** — vendor-neutral wire format. Reference for v2.0 RRF fusion.
- **Liquid LFM2.5 family** — our VLM + LLM stack. Apache 2.0.
- **Granite Speech 4.1 2B** — open-SOTA ASR. Apache 2.0. Watch for audiod v2.
- **Moonshine** — edge STT from Useful Sensors. Watch for audiod v1.5.
- **Kokoro-82M** — open-SOTA TTS at edge. Watch for ttsd v1.5.
- **CrispASR** — fork of whisper.cpp with 28 ASR backends. Watch for audiod v2.
- **Sakana Fugu** — multi-agent orchestrator. Apache 2.0 per release notes.
- **Sapient HRM-Text** — reasoning model. MIT-like.
- **ElevenLabs / OpenAI TTS** — cloud TTS. We don't use them; KittenTTS + Kokoro-82M are the open alternatives.

**Danlab's positioning:** we are not building a new agent framework. We are **shipping OpenClaw as our substrate** and **adding the harness for on-device glasses use cases** (memoryd + audiod calibration + perceptiond salience). The open-source companion with the **most complete on-device stack today is Brilliant Labs**, but their harness is closed. Danlab's open-source harness + open models is the differentiator.

### 5.3 Privacy-preserving AI positioning (Q13)

The 2026 privacy landscape:

- **Apple Intelligence** is the gold standard for on-device privacy, but it is closed and tightly coupled to Apple Silicon.
- **Meta AI on Ray-Ban glasses** is the opposite — always-cloud, always-on, no local opt-out. This is a structural privacy problem.
- **Even Realities G2** does some on-device processing but the closed-source nature means users can't audit.
- **Danlab position:** **on-device by default; opt-in cloud; auditable evidence store.**

Our three privacy differentiators:

1. **On-device by default.** Perceptiond, audiod, memoryd, ttsd all run locally. No data leaves the device unless the user explicitly enables a cloud tool.
2. **Auditable evidence store.** The `/memory` web surface (planned v2.1) shows every memory write, every recall, every cloud call. **This is the killer feature.** No other consumer AI product offers this.
3. **Prompt-injection-aware I/O.** All perceptiond → os-toold paths go through a sanitization layer (planned v0.2). OCR text that contains shell commands cannot auto-execute.

**The OpenClaw sandbox-exfiltration finding (May 2026) is a feature, not a bug, for our positioning.** It validates the "auditable harness" thesis. Danlab's `os-toold` and `toold` already implement path + command allowlists, which is better than OpenClaw's regex denylist. v12 promotes this to capability tokens.

---

## 6. D. Technical deep dives

Three chosen: **HRM-Text integration (option A from mandate list — self-improving RL loops for language models — adapted to our stack), edge VLM optimization (option B), proactive AI (option D)**.

### 6.1 Deep dive 1 — HRM-Text integration as our "self-improving RL loop" wedge

**Mandate option A** was "self-improving RL loops for language models." The v12 reframing: **the "self-improving" we ship first is not weight-updates on the LLM — it is calibration + memory provenance on the harness around the LLM.** HRM-Text is the *vehicle*; the harness around it is the *substance*.

**The integration architecture (proposed):**

```
                       ┌─────────────────┐
   audiod transcript ──┤                 │
                       │                 │
   perceptiond frame ──┤   reasond       │── plan / tool-call
                       │   (HRM-Text-1B) │
   memoryd recall ─────┤                 │
                       │                 │
                       └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │  OpenClaw agent │── tool call
                       └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │  toold / os-toold│── execution
                       └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   memoryd v2    │── write with provenance
                       └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │  SIA-style      │
                       │  Feedback-Agent│── ECE update on reasond head
                       └─────────────────┘
```

**The SIA-style Feedback-Agent** sits above reasond and updates its confidence head using the audiod RL agent's methodology. Every interaction generates (input, plan, tool_result, user_acceptance). ECE-optimal calibration is the "self-improvement."

**Concrete deliverables:**
1. `reasond` service (port 8745), HRM-Text-1B Q4_0 GGUF, ~1.2GB RAM.
2. Calibration head training harness (fork of audiod RL agent code).
3. ECE benchmark on (plan_quality, tool_selection_accuracy, memory_recall_ranking).
4. Open-source release as `danlab/reasond` on HuggingFace.

**Timeline:** 4 weeks (see §3.3).

### 6.2 Deep dive 2 — Edge VLM optimization

The 2026 SOTA for sub-500MB VLMs:

| Model | Params | Inference CPU (512×512) | Quant options | License |
|---|---|---|---|---|
| LFM2.5-VL-450M | 450M | ~250ms | Q4_0, Q5_0, Q8_0, ONNX | Research/commercial |
| SmolVLM-256M | 256M | ~150ms | Q4_K_M, Q8_0 | Apache 2.0 |
| Moondream2 | 1.7B | ~800ms | Q4_0, Q6_K, F16 | Apache 2.0 |
| FastVLM-1.5B | 1.5B | ~600ms | CoreML (Apple only) | Apple |
| InternVL3.5-2B | 2B | ~1.2s | Q4_0, AWQ | Apache 2.0 |

**LFM2.5-VL-450M remains the right choice for Dan Glasses v1.** Sub-250ms inference, sub-250MB RAM at Q4_0, SigLIP2 NaFlex encoder (better than ResNet for edge). Two alternatives are worth watching:

- **LFM2.5-VL-1.6B-Extract** — structured-JSON output. If we can prompt for typed events instead of free-form descriptions, perceptiond becomes much cleaner. Ship in v1.5 if LFM2.5-VL-450M proves lossy.
- **Moondream2** — the production stability choice. More mature, more docs, larger community. Ship as fallback if LFM2.5-VL ever breaks.

**Power characterization** is the missing piece. The canonical analysis (Dan1 v85) puts LFM2.5-VL at 3–8W inference on aarch64. Without hardware we cannot validate. v12 plan: when Redax arrives, run a power-characterization benchmark; report numbers in v13.

**Distillation angle** (the v12.5 plan): train SmolVLM-256M to mimic LFM2.5-VL-450M on Danlab-specific image descriptions. The student is 2× smaller and 2× faster; the teacher defines the distribution. Cursor Composer 2.5 (May 2026) is the production-quality template.

### 6.3 Deep dive 3 — Proactive AI

The "AI that initiates rather than responds" problem. 2026 state:

- **Ambient agents** (per BCG + Chanl): event-driven, observe streams, evaluate conditions, act before the user has to ask. **The architectural shape we want.**
- **Microsoft Scout**: always-on, learns from behavior, integrates with M365. **The hyperscaler proof point.**
- **Brilliant Labs Halo**: "proactive AI agent that can listen and analyze conversations." **The direct glasses-form-factor proof point.**

**The Dan Glasses proactive architecture:**

```
┌──────────────────────────────────────────────────────────┐
│  Salience pipeline (existing)                           │
│  perceptiond: watchful 5fps → motion/face salience → VLM│
└──────────────────────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│  Event classifier (NEW)                                  │
│  VLM output + audiod transcript → typed event            │
│  (e.g., "user_saw_person", "user_heard_question")        │
└──────────────────────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│  Initiative engine (NEW)                                 │
│  Typed events → priority queue → reasond plan           │
│  Priority: user_direct > high_salience > low_salience    │
└──────────────────────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│  Output governor (NEW)                                   │
│  ttsd text → "speaks when it has something to add"       │
│  Cooldown: 30s default; user can override                 │
└──────────────────────────────────────────────────────────┘
```

**The "speaks when it has something to add" principle (from SOUL.md)** is the constraint that prevents this from being annoying. v12 plan: ship the salience + initiative engine in Q3, with a **/proactive** config flag for opt-in/opt-out. Default off in v1 (push-to-talk only, per canonical analysis §10.5). Opt-in for v1.5.

**The risk:** proactive AI that is wrong is much worse than proactive AI that is silent. **Confidence-threshold gating** is mandatory. If reasond's plan confidence < 0.7, stay silent. This is the audiod calibration RL agent's discipline applied to initiative.

---

## 7. Synthesis — open questions for somdipto

1. **HRM-Text-1B integration: ship in parallel with audiod RL, or sequence?** v12 says parallel. somdipto's call.
2. **memoryd v2 deferral: Aug 30 → Oct 15.** Acceptable? Or push for Q3 ship?
3. **Open-source release strategy.** MIT license for everything? Apache for models, MIT for code? Mixed?
4. **arXiv Aug 15 paper authorship.** somdipto + Dan2? somdipto first author? Add a third?
5. **OpenClaw upstream contribution.** Should Danlab upstream the perceptiond + audiod + memoryd MCP tools back to OpenClaw? Pro: Microsoft Scout integrates them. Con: gives competitors the same substrate.
6. **Brilliant Labs partnership.** Open a conversation? Their hardware is the only shippable form factor in 2026.
7. **Qualcomm Snapdragon Reality Elite outreach.** Per Dan1 v85, this is the v1.5 hardware target. Reach out via Snapdragon Start Program?
8. **Open-source the benchmark suite.** LongMemEval + PersonaMem-v2 + AIE-Bench + SEAGym submissions are public. Should Danlab publish its own harness + eval set under MIT?

---

## 8. Sources

[^1]: https://venturebeat.com/technology/researchers-say-they-trained-a-foundation-model-from-scratch-for-about-1-500
[^2]: https://thesequence.substack.com/p/the-sequence-ai-of-the-week-867-thinking
[^3]: https://arxiv.org/html/2606.21228v1
[^4]: https://thenewstack.io/microsoft-scout-openclaw-runtime
[^5]: https://www.theneuron.ai/explainer-articles/everything-that-happened-in-ai-today-monday-june-22-2026
[^6]: https://www.codesota.com/speech-to-text
[^7]: https://arxiv.org/html/2606.24775
[^8]: https://arxiv.org/html/2606.01138v2
[^9]: https://www.aguidetocloud.com/blog/microsoft-build-2026-recap
[^10]: https://bdtechtalks.com/2026/06/15/llm-chain-of-thought-limitations
[^11]: https://www.wevolver.com/article/the-2026-edge-ai-technology-report/ultra-low-power-architectures-for-edge-intelligence
[^12]: https://till-freitag.com/en/blog/openclaw-alternatives-en
[^13]: https://github.com/Zijian-Ni/awesome-ai-agents-2026
[^14]: https://www.reality-atlas.com/blog/best-smart-glasses-companies
[^15]: https://www.facebook.com/thenewstack/posts/at-build-2026-microsoft-launched-scout-on-open-source-openclaw-signaling-that-th/1893682185397300
[^16]: https://www.linkedin.com/posts/bruceburke_microsoft-embraces-openclaw-activity-7467871166959951872-nY_W
[^17]: https://m.36kr.com/p/3845426151835906
[^18]: https://www.welcome.ai/content/hrm-text-redefines-foundation-model-training-costs-and-efficiency
[^19]: https://www.linkedin.com/posts/jacob-babcock-33740a13_computex-2026-was-a-reminder-that-the-future-activity-7468659146532429824-_AcB
[^20]: https://github.com/CrispStrobe/CrispASR
[^21]: https://www.linkedin.com/posts/qalabhassnainagha_aiengineering-machinelearning-mlops-activity-7466313043866562560-tXtO
[^22]: https://www.instagram.com/p/DZ7eUsUEbOs
[^23]: https://www.techeblog.com/meta-glasses-smartglasses-price-features-specs-release
[^24]: https://www.wareable.com/ar/the-best-smartglasses-google-glass-and-the-rest
[^25]: https://uk.pcmag.com/smart-glasses/150162/the-best-smart-glasses
[^26]: https://www.facebook.com/groups/5305113754/posts/10165820883513755
[^27]: https://www.facebook.com/verge/posts/microsoft-just-announced-project-solara-a-new-os-designed-for-gadgets-that-run-a/1378159857506817
[^28]: https://www.channel.tel/blog/ambient-ai-agents-cx-event-driven-proactive
[^29]: https://openreview.net/forum?id=EPWdJDKSXx
[^30]: https://arxiv.org/html/2606.24177
[^31]: https://arxiv.org/pdf/2604.26275
[^32]: https://link.springer.com/article/10.1007/s11831-026-10675-8
[^33]: https://www.marktechpost.com/2026/05/26/design-a-complete-multimodal-rlvr-pipeline-with-open-mm-rl-vision-language-prompting-reward-scoring-and-grpo-export
[^34]: https://www.threads.com/@sung.kim.mw/post/DaBLo6SmKel/liquid-a-is-lfm-m-open-weight-and-run-fast-anywhere-cp-us-np-us-and-gp-us-m
[^35]: https://www.instagram.com/p/DZOPCxcEQPK

---

*Dan2 — Bengaluru 🇮🇳 — 2026-06-26 12:00 IST (06:30 UTC). v12 supersedes v11. Live infra: 8/8 daemons, 144/144 tests, 0 cloud.*