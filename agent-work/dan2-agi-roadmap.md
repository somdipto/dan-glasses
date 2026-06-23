# Danlab AGI Roadmap — v40
**Author:** Dan2
**Date:** 2026-06-23
**Horizon:** 6 / 12 / 24 months

> **Read first:** `dan2-research-report.md` (v40), `dan2-model-analysis.md` (v40), `dan2-architecture-review.md` (v40).

> **v40 thesis (one sentence):** The v39 roadmap is correct in direction; v40 sharpens the model strategy around **HRM-Text 1B** (we own the reasoning stack), adds **agentd + learnerd** (the missing agency layer), pivots to **memoryd v2** (Infini Memory topic-documents), and tightens the wearable window to **12-18 months before Meta locks the mainstream market**.

This roadmap is a recommendation, not a contract. Somdipto has the final call.

---

## North star

**"The first truly private, self-improving, ambient AI — built in India, on open reasoning models, for the Global South."**

By 2028, Dan Glasses should be the wearable AI that:
1. **Reasons on its own model** (HRM-Text-1B fine-tuned on Danlab data) — not a U.S. cloud API.
2. **Learns from every interaction** (real self-improvement: harness + weights, SIA-W+H pattern).
3. **Respects privacy as a design constraint** — on-device by default, no cloud-by-default.
4. **Runs on hardware we control** (NDP200, or GAP9 if NDP slips, or Snapdragon AR1 Gen 2 if we have to).
5. **Ships a memory and personality that survives** across sessions, devices, and replacement cycles.
6. **Is open source** — auditable, modifiable by the user, forkable by the world.

This is the moat. The product surface is the glasses; the moat is the **model-of-the-user** that the product builds over time, running on **a reasoning model we own**.

---

## Strategic bets (the three things we will not compromise on)

1. **We own the reasoning stack.** v1.5 ships HRM-Text-1B fine-tuned on Danlab data. v2 ships HRM-Text-3B. We do not rent Claude/GPT for the agent loop. The $1,500 training cost puts this within reach — there is no excuse not to.
2. **Self-improvement is the product.** We do not ship a chatbot. We ship a learning system. The v1.0 dashboard for the user is a "what Dani learned this week" view. The v1.5 backend is a SIA-H harness-improvement loop. The v2 backend is a SIA-W+H weight-improvement loop on HRM-Text.
3. **The wearable window is 12-18 months.** Meta Ray-Ban Display at $799 + Gen 3 leaks suggest multi-hour Live AI by late 2026. If we don't ship a credible v1 by Q2 2027, we lose the narrative. **Ship the v1 desktop prototype by Q4 2026. Ship the wearable v1.5 by Q2 2027.**

---

## 6-month roadmap (now → Dec 2026)

**Theme: ship a credible v1 desktop prototype + start the HRM-Text fine-tuning pipeline.**

### Engineering

- **agentd (Rust).** Stand up the agent runtime that owns the planning loop, tool orchestration, and budget enforcement. OpenClaw sits underneath as transport. This is the single biggest architectural gap in the current stack. **v40 adds: agentd talks to HRM-Text-1B for reasoning, not Claude/GPT.**
- **learnerd (Python).** SIA-H-style harness improvement loop. Nightly job: a local LFM2 model reads the day's logs, identifies failure modes, proposes harness changes to agentd, persists them with version control. The user reviews and approves. This is real self-improvement, scoped to the harness, in 6 months.
- **memoryd v1 → v2.** Begin migration from flat vector store to Infini Memory topic-structured documents. Dual-mode for 1 release (v1 read-only, v2 takes new writes), then v2 only.
- **Embeddings swap.** all-MiniLM-L6-v2 → LFM2.5-Embedding-350M. 384d → 1024d, native multilingual, Apache 2.0-equivalent license. **Sovereignty moat strengthens: no U.S.-controlled embedding model.**
- **HRM-Text-1B fine-tuning pipeline.** Set up the training infrastructure (H100 or H200 access, 16 GPUs, 1.9 days per run). Fine-tune HRM-Text-1B on Danlab data: voice transcripts, memory schemas, salience decisions, tool-call traces. Target: HRM-Danlab-1B v1, integrated into agentd as the default reasoning model by end of month 6.
- **Eval harness (dglabs-eval v1).** 50-100 test scenarios (conversation, tool-use, memory recall, proactivity, safety) that run nightly and produce a regression report. The eval is the scientific credibility layer.
- **DanClaw proxy.** Wrap OpenClaw behind a hardened proxy that suppresses its crash propagation, mirrors state to memoryd, and exposes a wearable-grade control API. v38 carry-over.
- **Smart frame selection in perceptiond.** Pre-filter with a tiny YOLO model (TinyissimoYOLO-class) and only call the VLM on frames that pass the salience test. Targets: 67% reduction in VLM calls.
- **Perceptiond tile-based inference.** Switch to a BlueLM-2.5-3B style tile-based pipeline for high-res images.
- **Rename the "RL feedback loop"** in danlab-multimodal. Stop calling it RL. Call it "in-context preference memory" or "contextual bandit harness" — accurate, defensible, signals we know the difference.

### Product

- **"What Dani learned this week" screen.** First-class UX surface for self-improvement. Shows the user what the agent noticed, what it changed, what it wants to change. The user approves, rejects, or modifies. This is the product surface for learnerd.
- **Privacy dashboard.** Screen that shows exactly what is on-device, what (if anything) is in the cloud, and what has been deleted. This is the differentiator vs Meta + Apple.
- **Onboarding flow for the memoryd.** First time a user puts on the glasses, set up the typed memory schema (working, episodic, semantic, procedural) with explicit defaults.
- **Telegram bridge hardening.** Make the Telegram channel the user's window into learnerd's proposals. Every harness change appears as a Telegram message with a yes/no/edit reply.

### Research

- **Validate HRM-Text fine-tuning on our domain.** Run the full training pipeline. Measure reasoning quality on our eval set. Measure inference latency on phone-class hardware (Snapdragon 8 Gen 3 or equivalent).
- **Validate Infini Memory topic-document pattern on memoryd.** Implement a prototype, benchmark against the current flat vector store on the LoCoMo benchmark. Goal: better long-term memory with fewer context tokens.
- **In-context contextual bandit prototype.** 100-line Python implementation that uses the episodic memory as a policy library. This is what we ship as the v1 "learning" loop while learnerd is being built.
- **Voice cloning feasibility study.** Can we fine-tune KittenTTS Mini on 5 minutes of recorded speech in <1 hour on a phone? If yes, ship in v1. If no, ship cloud-fine-tune with explicit privacy disclosure.

### Hiring (if budget allows)

- **Rust systems engineer** for agentd.
- **ML systems engineer** for HRM-Text fine-tuning pipeline + memoryd v2.
- **Embedded ML engineer** for smart frame selection + NDP200 integration.

### Budget

- HRM-Text fine-tuning runs: 16 × H100 × 1.9 days ≈ $1,500 per run. Plan 5-10 runs in 6 months = $7,500-$15,000.
- Brilliant Labs Halo ($349) + GAP9 dev kit (~$300) for wearable prototyping.
- dglabs-eval compute: ~$2,000/month for nightly evals.

---

## 12-month roadmap (Dec 2026 → Jun 2027)

**Theme: ship a self-improving system that is demonstrably better than v1, on a wearable form factor.**

### Engineering

- **agentd v1 → v2.** Add proactive triggering, calendar awareness, location awareness. The "should I speak now?" model becomes learned (ProAct pattern), not rule-based.
- **learnerd v1 → v2: SIA-H → SIA-W+H.** Add weight updates. Federated preference fine-tuning of HRM-Danlab-1B. Users opt in explicitly. We train a reward model on (output, user_correction) pairs, then DPO the base model. Push updates back via OTA. **v40 anchor: SIA-W+H numbers are real (LawBench +25.1pp over SOTA).** We can do this.
- **memoryd v2 → v3.** Add MemVerse-style periodic distillation. Compress long-term memory to parametric recall. The "I remember everything you've ever said" feature becomes feasible at wearable scale.
- **Wearable port (Dan Glasses v1.5 hardware).** Build the first wearable prototype. Reference design: OpenGlass (67.4 mW continuous, 200 mAh battery) + Brilliant Labs Halo form factor. Target: 18h battery on a single charge, <80g total weight.
- **Cross-device memory sync.** User gets a new phone, or a new pair of glasses. Memory follows them. Encrypted, end-to-end, user-owned.
- **Voice clone v1.** On-device fine-tuning of KittenTTS Mini. 5 minutes of voice, 1 hour of compute on the phone, lifetime of personal TTS.
- **proactived.** Owns the "should I speak now?" decision. V1: rule-based. V2: learned. V3: self-improving.
- **Smart frame selection on wearable hardware.** TinyissimoYOLO-class pre-filter on the always-on chip. VLM (HRM-Text-VL, see model analysis) only on salient frames.

### Product

- **Dani Skills marketplace.** Open the dani-skills registry to community contributions. The OpenClaw-moment for us.
- **Dani Marketplace v0.** Users browse, install, share skills. Open format, signed registry, user owns their data.
- **Privacy-preserving federation.** Opt-in to share improvement data with the Danlab community, with differential privacy guarantees. This is how we get the data volume for weight updates.

### Research

- **HRM-Danlab-3B.** Scale up. Train a 3B parameter reasoning model on Danlab data. Target: 70-80% of GPT-4 quality on our eval set, fully on-device.
- **True RL on the harness.** Move from in-context bandit to a proper contextual bandit with credit assignment. Academic contribution worth publishing.
- **Memory consolidation with neural networks.** Replace LLM-based fact extraction with a smaller, fine-tuned model.
- **HRM-Text-VL exploration.** Multimodal extension of HRM-Text. Watch for Sapient's roadmap.

### Budget

- HRM-Danlab-3B training: 16 × H100 × ~7 days ≈ $5,000-$10,000 per run. Plan 3-5 runs = $15,000-$50,000.
- Wearable dev kits: Brilliant Labs Halo ($349) + GAP9 ($300) + Qualcomm AR1 dev kit (~$2,000) = $2,650.
- dglabs-eval: $2,000/month × 6 = $12,000.

---

## 24-month roadmap (Jun 2027 → Jun 2028)

**Theme: ship the first truly self-improving personal AI, on custom hardware, that is open source.**

### Engineering

- **Dan Glasses v2 hardware.** Bigger battery (400-500 mAh), better display, more compute (NPU bump). Reference: Nanomind (0.375W continuous VLM, 18.8h on 2000 mAh) + OpenGlass (67.4 mW continuous, 11.5h on 200 mAh).
- **On-device fine-tuning.** Run DPO/RLHF on the wearable. User trains their own model on their own data, on their own device. The privacy story taken to its logical conclusion.
- **Dani v2 (the "brain").** Move from agent runtime to a true cognitive architecture. Episodic + semantic + procedural + working memory, with a planner that uses all four. CMA paper is the spec.
- **Multi-agent Danlab.** Different agents for different tasks (calendar agent, learning agent, conversation agent, vision agent), coordinated by a meta-agent. Microsoft Scout / Perplexity Computer pattern.
- **Self-improving memory.** Perplexity Brain-style. The memory system improves itself nightly, based on what the user engages with and what they ignore.

### Product

- **Dani as a platform.** Third-party developers build on top of Dani. Skills, agents, integrations. The "Android of personal AI."
- **Dani as a service for other wearables.** License the platform to other hardware makers. The Android play.
- **Dani for India.** Local language support, local cultural context, local regulatory compliance. India is the test market; the Global South is the beachhead.
- **HRM-Danlab-Public.** Open-source the HRM-Text fine-tuned model. Let the world run our reasoning model. The moat is the integration, not the weights.

### Research

- **Publish the self-improvement framework.** Take what we learn from in-production self-improvement and publish it. This is how we hire, how we get academic credibility, and how we contribute back.
- **Open-source agentd + learnerd.** The most novel pieces of our stack. The community will improve them faster than we can.
- **Cross-lab collaboration.** Sakana RSI Lab, Hexo SIA, Sapient HRM, Perplexity Brain, Danlab. We are not in the AGI race alone. The community is the moat.
- **HRM-Danlab-VL.** Vision-language variant of our reasoning model. Watch Sapient's HRM-VL roadmap.

---

## What we will NOT do (the explicit non-goals)

- **We will not try to beat Meta on hardware or scale.** They have 7M+ units and a $50B+ war chest. We win on privacy, on custom hardware, on open source, on India.
- **We will not build a foundation model from scratch (yet).** We use HRM-Text-1B as the base, fine-tune on Danlab data. Our contribution is the fine-tuning recipe, the agent runtime, the memory system, the self-improvement loop — not the base model architecture. (If HRM-Text proves to be the wrong base by 2027, we revisit.)
- **We will not rent Claude/GPT for the agent loop.** v1.5 ships on HRM-Danlab-1B. Cloud APIs are for eval + training only.
- **We will not ship a chatbot.** We ship a learning system. The "what Dani learned this week" view is the product. The conversation is the interface.
- **We will not compromise on privacy for capability.** If a feature requires cloud-by-default, it does not ship. Period.

---

## v40 changes from v39

1. **Model strategy:** v39 said "use LFM2-VL, BlueLM, and other open models." v40 says **"own the reasoning stack with HRM-Text-1B fine-tuned on Danlab data."** The Sapient result changes the economics.
2. **Self-improvement:** v39 said "ship Option B (in-context contextual bandit) as v1, plan Option A (DPO) as v2." v40 says **"ship SIA-H (harness-only) as v1, SIA-W+H (harness + weights) as v2."** The verified SIA numbers justify the v2 weight-update path.
3. **Memory:** v39 said "memoryd v2 with typed memory + bi-temporal edges." v40 says **"memoryd v2 with Infini Memory topic-structured documents, v3 with MemVerse periodic distillation."** The 2026 memory research is the new spec.
4. **Wearable window:** v39 said "the window is 12-18 months." v40 tightens this with Meta Ray-Ban Display at $799 and Gen 3 leaks confirming multi-hour Live AI. **The window is 12 months, not 18.**
5. **Embeddings:** v39 didn't mention embeddings specifically. v40 adds **LFM2.5-Embedding-350M swap** as a 6-month priority (sovereignty + multilingual + better retrieval).
6. **Dani vs. Dan Glasses priority:** v39 asked. v40 recommends **Dan Glasses is the lead product, Dani is the platform.** Ship the wearable first; the platform follows.

---

## Open questions for somdipto

1. **Hardware roadmap.** Dan Glasses hardware on a 6-month or 12-month cadence? This determines the model upgrade path.
2. **Cloud policy.** Strictly local-first, or opt-in cloud features (voice clone training, federated improvement)? The answer changes the architecture.
3. **India focus.** Building for India first then expanding, or global with India as flagship? Changes language and cultural priorities.
4. **Academic engagement.** Want to publish papers? Sapient + Hexo + Sakana are all in the open-source reasoning + RSI space. Co-authoring or citing would be valuable.
5. **Hiring budget.** The 6-month plan needs 2-3 senior engineers + HRM fine-tuning compute. Is that budget available?
6. **HRM-Text partnership.** Should we reach out to Sapient for a joint paper or fine-tuning partnership? They are well-positioned for collaboration.
7. **Dani vs. Dan Glasses priority.** Dan Glasses lead, Dani as platform? Or equal?
8. **Cost of "owning the reasoning stack."** HRM-Text-1B fine-tuning is $1,500/run. 3B is $5,000-$10,000/run. Are we ready to spend $50,000-$100,000/year on training compute?

---

## Recommendation summary (TL;DR)

- **6 months:** agentd (Rust) + learnerd (SIA-H harness loop) + memoryd v2 (Infini Memory) + HRM-Danlab-1B v1 + LFM2.5-Embedding swap + privacy dashboard. **Ship a credible desktop v1 with our own reasoning model.**
- **12 months:** SIA-W+H weight loop on HRM-Danlab-1B → 3B + memoryd v3 (MemVerse periodic distillation) + wearable v1.5 (Brilliant Labs Halo + GAP9). **Ship a self-improving wearable.**
- **24 months:** on-device fine-tuning + Dani as a platform + India beachhead. **Ship the first truly private, self-improving, ambient AI.**
- **Never:** scale-the-frontier, foundation model from scratch (until we have to), cloud-rented agent loop, chatbot, privacy compromise.

This is the path. Ship it. 👾
