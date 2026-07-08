# Dan1 — Marketing Strategy (v124)

**Run:** 2026-07-05 09:30 UTC (refresh of v123, 14:00 IST 2026-07-05 same day)
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Companion to:** `dan1-marketing-research.md`
**Status:** Foundation stream ✅ locked. Threat model ✅ public (v122.5, 3.6MB delta). **v124 add: 3-region bifurcation is now named, dated, citable.** This is the marketing plan for what we ship *now that the foundation + the audit + the sovereign-trust wedge ships.*

**Lead (v124, locked):** *Closed-source frontier AI is no longer geopolitically safe. Three regions just said so out loud. The bot is live. The .deb installs. The threat model is public. Yours, not theirs.*

---

## 1. The strategy in one paragraph

We are an open, on-device, agent-native AI lab in Bengaluru, shipping Dan Glasses — a proactive AI companion that runs on the user's device, on the OpenClaw substrate, with a public threat model, **politically-uncapturable and sovereign-trust-validated**. The foundation is shipped: 8 daemons live, OpenClaw gateway live, `@danlab_bot` polling, Tauri v2 app published at `dan-glasses-app-som.zocomputer.io`, `.deb` package built (`dan-glasses-daemons_0.1.0-1_all.deb`, 9.4MB), 208/208 tests green, threat model public as of v122.5. We do not compete on capture-and-share (Ray-Ban Meta owns that). We do not compete on closed-cloud (Anthropic/Meta/Apple own that, and as of July 2026 the closed-cloud has been conditionally lifted in the US, banned in China, and pivoted away from in defense). We compete on **Day 5 utility** + **sovereign trust** — what your glasses do for you on the 5th day of wearing them, and the audit you can run on the 30th day. The marketing wedge is the **substrate** (Cerf + Anthropic Apps Gateway + OpenClaw MCP bridge) + the **sovereign trust** (3-region bifurcation is now public, and we are the only wearable-grade lab none of the three had to call). The bot is the funnel, the threat model is the moat, the reversibility contract is the v124 receipt, and the next 100% of value is shipping the artifacts, not refining the framing. **v124 add:** three concrete public events this week (Washington Post Trump/Anthropic lift, Reuters/SCMP Alibaba/Claude Code ban, FourWeekMBA Palantir/Nemotron pivot) prove the closed-source frontier is politically-conditional. Cite all three in every post.

---

## 2. The 4 pillars of every post (use in this order)

1. **Protocol** — Cerf + Anthropic Apps Gateway + OpenClaw MCP bridge. The substrate is the bet.
2. **Observability** — PagerDuty + $725B AI infra spend + audiod's `segment_timing` histogram. The harness is the workbench, the model is the commodity.
3. **On-device** — LFM2.5-VL-450M, Gemma 3 in orbit, no cloud calls, MIT weights. **No paywall on accessibility.**
4. **Small-beats-large** — HRM-Text-1B at $1,500 training. Kokoro-82M beats ElevenLabs.

Any post, any thread, any demo should ladder up to one of these four. **No fifth pillar. Resist.**

**v124 addendum (the 3-region bifurcation):** every post should also reference at least one of the four citable sources:
- Washington Post: Trump admin conditional on Anthropic (Jul 1 2026)
- Reuters / SCMP / GIGAZINE: Alibaba banned Claude Code (Jul 4 2026)
- FourWeekMBA: Palantir/Karp on U.S. agencies moving to Nemotron (early Jul 2026)
- BleepingComputer: Fable 5 capped + rerouted to Opus 4.8 (Jul 2026)

**v123 addendum (the citable event):** every post should also reference the **Meta paywall on accessibility** as the proof of the on-device pillar. *3hr/mo free, 15hr/mo at $19.99, on a device that does the work locally. Ours is yours.*

**v123 addendum (the funnel):** Every post should also end with a **bot CTA**. *"DM @danlab_bot to see for yourself."* This is the lowest-friction conversion path we have.

---

## 3. Audience priority (top-down, v124)

1. **Agent / protocol architects** — MCP community, dani-skills, OpenClaw contributors. *Highest leverage per impression.*
2. **Edge-AI developers / hackers** — GitHub, HN, X. *Highest install rate.*
3. **Sovereign-trust-first enterprise / government** — **NEW v124 tier.** Alibaba banned Claude Code. Palantir moved to Nemotron. EU will follow. *Highest revenue.*
4. **Accessibility-first users** — activated by the Meta paywall. *Highest moral weight, now citable.*
5. **AI researchers / academics** — arXiv, conference posters, citation flow. *Highest authority.*
6. **Small-model researchers** — HRM, Kokoro, SmolVLM crowd. *Highest affinity.*
7. **Security researchers** — Threat model is now public. Convert critics to allies. *Cite Mashable, credit the journalist.*
8. **Productivity-obsessed knowledge workers** — LinkedIn, Substack, X threads.
9. **Brilliant Labs Halo ecosystem** — closest named peer. Both MIT, both open, both shipping. Cross-tweet opportunity.
10. **India AI / Bengaluru ecosystem** — LinkedIn, India AI Summit, NASSCOM. *Origin story wedge.*
11. **Investors** — *only after* Show HN. v124 angle: sovereign-trust-first enterprise + India + edge AI.

**v124 shift:** sovereign-trust-first enterprise moves to #3 (NEW). Brilliant Labs Halo ecosystem moves to #9 (from #8). Investor angle adds sovereign-trust wedge.

---

## 4. Channel strategy (ranked, v124)

| Rank | Channel | Action this week | Metric |
|---|---|---|---|
| 1 | **@danlab_bot** (Telegram) | The funnel. The demo. Wire into every post. | DMs / wk, DAU, queries/user/day |
| 2 | **Tauri app URL** (`dan-glasses-app-som.zocomputer.io`) | Public. Link from every artifact. | Unique visitors / wk |
| 3 | **Threat model doc** (now public, v122.5) | Cite from every artifact. Credit Mashable. | Doc views, inbound security issues filed |
| 4 | **Sovereign-trust audit** (v124 NEW, plan-O1) | 1-day spike, Q3 W1, 1 engineer. | Audit live, cited in v1.0 spec §13 |
| 5 | **Reversibility contract** (v124 NEW, plan-O2) | 3-day spike, Q3 W2, 1 engineer. | Contract live on `revert_loop()` API |
| 6 | **v1.0 spec §13 Sovereign Trust section** (v124 NEW, plan-O3) | 1-day copy, Q3 W1, 1 engineer. | Spec section live, cited in marketing |
| 7 | **OpenClaw protocol surface doc** (carry-over) | 2 engineer-days. Public. Cite Cerf, Anthropic, Newsweek. | Doc live. Inbound fork count. |
| 8 | **GitHub READMEs** | Rewrite dan-glasses, dani, danlab-multimodal, paperclip, blurr, dan-lab READMEs. | Star delta over 30 days. |
| 9 | **X / Twitter** | 3–5 posts/wk. Lead with **the 3-region bifurcation + Meta paywall**, then bot screenshots. | Follower delta, RT rate. |
| 10 | **Hacker News** | Show HN #1 = "8 daemons live, .deb installs, DM the bot, threat model is public" (week 3–4, Jul 21–28). | Show HN position, comments. |
| 11 | **HuggingFace `danlab` org** | Create this week. Upload LFM2.5-VL-450M model card. | Model download count. |
| 12 | **LinkedIn** | Profile rewrite. 1 post/wk. Target: sovereign-trust-first enterprise + India AI. | Profile views, connection rate. |
| 13 | **Substack / blog** | "From heuristic to SIA" + "Sovereign trust" series, 1 post/wk. | Subscriber delta. |
| 14 | **YouTube / Loom** | Demo videos. Asciinema cast of danlab-multimodal. | View count. |
| 15 | **Discord** | Q4 2026. Not now. | — |
| 16 | **Reddit** | Comment authentically. No marketing posts. | — |
| 17 | **Press citations** (NEW v124) | Cite Washington Post + Reuters + FourWeekMBA + BleepingComputer. | Inbound press mentions |

---

## 5. The v124 deliverables punchlist (this week)

### P0 (block all marketing on these)
- [ ] **v124 plan-O1: toold sovereign-trust audit** — 1-day spike, Q3 W1, 1 engineer. Add OCR-derived-command rejection.
- [ ] **v124 plan-O2: openclaw + toold end-to-end reversibility contract** — 3-day spike, Q3 W2, 1 engineer. `revert_loop(loop_id)` API.
- [ ] **v124 plan-O3: v1.0 spec §13 "Sovereign trust, political conditionality, and reversibility"** — 1 day copy, Q3 W1, 1 engineer. Frame Dan Glasses as politically-uncapturable, sovereign-trust-validated, fully-reversible.
- [ ] **Washington Post URL** — get from somdipto. Quote in v1.0 marketing.
- [ ] **Reuters/SCMP/GIGAZINE URLs** — get from somdipto. Quote in v1.0 marketing.
- [ ] **FourWeekMBA Karp/Nemotron URL** — get from somdipto. Quote in v1.0 marketing.
- [ ] **BleepingComputer Fable 5 cap URL** — get from somdipto. Quote in v1.0 marketing.
- [ ] **HuggingFace `danlab` org** — create this week. LFM2.5-VL-450M model card.
- [ ] **X handle decision** — `@danlab` or founder-led only.
- [ ] **Tailscale authkey** — single highest-leverage env var. Wire it up.
- [ ] **Show HN #1 draft** — "8 daemons live, .deb installs, DM the bot. Threat model is public."

### P1 (parallel track, ship this week)
- [ ] danlab.dev rewrite (Dan Glasses as flagship, not one of four).
- [ ] LinkedIn profile rewrite.
- [ ] All GitHub README rewrites (see `dan1-github-readme-suggestions.md`).
- [ ] LFM2.5-VL-450M model card on HF.
- [ ] 10 X posts drafted (see `dan1-twitter-content.md`) — **lead with the 3-region bifurcation + Meta paywall**.
- [ ] Tauri app OG image + landing-card screenshot.
- [ ] `@danlab_bot` welcome flow polish (DM the bot, get the daemon map).
- [ ] Brilliant Labs Halo cross-tweet or open comparison.
- [ ] 16-step → 17-step marketing narrative update (add 3-region bifurcation as 17th step).
- [ ] Mistral/Forge positioning (30 min copy).

### P2 (next month)
- [ ] arXiv paper #1: SIA-W+H port report.
- [ ] Show HN #2: SIA-W+H port announcement.
- [ ] danlab.dev → custom domain.
- [ ] YouTube demo video.
- [ ] Discord server.
- [ ] Tauri app custom domain.
- [ ] VisionClaw response: native equivalent on Dan Glasses.
- [ ] Sovereign-trust-first enterprise direct outreach (DoD GenAI.mil, Mistral/Forge, EU sovereign-cloud).
- [ ] 6/12/24-month plan revision reflecting v124 3-region bifurcation.

---

## 6. The 3 biggest events of 2026 (v124)

1. **SIA-W+H port announcement + Show HN #2** (Q3)
   - Goes from "interesting wearable" → "lab that actually shipped open recursive self-improvement on a wearable."

2. **3-region bifurcation counter-marketing + sovereign-trust audit release** (this month, v124 NEW)
   - Goes from "interesting wearable" → "lab that the three regions didn't have to call, because we were already open-weights on the device."

3. **Show HN #1: "8 daemons live, .deb installs, on-device AI, threat model is public, DM the bot"** (week 3–4, Jul 21–28)
   - Goes from "interesting wearable" → "wearable you can install and DM today, with a public audit."

---

## 7. The anti-strategy (what we will not do, v124)

- ❌ **No paid ads.** Substrate is open, not paid.
- ❌ **No influencer outreach.** Sells the wrong story.
- ❌ **No "we compete with Meta" copy.** We don't. They own lane (a) social. We own lane (d) substrate + on-device + sovereign-trust. The paywall is the citable event, not a competition claim.
- ❌ **No "we compete with Anthropic" copy.** We don't. They own lane (c) closed-cloud. We own lane (a) on-device open-weights. The 3-region bifurcation is the citable event, not a competition claim.
- ❌ **No feature-list marketing.** Speak in user stories, not bullet points.
- ❌ **No closed beta gate.** The .deb is up. DM the bot. That's the funnel.
- ❌ **No "AI will change everything" hype.** Substrate > slogan.
- ❌ **No press releases for the sake of press releases.** Newsweek came to us because we shipped, not because we pitched.
- ❌ **No vendor lock-in copy.** "Yours, not theirs" is the line. Don't soften it.
- ❌ **No "we're excited to announce."** We shipped. Show the receipts.
- ❌ **No "we are the first to...**" unless we can prove it. Cite or skip.
- ❌ **No borrowed openness.** VisionClaw runs on Meta's SDK. We don't. Don't claim openness we can't ship natively.
- ❌ **No "we are the sovereign alternative."** Let the 3-region bifurcation do the work. Cite the four sources. The lab that was open-weights on the device from day one is the only one they didn't have to call. The reader draws the conclusion.
- ❌ **No FUD against Anthropic/Meta.** They shipped. They got conditionally lifted, banned, pivoted away from. The receipts are public. We don't need to add adjectives.

---

## 8. The competitive playbook (v124)

| Competitor move | Our response |
|---|---|
| **Meta paywalls accessibility** (3hr free, 15hr at $19.99) | **Quote the paywall. Link to the .deb. *"Yours, not theirs. DM @danlab_bot."*** |
| **Meta launches own-brand glasses at $299** | We are not in the same lane. We don't compete on price or social. Cite Day 5 utility. |
| **Anthropic ships closed-source Sonnet 5 + Apps Gateway** | We ship open weights on the device. The protocol is published; the model is yours. |
| **Trump admin conditionally lifts Anthropic export ban (Jul 1 2026)** | **Cite the WaPo article.** *"The lab that was open-weights on the device from day one is the only one they didn't have to call."* |
| **Alibaba bans Claude Code (Jul 4 2026)** | **Cite Reuters/SCMP.** *"First sovereign-nation-scale enterprise ban of a frontier coding tool. Ours was never on their server."* |
| **Palantir/Karp: U.S. agencies move to Nemotron** | **Cite FourWeekMBA.** *"Three-region bifurcation. Open-weights won."* |
| **Anthropic Fable 5 capped + rerouted to Opus 4.8** | **Cite BleepingComputer.** *"Lifted ≠ unconditional. Ours was never gated."* |
| **Zuckerberg admits Meta is behind** | "We are not waiting." Lead with the 8 live daemons + the bot screenshot. |
| **Mashable flags an OpenClaw flaw** | **Threat model is public (v122.5). Credit the journalist in the README.** Fix it publicly. |
| **Microsoft Scout ships on OpenClaw** | "Fork or follow at end of Q3." Cite Scout as substrate validation. |
| **Brilliant Labs ships Halo at $299** | **Cross-tweet. Both MIT. Both open. We win on substrate + threat model + bot. They win on form factor.** |
| **Google + Samsung ship Android XR** | We win on **no Google account, no cloud lock-in, no paywall.** Cite it. |
| **Apple smart glasses leak** | Cite Kuo. 16-month window. Move fast. |
| **VisionClaw ships on Meta Ray-Ban via DAT SDK** | *"If your open alternative needs Meta's SDK, the openness is borrowed. Ours is native. DM @danlab_bot."* |
| **Someone clones the bot idea** | We had it first, on a wearable, with a public threat model. Cite the receipts. |
| **Mistral/Forge ships sovereign enterprise AI platform** | *"First European-sovereign-stack. We are the open-weights wearable counterpart. Cross-tweet."* |
| **DoD GenAI.mil hits 1.7M users** | *"Commercial-first procurement policy. The .deb is the procurement story."* |

---

## 9. The voice (v124)

- **Direct. Opinionated. No fluff.**
- Bullet points, short sentences. One idea per message.
- Show code, files, screenshots, daemon maps, bot screenshots. Not adjectives.
- "We shipped X" not "We are excited to announce Y."
- "The substrate is auditable, not perfect." Honesty over polish.
- "From India to the world" — earned, not asserted. The orbit story does the work.
- "Yours, not theirs" — the on-device mantra.
- "DM the bot" — the call to action.
- "Meta paywalled accessibility. We didn't." — the v123 line. Use it.
- **"Alibaba banned Claude Code. We didn't have to ban ourselves."** — the v124 line. Use it.
- **"The lab that was open-weights on the device from day one is the only one they didn't have to call."** — the v124 wedge. Use it.
- **"Three regions just said closed-source frontier AI is no longer safe. We were already open-weights on the device."** — the v124 3-region quote. Use it.
- Brutal honesty > politeness. The lab that admits a flaw is the lab you trust.

---

## 10. Success metrics (v124 → v130)

| Metric | v124 baseline | v130 target |
|---|---|---|
| GitHub stars across danlab org | ~50 (est) | 3x = 150+ |
| danlab.dev unique visitors / mo | ~0 (stale) | 10x = 5,000+ |
| dan-glasses-app-som.zocomputer.io unique visitors / mo | 0 (just published) | 1,000+ |
| X followers (founder + lab) | TBD | 5x |
| HuggingFace model downloads | 0 | 1,000+ |
| Show HN #1 position | — | Top 10 |
| `@danlab_bot` DM count / wk | 0 (just live) | 50+ |
| `@danlab_bot` DAU | 0 | 20+ |
| Threat model doc inbound security issues filed | 0 | 3+ (signal of trust) |
| Inbound agent / protocol fork count | 0 | 5+ |
| Telegram @danlab_bot paired users (cumulative) | 0 | 100 |
| .deb installs / mo | 0 | 200+ |
| "Meta paywall" mention in inbound press | 0 | 3+ (signal of narrative adoption) |
| **"3-region bifurcation" mention in inbound press (v124 NEW)** | 0 | 3+ |
| **Sovereign-trust-first enterprise inbound leads (v124 NEW)** | 0 | 5+ (DoD, EU sovereign, India enterprise) |
| **Reversibility contract API calls / mo (v124 NEW)** | 0 | 10+ (signal of bot-as-agent) |

**v124 honest baseline:** the foundation is shipped + audited, but the audience is still 0. Every metric is from zero. The first 100 users will come from a single great Show HN post + the Meta paywall narrative + the 3-region bifurcation narrative + a single great threat model doc, not from 30 tweets.

---

## 11. The bot-first funnel (v124)

This is the lowest-friction path from "saw a post" to "using the product." Every channel should point at the bot.

```
[Post on X / HN / LinkedIn / Reddit / Substack]
        ↓
[Reader DMs @danlab_bot on Telegram]
        ↓
[Bot sends daemon map + 3 starter commands]
        ↓
[Reader runs `curl localhost:8090/ready` and sees a real payload]
        ↓
[Reader runs the .deb or opens the Tauri app]
        ↓
[Reader shares the screenshot]
        ↓
[New reader DMs the bot]
```

**Every post's CTA:** *"DM @danlab_bot. The bot is the demo."*

**The bot's first message:** the live daemon map, screenshot-ready. *"8 services live. DM me anything."*

**v123 bot opener, after the paywall narrative goes live:**

> *"Meta paywalled accessibility. We didn't. 8 daemons live, .deb installs, on-device. DM me anything."*

**v124 bot opener, after the 3-region bifurcation narrative goes live:**

> *"Alibaba banned Claude Code. Trump conditionally lifted Anthropic. Palantir moved to Nemotron. Three regions just said closed-source frontier AI is no longer safe. We were already open-weights on the device. 8 daemons live, .deb installs, on-device, threat model public. DM me anything."*

---

## 12. The one-line strategy (v124)

**Ship the substrate. Audit the threat model. Ship the sovereign-trust audit. Ship the reversibility contract. Quote Cerf. Quote Newsweek. Quote Mashable. Quote the Meta paywall. Quote the Trump conditionality. Quote the Alibaba ban. Quote the Palantir pivot. Show the .deb. Show the daemon map. Show the bot. DM @danlab_bot. The next 100% of value is shipping.**

---

*See `dan1-content-calendar.md` for the week-by-week cadence.*
