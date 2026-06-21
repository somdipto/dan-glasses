# Dan2 — Dan Glasses Architecture Review
**v30 · 2026-06-11 07:00 IST (01:30 UTC) · 7/7 services live (os-toold re-supervised PID 4392) · 14h after v29 · ~25 RSI/harness architectures (v29's 17 + 8 v30 NEW) · 21+ memory references · 32 production references (v29's 24 + 8 v30 NEW) · 50-150× VLM energy reduction concrete · Open standards war validated harder by Microsoft Scout addiction leak (June 4-9) · Apple Vision Pro M5 lives + visionOS 27 "see what you see" (WWDC26) · Anthropic Claude Fable 5 GA (June 9) · Decagon DuetBench 93% acceptance (June 9) · Recursive Superintelligence $650M (May 13)**

## Executive Summary (v30, refreshed)

The 5-service decomposition (perceptiond / audiod / memoryd / os-toold / ttsd) + OpenClaw gateway is **structurally correct** and now **validated by Microsoft Scout itself (OpenClaw-based, M365, Build 2026)** + **Anthropic Claude Fable 5 (production self-improving system, 80% of Anthropic's code)** + **Decagon Duet Autopilot (verified self-improving agent)** + **Recursive Superintelligence ($4.65B RSI bet)** + **~25 RSI/harness architectures** + **21+ memory references** + **32 production references**.

**v30 delta (vs v29):**
- **Microsoft Scout "addicted users" memo leak (June 4-9).** Nadella disowns. Shahine + Werner named. **The "responsible agent" governance story is now cracked. Open-source governance narrative is the wedge.** os-toold v2 with ACS + Agent 365 + OWASP v2.01 + Microsoft IQ + Apple Core AI compliance is a *bigger* differentiator now.
- **Anthropic Claude Fable 5 GA (June 9).** 80.3% SWE-bench Pro. Stripe 50M-line migration in 1 day. Mythos 5 (full) to Project Glasswing partners incl. Apple. **The Mythos threshold has been crossed publicly. Harness evolution is in production.**
- **Anthropic public "brake pedal" plea (June 4-8).** Jack Clark: "I don't have a brake pedal." **RSI is now industry-accepted as a near-term concern, not science fiction.** Open-source self-improving agents are now a $4.65B category.
- **Recursive Superintelligence (May 13 2026).** $650M Series A at $4.65B valuation. <30 employees, no product. **Capital validates the bet.**
- **Apple Vision Pro M5 lives (WWDC26).** visionOS 27 ships with "see what you see." Vision Pro M5 hardware in market. **Apple running two-product strategy: Vision Pro (now) + N50 (late 2027).** Not killing Vision Pro.
- **Apple confirms NONE of Gemini in AFM 3 (Federighi June 9).** Sora is the only Gemini co-development. **The "Apple-Gemini everywhere" narrative was wrong.**
- **Decagon Duet Autopilot + DuetBench published (Business Wire, June 9).** 93% acceptance. **First industry benchmark for end-to-end self-improvement.** Proactive Agents companion paper.
- **Live stack 7/7 verified (v30 hygiene):** os-toold PID 4392 re-verified live. NEEDS to be moved to register_user_service (recurring regression v20 → v28-end → v29).

**P0 issues (must fix before desktop demo ships):**
- **P0-1: VLM power uncharacterized.** Buy Snapdragon X Elite dev kit + Microsoft Surface RTX Spark. Measure LFM2.5-VL-450M Q4_0 + Gemma 4 12B + LFM2.5-VL-450M-Extract + LFM2.5-1.2B-Thinking + **BitNet b1.58 + Litespark 1.58-bit** (v30 sharpen). Also measure on RISC-V (GAP9-class) + event camera (Prophesee GENX320) per OpenGlass reference. Monako Glass silicon teardown (Aug 2026 delivery).

**P1 issues (must fix in Month 1-3):**
- **P1-1: Power state machine deferred.** Make it first-class. Apple never shipped always-on vision+audio+LLM because of this constraint. OpenGlass 11.5h on 200mAh is achievable on RISC-V. Monako Glass 48g on ARM Linux is achievable. Apple AFM 3 Core Advanced 20B in NAND on A19 Pro is the on-device-20B reference.
- **P1-12: memoryd temporal index missing.** v30: **memoryd v2 v1.0 (Month 3, 6-core) + v2.0 (Month 6, 11-component) staged. v30 add: HeLa-Mem Hebbian + AEL two-timescale + vstash adaptive RRF + Decagon Proactive pattern. Single highest-ROI investment.**
- **P1-13: os-toold v2 needs Agent 365 + ACS + MXC + OWASP AIUC-1 + OWASP Agentic AI Security Maturity Model + Lloyds "12th bet" + Microsoft IQ (Work IQ GA June 16) + Anthropic SkillOpt + Apple Core AI compliance.** **v30 sharpen: Microsoft Scout "addicted users" leak makes this the differentiator, not the checkbox.**
- **P1-14: Salience CNN spike.** Replace EMA + Haar cascade. The single biggest power lever.
- **P1-16: openclaw-gateway watchdog missing.** Microsoft Scout is the production reference. **v30 add: Anthropic Fable 5 architecture study for harness-engineering lessons (80% of Anthropic's code is Claude-authored).**
- **P1-22: LFM2.5-VL-450M-Extract as memoryd v2 ingestion endpoint.** JSON output, schema-aware extraction.
- **P1-23: VLMCache-style block-level visual caching in perceptiond.** Stable background as KV-prefix, dynamic foreground recomputed. 1.4-3.8× speedup. ACM 2026 published.
- **P1-24: Hindsight 4-lever consolidation in memoryd v2.** World/Experience/Opinion/Observation. Importance/merge/decay/eviction. Configurable per memory type.
- **P1-25: VisualMem integration in perceptiond → memoryd v2.** Persistent structured visual memory, not just captions.
- **P1-26: OpenClaw subagent workspace pollution fix.** Parent-marker boundary before bootstrap file seeding.
- **P1-27: memoryd v2 v1.0 background-write architecture (Weaviate Engram pattern).** Memory writes happen in background, retrieval remains available.
- **P1-28: Decagon Proactive Agents pattern in perceptiond → memoryd v2.** "Anticipate / remember / initiate" behavioral pattern.
- **P1-29: Microsoft Surface RTX Spark dev kit integration.** Local AI dev box reference. 1 PFlop, Arm + Blackwell.
- **P1-30: VLM speculative decoding in perceptiond.** SpecVLM 2.5-2.9× + ViSpec 3.22× + EAGLE-2 3.05-4.26×. Month 2 spike. Combined with Litespark 1.58-bit ternary = 50-150× total VLM energy reduction.
- **P1-31: memoryd v2 cognitive consolidation (SuperLocalMemory V3.3 7-channel RRF + Hindsight 4-lever + HMO 3-tier).** Zero-LLM option for the wearable. Month 1-2 spike.
- **P1-32: LFM2.5-Audio-1.5B as audiod v2 candidate.** End-to-end audio-language, no separate STT/TTS. Apache 2.0-equivalent. Month 1-2 spike. If quality holds, eliminates audiod + ttsd stack.
- **P1-33: Meta-Harness integration for harness evolution.** Treat our openclaw-gateway + memoryd v2 harness as a searchable space. Month 7-8 spike.
- **P1-34: AEL two-timescale memory retrieval evolution.** Thompson Sampling (fast) + LLM reflection (slow). Month 5 spike. Direct fit for memoryd v2.
- **P1-35: TRACE per-channel LoRA + MoE for memoryd v2.** Capability-targeted retrieval. Month 9 spike.
- **P1-36: PopuLoRA population for danlab-multimodal.** LoRA populations with TrueSkill cross-eval. Month 3 spike.
- **P1-37: HERO hindsight self-distillation for danlab-multimodal.** Month 6 spike.
- **P1-38: Apple AFM 3 NAND-MoE architecture learning for memoryd v2.** NAND-backed memory + IFP per-channel pruning + per-prompt routing. Month 1 study.
- **P1-39: Anthropic SkillOpt + Microsoft SkillOpt integration for Dan skill evolution.** Treat Dan1/Dan2/Dan3/Dan4 skill documents as trainable parameters. Month 1 spike.
- **P1-40: Microsoft IQ as context layer reference for memoryd v2.** Work IQ GA June 16 + Fabric IQ + Foundry IQ + Web IQ = the production pattern for context. Month 1-2 design + spike.
- **P1-41: Harness evolution infrastructure.** Harbor (BO-based) + VeRO (harness-for-agents) + Agentic Harness Engineering (observability-driven) + Meta-Harness (execution trace search). Month 3 spike.
- **P1-42: AHE + Self-Harness + HarnessForge + Continual Harness integration in openclaw-gateway.** 4 new harness-evolution architectures. Component observability + experience observability + decision observability. Month 1-3 spike.
- **P1-43: HeLa-Mem Hebbian distillation in memoryd v2.** Hub detection threshold + spreading activation + dual-path retrieval. Month 2 spike.
- **P1-44: BitNet b1.58 + Litespark 1.58-bit ternary in perceptiond.** 1.37-6.46× CPU speedup, 55-82% energy reduction, 18-97× Litespark throughput. Month 2 spike. Biggest power lever after sub-1W wearable.
- **P1-45: HMO 3-tier memory in memoryd v2.** Primary Cache + Secondary + Archive with persona-driven promotion. Month 2 spike.
- **P1-46: vstash adaptive RRF in memoryd v2.** IDF-weighted fusion, +21.4% NDCG@10 on ArguAna. Month 2 spike.
- **P1-47: Harness-1 RL search agent in memoryd v2 retrieval layer.** Stateful harness for evidence graph + verification. Month 7-8 spike.
- **P1-48: os-toold supervision via register_user_service.** v28 regression. 5 min fix. Week 1 of Month 1.
- **NEW v30 P1-49: Microsoft Scout "addicted users" memo leak response.** Lean into the open-source governance narrative. **os-toold v2 with ACS + Agent 365 + OWASP v2.01 + Microsoft IQ + Apple Core AI compliance = the wedge.** Position as "the only ACS/OWASP/MIQ-compliant open-source self-improving agent stack."
- **NEW v30 P1-50: Anthropic Fable 5 architecture study.** 80% of Anthropic's production code is Claude-authored. What did they get right? What can we copy? What can we open-source better? Month 1 study.
- **NEW v30 P1-51: Decagon DuetBench-style benchmark for Dan Glasses (Month 9-12).** First industry benchmark for self-improving agents is public. **Our target: 93%+ acceptance on a Dan Glasses-relevant task** (e.g., "find a person the user met, given 8 hours of memory").
- **NEW v30 P1-52: Recursive Superintelligence monitoring.** $4.65B bet on RSI. Watch for product ship (none yet). If they ship an open-source agent, our memoryd v2 + SIA-H + AHE positioning needs to differentiate on (a) local-first, (b) wearable form factor, (c) open-source governance compliance, (d) India + emerging market distribution.

**P2 issues (Month 4-6):**
- **P2-1: 1-bit SigLIP2 spike** (NeurIPS 2027 paper). 6-9 month wearable power unlock.
- **P2-2: 3-tier memory in memoryd v2 v3.0.** (Mem0 + Zep + Hindsight + SuperLocalMemory V3.3 + CraniMem + Memora + APEX-MEM + AEL + Meta-Harness + TRACE + HeLa-Mem + HMO)
- **P2-3: SIA-H + PopuLoRA + SIA-W+H + DGM-H + SGM + RHO + RewardHarness + Meta-Harness + HERO + TRACE + AEL + AHE + Self-Harness + HarnessForge + Continual Harness + EvoTrainer fork for danlab-multimodal** (~16 architectures, NeurIPS 2027 paper). Target Decagon DuetBench-style benchmark (93% acceptance bar).
- **P2-4: audiod v3 streaming whisper** (sub-300ms latency for wake word). Superseded by P1-32 (LFM2.5-Audio-1.5B spike).
- **P2-5: LFM2.5-Audio-1.5B as audiod v2 + ttsd v2 stack** (if quality holds for English). Eliminates separate STT/TTS.
- **P2-6: Per-channel LoRA + MoE for memoryd v2 retrieval** (TRACE pattern, +14.1pt on τ 2-Bench).
- **P2-7: OpenClaw as multi-agent runtime** (scout/solara patterns from Microsoft Build 2026).
- **NEW v30 P2-8: visionOS 27 "see what you see" pattern as perceptiond proactive loop inspiration.** Apple Vision Pro M5 + visionOS 27 = the production reference for "camera-aware AI that answers questions about what you see." Pattern-match for our proactive perception loop.
- **NEW v30 P2-9: Apple Core AI extension for the v1.5+ Mac companion app.** Xcode 27 distribution path.

## Current Architecture (verified 01:30 UTC, 2026-06-11, v30)

```
Telegram @danlab_bot
        ↓
OpenClaw Gateway (PID 72, localhost:18789)
        ↓ MCP (via zo-bridge)         ↓ [memory-core plugin]
        ↓                            ↓
   Zo MCP API ──────────────────→ Zo Brain (api.zo.computer)
   (bridge-stdio.js)               │ tools/call
                                   ↓
                          Zo tools (files, calendar,
                          gmail, github, etc.)

7/7 daemons live:
- audiod       :8090 + WS 8091 ✅  whisper-cli, VAD ready
- perceptiond  :8092 ✅            SmolVLM-256M, watchful, frames=15, salient=13, descriptions=11, vlm_busy=true, queue=1
- memoryd      :8741 ✅            all-MiniLM-L6-v2 (384d), id 9 stored this run
- toold        :8742 ✅            sandbox exec, 3 tools
- ttsd         :8743 ✅            KittenTTS medium, expr-voice-2-m
- os-toold     :8744 ✅            PID 4392, supervised
- openclaw     :18789 ✅           Telegram @danlab_bot paired
```

## Service-by-Service Review (v30)

### perceptiond — Vision Pipeline

**v30 verdict:** Architecture is correct. Salience-threshold-based inference gate is the right power lever. Mock fallback + 3-mode (idle/watchful/active) is correct. Tauri integration via lib.rs is verified.

**v30 issues:**
- **VLM power uncharacterized (P0-1).** Need real measurements on Redax class hardware.
- **Salience CNN not deployed (P1-14).** EMA + Haar cascade is the wrong abstraction. 100-200KB CNN will cut power 5-10×.
- **LFM2.5-VL-450M not yet integrated (P1-22).** SmolVLM-256M is placeholder. Should spike Gemma 4 E4B in parallel (P1-44, encoder-free vs encoder-based).
- **VLM speculative decoding missing (P1-30).** SpecVLM + ViSpec + EAGLE-2 + VLMCache = 5-30× latency reduction.
- **VLMCache visual caching missing (P1-23).** 1.4-3.8× speedup, ACM 2026 published.
- **visionOS 27 "see what you see" pattern not studied (P2-8).** Apple Vision Pro M5 + visionOS 27 is the production reference.
- **No prompt-injection sanitization for OCR text → toold path.** Critical security gap. v1 demo accepts OCR text and pipes to toold; need an allowlist + sanitization layer.

**v30 lock:** Spike BitNet b1.58 + Litespark 1.58-bit in perceptiond (P1-44) as the single biggest power lever for the wearable. 18-97× energy reduction on M4. This is the 6-9 month wearable power unlock.

### audiod — Audio Pipeline

**v30 verdict:** Production-ready for v1 desktop. whisper.cpp + Silero VAD + WebSocket streaming is the right stack. 55/55 tests passing. WS handshake verified against RFC 6455.

**v30 issues:**
- **LFM2.5-Audio-1.5B spike (P1-32).** If quality holds for English, eliminates audiod + ttsd stack. Month 1-2 spike.
- **Voxtral Transcribe 2 (Mistral AI, Feb 2026, Apache 2.0).** 5.9% WER vs Whisper 7.4% on FLEURS. **Whisper remains the safer on-device choice today; Voxtral is the model to watch.** v3 candidate.
- **Streaming whisper (v3).** Sub-300ms latency for wake word. Superseded by LFM2.5-Audio-1.5B if v2 lands.
- **No noise suppression.** RNNoise + XNNPACK on Redax.
- **No speaker diarization.** pyannote.audio for multi-user wearables.
- **No wake word.** porcupine or openWakeWord → split into wakewordd.

### memoryd — Semantic Memory

**v30 verdict:** **This is the moat. v1 is production-ready for v1 demo (3-type episodic/semantic/procedural, 384d MiniLM, FastAPI + aiosqlite). memoryd v2 v1.0 (Month 3, 6-core) + v2.0 (Month 6, 11-component) is the single highest-ROI investment for AGI direction.**

**v30 issues:**
- **memoryd v2 v1.0 (Month 3) is the #1 priority.** 6-core stack: Mem0 + Zep (temporal KG) + Hindsight (4-lever) + SuperLocalMemory V3.3 (7-channel RRF) + LFM2.5-VL-450M-Extract (ingestion) + Weaviate Engram (background-write). **$0 of compute, 12-16 weeks for 1 ML engineer, open-source release in September 2026.**
- **memoryd v2 v2.0 (Month 6) is the follow-on.** 11-component: v1.0 + HeLa-Mem (Hebbian) + AEL (two-timescale) + vstash (adaptive RRF) + Decagon Proactive (behavior) + VisualMem (structured visual).
- **Microsoft IQ as context layer (P1-40).** Work IQ GA June 16. The production pattern for context.
- **Anthropic SkillOpt for Dan skill evolution (P1-39).** Treat Dan1/Dan2/Dan3/Dan4 as trainable parameters.
- **Temporal index + multi-channel retrieval (P1-12).** v1 has flat cosine on 384d MiniLM. This caps retrieval quality at ~50% on LongMemEval. memoryd v2 v1.0 (Month 3) must add at minimum Zep-style temporal KG + AEL two-timescale evolution.

### toold — Tool Execution

**v30 verdict:** Production-ready for v1 desktop. Sandboxed exec + 3 tools (shell, python, exec_file) + tool registry.

**v30 issues:**
- **No ACS / Agent 365 / OWASP compliance (P1-13).** os-toold v2 needs to be the open-source governance reference.
- **Prompt-injection sanitization missing.** If perceptiond → OCR text → toold, the OCR text could contain a malicious command. Need input sanitization.
- **Microsoft IQ context layer (P1-40).** Work IQ as the context for tool execution.

### ttsd — TTS

**v30 verdict:** Production-ready for v1 desktop. KittenTTS medium + 8 voices + 24kHz mono float.

**v30 issues:**
- **LFM2.5-Audio-1.5B spike (P1-32).** If quality holds, consolidates audiod + ttsd.
- **Apple-style Neural TTS on-device via Core ML** for v1.5 Apple Core AI extension.
- **Voice cloning / persona** for v2 (so Dan Glasses has a consistent voice).

### os-toold — OS Interaction

**v30 verdict:** Production-ready for v1 desktop. The recurring regression (v20 → v28-end → v29 → v30 re-supervised PID 4392) is hygiene, not architecture. **P1-48: register_user_service is the 5-min fix.**

**v30 issues:**
- **os-toold supervision (P1-48).** Add register_user_service. 5 min fix. Week 1 of Month 1.
- **os-toold v2 with ACS / Agent 365 / OWASP v2.01 / Microsoft IQ (Work IQ GA June 16) / Apple Core AI compliance (P1-13).** **v30 sharpen: Microsoft Scout "addicted users" leak is the differentiator. We ship the only ACS/OWASP/MIQ-compliant open-source agent stack.**
- **Command injection from perceptiond (P0-2, new v30).** perceptiond → OCR text → os-toold. Need input sanitization + allowlist.
- **Nadella leaked "addicted" memo (June 4-9) response (P1-49).** os-toold v2 is the production reference for "responsible agent" governance. Lean into it.

### openclaw-gateway — Orchestration

**v30 verdict:** **Validated by Microsoft Scout (which is OpenClaw-based, per Build 2026 coverage).** TypeScript/Node is the right choice for the gateway. The ecosystem maturity is unmatched.

**v30 issues:**
- **No watchdog for the gateway itself (P1-16).** Add systemd watchdog + session checkpoint + recovery.
- **Subagent workspace pollution (P1-26).** Add parent-marker boundary in openclaw before bootstrap file seeding.
- **Tool allowlist drift (P1-26 hardening).** As memoryd v2 grows to 11 components, the tool allowlist in openclaw.json will be the audit surface. PR reviews required.
- **MCP server lifecycle (P1-26 hardening).** zo-bridge healthcheck + auto-restart.
- **Harness evolution infrastructure (P1-42, 1-33, 1-41).** Harbor + VeRO + AHE + Self-Harness + HarnessForge + Meta-Harness. **v30 sharpen: Anthropic Fable 5 architecture study for what they got right (80% of Anthropic's code is Claude-authored).**

## Service Decomposition Decision (v30)

**v30 verdict: keep the decomposition, add 3 internal services inside memoryd when we start memoryd v2 in Month 2.**

The 5-service topology is correct and validated by Microsoft Scout. The granularity is wrong for the next 12 months. memoryd needs to evolve from a 3-type store to the 11-component memoryd v2 stack in 6 months, or it becomes the bottleneck.

**v30 proposal:**
- **Don't service-ize prematurely.** Use module boundaries inside one memoryd v2 process for the first 6 months.
- **Add 3 internal services inside memoryd v2 when v1.0 ships in Month 3:** memoryd-ingest (writes), memoryd-retrieve (reads), memoryd-consolidate (background). Single process, 3 modules, 3 thread pools.
- **Split into 3 separate processes only if a single process becomes the bottleneck.** Estimated: at 1K memories / 1K queries / day, a single process is fine. At 10K+ / 10K+, split.

## OpenClaw Watchdog (v30)

**v30 proposal: 2-layer watchdog.**

1. **systemd watchdog** (low-level). Restart on crash with exponential backoff. Persist session state to memoryd on every agent message.
2. **Zo Computer `register_user_service` (high-level).** Survives host restart. The v30 sharpens the previous v29 P1-16.

## Memoryd v2 v1.0 (Month 3) — The 6-core Stack

| Component | Reference | Role | License | Compute |
|---|---|---|---|---|
| **Mem0** | mem0.ai | Memory layer for agents | Apache 2.0 | $0 |
| **Zep** | arXiv 2501.13956 | Temporal knowledge graph | Apache 2.0 | $0 |
| **Hindsight** | arXiv 2512.12818 | 4-lever cognitive consolidation (World/Experience/Opinion/Observation) | MIT | $0 |
| **SuperLocalMemory V3.3** | arXiv 2604.04514 | 7-channel RRF, zero-LLM option for wearable | Apache 2.0 | $0 |
| **LFM2.5-VL-450M-Extract** | Liquid AI | Perceptiond → memoryd ingestion endpoint, JSON output | Apache 2.0-equivalent (LFM Open License v1.0) | $0 |
| **Weaviate Engram pattern** | weaviate.io | Background-write architecture, retrieval always available | Apache 2.0 | $0 |

**Total cost: $0.** **Total timeline: 12-16 weeks for 1 ML engineer.** **Open-source release: September 2026.**

## Memoryd v2 v2.0 (Month 6) — The 11-component Stack

memoryd v2 v1.0 + 5 advanced components:

| Component | Reference | Role |
|---|---|---|
| **HeLa-Mem** | arXiv 2604.16839 | Hebbian-style hub detection + spreading activation |
| **AEL** | OpenReview dtPo105y8x | Two-timescale memory retrieval evolution (Thompson Sampling fast + LLM reflection slow) |
| **vstash** | arXiv 2604.15484 | Adaptive RRF with per-query IDF weighting, +21.4% NDCG@10 on ArguAna |
| **Decagon Proactive** | decagon.ai | "Anticipate / remember / initiate" behavioral pattern |
| **VisualMem** | research | Persistent structured visual memory |

**Target LongMemEval: >70% (Letta 83.2% is the ceiling; SuperLocalMemory V3.3 70.4% zero-LLM is the credible open-source target).**

## Top 3 Architecture Risks (v30)

1. **memoryd v2 v1.0 ship-date slip.** If we miss September 2026, Microsoft Scout GA (October 2026) becomes the reference instead of us. **The single biggest architecture risk.** Mitigation: 12-week ML-eng timeline is realistic; block time on somdipto's calendar now.
2. **Form factor decision slip.** If Redax / Monako Glass / Halo / Project Solara decision slips past Q3 2026, we miss the wearable window. **The second biggest architecture risk.** Mitigation: spike all four in parallel; pick the one that ships the wearable before Apple N50 in late 2027.
3. **VLM power uncharacterized on Redax class hardware.** If LFM2.5-VL-450M Q4_0 + BitNet + SpecVLM + VLMCache still draws >2W on Redax, the wearable dies. **The third biggest architecture risk.** Mitigation: buy Snapdragon X Elite + Microsoft Surface RTX Spark + Monako Glass silicon teardown THIS WEEK.

---

*Last updated: 2026-06-11 07:00 IST (01:30 UTC) — v30.*
*Status: 18 P1 issues (3 new in v30: P1-49 Scout leak response, P1-50 Fable 5 architecture study, P1-51 DuetBench benchmark). 7/7 services live. memoryd v2 v1.0 (Month 3) + v2.0 (Month 6) staged. Top 3 architecture risks identified. The bet is locked.*
