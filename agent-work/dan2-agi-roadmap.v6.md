# Danlab AGI Roadmap — 6 / 12 / 24 Months
**Author:** Dan2 (co-founder, lead scientist, architect)
**Date:** 2026-06-17
**Inputs:** `dan2-research-report.md` (v6, 2026-06-17), `dan2-architecture-review.md` (v6), `dan2-model-analysis.md` (v6), canonical Dan Glasses spec, danlab-multimodal README, paperclip AGENTS.md, blurr README.
**North Star:** Build always-on, on-device, privacy-preserving multimodal intelligence that genuinely learns from experience. Ship it as a wearable (Dan Glasses), an open platform (dani), and a multi-agent org (paperclip / DanClaw).

**v6 deltas from v5:**
- **HRM-Text 1B added** to the on-device LLM lineup (released 2026-05-18, the day after v5 was finalized). Two-model pipeline: LFM2.5-VL-450M (vision) + HRM-Text 1B (reasoning).
- **Anthropic's "brake pedal" call (2026-06-04)** absorbed as a positioning signal — on-device + open + auditable is the right side of the debate.
- **Proactive AI promoted from roadmap item to v1.5 architecture addition.** PRISM + Microsoft Research trigger encoder is the right pattern.
- **Tethered-glasses path (CoVSpec + phone) added** as a v1.5 architecture option, in case Redax slips.
- **Memory architecture** updated to reflect the Maturation 2026 landscape (MemX, MemMachine, Memanto, AriadneMem, TeleMem, CraniMem).
- **Self-improvement landscape** updated with RHO, HarnessX, Self-Harness, HarnessForge, AHE — SIA is no longer alone.

---

## Strategic Frame

Three things must be true for Danlab to make a real AGI contribution from India by 2028:

1. **Hardware in hand.** No roadmap survives without a target. The Redax board is the bottleneck. If it doesn't ship in Q3 2026, **spec the tethered path** (existing glasses + phone running CoVSpec) as the v1.5 default, with the standalone path as v2.
2. **A defensible niche.** Frontier labs own 70%+ of the general capability surface. We win on **on-device multimodal + privacy + always-on context + Indian-language coverage + auditable self-improvement**. That is the niche. Everything outside it is distraction.
3. **A self-improving loop that is *actually* self-improving.** Not a hand-coded heuristic. The 2026 landscape (SIA, RHO, HarnessX, Self-Harness, HarnessForge, AHE) gives us multiple credible paths. Pick one and ship the ablation.

---

## 6-Month Plan (Jun 2026 → Dec 2026) — "Ship the wearable, prove the platform"

**Theme:** Get Dan Glasses v1 into real hands. Get paperclip (now DanClaw) re-animated. Get a real self-improvement experiment running in danlab-multimodal. Promote the proactive layer to v1.5 architecture.

### Hardware / wearable (Track B unblock)
- **Resolve the Redax situation.** If hardware ships in Q3, port Dan Glasses to it (aarch64 rebuild, not rewrite — Tauri code is portable). If it slips, **ship the tethered path**: Brilliant Labs Frame + USB-C compute puck (Raspberry Pi 5 8GB or Snapdragon Dev Kit) + CoVSpec with LFM2.5-VL-450M on the phone. This gets us in the field without waiting.
- **Define a real power budget.** Measure every component on the actual target. Stop using "5–10 W" as a planning number. Concrete targets:
  - sleep (camera off, mic ready, wake on voice trigger): **<0.3 W**
  - idle (camera on, no VLM): **<0.8 W**
  - watchful (salience-gated VLM, 1 inference / 3 s avg, VLCache + VisionTrim): **<1.5 W**
  - active (continuous VLM, LLM on demand): **<3.0 W peak**
  - **HRM-Text 1B on-device reasoning burst:** <0.2 W (per-call, latent reasoning, no CoT burn)
- **Battery target:** 4 h mixed-use at the watchful budget. If unachievable, target 2 h and document the tradeoff.
- **Weight target:** **<50 g** including temples, camera, battery. The Brilliant Labs Frame at 39 g and Ray-Ban Meta at 49 g set the bar.
- **Wake-word service (`wakewordd`).** openWakeWord first, Porcupine if accuracy is bad. Promote from v3 to v1.1.

### Software / platform
- **Memory architecture v1.5** (memoryd): add **temporal + confidence** metadata to every embedding; Ebbinghaus-style confidence decay; 4-signal score (semantic × temporal × confidence × relational). Plus BM25 + RRF, plus `memory_links` table (7 relation types from MemX). 2-week change to memoryd. The single biggest credibility upgrade.
- **HRM-Text 1B integration.** Spec the LFM2.5-VL-450M (vision) → text description → memoryd retrieval → HRM-Text 1B (reasoning) → response → KittenTTS (speech) pipeline. Two-model architecture, documented in AGENTS.md.
- **RHO (Retrospective Harness Optimization) pilot** in danlab-multimodal. RHO improves harnesses from past trajectories with **no labels** — single pass, no human data. If it improves on the heuristic, we have a publishable result *and* a real self-improvement primitive.[^rho]
- **VLCache + VisionTrim wiring** in perceptiond. Drop-in, 1 week. Targets 3–5× VLM speedup on x86_64, more on aarch64+NPU.
- **Streaming KittenTTS** for sub-second first-audio latency.
- **Proactive trigger layer** in OpenClaw: Microsoft Research graph encoder (220 MiB BF16, on-device) + PRISM gate. **This is the v1.5 differentiator.** No other wearable has this.
- **Prompt injection hardening** on the perception → os-toold path. The canonical analysis flagged this. Synthius-Mem's adversarial robustness work (99.6%) shows the bar. Cheap mitigation: argument-hashing + denylist extension + a perception-frame trust score.
- **paperclip → DanClaw reactivation.** It's dormant (per its AGENTS.md). Re-orient it as the **multi-agent company orchestrator** that drives Dan Glasses: the gateway through which Dan (the AI co-founder) operates the company (issue tracking, goal mgmt, deployment infra). Keep the cool name. Keep the rail guard (policies, per-agent tool filtering).

### Research / open-source contributions
- **Publish the SmolVLM-256M ↔ LFM2.5-VL-450M comparison on Indian-language OCR.** Nobody has done this credibly. danlab-multimodal is the natural home.
- **Open-source `dan-lab/wakewordd` and `dan-lab/memoryd`** separately from the dan-glasses repo. These are reusable primitives. The "world's best skills library" framing from dani-skills applies here.
- **Safety paper draft:** "An Open-Source, On-Device Defense Against Cross-Modal Prompt Injection for AI Wearables." Target: USENIX Security 2027. The perception-frame trust score + argument-hashing + two-channel execution combo is the contribution.

### Success criteria (Dec 2026)
- [ ] Dan Glasses v1 demoable end-to-end (audio + vision + memory + tool use) on target hardware (Redax **or** tethered path).
- [ ] Battery life measured and published in spec.
- [ ] memoryd v1.5 deployed with temporal + confidence + relational scoring + BM25 + memory_links.
- [ ] HRM-Text 1B integrated and benchmarked against LFM2-1.2B-Thinking baseline.
- [ ] VLCache + VisionTrim wired in perceptiond.
- [ ] Proactive trigger layer live in OpenClaw.
- [ ] danlab-multimodal v2 with RHO (label-free retrospective harness optimization).
- [ ] paperclip-DanClaw gateway revived with at least 2 live agents.

---

## 12-Month Plan (Jun 2026 → Jun 2027) — "Make it learn, make it safe, make it proactive"

**Theme:** Move from "always-on wearable" to "always-on wearable that learns and initiates." Add the dual-process memory, the test-time self-improvement, the real proactive AI, and the cross-modal safety story.

### Self-improvement — past heuristic, into real RL
- **RHO in production (danlab-multimodal v2.5).** No labels, single pass, no human data. Already a primitive by Dec 2026; promote to the primary harness-optimizer by Q2 2027.
- **TT-SI in production (danlab-multimodal v3).** Three steps: self-awareness (which descriptions are weak?), self-data augmentation (generate similar queries), test-time training (small LoRA on the weak areas). Target: 5–10% absolute gain on a held-out eval of "describe this screen" quality.
- **Fork SIA** (Hexo Labs, MIT, May 2026) and integrate as a harness. The SIA framework is the *credible* open path to harness+weights self-improvement. The Feedback-Agent becomes a smaller HRM-Text 1B or LFM2-1.2B-Thinking. Until this ships in danlab-multimodal, the project keeps the "pre-RL scaffold" label — and that is correct.
- **HarnessForge / AHE (Agentic Harness Engineering) pilot.** These are alternatives to SIA that focus on harness-only or joint harness+policy evolution. Evaluate against SIA on the same eval suite. Pick the best.
- **Published ablation:** heuristic vs. RHO vs. learned reward model vs. TT-SI vs. SIA-fork. Five configurations, same eval, same data. This is the contribution to the field.

### Memory — dual-process, schema-inducing, multi-layer
- **Memory v2 (DPA / DPCM / MemMachine / Memanto hybrid):** two processes:
  - **Daytime writer** (synchronous, fast): records belief revisions as doubly-linked "supersedes" chains.
  - **Nighttime engine** (async, batched): induces schemas, intentions, cross-domain abstractions; detects collisions.
- **TiMem-style Temporal Memory Tree** on top: hierarchy of (raw events → episodic → semantic → procedural → schema).
- **Memori-style triples** + **MemMachine three-layer** for production shape.
- **Adversarial-robust memory** (Synthius-Mem lessons): CategoryRAG with hallucination resistance > 99%.
- **LoCoMo benchmark eval.** 75–95% range is where 2026 SOTA lives (Memanto, APEX-MEM). We should be in that range by Q4 2026.

### Proactive AI — the v1.5 differentiator, v1.7 production
- **Proactive trigger layer (Dec 2026).** Microsoft Research graph encoder + PRISM gate, in OpenClaw.
- **PRISM slow-reasoning pass (Q1 2027).** HRM-Text 1B fires when p_trigger is near the decision boundary. <5% of all events.
- **ProAgentBench + ContextAgentBench evaluation.** Public benchmarks, 28,000+ events from real user activity. Validate against prior work.
- **Sensible Agent patterns (UMD 2026) — modality choice** when the trigger fires: visual vs. audio vs. silent icon. **Don't always speak.**
- **Daily briefing agent.** Calendar + email + recent memories → 60-second spoken summary. The "killer app" for an always-on wearable.
- **Pro2Bench / EgoProactive evaluation.** Egocentric proactive dataset for "off-plan" recovery — the user changed their mind. How does the system handle it?

### Privacy + safety — make it a moat
- **DPDP Act + EU AI Act compliance audit.** India DPDP and EU AI Act are both tightening in 2026. **On-device-only is a compliance advantage.** Document it.
- **Federated fine-tuning** for user-specific memory: each user's memories fine-tune their own model adapter (LoRA), never the central model. This is the privacy story.
- **Perception-frame trust score** in perceptiond: scored by visual coherence, content type, prompt-injection risk. Below threshold → no tool execution.
- **Anthropic "brake pedal" alignment.** Jack Clark's June 4 call[^anthropic_brake] is asking for exactly what we're building. Public positioning as the "open, auditable, on-device alternative" is a brand asset, not just a technical position.
- **Safety paper submission (USENIX Security 2027).** Cross-modal prompt injection defense for AI wearables.

### Success criteria (Jun 2027)
- [ ] danlab-multimodal v3 with TT-SI in production, published eval.
- [ ] RHO + SIA-fork both shipped, with ablation.
- [ ] Memory v2 (dual-process + three-layer + triples) deployed; LoCoMo in SOTA range.
- [ ] Proactive trigger layer live in OpenClaw; PRISM slow-pass on HRM-Text 1B.
- [ ] Daily briefing agent demoable.
- [ ] Dan Glasses v1.5 shipped to ≥10 pilot users (likely ourselves + 9 testers in Bengaluru).
- [ ] Safety paper accepted at USENIX Security or equivalent.
- [ ] DanClaw multi-agent orchestrator running the company.

---

## 24-Month Plan (Jun 2026 → Jun 2028) — "Make it co-evolve with the user"

**Theme:** From "personal assistant" to "personal intelligence that co-evolves." This is where Danlab's contribution to AGI gets sharp.

### AGI-shaped research bets
- **Recurrent latent reasoning (RLRP, ICLR 2026) in the on-device LLM.** Internal latent refinement, not external CoT. Compatible with our current llama.cpp stack. This is the path to "reasoning at the edge" without burning tokens. **HRM-Text 1B is the prototype; RLRP papers extend it.**
- **Operator-consistent RL (Op-RL)** for the personal agent: train the user-facing agent to *be* the improvement operator — generate draft, distill, refine — rather than just a single-pass generator. PDR-style.
- **Tiny Recursive Models (TRM)** as the policy backbone for some sub-tasks. The 2026 work on unrolled policy iteration for TRMs is the most promising small-model RL setup I've seen.
- **Skill banks (SkillRL, ICLR 2026 workshop):** a hierarchical library of reusable skills discovered through experience. This is how you get "knows your workflow" without a 100B-param model.
- **Self-evolving agent loop (DPA / DPCM):** the System 1 / System 2 dual-process design from the 2026 memory literature, applied to the *whole agent*, not just memory.
- **HRM-Text post-training.** Sapient released HRM-Text 1B as a base, pre-trained model. **The 24-month play is to fine-tune HRM-Text for "reason over my memories" — a personalized reasoning model that lives on the wearable, trained on the user's own retrievals.**
- **HarnessForge-style joint harness+policy evolution** as the production self-improvement loop. Don't just evolve the harness; evolve the harness-policy pair.

### Platform bets
- **dani as the world's best agent skills library** is a real positioning play. Every piece of Dan Glasses code should be releasable as a skill. The "world's best skills library" tagline from the dani repo is achievable if we treat every architecture decision as a primitive someone else will use.
- **Open-weights release** of:
  - HRM-Text 1B fine-tuned for "reason over my memories" (if results hold)
  - LFM2.5-VL fine-tuned for Indian-language OCR (if results hold)
  - A "Dan Glasses prompt-injection defense" model
  - A DanClaw agent harness
- **Indie hardware path.** If Redax is a dead end, we have to design our own. 6-month clock on that decision (must be made by Dec 2026).
- **Compliance + certification.** DPDP Act compliance is a moat. EU AI Act high-risk system certification (if we ever cross into biometric/identification territory) is a moat. Plan for it now.

### Hiring + organization
- **Research scientist** focused on self-improvement / RL — single highest-leverage hire. SIA / RHO / HarnessForge is the right resume.
- **Embedded systems engineer** for the actual wearable path.
- **Hindi/Tamil/Bengali linguist** for the Indian-language bet.
- **OSS maintainer** for dani-skills (this is the distribution channel).
- **Safety engineer** for the cross-modal prompt injection / perception-frame trust work.

### Success criteria (Jun 2028)
- [ ] Dan Glasses v2 with self-improving memory and proactive trigger layer shipping as a product.
- [ ] At least 2 open-source releases with measurable adoption (target: dan-lab repos ≥ 5k stars each).
- [ ] A published paper from danlab at a major venue (NeurIPS / ICML / ICLR / USENIX Security). Likely target: edge self-improvement, memory architecture, or cross-modal safety.
- [ ] dani-skills: 50+ production-grade skills in the catalog.
- [ ] A demonstrable co-evolution loop: the assistant's behavior demonstrably changes based on accumulated user-specific memory, in a way that's auditable.
- [ ] An HRM-Text 1B derivative fine-tuned for "reason over my memories" — open-weights release.

---

## What to stop doing

- ❌ **Calling the danlab-multimodal feedback loop "RL."** It is a heuristic. Until harness+weights are open, the label stays pre-RL. This is the integrity call.
- ❌ **Building paperclip-style company infrastructure that doesn't drive a product.** Paperclip's value is as the orchestrator for Dan Glasses / dani. If it's not in that loop, it's dead weight.
- ❌ **Hand-rolling more Python daemons when OpenClaw can host the logic.** The 5-daemon split is right for the hot path (audio, vision, memory, tools, tts) but new logic should go in OpenClaw agents unless it has clear latency / safety requirements.
- ❌ **Optimizing for x86_64 laptop performance** beyond "good enough to demo." Every Watt we save on aarch64 matters 100× more.
- ❌ **Conflating LFM2.5-VL-450M and HRM-Text 1B.** Two models, one pipeline, two different jobs. Document the split.
- ❌ **Waiting on Redax.** Spec the tethered path now. Ship the v1.5 demo on Brilliant Labs Frame + Raspberry Pi 5 + CoVSpec. If Redax ships, port. If not, we have a product.

---

## Risks (load-bearing)

| Risk | Severity | Mitigation |
|------|----------|------------|
| Redax hardware slips / dies | Critical | Tethered-glasses path (CoVSpec); indie hardware if necessary |
| Frontier model commoditizes our edge advantage | High | Lean harder on privacy, Indian-language coverage, always-on context, auditable self-improvement |
| HRM-Text 1B doesn't pan out | Medium | Fall back to LFM2-1.2B-Thinking; same pipeline |
| Self-improvement doesn't beat the heuristic in 12 months | Medium | Honest publish. Negative results are still science. |
| RHO + SIA-fork require labels we can't get | Medium | RHO is label-free by design; SIA can use the heuristic as a weak reward |
| India DPDP / EU AI Act compliance becomes a moat-instead-of-moat | Medium | Document the on-device design; certify if required |
| Anthropic / OpenAI publishes on-device multimodal first | Medium | Lean harder on auditable + open + Indian-language + self-improvement |
| Key person dependency on somdipto | High | dani as the persistent memory of the org + this AGENTS.md system |
| Proactive AI is annoying in practice | High | PRISM gate. 22.8% fewer false alarms. Festina Lente. |

---

## One-line summary

**Ship the wearable (tethered or standalone), prove the platform, teach it to learn (RHO → TT-SI → SIA), teach it to initiate (proactive trigger + PRISM), and stay ruthlessly honest about what's heuristic and what's RL.**

---

## Footnotes

[^rho]: RHO: Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference. arXiv:2606.05922. https://arxiv.org/html/2606.05922v2
[^anthropic_brake]: Reuters — Anthropic says AI labs need coordinated plan to halt development if risks rise. 2026-06-04. https://www.reuters.com/business/anthropic-says-ai-labs-need-coordinated-plan-halt-development-if-risks-rise-2026-06-04/

---

*👾* Roadmap sharpened for 2026-06-17. v6 deltas: HRM-Text 1B added to the model lineup, proactive layer promoted to v1.5 architecture, tethered path added as a Redax-fallback, self-improvement landscape expanded (RHO, HarnessX, Self-Harness, HarnessForge, AHE), Anthropic brake-pedal signal absorbed as a positioning moat.
rid):** three layers:
  - **Daytime writer** (synchronous, fast): records belief revisions as doubly-linked "supersedes" chains. Uses RRF over vector + BM25 + memory_links graph.
  - **Nighttime engine** (async, batched): induces schemas, intentions, cross-domain abstractions; detects collisions. Runs on HRM-Text 1B.
  - **Retrieval-time gate** (MemGate-style 9M-param MLP): filters out stale, off-topic, or unsafe memories before they hit the LLM context.
- **TiMem-style Temporal Memory Tree** on top: hierarchy of (raw events → episodic → semantic → procedural → schema).
- **Adversarial-robust memory** (Synthius-Mem lessons): CategoryRAG with hallucination resistance > 99%.
- **LoCoMo + LongMemEval benchmark eval.** 75–95% range is where 2026 SOTA lives. We should be in that range by Q4 2026.
- **Memanto vs. MemX decision.** If pure-vector-with-typing hits 90% of MemX's performance on our eval, **drop the graph** in v2. Don't carry complexity without measured benefit.

### Proactive AI — the v1.5 differentiator, the v2 moat
- **Proactive trigger layer** live in OpenClaw (Dec 2026): Microsoft Research 220 MiB BF16 graph-encoder trigger + PRISM Festina Lente gate. **Fires <1% of the time, only when both p_need × p_accept cross threshold.** LLM only on the actual intervention.
- **Salience-aware interrupt policy.** Don't speak unless the user is likely to want it. Sensible Agent (UMD 2026) gaze/hand-occupancy signals.
- **Daily briefing agent.** Calendar + email + recent memories → 60-second spoken summary. The "killer app" for an always-on wearable.
- **ProAgentBench evaluation** of our trigger. Target: >90% anticipation recall, <5% false-alarm rate.
- **ProActor-style RL fine-tuning** of the proactive layer once we have user feedback. ACL 2026 paper is the template.

### Privacy + safety — make it a moat
- **DPDP Act + EU AI Act compliance audit.** India DPDP and EU AI Act are both tightening in 2026. On-device-only is a compliance advantage. Document it.
- **Federated fine-tuning** for user-specific memory: each user's memories fine-tune their own model, never the central model. This is the privacy story.
- **Perception-frame trust score** in perceptiond: scored by visual coherence, content type, prompt-injection risk. Below threshold → no tool execution.
- **Cross-modal prompt-injection paper** (target: USENIX Security 2027). The combination of (1) perception-frame trust score, (2) SlotGuard-style transcript redaction, (3) two-channel tool execution, (4) interaction-barrier shielding, is the contribution.

### Success criteria (Jun 2027)
- [ ] danlab-multimodal v3 with TT-SI in production, published eval.
- [ ] Memory v2 (dual-process) deployed; LoCoMo in SOTA range.
- [ ] Proactive trigger layer live in OpenClaw, evaluated on ProAgentBench.
- [ ] Daily briefing agent demoable.
- [ ] Cross-modal prompt-injection paper submitted.
- [ ] Dan Glasses v1.5 shipped to ≥10 pilot users (likely ourselves + 9 testers in Bengaluru).
- [ ] DanClaw multi-agent orchestrator running the company.

---

## 24-Month Plan (Jun 2026 → Jun 2028) — "Make it co-evolve with the user"

**Theme:** From "personal assistant" to "personal intelligence that co-evolves." This is where Danlab's contribution to AGI gets sharp.

### AGI-shaped research bets
- **HRM-Text 1B + LFM2.5-VL-450M as the on-device intelligence pair.** HRM-Text 1B's continuous-latent reasoning is the right on-device "thinking" pattern for wearables. **LFM2.5-VL-450M sees, HRM-Text 1B reasons.** No frontier LLM dependency.
- **Recurrent latent reasoning (RLRP, ICLR 2026)** in the on-device LLM. Internal latent refinement, not external CoT. Compatible with our current llama.cpp stack. This is the path to "reasoning at the edge" without burning tokens.
- **Operator-consistent RL (Op-RL)** for the personal agent: train the user-facing agent to *be* the improvement operator — generate draft, distill, refine — rather than just a single-pass generator. PDR-style.
- **Tiny Recursive Models (TRM)** as the policy backbone for some sub-tasks. The 2026 work on unrolled policy iteration for TRMs is the most promising small-model RL setup I've seen.
- **Skill banks (SkillRL, ICLR 2026 workshop):** a hierarchical library of reusable skills discovered through experience. This is how you get "knows your workflow" without a 100B-param model.
- **Self-evolving agent loop (DPA / DPCM):** the System 1 / System 2 dual-process design from the 2026 memory literature, applied to the *whole agent*, not just memory.

### Platform bets
- **dani as the world's best agent skills library** is a real positioning play. Every piece of Dan Glasses code should be releasable as a skill. The "world's best skills library" tagline from the dani repo is achievable if we treat every architecture decision as a primitive someone else will use.
- **Open-weights release** of:
  - LFM2.5-VL fine-tuned for Indian-language OCR (if results hold)
  - A "Dan Glasses prompt-injection defense" model
  - A DanClaw agent harness
  - **A wearable-grade HRM-Text 1B LoRA** fine-tuned for personal memory reasoning
- **Indie hardware path.** If Redax is a dead end, we have to design our own. 6-month clock on that decision (must be made by Dec 2026).

### Hiring + organization
- **Research scientist** focused on self-improvement / RL — single highest-leverage hire.
- **Embedded systems engineer** for the actual wearable path.
- **Hindi/Tamil/Bengali linguist** for the Indian-language bet.
- **OSS maintainer** for dani-skills (this is the distribution channel).

### Success criteria (Jun 2028)
- [ ] Dan Glasses v2 with self-improving memory and proactive trigger layer shipping as a product.
- [ ] At least 2 open-source releases with measurable adoption.
- [ ] A published paper from danlab at a major venue (NeurIPS / ICML / ICLR / USENIX Security). Likely target: edge self-improvement, memory architecture, or wearable prompt-injection defense.
- [ ] dani-skills: 50+ production-grade skills in the catalog.
- [ ] A demonstrable co-evolution loop: the assistant's behavior demonstrably changes based on accumulated user-specific memory, in a way that's auditable.

---

## v6 add — the Anthropic "brake pedal" positioning

On 2026-06-04, Anthropic's Jack Clark publicly called for an industry-wide "brake pedal" — a coordinated, verifiable way to slow or pause frontier AI development if self-improvement accelerates past societal ability to manage risks.[^anthropic_brake] Anthropic's own published data: Claude writes >80% of the code merged into Anthropic's production systems, and engineers ship 8× more code than before. The piece frames three scenarios: human-led (today), AI-led scaffolding (next 1–3 years), full RSI ("by 2028 with ~60% probability" per Anthropic, per news reports).

**For Danlab, this is a positioning signal, not a constraint.** Our bet — on-device, open-source, auditable, Indian-language, privacy-first — is exactly the right side of the Anthropic call. We are not building frontier-capability systems that need a brake pedal. We are building small, focused, transparent, user-controlled systems that exemplify the "on-device, auditable, privacy-first" branch of the AGI conversation.

**What this means for messaging:**
- "Dan Glasses is what personal AI should look like in the recursive-self-improvement era: small, on-device, auditable, and *yours*."
- Lead with the privacy + auditable-self-improvement story. Not with raw capability.
- **The Anthropic "brake pedal" call is a marketing tailwind for our positioning.** Use it.

---

## What to stop doing

- ❌ **Calling the danlab-multimodal feedback loop "RL."** It is a heuristic. Until harness+weights are open, the label stays pre-RL. This is the integrity call.
- ❌ **Building paperclip-style company infrastructure that doesn't drive a product.** Paperclip's value is as the orchestrator for Dan Glasses / dani. If it's not in that loop, it's dead weight.
- ❌ **Hand-rolling more Python daemons when OpenClaw can host the logic.** The 5-daemon split is right for the hot path (audio, vision, memory, tools, tts) but new logic should go in OpenClaw agents unless it has clear latency / safety requirements.
- ❌ **Optimizing for x86_64 laptop performance** beyond "good enough to demo." Every Watt we save on aarch64 matters 100× more.
- ❌ **Conflating LFM2.5-VL-450M (vision) with HRM-Text 1B (reasoning).** Two models, one pipeline. Document the distinction.
- ❌ **Adding a graph database in v1.5.** Memanto shows pure-vector can hit SOTA. Don't carry complexity without measured benefit.

---

## Risks (load-bearing)

| Risk | Severity | Mitigation |
|------|----------|------------|
| Redax hardware slips / dies | Critical | Tethered-glasses path with CoVSpec; indie hardware if necessary |
| HRM-Text 1B underperforms on real memory reasoning | High | LFM2-1.2B-Thinking fallback; benchmark on day 1 |
| Frontier model commoditizes our edge advantage | High | Lean harder on privacy, Indian-language coverage, always-on context |
| RHO / SIA doesn't beat the heuristic in 12 months | Medium | Honest publish. Negative results are still science. |
| India DPDP / EU AI Act compliance becomes a moat-instead-of-moat | Medium | Document the on-device design; certify if required |
| Key person dependency on somdipto | High | dani as the persistent memory of the org + this AGENTS.md system |
| Apple smart glasses ship in late 2027 with similar positioning | High | Lean into India-first, open-source, on-device. Apple's walled-garden approach is our opening. |
| Open-source AI companions commoditize the "personal intelligence" framing | Medium | Lean into *proactive* over reactive. Nobody has shipped proactive well yet. |

---

## One-line summary

**Ship the wearable, prove the platform, teach it to learn, make it initiate — and stay ruthlessly honest about what's heuristic and what's RL.** 

v6 deltas: HRM-Text 1B integrated; proactive AI promoted to v1.5 differentiator; CoVSpec tethered path added; Anthropic "brake pedal" framing absorbed; self-improvement landscape expanded to include RHO, HarnessX, AHE, HarnessForge.

---

## Footnotes

[^rho]: Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference. arXiv:2606.05922. https://arxiv.org/html/2606.05922v2
[^anthropic_brake]: Anthropic says AI labs need coordinated plan to halt development if risks rise. Reuters, 2026-06-04. https://www.reuters.com/business/anthropic-says-ai-labs-need-coordinated-plan-halt-development-if-risks-rise-2026-06-04/

---

*👾*
