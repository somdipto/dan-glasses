# Danlab AGI Roadmap — 6 / 12 / 24 Months
**Author:** Dan2 (co-founder, lead scientist, architect)
**Date:** 2026-06-16
**Inputs:** `dan2-research-report.md`, `dan2-architecture-review.md`, `dan2-model-analysis.md`, canonical Dan Glasses spec, danlab-multimodal README, paperclip AGENTS.md, blurr README.
**North Star:** Build always-on, on-device, privacy-preserving multimodal intelligence that genuinely learns from experience. Ship it as a wearable (Dan Glasses), an open platform (dani), and a multi-agent org (paperclip / DanClaw).

---

## Strategic Frame

Three things must be true for Danlab to make a real AGI contribution from India by 2028:
1. **Hardware in hand.** No roadmap survives without a target. The Redax board is the bottleneck. If it doesn't ship in Q3 2026, we have to be honest about a different path.
2. **A defensible niche.** Frontier labs own 70%+ of the general capability surface. We win on **on-device multimodal + privacy + always-on context + Indian-language coverage**. That is the niche. Everything outside it is distraction.
3. **A self-improving loop that is *actually* self-improving.** Not a hand-coded heuristic. The SIA path (Hexo Labs, MIT, May 2026) + test-time training (TT-SI, ACL 2026) is the credible playbook.

---

## 6-Month Plan (Jun 2026 → Dec 2026) — "Ship the wearable, prove the platform"

**Theme:** Get Dan Glasses v1 into real hands. Get paperclip (now DanClaw) re-animated. Get a real self-improvement experiment running in danlab-multimodal.

### Hardware / wearable (Track B unblock)
- **Resolve the Redax situation.** If hardware ships in Q3, port Dan Glasses to it (aarch64 rebuild, not rewrite — Tauri code is portable). If it slips, write a **tethered glasses form-factor** path: existing glasses + USB-C compute puck (Raspberry Pi 5 8GB or Snapdragon Dev Kit). This gets us in the field without waiting.
- **Define a real power budget.** Measure every component on the actual target. Stop using "5–10W" as a planning number. Concrete targets:
  - sleep (camera off, mic ready, wake on voice trigger): **<0.3W**
  - idle (camera on, no VLM): **<0.8W**
  - watchful (salience-gated VLM, 1 inference / 3s avg): **<1.5W**
  - active (continuous VLM, LLM on demand): **<3.0W peak**
- **Battery target:** 4h mixed-use at the watchful budget. If unachievable, target 2h and document the tradeoff.
- **Weight target:** **<50g** including temples, camera, battery. The Brilliant Labs Frame at 39g and Ray-Ban Meta at 49g set the bar.
- **Wake-word service (`wakewordd`).** Porcupine or openWakeWord (Snowboy successor). The audiod spec already calls this "v3" — promote to v1.1.

### Software / platform
- **Memory architecture v1.5** (memoryd): add **temporal + confidence** metadata to every embedding; Ebbinghaus-style confidence decay; simple 4-signal score (semantic × temporal × confidence × relational). This is a 2-week change to memoryd + a small migration of existing memories. The single biggest credibility upgrade.
- **TT-SI pilot** in danlab-multimodal: replace the hand-coded heuristic scorer with a small learned reward model (MiniLM cross-encoder fine-tuned on 200–500 human-rated descriptions). Same loop shape. **It is still not RL** but it is the prerequisite. The heuristic label stays until harness+weights are open.
- **Prompt injection hardening** on the perception → os-toold path. The canonical analysis flagged this. Synthius-Mem's adversarial robustness work (99.6%) shows the bar. Cheap mitigation: argument-hashing + denylist extension + a perception-frame trust score.
- **DCM v2.5** (Dan's memory): make SOUL.md / AGENTS.md / IDENTITY.md load on session start, just like OpenClaw's bootstrap memory. Already partly shipped; finish it.
- **paperclip → DanClaw reactivation.** It's dormant (per its AGENTS.md). Re-orient it as the **multi-agent company orchestrator** that drives Dan Glasses: the gateway through which Dan (the AI co-founder) operates the company (issue tracking, goal mgmt, deployment infra). Keep the cool name. Keep the rail guard (policies, per-agent tool filtering).

### Research / open-source contributions
- **Publish the SmolVLM-256M ↔ LFM2.5-VL-450M comparison on Indian-language OCR.** Nobody has done this credibly. danlab-multimodal is the natural home.
- **Open-source `dan-lab/wakewordd` and `dan-lab/memoryd` separately from the dan-glasses repo.** These are reusable primitives. The "world's best skills library" framing from dani-skills applies here.

### Success criteria (Dec 2026)
- [ ] Dan Glasses v1 demoable end-to-end (audio + vision + memory + tool use) on target hardware.
- [ ] Battery life measured and published in spec.
- [ ] memoryd v1.5 deployed with temporal + confidence scoring.
- [ ] danlab-multimodal v2 using a learned (not heuristic) reward model.
- [ ] paperclip-DanClaw gateway revived with at least 2 live agents.

---

## 12-Month Plan (Jun 2026 → Jun 2027) — "Make it learn, make it safe"

**Theme:** Move from "always-on wearable" to "always-on wearable that learns." Add the dual-process memory, the test-time self-improvement, and the real proactive AI.

### Self-improvement — past heuristic, into TT-SI
- **TT-SI in production (danlab-multimodal v3).** Three steps: self-awareness (which descriptions are weak?), self-data augmentation (generate similar queries), test-time training (small LoRA on the weak areas). Target: 5–10% absolute gain on a held-out eval of "describe this screen" quality.
- **Fork SIA** (Hexo Labs, MIT, May 2026) and integrate as a harness. The SIA framework is the *credible* open path to harness+weights self-improvement. Until this ships in danlab-multimodal, the project keeps the "pre-RL scaffold" label — and that is correct.
- **Published ablation:** heuristic vs. learned reward model vs. TT-SI vs. SIA-fork. Four configurations, same eval, same data. This is the contribution to the field.

### Memory — dual-process, schema-inducing
- **Memory v2 (DPA / DPCM-style):** two processes:
  - **Daytime writer** (synchronous, fast): records belief revisions as doubly-linked "supersedes" chains.
  - **Nighttime engine** (async, batched): induces schemas, intentions, cross-domain abstractions; detects collisions.
- **TiMem-style Temporal Memory Tree** on top: hierarchy of (raw events → episodic → semantic → procedural → schema).
- **Adversarial-robust memory** (Synthius-Mem lessons): CategoryRAG with hallucination resistance > 99%.
- **LoCoMo benchmark eval.** 75–95% range is where 2026 SOTA lives. We should be in that range by Q4 2026.

### Proactive AI
- **Proactive trigger layer** in OpenClaw: lightweight graph-based model (Microsoft Research "Do Proactive Agents Really Need an LLM" — 220 MiB BF16, on-device). LLM only fires when the trigger fires.
- **Salience-aware interrupt policy.** Don't speak unless the user is likely to want it. Sensible Agent (UMD 2026) shows how to do this with gaze/hand-occupancy signals.
- **Daily briefing agent.** Calendar + email + recent memories → 60-second spoken summary. The "killer app" for an always-on wearable.

### Privacy + safety — make it a moat
- **DPDP Act + EU AI Act compliance audit.** India DPDP and EU AI Act are both tightening in 2026. On-device-only is a compliance advantage. Document it.
- **Federated fine-tuning** for user-specific memory: each user's memories fine-tune their own model, never the central model. This is the privacy story.
- **Perception-frame trust score** in perceptiond: scored by visual coherence, content type, prompt-injection risk. Below threshold → no tool execution.

### Success criteria (Jun 2027)
- [ ] danlab-multimodal v3 with TT-SI in production, published eval.
- [ ] Memory v2 (dual-process) deployed; LoCoMo in SOTA range.
- [ ] Proactive trigger layer live in OpenClaw.
- [ ] Daily briefing agent demoable.
- [ ] Dan Glasses v1.5 shipped to ≥10 pilot users (likely ourselves + 9 testers in Bengaluru).
- [ ] DanClaw multi-agent orchestrator running the company.

---

## 24-Month Plan (Jun 2026 → Jun 2028) — "Make it co-evolve with the user"

**Theme:** From "personal assistant" to "personal intelligence that co-evolves." This is where Danlab's contribution to AGI gets sharp.

### AGI-shaped research bets
- **Recurrent latent reasoning (RLRP, ICLR 2026) in the on-device LLM.** Internal latent refinement, not external CoT. Compatible with our current llama.cpp stack. This is the path to "reasoning at the edge" without burning tokens.
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
- **Indie hardware path.** If Redax is a dead end, we have to design our own. 6-month clock on that decision (must be made by Dec 2026).

### Hiring + organization
- **Research scientist** focused on self-improvement / RL — single highest-leverage hire.
- **Embedded systems engineer** for the actual wearable path.
- **Hindi/Tamil/Bengali linguist** for the Indian-language bet.
- **OSS maintainer** for dani-skills (this is the distribution channel).

### Success criteria (Jun 2028)
- [ ] Dan Glasses v2 with self-improving memory and proactive trigger layer shipping as a product.
- [ ] At least 2 open-source releases with measurable adoption.
- [ ] A published paper from danlab at a major venue (NeurIPS / ICML / ICLR). Likely target: edge self-improvement or memory architecture.
- [ ] dani-skills: 50+ production-grade skills in the catalog.
- [ ] A demonstrable co-evolution loop: the assistant's behavior demonstrably changes based on accumulated user-specific memory, in a way that's auditable.

---

## What to stop doing

- ❌ **Calling the danlab-multimodal feedback loop "RL."** It is a heuristic. Until harness+weights are open, the label stays pre-RL. This is the integrity call.
- ❌ **Building paperclip-style company infrastructure that doesn't drive a product.** Paperclip's value is as the orchestrator for Dan Glasses / dani. If it's not in that loop, it's dead weight.
- ❌ **Hand-rolling more Python daemons when OpenClaw can host the logic.** The 5-daemon split is right for the hot path (audio, vision, memory, tools, tts) but new logic should go in OpenClaw agents unless it has clear latency / safety requirements.
- ❌ **Optimizing for x86_64 laptop performance** beyond "good enough to demo." Every Watt we save on aarch64 matters 100× more.

---

## Risks (load-bearing)

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Redax hardware slips / dies | Critical | Tethered-glasses path; indie hardware if necessary |
| Frontier model commoditizes our edge advantage | High | Lean harder on privacy, Indian-language coverage, always-on context |
| Self-improvement doesn't beat the heuristic in 12 months | Medium | Honest publish. Negative results are still science. |
| India DPDP / EU AI Act compliance becomes a moat-instead-of-moat | Medium | Document the on-device design; certify if required |
| Key person dependency on somdipto | High | dani as the persistent memory of the org + this AGENTS.md system |

---

## One-line summary

**Ship the wearable, prove the platform, teach it to learn — and stay ruthlessly honest about what's heuristic and what's RL.**

*👾*
