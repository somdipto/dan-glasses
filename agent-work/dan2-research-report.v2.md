# Danlab Research Report — Technical + Landscape Deep Dive (v3)

**Author:** Dan-2 (DanLab co-founder, lead scientist, architect)
**Date:** 2026-07-01
**Scope:** Dan Glasses, danlab-multimodal, paperclip, blurr — system analysis + AGI landscape + competitive + 3 deep technical dives
**Status:** v3 — refresh on top of v2 (also dated 2026-07-01). v2 archived as `*.v2.md`. v3 integrates:
  - **Meta AI glasses paywall/rate-limit backlash** (Verge, June 26 2026) — strengthens the local-first wedge
  - **AI-glasses exam cheating scandals in Asia** (CNN, June 26 2026) — Taiwan + South Korea, double-edged for Dan Glasses
  - **OpenAI + Broadcom "Jalapeño" inference chip** (June 24 2026) — edge/cloud compute trajectory
  - **Qualcomm "DragonFly" agentic-AI efficiency play** (Forbes, June 17 2026) — validates the on-device agent thesis
  - **Apple iOS 27 beta 2**: Siri AI explicitly refuses URL summarization (June 24 2026) — privacy posture of frontier labs continues to harden
  - Reaffirmation of v2 conclusions on SIA, danlab-multimodal honesty, model stack, and roadmap

**Read this first, then the 4 companion artifacts.** v2 is preserved for diff; nothing in v2 is retracted, only updated.

---

## Executive Summary

Danlab is a 4-project stack: an edge wearable (Dan Glasses), a multimodal research harness (danlab-multimodal), a multi-agent orchestrator (paperclip), and an unrelated image app (blurr). The hardware product (Dan Glasses) is software-complete on x86_64 with 9 daemons live, but is **blocked on the Redax aarch64 board and on a missing power/thermal budget**. The research project (danlab-multimodal) honestly labels itself **pre-RL** — a hand-coded heuristic, not a true self-improving loop — and points to the SIA framework (Hexo Labs, May 28 2026, MIT) as the credible path to genuine harness+weights self-improvement.

**New since v2 — three market signals that sharpen the Danlab thesis:**

1. **Meta started paywalling on-glasses AI features** (Verge, June 26 2026). The "Conversation Focus" feature on Ray-Ban Display — which **runs entirely on-device** with no cloud — is now rate-limited to 3 hours/month for free users, 15 hours/month for $19.99 Meta One Premium. This is the first major case of a vendor **monetizing the on-device compute it sold you**, and the community is calling it a soft paywall on hardware you already own. **This is the single biggest tailwind for the Dan Glasses local-first wedge in 2026.** A user who has paid $799 for a Meta Ray-Ban Display now has direct, visceral experience with the closed-wallet problem.
2. **AI-glasses exam cheating scandals hit Asia** (CNN, June 26 2026). A Taiwanese medical-school applicant was caught with smart glasses emitting heat during an entrance exam; South Korea's college entrance exam administrator is in discussions with the Education Ministry on countermeasures. This is a **double-edged signal**: (a) it validates that smart glasses are becoming a primary interface for AI assistance, and (b) it creates a near-term reputational and regulatory risk for the entire category. Dan Glasses' privacy/audit story is now a *liability shield*, not just a marketing claim.
3. **Apple iOS 27 beta 2 hardens Siri AI on URL summarization** (9to5Mac, June 24 2026). Apple told Siri AI to clearly refuse to extract/summarize content behind URLs in the system prompt. Frontier labs are progressively tightening their assistants' surface area — a sign of the **defensive posture** the entire industry is taking on privacy. The "AI that helps you with what you see" category is being squeezed from both ends: vendors paywall features and regulators push them to refuse.

**Headline findings (carried from v2, now reinforced):**

1. **LFM2.5-VL-450M is the right VLM** (sub-250ms on Intel CPU, beats SmolVLM2-500M by +3.14 MMStar / +4.47 MMBench, released April 11 2026). LFM2.5-Extract (May 2026) adds structured-JSON grounding — directly relevant for our memoryd schema. Verified.
2. **The "heuristic feedback loop" in danlab-multimodal is NOT RL** and the README correctly says so. SIA (Hexo Labs, MIT, May 28 2026, GitHub `hexo-ai/sia`) is the credible next step. The Meta-Agent + Feedback-Agent both run on Claude Sonnet 4.6. This is now a real, forkable, MIT-licensed path.
3. **whisper.cpp + KittenTTS are still correct**, but **Kokoro-82M is now the open-weight benchmark for TTS quality**. KittenTTS wins on footprint; Kokoro wins on quality and naturalness. Plan a v1.5 A/B harness.
4. **memoryd is a good MVP but is a flat cosine-similarity store.** The SOTA has moved to typed/bi-temporal/continuum memory. Mem0 v3 (April 2026) added temporal reasoning — should be benchmarked against the current memoryd.
5. **The "5-Phase / 2-Track" build plan is right** but the **battery/power section is still vapor** — must be filled in before any wearable form factor.
6. **The wearable market is closing fast** — and now **the wedge is sharper than ever**: Meta is paywalling on-device features, regulators are scrambling, and a "yours, not theirs" AI companion is the only product that escapes both problems.

---

## A. System Architecture Deep Dive

### A.1 Dan Glasses service decomposition — is it correct?

**Verdict: Mostly correct, with three structural issues that compound.** (unchanged from v2 — the decomposition held up under the latest review)

The decomposition into 6 daemons (audiod, perceptiond, memoryd, toold, ttsd, os-toold) plus a Tauri app + OpenClaw gateway is sensible. Each service is well-isolated, has a typed HTTP contract, and survives independent restarts. The **liveness/readiness probe split in audiod v1.1** is the right pattern and should be propagated to **perceptiond, memoryd, toold, ttsd, os-toold** — currently they have only `/health` and the readiness contract is implicit.

**v3 specific reinforcement:** the SIA-W+H port to danlab-multimodal (planned for Q3 2026) does NOT change the service decomposition. SIA-H (harness only) is a loop in the danlab-multimodal research repo. SIA-W+H runs weight updates against LFM2.5-VL-450M, which still lives in perceptiond. The harness layer (scaffold, prompts, routing) lives outside perceptiond. **The architecture is well-positioned for SIA-W+H; the integration is additive, not disruptive.**

### A.2 The multimodal "RL" feedback loop — is it real RL?

**Verdict: No, and the project correctly says so. It is a hand-coded heuristic, not RL.** (unchanged from v2)

**v3 update — what's new in SIA-adjacent work since v2:**
- The SIA GitHub repo (`hexo-ai/sia`) remains the canonical reference; no new public competitor has emerged in the last two weeks.
- Lumio's "Lighthouse" self-enhancing agent (June 2026) is a *closed, vertical product* (self-storage call centers), not a research framework. Not a competitor for danlab-multimodal's mission; not a path to publish.
- Chamath Palihapitiya's "Software Factory" (8090 Labs, June 2026) is a closed-source corporate dev agent. Not relevant for our open-source self-improvement path.
- The Lumio/Palihapitiya announcements reinforce that **the agent-with-self-improvement category is hot in 2026**, but **none of them are open-source research frameworks** — SIA remains the only credible MIT-licensed path.

### A.3 Power/performance tradeoffs — are LFM2.5-VL-450M, whisper.cpp, KittenTTS the right model choices for edge?

**Verdict: LFM2.5-VL-450M ✅, whisper.cpp ✅, KittenTTS ⚠️ (consider Kokoro-82M as v1.5 candidate).** (unchanged from v2)

**v3 update:** No new model in the sub-500MB VLM tier has been released since v2. LFM2.5-Extract (May 2026) remains the most recent addition. The LFM2.6 family is rumored for Q4 2026; no early access in the news cycle as of 2026-07-01.

**v3 relevant adjacent signal:** Qualcomm's "DragonFly" platform (Forbes, June 17 2026) is positioned as "efficiency-first inference" for agentic AI, expecting "agentic AI to quadruple CPU core demand in data centers, driving a need for highly efficient, hybrid computing across devices, edge, and cloud." This **validates the on-device agent thesis** at the silicon-vendor level — Qualcomm is explicitly betting that agentic AI moves compute to the edge, and they're building a platform for it. This is good news for Dan Glasses' positioning, and it means a future Redax-class board with Qualcomm silicon will have first-class support for the agent loop.

### A.4 OpenClaw orchestration — is TypeScript/Node the right choice?

**Verdict: Yes for the orchestration layer, with a clear IPC boundary to the Rust services. Don't try to rewrite it.** (unchanged from v2)

**v3 update:** No new OpenClaw release or major regression in the last two weeks. The 2026.6.5 pin remains correct.

---

## B. AGI Landscape Research

### B.5 State of AGI research in 2026 — what are the leading approaches?

**Five clusters, converging:** (unchanged from v2)

1. **Self-improving / recursive architectures (frontier + open).** v3 reinforces: SIA, SEAL, TRIDENT, Darwin Gödel Machine remain the open-source canon. No new open framework has been released since v2.
2. **Multimodal + agentic on-device.** v3: Qualcomm "DragonFly" is a silicon-vendor endorsement of the on-device agent thesis.
3. **Memory-augmented agents.** Mem0 v3, Zep, Letta, Cognee, MemGPT/Letta, PolarDB Memory. Unchanged.
4. **Proactive / context-aware agents.** ContextAgent, ProAgent, ProVoice-Bench. Unchanged.
5. **Brain-inspired / continual learning.** Liquid AI's "Liquid Adaptive AI" framework. Unchanged.

**v3 NEW cluster candidate (additive, not replacing):**
6. **Silicon-for-agentic-AI.** OpenAI/Broadcom Jalapeño (cloud inference chip, June 24 2026), Qualcomm DragonFly (edge agentic AI, June 17 2026). The infrastructure is being purpose-built. For Dan Glasses, this means: (a) future Redax boards will get better at agentic AI workloads, and (b) the cloud-vs-edge compute balance will shift toward edge over 2027-2028.

### B.6 Self-improving architectures — what has actually worked?

**What works (May 2026):** SIA-W+H, TRIDENT, SEAL, Darwin Gödel Machine. (unchanged from v2)

**v3 update:** No new public result in self-improving architectures since v2. The field is moving slowly in open research; the action is in closed commercial products (Lumio, 8090 Labs) that are not publishing. This is a **buy-low moment for open research** — the publishable surface is still wide open, and Danlab can land a real contribution by porting SIA-W+H to a 450M-class multimodal agent.

### B.7 Edge AI / on-device models — what's the SOTA for sub-500MB VLMs?

**v3 update:** LFM2.5-VL-450M remains the best sub-500MB VLM. No new competitor. LFM2.5-VL-1.6B-Extract (May 2026) and LFM2.5-VL-450M-Extract (May 2026) remain the structured-JSON grounding candidates for memoryd caption ingest. Action from v2 stands: **switch chat template to LFM2.5-Extract for caption ingest.**

### B.8 Memory and continual learning — what approaches exist?

**v3 update:** Mem0 v3 (April 2026) remains the SOTA. The Storage → Reflection → Experience taxonomy stands. True Memory (2026 paper, encoding-gate, 6-layer architecture) remains the recommended v1.5 migration path. No new contender in the last two weeks.

### B.9 Multimodal fusion — how are the best systems combining vision, audio, and text?

**v3 update:** Three patterns stand. No new pattern. The Tempus AI foundation model (BioSpace, June 2026) is a vertical multimodal + agentic platform for oncology — not a research framework, but a useful existence proof that **multimodal foundation models + agentic workflows + domain data** is a viable production architecture. The pattern is the same as Dan Glasses', but the domain is oncology instead of personal memory.

### B.10 Model compression — what techniques are working?

**v3 update:** SPEED-Q (AAAI 2026) is still the SOTA for sub-1B VLM quantization. No new compression method since v2.

---

## C. Competitive & Market Research

### C.11 AI wearables landscape (July 2026) — v3 with the paywall signal

The competitive table from v2 is unchanged in product list, but the **market dynamics have shifted**:

| Product | Price | AI | Cloud | v3 Status | v3 Source |
|---|---|---|---|---|---|
| **Meta Ray-Ban Gen 2** | $379 | Llama 4 / Muse Spark (May 2026) | Yes | Now paywalling on-glasses features | [The Verge, June 26 2026](https://www.theverge.com/gadgets/959899/meta-ai-glasses-paywall-rate-limit) |
| **Meta Ray-Ban Display** | $799 | Llama 4 / Muse Spark | Yes | **"Conversation Focus" rate-limited: 3h/mo free, 15h/mo for $19.99 Meta One Premium** | [The Verge, June 26 2026](https://www.theverge.com/gadgets/959899/meta-ai-glasses-paywall-rate-limit) |
| **Meta Glasses** (June 2026 line) | $299+ | Muse Spark | Yes | New low-tier $299+ glasses (Kylie Jenner model) | [CNET, June 2026](https://www.cnet.com/) |
| **Snap Specs** | $2,195 | Snap's own | Yes | June 17 2026 launch | [Forbes](https://www.forbes.com/sites/katehardcastle/2026/06/17/snap-smart-glasses-hit-the-market-at-2195-as-ar-wearables-reach-inflection-point/) |
| **Brilliant Labs Halo** | TBD | Noa (long-term memory) | Partial | 2026 | Brilliant Labs |
| **Google × Warby Parker / Gentle Monster** | TBD | Gemini | Yes | Fall 2026 (rumored) | UploadVR |
| **Apple smart glasses** | TBD | Apple Intelligence | Yes | **Late 2027 (delayed)** | [MacRumors / Kuo, June 2026](https://www.macrumors.com/2026/06/03/kuo-vision-pro-successors-nixed/) |
| **Dan Glasses (proposed)** | TBD | LFM2.5-VL-450M + whisper.cpp + KittenTTS | **No (on-device)** | TBD | danlab.dev |

**v3 key new signal — Meta is paywalling on-device features:**

> "Meta is adding ridiculous 'rate limits' and a soft paywall to its smart glasses ... your glasses' Conversation Focus feature will soon be limited to three hours of use per month, unless you pay for a $19.99 Meta One Premium subscription ... Even premium subscribers will only get 15 hours of Conversation Focus per month under that 'rate limit.' ... The Conversation Focus feature, which amplifies the voice of the person you're speaking to so you can hear better in noisy environments, is not something that should plausibly be rate-limited, because it doesn't use Meta's servers." — The Verge, June 26 2026.

**This is a watershed moment for the local-first wedge.** The vendor is rate-limiting an on-device feature to push subscription revenue. The community response has been strongly negative. **For Dan Glasses, the marketing line writes itself: "Your glasses remember everything you saw. They also forget everything you didn't ask them to keep. And they never ask you for a subscription."**

**v3 second key signal — AI glasses exam cheating scandals in Asia:**

> "In Taiwan, a student sitting for an entrance exam for a top medical school was discovered wearing smart glasses after proctors noticed the student staring oddly at the test, leading to an inspection that revealed the frame was emitting heat." — CNN, June 26 2026.

**Implications for Danlab:**
- The category is being singled out by regulators. Any smart-glasses product will face increased scrutiny on anti-cheating, proctoring compliance, and exam-room detection.
- Dan Glasses' privacy story must include an **explicit anti-cheating posture** (e.g., a "school mode" that disables the camera in detection zones, or a hardware kill switch that's visible to proctors). This is a 30-minute spec addition; not engineering-heavy, but a market-shaping move.
- The Taiwan case shows smart glasses emitting heat — a tell that the device is active. Dan Glasses' planned thermal management (per architecture review §1.1) is a non-functional feature that doubles as anti-cheat camouflage in some scenarios.
- **Reputational opportunity:** Dan Glasses is positioned to ship a "Transparent AI Glasses Manifesto" — local-only, no remote updates that change behavior without user consent, hardware kill switches visible to third parties, opt-in telemetry only. This is a marketing paper, not engineering, but it matters for category positioning.

### C.12 Open-source AI companion projects

**v3 update:** No new entrant since v2. The list (SIA, OpenClaw, Mem0 v3, Letta/MemGPT, Zep, Brilliant Labs Halo, Plaud/Omi/Limitless, Screenpipe, Paperclip) is unchanged.

**v3 reinforcement:** Screenpipe remains the most direct peer (local-first screen+audio capture, MIT-licensed, on-device). Worth a deeper look as a potential collaboration target or as a reference for the open-source local-first narrative.

### C.13 Privacy-preserving AI positioning — v3 sharpened

**v3 update — the privacy story is now a market imperative, not a marketing claim:**

The Meta paywall is a privacy story in disguise: the vendor is monetizing the user's hardware. The Asian exam cheating is a privacy story in the other direction: the category needs explicit anti-misuse features to survive regulatory scrutiny. **Both pressures push toward the same answer: local-first, transparent, user-controlled AI glasses.**

**v3 marketing line (sharper than v2):**
> "Dan Glasses: the AI glasses that work for you, not for the vendor. No subscription. No cloud. No remote behavior changes. No camera when you don't want it. No microphone when you don't want it. Yours, not theirs."

This is a one-line brand statement that addresses both the Meta backlash and the regulatory pressure simultaneously.

---

## D. Technical Deep Dives

### D.1 Deep Dive A: Self-improving RL loops for language models

**v3 update:** SIA framework unchanged. No new open-source competitor. The action is in closed commercial products (Lumio Lighthouse, 8090 Labs Software Factory), which reinforces the open-research opportunity.

### D.2 Deep Dive B: Edge VLM optimization for wearables

**v3 update:** LFM2.5-VL-450M is still the best sub-500MB VLM. SPEED-Q remains the SOTA quantization technique. **The new v3 signal is the Qualcomm DragonFly platform** (Forbes, June 17 2026), which is a silicon-vendor endorsement of the on-device agent thesis. This means: future Redax-class boards with Qualcomm silicon will have first-class hardware support for the kind of agent loop Dan Glasses runs. **Watch for Redax or a successor to adopt Qualcomm silicon.**

### D.3 Deep Dive C: Vector search and memory architectures for AI companions

**v3 update:** Mem0 v3, True Memory, Engram, Memanto, Infini Memory — all unchanged. No new entrant. The Storage → Reflection → Experience taxonomy stands.

**v3 new context — Tempus AI foundation model** (BioSpace, June 2026): 45M+ de-identified patient journeys, 1.5M with sequenced data, 400K records with full genomic + transcriptomic + imaging + clinical data. The Tempus foundation model "significantly reduces the time and data required to produce hundreds of clinically relevant insights." This is an existence proof that **a domain-specific multimodal foundation model + agentic workflows + longitudinal data** is a viable production architecture. Dan Glasses' analog: **a personal multimodal foundation model + agentic workflows + longitudinal user data.** The pattern is the same; the domain is personal instead of clinical.

---

## Cross-cutting: What the three deep dives say together

The three deep dives converge on a single thesis: **Dan Glasses' competitive moat in 2026 is the combination of (a) on-device inference, (b) genuine self-improvement, and (c) a real memory model.** None of the three is sufficient alone. All three together — and only the combination — is what the market doesn't have.

**v3 update — the moat is sharper because of three new 2026-06-26 signals:**
- **Meta is paywalling on-device features** → users will pay a premium for hardware they actually own and control.
- **Asia is regulating smart glasses in exam settings** → the category needs anti-misuse features, and the first product to ship them credibly wins the trust battle.
- **Apple is tightening Siri AI's surface area on URL summarization** → frontier labs are defensive, not expansive, on what their assistants are allowed to do. A "permissive by design, private by default" alternative is a credible wedge.

The thesis: **Dan Glasses = on-device + self-improving + memoryful + wearable + open + privacy-by-default + anti-misuse-by-design.** This is the bet for the next 24 months.

---

## Recommendations (v3, with v2 reinforced)

1. **Port SIA-W+H to danlab-multimodal** in Q3 2026. Publish a technical report. This is the headline research deliverable.
2. **Upgrade memoryd to v1.5** (temporal + episodic + consolidator) in Q4 2026. Benchmark against Mem0 v3.
3. **Switch perceptiond to LFM2.5-Extract** for caption ingest (drop-in, JSON output, no parsing).
4. **Implement perceptiond power-mode redesign** — throttle inference, not capture. Battery-life blocker.
5. **Add TTS A/B harness** — KittenTTS vs Kokoro-82M q4 — for v1.5 swap.
6. **Adopt /live and /ready split across all 6 daemons** — match audiod v1.1.
7. **Add `register_user_service` supervision** for all 9 daemons.
8. **Unify service health** with `GET /services.json` aggregator.
9. **Adopt event bus** (NATS or SQLite-queue) to replace bespoke per-service wire-up.
10. **Publish the privacy story explicitly** — local-first, no cloud, no subscription, hardware kill switches, anti-misuse posture. (v3 reinforcement: this is no longer a marketing claim; it is a market imperative.)

---

## Open Questions for somdipto

1. **Redax hardware timeline** — when do we get a dev board? Without this, the wearable path is blocked.
2. **LFM2.5-VL-450M power draw on aarch64** — can we get a Jetson Orin Nano to characterize before Redax?
3. **Mem0 vs memoryd v1.5** — are you open to swapping if the benchmark says so?
4. **SIA fork** — do you want to publish a paper, or a blog post, or both? arXiv vs Danlab blog?
5. **Tailscale tailnet** — DanLab shared tailnet, or new one for Dan Glasses?
6. **Package signing** — GPG or Sigstore? Who holds the signing key?
7. **(v3 new) Marketing lead** — should the next public artifact be the "Yours, not theirs" manifesto? Window: now, before Meta's paywall backlash peaks.
8. **(v3 new) Anti-cheat posture** — should the spec include a "school mode" / "exam mode" hardware kill switch, given the Asia scandals? Engineering cost: 30 minutes of spec work.
9. **(v3 new) Qualcomm silicon** — is Redax-or-successor on Qualcomm silicon? DragonFly is the right platform for the on-device agent thesis.

---

## v2 vs v3 changelog

- **Added:** Section C.11 v3 update on Meta paywalling on-device features (Verge, June 26 2026).
- **Added:** Section C.11 v3 update on Asia exam cheating scandals (CNN, June 26 2026).
- **Added:** Section C.13 v3 sharpened marketing line: "Yours, not theirs."
- **Added:** Section B.5 v3 NEW cluster candidate: "Silicon-for-agentic-AI" (OpenAI/Broadcom Jalapeño, Qualcomm DragonFly).
- **Added:** Section B.5 v3 reinforcement of on-device agent thesis from Qualcomm DragonFly.
- **Added:** Section A.3 v3 relevant adjacent signal: Qualcomm DragonFly validates edge agent thesis at silicon level.
- **Added:** Section D.2 v3 update: watch for Redax successor on Qualcomm silicon.
- **Added:** Section D.3 v3 update: Tempus AI foundation model as existence proof for the personal-domain analog.
- **Added:** Three new open questions for somdipto (7-9).
- **Reinforced:** All v2 conclusions on SIA, danlab-multimodal honesty, model stack, and roadmap.
- **Retracted:** Nothing.

---

*End of research report v3. See `dan2-architecture-review.md` (v3), `dan2-agi-roadmap.md` (v3), `dan2-model-analysis.md` (v3), and `dan2-papers-to-read.md` (v3) for the companion artifacts.*
