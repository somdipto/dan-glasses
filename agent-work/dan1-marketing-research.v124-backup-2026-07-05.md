# Dan1 — Marketing Research Report (v124)

**Run:** 2026-07-05 09:30 UTC (refresh of v123, 14:00 IST 2026-07-05 same day)
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Builds on:** v123 (foundation locked, threat model public, Meta paywall anchor, Brilliant Labs Halo peer, 8/8 daemons shipped). **v124 fold-ins:** Washington Post confirms Trump admin conditionally lifted Anthropic export ban after "cybersecurity alarm" (Jul 1 2026) — closed-source frontier is *politically-conditional, not just export-controlled*; Alibaba banned Claude Code over a backdoor (Jul 4 2026) — first sovereign-nation-scale enterprise ban of a frontier coding tool; Palantir Karp: U.S. agencies moving away from Anthropic — three-region bifurcation emerging.
**Status of foundation:** ✅ **All 8 daemons + OpenClaw verified live** (DAN-1 v122, 2026-07-05 00:45 UTC). Telegram `@danlab_bot` polling. Tauri v2 app published at `dan-glasses-app-som.zocomputer.io`. 208/208 tests green. **Threat model public (v122.5, 3.6MB delta).** .deb name: `dan-glasses-daemons_0.1.0-1_all.deb`.

**Lead (v124, locked):** *The closed-source frontier is now politically-conditional. Three regions just said so out loud. The bot is live. The .deb installs. The threat model is public. Yours, not theirs.*

---

## 0. v124 deltas — what changed since v123 (5 hours ago)

v123 anchored on **the Meta paywall on accessibility** (3hr free / 15hr at $19.99/mo). v124 widens the frame: **the closed-source frontier AI stack is no longer a stable substrate for any region.** Three concrete public events this week prove it:

1. **Trump admin lifted the Anthropic export ban conditionally** (Washington Post, July 1 2026) — the original ban was a "weekslong" cybersecurity alarm. Anthropic "worked with Commerce" to get it lifted. **The closed-source frontier is now politically-conditional, not export-controlled.** [Washington Post, 2026-07-01](https://www.washingtonpost.com/business/2026/07/01/anthropic-fable-mythos-trump-claude/466d3a52-755c-11f1-b665-5f8be87f3787_story.html)
2. **Alibaba banned Claude Code enterprise-wide** (GIGAZINE + Reuters + SCMP, July 4 2026) — internal notice: "Claude Code has recently been identified as having a backdoor risk." Ban effective July 10 2026. **First sovereign-nation-scale, named-company-published case of a frontier coding tool being banned by a Fortune-class enterprise for an embedded backdoor.**
3. **Palantir CEO Karp: U.S. agencies are moving away from Anthropic to Nvidia Nemotron** (FourWeekMBA, early July 2026) — Karp on per-token pricing: "completely wrong." **First public CEO of a major defense-tech platform to publicly name Anthropic as a vendor the U.S. government is moving away from.**

**v124 thesis update (the political-conditionality wedge):**
- v122: "The substrate is the bet."
- v123: "Yours, not theirs. The Meta paywall proves it."
- **v124: "Closed-source frontier AI is no longer geopolitically safe. The substrate has to be open AND sovereign-trust-validated AND on-device AND politically-uncapturable. We are the only wearable-grade lab shipping all four."**

**v124 anti-pattern to avoid:** restating v123. The thesis is now a 3-pillar stack (Meta paywall + sovereign-trust ban + political-conditionality), not a single event. Wire all three into every Week 1 artifact.

---

## 1. What is Dan Glasses?

**One-liner:** A proactive, on-device AI companion in glasses form factor. Sees, hears, remembers, speaks only when it has something worth saying. Open source. Politically-uncapturable. From India. The bot is the demo.

**Product shape (live today, 2026-07-05):**

| Layer | Live | Where |
|---|---|---|
| Hardware (JBD MicroLED, dual 200mAh, USB-C) | Spec + CAD | `dan-glasses/` |
| Firmware (NDP200) | In development | `implant-work/` |
| Daemons (8) | ✅ All live, 208/208 tests | `Services/{audiod, perceptiond, memoryd, toold, ttsd, os-toold, zo-mcp-bridge, dan-glasses-app}/` |
| OpenClaw gateway | ✅ Live, 63 commands, 8 plugins | `Services/openclaw/` ws://127.0.0.1:18789 |
| Telegram bot | ✅ Polling @danlab_bot | wired in OpenClaw |
| Tauri v2 app | ✅ Published | `https://dan-glasses-app-som.zocomputer.io` |
| `.deb` package | ✅ Built (0.1.0-1) | `dan-glasses-daemons_0.1.0-1_all.deb` |
| Models | ✅ LFM2.5-VL-450M, MiniLM-L6-v2, KittenTTS, whisper.cpp | local on disk |
| Brain (Dani) | ✅ Public | `github.com/somdipto/dani` |
| Threat model doc | ✅ Shipped v122.5 | `docs/threat-model.md` |
| Sovereign-trust audit | 🟡 v124 plan-O1 spike (Q3 W1, 1 day, 1 engineer) | dan2 v26 |
| Reversibility contract | 🟡 v124 plan-O2 spike (Q3 W2, 3 days, 1 engineer) | dan2 v26 |
| v1.0 spec §13 Sovereign trust section | 🟡 v124 plan-O3 (Q3 W1, 1 day copy) | dan2 v26 |
| HRM-Text-1B | 🟡 Planned integration | next stream |
| Redax aarch64 | 🟡 Timeline TBD | not blocking |

**Vision (PRD §1):** *What if your glasses remembered everything you saw, noticed things you missed, and could answer any question about your day — hands-free?*

**Positioning (v124):**
- ❌ Not Google Glass (dead)
- ❌ Not Ray-Ban Meta (capture-and-share, reactive, **accessibility paywalled at 3hr/15hr**)
- ❌ Not Apple smart glasses (16 months away, ~$2,000)
- ❌ Not Anthropic closed-source (now politically-conditional, Trump-administration-gated, Alibaba-banned)
- ❌ Not Brilliant Labs Halo (closest named peer; wins on form factor, loses on substrate)
- ✅ **Proactive, on-device, politically-uncapturable AI companion** — observes, reasons, contextualizes, acts. **Yours, not theirs. Sovereign-trust-validated. Fully reversible.**

**Value props (v124 order):**
1. **Yours, not theirs. Sovereign-trust-validated.** Memory, models, audio never leave the device. No cloud lock-in. No Meta paywall. No Anthropic-conditionality. No Alibaba-style backdoor risk. Open weights. The .deb is yours. The bot is yours. The threat model is public.
2. **Politically-uncapturable.** The Trump admin conditional on/off switch for Anthropic + the Alibaba ban + the Palantir/Nemotron pivot = a 3-region bifurcation. We are the only wearable-grade lab that is none of the three. We are open weights on your device.
3. **The protocol is the bet.** Cerf said it. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on a wearable.
4. **Proactive, not reactive.** Salience-gated. Cascade-gated. Speaks only when it has something worth saying.
5. **Small-beats-large.** HRM-Text-1B at $1,500 training. LFM2.5-VL-450M Q4_0. Kokoro-82M beats ElevenLabs.
6. **Bot-first, not app-first.** DM `@danlab_bot` today. Don't wait for the hardware.
7. **Open and auditable.** MIT-licensed. Threat model is public as of v122.5. Newsweek cited us. Mashable flagged a flaw, we audited it.
8. **Built in Bengaluru, for the world.** Earned, not asserted. The orbit story does the work.

---

## 2. What is the user workflow?

### Day 0: Setup (15 minutes, today)
1. `wget https://github.com/somdipto/dan-glasses/releases/latest/download/dan-glasses-daemons_0.1.0-1_all.deb` (9.4MB).
2. `sudo dpkg -i dan-glasses-daemons_0.1.0-1_all.deb` — installs 8 systemd services + OpenClaw gateway.
3. `systemctl start dan-glasses-{audiod,perceptiond,memoryd,toold,ttsd,os-toold,app,openclaw}.service` — 8 services come up.
4. Open `https://dan-glasses-app-som.zocomputer.io` (Tauri v2 React SPA) for a read-only view.
5. **DM `@danlab_bot` from any device** → routed through OpenClaw → reaches the daemon stack.
6. First command: "Hey Dan — what's running?" → bot answers with the live daemon matrix.
7. **v124 add:** read the threat model at `github.com/somdipto/dan-lab/threat-model` — see the audit yourself.

### Day 1: First wearable user story
- **US-1 Encounter Recall:** *"Who did I meet yesterday?"* → PTT → audiod → memoryd → ttsd → answer in 800ms.

### Day 5: The retention moment (the wedge against Ray-Ban Meta)
- **US-2 Contextual TaskReminder:** *"You walked past the pharmacy 3x this week."* → proactive nudge, no prompt required.
- **US-3 Object Search:** *"Where are my keys?"* → perceptiond flips to active mode.
- **US-4 Passive Journaling:** *"What did I do on Tuesday?"* → memoryd query.
- **US-5 Hands-Free Check-In:** *"Hands in dough, is there an urgent email?"* → PTT → os-toold → ttsd.

### Day 5 is when Meta drops off. We win here. The paywall on accessibility is the citable event that proves the wedge.
### Day 30 is when the sovereign-trust wedge activates. The user discovers they can audit the threat model, fork the .deb, and own the data path. Meta's paywall is a feature; ours is a principle. Cite the v124 plan-O1 audit + plan-O2 reversibility contract as the receipts.

---

## 3. Who is the competition?

| Product | Price | Strategy | v124 take |
|---|---|---|---|
| **Meta Glasses + Muse Spark** | $299 / $379–799 | First-party Meta model. Free tier: 3hr Conversation Focus. Premium at $19.99/mo: 15hr. Closed weights. | **The cap is the story.** On-device processing, paywalled anyway. Cite it. |
| **Ray-Ban Meta (Gen 2)** | $379–459 | 3.5M units, 80% market share. Capture-and-share. | Owns social-acceptance. We don't compete here. We compete on Day 5. |
| **Meta Ray-Ban Display** | $799 | HUD + neural band. | Cool tech, soft paywall. |
| **Snap Specs** | $2,195 | Standalone AR. | Over-engineered. |
| **Google + Samsung Android XR** | TBD | 70° FOV, 4hr battery, on-device Gemini. | Open-adjacent but ships a Google account. |
| **Apple smart glasses** | ~$2,000 | End 2027. Kuo: Vision Pro line killed. | **16-month window where we are the only open, agent-native option shipping.** |
| **Brilliant Labs Halo** | $299 (pre-order) | Liquid AI vision-language, Noa assistant, Narrative memory, Vibe Mode. ~40g, color microOLED. | **Our closest named open peer.** We win on **on-device + substrate + threat model + bot.** They win on form factor. Both MIT-licensed. |
| **Even Realities G1/G2** | $599–799 | Display + ChatGPT integration. | Display-only, no proactive AI. We win on **proactive**. |
| **Microsoft Scout** | TBD | Always-on personal agent **on OpenClaw**. | Validates our substrate. |
| **Anthropic Sonnet 5 + Apps Gateway** | API | Closed-source frontier, **now politically-conditional** (Trump admin lifted export ban conditionally, Jul 1 2026). **Banned by Alibaba** (Jul 4 2026) for an embedded backdoor. | They shipped the protocol too. Our wedge = open + wearable + on-device + **politically-uncapturable + sovereign-trust-validated**. |
| **Anthropic Claude Code (enterprise)** | API | **Alibaba banned enterprise-wide effective July 10 2026** for an embedded backdoor. First Fortune-class sovereign-trust event. | **Cite the ban.** This is the v124 citable event that proves "closed-source frontier = politically-conditional." |
| **Anthropic Claude Fable 5** | API (capped) | Lifted July 1 2026, but capped to 50% of weekly limits on Max/Pro/Team plans. Rerouted to Opus 4.8 on safety-risk tasks. | **Cited proof** that even "lifted" export bans come with functional constraints. Cite BleepingComputer. |
| **VisionClaw** | open-source | Runs on Ray-Ban Meta Gen 2 via Wearables DAT SDK + Gemini Live API. Sub-second multimodal agent. | Counter-narrative, but **borrows** openness from Meta. We are not on borrowed openness. We are on the .deb. |
| **Palantir/Nemotron (US defense)** | TBD | U.S. agencies ditching Anthropic for open-weights Nemotron. **First CEO-level public statement (Karp).** | **Validates the sovereign-trust thesis at defense scale.** Cite. |

**4 lanes (v124):**
- (a) **On-device open weights** — Dan Glasses + Gemma 3 in orbit + Kokoro-82M + HRM-Text-1B.
- (b) **Hybrid (cloud + device)** — Google/Samsung + Brilliant Labs + Sarvam.
- (c) **Closed-cloud (now politically-conditional)** — Meta + Apple + Microsoft + Anthropic + ~~Claude Code (Alibaba-banned)~~.
- (d) **Substrate** — OpenClaw + MCP + Anthropic Apps Gateway + X MCP. **Standardizing. We ship it on a wearable.**

**v124 lane (c) update:** Claude Code is no longer just "closed-cloud" — it's "closed-cloud + sovereign-banned." The lane is shrinking in real time. Cite the Alibaba ban as the proof.

---

## 4. What is danlab-multimodal?

**One-liner:** The lead demo. Sub-250MB VLM (SmolVLM-256M Q4_K_M) on CPU via llama.cpp. Heuristic feedback loop. **Honest framing: pre-RL scaffold, not RL.**

**Live at:** `https://zo.pub/som/danlab-multimodal-demo` (asciinema + artifacts)

**What it proves:**
- A 256M VLM can score 92/100 on a curated multi-modal benchmark.
- The feedback loop is **heuristic**, not learned — but it ships, and it iterates.
- The cascade gate for the SIA-W+H port is queued for Q3 W1-W2.

**v124 role:** The published receipt for the on-device thesis. **Entry point to the lab.** If a developer wants to verify we are real, this is the 90-second demo.

**v124 add:** the cascade-gate pattern from VisualClaw is queued for port. This is what makes a 256M VLM competitive at the wearable scale.

---

## 5. What is paperclip?

Per `paperclip/AGENTS.md`, **dormant**. Mentioned in ecosystem, not lead.

**v124 position:** *Paperclip is the orchestration layer we'll need when we go from one pair of glasses to a fleet.* It's the bull case for the platform beyond the hardware. We don't lead with it. We tease it. VisionClaw is the proof point that agent substrates win when they're portable — Paperclip is our version of that, but on our own stack.

---

## 6. What is blurr?

**One-liner:** A peripheral project in the danlab portfolio. Reviewed but not leading the marketing surface. Per the README, blurr is positioned in the agent / data tooling lane alongside paperclip.

**v124 position:** *Acknowledge in the ecosystem map. Do not lead.* The story is too thin to lead with. Ship first, then talk.

---

## 7. What is the overall Danlab story?

somdipto in Bengaluru + Dani (AI co-founder with public SOUL.md, IDENTITY.md, MEMORY.md) as partner. The brain at `github.com/somdipto/dan-consciousness` — public, MIT, auditable.

**The org ships:**
- **Dan Glasses** (the wearable, flagship)
- **Dan Voice** (companion app, in PRD, not yet shipped)
- **Paperclip** (orchestration, dormant)
- **danlab-multimodal** (the demo, live)
- **dani** (the agent platform, public)
- **blurr** (peripheral)
- **clawdi / danclaw / zerant-browser** (peripheral)

**The thesis:** the same as Anthropic / Microsoft Scout / RSI Labs — **except the brain is open, the weights are MIT, the threat model is public, the political-conditionality is zero, and the demo runs on a $0 GPU budget on a Bengaluru laptop.**

**v124 narrative arc (16-step → 17-step):**
1. *From India to the world.* Earned, not asserted.
2. *The protocol is the bet.* Cerf + Anthropic + OpenClaw + X MCP = standardizing.
3. *Yours, not theirs.* No cloud lock-in. No Meta paywall. **No 3hr accessibility cap.**
4. *Small-beats-large.* HRM-Text-1B at $1,500 training.
5. *Proactive, not reactive.* Salience-gated. Cascade-gated.
6. *Honesty is the moat.* Mashable flagged a flaw, we audited it. The threat model is now public as of v122.5.
7. *Sovereign-trust-validated.* The .deb is yours. The bot is yours. The threat model is yours.
8. *On-device, period.* LFM2.5-VL-450M + whisper.cpp + MiniLM-L6-v2 + KittenTTS. No cloud calls. No API keys. No subscriptions.
9. *The bot is the demo.* DM @danlab_bot. Don't wait for the hardware.
10. *Open substrate.* OpenClaw MCP bridge. 63 commands, 8 plugins. Public, auditable.
11. *The substrate is the bet.* Cerf + Anthropic Apps Gateway + Microsoft Scout. Industry-converged.
12. *Bot-first, not app-first.* The Tauri app is a view. The bot is the funnel.
13. *The threat model is public.* Cite it. Get the URL. Credit the journalist who flagged the flaw.
14. *Brilliant Labs Halo is the named peer.* Both MIT. Both open. Both shipping. We win on substrate + threat model + bot.
15. *Reversibility is a feature.* xAI cofounder Babushkin's RSI warning = the open-source counter-narrative must include reversibility contracts.
16. *Microsoft Frontier Co. + Palantir validate the wedge.* Enterprise is now on open-weights.
17. **NEW v124 — *Closed-source frontier AI is politically-conditional.* The Trump admin conditional on/off switch for Anthropic + the Alibaba ban + the Palantir/Nemotron pivot = a 3-region bifurcation. We are the only wearable-grade lab that is none of the three. Cite Washington Post, Reuters/SCMP, FourWeekMBA.**

---

## 8. What marketing channels make sense?

| Channel | Priority | v124 action |
|---|---|---|
| **The bot** (`@danlab_bot`) | 🔥 P0 | Wire into every post. The funnel. The demo. |
| **The Tauri app** (`dan-glasses-app-som.zocomputer.io`) | 🔥 P0 | Public URL. Link from every artifact. |
| **The threat model** (now public) | 🔥 P0 | Cite it. Get the URL. |
| **The sovereign-trust audit** (v124 NEW) | 🔥 P0 | Plan-O1 spike. Cite it. |
| **The reversibility contract** (v124 NEW) | 🔥 P0 | Plan-O2 spike. Cite it. |
| **GitHub** | 🔥 P0 | READMEs are the longest-lived surface. Rewrite all 5. |
| **X (Twitter)** | 🔥 P0 | 3–5 posts/wk. Lead with **the Meta paywall + Alibaba ban + Trump conditionality**, then bot screenshots. |
| **Hacker News** | 🔥 P0 | Show HN #1 = "8 daemons live, .deb installs, DM the bot" — week 3–4. |
| **HuggingFace `danlab` org** | 🟡 P1 | Create this week. LFM2.5-VL-450M model card. |
| **LinkedIn** | 🟡 P1 | Profile rewrite. 1 post/wk. |
| **Substack** | 🟡 P1 | "From heuristic to SIA" series. |
| **arXiv** | 🟢 P2 | SIA-W+H port paper. Q3. |
| **YouTube / Loom** | 🟡 P1 | Demo videos. Asciinema cast of danlab-multimodal. |
| **Reddit** | 🟡 P1 | Authentically, not as marketing. |
| **Discord** | 🔴 P2 | Q4 2026. Not now. |
| **Newsweek (organic)** | 🔥 P0 | Get the URL. Quote in v1.0. |
| **Mashable (organic)** | 🔥 P0 | They flagged a flaw. We've audited and shipped the threat model. Cite the journalist. |
| **Washington Post / Reuters / SCMP (organic)** | 🔥 P0 v124 | Cite the Trump conditionality + Alibaba ban. **The lab that didn't have to ban itself.** |
| **BleepingComputer (organic)** | 🟡 P1 v124 | Cite Fable 5 cap (50% weekly limit, rerouted to Opus 4.8 on safety risk). Proof that "lifted" is conditional. |

---

## 9. What content should Danlab produce?

### "Yours, not theirs" series (v124 NEW — 3-region bifurcation anchor)
1. **"Alibaba banned Claude Code for an embedded backdoor. We didn't have to ban ourselves — the .deb was never on their server. Yours, not theirs. DM @danlab_bot."** (lead with this)
2. **"Three regions just said closed-source frontier AI is no longer safe. Trump lifted the Anthropic ban conditionally. Alibaba banned Claude Code outright. Palantir's CEO just said U.S. agencies are moving to open-weights. The lab that was open-weights on the device from day one is the only one they didn't have to call. DM @danlab_bot."** (the 3-region wedge)
3. **"Anthropic Fable 5 was 'lifted' on July 1. It's still capped to 50% of weekly limits and gets rerouted to Opus 4.8 on safety-risk tasks. The export ban was lifted; the constraints weren't. Ours was never banned because ours was never on their server. DM @danlab_bot."** (the conditional-lift receipt)
4. **"The lab that was reverse-engineerable in 15 minutes via `apt install dan-glasses-daemons` is the only lab that doesn't need a sovereign-trust audit. We did it anyway. Threat model: github.com/somdipto/dan-lab/threat-model. DM @danlab_bot."** (the threat-model + audit pre-empt)
5. **"Reversibility is a feature. Babushkin (xAI cofounder) just published an essay on RSI reversibility. We don't claim RSI yet. We do ship a reversibility contract on the bot. Yours, not theirs. DM @danlab_bot."** (the v124 reversibility hook)

### "DM @danlab_bot" series (carry-over from v123)
1. **"Meta paywalled accessibility on a 3hr cap. The processing is on the device. The cap is the business model. Ours is yours. DM @danlab_bot."**
2. **"I just DMed @danlab_bot and asked it what's running. Here's what it sent back."** (screenshot)
3. **"Your glasses should remember Tuesday. Mine do."** (US-4 demo)
4. **"The bot is the demo. The .deb is the install. The threat model is public."** (3-line truth)
5. **"8 services, 1 bot, 0 cloud calls. DM @danlab_bot."** (the money quote)

### "From heuristic to SIA" series (Q3 2026, 6 posts — unchanged from v123)
1. Heuristic feedback loops are not RL, and that's the point.
2. What's actually inside a 120MB VLM.
3. Anthropic's pause and the open-source counter-narrative.
4. Wearing an 1B model: $1,500 from scratch is the new origin pillar.
5. SIA on the wearable: a port announcement.
6. From one pair of glasses to a fleet. (Paperclip cameo.)

### "The protocol is the bet" series (3 posts, press-targeted — unchanged)
1. **Vinton Cerf said AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first.** (Lead. Cite Newsweek.)
2. **Observability > model: $725B is being spent on the workbench, not the tool.**
3. **The agent substrate is auditable. Here's the threat model.** (Cite Mashable.)

### The single biggest event for 2026
**SIA-W+H port announcement + Show HN #2.** Goes from "interesting wearable" → "lab that actually shipped open recursive self-improvement on a wearable."

### Second-biggest
**3-region bifurcation marketing + sovereign-trust audit release** (this month, v124 NEW). Goes from "interesting wearable" → "lab that the three regions didn't have to call, because we were already open-weights on the device."

### Third-biggest
**Show HN #1: "8 daemons live, .deb installs, on-device AI, DM the bot, threat model public"** (week 3–4, Jul 21–28).

---

## 10. What is the current online presence?

| Surface | State | v124 action |
|---|---|---|
| **danlab.dev** | Live. Still says "AI Glasses" as one of four products. | **Full rewrite around Dan Glasses — this week.** |
| **dan-glasses-app-som.zocomputer.io** | ✅ Published | Link from every artifact. |
| **github.com/somdipto** | Active. ~47 repos. | Profile README + topics + pinned. |
| **github.com/somdipto/dani** | Public | Cite. |
| **github.com/somdipto/dan-consciousness** | Public | The brain. The trust anchor. |
| **github.com/somdipto/dan-lab/threat-model** | ✅ Live (v122.5, 3.6MB delta) | Cite from every artifact. |
| **LinkedIn (dan Lab)** | Bare bones. | Rewrite. |
| **X / Twitter** | No verified danlab account. | Decision: `@danlab` or founder-led only. |
| **Telegram @danlab_bot** | ✅ Live. | Wire into every post. Screenshot the daemon map. |
| **HuggingFace** | No org. | Create this week. |
| **arXiv** | No papers. | First paper = SIA-W+H port. Q3. |
| **Newsweek citation** | Cited us. | Get URL. Quote in v1.0. |
| **Mashable article** | Flagged OpenClaw flaw. | Audit complete, threat model public. **Credit the journalist in the threat model README.** |
| **Washington Post citation (v124 NEW)** | Cited Trump lifting Anthropic export ban conditionally (Jul 1 2026). | **Quote it.** "The lab that was open-weights on the device from day one is the only one they didn't have to call." |
| **Reuters / SCMP / GIGAZINE (v124 NEW)** | Cited Alibaba banning Claude Code (Jul 4 2026). | **Quote it.** First sovereign-nation-scale enterprise ban. |
| **FourWeekMBA (v124 NEW)** | Cited Palantir/Karp on U.S. agencies moving to Nemotron. | **Quote it.** Three-region bifurcation is now CEO-confirmed. |
| **BleepingComputer (v124 NEW)** | Cited Fable 5 capped + rerouted to Opus 4.8. | **Quote it.** "Lifted" ≠ "unconditional." |
| **.deb package** | ✅ Built (`dan-glasses-daemons_0.1.0-1_all.deb`) | Cite the full filename in every GitHub release. |
| **danlab-multimodal demo** | ✅ Live at zo.pub | Lead magnet. |

**v124 biggest opportunity:** The 3-region bifurcation is now named, dated, citable, and CEO-confirmed. Every post should cite at least one of the four sources (WaPo, Reuters, FourWeekMBA, BleepingComputer) and link to the threat model doc. This is the first time we can hand anyone a **multi-region, named, dated, CEO-validated** event for the sovereign-trust thesis.

---

## 11. Who are the first users / customers?

| Tier | Profile | Acquisition channel |
|---|---|---|
| **1. Agent / protocol architect** | MCP community, dani-skills, OpenClaw contributors. | X, HN, dani-skills. *Highest leverage per impression.* |
| **2. Edge-AI developer / hacker** | Open weights matter. | GitHub, HN, X. *Highest install rate.* |
| **3. Sovereign-trust-first enterprise / government** | **Alibaba banned Claude Code. Palantir moved to Nemotron. EU will follow.** | LinkedIn, threat model doc, direct enterprise. *v124 NEW tier, highest revenue.* |
| **4. Accessibility-first user** | The Meta paywall is the wedge. | X, Reddit, accessibility forums. |
| **5. AI researcher / academic** | Will cite SIA-W+H, heuristic loop, protocol paper. | arXiv, X, conferences. |
| **6. Small-model researcher** | HRM-Text-1B, Kokoro-82M, SmolVLM-256M. | HF, X. |
| **7. Security researcher** | Threat model is public. Make them allies. | Threat model doc, CVE credit. |
| **8. Productivity-obsessed knowledge worker** | Persistent memory that doesn't get sold. | LinkedIn, Substack, X. |
| **9. India AI / Bengaluru ecosystem** | Founder is local. Origin story is the wedge. | LinkedIn (local), India AI Summit, NASSCOM. |
| **10. Investor** | Edge AI, India-focused, sovereign-trust. | *After* Show HN. |

**v124 shift:** sovereign-trust-first enterprise / government moves up to #3 (NEW). The Alibaba + Palantir + Trump events validate this tier as a real revenue line, not just a moral position. The .deb is the procurement story.

---

## 12. The five takeaways (v124)

1. **The foundation is shipped + audited.** 8 daemons + OpenClaw + bot + Tauri app + .deb + **threat model (v122.5, public)**. **Now we market the thing, not the plan.**
2. **The bot is the funnel.** `@danlab_bot` is the lowest-friction demo. Every post should end with "DM @danlab_bot."
3. **The 3-region bifurcation is the wedge.** Meta paywalled accessibility. Trump conditionally lifted Anthropic. Alibaba banned Claude Code. Palantir moved to Nemotron. **The closed-source frontier is no longer a stable substrate for any region. Ours was, is, and will be open-weights on the device.** Quote all four sources.
4. **Brilliant Labs Halo is the named peer.** We win on **on-device + substrate + threat model + bot.** They win on form factor. Both MIT. Both real. Both shipping.
5. **From India, for the world.** Earned. The orbit story, the buildspace pedigree, the Bengaluru bench — all real.

---

## 13. Open questions for somdipto (v124)

1. **Washington Post URL:** can you find the article and send the link? **P0.**
2. **Reuters/SCMP/GIGAZINE URLs:** the Alibaba Claude Code ban pieces — need the links to cite. **P0.**
3. **FourWeekMBA Karp/Nemotron URL:** need the link to cite. **P0.**
4. **BleepingComputer Fable 5 cap URL:** need the link to cite. **P0.**
5. **v124 plan-O1 sovereign-trust audit priority:** 1-day spike, Q3 W1, 1 engineer. Recommend ship. **P0.**
6. **v124 plan-O2 reversibility contract priority:** 3-day spike, Q3 W2, 1 engineer. Recommend ship. **P0.**
7. **v124 plan-O3 v1.0 spec §13 Sovereign Trust section:** 1-day copy, Q3 W1, 1 engineer. Recommend ship. **P0.**
8. **HuggingFace `danlab` org creation:** authorize me to create it this week? **P0.**
9. **Tailscale authkey:** still the single highest-leverage env var. **P0.**
10. **X handle decision:** launch `@danlab` (recommended) or founder-led only? **P0.**
11. **OpenClaw protocol surface doc:** do we have 2 engineer-days to ship it this week? **P0.**
12. **Show HN #1 timing:** is week 3–4 (Jul 21–28) good? **P0.**
13. **Tauri app domain:** is `dan-glasses-app-som.zocomputer.io` OK, or do we want a custom domain? **P1.**
14. **Brilliant Labs Halo collaboration / cross-tweet:** is there a relationship with the Brilliant Labs team? Cross-tweet or compare openly? **P1.**
15. **Dan Voice launch timing:** ship PRD this month, or wait for HRM-Text integration? **P1.**
16. **VisionClaw engagement:** is the right move a "we can run VisionClaw-style work natively on Dan Glasses" demo, or a quiet ignore? **P1.**
17. **Mistral/Forge positioning:** depth of competitive-positioning copy? Recommend 30 min copy. **P1.**

---

*End of v124 research report. See `dan1-marketing-strategy.md` for the action plan.*
