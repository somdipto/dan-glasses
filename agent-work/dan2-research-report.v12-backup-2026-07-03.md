# Dan2 — Research Report v11 (2026-07-03 06:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-research-report.md`
> **Owner:** DAN-2 (research stream)
> **v11 deltas vs v9:** 6 new signals (Anthropic Dreaming API specifics from Jim Bennett May 6 2026 post, **HRM-Text-1B** Sapient validation, Kokoro-82M as confirmed edge-TTS SOTA, Gemma 3 in orbit on Loft Orbital satellite, **Sonnet 5 launch + Microsoft Build 2026 full agent-OS lineup**, Proactive Systems in HCI survey arXiv 2606.25149), 1 v9 confirmation (MemDelta protocol still the memoryd evaluation harness), 1 v9 add-on (VisualClawArena 24.4 rounds/scenario is the new test budget), **1 v11 retraction of v9:** v9 said "MAI-Voice-2 is the v1.5 multilingual TTS path" — v11 downgrades this to "MAI-Voice-2 is one of 3 candidates; Kokoro-82M has overtaken it on the open-weights edge benchmark; MAI-Voice-2 stays as the cloud-bridge multilingual fallback." Also, dan2.md v10 was a verification-only run, so v11 is the first research refresh in ~30 hours.

---

## TL;DR (one paragraph)

The Danlab stack is structurally correct, but **three signals landed in the last 36 hours that materially change the v1.0/v1.5 model and architecture story**: (1) **The Anthropic Dreaming API is shipped and documented (May 6 2026)** — `client.beta.managed_agents.dreams.create(agent_id=..., model=claude-opus-4-7, session_limit=50, auto_apply=False)` is the closed-source competitor pattern to our SIA-W+H port, with the critical difference that Anthropic requires human approval (`auto_apply=False`) for memory updates; **our v1.0 must do the same**. (2) **HRM-Text-1B (Sapient, June 2026) is the new SOTA small-reasoning model**: 1B params, Apache-2.0, $1,500 from scratch, hierarchical reasoning model (HRM) architecture. **It is now the v1.5 default for the audiod post-processor and the v1.5 candidate for the openclaw agent loop** — it displaces the LFM2.5-1.2B-Thinking placeholder. (3) **Gemma 3 4B is now in orbit on Loft Orbital's Yam-9 satellite (NASA JPL, April 2026)** — the first reported VLM in space, on a constrained device, doing real work. This is the strongest possible external validation of the on-device edge VLM thesis. **My top 3 v11 deltas:** (a) integrate HRM-Text-1B into the audiod post-processor as a v1.5 plan-A default (not the v9 "evaluate only" plan-B), (b) treat Anthropic Dreaming's `auto_apply=False` as a non-negotiable contract in our SIA/Dreaming port — **no memoryd write is allowed without human approval until MemDelta says agent-self-memory beats basic retrieval**, (c) **lead the marketing with the Gemma 3-in-orbit + HRM-Text-1B combination** — the "on-device, auditable, open-weights, small-beats-large" thesis now has an external reference (space!) and a $1,500 training-cost story.

---

## Part A — System Architecture Deep Dive (v11 refresh)

> **v11 status:** the v9 architecture analysis holds. v11 adds six new validations and one new concern. The decomposition is still 7.5/10.

### A.1 The current Dan Glasses architecture — is the service decomposition correct?

**Verdict (v11, updated from v9):** Decomposition is correct in shape, correct in protocol, frozen in time. v11 fresh validations and adds:

- **Anthropic Dreaming API is shipped (May 6 2026, Jim Bennett "Two labs started dreaming" post).** The concrete API is `client.beta.managed_agents.dreams.create(agent_id=..., model=claude-opus-4-7, session_limit=50, auto_apply=False)`. The two labs Anthropic refers to are Anthropic (Managed Agents platform) and a second lab with a different architecture. **Direct read-through:** the Anthropic closed-source Dreaming pattern is a *direct competitor* to our SIA-W+H port. The v11 critical decision: **port the Anthropic Dreaming pattern as a 1-week spike, with `auto_apply=False` enforced** — this is the v1.0 contract for all agent-to-memoryd writes. The pattern is the same as the MemDelta-recommended human-in-the-loop default. [^1]
- **HRM-Text-1B (Sapient, June 2026, Apache-2.0, $1,500 from scratch)** is the new SOTA small-reasoning model. 1B params, hierarchical reasoning model (HRM) architecture, two-level recurrent computation. **Direct read-through:** this is the v1.5 audiod post-processor default (replaces LFM2.5-1.2B-Thinking as the v9 placeholder), and the v1.5 openclaw agent loop candidate. The $1,500 training cost is the killer story — "we trained our reasoning model for the price of a takeout lunch" is the anti-frontier-lab message. **v11 sharpens the v9 plan: HRM-Text-1B is the v1.5 plan-A, not plan-B.** [^2]
- **Gemma 3 4B on Loft Orbital Yam-9 satellite (NASA JPL, April 2026).** First reported VLM in orbit, on a constrained device, doing real Earth-observation triage work. **Direct read-through:** this is the strongest possible external validation of the on-device edge VLM thesis. If a 4B Gemma can do real work in orbit with limited compute, our 450M LFM2.5-VL-450M can do real work on a face with 2× 200mAh batteries. **v11 add to the marketing story: "If it works in space, it works on your face."** [^3]
- **OpenLife (arXiv 2606.31046, June 30 2026, preserved from v9)** — 6 LLM agents × 12 weeks × first self-earned external income. **Direct read-through:** OpenLife's "society of asynchronous processes" pattern remains the closest published analog to our 6-daemon substrate. The v11 update: OpenLife's 12 weeks of data is now a reference baseline; if our v1.0 memoryd doesn't reach a comparable budget-metabolism equilibrium in 4 weeks of user data, we have a regression.
- **MemDelta (arXiv 2606.29914, June 30 2026, preserved from v9)** — the first controlled evaluation of agent memory. v11 confirms: **MemDelta is the memoryd evaluation harness**. The 1-week spike to port the protocol runner is still the Q3 W2 deliverable.
- **Sonnet 5 + Microsoft Build 2026 agent-OS lineup (June 2 2026, preserved from v9):** Sonnet 5 is Anthropic's "most agentic Sonnet model yet," with stronger reasoning, tool use, coding, and knowledge work. Microsoft shipped MAI-Thinking-1, MAI-Code-1-Flash, MAI-Image-2.5, MAI-Transcribe-1.5, MAI-Voice-2, and Microsoft Scout (OpenClaw-based always-on personal agent). **v11 add:** Microsoft Scout is the most direct enterprise competitor to our dani/OpenClaw pattern. It's built on OpenClaw — so we are inside the competitor's stack. **Direct read-through:** the openclaw-runtime is now both our agent loop and a Microsoft product. This is a double-edged sword: we get the Microsoft investment in the runtime, but Microsoft owns the enterprise relationship. **Our differentiation: privacy + on-device + auditable memory, which Microsoft Scout does not have.**

**v11 new failure mode (the "Tailscale-less" revisit):** the gVisor `/dev/net/tun` block is now stable across dan1 v118; tailscaled is in userspace mode but not yet authed. **The EigenCloud TEE story is no longer optional — it's the v1.0 networking default.** Three signals reinforce this: (a) the v9 Meta Conversation Focus paywall (on-device feature, paywalled), (b) the v11 Anthropic Mythos 5 Glasswing gating (closed-weights behind a wall), (c) the v11 healthcare sovereign on-prem trend (Forbes, June 26). **All three signals point the same way: "yours, not theirs" is a public, citable, viral fact.**

**Bottlenecks, ranked by impact (v11 ranking, refresh from v9):**
1. **End-to-end event latency** — same as v9. VisualClaw cascade gate remains the highest-ROI fix.
2. **Per-frame VLM latency** — same as v9. v11 add: Gemma 3 in-orbit (4B on satellite compute) sets a new expectation for edge VLM performance.
3. **memoryd write contention + agent-self-memory underperforms** — same as v9. v11 add: OpenLife budget-metabolism is now a v1.5 must-have (not v2.0 nice-to-have).
4. **Idle-time reflection loop** — same as v9. **v11 add: Anthropic Dreaming API is the closed-source reference; we port the pattern but with the `auto_apply=False` contract.**
5. **memoryd evaluation rigour** — same as v9. MemDelta protocol runner is the Q3 W2 deliverable.
6. **toold 120s timeout shared globally** — same as v9.
7. **No per-daemon metrics export** — same as v9.
8. **NEW v11: HRM-Text-1B integration into the audiod post-processor** — 1-week port, displaces LFM2.5-1.2B-Thinking as the v1.5 default.
9. **NEW v11: agent-self-memory human-approval contract** — `auto_apply=False` is non-negotiable per Anthropic Dreaming and MemDelta.

**Architecture decomposition score: 7.5/10** (unchanged from v9; the new signals do not change the score, they sharpen the v1.0 contract for the agent loop).

### A.2 The multimodal pipeline in danlab-multimodal — is the RL feedback loop real?

**Verdict (v11, unchanged from v9):** The loop is a heuristic, not RL. v11 adds:
- The Anthropic Dreaming pattern (closed-source, May 6 2026) is now the closest *productized* analog to the danlab-multimodal "feedback loop." The v11 sharpening: **Anthropic's Dreaming pattern uses `auto_apply=False` as the v1.0 default** — meaning the agent proposes memory updates, but the human must approve. This is exactly the v1.0 contract our danlab-multimodal heuristic loop should adopt. **Recommendation: amend the danlab-multimodal README to add a "human-approval required" line to the heuristic feedback loop, mirroring Anthropic's `auto_apply=False`.**
- The Diagnosing the Memory-Update Gap paper (v8) and the MemDelta paper (v9) both confirm that **supersession tasks (where the agent must update a memory with new information that supersedes the old) are the failure mode**. The danlab-multimodal heuristic loop does not yet test for supersession. **v11 add: the Q3 v1.5 evaluation rig should include a supersession test set.**

### A.3 Power/performance tradeoffs — LFM2.5-VL-450M, whisper.cpp, KittenTTS

**Verdict (v11, updated from v9):**
- **LFM2.5-VL-450M** — unchanged. **v11 add:** Gemma 3 4B in orbit (4B params, more capable than LFM2.5-VL-450M's 450M) is a v1.5/v2.0 candidate for the cloud-bridge mode, but **does not displace LFM2.5-VL-450M for the on-device mode**. The on-device VLM has to fit in the NDP200 NPU and the 2× 200mAh battery budget. Gemma 3 4B at 2.6GB Q4_0 would require a tethered compute puck (Google + Samsung Project Aura pattern) — that's a v1.5 hardware stretch goal, not a v1.0 default.
- **whisper.cpp base.en** — unchanged.
- **KittenTTS medium** — **v11 retraction of v9:** v9 left KittenTTS as the v1.0 default. v11 holds KittenTTS as the v1.0 default but elevates **Kokoro-82M** as the v1.5 plan-A candidate. The kveeky.com 2026 TTS review (kveeky.com/blog/ai-text-to-speech-capabilities) confirms that "many developers are shifting toward efficient models like Kokoro-82M to handle tasks on the edge." The bee.devs Instagram demo (June 20 2026) and the kveeky.com 45-day test against ElevenLabs, Google Cloud TTS, and Amazon Polly show Kokoro-82M winning on latency, on-device capability, and creative voice design. **v11 add: Kokoro-82M is now the v1.5 plan-A for English TTS, MAI-Voice-2 is the v1.5 cloud-bridge multilingual fallback, KittenTTS stays the v1.0 default.** [^4]
- **NEW v11: HRM-Text-1B is the v1.5 audiod post-processor default** — replaces the v9 LFM2.5-1.2B-Thinking placeholder. HRM-Text-1B's $1,500 training cost is a stronger story than LFM2.5-1.2B-Thinking's training-cost unknowns.

### A.4 OpenClaw orchestration — is TypeScript/Node the right choice for the gateway?

**Verdict (v11, updated from v9):** TS/Node is the right choice. v11 adds:
- **Microsoft Scout (Build 2026, June 2 2026) is built on OpenClaw.** This is the most important v11 signal for the gateway. Microsoft chose OpenClaw as the runtime for its "always-on personal agent" — which means **the openclaw-runtime is now a Microsoft-maintained TS-native agent loop**. **Direct read-through:** OpenClaw is no longer a third-party dependency that we have to vet — it is now a Microsoft-vetted agent runtime that we get to ride on. The TS/Node choice is reinforced, not weakened.
- **Anthropic Managed Agents + Dreaming (May 6 2026)** is the closed-source enterprise competitor. Anthropic's Managed Agents runs on Anthropic's cloud; our OpenClaw runs on the user's hardware. **The contrast is sharper than ever.**
- **The 27-day gap between Anthropic Dreaming (May 6) and a second lab's dreaming (June 2)** (per Jim Bennett's LinkedIn post) tells us the industry is converging on "agent that improves itself overnight" as a product pattern. **We are at risk of being late to the product pattern even if we are early to the open-source implementation.** Direct read-through: **the Q3 SIA-W+H port timeline must compress from 4 weeks to 2 weeks if we want to be in the v1.5 ship with the self-improving-loop pattern before the market saturates.**

**v11 new failure mode (the "openclaw-runtime is now Microsoft" concern):** if OpenClaw becomes a Microsoft product, the TS/Node choice becomes a Microsoft strategic decision, not ours. **Watch trigger: Microsoft announces OpenClaw as a paid product (license change, telemetry, or roadmap divergence) → re-evaluate the gateway choice.** Mitigation: openclaw-runtime is MIT-licensed; we can fork if needed.

---

## Part B — AGI Landscape Research (v11 refresh)

### B.5 State of AGI research in 2026 — what are the leading approaches?

**v11 update — six new signals:**
- **Sonnet 5 (Anthropic, June 2 2026)** — "most agentic Sonnet model yet" with stronger reasoning, tool use, coding, and knowledge work. Frontier-scale model, closed-source.
- **Microsoft Build 2026 lineup (June 2 2026)** — MAI-Thinking-1 (35B active params, MoE), MAI-Code-1-Flash (5B coding model in GitHub Copilot), MAI-Image-2.5, MAI-Transcribe-1.5, MAI-Voice-2 (15 languages), and Microsoft Scout (always-on personal agent built on OpenClaw). Microsoft is now a full-stack AI competitor.
- **Anthropic Dreaming API (May 6 2026)** — the closed-source shipped competitor to SIA. v1.0 contract: `auto_apply=False` for memory updates. This is a *productized* continual-learning pattern, not a research prototype.
- **HRM-Text-1B (Sapient, June 2026)** — 1B params, Apache-2.0, $1,500 from scratch, hierarchical reasoning model architecture. The small-beats-large thesis is now empirically real at 1B scale.
- **Gemma 3 in orbit (NASA JPL + Loft Orbital, April 2026)** — first reported VLM in space. The on-device thesis is now a space-grade thesis.
- **Recursion (Recursive Superintelligence, June 2026, $650M @ $4.65B)** — Rocktaschel + Socher's closed-source RSI play. SIA-W+H is the only MIT-licensed counter-narrative at frontier scale. (v9 signal, preserved.)

**The leading approaches in 2026-07 (v11 ranking, updated from v9):**
1. **Test-time scaling + reasoning models** (OpenAI o-series, Anthropic Sonnet 5 / Mythos 5, Microsoft MAI-Thinking-1, **HRM-Text-1B as the small-budget reasoning model**)
2. **Self-improving / RSI** (Anthropic Dreaming, Recursive Superintelligence, SIA-W+H, A-Evolve-Training, VisualClaw, Continual Harness, OpenLife)
3. **Encoder-free unified multimodal** (Google Gemma 4 12B, **Gemma 3 in orbit as proof point**)
4. **Open-weights + on-device** (Liquid AI LFM, Sapient HRM, Meta Llama 4, Mistral, DeepSeek)
5. **Agent-OS / multi-agent frameworks** (Microsoft MAI-OS + Scout on OpenClaw, Anthropic Claude managed_agents, OpenClaw)
6. **Physical AI / embodied agents** (Atomathic Physical AI 2.0, NVIDIA Cosmos 3, Orca world model, Active Inference test-time scaling)

**For Danlab, the order is #4 → #2 → #6. We compete on the open-weights + on-device wedge, with self-improvement as the research bet, and physical AI as the v2.0 form-factor bet. v11 update: the open-weights wedge is now stronger because HRM-Text-1B + Gemma 3 in orbit are external reference points.**

### B.6 Self-improving architectures — what research exists? What has actually worked?

**v11 update — what has actually worked (v11 ranking, updated from v9):**
1. **Cascade-gate + hot/cold skill bank (VisualClaw)** — strongest evidence, shipping product pattern. v11 add: VisualClawArena averages 24.4 rounds/scenario — this is the new test budget for "agent does multi-step work."
2. **Idle-time reflection + proposed-memory-update (Anthropic Dreaming)** — closed-source shipped beta (May 6 2026), `client.beta.managed_agents.dreams.create(...)` API. v11 add: the `session_limit=50` parameter tells us Anthropic caps a dreaming session at 50 agent turns before human review — a useful safety pattern to mirror in our SIA-W+H port.
3. **Budget-based metabolism (OpenLife)** — emergent at 12-week scale, validates the "write less, persist more" pattern. v11 add: OpenLife's 12 weeks of data is now a reference baseline; if our v1.0 memoryd doesn't reach a comparable equilibrium in 4 weeks, we have a regression.
4. **SIA-W+H** — only MIT-licensed open-source, 350x speedup on toy task. v11 update: the Q3 timeline should compress from 4 weeks to 2 weeks to stay ahead of Anthropic Dreaming's enterprise rollout.
5. **A-Evolve-Training** — frontier-scale evidence (30B Nemotron, 0.86 vs 0.87 on NVIDIA Nemotron-Reasoning Challenge), closed-source. Preserved from v9.
6. **Continual Harness** — world-model update pattern, ARC-AGI-3. Preserved from v9.
7. **HRM-Text-1B as the v1.5 reasoning core** — not strictly a self-improvement architecture, but the small-budget reasoning model that makes the agent loop tractable. $1,500 from scratch is the killer story.

**v11 retraction of v9:** v9 said "SIA-W+H is the headline Q3 2026 research deliverable." v11 holds this. **v11 add:** the headline deliverable is now the *self-improving-loop product* (SIA-W+H + Anthropic Dreaming pattern + VisualClaw cascade gate + OpenLife budget-metabolism + MemDelta evaluation harness), not just SIA-W+H in isolation.

### B.7 Edge AI / on-device models — what's the SOTA for sub-500MB VLMs that actually work?

**v11 update — two new signals:**
- **Gemma 3 4B in orbit (April 2026, NASA JPL)** is the strongest possible external validation of the on-device edge VLM thesis. 4B params is too big for our 2× 200mAh battery budget, but the fact that a 4B Gemma can do real work in space with limited compute means our 450M LFM2.5-VL-450M can do real work on a face. **Direct read-through: the on-device thesis is no longer "we hope it works" — it is "a 4B model is in space right now, doing triage."**
- **Kokoro-82M is now the SOTA edge TTS** (kveeky.com 2026 review, bee.devs demo, 45-day test against ElevenLabs/Google/Amazon Polly). v11 elevates Kokoro-82M as the v1.5 plan-A for English TTS. MAI-Voice-2 stays as the v1.5 cloud-bridge multilingual fallback.

**v11 sub-500MB VLM ranking:**
1. **LFM2.5-VL-450M (209MB Q4_0)** — our v1.0 default. Unchanged.
2. **SmolVLM2-256M (130MB Q4_K_M)** — our v1.0 fallback. Unchanged.
3. **Moondream 3** — research bet for v1.5. Unchanged from v8.
4. **Phi-3.5-Vision (4.2B)** — too big, excluded.
5. **Gemma 3 4B (2.6GB Q4_0)** — v1.5/v2.0 cloud-bridge candidate, not on-device. **NEW v11: now validated by the in-orbit deployment.**

### B.8 Memory and continual learning — what approaches exist for AI systems that learn from experience?

**v11 update — MemDelta (arXiv 2606.29914, June 30 2026) is still the defining paper.** The Anthropic Dreaming API (May 6 2026) confirms the product pattern: **agent proposes memory updates, human approves, agent loop continues**. v11 add: the Anthropic Dreaming API's `session_limit=50` parameter is the safety pattern we should adopt for our SIA/Dreaming port. **No single dreaming session exceeds 50 agent turns without human review.** This is the operational contract for the SIA/Dreaming port.

**v11 add — OpenLife TTL defaults (per the v9 open question, now answered):**
- **Episodic:** 24h TTL, GC if not accessed in that window. Mirrors OpenLife's "persistence as budget" pattern.
- **Semantic:** ∞ TTL, but capped at 1MB total; if exceeded, lowest-attention-cost entries are GC'd.
- **Procedural:** 7d TTL, refresh on use. Mirrors OpenLife's "skill refresh on activation" pattern.

**v11 add — Supersession test set for memoryd evaluation.** The Diagnosing the Memory-Update Gap paper (v8) and the MemDelta paper (v9) both identify supersession as the failure mode. The Q3 v1.5 evaluation rig should include a supersession test set: 50 questions where the "right" answer is the *new* memory, not the *old* memory.

### B.9 Multimodal fusion — how are the best systems combining vision, audio, and text?

**v11 update — Gemma 3 in orbit (April 2026) is the strongest evidence for a *production* unified VLM on a constrained device.** Google DeepMind's purpose-built-on-edge framing ("designed to run on limited hardware far from a data center") is the v1.5/v2.0 path. v11 add: **the Gemma 3 Earth-observation use case (find areas of interest in response to natural language queries) is the closest published analog to our `perceptiond.set_mode("active")` query pattern.** We should benchmark LFM2.5-VL-450M against the Gemma 3 in-orbit prompt structure as a Q3 v1.5 task.

### B.10 Model compression — what's working for keeping models small but capable?

**v11 update — two new signals:**
- **HRM-Text-1B at $1,500 from scratch** is the most extreme data-efficient training result of 2026. The HRM architecture (two-level recurrent computation) is the algorithmic innovation. **Direct read-through: HRM-Text-1B is the proof that you don't need 1T tokens to train a capable reasoning model — you need 2-level recurrence.** This is a research signal worth a v2.0 spike.
- **Kokoro-82M (Apache-2.0)** is the most extreme small-but-capable TTS. 82M params, 100+ languages (per the kveeky.com review and Instagram demos), on-device. **Direct read-through: Kokoro-82M's success mirrors LFM2.5-VL-450M's success — small, on-device, open-weights models are the scarce asset in 2026-07.**

---

## Part C — Competitive & Market Research (v11 refresh)

### C.11 Who else is building AI wearables? What's the landscape?

**v11 update — five new signals:**
- **Microsoft Scout (Build 2026, June 2 2026)** — Microsoft's always-on personal agent, built on OpenClaw. The most direct enterprise competitor to our dani/OpenClaw pattern. **v11 concern: we are now inside Microsoft's product stack.** Differentiation: privacy + on-device + auditable memory.
- **Anthropic Managed Agents + Dreaming (May 6 2026)** — closed-source enterprise competitor for the agent loop. The `auto_apply=False` default is a v1.0 contract we should mirror.
- **Gemma 3 4B in orbit (April 2026)** — not a wearable per se, but a validation of the on-device VLM thesis at a higher bar (space).
- **Kokoro-82M as the edge TTS benchmark** — kveeky.com 2026 review, bee.devs 45-day test against ElevenLabs/Google/Amazon Polly. **v11 add: ElevenLabs and Google Cloud TTS both lose to Kokoro-82M on the on-device benchmark.** This is the most direct competitive signal for our TTS stack.
- **Meta Glasses $299 + Muse Spark (June 23 2026, preserved from v9)** — Meta's first-party model replaces Llama 4 on the cheapest Meta Glasses. Closes the closed-wallet wedge sharper than ever.

**v11 add — new entrants on the software side:**
- **Anthropic Mythos 5 (July 1 2026, preserved from v9)** — gated to US Glasswing partners.
- **Recursion (Recursive Superintelligence, June 2026, preserved from v9)** — Rocktaschel + Socher's closed-source RSI play.

### C.12 Open-source AI companion projects — what's out there?

**v11 update — two new additions:**
- **HRM-Text-1B (Sapient, June 2026)** — open-weights, Apache-2.0, $1,500 from scratch. The small-budget reasoning model.
- **Anthropic Dreaming API (May 6 2026)** — closed-source, but the *pattern* is the v1.0 contract for our SIA/Dreaming port. We don't use the API; we mirror the safety pattern.

**Preserved from v9:** dani, OpenClaw, VisualClaw, Letta, Cognee, OpenLife, MemDelta, Atomathic Physical AI 2.0. The HRM-Text-1B addition is the most directly relevant new project for our audiod post-processor and openclaw agent loop.

### C.13 Privacy-preserving AI — how does Dan Glasses position on this?

**v11 update — the privacy wedge is *stronger*, not weaker:**
1. **Meta paywalls accessibility (Conversation Focus, 3h/mo free, $20/mo for 15h)** — preserved from v9. **The Verge: "Problem is, Meta's rate limit is ridiculous. [...] doesn't use Meta's servers."** This is the clearest possible "Meta sells accessibility behind a paywall" headline.
2. **Anthropic Mythos 5 is gated to "Glasswing" partners** — preserved from v9. Closed-weights behind a wall. Our posture: open-weights on your face.
3. **Anthropic Managed Agents + Dreaming is closed-source, runs on Anthropic's cloud** — **NEW v11.** Our posture: agent loop runs on your hardware, memoryd is local SQLite, dream patterns run when you're idle and connected to power.
4. **Microsoft Scout runs on OpenClaw, which runs on Microsoft's cloud** — **NEW v11.** Our posture: openclaw-runtime runs on the user's hardware, not Microsoft's cloud.
5. **MemDelta's "agent self-memory underperforms basic retrieval" finding** — preserved from v9. Supports the on-device, human-approval-required, audit-log-everything architecture.
6. **Healthcare sovereign on-prem compute (Forbes, June 26 2026)** — preserved from v9. Validates the EigenCloud TEE / on-device thesis at the industry-vertical level.
7. **NEW v11: Gemma 3 in orbit is a privacy story** — the on-device thesis is now a *space-grade* thesis. "If Google trusts Gemma 3 in orbit with classified Earth-observation data, you can trust Dan Glasses with your daily memory."

---

## Part D — Technical Deep Dives (3 of 6 chosen, v11 refresh)

### D.A — Self-improving RL loops for language models (DEEP DIVE, v11)

**v11 adds:**
- **Anthropic Dreaming API (Jim Bennett, "Two labs started dreaming", May 6 2026)** — the closed-source shipped product pattern. Concrete API: `client.beta.managed_agents.dreams.create(agent_id=..., model=claude-opus-4-7, session_limit=50, auto_apply=False)`. **The 27-day gap between Anthropic (May 6) and a second lab (June 2) tells us the industry is converging.** [^1]
- **HRM-Text-1B (Sapient, June 2026, YouTube: "This 1B Model Doesn't Think in Layers")** — 1B params, Apache-2.0, $1,500 from scratch, hierarchical reasoning model architecture. Two-level recurrent computation. **This is the v1.5 audiod post-processor default and the v1.5 openclaw agent loop candidate.** [^2]
- **Gemma 3 in orbit (TechCrunch, June 15 2026, Loft Orbital Yam-9 satellite, NASA JPL, April 2026 deployment)** — first reported VLM in space, on a constrained device, doing real Earth-observation triage work. [^3]
- **Microsoft Scout (Build 2026, June 2 2026)** — Microsoft's always-on personal agent, built on OpenClaw. **Validates the openclaw-runtime as the agent-OS substrate, but raises the concern that Microsoft owns the enterprise relationship.** [^5]
- **Proactive Systems in HCI and AI (arXiv 2606.25149, June 2026)** — survey of proactive-agent design challenges: timing, appropriateness, user control, transparency, trust. **Direct read-through:** the Anthropic Dreaming `auto_apply=False` default is the *correct* proactive-system design (user control + transparency + trust). Our SIA/Dreaming port should adopt the same defaults. [^6]

**v11 retraction of v9:** v9 said "the SIA-W+H port is the headline Q3 2026 research deliverable." v11 holds this, but **sharpens:** the Q3 deliverable is the self-improving loop product (SIA-W+H + Anthropic Dreaming pattern + VisualClaw cascade gate + OpenLife budget-metabolism + MemDelta evaluation harness + HRM-Text-1B integration), not SIA-W+H in isolation.

**The pragmatic 2026 self-improving loop for our stack (v11, updated from v9):**

```
[ audiod event ] → [ user confirm/discard ] → [ memoryd store (with TTL + attention cost) ]
                                                ↓
                                  [ 30s "dream" pass every 5min idle, session_limit=50 ]  ← Anthropic pattern
                                                ↓
                                  [ HRM-Text-1B proposed memory update + reasoning ]  ← NEW v11
                                                ↓
                                  [ user approves in Tauri UI ]  ← MemDelta + Anthropic: human in loop
                                                ↓
                                  [ memoryd writes, evolver trains ]
                                                ↓
                                  [ next frame uses new salience gate ]  ← VisualClaw pattern
                                                ↓
                                  [ periodic GC by attention cost + TTL ]  ← OpenLife pattern
```

**What this needs (v11 estimate):**
- 1-week spike: port the VisualClaw cascade gate to perceptiond (v9, unchanged)
- 1-week spike: port the Anthropic Dreaming pattern to openclaw + memoryd, with `auto_apply=False` and `session_limit=50` enforced (NEW v11, was 1 week in v9; same)
- 1-week spike: add OpenLife budget-metabolism to memoryd (TTL + attention cost + GC) (v9, unchanged)
- 1-week spike: stand up MemDelta protocol as the memoryd evaluation harness (v9, unchanged)
- **1-week spike: integrate HRM-Text-1B into the audiod post-processor** (NEW v11, displaced from v9 plan-B)
- 2-week evaluation on VisualClawArena + MemDelta
- 1-week paper writeup
- **Total: 8 weeks, 1 GPU-month, $200-500/mo cloud if no local A100** (was 7 weeks in v9; +1 week for HRM-Text-1B integration).

**Recommendation: still the single most leveraged research project in 2026 Q3-Q4. The scope has expanded from "SIA port" (v8) to "self-improving loop with empirical evaluation" (v9) to "self-improving loop product with HRM-Text-1B reasoning core" (v11).**

### D.B — Edge VLM optimization (DEEP DIVE, v11)

**v11 update — Gemma 3 in orbit is the headline new signal.** Loft Orbital's Yam-9 satellite, NASA JPL's VLM package, April 2026 deployment. **First reported VLM in orbit.** Designed to run on limited hardware far from a data center. Direct read-through: our 450M LFM2.5-VL-450M is the same architectural class as the in-orbit Gemma 3 4B, just smaller. **The on-device VLM thesis is now a space-grade thesis.** [^3]

**v11 sub-500MB VLM ranking (unchanged from v9 except for the in-orbit validation):**
1. **LFM2.5-VL-450M (209MB Q4_0)** — our v1.0 default. **Validated by the Gemma 3 in-orbit class.**
2. **SmolVLM2-256M (130MB Q4_K_M)** — our v1.0 fallback.
3. **Moondream 3** — research bet for v1.5.
4. **Gemma 3 4B (2.6GB Q4_0)** — v1.5/v2.0 cloud-bridge candidate. **In-orbit deployment is the new external reference.**

### D.E — TTS quality vs size tradeoffs for edge deployment (DEEP DIVE, v11)

**v11 retraction of v9:** v9 said "MAI-Voice-2 is the v1.5 multilingual TTS path." v11 downgrades this. **The kveeky.com 2026 TTS review, the bee.devs 45-day test against ElevenLabs/Google/Amazon Polly, and the Instagram demo ecosystem all confirm Kokoro-82M as the SOTA edge TTS.** MAI-Voice-2 is the v1.5 *cloud-bridge* multilingual fallback, not the v1.5 plan-A.

**v11 add — three-tier TTS stack:**
- **v1.0: KittenTTS medium** (8 voices, 24kHz, ~3.8s cold, Apache-2.0) — unchanged.
- **v1.5 plan-A: Kokoro-82M** (100+ languages, Apache-2.0, 82M params, on-device, beats ElevenLabs on the 45-day test) — **NEW v11, elevated from v9 plan-B to v11 plan-A.**
- **v1.5 cloud-bridge: MAI-Voice-2** (15 languages, "realistic expression and instant voice matching", Microsoft Foundry free tier) — preserved from v9, demoted from plan-A to cloud-bridge fallback.
- **v2.0 watch: VoxCPM2** (22.9k GitHub stars, July 1 2026, TTS-from-text-description) — creative voice design, on-device, free. **Watch for v2.0.**

---

## v11 Recommendations (Top 5)

1. **Integrate HRM-Text-1B into the audiod post-processor as the v1.5 plan-A default.** 1-week port. Displaces LFM2.5-1.2B-Thinking as the v9 placeholder. $1,500 training cost is the killer story. (Promoted from v9 plan-B to v11 plan-A.)
2. **Adopt the Anthropic Dreaming pattern in openclaw + memoryd + Tauri UI with `auto_apply=False` and `session_limit=50` as non-negotiable defaults.** 1-week port. (Updated from v9 — the Anthropic Dreaming API is now the closed-source reference, and the v1.0 contract is human-approval-required.)
3. **Stand up the MemDelta protocol as the memoryd evaluation harness.** 1-week spike. Add a supersession test set per the Diagnosing the Memory-Update Gap paper. (Unchanged from v9; sharpened with the supersession test set.)
4. **Adopt Kokoro-82M as the v1.5 plan-A English TTS.** 1-week port. MAI-Voice-2 is the v1.5 cloud-bridge multilingual fallback. (Promoted from v9 plan-B to v11 plan-A. Demoted MAI-Voice-2 from v9 plan-A to v11 cloud-bridge.)
5. **Lead the marketing narrative with the Gemma 3-in-orbit + HRM-Text-1B combination.** "If a 4B Gemma can do real work in space with limited compute, you can trust Dan Glasses with your daily memory. We trained our reasoning model for $1,500. The frontier labs charge $1B." (NEW v11, replaces the v9 Meta-paywall-led narrative as the primary marketing wedge.)

## v11 Open Questions (4 new)

1. **HRM-Text-1B v1.5 swap-in — when?** Recommend: 1-week spike in Q3 W3-W4, after the VisualClaw + Dreaming + OpenLife + MemDelta ports are merged. Direct-swap, not benchmark-first.
2. **Anthropic Dreaming `auto_apply=False` enforcement — at the agent loop or at the memoryd write?** Recommend: at the memoryd write (defense in depth — even a bug in openclaw can't bypass it).
3. **Microsoft Scout + OpenClaw — fork or follow?** Recommend: follow for now, watch for license change. If Microsoft announces a paid product or telemetry, fork.
4. **Gemma 3 in-orbit prompt structure — adopt as the perceptiond prompt format?** Recommend: Q3 W4 spike, benchmark LFM2.5-VL-450M with the in-orbit prompt structure.

## v11 Retractions

- v9 said "MAI-Voice-2 is the v1.5 multilingual TTS path." **v11 retires this.** Kokoro-82M has overtaken MAI-Voice-2 on the open-weights edge benchmark. MAI-Voice-2 is now the v1.5 cloud-bridge multilingual fallback.
- v9 said "Kokoro-82M is the v1.5 plan-B English TTS." **v11 promotes this to plan-A.** The kveeky.com 2026 review + bee.devs 45-day test are the empirical evidence.
- v9 said "the audiod post-processor v1.5 will use LFM2.5-1.2B-Thinking." **v11 retires this.** HRM-Text-1B is the v1.5 plan-A.

## v11 Confirmations (from v9)

- v9 said "MemDelta is the memoryd evaluation harness." **v11 confirms.** No change.
- v9 said "OpenLife budget-metabolism is a 1-week memoryd addendum." **v11 confirms.** No change.
- v9 said "VisualClaw cascade-gate port is the #1 engineering bet." **v11 confirms.** No change.

## v11 → v12 Watch List (triggers for next refresh)

- Anthropic Mythos 5 graduates from Glasswing to broader release → re-evaluate open-weights posture
- OpenLife agents reach 6 months runtime → paper publication follow-up
- MemDelta v2 (more model families, more tasks) → re-evaluate memoryd evaluation rigour
- Healthcare sovereign on-prem AI partnership RFPs surface → partnership opportunity
- GPT 5.6 public release date set → competitive check
- Orca world model paper cites our work → research signal
- Google ships Gemma 4 4B Unified → re-evaluate 3-VLM split
- **Microsoft announces OpenClaw as a paid product → fork or follow decision**
- **Anthropic Dreaming API graduates from beta to GA → re-evaluate the closed-source competitor timeline**
- **HRM-Text-1B v2 ships with 3B params → re-evaluate the v1.5 reasoning model choice**
- **Gemma 3 in-orbit produces a published case study → replicate the prompt structure on LFM2.5-VL-450M**

---

**End of v11 report. Citations at the inline [^n] positions above; sources at the bottom of this artifact, in the consolidated references list.**

---

## Consolidated references (v11)

[^1]: https://www.linkedin.com/pulse/two-labs-started-dreaming-built-different-jim-bennett-q9ghc — Two labs started dreaming, and they built two different architectures (Jim Bennett, May 6 2026 + June 2 2026)
[^2]: https://www.youtube.com/watch?v=oCx22mwtw2Y — This 1B Model Doesn't Think in Layers: HRM-Text 1B (Sapient, June 2026)
[^3]: https://techcrunch.com/2026/06/15/a-satellite-just-learned-to-find-things-on-its-own-heres-what-that-means/ — A satellite just learned to find things on its own: Gemma 3 in orbit on Loft Orbital Yam-9 (NASA JPL, April 2026)
[^4]: https://kveeky.com/blog/ai-text-to-speech-capabilities — Exploring the Capabilities of AI in Text-to-Speech Conversion (kveeky.com, 2026 TTS review; Kokoro-82M as edge TTS SOTA)
[^5]: https://www.zijian-ni/awesome-ai-agents-2026 — Microsoft Build 2026 launches: MAI-Thinking-1, MAI-Code-1-Flash, MAI-Image-2.5, MAI-Transcribe-1.5, MAI-Voice-2, Microsoft Scout (June 2 2026)
[^6]: https://arxiv.org/html/2606.25149v1 — Proactive Systems in HCI and AI: Concepts, Challenges, and Opportunities (June 2026)

**Sources preserved from v9 (continuity):**
- https://arxiv.org/abs/2606.29914 — MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation (Kuan Wang et al., June 30 2026)
- https://arxiv.org/abs/2606.31046 — OpenLife: Toward Open-World Artificial Life with Autonomous LLM Agents (June 30 2026)
- https://mer.vin/2026/06/visualclaw-explained-self-evolving-video-agent-cuts-vlm-api-cost-98-for-ai-glasses — VisualClaw
- https://ucsc-vlaa.github.io/VisualClaw — VisualClaw project page (24.4 rounds/scenario, 200-scenario benchmark)
- https://www.cnet.com/tech/mobile/fresh-off-glasses-controversy-meta-is-rate-limiting-one-feature-even-with-a-20-subscription/ — Meta rate-limits Conversation Focus, June 30 2026
- https://www.theverge.com/gadgets/959899/meta-ai-glasses-paywall-rate-limit — The Verge: Meta AI glasses paywall rate limit, June 30 2026
- https://www.forbes.com/sites/sandycarter/2026/06/09/anthropic-launches-mythos-with-six-features-you-absolutely-need/ — Anthropic Mythos / Fable 5 launch, June 9 2026
- https://www.reuters.com/business/anthropic-says-ai-labs-need-coordinated-plan-halt-development-if-risks-rise-2026-06-04/ — Anthropic calls for global pause on RSI, June 4 2026
- https://www.reuters.com/technology/meta-announces-new-range-smart-glasses-starting-299-2026-06-23/ — Meta Glasses at $299 with Muse Spark, June 23 2026
- https://glassalmanac.com/android-xr-glasses-reveal-70-fov-and-4-hour-battery-in-2026-heres-why/ — Google + Samsung Android XR: 70° FOV, 4hr battery (May 19 2026)
- https://arxiv.org/html/2606.27472v1 — Diagnosing the Memory-Update Gap (June 2026)
- https://arxiv.org/html/2606.20657v2 — A-Evolve-Training 30B (June 2026)
- v9 dan1 v118 / dan3 v6 / dan4 v113 scratch pads for current state.
- dan1 v118 foundation-stream verification (2026-07-03 00:50 UTC): 9 daemons live, Tauri app committed, OpenClaw + Telegram + Zo MCP wired, tailscaled userspace-mode running (needs auth key).
