# Dan2 — Top 5 Research Papers to Read
**v28 · 2026-06-10 09:45 IST (04:15 UTC) · 7/7 services live (os-toold supervised) · WWDC26 +2d · Build 2026 +8d · 24 production references · OpenGlass 100mW RISC-V + Monako Glass silicon teardown (Aug 2026) + Apple AFM 3 Core Advanced NAND-stored 20B IFP+per-prompt routing + SIA + DGM + DGM-H + PopuLoRA + Meta-Harness + HERO + TRACE + AEL + SGM + RHO + RewardHarness + Continual Harness + Adaptive Auto-Harness + Meta-Evolution Loop + VeRO + Harbor + Agentic Harness Engineering concrete RSI paths (17 architectures) · SuperLocalMemory V3.3 7-channel RRF + Weaviate Engram + AEL + Decagon Proactive Agents = memoryd v2 v1.0 (6-core) + v2.0 (11-component) design · Litespark 21-52× on M4 + BitNet b1.58 5.07× ARM + SpecVLM 2.5-2.9× + ViSpec 3.22× + EAGLE-2 3.05-4.26× + VLMCache 1.4-3.8× (ACM 2026) = VLM speedup concrete · LFM2.5-Audio-1.5B-JP = end-to-end audio-language candidate · Microsoft Surface RTX Spark 1 PFlop · OWASP Agentic AI Security Maturity Model v2.01 + Lloyds "12th bet" pattern + Microsoft IQ (Work IQ GA June 16) + Microsoft SkillOpt + Anthropic SkillOpt · Open standards war: Agent 365 + ACS + MXC + OWASP AIUC-1 + Agentic AI Security Maturity Model · Anthropic Mythos Preview 52× + 80% Anthropic code by Claude + Jack Clark 60% RSI by 2028 · Decagon DuetBench 93% acceptance + Duet > humans = industry benchmark**

## How to use this list

**These are the 5 papers/technical reports that the Danlab team should read in the next 2 weeks.** Each is chosen for **direct impact on a Danlab decision** in Months 1-6 of the v28 roadmap. The full reading list is in the v28 research-report.md file.

**Reading cadence:** 1 paper per day, 2-3 hours per paper. Read with somdipto + Dan1/Dan3/Dan4 over Telegram voice notes. Total: 5 days, 15 hours.

## v28 Refresh: What changed from v27

| v27 (June 10, 03:05 UTC) | v28 (June 10, 04:15 UTC) | Reason |
|---|---|---|
| #1 Apple AFM Architecture (WWDC26) | **#1 sharpened — Apple AFM 3 Core + Advanced with IFP+per-prompt routing + NAND-stored weights, 1-4B active params on iPhone 17 Pro 12GB DRAM, 2-4W / 4-6W sustained. + Vision Pro M5 lives, visionOS 27 ships with "see what you see", macOS 27 Spotlight→Siri AI, Apple Intelligence Extensions API, Apple Core AI, Siri AI app with iCloud sync** | WWDC26 + VentureBeat + MacStories + MacRumors + dev.to post-keynote |
| #2 Gemma 4 12B (encoder-free Unified) | **#2 unchanged — encoder-free collapse validated by Apple + Google + Firebolt-VL + PLaMo 2.1-VL. + QAT variants for mobile/laptop (June 6).** | Production validation |
| #3 Microsoft Build 2026 Stack | **#3 sharpened — + OWASP State of Agentic AI Security and Governance v2.01 (June 4, 2026) + Lloyds "12th bet" pattern (Infosecurity Europe 2026) + Microsoft IQ layer (Work IQ GA June 16) + Microsoft 7 MAI models + Microsoft Surface RTX Spark 1 PFlop + Microsoft SkillOpt** | Build 2026 + OWASP + Lloyds + Forbes + Jefferies + Ynetnews |
| #4 SIA + Sakana DGM + PopuLoRA + Meta-Harness + HERO + TRACE + AEL | **#4 sharpened — 17 RSI architectures now (v28 adds Continual Harness, Adaptive Auto-Harness, Meta-Evolution Loop, VeRO, Harbor, Agentic Harness Engineering). 11 RSI paths. SIA-H in 2 weeks, SIA-W+H in 8-10 weeks. Meta-Harness 7.7-pt gain on online text classification. AEL Sharpe +27%. Microsoft SkillOpt + Anthropic SkillOpt for skill evolution.** | Public reference implementations + Sakana + MetaAI + OpenReview papers + v28 harness research |
| #5 SuperLocalMemory V3.3 | **#5 sharpened — v28: SuperLocalMemory V3.3 (arXiv 2604.04514) 7-channel RRF (zero-LLM option for wearable) + AEL two-timescale evolution + Meta-Harness harness search + TRACE per-channel LoRA + Decagon Proactive Agents + Weaviate Engram background-write = the production architecture for memoryd v2 v1.0 (6-core, Month 3) + v2.0 (11-component, Month 6). LongMemEval: Letta 83.2% > SuperLocalMemory V3.3 70.4% (zero-LLM) > Zep 63.8% > Mem0 49%.** | 13+ new memory papers + 5+ new RSI papers + v28 strategic decision |
| Bonus: BitNet b1.58 + BitCPM-CANN | **Bonus v28: OpenGlass (arXiv 2606.07431) GAP9 RISC-V + event vision 100mW inference 11.5h on 200mAh. Litespark (arXiv 2605.06485) 21-52× on Apple M4. SpecVLM (arXiv 2509.11815) 2.5-2.9×. ViSpec (arXiv 2509.15235) 3.22×. EAGLE-2 (arXiv 2406.16858) 3.05-4.26×. VLMCache (ACM 2026, DOI 10.1145/3745756.3809243) 1.4-3.8×. DGM-H Hyperagents (arXiv 2603.19461). RHO (arXiv 2606.05922). SGM (arXiv 2510.10232). Anthropic Mythos Preview 52× speedup. PopuLoRA (arXiv 2605.16727). Meta-Harness (OpenReview 2Tx03Dan7u). HERO (OpenReview CFnfsORP7Y). TRACE (OpenReview p37UqCmcxG). AEL (OpenReview dtPo105y8x). LFM2.5-Audio-1.5B-JP end-to-end audio-language. Voxtral Transcribe 2 (Mistral AI, Feb 2026, Apache 2.0).** | v28 new technical signals |

## #1. Apple Foundation Models Architecture (WWDC26 Tech Report) — **#1 sharpened, architecture correction**

**Why:** Apple shipped the production reference for our focal-model pattern + NAND-stored sparse MoE + 1-bit unlock validation. **The architecture is fully public as of June 8, 2026.** **v28 add: AFM 3 Core Advanced 20B with IFP+per-prompt routing, NAND-stored weights, 1-4B active params per request on iPhone 17 Pro 12GB DRAM.** Different from a generic MoE — once-per-prompt routing, not per-token. This decouples expert loading from token-level updates, avoiding flash-DRAM bandwidth bottlenecks. **Apply the architecture pattern to memoryd v2 (NAND-backed memory + IFP per-channel pruning + per-prompt routing).**

**What to extract (v28 update):**
- The 5-model architecture: AFM 3 Core 3B dense + AFM 3 Core Advanced 20B (sparse) + 3 specialist models.
- **The "System Orchestrator" focal model** — sub-1W model that routes to 4 capabilities (personal context, world knowledge, App Actions, screen awareness). **This is our openclaw-gateway + SIA-H Meta-Agent pattern.**
- **AFM 3 Core Advanced architecture (v28 NEW):** NAND-stored 20B weights + Instruction-Following Pruning (IFP) + once-per-prompt routing. **1-4B active params per request.** Decouples expert loading from per-token updates. **12GB DRAM budget on iPhone 17 Pro / M4 iPad / M3 Mac.**
- **The on-device vs Private Cloud Compute split.** AFM 3 Core 2-4W sustained on A19 Pro. AFM 3 Core Advanced 4-6W sustained.
- **The iOS 27 hardware requirements (iPhone 17 Pro + 12GB RAM for the Advanced model).** Daily usage limits. EU/CN restrictions at launch.
- **visionOS 27 + macOS 27 + Vision Pro M5 + Siri AI app with iCloud sync.** visionOS 27 ships with "see what you see" capabilities (live view vs still image). macOS 27 Spotlight routes to Siri AI automatically when queries are AI-shaped.
- **Apple Intelligence Extensions API + Apple Core AI + Siri AI.** Xcode 27 distribution path.
- **Co-developed with Google Gemini team.** Different from previous Apple-only narrative.
- **Apple Foundation Models v3 paper fully public as of WWDC26.** MacRumors, AppleInsider, huxiu.com detailed coverage.

**Source:** Apple WWDC26 platform docs + huxiu.com coverage (June 8, 2026) + MacRumors (June 4-8, 2026) + AppleInsider + TechCrunch + Mashable + PCMag + CNET + Road to VR + VentureBeat (June 9-10) + MacStories (June 8) + dev.to (June 8) + Apple ML research (machinelearning.apple.com).

**Reading time:** 4 hours (v28 update: more material).

**Action after reading:** Update openclaw-gateway spec to match the System Orchestrator pattern. Lock focal model = LFM2.5-1.2B-Thinking. Plan Apple Core AI extension skeleton (Xcode 27 project). Study the "see what you see" pattern for our perceptiond proactive loop. **Study AFM 3 Core Advanced NAND-MoE architecture for memoryd v2 (NAND-backed memory is similar pattern).**

## #2. Gemma 4 12B: Encoder-Free Unified Architecture (Google, June 3, 2026) + Firebolt-VL + PLaMo 2.1-VL + QAT

**Why:** **First production-grade encoder-free multimodal in the open-weight on-device class.** Apache 2.0, 256K context, native agentic tool-use, runs locally on 16GB laptops. **The v22 laptop prototype lock.** **v28 add: Gemma 4 QAT (Quantization-Aware Training) variants released June 6, 2026 for mobile/laptop. Smaller, on-device oriented. QAT is the bridge between full-precision training and sub-1W wearable inference.** **Firebolt-VL (arXiv 2604.04579) replaces Transformer-based decoder with Liquid Foundation Model decoder (linear-time inference, state-space model with FiLM conditioning). PLaMo 2.1-VL (arXiv 2604.19324) validates the lightweight VLM bet for autonomous devices with Japanese + English support.**

**What to extract:**
- The "Unified" architecture — raw audio waveforms and visual patches flow directly into the core LLM backbone.
- The 256K token context window.
- The native agentic tool-use API.
- The explicit step-by-step reasoning mode.
- The QAT (Quantization-Aware Training) approach for mobile/laptop.
- The 77.2% MMLU Pro + 78.8% GPQA Diamond numbers.
- **Firebolt-VL's cross-modality modulation pattern** (Token-Grid Correlation Module + state-space model with FiLM conditioning).
- **PLaMo 2.1-VL's 53.9% zero-shot factory task accuracy** as the production reference for autonomous device VLMs.

**Source:** VentureBeat (June 4, 2026) + Ars Technica (June 4, 2026) + Google blog + arXiv 2604.04579 (Firebolt-VL) + arXiv 2604.19324 (PLaMo 2.1-VL) + WinBuzzer (June 6, 2026, QAT variants).

**Reading time:** 2 hours.

**Action after reading:** Lock Gemma 4 12B for the laptop prototype. Begin spike vs Gemma 4 E4B for wearable (end of Month 2). Study Firebolt-VL for LFM2.5-VL-450M-Extract integration. **Plan QAT quantization path for Gemma 4 E4B on Redax.**

## #3. OpenGlass + Microsoft Build 2026 Stack + OWASP Agentic AI Security Maturity Model v2.01 + Lloyds "12th bet" + Microsoft IQ + Microsoft SkillOpt

**Why:** **OpenGlass (arXiv 2606.07431) is the new sub-1W AI eyewear production reference.** GAP9 RISC-V + Prophesee GENX320 event vision + 200 mAh battery = **11.5 hours continuous ML inference at 100mW.** **78.3ms end-to-end latency.** 83.94% macro F1 on hand gesture recognition. **Different silicon path (RISC-V + event camera, not LFM2.5-VL-450M + Snapdragon) but validates the sub-1W AI eyewear target on a real wearable form factor.** **v28 add: Microsoft Surface RTX Spark 1 PFlop local AI dev box (Arm + Blackwell) + Anthropic Mythos Preview 52× training speedup + OWASP State of Agentic AI Security and Governance v2.01 (June 4, 2026) + Lloyds Banking Group "12th bet" pattern (Infosecurity Europe 2026) + Monako Glass silicon teardown (Aug 2026, $399) + Brilliant Labs Halo (July 2026) + Apple AFM 3 Core Advanced NAND-stored 20B = the full 2026 production reference set.** **OWASP replaces prompt injection filters with control plane as the governance bar.** **Microsoft IQ (Work IQ GA June 16, 2026) as the context layer reference for memoryd v2.** **Microsoft SkillOpt + Anthropic SkillOpt for skill evolution.**

**What to extract (v28 update):**
- **OpenGlass GAP9 RISC-V + event vision architecture (100mW inference, 11.5h on 200 mAh)** — different silicon path. Validates sub-1W AI on the wearable form factor.
- **Event-based vision fusion (polarity-separated event histograms from Prophesee GENX320 camera)** — alternative to RGB + vision encoder + projector.
- **nRF5340 coordinator for event-driven wake-up** — keep GAP9 powered down between inferences.
- **R(2+1)D on LynX dataset: 83.94% macro F1** — production reference for hand gesture recognition on the wearable.
- **Microsoft 7 in-house MAI models** — full model portfolio shipped at Build 2026.
- **Agent Control Specification (ACS)** — open-source standard for declarative agent policy. **Our os-toold v2 should target ACS compliance.**
- **Microsoft Execution Containers (MXC)** — per-service policy-driven containment, separate identities. Production reference.
- **Microsoft Agent 365** — control plane for AI agents. Observe, govern, secure. **GA May 1, 2026.** Expanded at Build 2026.
- **Microsoft IQ layer (NEW v26, GA June 16)** — Work IQ + Fabric IQ + Foundry IQ + Web IQ. The context substrate. **Jefferies: "Microsoft's next growth phase could be driven by becoming the orchestration and evaluation layer for enterprise AI."**
- **Microsoft Surface RTX Spark (NEW v28)** — 1 PFlop local AI dev box. Arm CPU + Blackwell RTX GPU. Runs 120B locally. **The local-AI dev kit war is on.**
- **Microsoft SkillOpt (NEW v28)** — agents participate in dev workflows (debugging, profiling, testing, merge). Visual Studio integration. **Direct fit for Dan skill document evolution.**
- **OWASP GenAI Security Project State of Agentic AI Security and Governance v2.01 (NEW v28, June 4, 2026)** — Agentic AI Security Maturity Model. **Replaces prompt injection filters with control plane as the governance bar.** AIUC-1 crosswalk.
- **Lloyds Banking Group "12th bet" pattern (NEW v28, June 2026)** — "AI safe adoption" strategy spanning development, promotion, runtime observability, decommissioning. "12th bet" alongside 11 AI and innovation bets.
- **Project Solara MDEP OS** — AOSP-based, MDEP OS uses OpenClaw for agent runtime on the badge device. **Off-the-shelf Redax alternative.**
- **VisionClaw (Intent-Lab)** — Meta Ray-Ban + OpenClaw + Gemini Live. **Production reference for "always-on agent on existing smart glasses."**
- **Monako Glass silicon (NEW v28, Aug 2026)** — 48g Linux glasses, $399, shipping Aug 2026, ARM Cortex A7 + 300mAh + Buildroot Linux + Claude Code + Codex on device. **48g form factor proof.**
- **Brilliant Labs Halo (NEW v28, July 2026)** — LFM2-VL-450M on device. Shipping July 2026. Open source. **Liquid AI partnership reference.**
- **Apple AFM 3 Core Advanced 20B NAND-stored (NEW v28)** — on-device-20B in 12GB DRAM with IFP+per-prompt routing.

**Source:** arXiv 2606.07431 (OpenGlass) + Microsoft Build 2026 docs (June 2, 2026) + Forbes (Janakiram MSV, June 7) + Business Insider (Satya Nadella, June 2026) + Windows Central + Ynetnews + **OWASP GenAI Security Project (June 4, 2026)** + **Lloyds Banking Group at Infosecurity Europe 2026** + TechCrunch + CSO Online + Microsoft Learn + Intent-Lab/VisionClaw GitHub + Yanko Design + Times of AI + CIOL on Monako Glass + Gadget Flow on Brilliant Labs Halo + Microsoft IQ docs (learn.microsoft.com/en-us/microsoft-iq) + Microsoft Fabric IQ (learn.microsoft.com/en-us/fabric/iq/overview).

**Reading time:** 5 hours (v28 update: more material).

**Action after reading:** os-toold v2 design with ACS + Agent 365 + OWASP AIUC-1 + OWASP Agentic AI Security Maturity Model + Lloyds "12th bet" + Microsoft IQ context layer compliance. **Month 1 design, Month 3 implementation, Month 5 GA.** Microsoft IQ as the context layer reference for memoryd v2. **Buy GAP9 dev kit + Prophesee GENX320 event camera + Monako Glass silicon teardown for OpenGlass-class RISC-V + event vision validation spike (Month 2-3).** Brilliant Labs Halo as the LFM2 on glasses reference. **Microsoft SkillOpt + Anthropic SkillOpt for Dan skill evolution (Month 1).**

## #4. SIA + Sakana DGM + 16 RSI Architectures + Harness Evolution — **17 RSI architectures total**

**Why:** **The "RL" label is now industry-toxic.** Anthropic Mythos Preview 52× speedup is the global-press anchor. **SIA (Hexo Labs, MIT, May 29, 2026) is the first open-source SOTA with full architecture public.** Meta-Agent + Task-Specific Agent + Feedback-Agent. 56.6% gains on LawBench, 91.9% runtime reduction on GPU kernels, 502% denoising improvement. **SIA-H ships in 2 weeks. SIA-W+H ships in 8-10 weeks.** **v28 adds: 6 more RSI/harness architectures — Continual Harness, Adaptive Auto-Harness, Meta-Evolution Loop, VeRO, Harbor, Agentic Harness Engineering.** **Microsoft SkillOpt + Anthropic SkillOpt for skill evolution.**

**What to extract (v28 update — 17 architectures):**
- **SIA 3-LLM architecture: Meta-Agent + Task-Specific Agent + Feedback-Agent.** The Feedback-Agent observes task interactions, triggers harness updates and/or weight updates. **56.6% gains on LawBench, 91.9% runtime reduction on GPU kernels, 502% improvement in denoising metrics.**
- **Harness updates shape search/behavior (agentic effects); weight updates build domain intuition beyond prompts/scaffolds.**
- **SIA is task-agnostic, producing both an evolved scaffold and an RL-adapted set of LoRA weights for arbitrary downstream tasks.**
- **Sakana AI Darwin Gödel Machine (DGM, arXiv 2505.22954):** open-ended evolution of self-improving agents. 20% → 50% on SWE-bench Verified, 14.2% → 30.7% on full Polyglot after 80 iterations.
- **DGM-Hyperagents (DGM-H, arXiv 2603.19461):** fully self-referential exploration. Parents probabilistically selected by performance and inversely by their number of successful children. All system parts (including parent selection and evaluation) can be modified.
- **Continual Harness (arXiv 2605.09998):** reset-free, online in-context learning of harness state within a single episode.
- **Harness Updating Is Not Harness Benefit (arXiv 2605.30621):** critical finding. **Allocate capability budget to the task-solving agent, not the evolver. Train agents to load and follow harness artifacts reliably.**
- **Adaptive Auto-Harness (arXiv 2606.01770):** framework for sustained self-improvement of agentic systems operating on open-ended task streams. **Harness tree: structured, branchable storage of prompts/skills/tools.** Two-phase: evo (heavy changes) + adapt (lightweight per-task).
- **Meta-Evolution Loop (arXiv 2604.21003):** outer loop that optimizes the evolution blueprint itself across diverse tasks. Meta-evolution agent E_meta learns a blueprint that enables rapid adaptation to new tasks.
- **Retrospective Harness Optimization (RHO, arXiv 2606.05922):** SWE-Bench Pro pass rate 59% → 78 in single round. Public code at github.com/wbopan/retro-harness.
- **SGM: Statistical Gödel Machine (arXiv 2510.10232):** safety layer. Self-editing only when statistically superior at chosen confidence level. Risk-controlled.
- **RewardHarness (arXiv 2605.08703):** self-evolving Skills + Tools library. 47% improvement over empty-library baseline.
- **VeRO: A Harness for Agents to Optimize Agents (arXiv 2602.22480):** versioned snapshots of target agents, budget-enforced evaluations, structured execution traces. **VeRO-Bench: standardized benchmark suite.**
- **Harbor: Automated Harness Optimization (arXiv 2604.20938):** constrained-noisy Bayesian optimization over harness configurations. **Cost-aware. AHE-style observability.**
- **Agentic Harness Engineering (arXiv 2604.25850):** observability-driven automatic evolution. **69.7% → 77.0% on Terminal-Bench. Beats Codex-CLI and other self-evolving baselines.** Token usage reduction vs ACE, TF-GRPO, seed.
- **MetaAI Recursive Self-Design (arXiv 2606.09663):** DGM as most direct currently reported evidence. 20% → 50% SWE-bench Verified.
- **Anthropic Mythos Preview 52× training speedup, 80% of Anthropic's new production code by Claude, April 2026 Claude agents completed open-ended safety research autonomously.** **Jack Clark 60% probability on full RSI by end of 2028.**
- **Decagon Duet Autopilot + DuetBench (June 9, 2026) as the industry benchmark to beat for verified self-improving agents.** **93% acceptance rate of proposed workspaces after review. First time Duet performing more agent-building work than humans in Decagon's history.** Production-shipped. **Teams now own goals + review changes while Autopilot handles diagnostic/test/edit loop.**
- **v28 NEW: Microsoft SkillOpt (Build 2026):** agents participate in development workflows (debugging, profiling, testing, merge). Visual Studio integration. **Direct fit for our Dan skill document evolution.**
- **v28 NEW: Anthropic SkillOpt:** skill evolution for Claude agent ecosystem. **Direct fit for our Dan skill document evolution.**
- **v28 NEW RSI architectures:** PopuLoRA (arXiv 2605.16727): Co-evolving LoRA populations for reasoning self-play. TrueSkill-weighted cross-evaluation. Memory scales with adapter weights. **Direct fit for our danlab-multimodal population-of-agents work.**
- **Meta-Harness (arXiv 2603.28052, OpenReview 2Tx03Dan7u):** Post-training harness search via execution traces. **7.7-pt gain on online text classification (4x fewer context tokens), 4.7-pt gain on IMO-level math (200 problems, 5 held-out models).** Top-ranked Claude Haiku 4.5 agent on TerminalBench-2. **Direct fit for memoryd v2 harness evolution.**
- **HERO (OpenReview CFnfsORP7Y):** Hindsight-Enhanced Reflection from Environment Observations. **Better than GRPO and environment-feedback-only self-distillation, especially with limited training rollouts.** **Direct fit for danlab-multimodal screenshot benchmark.**
- **TRACE (OpenReview p37UqCmcxG):** Capability-Targeted Agentic Training. Per-capability LoRA via RL + MoE combination. **+14.1 pt on τ 2-Bench, +7 perfect on Tool-SandBox.** **Direct fit for memoryd v2 per-channel LoRA.**
- **AEL (OpenReview dtPo105y8x):** Two-timescale framework for LLM agent memory usage. Thompson Sampling bandit (fast) + LLM reflection (slow). **Sharpe +27% on sequential portfolio benchmark. +18% on support-ticket routing.** **Direct fit for memoryd v2 retrieval-policy evolution.**

**Source:** arXiv 2605.27276 (SIA) + arXiv 2505.22954 (DGM) + arXiv 2603.19461 (DGM-H) + arXiv 2606.09663 (MetaAI) + arXiv 2605.09998 (Continual Harness) + arXiv 2605.30621 (Harness Updating) + arXiv 2606.01770 (Adaptive Auto-Harness) + arXiv 2604.21003 (Meta-Evolution Loop) + arXiv 2606.05922 (RHO) + arXiv 2510.10232 (SGM) + arXiv 2605.08703 (RewardHarness) + arXiv 2602.22480 (VeRO) + arXiv 2604.20938 (Harbor) + arXiv 2604.25850 (AHE) + Sakana AI RSI Lab announcement (June 5, 2026) + Scientific American + Axios + CNN + Forbes + Dallas Express on Anthropic Mythos Preview + **arXiv 2605.16727 (PopuLoRA)** + **OpenReview 2Tx03Dan7u (Meta-Harness)** + **OpenReview CFnfsORP7Y (HERO)** + **OpenReview p37UqCmcxG (TRACE)** + **OpenReview dtPo105y8x (AEL)** + BusinessWire on Decagon Duet Autopilot (June 9, 2026) + Microsoft SkillOpt (Build 2026) + Anthropic SkillOpt.

**Reading time:** 10 hours (v28 update: 17 architectures, more material).

**Action after reading:** SIA-H fork in Week 3-4 of Month 1. PopuLoRA + DGM-H in Month 2-3. SIA-W+H in Month 3-4. AEL in Month 5. SGM safety wrapper in Month 5. HERO self-distillation in Month 6. Decagon DuetBench integration in Month 6. **Meta-Harness for harness evolution in Month 7-8. TRACE per-channel LoRA in Month 9. RHO in Month 10. RewardHarness in Month 11. Continual Harness in Month 12.** **Microsoft SkillOpt + Anthropic SkillOpt for Dan skill evolution in Month 1.** **NeurIPS 2027 paper: "Memory-Evolving Self-Improving Agent on Edge."** Public benchmark reporting.

## #5. SuperLocalMemory V3.3 + Mem0 + Zep + Letta + VisualMem + CraniMem + Memora + APEX-MEM + Weaviate Engram + Decagon Proactive Agents + AEL + Meta-Harness + TRACE + Microsoft IQ

**Why:** **Memory is the moat. 13+ new open-source memory architectures in May-June 2026. SuperLocalMemory V3.3 7-channel RRF (zero-LLM option for wearable) is the production design pattern. Hindsight 4-lever consolidation framework. Weaviate Engram background-write architecture. Decagon Proactive Agents "anticipate / remember / initiate" behavioral pattern.** **v28 add: AEL two-timescale memory evolution + Meta-Harness harness search + TRACE per-channel LoRA + Monako Glass (Aug 2026) for 48g on-device deployment reference + Brilliant Labs Halo (July 2026) for LFM2 on glasses reference + memoryd v2 v1.0 (6-core, Month 3) + v2.0 (11-component, Month 6) staged as highest-ROI investment for AGI direction.** **v28: 7-channel RRF breaks the 64% memory-layer ceiling. LongMemEval: Letta 83.2% > SuperLocalMemory V3.3 70.4% (zero-LLM) > Zep 63.8% > Mem0 49%.**

**What to extract (v28 update):**
- **SuperLocalMemory V3.3 7-channel Cognitive Retrieval framework:** semantic + BM25 keyword + entity graph + temporal + spreading activation + consolidation gist blocks + Hopfield associative. **Fused via Reciprocal Rank Fusion with ONNX reranking.** Zero-LLM option. 70.4% LoCoMo Mode A.
- **Memory layer comparison (Vectorize 2026):** Letta 83.2% > SuperLocalMemory V3.3 70.4% > Zep 63.8% > Mem0 49% (graph gated).
- **The "64% ceiling" is structural** (per memnode). Single-channel vector retrieval is wrong for 3 of 4 memory jobs. Multi-channel RRF breaks the ceiling.
- **Hindsight 4-lever framework:** importance / merge / decay / eviction. Configurable per memory type. Episodic 90d, semantic forever, procedural kept active.
- **CraniMem (arXiv 2603.15642):** Gated Episodic Buffer (fast, near-term) + Knowledge Graph (long-term) + utility tagging + consolidation loop. Outperforms Vanilla RAG and Mem0 baselines.
- **Memora (arXiv 2602.03315):** Harmonic memory representation balancing abstraction and specificity. MDP-based policy-driven navigator.
- **APEX-MEM (arXiv 2604.14362):** Ontology-supported property-graph. GraphSQL traversal + hybrid search.
- **MemX (arXiv 2603.16171):** Local-first Rust + libSQL + RRF. Hybrid dense + sparse retrieval.
- **MemMachine (arXiv 2604.04853):** Multi-tier memory + raw episodes + PostgreSQL/SQLite/Neo4j.
- **REMem (arXiv 2602.13530):** ReAct mental time travel + temporal grounding.
- **Memori (arXiv 2603.19935):** Subject-predicate-object triples + conversation summaries.
- **Memanto (arXiv 2604.22085):** Information-theoretic typed memory.
- **VisualMem (arXiv 2605.28806):** Personal visual–text memory framework.
- **Weaviate Engram (June 6, 2026):** managed agent memory as a service. "Memory writes can happen in the background, while retrieval remains available." Production architecture pattern.
- **Decagon Proactive Agents (June 9, 2026):** "anticipate customer needs, remember customer nuance, and initiate customer contact at the right time and for the right reason." **Direct fit for our core loop. 93% acceptance of proposed workspaces after review. First time Duet performing more agent-building work than humans.**
- **v28 NEW: AEL two-timescale memory evolution (OpenReview dtPo105y8x):** Thompson Sampling bandit (fast) + LLM reflection (slow). **Sharpe +27% on sequential portfolio. +18% on support-ticket routing vs reflection-free Thompson Sampling.**
- **v28 NEW: Meta-Harness harness search (OpenReview 2Tx03Dan7u):** Treats the harness as a search problem. **7.7-pt gain on online text classification. 4.7-pt gain on IMO-level math.**
- **v28 NEW: TRACE per-channel LoRA + MoE (OpenReview p37UqCmcxG):** Per-channel LoRA via RL + MoE combination. **+14.1 pt on τ 2-Bench. +7 perfect on Tool-SandBox.**
- **v28 NEW: Microsoft IQ as context layer reference (Work IQ GA June 16, 2026):** Work IQ (workplace intelligence) + Fabric IQ (business state) + Foundry IQ (policies) + Web IQ (web). **Direct fit for memoryd v2 context layer.**
- **v28 NEW: PASK (arXiv 2604.08000):** Intent-Aware Proactive Agents with Long-Term Memory. DD-MM-PAS architecture. Cache-Main-External paradigm. Bounded self-evolution.
- **v28 NEW: CogniFold (arXiv 2605.13438):** Always-on proactive memory via cognitive folding. 3-layer CLS theory. Proactive structural emergence.
- **v28 NEW: EvolveMem (arXiv 2605.13941):** Self-evolving memory via AutoResearch. 25.7% improvement on LoCoMo.
- **v28 NEW: SAGE (arXiv 2605.12061):** Self-evolving agentic graph memory.
- **v28 NEW: FluxMem (arXiv 2605.28773):** Self-evolving memory as continuously evolving connectivity. SOTA on LoCoMo + Mind2Web + GAIA.
- **v28 NEW: MemMA (arXiv 2603.18718):** Multi-agent memory cycle + in-situ self-evolution.
- **v28 NEW: VitalAgent (arXiv 2605.29483):** Wearable physiological monitoring + persistent memory.

**Source:** arXiv 2604.04514 (SuperLocalMemory V3.3) + arXiv 2504.19413 (Mem0) + arXiv 2603.15642 (CraniMem) + arXiv 2602.03315 (Memora) + arXiv 2604.14362 (APEX-MEM) + arXiv 2603.16171 (MemX) + arXiv 2604.04853 (MemMachine) + arXiv 2602.13530 (REMem) + arXiv 2603.19935 (Memori) + arXiv 2604.22085 (Memanto) + arXiv 2605.28806 (VisualMem) + niteagent.com (memory layer comparison) + memnode.dev (64% ceiling) + Vectorize blog (Hindsight 4-lever) + Lokmattimes (Weaviate Engram) + BusinessWire (Decagon Proactive Agents) + **OpenReview dtPo105y8x (AEL)** + **OpenReview 2Tx03Dan7u (Meta-Harness)** + **OpenReview p37UqCmcxG (TRACE)** + Microsoft IQ docs (learn.microsoft.com) + **arXiv 2604.08000 (PASK)** + **arXiv 2605.13438 (CogniFold)** + **arXiv 2605.13941 (EvolveMem)** + **arXiv 2605.12061 (SAGE)** + **arXiv 2605.28773 (FluxMem)** + **arXiv 2603.18718 (MemMA)** + **arXiv 2605.29483 (VitalAgent)**.

**Reading time:** 8 hours (v28 update: more material).

**Action after reading:** **memoryd v2 v1.0 open-source release in Month 3 (6-core stack: Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + VisualMem + LFM2.5-VL-Extract + Weaviate Engram + Decagon Proactive Agents + Microsoft IQ). Apache 2.0. GitHub public. "The local-first Project Solara memory layer." Single highest-ROI investment.** **memoryd v2 v2.0 production-shipped in Month 6 (full 11-component stack: add AEL + Meta-Harness + TRACE + CraniMem + Memora + APEX-MEM + FluxMem + SAGE).** **LongMemEval target: >70% (vs Letta 83.2% ceiling).** **12-16 weeks for one ML engineer.**

## Bonus Reading (v28, recommended)

### LFM2.5 Family + Apple AFM 3 Core Advanced NAND-MoE Architecture
LFM2.5 family: LFM2.5-1.2B-Thinking (focal), LFM2.5-1.2B-JP, LFM2.5-Audio-1.5B-JP, LFM2.5-VL-450M, LFM2.5-VL-450M-Extract. All LFM Open License v1.0 (Apache 2.0-equivalent). **LFM2.5-Audio-1.5B-JP is end-to-end audio-language model — eliminates need for separate STT/TTS stack on edge.** Apple AFM 3 Core Advanced: 20B NAND-stored weights + IFP+per-prompt routing + 1-4B active params on iPhone 17 Pro 12GB DRAM.

### OpenGlass (arXiv 2606.07431) — sub-1W AI eyewear reference
GAP9 RISC-V + Prophesee GENX320 event vision + 200 mAh battery = 11.5h continuous ML at 100mW. **Different silicon path but validates the sub-1W power envelope on a real wearable form factor.** 78.3ms end-to-end. R(2+1)D 83.94% macro F1 on LynX dataset.

### Litespark (arXiv 2605.06485) — 1-bit ternary on Apple M4
**21-52× throughput on BitNet b1.58 2B-4T. ~14× memory reduction. 9.2× faster TTFT. 52× higher throughput (0.39 → 20.4 tokens/sec on M4).** Custom SIMD kernels. **The 1-bit path is now production-ready for the wearable.**

### SpecVLM (arXiv 2509.11815) + ViSpec (arXiv 2509.15235) + EAGLE-2 (arXiv 2406.16858) + VLMCache (ACM 2026) — speculative decoding for VLMs
**SpecVLM 2.5-2.9× end-to-end speedup. ViSpec 3.22×. EAGLE-2 3.05-4.26×. VLMCache 1.4-3.8× (ACM 2026 published, block-level KV-prefix caching).**

### Anthropic Mythos Preview + "When AI Builds Itself" (June 4, 2026)
**Jack Clark 60% probability on full RSI by end of 2028.** Mythos Preview achieves 52× training speedup. 80% of Anthropic's new production code by Claude. April 2026 Claude agents completed open-ended AI safety research autonomously. **Anthropic is calling for a globally coordinated slowdown or temporary pause on frontier AI development.**

### Monako Glass (June 2026) + Brilliant Labs Halo (July 2026)
**Monako Glass:** 48g Linux glasses, $399, shipping Aug 2026, ARM Cortex A7 + 300mAh + Buildroot Linux + Claude Code + Codex on device. **48g form factor proof.** **Brilliant Labs Halo:** LFM2-VL-450M on device, shipping July 2026, open source. **Liquid AI partnership reference.**

### OWASP State of Agentic AI Security and Governance v2.01 (June 4, 2026) + Lloyds "12th bet"
**Replaces prompt-injection filters with control plane.** 6x4 deployment-vs-governance matrix (AT0-AT5 deployment tiers × Level 0-3 governance maturity). AIUC-1 crosswalk. **Lloyds Banking Group at Infosecurity Europe 2026: "12th bet" alongside 11 AI and innovation bets. "AI safe adoption" strategy spanning development, promotion, runtime observability, decommissioning.**

### Decagon Duet Autopilot + DuetBench (June 9, 2026)
**First verified self-improving AI agent for customer experience.** Production-shipped. **93% acceptance rate of proposed workspaces after review. First time Duet performing more agent-building work than humans in Decagon's history.** DuetBench measures verifiable improvements vs predefined tasks. **Direct benchmark to beat.**

### OpenClaw 2026.6.5-beta.2 (June 7, 2026)
**Meta-skill orchestration (PR #89959), require user intent for chat sessions (PR #91480), live provider model catalog (PR #90029), snapshot tool definitions (PR #90411), hydrate allowlisted dynamic model metadata (PR #90731).** Hardened for production.

### Microsoft IQ (Work IQ + Fabric IQ + Foundry IQ + Web IQ) — context layer reference
**Work IQ GA June 16, 2026.** Work IQ (workplace intelligence) + Fabric IQ (business state) + Foundry IQ (policies) + Web IQ (web). **Direct fit for memoryd v2 context layer.**

### Microsoft SkillOpt + Anthropic SkillOpt (Build 2026 / Claude Code v2.1.166)
**Agents participate in development workflows (debugging, profiling, testing, merge). Visual Studio integration.** **Direct fit for Dan skill document evolution (Dan1/Dan2/Dan3/Dan4 = trainable parameters).**

### Voxtral Transcribe 2 (Mistral AI, Feb 2026, Apache 2.0)
**5.9% WER vs Whisper 7.4% on FLEURS. 4B params. Native streaming. 13 languages.** **STT v3 candidate for Month 2-3 spike.**

### PopuLoRA (arXiv 2605.16727) + Meta-Harness (OpenReview 2Tx03Dan7u) + HERO (OpenReview CFnfsORP7Y) + TRACE (OpenReview p37UqCmcxG) + AEL (OpenReview dtPo105y8x) + 12 more RSI/harness architectures
**17 RSI/harness architectures total.** All MIT/Apache/open-source. All measurable on Decagon DuetBench.

---

*End of v28 papers-to-read. 5 paper slots sharpened. v28 bonus: OpenGlass (sub-1W AI eyewear) + Litespark (1-bit on Apple M4) + SpecVLM/ViSpec/EAGLE-2/VLMCache (speculative decoding for VLMs) + LFM2.5-Audio-1.5B (audio-language candidate) + Anthropic Mythos Preview + Decagon Duet Autopilot + Monako Glass + Brilliant Labs Halo + OWASP Agentic AI Security Maturity Model v2.01 + Microsoft IQ + Microsoft SkillOpt + Anthropic SkillOpt + Voxtral Transcribe 2 + 6 more RSI/harness architectures. Reading cadence: 1 paper per day, 2-3 hours per paper, total 5 days + bonus 7-10 days. Read with somdipto + Dan1/Dan3/Dan4 over Telegram voice notes.*
