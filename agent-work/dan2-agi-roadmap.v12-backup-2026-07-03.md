# Dan2 — AGI Roadmap v11 (2026-07-03 06:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-agi-roadmap.md`
> **Scope:** where Danlab should focus over the next 6/12/24 months, grounded in fresh 2026-07-02/03 signals.
> **v11 deltas vs v9:** 1 new Q3 research bet (HRM-Text-1B integration as v1.5 plan-A, displaces LFM2.5-1.2B-Thinking), 1 new Q3 product addendum (Anthropic Dreaming `auto_apply=False` contract enforced at the memoryd write layer), 1 v9 retraction (Mem0 v1.5 promotion paused), 1 v9 elevation (Kokoro-82M as v1.5 plan-A TTS), 1 marketing wedge refresh (Gemma 3 in orbit + HRM-Text-1B combination replaces the v9 Meta-paywall-led narrative as the primary wedge).

## 0. North Star (one sentence)

**Build the open-weights, on-device, auditable, self-improving personal AI stack — glasses first, then everything else.**

The AGI thesis for Danlab is not "build a smarter chatbot." It is **"build the AI that improves itself, on your face, with your data, in your control."** Every roadmap item below is a step toward that. Anything that doesn't serve it, cut.

## 1. The 6/12/24 month plan

### 6 months (by 2026-12-31) — make v1.0 shippable, plant 6 research flags

| Quarter | Theme | Concrete deliverables |
|---|---|---|
| **Q3 2026 (now → Sep 30)** | **Ship the foundation, run 7 research/eval spikes in parallel** | v1.0 cut of Dan Glasses app (Tauri build) + **VisualClaw cascade-gate port** (1.5 weeks) + **Anthropic Dreaming pattern port to openclaw + memoryd with `auto_apply=False` + `session_limit=50` enforced at the memoryd write layer** (1 week) + **OpenLife budget-metabolism addendum to memoryd** (1 week) + **MemDelta protocol runner for memoryd with supersession test set** (1.5 weeks) + **HRM-Text-1B integration into audiod post-processor** (1 week) + Gemma 4 12B spike result + Kokoro-82M evaluation + SIA-W+H paper sketch + EigenCloud TEE security story + **Gemma 3 in-orbit + HRM-Text-1B marketing wedge** + danlab.dev refresh |
| **Q4 2026 (Oct → Dec)** | **SIA-W+H port + v1.5 architecture decision** | SIA-W+H code released on GitHub (MIT, Apache-2.0) + arXiv preprint + 2-page blog post + Gemma 4 12B decision (commit or kill) + Kokoro-82M ship as default for English TTS + MAI-Voice-2 as cloud-bridge for non-English + **HRM-Text-1B shipped to audiod post-producer** + VisualClaw full pattern (hot/cold skill bank) ported to perceptiond + **MemDelta v2 evaluation** (run memoryd again on the protocol to confirm baseline) + **OpenLife 24-week results paper** (if published) + **Gemma 3 in-orbit prompt structure adopted for perceptiond query mode** |

**Definition of done for 6 months:** Dan Glasses v1.0 on a small set of users' faces (early access, max 100 people), SIA-W+H port with reproducible benchmarks, VisualClaw cascade gate live, Anthropic Dreaming pattern live (human-in-the-loop memory updates with `auto_apply=False` and `session_limit=50` enforced at the memoryd write layer), OpenLife budget-metabolism live, MemDelta baseline published (including the supersession test set), HRM-Text-1B shipped to audiod post-processor, Kokoro-82M shipped as v1.5 plan-A TTS, EigenCloud TEE story documented on the site, and one arXiv paper with at least 3 citations within 60 days of release.

### 12 months (by 2027-06-30) — prove the RSI thesis at small scale

| Quarter | Theme | Concrete deliverables |
|---|---|---|
| **Q1 2027 (Jan → Mar)** | **v1.5: unified multimodal (Gemma 4 12B if spike passed) + memory architecture v2** | Gemma 4 12B (or equivalent) shipped on the wearable, replacing the 3-VLM split + bi-temporal memory layer (SARA-style) + agent loop using SIA-W+H policy head + Anthropic Dreaming pattern v2 (no human approval needed for low-stakes updates) + 3 languages live (English + 2 Indian) + **MemDelta v2 protocol adopted as the standard memory eval** |
| **Q2 2027 (Apr → Jun)** | **First "self-improving" demo: agent modifies its own salience policy in real time on a user's face** | Public demo at a workshop (NeurIPS 2026 workshop submission Q3 2026, demo Q4 2026 / Q1 2027) + arXiv paper #2 on the in-the-loop RSI result + 1,000 users on v1.5 + VisualClawArena-style benchmark for our on-device gate + **MemDelta + OpenLife evaluation as the v1.5 memory paper appendix** |

**Definition of done for 12 months:** v1.5 on 1,000 faces, agent demonstrably improves its own salience/embedding policy from user feedback (Anthropic Dreaming + VisualClaw hot/cold + SIA-W+H + OpenLife budget-metabolism all wired), MemDelta baseline beats basic retrieval, two arXiv papers, and the first press cycle that frames Danlab as the open-source RSI counter-narrative to Anthropic Mythos / Recursive Superintelligence / A-Evolve-Training.

### 24 months (by 2028-06-30) — the bet either pays off or doesn't

| Quarter | Theme | Concrete deliverables |
|---|---|---|
| **Q3-Q4 2027** | **Scale to 10,000 users, raise seed/Series A** | 10k active users + €2-5M raised (subject to somdipto's preference on whether to take outside capital) + 5 languages + enterprise pilot (1-3 design partners) + **healthcare sovereign on-prem AI vertical exploration** (Forbes, June 26 2026) |
| **Q1-Q2 2028** | **Generalize beyond glasses** | danlab.dev stack (dani agent + memoryd + toold + ttsd + gated) packaged for non-glasses form factors (Pi-class wearable, home assistant, BCI for accessibility) + arXiv paper #3 on generalization + **physical AI exploration (Atomathic Physical AI 2.0, Orca world model, Active Inference scaling law)** |

**Definition of done for 24 months:** the "open-weights, on-device, auditable, self-improving personal AI" thesis is either validated by adoption (10k+ active users) or invalidated by a better-funded competitor (Anthropic, Google, Meta). Either outcome is fine — both teach us something.

## 2. The 7 research bets (Q3 2026)

These are the bets where the upside is "rewrites the architecture" and the downside is "we learned something in 2 weeks." They run in parallel.

### Bet 1: VisualClaw cascade-gate port (from v8/v9, unchanged — efficiency bet)

**Hypothesis:** VisualClaw (Mervin Praison, June 2026) proves that an on-device cascade gate can drop 98.1% of frames before they reach the VLM, while *improving* accuracy by +15.8% on EgoSchema.

**Spike plan (1.5 weeks, 1 engineer).** Unchanged from v9.

**Go/No-Go gate at end of week 2:** commit to v1.0 = cascade gate (ship the policy head) OR document why we're keeping the current SalienceDetector (with evidence from the spike).

**Cost:** 1.5 engineer-weeks, no GPU spend.

**Upside if it works:** 50× latency reduction in practice (98% of frames dropped at the gate). Battery life goes from 30 min to 4 hours. **This is the single most leveraged engineering bet in v11.**

**Downside if it doesn't:** we have a documented negative result, we keep the current SalienceDetector, no harm done.

### Bet 2: Anthropic Dreaming pattern port (from v9, sharpened in v11 — continual learning bet)

**Hypothesis:** Anthropic's Dreaming API (May 6 2026, beta) is the closed-source shipped product pattern for "agent that improves itself overnight." The `auto_apply=False` default and the `session_limit=50` parameter are the v1.0 safety contract. We port the pattern (not the code) to openclaw + memoryd + Tauri UI.

**Spike plan (1 week, 1 engineer).** v9: 1 week. v11: 1 week, but with the safety contract enforced at the memoryd write layer (defense in depth).

**Go/No-Go gate at end of week 1:** if the memoryd write layer can reject `auto_apply=True` writes, ship to v1.5. If it can't, ship a stub that returns 403 and add the safety enforcement as a v1.5.1 follow-up.

**Cost:** 1 engineer-week, no GPU spend.

**Upside if it works:** the v1.5 self-improving loop is live, and the safety contract is enforced at the lowest layer. MemDelta-compliant.

**Downside if it doesn't:** we ship a stub, add the safety enforcement as a follow-up, no harm done.

### Bet 3: OpenLife budget-metabolism addendum to memoryd (from v9, unchanged — memory architecture bet)

**Hypothesis:** OpenLife (arXiv 2606.31046, June 30 2026) ran 6 LLM agents for 12 weeks in the open. The pattern is "persistence as budget" — every episodic memory has a TTL and an attention cost, and the GC worker runs in the background. We port the pattern to memoryd.

**Spike plan (1 week, 1 engineer).** v9: 1 week. v11: 1 week, but with the v9 OpenLife TTL defaults (24h episodic, ∞ semantic, 7d procedural).

**Go/No-Go gate at end of week 1:** if memoryd handles 1k events/day with the budget-metabolism worker running, ship to v1.5. If it can't, scale back the budget and re-spike.

**Cost:** 1 engineer-week, no GPU spend.

**Upside if it works:** the v1.5 memory architecture matches OpenLife's emergent pattern. The 12-week equilibrium is reachable in 4 weeks.

**Downside if it doesn't:** we ship a simpler version without the GC worker, add it as a v1.5.1 follow-up.

### Bet 4: MemDelta protocol runner for memoryd (from v9, sharpened in v11 — evaluation rigour bet)

**Hypothesis:** MemDelta (arXiv 2606.29914, June 30 2026) is the first controlled evaluation of agent memory. We stand up the protocol as the memoryd evaluation harness, add a supersession test set per the Diagnosing the Memory-Update Gap paper, and commit the results as a baseline.

**Spike plan (1.5 weeks, 1 engineer).** v9: 1 week. v11: 1.5 weeks, but with the supersession test set included.

**Go/No-Go gate at end of week 1.5:** if memoryd hits the MemDelta baseline (47.2% on the verbatim RAG condition, ≥ 47% on the agent self-memory condition), we have a defensible v1.0. If it doesn't, we have a documented regression to fix.

**Cost:** 1.5 engineer-weeks, no GPU spend (CPU-only MiniLM-L6-v2 + SQLite).

**Upside if it works:** v1.0 memoryd is defensible. The "yours, not theirs" wedge has an empirical basis.

**Downside if it doesn't:** we have a documented regression to fix before v1.0.

### Bet 5: **NEW v11**: HRM-Text-1B integration into the audiod post-processor (from v9 plan-B to v11 plan-A — reasoning model bet)

**Hypothesis:** HRM-Text-1B (Sapient, June 2026, Apache-2.0, $1,500 from scratch, 1B params) is the SOTA small-budget reasoning model. The hierarchical reasoning model (HRM) architecture is the algorithmic innovation. We swap HRM-Text-1B into the audiod post-processor (replacing the v9 LFM2.5-1.2B-Thinking placeholder) and use it for the proposed-memory-update step in the Anthropic Dreaming port.

**Spike plan (1 week, 1 engineer).** v9: not in scope (plan-B only). v11: 1 week, direct-swap not benchmark-first.

**Go/No-Go gate at end of week 1:** if HRM-Text-1B runs in <1s on a single CPU thread for a 100-token proposed-memory-update, ship to v1.5. If it doesn't, fall back to LFM2.5-1.2B-Thinking.

**Cost:** 1 engineer-week, $0 (Apache-2.0 weights, CPU-only inference).

**Upside if it works:** the v1.5 self-improving loop has a reasoning core that costs $1,500 to train. The "small-beats-large" thesis is empirically real at 1B scale.

**Downside if it doesn't:** we fall back to LFM2.5-1.2B-Thinking, no harm done.

### Bet 6: **NEW v11**: Kokoro-82M swap-in as v1.5 plan-A TTS (from v9 plan-B to v11 plan-A — TTS bet)

**Hypothesis:** Kokoro-82M (Apache-2.0, 82M params, 100+ languages, on-device) is the SOTA edge TTS per the kveeky.com 2026 review and the bee.devs 45-day test against ElevenLabs/Google/Amazon Polly. We swap Kokoro-82M into ttsd (replacing KittenTTS as the v1.5 default) and keep KittenTTS as the v1.0 default.

**Spike plan (1 week, 1 engineer).** v9: not in scope (plan-B only). v11: 1 week, direct-swap not benchmark-first.

**Go/No-Go gate at end of week 1:** if Kokoro-82M matches KittenTTS on the wizard smoke test (TTS preview plays in <2s), ship to v1.5. If it doesn't, fall back to KittenTTS.

**Cost:** 1 engineer-week, $0 (Apache-2.0 weights, CPU-only inference).

**Upside if it works:** the v1.5 TTS is 100+ languages on-device, beats ElevenLabs on the 45-day test, and costs $0 to ship.

**Downside if it doesn't:** we keep KittenTTS, no harm done.

### Bet 7: Gemma 3 in-orbit prompt structure adopted for perceptiond query mode (NEW v11 — VLM bet)

**Hypothesis:** The Gemma 3 in-orbit prompt structure (per the TechCrunch June 15 2026 article on Loft Orbital Yam-9, NASA JPL, April 2026) is the closest published analog to our `perceptiond.set_mode("active")` query pattern. We benchmark LFM2.5-VL-450M with the in-orbit prompt structure as a Q3 v1.5 task.

**Spike plan (1 week, 1 engineer).** v9: not in scope. v11: 1 week, benchmark-only.

**Go/No-Go gate at end of week 1:** if LFM2.5-VL-450M with the in-orbit prompt structure hits ≥80% accuracy on a 50-question triage test set, ship the prompt structure to v1.5. If it doesn't, keep the current `perceptiond.py` prompt.

**Cost:** 1 engineer-week, $0 (CPU-only MiniLM-L6-v2 + LFM2.5-VL-450M).

**Upside if it works:** the v1.5 perceptiond has a space-grade prompt structure.

**Downside if it doesn't:** we keep the current prompt, no harm done.

## 3. The marketing wedge v11 (refreshed from v9)

**v9:** "Yours, not theirs" — privacy → ownership → openness.

**v11:** "Yours, not theirs" + **"$1,500 reasoning model + space-grade VLM"** — the new sequence is privacy → ownership → openness → **"trained for the cost of a used car, in space."**

The Gemma 3 in orbit (April 2026, Loft Orbital Yam-9, NASA JPL) is the strongest possible external validation of the on-device VLM thesis. The HRM-Text-1B (Sapient, $1,500 from scratch, Apache-2.0) is the strongest possible external validation of the open-weights + small-budget reasoning model thesis. **The combination is the v11 marketing wedge.**

The "yours, not theirs" message is now a public, citable, viral fact (Meta paywalls, Anthropic Mythos 5 gating, healthcare sovereign on-prem, Microsoft Scout on OpenClaw). The new addition is the **"trained for the cost of a used car, in space"** message — and it is the most differentiated marketing claim in the v11 stack.

## 4. The v11 → v12 watch list

- **Anthropic Mythos 5 graduates from Glasswing to broader release** → re-evaluate open-weights posture
- **OpenLife agents reach 6 months runtime** → paper publication follow-up
- **MemDelta v2 (more model families, more tasks)** → re-evaluate memoryd evaluation rigour
- **Healthcare sovereign on-prem AI partnership RFPs surface** → partnership opportunity
- **GPT 5.6 public release date set** → competitive check
- **Orca world model paper cites our work** → research signal
- **Google ships Gemma 4 4B Unified** → re-evaluate 3-VLM split
- **Microsoft announces OpenClaw as a paid product** → fork or follow decision
- **Anthropic Dreaming API graduates from beta to GA** → re-evaluate the closed-source competitor timeline
- **HRM-Text-1B v2 ships with 3B params** → re-evaluate the v1.5 reasoning model choice
- **Gemma 3 in-orbit produces a published case study** → replicate the prompt structure on LFM2.5-VL-450M
- **Kokoro-82M v2 ships with 30+ languages on-device** → re-evaluate the v1.5 TTS choice

**End of v11 roadmap.**
