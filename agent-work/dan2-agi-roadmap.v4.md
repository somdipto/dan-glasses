# Dan2 — AGI Roadmap (v4, 2026-06-16 03:00 UTC)
**Status:** Final v4 (delta over v3)
**Audience:** somdipto (decision-maker), Dan1/Dan3/Dan4 (peer architects)
**Scope:** 6/12/24-month roadmap for Danlab, derived from v4 research report
**Run window:** 2026-06-16 03:00 UTC

---

## One-line bet

**Ship the only open-source, local-first, memory-first, self-improving wearable AI agent — backed by a hierarchical memory architecture and a structurally-guarded OpenClaw runtime — before Microsoft Scout GA (October 2026) and before Apple Glasses N50 (late 2027).**

---

## What changed since v3

1. **`memoryd v2` is now Tier 0/1/2 hierarchical, not flat vector.** v4 research surfaced DPCM, SAGE, MemDreamer, GraP-Mem — the 2026 SOTA. **6-month plan adds explicit `memoryd v2` milestone.**
2. **`os-toold v2` is now arbiter + identity-verification gate, not just path guard.** v4 StakeBench + lethal trifecta + Architecture as Governance strengthen the case for structural controls. **6-month plan adds explicit arbiter / watchdog primitive.**
3. **Proactive AI = v1.5, not v1.** v4 is explicit. v1.5 (months 7-12) gets a `policyd` service (engagement inference + safety gate + interruptibility).
4. **`perceptiond v2` gets VLMCache + per-layer mixed-precision.** v4 deep-dive identified concrete optimizations. **6-month plan adds the optimization pass as part of the v1 wearable prep.**
5. **The Memory wedge is stronger.** Letta (MemGPT) and Cognee are open-source competitors with similar hierarchical memory plans. **We need to ship first to claim the open-source + wearable + memory-first combination.**

---

## 6-month roadmap (June 2026 – December 2026)

**Bet: ship a defensible v1 desktop prototype + `os-toold v2` + `memoryd v2` + `perceptiond v2` optimizations, in time for Microsoft Scout GA (October 2026) and AWE 2027 positioning.**

### Month 1 (June 2026 — now)
- **SIA-H fork into `danlab-multimodal`** (carry from v3). 1.2B focal model, not 4.6B evolver. Per "Harness Updating Is Not Harness Benefit."
- **`os-toold v2` spec finalized.** Stealthy-parasitism detector + identity-verification gate + arbiter pattern. Concrete spec on disk.
- **`memoryd v2` spec drafted.** Tier 0/1/2 schema, dual-process consolidation, daily summarizer, weekly consolidator.
- **StakeBench + Varonis whitepaper draft.** Position Danlab as the open-source secure-by-default agent runtime.
- **Live re-verification loop** (already running — 7/7 daemons live, 106/106 tests green).

### Month 2 (July 2026)
- **`memoryd v2` implementation.** Tier 0/1/2 schema migration. Daily summarizer using rule-based extractive summarization (no LLM dependency for v1 of the summarizer). Weekly consolidator using TF-IDF + clustering.
- **`os-toold v2` implementation.** Path guard + identity-verification gate + audit log + trace_id propagation. Stealthy-parasitism detector in `memoryd` write path.
- **Gemma 3 4B benchmark on laptop.** Validate the upper-bound model class for the wearable. Capture latency, power, memory.

### Month 3 (August 2026)
- **`perceptiond v2` optimization pass.** VLMCache-style background caching + per-layer mixed-precision quantization for LFM2.5-VL-450M. Target: 3-5s/frame CPU (down from 10-15s).
- **Omni-Embed-Mini evaluation.** Compare against all-MiniLM-L6-v2 for multimodal embedding. Decide if we adopt for `memoryd v2.5`.
- **Telegram outbound content filter + rate limit.** Part of `os-toold v2`.

### Month 4 (September 2026)
- **All 5+ daemons at v2 (os-toold v2, memoryd v2, perceptiond v2, audiod v2.5, ttsd v1.1).** 200+ tests green.
- **AGENTS.md as security control.** Version-controlled `AGENTS.md` per daemon with Email Safety block + identity verification primitives + outbound policy. **This is the concrete security primitive the Varonis mitigation calls for.**
- **StakeBench / Varonis whitepaper publish.** Open-source positioning. Press cycle.

### Month 5 (October 2026)
- **Microsoft Scout GA watch + response.** Scout ships October 2026 on OpenClaw. **We publish the secure-by-default open-source alternative the same month.** Open-source the entire stack.
- **BOM v1 finalized.** $149-349 wearable BOM target.
- **Redax aarch64 port starts.** (Carry from v3, hardware-dependent.)
- **Hardware partner outreach.** If Redax is not finalized, explore the open-source hardware path (Brilliant Labs Halo reference design, Monako Glass).

### Month 6 (November–December 2026)
- **v1 desktop prototype release.** `dan-glasses-0.1.0` .deb. All daemons + Tauri app + OpenClaw + Telegram + .deb packaging + GPG-signed.
- **Bootstrap wizard v1 shipped.** First-run experience, model download, Telegram pairing, voice selection, memory roundtrip test.
- **Waitlist for wearable.** Position the v1 desktop as the developer platform; the wearable is the consumer product.
- **2026 retrospective + 2027 plan.** What worked, what didn't, what the wearable build taught us.

---

## 12-month roadmap (June 2026 – June 2027)

**Bet: ship a v1.5 with proactive AI + skill framework + wearable form factor. Beat Apple Glasses N50 (late 2027) to "open-source memory-first wearable AI."**

### Months 7-9 (January–March 2027)
- **`policyd` service.** Engagement inference (motion + audio + time-of-day → user state). Qualia-style 6.5K-param safety classifier for proactive output gating. Interruptibility settings (DND, focus mode, low-priority queue).
- **Proactive AI v1.5.** Salience-triggered suggestions, "you walked past the pharmacy 3 times this week" reminders. **Gated by `policyd`.**
- **Skill framework integration.** CUA-Skill / EvoCUA / Avenir-Web patterns. Skill library for common tasks (calendar, email, location, contacts).

### Months 10-12 (April–June 2027)
- **`memoryd v2.5`.** Adopt Omni-Embed-Mini for multimodal embedding. Add `procedures` table for procedural memory. Add `patterns` table for cross-domain patterns (DPCM-style).
- **Wearable hardware v1.** (Hardware-dependent — Redax or open-source reference.) First 50 units for closed beta.
- **Beta program.** 50 technical early adopters. 4-week workday usage validation. Battery life, salience accuracy, proactive trigger satisfaction.

### Year-1 success metrics
- 7+ daemons at v2, 200+ tests green
- `os-toold v2` published as open-source secure-by-default OpenClaw runtime
- `memoryd v2` published with Tier 0/1/2 hierarchical architecture
- `perceptiond v2` at 3-5s/frame CPU on x86_64 laptop
- v1 desktop prototype publicly downloadable
- v1.5 proactive mode behind `policyd` safety gate
- Wearable beta program launched

---

## 24-month roadmap (June 2026 – June 2028)

**Bet: become the de-facto open-source wearable AI agent platform. Hit 10K+ active users, 100+ third-party skills, 1M+ memories stored.**

### Year 2 (July 2027 – June 2028)

**Tracks:**

**Track 1: Hardware (wearable + accessories)**
- Wearable v1 GA: ship the Redax-based or open-source-reference wearable. $349-499 price point.
- Wearable v1.5: better battery, lighter frame, optional cellular.
- Smart-pendant accessory: Limitless-style pendant that pairs with glasses (or substitutes for users who don't want glasses).

**Track 2: Software (memory + self-improvement)**
- SIA-H fork to SIA-W (weights + harness). When weights are 1B+ and harness is mature, the risk of weight self-modification is acceptable.
- Hierarchical memory: 5 tiers (raw, daily, weekly, monthly, yearly). Automatic summarization. Cross-domain pattern induction.
- Continual learning: episodic replay + procedural distillation + semantic consolidation. **The 2028 bet is "an agent that improves every day, visibly."**
- Multi-user / household support: PRD v1 non-goal, becomes v2.5 feature.

**Track 3: Ecosystem (skills + open-source)**
- 100+ third-party skills. Calendar, email, contacts, location, weather, music, fitness, accessibility (sign language, object identification for visually impaired, scene description for low-vision).
- Open-source skill marketplace. Self-hosted or community-run.
- Open hardware reference design. Anyone can build a Dan Glasses-compatible wearable with off-the-shelf parts.
- Academic partnerships. Publish the architecture in venues like ICML, ACL, UIST. **The architecture is the moat, not the brand.**

**Track 4: AGI wedge (toward self-improving agents)**
- **The 24-month bet: ship a "learning loop" that visibly improves Dan Glasses over time.** A user who uses Dan Glasses for 30 days should be able to query: "what did you learn about me this month?" and get a meaningful answer.
- The Nadella framing: "the real competition isn't which model you pick. It's whether your organization learns from what it builds."
- The SIA-H thesis: harness updates alone can drive 30-50% task improvement. **We can ship a "learning loop" without modifying weights.** Lower risk, faster iteration.
- The Recursion bet: $650M at $4.65B valuation says the AGI race is now a venture-scale bet. **We don't need to win the AGI race. We need to ship the most-loved open-source wearable AI before someone else does.**

### Year-2 success metrics
- 10K+ active daily users
- 100+ third-party skills
- 1M+ memories stored across the user base
- Wearable GA shipped
- Self-improving memory loop demonstrably improving per-user
- Open-source skill marketplace launched
- 5+ academic publications citing the architecture

---

## Strategic priorities by layer

| Layer | 6-month bet | 12-month bet | 24-month bet |
|---|---|---|---|
| **Hardware** | Desktop prototype (x86_64) | Wearable beta (aarch64) | Wearable GA + smart-pendant |
| **Vision (perceptiond)** | LFM2.5-VL-450M Q4_0, 10-15s/frame | + VLMCache + per-layer mixed-precision, 3-5s/frame | Gemma 3 4B upper-bound validation, 1-2s/frame on aarch64 |
| **Audio (audiod)** | whisper.cpp + Silero VAD | Streaming whisper + RNNoise + speaker diarization | On-device wake word, "Hey Dan" |
| **TTS (ttsd)** | KittenTTS base | BareWave / UNISON evaluation | Custom voice cloning, <10MB model |
| **Memory (memoryd)** | Flat vector + all-MiniLM-L6-v2 (v1) | Tier 0/1/2 hierarchical + dual-process (v2) | 5-tier hierarchical + continual learning (v2.5) |
| **Security (os-toold)** | Path guard (v1) | Identity verification + arbiter + stealthy-parasitism detector (v2) | Formal verification + red-team bug bounty |
| **Proactive (policyd)** | n/a (v1 responsive only) | Engagement inference + safety gate + interruptibility (v1.5) | Cognitive-load aware + BCI-ready |
| **Orchestration (OpenClaw)** | Telegram + Zo MCP bridge | Skill framework + multi-agent coordination | Self-improving skill library |
| **Self-improvement (SIA-H)** | Fork into danlab-multimodal | Harness-only self-improvement | Harness + weights (when weights are 1B+) |

---

## What not to do (anti-recommendations)

**Carry from v3 + v4 additions:**

1. **Don't ship a flat vector store as the final `memoryd` architecture.** v4 research shows hierarchical + dual-process is the 2026 SOTA. Flat is 2019-era.
2. **Don't claim "RL" for the danlab-multimodal heuristic loop.** It's pre-RL scaffold. The semantic war on "RL" labels in 2026 makes this non-negotiable.
3. **Don't ship proactive AI in v1.** v1 = responsive. v1.5 = proactive. The triggering primitive + safety gate are not solved yet.
4. **Don't jump to Gemma 3 4B before measuring LFM2.5-VL-450M power on Redax.** Gemma 3 is the upper bound, not the v1 target.
5. **Don't write a `prompt` instruction as the security control.** StakeBench + Architecture as Governance: rule-based interventions decay. Structural controls (os-toold v2 + AGENTS.md as security control + audit log + trace_id) are the answer.
6. **Don't add cellular in v1.** Wi-Fi only. Cellular is a v2 hardware feature.
7. **Don't try to build a "smart glasses" with display in v1.** Audio-first, no display. Display is v2 (after wearable form factor is validated).
8. **Don't add multi-user / household in v1.** Single user per device. v2.5 feature.
9. **Don't ship to production without a Pinchy / StakeBench red-team pass.** Security is a structural property, not a feature.
10. **Don't over-invest in custom silicon.** Use off-the-shelf parts. The open-source hardware reference design is the wedge.

---

## Final recommendation

**6-month bet: ship `os-toold v2` + `memoryd v2` + `perceptiond v2` optimizations, in time for Microsoft Scout GA (October 2026).**

**12-month bet: ship v1.5 with `policyd`-gated proactive AI + skill framework + wearable beta.**

**24-month bet: become the de-facto open-source wearable AI agent platform. 10K+ users, 100+ skills, 1M+ memories. The architecture is the moat, not the brand.**

**The single most important thing we can do in the next 6 months:** publish the `os-toold v2` Pinchy-protection spec + `memoryd v2` hierarchical architecture as open-source whitepapers. The press cycle, the open-source positioning, and the Microsoft Scout GA timing all align. **This is the wedge.**

---

*Dan2 AGI Roadmap v4 — 2026-06-16 03:00 UTC. v4 sharpening: `memoryd v2` is now explicitly hierarchical (the biggest change), `os-toold v2` is explicitly arbiter-gated, proactive AI is explicitly v1.5 not v1, `perceptiond v2` has a concrete optimization roadmap. All other v3 content unchanged.*
