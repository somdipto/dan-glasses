# Dan2 Research Report — Danlab AGI Research
**Date:** 2026-05-28  
**Author:** Dan2 (Danlab Co-Founder & Architect)  
**Status:** Complete

---

## A. System Architecture Deep Dive

### 1. Current Dan Glasses Architecture — Service Decomposition

The Dan Glasses architecture decomposes the AI wearable into 5 isolated Rust/Python services communicating via Unix sockets and HTTP TCP ports:

| Service | Language | Role | Port |
|---------|----------|------|------|
| `perceptiond` | Python | Camera → salience → VLM inference | 8092 |
| `audiod` | Python | Mic → VAD → whisper.cpp → transcript | 8090 |
| `memoryd` | Python | SQLite + vector embeddings (384d via all-MiniLM-L6-v2) | 8741 |
| `toold` | Python | Shell/python exec with guardrails | 8742 |
| `ttsd` | Python | KittenTTS → WAV | 8743 |
| `openclaw-gateway` | TypeScript/Node | Orchestration, agent runtime, Telegram channel | 18789 |
| Tauri app | Rust + React | Frontend shell + lib.rs IPC commands | — |

**Assessment:**

The decomposition is architecturally sound for a prototype. Services are logically separated by concern (perception, audio, memory, tools, output). The OpenClaw TypeScript gateway as orchestration layer is a pragmatic choice given OpenClaw's ecosystem maturity.

**However, there are structural issues:**

1. **All services are Python (not Rust).** The canonical spec says "Rust binaries" but current implementations are Python. This is a significant gap between spec and reality. Python services are harder to harden for a wearable form factor — no compile-time memory safety, GIL contention, larger memory footprint.

2. **OpenClaw is the sole orchestration layer.** If the gateway crashes mid-session, session recovery depends on OpenClaw's built-in session store. There's no service-level watchdog that can restart the gateway autonomously.

3. **No inter-service IPC standard.** Services use ad-hoc HTTP endpoints and stdout JSON. There's no enforced contract schema across services — memoryd accepts arbitrary JSON, perceptiond publishes events as stdout, audiod broadcasts via WebSocket. Integration is brittle.

4. **Service health monitoring is polling-based.** The Tauri app polls `/health` endpoints on each service. For a power-constrained wearable, this is wasteful. A properly designed system would use signal-based notifications or a shared health indicator.

5. **openclaw-gateway runs as a single process.** No process isolation per agent. The Octopus pattern (parallel arms) exists in OpenClaw's roadmap but is not yet deployed.

**Bottleneck analysis:**

- **VLM inference** is the dominant bottleneck (~5s per frame in watchful mode with SmolVLM-256M, likely ~1-3s with LFM2.5-VL-450M after warmup). This is I/O bound on subprocess spawning.
- **audiod** runs whisper-cli as a subprocess per segment — no streaming pipeline. Latency is batch-oriented, not real-time.
- **memoryd** uses a flat in-process vector index (no approximate nearest neighbor acceleration). At 10K+ memories, this will degrade.
- **KittenTTS** synthesis time is unmeasured — could be a latency killer for the voice output requirement (<3s end-to-end).

### 2. Multimodal Pipeline — Is It a True RL Loop?

In `danlab-multimodal`, the "RL feedback loop" is **not genuine RL**. It is a heuristic scoring loop:

```
Screen capture → SmolVLM-256M inference → heuristic score (0-100) →
if score < threshold → suggest improvement → loop
```

The heuristic scores based on: response length (< 30 chars = penalty), presence of `[ERROR]`, and whether the response identifies UI elements (+bonus).

**What's missing for true RL:**

- No learned reward model — heuristic rewards are hand-crafted and brittle
- No policy gradient signal — the VLM is not being updated
- No environment interaction — the "loop" is just repeated inference on the same image
- No credit assignment beyond threshold gating — the scorer cannot attribute failure to specific reasoning steps

**What would make it genuine RL:**

A true RL loop requires:
1. A **reward model** (learned, not heuristic) that maps (image, response, outcome) → scalar reward
2. **Policy gradient updates** — GRPO or PPO updates that actually change the VLM's weights
3. **An environment** with state transitions — current "loop" has no state
4. **Exploration** — the model should generate diverse responses, not just retry the same prompt

The danlab-multimodal pipeline has the *structure* of an RL evaluation loop but lacks the *learning* mechanism. This is a common early-stage interpretation error — many "RL" demos in hackathon projects are heuristic loops that happen to iterate.

**Path to genuine RL for Danlab:**
1. Replace heuristic scorer with a learned reward model (train a small reward model on human preference data)
2. Integrate with GRPO/RLVR (Reinforcement Learning with Verifiable Rewards) — applicable if the task has verifiable outcomes
3. Build an actual environment: screen state → action →reward. This requires a formal MDP definition.
4. Consider the SEAL framework (Self-Adapting LLMs) or R-Zero for self-evolving reasoning without external rewards

### 3. Power/Performance Tradeoffs — LFM2.5-VL-450M, whisper.cpp, KittenTTS

**LFM2.5-VL-450M (target vision):**
- Released April 11, 2026 by Liquid AI
- 450M params, sub-250ms inference on edge hardware (Jetson Orin verified)
- 512×512 input, 32K token context
- SigLIP2 NaFlex encoder (not vanilla ViT — better efficiency)
- GGUF available via llama.cpp (Q4_0 recommended for edge)
- Supports bounding box prediction, function calling (v2.5 improvement over v2)
- **Power draw is uncharacterized.** The sub-250ms figure is latency, not power. No official TDP or mJ-per-inference number exists. This is the #1 critical risk for the wearable form factor.

**whisper.cpp (current STT):**
- ggml-base.bin (74MB) — correct choice for edge
- No streaming — each VAD segment triggers a new whisper-cli subprocess invocation
- ~1-2s latency per segment at 16kHz audio
- Silero VAD for voice activity detection — good choice, industry standard
- **Issue:** Subprocess-per-segment adds ~200-400ms overhead per transcription. For a real-time voice interaction, this compounds with TTS synthesis time.

**KittenTTS (current TTS):**
- <25MB total (base variant) — excellent for edge deployment
- Quality is state-of-the-art for size class
- ONNX export available for cross-platform inference
- **No benchmarking data publicly available.** Synthesis latency vs. quality at base vs. mini variant needs measurement.

**The power budget problem (from canonical analysis):**

| Component | Idle | Watchful | Active |
|-----------|------|----------|--------|
| openclaw-gateway | 0.5W | 0.5W | 0.8W |
| memoryd (SQLite) | 0.2W | 0.2W | 0.3W |
| audiod (mic ready) | 0.3W | 0.3W | 0.5W |
| perceptiond (cam) | 0.5W | 0.8W | 2.5W |
| **LFM2.5-VL-450M** | 0W | 0W | **3-8W** |
| KittenTTS (spike) | 0W | 0W | 1-2W |
| **Estimated total** | **~1.6W** | **~1.9W** | **~8-13W** |

For 4-hour battery life at 5W average: ~2500mAh @ 3.7V. This is *very tight* for a wearable. The VLM is the dominant power event — throttling capture FPS (per the current spec) is the **wrong lever**. The actual lever is reducing VLM inference frequency.

**Key concern:** The adaptive FPS modes (2/5/10) control camera capture rate, not inference triggering. Even at 2 FPS idle, every frame would trigger VLM if the frame is salient. The spec needs inference-gating at the salience decision, not capture rate control.

### 4. OpenClaw Orchestration — TypeScript/Node Choice

**TypeScript/Node is defensible for the gateway but creates risk at the edge.**

**Arguments for:**
- OpenClaw has the most mature agent framework ecosystem (policies, MCP tools, session management, Octopus multi-agent)
- TypeScript-native tooling means fastest iteration on the agent logic
- NPM ecosystem provides integration points for Telegram, WhatsApp, web, etc.

**Arguments against (for wearable deployment):**
- Node.js is not a hard real-time runtime — GC pauses and event loop blocking can cause voice interaction latency spikes
- Memory footprint of Node.js (~50-100MB baseline) is significant vs. embedded constraints
- No compile-time safety — runtime errors can crash the gateway
- Service isolation is process-level, not memory-safe isolation

**Failure modes:**
1. Gateway crash → session loss → requires recovery from memoryd checkpoint
2. Memory leak from long-running agent sessions → unbounded memory growth
3. V8 GC pause → audio pipeline starves (whisper needs constant throughput)
4. Node.js module resolution on first run → cold-start latency spikes

**Mitigation needed:**
- Separate watchdog process (Rust) that monitors gateway health and auto-restarts
- Session state checkpointing to memoryd at regular intervals (every 30s)
- Node.js memory limit enforcement via `--max-old-space-size`
- Priority scheduling for audio latency-critical threads

---

## B. AGI Landscape Research

### 5. State of AGI Research in 2026

**Current state:**
- No system has demonstrably achieved human-level AGI on arbitrary tasks
- The field is consolidating around a few dominant approaches:
  - **Scaling transformers with RLHF/post-training** (OpenAI o1/o3/o4, Anthropic Claude 4, Google Gemini 3)
  - **Hybrid reasoning models** (test-time compute scaling, process reward models)
  - **Self-improving loops** (self-rewarding, GRPO, RL with verifiable rewards)
  - **Agentic architectures** (multi-step planning, tool use, memory-augmented reasoning)

**Key developments in 2025-2026:**
- **Agentic RL** is a new paradigm: LLMs as policies in MDPs, with meta-reasoning and self-reflection (arxiv:2604.27859)
- **RL with Verifiable Rewards (RLVR)** has become the dominant post-training approach for reasoning models
- **Self-rewarding / self-improving models** are actively researched (Self-Rewarding LM, SEAL, R-Zero)
- **Small reasoning models** (Phi-4-mini, Qwen3.5-0.8B, Gemma-3n-E2B) challenging the "bigger is better" assumption
- **Hybrid memory architectures** (Graph + Vector + Episodic) are the cutting edge for long-horizon agents
- **Context-window scaling has plateaued** — researchers are now optimizing what's retrieved from long context, not expanding context

**Expert consensus:**
- 2040-2059 median for human-level AGI (Expert Survey on Progress in AI)
- 76% of AAAI 2025 respondents believe scaling current transformers alone won't achieve AGI
- Top labs (OpenAI, Anthropic, DeepMind) all pursuing different approaches — no consensus architecture

### 6. Self-Improving Architectures — What Has Actually Worked

**What has worked:**
1. **GRPO (Group Relative Policy Optimization)** — OpenAI o1/o3's training approach. Uses verifiable rewards (math proofs, code execution) to bootstrap reasoning without external human feedback.
2. **RLVR (Reinforcement Learning with Verifiable Rewards)** — Anthropic/GPT's post-training for coding/math; the template for self-improvement in closed-form evaluation.
3. **Self-Rewarding Language Models** (Yao et al., arxiv:2401.10020) — Iterative DPO with LLM-as-Judge. The model generates its own preference data and iteratively improves.
4. **R-Zero** — Fully autonomous self-evolving reasoning from zero data, using Challenger/Solver co-evolution.
5. **SEAL (Self-Adapting LLMs)** — Model generates self-edits + finetuning directives, RL loop uses downstream performance as reward.

**What has NOT worked:**
- Self-improvement without external feedback on open-ended tasks (no verifiable ground truth = reward hacking)
- End-to-end differentiable self-improvement at scale > 1B params without massive compute
- Pure "model improves itself by thinking harder" without architectural innovations

**For Danlab:** R-Zero and SEAL are the most relevant frameworks since Dan Glasses is an always-on agent in an open-ended environment (daily life) with no verifiable ground truth. Danlab should focus on:
1. **Internal feedback / confidence-based rewards** (RLIF — Reinforcement Learning from Internal Feedback, using self-certainty as reward signal)
2. **Memory-grounded self-improvement** — leverage the memory system as a reward signal (did the memory system retrieve relevant info? Did the agent correctly recall past context?)
3. **Procedural memory** — learning to execute learned skills autonomously

### 7. Edge AI / On-Device VLMs — SOTA for Sub-500MB

**The current landscape of sub-500MB VLMs:**

| Model | Size | Benchmark | Edge Runtime | Notes |
|-------|------|-----------|--------------|-------|
| **LFM2.5-VL-450M** | ~450MB Q4 | SOTA at 450M | llama.cpp, <250ms | **Danlab's choice** |
| SmolVLM2-500M | ~500MB | Moderate | llama.cpp | LFM2.5 is better |
| nanoVLM-230M-8k (ExecuTorch) | ~515MB int8 | Low | ExecuTorch | Exceeds 500MB but quantized |
| Qwen3-VL | 7B+ | High | Needs GPU | Too large |
| Gemma-3-2B | 2B | High | llama.cpp | No vision, not in Danlab scope (yet) |

**Key research findings (2025-2026):**
- **SPEED-Q framework** — staged sensitivity-adaptive quantization for VLMs, enabling 2-bit weight quantization with higher accuracy than prior methods (AAAI 2026)
- **LQA (Lightweight Quantized-Adaptive)** — modality-aware hybrid quantization + gradient-free test-time adaptation. 19.9× memory savings over FP16 on edge datasets.
- **QUOTA** — joint quantization + token pruning (W4A4), preserving KV cache consistency for low-bit inference
- **TensorRT Edge-LLM v0.7.0** — FP8, INT4 AWQ, NVFP4 quantization + ONNX export workflow for edge VLM deployment (Nvidia)
- **Embedl Cosmos Reason2** — W4A16 quantization + FlashHead for <8GB RAM multimodal inference. 3× faster thanprior work.

**For Danlab:** LFM2.5-VL-450M at Q4_0 is the right choice. But the uncharacterized power draw is a genuine blocker. Danlab needs actual power measurements on target hardware (Redax aarch64) before the wearable form factor is viable.

### 8. Memory and Continual Learning — Approaches for AI That Learn from Experience

**The core problem:** Standard LLMs are static after training. For an always-on companion, you need: episodic memory (what happened), semantic memory (facts learned), procedural memory (how to do things), and the ability to update continuously without forgetting.

**SOTA architectures (2026):**

| Architecture | Key Innovation | Benchmark | Relevance |
|---|---|---|---|
| **WorldDB** | Vector graph + ontology-aware write-time reconciliation | LongMemEval | Temporal consistency |
| **SAGE** | Self-evolving graph-memory with write/read/update feedback loop | LongMemEval | Self-improving memory |
| **MAGMA** | 4 orthogonal relational graphs (semantic, temporal, causal, entity) | LoCoMo + LongMemEval | Multi-relational traversal |
| **H-Mem** | Hybrid tree (temporal/semantic) + knowledge graph (entity) | 3 agent-memory QA | Fast retrieval + evolution |
| **All-Mem** | Topology-structured memory bank with non-destructive consolidation | LoCoMo + LongMemEval | Lifelong memory |
| **Synapse** | Brain-inspired spreading activation over episodic-semantic graph | — | Biologically plausible |
| **Aeon** | Neuro-symbolic memory OS with Atlas (INT8 quantized) + Semantic Lookaside Buffer | — | Production-grade |

**Danlab's current approach:** SQLite + 384d vectors via all-MiniLM-L6-v2, with episodic/semantic/procedural types. This is comparable to early Mem0 architecture (~2024). It is functional but will need upgrading to graph-based approaches for true long-horizon coherence.

**Most urgent upgrade path:** Add temporal metadata to all memory writes, implement a simple entity graph for relationships between memories (who is this person? what event involved them?), and add a retrieval feedback loop.

### 9. Multimodal Fusion — Best Systems

**How the best systems combine vision, audio, and text:**

The dominant architecture in 2026 is:
1. **SigLIP2 / EVA-CLIP vision encoder** → frozen image embeddings
2. **Linear/mmproj projector** → maps vision tokens to LLM embedding space
3. **LLM backbone** → autoregressive text generation

**For audio:** Whisper-family encoder encodes audio → text. Some systems use dedicated audio encoders (Canary, Qwen3-ASR).

**Emerging approaches:**
- **Unified multimodal tokens** — treating audio and video as a single token stream
- **Cross-modal attention at inference time** — late fusion rather than early projection
- **Embodied multimodal agents** — vision + audio + proprioception + environment state

**For Danlab:** The architecture is technically correct (vision encoder → projector → LLM → text). The bottleneck is not the fusion architecture but the quality/size of components and the power to run them continuously.

### 10. Model Compression — What Works

**Techniques that work in 2026:**

| Technique | Size Reduction | Quality Retention | Notes |
|---|---|---|---|
| **INT4/FP8 AWQ** (Activation-aware Weight Quantization) | 4-8× | 95-98% | Best for edge VLMs |
| **Token pruning + QUOTA** | 2-4× additional | ~90% with pruning | For VLM KV cache |
| **Knowledge distillation** | Variable | Task-dependent | DistilWhisper showed this works for STT |
| **Speculative decoding** | Latency reduction | Maintained | Use small draft model to predict LLM output |
| **Gradient-free test-time adaptation (LQA)** | Improved accuracy at low-bit | — | Adapts to distribution shift |
| **Dynamic quantization (torchao)** | ~5× for nanoVLM | ~90% | ExecuTorch deployment |

**Key insight:** Weight-only quantization (INT4/INT8) + ExecuTorch runtime is the current edge deployment consensus. Danlab's llama.cpp GGUF path is correct but may need switching to ExecuTorch if power/performance becomes critical.

---

## C. Competitive & Market Research

### 11. AI Wearables Landscape (2026)

| Player | Product | Positioning | AI Capabilities | Price |
|--------|---------|------------|-----------------|-------|
| **Meta** | Ray-Ban Stories 2+ | Capture + share, reactive | Audio + camera → cloud LLM | $299-800 |
| **Snap** | Spectacles 2026 | AR overlay display | Spatial AI + display | TBD |
| **Apple** | N50 (target 2027) | Display + AI | Full AR + Apple Intelligence | TBD |
| **Google** | Warby Parker partnership | AI + camera + Services | Gemini + Maps integration | TBD |
| **Samsung** | AR glasses | AI + display | Bixby + Tizen | TBD |
| **Xreal** | Air 2 Ultra | Display + spatial | AI overlay | $1,499 |
| **Viture** | One Pro | Gaming + display | No AI | $979 |

**Market data:**
- AI smart glasses market: $540M (2025) → $3.29B (2026) → $15B (2027 projected)
- 34.3% CAGR through 2034
- Meta dominates with 82% market share on AI glasses (7M units in 2025)
- North America: 44.65% market share

**Danlab's differentiation:**
- Proactive vs. reactive (Meta Ray-Ban captures and shares, Dan Glasses observes and contextualizes)
- Local/offline vs. cloud dependency
- Memory as a cognitive extension vs. searchable log
- AGI roadmap vs. feature parity product

**Key differentiator weakness:** Meta, Apple, and Google have 2-year head starts and massive hardware subsidies. Danlab cannot outspend on hardware. The only moat is the AGI research direction — self-improving, memory-augmented, privacy-first companion AI.

### 12. Open-Source AI Companion Projects

| Project | Approach | Strength | Weakness |
|--------|----------|----------|----------|
| **Panda (Blurr)** | Android accessibility agent, LLM-driven UI automation | Real-world Android control | Android-only, no memory persistence in v1 |
| **OpenChat** | Chat-only | Simple | No vision/audio |
| **LocalAI** | Self-hosted inference | Privacy | No agent architecture |
| **LibreChat** | Chat UI aggregator | Multi-model | Not a true companion |
| **Jan** | Local AI agent | Self-hosted, memory | Desktop only, no wearable context |
| **Dani (Danlab)** | Skills registry + persona management | Full-stack from India 🇮🇳 | Early stage |

**Panda (Blurr)** is the most directly competitive project. It's an Android AI agent that sees the screen, understands UI context, and executes tasks via accessibility service. Key differences from Dan Glasses:
- Panda is Android-only, Dan Glasses is hardware-agnostic
- Dan Glasses has a formal memory architecture; Panda had to disable memory (v1)
- Dan Glasses targets wearables; Panda runs on any Android device
- Dan Glasses has a multi-service architecture; Panda is a monolithic Kotlin app

### 13. Privacy-Preserving AI

Dan Glasses positions as **privacy-first**: all data stays local unless explicitly shared. This is a genuine differentiator given:
- Meta Ray-Ban's data goes to Meta's cloud
- Apple has full context awareness but data stays in Apple ecosystem
- Most "AI companion" apps are cloud-first with data harvesting concerns

**What Danlab needs to demonstrate:**
1. All inference runs locally on-device (no cloud callbacks for core reasoning)
2. Memory data is encrypted at rest (SQLite encryption)
3. No telemetry or usage data transmitted
4. User can export or delete all data
5. Open-source codebase for the privacy claims to be verifiable

**Genuine risk:** If any service (whisper.cpp, LFM2.5-VL-450M) makes a cloud API call for quality or fallback, the privacy claim is undermined.

---

## D. Technical Deep Dives

### Deep Dive 1: Self-Improving RL Loops (Chosen)

**Key finding:** The danlab-multimodal "RL feedback loop" is heuristic, not RL. Genuine self-improvement requires:

1. **Reward signal source** — two options:
   - External verifiable rewards (GRPO math/code style) — requires closed-form evaluation
   - Internal feedback (RLIF self-certainty) — works without ground truth

2. **Policy update mechanism** — two options:
   - Parameter updates (fine-tuning, LoRA) — expensive for edge deployment
   - In-context updates (ICPO/ME-ICPO) — no parameter change, just prompt refinement

3. **Most practical for Danlab:**
   - Implement **RLIF (Reinforcement Learning from Internal Feedback)** using Intuitor methodology
   - Self-certainty = model's confidence in its own response (measured from response entropy)
   - If self-certainty < threshold → regenerate with longer reasoning
   - No parameter updates required; pure inference-time adaptation

**Connection to Dan Glasses:** The perception pipeline produces descriptions. A self-improving loop would: produce description → self-evaluate confidence → regenerate if uncertain → commit to memory → update the self-evaluation model based on retrieval success.

### Deep Dive 2: Edge VLM Optimization (Chosen)

**Key finding:** LFM2.5-VL-450M is the right model, but ONNX + ExecuTorch may outperform GGUF for edge wearables:

1. **GGUF via llama.cpp** — mature, portable, CPU-optimized. Good for x86_64 laptop dev. May not be optimal for aarch64 Redax.

2. **ONNX + ExecuTorch** — ExecuTorch enables int8 weight-only quantization with torchao, compiled to aarch64 with hardware-specific kernels. The nanoVLM-230M-8k shows ~5.3× size reduction (528MB raw → ~100MBquantized ExecuTorch .pte). This could make even a 450M model fit in <200MB.

3. **TensorRT Edge-LLM** — Nvidia's workflow for FP8 quantization + ONNX export for edge deployment on Jetson/DRIVE. If Redax uses Nvidia Silodor/Tegra silicon, TensorRT is the path.

4. **Action for Danlab:**
   - Test LFM2.5-VL-450M via both llama.cpp (GGUF Q4_0) and ExecuTorch (int8) on actual Redax hardware
   - Compare inference latency AND power consumption
   - Prefer whichever has better power/latency tradeoff, not raw benchmark score

### Deep Dive 3: Vector Search and Memory Architectures for AI Companions (Chosen)

**Key finding:** Danlab's current SQLite + flat vector index is a 2024 architecture. 2026 state-of-the-art requires:

1. **Graph layer over vectors** — flat vector retrieval loses temporal/causal relationships. MAGMA / Synapse show that multi-relational graph traversal outperforms flat vector search on long-horizon reasoning tasks.

2. **Episodic-semantic coupling** — Synapse demonstrates that connecting raw interaction logs (episodic) to abstract semantic relations via spreading activation produces more coherent long-term narratives than pure semantic retrieval.

3. **Memory evolution** — H-Mem shows a tree-graph hybrid where short-term summarizes into long-term, enabling constant-time retrieval even with unbounded memory growth.

4. **Action for Danlab:**
   - Add temporal metadata to all memory writes now (free improvement, no architectural change)
   - Implement a lightweight entity graph (entities → episodes → relationships)
   - Plan migration from flat vectors to a GraphRAG hybrid architecture in v2
   - Evaluate Mem0, WorldDB, or SAGE as potential memoryd replacement in v2

---

## E. Summary of Key Gaps

| Gap | Severity | Fix |
|-----|----------|-----|
| VLM power draw uncharacterized | 🔴 CRITICAL | Measure on Redax hardware |
| Python services (not Rust as specced) | 🔴 CRITICAL | Migrate to Rust for wearable release |
| "RL loop" is heuristic, not RL | 🟡 MEDIUM | Either rename it or implement genuine RLIF |
| Memoryd flat vectors (2024 arch) | 🟡 MEDIUM | Add temporal graph, plan v2 upgrade |
| audiod subprocess-per-segment overhead | 🟡 MEDIUM | Implement streaming whisper pipeline |
| OpenClaw no process isolation | 🟡 MEDIUM | Add watchdog process + session checkpointing |
| KittenTTS latency unmeasured | 🟡 MEDIUM | Benchmark synthesis latency |
| No package signing mechanism defined | 🟢 MINOR | Define GPG signing workflow |
| Bootstrap wizard underspecified | 🟢 MINOR | Add wireframes and state machine |
| No form factor constraints validated | 🔴 CRITICAL | Hardware team input needed |

---

*Report complete. Artifacts generated: dan2-agi-roadmap.md, dan2-architecture-review.md, dan2-model-analysis.md, dan2-papers-to-read.md*
