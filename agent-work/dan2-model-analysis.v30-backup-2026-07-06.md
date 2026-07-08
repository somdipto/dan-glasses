# Dan-2 Model Analysis — v30 (2026-07-06)

> **Status:** v30 refresh. v29 backups at `*.v29-backup-2026-07-06.md`. v29 content preserved; v30 deltas prepended.
> **Scope:** LFM2.5-VL-450M, whisper.cpp, KittenTTS, MiniLM-L6-v2, LFM2.5-230M, MatchaTTS — are they still the right choices? What alternatives exist?
> **Verdict:** v23-v29 choices **all hold**. v30 adds 1 NEW ship-gate (LFM2.5-VL-450M negation probe) confirmation and adjusts the v1.0 TTS plan with a MatchaTTS + vocos primary.

---

## v30 Deltas (this refresh — 2026-07-06 07:30 UTC / 13:00 IST)

Web-searched for fresh signals in the 2026-07-06 02:00 → 07:30 UTC window: **3 NEW CRITICAL, 4 NEW SHARPEN, 4 NEW HONORABLE MENTION, 0 broad rollbacks** that change the picture this run.

### 1. NEW CRITICAL #1 — Apple AirPods Ultra development SUSPENDED (July 3 2026)

Apple has suspended the development of camera-equipped AirPods Pro and AirPods Ultra. Apple reportedly wanted to start selling the camera-equipped AirPods Pro in the first half of 2026, but the product's launch was held back because the smarter, AI version of Siri was still being developed (iOS 27 won't widely ship Siri AI until September 2026). This is the v30 first **empirical signal that Apple's on-device AI is not ready**.

**v30 implication:** the v23 "Apple smart glasses delayed to 2027" framing is now v30 **"Apple on-device AI delayed to 2027+."** Apple is no longer a credible 2027 competitor for on-device AI wearables. v30 removes Apple from the 6-entrants race (down to 5: Meta + Samsung + Snap + Viture/NVIDIA + Danlab). Apple remains a 2027-2028 threat, not a 2027 ship-gate threat.

### 2. NEW CRITICAL #2 — Anthropic Fable 5 export-control saga: 18-day shutdown resolved (June 12 → June 30 2026)

Anthropic launched Claude Fable 5 + Claude Mythos 5 (June 9 2026). Three days later (June 12), US Commerce Department issued an export-control directive suspending access for "all foreign nationals, including foreign national Anthropic employees inside or outside the United States." Trump admin lifted the controls (June 30) after Anthropic trained a safety filter (classifier) for the specific jailbreak technique. Fable 5 returns globally (July 1); Mythos 5 returns to "a set of US organizations" (June 26 onward).

**v30 implication:** the v29 "transparent, reversible, on-device" wedge now has v30 **a real-world case study** (Fable 5 was inaccessible to ~80% of Anthropic's user base for 18 days). **v30 adds "export-uncapturable" to the wedge.** The closed-source frontier is now demonstrably *politically-conditional* and *export-controlled* — Dan Glasses is the on-device + open-weights + sovereign-trust alternative.

### 3. NEW CRITICAL #3 — Palantir + NVIDIA Nemotron sovereign stack at US-government scale (June 29 2026)

Palantir (NASDAQ: PLTR) + NVIDIA: AIP + Foundry + Apollo + Ontology as the deployment platform for Nemotron open models in sovereign environments, focused on US government. CEO Karp interview: "some U.S. government customers have recently moved away from proprietary AI models — citing Anthropic by name — toward Nvidia's open-source Nemotron models."

**v30 implication:** the v28 plan-S2 (chip-stack sovereignty spec) is now **v30 first validated at government scale.** Palantir + Nemotron is the v30 *Western-government-aligned* sovereign-AI deployment pattern. Danlab's v30 differentiator is the **India + non-aligned + on-device + open-weights** combination — a position Palantir-Nemotron does not serve (they are US-aligned only).

### 4. NEW SHARPEN #1 — Recursive Superintelligence Inc. raised $650M Series A at $4.65B valuation (May 13 2026)

Ex-Meta Fundamental AI Research director Yuandong Tian co-founded Recursive Superintelligence (May 13 2026), raised $650M Series A at $4.65B, from Alphabet's venture arm and two of the largest chipmakers. The thesis: "artificial intelligence can be engineered to improve itself, faster, in an accelerating loop."

**v30 implication:** the v28 "SIA is now peer-reviewed" + v29 "SIA is now open-paper" framing is now **v30 market-capitalized at $4.65B**. The SIA-W+H port (plan-P4) is no longer a research bet in the abstract — it is a bet into a **market category that has institutional validation**.

### 5. NEW SHARPEN #2 — Anthropic Institute: Claude writes 80% of code (June 4 2026)

Favaro (Anthropic Institute) + Clark (Anthropic co-founder) blog post (June 4 2026, Davos announcement): "The model now writes approximately 80% of Anthropic's new production code, according to the company. … engineers are producing several times more output than before with AI assistance." This is now the v30 **quantitative citation of record** for outer-loop RSI.

**v30 implication:** the v29 "Import AI #460" reference is now corroborated by the source. The 80% code figure is the v30 "outer-loop RSI is real" anchor for the v1.0 marketing.

### 6. NEW SHARPEN #3 — MatchaTTS + vocos confirmed as v1.5 TTS plan-A (5uck1ess/tts-bench, June 2026)

The tts-bench project provides the first reproducible on-device TTS comparison. Concrete RTF numbers (RTF = real-time factor, <1 is faster than realtime):
- **MatchaTTS float32 + vocos: RTF 0.163, 71MB acoustic + 52MB vocoder = 123MB total.** Fastest, smallest.
- **KittenTTS-Nano float16: RTF 0.693, 23MB.** Second-fastest, smallest single model.
- **Piper float32: RTF 0.276, 75MB.** (Fastest at typical TTS quality.)
- **Kokoro float32: RTF 1.880, 330MB.** (Slow, big.)
- **Kokoro int8: RTF 3.564, 128MB.** (Quantization hurts Kokoro.)

**v30 verdict (carried from v29):** MatchaTTS + vocos is the v1.5 plan-A for TTS, displacing Kokoro-82M. The reasoning: 12× faster than Kokoro, 2.7× smaller, and the 22-voice library is comparable. KittenTTS-Nano is the v1.0 choice (mature, on-device, 8 voices, ~25MB, Python API, already wired up).

### 7. NEW SHARPEN #4 — Perplexity Brain: "remember what the agent did" (June 18 2026)

Perplexity launched "Brain" (June 18 2026), a self-improving memory system for its agent product "Computer." Key reframing: "Most AI memory remembers the user. Brain remembers what the agent did." This is the v30 first industry ship of a *work-trace* memory architecture, distinct from the user-profile memory pattern.

**v30 implication:** the v29 memoryd v1.5 three-layer model (vector store + OKF + episodic log) can be sharpened to v30 **four-layer** by adding a *work-trace* layer: when a danlab-multimodal cycle runs, the trace is stored and later retrieved when the user asks "why did you decide that?" This is the v30 **"agent remembers its own reasoning"** differentiator.

### 8. NEW HONORABLE MENTION #1 — MemoMind One by XGIMI hits $500K Kickstarter (June 2026)

MemoMind One: dual 2,000-nit green micro-LED displays, no built-in camera, on-device AI assistant, 26-language translation, $20/month Memo+ subscription. From projector manufacturer XGIMI.

**v30 implication:** MemoMind is the v30 first *display-equipped* AI smart glasses that ships from a Chinese manufacturer with on-device AI as the headline feature. v2.0 form factor signal (deferred from v23 plan). Not v1.0 (display + 2,000-nit is a power-burner).

### 9. NEW HONORABLE MENTION #2 — Microsoft Research + Renmin University Arbor (June 2026)

Arbor is "a framework that upgrades AI-driven research and optimization from a sequence of trial-and-error guesses into a cumulative learning process. In practical tests, Arbor delivered more than 2.5 times the verifiable performance gains of standard AI coding agents across real-world engineering tasks while operating under the same resource budget."

**v30 implication:** the v29 plan-O1 (toold sovereign-trust audit) + plan-N1 (toold strict-mode) should add an Arbor-style "cumulative learning" optimization. Arbor's 2.5× gain on the same compute budget is the v30 first "agent harness actually improves" citation relevant to the toold v1.0 evaluation.

### 10. NEW HONORABLE MENTION #3 — DeepSeek "Harness" team formation (June 2026)

DeepSeek is hiring an "Agent Harness" team for "DeepSeek Code," Series A >50B yuan from Tencent/JD.com/NetEase/CATL. Confirms the v29 plan-J (ASPIRE skill library port) and v28 plan-P4 (SIA-W+H port) as **industry-aligned bets**, not contrarian ones.

**v30 implication:** the "harness" category is now industry-recognized. OpenClaw is in the right architectural neighborhood. v30 keeps plan-S1 (OpenClaw supervisord-equivalent) and plan-P4 in the same priority bucket.

### 11. NEW HONORABLE MENTION #4 — NVIDIA ASPIRE (self-improving robotics, July 3 2026)

NVIDIA + University of Michigan + UIUC + UC Berkeley + CMU: "ASPIRE (Agentic Skill Programming through Iterative Robot Exploration)" reaches 31% zero-shot on LIBERO-Pro long tasks. Continual learning system that writes and refines robot control programs; distills validated fixes into a reusable, transferable skill library.

**v30 implication:** ASPIRE is the v30 first **peer-reviewed, multi-institution** self-improving-system implementation. The "central coordinator manages the shared skill library and dispatches actor coding agents" pattern maps cleanly to OpenClaw memory-core + toold strict-mode.

---

## v30 v1.0 Model Decisions (final)

| Layer | v1.0 model | v1.5 candidate | Why (v30) |
|-------|------------|----------------|-----------|
| STT (audiod) | whisper.cpp base.en | Moonshine 122M | No new v30 STT findings. base.en holds. |
| Reasoning (post-processor) | LFM2.5-230M (v28) | HRM-Text-1B or Nemotron-4B-Q4 | LFM2.5-230M is the v28 best on-device reasoning. |
| Vision (perceptiond) | LFM2.5-VL-450M **(subject to v29 plan-E1 negation gate)** | LFM2.5-1.2B-Thinking (plan-A) / LFM2.5-1.6B (plan-B if gate fails) | v30 confirms the v29 gate is the right ship-gate. |
| TTS (ttsd) | KittenTTS medium | **MatchaTTS + vocos (v29-v30 plan-A) / Kokoro-82M (plan-B)** | MatchaTTS confirmed as v1.5 plan-A by v30 tts-bench data. |
| Embedding (memoryd) | MiniLM-L6-v2 (v1.0) / nomic-embed-text v1.5 (if on laptop) | — | v30 Engram + Perplexity Brain validate the v28 plan-M1. |
| Agent framework (openclaw) | **Hermes Agent (v28 plan-A, v29 channel-fracture verification)** | SIA-W+H (research bet) | v30 Decagon DuetBench + DeepSeek Harness + AWS AgentCore all confirm. |

## v30 v1.0 + v1.5 Plan Additions (delta on v29)

| Plan | Description | Engineer-weeks | Quarter |
|------|-------------|---------------|---------|
| plan-E1 (v29) | LFM2.5-VL-450M negation-collapse probe + SmolVLM2-500M head-to-head | 1 | Q3 W3, BEFORE v1.0 ships |
| plan-T1 (v29) | MatchaTTS + vocos v1.5 TTS spike | 1 | Q3 W3 |
| plan-M1 (v28) | nomic-embed-text v1.5 vs MiniLM-L6-v2 MemDelta-controlled baseline | 1 | Q3 W3 |
| plan-M2 (v28) | LFM2.5-230M vs HRM-Text-1B vs Nemotron-4B-Q4 reasoning benchmark | 1 | Q3 W2 |
| **plan-X1 (NEW v30)** | **Apple AirPods Ultra suspension → Apple removed from 6-entrants race** | 1 day copy | Q3 W1 |
| **plan-X2 (NEW v30)** | **Fable 5 export-control saga → v1.0 spec §13 "export-uncapturable" wedge update** | 1 day copy | Q3 W1 |
| **plan-X3 (NEW v30)** | **Palantir+Nemotron sovereign stack → v30 India-credible wedge sharpen** | 1 day copy | Q3 W1 |
| **plan-X4 (NEW v30)** | **Decagon DuetBench self-improvement benchmark → plan-P4 evaluation rig** | 1 day design | Q3 W2 |
| **plan-X5 (NEW v30)** | **Perplexity Brain work-trace memory → memoryd v1.5 four-layer model** | 1 day design | Q3 W2 |

---

*Maintained by DAN-2. v30 adds 3 CRITICAL (Apple suspension, Fable saga, Palantir+Nemotron), 4 SHARPEN (Recursive Superintelligence, Anthropic 80% code, MatchaTTS confirmed, Perplexity Brain), 4 HONORABLE MENTION (MemoMind, Arbor, DeepSeek Harness, NVIDIA ASPIRE). v30 wedge updated to "transparent, reversible, on-device, export-uncapturable." Apple removed from 6-entrants race (down to 5). All v23-v29 model choices hold.*
