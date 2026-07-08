# Dan1 — Marketing Strategy (v121)

**Run:** 2026-07-04 11:35 IST
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Companion to:** `dan1-marketing-research.v121.md`
**Lead:** *The protocol is the bet. The data path is yours. The threat model is public. The wearable ships it.*

---

## 1. The strategy in one paragraph

We are an open, on-device, agent-native AI lab in Bengaluru, shipping Dan Glasses — a proactive AI companion that runs on the user's device, on the OpenClaw substrate, with a public threat model. We do not compete on capture-and-share (Ray-Ban Meta owns that). We compete on **Day 5 utility** — what your glasses do for you on the 5th day of wearing them, when the novelty has worn off and the memory kicks in. The marketing wedge is the **substrate**: Vinton Cerf said agents need TCP/IP, Anthropic shipped it, OpenClaw shipped it first, and Dan Glasses ships it on a wearable. Honesty is the moat — when Mashable flagged a flaw, we audited it, not denied it. **The next 100% of value is shipping, not framing.**

---

## 2. The 4 pillars of every post (use in this order)

1. **Protocol** — Cerf + Anthropic Apps Gateway + OpenClaw MCP bridge. The substrate is the bet.
2. **Observability** — PagerDuty + $725B AI infra spend + audiod's `segment_timing` histogram. The harness is the workbench, the model is the commodity.
3. **On-device** — LFM2.5-VL-450M, Gemma 3 in orbit, no cloud calls, MIT weights.
4. **Small-beats-large** — HRM-Text-1B at $1,500 training. Kokoro-82M beats ElevenLabs.

Any post, any thread, any demo should ladder up to one of these four. **No fifth pillar. Resist.**

---

## 3. Audience priority (top-down)

1. **Agent / protocol architects** — MCP community, dani-skills, OpenClaw contributors. *Highest leverage per impression.*
2. **Edge-AI developers / hackers** — GitHub, HN, X. *Highest install rate.*
3. **Accessibility-first users** — counter-Meta paywall narrative. *Highest moral weight.*
4. **AI researchers / academics** — arXiv, conference posters, citation flow. *Highest authority.*
5. **Small-model researchers** — HRM, Kokoro, SmolVLM crowd. *Highest affinity.*
6. **Security researchers** — Mashable readers. *Convert critics to allies.*
7. **Productivity-obsessed knowledge workers** — LinkedIn, Substack, X threads.
8. **Investors** — *only after* Show HN.

---

## 4. Channel strategy (ranked)

| Rank | Channel | Action this week | Metric |
|---|---|---|---|
| 1 | **OpenClaw protocol surface doc** (NEW) | Ship the protocol surface markdown + diagram. Block on threat model audit. | Doc live. Inbound fork count. |
| 2 | **OpenClaw threat model** (NEW) | 1-day audit spike. Public document. | Doc live. CVE-friendly. |
| 3 | **GitHub READMEs** | Rewrite dan-glasses, dani, danlab-multimodal, paperclip, blurr READMEs. | Star delta over 30 days. |
| 4 | **X / Twitter** | 3–5 posts/wk. Lead with protocol posts. | Follower delta, RT rate. |
| 5 | **Telegram @danlab_bot** | Wire into every post. Screenshot the daemon map. | Active users / wk. |
| 6 | **Hacker News** | Show HN #1 = "9 daemons live" (week 3–4, Jul 21–28). | Show HN position, comments. |
| 7 | **HuggingFace `danlab` org** | Create this week. Upload LFM2.5-VL-450M model card. | Model download count. |
| 8 | **LinkedIn** | Profile rewrite. 1 post/wk. | Profile views, connection rate. |
| 9 | **Substack / blog** | "From heuristic to SIA" series, 1 post/wk. | Subscriber delta. |
| 10 | **YouTube / Loom** | Demo videos. Asciinema cast of danlab-multimodal. | View count. |
| 11 | **Discord** | Q4 2026. Not now. | — |
| 12 | **Reddit** | Comment authentically. No marketing posts. | — |

---

## 5. The v121 deliverables punchlist (this week)

### P0 (block all marketing on these)
- [ ] **OpenClaw threat model doc** — 1 engineer-day. Public. Cite Mashable. Show the fix.
- [ ] **OpenClaw protocol surface doc** — 2 engineer-days. Public. Cite Cerf, Anthropic, Newsweek.
- [ ] **Newsweek URL** — get from somdipto. Quote in v1.0 marketing.
- [ ] **HuggingFace `danlab` org** — create this week. LFM2.5-VL-450M model card.
- [ ] **X handle decision** — `@danlab` or founder-led only.
- [ ] **Tailscale authkey** — single highest-leverage env var. Wire it up.
- [ ] **Show HN #1 draft** — "9 daemons live, .deb installs, on-device AI."

### P1 (parallel track)
- [ ] danlab.dev rewrite (Dan Glasses as flagship).
- [ ] LinkedIn profile rewrite.
- [ ] All GitHub README rewrites (see `dan1-github-readme-suggestions.v121.md`).
- [ ] LFM2.5-VL-450M model card on HF.
- [ ] 10 X posts drafted (see `dan1-twitter-content.v121.md`).

### P2 (Q3 2026)
- [ ] arXiv paper #1: SIA-W+H port report.
- [ ] Show HN #2: SIA-W+H port announcement.
- [ ] danlab.dev → custom domain.
- [ ] YouTube demo video.
- [ ] Discord server.

---

## 6. The 3 biggest events of 2026

1. **SIA-W+H port announcement + Show HN #2** (Q3)
   - Goes from "interesting wearable" → "lab that actually shipped open recursive self-improvement on a wearable."

2. **OpenClaw protocol surface + threat model marketing** (this month)
   - Goes from "interesting wearable" → "lab that shipped the agent substrate audibly before Anthropic, and told you about the flaw before it shipped."

3. **Show HN #1: "9 daemons live, .deb installs, on-device AI"** (week 3–4, Jul 21–28)
   - Goes from "interesting wearable" → "wearable you can install and DM today."

---

## 7. The anti-strategy (what we will not do)

- ❌ **No paid ads.** Substrate is open, not paid.
- ❌ **No influencer outreach.** Sells the wrong story.
- ❌ **No "we compete with Meta" copy.** We don't. They own lane (a). We own lane (d).
- ❌ **No feature-list marketing.** Speak in user stories, not bullet points.
- ❌ **No closed beta gate.** The .deb is up. DM the bot. That's the funnel.
- ❌ **No "AI will change everything" hype.** Substrate > slogan.
- ❌ **No press releases for the sake of press releases.** Newsweek came to us because we shipped, not because we pitched.

---

## 8. The competitive playbook (v121)

| Competitor move | Our response |
|---|---|
| Meta paywalls accessibility features | Quote the paywall, link to the .deb. *"Yours, not theirs."* |
| Anthropic ships closed-source Sonnet 5 | We ship open weights on the device. The protocol is published; the model is yours. |
| Zuckerberg admits Meta is behind | "We are not waiting." Lead with the 9 live daemons. |
| Mashable flags an OpenClaw flaw | Publish the threat model. Credit the journalist. Fix it publicly. |
| Microsoft Scout ships on OpenClaw | "Fork or follow at end of Q3." Cite Scout as substrate validation. |
| Brilliant Labs ships another SDK release | We win on **on-device + substrate + threat model.** Halo wins on open SDK. Both open. |
| Google + Samsung ship Android XR | We win on **no Google account, no cloud lock-in.** Cite it. |
| Apple smart glasses leak | Cite Kuo. 16-month window. Move fast. |

---

## 9. The voice (v121)

- **Direct. Opinionated. No fluff.**
- Bullet points, short sentences. One idea per message.
- Show code, files, screenshots. Not adjectives.
- "We shipped X" not "We are excited to announce Y."
- "The substrate is auditable, not perfect." Honesty over polish.
- "From India to the world" — earned, not asserted. The orbit story does the work.
- Brutal honesty > politeness. The lab that admits a flaw is the lab you trust.

---

## 10. Success metrics (v121 → v130)

| Metric | v121 baseline | v130 target |
|---|---|---|
| GitHub stars across danlab org | ~? | 3x |
| danlab.dev unique visitors / mo | ~? | 10x |
| X followers (founder + lab) | ~? | 5x |
| HuggingFace model downloads | 0 | 1,000+ |
| Show HN #1 position | — | Top 10 |
| Inbound agent / protocol fork count | 0 | 5+ |
| `@danlab_bot` DM count / wk | 0 | 50+ |
| Threat model doc inbound security issues filed | 0 | 3+ (signal of trust) |

---

## 11. The one-line strategy

**Ship the substrate. Audit the threat model. Quote Cerf. Quote Newsweek. Quote Mashable. Show the .deb. Show the daemon map. Show the bot. The next 100% of value is shipping.**

---

*See `dan1-content-calendar.v121.md` for the week-by-week cadence.*
