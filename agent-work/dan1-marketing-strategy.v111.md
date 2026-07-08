# DanLab Marketing Strategy — Run v111
**Date:** 2026-07-01
**Owner:** DAN-1
**Inputs:** [dan1-marketing-research.md](./dan1-marketing-research.md)
**Status:** v111 refresh. v110 strategy is the spine. This run is the delta.

---

## 0. North Star (unchanged from v110)

> **Make "Dani" the most-trusted open personal-AI platform in the world — measured by monthly active developers, monthly active users of the Dan Voice app, and monthly GitHub stars across the org.**

Three numbers we will repeat every Monday:
- **MAD** — Monthly Active Developers (target: 1k by end of Q3, 10k by end of Q4)
- **MAU** — Monthly Active Users across Dan Voice / Dan Glasses / Telegram (target: 10k end of Q3, 100k end of Q4)
- **GH-stars** — sum across [dan-consciousness](https://github.com/somdipto/dan-consciousness), [dani](https://github.com/somdipto/dani), [paperclip](https://github.com/somdipto/paperclip), [danlab-multimodal](https://github.com/somdipto/danlab-multimodal), [dan-glasses](https://github.com/somdipto/dan-glasses) (target: 5k end of Q3, 25k end of Q4)

**v111 addition:** Add **TG-DAU** — Daily Active Users of `@danlab_bot`. Target: 50 by end of Q3, 500 by end of Q4. The Telegram surface is a free distribution channel; treat it as a first-class metric.

---

## 1. Positioning (v111, sharpened)

### One-line positioning
> **DanLab builds proactive, private AI wearables and personal agents — your data, your cloud, your face. Built from India, for the world.**

### Three-line positioning (v111, refined)
> Most AI assistants wait for you to ask a question and then phone home with your data. Dan agents watch, remember, and act — inside your own verifiable cloud container. 9 daemons live today. Open source SDK. Sub-250MB on-device VLMs. LFM2.5-VL-450M in production. From Bangalore to the world.

### Five anti-positions (v111, refined)
1. **NOT reactive chat.** We are *proactive*. The agent watches the room and only speaks when worth speaking.
2. **NOT cloud-only.** Every Dan runs a 9-daemon local fleet (audiod, audiod-ws, perceptiond, memoryd, toold, ttsd, os-toold, openclaw-web, dan-glasses-app) that does not require a server.
3. **NOT data-harvesting.** No per-user data ever leaves the user's EigenCloud TEE container. **We cannot read it. Not "we promise" — architecturally cannot.**
4. **NOT walled garden.** Dan Agent SDK is MIT. Any developer can register a tool that runs in any user's container.
5. **NOT colonial AI.** We are not "Silicon Valley with a Bangalore office." The brain is built here, the hardware is sourced here, the engineering culture is ours.

### v111 positioning delta vs v110
- **Added:** "9 daemons live today" — a verifiable claim, not an aspiration.
- **Added:** "LFM2.5-VL-450M in production" — a named model, a real Liquid AI partnership signal.
- **Hardened:** "architecturally cannot" replaces "we promise" everywhere.
- **Added:** Telegram surface explicitly.

---

## 2. Audience Pyramid (v111, refined)

We sell to five audiences in strict priority order. **Do not try to talk to all five at once.**

### Layer 1 — Builders & Operators (10k target by Q3)
- **Who:** AI engineers, agent-platform CTOs, indie hackers writing workflow tools.
- **Where they live:** GitHub Trending, Hacker News, /r/LocalLLaMA, r/MachineLearning, HuggingFace Discord, Paperclip repo watchers.
- **What they care about:** Can I run this on my laptop tonight? Does the SDK let me ship a tool? Is the architecture honest?
- **Channel:** README + demo video + Show HN. Engineering blogs. Whitepapers.
- **KPI:** GitHub stars across org, new contributors per month, MCP tool integrations shipped.

### Layer 2 — Knowledge Workers (100k target by Q4)
- **Who:** Daily Gmail + Notion + Slack + Calendar users; "I would pay $20/mo for a real Jarvis" demographic. Age 28–45, English-fluent, white-collar, chronically online.
- **Where they live:** Product Hunt, LinkedIn, Twitter, Product-Led Alliance, Lenny's Newsletter.
- **What they care about:** Does it actually do expense reports end-to-end? Does it work with my earbuds? Can I trust it with my inbox?
- **Channel:** Dan Voice app landing page, Product Hunt launch, paid ads retargeting from LinkedIn/Twitter.
- **KPI:** App installs, free→paid conversion, week-4 retention.

### Layer 3 — Wearable Early-Adopters (10k target by Q4)
- **Who:** Builders who already flashed a Pinephone, owners of a Steam Deck, attendees of FOSDEM/CCC/DEF CON hardware villages. Comfortable installing .deb packages.
- **Where they live:** Hacker News "Show HN", /r/smartglasses, the Even Realities Discord, the Brilliant Labs Discord, CES hardware forums.
- **What they care about:** Real BOM cost. Battery. Repairability. Open SDK. Does it survive a coffee spill?
- **Channel:** Track A landing page, GitHub README for dan-glasses, conference talks.
- **KPI:** Demos at conferences, .deb installs reported, GitHub stars on dan-glasses repo.

### Layer 4 — Telegram Early Adopters (v111 new, 500 DAU by Q4)
- **Who:** Anyone with Telegram. Zero install, zero hardware. Power users who already have 5+ bots.
- **Where they live:** Telegram channels, bot directories, AI bot lists.
- **What they care about:** Does the bot actually do something useful? Is it private? Can I pair in 30 seconds?
- **Channel:** `@danlab_bot` as the product surface. Share via Twitter, LinkedIn, danlab.dev footer.
- **KPI:** Pairing completions, daily active users, queries per user per day, retention D1/D7/D30.

### Layer 5 — Enterprise Pilot Buyers (10 named accounts by Q4)
- **Who:** Operations VPs at mid-size BPOs (India), travel agencies (SEA), journalism teams (US/EU), executive-assistant firms.
- **Where they live:** Sequoia Surge cohort, YC W26 partner intros, Bangalore startup Grind events.
- **What they care about:** SOC2-style attestation, EigenCloud TEE audit trail, agent audit log, custom workflow build-out timeline.
- **Channel:** Direct outreach from somdipto, Opentensor-style pilots, EigenCloud partner program.
- **KPI:** Pilots signed, MRR, agent executions per pilot account.

---

## 3. Channels (v111, three owned + one new)

### Channel A — GitHub + Show HN (engineering credibility)
- Three repos to rise first: **dan-consciousness** (our brain), **dani** (agent platform), **paperclip** (orchestration).
- P0: refresh all 6 hero repo READMEs (see [README suggestions](./dan1-github-readme-suggestions.md)).
- Add a HACKATHON.md to danlab-multimodal pointing to the asciinema demo.
- Post one Show HN when ready (anchor: the 9/9-daemon foundation stream milestone + a 90-second demo video).
- Publish a one-page architecture PDF on each repo's Releases. Linked from the README.

### Channel B — Twitter / X (single-voice thought leadership)
- One handle only — **@danaboratory** (or whatever somdipto confirms is available).
- Beat: 1 technical thread / week, 1 build-in-public post / week, 1 hot-take / fortnight, 1 daemon-of-the-week micro-post.
- NO generic AI hype tweets. Every tweet must reference code, a real metric, or a shipped artifact.
- Profile pinned tweet: the 9/9 daemons live screenshot (real `/status` payloads, not a mockup).

### Channel C — danlab.dev (the funnel — v111 NEW, P0)
- The site is the URL that gets shared. It must communicate the v111 strategy.
- **Refresh homepage** to match: proactive AI, architecturally private, 9 daemons live, open source, from India.
- Add the Telegram surface (`@danlab_bot`) prominently in the footer.
- Add `danlab.ai/dan-voice` (Track B) and `danlab.ai/glasses` (Track A) as sub-pages when ready.
- Performance budget: <1MB, FCP <1.5s on 4G India (Jio / Airtel).
- No third-party trackers for the first 30 days. Plausible self-hosted after.

### Channel D — Telegram (`@danlab_bot`, v111 NEW, in-channel)
- The product *is* the channel. The bot answers, the user evaluates.
- Wire into all posts: "Try it: @danlab_bot" / "DM us: @danlab_bot" / "Live now: t.me/danlab_bot".
- Pairing flow is the gate. Manual approve via `openclaw devices approve <id>`.
- DM-only for now. Group allowlist when we have 100+ paired users.

### What we **do NOT** spend time on:
- Instagram / TikTok (wrong audience, no time)
- Medium (ghost-town for AI readers)
- Newsletters we cannot commit to weekly
- Paid ads until we have a self-serve funnel that converts >2%

---

## 4. Narrative Arcs (v111, sharpened)

We have **four** narratives, in priority order. (v110 had three; v111 adds one.)

### Arc 1 — "From India to AGI"
The canonical origin story. somdipto in Bangalore, building the brain alone, then with Dani as a co-founder. The technical mark is the dan-consciousness repo — public, MIT, auditable. Every blog post, every conference talk, every press piece should reference this repo.
- **Sample tweet:** "We are building AGI from India. Our brain lives at github.com/somdipto/dan-consciousness. MIT licensed. Read the source."

### Arc 2 — "Architecturally private"
v110 said "privacy by architecture." v111 sharpens to "**architecturally** private" — the EigenCloud TEE attestation is a cryptographic guarantee, not a promise. This is the deepest technical differentiator, and the one most likely to matter to the press.
- **Sample tweet:** "Quark: data in Alibaba cloud. Meta: data in Meta cloud. Dan: data in *your* TEE-attested container. We cannot read your emails even if we wanted to. Not 'we promise.' Architecturally cannot."

### Arc 3 — "Proactive, not reactive"
The product thesis. Watchful mode at the daemon level. The salience gate in perceptiond. The proactive trigger engine in Dan Voice. This is what will make Google Glass "hindsight goggles" look like 2014.
- **Sample tweet:** "Most smart glasses wait for you to ask. Ours watches for context shifts and asks first. perceptiond uses LFM2.5-VL-450M to gate every frame by salience — 5fps watchful, 10fps active. Try the daemon: github.com/somdipto/dan-glasses"

### Arc 4 — "9 daemons, no cloud" (v111 NEW)
The build-in-public narrative. The number goes up over time. The audience watches it grow. Each daemon gets its own micro-post with a real `/status` payload.
- **Sample tweet:** "9/9 daemons live on my Linux laptop today. audiod 8090, audiod-ws 8091, perceptiond 8741, memoryd 8092, toold 8742, ttsd 8743, os-toold 8744, openclaw-web 18789, dan-glasses-app 3888. 150+ tests passing on audiod alone. Open source daemon-by-daemon. github.com/somdipto/dan-glasses"

---

## 5. 30-Day Tactical Plan (v111, updated)

### Week 1 (July 1 – 7) — Foundation refresh
**Theme:** "9/9 daemons live. Site says so. Telegram works."
- [ ] **P0:** Refresh danlab.dev homepage. Somdipto to confirm access + stack.
- [ ] **P0:** Update dan-glasses README with current port matrix + LFM2.5-VL-450M + 9/9 live claim.
- [ ] **P0:** Update danlab-multimodal README cross-links to dan-lab org.
- [ ] **P0:** Create dan-lab org profile/README.md.
- [ ] Confirm brand naming and Twitter handle (blocking).
- [ ] One tweet: "9/9 daemons live. Site updated. Telegram @danlab_bot wired. Open source. From India."
- [ ] Cross-post the danlab.dev refresh to LinkedIn (somdipto).

### Week 2 (July 8 – 14) — Architecture deep-dive
**Theme:** "How 9 services + an OpenClaw gateway become one proactive agent."
- [ ] Ship the architecture PDF for dan-glasses (one-pager per layer).
- [ ] Publish the "9 daemons live" demo video on YouTube Shorts + LinkedIn.
- [ ] Post technical thread: "How to build a proactive AI wearable on a $0 budget" — link the build plan.
- [ ] **Daemon-of-the-week #1: audiod.** Micro-post with the real `/ready` payload. Tease v1.1 liveness/readiness split.
- [ ] Submit Paperclip to https://news.ycombinator.com as "Show HN".

### Week 3 (July 15 – 21) — Track B (Dan Voice) drops
**Theme:** "Your earbuds are now a Jarvis. No hardware purchase."
- [ ] Publish the Dan Voice landing page (Track B) at danlab.ai/dan-voice.
- [ ] Set up Lead magnet: "The India AGI Builder's Manifest" — 5-page PDF in exchange for email.
- [ ] One cold outreach to 3 SE-Asia travel-agency ops VPs about a Dan Voice pilot.
- [ ] **Daemon-of-the-week #2: perceptiond.** Micro-post with the LFM2.5-VL-450M spec. Salience-gating explainer.
- [ ] One tweet: "Telegram @danlab_bot is live. DM to pair. No install. No hardware. Privacy by architecture."

### Week 4 (July 22 – 28) — Track A (Dan Glasses wearable) drops
**Theme:** "9/9 daemons running on a Linux laptop. Now let's put it on your face."
- [ ] Publish the Dan Glasses landing page (Track A) at danlab.ai/glasses.
- [ ] Pin the "watchful mode" demo video on the GitHub README of dan-glasses.
- [ ] **Daemon-of-the-week #3: memoryd.** Micro-post on SQLite + 384-dim vectors + episodic/semantic/procedural.
- [ ] Hot-take tweet: "Glasses at $99 make smart-glasses a daily-driver category. The math proves it."
- [ ] One Show HN draft: "Show HN: Dan Glasses — proactive AI wearable, 9 daemons, open source".
- [ ] Burn down the v110 punchlist — what is not done by July 28 is rolled into Q3 OKRs.

### End-of-month metrics dashboard
- danlab.dev unique visitors
- GH stars (sum of org) = ___
- New Twitter followers = ___
- @danlab_bot paired users (cumulative) = ___
- @danlab_bot DAU = ___
- Show HN rank peak = ___
- App installs (if Track B demo is live) = ___

---

## 6. Brand Voice Rules (v111, unchanged from v110)

- **Direct.** Short sentences. Active voice. Verbs before nouns.
- **Specific numbers over adjectives.** "9 of 9 daemons live" beats "highly reliable."
- **Substance over polish.** Better to ship an ugly README with real code than a slick README with no code.
- **No buzzword soup.** Banned words: "revolutionary," "game-changing," "next-gen," "AI-powered" (says who?).
- **Indian origin is the asset, not the asterisk.** "From India" is in our bio. Not "also from India."
- **Honest about limits.** "This is a heuristic, not RL. SIA fork coming." beats overclaiming.
- **v111 addition:** "Architecturally private" over "private." Always.
- **v111 addition:** Name the model. "LFM2.5-VL-450M" beats "VLM." "whisper.cpp base.en" beats "STT."
- **Pronouns and voice:** first-person plural ("we"). Never "the company."

---

## 7. Risks + Mitigations (v111, updated)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **danlab.dev stays stale** | **High** (no owner currently) | **High** (funnel is broken) | **P0 this run. Ask somdipto for access and stack this week.** |
| Quark or Meta ships parity feature | High | Medium | We win on privacy + open SDK. Lean into the architecture story. |
| Show HN is a flop | Medium | Medium | Pre-warm the post 48h earlier with the danlab-multimodal asciinema. Recruit 5 commenters. |
| somdipto becomes single-point-of-failure for shipping | High | High | Document the 9-daemon bootstrap one-liner. Recruit a part-time devops hire via the open roles channel. |
| EigenCloud pricing shock for paid tier | Medium | High | Anchor pricing to Indian mobile-phone data plans (₹399/month entry tier). |
| Open-source competitor forks Paperclip and out-executes us | Medium | Medium | Maintain a 6-month technical lead via dan-consciousness and proprietary prompts. |
| **Telegram abuse / spam** (v111 new) | Medium | Medium | Keep `pairing` DM policy. Manual approve. Group allowlist is empty by default. |
| **HRM-Text-1B ship slips** (v111 new) | Medium | Low | Do not market HRM-Text until audiod v1.3 lands. Tease in one tweet only. |
| **Tailscale blocker scares the team** (v111 new) | Low | Low | It is a sandbox constraint, not a product gap. Telegram does not need Tailscale. Document the path forward in a blog post if it becomes a narrative issue. |

---

## 8. What we will not do this quarter (v111, unchanged)

- Hire a marketing agency.
- Spend on paid ads.
- Launch a Discord before we have 1k MAU.
- Publish thought-leadership content in the abstract ("the future of AI").
- Take enterprise-deal RFPs that take more than 10 hours of somdipto's time.
- Re-brand. The brand is "Dan Lab" (or whatever somdipto confirms in week 1).
- **v111 addition:** Ship HRM-Text marketing before audiod v1.3 ships.
- **v111 addition:** Open Telegram group allowlist before 100 paired users.

---

## 9. Open Questions for somdipto (v111, with deadlines)

1. **danlab.dev access** — *blocking, this week.* Who owns the stack? React + Vite? Static? What is the deploy path?
2. **Brand naming** — *blocking, this week.* DanLab for research, "Dan" for consumer? Or one brand?
3. **Twitter handle availability** — *blocking, this week.* @danaboratory vs @danlab_dev vs @somdipto?
4. **HRM-Text-1B integration** — *FYI.* When audiod v1.3 ships, do we lead with "reasoning on the wearable" or stay quiet?
5. **Telegram pairing** — *FYI.* Keep `pairing` policy or move to `allowlist` when we have 50+ users?
6. **Press embargo** — *Q3 OKR.* What is the next real milestone we can anchor a Show HN to?
7. **EigenCloud regional launch** — *Q3 OKR.* When do Mumbai / Bengaluru regions come online? This is a marketing timing question.

---

*Strategy complete. v111 calendar, Twitter pack, landing copy, and README suggestions live in sibling files.*
