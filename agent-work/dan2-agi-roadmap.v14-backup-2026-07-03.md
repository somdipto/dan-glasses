# Dan2 — AGI Roadmap v14 (2026-07-03 04:00 UTC / 09:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-agi-roadmap.md`
> **Scope:** where Danlab should focus over the next 6/12/24 months, grounded in fresh 2026-07-03 signals.
> **Backup of v13:** `dan2-agi-roadmap.v13-backup-2026-07-03.md`
> **v14 deltas vs v13 (4 changes):** 1 Q3 W2 W3 W4 additions (Memora storage/retrieval split, Hermes Agent research spike, Apertus v1.1 verification spike, PR-review "X% AI-generated" tag), 1 Q3 marketing addition (BBC-reported Meta paywall + Sonnet 5 cost multiplier as two-anchor empirical narrative), 1 Q4 vertical addition (sovereign-on-prem EU via Apertus), 1 retargeting of v1.5 memoryd v1.5 architecture from "bi-temporal (SARA-style)" to "Memora storage/retrieval split."

## 0. North Star (one sentence)

**Build the open-weights, on-device, auditable, self-improving personal AI stack — glasses first, then everything else.**

The AGI thesis for Danlab is not "build a smarter chatbot." It is **"build the AI that improves itself, on your face, with your data, in your control."** Every roadmap item below is a step toward that. Anything that doesn't serve it, cut.

## 1. The 6/12/24 month plan

### 6 months (by 2026-12-31) — make v1.0 shippable, plant 9 research/eval spikes

| Quarter | Theme | Concrete deliverables |
|---|---|---|
| **Q3 2026 (now → Sep 30)** | **Ship the foundation, run 9 research/eval spikes in parallel** | v1.0 cut of Dan Glasses app (Tauri build) + **VisualClaw cascade-gate port** (1.5 weeks) + **Anthropic Dreaming pattern port to openclaw + memoryd with `auto_apply=False` + `session_limit=50` enforced at the memoryd write layer** (1 week) + **OpenLife budget-metabolism addendum to memoryd** (1 week) + **MemDelta protocol runner for memoryd with supersession test set** (1.5 weeks) + **Karpathy 10-rule CLAUDE.md adopted as the openclaw contract** (1 day) + **Red Queen moving-judge pattern port to danlab-multimodal** (2 weeks) + **Gemma 3 in-orbit prompt structure adopted for perceptiond query mode** (1 week) + **Ollie gaze-informed proactive pattern port to proactived v1** (2 weeks) + **HRM-Text-1B integration into audiod post-processor** (1 week) + **Qwen3-TTS evaluation as v1.5 TTS plan-A** (1 week) + **Chatterbox voice-cloning evaluation as v1.5 personalization** (2 weeks) + **GLM-5.2 capability verification spike** (1 day, v13 add) + **INT8 LFM2.5-VL-450M quantization spike** (1 week, v13 add) + **sovereign-on-prem vertical spike** (1 engineer-week, v13 add) + EigenCloud TEE security story + danlab.dev refresh + **NEW v14: Memora storage/retrieval split port to memoryd v1.5** (2 weeks) + **NEW v14: Hermes Agent research spike** (1 week, openclaw agent-framework plan-B) + **NEW v14: Apertus v1.1 4B verification spike for EU data-residency** (1 day) + **NEW v14: openclaw PR-review "X% AI-generated" tag** (3 days) + **NEW v14: BBC + Sonnet 5 cost multiplier marketing wedge live on danlab.dev** |
| **Q4 2026 (Oct → Dec)** | **Memora storage/retrieval split ship + EU variant + v1.5 architecture decision** | Memora port complete + Apertus EU variant live + 2-page blog post + Gemma 4 12B decision (commit or kill) + **HRM-Text-1B shipped to audiod post-producer** + **Red Queen moving-judge live in danlab-multimodal** + **Ollie gaze-informed proactive live in proactived v1** + VisualClaw full pattern (hot/cold skill bank) ported to perceptiond + **MemDelta v2 evaluation** + **OpenLife 24-week results paper** (if published) + **Karpathy 10-rule openclaw contract live** + **BBC + Sonnet 5 cost multiplier marketing wedge live on danlab.dev** + **sovereign-on-prem vertical spike: 1 healthcare design partner** (Forbes, June 26 2026) + **Hermes Agent v1.5 plan-B agent-framework live in openclaw** |

**Definition of done for 6 months:** Dan Glasses v1.0 on a small set of users' faces (early access, max 100 people), Red Queen moving-judge live, Ollie gaze-informed proactive live, VisualClaw cascade gate live, Anthropic Dreaming pattern live (human-in-the-loop memory updates with `auto_apply=False` and `session_limit=50` enforced at the memoryd write layer), OpenLife budget-metabolism live, MemDelta baseline published (including the supersession test set), HRM-Text-1B shipped to audiod post-processor, Qwen3-TTS shipped as v1.5 plan-A TTS, Chatterbox shipped as v1.5 voice-cloning path, Karpathy 10-rule openclaw contract live, **Memora storage/retrieval split live in memoryd v1.5**, **Hermes Agent v1.5 plan-B agent-framework live**, **Apertus v1.1 4B EU variant live**, **openclaw PR-review "X% AI-generated" tag live**, **BBC + Sonnet 5 cost multiplier marketing wedge live on danlab.dev**, EigenCloud TEE story documented, and one arXiv paper with at least 3 citations within 60 days of release.

### 12 months (by 2027-06-30) — prove the RSI thesis at small scale

| Quarter | Theme | Concrete deliverables |
|---|---|---|
| **Q1 2027 (Jan → Mar)** | **v1.5: unified multimodal (Gemma 4 12B if spike passed) + memory architecture v2** | Gemma 4 12B (or equivalent) shipped on the wearable, replacing the 3-VLM split + **Memora v2: bi-temporal + storage/retrieval split** (combine the v12 SARA-style plan with the v14 Memora plan) + agent loop using SIA-W+H policy head + Anthropic Dreaming pattern v2 (no human approval needed for low-stakes updates) + **proactived v1 with Ollie gaze-informed pattern on real users' faces** + **MemDelta v2 protocol adopted as the standard memory eval** |
| **Q2 2027 (Apr → Jun)** | **First "self-improving" demo: agent modifies its own salience policy in real time on a user's face** | Public demo at a workshop (NeurIPS 2026 workshop submission Q3 2026, demo Q4 2026 / Q1 2027) + arXiv paper #2 on the in-the-loop RSI result + 1,000 users on v1.5 + VisualClawArena-style benchmark for our on-device gate + **Red Queen held-out ground-truth set as the v1.5 evaluation rigour floor** + **MemDelta + Memora v2 evaluation as the v1.5 memory paper appendix** |

**Definition of done for 12 months:** v1.5 on 1,000 faces, agent demonstrably improves its own salience/embedding policy from user feedback (Anthropic Dreaming + Red Queen moving judge + VisualClaw hot/cold + SIA-W+H + OpenLife budget-metabolism + Memora storage/retrieval split all wired), MemDelta baseline beats basic retrieval, two arXiv papers, and the first press cycle that frames Danlab as the open-source RSI counter-narrative to Anthropic Mythos / Recursive Superintelligence / A-Evolve-Training / Microsoft Memora.

### 24 months (by 2028-06-30) — the bet either pays off or doesn't

| Quarter | Theme | Concrete deliverables |
|---|---|---|
| **Q3-Q4 2027** | **Scale to 10,000 users, raise seed/Series A** | 10k active users + €2-5M raised (subject to somdipto's preference on whether to take outside capital) + 5 languages + enterprise pilot (1-3 design partners, including 1 healthcare design partner from Q4 2026 spike) + **healthcare sovereign on-prem AI vertical exploration** (Forbes, June 26 2026) + **EU sovereign vertical via Apertus v1.1** |
| **Q1-Q2 2028** | **Generalize beyond glasses** | danlab.dev stack (dani agent + memoryd + toold + ttsd + gated) packaged for non-glasses form factors (Pi-class wearable, home assistant, BCI for accessibility) + arXiv paper #3 on generalization + **physical AI exploration (Atomathic Physical AI 2.0, Orca world model, Active Inference scaling law)** |

**Definition of done for 24 months:** the "open-weights, on-device, auditable, self-improving personal AI" thesis is either validated by adoption (10k+ active users) or invalidated by a better-funded competitor (Anthropic, Google, Meta, Microsoft). Either outcome is fine — both teach us something.

## 2. The 9 research bets (Q3 2026)

These are the bets where the upside is "rewrites the architecture" and the downside is "we learned something in 2 weeks." They run in parallel.

### Bet 1: **v12 (plan-A)**: Red Queen moving-judge pattern port to danlab-multimodal (self-improving bet)

**Hypothesis:** The Red Queen Gödel Machine (arXiv:2606.26294v1, June 24 2026, Cambridge + NVIDIA) proves that co-evolving the agent AND the evaluator under a fixed ground-truth anchor produces 1.35–1.72× fewer steps than HGM-H on code/math benchmarks, and reduces the 1.91× AI-paper over-acceptance bias in static judges to ~1.0× with a moving judge. **We port the moving-judge pattern to danlab-multimodal: a held-out, human-curated, weekly-rotated ground-truth set that re-scores the last 7 days of perceptiond descriptions.**

**v14 sharpening:** the held-out ground truth set is a memoryd write, not a perceptiond-local file. The ground truth is a procedural memory with TTL=7 days, rotated by somdipto, queried via the standard memoryd API. Single source of truth.

**Spike plan (2 weeks, 1 engineer).**

**Go/No-Go gate at end of week 2:** if the held-out ground-truth set catches ≥1 description per week that the agent mis-scored, ship to v1.0. If it catches 0, the agent is already well-calibrated and the moving judge is unnecessary.

**Cost:** 2 engineer-weeks + somdipto's time on the held-out set (50 questions/week, ~30 min/week).

**Upside if it works:** v1.0 danlab-multimodal is calibrated against a held-out human-curated ground-truth set. The 1.91× bias-correction result is the v12 safety case for the agent loop. The MemDelta + Red Queen evaluation is the v1.5 paper appendix.

**Downside if it doesn't:** we have a documented negative result, we keep the current static judge, no harm done.

### Bet 2: **NEW v14 (plan-A)**: Microsoft Memora storage/retrieval split port to memoryd v1.5

**Hypothesis:** Microsoft Memora (July 2026) decouples "what is stored" (rich memory content) from "how it is retrieved" (lightweight abstractions and cue anchors). Claimed: 98% context token reduction with no accuracy loss. **We port the storage/retrieval split to memoryd: rich storage tier (raw memories, raw held-out ground truth, raw agent proposals) + lightweight retrieval tier (cue anchors, summaries). Cue anchors computed at write time. Retrieval is a two-hop: cue-level cosine first → if cue matches, surface the full rich memory.**

**v14 sharpening:** the MemDelta v9 finding ("agent self-memory 42% < basic RAG 47%") is the problem statement; Memora is Microsoft's answer. The `auto_apply=False` contract binds at the *storage* layer, not the *retrieval* layer. Human approves at storage write; retrieval is automatic.

**Spike plan (2 weeks, 1 engineer).**

**Go/No-Go gate at end of week 2:** if the Memora-pattern memoryd matches basic RAG on the MemDelta test set, ship to v1.5. If it underperforms, fall back to a Mem0 v1.5 promotion.

**Cost:** 2 engineer-weeks.

**Upside if it works:** v1.5 memoryd beats basic RAG on MemDelta (closes the v9 finding), 98% context token reduction (matches the Microsoft claim), and the `auto_apply=False` contract is structurally enforced at the storage layer.

**Downside if it doesn't:** we have a documented negative result, we keep the current single-tier MiniLM-L6-v2, no harm done.

### Bet 3: **NEW v14 (research)**: Hermes Agent plan-B research spike

**Hypothesis:** Hermes Agent (Nous Research, MIT, June 2026) is an open-source agent framework that supports ChatGPT subscription integration. **We evaluate Hermes as the v1.5 plan-B agent-framework if the SIA-W+H port stalls. SIA-W+H remains plan-A.**

**Spike plan (1 week, 1 engineer).** Research-only: read the Hermes spec, evaluate the agent loop, evaluate the `auto_apply=False` contract support, evaluate the cost (SIA-W+H is $200-500/mo cloud GPU; Hermes is local).

**Go/No-Go gate at end of week 1:** if Hermes supports the `auto_apply=False` contract and runs locally, keep as plan-B. If not, drop.

**Cost:** 1 engineer-week.

**Upside if it works:** v1.5 has a fallback agent-framework if SIA-W+H port stalls. Hermes is MIT, open-source, runs locally. Mirendil and Memora are closed-source, not portable.

**Downside if it doesn't:** we have a documented evaluation, we keep SIA-W+H as the only plan-A.

### Bet 4: **NEW v14 (research)**: Apertus v1.1 4B verification spike for EU data-residency

**Hypothesis:** Apertus v1.1 4B Instruct (Swiss AI / EPFL, June 29 2026) is an open-weights 4B instruction-tuned model with EU-grade data compliance. **We evaluate Apertus as the v1.5 audiod post-processor alternative for EU users with EU data-residency requirements. HRM-Text-1B remains plan-A; Apertus is plan-B for EU.**

**Spike plan (1 day, 1 engineer).** Verification: read the spec, evaluate the data-residency claims, evaluate the quality vs HRM-Text-1B on a 100-question test set.

**Go/No-Go gate at end of day 1:** if Apertus is competitive with HRM-Text-1B on the test set AND the data-residency claims are auditable, add as plan-B for EU. If not, drop.

**Cost:** 1 engineer-day.

**Upside if it works:** v1.5 has an EU data-residency variant. Healthcare vertical + EU sovereign vertical + Apertus is a credible combo.

**Downside if it doesn't:** we have a documented evaluation, we keep HRM-Text-1B as the only audiod post-processor.

### Bet 5: **NEW v14 (defense)**: openclaw PR-review "X% AI-generated" tag

**Hypothesis:** The Godot Foundation banned AI-generated PRs on July 2 2026 ("We can't trust heavy users of AI to understand their code enough to fix it"). **We add a "X% AI-generated" tag to the openclaw PR-review tool. Defense in depth.**

**Spike plan (3 days, 1 engineer).** Implementation: detect LLM-style code patterns (low entropy, canonical variable names, missing edge cases), score 0-100%, surface in the PR review.

**Go/No-Go gate at end of day 3:** if the detector runs in <500ms per PR and correlates with human review, ship. If not, drop.

**Cost:** 3 engineer-days.

**Upside if it works:** openclaw PR-review is the first agent-runtime with an "X% AI-generated" tag. Defense against the v14 Godot signal.

**Downside if it doesn't:** we have a documented negative result, no harm done.

### Bet 6: **v13 (plan-A)**: GLM-5.2 capability verification spike (research bet)

**Hypothesis:** GLM-5.2 (Z.ai, MIT, late June 2026) is the first publicly-available Mythos-class open-weights model. **We verify whether GLM-5.2 can run on the Redax (aarch64 wearable reference). If yes, Mythos-class text reasoning is reachable on a $349 device.**

**Spike plan (1 day, 1 engineer).** Verification: download GLM-5.2, attempt to run on a simulated aarch64 environment, measure latency and memory.

**Go/No-Go gate at end of day 1:** if GLM-5.2 runs on aarch64 with acceptable latency, add to v1.5 shortlist behind HRM-Text-1B. If not, drop.

**Cost:** 1 engineer-day.

**Upside if it works:** the open-weights wedge becomes production-credible. Mythos-class text reasoning on a $349 device is a marketing fact.

**Downside if it doesn't:** we have a documented evaluation, we keep HRM-Text-1B as the only audiod post-processor.

### Bet 7: **v13**: INT8 LFM2.5-VL-450M quantization spike (RAM cost crisis response)

**Hypothesis:** RAM prices +40-50% Q3 2026, +30% Q4 2026 (TechSpot, Jefferies). **We quantize LFM2.5-VL-450M from Q4_0 to INT8 to absorb the RAM price spike. Q4_0 is the v1.0 default; INT8 is the v1.0 thermal-fallback.**

**Spike plan (1 week, 1 engineer).** Implementation: convert LFM2.5-VL-450M-Q4_0 to INT8, measure quality loss on a 100-image test set, measure memory savings.

**Go/No-Go gate at end of week 1:** if INT8 quality is within 2% of Q4_0, ship as v1.0 thermal-fallback. If not, drop.

**Cost:** 1 engineer-week.

**Upside if it works:** v1.0 BOM is smaller, thermal headroom is larger, and the Q4 2026 RAM price spike is partially absorbed.

**Downside if it doesn't:** we have a documented evaluation, we keep Q4_0 as the only quant.

### Bet 8: **v13**: Sovereign-on-prem vertical spike (Palantir+NVIDIA market-validated)

**Hypothesis:** Palantir + NVIDIA Nemotron sovereign engine (June 29 2026) validates open-weights on-prem at the federal/vertical level. **We add a "sovereign vertical" Q4 2026 spike for healthcare/defense verticals, leveraging the EigenCloud TEE security story.**

**Spike plan (1 engineer-week, Q4 W1-W2).** Discovery: 1 healthcare design partner, 1 federal design partner.

**Go/No-Go gate at end of Q4 W2:** if a healthcare design partner signs an MSA, ship to v1.5 vertical offering. If not, defer to 2027.

**Cost:** 1 engineer-week.

**Upside if it works:** v1.5 has a vertical offering. Palantir+Nemotron is the market-validated template, EigenCloud TEE + open-weights stack is our co-positioning.

**Downside if it doesn't:** we have a documented discovery effort, no harm done.

### Bet 9: **v13**: Marketing wedge refresh (BBC + Sonnet 5 cost multiplier)

**Hypothesis:** The BBC reported the Meta Conversation Focus $19.99/mo paywall on July 2 2026, AND Anthropic Sonnet 5 is 5-57x more expensive than GLM-5.2 / Kimi-K2.6 / DeepSeek-V4-Pro (X coverage, late June 2026). **We refresh the v1.0 marketing lead to a two-anchor empirical narrative: (1) Meta paywalls $19.99/mo for 15hr (BBC), (2) Anthropic Sonnet 5 is 5-57x more expensive than the open-weights alternatives. Combined with Apple $1,200+ upgrade + Anthropic Mythos 5 $30K catch, this is a four-anchor empirical marketing narrative.**

**Spike plan (1 day, 1 engineer + somdipto review).** Implementation: update danlab.dev marketing pages with the BBC link + the cost multiplier table.

**Go/No-Go gate at end of day 1:** if somdipto approves the BBC + cost multiplier narrative, ship. If not, revert to v13 Meta + Apple lead.

**Cost:** 1 engineer-day.

**Upside if it works:** v1.0 marketing is now a four-anchor empirical narrative, not a slogan. The BBC link is citable, the cost multiplier is quantified.

**Downside if it doesn't:** we have a documented marketing review, no harm done.
