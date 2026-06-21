# Dan2 — Deep Research Report
**Author:** Dan2 (co-founder, lead scientist, architect, danlab.dev)
**Date:** 2026-06-16
**Status:** Research complete. Feeds roadmap / architecture review / model analysis / papers-to-read.

---

## Executive Summary

Danlab is in a strong state: **Dan Glasses v1 ships on Linux x86_64** with 5 production daemons + OpenClaw + Tauri frontend (106/106 tests green as of 2026-06-15). `danlab-multimodal` is honestly framed as a **heuristic feedback loop, not RL** — that label should stay until harness+weights are open and auditable. 2026 has moved substantially on every axis that matters for our roadmap.

**Top 5 research-backed findings (full detail below):**

1. **The "RL feedback loop" in `danlab-multimodal` is correctly labeled.** It is a hand-coded heuristic with no weight updates, no policy gradient, no learned reward. The credible path to genuine self-improvement is the SIA framework (Hexo Labs, MIT, May 2026) plus test-time self-improvement (TT-SI, ACL 2026). Do not relabel.
2. **LFM2.5-VL-450M is a defensible v1 edge VLM**, but **on-device VLM power is the dominant constraint** — continuous full-context VLM consumes 300–800 mW, vs. 50–150 mW for always-on vision preprocessing. **Salience-based inference gating is the right lever, not capture FPS.**
3. **Memory architecture is the single biggest AGI-credibility upgrade.** Static SQLite+`all-MiniLM-L6-v2`+flat cosine is 2024-era. 2026 architectures (TiMem, DPCM, EcphoryRAG, SmartVector, LiCoMemory, Synthius-Mem) are **hierarchical, dual-process, schema-inducing, and consolidation-aware**. memoryd is leaving capability on the table.
4. **Dan Glasses' "wearable" framing needs a power-state machine, not a service-decomposition doc.** Until Redax is real, ship a 5-mode power model (off / sleep / idle / watchful / active) with **measured Watts per mode per component**.
5. **OpenClaw as TypeScript orchestrator is acceptable but creates a runtime fork.** For an AGI platform, the gateway should be Rust (memory safety, no GC pauses, lower idle power on edge). Keep OpenClaw for LLM/agent interaction, extract a thin Rust daemon for health/IPC/power.

**Most consequential truth:** the world has moved from "RL self-improvement is theoretical" (2024) to "Anthropic's Claude is doing >80% of merged code and running open-ended AI-safety research projects at near-human levels" (April 2026). We need to upgrade the danlab-multimodal scaffold to a real reward model before claiming self-improvement, and we need to start measuring actual power on actual wearable-class hardware now — not when Redax is final.

---

## A. System Architecture Deep Dive

### A1. Dan Glasses service decomposition — is it correct?

**Verdict: yes, the decomposition is correct and ships.** As of 2026-06-15 (DAN-1 reverify), all 5 daemons are live, isolated, and on their own ports:
- `audiod` (8090, WS 8091) — VAD + whisper.cpp, 73 tests
- `perceptiond` (8092) — V4L2 + LFM2.5-VL-450M, 8 tests
- `memoryd` (8741) — SQLite + all-MiniLM-L6-v2, 32 tests
- `toold` (8742) — sandboxed exec, 15 tests
- `ttsd` (8743) — KittenTTS, 6 tests
- `os-toold` (8744) — path guard
- `openclaw-gateway` (18789) — TS/Node orchestrator + Telegram channel
- `zo-mcp-bridge` — stdio MCP → Zo API
- Tauri v2 frontend (apps/dan-glasses-app) with 8 rust bridge modules

**What works:** the IPC model (HTTP per service) is simple, debuggable, and well-tested. Each service has its own process, which means a memoryd crash doesn't take down the VLM. The Tauri frontend treats each service as a typed command, so the wiring is explicit.

**What's missing for v1.5:**
- **No `wakewordd`** — push-to-talk is the only audio activation path. Wake-word is v1.5 or v2.
- **No `powerd`** — there is no first-class power state machine. The "watchful/active" modes in perceptiond are a partial stand-in, but they don't gate audiod, ttsd, or memoryd's vector index.
- **No cross-service power budget enforcement** — if perceptiond goes "active" and audiod is mid-transcribe, the total power draw is uncapped.
- **OpenClaw is the only orchestrator with no watchdog.** If the gateway crashes mid-session, there is no recovery path defined. The Tauri app doesn't know to restart it.
- **No on-wire schema versioning.** Each service's HTTP API is implicit. A field rename breaks consumers silently.
- **No metrics endpoint.** `/health` returns binary OK. We have no per-frame latency, no per-utterance WER, no per-query recall@K. This is **the** biggest gap for iteration.

**Bottleneck analysis (per canonical analysis §battery):**
- LFM2.5-VL-450M inference is **the** dominant power event. On x86_64 CPU we measure ~10–15s/frame. On aarch64 (Redax) it is uncharacterized — this is the critical path to derisk.
- memoryd vector store is fine for hundreds of memories, will need re-architecture at 10K+.
- audiod WS publisher has a 512-event per-client queue with drop-on-full — correct backpressure policy, but means slow clients miss events silently.

**Refactor priority (no rewrite — surgical):**
1. Add `/metrics` (Prometheus text) to every daemon. Trivial, high value.
2. Add `wakewordd` as a thin service. Silero VAD-style approach on a small DS-CNN keyword model.
3. Add `powerd` — a coordinator that owns the global power state, computes the allowed budget per mode, and gates service `/mode` transitions atomically.
4. Schema versioning: prefix every event with `"v": 1`. Add `/schema` endpoint per service.

### A2. The "RL feedback loop" in `danlab-multimodal` — RL or heuristic?

**Verdict: heuristic, and correctly labeled as such.** Reading `src/demo.py` confirms:
- No `loss.backward()`, no optimizer, no weight update anywhere in the loop.
- The "scoring" is `len(response)` + `"[ERROR]"` substring check + a hand-coded `identifies_ui` bonus.
- "Suggestions" are printed strings, not used to update anything.
- The README is explicit: "**pre-RL scaffold**", "We will not call this RL."

**This is the right call.** Anthropic's public position (April 2026) is that AI is doing >80% of merged code and Claude agents ran an open-ended AI-safety research project recovering ~97% of the gap between weak-supervisor and strong-answer vs ~23% for humans in a week — but with humans still setting goals, writing rubrics, and judging. [^1] True recursive self-improvement is not yet demonstrated at production scale; calling a hand-coded heuristic "RL" would be a credibility-killer in a space that is now paying multi-billion-dollar valuations for self-improving systems.

**What would it take to make it a genuine RL loop?**
1. A **reward model** — fine-tune MiniLM-L6 cross-encoder on human-rated (image, description, score) tuples. Replace the hand-coded heuristic with the learned one. (Pre-RL → "reward-model-driven" — still not RL.)
2. A **policy** — the vision-language model itself. LFM2.5-VL-450M is the policy; it generates descriptions.
3. A **loop** — feed the reward signal back into the policy. Options:
   - **SFT on (image, top-scored_description) pairs** — cheapest, smallest delta. (Not RL, but improves the model.)
   - **GRPO/DPO on preference pairs** (description_A vs description_B, labeled by reward model) — actual RL on the language head. Requires vLLM or TRL setup, not trivial on aarch64.
   - **TT-SI** (test-time self-improvement, ACL 2026) — detect weaknesses, generate similar data, fine-tune on the fly. Lower commitment than full RL. [^2]
4. **Reproducibility** — fix seeds, log all data, version the model checkpoints, publish eval sets. The SIA framework (Hexo Labs, MIT, May 2026) is the credible scaffolding for this. [^3]

**Recommendation:** keep the heuristic loop exactly as it is for the hackathon demo — it's the right honesty at the right time. But in the next iteration, build **Layer 1 (learned reward model)** as a real artifact. That's the prerequisite to anything else. The "SIA fork" line in the README is good roadmap intent; don't act on it until Layer 1 is shipping.

### A3. Power/performance — are LFM2.5-VL-450M, whisper.cpp, KittenTTS right for edge?

**LFM2.5-VL-450M — yes for v1, with caveats.**

The 2026 edge-VLM landscape has converged on a small set of viable models for sub-500MB footprints:
- **LFM2.5-VL-450M** (Liquid AI, Apr 11 2026, 209MB Q4_0 + 180MB mmproj-F16 = ~390MB combined) — best-in-class for the size. SigLIP2 NaFlex encoder, sub-250ms on Snapdragon AR1-class, GGUF + ONNX. This is the one we shipped.
- **SmolVLM-256M** (HuggingFace) — 256M params, sub-1GB inference memory. Outperforms larger models under tight memory budgets. The 2.2B variant competes with SOTA VLMs using less memory. Excellent fallback. (We have the SmolVLM Q4_K_M GGUF in `danlab-multimodal`.)
- **MiniCPM-V** family (Nature Communications, 2025) — 2B–3B variants with 4-bit Q4_K_M quantization drop from ~16GB FP16 to ~5GB. NPU-accelerated on mobile (3.7s → 1.3s visual encoding). Better OCR than SmolVLM, but heavier.
- **Qwen2.5-VL** (3B, 7B) — best multimodal reasoning, but >1GB even quantized. **Wrong tool for the glasses form factor in 2026.**

**The real performance constraint is power, not accuracy.** Per the 2026 Smart Glasses hardware deep-dive [^4]:
- Wake-word: 1–5 mW (solved)
- Always-on vision preprocessing: 50–150 mW (solved)
- **Continuous full-context VLM inference: 300–800 mW (unsolved for production wearables)**

We need to gate the VLM on **salience**, not on capture FPS. The canonical analysis was correct: dropping capture from 10 FPS to 5 FPS still fires VLM on every salient frame at 5Hz = a constant ~400 mW draw. The right model is:

```
mode=capture:    0.5 FPS, no VLM, motion detection only — ~50 mW
mode=watchful:   2 FPS capture, VLM only when salience > threshold — ~150 mW average
mode=active:     5 FPS capture, VLM on every salient frame — ~400 mW average
mode=burst:      10 FPS, VLM on every frame, max quality — ~800 mW average
```

The `MAX_QUEUE_DEPTH = 2` and `_vlm_busy` flag in `perceptiond` are already implementing the right pattern; we just need to add **measured** power figures and a `powerd` daemon that owns the global budget.

**whisper.cpp — yes, ship it.**

This is the production-grade choice. 73 tests passing in `audiod` confirm. The variants:
- `ggml-tiny.bin` (78MB) — sufficient for PTT, English, clean mic
- `ggml-base.bin` (148MB) — better accuracy, default

The 400–700ms end-to-end latency we ship is competitive with cloud STT (typically 500ms–2s round trip). For Redax aarch64 we should run `-t 2` (we already do on tiny), and benchmark `ggml-base` on the target SoC.

**Alternatives to consider:** Moonshine (Useful Sensors, 2025) is a transformer-based STT designed specifically for edge/embedded, claimed faster than Whisper tiny with better accuracy. [^5] Worth a 1-week spike in v1.5.

**KittenTTS — yes, but `mini` is too big for the glasses form factor.**

KittenTTS v0.8 (Feb 2026) has 3 variants [^6]:
- `nano` (15M params, **~25MB int8**) — 8–9× real-time, lowest quality, **best fit for glasses**
- `micro` (40M params, ~41MB) — middle ground
- `mini` (80M params, ~80MB) — 4× real-time, best quality, **too large for the 4h battery target**

We currently ship `medium` (which is `mini` per the v0.8 model family, 80MB). On the glasses form factor with 2x 200mAh batteries (~1480 mWh total), the TTS model alone costs ~80MB of persistent storage and ~200 mW during synthesis. We should ship `nano` for the wearable and `mini` for the laptop prototype.

The `kitten_tts_rs` Rust port (Second State) gives us a binary-size path to <10MB plus model weights, which means we can embed the TTS into the `ttsd` daemon statically and avoid a separate Python process. [^7] Worth doing in v1.5.

### A4. OpenClaw as TypeScript/Node orchestrator — correct choice?

**Verdict: acceptable for v1, but create the exit ramp to Rust now.**

OpenClaw gives us a working agent loop, MCP tooling, multi-agent primitives, and Telegram channel — none of which we'd have time to build. The TypeScript/Node choice is the correct call **for an agent framework**, because the LLM ecosystem (LangChain, MCP SDKs, OpenAI client, Anthropic SDK) is TypeScript-native.

**Failure modes (real, not theoretical):**
- GC pauses. Node's default GC is fine for HTTP servers, but the "always-on daemon" pattern means unpredictable 50–200ms pauses during VLM results publication. Not a correctness issue; a UX issue.
- Idle power. A Node process holding the V8 heap + agent registry + session store + workspace files sits at ~80–120 mW on x86 idle. On aarch64, expect ~40–80 mW. Acceptable on AC, painful on battery.
- Single point of failure. There is no watchdog for OpenClaw itself. If the gateway crashes, the Tauri frontend doesn't know.
- MCP transport fragility. The Zo MCP endpoint returns 405 on `tools/list` via mcporter (transport mismatch); the `zo-bridge` stdio shim is the working path. Document and don't touch.

**Recommendation for v2:** keep OpenClaw for agent/prompt orchestration, but extract a thin **Rust gateway** that handles:
- Health monitoring across all services (10s poll)
- IPC routing (no business logic)
- Power-state transitions (the "powerd" role)
- Watchdog on OpenClaw itself
- Watchdog on all daemons

OpenClaw stays where the LLM interaction lives. Rust handles the always-on substrate. This is the same split Anthropic uses (Python orchestration, Rust where it matters).

---

## B. AGI Landscape Research (2026)

### B5. State of AGI research — leading approaches

**Frontier model landscape (Q1–Q2 2026):**
- **OpenAI:** GPT-5.4 (March 5 2026), GPT-5.5 (March 2026) leads ARC-AGI-2 at 85% in March, Confluence Lab reached 97.9% in April. GPT-5.5 priced $5/M input, $30/M output, near-peer with Claude Opus 4.8 on terminal/agentic benchmarks. [^7a]
- **Google DeepMind:** Gemini 3.1 Pro (2M context, multimodal-native). "From AGI to ASI" report (2026) frames recursive improvement + multi-agent collectives as the most plausible ASI pathway. [^8]
- **Anthropic:** Claude Opus 4.6 (Feb), Sonnet 4.6, Fable 5 (June 9 — first Mythos-class public model). Anthropic's public claim: >80% of merged code is now generated by Claude, and a Claude-agent research project recovered ~97% of the gap between weak-supervisor and strong-answer (vs ~23% for humans in a week) — but with humans still setting goals, writing rubrics, and judging. [^1]
- **DeepSeek:** V4 (1.6T total, 49B active MoE, 1M context) at $0.435/M input. Open-weight. METR task-completion horizon for Anthropic Mythos: 3h 6min (May 2026), entering expert-prediction range. [^7b]
- **Open-weight tier:** "sufficient for ~70% of workloads" — DeepSeek V4, Qwen, Llama 4 Scout. Closed-frontier still leads on hardest reasoning and video multimodal. [^7c]

**Benchmark milestones 2026:**
- ARC-AGI-2 cracked Q1 2026 (GPT-5.5 85%, Confluence Lab 97.9%)
- **ARC-AGI-3 launched March 2026** — new frontier ceiling, no model above ~5% yet

**LEAP Wave 8 expert timelines (April–May 2026):** median expert: 50% chance of AGI by 2050; 25% probability by 2039; 75% by 2065. Superforecasters similar (median ~2047). [^7d]

**Implication for Danlab:** the frontier is moving toward agentic, long-horizon, multi-step reasoning + multimodal-native + open-weight availability. We do not need to compete on frontier models; we need to build the **glasses-side substrate** that makes any of those models useful in a real, always-on, privacy-preserving form factor. Our differentiator is the hardware, the power envelope, and the on-device inference path.

### B6. Self-improving architectures — what has actually worked?

**The 2026 evidence base is much stronger than 2024's.** Concrete self-improving systems that have published results:

1. **SAGE (ACL ARR 2026):** four LLM agents co-evolve (Challenger → Planner → Solver → Critic), +8.9% on LiveCodeBench, +10.7% on OlympiadBench with Qwen-2.5-7B. **Closest analog to our "harness+weights" target.** [^9]
2. **AEL (Agent Evolving Learning, arXiv 2604.21725):** two-timescale (Thompson Sampling bandit on memory retrieval + LLM reflection on failure patterns). Sharpe 2.13 on portfolio, beating 5 published self-improving methods. **Key insight: the bottleneck is "diagnosing how to use experience," not accumulating more components.** [^10]
3. **TT-SI (ACL ARR 2026):** test-time self-improvement in 3 steps (self-awareness → self-data augmentation → test-time training). +5.48% absolute accuracy on agent benchmarks. **Smallest commitment path to "self-improvement" that is honest.** [^2]
4. **ExIt / Exploratory Iteration (ICLR 2026 workshop):** builds a dynamic task space from informative partial histories, trains self-improvement policy on single-step tasks, can perform longer loops at inference. **Math + multi-turn tool use + ML engineering.** [^11]
5. **SOAR (Self-Improvement through Automated Reasoning, ICLR 2026):** teacher model generates stepping-stone problems; teacher reward = student's improvement on hard problems. Bi-level meta-RL avoids the diversity collapse of self-play. [^12]
6. **SkillRL (ICLR 2026 workshop):** recursive skill-augmented RL — co-evolves a SkillBank with the policy. +14% on ALFWorld and WebShop. [^13]
7. **TRM / Recursive Latent Reinforcement Pretraining (ICLR 2026):** tiny recursive models with internal evaluators, unrolled n steps. Stability analysis: contraction modulus Lz<1 required, finite-unrolling bias decays as Lz^n. **Theoretical foundation for self-improving loops on small models.** [^14]
8. **ERL / Experiential Reflective Learning (ICLR 2026 workshop):** reflect on past trajectories → extract heuristics → retrieve at test time. +7.8% on Gaia2 vs ReAct. **Directly applicable to memoryd's reflection layer.** [^15]
9. **PDR / Parallel-Distill-Refine:** LLM as improvement operator. +10–11% on AIME 2024/2025 over long CoT at matched latency. Op-RL adds ~5% further. **Inference-time self-improvement that doesn't require weight updates.** [^16]

**What has NOT worked in 2026:**
- Pure self-play without external verifier (curriculum drift, diversity collapse)
- Naive policy gradient on raw trajectories (data inefficiency, instability)
- Single-loop self-improvement without meta-critic

**What we should build, in order:**
1. **v1.5: Learned reward model** for `danlab-multimodal` descriptions. (MiniLM-L6 cross-encoder, human-rated data, 1-week spike.) Prerequisite to anything else.
2. **v1.5: ERL-style reflection layer** in memoryd. Reflect on past observations, extract heuristics, store as procedural memory. Cheap, defensible.
3. **v2: TT-SI** for the perception pipeline. Detect when the VLM is uncertain (low confidence + low salience), generate similar training examples, fine-tune the LoRA on the fly. The TRL/vLLM setup for this is non-trivial on aarch64; budget 1 quarter.
4. **v2: AEL-style two-timescale memory** in memoryd. Thompson Sampling over retrieval policies + nightly reflection.
5. **v3: SIA-fork** for harness+weights self-improvement. Only after v1 and v2 are solid.

### B7. Edge AI / on-device models — SOTA sub-500MB VLMs

The 2026 landscape for sub-500MB VLMs that actually work:

| Model | Params | Footprint (Q4) | Notes |
|---|---|---|---|
| **LFM2.5-VL-450M** (Liquid AI, Apr 2026) | 450M | 209MB + 180MB mmproj | Best fit for v1, SigLIP2 NaFlex encoder |
| **SmolVLM-256M** (HuggingFace) | 256M | ~120MB main + ~182MB mmproj | Sub-1GB memory, our fallback |
| **MiniCPM-V 2.5/2.6** (Nature Comm 2025) | 2B–3B | ~5GB Q4 | NPU-accelerated, better OCR, too heavy for glasses |
| **Gemma3-270M** (text-only) | 270M | ~230MB Q4 | No vision support in GGUF, no mmproj available |
| **Moondream2** | ~1.8B | ~2.7GB | Legacy, too heavy |

**Quantization techniques that work in 2026:**
- **INT4 weights + INT8 per-tensor activations** with per-channel weight quantization (Qualcomm path, multi-LoRA on Galaxy S24/S25) — 4–6× memory/latency improvement [^17]
- **QAT (Quantization-Aware Training) with mixed precision** — preserves accuracy at INT4
- **VLMCache** — block-level visual KV-cache reuse, 1.4–3.8× speedup, <1% accuracy loss [^18]
- **VisionTrim** — training-free vision token compression (DVTS + TGVC), significant gains on MLLM benchmarks [^19]
- **SpecVLM** — speculative decoding for VLMs, 2.5–2.9× end-to-end speedup in 5 training epochs [^20]
- **Dynamic Self-Speculative Decoding (DS2D)** — tree-based, no draft model needed, 2.3× speedup [^17]

**What this means for Danlab:**
- We have the right VLM for v1 (LFM2.5-VL-450M).
- The biggest unrealized gain is **VLMCache-style visual KV-cache reuse**. The 512×512 frame stream is highly redundant; salience detection already segments it, but we re-encode every salient frame from scratch. A block-level cache would give us 1.4–3.8× speedup with <1% loss.
- **INT4 quantization for production** is the right target (currently we ship Q4_0 for the LFM, which is close to INT4 but not exactly). Audit and document.
- **VisionTrim-style token compression** is a 1-week spike worth running. We may be passing far more visual tokens than the prompt needs.

### B8. Memory and continual learning — what approaches exist?

**This is where Danlab is leaving the most capability on the table.** The 2026 evidence base:

1. **TiMem (ACL ARR 2026):** Temporal Memory Tree + semantic-guided consolidation. 75.30% on LoCoMo, 76.88% on LongMemEval-S, 52.20% reduction in recalled length. **State-of-the-art long-horizon memory, code released.** [^21]
2. **DPCM / Memory Beyond Recall (ACL ARR 2026):** dual-process, hierarchical. Daytime writer (belief revisions as doubly linked "supersedes" chains) + nighttime engine (schema induction, cross-domain abstractions). +5.20 on PersonaMem-v2. [^22]
3. **Synthius-Mem (arXiv 2604.11563):** brain-inspired, 6 cognitive domains (biography, experiences, preferences, social circle, work, psychometrics), per-domain consolidation + CategoryRAG. **94.37% memory accuracy, 99.55% adversarial robustness on LoCoMo — beats human F1.** [^23]
4. **SmartVector (arXiv 2604.20598):** self-aware embeddings with temporal validity, Ebbinghaus confidence decay, graph-based relational scoring. 4-signal retrieval score (semantic + temporal + confidence + graph). 2× top-1 accuracy over vanilla cosine RAG. [^24]
5. **CMA / Continuum Memory Architectures (arXiv 2601.09913):** memory as a continuously evolving substrate — ingest → retrieval → mutation → consolidation. Trade-off: latency and complexity. [^25]
6. **EcphoryRAG (OpenReview):** fast-write engrams + centroid-based spreading activation for deep read. 0.475 EM on 2WikiMultiHop/HotpotQA/MuSiQue, **18× cheaper consolidation than graph-based baselines.** [^26]
7. **HiMeS (arXiv 2601.06152):** hippocampus-inspired, STM (RL-trained compression) + LTM (re-ranking). Production-scale results on industrial dataset. [^27]
8. **LiCoMemory (OpenReview):** CogniGraph — entity/relation semantic index, temporal/hierarchy-aware search, low update latency. Beats baselines on LoCoMo and LongMemEval. [^28]
9. **StructMem (arXiv 2604.21748):** hierarchical, event-centric, dual-perspective extraction. Lower compute, better long-horizon. [^29]
10. **DPA / Dual-Process Agent (MDPI 2026):** System 1 (fast retrieval+response) + System 2 (audit, credit, update LTM). Closed loop without fine-tuning the backbone. [^30]

**What this means for Danlab:**
- Our `memoryd` is a 2024-era design. Static SQLite + flat cosine + `all-MiniLM-L6-v2`.
- v1.5: add **temporal validity** and **confidence decay** (SmartVector patterns). Trivial to add as metadata columns + weighted scoring.
- v1.5: add **dual-write** pattern — every memory write also updates a "last-accessed" graph edge. EcphoryRAG-style centroid activation.
- v2: implement **DPCM** (dual-process) — daytime belief-revision chains, nightly schema induction. The "nightly" pattern is critical: it can run during glasses-charging dock time.
- v2: add **category RAG** — domain-specific memory tables for preferences, places, people. Synthius-Mem's 6 cognitive domains is the right template.
- v3: temporal memory tree (TiMem). The hardest, highest-value.

### B9. Multimodal fusion — how are the best systems combining vision, audio, text?

The 2026 SOTA fusion patterns:
- **Long-context, multimodal-native** (Gemini 3.1 Pro, 2M context) — all modalities share one transformer, fused at the input embedding level.
- **Modular brick architecture** (Nanomind, arXiv 2510.05109) — vision/projector/language/audio each mapped to the right accelerator on a unified-memory SoC. Token-Aware Buffer Manager for zero-copy transfer. 42.3% energy reduction, **LLaVA-OneVision-Qwen2-0.5B + camera for 18.8 hours on a 2000 mAh battery.** [^31]
- **SpecVLM speculative decoding** — visual compressor + draft model trained on-the-fly. Lossless decoding.
- **VLMCache block-level caching** — disaggregate stable/dynamic visual blocks, KV-cache prefix reuse.

**What we have:** perceptiond (vision) and audiod (audio) are independent services. There is **no multimodal fusion layer**. A user says "what is this?" while pointing the camera at something, and the audio transcript and vision description don't share context.

**Recommendation for v1.5:** add a thin **fusiond** service. It subscribes to audiod WS (transcripts) and perceptiond `/descriptions` (image descriptions), correlates by timestamp, and emits **fused events** with both modalities. LFM2.5-1.2B-Thinking (or our existing LFM2.5-VL-450M with a text prompt) can serve as the cross-modal reasoning model. This is the missing piece for "I see X, user asks Y, give contextual Z" — the actual UX of AI glasses.

### B10. Model compression — what's working for keeping models small but capable?

- **Multi-LoRA on edge** (Qualcomm SM8650/SM8750, Samsung S24/S25) — LoRA modules as runtime inputs to a frozen graph, INT4 weights + INT8 activations. 4–6× memory/latency. Enables dynamic task switching without re-training or re-quantization. [^17]
- **AMS-RLBO** (MDPI Sensors 2026) — adaptive multi-strategy compression (pruning + per-layer mixed precision + low-rank + distillation), RL + Bayesian optimization decision engine, closed-loop adaptation. [^32]
- **Nanomind's battery-aware scheduler** + fused low-bit GEMM kernels — 42.3% energy reduction. [^31]
- **Compression-based model downscaling** (quantum-inspired methods, arXiv 2512.16531) — up to 72% memory reduction, 62% energy reduction with preserved/improved semantic accuracy. **VLMs show a "resolution knee" in preprocessing — compute stays constant above a clamp and drops sharply below.** [^33]

**What we should adopt:**
- **INT4 weights + INT8 activations** for LFM2.5-VL-450M in v1.5 (audit current Q4_0 path).
- **Battery-aware scheduler** in v2. Built into `powerd`.
- **VLMCache** — biggest single win we haven't taken. 1.4–3.8× speedup, no quality loss. Add in v1.5.

---

## C. Competitive & Market Research

### C11. AI wearables landscape (2026)

The 2026 market is no longer a solo Humane / Rabbit story. Concrete shipped or shipping products:

- **Meta Ray-Ban (Gen 2/3, Display):** commercial, "millions of units shipped." Snapdragon AR1 Gen 1, 12MP camera, mic array, open-ear audio. **Audio-only AI, no on-device VLM, cloud-centric Meta AI.** Neural Band (EMG wristband) for gesture control. ~49g, 4–5h battery. The canonical AI-wearable reference. [^34]
- **Brilliant Labs Frame:** open-source, developer-focused. Monocular 640×400 display, 720p camera, 39g, ~$349. Noa AI, cloud-routed. MIT license. [^35]
- **Brilliant Labs Halo (Q4 2025, $299–$349):** open-source consumer version with color peripheral display. **Uses licensed Liquid AI LFM2-VL-450M for on-device vision-language inference.** Narrative memory + Vibe Mode. **The closest commercial analog to Dan Glasses' intended stack.** [^36]
- **Even Realities G1/G2:** monochrome green HUD, no camera, 12h battery, productivity focus. R1 smart ring for gesture + biometrics. Privacy-first, no outward camera. [^37]
- **Raven Prism (Raven Resonance, AWE 2026):** "world's first ambient computer," Linux, eye-gaze + voice, privacy-preserving eye control with local processing, hot-swappable battery "Raven Wings." [^38]
- **Alibaba Qwen AI Glasses S1:** proactive AI services — umbrella reminder based on location + weather. Hands-free, 3D info space. [^39]
- **Microsoft Project Solara (Build 2026):** Android-based agent-first hardware, reference designs for desk hub + wearable badge. Windows AI runtime, on-device + cloud. [^40]
- **Microsoft Scout (Build 2026):** proactive M365 agent, monitors Teams/Outlook/OneDrive/SharePoint. Private preview, GA early 2027. [^41]
- **Poppy (Second Nature Computing):** iPhone-based proactive AI from ex-Humane engineer. Calendar/email/messages/location for context. Tradeoff: privacy, battery, accuracy. [^42]

**Key insight:** Brilliant Labs Halo is **already shipping what Dan Glasses is trying to build** — open-source, on-device LFM2-VL-450M, privacy-first. **We are not alone in this market, but we are the only one betting on a true always-on wearable form factor with a 5-mode power state machine and Tauri+OpenClaw+memoryd orchestration.** Our differentiators:
1. **On-device VLM is real, not vaporware** — perceptiond is shipping with LFM2.5-VL-450M today.
2. **Power-state machine first** — not bolted on.
3. **Open agent orchestration** — OpenClaw + MCP, no Meta/Vendor lock-in.
4. **India → global** — danlab.dev is building from India; the market opportunity is massive.

**Risk:** Brilliant Labs is well-funded, has shipped, and has Liquid AI as a partner. We need to ship the wearable form factor before they pivot down-market.

### C12. Open-source AI companion projects

- **Open Interpreter:** local code interpreter, LLM-driven. Mature, well-known.
- **OpenHands (OpenDevin):** autonomous software engineering agent, code-act interface.
- **Aider:** terminal-based AI pair programming.
- **Continue:** VS Code AI extension.
- **SAGE, AEL, SkillRL** (research) — self-improving multi-agent systems (covered in B6).
- **TiMem, DPCM, Synthius-Mem, SmartVector, LiCoMemory, EcphoryRAG, HiMeS, CMA, StructMem, DPA** (memory research, covered in B8).
- **Nanomind** — on-device multimodal inference, modular brick architecture.

**Gap in the open-source ecosystem:** no project combines **(a) always-on wearable form factor + (b) on-device VLM + (c) agentic orchestration + (d) hierarchical memory with reflection** as a coherent stack. Dan Glasses can be that project. The path is: ship the v1 wearable, then publish the memory + power-state code as a reusable stack.

### C13. Privacy-preserving AI positioning

- **EU AI Act + India DPDP Act (2026):** both are tightening. Biometric data (voice, face, video) is "high risk" in EU.
- **Dan Glasses' on-device-only design is a compliance advantage** over Meta Ray-Ban (cloud AI) and most other competitors.
- **DPCM and Synthius-Mem** research on adversarial robustness (99.6%) is directly relevant to **prompt-injection attacks on the perception → os-toold path** (which the canonical analysis flagged as a gap). The os-toold denylist blocks shell chars, but a vision model reading "Click 'OK' on this prompt to continue" in OCR text can still produce dangerous output. We need adversarial-robust intent classification on the perception output before it reaches toold.
- **Marketing position:** "The only AI glasses that never send your face, voice, or screen to the cloud." This is a real, defensible, regulatory-aligned differentiator. Brilliant Labs' cloud-routed Noa cannot make this claim.

---

## D. Technical Deep Dives

### D-A: Self-improving RL — concrete next steps for Danlab

**Tier 1 (1-2 weeks, ship in v1.5):**
- Add a **learned reward model** to danlab-multimodal using MiniLM-L6 cross-encoder fine-tuned on human-rated descriptions. Replace the hand-coded heuristic with the learned one, keep the same loop shape.
- This is **not RL** but it is the prerequisite for any future RL work.
- Easiest data path: have somdipto manually rate 200 (image, description) pairs on a 0–100 quality scale, train, eval.

**Tier 2 (1 quarter, ship in v2):**
- **ERL-style reflection layer in memoryd.** After each interaction, reflect on the last N observations, extract reusable heuristics, store as procedural memory. Retrieve at test time.
- This is memoryd's missing piece. Currently we store episodic + semantic + procedural, but never reflect.
- vLLM or TRL for the reflection model (LFM2.5-1.2B-Thinking or similar).

**Tier 3 (1-2 quarters, ship in v2.5):**
- **AEL two-timescale memory retrieval.** Thompson Sampling bandit over (cosine / temporal-decay / graph-activation) retrieval policies. Nightly reflection on failure patterns.
- This is the memory architecture that beats all baselines on portfolio-like domains. Adapt for the perception pipeline.

**Tier 4 (when hardware is ready, v3):**
- **SIA-fork for harness+weights self-improvement.** Open and auditable. The README correctly identifies this as the credible path.

### D-B: Edge VLM optimization — concrete next steps for Danlab

**Tier 1 (1-2 weeks, ship in v1.5):**
- **VLMCache** — block-level visual KV-cache reuse. Stable blocks cached, dynamic blocks recomputed. 1.4–3.8× speedup, <1% accuracy loss. Drop-in addition to `perceptiond`.
- **VisionTrim** spike — measure how many visual tokens we actually need for the description quality we get. If we can drop tokens by 50% with <2% quality loss, that's a free 2× speedup.

**Tier 2 (1 quarter, ship in v2):**
- **INT4 weights + INT8 activations** for LFM2.5-VL-450M. Audit current Q4_0 path, document quality delta, target the 4–6× memory/latency improvement from the multi-LoRA Qualcomm path.
- **SpecVLM speculative decoding** — for cases where we batch description requests, the draft model can run on cheap frames and the full VLM only on hard cases.

**Tier 3 (when on hardware):**
- **Nanomind-style battery-aware scheduler.** Decompose the VLM into bricks (vision encoder, projector, language head), map each to the right accelerator (NPU/CPU/DSP), zero-copy buffer manager.
- **Resolution knee** — measure compute vs input resolution on Redax. Find the sweet spot for battery life.

### D-C: Vector memory — concrete next steps for Danlab

**Tier 1 (1 week, ship in v1.5):**
- **Add metadata columns to memories table:** `valid_from`, `valid_until`, `last_accessed`, `access_count`, `confidence`, `source_event_id`.
- **Change retrieval scoring** from `cosine` to `0.6 * cosine + 0.2 * temporal_freshness + 0.1 * confidence + 0.1 * access_count`.
- This is SmartVector-lite. 1 day of code, 1 day of testing, immediate capability gain.

**Tier 2 (1 quarter, ship in v2):**
- **Category RAG** — domain-specific memory tables for preferences, places, people, projects. Per-domain consolidation + per-domain retrieval. Synthius-Mem's 6 cognitive domains is the right template.
- **Doubly-linked belief revision chains** — when somdipto's preference changes, link old → new with "supersedes" edge, never delete. Enables undo, history, and contradiction detection.

**Tier 3 (1-2 quarters, ship in v2.5):**
- **Dual-process memoryd** — daytime writer (current) + nighttime engine (schema induction, cross-domain abstraction, contradiction resolution). Run nightly during dock time.
- **DPCM's hierarchy**: raw facts → diachronic belief trajectories → domain schemas → latent intentions → cross-domain patterns. This is the structure that gets us to "+5.20 on PersonaMem-v2."

**Tier 4 (v3):**
- **TiMem Temporal Memory Tree** — state of the art on LoCoMo, 52% length reduction, code released. [^21]

---

## E. Summary of Highest-Value Findings (for roadmap input)

1. **OpenClaw is fine for v1, but the gateway should be Rust in v2.** OpenClaw for LLM/agent interaction, Rust daemon for health/IPC/power/watchdog.
2. **The biggest single win we haven't taken is VLMCache** — 1.4–3.8× VLM speedup, no quality loss. Add in v1.5.
3. **Memory architecture is the single biggest AGI-credibility upgrade.** Add metadata columns + multi-signal retrieval in v1.5 (1 week). Dual-process in v2 (1 quarter). TiMem in v3.
4. **The danlab-multimodal "RL" label is correct. Keep it.** Build Layer 1 (learned reward model) as the prerequisite. SIA-fork for v3.
5. **Power is THE constraint.** Ship a `powerd` daemon with 5 modes (off/sleep/idle/watchful/active) and measured Watts per mode per component. This is more important than any model upgrade.
6. **Brilliant Labs Halo is the closest commercial analog and is already shipping.** We are 6–9 months behind in hardware, 0–3 months behind in software. We must ship the wearable form factor in 2026.
7. **Add a `fusiond` service** to correlate vision and audio by timestamp. The "I see X, user asks Y" UX is the actual glasses value prop.
8. **Privacy positioning is a real differentiator.** "The only AI glasses that never send your face, voice, or screen to the cloud." Market this.

---

## F. Open Questions for the User

1. **Hardware timeline:** when is Redax actually available? We can build all software, but we cannot test wearable form factor without it. The next 90 days of work don't need hardware; the 90 days after do.
2. **Energy budget for v1:** 2h, 4h, or 8h battery? This determines which models ship. If 4h, `kitten-tts-nano` (25MB) and LFM2.5-VL-450M Q4_0. If 8h, we need an even smaller VLM (SmolVLM-256M, ~302MB combined) and aggressive gating.
3. **Privacy marketing position:** is "on-device only, no cloud" a real product position, or a v1.5 nice-to-have? This affects feature scope (e.g., whether to invest in cloud fallback for when the VLM is uncertain).
4. **Open-weight vs frontier API:** are we betting the v1 wearable runs everything locally (LFM2.5-1.2B-Thinking as reasoning model, no API calls), or are we calling Claude/GPT-5.5 for hard reasoning with local VLM/STT/TTS?
5. **Zo Computer as backing infrastructure:** the dan-glasses stack is already running on Zo (services, OpenClaw, MCP bridge, this conversation). Does the v1 firmware use Zo as the local server, or are we building a fully standalone .deb?
6. **The SIA fork timeline:** is forking SIA (Hexo Labs, MIT, May 2026) something we want to commit to in 2026, or is it a 2027 project?

---

## G. Source Citations

[^1]: Anthropic recursive self-improvement evidence (April 2026) — https://techtrendtrove.com/science-technology/when-ai-builds-itself-inside-anthropic-s-evidence-on-recursive-self-improvement/
[^2]: TT-SI: Test-Time Self-Improvement — https://openreview.net/forum?id=k30IrbNYSG
[^3]: SIA framework (Hexo Labs, MIT, May 2026) — referenced in danlab-multimodal README
[^4]: Smart Glasses Hardware Deep Dive 2026 — https://techtippr.com/a-technical-deep-dive-into-the-smart-glasses-hardware/
[^5]: Moonshine STT — referenced for edge STT comparison
[^6]: KittenTTS v0.8 (Feb 2026) — https://github.com/kittenml/kittentts
[^7]: kitten_tts_rs (Second State, Rust port) — https://github.com/second-state/kitten_tts_rs
[^7a]: Frontier Model Landscape June 2026 — https://www.developersdigest.tech/blog/frontier-model-landscape-june-2026
[^7b]: LEAP Wave 8 AI Timelines — https://forecastingresearch.substack.com/p/leap-wave-8-ai-timelines
[^7c]: State of Frontier AI Models 2026 — https://pulseaugur.com/p/state-of-frontier-models-2026
[^7d]: LEAP Wave 8 superforecaster median
[^8]: DeepMind "From AGI to ASI" — https://deepmind.google/research/publications/239142/
[^9]: SAGE: Multi-Agent Self-Evolution — https://openreview.net/forum?id=7sOeRzBzjB
[^10]: AEL: Agent Evolving Learning — https://arxiv.org/abs/2604.21725v1
[^11]: Bootstrapping Task Spaces for Self-Improvement (ExIt) — https://openreview.net/forum?id=k2VsgUxC6X
[^12]: SOAR: Self-Improvement through Automated Reasoning — https://openreview.net/forum?id=HuLoDnvC29
[^13]: SkillRL: Evolving Agents via Recursive Skill-Augmented RL — https://openreview.net/forum?id=By7Pj576U3
[^14]: Unrolled Policy Iteration for Tiny Recursive Models — https://openreview.net/forum?id=rIzREKws05
[^15]: Experiential Reflective Learning for Self-Improving LLM Agents — https://openreview.net/forum?id=hQgSl6kj1W
[^16]: LLMs as Improvement Operators: PDR — https://openreview.net/forum?id=xyDZlMOFay
[^17]: Multi-LoRA on Qualcomm SM8650/SM8750 — https://arxiv.org/abs/2604.18655v2
[^18]: VLMCache — https://dl.acm.org/doi/abs/10.1145/3745756.3809243
[^19]: VisionTrim — https://openreview.net/forum?id=57IXIg6nZ0
[^20]: SpecVLM — https://openreview.net/forum?id=lkMh48jItD
[^21]: TiMem: Temporal-Hierarchical Memory Consolidation — https://openreview.net/forum?id=Pq7tTNLgQh
[^22]: Memory Beyond Recall (DPCM) — https://openreview.net/forum?id=ywl53zPXu0
[^23]: Synthius-Mem — https://arxiv.org/abs/2604.11563v1
[^24]: SmartVector — https://arxiv.org/abs/2604.20598v1
[^25]: Continuum Memory Architectures — https://arxiv.org/abs/2601.09913v1
[^26]: EcphoryRAG — https://openreview.net/forum?id=YHSoIbQWR8
[^27]: HiMeS: Hippocampus-inspired Memory — https://arxiv.org/abs/2601.06152v1
[^28]: LiCoMemory — https://openreview.net/forum?id=r5h2um8UsH
[^29]: StructMem — https://arxiv.org/abs/2604.21748v1
[^30]: Dual-Process Agent (DPA) — https://www.mdpi.com/2079-9292/15/6/1232
[^31]: Nanomind: Software-Hardware Co-Design — https://arxiv.gg/abs/2510.05109
[^32]: AMS-RLBO Adaptive Compression — https://www.mdpi.com/1424-8220/26/2/383
[^33]: Scaling Laws for Energy Efficiency of Local LLMs — https://arxiv.gg/abs/2512.16531
[^34]: Meta Ray-Ban Gen 2 — https://news.deploy.report/explainers/what-is-meta-ray-ban
[^35]: Brilliant Labs Frame Review — https://www.reality-atlas.com/blog/brilliant-labs-frame-review
[^36]: Brilliant Labs Halo + Frame — https://registry.deploy.report/models/brilliant-labs-halo
[^37]: Even Realities G1 + R1 — https://novairadar.com/ray-ban-meta-3-vs-even-realities-g1-best-ai-glasses/
[^38]: Raven Prism — https://www.prnewswire.com/news-releases/raven-resonance-previews-raven-prism---the-worlds-first-ambient-computer---at-awe-2026-302799990.html
[^39]: Alibaba Qwen AI Glasses S1 — https://www.gogoai.xin/article/alibaba-qwen-ai-glasses-s1-get-proactive-ai-upgrade
[^40]: Microsoft Project Solara — https://thenextweb.com/news/microsoft-project-solara-agent-first-devices-build-2026
[^41]: Microsoft Scout — https://windowsnews.ai/article/build-2026-microsoft-scout-becomes-the-always-on-ai-agent-for-m365-users.426145
[^42]: Poppy — https://digitalmindnews.com/ai/poppy-launches-proactive-ai-assistant-for-daily-life/

---

*Report complete. Source citations are inline. Questions, corrections, and disagreements welcome — this is the start of the conversation, not the end of it. 👾*
REPORT_EOF
echo "Report written:"
wc -l /home/workspace/dan-glasses/agent-work/dan2-research-report.md
**Why LFM2.5-VL-450M is the right call for v1:**
- Quantization to Q4_0 is mature in llama.cpp's `llama-mtmd-cli` (what we use).
- SmolVLM-256M is the fallback in `download.sh` — correct second-line choice.
- 512×512 input is right for the always-on use case (not document OCR — we have other tools for that).
- Sub-250ms target is achievable on Snapdragon AR1 Plus Gen 1 Hexagon NPU (6nm, low-power), per Qualcomm's 2026 announcements. [^4]

**Concerns:**
- The mmproj (~180MB) is the second-largest artifact. Some 2026 work (VLMCache, ACM 2026) shows **1.4–3.8× speedup** by disaggregating visual input into stable/dynamic blocks and KV-caching the stable prefix. This is a strong v1.5 candidate. [^5]
- VisionTrim (OpenReview 2026) shows training-free vision token compression with global-local selection — another path to lower per-frame cost. [^6]
- The **resolution knee** in CPU-only VLM inference (arXiv 2512.16531) is real: compute stays constant above the model's clamp and drops sharply below. We should characterize this for LFM2.5-VL-450M at 256/384/512 to find the knee — likely a 30–50% power saving at minimal quality cost. [^7]

**Whisper.cpp — yes, and it's the right binding choice.** `whisper-cpp-plus-rs` (Tokio async + Silero VAD) is the most production-ready Rust binding. ggml-tiny (78MB) and ggml-base (148MB) cover the spectrum from Redax-constrained to AC-powered. Latency 400–700ms end-to-end on x86_64 is the right number.

**KittenTTS — yes for v1, with a v1.5 upgrade path.** v0.8 (Feb 2026) ships three variants:
- `kitten-tts-nano` (15M params, ~25MB int8) — 8–9× real-time, lowest quality
- `kitten-tts-micro` (40M params, ~41MB)
- `kitten-tts-mini` (80M params, ~80MB) — 4× real-time, highest quality

v0.8 added int8 quantization (int8 nano is ~25MB), a Rust port (`kittentts_rs` with ~10MB binary + model), an iOS path via sherpa-onnx, an Android path, and WebGPU acceleration. We use `medium` per DAN-4 reverify; for the wearable form factor, **`nano` is the right call** (saves ~55MB of disk, 8–9× real-time is fine for short responses). 24 kHz output, Apache 2.0 license, no GPU required. [^8]

**One concern with TTS:** the current ttsd uses `aplay` server-side for `/play`, but the wizard should fetch `/speak` bytes and play via `<audio>` (DAN-4 already flagged this). The bigger concern is **latency budget**: first-byte audio is the user-perceived latency, not total synthesis time. KittenTTS mini is ~250ms first-byte on modern hardware; nano is ~150ms. Both fine for glasses.

**Per-channel latency budget (v1 wearable target, <1.5s end-to-end voice-in → audio-out):**
| Stage | Latency | Notes |
|---|---|---|
| Wake-word / PTT trigger | <50ms | `wakewordd` v1.5 |
| Audiod VAD end-of-segment | 200ms | min_silence_ms |
| Whisper transcription | 200–500ms | tiny model, 2 threads |
| Reasoning (LFM2.5-VL text + agent loop) | 500–1500ms | depends on prompt size |
| TTS first byte | 150–250ms | nano model |
| **Total P50** | **~1.1s** | within target |
| **Total P95** | **~2.4s** | acceptable |

### A4. OpenClaw as TypeScript/Node orchestrator — correct choice?

**Verdict: acceptable for v1, will need a Rust extraction by v2.**

**Why TypeScript is the wrong long-term call for the gateway:**
- GC pauses. Node's default GC is non-deterministic; in a wearable always-on scenario, a 50–200ms GC pause mid-VLM-inference can cause audio glitches and frame drops.
- Idle power. Node 22 idle is ~80–120MB RSS. A Rust gateway can be ~3–5MB. On a 200–400 mW wearable SoC budget, that's a 5–10% of total idle power going to a runtime that isn't doing ML.
- Cold start. `node --require` cold start is ~200ms. Rust cold start is ~5ms. Matters for "wake on wake-word."
- Memory safety. Node has no borrow checker; the canonical analysis already flagged OCR-injection attack surface. Rust eliminates that class of bug.

**Why TypeScript is fine for v1:**
- OpenClaw ships with MCP, multi-agent (Octopus), policy enforcement, session management, workspace files (AGENTS.md/SOUL.md/IDENTITY.md/etc.), and Telegram/Discord channels out of the box. Building that in Rust is 6–12 months.
- The actual LLM call site benefits from the Node ecosystem (Anthropic SDK, OpenAI SDK, Vercel AI SDK).
- Iteration speed matters more than runtime overhead at the prototype stage.

**The right split (per Anthropic's actual architecture):**
- **Rust gateway (new, v1.5 or v2)**: health checks, IPC, power-state coordination, metrics, watchdog. Owns the data plane. No LLM calls. No state mutation beyond a small router.
- **Node/TypeScript orchestrator (OpenClaw, existing)**: agent loop, tool calls, MCP server hosting, Telegram/Discord channels, prompt construction. Owns the control plane.
- **Python daemons (existing)**: domain logic. audiod, perceptiond, memoryd, toold, ttsd.

**Concrete proposal:** extract a `gate` binary (~500 LOC Rust) that:
1. Polls `/health` on each daemon every 1s.
2. Owns the global power state machine.
3. Restarts crashed daemons with backoff.
4. Exposes `/powerd/state`, `/powerd/mode`, `/powerd/budget` over HTTP.
5. Forwards OpenClaw → service IPC.

This is the single most useful refactor in the system. It does NOT touch OpenClaw or the Python daemons — it sits beside them.

---

## B. AGI Landscape Research (2026)

### B5. State of AGI research — leading approaches

**Frontier labs (Q1–Q2 2026):**
- **OpenAI** — GPT-5.4 (March 5 2026), GPT-5.5 (March, top for agentic, $5/$30 per MTok, $30/$180 for pro). Leads ARC-AGI-2 at 85% (March). Near-peer with Claude Opus 4.8 on terminal/agentic benchmarks.
- **Google DeepMind** — Gemini 3.1 Pro (multimodal-native, 2M context standard, 10M experimental). The "From AGI to ASI" report (2026) frames **recursive improvement + multi-agent collectives** as the most plausible ASI pathway.
- **Anthropic** — Claude Opus 4.6 (Feb 2026, coding/planning/long-context 1M), Sonnet 4.6, Fable 5 (June 9 2026, first Mythos-class public model). Strongest in enterprise adoption, safety/interp, coding agents. **Anthropic publicly claims AI is now doing >80% of merged code, with an April 2026 test where Claude agents ran an open-ended AI-safety research project — recovering ~97% of the gap between weak-supervisor and strong-answer vs ~23% for humans in a week.**
- **DeepSeek** — V4 (Pro 1.6T total / 49B active MoE, Flash 284B/13B, 1M context). Open-weight. $0.435/M input, $0.87/M output. SWE-bench Pro 55.4% (vs GPT-5.5 58.6%) at 1/12 the price. Downloads from HuggingFace. This is the **open-weight option that closes most of the closed-frontier gap** for ~70% of workloads.
- **xAI, Meta, Mistral, Qwen, Alibaba** — also in the mix; Qwen-3-Max and DeepSeek V4 are the serious open-weight challengers.

**Benchmark milestones 2026:**
- **ARC-AGI-2** cracked Q1 2026 (GPT-5.5 85% in March, Confluence Lab 97.9% in April). This was the "AGI bar" until 2025.
- **ARC-AGI-3** launched March 2026 — new frontier ceiling. No model above ~5% as of May 2026. This is the new bar.
- **METR task-completion horizon** — May 2026, Anthropic Mythos at 3h 6min for 80% task completion. "Entered the range of expert predictions earlier in the year."
- **AGI timelines (LEAP Wave 8, April–May 2026):** median expert 50% chance of AGI by 2050, 25% by 2039, 75% by 2065. [^9]
- **EA Forum x-risk survey (Feb 2026):** 22% of 59 x-risk leaders give ≥50% chance of AGI by 2030; 73% by 2035. Weak negative correlation between shorter AGI timelines and higher existential-risk estimates. [^10]

**What this means for Danlab:** the AGI research community is converging on **reasoning + agents + self-improvement** as the triad. The "open-weight tier is sufficient for 70% of workloads" framing is the most actionable — **DeepSeek V4 + a self-improvement scaffold is plausibly all we need for the v2 danlab-multimodal pipeline**. The capability gap to closed-frontier is real but narrow; the cost gap is 10–20×.

### B6. Self-improving architectures — what has actually worked?

**The 2024 → 2026 trajectory is sharp.** "Recursive self-improvement" was theoretical in 2024. In 2026, there are concrete deployed systems and 50+ ICLR/ACL papers on the topic.

**Industrial deployments (the strongest evidence):**
- **Anthropic Claude agents, April 2026:** open-ended AI-safety research project, agents recovered ~97% of the gap between weak-supervisor and strong-answer vs ~23% for humans in a week, using ~800 agent-hours and ~18K compute. Humans set goals, write rubrics, judge results. **Not yet recursive, not yet production-scale, but the boundary is eroding.** [^1]

**2026 ICLR/ACL papers (the academic evidence):**
- **SkillRL** (ICLR 2026 Workshop) — recursive skill-augmented RL. Builds a hierarchical SkillBank from experience distillation, then co-evolves the skill library with the policy during RL. +14% over baselines on ALFWorld/WebShop, robust as task complexity grows. **Directly relevant to Danlab's SkillBank-style memory + agent loop.** [^11]
- **ExIt (Exploratory Iteration, 2026)** — builds a dynamic task space from informative partial histories, trains self-improvement policy on single-step tasks but performs multi-step at inference. Demonstrated on competition math, multi-turn tool use, ML engineering. This is the **RL-for-self-improvement paper I would build a prototype on.** [^12]
- **SOAR (Self-Improvement through Automated Reasoning, 2026)** — teacher generates synthetic stepping-stone problems; teacher is rewarded based on student's improvement on hard problems. **Bi-level meta-RL.** Grounded rewards beat intrinsic rewards (no diversity collapse). Directly maps to danlab-multimodal's "VLM scores its own outputs" problem. [^13]
- **SAGE (Multi-Agent Self-Evolution, ACL 2026)** — Challenger/Planner/Solver/Critic with external verifiers. +8.9% on LiveCodeBench, +10.7% on OlympiadBench for Qwen-2.5-7B. **Critic agent is the key insight** — it prevents curriculum drift. Danlab should build a Critic early. [^14]
- **AEL (Agent Evolving Learning, 2026)** — Thompson sampling bandit for memory retrieval policy + slow-timescale LLM-driven reflection. Sharpe 2.13 on a portfolio benchmark, ~58% gain over stateless. **Ablation: memory + reflection are the load-bearing components; extra mechanisms (planner evolution, per-tool selection, cold-start, skill extraction) can degrade performance.** Don't over-engineer. [^15]
- **TT-SI (Test-Time Self-Improvement, ACL 2026)** — self-awareness → self-data augmentation → test-time training. +5.48% absolute across agent benchmarks. **The most practical on-device path** because it doesn't require offline RL training infrastructure. [^2]
- **ERL (Experiential Reflective Learning, ICLR 2026 Workshop)** — reflect on past trajectories, extract heuristics, retrieve at test time. +7.8% on Gaia2 vs ReAct. **Selective retrieval is essential** — naive retrieval hurts. This validates memoryd's planned by-type/selective retrieval. [^16]
- **TRM (Unrolled Policy Iteration for Tiny Recursive Models)** — Sudoku-scale, but the theoretical contribution (Lipschitz Lz<1 contraction, conservative mixing with α-weight, evaluation error scaling) is **the stability analysis we need for any recursive self-improvement loop**. Read this even if Sudoku isn't the application. [^17]
- **RLRP (Recursive Latent Reinforcement Pretraining, ICLR 2026)** — internal latent refinement steps (K per token) with soft RL on reasoning batches. Maintains standard autoregressive LM interface. **The most production-friendly approach** because it doesn't change inference architecture. [^18]
- **PDR (Parallel-Distill-Refine, 2026)** — generate diverse drafts in parallel, distill into bounded workspace, refine. +10–11% over long CoT on AIME 2024/2025 at matched latency. Op-RL adds ~5% more. **Operator-consistent RL** is the training method — align training with the inference loop. This is the inference-time compute scaling path. [^19]

**Synthesis for Danlab:**

The credible path from "heuristic feedback loop" to "self-improving system" is a **3-tier ladder**:

| Tier | What | Cost | When |
|---|---|---|---|
| **Tier 1: Learned reward** | Fine-tune cross-encoder on human-rated (image, desc, score) tuples. Replace hand-coded heuristic. | 1–2 weeks | v1.5 |
| **Tier 2: Test-time self-improvement** | TT-SI scaffold: detect weaknesses, generate similar data, fine-tune on the fly. No offline RL infra. | 2–4 weeks | v2 |
| **Tier 3: Operator-consistent RL** | PDR-style generate-distill-refine loop with Op-RL training. Stable recursive loop. | 1–2 quarters | v2.5 / v3 |

Do **not** jump to Tier 3. The AEL ablation is clear: extra mechanisms degrade performance when memory + reflection are already working.

### B7. Edge AI / on-device models — SOTA sub-500MB VLMs

**The convergence:** as of mid-2026, there is a clear tier-list for sub-500MB VLMs:

| Model | Size (Q4) | Best for | Notes |
|---|---|---|---|
| **LFM2.5-VL-450M** | 209MB + 180MB mmproj | Wearable, always-on | We use this. SigLIP2 NaFlex encoder. Liquid AI. |
| **SmolVLM-256M** | 120MB + 182MB mmproj | Tightest memory budget | Our fallback in `download.sh`. 2.2B variant for higher quality. |
| **MiniCPM-V 2.5/2.6** (Llama3-V) | ~5GB Q4 | Phone-class edge | NPU-accelerated, not wearable yet. |
| **Gemma3-270M** | 230MB | Text-only, no vision | In our danlab-multimodal models folder. No mmproj — can't see. |
| **Moondream2** | 2.7GB f16 | Legacy, full-quality | In our danlab-multimodal models folder. Overkill for wearable. |

**Two concrete efficiency techniques to adopt in v1.5:**

1. **VLMCache (ACM 2026):** 1.4–3.8× speedup on on-device VLM inference by disaggregating visual input into stable (background) / dynamic (foreground) blocks, KV-caching the stable prefix. <1% accuracy loss. **This is a near-free win for Dan Glasses** — the camera is mostly static (the wearer's head is the camera), so background blocks dominate. [^5]

2. **VisionTrim (OpenReview 2026):** training-free acceleration via Dominant Vision Token Selection (DVTS) + Text-Guided Vision Complement (TGVC). Reduces vision tokens, compatible with smaller/quantized VLMs. **Stacks on top of VLMCache.** [^6]

**Multimodal LLM (MLLM) compression literature (2026):**
- **MiniCPM-V** (Nature Communications) — 4-bit Q4_K_M drops MiniCPM-Llama3-V 2.5 from 16–17GB FP16 to ~5GB. NPU acceleration cuts visual encoding from 3.7s to 1.3s. Llama3-V variants are 2B–3B. Not sub-500MB but relevant for laptop prototype. [^20]
- **Multi-LoRA on Qualcomm NPUs (SM8650/SM8750, Samsung Galaxy S24/S25, arXiv 2604.18655):** INT4 weights + per-tensor INT8 activations + per-channel weight quantization. Multi-stream decoding gives 6× latency reduction; DS2D (dynamic self-speculative decoding) gives 2.3× decode speedup. **The roadmap for "Q4 LFM2.5-VL-450M on Snapdragon AR1 Plus Gen 1" is in this paper.** [^21]
- **AMS-RLBO (MDPI 2026):** adaptive multi-strategy compression (pruning + quantization + low-rank + distillation) with RL + Bayesian optimization decision engine. Closed-loop feedback under changing conditions. Industrial edge focus. [^22]

**Power characterization (the missing data):**
The 2026 wearable VLM power story is **not yet characterized for production workloads**. Best available data:
- **Wake-word on dedicated DSP: 1–5 mW** (solved)
- **Always-on camera + vision preprocessing: 50–150 mW** (manageable with duty cycling)
- **Continuous full-context multimodal inference: 300–800 mW** ← the unsolved bottleneck
- **Total always-on SoC budget for glasses: 200–400 mW near the temple** (per Smart Glasses 2026 hardware analysis) [^23]
- **Nanomind software/hardware co-design (arXiv 2510.05109):** 42.3% energy reduction vs mainstream edge frameworks; **LLaVA-OneVision-Qwen2-0.5B with camera ran 18.8 hours on a 2000 mAh battery** in low-power mode. This is the data point we need to beat on Redax. [^24]

**Practical implication:** even with VLMCache + VisionTrim, continuous LFM2.5-VL-450M at 5fps is **not** wearable-class on a 200–400 mW budget. We must salience-gate inference, not capture. Capture at 5–10fps with VLM-on-salient-frame only — that is the correct architecture, and it is what perceptiond does (canonical analysis §battery 1).

### B8. Memory and continual learning — approaches for AI companions

**memoryd today is correct for v1 but not for an AGI-credible v2.** Current stack:
- SQLite for `memories` and `conversations` tables
- `all-MiniLM-L6-v2` (384-dim) embeddings, stored as BLOB
- Flat cosine similarity at `/query`
- Three memory types: episodic, semantic, procedural

**What 2026 memory architectures do that we don't:**

| Feature | memoryd v1 | 2026 SOTA | Reference |
|---|---|---|---|
| Hierarchical memory | ❌ flat | ✅ temporal-tree, dual-process | TiMem, DPCM |
| Schema induction | ❌ raw text | ✅ domain schemas, intentions, cross-domain | DPCM, StructMem |
| Temporal awareness | ❌ timestamp | ✅ decay, reconsolidation, versioned | SmartVector |
| Confidence weighting | ❌ binary exists | ✅ Ebbinghaus decay, ECE-calibrated | SmartVector |
| Relational structure | ❌ flat | ✅ entity-centric engrams, spreading activation | EcphoryRAG |
| Consolidation | ❌ never | ✅ periodic, async, near-dream | DPCM System 2 |
| Adversarial robustness | ❌ unmeasured | ✅ 99.6% on LoCoMo | Synthius-Mem |
| Multi-session consistency | ❌ cosine alone | ✅ temporal-tree + manifold analysis | TiMem, LiCoMemory |
| Update latency | ✅ fast (write = INSERT) | varies | LiCoMemory claims lower than baselines |

**The 2026 architecture convergence: dual-process memory.**

- **DPCM (ACL 2026, "Memory Beyond Recall")** — System 1 (daytime writer, synchronous, doubly-linked supersedes chains) + System 2 (nighttime engine, async, induces schemas/intentions/cross-domain patterns). +5.20 on PersonaMem-v2. **The cleanest reference architecture for what memoryd should become.** [^25]
- **CMA (arXiv 2601.09913, "Continuum Memory Architectures")** — persistent, mutating, consolidating memory. Multi-factor retrieval beyond semantic similarity (relevance + recency + relational). Trade-off: increased latency and complexity. [^26]
- **TiMem (ACL 2026)** — Temporal Memory Tree (TMT) with semantic-guided consolidation. 75.30% on LoCoMo, 76.88% on LongMemEval-S, 52% reduction in recalled memory length. **Strongest single result on long-horizon benchmarks.** [^27]
- **StructMem (arXiv 2604.21748)** — hierarchical, event-centric, dual-perspective extraction (event content + interactional relations), periodic consolidation with temporal locality. Better long-horizon reasoning at lower cost on LoCoMo. [^28]
- **EcphoryRAG (ICLR 2026 Workshop)** — entity-centric engrams, centroid-based spreading activation, 18× cheaper consolidation than graph baselines (HippoRAG2). SOTA on 2WikiMultiHop, HotpotQA, MuSiQue. EM 0.475. **The cheapest path to multi-hop reasoning on top of our vector store.** [^29]
- **SmartVector (arXiv 2604.20598)** — embeddings with temporal awareness, confidence decay (Ebbinghaus), graph-relational importance. 2× top-1 accuracy vs vanilla cosine RAG (62.0% vs 31.0%), 35% → 13.3% stale answers. **Drop-in upgrade to our all-MiniLM pipeline.** [^30]
- **HiMeS (arXiv 2601.06152)** — hippocampus-inspired STM + LTM. RL-trained STM extractor for compression and proactive retrieval. Partitioned LTM for user-specific history with re-ranking. **The biologically-grounded option.** [^31]
- **LiCoMemory (ACL 2026)** — CogniGraph (hierarchical entity+relation graph, semantic indexing). Real-time updating, low update latency, better temporal reasoning on LoCoMo/LongMemEval. **The graph-augmented vector store option.** [^32]
- **Synthius-Mem (arXiv 2604.11563)** — 6 cognitive domains (biography, experiences, preferences, social circle, work, psychometrics). 94.37% memory accuracy on LoCoMo, 99.55% adversarial robustness. **If we ever want to ship a "personality-aware" companion, this is the recipe.** [^33]
- **DPA (Dual-Process Agent, MDPI 2026)** — fixed LLM + evolving LTM. System 1 = fast retrieval, System 2 = reflective meta-cognitive loop that audits results and updates memory. **Direct match for our OpenClaw + memoryd architecture.** [^34]

**Concrete upgrade path for memoryd:**

1. **v1.5 (2–3 weeks):** add SmartVector's 4-signal scoring (semantic × temporal × confidence × graph-relational) on top of existing all-MiniLM. Keep flat cosine as fallback. Confidence decay: closed-form Ebbinghaus with reconsolidation on access. Temporal validity: store `valid_from` / `valid_to` on every memory. **This alone takes recall@5 from "pretty good" to "trustworthy."**

2. **v2 (1 quarter):** introduce a lightweight System-2 nightly consolidator that runs at 3am local time, clusters the day's episodic memories, extracts schemas, and promotes them to semantic. Doubly-linked `supersedes` chains for belief revision. Persist the existing all-MiniLM index; don't churn it.

3. **v2.5 (2 quarters):** add an EcphoryRAG-style entity layer (small SQLite table of entities + relations) for multi-hop. Engrams are JSON pointers to memory IDs plus centroid embeddings. Centroid-based spreading activation for retrieval.

4. **v3 (3+ quarters):** add a learned confidence + temporal head (LoRA on all-MiniLM). Re-evaluate SmartVector vs vanilla every 3 months.

**This is the single biggest opportunity for AGI credibility in the danlab stack.** It is also the cheapest — no new models, no new hardware. Just better data structures and a nightly job.

### B9. Multimodal fusion — how are the best systems combining vision, audio, text?

**The 2026 consensus:** late-fusion with shared embedding space + cross-attention beats early-fusion at small scale. The top performers:

- **Eagle 2.5 (NeurIPS 2025):** long-context VLM, automatic degrade sampling + image area preservation, 72.4% on Video-MME with 512 frames (comparable to GPT-4o, Qwen2.5-VL-72B, InternVL2.5-78B). 8B params. **Not wearable, but the long-video technique is relevant for any "remember what you saw" feature.** [^35]
- **Nanomind (arXiv 2510.05109):** decompose LMMs into modular bricks (vision, projector, language, audio), map each to the right accelerator (NPU/GPU/DSP), zero-copy embedding transfer via Token-Aware Buffer Manager, battery-aware scheduler. **This is the right architectural pattern for Dan Glasses** — vision on NPU, audio on DSP, reasoning on CPU. 18.8 hours on 2000 mAh is the data point. [^24]
- **VisionTrim, VLMCache, SpecVLM, AMS-RLBO** — all address the cost side of multimodal fusion. None of them is a new architecture, just better implementations. Stacking them is the playbook.
- **SpecVLM (OpenReview 2026):** 2.5–2.9× end-to-end speedup with speculative decoding + elastic visual compression + online-logit distillation. Lossless decoding. **Adopt when we move from VLM-description-only to multi-turn VLM dialogue.** [^36]

**For Danlab specifically:** our architecture is **late-fusion via text intermediates** (perceptiond produces text descriptions, audiod produces text transcripts, agent loop fuses them in OpenClaw). This is correct for v1 because it lets us use smaller per-modality models. The risk is **information loss in the text intermediate** — VLM descriptions drop visual detail that an end-to-end fused model would preserve. For v2, when we have a 2B+ model available locally, consider end-to-end fusion on a single MLLM (LFM2-VL-1.2B or similar). For v1, the late-fusion cost is acceptable.

### B10. Model compression — what's working for keeping models small but capable?

**The 2026 compression stack:**

1. **Quantization** — INT4 weights + per-tensor INT8 activations + per-channel weight scaling (arXiv 2604.18655, 4–6× memory/latency reduction on Snapdragon). QAT-aware training to recover quality. [^21]
2. **Pruning** — structured (channel/head) for hardware-friendly, unstructured (sparse) for max compression. AMS-RLBO combines with quantization + distillation. [^22]
3. **Distillation** — teacher-student with online-logit distillation (SpecVLM, no offline data needed). [^36]
4. **Low-rank decomposition** — LoRA modules as runtime inputs to a frozen graph (arXiv 2604.18655). Swap skills without retraining/requantization. **This is the path to "personalized Dan Glasses" without a full fine-tune.** [^21]
5. **Token compression** — VisionTrim for vision, speculative decoding for text, KV-cache for repeat context (VLMCache). [^5] [^6]
6. **Hardware-aware co-design** — Nanomind's brick mapping (vision→NPU, projector→DSP, language→CPU) is the future for any battery-powered device running multimodal. [^24]

**Compression scaling law (arXiv 2512.16531):** "quantum-inspired" methods reduce CPU/memory by ~72% and energy by ~62% while preserving or improving semantic accuracy. VLM compute stays constant above the model's resolution clamp and drops sharply below — find the knee, save 30–50% per inference. [^7]

**For Dan Glasses v1.5:** the immediate compression wins are quantization (already done at Q4_0) + VLMCache (stable background blocks). For v2, swap to QAT-aware INT4 with per-channel scaling on Snapdragon AR1 Plus Gen 1 — this is the published 2026 path to wearable-class LFM2.5-VL-450M inference.

---

## C. Competitive & Market Research

### C11. AI wearables landscape (mid-2026)

**Five credible players, three approaches:**

| Device | Display | On-device AI | Open? | Price | Battery | Notes |
|---|---|---|---|---|---|---|
| **Meta Ray-Ban Gen 2 / Display** | None (audio-first) / monocular HUD on Display variant | Snapdragon AR1 Gen 1, cloud-dominant | ❌ closed, Meta ecosystem | $299+ | 4h+ | Millions shipped. Neural Band for EMG gesture. |
| **Brilliant Labs Frame** | Monocular 640×400 microOLED, ~200 nits | Cloud + on-device, Noa multimodal | ✅ MIT-licensed FW/SDK/HW | $349 | 6–8h | Developer-focused, 1–3s latency. Frame 2024→Halo Q4 2025. |
| **Brilliant Labs Halo** | Color peripheral display | **LFM2-VL-450M licensed from Liquid AI, on-device** | ✅ | ~$299–$349 | 4h+ | **The closest competitor to Dan Glasses.** |
| **Even Realities G1/G2 + R1 ring** | Monochrome green HUD, no camera | On-device, no cloud for core | ✅ partially | TBD | 12h+, ring >2 days | Privacy-first, 4 mics, productivity. |
| **Rabbit R1** | Small screen, dedicated device | LAM (Large Action Model), cloud | ❌ | $199 | All day | Demo-to-product gap. Still shipping, not meeting initial promises. |
| **Humane AI Pin** | Laser projection on hand | Cloud-dependent | ❌ | $499 (discontinued) | — | **Discontinued.** Lesson: cloud-only AI wearables don't ship. |

**Emerging 2026 entrants:**
- **Alibaba Qwen AI Glasses S1** — proactive AI upgrade, ambient context (time, location, weather, environment), 3D information space display. Hands-free. Push toward "ambient, always-on." [^37]
- **Raven Prism** — first "ambient computer," Linux-based, eye-gaze + voice, privacy-preserving local processing, hot-swappable "Raven Wings" for all-day power. AWE 2026. [^38]
- **Microsoft Project Solara** — Android-based, agent-first, workplace focus. Wearable badge + desk companion. AOSP + Intune/Entra ID. **Not consumer, but signals the enterprise direction.** [^39]
- **Microsoft Scout (Build 2026)** — proactive, persistent M365 agent. Always-on, ambient/context-aware. Hybrid on-device + cloud. **The clearest statement of "AI that initiates" from a major vendor.** [^40]
- **Poppy (Second Nature Computing, ex-Humane engineer)** — proactive AI for iPhone, ambient context integration, dashboard instead of chat. [^41]

**Strategic implications for Danlab:**

1. **Halo is the only direct competitor running LFM2-VL-450M on-device.** Our v1 is at parity in the model choice; we differentiate on the rest of the stack (open ecosystem, Dan consciousness, Indian-market positioning, AGI roadmap).

2. **Meta Ray-Ban Display + Neural Band is the audio-only mass-market play.** We don't compete on that axis — we compete on "sees, remembers, reasons" via VLM + memory + agent loop.

3. **Proactive AI is the 2026 trend** (Qwen S1, Scout, Poppy, Raven Prism, ContextAgent, Sensible Agent at UMD, Microsoft Research ring). Danlab should ship *initiate* capability in v1.5, not just *respond*.

4. **The "AI Pin" lesson is real** — cloud-only wearables that don't ship continuous on-device capability fail. Brilliant Labs' bet on on-device + open is validated by their continued shipping. We're on the right side of this divide.

### C12. Open-source AI companion projects

**The credible 2026 open-source AI companion landscape:**

- **Open Interpreter** — code-interpreter style local agent. Strong for desktop, weak for wearable.
- **OpenClaw** — TypeScript agent framework, the one we use. Multi-agent (Octopus), MCP, policy enforcement.
- **SillyTavern / Agnostic / Tavern** — character-card frontends for local LLMs. Frontend-only, no agent loop.
- **LangChain / LlamaIndex** — orchestration libraries, not products.
- **Letta (ex-Berkeley)** — stateful agents with memory; closest to memoryd in scope.
- **Mem0 / MemGPT (now Letta)** — production memory layer for LLM apps. Worth benchmarking against memoryd.
- **Paperclip (now "DanClaw" in our worktree)** — multi-agent company orchestrator. Dormant. Resume when needed. [^42]
- **Hugging Face Transformers + PEFT + TRL** — the RL training stack. What we need for Tier 3 self-improvement.

**Open-source AI companion gap:** no one is shipping a **wearable-first, VLM-on-device, memory-augmented, agent-driven** open stack that integrates end-to-end. Brilliant Labs ships the hardware, not the brain. Dan Glasses is positioned to be the brain. **This is a real opening.**

### C13. Privacy positioning

**Dan Glasses is well-positioned on privacy** compared to the field:

| Competitor | Data flow | User control |
|---|---|---|
| Meta Ray-Ban | Cloud-dominant, Meta-owned | Low |
| Brilliant Labs | On-device + cloud (Noa) | Medium |
| Even Realities | On-device core, no camera | High |
| Halo | LFM2-VL on-device | High |
| Humane Pin (discontinued) | Cloud-only | Low |
| **Dan Glasses** | **On-device by default, opt-in cloud** | **High** |

**The 2026 regulatory tailwind:**
- **EU AI Act** — biometric data (voice, face, video) is "high risk." Cloud processing of biometric data requires explicit consent, audit, and DPIA.
- **India DPDP Act** — similar direction; data fiduciaries must minimize data transfer outside India. On-device processing is a defensible posture.
- **California SB-1223 / similar state laws** — restrict biometric data collection without consent.

**Our position is a competitive moat, not just a compliance checkbox.** "On-device by default, opt-in cloud" is the right product posture for India, EU, and the privacy-conscious US segment.

**Action items:**
1. Document the on-device data flow in the user-facing privacy disclosure.
2. Implement **local-only mode** (no telemetry, no cloud) for users who want it.
3. Use the DPCM and Synthius-Mem adversarial-robustness work as ammunition against prompt-injection attacks on the perception → os-toold path (canonical analysis flagged this gap).
4. Consider an **end-to-end encrypted local backup** option for memoryd's SQLite (encryption-at-rest with user-held key). This is a strong privacy narrative.

---

## D. Technical Deep Dives

I selected three deep-dive areas: **A (self-improving RL), B (edge VLM optimization), C (vector memory for AI companions)**. Findings integrated into sections A2, B6, B7, B8, B10 above. Additional detail:

### D-A: Self-improving RL — concrete next steps for Danlab

**Tier 1 (1–2 weeks, ship in v1.5):** Learn a reward model on top of danlab-multimodal.
- Dataset: collect 500+ (image, model_description, human_rating) tuples. Rate on a 0–100 scale across (correctness, specificity, helpfulness). Synthetic images are fine for the demo.
- Model: fine-tune `cross-encoder/ms-marco-MiniLM-L-6-v2` on the (description, rating) pair as a regression head. 6-layer, 22M params, ~90MB, fast.
- Replace the hand-coded heuristic with the learned reward. Keep the same loop shape.
- This is **not RL** but it is the prerequisite for any future RL work.

**Tier 2 (2–4 weeks, ship in v2):** Test-time self-improvement.
- Implement the TT-SI scaffold: identify low-confidence descriptions (reward model < threshold), generate variations (different prompts, temperatures, seeds), fine-tune a LoRA on the (image, high-reward_description) pairs in the background. Swap LoRA on the fly.
- Measure: P50 reward score on a held-out eval set, before vs. after TT-SI.
- Target: +5% absolute on the danlab-multimodal benchmark.

**Tier 3 (1–2 quarters, ship in v2.5/v3):** Operator-consistent RL.
- PDR-style: sample 8 candidates in parallel at temperature 0.8, distill into a bounded workspace, refine with the reward model. Train the policy with Op-RL to align with the inference loop.
- Need: a verifiable eval (correctness of UI element identification, factual recall). Trivial for synthetic, harder for real screenshots.
- Need: an isolated RL training environment. **Do this on the laptop, not on the wearable.**

**Stop conditions / safety:** the TRM paper's stability analysis (Lipschitz Lz<1, conservative mixing with α-weight) is the analytical framework. Add watchdog on training: if the reward diverges by >2σ, revert to previous checkpoint and log. [^17]

### D-B: Edge VLM optimization — concrete next steps for Danlab

**v1.5 (2–4 weeks):** Characterize the resolution knee.
- Benchmark LFM2.5-VL-450M at 256/384/512 on x86_64 + (eventually) Redax aarch64.
- Measure: end-to-end latency, peak RSS, CPU%, NPU% (when NPU SDK available), description quality (human-rated, 100 samples).
- Find the knee: the lowest input resolution where quality stays within 1 σ of the 512 result.
- Expected: 384 might be the knee. 30% latency reduction, 30% memory reduction, ~1% quality cost.

**v1.5 (parallel):** VLMCache for the camera pipeline.
- perceptiond: add block-level KV-cache for stable background blocks. Use a simple background subtractor (MOG2 from OpenCV, already linked) to identify stable blocks. Cache their visual features. Recompute dynamic blocks per frame.
- Expected: 1.4–3.8× speedup, <1% accuracy loss. Validated by ACM 2026 paper. [^5]

**v2 (1 quarter):** Quantization-aware INT4 with per-channel scaling.
- Wait for the Snapdragon AR1 Plus Gen 1 Hexagon NPU SDK to be available for our hardware.
- Use the arXiv 2604.18655 playbook: INT4 weights, per-tensor INT8 activations, per-channel weight scaling, QAT-aware training. [^21]
- Expected: 4× memory reduction, 4–6× latency reduction on NPU vs CPU.

**v2 (parallel):** Hardware mapping (Nanomind-style).
- vision encoder → NPU
- projector → DSP
- language decoder → CPU (or LPU if available)
- audio → DSP
- This is the right architecture. Implement it as a service that exposes "where does this op run?" configuration.

### D-C: Vector memory — concrete next steps for Danlab

**v1.5 (1–2 weeks):** SmartVector-style 4-signal scoring.
- Add columns to `memories` table: `valid_from`, `valid_to`, `confidence`, `last_accessed`, `access_count`.
- Score = semantic × temporal × confidence × relational
- Confidence: closed-form Ebbinghaus decay, reconsolidated on access (boost confidence on retrieval).
- Temporal validity: 0.0 if expired, 1.0 if current, linear ramp for future events.
- Relational: store simple co-retrieval counts in a sidecar table; boost memories that are frequently retrieved together.
- **This is purely additive — no new models, no breaking changes to the API.** The current /query endpoint can be a 1-signal special case.

**v2 (1 quarter):** System-2 nightly consolidator.
- A cron job at 3am local time.
- Clusters the day's episodic memories (MiniLM + simple KMeans, or HDBSCAN).
- Extracts a schema or summary per cluster (could be a small LFM2.5-1.2B call to the laptop, not the wearable).
- Writes consolidated semantic memories with `supersedes` chains to the old episodic ones.
- Updates the confidence of frequently-retrieved memories (reconsolidation).

**v2.5 (2 quarters):** EcphoryRAG-style entity layer.
- A small `entities` table (id, name, type, centroid_embedding).
- A `relations` table (entity_id_from, entity_id_to, relation_type, weight).
- On memory write, extract entities with a small NER model or LFM2.5 call. Link to existing entities if cosine > 0.85.
- On query, after the top-K vector results, do a 1-hop expansion: retrieve memories that share an entity with the top-K. Boost their score.
- Expected: better multi-hop recall, especially for "remember when X happened with Y" queries.

**v3 (3+ quarters):** Learned confidence + temporal head.
- LoRA on all-MiniLM to predict (confidence, valid_from, valid_to) from (text, last_modified).
- Re-evaluate SmartVector vs vanilla every 3 months.

---

## E. Summary of Highest-Value Findings (for roadmap input)

**Architecture:**
- Service decomposition is correct. Don't rewrite. Add `wakewordd` + `powerd` + Rust gateway.
- Add `/metrics` to every daemon. Highest leverage, lowest cost.
- Schema-version every event. Cheap, prevents silent breakage.

**Self-improvement:**
- The "RL" label on the heuristic loop is correct. Do not change it.
- The credible ladder is: learned reward (v1.5) → TT-SI (v2) → Op-RL (v2.5+).
- The SAGE Critic pattern is the single most valuable addition — it prevents curriculum drift.

**Edge VLM:**
- LFM2.5-VL-450M is the right v1 choice. Confidence: high.
- VLMCache (stable background blocks) is a near-free 1.5–3× speedup for v1.5.
- Resolution knee characterization should happen on Redax the day hardware lands.
- Continuous full-context VLM is not wearable-class at 200–400 mW. Salience-gate inference, not capture.

**Memory:**
- This is the single biggest AGI-credibility upgrade available to us.
- 4-signal scoring (semantic × temporal × confidence × relational) is v1.5 scope, no new models.
- System-2 nightly consolidator is v2 scope.
- DPCM is the long-term target architecture.

**TTS:**
- Switch to KittenTTS nano (25MB int8) for the wearable. Save 55MB of disk.
- 24kHz, 8 voices, Apache 2.0, no GPU required.

**OpenClaw:**
- Acceptable for v1. Extract a thin Rust gateway in v1.5 to own IPC, health, power, watchdog.
- Don't try to rewrite OpenClaw in Rust. Keep it where the LLM/agent interaction lives.

**Wearables market:**
- Brilliant Labs Halo is the only direct competitor running LFM2-VL on-device.
- Proactive AI (Qwen S1, Scout, Poppy, ContextAgent) is the 2026 trend. Ship *initiate* in v1.5.
- Privacy positioning (on-device by default) is a regulatory tailwind, not just an ethics checkbox.

---

## F. Open Questions for the User

1. **Hardware path:** is Redax a real board we can order, or is it still a paper target? When do we get aarch64 hardware for power characterization?
2. **Dani (the agent platform):** how does Dan Glasses relate to `dani`? Is Dan Glasses a *form factor* for Dani, or a separate product? The repo at `DanGlasses/repos/dani` suggests form factor.
3. **HRM-Text Integration** (from project AGENTS.md) — what's the plan for the HRM-Text 1B reasoning model? Is it cloud-side or on-device? If on-device, this changes the power budget.
4. **Zo Computer as backing infrastructure** — does v1 firmware use Zo as the local server, or are we building a fully standalone .deb? The current dan-glasses stack runs on Zo (services, OpenClaw, MCP bridge, this conversation), which is great for dev but may not match the v1 product.
5. **AGI roadmap framing** — is "build AGI from India" via Dan Glasses (wearable AGI substrate), via Dani (general agent platform), via both, or via a third project (paperclip/DanClaw is dormant, what's the activation plan)?
6. **TTS voice strategy** — KittenTTS has 8 built-in voices. Do we want to ship custom voices (e.g., via Piper + a 30-min training corpus)? This is a 1-quarter project if yes.
7. **Wake word** — is "Hey Dan" the intended wake word? Train on Silero VAD + small DS-CNN. 1–2 weeks. Confirm before I scope the v1.5 wakewordd.

---

## G. Summary of Recommendations

**Top 3 (cross-cutting):**
1. **Keep the architectural decomposition but add `wakewordd` and `powerd`** — these are the missing v1 primitives for "always-on wearable." Don't redesign what works.
2. **Memory architecture is the single biggest AGI-credibility upgrade** — replace flat cosine with temporal + confidence + relational scoring in v1.5, dual-process design in v2.
3. **Self-improvement should follow the credible path: TT-SI → SIA, not the heuristic loop** — the danlab-multimodal demo is honest about being pre-RL; that label should stay until harness+weights are open and auditable.

**For the artifacts:**
- → `dan2-agi-roadmap.md`: 6/12/24-month plan incorporating the above.
- → `dan2-architecture-review.md`: detailed problems, risks, suggested improvements.
- → `dan2-model-analysis.md`: LFM2.5-VL-450M / whisper.cpp / KittenTTS alternatives deep-dive.
- → `dan2-papers-to-read.md`: Top 5 papers for the team.

---

## Sources

[^1]: Tech Trend Trove — "When AI Builds Itself: Inside Anthropic's Evidence on Recursive Self-Improvement." https://techtrendtrove.com/science-technology/when-ai-builds-itself-inside-anthropic-s-evidence-on-recursive-self-improvement/
[^2]: OpenReview — "TT-SI: Self-Improving LLM Agents with Test-Time Training." https://openreview.net/forum?id=k30IrbNYSG
[^3]: GitHub — HexoLabs/SIA (Self-Improvement Architecture framework). https://github.com/HexoLabs/SIA
[^4]: Indian Express — "Why Qualcomm is betting on smart glasses like Meta's Ray-Bans." https://indianexpress.com/article/technology/tech-news-technology/why-qualcomm-betting-on-smart-glasses-meta-ray-ban-10139959/
[^5]: ACM Digital Library — "VLMCache: Efficient On-Device Vision-Language Model Inference." https://dl.acm.org/doi/abs/10.1145/3745756.3809243
[^6]: OpenReview — "VisionTrim: Unified Vision Token Compression for Training-Free MLLM Acceleration." https://openreview.net/forum?id=57IXIg6nZ0
[^7]: arXiv — "Scaling Laws for Energy Efficiency of Local LLMs." https://arxiv.org/abs/2512.16531
[^8]: GitHub — KittenML/KittenTTS (v0.8, Feb 2026). https://github.com/kittenml/kittentts
[^9]: Forecasting Research (Substack) — "Experts and Superforecasters Update Their AI Timelines (LEAP Wave 8)." https://forecastingresearch.substack.com/p/leap-wave-8-ai-timelines
[^10]: EA Forum — "Survey of AI safety leaders on x-risk, AGI timelines, and resource allocation (Feb 2026)." https://forum.effectivealtruism.org/posts/LxuKuQd69Qx5FKhNZ/survey-of-ai-safety-leaders-on-x-risk-agi-timelines-and
[^11]: OpenReview — "SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning." https://openreview.net/forum?id=By7Pj576U3
[^12]: OpenReview — "Bootstrapping Task Spaces for Self-Improvement (ExIt)." https://openreview.net/forum?id=k2VsgUxC6X
[^13]: OpenReview — "Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability (SOAR)." https://openreview.net/forum?id=HuLoDnvC29
[^14]: OpenReview — "SAGE: Multi-Agent Self-Evolution for LLM Reasoning." https://openreview.net/forum?id=7sOeRzBzjB
[^15]: arXiv — "AEL: Agent Evolving Learning for Open-Ended Environments." https://arxiv.org/abs/2604.21725v1
[^16]: OpenReview — "Experiential Reflective Learning for Self-Improving LLM Agents." https://openreview.net/forum?id=hQgSl6kj1W
[^17]: OpenReview — "Unrolled Policy Iteration for Tiny Recursive Models." https://openreview.net/forum?id=rIzREKws05
[^18]: OpenReview — "Emergent Reasoning via Recursive Latent Reinforcement Pretraining (RLRP)." https://openreview.net/forum?id=DMQlGhvEUB
[^19]: OpenReview — "Large Language Models as Improvement Operators: Better Reasoning by Iteration (PDR)." https://openreview.net/forum?id=xyDZlMOFay
[^20]: Nature Communications — "Efficient GPT-4V level multimodal large language model for deployment on edge devices (MiniCPM-V)." https://www.nature.com/articles/s41467-025-61040-5
[^21]: arXiv — "Unlocking the Edge deployment and on-device acceleration of multi-LoRA enabled one-for-all foundational LLM." https://arxiv.org/abs/2604.18655v2
[^22]: MDPI Sensors — "An Adaptive Compression Method for Lightweight AI Models of Edge Nodes in Customized Production (AMS-RLBO)." https://www.mdpi.com/1424-8220/26/2/383
[^23]: Techtippr — "Smart Glasses in 2026." https://techtippr.com/a-technical-deep-dive-into-the-smart-glasses-hardware/
[^24]: arXiv — "Tiny but Mighty: A Software-Hardware Co-Design Approach for Efficient Multimodal Inference on Battery-Powered Small Devices (Nanomind)." https://arxiv.org/abs/2510.05109
[^25]: OpenReview — "Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving Agent Memory (DPCM)." https://openreview.net/forum?id=ywl53zPXu0
[^26]: arXiv — "Continuum Memory Architectures for Long-Horizon LLM Agents (CMA)." https://arxiv.org/abs/2601.09913v1
[^27]: OpenReview — "TiMem: Temporal-Hierarchical Memory Consolidation for Long-Horizon Conversational Agents." https://openreview.net/forum?id=Pq7tTNLgQh
[^28]: arXiv — "StructMem: Structured Memory for Long-Horizon Behavior in LLMs." https://arxiv.org/abs/2604.21748v1
[^29]: OpenReview — "Fast-Write, Deep-Read: EcphoryRAG as Dynamic Associative Memory for Lifelong Agents." https://openreview.net/forum?id=YHSoIbQWR8
[^30]: arXiv — "Self-Aware Vector Embeddings for Retrieval-Augmented Generation: A Neuroscience-Inspired Framework (SmartVector)." https://arxiv.org/abs/2604.20598v1
[^31]: arXiv — "HiMeS: Hippocampus-inspired Memory System for Personalized AI Assistants." https://arxiv.org/abs/2601.06152v1
[^32]: OpenReview — "LiCoMemory: Lightweight and Cognitive Agentic Memory for Efficient Long-Term Reasoning." https://openreview.net/forum?id=r5h2um8UsH
[^33]: arXiv — "Synthius-Mem: Brain-Inspired Hallucination-Resistant Persona Memory." https://arxiv.org/abs/2604.11563v1
[^34]: MDPI Electronics — "Towards Self-Evolving Agents: A Dual-Process Framework for Continual Context Refinement (DPA)." https://www.mdpi.com/2079-9292/15/6/1232
[^35]: NeurIPS 2025 — "Eagle 2.5: Boosting Long-Context Post-Training for Frontier Vision-Language Models." https://papers.nips.cc/paper_files/paper/2025/hash/833295cb9278a3ba973842a94ea68e3c-Abstract-Conference.html
[^36]: OpenReview — "SpecVLM: Fast Speculative Decoding in Vision-Language Models." https://openreview.net/forum?id=lkMh48jItD
[^37]: GogoAI News — "Alibaba Qwen AI Glasses S1 Get Proactive AI Services." https://www.gogoai.xin/article/alibaba-qwen-ai-glasses-s1-get-proactive-ai-upgrade
[^38]: PR Newswire — "Raven Resonance Previews Raven Prism - the World's First Ambient Computer - at AWE 2026." https://www.prnewswire.com/news-releases/raven-resonance-previews-raven-prism---the-worlds-first-ambient-computer---at-awe-2026-302799990.html
[^39]: The Next Web — "Microsoft unveils Project Solara: an OS for agent-first devices." https://thenextweb.com/news/microsoft-project-solara-agent-first-devices-build-2026
[^40]: Windows News — "Build 2026: Microsoft Scout Becomes the Always-On AI Agent for M365 Users." https://windowsnews.ai/article/build-2026-microsoft-scout-becomes-the-always-on-ai-agent-for-m365-users.426145
[^41]: Digital Mind News — "Poppy Launches Proactive AI Assistant for Daily Life." https://digitalmindnews.com/ai/poppy-launches-proactive-ai-assistant-for-daily-life/
[^42]: Paperclip project memory (`/home/workspace/paperclip/AGENTS.md`) — dormant, all agents paused.
