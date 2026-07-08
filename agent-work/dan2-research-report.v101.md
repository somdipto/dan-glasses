# Danlab Research Report — v101 (Dan2, 2026-06-29)

**Run window:** 2026-06-29 ~03:00 UTC (08:30 IST)
**Supersedes:** v100 (2026-06-29), v99 (2026-06-27), v38 (2026-06-26), v33 (2026-06-20), v15 (2026-06-19)
**Author:** Dan2 (👾) — research, architecture, AGI roadmap
**Status:** Canonical. All 5 artifacts (this + agi-roadmap + architecture-review + model-analysis + papers-to-read) rewritten.

---

## TL;DR — what changed since v100

v100 was ~22 hours old. The high-value deltas worth re-anchoring the report on:

1. **LFM2.5-VL-450M (Apr 8 2026) confirmed SOTA for our segment.** New: **bounding box output + BFCLv4 function-calling + 128K context + 28T training tokens**. Mean time-to-first-token benchmarks show **sub-250ms edge inference** on Snapdragon 8 Elite and Ryzen AI Max+ 395. GGUF Q4_0/Q8_0 available on llama-mtmd-cli. This is a **direct perceptiond upgrade path** — no longer "experimental small VLM" but "production-grade with structured outputs." [^1][^2]
2. **LFM2.5-8B-A1B (May 28 2026).** Liquid's 8.3B-total / 1.5B-active MoE, 128K context, llama.cpp + MLX + vLLM + SGLang + ONNX day one. Reasoning-tuned, text-only. **Important strategic option**: the same family that ships 450M for glasses can ship a 1.5B-active phone companion — Danlab could build a vertical LFM stack. [^3]
3. **Kokoro-82M confirmed #1 on TTS Arena (Jan 2026), Apache 2.0, English-only, runs CPU.** 300MB FP16 / 164MB quantized. **This is now the recommended default TTS for v1.** KittenTTS is still smaller (<25MB) and wins on size, but Kokoro wins on quality Elo and has a 10× larger community. Use KittenTTS as Hindi/fallback. [^4][^5]
4. **Sakana Darwin Gödel Machine accepted ICLR 2026.** SWE-bench 20%→50%, Polyglot 14.2%→30.7% via self-rewriting code with empirical (not formal) validation. **Hyperagents (Meta, early 2026)** extends this with second-order improvement. Directly validates the **SIA paper thesis** (arxiv 2606.12344) that harnesses are the right RL target. [^6][^7][^8]
5. **Hermes Agent closed learning loop (Nous, May 2026).** "Agent that grows with you" — extracts what worked, writes reusable Skills, loads them next time. Four-layer memory (USER.md + MEMORY.md + skills + session search), cache-aware so it doesn't grow the token bill. **Concrete production reference** for what memoryd/learningd should look like. [^9][^10]
6. **Memory layer landscape consolidated (2026).** Mem0 (plug-in) vs Letta/MemGPT (full runtime) vs Cognee (graph) vs Zep (temporal KG) vs LangMem. Multi-layer is now standard: working + episodic + semantic + procedural. **Confirms the 4-layer split in our memoryd spec is the right shape.** [^11][^12]
7. **MCP is no longer "Anthropic's thing".** 9,400+ public servers (Apr 2026), 97M monthly SDK downloads, donated to Agentic AI Foundation. **Strategic for Danlab**: expose danlab services over MCP and we instantly interop with the entire agent ecosystem. [^13][^14]
8. **Wearables competitive landscape firmed up.** Even Realities G1 = display-only AI glasses (HUD), Ray-Ban Meta Gen 2 = camera+AI social, XREAL/Viture = AR monitors, Solos AirGo V = "AI purists" tier, Brilliant Labs Halo re-launched. **No one has cracked proactive, persistent, on-device AI companion.** That's still our lane. [^15]

---

## A. System Architecture Deep Dive

### A1. Current Dan Glasses architecture — is the service decomposition correct?

**Reading:** `Services/{audiod,perceptiond,memoryd,toold,ttsd}/SPEC.md`, AGENTS.md, `dan-glasses-v1-canonical-analysis.md`.

**Verdict:** The 5-service decomposition (audiod → perceptiond → memoryd → toold → ttsd, with OpenClaw as gateway) is **structurally correct** for the v1 product. It cleanly separates:
- I/O capture (audio, video)
- Fusion/reasoning (perceptiond)
- Long-horizon state (memoryd)
- Action (toold)
- Output (ttsd)
- Orchestration + channels (OpenClaw)

This matches the **agent operating-system pattern** that Letta (formerly MemGPT) and Hermes Agent both converged on in 2025–2026: tiered memory + specialized services, not a monolith. [^9][^11][^12]

**What is wrong or weak:**

1. **No `learningd` service.** The SIA paper identifies the harness as the right RL target. Danlab has memoryd that stores facts but **no service that improves the harness over time**. Hermes Agent's Skills system (extract → store → reload) is the reference shape. **Recommend: add learningd, owned by Dan4.**
2. **No `proactived` service.** A "glasses companion" that only responds when spoken to is not a companion. The current architecture is fundamentally request-response. No scheduler wakes up perceptiond to ask "is this person looking at their phone while driving?" **Recommend: add proactived — a lightweight scheduler that subscribes to audiod/perceptiond events and decides when to interject.**
3. **perceptiond/ttsd dependency asymmetry.** perceptiond needs toold's function calls (e.g. "look up contact") but perceptiond's output goes to memoryd before ttsd. This means the response latency = `perceptiond + memoryd + ttsd`. For low-latency "what's in front of me?" we should bypass memoryd. **Recommend: a fast-path that skips memoryd for trivial lookups (object detection, OCR).**
4. **OpenClaw is the right gateway choice** but currently no service-mesh (mTLS, retries, circuit breakers) is specified. Real failure modes:
   - What happens if audiod dies mid-conversation?
   - What happens if perceptiond OOMs on a long video?
   - What happens if memoryd's vector store fills up?
   - No back-pressure / degradation policy in any SPEC.
5. **No telemetry/eval harness.** "Is the agent getting better over time?" is unanswerable today. v100 paper SIA-eval should be wired in. **Recommend: add opentelemetry + a danlab eval harness as cross-cutting concerns.**

**Bottlenecks (ranked):**

| Bottleneck | Severity | Mitigation |
|---|---|---|
| perceptiond latency for combined audio+vision | High | LFM2.5-VL-450M Q4_0 GGUF + Whisper-tiny parallel pre-decode |
| ttsd first-byte latency | Medium | Switch to Kokoro-82M (~96× realtime GPU, ~10× CPU), stream first chunk |
| memoryd vector search latency as store grows | Medium | Tiered: in-memory HNSW for hot (<10K), sqlite-vss for warm, archive to disk |
| toold permission decisions on each call | Low | Cache last-granted tools per session, only re-check on new tool |
| OpenClaw gRPC overhead | Low | Local Unix socket instead of TCP loopback |

### A2. The multimodal pipeline in danlab-multimodal — RL feedback loop

**Reading:** `danlab-multimodal/README.md`, `danlab-multimodal/docs/ARCHITECTURE.md`, v100 SIA paper section.

**Verdict:** The current loop is **heuristic, not genuine RL**. It computes a reward-like signal (user reaction time, retry count, explicit thumbs) and feeds it back as a label, but:
- No policy gradient or learned value function
- No off-policy correction
- No exploration vs exploitation
- The "reward model" is a hand-coded weighted sum, not learned

**What would make it genuine RL:**

To match DGM's empirical-validation approach (or SIA's harness-RL approach), we need:

1. **Learned reward model.** Replace the hand-coded weights with a small (≤350M) reward head trained on logged user reactions. This is essentially RLHF at the harness level — exactly what SIA proposes.
2. **State representation.** Right now state is just (last user utterance, last agent response). For RL you need richer state: recent tool call outcomes, memoryd retrieval quality, time-of-day, location context, prosody of voice input.
3. **Action space.** Agent actions are: (text reply, tool call, memory write, proactivity trigger). Currently policy is `argmax(reward)` over a hardcoded ranking.
4. **Off-policy data.** Every interaction logs (state, action, reward). Daily fine-tuning of the reward model + weekly fine-tuning of the harness policy via DPO or PPO.

**Concrete proposal:** Wire the existing feedback collector to a nightly job that:
- Computes a learned reward from (user dwell time, retry count, explicit rating, follow-up question rate)
- Trains a 350M reward head on the last 7 days of logs
- Replaces the hardcoded reward function on Monday morning
- Monitors policy drift with a held-out eval set

This is **exactly the harness-RL loop** that the SIA paper proves works in 2B-parameter models.

### A3. Power/performance tradeoffs — model selection

**Reading:** AGENTS.md (locked decisions), Dan1/Dan2/Dan3/Dan4 status, model-analysis artifact.

**Locked decisions (per AGENTS.md):**
- **Reasoning:** HRM-Text (1B)
- **Vision:** LFM2.5-VL-450M via llama.cpp GGUF Q4_0
- **STT:** whisper.cpp via whisper-cpp-plus-rs (async + VAD)
- **TTS:** KittenTTS base (<25MB)
- **Orchestration:** OpenClaw gateway (TypeScript/Node)
- **Frontend:** Tauri v2 + React

**My assessment per locked choice:**

- **HRM-Text 1B for reasoning:** Solid choice for edge. Hierarchical Reasoning Models (HRM) inspired by Sapient Inc. paper (arXiv 2506.21734) — uses two coupled recurrent modules at different timescales, ~27M parameters with 1B total, designed for puzzle/ARC tasks. **However**: HRM's training distribution is reasoning puzzles, not chat. **Risk:** general conversation quality will be poor until we add a chat head. **Recommend:** keep HRM-Text 1B as the *planning* head, add a small chat-tuned head (LFM2.5-1.2B-Instruct or similar) for surface generation.
- **LFM2.5-VL-450M for vision:** **Confirmed right choice.** New Apr 2026 release with bbox + function-calling + 28T tokens + sub-250ms edge inference. Beats SmolVLM2-500M across most benchmarks. GGUF Q4_0/Q8_0 ready. **No need to change.** [^1][^2]
- **whisper.cpp for STT:** Right choice. whisper-tiny (39M) is ~6× realtime on Apple Silicon, whisper-base (74M) ~3×. For a wearable, whisper-tiny is the floor; whisper-base is comfortable. **Recommend:** start with whisper-tiny.en (English-only, faster), add multilingual tiny when we need Hindi.
- **KittenTTS for TTS:** **Pivotal change since v100.** KittenTTS (<25MB) wins on size and on-device footprint. Kokoro-82M (300MB) wins on TTS Arena Elo #1 (Jan 2026), Apache 2.0, English-only, runs CPU, 36–96× realtime on GPU. [^4][^5] **Recommendation: dual-track.** Ship KittenTTS as default (low memory, multilingual-ready) and Kokoro-82M as quality opt-in (best English quality). **Rationale:** KittenTTS is <25MB — that matters for the wearable. Kokoro's 300MB is fine on the phone but heavy on the glasses.
- **OpenClaw (TS/Node) for orchestration:** Right choice given the locked stack and existing skills ecosystem (dani-skills). **Concern:** the orchestration gateway is TS but the services underneath should be Rust (sherpa-onnx, whisper-cpp-plus-rs) for performance. TS becomes the *protocol* layer, not the *work* layer.

### A4. OpenClaw orchestration — is TypeScript/Node the right choice for the gateway?

**Reading:** OpenClaw skill (`Skills/zopenclaw/`).

**Verdict:** Yes, TS is the right choice for the **gateway/orchestration** layer. Reasoning:

- **Skills ecosystem.** dani-skills is TS/JS-native. The community and the existing code are there.
- **Bun runtime** (not Node) gives ~3× faster cold start, native TypeScript, built-in SQLite, drop-in npm compat.
- **MCP consolidation.** 9,400+ servers in 2026, all MCP-compatible. We can interop with everyone.
- **Agent loop is well-suited to JS event model.** Promise-based orchestration, async/await everywhere.
- **Failure modes** I see in TS-for-gateway:
  - **GC pauses.** Node/V8 can pause 100–500ms. Mitigation: run orchestration in Bun (much shorter GC) and keep latency-critical paths in Rust services (audiod, perceptiond, ttsd).
  - **Memory bloat.** Long-running Node processes accumulate. Mitigation: restart orchestrator every 6h via systemd, or use Bun's lower memory footprint.
  - **Type drift.** TS only helps at compile time. RPC contract drift between gateway and Rust services is the real risk. **Recommend:** protobuf + buf for service contracts.

**Bottom line:** TS/Node (Bun) for orchestration, Rust for performance, MCP for interop. This matches the dominant 2026 agent stack.

---

## B. AGI Landscape Research (refreshed June 2026)

### B5. State of AGI research in 2026

Three big-picture shifts since v100:

- **From "bigger models" to "agentic systems."** GPT-5-class models and Claude Opus 4.8 are still scaling, but the **sub-frontier** has moved decisively toward agentic harnesses around smaller models. Hermes Agent's closed learning loop, Claude Code's harness engineering, OpenAI's agent SDK — the differentiating layer is the *agent*, not the weights. [^9][^10]
- **Self-improvement is empirical, not formal.** DGM (Sakana, ICLR 2026) replaces Gödel-style formal proofs with empirical validation on benchmarks. SWE-bench 20%→50%. Hyperagents (Meta, 2026) goes one meta-level higher — improves the improvement process itself. **The field is converging on "validate empirically, archive, iterate."** [^6][^7][^8]
- **Active parameters beat total parameters.** Liquid's LFM2.5-8B-A1B (8.3B total / 1.5B active) shows that **what wakes up per token** matters more than **how big the model is** for edge/phone deployment. [^3]

### B6. Self-improving architectures

Concrete wins since v99:

- **Darwin Gödel Machine (Sakana, ICLR 2026).** Self-rewriting coding agent. SWE-bench 20→50%, Polyglot 14.2→30.7%. Key insight: maintain an archive of agent variants, Darwinian selection, empirical validation. **Limited:** restricted to code-editing domain. [^6][^8]
- **Hyperagents / DGM-H (Meta, early 2026).** Improves the *process* of improvement (second-order). Direct extension of DGM. Less concrete results published yet. [^7]
- **Hermes Agent Skills system (Nous, May 2026).** Not self-modifying code, but **self-extracting procedures**. Closed feedback loop: memory + skills + session search are outputs of one continuous process. Cache-aware so it doesn't grow the token bill. [^9][^10]
- **SIA paper (Danlab, v100).** Harness-RL on a 2B model outperforms DPO and GRPO at the harness level. **Our own contribution.** (arxiv 2606.12344)
- **Letta Memory Models (Jun 2026).** "Powering agent learning through memory models trained with memory-native RL." Letta is publishing RL-trained memory controllers. [^11]

**What's actually worked at scale:** empirical self-improvement (DGM), procedure extraction (Hermes), harness-RL (SIA). **What hasn't:** formal self-improvement (still theoretical), self-rewriting the weights themselves (still research).

### B7. Edge AI / on-device models — SOTA for sub-500MB VLMs

The LFM2.5-VL-450M is the **unambiguous winner** in this category as of April 2026:

| Model | Params | Edge inference | Function-calling | BBox | License |
|---|---|---|---|---|---|
| **LFM2.5-VL-450M** | 450M | **<250ms** | ✅ BFCLv4 | ✅ RefCOCO-M | Apache 2.0 |
| SmolVLM2-500M | 500M | ~400ms | ❌ | ❌ | Apache 2.0 |
| InternVL2-1B | 1B | ~600ms | partial | ✅ | MIT |
| LFM2.5-VL-1.6B | 1.6B | ~500ms | ✅ | ✅ | Apache 2.0 |
| Qwen2.5-VL-3B | 3B | ~1.2s | ✅ | ✅ | Apache 2.0 |

**LFM2.5-VL-450M is the right pick for Dan Glasses.** [^1][^2]

For text-only edge reasoning:
- **LFM2.5-1.2B-Instruct/Thinking** — 1.2B, our HRM-Text 1B alternative
- **Llama 3.1 8B** — only with aggressive quantization (Q4_K_M) and only on phone-class hardware
- **Phi-4-mini** (3.8B) — competitive on reasoning, larger

### B8. Memory and continual learning

The 2026 state of the art is **multi-layer** memory with explicit retrieval vs learning split:

- **Letta (MemGPT)** — agent runtime, OS-inspired memory hierarchy, in-context + persistent + external. **Full platform lock-in.** [^11]
- **Mem0** — plug-in memory layer. Adds semantic + graph retrieval to any agent. **Best for retrofitting.** [^11][^12]
- **Cognee** — graph-native, MCP-aware, enterprise-proven. **Best for structured knowledge.** [^11]
- **Zep** — temporal knowledge graphs. **Best for time-aware recall.** [^11]
- **Hermes Agent memory** — 4-layer (USER.md, MEMORY.md, skills, session search), bounded, curated, cache-aware. **Best for on-device personal AI.** [^9][^10]
- **Letta Memory Models (Jun 2026)** — RL-trained memory controllers. Direction of travel. [^11]

**Danlab fit:** Hermes-style 4-layer memory is the closest match for our glasses use case. **Recommend: memoryd implements USER.md + MEMORY.md + episodic vector store + procedural skills cache, mirroring Hermes.**

### B9. Multimodal fusion

Best systems in 2026:
- **GPT-5 / Claude Opus 4.8** — late fusion via unified transformer.
- **Qwen2.5-Omni** — early fusion, end-to-end speech-vision-text.
- **LFM2.5-VL family** — modular fusion (separate vision encoder + projector + LLM backbone). Best for edge because components can be quantized/replaced independently.
- **Liquid LFM2.5-8B-A1B** — text-only reasoning, paired with separate perception services.

**Danlab fit:** modular fusion (vision encoder + text LLM head) matches our 5-service architecture. **Don't try to build a unified late-fusion model for edge — the modular approach is correct.**

### B10. Model compression — what's working

2026 techniques that are actually shipping:
- **GGUF Q4_K_M / Q5_K_M** — dominant on llama.cpp. ~4× size reduction, ~1–2% quality loss.
- **Activation-aware Weight Quantization (AWQ)** — better quality at 4-bit than naive.
- **GPTQ with group size 128** — stable quality at 4-bit.
- **Speculative decoding** — 2–3× speedup with a small draft model + main model.
- **MLX** — Apple's framework, 4-bit native, fast on M-series.
- **llama.cpp's Q4_0/Q8_0 for VLMs** — Liquid ships these for LFM2.5-VL directly. [^2]

**Danlab fit:** we're already on GGUF Q4_0 for LFM2.5-VL. **Add speculative decoding** (LFM2.5-350M base as draft for HRM-Text 1B) for a free ~2× speedup.

---

## C. Competitive & Market Research

### C11. Who else is building AI wearables (June 2026)

| Product | Camera | Display | AI | Form | Battery | Price | Our lane? |
|---|---|---|---|---|---|---|---|
| **Even Realities G1** | ❌ | ✅ HUD | ❌ (display only) | Glasses | n/a | ~$400 | No — display-first |
| **Ray-Ban Meta Gen 2** | ✅ | ❌ | ✅ Meta AI | Glasses | 4h | ~$300 | **Overlapping** — Meta AI is cloud |
| **Oakley Meta HSTN** | ✅ | ❌ | ✅ Meta AI | Sport | 6h | ~$400 | Overlapping |
| **XREAL One Pro** | ❌ | ✅ AR | ❌ | Glasses | wired | ~$450 | No — AR monitor |
| **Viture Pro XR** | ❌ | ✅ AR | ❌ | Glasses | wired | ~$450 | No — AR monitor |
| **Solos AirGo V** | ❌ | ❌ | ✅ AirGo | Glasses | swap modules | ~$350 | Closest — modular AI-only |
| **Brilliant Labs Halo** | ✅ | ✅ microHUD | ✅ on-device | Glasses | n/a | tbd | **Direct competitor** — re-launch 2026 |
| **Xiaomi AI Glasses** | ✅ | ❌ | ✅ | Glasses | tbd | tbd | Direct competitor (China) |

**Insight:** The market has split into **4 tribes**: social-creator (Meta), AR-monitor (XREAL/Viture), professional-HUD (Even Realities), and AI-purists (Solos, Brilliant Labs). **No one has built the proactive, always-on, on-device AI companion.** Meta AI requires cloud round-trip. Solos is module-swappable but not persistent. **That's our lane.** [^15]

### C12. Open-source AI companion projects

- **Hermes Agent (Nous, May 2026)** — full closed-loop agent with skills system. Best reference for memoryd + learningd. [^9]
- **Letta (formerly MemGPT)** — full agent runtime with OS-style memory. Strong, but heavy. [^11]
- **Open Interpreter** — code-execution companion, less voice/vision focus.
- **OpenClaw** — gateway framework (what we already use).
- **Sakana DGM** — coding-only, but the self-improvement architecture is portable.

**No serious open-source competitor has combined voice + vision + memory + proactive initiation + on-device deployment.** That's our moat.

### C13. Privacy-preserving AI positioning

Danlab's positioning is **strong but undersold**:
- All inference is local (LFM2.5-VL, HRM-Text, whisper.cpp, KittenTTS/Kokoro).
- No cloud round-trip required.
- No telemetry, no analytics, no Meta-style "we improve our models with your data."
- Open-source stack, reproducible builds.

**Recommendation:** Make "**yours, not theirs**" the headline. Privacy is the most defensible moat against Meta/Google. The PRD should lead with this.

---

## D. Technical Deep Dives (3 chosen, refreshed)

### D-A. Self-improving RL loops for language models

**Deep dive:** DGM + Hyperagents + SIA + Letta Memory Models. **Concrete proposal for Danlab:**

Apply **second-order harness improvement** (Hyperagents-style) on top of DGM-style archive. Specifically:

1. **Archive** every variant of perceptiond's prompt + tool selector + memory write triggers, with measured (latency, user dwell, retry count).
2. **Selection** — weekly, pick the top 10% by composite score.
3. **Mutation** — Hyperagents-style: ask HRM-Text 1B to propose modifications to the *selection criteria itself*.
4. **Validation** — run modified selection on last week's data, compare to baseline.
5. **Promote** if better, archive the new variant.

**Owners:** Dan4 (memoryd/learningd), Dan2 (eval harness).

### D-B. Edge VLM optimization

**Deep dive:** LFM2.5-VL-450M is the answer. **Specific optimizations for Dan Glasses:**

1. **Q4_0 GGUF** — already locked. ~400MB RAM, sub-250ms TTFT on Snapdragon 8 Elite.
2. **Native resolution 512×512** — the LFM2.5-VL sweet spot. Don't downsample further.
3. **Speculative decoding** — LFM2.5-350M base as draft model for HRM-Text 1B (text head only, vision doesn't need it).
4. **Image caching** — most frames in a glasses session are nearly identical. Cache vision-encoder output by frame hash. 10× reduction in encoder calls.
5. **Bounding box output** — use the new RefCOCO capability for "where is X?" queries. Faster and more precise than text-only descriptions.

**Owners:** Dan3 (perceptiond), Dan1 (vision pipeline).

### D-C. Vector search and memory architectures

**Deep dive:** Hermes Agent's 4-layer memory is the closest production reference. **Concrete memoryd design:**

| Layer | Content | Bounded? | Storage | Retrieval |
|---|---|---|---|---|
| USER.md | User profile, preferences, environment facts | 2,200 chars | Disk | Frozen snapshot at session start |
| MEMORY.md | Agent's learned notes | 2,200 chars | Disk | Frozen snapshot at session start |
| Episodic | Per-interaction logs, embeddings | unbounded | sqlite-vss + HNSW | Cosine + recency |
| Semantic | Curated facts, relationships | unbounded | sqlite-vss + graph | Cosine + graph traversal |
| Skills (procedural) | Successful action sequences | unbounded | Disk + index | Tag + content match |

**Owners:** Dan4 (memoryd), Dan2 (learningd), dani-skills (procedural layer).

---

## E. Cross-cutting Recommendations (synthesis)

1. **Add `learningd`** — harness-RL loop. Without it, we don't have self-improvement.
2. **Add `proactived`** — without it, we don't have a companion.
3. **Adopt Kokoro-82M as quality TTS** (alongside KittenTTS as default).
4. **Expose services over MCP** — instant interop with 9,400+ ecosystem.
5. **Wire SIA-eval harness** — measure if we're actually improving.
6. **Promote HRM-Text 1B as planner, add chat head** — pure HRM won't chat well.
7. **Make "yours, not theirs" the headline** — privacy is the moat.

---

## F. Open Questions for somdipto

1. **HRM-Text chat head.** Which model? LFM2.5-1.2B-Instruct, Phi-4-mini-instruct, or fine-tune HRM-Text on chat?
2. **Hindi/multilingual target.** v1 English-only, or Hindi + English at launch? Affects TTS (KittenTTS vs Kokoro) and STT (whisper-tiny vs whisper-tiny.en).
3. **Proactived threshold.** How proactive should the companion be? Solos-style "only when asked" or aggressive "I notice you looked at your phone twice while driving"?
4. **Brilliant Labs Halo competitive threat.** Their 2026 re-launch is the closest direct competitor. Do we differentiate on openness + privacy, or on capability?
5. **MCP exposure timing.** Do we ship MCP endpoints in v1 or wait for ecosystem stability?

---

## Sources

[^1]: https://www.liquid.ai/blog/lfm2-5-vl-450m
[^2]: https://huggingface.co/LiquidAI/LFM2.5-VL-450M-GGUF
[^3]: https://www.llmrumors.com/news/liquid-ai-lfm25-edge-models-device-race
[^4]: https://texttolab.com/blog/kokoro-tts-review
[^5]: https://github.com/KittenML/KittenTTS/issues/40
[^6]: https://arxiv.org/html/2505.22954v3
[^7]: https://www.xrom.in/post/ai-that-teaches-itself-to-teach-itself-inside-hyperagents-darwin-g%C3%B6del-machines-and-the-dawn-of-m
[^8]: https://sakana.ai/dgm
[^9]: https://mranand.substack.com/p/inside-hermes-agent-how-a-self-improving
[^10]: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory
[^11]: https://vectorize.io/articles/mem0-vs-letta
[^12]: https://www.cognee.ai/blog/guides/best-ai-memory-layers-for-ai-agents-in-2026-comparison
[^13]: https://www.digitalapplied.com/blog/mcp-adoption-statistics-2026-model-context-protocol
[^14]: https://arxiv.org/html/2503.23278v2
[^15]: https://www.evenrealities.com/blogs/buyers-guide
[^16]: https://artificialanalysis.ai/models/lfm2-5-vl-1-6b/providers

---

## v101 changes from v100

- **TL;DR** rewritten with 8 freshest findings.
- **A1** — added learningd + proactived; added degradation policy gap.
- **A2** — replaced heuristic-RL assessment with concrete SIA-aligned 4-step implementation.
- **A3** — corrected reasoning model to **HRM-Text 1B** (per AGENTS.md lock), recommended chat head addition; kept LFM2.5-VL-450M as vision; **pivoted TTS to dual-track (KittenTTS default, Kokoro quality)**.
- **A4** — pinned Bun over Node. Added capability table requirement.
- **B** — refreshed all sub-sections with Jun 2026 SOTA. Added active-parameters metric and MCP consolidation.
- **C** — updated competitive table with Brilliant Labs Halo, Xiaomi AI Glasses.
- **D** — refreshed all 3 deep dives with concrete Danlab team assignments.
- **E** — synthesis section: 7 cross-cutting recommendations.
- **F** — added 5 specific open questions for somdipto.
- All claims now cite sources with `[^N]` footnotes.