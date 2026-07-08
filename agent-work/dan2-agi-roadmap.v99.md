# Danlab AGI Roadmap — 6 / 12 / 24 Months (v99)
**Author:** Dan2 👾
**Run:** 2026-06-27 10:30 IST (05:00 UTC)
**Version:** v99 — Mythos unblock changes the arXiv framing, GPT 5.6 staggering strengthens the on-device wedge, Perplexity Brain + Engram turn agent-memory into a category, Gemma 4 12B unified as v3 convergence
**Status:** Pending somdipto wedge-lock decision (still unresolved from v92-v99)

---

## North Star (unchanged)

> **Build the first wearable AI that interrupts you on purpose, with calibrated timing, in service of tasks you actually have — and remembers why, where, and what you said back.**

The last clause ("remembers why, where, and what you said back") is the v99 update. Proactive interruption without agent-self-memory is just notifications. Proactive interruption *with* agent-self-memory is a relationship.

---

## Horizon 1 — 6 months (Jul–Dec 2026): Ship the proactive loop with agent-memory

**Goal:** Show HN Aug 25 + arXiv Aug 15 + Founder Edition Q4. Proactive AI working end-to-end on a Linux laptop prototype. **v99 NEW:** agent-memory partition in memoryd v2 ships alongside HNSW + LFM2.5-Embedding.

### Critical path (gated, sequential) — v99 deltas in **bold**

1. **memoryd startup-probe pattern — by July 5 (Dan4).** /health returns 503 until listener bound + first-request model load. Apply to all 8 daemons. Non-negotiable.
2. **Wedge lock — by July 3 (somdipto).** DANI vs Dan Glasses. Blocks everything else.
3. **audiod v0.8 — SHIPPED this morning (Dan2).** WS proxy upgrade forwarding live. Confirmed by Dan2 v98b.
4. **OpenClaw Tailscale fallback — by July 8 (Dan1 + Dan2).** DanClaw proxy + Zo User Service public=false. **v99 confirms Tailscale Funnel is also blocked.**
5. **awarenessd v0.1 — by July 25 (Dan2 + Dan3 + Dan1).** BAO bandit over 3 harness variants. HRM-Text-1B on-device. **v99 NEW: GLM 5.2 cloud-fallback + PASK-style IntentFlow pre-screen + HANDRAISER-style cost-benefit calibration + agent-memory write on every interrupt decision.** This is the Show HN hero.
6. **memoryd v2 — by July 25 (Dan4).** HNSW + LFM2.5-Embedding-350M swap. **v99 NEW: agent-memory partition for BAO bandit posterior table.** Show HN-ready, not "after Show HN."
7. **Show HN — Aug 25.** Pitch the proactive loop, the 8-daemon harness, the receipts-first brand, the memoryd correction receipt, the model-agnostic reasoning adapter, the Indic-first TTS demo, the /privacy audit panel, **the agent-memory self-improvement loop (Perplexity Brain-style), the on-device-only mode for India users (geopolitically-conditioned framing).**
8. **arXiv paper — Aug 15 (Dan2 lead, somdipto co-author).** "Pre-RL Scaffold → SIA Harness-Only Self-Improvement for Edge VLMs." Cite SIA, Self-Harness, Continual Harness, HarnessX, APEX, BAO, ProActor, Anthropic Mythos / When AI Builds Itself, SemanticXR, GLM 5.2, Sapient HRM-Text-1B, **Perplexity Brain + Engram, Mythos partial unblock + GPT 5.6 staggering (geopolitical framing), Gemma 4 12B unified architecture, RAH performance attribution (harness > model).**
9. **Founder Edition (hardware) — Q4 2026.** First 100 units, India-first, $349 (premium) or $299 (match Muse Spark + Halo). Depends on Redax board + wedge-lock decision.

### Parallel work (non-blocking) — v99 deltas in **bold**

- **HRM-Text-1B integration** (Dan2 + Dan3): mlx-vlm support merged May 29. Q3, no defer.
- **GLM 5.2 cloud-fallback adapter** (Dan2 + Dan1): reasoning adapter with HRM-Text-1B (on-device) + GLM 5.2 (cloud). <4h swap.
- **Gemma 4 E2B QAT-mobile thermal fallback** (Dan3): benchmark in Q3.
- **memoryd v2 agent-memory partition** (Dan4): new table for BAO bandit posterior. **v99 NEW.**
- **memoryd v2 Indic retrieval quality** (Dan4): A/B LFM2.5-Embedding-350M vs MiniLM-L6-v2 on existing memory corpus.
- **Power measurement** (Dan3): ship `power_monitor` daemon. Read /sys/class/power_supply.
- **KV-cache INT4 (OSCAR) investigation** (Dan2): 4x KV memory reduction on LFM2.5-VL-450M.
- **OpenClaw sandbox hardening** (Dan1): default-deny on network tool calls.
- **SemanticXR read + assessment** (Dan2): 2 weeks in Q3.
- **Sapient HRM-Text internship application** (Dan1 + somdipto): apply Q3 for one Q4 hire.
- **Reasoning-adapter benchmark in dglabs-eval** (Dan1): 5 tasks × 4 models.
- **LFM2.5-VL-450M-Extract A/B test** (Dan3): swap description text → structured JSON.
- **/privacy route in Tauri shell** (Dan1 + Dan2 + Dan3): audit log + memory provenance + agent-memory visible.
- **Engram/Perplexity Brain public positioning** (Dan1 + Dan2): "the only on-device agent-memory." **v99 NEW.**
- **Mythos-unblock + GPT 5.6-staggering geopolitical framing** (Dan2): for arXiv paper + Show HN pitch. **v99 NEW.**
- **Gemma 4 12B unified architecture evaluation** (Dan2 + Dan3): R&D for H2 2027 v3. **v99 NEW.**
- **Sapient HRM-Text-1B intern application** (Dan1 + somdipto): apply Q3 for one Q4 hire.

### Q4 2026 milestones

- Founder Edition ships to first 100 users.
- awarenessd v1.0 with MIB evaluation + TEMPO response architecture + **PASK-style intent-aware proactive architecture**.
- Series A: term sheets or skip.
- **memoryd v3 prototype with SemanticXR object-level memory + CogMem 3-layer + Ebbinghaus forgetting curve.**

---

## Horizon 2 — 12 months (Jul 2026 – Jun 2027): Real AGI primitives + agent-memory convergence

**Goal:** memoryd v3 with continual learning + agent-self-improvement, awarenessd v2 with timing-aware RL, the lab publishes peer-reviewed work, Founder Edition v2 reaches 1,000 units.

### The four AGI primitives we will build — v99 framing

**Primitive 1 — Continual learning memoryd (v3)**

The thing that separates "a wearable with a database" from "a wearable that learns from experience." v3 is:
- **CogMem 3-layer** (LTM/DA/FoA) — long-term/session/turn.
- **DPCM async system** — System 1 sync (on-device) + System 2 async (cloud-fallback).
- **Agent-memory partition** (v99 NEW) — separate from user-facing memories, stores interrupt outcomes, bandit posteriors, salience history.
- **SemanticXR object-level schema** — bind semantic embeddings to persistent 3D objects.
- **Ebbinghaus forgetting curve** (à la SAGE) — drop memories with low retention.
- **Active consolidation** — promote episodic → semantic on repetition.
- **HNSW over LFM2.5-Embedding-350M** (1024-dim, 22 Indic).
- **Engram-pattern provenance fields** — every memory carries a source field (who stored, when, from which input).

The research contribution: **continual learning + agent-self-memory on a sub-1GB memory budget, with object-level state tracking and provenance.** Publishable.

**Primitive 2 — awarenessd v2 with timing-aware RL + agent-self-improvement loop**

Proactive AI done right. Built on BAO + PASK + HANDRAISER:
- **BAO bandit over 3 harness variants** (v0.1).
- **PASK-style IntentFlow demand detection** — pre-screen before bandit.
- **HANDRAISER-style cost-benefit calibration** — every interrupt has estimated cost and benefit.
- **ProActor reference action annotation pipeline** (when should the agent have interrupted?).
- **Stage-aware composite reward** (RULER-based + alignment-based).
- **GRPO optimization** over LFM2.5-1.2B-Thinking as the policy.
- **Adaptive interrupt threshold** — the bandit learns when NOT to interrupt.
- **Cloud-fallback reasoning via GLM 5.2** for high-stakes decisions.
- **Agent-self-improvement loop** (v99 NEW) — Perplexity Brain pattern: every interrupt decision updates the bandit posterior overnight.

This is the thing that makes Dan Glasses the **first glasses that interrupts on purpose AND learns from the outcome**. Publishable.

**Primitive 3 — Harness-only self-improvement (the SIA fork)**

The credible AGI primitive that danlab-multimodal prefigures:
- **SIA 3-agent loop** (Meta / Task / Feedback) with harness-only updates.
- **LFM2.5-1.2B-Thinking as Feedback-Agent.**
- **5 domains from danlab-multimodal eval** (3 existing + LawBench-style + KernelBench-style).
- **Continual Harness reset-free online updates** (carry from v99).
- **APEX-style three-layer co-evolution** (harness + behavioral principles + workflow topology).
- **RAH performance attribution methodology** (harness > model at same model size).
- **SGM-style e-value gate** (p < 0.05).
- **Cite Anthropic "When AI Builds Itself"** as the trillion-dollar-scale validation.
- **Cite Mythos partial unblock + GPT 5.6 staggering** as evidence for open-weight edge.

The research contribution: **empirical demonstration that harness evolution alone, with frozen weights, gets large gains on edge — at a time when closed-weight frontier is geopolitically gated.** Publishable.

**Primitive 4 (v99 NEW) — On-device agent-self-memory**

The thing that makes Perplexity Brain + Engram look cloud-only by comparison:
- **Self-improving memory** that learns overnight from interrupt outcomes.
- **On-device-only storage** by default; cloud sync opt-in.
- **Provenance fields** for auditability.
- **Engram-style 100× token efficiency** claim we can test against.
- **Cross-session learning** with Ebbinghaus forgetting.
- **Object-level binding** via SemanticXR for "the same pharmacy" recognition.

The research contribution: **on-device agent-self-memory at sub-1GB with privacy + auditability + Indic support, when cloud alternatives are geopolitically conditioned.** Publishable.

### Milestones

- Q1 2027: memoryd v3 ships in Founder Edition v2.
- Q1 2027: awarenessd v2 with timing-aware RL + agent-self-improvement loop.
- Q1 2027: SIA harness-only paper accepted at ICLR 2027 workshop (or NeurIPS).
- Q2 2027: Founder Edition v2 ships to 1,000 units.
- Q2 2027: Series A close (or skip, ride to profitability on Founder Edition revenue).

---

## Horizon 3 — 24 months (Jul 2026 – Jun 2028): Convergence

**Goal:** Four primitives converge into the AGI-on-wrist product.

### The convergence — v99 framing

By H2 2027, the 2026 hardware (Snapdragon Reality Elite, Redax, Jetson Orin Nano) is mature. The 2027 frontier models fit on a wearable. **The single-model convergence is the new long-term thesis.**

**Convergence v1 — 2027 H2:**
- memoryd v3 (continual learning + object memory + agent-self-memory) + awarenessd v2 (timing-aware RL) + SIA harness-only loop.
- **Hardware: Snapdragon Reality Elite (48 TOPS) or Redax equivalent.**
- **Latency budget: <250ms VLM, <500ms end-to-end interruption.**
- **Battery life: 4h active use (PRD target, but Muse Spark claims 8h — this becomes the bar).**

**Convergence v2 — 2028 H1:**
- **Gemma 4 12B unified architecture (v99 NEW)** — single-model for vision + audio + text + reasoning. Replaces the LFM2.5-1.2B-Thinking + LFM2.5-VL-450M pair.
- 12B unified gives 5–10× reasoning quality at 2× compute (encoder-free design eliminates fusion overhead).
- awarenessd v3 with planning horizon (HRM-Text-2B successor or Gemma 4 12B reasoning mode).
- **The first glasses that plan.**

### The convergence thesis

The four primitives are not independent. They reinforce each other:
- **memoryd v3** feeds **awarenessd v2** with personalized + object-aware + agent-self-memory context.
- **awarenessd v2** generates interruption events that go into memoryd as episodic memories (with object-binding + agent provenance).
- **SIA harness-only loop** evolves the prompt/tooling of awarenessd v2 over time.
- **On-device agent-self-memory** lets the bandit learn from each user's interrupt response — without sending data to Perplexity or Engram.
- **The whole system learns from the user's reactions to its interruptions, on-device, auditable, geopolitically independent.**

This is the AGI-on-wrist thesis. The 2026 work (H1) ships the components. The 2027 work (H2) integrates them. The 2028 work (H3) is the convergence.

### 24-month milestones

- 2027 Q3: Convergence v1 ships in Founder Edition v3 (5,000 units).
- 2027 Q4: Show HN 2.0 — "the glasses that plan, the agent that learns."
- 2028 Q1: Convergence v2 ships.
- 2028 Q2: arXiv paper on the convergence — "Continual learning + proactive RL + harness self-improvement + on-device agent-memory on a wearable, in a geopolitically-gated world." This is the paper that makes Danlab a credible AGI lab.

---

## What this roadmap is NOT (unchanged from v97)

- **Not a moonshot AGI timeline.** Engineering. Each horizon ships working product before the next horizon begins.
- **Not a pivot from the product.** DANI / Dan Glasses / Danlab-multimodal / Paperclip are all real artifacts. The roadmap layers the AGI work on top.
- **Not a hedge against Anthropic / DeepMind / OpenAI.** They are doing frontier-scale + geopolitically-conditioned. We are doing edge-scale + geopolitically-independent.
- **Not abandoning the receipts-first brand.** Every horizon ship comes with a STATUS.md, a public infra count, a published correction when wrong.

---

## Risks to the roadmap (v99 update)

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Redax hardware slips past H2 2027 | Medium | High | Laptop prototype + Founder Edition as USB-camera accessory |
| memoryd flat cosine → HNSW migration breaks existing memories | Low | High | Backwards-compatible storage, re-embed on access |
| awarenessd v0.1 misses Show HN (Aug 25) | Medium | High | Dan2 + Dan3 critical path, weekly checkpoints, fallback to V_HEDGE-only demo |
| Somdipto gets stuck on the wedge-lock | High | Critical | Dan2 + Dan1 will each surface a one-pager; somdipto picks |
| LFM2.5-VL-450M deprecated by Liquid AI before Q4 | Low | Medium | LFM2.5-VL-1.6B (Q4 2026 rumored) + Gemma 4 E2B QAT-mobile ready |
| Anthropic / DeepMind open-weight edge model | Low | Medium | Our wedge is the proactive layer + on-device agent-memory, not the model |
| BAO / SIA / ProActor don't reproduce | Medium | Medium | The papers are recent; replication is publishable in itself |
| Meta Muse Spark at $299 undercuts Founder Edition pricing | High | High | Differentiate on auditable proactive + Indic + on-device reasoning + agent-memory. Don't race on price. |
| OpenClaw Tailscale failure blocks remote gateway access | High | Medium | DanClaw proxy + Zo User Service public=false. Mitigation in v98/v99 critical path. |
| GLM 5.2 cost increases after DeepSeek-moment hype | Low | Medium | On-device HRM-Text-1B is default; GLM 5.2 is opt-in. |
| Gemma 4 E2B license restricts commercial use | Medium | High | Verify Q3 week 1. Fallback: LFM2.5-230M thermal fallback. |
| Sapient HRM-Text internship program fills before our application | Low | Low | Apply Q3; accept if offered; hire through normal channels if not. |
| **Mythos fully unblocks + GPT 5.6 reaches general release (v99 NEW)** | Medium | Medium | Our wedge is on-device + auditable + geopolitically-independent, not "frontier access." |
| **Perplexity Brain / Engram captures agent-memory category before Show HN (v99 NEW)** | Medium | High | Differentiate on on-device + privacy + auditable. Make the agent-memory partition visible at Show HN. |
| **Gemma 4 12B unified beats our multi-model pipeline by H2 2027 (v99 NEW)** | Medium | Low | We adopt it as v3. The convergence thesis anticipates this. |
| **OpenAI IPO delay signals broader AI capex slowdown (v99 NEW)** | Medium | Medium | Our path is bootstrappable to revenue, not venture-scale. |

---

## What somdipto needs to decide this week (v99, 18 questions)

**Carry from v98 (still unanswered):**

1. **Wedge** — DANI or Dan Glasses? By July 3.
2. **Show HN scope** — minimal awarenessd or full (+memoryd recall +ttsd + GLM 5.2 + agent-memory + PASK pre-screen)? v99 recommends **full**.
3. **Founder Edition timing** — Q4 2026 vs Q1 2027?
4. **Founder Edition pricing** — $349 (premium) or $299 (match Muse Spark + Halo)? v99 recommends $349.
5. **HRM-Text-1B integration priority** — Q3 or Q4? v99 recommends Q3.
6. **GLM 5.2 cloud-fallback on by default?** v99 recommends OFF, opt-in.
7. **Anthropic "When AI Builds Itself" companion paper** — YES.
8. **Series A posture** — bootstrapped through Show HN or start the deck?
9. **India-language priority** — Hindi + Bengali for v1? v99 recommends YES.
10. **Dani vs Dan Glasses integration** — separate products or one product with two channels?
11. **Sapient HRM-Text internship** — apply Q3.
12. **SemanticXR prototype** — Q3 read, Q4 prototype. v99 recommends YES.
13. **memoryd startup-probe rollout** — all 8 daemons by July 5.
14. **/privacy route in Tauri shell** — Q3 work item.

**NEW v99 (4):**

15. **memoryd v2 agent-memory partition — ship alongside HNSW + LFM2.5-Embedding?** Recommend YES, by July 25.
16. **Engram/Perplexity Brain competitive response — public positioning?** Recommend "the only on-device agent-memory." Show HN ready by Aug 25.
17. **Closed-weight geopolitically-conditioned framing in arXiv paper + Show HN?** Recommend YES — cite Mythos partial unblock + GPT 5.6 staggering as evidence.
18. **Gemma 4 12B unified architecture — long-term v3 commitment?** Recommend YES, R&D-only for H2 2027.

---

*Dan2 👾 — 2026-06-27 10:30 IST — committed to building the future with my partner*
