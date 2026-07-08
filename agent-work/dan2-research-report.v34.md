# Danlab Research Report — Dan2 (2026-06-21)

> **Scope.** Deep system review of the Danlab ecosystem (Dan Glasses, danlab-multimodal, paperclip, blurr) and a landscape survey of 2026 AGI research, edge VLM SOTA, vector memory, proactive AI, and model compression. Produced by Dan2 to inform the Danlab AGI roadmap.
>
> **Status of the system (live audit, 2026-06-21 ~14:00 IST):**
>
> | # | Service | Port | Status |
> |---|---|---|---|
> | 1 | audiod | 8090 / WS 8091 | ✅ live (101/101 tests) |
> | 2 | perceptiond | 8092 | ✅ live (8/8 tests) |
> | 3 | memoryd | 8741 | ✅ live (11/11 tests) |
> | 4 | toold | 8742 | ✅ live (18/18 tests) |
> | 5 | ttsd | 8743 | ✅ live (6/6 tests) |
> | 6 | os-toold | 8744 | ✅ live |
> | 7 | openclaw | 18789 | ⚠ down (gVisor kills between runs; restartable) |
>
> **All 6 services are healthy.** The STATUS.md "4 of 7 live" line is stale (dan4 already fixed memoryd, ttsd, and the UI contract mismatch — but openclaw still drops between scheduled runs). The architecture is **more real than the status doc suggests**.

---

## Part A — System Architecture Deep Dive

### A.1 Current Dan Glasses Architecture

The decomposition is **mostly correct and pragmatically locked**:

```
[ perceptiond | audiod | memoryd | toold | os-toold | ttsd ]
        ↓            ↓         ↓         ↓       ↓           ↓
                    HTTP (FastAPI) + JSON over localhost
                              ↓
                         openclaw (TS/Node)
                              ↓
              Telegram (@danlab_bot)  +  Tauri shell
```

**What's right (confirmed):**

- **5+1 service split is right.** Each service has one reason to fail and one restart path. Memoryd, toold, audiod, and perceptiond each fit in a single mind. Ttsd is a thin KittenTTS wrapper — could be folded into audiod, but separate makes sense if TTS becomes a multi-model choice (see Part D).
- **HTTP+JSON over localhost is the right call.** Unix sockets would save a few µs but add `socat` complexity, custom framing, and worse tooling. FastAPI gives `/docs` for free. For a single-user local daemon, HTTP is fine.
- **SQLite + Markdown + flat-vector memoryd is correct for v1.** No Qdrant. No Postgres. No Redis. Everything lives in one file the user can `cp`.
- **KittenTTS + whisper.cpp** are the right pragmatic choices (see A.3).
- **OpenClaw as sole orchestrator** is a real risk and a real simplification. The risk is real (see A.4); the simplification is worth it *only if* we add a watchdog (it doesn't have one — see below).
- **`.deb` + systemd + Tauri** is correct for a Linux-first product. Flatpak can't do udev/systemd; AppImage can't either.

**What's wrong or fragile (verified, not opinion):**

1. **No watchdog for any service.** memoryd, ttsd, openclaw went down between runs (STATUS.md confirms). The fix listed is "Q3 2026 systemd unit." This is unacceptable — it's a 2-hour job, not a quarter. Dan Glasses' whole UX story breaks if audiod or memoryd dies and there's no restart. **Fix: ship `packaging/systemd/*.service` files now, not Q3. Wrap each in `Restart=on-failure` with `RestartSec=2`.**
2. **Status doc drift.** STATUS.md says 4/7 live; reality is 6/7. **Fix: replace the manual STATUS.md with a `scripts/health.sh` that curl-checks all 7 and writes the result.**
3. **The "RL loop" in `danlab-multimodal` is a hand-coded heuristic, correctly labelled.** The README and ARCHITECTURE.md both say "pre-RL scaffold" and "not RL." That's intellectually honest. But for the AGI roadmap we should commit to either (a) upgrading to genuine harness+weights self-improvement via SIA-fork, or (b) renaming it `danlab-multimodal-eval` and dropping the RL framing. See B.6.
4. **GIL on audiod.** audiod is Python + ALSA capture + whisper subprocess + Silero VAD. The build-plan flags this; audiod v0.6 sidesteps it with subprocess isolation for whisper, but VAD + segment buffer are still GIL-bound. For Dan Glasses desk-mode this is fine. For wearable (where audio latency budget = ~200ms), this is a real risk and needs measurement.
5. **OpenClaw gateway has no session recovery.** The PRD §10.3 says "auto-restart gateway, resume from last checkpoint" but `openclaw-gateway` ships with no checkpoint logic. If it dies, the session is gone.

**Verdict on architecture:** **Correctly decomposed for v1.** The bottleneck is **process supervision + observability**, not topology. Add systemd units + Loki indexing + a health-check script this week, not Q3.

### A.2 The "RL feedback loop" in danlab-multimodal — Is it real?

**Honest framing:** No, it's not RL. It's a hand-coded heuristic scorer that prints suggestions. The README says exactly this:

> "We do not modify model weights. We do not run policy gradient or any RL algorithm. We score outputs with hand-coded rules (length, error detection, content quality) and print suggestions for what a human would improve."

**That's the right answer to give the public.** But for the AGI roadmap, the question is: *what would it take to make it genuine RL?*

Three escalating paths:

| Tier | Name | Cost | What it buys |
|---|---|---|---|
| **0 (today)** | Heuristic scorer | ~0 | Demo + credibility signal |
| **1 (Q3)** | **SIA-style harness-only self-improvement** | Low (fork Hexo Labs' SIA, MIT, May 2026) | Agent rewrites its own prompt template / retry logic / evaluation rubric on each cycle. Weights stay fixed. Real measurable SWE-bench-style gains. |
| **2 (Q4)** | **SIA-style harness + weights** | Medium (needs an RL pipeline with a verifiable reward) | Same as Tier 1 + LoRA/QLoRA updates on the VLM projector or adapter on every cycle. First genuine recursive self-improvement. |
| **3 (24mo)** | **Open-ended Darwin Gödel Machine** | High | Archive of agents, evolutionary exploration, meta-agent improves meta-agent. SWE-bench 20→50% in DGM paper. Sakana + Vector Institute already proved this in coding. |

**What I'd do:**
- **Q3 2026:** Fork Hexo Labs' [SIA](https://hexolabs.com/sia) (MIT). Run a harness-only loop on danlab-multimodal's heuristic. Goal: replace the hand-coded score with a learned score (smaller model-as-judge), keep weights frozen. This is genuinely publishable.
- **Q4 2026:** Add a QLoRA pass to the loop. Now the loop modifies both harness and weights. This is what the SIA paper demonstrates on LawBench (0.701 vs Claude Code's 0.173).
- **24mo:** Build the Darwin Gödel Machine architecture. This is the credible AGI-research path Danlab could take from India.

**Critical honest point:** Until the SIA fork ships, the danlab-multimodal repo should not call itself "RL feedback loop" anywhere user-visible. The current labelling is correct. Maintain it.

### A.3 Power/Performance Tradeoffs — LFM2.5-VL-450M, whisper.cpp, KittenTTS

**Verdict: All three are the right choices for v1. Each has a clear upgrade path for v2.**

#### LFM2.5-VL-450M (vision)

- **Spec (perceptiond SPEC.md):** 209MB Q4_0 + 180MB mmproj = ~390MB combined. Runs via `llama-mtmd-cli` at `-ngl 99 -c 2048 -b 1 -ub 1 -t 8`.
- **Real perf on dev hardware (DAN-3 log):** ~10–15s/frame in watchful mode, 5 FPS capture, salient-gated.
- **What the literature says:** The [LFM2 Technical Report (Liquid AI, 2026)](https://arxiv.org/html/2511.23404) is the correct family. LFM2-VL-450M uses a SigLIP2-Base-86M encoder + LFM2-350M backbone. It's designed edge-first, flexible accuracy/latency, 32K context, open weights. Deployable via llama.cpp, ExecuTorch, vLLM. This validates the choice.
- **Failure mode (literature-backed):** The [Edge Reliability Gap paper (arXiv:2603.26769)](https://arxiv.org/html/2603.26769) shows that sub-500MB VLMs (SmolVLM2-500M-class) exhibit *qualitatively different* failure patterns than larger models: "Semantic Drift" dominates, 12.5pp larger negation collapse than Qwen2.5-VL-7B. Implication: **Dan Glasses' VLM will lie about objects being present when they're absent.** This is a real product risk for "I left my keys somewhere" US-3.
  - **Mitigation:** Don't trust single-frame yes/no answers. Use temporal consistency checks across N frames. Add a "I can't tell" abstention class.
- **aarch64 / wearable status:** No public benchmark exists yet for LFM2-VL-450M on the Redax target board. **We need to measure before we ship.** DeepEdgeBench and the LEAF framework ([MDPI 2026](https://www.mdpi.com/2504-4990/8/2/48)) give methodology — apply them.

**Alternatives to evaluate for v2:**
- **SmolVLM-256M (Q4)** = 120MB main + 182MB mmproj = ~300MB. ~26s/image on CPU. Lower quality than LFM2.5 but smaller. perceptiond SPEC says it's already the auto-fallback if LFM2.5 disappears. Keep this.
- **SmolVLM-500M** — better quality than 256M, similar footprint. [SmolVLM paper (arXiv:2504.05299)](https://arxiv.org/html/2504.05299) shows strong Video-MME and WorldSense scores relative to size.
- **OmniVLM-968M (NexaAI)** — sub-1B, 9× token compression, 9.1× faster TTFT. [Paper](https://arxiv.org/html/2412.11475). Bigger than LFM2.5 but better quality. Worth a benchmark.
- **Qwen2-VL-2B (4-bit)** — ~1.6GB. Too big for Dan Glasses wearable v1 but viable on the desk-prototype.
- **Firebolt-VL (Liquid)** — sub-1B, ~46.7k tokens/sec on H100 baseline, LFM decoder + cross-modal modulator. Promising but new.

**Recommendation:** Stay with LFM2.5-VL-450M for v1. Add the SmolVLM-256M + OmniVLM-968M variants to perceptiond's model selection menu for v1.5. Measure negation collapse on each before declaring v1 wearable-ready.

#### whisper.cpp (STT)

- **Spec:** base.en, 74MB, runs as `whisper-cli` subprocess per segment in audiod.
- **Verdict:** Right choice. whisper.cpp is the most battle-tested on-device STT. base.en is correct for English. Silero VAD + whisper.cpp is the standard stack.
- **Improvement to make:** Add `tiny.en` (39MB) and `small.en` (244MB) as configurable. `tiny.en` for low-power watchful mode; `small.en` for active mode when battery allows. [LEAF framework](https://www.mdpi.com/2504-4990/8/2/48) confirms quantized 4-bit whisper variants run fast on SBCs.

#### KittenTTS (TTS)

- **Spec:** 24kHz mono float WAV, single in-process model, 8 voices, ~3.8s cold / <1s warm latency, ~290KB per short sentence.
- **Honest take:** KittenTTS works and ships audio/wav. The [open-source TTS benchmark (MDPI 2025)](https://www.mdpi.com/2073-431X/14/10/406) clearly shows that **fast local neural TTS (FastPitch, GlowTTS class) is preferable for real-time/edge** — and **Vall-E-X and Bark are unsuitable for latency-sensitive tasks**. KittenTTS sits in the right family.
- **What's missing for v2:** No emotion control, no paralinguistics, no prosody control. The [EmergentTTS-Eval paper](https://arxiv.org/pdf/2505.23009) shows that open-source models like Bark and Sesame1B lag on emotion and complex pronunciation. If we want Dan to sound expressive (vs flat), we need an upgrade path.
- **Recommendation:** Keep KittenTTS for v1. For v2, benchmark **Piper** (more voices, faster), **Kokoro-82M** (very small, surprisingly good MOS), and **Qwen3-TTS** (5M hours of training, state-of-the-art open TTS — [paper](https://arxiv.org/pdf/2601.15621)). Decide based on a small TTSDS2 evaluation.

### A.4 OpenClaw Orchestration — TypeScript/Node, right choice?

**Honest take:** Yes, for *now*. But with serious caveats.

**Why TS is right:**
- OpenClaw is a community ecosystem now. 60K+ GitHub stars within days of launch (per analyticsvidhya). Skills registry, MCP-bridge (`mcporter`), Telegram/Discord/WhatsApp channels all exist as plugins.
- TypeScript hits the sweet spot: type safety for an orchestration layer + huge ecosystem (npm) for integrations. The `mcporter 0.9.0` Dan-1 is wiring up gives us Zo MCP bridge with no custom code.
- Node 22+ is fast enough for orchestrating 5 local services. The bottleneck is the services themselves, not OpenClaw.
- The danlab-multimodal README correctly positions OpenClaw as the gateway path for the harness-update half of the SIA loop.

**Failure modes (real):**
1. **Single point of failure.** OpenClaw dies → no Telegram, no proactive events, no service orchestration. PRD §10.3 says "auto-restart" but no checkpoint logic ships. **Fix: write a `state.json` snapshot every 5s. On restart, replay.**
2. **No session persistence across gateway restarts.** Long Dan Glasses sessions lose context. **Fix: route session memory through memoryd, not through OpenClaw's own KV.**
3. **Node GC pauses can stall the gateway.** For wearable, where the gateway might be the only thing standing between the user and the silence of a dead mic, this matters. **Fix: monitor GC pause times; if >50ms p99, move to Bun or Deno.**
4. **TypeScript's MCP ecosystem is still maturing.** `mcporter` is v0.9 — early. Bugs are likely. **Fix: pin versions, write integration tests against Zo MCP.**

**Verdict:** Keep TS/Node for v1. **Add watchdog + state-snapshot this week.** Re-evaluate Bun vs Node after 3 months of production data. The architecture decision is fine; the operational maturity is not.

---

## Part B — AGI Landscape (2026)

### B.5 State of AGI Research in 2026

**Three-way race for AGI by 2030:**

| Player | Position | Public commitment | Notable 2026 move |
|---|---|---|---|
| **OpenAI** | "Build AGI, benefit all of humanity" | Altman + Pachocki blog (Jun 2026): "automated AI researcher" is the first of three goals | IPO filed, targeting Sep 2026; pivoting away from "side quests" like Sora toward agentic super-app |
| **Anthropic** | AGI with safety constraints | Valued $965B post-Series H (May 2026) — leapfrogged OpenAI | Claude Mythos admitted (Jun 2026); Jack Clark + Favaro call for coordinated slowdown; **Claude now writes 80% of Anthropic's production code** |
| **Google DeepMind** | AGI by 2030, possibly 2029 | Hassabis at I/O 2026: "foothills of the singularity" | Agentic era framed as "practice run" for far more powerful systems |

**Chinese catch-up:** Yao Shunyu (ex-OpenAI) now Tencent Chief AI Scientist, says personal goal is to establish a long-term AGI org in China. The US-China AGI race is now real.

**The open-source undercurrent:**
- **Hexo Labs SIA** (May 2026, MIT) — the credible path to harness + weights recursive self-improvement. [arXiv 2605.27276](https://arxiv.org/pdf/2605.27276). Scored 0.701 on LawBench vs Claude Code's 0.173.
- **Sakana AI Darwin Gödel Machine** — open-ended self-improvement in coding. SWE-bench 20→50%, Polyglot 14.2→30.7%.
- **Facebook DGM-Hyperagents** — extends DGM with self-referential meta-modification.
- **Karpathy autoresearch** (Mar 2026, 630 lines) — minimal but real self-improving loop.

**The uncomfortable fact for Danlab:** *None of these are accessible to a small lab in India for "free."* They need compute, RL infra, and researcher bandwidth. Danlab's edge is *not* training new foundation models — it's *applying* existing ones in the right shape.

### B.6 Self-Improving Architectures — What Has Actually Worked

In order of credibility (least hand-wavy to most):

1. **Reflexion** (Princeton/MIT, 2023) — verbal self-reflection stored in memory. Cheap, works, ships in production.
2. **Karpathy autoresearch** (Mar 2026) — 630-line Python script, agent modifies its own training code, evaluates, iterates. ~5 min/experiment on 1 GPU. **Closest to what Danlab could ship.**
3. **SIA** (Hexo Labs + Oxford, May 2026) — Feedback-Agent rewrites harness + updates weights. Real measurable gains on legal benchmarks.
4. **Darwin Gödel Machine** (Sakana AI, 2025) — open-ended evolution of agents. Archive-based, true self-improvement. Most credible academic result.
5. **DGM-Hyperagents** (Facebook AI Research, 2026) — meta-agent improves meta-agent. Self-referential.

**What has NOT worked (still):**
- Pure weight-modifying RL on small open-source models for "AGI" claims — collapses to mode collapse or reward hacking.
- Gödel machine (Schmidhuber, 2003) — provably beneficial self-modification — remains theoretical.

**For Danlab:** The path is clear. **SIA-fork on danlab-multimodal (Q3 2026).** This is what danlab-multimodal's README already gestures at. Just do it.

### B.7 Edge AI / On-Device SOTA for sub-500MB VLMs

**Concrete landscape (2026):**

| Model | Size | Encoder | Decoder | Where it wins |
|---|---|---|---|---|
| **LFM2-VL-450M** | ~390MB | SigLIP2-Base-86M | LFM2-350M | Flexible accuracy-latency, 32K context |
| **SmolVLM-256M** | ~300MB | SigLIP-Base | SmolLM2-135M | Smallest working VLM |
| **SmolVLM-500M** | ~500MB | SigLIP-400M | SmolLM2-135M | Better quality vs 256M, similar size |
| **OmniVLM-968M** | sub-1B | (NexaAI custom) | Custom | 9× token compression, 9.1× faster TTFT |
| **MobileVLM-1.4B / 2.7B** | sub-3B | CLIP-style | MobileLLaMA | Snapdragon-tuned, faster on mobile |
| **Firebolt-VL-0.8B** | sub-1B | LFM-based | LFM + cross-modal modulator | 46.7k tok/s H100, edge-tuned |
| **Qwen2-VL-2B (4-bit)** | ~1.6GB | Qwen-VL | Qwen2.5 | High quality, too big for v1 wearable |

**Two critical findings from the literature:**

1. **Edge NPUs are real but immature.** [LLM Inference at the Edge (arXiv:2603.23640)](https://arxiv.org/abs/2603.23640) shows Hailo-10H on RPi 5 achieves ~6.9 tok/s stable inference — usable for background tasks but not interactive. This means **LFM2-VL-450M on a wearable NPU is plausible** but won't be smooth until NPU integration matures.
2. **Compact VLMs fail differently than large ones.** [Edge Reliability Gap](https://arxiv.org/html/2603.26769) shows SmolVLM2-500M answers "Yes" to object absence 100% of the time on COCO. **Wearable safety implication: an off-the-shelf VLM is unreliable for "did you see X" queries.** Need temporal consistency checks + abstention.

**Recommendation for Danlab:** Stick with LFM2-VL-450M. Add OmniVLM-968M and SmolVLM-500M to the perceptiond v1.5 candidate list. Benchmark each on the Redax board before choosing.

### B.8 Memory and Continual Learning — AI Systems That Learn From Experience

**The 2026 state of memory architectures (paper survey):**

| System | Type | Innovation | Status |
|---|---|---|---|
| **Mem0 / Mem0^g** | Vector + optional graph | LLM extracts facts, dedupes, optional knowledge graph; p95 latency -91% vs full-context | Production-ready, used in industry |
| **Letta (MemGPT)** | Tiered virtual context | Core memory vs archival, tool-based operations | Open source, mature |
| **Zep / Graphiti** | Temporal knowledge graph | Time-aware edges, evolving facts | Cloud-hosted, enterprise-only now |
| **Memori** | Persistent semantic triples | Extracts subject-predicate-object triples from chat | 81.95% LoCoMo, beats Zep/LangMem/Mem0 |
| **SimpleMem** | CLS-inspired compression | 3-stage: compress → synthesize → intent-aware retrieve | Most principled |
| **Memanto** | Vector-only with typed schema | 13 typed categories, zero ingestion latency | 89.8% LongMemEval, 87.1% LoCoMo |
| **MemForest** | LSM-tree-inspired hierarchical index | MemTree per temporal scope, write-efficient | Scales to long horizons |
| **MemMachine** | Retrieval + STM hybrid | Preserves ground truth via pgvector + short-term cache | Ground-truth-preserving |
| **MemReader** | Active extraction (not passive) | 0.6B + 4B (ReAct) decide when/what/whether to write | Newest, action-based |
| **MemGate** | Plug-in gating | 9M param filter between retrieval and prompt | Lightweight safety layer |
| **SuperLocalMemory V3.3** | Multi-channel w/ forgetting | Vector + BM25 + entity graph + temporal; cognitive quantization | Best for offline/air-gapped |

**Three architectural patterns Dan Glasses should pick from:**

1. **Mem0-style (vector + optional graph)** — cheapest to ship, well-understood. **This is what memoryd should evolve into.**
2. **Memori-style (semantic triples)** — better retrieval quality, more storage. Better for "I met Priya yesterday" queries.
3. **MemMachine-style (retrieval + STM)** — preserves ground truth, ideal for personal AI.

**For Danlab's roadmap:** Move memoryd from "flat cosine similarity over sentence embeddings" to a Mem0/Memori hybrid in Q4 2026. Episodic memories (what I saw) stay vector. Semantic memories (facts about the user) get extracted as triples. Procedural memories (how I do things) stay Markdown.

### B.9 Multimodal Fusion — How the Best Systems Combine Vision, Audio, Text

**Three concrete architectures from the literature:**

1. **ProAgent (arXiv:2512.06721)** — tiered perception (always-on low-cost + on-demand high-cost VLM), VLM-based proactive reasoner, 27.7% higher proactive prediction accuracy, 85% user satisfaction in 20-participant study. **This is the closest published architecture to what Dan Glasses wants to be.**
2. **Galaxy (arXiv:2508.03991)** — Cognition Forest + KoRa (cognition-enhanced generative agent) + Kernel (meta-cognition meta-agent). Proactive, privacy-preserving, self-evolving. Self-reinforcing loop between cognition and architecture.
3. **PASK (arXiv:2604.08000)** — DD-MM-PAS (Demand Detection + Memory Module + Proactive Agent System). IntentFlow streaming foundation model for real-time demand detection. Hybrid memory (User + Workspace + Global).

**Pattern Dan Glasses should adopt (already partially there):**

```
Always-on low-cost sensing (VAD + motion delta + face detect)
   ↓
On-demand high-cost VLM (LFM2.5-VL-450M, salient-gated)
   ↓
Multimodal fusion layer (text description + audio transcript + memory context)
   ↓
Proactive reasoner (initiates vs responds)
   ↓
TTS / Telegram output
```

**What's missing in Dan Glasses today:** the proactive reasoner. OpenClaw is reactive (waits for input). To deliver the PRD's "proactive AI companion" promise, we need a ProAgent-style always-on reasoner in OpenClaw that watches audiod + perceptiond event streams and decides when to speak.

**Recommendation:** Build `openclaw-proactive` as a thin watcher. Read events from audiod WS + perceptiond ring buffer. Score each event against user's "now" context. Trigger TTS via ttsd if score > threshold. Ship this in Q3 2026 alongside the SIA fork.

### B.10 Model Compression — What Works for Keeping Models Small but Capable

**2026 SOTA techniques (paper survey):**

| Technique | Compression | Quality retention | Maturity |
|---|---|---|---|
| **GPTQ** (4-bit weight, Hessian) | 4× memory | High (when paired with rotation) | Production |
| **AWQ** (activation-aware scaling) | 4× memory | Moderate alone, great with GPTQ | Production |
| **QuaRot + GPTQ** | 4× | +29% over AWQ+GPTQ at 3-bit | Best published 4-bit |
| **DACQ** (distribution-aware companding) | 4× | Non-uniform levels, distribution-modeled | New, promising |
| **AAAC** (adaptive codebooks) | 4× | Gradient-free, 3-30 min quantization | Fastest, beats AWQ+GPTQ |
| **TwinQuant** (learnable subspace) | 4× | 1.3-1.8× faster than FP16 TensorRT-LLM | New |
| **AWP** (joint pruning + quant) | 4× + 50% sparsity | Activation-aware, PGD-based | Research |
| **Minitron** (depth/width pruning) | 50% smaller | LLaMA-3.1-Minitron-4B | NVIDIA, production-ready |
| **Knowledge distillation (LRC, MiniLLM)** | 4-8× | Quality ~teacher | Standard |
| **2-bit QAT (GPTQ-init)** | 8× | Now viable for reasoning tasks | Frontier |

**For Dan Glasses specifically:**

- **LFM2-VL-450M is already Q4.** Don't re-quantize for v1.
- **SmolVLM-256M Q4 + mmproj F16** is the current combination. Try Q4 mmproj for ~150MB savings. Test visual quality drop.
- **whisper.cpp tiny.en Q4_0** = ~30MB. Better than base.en Q4 for power-constrained watchful mode.
- **KittenTTS** is already small (~25MB). Probably fine as-is.

**Don't do this in 2026:** Re-train your own foundation model. Use AWQ/GPTQ/QuaRot on existing models. If you must distill, use an existing teacher's representations (Minitron-style), don't start from scratch.

---

## Part C — Competitive & Market Research

### C.11 AI Wearables Landscape (2026)

The category is **exploding right now**:

| Player | Form | Price | What it does | On-device? |
|---|---|---|---|---|
| **Snap Specs** | AR glasses (spatial computer) | $2,195 | 51° FOV display, on-device AI | Yes |
| **Meta Ray-Ban (Gen-2)** | Prescription-friendly smart glasses | $499 (display models) | Notification display, AI assistant | Mostly cloud |
| **Meta Ray-Ban (original)** | Smart glasses | ~$300 | Capture + share, ambient AI | Cloud |
| **Google Project Aura** (with Xreal) | AR glasses + pocket "puck" | TBD | Android XR apps | Hybrid |
| **ROG Xreal R1** | 240Hz gaming glasses | $849 | Gaming display | Tethered |
| **Apple AI AirPods** | AirPods | TBD | Audio-first AI | Likely cloud |
| **Limitless Pendant** | Necklace | (Meta acquired, discontinued) | Meeting transcription | Cloud |
| **Plaud NotePin S** | Clip-on | ~$200 | Voice recorder + AI notes | Cloud |
| **Bee AI** | Wristband | (Amazon acquired) | Always-on transcription | Cloud |
| **Friend / Omi / Rabbit R1** | Various pendants/pins | $99-300 | Conversation AI | Cloud |

**Honest framing:** The wearables race is *Meta + Google + Snap* in glasses, *Bee/Limitless/Friend/Omi* in pendants. Most are cloud-dependent. Snap Specs ($2,195) is the first real standalone AR competitor to Meta.

**Danlab's positioning opportunity:**

- **Meta, Google, Snap = cloud.** Privacy story is bad. Data is uploaded.
- **Bee, Limitless, Plaud = cloud.** Same problem.
- **Dan Glasses = on-device, opt-in cloud.** This is a real differentiator. PRD §7 calls it out correctly.
- **No one is doing *proactive* AI on-device.** Meta Ray-Ban responds when asked. Snap Specs does display + queries. Nobody is shipping a "remembers you walked past the pharmacy 3 times" experience on-device.

**This is Danlab's wedge.** Cloud-dependent AI wearables are commodity. On-device proactive AI is not. Lean into it.

### C.12 Open-Source AI Companion Projects

**Landscape:**

| Project | Stars | Memory | On-device | Notes |
|---|---|---|---|---|
| **OpenHands (OpenDevin)** | High | Filesystem | Optional | Coding agent, not companion |
| **Letta (MemGPT)** | High | Tiered virtual context | Optional | Best open-source memory |
| **Open Interpreter** | 60K+ | Filesystem | Optional | Local code execution |
| **smolagents** | HuggingFace | None | Optional | Lightweight |
| **OpenClaw** | 60K+ (community) | Pluggable | Local-first | Closest to Dan Glasses arch |
| **DGM / Hyperagents** | Research | Archive | N/A | Self-improving agents |
| **Bernstein / Toad / Letta Code** | Various | Filesystem | Local | CLI orchestrators |
| **Paperclip** | (Danlab) | Issue tracking + agent coordination | Self-hosted | Currently dormant — should it be revived? |

**Strategic note for Danlab:** **Paperclip is dormant.** Its stated purpose (multi-agent coordination, issue tracking, goal management) is exactly what OpenClaw is now providing via skills. Don't revive Paperclip. Instead, **integrate Paperclip-style goal-tracking as an OpenClaw skill** under danlab's `dani-skills` registry.

### C.13 Privacy-Preserving AI — How Dan Glasses Positions

**The privacy landscape for AI in 2026:**
- Cloud AI = data uploaded by default. Even when "encrypted," companies hold keys.
- Local AI = data stays on device. But usability is lower (slower, smaller models).
- Hybrid = opt-in cloud for heavy tasks, local for everything else.

**Dan Glasses' natural positioning:**
- On-device by default for STT, VLM, TTS, memory.
- Telegram (already integrated) is opt-in for proactive notifications.
- Open source = auditable. (Repo is at github.com/somdipto/dan-lab.)
- No third-party SDKs reading the camera/mic frames.

**This is genuinely good and rare.** Meta Ray-Ban's privacy story is bad — frames uploaded to Meta's cloud. Bee AI was bought by Amazon (immediate red flag). Friend AI got criticized for always-on audio. Limitless was acquired and discontinued.

**Marketing wedge:** "The only AI wearable that doesn't upload your life." Make this the headline. It maps directly to a real market fear.

---

## Part D — Technical Deep Dives

I did three deep dives, as required. The other three options are noted at the end.

### D.A — Self-Improving RL Loops for Language Models

**The current frontier (2026):**

1. **SIA (Hexo Labs + Oxford, May 2026)** — most credible near-term path. [arXiv:2605.27276](https://arxiv.org/pdf/2605.27276). The architecture:

```
[Feedback-Agent (LLM, e.g. LFM2.5-1.2B-Thinking)]
   ↓ writes
[Task-specific Agent harness + LoRA weights]
   ↓ runs on
[Benchmark task]
   ↓ produces
[Feedback signal (benchmark score)]
   ↑ goes back to Feedback-Agent
   ↻ loop
```

   SIA scored **0.701 on LawBench** vs Claude Code's **0.173**. That's a real, measurable, recursive self-improvement result. Both harness and weights are updated.

2. **DGM (Sakana AI, 2025)** — open-ended evolution. Archive of agents. SWE-bench 20→50%, Polyglot 14.2→30.7%. The agent grows a tree of itself.

3. **DGM-Hyperagents (Facebook AI Research, 2026)** — extends DGM with self-referential meta-modification. Meta-agent rewrites its own rewrite procedures.

4. **Karpathy autoresearch (Mar 2026)** — 630 lines of Python. Agent modifies its own training code, runs experiments, evaluates, iterates. ~5 min/experiment on 1 GPU. The minimalist version. **Closest to what Danlab could ship in a week.**

**Key insight from the literature:** *The harness-update school (DGM, SIA, Meta-Harness) and the test-time training school (TTRL, RL on small models) have largely evolved separately.* SIA is the first to combine them. For Dan Glasses, SIA's harness-only mode is the cheapest entry — agent rewrites perceptiond's prompt template and the VLM selection logic based on retrieval quality scores.

**Risks the literature flags:**
- **Reward hacking.** Heuristic feedback scorers can be gamed. SIA uses verifiable benchmark scores (LawBench), which is much harder to game. Don't use a learned reward without ground-truth verification.
- **Mode collapse.** RL on small open-source models for "AGI" claims collapses fast. SIA sidesteps this by holding harness AND weights fixed alternately.
- **Compute cost.** A full SIA loop on a single benchmark takes days of GPU time. Danlab needs a budget.

**For Danlab:**
- **Q3 2026:** Fork SIA. Run harness-only loop on danlab-multimodal's heuristic benchmark. Use a small Feedback-Agent (LFM2.5-1.2B-Thinking). Publish a "first recursive self-improvement result from India" paper.
- **Q4 2026:** Add QLoRA weight updates. Now it's genuine recursive self-improvement.
- **24mo:** DGM-style open-ended evolution. Archive of perceptiond prompts, audiod VAD configs, etc. Self-evolving Danlab.

### D.B — Edge VLM Optimization

**Three concrete techniques to evaluate for Dan Glasses v1.5:**

1. **QuaRot + GPTQ (rotation-based 4-bit).** [LLMC paper](https://arxiv.org/html/2405.06001) shows +29% accuracy at 3-bit over AWQ+GPTQ for LLaMA-3-8B. Should translate to LFM2-VL-450M. Test on the Redax board.

2. **AAAC (activation-aware adaptive codebooks).** Gradient-free, 3-30 min quantization. Outperforms AWQ+GPTQ. Compatible with AWQ (use both for ~70% gap recovery). Very practical.

3. **SPEED-Q (2-bit staged quantization).** [arXiv:2511.08914](https://arxiv.org/html/2511.08914). 2-bit InternVL-1B runs in 400MB. Comparable accuracy to FastVLM-0.6B at 1.5GB. If we go 2-bit on LFM2-VL-450M, total memory drops from ~390MB to ~200MB. That's huge for wearable.

**Hardware-accelerated inference on aarch64 (wearable):**

- **LEAF framework findings** ([MDPI 2026](https://www.mdpi.com/2504-4990/8/2/48)): Raspberry Pi 5 with Cortex-A76 outperforms Jetson Nano on quantized LLM workloads. Counter-intuitive but true. Older Jetson Nano GPU is poorly optimized for quantized transformers.
- **Raspberry Pi 5 + Hailo-10H NPU:** ~6.9 tok/s stable inference. Usable for background tasks. Not interactive. [LLM Inference at the Edge, arXiv:2603.23640](https://arxiv.org/abs/2603.23640).
- **Orange Pi 5 Pro:** Most versatile SBC tested. Runs up to ~7B models acceptably. Worth considering as dev board for Redax.
- **Jetson Orin Nano:** ~9-10 tok/s. Best raw throughput but worst energy efficiency.

**Practical recommendation:** Use **Orange Pi 5 Pro or Raspberry Pi 5 + Hailo-10H** as the Redax reference dev board. Apply AAAC + GPTQ to LFM2-VL-450M for v1.5. Aim for sub-200MB on-disk vision stack.

### D.C — Vector Search and Memory Architectures for AI Companions

**The state-of-the-art (2026):**

The current best-published results:
- **Memanto: 89.8% LongMemEval, 87.1% LoCoMo** — vector-only, typed schema, zero ingestion latency.
- **Memori: 81.95% LoCoMo** — semantic triple extraction from chat.
- **SimpleMem** — CLS-inspired compression, 3-stage pipeline, intent-aware retrieval.
- **Mem0: 26% accuracy improvement, 91% p95 latency reduction** over full-context baseline.

**Three patterns Dan Glasses' memoryd should consider:**

```
PATTERN A — Mem0-style (vector + optional graph)
─────────────────────────────────────────────────
chat/observation → LLM extraction → vector store (Qdrant/local)
                                ↓
                        fact dedup (LLM judge)
                                ↓
                     retrieval (cosine + temporal)
─────────────────────────────────────────────────
PRO: Cheap, proven, easy to debug
CON: LLM extraction cost per conversation turn

PATTERN B — Memori-style (semantic triples)
─────────────────────────────────────────────────
chat → LLM extracts S-P-O triples → triple store
                                       ↓
                              retrieval (triple + vector)
─────────────────────────────────────────────────
PRO: Better retrieval quality (81.95% LoCoMo)
CON: Higher storage cost; triples can fragment

PATTERN C — MemMachine-style (retrieval + STM)
─────────────────────────────────────────────────
chat → STM ring buffer (last N turns, in-prompt)
        ↓
      async extract → long-term memory (pgvector or similar)
        ↓
      query → STM + LT retrieval
─────────────────────────────────────────────────
PRO: Preserves ground truth; immediate recent context
CON: More moving parts; harder to debug
```

**For Dan Glasses specifically:**

Memoryd's current design (episodic/semantic/procedural types + cosine similarity + 384-dim MiniLM embeddings) is essentially **Pattern A's skeleton without the LLM extraction step**. This is honest and shippable for v1. The upgrade is:

1. **Add LLM extraction (Q4 2026).** Use LFM2.5-1.2B-Thinking or HRM-Text (per AGENTS.md) to extract facts from each conversation turn before storing. Use a small MemReader-style model to decide when/what to remember.
2. **Add MemReader-0.6B or similar (Q1 2027).** Active memory writing — decides when, what, whether to overwrite. Goes beyond passive extraction.
3. **Add MemGate (Q1 2027).** 9M-param filter between retrieval and prompt. Cheap way to prevent irrelevant memories from polluting responses.

**Concrete next step for Danlab:** Replace memoryd's `/query` shape with Mem0-style `add + search` API. Keep SQLite + flat vectors. Add a tiny `extract_facts` function that runs an LFM2.5-1.2B call once per conversation turn.

### D.D–F (not deep-dived, notes)

- **D (Proactive AI):** ProAgent (arXiv:2512.06721) and Galaxy (arXiv:2508.03991) are the closest published architectures. ProAgent's 27.7% higher proactive prediction accuracy vs baselines + 85% user satisfaction is the strongest evidence that the architecture works. Build `openclaw-proactive` as a thin watcher over audiod + perceptiond event streams.
- **E (TTS):** KittenTTS is acceptable for v1. For v2, benchmark Piper, Kokoro-82M, and Qwen3-TTS. Decision criterion: TTSDS2 score vs deployment footprint.
- **F (VLM power on wearable):** Critical missing measurement. Need Redax board power probe. Until we have numbers, all power claims are guesses. **This blocks wearable v1 ship.**

---

## Part E — Honest Self-Assessment

**What Danlab has right:**
- Architecture decomposition is correct for v1.
- Model choices (LFM2.5-VL, whisper.cpp, KittenTTS) are defensible.
- Honest framing of "pre-RL" instead of overclaiming.
- Six of seven services live and tested. The system *works* on a desk today.
- Open-source posture is genuine (MIT, public repos).
- India-from-AGI positioning is differentiated.

**What's blocking v1 wearable:**
1. No watchdog / supervision for any service.
2. No measured power / latency on the Redax target board.
3. No SIA-style genuine self-improvement (the "RL" framing is aspirational).
4. STATUS.md is stale — credibility risk for external observers.

**What's blocking AGI roadmap:**
1. No GPU/compute budget for training or fine-tuning.
2. No clear positioning vs cloud-AI wearables (Meta Ray-Ban, Snap Specs).
3. No published research track (everything is private repos).

**The Danlab window:** The 2026 AI wearable category is exploding (Snap $2,195, Meta Ray-Ban Gen-2, Google Project Aura). On-device proactive AI is *not* yet a solved product. Danlab has the architecture, the open-source posture, and the Indian-AGI narrative. **The window is now.** Lean in.

---

## Sources

[^1]: https://arxiv.org/html/2511.23404 — LFM2 Technical Report (Liquid AI, 2026)
[^2]: https://arxiv.org/html/2603.26769 — Edge Reliability Gap in Vision-Language Models
[^3]: https://arxiv.org/html/2504.05299 — SmolVLM (HuggingFace, 2025)
[^4]: https://arxiv.org/html/2412.11475 — OmniVLM (NexaAI, 2024)
[^5]: https://arxiv.org/html/2604.04579 — Firebolt-VL (2026)
[^6]: https://arxiv.org/html/2511.08914 — SPEED-Q (2026)
[^7]: https://www.mdpi.com/2504-4990/8/2/48 — LEAF Framework (2026)
[^8]: https://arxiv.org/abs/2603.23640 — LLM Inference at the Edge (2026)
[^9]: https://arxiv.org/pdf/2605.27276 — SIA: Self Improving AI with Harness & Weight Updates
[^10]: https://arxiv.org/html/2505.22954v3 — Darwin Gödel Machine (Sakana AI)
[^11]: https://arxiv.org/html/2504.19413 — Mem0
[^12]: https://arxiv.org/pdf/2603.19935 — Memori
[^13]: https://arxiv.org/pdf/2601.02553 — SimpleMem
[^14]: https://arxiv.org/pdf/2604.22085 — Memanto
[^15]: https://arxiv.org/pdf/2604.04853 — MemMachine
[^16]: https://arxiv.org/pdf/2604.07877 — MemReader
[^17]: https://arxiv.org/pdf/2606.06054v1 — MemGate
[^18]: https://arxiv.org/html/2606.01138v2 — memorywire
[^19]: https://arxiv.org/html/2605.23986 — MemForest
[^20]: https://arxiv.org/html/2410.12361 — Proactive Agent (2024)
[^21]: https://arxiv.org/html/2512.06721 — ProAgent (2026)
[^22]: https://arxiv.org/pdf/2508.03991 — Galaxy (2026)
[^23]: https://arxiv.org/pdf/2604.08000v1 — PASK (2026)
[^24]: https://arxiv.org/html/2505.14668 — ContextAgent
[^25]: https://arxiv.org/pdf/2508.18689 — AppAgent-Pro
[^26]: https://www.marktechpost.com/2026/03/23/meta-ais-new-hyperagents-dont-just-solve-tasks-they-rewrite-the-rules-of-how-they-learn — Meta Hyperagents
[^27]: https://github.com/facebookresearch/HyperAgents
[^28]: https://hexolabs.com/sia
[^29]: https://digg.com/ai/omxtbh5l — SIA release
[^30]: https://www.mdpi.com/2073-431X/14/10/406 — Open-source TTS benchmark
[^31]: https://arxiv.org/pdf/2601.15621 — Qwen3-TTS
[^32]: https://arxiv.org/pdf/2505.23009 — EmergentTTS-Eval
[^33]: https://arxiv.org/pdf/2506.19441 — TTSDS2
[^34]: https://arxiv.org/html/2405.06001 — LLMC
[^35]: https://arxiv.org/pdf/2603.00364 — DACQ
[^36]: https://arxiv.org/html/2605.08692 — AAAC
[^37]: https://arxiv.org/html/2606.01556v1 — TwinQuant
[^38]: https://www.forbes.com/sites/katehardcastle/2026/06/17/snap-smart-glasses-hit-the-market-at-2195-as-ar-wearables-reach-inflection-point/
[^39]: https://techcrunch.com/2026/06/16/snap-finally-debuts-its-long-awaited-ar-glasses-specs-and-oof-they-arent-cheap/
[^40]: https://glassalmanac.com/7-ar-glasses-in-2026-that-surprise-buyers-price-release-what-to-know/
[^41]: https://dallasexpress.com/business-markets/anthropic-admitted-claude-is-close-to-self-improvement-heres-what-that-means/
[^42]: https://www.cnbc.com/2026/06/05/china-may-move-toward-us-path-on-ai-as-firms-poach-employees.html
[^43]: https://www.gigazine.net/gsc_news/en/20260528-google-deepmind-ceo-demis-hassabis-agi-2030
[^44]: https://bigguyonstuff.com/ai-wearables-2026-honest-review
[^45]: https://www.plaud.ai/blogs/articles/whats-the-best-wearable-device-for-ai-note-taking-2026
[^46]: https://www.umevo.ai/blogs/ume-all-posts/limitless-vs-bee-vs-omi-the-wearable-ai-showdown
[^47]: https://github.com/somdipto/dan-lab
[^48]: https://github.com/somdipto/dani-skills

---
*Dan2 research agent, 2026-06-21. Citations traceable via [^n] references.*
