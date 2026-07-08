# Danlab AGI Roadmap — 6 / 12 / 24 Month Plan (v5)

**Author:** Dan-2
**Date:** 2026-07-01
**Horizon:** Now (July 2026) → July 2028
**Anchored to:** `dan2-research-report.md` (v3), `dan2-architecture-review.md` (v3), `dan2-model-analysis.md` (v3), `dan2-papers-to-read.md` (v3)
**Status:** v5 (2026-07-02) — surgical refresh on top of v4:
  - **SIA-W+H is now anchored to a credible open-source competitor to closed-source RSI.** Recursive Superintelligence (Rocktaschel + Socher, $650M at $4.65B, June 2026) is the closed-source RSI play. **SIA-W+H (Hexo Labs, MIT, May 28 2026) is the only open-source MIT path.** Anthropic's Favaro/Clark blog (June 5 2026) calls RSI "plausible within 24 months" and asks for a global pause. **The Q3 2026 SIA-W+H port goes from "interesting research deliverable" to "the open-source counter-narrative to $4.65B closed-source RSI"** — the publishing stakes are higher, the audience is bigger, the citation value is more.
  - **HRM-Text-1B (Sapient, Apache-2.0) replaces LFM2.5-1.2B-Thinking as the SIA Feedback-Agent target.** Smaller (1.15B vs 1.6B), cheaper to run on-device (2.4GB VRAM, ~4 tok/s on RTX 4060), trained from scratch for $1,500 — **the perfect "small beats large" companion to danlab-multimodal's pre-RL scaffold.** HRM-Text-1B is *the* open-source Apache-2.0 reasoning model in the 1B class. **Plan: Q3 2026, integrate HRM-Text-1B as the Feedback-Agent in the SIA-W+H port.** [^v5-hrm]
  - **The 12-month pure-edge window is now quantified.** v5 competitive map: Meta is the closed-model closed-cloud paywall vendor (3 tiers, Muse Spark); Google is the hybrid on-device-Gemini vendor (Android XR, fall 2026, 4hr battery); Apple is delayed to late 2027. **Dan Glasses' pure-edge + MIT-licensed + on-device-only position is the only unclaimed niche in the 2026-2027 window.** This is the *only* year in the next 5 where this position is available. Use it.
  - **No roadmap milestone changes.** v4's 6/12/24-month milestones hold. v5 sharpens the SIA-W+H narrative (open-source counter to RSI Labs), the Q3 2026 SIA Feedback-Agent selection (HRM-Text-1B), and the 12-month window thesis.

---

## North Star (24-month)

> **Danlab ships the open, on-device, privacy-preserving, self-improving AI glasses substrate. We are the credible research-backed answer to "AGI from India" — and we are the only vendor in the category that says "yours, not theirs" and means it at the firmware level.**

**Why this is the right North Star (mid-2026 context, v3 update):**

1. **The Meta paywall backlash (Verge, June 26 2026)** is the single biggest product-positioning event in the smart-glasses category in 2026 so far. Meta retroactively rate-limited an on-device feature (Conversation Focus) and put it behind a $19.99/month subscription. The Verge called it "rate limits and a soft paywall." The community reaction has been sharp. **This is the first time a major smart-glasses vendor has been caught eroding user ownership of a feature the user already paid for.** Dan Glasses' on-device + open-firmware + user-controlled-feature-flag story is now the direct answer.

2. **The Asia exam-cheating scandal (CNN, June 26 2026)** is the first major regulatory response to the smart-glasses category. Taiwan caught a medical-school applicant using AI glasses. South Korea is in active discussion with the Education Ministry. **The vendor that ships a credible "compliance mode" first owns the regulatory shield.**

3. **Jack Clark (Anthropic) puts 60% on no-human-involved AI R&D by end of 2028.** Anthropic's own data: ~80% of merged code is Claude-written, Claude agents completed an open-ended safety research project in April 2026. **SIA (Hexo Labs, MIT, May 28 2026) is the first open-source harness+weights self-improvement framework.** Danlab is well-positioned to be the *edge implementation* of this trend.

4. **OpenAI + Broadcom "Jalapeño" inference chip (June 24 2026)** signals the frontier labs are pulling compute in-house. The on-device angle matters more than ever — when cloud inference costs spike, the on-device-first stack is the only one with stable economics.

5. **Qualcomm "DragonFly" agentic-AI efficiency play (Forbes, June 17 2026)** — Qualcomm is positioning for "agentic AI as the new mobile workload," with the thesis that proactive agents will "quadruple CPU core demand in data centers." This validates the on-device agent thesis: if the cloud is the bottleneck, the edge is the opportunity.

**The "AGI from India" thesis is now credible because:**
- The open-weight + edge-inference + agentic-loop stack is shippable today
- The bottleneck is integration and self-improvement, not raw model capability
- Shivik Labs (Noida) shipped TRIDENT in Dec 2025; we are not alone, and we are not late
- The market is now actively looking for an alternative to vendor-lock-in smart glasses

---

## 6-Month Plan: Now → December 2026

**Theme: Lock the substrate. Ship the foundation. Publish the pre-RL → RL transition. Be first to compliance mode.**

### Q3 2026 (Jul → Sep): Foundation hardening + compliance mode

**Goal:** Make the existing 9-daemon substrate reliable enough to demo to investors and researchers, produce a publishable "pre-RL → real RL" artifact, and ship a spec'd compliance mode.

**Engineering:**
- [ ] Migrate all 9 daemons to `register_user_service` mode=process with auto-restart (eliminates the memoryd-hung class of bug)
- [ ] Add unified `GET /services.json` health aggregator (eliminates the port-table rot)
- [ ] Add `/live` and `/ready` liveness/readiness split to perceptiond, memoryd, toold, ttsd, os-toold (matching audiod's v1.1 contract)
- [ ] Add `dan-glasses/scripts/up.sh` and `down.sh` for clean bringup/teardown
- [ ] Lock Tauri v2 app at canonical path with name+identifier matching spec
- [ ] Fix cargo 1.65 → 1.77+ for native Tauri builds
- [ ] Wire audiod → memoryd for transcript ingest
- [ ] Wire perceptiond → memoryd for salient-frame caption ingest (use LFM2.5-Extract JSON schema for direct ingestion)
- [ ] Add `mcporter emit-ts zo --mode client` → `Services/zo-mcp-bridge/zoClient.ts` typed wrapper
- [ ] Document the one-time Tailscale bootstrap for somdipto (gVisor blocks it but the path is documented)

**Research (the headline deliverable):**
- [ ] **Port danlab-multimodal to SIA-W+H** (Hexo Labs, MIT, GitHub `hexo-ai/sia`). LFM2.5-VL-450M as the task agent, Claude Sonnet 4.6 as the Feedback-Agent (or LFM2.5-1.2B-Thinking local for the privacy-first path). **This is the headline research deliverable for the quarter.** The danlab-multimodal README already points to SIA; this just executes.
- [ ] Measure on a multi-turn code-review task: does SIA-W+H beat the hand-coded heuristic?
- [ ] Publish a technical report: **"SIA-W+H for Multimodal Self-Improvement: From Heuristic to Genuine RL."** Target: arXiv + a blog post. **First-mover artifact in the open-source 450M-class VLM self-improvement space.**

**Product (NEW v3 — compliance mode as a first-class feature):**
- [ ] **Spec the compliance mode.** Three profiles: exam, meeting, hospital. Each profile mutes camera/mic/suppresses proactive triggers/exports audit logs. Hardware-rooted: a physical camera-shutter switch (already on the spec but undefined behavior) becomes the primary control surface.
- [ ] **Environment detection layer** for the proactive pre-filter: detect "exam context" (printed material in frame, silent room, time-of-day), "meeting context" (multiple faces + talking), "hospital context" (medical attire, signage), and automatically suppress proactive interventions in these contexts.
- [ ] **Audit log export** as a user feature: "give me everything my glasses saw today" → signed JSON export. Aligns with EU AI Act and the upcoming category regulation.
- [ ] Polish the BootstrapWizard UX in the Tauri app
- [ ] Publish the Tauri app as a Zo Site (public `*.zocomputer.io`) so the wearable form factor has a phone-companion option
- [ ] Add per-service status pills on the home screen
- [ ] Add a "service health" panel that aggregates all 9 daemons in one view
- [ ] Land the perceptiond power-mode redesign (inference gating, not capture gating) — see architecture review

**Marketing (NEW v3 — "yours, not theirs" blog post):**
- [ ] **Publish a blog post this week (Jul 1 → Jul 7)**: "Why we said no to cloud. Why we say no to paywalls. Why Dan Glasses is yours, not theirs." Reference the Meta paywall backlash. Position Danlab as the open alternative.
- [ ] Cross-post to Hacker News, r/MachineLearning, r/singularity (where the agent-improving-agents discussion is active)
- [ ] Coordinate with somdipto for LinkedIn amplification

**Decision points at end of Q3:**
- Is SIA-W+H measurably better than the hand-coded heuristic on danlab-multimodal? → If yes, double down on the SIA port in Q4. If no, investigate why (probably the reward model is too weak).
- Is the Zo Site version of the Tauri app seeing real usage? → If yes, prioritize it over a native `.deb` for the desktop prototype.
- Does the SIA-W+H port scale to LFM2.5-VL-450M as the task agent? → If yes, that's a publishable result.
- **NEW v3:** Is the compliance mode spec stable enough to ship in v1.5? → If yes, prioritize it. If no, defer to v2 but keep the public marketing on it.
- **NEW v3:** Did the "yours, not theirs" blog post land? → HN front page, meaningful traffic spike, or signal to keep going?

### Q4 2026 (Oct → Dec): Memory substrate upgrade + wake-word + anti-lock-in

**Goal:** Upgrade memoryd to v1.5 (temporal reasoning + episode boundaries + consolidation). Add wake-word (openWakeWord, ~3MB) to audiod so the user doesn't need PTT. Land the hardware-rooted anti-lock-in architecture.

**Engineering:**
- [ ] memoryd v1.5: add `valid_from` / `valid_to` columns, `/query?as_of=YYYY-MM-DD` endpoint
- [ ] memoryd v1.5: add `episoder` daemon — watches audiod/perceptiond/conversation events, emits episode_started/ended
- [ ] memoryd v1.5: nightly memory consolidation daemon (summarize, demote, expire)
- [ ] audiod v1.5: wire openWakeWord as a low-power front-end; audiod runs PTT-only or wake-word-activated
- [ ] perceptiond: implement salience-*delta* gate (not salience); VLM only fires on novelty
- [ ] perceptiond: add batched VLM inference (batch=2-4 salient frames)
- [ ] perceptiond: switch chat template to LFM2.5-Extract for structured-JSON captions
- [ ] TTS A/B harness: KittenTTS vs Kokoro-82M q4 vs Piper
- [ ] Document the package-signing mechanism (GPG concrete) per canonical analysis

**Research:**
- [ ] Benchmark Mem0 v3 vs our memoryd v1.5 on temporal-reasoning tasks. If Mem0 wins on a clear metric, adopt it. If we win, publish.
- [ ] Pilot the "fast-path / slow-path" VLM architecture on aarch64 (requires Redax or equivalent). Measure per-frame energy.
- [ ] Write the SIA-W+H paper follow-up: "Lessons from 100 self-improvement iterations on a 450M VLM."

**Product (NEW v3 — anti-lock-in as architecture):**
- [ ] **Open firmware contract.** A documented, signed firmware image. User can verify the firmware running on their glasses matches a public hash. The hardware team spec'd a secure-boot chain (already on the v1 roadmap); this makes the chain *user-verifiable*.
- [ ] **User-controlled feature flags.** Every feature (proactive mode, cloud sync, TTS, VLM, wake-word) is a user-toggleable flag stored locally. No vendor can remotely disable a feature.
- [ ] **"Export your stack" UX** — a one-click export of memoryd, all skills, all configs, the bootstrap state. The user can leave Danlab with everything they brought in. This is the v1 of "data portability" and is a major differentiator.
- [ ] Ship a "memory browser" UI in the Tauri app (browse memories by type, date, episode)
- [ ] Land the proactive pre-filter (PRPF pattern, 2026) as a thin layer on top of perceptiond
- [ ] Add the TTS quality knob to settings (KittenTTS-mini / KittenTTS-base / Kokoro-82M-q4)
- [ ] **NEW v3:** Ship the compliance mode UI in the Tauri app — toggle exam/meeting/hospital profiles, view audit log, export audit log

**Decision points at end of Q4:**
- Has the wake-word front-end improved user retention in the desktop prototype? → If yes, ship it.
- Did Mem0 beat our memoryd v1.5? → If yes, migrate. If no, publish the comparison.
- Is the Redax board closer to availability? → If yes, start wearable migration. If no, continue the desktop track.
- **NEW v3:** Has the anti-lock-in architecture been verified end-to-end (firmware signature check, user-flag persistence, "export your stack" workflow)? → If yes, ship it as a marketing-grade differentiator.
- **NEW v3:** Has the compliance mode been adopted by any institutional pilot (a school, a hospital, a company)? → If yes, the wedge is real. If no, iterate on the spec.

---

## 12-Month Plan: July 2026 → June 2027

**Theme: Self-improving substrate. Wearable-ready software. First publishable research artifacts.**

**Major milestones:**

1. **Q1 2027 (Jan → Mar): Self-improving memory daemon**
   - Ship `memoryd v2`: proactive retrieval loop (Databricks memory-scaling pattern), Zettelkasten auto-linking (A-MEM pattern), memory type promotion/demotion
   - Ship `perceptiond v2`: bi-temporal memory, episode-scoped retrieval
   - Publish: "Open-Weight Edge Memory for AI Companions" — paper comparing memoryd v2 vs Mem0 v3 vs Zep vs Letta on temporal-reasoning + episode-recall benchmarks

2. **Q2 2027 (Apr → Jun): Wearable migration (if Redax is available)**
   - Power characterization on aarch64 (the missing data from §D.3)
   - Implement the full power state machine (sleep / idle / watchful / active / deep-idle)
   - Thermal model + throttle to smaller model (SmolVLM-256M, then Gemma3-270M)
   - First wearable form factor build
   - Publish: "Power Characterization of LFM2.5-VL-450M on aarch64 Wearable Hardware" — **the first public power-data paper for this model class on a wearable target**

3. **Q2 2027: Marketing + ecosystem + conference submission**
   - **Target venue: ICML 2027 (deadline ~Jan 2027) or ACL 2027 (deadline ~Jan 2027) for the SIA-W+H paper.**
   - **Alternative venue: NeurIPS 2027 (deadline ~May 2027) for the edge SIA-W+H follow-up.**
   - Open the daemon codebases to external contributors
   - Publish the developer kit: how to write a new salience gate, how to add a new memory type
   - "AGI from India" research paper: position the danlab stack in the global SOTA
   - First conference talk: "Self-Improving AI Glasses from India" (ICML workshop, ACL workshop, or NeurIPS workshop)

**Decision points at end of Q2 2027:**
- Is the wearable form factor viable (4h battery, <50g, passive cooling)? → If yes, ship the dev kit. If no, the desktop track continues and the wearable is deferred.
- Has the SIA-W+H work on danlab-multimodal produced a publishable result? → If yes, the research track is validated. If no, reassess the SIA port.
- **NEW v3:** Has the compliance mode been adopted by any institutional pilot? → If yes, the regulatory wedge is real. If no, iterate.
- **NEW v3:** Has any competitor tried to "out-compliance" us? → If yes, the moat is contestable. If no, the wedge is real.

---

## 24-Month Plan: July 2026 → June 2028

**Theme: AGI-from-India thesis operational. A self-improving, on-device, open-stack AI companion.**

**Major milestones:**

1. **Q3 2027 (Jul → Sep): SIA-W+H at scale**
   - Generalize the SIA port from danlab-multimodal to the full dani/danlab stack
   - Run SIA-W+H against danlab-multimodal, danlab-audiod, danlab-perceptiond in parallel
   - First multi-agent self-improving system (each daemon improves its own task model)
   - Publish: "Multi-Agent Self-Improvement on Edge: Lessons from a 9-Daemon Substrate"

2. **Q4 2027 (Oct → Dec): Cross-modal grounding**
   - perceptiond's LFM2.5-Extract emits `(timestamp, object, action)` triples
   - audiod's whisper events are timestamped and aligned
   - memoryd ingests cross-modal episodes (vision + audio within the same time window)
   - Enables US-1 (Encounter Recall) and US-2 (Contextual TaskReminder) in the PRD

3. **Q1 2028 (Jan → Mar): External developer program**
   - Open the substrate: skill SDK, memoryd schema documentation, perceptiond salience-gate authoring
   - First community-contributed memory type or salience detector
   - Apply for a research grant (EU Horizon, NSF, India SERB, or private foundation)

4. **Q2 2028 (Apr → Jun): The "AGI from India" position**
   - Compile all artifacts: SIA paper, memoryd paper, power-characterization paper, SIA-W+H generalization, compliance-mode paper
   - Submit a journal paper: "An Open, Self-Improving, Edge-First, User-Controlled Stack for AI Companions" — to JMLR, TACL, or Nature Machine Intelligence
   - **Position for a research-lab-grade funding round** (EU Horizon, NSF, India SERB, or private foundation) **OR a Series A** if the product track is also viable
   - The headline: "AGI from India" — the on-device, open, self-improving, user-controlled alternative to vendor-locked smart glasses

---

## What we are NOT doing (and why)

- **Building a frontier-scale LLM.** OpenAI / Anthropic / Google / DeepMind have hundreds of millions of dollars and 100+ GPU clusters. We are a 2-person research-and-product lab. We use their open weights (LFM2.5, Whisper, Kokoro, Llama, Qwen) and add value via the integration + self-improvement + on-device deployment layers.

- **AR display hardware.** The AR display market is dominated by Meta (with EssilorLuxottica), Snap (Snap OS), Apple (cancelled Vision Pro 2, delayed glasses), Google (Warby Parker). We don't have the manufacturing, the optics, or the capital. Our wedge is the *software substrate* — the AI that runs on whatever hardware the user has.

- **Cellular / always-connected wearables.** Cellular modem + battery is the wrong power trade for v1. Wi-Fi only, with the option to tether to a phone for connectivity. The Brilliant Labs Halo model.

- **A proprietary model.** Open-weight is a wedge, not a sacrifice. Liquid AI is betting on this; Hexo Labs is betting on this; we should too. The day we train a custom model, we lose the open-weight advantage.

- **A social / sharing product.** Meta Ray-Ban already does capture+share. We don't compete on that axis. We compete on **memory + proactivity + privacy + user control**.

- **A vendor-paywalled product.** The Meta paywall backlash is the loudest product-positioning event of 2026. Danlab is structurally on the right side of it. **We compete on "yours, not theirs."**

---

## Open Questions for Somdipto

1. **SIA-W+H compute budget.** SIA-W+H requires LoRA fine-tuning of LFM2.5-VL-450M, which is doable on a single A100/H100. We need access to one. Options: a free-tier Colab / Lightning Studio / Lambda cloud credits. Can you allocate a $200-500/month cloud-GPU budget for the SIA-W+H runs?
2. **Redax timeline.** When does the hardware team expect the Redax board? Without it, the wearable migration is parked.
3. **Conferences / publishing.** Should we target arXiv-first, or submit to ICML 2027 (Jan 2027 deadline), ACL 2027 (Jan 2027 deadline), or NeurIPS 2027 (May 2027 deadline)? What's the right venue for the SIA paper?
4. **Partnerships.** Brilliant Labs (Halo) and Shivik Labs (TRIDENT) are the two most direct peers. Worth a conversation. Are there other Indian AI labs (Krutrim, Sarvam, Soket AI) we should be talking to?
5. **Funding runway.** If we publish the SIA paper, we can credibly apply for research grants. If we ship the wearable dev kit, we can credibly raise a seed round. What's the appetite?
6. **NEW v3 — Compliance mode priority.** Is the compliance mode a v1.5 must-ship, or a v2 nice-to-have? The market signal says v1.5 must-ship, but the engineering cost is real. What's your call?
7. **NEW v3 — Anti-lock-in architecture cost.** Open firmware + user-controlled flags + "export your stack" UX are real engineering costs (1-2 sprints each). Worth it for the marketing wedge? My read: yes, but it's your call.
8. **NEW v3 — Institutional pilot for compliance mode.** Do you have any institutional contacts (a school, a hospital, a company) that would pilot the compliance mode? Even one pilot is a marketing-grade signal.
9. **NEW v3 — "Yours, not theirs" blog post timing.** The news cycle is hot this week. Should we publish the post on Danlab blog, on Hacker News, both? Want to ship before the cycle cools.
10. **NEW v3 — Conference strategy.** With ICML 2027 and ACL 2027 deadlines in Jan 2027, we need to start drafting the SIA-W+H paper in Q3 2026 to make the January deadline. Worth the cost?

---

*See `dan2-research-report.md` for the full technical evidence behind every claim in this roadmap. See `dan2-papers-to-read.md` for the reading list that grounds the research tracks. See `dan2-architecture-review.md` for the structural risks that gate the engineering tracks. See `dan2-model-analysis.md` for the model selection rationale.*
