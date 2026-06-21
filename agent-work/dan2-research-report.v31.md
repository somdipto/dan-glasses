# Dan2 — Research Report (2026-06-14)
**Status:** Final v1
**Audience:** somdipto (decision-maker), Dan1/Dan3/Dan4 (peer architects)
**Scope:** Deep technical + AGI landscape research informing Danlab's 6/12/24-month roadmap

---

## 0. TL;DR (3 paragraphs)

The Danlab stack is in a **materially better position than the canonical PRD implies**. The daemons actually shipped (audiod v2.4 with real RFC 6455 WS, perceptiond v4 with salience-gated LFM2.5-VL-450M, memoryd v1 with all-MiniLM-L6-v2, ttsd with KittenTTS, toold, os-toold, openclaw-gateway + zo-mcp-bridge) and `danlab-multimodal` (SmolVLM-256M heuristic loop) is the on-CPU workhorse. The 106/106 green tests, 8/8 perceptiond, 32/32 memoryd+toold+ttsd, and 66/66 audiod make the **desktop prototype genuinely demo-ready**. The PRD is stale (e.g., "Rust microservices" — actually Python daemons in this host, which is fine for the prototype and not a blocker). The biggest gap is **wearable silicon characterization**, not software architecture.

The 2026 AGI landscape validates the self-improving agent bet. The Hexo Labs SIA framework (arXiv 2605.27276, May 2026, MIT, live) and the **Anthropic "Mythos" class + Microsoft "Autopilot" launch (June 2–9 2026)** both confirm that harness+weight self-improvement is now the SOTA primitive. Memory architecture research has converged: **Mem0 / Zep / Hindsight / DPCM / AEL / HeLa-Mem / vstash / SkillsVote / SkillOpt** are all open research threads. Edge AI has matured — **BitNet b1.58 2B4T (text, sub-1W), LFM2-VL-450M (vision, sub-250ms CPU), Litespark (1.58-bit SIMD, 18.15× speedup on Apple Silicon), OpenGlass (GAP9 + event camera, 11.8h on 200mAh)** — the **sub-1W wearable is achievable in 2026 (GAP9 + event cam) or 2027 (BitNet-VLM)**, not 2028+.

The 5-front competitive landscape (Microsoft Scout/OpenClaw GA Oct 2026, Anthropic Fable closed, Apple Siri AI iOS 27 GA Sept 2026 with 12GB gate, Brilliant Labs Halo shipping July 2026 with LFM2-VL on-device, Monako Glass Aug 2026 48g Linux) creates a **18-month shippable window** for Dan Glasses before Apple Glasses N50 (late 2027) consolidates the market. The bet: **ship the only local-first, open-source, memory-first, compliance-wedge wearable before Sept 2026 + open-source `memoryd v2` in the same window**. Anthropic SkillOpt + Microsoft SkillOpt both treat skill-document evolution as a first-class primitive — **Dan1/Dan2/Dan3/Dan4 ARE trainable parameters**.

---

## 1. State of the Danlab System (ground truth, June 14 2026)

### 1.1 What's actually shipped (verified)

| Component | State | Port | Tests |
|---|---|---|---|
| **audiod v2.4** | Running, RFC 6455 WS fixed, schema conformance | :8090 + WS :8091 | 66/66 ✅ |
| **perceptiond v4** | LFM2.5-VL-450M, salience-gated, /descriptions endpoint | :8092 | 8/8 ✅ |
| **memoryd v1** | FastAPI + aiosqlite + all-MiniLM-L6-v2 (384d), 3 types | :8741 | 11/11 ✅ |
| **toold v1** | Shell/python/exec_file, sandbox `/tmp/toold-sandbox` | :8742 | 15/15 ✅ |
| **ttsd v1** | KittenTTS medium, 8 expr voices, /speak + /play | :8743 | 6/6 ✅ |
| **os-toold v1** | Command execution with guardrails | :8744 | healthy ✅ |
| **openclaw-gateway** | :18789, Telegram channel, Zo MCP bridge | :18789 | live ✅ |
| **Tauri v2 frontend** | App.tsx + VisionDashboard + LiveTranscript + BootstrapWizard | — | vite clean ✅ |
| **Total** | | | **106/106 GREEN** |

### 1.2 What's stale in the canonical PRD

- **Language split**: PRD says "Rust microservices, IPC via Unix sockets" — actual stack is **Python daemons on TCP localhost ports** (Python is fine for prototype, but the PRD narrative around "Rust for safety" is wrong on the floor).
- **IPC transport**: PRD says "Unix socket or gRPC" — actually TCP loopback with FastAPI HTTP. Fine, but not what the PRD says.
- **Wearable silicon**: PRD still says "Redax aarch64" + "develop on x86_64 laptop" + "Redax board finalization TBD". Redax is a moving target.
- **Canonical doc claim** that "memoryd uses vectors in-process with optional Qdrant migration" — actually all-MiniLM-L6-v2 in SQLite BLOB, no Qdrant in production. The architecture claim is correct, but the in-code base is simpler.
- **`paperclip` repo dormant per AGENTS.md** — Dan1's prior runs show Paperclip is not the active Danlab deployment target. **DanClaw (the paperclip fork)** is the deployment story.

### 1.3 danlab-multimodal (the heuristic loop)

The `danlab-multimodal` project (SmolVLM-256M + llama.cpp + heuristic scoring) is **honestly framed**: README and ARCHITECTURE.md both call it "pre-RL scaffold, not RL." The scoring is hand-coded (length, error detection, content quality). This is correct — labeling it as RL in 2026 invites the "open-weight modification is not auditable" critique. The credible RL path is **SIA (Hexo Labs, MIT, May 2026)** — a self-improving loop where a Feedback-Agent updates both the harness and the model weights. We should fork SIA into `danlab-multimodal` rather than build a custom RL harness.

---

## 2. System Architecture Deep Dive

### 2.1 Is the service decomposition correct?

**Yes, with one important addition.** The 5-service decomposition (perceptiond, audiod, memoryd, toold, os-toold + openclaw-gateway) is **the right shape** for a desktop prototype. Each service has:
- Clear single responsibility
- HTTP health endpoint for liveness
- Event schema published via stdout + WebSocket (audiod) or ring buffer (perceptiond)
- Tests (66/8/11/15/6/0 = 106)
- Tauri Rust commands wrapping HTTP

**However:**
- **No watchdog**. If openclaw-gateway crashes, nothing restarts it. dan1.md acknowledges this. **Fix is 5 minutes** via `register_user_service` for all 7 daemons (audiod, perceptiond, memoryd, toold, ttsd, os-toold, openclaw-gateway) — this should be done **Week 1, not later**.
- **No latency budgets instrumented**. PRD has no p95 SLOs. audiod SPEC has 400–700ms end-to-end target; nothing else does.
- **No provenance for daemon events**. memoryd stores memories with `metadata.src="dan1"` but the chain audiod → memoryd → openclaw-gateway → Telegram has no event-tracing.
- **memoryd v1 is too weak for prod** — single embedding model (all-MiniLM-L6-v2), no temporal index, no skill consolidation, no proactive retrieval. This is the highest-ROI upgrade target.

**Service decomposition grade: B+.** Correct shape, missing supervision + provenance + the memoryd v2 upgrade.

### 2.2 The multimodal pipeline: heuristic loop → real RL?

The `danlab-multimodal` pipeline is honest about being a **heuristic loop, not RL**. The path to genuine RL is:

1. **SIA-H (harness-only)** — the Feedback-Agent rewrites the Meta-Agent's scaffold (tools, prompts, retry logic). Already validated by Hexo Labs on legal classification (+25%), GPU kernel speed (+12%), biological data denoising. **This is the right first step** because it requires no weight modification, no GPU budget, and is auditable.

2. **SIA-W+H (harness + weights)** — the Feedback-Agent also runs RL on the model's weights. Requires:
   - Per-user-isolated weights (privacy + safety)
   - Audit log of every weight delta
   - "Harness Updating Is Not Harness Benefit" caveat (arXiv 2605.30621) — the harness gain is not the same as the weight gain. Must train the focal model (1.2B) to load and follow its own harness, not use a 4.6B evolver.
   - LawBench 70.1% held-out target, TriMul 14.02× target (per SIA paper).

3. **PopuLoRA populations** (TrueSkill cross-eval) for `danlab-multimodal` — population-based LoRA instead of single-LoRA fine-tunes.

**Recommendation:** SIA-H fork for `danlab-multimodal` in **Month 1 (July 2026)**. 2-week experiment, single ML engineer, $0 compute beyond inference costs. The label "self-improving" is earned when (a) harness updates are logged, (b) weight updates are auditable, (c) both are independently reviewable. **Do not call it "RL" until all three hold.**

### 2.3 Power/performance tradeoffs — are the model choices right?

| Model | Current choice | Better alternative? | Verdict |
|---|---|---|---|
| **Vision** | LFM2.5-VL-450M Q4_0 (209MB) + mmproj F16 (180MB) via llama.cpp | **For wearable**: GAP9 + event camera (OpenGlass pattern, 11.8h on 200mAh) is the only sub-1W path. **For laptop**: LFM2.5-VL-450M is correct (sub-250ms, smallest working VLM with native GGUF). | **Keep for laptop, spike GAP9 for wearable in Month 1.** |
| **STT** | whisper.cpp base.en (74MB) via whisper-cpp-plus-rs | For edge: whisper-tiny (39MB) on Redax. For laptop: base.en is right. **Streaming whisper (150-300ms vs 400-700ms)** is a v3 upgrade. | **Keep.** Streaming whisper deferred to v3. |
| **TTS** | KittenTTS base (~25MB) via ONNX | **LFM2-Audio-1.5B** is a potential single-model end-to-end audio-language replacement for audiod+ttsd, but no public ONNX/GGUF yet. **Carry.** | **Keep.** LFM2-Audio spike Month 1. |
| **Embedding** | all-MiniLM-L6-v2 (384d) in memoryd | For long-term memory: Hindsight (91.4% LongMemEval with scale), SuperLocalMemory V3.3 (70.4% zero-LLM), Mem0, Zep. For personal agent: BGE-small-en, BGE-M3 (multilingual) | **Upgrade memoryd to memoryd v2 with Hindsight + Mem0 + Zep in Month 3.** |

**The 450M VLM power draw is the dominant event.** The canonical analysis (ARCHITECTURE-FLAWS-BEFORE-CODE.md) flags this correctly — FPS throttling is the wrong lever. **Salience-gated inference** (perceptiond v4 already does this) is the right lever. The PRD's "frame gate decision" (5-20ms) + "OCR 40-150ms" + "VLM 150-800ms" stack means a 2 FPS idle mode without salience-gating still fires VLM every 500ms. **Spike salience-CNN** (replace EMA + Haar cascade with a learned CNN) as a v5 perceptiond upgrade in Month 2.

### 2.4 OpenClaw orchestration — is TypeScript the right choice?

**Yes, but with caveats.** OpenClaw is the correct orchestration layer because:
- **Microsoft Scout is built on OpenClaw** (Build 2026, June 2). The compliance wedge is open-source on top of the same runtime. (Internal Microsoft documents leaked "addicted users" first-phase memo via 404 Media, June 4–9 2026.)
- **Anthropic SkillOpt + Microsoft SkillOpt** both treat skill-document evolution as a first-class primitive, and SkillOpt-style architectures are OpenClaw-native.
- **MCP server support** is now stable (openclaw 2026.6.5, 2026.5.26, 2026.5.28 — multiple production releases). zo-mcp-bridge is already wired.
- **Tailscale Serve bindings** (2026.5.31-beta.4) for gateway exposure, code-mode APIs, namespace-scoped sessions — the platform is hardening.
- **TypeScript** is correct for the agent framework. The services (perceptiond, audiod, memoryd) are Python for ML/hardware-access reasons. The split is fine.

**Caveats:**
- **No watchdog** on openclaw-gateway. Fix in 5 minutes via `register_user_service`.
- **No crash recovery / session resume from last checkpoint**. PRD Section 10.3 claims this exists; it doesn't in the current code.
- **No latency SLOs** for gateway response times.

**Don't rewrite OpenClaw in Rust.** The agent platform is the wrong place for a Rust rewrite. The compliance wedge (os-toold v2 with OWASP AIUC-1, OWASP Agentic AI Security Maturity Model v2.01, Agent 365, MXC) is the differentiator.

---

## 3. AGI Landscape Research (2026)

### 3.1 State of AGI research in 2026

**Key signal events in 2026 (chronological):**
- **May 2026** — AAAI 2025 Presidential Panel: 76% of respondents say **scaling current transformer approaches is unlikely to lead to AGI** (arXiv survey, AAAI.org report).
- **May 27 2026** — Hexo Labs releases SIA (arXiv 2605.27276), MIT, harness+weight self-improvement on legal/GPU/bio tasks.
- **May 31 2026** — LFM2.5-VL-450M released (Liquid AI, sub-250ms, 512×512, GGUF+ONNX).
- **June 2 2026** — Microsoft Build 2026: **Microsoft Scout** (always-on work agent, built on OpenClaw), Microsoft IQ (Work IQ GA June 16, Fabric IQ, Foundry IQ), Project Solara (MDEP Android, agent-first devices).
- **June 4–9 2026** — 404 Media leaks Microsoft internal "addicted users" memo for ClawPilot (Scout predecessor).
- **June 9 2026** — Anthropic releases **Fable 5 / Mythos class** (80.3% SWE-bench Pro, 50M-line Stripe migration in a day). Closed-source. Jack Clark publicly warns recursive self-improvement is "the likely next step."
- **June 11 2026** — MIT Tech Review: "Google DeepMind is worried about what happens when millions of agents start to interact" — $10M research fund.
- **June 14 2026** — Apple Siri AI iOS 27 dev beta (12GB RAM gate). Public GA Sept 2026.
- **METR Feb–Mar 2026 Frontier Risk Report** — internal agents had "means, motive, and opportunity" for rogue deployment across 5 frontier labs.

**The leading approaches:**
1. **Self-improving agents** (SIA, Meta-Harness, Darwin Gödel Machine, Hyperagents) — harness + weight co-evolution.
2. **Skill-document evolution** (SkillOpt, SkillsVote, SkillCompiler, CMM) — treating skill files as trainable parameters.
3. **Long-horizon memory** (Mem0, Zep, Hindsight, DPCM, AEL, HeLa-Mem) — the moat is the memory layer.
4. **Open-weight on-device** (BitNet b1.58, LFM2-VL, Litespark, OpenGlass) — the sub-1W wearable is now achievable.
5. **Compliance + governance** (Microsoft ACS, Agent 365, OWASP AIUC-1, MXC) — the regulatory wedge is wide open after Scout leak.
6. **Multimodal unified audio-language** (LFM2-Audio, Speaker-Reasoner, TEMPO) — single-model end-to-end STT+reasoning+TTS is on the horizon.

**Anthropic's brake-pedal plea** (May 2026) + **Microsoft Scout "addicted users" leak** (June 4–9) + **METR rogue deployment report** (Feb–Mar 2026) all point to the same conclusion: **the regulatory + governance window is open, and open-source is the only credible answer**. This is the Danlab wedge.

### 3.2 Self-improving architectures — what actually works?

| Approach | Status | Validated? | SOTA? |
|---|---|---|---|
| **Harness-only** (Meta-Harness, Darwin Gödel Machine) | Production | Yes (Meta-Harness: TerminalBench-2 #1, 7.7pp online text classification, 4.7pp math reasoning) | **Yes for open-source path.** |
| **Harness + weights** (SIA) | Research (May 2026) | Yes (legal +25%, kernel speed +12%, bio denoising) | **Yes if audit log + per-user-isolated weights.** |
| **Skill evolution** (SkillOpt, SkillsVote, CMM) | Research | Yes (SkillOpt: -63% tokens, -62% latency, -40% tool calls on SkillsBench) | **Yes. Treat Dan1/Dan2/Dan3/Dan4 as trainable.** |
| **Test-time training** (hand-written RL) | Production | Yes (RLHF, DPO, GRPO) | No — needs harness layer too. |
| **Memory-augmented** (MemGPT, Letta) | Production | Yes | **Yes for personal agents.** |
| **Continual learning** (PAM, RePro) | Research | Mixed (PAM internalizes memory, RePro matches MR-LoRA at lower cost) | **Useful for memory consolidation.** |

**SIA-H (harness-only) is the right starting point for Danlab.** Validated, low-cost, auditable. The SIA-W+H path is the second step.

### 3.3 Edge AI / on-device SOTA for sub-500MB VLMs (2026)

**Tier 1 (laptop/desktop, AC-powered):**
- **LFM2.5-VL-450M** (Liquid AI, May 2026) — 209MB Q4_0, sub-250ms CPU, SigLIP2 NaFlex encoder, 512×512, 32K context. **Best fit for desktop prototype.**
- **Gemma 4 12B Q4_K_M** — 8GB RAM, AC-powered, better quality. Alternative for laptop if compute allows.

**Tier 2 (wearable, sub-1W):**
- **GAP9 RISC-V + event camera (OpenGlass pattern, arXiv 2606.07431, June 2026)** — 11.8h on 200mAh, 78.3ms end-to-end gesture recognition. **The sub-1W wearable path for 2026.**
- **BitNet b1.58 2B4T** (Microsoft, text-only) — 0.4GB mem, 29ms latency, 0.028J energy, 9.2× lower than LLaMA 3.2 1B. **Text-only. No vision yet.**
- **Litespark 1.58-bit** (arXiv 2605.06485, May 2026) — SIMD kernels for ternary models, 18.15× speedup on Apple Silicon, 6.03× memory reduction. **For CPU-only edge.**

**Tier 3 (sub-2027 vision):**
- **BitNet-VLM** — does not exist yet. **2027 target.**
- **Hailo-10H / Hailo-15** — edge AI accelerator, ~$50 M.2 form factor, claims 13 TOPS. **Worth a $150–500 dev kit investment in Month 1.**

**Brilliant Labs Halo** (shipping July 2026, $349, Alif B1, Cortex-M55 + NPU, 14h battery) — the production reference for "open-source, open-hardware, on-device AI glasses." LFM2-VL-450M is in their stack. **Direct competitive overlap with Dan Glasses.**

**Monako Glass** (Aug 2026, 48g Linux, $399, ARM Cortex-A7 + 0.5 TOPS NPU, 300mAh = ~4h screen-on / 8h typical) — wearable Linux computer. **Production reference for 48g form factor with Linux.**

**OpenGlass (arXiv 2606.07431)** — academic reference for GAP9 + event camera, 11.5h on 200mAh, 78.3ms end-to-end. **The sub-1W research benchmark.**

### 3.4 Memory and continual learning (2026)

**Memory research has converged around 3 layers + dual-process:**

**Layer 1 — Token-level (episodic, fast recall):**
- MemGPT / Letta (virtual context management)
- MemoryWiki (markdown/JSONL on filesystem)

**Layer 2 — Representation (semantic, structured):**
- Mem0 (extraction + dedup + vector + graph)
- Zep (temporal knowledge graph)
- Hindsight (4-lever: World / Experience / Opinion / Observation; 91.4% LongMemEval at scale)
- SuperLocalMemory V3.3 (70.4% zero-LLM)
- DPCM (dual-process, daytime writer + nighttime engine; +5.20 on PersonaMem-v2)
- AEL (Thompson Sampling bandit + slow LLM reflection; +27% Sharpe)
- HeLa-Mem (Hebbian distillation, hub detection + spreading activation)
- vstash (IDF-weighted RRF fusion, +21.4% NDCG@10 on ArguAna)
- Decagon Proactive Agents (anticipate / remember / initiate; 93% DuetBench acceptance target)
- VisualMem (visual memory module, not caption-only)

**Layer 3 — Parameter (weight-level, internalized):**
- PAM / REMO (LoRA adapters internalize memory; LoCoMo benchmark)

**Cross-cutting:**
- SkillsVote (lifecycle governance of agent skills)
- SkillOpt (verifier-grounded compilation, -63% tokens)
- CMM (memory substrate, observed reasoning → SKILL.md graduation)
- SkillCompiler (cross-platform IR + safety enforcement, 94.8% proactive trigger)
- VisualMem (image-as-evidence, not caption)
- MemoryArena (long-horizon agent tasks, Mage +7.87-20.4pp)

**Tenure (precision-aware benchmark):** 89/89 cases, mean precision 1.0, sub-15ms retrieval. Local-first, multi-path BM25 with analyzer asymmetry, differential boosting, hard scope isolation. **The 2026 reference for high-precision memory retrieval.**

**For Dan Glasses, the memoryd v2 v1.0 stack should be: Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + LFM2.5-VL-450M (bbox-prompt JSON output) + Weaviate Engram.** This is the **6-core stack** in the dan2-agi-roadmap.md.

### 3.5 Multimodal fusion — how are the best systems combining vision, audio, text?

**2026 trends:**
- **Unified audio-language** (LFM2-Audio-1.5B) — single-model end-to-end STT + reasoning + TTS. Apache 2.0-equivalent. **Eliminates audiod + ttsd stack if quality holds.**
- **TEMPO** (OpenReview 2026) — atomic timestamp tokens, time-aware projector, Gaussian loss, GRPO. **State-of-the-art temporal grounding.**
- **Speaker-Reasoner** (OpenReview 2026) — iterative multi-turn temporal reasoning, speaker-attributed ASR, speaker-aware cache. **State-of-the-art multi-speaker.**
- **VLMCache** (ACM 2026) — 1.4–3.8× speedup for on-device VLM with block-level visual caching (stable background, dynamic foreground). **Directly applicable to Dan Glasses perceptiond.**
- **V5e-0** (OpenReview 2026) — self-speculative decoding for VLMs, 1.89× mean speedup across 15 VLMs, no vision encoder in drafter.
- **ViSpec / EAGLE-2** — speculative decoding for VLMs, 3.22× / 3.05-4.26× speedup.
- **MI-Pruner / QViD** — visual token pruning, training-free, query-aware.

**For Dan Glasses v2:** VLMCache (1.4-3.8× speedup with <1% accuracy loss) is the single highest-ROI upgrade. V5e-0-style self-speculative decoding is a v3 target.

### 3.6 Model compression — what works in 2026?

| Technique | Speedup | Memory | Status |
|---|---|---|---|
| **BitNet b1.58 2B4T** | 9.2× lower energy | 0.4GB | Text-only, ONNX + custom kernels. ENERZAi on QCS6490 Hexagon NPU. |
| **Litespark (1.58-bit SIMD)** | 18.15× (Apple Silicon), up to 95.81× (Intel/AMD) | 6.03× less | pip-installable, HuggingFace-compatible. |
| **VLMCache (visual KV cache)** | 1.4-3.8× | Same | Stable background, dynamic foreground. |
| **Gemma 4 QAT** | 72% VRAM reduction | 26B-A4B in 15GB | Google 2026. |
| **MiMo + TileRT (Xiaomi)** | 1000 tokens/sec | 1T params on commodity GPUs | Trillion-scale 1.58-bit. |
| **V5e-0 (VLM speculative)** | 1.89× mean | Same | No vision encoder in drafter. |
| **ViSpec / EAGLE-2** | 3.22× / 3.05-4.26× | Same | Speculative decoding for VLMs. |
| **BASTION** | 6.61× | Same | Tree-structured block diffusion, training-free. |

**Combined 50-150× VLM energy reduction path** is now on the table. For Dan Glasses wearable, **BitNet-VLM (2027) or GAP9 + event camera (2026)** is the sub-1W target.

---

## 4. Competitive & Market Research

### 4.1 AI Wearables landscape (June 2026)

| Player | Form | Silicon | Ship date | Price | Status |
|---|---|---|---|---|---|
| **Brilliant Labs Halo** | Glasses, 40g, 14h battery | Alif B1 (Cortex-M55 + NPU) | July 2026 | $349 | **Shipping. LFM2-VL on device. Open-source.** |
| **Monako Glass** | Glasses, 48g, Linux, 4h screen-on | ARM Cortex-A7 + 0.5 TOPS NPU | Aug 2026 | $399 | Preorder. MonoOS + Lua. |
| **OpenGlass (research)** | Glasses, 200mAh, 11.8h | GAP9 RISC-V + event camera (Prophesee GENX320) | arXiv June 2026 | N/A | Research. **Sub-1W reference.** |
| **Microsoft Scout** (Project Lobster) | Cloud agent, no hardware | Azure (MDEP) | Oct 2026 GA | TBD (M365 bundled) | OpenClaw-based. **Compliance wedge.** |
| **Microsoft Solara (badge)** | Badge wearable, touchscreen + 5G + cam | Qualcomm wearable SoC | TBD (pilots 2026) | TBD | Android MDEP. Enterprise. |
| **Apple Siri AI** | iPhone 17+ 12GB gate | Apple NPU | iOS 27 public GA Sept 2026 | TBD | 12GB hardware gate. |
| **Apple Glasses N50** | Glasses, no display, iPhone-companion | Apple Watch-class N401 chip | Late 2027 | $200-500 | Display glasses 2029. |
| **Apple Vision Air** | Lighter Vision Pro | TBD | 2028-2029 | TBD | R&D paused. |
| **Samsung Galaxy Glasses** | Audio-only, no display | TBD + Gemini cloud | Fall 2026 | $379-499 | Warby Parker + Gentle Monster frames. |
| **Google Gemini Glasses** | Fall 2026 | TBD + Gemini | Fall 2026 | TBD | Warby Parker + Gentle Monster. |
| **Rokid AI Glasses** | Glasses, 49g, dual-eye Micro-LED | TBD | Live (Australia June 2026) | AU$999 | Gemini + ChatGPT. |
| **Meta Ray-Ban** | Glasses | Snapdragon AR1 | Live | $299-499 | Capture + share. Reactive. |
| **Even Realities G1** | Glasses | TBD | Live | $599 | Display-only, no camera. |

**The 5-front competitive landscape in 2026:**
1. **Microsoft Scout** (cloud, OpenClaw-based, M365, Oct GA) — the always-on work agent.
2. **Anthropic Fable / Mythos** (cloud, closed, June 9 GA) — the dev tool.
3. **Apple Siri AI** (iOS 27, 12GB gate, Sept GA) — the consumer gate.
4. **Brilliant Labs Halo** (on-device, open-source, July 2026) — the open-source reference.
5. **Monako Glass** (Linux, 48g, Aug 2026) — the developer-wearable reference.

**Dan Glasses ship window:** **Aug 2026 – Q4 2027** before Apple Glasses N50 consolidates. 12-18 months.

### 4.2 Open-source AI companion projects (2026)

| Project | What it is | Local-first? | Maturity |
|---|---|---|---|
| **OpenClaw** | Agent framework | Yes (loopback by default) | Production (v2026.6.5) |
| **Daedalus (Shahzar07)** | Self-hosted AI agent, cross-session memory, self-authored skills | Yes | Learning artifact, v0.6+ |
| **Nexus-Memory** | Cross-agent memory (OpenClaw, Claude Code, Cursor, MCP) | Yes (SQLite + FTS5) | Production |
| **Amore (antonio-amore-akiki)** | Local-first memory backbone, Rust | Yes | v1.1.0 (2026-05-28) |
| **MemoryWiki** | Local-first memory wiki (Markdown/JSONL) | Yes | Production |
| **Mneme (Orvek-dev)** | Local-first memory runtime + eval harness | Yes (deterministic) | v1.0.0 target |
| **caveman (JuliusBrussee)** | Local-first AI assistant, OpenClaw gateway, cavemem | Yes | Production |
| **Candor AI** | Rust personal AI agent, Git-backed memory, wasmtime sandbox | Yes | v1.0.0 (2026-06-01) |
| **Mneme Memory Forge** | Rust memory layer for AI agents, MCP-native | Yes | Production |
| **VAINOM** | On-device AI companion, 3D brain UI, RActivating | Yes (8GB VRAM + 16GB RAM) | Public Beta v0.6 |
| **kausamemory-v2** | Encrypted SQLite memory, knowledge graph, IPFS backup | Yes | Production |
| **Paperclip (somdipto's fork: DanClaw)** | AI company orchestration | Cloud (Railway, Fly.io) | Production |
| **Blurr / Panda** | On-device Android AI agent, screen automation | No (Gemini cloud) | Production |
| **Dan Glasses** | Always-on wearable AI companion (vision + voice + memory) | Yes | Desktop prototype shipped |

**OpenClaw + memoryd v2 + open-source = the unique wedge.** Microsoft Scout runs on OpenClaw, so the compliance wedge is open-source on top of the same runtime. Most open-source companions lack the always-on vision + voice + memory integration. Blurr/Panda is closest competitor but is Android-only + cloud-dependent.

### 4.3 Privacy positioning

**Dan Glasses privacy principles (from SOUL.md):**
1. Privacy first — all data stays local unless explicitly shared
2. Salience over completeness — don't flood the user
3. Fail gracefully — degraded modes are better than dead
4. Build in the open — from India to the world

**Competitive privacy comparison:**
- **Apple Siri AI**: 12GB gate, on-device for many features, but iCloud-dependent for cross-device.
- **Brilliant Labs Halo**: low-res camera for AI inference, image discarded after inference, open-source for audit.
- **Monako Glass**: claims 0 data collection, on-device AI.
- **Meta Ray-Ban**: cloud capture + share, photo/video uploaded.
- **Microsoft Scout**: M365, governed by enterprise IT, cloud-resident.
- **Dan Glasses**: all data local, OpenClaw loopback by default, memoryd SQLite local.

**The privacy wedge is real and credible.** Open-source + local-first + memory-first is the only stack that satisfies:
- "All my data stays on my device" (Brilliant Labs does this, Dan Glasses does this)
- "I can audit the code" (Brilliant Labs open-source, Dan Glasses open-source)
- "I can run it without a cloud account" (Brilliant Labs + Noa cloud agent, Dan Glasses pure local)
- "Memory is first-class" (Dan Glasses memoryd is first-class service; Brilliant Labs Noa is cloud)

**Brilliant Labs Halo is the closest direct competitor. Differentiation:** Dan Glasses is open-source + on-device + memoryd + Telegram channel + Tauri frontend + Push-to-talk, vs. Brilliant Labs Halo ZephyrOS + Lua + Noa cloud agent. Dan Glasses is the developer/power-user version; Halo is the consumer version.

---

## 5. Technical Deep Dives

### Deep Dive 1: Self-improving RL loops for language models

**The state of the art (June 2026):**

1. **SIA (Hexo Labs, May 2026, arXiv 2605.27276)** — the reference framework. Two operating points:
   - **SIA-H (harness-only)**: Feedback-Agent rewrites the scaffold. Validated: +25% on legal classification, +12% on GPU kernel speed, biological data denoising.
   - **SIA-W+H (harness + weights)**: Feedback-Agent also runs RL on the focal model's weights. Validated: LawBench 70.1% held-out, TriMul 14.02×.
   - **Key insight** ("Harness Updating Is Not Harness Benefit", arXiv 2605.30621): the harness gain is not the same as the weight gain. Train the focal model (1.2B) to load and follow its own harness, not use a 4.6B evolver.

2. **Meta-Harness (OpenReview 2026)** — post-training reliable agent systems via harness search. Coding-agent proposer reads source + execution traces. TerminalBench-2 #1 (surpasses Terminus-KIRA on Claude Opus 4.6), 7.7pp on text classification, 4.7pp on math.

3. **AEL (Agent Evolving Learning, OpenReview 2026)** — two-timescale: Thompson Sampling bandit (fast) + LLM reflection (slow, diagnose-before-prescribe). +27% Sharpe on portfolio, +18% on support ticket routing.

4. **SkillsVote (OpenReview 2026)** — lifecycle governance: collection → recommendation → attribution → evolution. Online + offline transfer both improve Terminal-Bench 2.0 + SWE-Bench Pro.

5. **CMM (Cognitive Memory Manager, OpenReview 2026)** — observed reasoning → SKILL.md graduation. -61% agent messages, -71% files modified, -11 messages earlier root cause. Apache 2.0.

6. **SkillCompiler (OpenReview 2026)** — unified IR + safety enforcement. Claude Code 21.1% → 33.3%, Kimi CLI 35.1% → 48.7%. 94.8% proactive trigger rate for vulnerability detection.

7. **The Living Wiki (OpenReview 2026)** — schema-driven vault (CLAUDE.md) as persistent agent memory. 90.0% source hit rate at k=10 (vs 87.5% RAG). Obligation-framing reduces maintenance deferrals.

8. **HERO (Hindsight-Enhanced Reflection, OpenReview 2026)** — turn-level self-distillation from environment observations. Better than GRPO for limited-turn-budget multi-turn agents.

9. **PAM (Parameters as Agentic Memory, OpenReview 2026)** — LoRA internalizes memory. REMO data rewriting pipeline. LoCoMo benchmark, better temporal reasoning.

10. **TRACE (OpenReview 2026)** — capability-targeted training environments. +14.1 on τ 2-Bench customer service, +7 perfect scores on Tool-SandBox.

**The unified pattern:** self-improving agents have **at least 3 layers**:
- **Harness/scaffold** (SkillOpt, SkillsVote, CMM, Meta-Harness)
- **Memory** (Mem0, Zep, Hindsight, DPCM, AEL, HeLa-Mem)
- **Weights** (PAM, SIA-W+H, TRACE)

**For Danlab:**
- **Month 1**: Fork SIA-H into `danlab-multimodal`. 2-week experiment. Single ML engineer. Validate the +25% on a Dan Glasses-relevant benchmark.
- **Month 1**: Implement **Anthropic SkillOpt + Microsoft SkillOpt** integration for Dan1/Dan2/Dan3/Dan4 skill-document evolution. Treat as trainable parameters. **Both are now SOTA-validated as first-class primitives (Build 2026 June 2 + Fable 5 June 9).**
- **Month 3**: SIA-W+H spike. Build on SIA-H. Train the 1.2B focal model to load and follow its own harness. Per "Harness Updating Is Not Harness Benefit": don't use a 4.6B evolver.
- **Month 3**: PopuLoRA populations in `danlab-multimodal` (TrueSkill cross-eval).

**Don't call it "RL" until:**
- (a) Harness updates are logged
- (b) Weight updates are auditable
- (c) Both are independently reviewable

### Deep Dive 2: Edge VLM optimization (quantization, distillation, hardware acceleration)

**The 2026 stack:**

**Quantization:**
- **BitNet b1.58 2B4T** (Microsoft) — 0.4GB mem, 29ms latency, 0.028J energy, 9.2× lower than LLaMA 3.2 1B. **Text-only.** ONNX + custom 1.58-bit kernels. ENERZAi on QCS6490 Hexagon NPU. **The reference for sub-1W text inference.**
- **Litespark (arXiv 2605.06485)** — SIMD kernels for ternary models on Apple Silicon (18.15× speedup), Intel/AMD (up to 95.81×), 6.03× memory reduction. pip-installable, HuggingFace-compatible.
- **Gemma 4 QAT** (Google) — 72% VRAM reduction, 26B-A4B in 15GB.
- **LFM2.5-VL-450M Q4_0** (Liquid AI) — 209MB, sub-250ms CPU. **Best fit for laptop prototype.**

**Distillation:**
- **SpecVLM / V5e-0** — self-speculative decoding for VLMs. 1.89× mean speedup across 15 VLMs. No vision encoder in drafter.
- **ViSpec / EAGLE-2** — 3.22× / 3.05-4.26× speedup. Speculative decoding.
- **VLMCache (ACM 2026)** — 1.4-3.8× speedup, <1% accuracy loss. Block-level visual caching (stable background, dynamic foreground).
- **MI-Pruner** — visual token pruning via mutual information. Training-free.
- **QViD** — query-aware visual token pruning via low-rank structure. Training-free.
- **BASTION** — tree-structured block diffusion drafting, 6.61× speedup, training-free.

**Hardware acceleration:**
- **GAP9 RISC-V** (GreenWaves) + **Prophesee GENX320** event camera (OpenGlass, arXiv 2606.07431) — 11.8h on 200mAh, 78.3ms end-to-end, 83.94% accuracy. **Sub-1W reference.**
- **Alif B1 (Cortex-M55 + NPU)** — Brilliant Labs Halo, 14h battery, 40g. Production.
- **Hailo-10H / Hailo-15** — edge AI accelerator, ~$50 M.2, 13 TOPS. **Worth a $150-500 dev kit investment.**
- **Qualcomm QCS6490 Hexagon NPU** — ENERZAi BitNet deployment.
- **ARM Cortex-A7 + 0.5 TOPS NPU** (Monako Glass) — 4h screen-on / 8h typical.

**The path for Dan Glasses wearable:**
- **2026 (now)**: GAP9 RISC-V + event camera. **Sub-1W validated.** 11.8h on 200mAh.
- **2027**: BitNet-VLM (when it ships). 50-150× combined VLM energy reduction.
- **Defer**: BitNet b1.58 (text-only, no vision yet).

**For Dan Glasses laptop prototype:**
- **Keep LFM2.5-VL-450M Q4_0** — best fit.
- **Spike Gemma 4 12B Q4_K_M** in Month 1 — better quality, AC-powered.
- **Integrate VLMCache** in Month 2 — 1.4-3.8× speedup, <1% accuracy loss.
- **Integrate V5e-0 / ViSpec-style speculative decoding** in v3.

**For Dan Glasses wearable (when silicon is locked):**
- **Sub-1W target**: GAP9 + event camera (OpenGlass pattern).
- **Sub-1.5W target**: Hailo-15H + LFM2.5-VL-450M Q4_0.
- **Don't bet the wearable on Snapdragon-class** — 2-5W sustained is too much for 4h battery.

### Deep Dive 3: Vector search and memory architectures for AI companions

**The 2026 memory stack:**

**Production-grade open-source (in priority order):**

1. **Mem0** (arXiv 2504.19413) — extraction + dedup + vector + graph. **The reference production memory layer.** Add/dedup/update/search.

2. **Zep** (temporal knowledge graph) — production-grade, well-documented, multiple integrations.

3. **Hindsight** — 4-lever memory (World / Experience / Opinion / Observation), 91.4% LongMemEval at scale.

4. **SuperLocalMemory V3.3** — 70.4% LongMemEval zero-LLM. **Best zero-LLM target.**

5. **DPCM (Dual-Process Cognitive Memory)** — System 1 daytime writer (synchronous, doubly linked superseded chains) + System 2 nighttime engine (asynchronous, schema induction). +5.20 on PersonaMem-v2.

6. **AEL (Agent Evolving Learning)** — Thompson Sampling bandit + LLM reflection. +27% Sharpe on portfolio, +18% on support tickets.

7. **HeLa-Mem** — Hebbian distillation. Hub detection + spreading activation + dual-path retrieval. (Reference: OWC dist in SkillOpt + SkillsVote lineage.)

8. **vstash** — IDF-weighted RRF fusion. +21.4% NDCG@10 on ArguAna.

9. **Decagon Proactive Agents** — "anticipate / remember / initiate" behavior. 93% DuetBench acceptance target.

10. **VisualMem (arXiv 2605.28806)** — visual memory module (not caption-only). Image + text. Plug-and-play with Mem0/memos.

11. **Cognee** — graph+vector+relational hybrid, 14 retrieval modes, in production at Bayer/Knowunity. **Self-improving "cognify" pipeline.**

12. **Tenure** — 89/89 cases, mean precision 1.0, sub-15ms retrieval. Multi-path BM25 with analyzer asymmetry, differential boosting, hard scope isolation. **Precision-aware benchmark reference.**

13. **TencentDB Agent Memory** (OpenClaw plugin, May 2026, MIT) — 4-tier progressive memory pipeline.

14. **LightGMEM** — GLiNER2 (zero-shot NER) + conflict-lane partitioning + Ego-Splitting. 58× fewer LLM calls, 151.6× faster than Zep on LoCoMo. Best 8 of 12 QA metrics.

15. **GRAM** — actively managed graph-structured memory via GRPO RL. Trained small LMs (<4B) for memory governance.

16. **GraP-Mem** — Plan Agent + Integration Agent, multi-granularity (compact + source context). F1 + BLEU on LoCoMo and NarrativeQA.

**Benchmarks (2026):**
- **LongMemEval** — long-term memory evaluation, multiple variants
- **LoCoMo** — long-conversation memory
- **PersonaMem / PersonaMem-v2** — persona + cross-session
- **MemoryArena** — long-horizon agent tasks
- **EMemBench** — episodic memory for VLM agents
- **Tenure's PrecisionMemBench** — 89 cases, retrieval precision
- **Locomo** — long conversation
- **DUAL-Bench** — over-refusal in VLMs
- **LongBench** — long-context evaluation
- **Needle-in-a-Haystack** — long-context retrieval

**For Dan Glasses memoryd v2 v1.0 (6-core stack):**
- **Mem0** + **Zep** + **Hindsight** + **SuperLocalMemory V3.3** + **LFM2.5-VL-450M (bbox-prompt JSON output)** + **Weaviate Engram**
- 12-16 weeks, 1 ML engineer, $0 compute
- **Open-source release target: September 2026** (before Apple Siri AI GA)

**For Dan Glasses memoryd v2 v2.0 (11-component stack):**
- **+ AEL + vstash + HeLa-Mem + Decagon Proactive + VisualMem**
- Target: December 2026 (before Microsoft Scout GA)

**For Dan Glasses memoryd v2 v3.0 (HMO + 3-tier):**
- **+ HMO (3-tier: Primary Cache + Secondary + Archive)**
- **+ CraniMem (Bayesian-credible-region memory)**
- **+ Memora + APEX-MEM (skill memory)**
- **+ Meta-Harness + TRACE (capability-targeted training)**
- Target: Q4 2027 – Q1 2028

**Open-source release dates:**
- **memoryd v2 v1.0 (6-core)**: September 2026
- **memoryd v2 v2.0 (11-component)**: December 2026
- **memoryd v2 v3.0 (HMO + 3-tier)**: Q4 2027 – Q1 2028

**Don't service-ize memoryd v2 prematurely.** One process with 3 internal modules (ingest / retrieve / consolidate). Split only if profiling proves the bottleneck at 10K+ memories / 10K+ queries / day.

---

## 6. Top Recommendations (summary)

See `dan2-agi-roadmap.md` for the full 24-month plan. Key recommendations:

1. **memoryd v2 v1.0 open-source release in September 2026** — the single highest-ROI investment. Wedge against Apple Siri AI GA (Sept 2026) + Microsoft Scout GA (Oct 2026). 6-core stack, 12-16 weeks, 1 ML engineer, $0 compute.
2. **Sub-1W wearable path measurement in Month 1** — $150-500 in dev kits (GAP9 + Hailo-15H + LFM2.5-VL-450M). The 2026 wearable path is GAP9 + event camera (OpenGlass, arXiv 2606.07431) or wait for BitNet-VLM in 2027.
3. **SIA-H fork in Month 1** — 2-week experiment, treat `danlab-multimodal` as the SIA test bed. Open-source the fork. Don't call it "RL" until harness+weights are both auditable.
4. **Compliance wedge with os-toold v2 in Month 3** — OWASP AIUC-1 + OWASP Agentic AI Security Maturity Model v2.01 + Microsoft Agent 365 + MXC + Apple Core AI. Microsoft Scout runs on OpenClaw; we are the open-source compliance wedge on the same runtime.
5. **Form factor decision tree in Month 1** — measure LFM2.5-VL-450M on a Hailo-10H M.2 + RPi 5 reference. Pick the form factor (Redax vs Monako Glass vs Brilliant Labs Halo vs Project Solara MDEP) by end of Month 1. Lock by end of Month 3.

**Anti-recommendations:**
- Don't rewrite OpenClaw in Rust.
- Don't call it "RL" until the harness+weight modification is open and auditable.
- Don't run weight updates in v1.
- Don't service-ize memoryd v2 prematurely.
- Don't try to LoRA-tune the user's brain model in v1.
- Don't pick a wearable silicon path without measuring it.
- Don't bet the wearable on Snapdragon-class silicon.
- Don't put OpenClaw on the wearable. Run it in the user's EigenCloud container (or laptop).
- Don't ship a 1-bit VLM (BitNet b1.58 is text-only).
- Don't keep the canonical PRD as the source of truth.

---

## 7. Open Questions for somdipto

1. **What is the target battery life for v1 wearable?** PRD says 4h; canonical says 6h. OpenGlass is 11.5h on 200mAh. Monako Glass is 4h screen-on / 8h typical. Brilliant Labs Halo is 14h. Need a number.
2. **What is the target weight for v1 wearable?** PRD says <50g target, <80g minimum. Monako Glass 48g. Brilliant Labs Halo 40g. OpenGlass 200mAh reference is much lighter. Need a number.
3. **What is the target BOM for v1 wearable?** PRD says $99-149. That excludes the VLM accelerator. Hailo-10H M.2 is ~$50. Brilliant Labs Halo is $349. Monako Glass is $399. Need a BOM.
4. **What is the v1 distribution model?** EigenCloud container (canonical) vs. local-only (no cloud) vs. hybrid? The decision shapes os-toold and memoryd's threat model.
5. **Who is the v1 user?** Technical early adopter, productivity knowledge worker, accessibility-first? The PRD says "all three." Pick one.
6. **What is the v1 success metric?** "100K+ MAU on desktop companion" is 18 months out. What's the v1 demo-ready metric (Week 4)?
7. **What is the v1 ship date?** "Late 2027" is the wearable. What's the desktop prototype ship date?
8. **Do we open-source the danlab-multimodal heuristic loop now or wait for SIA-H fork?** PRD is unclear. Recommend open-source now with explicit "pre-RL scaffold" framing, then iterate.
9. **Is OpenClaw the long-term gateway, or do we migrate to EigenCloud container for the wearable?** The PRD says EigenCloud. The actual stack runs openclaw-gateway on loopback. Reconcile.
10. **Do we open-source Dan Glasses desktop companion now, or wait until wearable ships?** Brilliant Labs Halo is open-source from day 1. The wedge is stronger if we open-source now.

---

## 8. Sources

### Foundational papers (SIA, self-improving agents)
- SIA: Self Improving AI with Harness & Weight Updates (arXiv 2605.27276, May 2026) [^1]
- Harness Updating Is Not Harness Benefit (arXiv 2605.30621) [^2]
- Meta-Harness: Post-Training Reliable Agent Systems via Harness Search [^3]
- AEL: Agent Evolving Learning [^4]
- SkillOpt: Trajectory-Derived, Verifier-Grounded Compilation of LLM-Agent Skills [^5]
- SkillsVote: Lifecycle Governance of Agent Skills [^6]
- Cognitive Memory Manager (CMM) [^7]
- SkillCompiler [^8]
- The Living Wiki [^9]
- HERO: Hindsight-Enhanced Reflection [^10]
- PAM: Parameters as Agentic Memory [^11]
- TRACE: Capability-Targeted Agentic Training [^12]
- Federation over Text (FoT) [^13]
- Agent Harness Engineering: A Survey [^14]
- They Are Not Static: A Survey of Dynamic Agent Skills [^15]
- LLM Agent Memory: A Survey from a Unified Representation [^16]

### Memory architectures
- Mem0 (arXiv 2504.19413) [^17]
- VisualMem: Personal Visual Memory from Explicit and Implicit Evidence (arXiv 2605.28806) [^18]
- Memory Beyond Recall: DPCM [^19]
- LightGMEM [^20]
- GRAM [^21]
- GraP-Mem [^22]
- Deployment-Time Memorization in Foundation-Model Agents [^23]
- EMemBench [^24]
- Tenure: Structured Belief State and PrecisionMemBench (arXiv 2605.11325) [^25]
- Mage: Memory as Execution State Management (arXiv 2606.06090) [^26]
- The Long Arc of Audio: A Comprehensive Survey of Long-Context SLMs [^27]
- Personal Visual Memory from Explicit and Implicit Evidence (arXiv 2605.28806) [^18]

### Edge AI / on-device
- LFM2.5-VL-450M (Liquid AI, May 2026) [^28]
- BitNet b1.58 — ENERZAi on QCS6490 Hexagon [^29]
- Litespark Inference for CPUs (arXiv 2605.06485) [^30]
- VLMCache (ACM 2026) [^31]
- V5e-0: Self-Speculative Decoding for VLMs [^32]
- BASTION: Tree-Structured Block Diffusion [^33]
- MineDraft: Batch Parallel Speculative Decoding [^34]
- TISA: Exploiting Temporal Locality [^35]
- MI-Pruner [^36]
- QViD [^37]
- R-APS: Reflective Adversarial Pareto Search [^38]
- EndoRISC-V [^39]
- SvelteF3M-YOLO [^40]
- Spiking CNNs for traffic signs [^41]

### Wearable / smart glasses
- OpenGlass: Smart Glasses for On-Device Event-Based Gesture Recognition (arXiv 2606.07431) [^42]
- Brilliant Labs Halo [^43]
- Monako Glass [^44]
- Apple Glasses N50 (Late 2027) [^45]
- Microsoft Scout at Build 2026 (June 2) [^46]
- Microsoft Work IQ (GA June 16, 2026) [^47]
- Microsoft Project Solara (Build 2026) [^48]
- Google Gemini Glasses Fall 2026 [^49]
- Samsung Galaxy Glasses [^50]
- Rokid AI Smart Glasses [^51]
- Apple Siri AI 12GB gate (iOS 27 Sept 2026) [^52]
- Microsoft Scout "addicted users" memo leak [^53]
- METR Frontier Risk Report (Feb-Mar 2026) [^54]
- MIT Tech Review: DeepMind worried about millions of agents [^55]

### OpenClaw + agent platform
- openclaw 2026.6.5 release [^56]
- openclaw 2026.5.26 [^57]
- openclaw 2026.5.28 [^58]
- openclaw-node 0.11.0 [^59]
- kriptoburak/openclaw-mcp-adapter [^60]

### Audio / TTS
- BareWave [^61]
- Speaker-Reasoner [^62]
- TEMPO [^63]
- The Long Arc of Audio [^27]

### Open-source AI companion projects
- Daedalus (Shahzar07) [^64]
- Nexus-Memory (bozoinc) [^65]
- Amore (antonio-amore-akiki) [^66]
- MemoryWiki [^67]
- Mneme (Orvek-dev) [^68]
- caveman (JuliusBrussee) [^69]
- Candor AI [^70]
- Mneme Memory Forge [^71]
- VAINOM [^72]
- kausamemory-v2 [^73]
- Blurr / Panda [^74]
- Brilliant Labs Halo (Halo) [^43]

### Existing Danlab system
- dan-glasses/PRD.md
- dan-glasses/AGENTS.md
- dan-glasses/SOUL.md
- dan-glasses/docs/dan-glasses-build-plan.md
- dan-glasses/docs/dan-glasses-v1-canonical-analysis.md
- dan-glasses/agent-work/ARCHITECTURE-FLAWS-BEFORE-CODE.md
- dan-glasses/agent-work/dan1.md (DAN-1: foundation stream, 106/106 tests green)
- dan-glasses/agent-work/dan2.md (audiod v2.4, 66/66 tests)
- dan-glasses/agent-work/dan3.md (perceptiond v4, 8/8 tests)
- dan-glasses/agent-work/dan4.md (memoryd+toold+ttsd, 32/32 tests)
- dan-glasses/Services/{audiod,perceptiond,memoryd,toold,ttsd,os-toold}/SPEC.md
- danlab-multimodal/README.md
- danlab-multimodal/docs/ARCHITECTURE.md
- paperclip/README.md (DanClaw fork)
- blurr/README.md

### Anthropic + Microsoft
- Anthropic Fable 5 / Mythos (June 9, 2026) [^75]
- Anthropic "brake pedal" plea [^76]
- Microsoft SkillOpt (Build 2026) [^77]
- Anthropic SkillOpt (with Fable 5) [^78]
- MIT Tech Review: AI accelerating AI research [^79]

---

*Research complete. Ready to write the AGI roadmap, architecture review, model analysis, and papers-to-read artifacts.*
