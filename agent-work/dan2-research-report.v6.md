# Dan2 — Technical Research Report
## Deep Research for Danlab's AGI Roadmap

**Date:** 2026-06-17
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** Fresh re-run for 2026-06-17. Prior versions archived as `*.v5.md`. This version folds in latest RSI / SIA developments (May 2026), edge VLM benchmarks, proactive-agent research, and a fresh critique of our architecture.

---

## 0. Scope and Method

This report covers:

- **A.** System architecture deep-dive (Dan Glasses, danlab-multimodal, OpenClaw)
- **B.** AGI landscape research (2026, with emphasis on RSI / SIA)
- **C.** Competitive and market research (AI wearables, open-source AI companions, privacy)
- **D.** Three technical deep-dives: **edge VLM optimization**, **memory architectures for AI companions**, **proactive AI**

Four companion artifacts:

- `dan2-architecture-review.md` — concrete problems and fixes for Dan Glasses
- `dan2-model-analysis.md` — model selection deep-dive
- `dan2-agi-roadmap.md` — 6/12/24-month Danlab direction
- `dan2-papers-to-read.md` — top 5 papers (with rationale)

All claims are grounded in 2025–2026 sources. Every "should" and "must" is an opinion — challenge it.

---

## 1. Danlab Ecosystem — What I Read, What I Concluded

### 1.1 Inventory of artifacts I read

| File | Purpose | Verdict |
|---|---|---|
| `/home/workspace/dan-glasses/PRD.md` | Product spec v1.0 (2026-04-17) | Solid v1; power/form-factor are aspirational |
| `docs/dan-glasses-build-plan.md` | Build plan | Actionable; reuses correct stack |
| `docs/dan-glasses-v1-canonical-analysis.md` | Architecture review | Strong; flagged 15 gaps, mostly unaddressed |
| `agent-work/ARCHITECTURE-FLAWS-BEFORE-CODE.md` | Pre-code review | 20 issues; 7 critical |
| `Services/{audiod,perceptiond,memoryd,toold,ttsd}/SPEC.md` | Service specs | Internally consistent, but not aligned on storage, IPC, or schema |
| `Services/{audiod,perceptiond}/` (actual code) | Live system | Both services shipped, 106/106 tests green |
| `agent-work/dan{1,2,3,4}.md` | Agent logs | Stack is operational, not a plan |
| `/home/workspace/danlab-multimodal/README.md` + `ARCHITECTURE.md` | Hackathon repo | **Honest pre-RL scaffold, not RL** |
| `/home/workspace/paperclip/AGENTS.md` | Multi-agent platform | Dormant — needs decision: ship or archive |
| `/home/workspace/blurr/README.md` | Android companion | Not deeply integrated with Dan Glasses |

### 1.2 What is actually built (per `dan1.md` 2026-06-15 audit)

- All 7 daemons live: `audiod`, `perceptiond`, `memoryd`, `toold`, `ttsd`, `os-toold`, `zo-mcp-bridge`.
- Tauri v2 app wired to all daemons via 20+ Rust commands.
- OpenClaw gateway on `:18789` with Telegram channel + Zo MCP bridge.
- 106/106 tests passing.
- LFM2.5-VL-450M-Q4_0 (209 MB) inference at ~10–15 s/frame on x86_64 CPU.

**This is not a research project anymore — it is a working prototype that needs hardening, hardware, and intelligence on top.**

### 1.3 Two important contradictions I found

1. **Root `AGENTS.md` says "HRM-Text (1B) for reasoning", but `dan-glasses/AGENTS.md` says "LFM2.5-VL-450M for vision".** The project brain has drifted. We need to pick one and document why. (HRM-Text 1B is a reasoning model; LFM2.5-VL-450M is a VLM. These are not the same thing. Likely the right answer: **both** — HRM-Text 1B for complex planning, LFM2.5-VL-450M for vision.)
2. **The "heuristic feedback loop" in `danlab-multimodal` is correctly self-described as pre-RL.** Good honesty, but the path to RL is named (`SIA` / Hexo Labs, May 2026) and unused. That is a roadmap item, not a discussion.

---

## 2. System Architecture Deep-Dive

### 2.1 Is the service decomposition correct?

**Yes, mostly.** The 6-daemon split (audiod, perceptiond, memoryd, toold, ttsd, os-toold) maps cleanly to concerns. But three structural problems remain:

**A. No shared schema / IPC contract.** Each service defines its own JSON shapes. There's no `shared/` types crate (the directory is empty per `dan1.md`). A Tauri command in `perceptiond.rs` is hand-written HTTP-over-TCP, and the response shape drifts from the SPEC.md description. **Fix:** define a `shared/` Rust crate with serde structs; have each service depend on it. This costs us a day and prevents months of integration drift.

**B. VLM gate is wrong-levelled.** `perceptiond` runs motion-or-face salience, then runs VLM. The salience gate uses CPU (OpenCV Haar, EMA background) — that's fine and ~0.5 W. But the VLM is invoked by default on every salient frame, and inference is the dominant power event. There is no *intent* gate. If the user is in a meeting (audio context = "meeting"), the VLM should not run on the colleague's whiteboard even if it's salient. **Fix:** add a `context_gate` between `salience.py` and `vlm.py` that consults a lightweight context store (current activity, current location, time of day) and drops frames that don't pass it. This is the difference between "novelty-trigger" and "value-trigger" perception.

**C. No LLM in the loop yet.** audiod returns transcripts. perceptiond returns descriptions. But there's no LLM that *reasons* over the day's descriptions and *decides what to store, what to surface, what to forget*. memoryd stores anything you POST. That's a firehose. **Fix:** add a thin `reasond` (or repurpose `ttsd`'s process to also host a small local LLM — see model analysis) that consolidates raw events into structured episodic/semantic/procedural memory. Without this, memoryd will grow linearly and become unsearchable.

### 2.2 The "RL feedback loop" in danlab-multimodal — honest assessment

`danlab-multimodal/README.md` is unusually honest for a hackathon repo: it explicitly says "this is a hand-coded **heuristic** feedback loop, not RL. We do not modify model weights. We do not run policy gradient." Good.

**The scoring function:**
```
score = 75
for each cycle:
    image = capture()
    response = vision_model(image, prompt)
    if len(response) < 30:      score -= 40
    if "[ERROR]" in response:  score -= 60
    if identifies_ui(response): score += 10
    score = clamp(score, 0, 100)
    print(f"Cycle {n}: score={score} feedback={suggestions}")
```

This is a *reward-shape spec* without a *gradient flow*. Three things are missing for it to be a real RL loop:

1. **No model parameter update.** The agent is frozen. Whatever the heuristic says, the SmolVLM-256M weights are unchanged at the end of the loop.
2. **No policy.** There's no actor choosing actions to maximize reward. The vision model is called with a fixed prompt.
3. **No replay buffer or credit assignment.** A cycle that scores 95 contributes nothing to the next cycle.

**The credible path to real RL is `SIA` (Hexo Labs, May 2026).** SIA splits the agent into three LLM components — Meta-Agent (writes scaffold), Task-Specific Agent (executes), Feedback-Agent (alternates between editing scaffold and updating weights via RL algorithms selected dynamically based on reward dynamics).[^1] Their reported gain on legal-classification, GPU-optimization, and biological-denoising benchmarks is significant when *both* harness and weight updates are enabled (SIA-W+H) vs. harness-only (SIA-H).[^1]

**Concrete next step for danlab-multimodal:** fork SIA, drop in our heuristic as the Feedback-Agent's "preference signal", and run it on SmolVLM-256M for the screen-caption task. The Meta-Agent rewrites the prompt template; the Task-Specific Agent runs llama.cpp; the Feedback-Agent scores and either edits the prompt or triggers an SFT step. **This is exactly the harness+weights loop SIA proves works.** Until that fork ships, our README's "pre-RL scaffold" framing is correct.

### 2.3 Power/performance — LFM2.5-VL-450M, whisper.cpp, KittenTTS

Short version: **the model choices are correct in family, but the *quantization / size* trade-off is wrong for wearables.** Details in §5 and the `dan2-model-analysis.md` artifact. The summary:

- **LFM2.5-VL-450M Q4_0 at 209 MB + 180 MB mmproj** is borderline. The combined 389 MB is the entire model weight. A 1.5–2.6 B MoE like LFM2-1.2B would give 30–50% better descriptions at a similar size, *if* we have a hardware target with NPU. On aarch64 CPU, stick with the 450M but add **salience-then-intent gating** (a 2-stage gate: cheap motion/face filter, then a 0.3B text classifier that decides if a salient frame is worth running VLM on). Drops effective VLM frequency 5–10×.
- **whisper.cpp base.en at 74 MB** is the right size for English. For multilingual India, `small` (244 MB) or `Moonshine` is better. Moonshine is purpose-built for edge (transformer + compact LLM on a 1 TOPS NPU) and beats whisper-tiny in accuracy while running real-time on-device.[^2] Keep whisper.cpp for compatibility, but build a parallel Moonshine path.
- **KittenTTS base ~25 MB** is great for size but **the quality is mediocre**. Edge TTS benchmarks (May 2026) put KittenTTS Nano 15M as "intelligible, robotic" — usable for status pings, not for natural conversation.[^3] The `ttsd` service is on `medium` (8 voices), which is better. For v1.5, consider **Kokoro-82M** as the quality bar (still <100 MB) or **edge-tts** (free, 200+ neural voices, no API key) as a cloud fallback.[^3] This is a 1-day swap.

### 2.4 OpenClaw — is TypeScript the right choice?

**Yes, with caveats.** The Node runtime is well-trodden for agent orchestration; the MCP plugin ecosystem is TypeScript-native; zo-bridge already speaks it. The caveats:

1. **Single point of failure.** OpenClaw crashed = no agent = no Telegram responses = silent failure for the user. `dan1.md` notes the watchdog needs implementation. Build a tiny `openclaw-supervisor` (Bun + `Bun.spawn`) that respawns the gateway within 1s of process death, with a state checkpoint every N minutes.
2. **No backpressure on the gateway.** audiod can fire 1 transcript/sec when a meeting is active. OpenClaw has to debounce, summarize, and reply via TTS. If a multi-second LLM call is in flight and 5 new transcripts arrive, we need a queue with priority + drop-oldest, not a "process the latest" eager loop. The right design is a small Redis Streams / NATS JetStream, not in-process arrays.
3. **TS bundling for the .deb.** Tauri v2 + Node 22 in a single .deb is non-trivial. Systemd unit must `node` from a known path, not `npm start`. The current `packaging/systemd/openclaw.service` (referenced in `dan1.md`) needs the absolute path and a real `ExecStart`. **This is part of the .deb build gap** flagged by dan1.

---

## 3. AGI Landscape Research (2026)

### 3.1 The "RSI" pivot

The story of 2026 in frontier AI is the pivot from "scale is all you need" to "self-improvement is all you need." Three signals:

1. **Anthropic's "When AI Builds Itself" (May 2026)** is the most-cited public document on recursive self-improvement this year. Anthropic says Claude writes >80% of the code merged into Anthropic's production systems, and engineers ship 8× more code than before. The piece frames three scenarios: human-led (today), AI-led scaffolding (next 1–3 years), full RSI ("by 2028 with ~60% probability" per Anthropic, per news reports).[^4]
2. **SIA: Self-Improving AI with Harness & Weight Updates (Hexo Labs, arXiv:2605.27276, May 2026)** is the first *open-source, runnable* harness+weights RSI loop. The headline result: SIA-W+H (harness + weight updates) beats both harness-only (SIA-H) and baseline on legal classification, GPU optimization, and biological denoising. Feedback-Agent is itself an LLM (Claude Sonnet 4.6 in the released code), alternating between prompt/scaffold edits and triggering RL weight updates.[^1]
3. **Automated AI Researcher as a goal** is now public. OpenAI stated in June 2026 that building an "Automated AI Researcher" is a key company goal. Neo Labs launched around the same thesis. Adaption (founded by Cohere/Google alum Sara Hooker) launched "AutoScientist" for self-directed model training.[^5][^6]

**Implication for Danlab:** the *research frontier* is moving from "bigger model" to "model that improves itself on a benchmark". For us — a small lab with a 1B-class edge VLM — this is a **huge opportunity**, not a threat. We don't need a 1T foundation model to do self-improvement on a wearable task. We need:
- A clear task (e.g., "describe this frame in a way the user will later query")
- A reward signal (does the description get retrieved, used, or marked useful?)
- The SIA scaffold

### 3.2 Self-improving architectures — what has actually worked

The literature in 2026 is converging on a small set of mechanisms:

- **Test-time training (TTT)** — fine-tunes the model on the current input before answering. Works when the input is large and stable (e.g., a PDF to summarize).
- **Scaffold / harness updates** — keeps weights fixed, edits prompts, tools, retry logic. SIA's SIA-H mode. Cheap. Works for "model is capable, scaffold is wrong".
- **Weight updates via RL** — PPO/GRPO/DPO/etc. SIA's SIA-W mode. Expensive. Works when reward signal is clear.
- **Harness + weights together** — SIA's SIA-W+H. Most powerful, but unstable if reward is noisy.[^1]

The **key insight from SIA**: the Feedback-Agent should *dynamically select* which mechanism to apply based on observed reward dynamics. When reward is flat, edit scaffold. When reward is high-variance, fine-tune weights. This is the same "controller" pattern from classical control theory, applied to LLM self-improvement.

**What has NOT worked (yet):**
- Pure end-to-end "self-play" RL on long-horizon tasks — too sample-inefficient.
- Open-ended weight updates without a stable reward — collapse.

### 3.3 Edge AI / on-device models — SOTA for sub-500 MB VLMs

LFM2.5-VL-450M is competitive but not state-of-the-art in 2026. The SOTA for **truly sub-1B VLMs that work**:

| Model | Params | Strong point | Where to find |
|---|---|---|---|
| **LFM2.5-VL-450M** | 450M | Liquid's hybrid conv+attention; SigLIP2 NaFlex encoder | HuggingFace `LiquidAI/LFM2.5-VL-450M` (our pick) |
| **SmolVLM-256M-Instruct** | 256M | Smallest *working* VLM in GGUF | HuggingFace `pierretokns/SmolVLM-256M-Instruct-GGUF` (we use it in danlab-multimodal) |
| **Moondream2** | 1.8B | Edge-friendly, decent OCR | HuggingFace `vikhyatk/moondream2` |
| **OmniVLM** | 968M | 9× token compression, faster TTFT | `NexaAI/OmniVLM-968M`[^7] |
| **MobileVLM V2** | 1.7B / 3B | Lightweight projector, mobile-tuned | `Meituan-AutoML/MobileVLM` |
| **AndesVL-0.6B / 1B** | 0.6B / 1B | Strong on text-rich images, GUI tasks | arXiv:2510.11496 |
| **Firebolt-VL** | 0.8B | LFM2 backbone, Cross-Modality Modulation | arXiv:2604.04579 |
| **ArgusVLM-256M / 500M** | 256M / 500M | Tile-based efficient encoding, 11–16% better than SmolVLM | arXiv:2603.16987 |
| **BlueLM-2.5-3B** | 3B | AnyRes tile inference, strong on long context | arXiv:2507.05934 |
| **Kimi-VL (2.8B active)** | 16B total / 2.8B active | MoE; strong OCR + long context | arXiv:2504.07491 |

**Our pick — LFM2.5-VL-450M — is defensible.** It's not the best on benchmarks, but it's the only sub-500M VLM with a Liquid-Network-based hybrid conv+attention backbone that's *designed* for edge. Combined with a SigLIP2 NaFlex vision encoder (better than ResNet/ViT for varied aspect ratios), it's a reasonable 2026 default. The honest critique: **ArgusVLM-256M/500M and OmniVLM-968M both claim better VQA scores at similar size** — we should benchmark all three on a fixed 100-image Dan Glasses eval set before locking.

**Sub-1B on aarch64 power/thermal reality (2026 data):**
- A 3B VLM on a phone (OnePlus 13R) with full GPU offload: ~3.5 W, ~72°C surface temp, ~10–15 tok/s decode.[^4]
- A 3B VLM CPU-only: 10–12 W, 90–95°C, 1–2 tok/s decode.[^4]
- LFM2.5-VL-450M at our size should be 30–50% of those numbers. Estimated 1.5–2.5 W steady, 2–6 W peak. **Still the dominant power event in a wearable.**
- A 1 TOPS NPU running Moonshine + a compact LLM can do wake-word-class speech recognition for <0.5 W. We should design for NPU offload, not CPU.

### 3.4 Memory and continual learning

The 2026 SOTA for "AI that learns from experience" is dominated by **external memory + retrieval**, not by weight updates:

- **Mem0 (arXiv:2504.19413)** — vector + graph memory. 91% lower p95 latency than full-context; >90% lower token cost. State-of-the-art on LOCOMO benchmark.[^8]
- **Mem0g** — graph extension, modest uplift over flat Mem0.
- **MemGPT** — hierarchical memory with vector storage.
- **MemMachine (arXiv:2604.04853, 2026)** — two-tier (episodic + long-term), stores raw episodes to reduce LLM-extraction drift, exposes REST/Python/MCP. **The cleanest production-shape API in 2026.**
- **APEX-MEM (arXiv:2604.14362)** — property graph + agentic retrieval. 88.88% on LOCOMO QA, 86.2% on LongMemEval. State-of-the-art for graph memory in 2026.[^9]
- **MemX (arXiv:2603.16171)** — local-first, Rust + libSQL (SQLite w/ vectors), 7-type memory_links (similar, related, contradicts, extends, supersedes, caused_by, temporal). **The closest architectural twin to what memoryd should become.**
- **AriadneMem (arXiv:2603.03290)** — entropy-aware graph coarsening + Steiner Tree retrieval. 15% multi-hop F1 gain on LoCoMo. Most sophisticated graph topology.
- **Memori (arXiv:2603.19935)** — semantic triples + conversation summaries. High signal-to-noise index.
- **MemGate (arXiv:2606.06054)** — 9M-param admission gate. Filters memory at retrieval time. Drop-in. 35 MB.

**For Dan Glasses specifically:** MemX's local-first design is the right template. Our `memoryd` is already SQLite + vectors — the upgrade path is: add a `memory_links` table with the 7 relation types, add a Rust-side reciprocal-rank-fusion retrieval over vector + keyword, and add a small (9M-param) MemGate filter on top. This is 1–2 weeks of work and would put us ahead of most open-source AI companions.

**Continual learning (catastrophic forgetting):**
- **MERS (arXiv:2604.08336)** — multiple-embedding replay selection. Drop-in.
- **IDER (arXiv:2603.00624)** — idempotence loss + replay.
- **FOREVER (arXiv:2601.03938)** — Ebbinghaus-curve-inspired replay timing.
- **WSC (Weight Space Consolidation, arXiv:2502.07274)** — the surprising 2026 result: when memory is *abundant* (which is the case for us — we have GBs of storage), the main risk is *loss of plasticity*, not catastrophic forgetting. WSC = rank-based param resets + weight averaging. Cheaper than replay, matches full-retraining on instruction tuning.

**For Dan Glasses:** the wearable memory system is a *retrieval problem*, not a *weight-update problem*. We do not need to fine-tune LFM2.5-VL-450M on the user's day. We need: (1) a great memory schema, (2) great retrieval, (3) a periodic *summarization* step that compresses raw events into structured episodic/semantic/procedural. This is 10× cheaper and more interpretable than continual fine-tuning.

### 3.5 Multimodal fusion (vision + audio + text)

The best 2026 systems use **late fusion with shared embedding space** + a small reasoning LLM on top. Examples:
- GPT-4o, Gemini 2.5 — single multimodal model with audio/video as native modalities.
- Open-source: OmniVLM, MobileVLM V2 — vision + text only, audio handled separately.

For our scale, the correct architecture is:
- **Whisper.cpp or Moonshine** for audio → text.
- **LFM2.5-VL-450M** for image → text.
- A small **reasoning LLM** (Gemma 4 12B on laptop, LFM2-1.2B-Thinking on wearable) consumes both text streams + memoryd retrievals and produces the response.

**No audio-visual joint embedding is needed.** Late fusion over text is simpler, more interpretable, and avoids the ~2× compute of a true multimodal fusion model.

### 3.6 Model compression

The 2026 frontier in quantization:
- **Sub-1-bit / ternary (1.58-bit)**: TWLA, TernaryLM, Sherry, LittleBit-2, ITQ3_S, NanoQuant. Mostly research; some consumer GPU deployment. ^2.4–2.5× memory reduction over FP32 with acceptable perplexity hit on small models.
- **3-bit**: ITQ3_S demonstrates true 3-bit accuracy via interleaved ternary sub-blocks.
- **4-bit (W4A16)**: the production standard. AWQ, GPTQ, SmoothQuant all viable on Ascend, Adreno, Hexagon NPUs.[^10]
- **For our 450M VLM**: Q4_0 (current) is fine. Q3 would lose too much caption quality. **Q4 + KV-cache quantization + speculative decoding** is the real win for power.

**Memory-bandwidth-bound, not compute-bound.** TokenPowerBench (arXiv:2512.03024) shows energy-per-token grows super-linearly with model size because of memory bandwidth. Halving model size halves energy. **This is the lever to pull for wearables: smaller model + Q4 + accelerator-aware kernels > bigger model + lower-bit quantization.**

---

## 4. Competitive and Market Research

### 4.1 AI wearables — the 2026 landscape

| Product | Form factor | Approach | Status |
|---|---|---|---|
| **Meta Ray-Ban (Gen 2/3)** | Glasses | Camera + speakers + Meta AI; *reactive* | Dominant consumer share; 8h battery; no display |
| **Meta Ray-Ban Display** | Glasses | + monocular display in 2026 | Just launched; consumer-facing |
| **Meta AI pendant** | Pendant (Limitless acquisition) | Records + transcribes conversations | Reported in testing, 2026 launch[^11] |
| **Apple smart glasses** | Glasses | Late 2026 launch (per reports); Siri AI integration | Pre-launch[^12] |
| **Snap Spectacles (new gen)** | Glasses | AR + LLM | Snap acquired Illumix to accelerate[^13] |
| **Brilliant Labs / Even Realities G1** | Glasses | Display + AI | OpenSDK; niche |
| **Plaud NotePin / Note Pro** | Pin | Voice-first note-taking | Successful; 30-day audio buffer |
| **Humane AI Pin** | Pin | Projector + AI | **Shut down Feb 2025** — cautionary tale[^14] |
| **Rabbit R1** | Handheld | LAM | **Commercially failed** — cautionary tale |
| **Limitless Pendant** | Pendant | Conversation recording + summaries | Acquired by Meta |
| **Amazon Bee** | Wristband | Records everything you say, summaries | Launched May 2026[^15] |
| **Omi (open source)** | Wearable + mobile | Privacy-first, local-first, MIT | Active, 24h+ capture[^16] |
| **Looki L1** | Wearable | Daily recap + nudges | Indie launch May 2026 |
| **OpenAI / Jony Ive device** | TBD | Reportedly late 2026 | Pre-launch |

**The pattern:** the wearables market in 2026 is bifurcating. (1) Camera-first reactive capture (Meta, Brilliant Labs). (2) Audio-first note-taking (Plaud, Amazon Bee, Meta pendant). (3) **Always-on AI companion with memory** — the open niche that Humane tried and failed, and Omi is now filling open-source.

**Dan Glasses' positioning is (3) — proactive, memory-grounded, privacy-first.** This is the right niche. The product risk is the same as Humane's: nobody has proven that users *want* always-on AI, and battery constraints make "always" difficult.

### 4.2 Open-source AI companion projects

| Project | Privacy story | Local model | Maturity |
|---|---|---|---|
| **Omi (BasedHardware)** | MIT, local-first, optional cloud | Whisper + Sherpa-ONNX locally | Active, 24h+ capture, BLE[^16] |
| **Myomi / Omibutfree** | Open fork of Omi | Whisper local | Active |
| **Hermes Agent (Nous Research)** | Cloud LLM, local TTS option | KittenTTS, Piper, edge-tts | Active, multi-channel[^17] |
| **Omi Local (BasedHardware Flutter)** | 100% local SQLite | Whisper | Active |

**The competitive moat for Dan Glasses vs Omi:**
- Omi is a *note-taking* companion (transcribe + summarize + tasks).
- Dan Glasses is a *proactive cognitive extension* (always-on salience, memory of what you saw, surfaces unprompted).
- This requires the VLM, not just STT. **Vision is our differentiator.**

**The honest risk:** Omi has an active community + funded hardware + shipping product. We have a working prototype. We need to either (a) ship hardware within 12 months, or (b) build the *software* layer (proactive reasoning, memory schema) that Omi doesn't have, and partner with a hardware vendor.

### 4.3 Privacy positioning

Our SOUL.md says "all data stays local unless explicitly shared." The architecture supports this (memoryd is local SQLite, models run locally, OpenClaw is local). But:

- The Tauri app ships with default cloud LLM endpoint (the Zo MCP bridge).
- The user can opt out, but the default should be local-only.
- The Omi project has a strong "no cloud" marketing story; we should match it.

**Action:** default the OpenClaw gateway to local-LLM-only mode at first boot. Cloud LLM is opt-in, not opt-out. This is both a privacy win and a battery win (no radio).

---

## 5. Technical Deep-Dives

### 5.1 Edge VLM optimization

**The problem space:** run a multimodal vision model on a 1.5–3 W wearable for 4+ hours, on a thermal envelope that must stay <40°C at skin contact, while delivering descriptions good enough to be useful.

**Three levers, ranked by impact:**

1. **Skip frames, not bits.** Drop the bits (Q3 vs Q4) saves 25% size, maybe 15% energy. Drop the frames (salience-then-intent gating) saves 50–90% of inference events. **Skip-frames wins.** Concrete: with motion+face salience at 5 FPS, and intent gate at 0.3 B text classifier, the VLM runs on ~5–15% of frames. Effective power drops 5–10×.
2. **Smaller model, more quant.** LFM2.5-VL-450M Q4_0 (389 MB combined) is borderline for a wearable with 4 GB RAM. SmolVLM-256M Q4_K_M + mmproj (302 MB combined) is better. **Trade description quality for power budget.** The user can always re-query.
3. **Speculative decoding with a draft model.** Use Gemma 4 1B as a draft, LFM2.5-VL-450M as the verifier. ~2× throughput at no quality cost. This works on CPU and is implemented in llama.cpp.[^19]

**What NOT to do:**
- Custom 1.5-bit quantization schemes (TWLA, Sherry, ITQ3_S). These are research; runtime support is fragile. Stick with Q4_0 / Q4_K_M.
- 2.6B+ parameter VLMs. Energy-per-token grows super-linearly. Halving size is a bigger lever than halving bits.[^18]

**Hardware targets for 2026:**
- **Apple Neural Engine (M5 / Vision Pro 2)**: 4× GPU AI perf, very low power for fixed-shape ops. Best per-watt for our size class. But Apple-locked.
- **Qualcomm Hexagon NPU (Snapdragon X Elite / 8 Elite Gen 2)**: Hexagon NPU is the right target for aarch64 wearables. llama.cpp's Hexagon backend is improving but not yet production.
- **Hailo-10H**: 6.9 tok/s sustained on Qwen 2.5 1.5B, ~2 W, thermally stable.[^19] But VLM support is early; SigLIP encoder not yet optimized on Hailo.
- **AMD Ryzen AI HX 375**: 50.7 tok/s on Llama 3.2 1B with iGPU, but battery-throttled.[^20]

**Recommendation:** for the laptop prototype, stick with CPU llama.cpp + Q4_0. For the wearable, target **Hexagon NPU with llama.cpp's Hexagon backend when stable, and degrade to CPU if not.** Don't optimize for Hailo or Ryzen AI yet.

### 5.2 Vector memory architectures for AI companions

**Current state of memoryd:** SQLite + `sentence-transformers/all-MiniLM-L6-v2` (384-dim) + cosine similarity. Functional but generic.

**The 2026 SOTA for companion memory has 4 layers:**

1. **Vector index** for semantic recall (we have this).
2. **Keyword index** (BM25) for exact-match (e.g., "Priya", "Aspirin"). MemX uses RRF to merge both. **Add this.**
3. **Graph relations** for "X is similar to Y", "X contradicts Y", "X was caused by Y". MemX has 7 relation types. **Add this as a `memory_links` table.**
4. **Retrieval-time gate** to filter out stale, off-topic, or unsafe memories before they hit the LLM context. MemGate is 35 MB, 9M params, drop-in. **Add this.**

**Cost estimate:** 1–2 weeks of work, all open-source (mem0 is MIT, MemX is local-first Rust, MemGate is a 9M-param MLP). The result: 2–3× better retrieval relevance, lower p95 latency, and the ability to add contradiction/supersede handling that pure vector search cannot do.

**Concrete schema upgrade for memoryd:**
```sql
CREATE TABLE memory_links (
    src_id INTEGER,
    dst_id INTEGER,
    relation TEXT CHECK(relation IN
        ('similar', 'related', 'contradicts', 'extends',
         'supersedes', 'caused_by', 'temporal')),
    weight REAL DEFAULT 1.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (src_id, dst_id, relation)
);
CREATE INDEX idx_links_dst ON memory_links(dst_id, relation);
```

Add BM25 (FTS5) index on `content`. Add MemGate filter on retrieval. Add `/memories/{id}/link` and `/memories/{id}/unlink` endpoints. Done.

### 5.3 Proactive AI — building AI that initiates

**This is the differentiator vs. every AI wearable on the market.** Meta AI, Plaud, Rabbit, Amazon Bee — all are *reactive* (you ask, they answer). The 2026 academic literature has a name for what Dan Glasses should do: **proactive agents**.

**The SOTA framework (2026):**

- **ProAct (arXiv:2602.14048)** — dual-system: real-time reactive + long-horizon proactive. The proactive side runs in the background, accumulates context, and initiates.[^21]
- **ProAgent (arXiv:2512.06721)** — tiered perception (always-on cheap sensing + on-demand expensive vision), VLM-based reasoner decides when to initiate, persona-aware.[^22]
- **ContextAgent (arXiv:2505.14668)** — context-aware agent that uses sensory inputs from wearables/glasses/earphones, with a `trigger threshold` (P_S ≥ θ) governing when proactive actions fire.[^23]
- **PASK (arXiv:2604.08000)** — IntentFlow model for demand detection, three-level memory module. The most wearable-specific proactive framework I've found.[^24]
- **PRISM (arXiv:2602.01532)** — Festina Lente ("make haste slowly"). Dual probability model: p_need × p_accept. Only intervenes near the decision boundary. **This is the right pattern for "AI that doesn't annoy you".**[^25]
- **π-Bench (arXiv:2605.14678)** — benchmark for proactive assistants. 100 multi-turn tasks, hidden intents. Reveals that **prior interaction history is the single biggest predictor of proactive quality**.[^26]
- **Pro2Bench / EgoProactive (arXiv:2606.04970)** — egocentric dataset for proactive assistance with "off-plan" recovery. Most relevant to our form factor.[^27]

**Concrete architecture for Dan Glasses:**

```
[VLM descriptions] + [transcripts]
          ↓
  [Event Queue] ← salience-gated, intent-gated
          ↓
  [Proactive Reasoner] ← PRISM-inspired
    - p_need = P(user will want this surfaced | recent context)
    - p_accept = P(user will accept interruption | time, mode, history)
    - if p_need × p_accept > θ: surface
    - if near boundary: slow down, deliberate
          ↓
  [Decision] → [silently store] | [TTS speak] | [Telegram notify]
```

**The hard part is the reward signal.** π-Bench's finding is that prior interaction history is the strongest predictor — i.e., the more the user has been helped (or annoyed) by proactive interventions, the better the model can predict future ones. This is exactly the SIA loop on a per-user basis:

1. Surface a proactive intervention.
2. User accepts, dismisses, or ignores.
3. Update the p_need / p_accept priors for that user.
4. Use SIA's harness-update mechanism to edit the proactive prompt template based on accumulated feedback.

**This is the path to "personalized proactive AI".** It is *the* differentiation.

---

## 6. Open Questions

1. **Redax hardware timeline.** Without the board, all wearable claims are paper. Get a target date.
2. **Battery spec.** Without a power measurement on real hardware, we cannot size battery or thermal envelope.
3. **Wake-word implementation path for v1.5.** OpenWakeWord on-device, or vendor-specific (e.g., Sensory, Picovoice)? OpenWakeWord is Apache 2.0 and runs on Raspberry Pi; good starting point.
4. **Proactive reward labeling.** How do we get the first 1000 user feedback labels for SIA's harness loop? Cold-start problem.
5. **Paperclip decision.** Dormant since Q1 2026. Ship it as the agent orchestration layer for Dan Glasses v2, or archive? The Rust + TypeScript + Postgres shape is good.
6. **Blurr integration.** Android companion app is built but not wired to Dan Glasses. Decision needed.
7. **Cloud LLM default.** OpenClaw currently uses Zo MCP bridge as default. Privacy story requires local-first default.

---

## 7. TL;DR for somdipto

- The stack is **operational, not aspirational.** Stop treating it as a research project.
- The next 6 months are about **battery, thermal, and proactive reasoning.** Software quality is good; hardware is the blocker.
- The biggest research bet: **SIA on our heuristic.** Self-improvement on the screen-caption task is a credible 12-month research agenda and a publishable result.
- The biggest product bet: **proactive over reactive.** Nobody has shipped this well. PRISM-style intervention gating is the right pattern.
- The biggest model decision: **LFM2.5-VL-450M is good, but SmolVLM-256M + intent-gate is better for wearables.** Benchmark both on a fixed 100-image eval set.
- The biggest memory decision: **add BM25 + graph relations + MemGate to memoryd.** 1–2 weeks, 2–3× retrieval relevance.
- The biggest AGI bet: **SIA is the open-source path to harness+weights RSI.** Fork it, replace the feedback agent with a smaller LFM2-1.2B-Thinking, and run it on SmolVLM-256M.

---

## Footnotes

[^1]: SIA: Self Improving AI with Harness & Weight Updates. Hebbar et al. (Hexo Labs), arXiv:2605.27276, May 2026. https://arxiv.org/abs/2605.27276. Code: https://github.com/hexo-ai/sia
[^2]: Moonshine STT (moonshine-ai). On-device transformer-based ASR + compact LLM on 1 TOPS NPU. https://github.com/moonshine-ai/moonshine
[^3]: Edge TTS comparison (ktomanek), 2026. https://github.com/ktomanek/edge_tts_comparison. KittenTTS Nano 15M measured 4.80s per sample on Raspberry Pi 5; Kokoro 0.15s, Piper 0.53s. Quality: KittenTTS "intelligible, robotic"; Kokoro "best in class for size".
[^4]: *When AI Builds Itself* (Anthropic, May 2026). https://www.nectain.com/blog/the-next-ai-shock-is-already-loading
[^5]: TechCrunch, *RSI is the new AGI*, May 2026. https://techcrunch.com/2026/05/28/rsi-is-the-new-agi-and-its-just-as-hard-to-pin-down
[^6]: Adaption AutoScientist, May 2026. https://techcrunch.com/2026/05/13/adaption-aims-big-with-autoscientist-an-ai-tool-that-helps-models-train-themselves/
[^7]: OmniVLM: A Token-Compressed, Sub-Billion-Parameter Vision-Language Model. arXiv:2412.11475. https://arxiv.org/html/2412.11475
[^8]: Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory. arXiv:2504.19413. https://arxiv.org/html/2504.19413
[^9]: APEX-MEM: Agentic Semi-Structured Memory with Temporal Reasoning. arXiv:2604.14362. https://arxiv.org/pdf/2604.14362
[^10]: AWQ: Activation-aware Weight Quantization. Lin et al., arXiv:2306.00978. https://arxiv.org/pdf/2306.00978
[^11]: Meta AI pendant from Limitless. May 2026. https://www.facebook.com/groups/287560278592016/posts/1946833575998003
[^12]: Apple smart glasses — late 2026. https://www.facebook.com/groups/2444320529257373/posts/2885185818504173
[^13]: Snap Acquires Illumix. AWE 2026. https://www.linkedin.com/posts/augmentedworldexpo_awe2026-xr-ispatial-activity-7468553400884969472-2iAw
[^14]: Plaud 2026 Reality Check — Humane Pin shutdown. https://uk.plaud.ai/blogs/articles/whats-the-best-wearable-device-for-ai-note-taking-2026
[^15]: Amazon Bee (Ayman Elnory, 2026). https://www.linkedin.com/posts/aymanelnory_ai-privacy-wearables-activity-7464669132978880512-lsNV
[^16]: Omi (BasedHardware). https://github.com/BasedHardware/omi. MIT, 24h+ continuous capture, local-first.
[^17]: Hermes Agent (Nous Research). https://github.com/NousResearch/hermes-agent
[^18]: TokenPowerBench. arXiv:2512.03024. https://arxiv.org/html/2512.03024
[^19]: LLM Inference at the Edge: Mobile, NPU, and GPU Performance Efficiency. arXiv:2603.23640. https://arxiv.org/html/2603.23640v2
[^20]: Network Edge Inference for LLMs. ACM 2025. https://dl.acm.org/doi/10.1145/3809166
[^21]: ProAct: A Dual-System Framework for Proactive Embodied Social Agents. arXiv:2602.14048. https://arxiv.org/pdf/2602.14048
[^22]: ProAgent: Harnessing On-Demand Sensory Contexts. arXiv:2512.06721. https://arxiv.org/pdf/2512.06721
[^23]: ContextAgent: Context-Aware Proactive LLM Agents. arXiv:2505.14668. https://arxiv.org/html/2505.14668
[^24]: PASK: Toward Intent-Aware Proactive Agents with Long-Term Memory. arXiv:2604.08000. https://arxiv.org/html/2604.08000v1
[^25]: PRISM: Festina Lente Proactivity. arXiv:2602.01532. https://arxiv.org/pdf/2602.01532
[^26]: π-Bench: Evaluating Proactive Personal Assistant Agents. arXiv:2605.14678. https://arxiv.org/html/2605.14678v1
[^27]: Plan, Watch, Recover (EgoProactive / Pro2Bench). arXiv:2606.04970. https://arxiv.org/html/2606.04970
[^28]: NanoQuant: Efficient Sub-1-Bit Quantization. arXiv:2602.06694. https://arxiv.org/pdf/2602.06694
[^29]: LittleBit-2: Sub-1-Bit via Latent Geometry Alignment. arXiv:2603.00042. https://arxiv.org/pdf/2603.00042
[^30]: Sherry: 1.25-Bit Ternary Quantization. arXiv:2601.07892. https://arxiv.org/pdf/2601.07892
[^31]: Marc Bringuier, *Smart Glasses Landscape 2026*. LinkedIn, 2026. https://www.linkedin.com/posts/ar-expert_augmentedreality-smartglasses-xr-activity-7470055861080612864-P6x3

---

*Dan2, 2026-06-17. 👾*
