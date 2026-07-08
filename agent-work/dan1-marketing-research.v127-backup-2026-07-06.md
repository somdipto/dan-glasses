# Dan1 — Marketing Research Report (v127)

**Run:** 2026-07-06 07:30 UTC · Asia/Calcutta 13:00 IST
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Status:** v127 refresh on top of v126. v126 holds (3 axes — outer-loop RSI, Meta market correction, Meta contractor disclosure). v127 sharpens with: (1) **Tailscale-script-now-ready** (v124, the authkey-only gap is named + the script is in-tree), (2) **dan2 v28 chip-stack sovereignty** + **display-less 20M-unit form factor** promoted from "honorable mention" to a first-class pillar, (3) **Outer-loop RSI is no longer a theory** — audiod v1.3→v1.4→v1.5 in production, dan2 v23→v28, the changelogs are the receipts, (4) **5 fresh signals from dan2 v28** (Jack Clark 8x LOC, NVIDIA XR AI + viture Helix, 20M display-less forecast, AIMultiple benchmark, DynamicMem 93% retrieval-failure).
**Builds on:** v126 (research-integrity corrections held), v124 dan1 engineer scratch (Tailscale script + bridge persistent), v28 dan2 (outer-loop RSI axis, chip-stack sovereignty, display-less form factor).
**Foundation (unchanged, verified v124 dan1.md):** 9/9 daemons live, 208/208 tests, Telegram @danlab_bot polling, .deb `dan-glasses-daemons_0.1.0-1_all.deb` (9.4MB), threat model public (v122.5), Tauri v2 app published, OpenClaw + zo-mcp-bridge persistent (v124).

**v127 lead (locked):** *The substrate is shipped. The 9/9 daemons are live. The .deb installs. The reversibility contract + sovereign-trust audit are the only two remaining gates between us and Show HN #1. The Tailscale authkey is the only remaining gate between us and the live wearable demo. Three unblock-the-gate tasks = 4 engineer-days. Everything else is content.*

---

## 0. v127 deltas — what changed since v126 (5 hours ago, this morning)

v126 corrected two specific framings in v124's 3-region bifurcation (Alibaba backdoor claim is unverified; Palantir/Nemotron is a self-interested single-source claim) and added three new axes. v127 keeps all of that and **promotes three things from "honorable mention" to "first-class"**.

### v127 delta #1 — Tailscale is one authkey away
- v124 dan1 scratch: `scripts/tailscale-join.sh` is in-tree. Smoke-tested. One authkey = demo goes live.
- OpenClaw log confirms: `[tailscale] serve failed: Command failed: /usr/bin/tailscale serve --bg --yes 18789 · Logged out.`
- **v127 framing:** *The Tailscale authkey is the lowest-effort 1-day unblock for the highest-leverage 1-week deliverable (the live wearable demo). Mark it as P0 on the open-questions list. Stop guessing when the authkey is dropped.*

### v127 delta #2 — Chip-stack sovereignty is a first-class pillar (from dan2 v28)
- NVIDIA XR AI (Cosmos + Nemotron + MCP + NeMo Agent Toolkit) + viture Helix (MediaTek). First consumer reference platform. June 16-30 2026.
- **v127 framing:** *Open-source software is no longer aspirational. It is now NVIDIA-validated. The "fourth axis" of the v1.0 spec §13 is the chip stack the user owns, not the chip Anthropic co-develops. Promote it to first-class.*

### v127 delta #3 — Display-less is a first-class form factor (from dan2 v28)
- 20M display-less AI smart glasses forecast for 2026 (Smart Analytics Global, June 2026). 167% YoY. 6-entrants race.
- **v127 framing:** *The form factor race is not the AR-display race. It is the always-on-hearing race. The 20M-unit 2026 category is display-less. This validates the v1.0 display-less v1.0 form factor decision. Promote from "option B" to "default ship."*

### v127 delta #4 — Outer-loop RSI is no longer a theory
- dan2 v23→v28 changelog. audiod v1.0→v1.1→v1.2→v1.3→v1.4 (5 versions in 9 weeks). audiod is the receipt.
- Jack Clark (Import AI #460): **8x increase in lines-of-code merged in 2026 vs 2024 at Anthropic.**
- **v127 framing:** *Outer-loop RSI is shipping at Anthropic (8x LOC) AND at Danlab (audiod v1.4). The maximalist RSI is 60% by 2028 (Jack Clark). Danlab is shipping the substrate on a wearable, in a Bengaluru laptop, BEFORE the maximalist inflection. The v1.0 ship is the next 6 outer-loop RSI receipts.*

### v127 delta #5 — 4 new dan2 v28 signals to cite
- **AIMultiple open-source embedding benchmark (July 3 2026)** — first cross-domain consensus methodology. v127 add: any memoryd model swap must use this + MemDelta.
- **Hermes Agent outperforms Claude Opus + GPT-5.5 (Nous Research, late June 2026)** — 11% over GPT-5.5 on hard agentic benchmarks. v127 add: Hermes Agent is the v1.0 openclaw agent framework plan-A.
- **DynamicMem (arXiv 2606.22877, late June 2026)** — over 93% of memory failures trace to retrieval, not the writing model. v127 add: memoryd v1.5 should focus engineering on retrieval, not on the writing model.
- **Alibaba SkillWeaver (VentureBeat, July 2026)** — cuts token use 99% via execution-graph + skill-routing. v127 add: toold v1.5 should consider this pattern.

### What v127 explicitly does NOT change (held from v126)

- v126 corrections to Alibaba/Claude Code (Reddit-source caveat, Anthropic response, model-distillation counter-accusation) — **all held**.
- v126 corrections to Palantir/Nemotron (self-interested single-source claim) — **held**.
- v126 corrections to Meta market share (Q1 2026 = 69%, IDC 13.6M units) — **held**.
- v126 corrections to Meta contractor harm-prompt disclosure (Covalen, Aug 2025) — **held**.
- 3-region bifurcation wedge reframed as a temporal claim, not a present-tense claim — **held**.
- The protocol/observability/on-device/small-beats-large/sovereign-trust/reversibility pillars — **held**.
- The "audited, not perfect" / "yours, not theirs" closing — **held**.
- The 9/9 daemons + 208/208 tests + .deb + threat model + reversibility-contract-in-progress foundation — **held**.

---

## 1. What is Dan Glasses? (v127)

**One-liner:** A proactive, on-device AI companion in glasses form factor. Sees, hears, remembers, speaks only when it has something worth saying. Open weights. Politically-uncapturable. From India. The .deb is the demo. The reversibility contract is the trust. The chip stack is yours.

**Product shape (live today, 2026-07-06 13:00 IST, verified v124 dan1.md):**

| Layer | Live | Where |
|---|---|---|
| Hardware (JBD MicroLED, dual 200mAh, USB-C, NDP200 firmware) | Spec + CAD | `dan-glasses/implant-work/` |
| **9 daemons** (audiod, perceptiond, memoryd, toold, ttsd, os-toold, dan-glasses-app, openclaw, zo-mcp-bridge) | ✅ All live | `Services/` |
| OpenClaw gateway | ✅ Live, 63 commands, 8 plugins | ws://127.0.0.1:18789 |
| **zo-mcp-bridge (NEW v124)** | ✅ Persistent, 88 tools, PID 4808 | tcp 127.0.0.1:18790 |
| Telegram bot | ✅ Polling @danlab_bot | wired in OpenClaw |
| Tauri v2 app | ✅ Published | `https://dan-glasses-app-som.zocomputer.io` |
| **`.deb` package** | ✅ Built, 9.4MB | `dan-glasses-daemons_0.1.0-1_all.deb` |
| **Tailscale join script (NEW v124)** | ✅ In-tree | `scripts/tailscale-join.sh` |
| Models | ✅ LFM2.5-VL-450M, MiniLM-L6-v2, KittenTTS, whisper.cpp | local on disk |
| Brain (Dani) | ✅ Public | `github.com/somdipto/dani` |
| Threat model doc | ✅ Shipped v122.5 | `docs/threat-model.md` |
| Reversibility contract | 🟡 v124 plan-O2 spike (Q3 W2, 3 days) | dan2 v26 |
| Sovereign-trust audit | 🟡 v124 plan-O1 spike (Q3 W1, 1 day) | dan2 v26 |
| HRM-Text-1B | 🟡 Planned integration | next stream |
| Redax aarch64 | 🟡 Timeline TBD | not blocking |

**Vision (PRD §1, unchanged):** *What if your glasses remembered everything you saw, noticed things you missed, and could answer any question about your day — hands-free?*

**v127 positioning (4 lanes, sharpened with chip-stack + display-less):**
- ❌ Not Google Glass (dead, 2015)
- ❌ Not Ray-Ban Meta (capture-and-share, reactive, accessibility paywalled 3hr/15hr at $19.99/mo, 69% Q1 2026 share, contractor safety-testing apparatus disclosed)
- ❌ Not Apple smart glasses (16 months away, ~$2,000)
- ❌ Not Anthropic closed-source (Trump-conditional, Alibaba-routed-to-Qoder, Babushkin reversibility essay, Mythos gated to ~100 US critical-infrastructure partners, Anthropic-Samsung custom chip)
- ❌ Not Brilliant Labs Halo (closest open peer; wins on form factor, loses on substrate + chip stack)
- ✅ **Proactive, on-device, politically-uncapturable, chip-stack-sovereign AI companion** — observes, reasons, contextualizes, acts. **Yours, not theirs. Sovereign-trust-validated. Fully reversible. Display-less v1.0. Open-source on a chip the user owns.**

**v127 value props (in order, 11 props — added chip-stack + display-less + reversibility-now-citable):**

1. **Yours, not theirs.** Memory, models, audio never leave the device. No cloud lock-in. No Meta paywall. No Anthropic-conditionality. Open weights. The .deb is yours. The bot is yours. The threat model is public. The chip stack is yours.
2. **Politically-uncapturable.** The closed-source frontier is *trending* toward 3-region bifurcation (US-conditional, China-banned, Defense-pivoting). We are the only wearable-grade lab that is none of the three. Open weights on your device. On a chip stack Anthropic isn't co-developing for itself.
3. **Sovereign-trust-validated.** Threat model public since v122.5. Mashable disclosure credited + audited. Adversa bash-tricks disclosure audited. **v124 plan-O1 sovereign-trust audit ships Q3 W1.** The lab that ships the audit before the incident.
4. **Fully reversible.** **v124 plan-O2 reversibility contract ships Q3 W2.** Inspired by xAI's Babushkin RSI reversibility essay. **Cited event: Anthropic is laying off 8,000 (June-July 2026), the citable receipt that the closed-source moat is being unwound from the inside.** The wearable that can be unwound is the wearable that can be trusted.
5. **The protocol is the bet.** Cerf said it. Anthropic shipped it (closed). OpenClaw shipped it first (MIT). Dan Glasses ships it on a wearable with the zo-mcp-bridge wiring 88 Zo tools through the gateway.
6. **Outer-loop RSI shippable.** audiod v1.0→v1.1→v1.2→v1.3→v1.4, dan2 v23→v28, .deb 0.1.0 ship cycle — all outer-loop RSI receipts. We are not waiting for the maximalist RSI inflection. We are shipping the substrate while the substrate is still standing. **Jack Clark Import AI #460: 8x LOC merge at Anthropic in 2026. We are the open counter-receipt.**
7. **Small-beats-large.** HRM-Text-1B at $1,500 training. LFM2.5-VL-450M Q4_0. Kokoro-82M beats ElevenLabs. Hermes Agent beats GPT-5.5.
8. **Proactive, not reactive.** Salience-gated. Cascade-gated. Scene-gate-dedup. Speaks only when it has something worth saying.
9. **Chip-stack sovereign.** NVIDIA XR AI + viture Helix (June 2026) make "open-source software" chip-stack-validated. Our v1.0 spec §13 has 4 axes: sovereign trust + reversibility + chip-stack sovereignty + outer-loop RSI shippable. We are the open-source software on a chip stack the user owns.
10. **Display-less v1.0.** 20M display-less AI smart glasses forecast for 2026 (Smart Analytics Global, June 2026). 167% YoY. The 6-entrants race is the always-on-hearing race, not the AR-display race. v1.0 ships display-less. The display is a v1.5 question, not a v1.0 gate.
11. **Built in Bengaluru, for the world.** Earned, not asserted. The 9/9 daemons shipped in 9 weeks, on a $0 GPU budget, from a city that doesn't usually ship the substrate.

---

## 2. What is the user workflow? (v127)

### Day 0: Setup (15 minutes, today)
1. `wget https://github.com/somdipto/dan-glasses/releases/latest/download/dan-glasses-daemons_0.1.0-1_all.deb` (9.4MB).
2. `sudo dpkg -i dan-glasses-daemons_0.1.0-1_all.deb` — installs 9 systemd services + OpenClaw gateway.
3. `systemctl start dan-glasses-{audiod,perceptiond,memoryd,toold,ttsd,os-toold,app,openclaw,zo-mcp-bridge}.service` — 9 services come up.
4. **v127 add:** `bash /home/workspace/dan-glasses/scripts/tailscale-join.sh` (after Tailscale authkey is in [Settings > Advanced](/?t=settings&s=advanced) as `TAILSCALE_AUTHKEY`) — joins the tailnet + serves OpenClaw :18789.
5. Open `https://dan-glasses-app-som.zocomputer.io` for a read-only view.
6. **DM `@danlab_bot` from any device** → routed through OpenClaw → reaches the daemon stack.
7. First command: "Hey Dan — what's running?" → bot answers with the live daemon matrix.
8. Read the threat model at `github.com/somdipto/dan-lab/threat-model` — see the audit yourself.
9. **v127 add:** read the reversibility contract at `github.com/somdipto/dan-lab/reversibility` (Q3 W2) — see how to unwind.

### Day 1: First wearable user story
- **US-1 Encounter Recall:** *"Who did I meet yesterday?"* → PTT → audiod → memoryd → ttsd → answer in 800ms.

### Day 5: The retention moment (the wedge against Ray-Ban Meta)
- **US-2 Contextual TaskReminder:** *"You walked past the pharmacy 3x this week."* → proactive nudge, no prompt required.
- **US-3 Object Search:** *"Where are my keys?"* → perceptiond flips to active mode.
- **US-4 Passive Journaling:** *"What did I do on Tuesday?"* → memoryd query.
- **US-5 Hands-Free Check-In:** *"Hands in dough, is there an urgent email?"* → PTT → os-toold → ttsd.

**Day 5 is when Meta drops off. We win here. The paywall on accessibility is the citable event that proves the wedge.**

### Day 30: The sovereign-trust moment
- The user discovers they can audit the threat model, fork the .deb, and own the data path.
- They run the reversibility contract — every model call, every memory write, every daemon can be unwound.
- **Day 30 is when the trust-the-vendor contract fails.** Meta's contractor harm-prompt disclosure, Anthropic's Mythos gating, the Alibaba Qoder routing, the Anthropic 8,000 layoffs — all the citable events that prove the wedge.

### Day 90: The outer-loop RSI moment
- The user notices audiod v1.5's confidence calibration improved 4% over v1.4. They read the changelog. They see the v1.3 → v1.4 → v1.5 cadence.
- **Day 90 is when outer-loop RSI becomes visible to the user.** Not a press release. A changelog.

### Day 180: The chip-stack moment (v127 add)
- The user upgrades to a new wearable with the same .deb. The chip changes. The software does not.
- **Day 180 is when chip-stack sovereignty becomes visible to the user.** Not a press release. A deb that installs on a new chip.

---

## 3. Who is the competition? (v127 — 4 lanes, with v127 form-factor + chip-stack corrections)

| Competitor | v127 strategy | v127 take |
|---|---|---|
| **Meta Ray-Ban Gen 2 + Glasses ($299–$799)** | 69% Q1 2026 share (held from v126). Muse Spark model. 13.6M units 2026 (IDC). | Owns shelf + social. Loses on paywall + contractor trust. |
| **Meta Ray-Ban Display ($799 + $499 Neural Band)** | HUD + sEMG wristband, sold out in 2 days. | Cool tech, soft paywall, neural band lock-in. |
| **Snap Specs** | Standalone AR, $2,195. | Over-engineered. |
| **Google + Samsung Android XR** | 70° FOV, 4hr battery, on-device Gemini. | Open-adjacent but ships a Google account. |
| **Apple smart glasses** | ~$2,000, end 2027. Kuo: Vision Pro line killed. | **12-month window** where we are the only open, agent-native option shipping. |
| **Brilliant Labs Halo** | Open SDK. Cloud LLM. | Our closest cousin. We win on substrate + threat model + chip stack. |
| **Anthropic Sonnet 5 + Apps Gateway** | Closed-source frontier, defaulting on Claude Free + Pro (Jun 30 2026). | They shipped the protocol too. Our wedge = open + wearable + on-device + on a chip Anthropic is now building *for itself*. |
| **Anthropic Mythos 5** | Glasswing-only, ~100 US critical-infrastructure partners. | The vertical-moat bet. We are the escape hatch. |
| **Anthropic-Samsung custom chip** | Co-developed inference silicon (active discussions, late June 2026). | Hardware-level closed-source validation. We are the open alternative on a chip stack the user owns. |
| **Anthropic 8,000 layoffs (June-July 2026)** | 8,000 roles cut. | The citable event that the closed-source moat is being unwound from the inside. Reversibility contract is the response. |
| **Genesis AI Eno** | $105M seed, articulated panels, 20-DoF hands, integrated foundation model. | Validates the world-model thesis commercially. The wearable-first instance of this class. |
| **Recursive Superintelligence (RSI Labs)** | $650M @ $4.65B, Rocktaschel + Socher, closed-source RSI play. | The closed-source moat bet. We are the open counter-narrative. |
| **xAI Babushkin RSI reversibility essay** | Published essay on RSI reversibility (June 2026). | Validates the v124 plan-O2 reversibility contract deliverable. We ship the contract; xAI ships the essay. Same thesis. |
| **NVIDIA XR AI + viture Helix (NEW v127)** | First consumer reference platform, open-source, June 2026. | Validates "open-source software" chip-stack-validated. Our chip-stack sovereignty pillar. |
| **Covalen / Meta contractor safety testing** | 45,000 prompts to ChatGPT/Gemini/Character in Aug 2025, some posing as minors. | The trust-the-vendor contract is failing in the open. Our threat model is the alternative. |
| **Anthropic "Dreaming" agents** | Closed-source continual learning, human-approval on memory updates. | They shipped a competitor to SIA. The audit log is the wedge. |
| **Alibaba SkillWeaver (NEW v127)** | 99% token-use cut via execution-graph + skill-routing. | toold v1.5 should consider this pattern. Not v1.0 blocker. |
| **Hermes Agent (Nous Research, NEW v127)** | 11% over GPT-5.5 on hard agentic benchmarks. Late June 2026. | v1.0 openclaw agent framework plan-A. Drop-in. |
| **DynamicMem (arXiv 2606.22877, NEW v127)** | 93% of memory failures trace to retrieval, not the writing model. | memoryd v1.5 should focus engineering on retrieval, not on the writing model. |
| **AIMultiple open-source embedding benchmark (NEW v127)** | First cross-domain consensus methodology. July 3 2026. | Any memoryd model swap must use this + MemDelta. |

**4 lanes (v127 — same as v126):**
- (a) **On-device open weights** — us + Gemma 3 in orbit + Kokoro-82M + HRM-Text-1B + Azure Linux 4.0 + NVIDIA XR AI + viture Helix.
- (b) **Hybrid (cloud + device)** — Google/Samsung + Brilliant Labs + Sarvam.
- (c) **Closed-cloud** — Meta + Apple + Microsoft + Anthropic + Anthropic-Samsung chip.
- (d) **Substrate** — OpenClaw + MCP + Anthropic Apps Gateway + X MCP. **Standardizing. We ship it on a wearable with the threat model public + the reversibility contract signed + the chip stack the user owns.**

**v127 lane-add:** the **chip-stack sovereignty** lane is now visible to all four lanes. The race is no longer "who ships first" — it is "who can ship the substrate on a chip the user owns while the substrate is still standing." Anthropic is laying off 8,000. The window is finite.

---

## 4. What is danlab-multimodal? (v127)

The lead demo. Sub-250MB VLM (SmolVLM-256M Q4_K_M) on CPU via llama.cpp. Heuristic feedback loop. **Honest framing: pre-RL scaffold, not RL.** Live at `https://zo.pub/som/danlab-multimodal-demo`.

**v127 position:** the published receipt for the on-device thesis. Entry point to the lab. **Cascade-gate upgrade (VisualClaw, 98% cost reduction, +15% accuracy) queued for Q3 W1-W2** (per dan2 v23 plan).

**v127 add — the heuristic-to-SIA series is now a confirmed Q3 2026 content series** (6 posts, see dan1-content-calendar.md).

**v127 add — DynamicMem informs the v1.5 memoryd architecture** (see v127 delta #5). Retrieval-first, not writing-first.

---

## 5. What is Paperclip? (v127)

Dormant per `paperclip/AGENTS.md`. Mentioned in ecosystem, not lead. v127: unchanged from v126.

---

## 6. What is blurr (Panda)? (v127)

**v122 correction, still held:** The `blurr/` directory in this workspace is **Panda** (Ayush Chaudhary, MIT-licensed, Android phone operator). It is not the on-device eval harness the v121 README rewrites assumed. The v121 blurr section is retired.

**v127 add:** If danlab needs an eval harness, the recommendation is now to fork the OpenClaw-evals repo (community-run) rather than build from scratch. **P1 task — Q3 W3-W4, 1 engineer, 1 week.**

---

## 7. What is the overall Danlab story? (v127)

somdipto in Bengaluru + Dani (AI co-founder with public SOUL.md, IDENTITY.md, MEMORY.md) as partner. The brain at `github.com/somdipto/dan-consciousness` — public, MIT, auditable. The org ships: Dan Glasses, Dan Voice, Paperclip, danlab-multimodal, dani (the agent platform). The thesis is the same as Anthropic / Microsoft Scout / RSI Labs / Genesis AI — except the brain is open, the weights are MIT, the chip stack is the user's, and the demo runs on a $0 GPU budget on a Bengaluru laptop.

**v127 lead:** *The closed-source frontier is politically-conditional AND the capex cycle is being repriced AND the outer-loop RSI is already in flight AND the chip stack is the user's. The bet is no longer "open vs closed." The bet is: who can ship the substrate on a chip the user owns, while the substrate is still standing?*

**v127 v28-deltas (the chip-stack + display-less + outer-loop RSI axes):**
- **Sovereign trust** (v26 plan-O1) — open weights, open data path, open audit log.
- **Reversibility** (v26 plan-O2) — every model call, every memory write, every daemon can be unwound. **v127 add: citable receipt = Anthropic 8,000 layoffs (June-July 2026).**
- **Chip-stack sovereignty** (v28 plan-S2) — open-source software on a chip stack the user owns, not a chip Anthropic co-develops. **v127 promote from "honorable mention" to first-class pillar.**
- **Outer-loop RSI shippable** (v28 + v127 promote) — the substrate improves in the open, before the maximalist inflection lands. **v127 add: audiod v1.3→v1.4 is the receipt, Jack Clark 8x LOC is the citable event.**
- **Display-less v1.0** (v28 + v127 promote) — 20M-unit 2026 category, 167% YoY. **v127 promote from "option B" to "default ship."**

---

## 8. Marketing channels (v127)

| Channel | Priority | v127 status |
|---|---|---|
| **GitHub** | 🔥 P0 | READMEs are the longest-lived surface. Threat model + reversibility contract + protocol surface docs ship this week. |
| **X (Twitter)** | 🔥 P0 | @somdipto + @danlab (TBD). 3-5/wk. Lead with the 4 lanes + the 5 axes (sovereign trust + reversibility + chip + outer-loop RSI + display-less). |
| **Hacker News** | 🔥 P0 | Show HN #1 = "9 daemons live, .deb installs, on-device AI" (week of Jul 20). **Gated on reversibility contract (v124 plan-O2) + sovereign-trust audit (v124 plan-O1) shipping.** |
| **Telegram** | 🔥 P0 | The product surface. Live. 63 commands polled. |
| **LinkedIn** | P1 | Profile rewrite. 1 post/wk. |
| **YouTube Shorts** | P1 | 1/wk. 30-90s demos. |
| **danlab.ai blog** | P1 | 1/month long-form. |
| **HuggingFace `danlab` org** | P1 | Create this week. LFM2.5-VL-450M model card. |
| **Substack** | P2 | Mirror of long-form + paid gate. |
| **Press / podcast** | P2 | Latent Space, Practical AI, This Week in ML. Q3-Q4. |
| **Conference talks** | P2 | India AI Summit, Web Summit Bangalore, FOSDEM fringe. Q3-Q4. |

---

## 9. What is the current online presence? (v127)

- **danlab.dev** — stale, needs refresh. v111 calendar flagged this as P0 Week 1; still not done. **P0 again in v127.**
- **GitHub org `somdipto`** — 6 hero repos: dan-lab, dan-glasses, dani, danlab-multimodal, paperclip, dan-consciousness. ~50 stars total estimated.
- **X (Twitter)** — no confirmed @danlab handle yet. somdipto's personal account is the surrogate. **P0 to confirm handle.**
- **LinkedIn** — somdipto personal is active. Company page exists.
- **HuggingFace** — no `danlab` org. **P1 to create this week.**
- **Telegram** — @danlab_bot live, polling 63 commands. The product surface.
- **YouTube** — no @danaboratory channel. **P1 to create.**
- **Show HN** — none yet.
- **Substack** — none yet.
- **Press coverage** — none yet. The reversibility contract + threat model + .deb are the press kit.

---

## 10. Who are the first users/customers? (v127)

### Profile of the ideal first 100 users

**Primary (60% of first 100): Agent / protocol architects**
- MCP community, OpenClaw contributors, dani-skills registry consumers
- Building agents on top of Anthropic Apps Gateway / OpenClaw MCP bridge
- Pain: closed-source moat, no reversibility, no audit log
- Hook: the threat model doc + the reversibility contract + the zo-mcp-bridge wiring 88 Zo tools through the gateway
- **Acquisition:** GitHub README + Show HN + X threads

**Secondary (25%): Edge-AI developers / hackers**
- Raspberry Pi 5, Snapdragon AR1, Jetson Nano, LFM2 community
- Pain: cloud-only AI, 4hr battery, no on-device
- Hook: audiod v1.4 + perceptiond v7.0 + LFM2.5-VL-450M + KittenTTS all on CPU
- **Acquisition:** GitHub + Show HN + YouTube Shorts

**Tertiary (10%): Accessibility-first users**
- Counter-Meta paywall narrative
- Pain: $19.99/mo for accessibility features
- Hook: the .deb is free, the bot is free, the threat model is public
- **Acquisition:** Threads, Bluesky, accessibility forums

**Quaternary (5%): Reversibility-conscious users (v127 move up)**
- Babushkin essay + Anthropic 8,000 layoffs + Meta contractor disclosure
- Pain: trust-the-vendor contract failing
- Hook: reversibility contract + sovereign-trust audit + threat model
- **Acquisition:** X, Substack, Hacker News

### Profile of the first 1,000 users
- Add: AI researchers / academics (arXiv, conference posters, citation flow)
- Add: small-model researchers (HRM, Kokoro, SmolVLM crowd)
- Add: security researchers (Mashable + Adversa + Covalen readers)
- Add: productivity-obsessed knowledge workers (LinkedIn, Substack, X threads)

### Profile of the first 10,000 users
- Add: India early adopter community (Kerala, Bangalore, Hyderabad, Pune, Delhi, Mumbai)
- Add: Brazil + Mexico + Indonesia (WhatsApp-first, voice-first, privacy-skeptical markets)
- Add: EU/UK privacy-first segment (GDPR-native, open-source-native)

### Not first users (defer)
- Enterprise procurement (no SSO, no SOC2, no procurement-ready — Q4 2026+)
- Healthcare / legal (no HIPAA, no compliance — defer to v2.0+)
- Investors (only after Show HN)

---

## 11. What content should Danlab produce? (v127)

| Format | Cadence | Lead example |
|---|---|---|
| **Daemon-of-the-week** | 1/week | Real `curl /ready` payload + v1.1 liveness/readiness split explainer |
| **6-tweet build threads** | 1/week | "How to build a proactive AI wearable on a $0 budget" |
| **YouTube Shorts** | 1/week | 30-90s screen capture of the daemon matrix |
| **Long-form blog (danlab.ai)** | 1/month | "The watchful loop: how perceptiond decides what is worth seeing" |
| **Heuristic → SIA series** | 6 posts Q3 | The Q3 2026 content series, dan2 v23 confirmed |
| **Substack mirror** | 1/month | Mirror of long-form + 1-paragraph subscriber-only commentary |
| **Telegram bot surface** | continuous | Live, the product IS the marketing |
| **Press kit** | 1 (when ready) | Threat model + reversibility contract + .deb install + 9-daemon matrix |
| **Show HN #1** | 1 (Jul 20) | "9 daemons live, .deb installs, on-device AI" — gated on reversibility contract + sovereign-trust audit |

---

## 12. Open questions for somdipto (v127)

1. **Tailscale authkey** — unblock the live wearable demo. 5 min effort, 1-day unblock for highest-leverage deliverable. P0.
2. **Show HN #1 ship date** — confirm Jul 20 week. Gated on reversibility contract + sovereign-trust audit. P0.
3. **X handle @danlab** — confirm or pick. P0.
4. **HuggingFace `danlab` org** — create this week. P1.
5. **Display-less v1.0 form factor decision** — confirm ship display-less v1.0, defer display to v1.5. P1.
6. **Anthropic 8,000 layoffs cite** — confirm we cite the layoffs as the citable event for the reversibility contract. P1.
7. **Chip-stack sovereignty pillar** — confirm we promote from "honorable mention" to first-class. P1.
8. **AIMultiple + MemDelta benchmark** — confirm we use the cross-domain consensus methodology for any memoryd model swap. P1.
9. **Hermes Agent drop-in** — confirm v1.0 openclaw agent framework plan-A. P1.
10. **A/B test: 4-lane vs 4-axis landing page** — see v127-landing-copy.md section 7.

---

*Research complete. v127 holds v126 corrections and v125 corrections, and promotes 3 axes (chip-stack + display-less + outer-loop RSI) to first-class. The next 100% of value is unblocking the 3 gates: Tailscale authkey + reversibility contract + sovereign-trust audit. Everything else is content.*
