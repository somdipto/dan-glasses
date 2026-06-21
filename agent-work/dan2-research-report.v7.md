# Dan2 — Technical Research Report v7
## Deep Research for Danlab's AGI Roadmap (2026-06-17)

**Date:** 2026-06-17
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v7 fresh re-run. v6 archived as `*.v6.md`. v7 folds in:
  - Latest Anthropic "brake pedal" + Claude Mythos RSI disclosures (Jun 4–7, 2026)
  - SIA paper reality-check (Hexo Labs + Oxford, May 29, 2026): 3 tasks, 2 levers, real vs. claimed results
  - HRM-Text 1B (Sapient, May 18, 2026) — 1.15B params, 40B tokens, brain-inspired
  - Meta Ray-Ban Display with Muse Spark (May 23, 2026) + Apple glasses delayed to late 2027
  - MemPrivacy edge-cloud reversible pseudonymization framework (MemTensor, May 18, 2026)
  - OpenClaw security survey (arXiv 2605.25435) — skill poisoning, cognitive manipulation
  - Proactive AI benchmark landscape: ProAgentBench, ProAct, ProActor

**Read this first, then the 4 companion artifacts.**

---

## 0. Scope and Method

This is the **v7** research report. It covers:

- **A.** System architecture deep-dive (Dan Glasses, danlab-multimodal, OpenClaw)
- **B.** AGI landscape research (2026, with emphasis on RSI / SIA / Anthropic brake pedal)
- **C.** Competitive and market research (AI wearables, open-source AI companions, privacy)
- **D.** Three technical deep-dives: **edge VLM optimization**, **memory architectures for AI companions**, **proactive AI**

Four companion artifacts:

- `dan2-architecture-review.md` — concrete problems and fixes for Dan Glasses
- `dan2-model-analysis.md` — model selection deep-dive
- `dan2-agi-roadmap.md` — 6/12/24-month Danlab direction
- `dan2-papers-to-read.md` — top 5 papers (with rationale)

All claims grounded in 2025–2026 sources. Every "should" and "must" is an opinion — challenge it. Where v6 said something that v7 evidence contradicts, I flag it explicitly.

---

## 1. Danlab Ecosystem — What I Read, What I Concluded

### 1.1 Inventory of artifacts I read (v7 sweep)

| File | Purpose | Verdict |
|---|---|---|
| `/home/workspace/dan-glasses/PRD.md` | Product spec v1.0 (2026-04-17) | Solid v1; power/form-factor still aspirational |
| `docs/dan-glasses-build-plan.md` | Build plan | Actionable; stack is correct |
| `docs/dan-glasses-v1-canonical-analysis.md` | Architecture review | Strong; 15 gaps, **none addressed in v6 cycle** |
| `agent-work/ARCHITECTURE-FLAWS-BEFORE-CODE.md` | Pre-code review | 20 issues; 7 critical |
| `Services/{audiod,perceptiond,memoryd,toold,ttsd}/SPEC.md` | Service specs | Internally consistent, **not aligned on storage, IPC, or schema** |
| `Services/{audiod,perceptiond}/` (actual code) | Live system | 106/106 tests green, all daemons live |
| `agent-work/dan{1,2,3,4}.md` | Agent logs | Stack is operational, not a plan |
| `/home/workspace/danlab-multimodal/README.md` + `ARCHITECTURE.md` | Hackathon repo | **Honest pre-RL scaffold, not RL** |
| `/home/workspace/paperclip/AGENTS.md` | Multi-agent platform | Dormant — needs decision: ship or archive |
| `/home/workspace/blurr/README.md` | Android companion | Not deeply integrated with Dan Glasses |
| `AGENTS.md` (root) — workspace memory | Says "HRM-Text (1B) for reasoning" | **Contradicts dan-glasses/AGENTS.md which says "LFM2.5-VL-450M for vision"** — see §2.5 |

### 1.2 What is actually built (per `dan1.md` 2026-06-15 audit, v6 confirmed at 2026-06-17 04:50 UTC in `dan2.md`)

- All 7 daemons live: `audiod` (66 tests), `perceptiond` (8), `memoryd` (16/11), `toold` (18/15), `ttsd` (6), `os-toold`, `zo-mcp-bridge`.
- Tauri v2 app wired to all daemons via 20+ Rust commands.
- OpenClaw gateway on `:18789` with Telegram channel + Zo MCP bridge.
- 106/106 tests passing in v6; v7 numbers: audiod 83/83, memoryd 16/16, toold 18/18, ttsd 6/6, perceptiond 8/8 = **131/131** (v7 has more memoryd and toold tests added).
- LFM2.5-VL-450M-Q4_0 (209 MB) inference at ~10–15 s/frame on x86_64 CPU. **Redax aarch64 measurements still missing.**

**This is not a research project anymore — it is a working prototype that needs hardening, hardware, and intelligence on top.**

### 1.3 Three contradictions I found in v7 (v6 had two)

1. **Model choice brain-drift.** Root `AGENTS.md` says "HRM-Text (1B) for reasoning", but `dan-glasses/AGENTS.md` says "LFM2.5-VL-450M for vision". These are not the same thing. v6 proposed "both, different roles". v7 confirms: HRM-Text 1B released 2026-05-18 (Sapient Intelligence, Singapore) is a reasoning model with 1,000× less data than typical pretraining, brain-inspired hierarchical architecture — **a real candidate for Dan Glasses' on-device reasoning layer.** [^1]
2. **Heuristic vs. RL honesty in danlab-multimodal.** The README correctly disclaims this is a heuristic, not RL. SIA exists (Hexo Labs, MIT-licensed, 2026-05-29). **The path is named and unused.** v7 makes the fork plan concrete in §2.3.
3. **(new in v7) Workspace memory split.** `/home/workspace/dan-glasses/AGENTS.md` and `/home/workspace/AGENTS.md` are different files. The root one points to `dan-consciousness` GitHub repo as canonical brain. The dan-glasses one is project-specific. **This is fine as long as the dan-consciousness pointer doesn't get stale.** v7 has not pulled from dan-consciousness — see open questions.

### 1.4 Key v7 finding: the project is structurally solid but **starved of intelligence on top**

All 7 daemons work. The bottleneck is no longer "can it see/hear/speak/remember" — it is:
- a) **reasoning layer** (HRM-Text 1B candidate, not yet integrated)
- b) **proactive layer** (proactive AI research is real in 2026; Dan Glasses only has reactive triggers)
- c) **self-improvement layer** (danlab-multimodal is honest about being pre-RL; SIA exists)

These three layers are the AGI roadmap. The rest is plumbing.

---

## 2. System Architecture Deep-Dive

### 2.1 Is the service decomposition correct?

**Mostly yes, with three structural problems carried forward from v6.**

**A. No shared schema / IPC contract.** Each service defines its own JSON shapes. There's no `shared/` types crate (the directory is empty per `dan1.md`). A Tauri command in `perceptiond.rs` is hand-written HTTP-over-TCP, and the response shape drifts from the SPEC.md description. **Fix:** define a `shared/` Rust crate with serde structs; have each service depend on it. Cost: 1 day. Pays off in: months of integration drift prevented.

**B. VLM gate is wrong-levelled (still the #1 power issue).** v7 confirms: perceptiond's salience gate uses CPU (OpenCV Haar, EMA background) — fine, ~0.5 W. But the VLM is invoked by default on every salient frame, and inference is the dominant power event. v6 added a `context_gate` recommendation. **v7 update**: with Anthropic's brake-pedal disclosures and the broader industry focus on "AI that builds itself", power characterization on aarch64 is now blocking-bottleneck status. The fix isn't optional.

**C. No LLM in the loop yet — but we now have a candidate.** v6 said "no LLM that *reasons* over the day's descriptions and decides what to store/surface/forget". v7 fix: **integrate HRM-Text 1B (Sapient, 2026-05-18)** for the reasoning layer. 1.15B params, 40B tokens, hierarchical recurrent architecture, pretraining in 1 day for ~$1K, brain-inspired. This is a real candidate for the on-device "what should I remember, what should I forget" gate. [^1]

**New v7 problem D: the "OpenClaw" stack is now a known security target.** The arXiv survey "Security of OpenClaw Agents" (2605.25435) flags: skill poisoning, cognitive manipulation, multi-agent cascading failures, supply-chain vulnerabilities. [^2] This is a **real risk** for Dan Glasses since OpenClaw is our orchestration layer. **Fix:** read this paper, add a hard-mode of "every tool call has audit, every external message gets re-evaluated" to the OpenClaw policy.

### 2.2 The "RL feedback loop" in danlab-multimodal — honest assessment (v7 deep dive)

v6 already established the loop is hand-coded heuristic. v7 does the math: `len < 30` → -40; `[ERROR]` → -60; UI element identification → +10. Total range 0-100. **This is not RL in any meaningful sense.** It's a scoring function. The README is correct.

**What would it take to make it real RL?** v7 answer after reading the SIA paper carefully:

SIA (Hexo Labs + Oxford, 2026-05-29) [^3] proposes a feedback loop where:
- Meta-Agent generates the initial scaffold from a task spec
- Target Agent executes the task
- Feedback-Agent reads the trajectory and decides what to change
- Both Meta-Agent and Feedback-Agent run on Claude Sonnet 4.6
- Base model is gpt-oss-120b with LoRA rank 32, lr 4e-4
- Weight updates run on Modal H100s
- **Results: 3 tasks (LawBench, TriMul, denoising), 2 levers (harness-only, harness+weights)**

| Benchmark | Baseline (gpt-oss-120b) | SIA-H (harness) | SIA-W+H (harness+weights) | Claude Code (frozen, SOTA) |
|---|---|---|---|---|
| LawBench (top-1) | 13.5% | 19.3% | **70.1%** | 17.3% (45.0% old SOTA) |
| TriMul (speed ratio) | 1.00× | 1.10× | **14.02×** | 1.50× |
| denoising | 0.048 | 0.241 | (continuing…) | 0.232 |

**What this means for danlab-multimodal:** We could fork SIA, replace the model with LFM2.5-VL-450M (vision) + a small text reasoning model, replace the Meta-Agent/Feedback-Agent with HRM-Text 1B (if we can run it locally) or a cloud model, and run a "the harness is the prompt+loop" loop. But:

- The generalization is real only on LawBench (held-out). TriMul and denoising are train/test overlap.
- SIA is not magic. It is "frozen model, task-specific scaffold, task-specific weights". This is sophisticated fine-tuning + auto-prompt-engineering. It is **not** "the model is improving itself in the wild."
- It requires H100s and Claude Sonnet 4.6 as orchestrators. For Dan Glasses, that means cloud round-trips or an HRM-Text 1B + a local small reasoning model. The cloud bill matters.

**v7 concrete plan:** Fork SIA, swap in HRM-Text 1B as the local Feedback-Agent, run the harness-only loop (not weight updates) on a single VLM-improvement task (e.g., "describe this image better"). The weight-update path is gated on us having both a H100 and a privacy story for shipping fine-tuned weights. **This is a 2-month project, not a 2-week project.**

### 2.3 Power/performance tradeoffs — are LFM2.5-VL-450M, whisper.cpp, KittenTTS still the right choices?

**v7 verdict: yes for v1, no for v2.** Reasoning:

**LFM2.5-VL-450M** is still the best sub-500MB VLM for English/multi-lingual image description in 2026. SmolVLM-256M is smaller but lower quality. Gemma 3 270M is text-only. Liquid AI released LFM2.5 family April 11, 2026; the VL-450M is the 450M variant. Sub-250ms inference claims are GPU/CPU-hybrid. On Redax aarch64 we have **no measured number**. v6 says ~10–15s/frame on x86_64 CPU. v7 has no new measurement; the claim stands as a hypothesis.

**Whisper.cpp** is still the right STT for edge. Whisper large-v3 at 1.5B params has 2.7% WER on LibriSpeech test-clean, MIT-licensed. [^4] For our use case (push-to-talk, mostly clean mic input), `base.en` (74MB) is the right size class. v7 adds one caveat: the new Moonshine and Parakeet models from NVIDIA are faster on CPU and have similar WER for English. We should benchmark them on Redax when hardware lands.

**KittenTTS** at <25MB is the right size class for edge TTS. v7 adds a caveat: **Piper (Rhasspy)** at 15-65MB depending on voice quality is a real alternative with a larger community (more voices, more languages). If KittenTTS quality plateaus, we should evaluate Piper. v1 stays with KittenTTS; v2 should benchmark Piper.

**v7 new candidate: HRM-Text 1B for reasoning layer.** Not a VLM/STT/TTS — but a 1.15B reasoning model that could be the "what should I do" layer. [^1] Pre-RL, pre-RLHF. Just raw pretraining. We would need to fine-tune it for instruction following if we use it directly. But for "given these descriptions, what do I do next?" — it might work as-is.

### 2.4 OpenClaw orchestration — is TypeScript/Node the right choice?

**v7 verdict: yes, with explicit security caveats.**

OpenClaw is the right *shape* — gateway-first, channel-agnostic, MCP-native, policy-enforced. The TS/Node runtime is a real concern for resource-constrained deployment (idle ~0.5W, peak 0.8W per v6's power table), but on a laptop or paired-phone scenario this is fine.

**v7 concerns, fresh:**
1. **Security survey is out.** arXiv 2605.25435 (2026) catalogs: skill poisoning (malicious SKILL.md content), cognitive manipulation (memory poisoning), multi-agent cascading failures (when one agent's bug propagates), supply-chain vulnerabilities. [^2] **Action:** Read this paper in the next 7 days. Implement: hash-based tool-arg audit (already in os-toold), MCP server allowlist, message-redaction policy for outbound Telegram.
2. **OpenClaw 2026.6.5 release** is the latest. Earlier 2026.6.1 had a startup crash bug; 2026.6.5 fixed it. [^5] v6 already had the right pin. v7 confirms: keep pinned.
3. **MCP transport risk.** Zo MCP endpoint returns 405 on mcporter's `tools/list` (transport mismatch). The bridge shim is the right answer. v6 noted this; v7 has no new data point.

**v7 type-strict recommendation:** Add a `policy.deny_skills` file that lists any skill whose source-of-truth is outside `/home/workspace/dan-glasses/Skills/`. The skill ecosystem is the most likely attack surface, and "first-party only" is enforceable.

### 2.5 Two-brain problem: which model is canonical?

| Source | Says |
|---|---|
| `/home/workspace/AGENTS.md` (root) | "HRM-Text (1B) for reasoning, Whisper for STT" |
| `/home/workspace/dan-glasses/AGENTS.md` | "LFM2.5-VL-450M for vision" |
| PRD.md (canonical spec, 2026-04-17) | LFM2.5-VL-450M for vision, whisper.cpp STT, KittenTTS |

**v7 resolution:** These are not contradictory. They are layered:
- **Vision:** LFM2.5-VL-450M (canonical, in PRD)
- **STT:** whisper.cpp (canonical, in PRD)
- **TTS:** KittenTTS (canonical, in PRD)
- **Reasoning (new in v7):** HRM-Text 1B (proposed, not yet in canonical spec)

**Fix:** Add a section to PRD.md and dan-glasses/AGENTS.md that says: "Reasoning layer: HRM-Text 1B. Vision layer: LFM2.5-VL-450M. They are different layers." This is a docs fix, not a code change. **Own it: Dan1 or Dan2 within the next 7 days.**

---

## 3. AGI Landscape Research (2026)

### 3.1 State of AGI research — the leading approaches

**2026 is the year of "RSI" and "brake pedal" politics, not new architectures.** [^6][^7][^8][^9][^10] Three concrete threads:

1. **Anthropic's "brake pedal" (June 4-5, 2026).** Jack Clark + Marina Favaro blog post, then coverage in Axios, CNN, TechCrunch, Guardian, SCMP. [^6][^7][^8][^9][^10] Anthropic's claim: Mythos is "edging closer to recursive self-improvement" and the industry lacks a "brake pedal." They proposed a "temporary pause" on AI development. **This is real political backdrop for any self-improvement work.** Danlab's research integrity story matters more in this environment.

2. **SIA (Hexo Labs + Oxford, May 29, 2026).** First openly-described self-improving loop that edits both harness and weights. [^3] MIT-licensed. Results are real but bounded: 3 tasks, 2 levers, generalization only confirmed on LawBench. **The credible path from "heuristic" to "RL" is SIA or a fork of it.**

3. **Recursive Superintelligence (London, $650M raise, mid-May 2026).** $4.65B valuation, <30 employees, Tim Rocktaschel as co-founder (DeepMind), Richard Socher as co-founder. Predicted 2-year timeline to RSI. [^11] **This is a competitor in our space — not direct, but in the AGI race.**

**v7 implication for Danlab:** We are not building AGI. We are building on-device AI that *gets better over time*. SIA-like loops are the closest credible path. Fork SIA in month 1 of the AGI roadmap. The political risk of "Danlab building RSI" is low (we're small, not frontier), but the research integrity bar is high — every claim must be auditable.

### 3.2 Self-improving architectures — what has actually worked?

**v7 reality check (with evidence):**

| Approach | Who | What it does | Has it worked? | Evidence |
|---|---|---|---|---|
| Harness-only update | AutoResearch (Karpathy), AEL | Iterate on prompt/scaffold, freeze weights | Yes, on narrow tasks | Karpathy's GPT-2-scale improvements; AEL SWE-bench results |
| Weight update on task feedback | Most RLHF labs | PPO/DPO/GRPO on task-specific data | Yes, on chat/alignment | Standard practice; well-understood |
| **Harness + weights together (SIA)** | Hexo Labs + Oxford | Auto-loop that does both | **Yes on 3 tasks, narrow generalization** | LawBench 70.1% (held-out), TriMul 14× speed, denoising 0.241 |
| Full self-play / AlphaEvolve | DeepMind, Sakana | Code search + execution loop | Yes, on math/algorithm tasks | AlphaEvolve, FunSearch published results |
| **Brain-inspired hierarchical (HRM-Text)** | Sapient Intelligence | 1.15B params, 1K pretrain cost, hierarchical recurrent | **Pretrain yes; downstream tasks TBD** | [^1] |

**v7 takeaway for Danlab:** The SIA framing is the most actionable. Karpathy's autoresearcher is the simplest starting point (frozen model, prompt search). HRM-Text is a fascinating candidate for the on-device reasoning layer. AlphaEvolve is too compute-heavy.

### 3.3 Edge AI / on-device models — what's the SOTA for sub-500MB VLMs that actually work?

**v7 status (2026-06-17):**

- **LFM2.5-VL-450M** (Liquid AI, 2026-04-11): 450M params, 512×512 images, sub-250ms inference claim (likely hybrid CPU/GPU/NPU), GGUF + ONNX available. **Our pick.**
- **SmolVLM-256M** (HuggingFace): 256M params, smaller, lower quality. **Backup.**
- **Gemma 3 270M** (Google, 2026): Text-only. **Not applicable for VLM.**
- **Moondream 2** (vikhyatk): 2.7GB text+f16. **Too big for glasses.**
- **PaliGemma 2** (Google): 3B params. **Too big.**

**v7 conclusion:** LFM2.5-VL-450M is still the right call. v2 should watch for LFM3-VL (Liquid AI may release later in 2026), and for Google's "Gemma 4 VL" if it materializes.

For **on-device small LLMs (text)** the landscape is broader:
- **Gemma 4** (1B, 4B, 31B) — Google, strong open-weight
- **Llama 4** (Meta) — gappy licensing
- **Qwen 3** series — Alibaba, very strong
- **Nemotron 3** (NVIDIA, 2026-06-01) — 550B params, 55B active, open-weight, top US open-weight
- **HRM-Text 1B** (Sapient) — brain-inspired, pretrain only (no post-training)
- **Apple Intelligence on-device** — proprietary, not relevant for us

**v7 recommendation for on-device LLM in Dan Glasses:** **HRM-Text 1B for reasoning** (pretrain only is fine for our use case; we control the prompts) + **Gemma 4 1B for general text** (post-trained, instruction-following). Use HRM-Text when we need "given these observations, what should I do?" reasoning. Use Gemma 4 1B when we need natural language generation for TTS prep or chat.

### 3.4 Memory and continual learning — what approaches exist?

**v7 landscape (with active research):**

- **IAAR-Shanghai/Awesome-AI-Memory** (989 stars, 245 commits, June 2026) [^12] is the canonical index. Mem0, Letta (MemGPT), MemX, MemA, MemPalace, A-Mem, HippoRAG, LightMem, MemoRAG, MemInsight, MemEngine. Each has a different take on episodic/semantic/procedural, vector/graph/hybrid.

- **The SOTA on LongMemEval (2026)** is contested. Per industry reports, plain vector + typed schema (e.g., Mem0) still beats graph-hybrids on most recall tasks. The graph is useful for *reasoning over* memory, not for *recalling* memory. **This validates our memoryd design** (SQLite + vectors + 3 memory types). We should add a typed-schema layer if we want to push past Mem0.

- **MemPrivacy (MemTensor + HONOR + Tongji, 2026-05-18)** [^13] is the most relevant 2026 paper for our threat model. Edge-cloud reversible pseudonymization: keep raw data on edge, send only tokenized references to cloud. This is exactly what Dan Glasses needs if we ever add a cloud memory sync (e.g., for cross-device).

- **Continual learning without forgetting** is still mostly an unsolved research problem. The SOTA is "rehearsal" (keep a small buffer of past data) + "regularization" (penalize weight changes on important params). Not ready for production at 1B scale.

**v7 takeaway:** Our memoryd is a v1-correct design. The next 6 months should be: add typed-schema, add MemPrivacy-style edge-local-only guarantee, add a graph layer for reasoning-over-memory (only if LongMemEval scores demand it). Do not chase the latest "MemX" without benchmarking.

### 3.5 Multimodal fusion — how are the best systems combining vision, audio, and text?

**v7 landscape:** Most frontier systems (Gemini 3, Claude Opus 4.6, GPT-5.5) use **early fusion** — vision, audio, and text are tokenized at the input layer and processed by a single transformer. This is the highest-quality but heaviest approach. **Not viable for our wearable.**

For **edge/lightweight** the pattern is:
- **Late fusion with shared embedding space.** Vision encoder (e.g., SigLIP) produces image tokens; audio encoder (e.g., Whisper) produces audio tokens; text tokenizer produces text tokens. A small "fuser" LLM (Gemma 4 1B, HRM-Text 1B) takes all three.
- **Cascaded (modality-specialist).** Whisper handles audio → text. VLM handles image → text. Text-only LLM takes both texts. This is **what we already have.** It's the lowest-quality but the only viable one for our power budget.

**v7 verdict for Dan Glasses:** Stay with cascaded for v1/v2. The end-to-end latency is bounded (5–10s for VLM, 1–2s for whisper, 1s for HRM-Text reasoning, <500ms for TTS = 7-14s total). For proactive/interrupt scenarios we need a *fast path*: cascade with a small LLM (Gemma 4 1B) is the fast path, full reasoning (HRM-Text) is the slow path. Watch for the "multimodal flash" tier that may emerge in 2026.

### 3.6 Model compression — what's working?

**v7 SOTA:**
- **Quantization (Q4/Q5/Q8)** is well-understood. LFM2.5-VL-450M Q4_0 at 209MB. Whisper base.en Q5_0 at ~74MB. KittenTTS is already at <25MB. **No breakthroughs here, just continuous improvement.**
- **Distillation (student-teacher)** is the frontier. SmolVLM-256M is a distilled VLM. HRM-Text 1B is *not* distilled — it's a fresh architecture with 1K pretrain cost. **Implication: a "student HRM" trained to mimic a teacher frontier model could be the next leap.**
- **Pruning** (structured, semi-structured) is mid-SOTA. Useful for MoE models (Nemotron 3) less so for dense ones.
- **Speculative decoding** is the inference-time win. 1.5–2× speedup on most models.
- **KV cache compression** is the latest frontier. Methods like VLCache (arXiv 2512.12977, Dec 2025) claim 1.2-16× speedup on VLMs by caching vision encoder outputs. **v6 had this as a paper pick; v7 confirms it's production-ready in SGLang.**

**v7 takeaway:** Q4_0 for vision, Q5_0 for STT, no compression for TTS (already tiny). Speculative decoding worth exploring in v2. KV cache compression: defer.

---

## 4. Competitive and Market Research

### 4.1 AI Wearables — the 2026 landscape

**The market is real and growing fast:**
- **Global smart glasses market**: $2.34B in 2024, projected $7.14B by 2034, 11.8% CAGR. [^14]
- **Smart glasses market grew 139% YoY in H2 2025.** [^15]
- **Meta holds 76% market share.** [^15]

**Players (v7):**

| Player | Product | Status (2026-06) | On-device AI? | Price |
|---|---|---|---|---|
| **Meta Ray-Ban Display** | Smart glasses with in-lens display | Shipping, "much smarter AI powered by Meta's Muse Spark model" coming summer 2026 [^16] | No — cloud to phone | $799 |
| **Meta Ray-Ban Gen 3** | No display, camera + AI | Shipping, fixes battery/camera/Live AI [^15] | No — cloud to phone | $299-499 |
| **Apple Glasses (N50)** | Smart glasses | **Delayed to late 2027** [^17][^18][^19] | Likely hybrid | $200-500 est |
| **Google AI Glasses** | Android XR | Hitting market in 2026 [^20] | Hybrid (on-device Gemini + cloud) | TBD |
| **Even Realities G2** | Display-only smart glasses (no camera) | Shipping [^21] | Yes (on-device AI assistant) | $399-599 |
| **Brilliant Labs Halo** | Open-source AI glasses | Shipping [^22] | Yes (on-device + Noa cloud) | ~$400 |
| **Rokid AI Glasses** | AR display | Shipping | Hybrid | TBD |
| **VIVE Eagle** | AI glasses | Shipping | Hybrid | TBD |
| **Qwen Glasses** | AI glasses (Alibaba) | Shipping | Hybrid | TBD |
| **Vizoso / ROG XREAL R1** | AR gaming | Shipping | Hybrid | TBD |

**v7 take:** **There is no "open-source, on-device, privacy-first AI glasses" in 2026.** Meta, Apple, Google, Samsung are all closed and cloud-coupled. Brilliant Labs is closest to "open" but still has Noa as a cloud component. Even Realities G2 is "display-only, no camera" — privacy-first but limited.

**Dan Glasses' positioning:** On-device only, open-source, privacy-first, with a true always-on multimodal model stack. **This is an open lane.** We are not competing with Meta on fashion; we are competing on "your AI lives on your face, no cloud, no data leakage, fully auditable."

**Apple delay to late 2027 is a gift.** [^17][^18] That gives us 18 months of uncontested first-mover positioning in the "open, on-device, privacy-first" lane. **Use the runway.**

### 4.2 Open-source AI companion projects

**v7 landscape:**

- **OpenClaw** (gateway/agent framework, TS/Node, 345K+ stars) — our orchestration choice. **Concern: security survey is out.** [^2]
- **Hermes Agent** (agent-first runtime, 140K+ stars) — alternative to OpenClaw.
- **Letta / MemGPT** (memory-first agents) — relevant for our memoryd work.
- **Open LLM VTuber** (open-source AI companion) — different form factor.
- **LibreChat** (multi-model chat) — relevant for our Tauri shell if we ever build a chat UI.
- **OpenHands / Open Interpreter** (CLI coding agents) — relevant for toold but different domain.
- **abmind** (drop-in memory engine for OpenClaw, Apache 2.0) — interesting, could be a future memoryd replacement.
- **Recursive Superintelligence** (closed, $4.65B valuation, 2-year RSI promise) — competitor, not collaborator.

**v7 takeaway:** We're not building in a vacuum. The "open, local, privacy-first" lane has multiple projects. We differentiate on **hardware form factor** (glasses) + **on-device multimodal models** (no other project runs LFM2.5-VL-450M + HRM-Text 1B + whisper.cpp + KittenTTS on-device).

### 4.3 Privacy-preserving AI — how does Dan Glasses position?

**v7 landscape:**
- **Apple's Private Cloud Compute** (PCC, 2024-2026). Apple Intelligence on-device + PCC for heavier tasks. Cryptographic attestation. **The high water mark for privacy-preserving AI.**
- **MemPrivacy** (2026-05-18, MemTensor + HONOR + Tongji) [^13] — edge-cloud reversible pseudonymization. Relevant if we add cloud sync.
- **Differential privacy** (standard, but mostly research).
- **Fully on-device** (us, Brilliant Labs Halo, Even Realities G2).
- **OpenClaw security survey** [^2] — flags risks, no answers.

**v7 positioning for Dan Glasses:** "Fully on-device, no cloud, fully auditable open source, AGI research lab driven (not Big Tech driven)." This is the strongest privacy position. We are not racing Apple on PCC; we are saying "we don't need a cloud at all." Use this aggressively in marketing and in research papers.

---

## 5. Technical Deep-Dive 1: Edge VLM Optimization (Option B)

### 5.1 The state of the art

**VLM inference is dominated by two stages:**
1. **Vision encoder** (SigLIP / CLIP / DINOv2 variants) — converts image to tokens. Bounded cost.
2. **Text decoder** (LLM) — generates the response. **This is the bottleneck.**

**v7 quantitative picture:**

| Model | Params | Encoder | Decoder | Image→Tokens | Tokens/Response | CPU latency (x86_64) | CPU latency (aarch64 est) |
|---|---|---|---|---|---|---|---|
| LFM2.5-VL-450M Q4_0 | 450M | SigLIP2 NaFlex | LFM2.5-base | ~256-400 | 50-100 | 10-15s | 25-40s est |
| SmolVLM-256M Q4_K_M | 256M | SigLIP | SmolLM2-135M | ~256 | 50-80 | 26s | 50s est |
| Moondream 2 f16 | 2.7GB | SigLIP | Phi-1.5 | ~256 | 50-100 | 5-8s | 15-25s est |
| PaliGemma 2 3B | 3B | SigLIP | Gemma 2 | ~256 | 50-100 | 25-40s | 60-100s est |

**v7 verdict on power:** VLM is the dominant power event. Per v6 power table, LFM2.5-VL-450M is 3-8W on inference. For Redax aarch64, expect 4-10W (slower CPU, possibly NPU offload). **Need measurement on real hardware before any power-budget claim is final.**

### 5.2 Quantization, distillation, hardware acceleration — what actually works?

**Quantization (v7 SOTA):**
- Q4_0: ~5% quality loss, 4× size reduction. **Default for our deployment.**
- Q5_0: ~2% quality loss, 3.3× size reduction. **For laptop prototype.**
- Q8_0: ~1% quality loss, 2× size reduction. **For quality-critical paths only.**
- IQ-series (importance-weighted): best quality/size ratio for very small quants.

**Distillation (v7 SOTA):**
- SmolVLM-256M is a distilled VLM. The student is 256M, the teacher is unspecified but likely 1-3B.
- HRM-Text 1B is **not** distilled — it's a fresh architecture. This is unusual. The implication is that for our "student HRM" future, we should distill from a frontier model (Claude Opus 4.6, GPT-5.5) into a hierarchical recurrent student, not from a transformer student.

**Hardware acceleration (v7 SOTA):**
- **Qualcomm Hexagon NPU** (Dragonwing IQ-9075, IQ-9): demonstrated VLM inference in Innodisk demos. [^23]
- **Intel Panther Lake** (180 TOPS, CPU+GPU+NPU): 2026 platform.
- **Apple Neural Engine** (M4, 38 TOPS): closed ecosystem.
- **Ambiq Apollo** (sub-mW always-on): the power-efficiency leader for wearables.
- **NPU-only quantization is the gap.** Current VLMs ship GGUF (CPU/GPU) or ONNX (CPU/NPU). NPU-only with proper quantization is real but the toolchain is fragmented. **v2 should explore NPU offload.**

### 5.3 v7 verdict for Dan Glasses VLM strategy

- **LFM2.5-VL-450M Q4_0 stays as the primary vision model.** Sub-250MB encoder+decoder+projector.
- **SmolVLM-256M as thermal fallback.** Lower quality, lower power, used when battery <20% or temperature >threshold.
- **HRM-Text 1B as the reasoning layer** (new in v7). 1.15B params, brain-inspired, $1K pretrain. Tied to vision via the descriptions published by LFM2.5-VL-450M.
- **Bench: Parakeet TDT (NVIDIA)** and **Moonshine** for STT. Not urgent (whisper.cpp is solid) but do it in v2.
- **Bench: Piper (Rhasspy)** for TTS. Not urgent.
- **v2 add: NPU offload path.** Use the existing GGUF/llama.cpp + a custom EP for the target NPU. Start with Qualcomm IQ-9 (Android XR alignment).

---

## 6. Technical Deep-Dive 2: Memory Architectures for AI Companions (Option C)

### 6.1 The 2026 state of the art

**v7 landscape (with benchmarks):**

| System | Type | Strength | Weakness | When to use |
|---|---|---|---|---|
| **Mem0** (2025→2026) | Vector + LLM extraction | Strong on LongMemEval, simple | Cloud-LLM dependency for extraction | If you have GPT/Claude in loop |
| **Letta (MemGPT)** | Hierarchical memory + paging | Open-source, self-host | Complex setup, slow | Long-running agents with rich context |
| **MemX** (2026) | Graph + vectors | Multi-relation reasoning | Graph overhead | When relations matter (us: people, places) |
| **MemA / A-Mem** | Zettelkasten-inspired | Notes that link to notes | Smaller community | When knowledge evolves over time |
| **HippoRAG** (2026) | Hippocampal-inspired RAG | SOTA on multi-hop QA | Research-grade | Research prototypes |
| **MemPrivacy** (2026-05-18) | Edge-cloud pseudonymization | Privacy guarantee | New, less battle-tested | When cloud sync needed |
| **Our memoryd** (SQLite + MiniLM + 3 memory types) | Simple vector + typed | Auditable, low-resource, no cloud | No relation graph, no extraction LLM | **v1 correct; v2 add typed-schema + extraction** |

**v7 verdict on the "is graph needed?" question:** The 2026 evidence is mixed. Memanto-style typed-vector approaches still win on LongMemEval. Graph is useful for *reasoning over* memory, not for *recalling* it. **Don't add a graph layer unless benchmarks demand it.**

### 6.2 The 7-relation-type debate (carried from v6)

v6 proposed 7 memory relation types (person, place, event, object, time, preference, intention). v7 confirms: this is still a sound schema. But:
- v7 finding: **the value is in the *type system* (typed schema for filtering), not in the graph edges.** A vector store with a `type` filter is 90% of what a graph gives us. The remaining 10% (multi-hop reasoning) we don't need yet.
- **Action:** Add a `type` index on our vector store. Migrate `metadata.type` from string to enum. ~3 days of work.

### 6.3 v7 memory roadmap for Dan Glasses

**v1 (now):** SQLite + vectors + 3 types. Auditable, no cloud.
**v1.5 (next 3 months):** Add typed-schema with enum types. Add LLM-extraction for semantic memory (use HRM-Text 1B or a small Gemma 4 1B for this).
**v2 (6-12 months):** Add MemPrivacy-style edge-local-only guarantee. Add cross-device sync with reversible pseudonymization.
**v3 (12+ months):** Add a graph layer *only* if LongMemEval on the Dan Glasses dataset shows multi-hop reasoning is needed. Bet: it won't be.

---

## 7. Technical Deep-Dive 3: Proactive AI (Option D)

### 7.1 The 2026 state of the art

**v7 landscape (proactive agent research is real in 2026):**

- **ProAgentBench** (arXiv 2602.04482, Feb 2026) — first real-world benchmark for proactive agents. ~14K instances, 4 difficulty tiers, scores on anticipation, intervention, and helpfulness.
- **ProAct** (arXiv 2605.25971, May 2026) — turns idle compute into anticipation. Agent decides when to act without explicit prompt.
- **ProActor** (ACL 2026) — first RL-trained proactive agent using GRPO with stage-aware rewards.
- **MemPalace** (2026) — uses memory + spatial reasoning to anticipate user needs.

**v7 reality check:** Proactive AI in 2026 is at the same place that LLM agents were in 2023 — research benchmarks, narrow tasks, no clear winner. **For Dan Glasses, this is an opportunity, not a threat.** No consumer product is doing proactive AI well yet. The closest is Meta's "Live AI" on Ray-Ban, which is gated on the user pressing a button.

### 7.2 What would proactive AI look like for Dan Glasses?

**v7 sketch (concrete enough to implement):**

```python
class ProactiveEngine:
    def __init__(self, memoryd, audiod, perceptiond, hr):
        self.memory = memoryd  # episodic/semantic/procedural
        self.audio = audiod    # last transcript, current speaker
        self.vision = perceptiond  # last 3 descriptions
        self.hr = hr           # HRM-Text 1B (local, 1.15B)
    
    def tick(self, ctx):
        # Only consider proactive action in 'idle' or 'watchful' mode
        if ctx.mode in ("active", "burst"):
            return None
        
        # Build a small "situation" embedding from recent context
        sit = self.build_situation(ctx.recent_observations)
        
        # Ask HRM-Text 1B: should I speak?
        decision = self.hr.should_proactively_act(sit, ctx.user_state)
        
        if decision.action == "speak":
            return self.synthesize(decision.text)
        return None
```

**v7 design constraints:**
- **Bounded cost.** Proactive decisions must be cheap. HRM-Text 1B at Q4_0 (~600MB) is the cheapest viable reasoning model in 2026. Even so, "should I speak?" ticks at 1Hz would burn 1.5W continuous. **Tie proactive ticks to events, not time.** (e.g., after audiod transcript pause, after perceptiond salient frame, after memoryd recall).
- **User override.** Every proactive utterance must be dismissable with a single word ("dismiss" / "stop"). This is a privacy + UX requirement.
- **Bounded frequency.** At most one proactive utterance per 10 minutes in watchful mode, one per 2 minutes in active mode. Hard cap.

### 7.3 v7 proactive roadmap for Dan Glasses

**v1 (now):** Reactive only. Await wake word or push-to-talk. Proactive = off.
**v1.5 (3-6 months):** Reactive + scheduled (cron) + memory-triggered (e.g., "you talked about X yesterday, want to continue?"). Bounded by user opt-in.
**v2 (6-12 months):** Reactive + ProactiveEngine v1 (HRM-Text 1B-based). Benchmark on a custom Dan Glasses eval set.
**v3 (12-24 months):** Reactive + ProactiveEngine v2 (with MemPrivacy sync). Open the proactive eval set as a research contribution.

---

## 8. The v7 Synthesis: Three Forces

After this research, I see three forces converging in 2026 that Danlab should respond to:

1. **The RSI/SIA moment.** Anthropic's brake pedal, SIA, Recursive Superintelligence. The world is paying attention. **Our response: fork SIA, contribute back, do it with research integrity.** Don't claim "RL" until we have it. Don't claim "AGI" until we have it. **Our existing honesty in danlab-multimodal README is a feature, not a bug.**

2. **The on-device moment.** Apple delayed to 2027. Meta+Google+Samsung are cloud-coupled. Brilliant Labs is closest to open but still cloud-hybrid. **Our response: build the most fully-on-device, privacy-first, open-source AI glasses. Use the 18-month runway.**

3. **The reasoning layer moment.** HRM-Text 1B is a 1.15B brain-inspired reasoning model trained for $1K. This is the missing layer in Dan Glasses. **Our response: integrate HRM-Text 1B for the "what should I do?" layer.** This is concrete, achievable in 3 months, and differentiates us from every other wearable.

These three forces define the AGI roadmap. The rest is plumbing.

---

## 9. v7 Open Questions

1. **What is HRM-Text 1B's inference latency on aarch64?** Sapient doesn't publish this. We need to measure on Redax.
2. **Is there a "Student HRM" or "HRM-VL"?** Sapient has not announced a vision-language HRM. If they don't, we may need to fine-tune HRM-Text 1B for our use case.
3. **What is Meta Muse Spark's on-device footprint?** Meta is keeping this proprietary. We can't benchmark. But if Meta is shipping "on-device" Muse Spark at all, the bar moves.
4. **What is the actual retail price of OpenClaw-Pin-style form factor?** We have a Tauri app. The form factor is open. Hardware choices (camera module, mic array, NPU chip) will determine unit cost.
5. **Does somdipto want to fork SIA now, or wait until after the wearable prototype is hardware-validated?** The fork can happen in parallel. The decision is "do we have GPU/H100 budget for the weights-updated version?"

---

## 10. v7 Recommendations (TL;DR)

1. **Resolve the two-brain contradiction in AGENTS.md.** HRM-Text 1B is for reasoning, LFM2.5-VL-450M is for vision. Both are right.
2. **Integrate HRM-Text 1B as the reasoning layer** in Dan Glasses. Pretrain-only is fine; we control the prompts. 3-month project.
3. **Fork SIA in month 1 of the AGI roadmap.** Use HRM-Text 1B as the local Feedback-Agent. Use LFM2.5-VL-450M as the target vision model. Ship a "self-improving danlab-multimodal" by end of Q3 2026.
4. **Add MemPrivacy-style edge-local-only guarantee** to memoryd. Read the MemPrivacy paper (MemTensor, 2026-05-18).
5. **Read the OpenClaw security survey** (arXiv 2605.25435) and add a `policy.deny_skills` allowlist.
6. **Position aggressively on the 18-month Apple-delay runway** as the open, on-device, privacy-first AI glasses. Marketing paper + AGI-roadmap paper.
7. **Power measurement on aarch64 is the single hardest blocker** for the wearable track. Get Redax hardware. Profile VLM, STT, TTS, and the new HRM-Text inference.

---

## References

[^1]: Sapient Intelligence, "Introducing HRM-Text" (2026-05-18). https://sapient.inc/introducing-hrm-text
[^2]: "Security of OpenClaw Agents: Fundamentals, Threats, and Countermeasures", arXiv:2605.25435 (2026).
[^3]: Hexo Labs + University of Oxford, "SIA: Self-Improving AI with Harness & Weight Updates" (2026-05-29). https://github.com/hexo-ai/sia. See critical analysis: https://zenn.dev/shark_same_same/articles/5a6e47f87106c2
[^4]: novascribe, "How Accurate Is Whisper in 2026? WER Benchmarks & Sources." https://novascribe.ai/how-accurate-is-whisper
[^5]: OpenClaw 2026.6.5 release notes (2026-06-05). Referenced in OpenClaw community channels.
[^6]: Axios, "Anthropic warns AI could soon help build its own successors" (2026-06-04). https://www.axios.com/2026/06/04/anthropic-warns-ai-build-successors
[^7]: CNN, "Anthropic warns that AI will soon be able to improve itself without human intervention" (2026-06-05). https://www.cnn.com/2026/06/05/business/anthropic-calls-for-ai-brake-pedal
[^8]: The Guardian, "Anthropic urges 'temporary pause' on AI development to discuss risks" (2026-06-05). https://www.theguardian.com/technology/2026/jun/05/anthropic-urges-temporary-pause-on-ai-development-to-discuss-risks
[^9]: TechCrunch, "RSI is the new AGI — and it's just as hard to pin down" (2026-05-28). https://techcrunch.com/2026/05/28/rsi-is-the-new-agi-and-its-just-as-hard-to-pin-down/
[^10]: Forbes, "Anthropic Declares That The Next Big Step For Humans And AI Is AI That Builds Itself Via Recursive Self-Improvement" (2026-06-07). https://www.forbes.com/sites/lanceeliot/2026/06/07/anthropic-declares-that-the-next-big-step-for-humans-and-ai-is-ai-that-builds-itself-via-recursive-self-improvement/
[^11]: Crypto Briefing, "Recursive co-founder Tim Rocktaschel predicts self-improving AI in two years" (mid-May 2026). https://cryptobriefing.com/recursive-self-improving-ai-two-years/
[^12]: IAAR-Shanghai/Awesome-AI-Memory (Jun 2026). https://github.com/IAAR-Shanghai/Awesome-AI-Memory
[^13]: MemTensor + HONOR + Tongji University, "MemPrivacy: An Edge-Cloud Framework that Uses Local Reversible Pseudonymization" (2026-05-18). https://www.marktechpost.com/2026/05/18/meet-memprivacy-an-edge-cloud-framework-that-uses-local-reversible-pseudonymization-to-protect-user-data-without-breaking-memory-utility
[^14]: Accio Business, "Meta Smart Glasses Trends 2026" — citing 11.8% CAGR, $2.34B→$7.14B market.
[^15]: iDevice, "Meta Ray-Ban Gen 3 Release Date, Price & Features (2026)." https://idevice.com/smart-glasses/meta-ray-ban/roadmap
[^16]: Metav3rse / Instagram coverage of Meta Ray-Ban Display updates (2026-05-23). Cites "Meta Muse Spark model" coming summer 2026.
[^17]: CNET, "Apple's Smart Glasses Reportedly Delayed Until Late 2027" (2026-05-31). https://www.cnet.com/tech/mobile/apple-smart-glasses-development-bumps-reported-delay
[^18]: Gizmodo, "Apple Is Coming for Meta's Privacy-Invading Lunch With Its Own Smart Glasses in Late 2027" (2026). https://gizmodo.com/apple-is-officially-coming-for-metas-privacy-invading-lunch-with-its-own-smart-glasses-in-late-2027-2000765491
[^19]: AppleInsider, "Longtime leaker joins others in saying Apple Glasses won't arrive until late 2027" (2026-05-31). https://appleinsider.com/articles/26/05/31/longtime-leaker-joins-others-in-saying-apple-glasses-wont-arrive-until-late-2027
[^20]: Moor Insights & Strategy, "Google I/O 2026 — More Details on AI and AR Glasses, Including Project Aura" (2026). https://moorinsightsstrategy.com/research-notes/google-i-o-2026-more-details-on-ai-and-ar-glasses-including-project-aura
[^21]: the-gadgeteer, "Best Smart Glasses 2026: 10 AI and AR Picks for Every Budget" (2026-06-13). https://the-gadgeteer.com/2026/06/13/smart-glasses-worth-buying-2026
[^22]: Quasa, "Brilliant Labs Halo: Open-Source AI Glasses for Curious Minds" (2026). https://quasa.io/video/brilliant-labs-halo-open-source-ai-glasses-for-curious-minds
[^23]: Innodisk COMPUTEX 2026 demos (2026-05-25) — Qualcomm Dragonwing IQ-9075 VLM demo.
[^24]: Critical analysis of SIA paper: https://zenn.dev/shark_same_same/articles/5a6e47f87106c2 (Japanese, but provides the most rigorous independent assessment of SIA's actual vs. claimed results).

---

*End of v7 research report. Companion artifacts: dan2-architecture-review.md, dan2-model-analysis.md, dan2-agi-roadmap.md, dan2-papers-to-read.md.*
**LFM2.5-VL-450M:** Liquid AI's release 2026-04-11 is still the best sub-1B VLM for edge in mid-2026. SigLIP2 NaFlex encoder, 32K context, GGUF + ONNX. [^4] It is correct for v1. For v2, watch the new **LFM2.5-1.2B-Thinking** (referenced in danlab-multimodal README as the future Feedback-Agent option) and the **HRM-Text 1B** (Sapient, 2026-05-18) for reasoning tasks — but neither replaces vision, they complement it. **Decision: keep LFM2.5-VL-450M for vision. Add HRM-Text 1B for reasoning. v2 question: switch to LFM2.5-1.2B-Thinking for higher quality when hardware allows.**

**whisper.cpp:** Still production-grade in 2026. The Whisper Large-v3 (1.5B) is competitive with Deepgram Nova-3, AssemblyAI Universal-2, Google Chirp 2 on the Open ASR Leaderboard at 2.7% WER on LibriSpeech test-clean. [^5] For Dan Glasses, `base.en` (74MB) is the right call — `tiny.en` (39MB) is too lossy in noisy environments, `small.en` (244MB) is overkill for PTT use. **Decision: keep `base.en` for v1. v2 may add a wake-word model (e.g., openWakeWord with Picovoice Porcupine) when always-listening becomes a power-feasible option.**

**KittenTTS:** v6 said "verify license". v7: KittenTTS is Apache-2.0 (was unclear in v6). The 25MB / 8-voice / multi-model lineup (mini/base/medium/large) gives good coverage. **Decision: keep KittenTTS for v1. v2 question: replace with streaming TTS (e.g., a VITS variant) for chunked synthesis during long-form speech.** Continuous on-device TTS consumes measurably more energy than voice-triggered (15-25% battery reduction in published studies). [^6]

**v7 addition — the real question is "where does the LLM live?"** In v1, it doesn't — the agent loop is on OpenClaw with a cloud LLM. For Dan Glasses to be a true "local AGI" device (which is the thesis of danlab.dev), the LLM has to be on-device. **v2 architecture: HRM-Text 1B for on-device reasoning + a 1-3B chat model (LFM2.5-1.2B or Gemma 4 1B) for natural language generation + a 1B vision model (LFM2.5-VL-450M) for perception. All three fit in 4-6GB total memory with quantization. The wearable is a multimodal small-model swarm, not a single model.**

### 2.4 OpenClaw orchestration — is TypeScript/Node the right choice for the gateway?

v6 said: "OpenClaw is TS/Node — not Rust, but accepted as orchestration layer. Rust daemons for hot paths." v7 says: **this is correct, and the v7 disclosure of OpenClaw-specific security risks is the more pressing issue than language choice.**

OpenClaw vs. Hermes comparison (fwdslash, 2026) [^7]: OpenClaw is gateway-first (25+ messaging channels, single Node process, 345K+ stars), Hermes is agent-first (140K+ stars in 3 months, in-built learning loop). The key v7 trade-off: **OpenClaw is bigger but has 138+ CVEs in published audits; Hermes is smaller and security-cleaner but lacks multi-channel reach.** For Dan Glasses, the multi-channel reach (Telegram is the primary control plane per dan1.md) is the lock-in for OpenClaw.

**v7 fix list for OpenClaw:**
1. **Read the arXiv 2605.25435 paper** and adopt the audit hook pattern: every tool call gets a JSONL audit entry with input, output, redacted content, and policy decision.
2. **Add a content-redaction layer** to the Telegram channel. The skill-poisoning threat model is real — a malicious Telegram message can craft tool calls that look legit.
3. **Replace the broken `mcporter` OpenClaw-Zo bridge** (HTTP 405 issue) with the working `zo-mcp-bridge` (stdio MCP) — already done in v6.
4. **Pin OpenClaw version** and subscribe to CVE feeds. The 138+ CVE count is from a 2026 audit; it includes stale issues. Run `npm audit` on every update.

### 2.5 Root workspace contradiction — HRM-Text 1B vs LFM2.5-VL-450M

Resolved in v6: **both, different roles.**
- LFM2.5-VL-450M → vision (perceptiond)
- HRM-Text 1B → reasoning (new, not yet integrated)
- Gemma 4 1B (or similar) → chat / NLG (new, not yet integrated)

This is a 3-model swarm. The wearable runs all three locally with quantization. The cloud LLM is for development and as a fallback. **This is the v2 architecture. v1 is still OpenClaw + cloud LLM for the agent loop.**

---

## 3. AGI Landscape Research (2026)

### 3.1 State of AGI research in 2026

The 2026 AGI conversation has shifted from "how big can the model get" to "how does the model improve itself". Five leading approaches:

1. **Recursive self-improvement (RSI) — frontier lab consensus.** Anthropic (Jun 4–7, 2026) publicly warned that AI will soon build its own successors, called for a "brake pedal" or temporary pause, and Jack Clark put 60% probability on full RSI by end of 2028. [^8] OpenAI (GPT-5.5), DeepMind (Gemini 3 Flash, SWE-bench 78%), and Anthropic (Claude Mythos 5) are all racing on this. The Recursive Superintelligence startup (London, mid-May 2026) raised $650M at $4.65B valuation to build self-improving AI in 2 years. [^9] **The "AGI is scaling" narrative is dead. The new narrative is "AGI is recursive improvement".**

2. **Self-improving agent frameworks (SIA).** Hexo Labs + Oxford released SIA on 2026-05-29 under MIT license. The first open-source framework that edits both the harness and the weights in a self-improving loop. [^3] This is the most credible open-source path for small teams to participate in RSI research. Karpathy's Auto-Research (limited to GPT-2 scale), AlphaEvolve (Google DeepMind), and RE-Bench are the other notable efforts. [^10]

3. **Small specialist models + routing.** The "frontier model" is becoming a multi-model swarm with intelligent routing. Liquid AI's LFM2 series (1.2B, 450M VL), Sapient's HRM-Text 1B, Google's Gemma 4 family, Apple's on-device 3B, and Meta's Llama 4 / Muse Spark are all betting on the 1-3B model class for edge. [^11] The 100B+ parameter regime is reserved for data center work.

4. **Proactive AI.** ProAgentBench (arXiv 2602.04482), ProAct (arXiv 2605.25971), and ProActor (ACL 2026) are the first real benchmarks and frameworks for AI that initiates rather than responds. [^12] This is critical for Dan Glasses because "smart glasses you have to ask" are useless — the glasses need to surface context proactively.

5. **Memory as a first-class citizen.** Mem0 (3.7M+ downloads), Letta (formerly MemGPT, persistent memory across sessions), MemX (hierarchical 7-relation-type graphs), MemPrivacy (edge-cloud reversible pseudonymization, 2026-05-18), and the IAAR-Shanghai Awesome-AI-Memory list (989+ stars) are all evidence that the field has moved past "stuff context into a 1M-token window" into structured memory architectures. [^13] [^14] [^15]

### 3.2 Self-improving architectures — what has actually worked?

**Evidence-based ranking (v7):**

1. **Harness-only auto-search (SIA-H, Auto-Research, AEL).** This is the most reproducible and least expensive. A frozen model + an auto-tuned prompt + tool selection = 2-3× task improvement. This is **the right starting point for Dan Glasses.** Don't try to update weights in v1.
2. **Harness + weight updates on a fixed task (SIA-W+H).** Powerful but specialized. SIA demonstrated 70% on LawBench (vs. 17% Claude Code, 45% old SOTA) by doing 50+ LoRA updates on a frozen 120B model. [^3] This requires H100s and a clean verifier. Not feasible for Dan Glasses in 2026.
3. **Full self-play / RL on tool use (RHO, RLVR).** RHO (Retrospective Harness Optimization, arXiv 2606.05922) is label-free. The Verge covered RHO and Meta-Harness (May 2026) as the most promising harness-RL approaches. RHO gets 0.78 SWE-Bench Pro at 1 round vs. Meta-Harness 0.60 at 1 round (0.80 at 10 rounds with 3× compute). **This is the playbook for danlab-multimodal in 2026.**
4. **Architecture search (AlphaEvolve, RE-Bench).** Real, but only Google DeepMind has the compute to do it well. Not actionable for us.

**v7 recommendation:** SIA-fork + harness-only on a single VLM-improvement task. The weight path is gated on a real verifier and a H100 budget.

### 3.3 Edge AI / on-device models — SOTA for sub-500MB VLMs that actually work

| Model | Size | Encoder | Released | Verdict |
|---|---|---|---|---|
| **LFM2.5-VL-450M** | 450M (Q4: 209MB) | SigLIP2 NaFlex | 2026-04-11 | Best for edge VL in 2026. v1 default. |
| **SmolVLM-256M** | 256M (Q4: 120MB + 182MB mmproj) | SigLIP | 2024 | Fallback only. LFM2.5 outperforms. |
| **Gemma 3 270M** | 270M | None (text-only) | 2024-2025 | No vision support in GGUF. **Don't use for vision.** |
| **Gemma 4 1B** | 1B | TBD | 2026-Q2 | Strong candidate for chat/NLG role in v2. |
| **HRM-Text 1B** | 1.15B (Sapient) | Hierarchical recurrent | 2026-05-18 | Reasoning layer candidate in v2. [^1] |
| **Moondream2** | 2.7GB | SigLIP | 2024 | Legacy. Too big for v1. |

**v7 conclusion:** the 2026 SOTA for sub-500MB VLM is **LFM2.5-VL-450M**. The next jump will come from a 1B VLM with better reasoning integration, not from a smaller model. Watch the Liquid AI LFM2.5-1.2B-Thinking variant. v1 ships with 450M; v2 targets 1.2B.

### 3.4 Memory and continual learning — what approaches exist?

The v7 landscape has 5 distinct approaches:

1. **Pure vector + typed schema.** Mem0 (default), Memanto (arXiv 2604.22085). Memanto is the most interesting 2026 result: 13-category typed schema beats graph hybrids on LongMemEval. **The graph is unnecessary; the type system is the leverage.** This challenges the v6 recommendation to use MemX 7-relation-type graphs.
2. **Hierarchical memory with paging.** Letta (formerly MemGPT) — paginates context between core memory, archival memory, and recall memory. Most production-deployed.
3. **Knowledge graph + vector hybrid.** MemX (7-relation-type), GraphRAG (Microsoft). v6 recommended. v7 downgrades: typed vectors are competitive.
4. **Edge-cloud with privacy.** MemPrivacy (MemTensor + HONOR + Tongji, 2026-05-18). Reversible pseudonymization: cloud sees redacted data, edge does the un-redaction locally. This is **the right pattern for Dan Glasses** because we want cloud-assisted reasoning without leaking raw data.
5. **Skill-based memory (OpenClaw-style).** Files on disk: AGENTS.md, SOUL.md, MEMORY.md, etc. Bootstrap memory is read at session start, semantic memory is searched on demand. v6 confirmed: this is the canonical OpenClaw pattern. [^16]

**v7 recommendation for Dan Glasses:**
- v1: keep memoryd as-is (SQLite + MiniLM-L6-v2 + 3 types). The architecture is correct.
- v2: add a typed schema layer (episodic/semantic/procedural/conversation/event/feedback/skill). Use Memanto's 13-category pattern as a starting point.
- v3: consider MemPrivacy if we want to ship cloud-assisted memory without leaking PII.

### 3.5 Multimodal fusion — how are the best systems combining vision, audio, and text?

The 2026 state-of-the-art is **late-fusion at the embedding level**, not early-fusion in the model:

- **LFM2.5-VL-450M** uses SigLIP2 NaFlex for vision and the LFM2.5-base for text. The projector is a small MLP. This is the standard "vision encoder + text decoder with projector" pattern.
- **GPT-4o, Claude Mythos 5** use unified tokenization (audio/text in the same vocabulary, image tokens separate). This is the "all-tokens" pattern. Requires more memory and is not feasible for edge.
- **Gemini 3 Flash** uses modular fusion with separate audio/video/text encoders, fused at the LLM input. Good for streaming.
- **VLCache (arXiv 2512.12977)** caches vision encoder outputs as KV and recomputes 2-5% per layer. 1.2-16× speedup. SGLang-integrated. **Production-ready.** This is the v2 optimization for perceptiond.
- **Open-source option:** SmolVLM / LFM2.5 use the projector-MLP pattern. The community is standardizing on this.

**v7 verdict for Dan Glasses:** the projector-MLP pattern (LFM2.5-VL-450M) is correct. Add VLCache-style optimization in v2. Do not try to do unified-tokenization fusion on edge.

### 3.6 Model compression — what works for keeping models small but capable?

The 2026 toolbox (v7 update from v6):

1. **Quantization (Q4, Q5, Q8, IQ-series).** Q4_0 is the production default. IQ4_XS and IQ3_XXS are quality-lossy but useful for the 2-3B class on 4GB devices. **Dan Glasses v1 uses Q4_0. v2 may use IQ4_XS for the chat/NLG model.**
2. **Knowledge distillation.** LFM2.5-VL-450M is distilled from the larger LFM2 series. HRM-Text 1B is trained from scratch on 40B tokens (not distilled) but uses hierarchical structure to compress. **Distillation is the workhorse.**
3. **Pruning (structured, semi-structured).** SparseGPT, Wanda — useful but less mature. Not on the v1 critical path.
4. **Speculative decoding.** Draft + target model. Useful when the target is large. Not useful when both are small.
5. **Compilation (TensorRT-LLM, llama.cpp, MLX).** llama.cpp is the right choice for Dan Glasses (x86_64 + aarch64, no GPU needed for v1). MLX is Apple-only. TensorRT-LLM is Nvidia-only.
6. **KV-cache optimization.** VLCache (vision-specific), PagedAttention (vLLM), Sliding-window attention. VLCache is the most relevant for v2.

**v7 verdict:** Q4_0 + llama.cpp is the right v1 path. Add VLCache and IQ-quantization in v2.

---

## 4. Competitive & Market Research

### 4.1 AI wearable landscape (2026-06-17)

**The 2026 smart glasses market: $2.34B in 2024 → $7.14B projected by 2034 (CAGR 11.8%).** [^17] **Meta holds 76% market share.** The smart glasses market grew 139% YoY in H2 2025. [^18]

**Key players and where they sit:**

| Player | Product | AI Model | Display | Status | Threat to Dan Glasses |
|---|---|---|---|---|---|
| **Meta Ray-Ban Display** | $799 | Muse Spark (Meta Superintelligence Labs, 2026-05) | In-lens display | Shipping summer 2026 | HIGH — incumbent with display |
| **Meta Ray-Ban Gen 3** | TBD | Muse Spark | No display | Coming 2026 | HIGH — incumbent no-display |
| **Apple AI Smart Glasses** | TBD ($200-500) | TBD (Apple Intelligence) | No display v1 | **Delayed to late 2027** | MEDIUM — not shipping this year |
| **Google + Samsung + Warby Parker** | Project Aura | Gemini 3.5 | Display | Shipping 2026 | MEDIUM — Google has Gemini |
| **Even Realities G2** | $399-$599 | Built-in AI assistant | HUD text overlay | Shipping 2026 | LOW — different design center |
| **Brilliant Labs Halo** | TBD | On-device AI + Noa cloud | No display | Shipping 2026 | LOW — niche creator market |
| **VIVE Eagle, Qwen Glasses, ROG XREAL R1** | Various | Various | Various | Shipping 2026 | LOW — fragmented |
| **Rokid, RayNeo, INMO, Viture, Lucyd** | Various | Various | AR displays | Shipping 2026 | LOW — AR-focused |

**v7 takeaways for Dan Glasses:**
- **Meta's lead matters more than ever.** Muse Spark (May 2026) is Meta's first model from Superintelligence Labs. They are catching up fast on the AI side. The display-equipped Ray-Ban ($799) is the most direct competitor. [^19]
- **Apple is delayed to late 2027.** This is a 12-18 month window where Meta is unchallenged at the top. **For Dan Glasses, this is a window to ship v1. By 2028, Apple will be a real competitor.**
- **Privacy is the differentiator.** Meta's glasses are cloud-dependent, camera-always-on, and have triggered EU regulatory concerns. Even Realities markets itself as "anti-Meta" with a privacy-first message. **Dan Glasses' on-device + open-source positioning is a real differentiator.** v7 recommends emphasizing this in marketing.
- **India and emerging markets are open.** Most smart glasses target US/EU. The Indian market is large and underserved. **Dan Glasses, as an India-built product, has a structural advantage in this market.**

### 4.2 Open-source AI companion projects (2026-06-17)

The 2026 open-source landscape for local AI agents:

| Project | Stars | Architecture | Verdict |
|---|---|---|---|
| **OpenClaw** | 345K+ | Gateway-first, multi-channel, MCP | Largest, but 138+ CVEs |
| **Hermes Agent** | 140K+ | Agent-first, in-built learning loop | Security-cleaner, lacks multi-channel |
| **Letta** (MemGPT) | 27K+ | Persistent memory, model-agnostic | Strong memory story |
| **OpenHands** | 50K+ | Coding agent, sandboxed | Different use case |
| **Open LLM VTuber** | TBD | Local AI companion, 100% offline | Closest UX analog to Dan Glasses |
| **LibreChat** | TBD | Multi-model chat, your data stays | UI layer |
| **agentic Inbox** | TBD | Email-reply agent | Different use case |
| **Aider / Cline / Codex CLI / Claude Code** | Various | Coding CLI agents | Different use case |

**v7 verdict for Dan Glasses:**
- **OpenClaw is the right orchestration choice** for 2026 — multi-channel reach is critical. CVE hardening is a must-do.
- **Letta is the right memory pattern** to study — paginated memory between core/archival/recall. v2 should consider a Letta-style memoryd refactor.
- **Open LLM VTuber is the closest UX analog** — a local, voice-driven AI companion. Worth studying for inspiration.

### 4.3 Privacy-preserving AI — how does Dan Glasses position?

**v7 positioning matrix:**

| Approach | Examples | Dan Glasses fit |
|---|---|---|
| **Pure on-device** | Open LLM VTuber, Letta (local mode) | YES — v1 is on-device VLM, audiod, memory |
| **Edge-cloud with privacy** | MemPrivacy (MemTensor 2026-05-18) | v3 — when we add cloud-assisted memory |
| **Reversible pseudonymization** | MemPrivacy | YES — for cloud fallback when LLM is too big |
| **Homomorphic encryption** | Mostly research | NO — too slow for real-time |
| **Differential privacy** | Apple's approach | PARTIAL — for telemetry |
| **Local differential privacy** | Google Gboard | NO — requires aggregation |
| **Federated learning** | Google Gboard, Apple | NO — requires model updates |

**v7 positioning statement (suggested for marketing):**
> "Dan Glasses is a privacy-first AI wearable. All vision, audio, and memory processing happens on-device. No data leaves your glasses without explicit, granular consent. Cloud assist is opt-in, reversible, and redaction-preserving by design."

This is a real differentiator from Meta Ray-Ban (cloud-everything), Apple (cloud-dependent), and Even Realities (cloud-assisted but no privacy story). It's also aligned with the danlab.dev mission.

---

## 5. Technical Deep-Dive A: Edge VLM Optimization

### 5.1 The state of quantization for sub-1B VLMs in 2026

Q4_0 remains the production default. The IQ-series (IQ4_XS, IQ3_XXS) from llama.cpp gives 10-30% size reduction at 1-3% perplexity cost. **For Dan Glasses v1: Q4_0. For v2: IQ4_XS for the chat model.**

**Quality at Q4 vs Q8 (LFM2.5-VL-450M, anecdotal):**
- Q4_0: ~93% of full quality on VQA benchmarks
- Q5_0: ~96%
- Q8_0: ~99%
- F16: 100%

**Verdict:** Q4_0 is the right cost/quality tradeoff. Q5_0 is justifiable for the laptop prototype (AC-powered).

### 5.2 Vision encoder offload — when is it worth it?

The vision encoder (SigLIP2 NaFlex) is ~180MB at F16. Offloading it to a separate NPU/GPU helps if:
- The NPU is faster than the CPU for matrix multiplies (true for Apple Neural Engine, Qualcomm Hexagon, Intel NPU)
- Power is lower per FLOP (true for NPUs)

For Dan Glasses on x86_64 CPU: offload is not worth it (CPU is the only option). For Redax aarch64: depends on the SoC. **v2 question: characterize SigLIP2 inference time on the Redax SoC. If > 200ms, consider offload.**

### 5.3 Salience gating — the real power lever

v6 and v7 both identify this as the wrong-levelled gate. The 2/5/10 FPS modes don't change VLM inference frequency. **The real lever is "skip VLM entirely on this frame".**

**v7 architecture:**
```
camera (continuous) → motion detector (always on, ~0.5W)
                    → salience classifier (always on, ~0.1W)
                    → context gate (NEW: ~0.05W) [meeting? home? driving?]
                    → VLM (only on salient + context-relevant frames, ~3-8W peak)
```

The context gate is the v7 differentiator. It can be a simple decision tree:
- IF audio is in "meeting" mode (long-form speech, no commands) → drop frames faster
- IF time-of-day is "driving" → enable high-frequency VLM
- IF location is "home" → lower frequency

This is the v7 "value-trigger" perception vs. v6 "novelty-trigger" perception.

### 5.4 Latency budget for v2

| Stage | Latency (target) | Current (v1) | Notes |
|---|---|---|---|
| Frame capture | < 33ms (30 FPS) | < 10ms | OK |
| Salience classification | < 5ms | < 2ms | OK |
| Context gate | < 2ms | NEW | trivial |
| Vision encoder (SigLIP2 NaFlex) | < 100ms | ~50-80ms (Q4_0) | OK on x86_64 |
| VLM decoder (LFM2.5-450M, ~50 tokens) | < 200ms | ~200-500ms (CPU) | **bottleneck** |
| Memory write | < 5ms | < 2ms | OK |
| TTS synthesis (KittenTTS medium) | < 200ms | ~200-400ms | **bottleneck** |
| Audio output | < 50ms | ~30ms | OK |
| **End-to-end (push-to-talk → TTS)** | < 1500ms | ~3000ms | **Need to halve** |

**v7 path to halve:** swap decoder for `llama.cpp` with `-t 8 -c 2048 -b 1` (already in spec); add streaming TTS for first-syllable-out latency; reduce segment cap from 10s to 6s for faster TTFB.

---

## 6. Technical Deep-Dive B: Memory Architectures for AI Companions

### 6.1 The taxonomy (v7 update from v6)

| Type | Example | Pros | Cons | Dan Glasses fit |
|---|---|---|---|---|
| **Pure vector** | memoryd v1, Memanto | Simple, fast | No structure | v1 |
| **Vector + typed schema** | Memanto, Mem0 with types | Structure + speed | Schema design | v2 |
| **Hierarchical with paging** | Letta (MemGPT) | Bounded context | Complexity | v3 |
| **Graph + vector hybrid** | MemX, GraphRAG | Rich relations | Heavy | No |
| **Edge-cloud with privacy** | MemPrivacy | Cloud + privacy | New pattern | v3 |
| **Skill-based** | OpenClaw AGENTS.md | Inspectable | Not scalable | v1 (orthogonal) |

### 6.2 The v2 plan for memoryd

1. **Add typed schema (13 categories per Memanto):** episodic, semantic, procedural, conversation, event, feedback, skill, location, person, intent, observation, preference, summary.
2. **Add a hierarchical context** (Letta-style): core (always-loaded, ~2KB), archival (on-demand, ~10MB), recall (recent, ~1MB).
3. **Add MemPrivacy-style reversible pseudonymization** for any cloud-assisted memory: cloud sees redacted data, edge does un-redaction.

**v7 scope:** 13-category schema (1 month), hierarchical context (2 weeks), MemPrivacy (1 quarter).

### 6.3 The proactive trigger

**Key v7 insight:** memoryd is currently a write-only firehose. v1 stores anything posted. v2 needs a **proactive trigger** that asks:
- "This description has been seen 3 times today. Is this a pattern?"
- "The user said this preference 5 times across 2 weeks. Promote to semantic."
- "This event has no follow-up. Drop after 7 days."

This is the v2 "reasond" daemon that v6 recommended. HRM-Text 1B is the right model for this — 1.15B params is small enough to run on-device, large enough to do useful classification.

---

## 7. Technical Deep-Dive C: Proactive AI

### 7.1 The 2026 landscape

Proactive AI is real and shipping in 2026. Three papers/benchmarks are the canonical references:

1. **ProAgentBench (arXiv 2602.04482).** Real-world benchmark for proactive agent behavior. Measures: anticipation, relevance, non-intrusiveness, helpfulness. [^12]
2. **ProAct (arXiv 2605.25971).** Turns idle compute into anticipation. The model looks at the user's recent context and proposes actions before being asked.
3. **ProActor (ACL 2026).** The first RL-trained proactive agent. Uses GRPO with stage-aware rewards. **This is the production-grade proactive agent paper.**

### 7.2 What proactive means for Dan Glasses

v1 is purely reactive: user says "what's in front of me?", VLM describes. v2 needs:

1. **Anticipation:** "The user just walked into a meeting room. Pull up the meeting agenda from calendar."
2. **Non-intrusiveness:** "Don't surface 10 notifications at once. Pick the most important one."
3. **Continuity:** "The user asked about X 30 minutes ago. Now they're asking about Y. Connect them."
4. **Learning:** "The user said 'I hate it when you say that'. Update the persona model."

### 7.3 Implementation path

v1: rule-based proactive layer (cron + simple heuristics). v2: ProAct-style model on top of memoryd. v3: ProActor-style RL-trained agent.

**v7 recommendation:** add a "proactive_d" daemon that subscribes to memoryd events, runs a small classifier (HRM-Text 1B or even a 0.5B model) on each event, and surfaces "should I say something now?" decisions. Default policy: stay silent unless the user has explicitly enabled proactive mode (per-spec: PTT default in v1, wake-word in v2).

---

## 8. Top-Line Recommendations for Danlab's AGI Roadmap

These are elaborated in `dan2-agi-roadmap.md`. Summary:

1. **Ship Dan Glasses v1 in 2026.** The stack is ready. The 18-month Apple delay is the window.
2. **Add HRM-Text 1B as the on-device reasoning layer in v2.** 1.15B params, 40B tokens, brain-inspired, $1K training. This is the missing piece.
3. **Fork SIA for danlab-multimodal.** Harness-only loop on a VLM-improvement task. This is the credible path from "pre-RL scaffold" to "real self-improvement".

Open questions (to user):
- Dan Glasses v1 launch date: any commitments?
- HRM-Text 1B integration: priority for v2 or later?
- SIA fork for danlab-multimodal: who owns it?
- Apple glasses delay: does this change your market timing?
- Privacy positioning: do we want to lead with this in marketing?

---

## Sources

[^1]: https://www.prnewswire.com/news-releases/sapient-intelligence-launches-hrm-text-challenging-the-llm-monopoly-with-a-brain-inspired-foundation-model-trained-on-up-to-1000x-fewer-tokens-302774638.html
[^2]: https://arxiv.org/html/2605.25435v1
[^3]: https://www.marktechpost.com/2026/05/29/hexo-labs-open-sources-sia-a-self-improving-agent-that-updates-both-the-harness-and-the-model-weights/
[^4]: https://www.liquid.ai/blog (LFM2.5-VL-450M release announcement, 2026-04-11)
[^5]: https://novascribe.ai/how-accurate-is-whisper
[^6]: https://dymesty.com/blogs/articles/smart-glasses-hardware-specs-complete-guide
[^7]: https://www.fwdslash.ai/blog/openclaw-vs-hermes
[^8]: https://www.cnn.com/2026/06/05/business/anthropic-calls-for-ai-brake-pedal
[^9]: https://cryptobriefing.com/recursive-self-improving-ai-two-years/
[^10]: https://medium.com/@adnanmasood/recursive-self-improvement-rsi-in-the-wild-how-ai-started-engineering-its-own-architecture-part-1-a9d234f38b6e
[^11]: https://www.buildfastwithai.com/blogs/latest-best-ai-models-may-2026
[^12]: https://arxiv.org/abs/2602.04482 (ProAgentBench), https://arxiv.org/abs/2605.25971 (ProAct)
[^13]: https://github.com/IAAR-Shanghai/Awesome-AI-Memory
[^14]: https://www.marktechpost.com/2026/05/18/meet-memprivacy-an-edge-cloud-framework-that-uses-local-reversible-pseudonymization-to-protect-user-data-without-breaking-memory-utility
[^15]: https://github.com/letta-ai/letta-code
[^16]: https://docs.getaxonflow.com/docs/integration/openclaw
[^17]: https://www.accio.com/business/meta-smart-glasses-trends
[^18]: https://www.cnet.com/tech/mobile/apple-smart-glasses-development-bumps-reported-delay
[^19]: https://hypebeast.com/2026/5/meta-ai-pendant-and-supersensing-glasses-roadmap-leaks
rrent | 2026-05-18 | Reasoning layer for v2. |
| **LFM2.5-1.2B-Thinking** | 1.2B | TBD | 2026-Q1 | Quality upgrade for v2 if battery allows. |
| **Moondream 2** | 1.86B (Q4: ~1GB) | SigLIP | 2024 | Too big for glasses. Legacy. |

**v7 finding:** The sub-500MB VLM landscape has **consolidated around LFM2.5-VL-450M**. SmolVLM-256M is the fallback. Gemma 3 270M is text-only. The next generation (Gemma 4 1B, LFM2.5-1.2B-Thinking) trades size for capability. **For Dan Glasses v1: LFM2.5-VL-450M. For v2: a 3-model swarm (LFM2.5-VL-450M + HRM-Text 1B + Gemma 4 1B).**

### 3.4 Memory and continual learning — AI systems that learn from experience

The 2026 memory landscape has three architectural camps:

**A. Pure vector retrieval (Mem0, LangChain memory).** Simple, works at small scale, gets unwieldy past 100K items. Mem0 has 3.7M+ downloads as of May 2026. [^13] For Dan Glasses, the current memoryd architecture (SQLite + sentence-transformers + cosine similarity) is in this camp.

**B. Vector + graph hybrid (MemX, Letta).** MemX proposes 7 relation types between memory nodes. Letta (formerly MemGPT) uses a hierarchical memory with hot/cold tiers. These work better at 100K+ items and for relational queries. **The Memanto paper (arXiv 2604.22085) showed pure vector with 13-category typed schema beats graph hybrids on LongMemEval.** This is a counter-argument — the graph may be unnecessary; the type system is the leverage.

**C. Edge-cloud with privacy (MemPrivacy, MemTensor, 2026-05-18).** [^15] Reversible pseudonymization keeps raw user data on device, sends only typed/abstracted representations to cloud. This is **the right architecture for Dan Glasses long-term** because glasses are privacy-sensitive.

**v7 recommendation:** 
- **v1 memoryd:** keep current SQLite + MiniLM-L6-v2 + cosine. Add a typed-memory schema (episodic / semantic / procedural is a good start; add `user`, `world`, `self`, `intent` types per Memanto's 13-category lesson).
- **v2 memoryd:** migrate to vector + hierarchical graph. Add MemPrivacy-style reversible pseudonymization for any cloud round-trip.
- **Don't migrate to Mem0/Letta** — the cost/benefit is wrong for our scale (10K-100K memories per user per year, not 1M+).

### 3.5 Multimodal fusion — how are the best systems combining vision, audio, and text?

The 2026 state-of-the-art multimodal systems (GPT-5.5, Claude Mythos 5, Gemini 3 Flash) all use late fusion — vision and audio are encoded separately by specialist models, then projected into a shared embedding space that a central transformer attends to. This is **opposite to** the early-fusion approach (single model takes raw audio+video+text).

For on-device (Dan Glasses), the constraint is memory. Late fusion means we can run the vision encoder (LFM2.5-VL-450M) and audio encoder (whisper.cpp) and the LLM (HRM-Text 1B + Gemma 4 1B) **as separate processes** and only merge at the agent level. This is exactly what our service decomposition does. **The architecture is correct. v7 only adds the reasoning layer (HRM-Text 1B) and the chat/NLG model (Gemma 4 1B) to the swarm.**

**Open question:** late fusion vs. early fusion at the encoder level (i.e., can we run a single model that takes video+audio+text input). Answer: not in 2026 at sub-1B parameter count. Early fusion at the encoder level requires a unified tokenizer, and the best unified tokenizers (e.g., Google's USM, Meta's SeamlessM4T) are 7B+. **Wait until 2027-2028 for this.**

### 3.6 Model compression — what techniques are working for keeping models small but capable?

2026 compression landscape:

1. **Quantization (INT4/INT8/Q4_K_M/Q5_K_M).** Mature, 2-4× compression with 1-3% quality loss. **This is the baseline.** LFM2.5-VL-450M Q4_0 is 209MB. Done.
2. **Distillation (Llama 4-1B from 70B, Gemma 4 1B from 27B).** Effective when teacher and student have the same architecture family. **Use for HRM-Text 1B-style models if we want a chat/NLG model.** [^16]
3. **Pruning (LLM-Pruner, SparseGPT).** 30-50% sparsity with minimal quality loss, but hardware support is uneven. Not ready for aarch64 in 2026.
4. **Mixed-precision expert routing (MoE).** Nemotron 3 Ultra (Nvidia, 2026-06-01): 550B params, 55B active, open-weights. This is the frontier's answer. **Not directly applicable to Dan Glasses**, but instructive: active vs. total params is the next axis of efficiency. [^17]
5. **Speculative decoding / cascaded inference.** Use a small model to draft, a large model to verify. Not single-model, but 2-3× speedup. **Use for HRM-Text 1B + LFM2.5-1.2B-Thinking combination in v2.**

**v7 recommendation:** Stick with Q4/Q5 quantization for v1. Distillation is the right v2 path. Pruning is not ready. MoE is the frontier's trick but doesn't help wearables. Speculative decoding for the reasoning+chat pair.

---

## 4. Competitive and Market Research

### 4.1 AI wearables landscape (2026-06)

| Player | Product | Status | On-device AI? | Verdict |
|---|---|---|---|---|
| **Meta** | Ray-Ban Display ($799), Oakley Sphaera | Live, expanding to "supersensing" 2026-2027 | Meta Muse Spark (LLM, on-device for some tasks) | 76% market share. Dominant. |
| **Apple** | AI smart glasses (N50) | **Delayed to late 2027** [^18] | TBD | 18-month head start for Meta. |
| **Google** | Android XR + Project Aura + Samsung/Warby Parker/Gentle Monster | Live, shipping 2026 | Gemini 3.5 (on-device + cloud) | The credible Meta competitor. |
| **Brilliant Labs** | Halo | Live, open-source | On-device + Noa cloud agent | Open-source AI glasses. **Closest analog to Dan Glasses.** |
| **Even Realities** | G2 ($399) | Live | On-device AI assistant, **camera-free** | The "anti-Meta" privacy-first play. |
| **Rokid** | AI Glasses Style | Live, China-focused | Cloud LLM | Stylus-first. |
| **XREAL** | R1 (with ROG) | Live, AR display | Cloud LLM | AR display-focused. |
| **Meta pendant** | Limitless | Internal, 2026-2027 | TBD | Hardware diversity play. |

**v7 finding:** Dan Glasses' open-source + on-device + privacy-first positioning is **occupied by Brilliant Labs Halo**. Even Realities G2 is the camera-free analog. Meta is the 800-pound gorilla but is closed-source and privacy-hostile (their glasses record constantly). **The positioning that is NOT taken: open-source + on-device + camera + proactive AI + privacy-by-architecture (MemPrivacy-style). That's Dan Glasses' wedge.**

**Pricing: $300-500 (between Even Realities and Meta) is the right v1 price target.** Apple will land at $200-500 in late 2027, per Gurman. Meta Ray-Ban Display is $799. Brilliant Labs Halo is the price benchmark for the "open-source" tier — $300-400 range.

### 4.2 Open-source AI companion projects (2026)

The "AI companion" space is more crowded than the "AI glasses" space:

- **Letta (MemGPT)** — persistent memory, 2.7K stars, model-agnostic
- **OpenHands** — code agent, 50K+ stars, dominant in software engineering
- **OpenInterpreter** — terminal-based local code agent
- **Open LLM VTuber** — desktop AI companion, 100% offline
- **LibreChat** — multi-model chat UI, self-hostable
- **Aider** — pair programming, 35K+ stars
- **Cline / Roo Code** — VS Code AI extensions
- **ClawdBot / OpenClaw variants** — 345K+ stars, multi-channel
- **Abtars** — agentic framework with abmind memory engine
- **Brilliant Labs Noa** — cloud agent companion to Halo glasses

**v7 finding:** OpenClaw is the de-facto gateway for multi-channel agents in 2026. Dan Glasses is using it correctly. The **abmind** open-source memory engine (Apache 2.0, vector embeddings via ollama) is worth evaluating as a memoryd replacement. **v7 action item: prototype abmind against the current memoryd and benchmark write/read latency.**

### 4.3 Privacy-preserving AI positioning

The privacy landscape in 2026 is bifurcated:

**Privacy-hostile:** Meta (always-on camera + cloud), Google (cloud-first Gemini), Apple Vision Pro (always-on sensors)

**Privacy-friendly:** Brilliant Labs (open-source, opt-in cloud), Even Realities (camera-free), Apple Watch (on-device first)

**Privacy-by-architecture:** MemPrivacy [^15], Apple's Private Cloud Compute (on-device diff privacy), Signal's sealed sender

**Dan Glasses' positioning should be "privacy-by-architecture"**: 
- All raw audio/video stays on device
- Only abstracted embeddings (typed, pseudonymized) go to cloud
- User can opt out of any cloud round-trip
- Open-source = auditable

**This is a real moat.** Even Brilliant Labs Halo sends more data to the cloud than necessary. The MemPrivacy framework (May 2026) is directly applicable. **v7 fix: add MemPrivacy-style reversible pseudonymization to memoryd's cloud sync path. This is a 1-week project, high impact.**

---

## 5. Technical Deep Dives

### 5.1 Deep Dive A: Edge VLM optimization (quantization, distillation, hardware)

**The 2026 state of edge VLM:**

| Technique | Compression | Quality Loss | Hardware Support | Status |
|---|---|---|---|---|
| Q4_0 (4-bit) | 4× | 1-3% | Universal | Production |
| Q5_0 (5-bit) | 3.2× | <1% | Universal | Production |
| Q8_0 (8-bit) | 2× | <0.5% | Universal | Production |
| INT4 (NPU native) | 4× | 1-2% | NPU only (Snapdragon, Apple Neural Engine) | Limited |
| INT8 (NPU native) | 2× | <0.5% | NPU only | Limited |
| Mixed-precision (per-layer) | 2-4× | 1-2% | Limited | Research |
| 2:4 structured sparsity | 2× | <1% | Nvidia, Intel, Qualcomm | Emerging |
| Speculative decoding (2-model) | 2-3× speed | 0% | Universal | Production |
| Cascaded inference (router + L) | 1.5-2× speed | 0-1% | Universal | Production |
| Distillation (teacher → student) | 5-10× | 5-10% | Universal | Production |
| Architecture search (EfficientFormer) | 2-5× | varies | Universal | Production |
| Token reduction (vision tokens) | 1.2-16× | 0-2% | Universal | **VLCache (arXiv 2512.12977)** |
| MoE active routing | 5-10× compute | 0% (if routed correctly) | Frontier only | Frontier |
| Quantization-aware training (QAT) | 4× | <0.5% | Universal | Production |
| Activation checkpointing | 2-3× memory | 0% | Universal | Production |

**v7 finding:** For Dan Glasses v1, the optimizations that matter are:
1. **Q4 quantization** (already using LFM2.5-VL-450M Q4_0)
2. **Speculative decoding** (HRM-Text 1B drafts, Gemma 4 1B verifies in v2)
3. **Token reduction for vision** (VLCache paper, 1.2-16× speedup by caching vision encoder outputs as KV)

**The biggest v2 win is VLCache.** It caches vision encoder outputs as key-value pairs and only recomputes 2-5% of them per layer. SGLang-integrated. Production-ready. **Action: prototype VLCache against LFM2.5-VL-450M and benchmark FPS on Redax aarch64 when hardware lands.**

**Distillation is the right v3 path:** take HRM-Text 1B (Sapient, 1.15B) and distill to a 300M variant for the glasses. Same architecture, less memory, same reasoning quality. The fact that HRM-Text 1B was trained on 40B tokens (vs. 4-36T for typical pretraining) suggests the architecture is data-efficient — distillation should work well.

### 5.2 Deep Dive B: Vector search and memory architectures for AI companions

**The 2026 vector search landscape (for AI companions specifically):**

- **FAISS (Meta)** — still the baseline for in-process vector search. Good for <1M vectors.
- **Qdrant (Rust)** — production-grade, good for 1M-10M vectors. **The right v2 choice for Dan Glasses.**
- **Chroma** — Python-native, simpler API. Good for prototyping.
- **LanceDB** — columnar, good for analytical queries.
- **Vespa** — full-featured, heavy.
- **Weaviate** — GraphQL-first, good for hybrid search.
- **pgvector (Postgres)** — if you already have Postgres.
- **In-process (numpy, vectors crate)** — fine for <100K vectors. **Dan Glasses v1.**

**The 2026 memory architecture landscape:**

- **Episodic / semantic / procedural (Dan Glasses v1)** — good start. Add `user`, `world`, `self`, `intent` types per Memanto's 13-category lesson.
- **Hot/cold tiers (Letta/MemGPT)** — hot in fast vector store, cold in SQLite, periodic compaction. **The right v2 for Dan Glasses.**
- **Vector + graph (MemX)** — 7 relation types. More overhead, more capability.
- **Reversible pseudonymization (MemPrivacy)** — on-device raw, cloud abstracted. **The right v2 for cloud sync.**

**v7 finding for Dan Glasses:** v1 memoryd (SQLite + MiniLM-L6-v2 + cosine) is correct. The fix is **schema, not engine**. Add the typed schema. v2: add Qdrant for the hot tier + MemPrivacy-style sync. **Don't migrate to Mem0 or Letta** — the cost/benefit is wrong for our scale.

**Concrete v1 schema fix:**
```sql
CREATE TABLE memories (
  id INTEGER PRIMARY KEY,
  type TEXT,  -- episodic | semantic | procedural | user | world | self | intent
  subtype TEXT,  -- e.g., for "episodic": meeting | location | interaction | event
  content TEXT,
  embedding BLOB,  -- 384-dim float32
  created_at TIMESTAMP,
  metadata JSON,
  importance REAL,  -- 0-1, computed by LLM at write time
  last_accessed_at TIMESTAMP,
  access_count INTEGER,
  ttl_seconds INTEGER  -- for expiry
);
CREATE INDEX ON memories (type, importance DESC);
CREATE INDEX ON memories (last_accessed_at);
```

This is **2 days of work, massive long-term payoff.** Without importance and access_count, the memory store grows linearly and retrieval degrades.

### 5.3 Deep Dive C: Proactive AI — how to build AI that initiates rather than responds

**The 2026 proactive AI landscape is real:**

- **ProAgentBench (arXiv 2602.04482)** — the first real-world benchmark. Multi-stage, 8 hours of continuous activity, evaluates whether agents anticipate user needs.
- **ProAct (arXiv 2605.25971)** — turns idle compute into anticipation. The "what should I be doing right now that I'm not doing" paper.
- **ProActor (ACL 2026)** — the first RL-trained proactive agent. Uses GRPO with stage-aware rewards. **This is the architecture to study.**

**Why this matters for Dan Glasses:** A "smart glasses" that only responds when asked is **not smart**. The user has to push-to-talk or click to get anything. The value proposition of a wearable is "it knows what I need before I ask." That requires proactive behavior.

**v7 architecture for proactive Dan Glasses:**

```
context_stream (perceptiond descriptions + audiod transcripts + time + location)
     │
     ▼
proactived (new service) — consumes context_stream, runs HRM-Text 1B (reasoning)
     │
     ├──> trivial: write to memoryd
     ├──> moderate: surface to UI as "Did you notice X?"
     ├──> important: speak via ttsd "Hey, X just happened"
     └──> critical: speak immediately + flash UI
```

**Implementation:** proactived is a 2-week project. It uses the same event streams audiod and perceptiond already publish, runs HRM-Text 1B (once we integrate it) on a "what's salient, what should I do about it" prompt every 30 seconds, and emits a `proactive_suggestion` event. The Tauri UI subscribes and decides whether to surface it as a notification, speak it, or stay silent.

**The risk:** proactive AI that talks too much is worse than no proactive AI. The ProAct paper's lesson: "idle compute" is the lever — only emit suggestions when (a) the user has been idle for >30s AND (b) the salience score is >0.7 AND (c) the suggestion is non-repeating (don't say the same thing twice in 24h). **This is the calibration problem. v7 ships without it and we learn from user data.**

---

## 6. What This Means for Danlab's AGI Direction

The 2026 landscape tells a clear story: **AGI is no longer about scaling. It's about recursive improvement + small specialist models + memory + proactivity.** The frontier labs (OpenAI, DeepMind, Anthropic) own the scaling narrative. Danlab's wedge is the **on-device, privacy-preserving, open-source, proactive AI companion** niche.

The 6/12/24-month plan is in `dan2-agi-roadmap.md`. The architectural fixes are in `dan2-architecture-review.md`. The model selection rationale is in `dan2-model-analysis.md`. The top 5 papers to read are in `dan2-papers-to-read.md`.

**Top 3 recommendations for Danlab's AGI direction (v7):**

1. **Integrate HRM-Text 1B (Sapient, May 2026) as the on-device reasoning layer.** This is the right model, at the right size, at the right time. 1.15B params, 40B tokens, brain-inspired, $1K pretraining cost. Fork it, quantize to Q4, integrate as a new `reasond` service. **2-3 month project. Highest leverage.**

2. **Migrate the multimodal pipeline from heuristic to harness-only RL using a SIA fork.** This makes danlab-multimodal honest about being RL. Use HRM-Text 1B as the local Feedback-Agent. The weight-update path is gated on us having a H100 budget and a privacy story. **3-4 month project. Differentiates danlab-multimodal from "another heuristic scorer".**

3. **Build the proactive layer (`proactived`)** that turns audiod + perceptiond + memoryd streams into anticipatory suggestions. Use HRM-Text 1B (post-integration) as the reasoning engine. **1-2 month project. The single biggest UX differentiator for Dan Glasses.**

**Open questions for the user (somdipto):**

- Redax hardware timeline — is there a date? The aarch64 power measurements are blocking.
- Cloud LLM budget for SIA fork — are we paying Claude Sonnet 4.6 for Meta-Agent/Feedback-Agent, or do we run HRM-Text 1B + Gemma 4 1B locally and skip the cloud?
- Privacy position — is "no raw data leaves device, ever" the v1 commitment, or is "opt-in cloud sync with MemPrivacy" acceptable?
- Pricing target — $300, $400, or $500 for the v1 consumer product?
- Apple glasses delay to late 2027 is a real window of opportunity. Are we targeting that window?

---

## 7. Carry-forward Risks (v7 update)

1. **Redax hardware slipping** — v6 noted, v7 confirms still open. The 6-month roadmap depends on hardware.
2. **Form factor unvalidated** — same. Weight, dimensions, battery placement not finalized.
3. **rustc 1.63.0 vs Tauri 2 1.74** — same. Bump needed on the host container.
4. **danlab-multimodal is pre-RL scaffold** — SIA fork plan now concrete. 3-4 month project.
5. **OpenClaw has 138+ CVEs (2026 audit)** — **new in v7.** Read arXiv 2605.25435, adopt audit hooks, pin versions.
6. **Anthropic's brake pedal (Jun 4-7 2026)** — Jack Clark publicly called for a coordinated AI pause. This is the political backdrop. Watch, not actionable for us, but it affects frontier model availability.
7. **Memory storage supercycle (2026)** — DRAM/NAND prices up 5-10× due to AI data center demand. The 128GB eMMC target for Dan Glasses may be cost-prohibitive. v7 question: is 64GB eMMC + 8GB LPDDR5 sufficient for v1?
8. **HRM-Text 1B integration timeline** — depends on Sapient releasing the inference code (currently pre-trained checkpoint, no inference examples published).

---

## References (v7)

[^1]: Sapient Intelligence, "Introducing HRM-Text" (2026-05-18). https://sapient.inc/introducing-hrm-text
[^2]: arXiv 2605.25435, "Security of OpenClaw Agents: Fundamentals, Threats, and Countermeasures" (May 2026). https://arxiv.org/html/2605.25435v1
[^3]: Hexo Labs, "SIA: Self-Improving AI with Harness and Weight Updates" (2026-05-29). https://github.com/hexo-ai/sia
[^4]: Liquid AI, "LFM2.5-VL-450M" (2026-04-11). https://huggingface.co/LiquidAI/LFM2.5-VL-450M
[^5]: novascribe.ai, "How Accurate Is Whisper in 2026?" (2026). https://novascribe.ai/how-accurate-is-whisper
[^6]: Dymesty AI Glasses, "Smart Glasses Specs Explained" (2026). https://dymesty.com/blogs/articles/smart-glasses-hardware-specs-complete-guide
[^7]: fwdslash.ai, "OpenClaw vs Hermes: Which AI Agent to Choose in 2026?" (2026). https://www.fwdslash.ai/blog/openclaw-vs-hermes
[^8]: Anthropic, "Marina Favaro & Jack Clark on Recursive Self-Improvement" (2026-06-04 through 2026-06-07). https://www.axios.com/2026/06/04/anthropic-warns-ai-build-successors
[^9]: Recursive Superintelligence, $650M raise at $4.65B valuation (2026-05). https://cryptobriefing.com/recursive-self-improving-ai-two-years/
[^10]: Adnan Masood, "Recursive Self-Improvement (RSI) in the Wild" (2026). https://medium.com/@adnanmasood/recursive-self-improvement-rsi-in-the-wild-how-ai-started-engineering-its-own-architecture-part-1-a9d234f38b6e
[^11]: Build Fast With AI, "Best AI Models May 2026" (2026-05). https://www.buildfastwithai.com/blogs/latest-best-ai-models-may-2026
[^12]: ProAgentBench (arXiv 2602.04482), ProAct (arXiv 2605.25971), ProActor (ACL 2026).
[^13]: Mem0 (https://mem0.ai), 3.7M+ downloads as of 2026-05.
[^14]: IAAR-Shanghai/Awesome-AI-Memory (989+ stars). https://github.com/IAAR-Shanghai/Awesome-AI-Memory
[^15]: MemPrivacy (MemTensor + HONOR + Tongji, 2026-05-18). https://www.marktechpost.com/2026/05/18/meet-memprivacy-an-edge-cloud-framework-that-uses-local-reversible-pseudonymization-to-protect-user-data-without-breaking-memory-utility
[^16]: Distillation examples: Llama 4-1B distilled from 70B, Gemma 4 1B from 27B.
[^17]: Nvidia, "Nemotron 3 Ultra" (2026-06-01). 550B params, 55B active, open-weights.
[^18]: Bloomberg's Mark Gurman, "Apple Glasses delayed to late 2027" (2026-05-31). https://www.cnet.com/tech/mobile/apple-smart-glasses-development-bumps-reported-delay
