# DanLab Marketing Strategy — Run v110
**Date:** 2026-06-29
**Owner:** DAN-1
**Inputs:** dan1-marketing-research.v110.md
**Status:** Strategy set. All five streams have concrete 30-day deliverables.

---

## 0. North Star

> **Make "Dani" the most-trusted open personal-AI platform in the world — measured by monthly active developers, monthly active users of the Dan Voice app, and monthly GitHub stars across the org.**

Three numbers we will repeat every Monday:
- **MAD** — Monthly Active Developers (target: 1k by end of Q3, 10k by end of Q4)
- **MAU** — Monthly Active Users across Dan Voice / Dan Glasses (target: 10k end of Q3, 100k end of Q4)
- **GH-stars** — sum across [dan-consciousness](https://github.com/somdipto/dan-consciousness), [dani](https://github.com/somdipto/dani), [paperclip](https://github.com/somdipto/paperclip), [danlab-multimodal](https://github.com/somdipto/danlab-multimodal), [dan-glasses](https://github.com/somdipto/dan-glasses) (target: 5k end of Q3, 25k end of Q4)

These three numbers are how we will measure whether marketing is working.

---

## 1. Positioning (lock this in writing)

### One-line positioning
> **DanLab builds proactive, private AI wearables and personal agents — your data, your cloud, your face. Built from India, for the world.**

### Three-line positioning
> Most AI assistants wait for you to ask a question and then phone home with your data. Dan agents watch, remember, and act — inside your own verifiable cloud container. Open source SDK. Sub-250MB on-device VLMs. From Bangalore to the world.

### Five anti-positions (what we are NOT)
1. **NOT reactive chat.** We are *proactive*. The agent watches the room and only speaks when worth speaking.
2. **NOT cloud-only.** Every Dan runs an on-device fleet (audiod, perceptiond, memoryd, toold, ttsd, os-toold) that does not require a server.
3. **NOT data-harvesting.** No per-user data ever leaves the user’s EigenCloud TEE container. We literally cannot read it.
4. **NOT walled garden.** Dan Agent SDK is MIT. Any developer can register a tool that runs in any user’s container.
5. **NOT colonial AI.** We are not "Silicon Valley with a Bangalore office." The brain is built here, the hardware is sourced here, and the engineering culture is ours.

---

## 2. Audience Pyramid

We sell to four audiences in strict priority order. **Do not try to talk to all four at once.**

### Layer 1 — Builders & Operators (10k target by Q3)
- **Who:** AI engineers, agent-platform CTOs, indie hackers writing workflow tools.
- **Where they live:** GitHub Trending, Hacker News, /r/LocalLLaMA, r/MachineLearning, HuggingFace Discord, Paperclip repo watchers.
- **What they care about:** Can I run this on my laptop tonight? Does the SDK let me ship a tool? Is the architecture honest?
- **Channel:** README + demo video + Show HN. Engineering blogs. Whitepapers.
- **KPI:** GitHub stars across org, new contributors per month, MCP tool integrations shipped.

### Layer 2 — Knowledge Workers (100k target by Q4)
- **Who:** Daily Gmail + Notion + Slack + Calendar users; "I would pay $20/mo for a real Jarvis" demographic. Age 28–45, English-fluent, white-collar, chronically online.
- **Where they live:** Product Hunt, LinkedIn, Twitter, Product-Led Alliance, Lenny’s Newsletter.
- **What they care about:** Does it actually do expense reports end-to-end? Does it work with my earbuds? Can I trust it with my inbox?
- **Channel:** Dan Voice app landing page, Product Hunt launch, paid ads retargeting from LinkedIn/Twitter.
- **KPI:** App installs, free→paid conversion, week-4 retention.

### Layer 3 — Wearable Early-Adopters (10k target by Q4)
- **Who:** Builders who already flashed a Pinephone, owners of a Steam Deck, attendees of FOSDEM/CCC/DEF CON hardware villages. Comfortable installing .deb packages.
- **Where they live:** Hacker News "Show HN", /r/smartglasses, the Even Realities Discord, the Brilliant Labs Discord, CES hardware forums.
- **What they care about:** Real BOM cost. Battery. Repairability. Open SDK. Does it survive a coffee spill?
- **Channel:** Track A landing page, GitHub README for dan-glasses, conference talks.
- **KPI:** Demos at conferences, .deb installs reported, GitHub stars on dan-glasses repo.

### Layer 4 — Enterprise Pilot Buyers (10 named accounts by Q4)
- **Who:** Operations VPs at mid-size BPOs (India), travel agencies (SEA), journalism teams (US/EU), executive-assistant firms.
- **Where they live:** Sequoia Surge cohort, YC W26 partner intros, your local startup Grind events in Bangalore.
- **What they care about:** SOC2-style attestation, EigenCloud TEE audit trail, agent audit log, custom workflow build-out timeline.
- **Channel:** Direct outreach from somdipto, Opentensor-style pilots, EigenCloud partner program.
- **KPI:** Pilots signed, MRR, agent executions per pilot account.

---

## 3. Channels — Pick Three, Own Them

We do **not** do all-of-the-above. Three channels only.

### Channel A — GitHub + Show HN (engineering credibility)
- Three repos to rise first: **dan-consciousness** (our brain), **dani** (agent platform), **paperclip** (orchestration).
- Add a HACKATHON.md to danlab-multimodal pointing to the asciinema demo.
- Post one Show HN when ready (anchor: the 9/9-daemon foundation stream milestone + a 90-second demo video).
- Publish a one-page architecture PDF on each repo’s Releases. Linked from the README.

### Channel B — Twitter / X (single-voice thought leadership)
- One handle only — **@danaboratory** (or whatever somdipto confirms is available).
- Beat: 1 technical thread / week, 1 build-in-public post / week, 1 hot-take / fortnight.
- NO generic AI hype tweets. Every tweet must reference code, a real metric, or a shipped artifact.
- Profile pinned tweet: the 9/9 daemons live screenshot.

### Channel C — YouTube (long-form demo + conference talks)
- One 90-second "9 daemons live, no cloud required" demo. Posted to YouTube Shorts + LinkedIn + Twitter.
- One 12-minute "Watchful AI: how Dan Glasses sees without always-on recording" technical talk.
- Re-use the same demo for India AI Summit, FOSDEM, and Web Summit Bangalore pitches.

What we **do NOT** spend time on:
- Instagram / TikTok (wrong audience, no time)
- Medium (ghost-town for AI readers)
- Newsletters we cannot commit to weekly
- Paid ads until we have a self-serve funnel that converts >2%

---

## 4. Narrative Arcs (the stories we tell)

We have **three** narratives we can run, in order of priority.

### Arc 1 — "From India to AGI"
The canonical origin story. somdipto in Bangalore, building the brain alone, then with Dani as a co-founder. The technical mark of this is the dan-consciousness repo — public, MIT, auditable. Every blog post, every conference talk, every press piece should reference this repo.
- **Sample tweet:** "We are building AGI from India. Our brain lives at github.com/somdipto/dan-consciousness. MIT licensed. Read the source."

### Arc 2 — "Privacy by architecture"
Every other AI wearable phones home. Ours does not. This is the deepest technical differentiator, and the one most likely to matter to the press. Anchor it in eigencloud attestation screenshots in the app.
- **Sample tweet:** "Quark: data in Alibaba cloud. Meta: data in Meta cloud. Dan: data in *your* cloud. We cannot read your emails even if we wanted to."

### Arc 3 — "Proactive, not reactive"
The product thesis. Watchful mode at the daemon level. The salience gate in perceptiond. The proactive trigger engine in Dan Voice. This is what will make Google Glass "hindsight goggles" look like 2014.
- **Sample tweet:** "Most smart glasses wait for you to ask. Ours watches for context shifts and asks first. Try it (demo link)."

---

## 5. 30-Day Tactical Plan (concrete + measurable)

### Week 1 (June 30 – July 6)
- [ ] somdipto confirms brand naming and Twitter handle (blocking).
- [ ] Set up `dan-lab` GitHub org with topic tagging for the 8 hero repos.
- [ ] Polish the danlab-multimodal README so it ranks "sub-250MB multimodal" on Hacker News' front page within 30 days.
- [ ] Publish Show HN draft on Show HN sandbox. Have 3 reviewers.
- [ ] One tweet: "9/9 daemons live, open source, runs on a Linux laptop. We are building proactive AI from India."

### Week 2 (July 7 – 13)
- [ ] Ship the architecture PDF for dan-glasses (one-pager per layer).
- [ ] Publish the "9 daemons live" demo video on YouTube Shorts + LinkedIn.
- [ ] Post technical thread: "How to build a proactive AI wearable on a $0 budget" — link the build plan.
- [ ] Submit Paperclip to https://news.ycombinator.com as "Show HN".

### Week 3 (July 14 – 20)
- [ ] Publish the Dan Voice landing page (Track B) at danlab.ai/dan-voice.
- [ ] Set up Lead magnet: "The India AGI Builder's Manifest" — 5-page PDF in exchange for email. Captures Layer 2 audience.
- [ ] One cold outreach to 3 SE-Asia travel-agency ops VPs about a Dan Voice pilot.

### Week 4 (July 21 – 27)
- [ ] Publish the Dan Glasses landing page (Track A) at danlab.ai/glasses.
- [ ] Pin the "watchful mode" demo video on the GitHub README of dan-glasses.
- [ ] Burn down the punchlist (separate file) — what is not done by July 27 is rolled into Q3 OKRs.

### End-of-month metrics dashboard
- GH stars (sum of org) = ___
- New Twitter followers = ___
- Show HN rank peak = ___
- App installs (if Track B demo is live) = ___

---

## 6. Brand Voice Rules (so we sound like one company)

- **Direct.** Short sentences. Active voice. Verbs before nouns.
- **Specific numbers over adjectives.** "9 of 9 daemons live" beats "highly reliable."
- **Substance over polish.** Better to ship an ugly README with real code than a slick README with no code.
- **No buzzword soup.** Banned words: "revolutionary," "game-changing," "next-gen," "AI-powered" (says who?).
- **Indian origin is the asset, not the asterisk.** "From India" is in our bio. Not "also from India."
- **Honest about limits.** "This is a heuristic, not RL. SIA fork coming." beats overclaiming.
- **Pronouns and voice:** first-person plural ("we"). Never "the company."

---

## 7. Risks + Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Quark or Meta ships parity feature | High | Medium | We win on privacy + open SDK. Lean into the architecture story. |
| Show HN is a flop | Medium | Medium | Pre-warm the post 48h earlier with the danlab-multimodal asciinema. Recruit 5 commenters. |
| somdipto becomes single-point-of-failure for shipping | High | High | Document the 9-daemon bootstrap one-liner. Recruit a part-time devops hire via the open roles channel. |
| EigenCloud pricing shock for paid tier | Medium | High | Anchor pricing to Indian mobile-phone data plans (₹399/month entry tier). |
| Open-source competitor forks Paperclip and out-executes us | Medium | Medium | Maintain a 6-month technical lead via dan-consciousness and proprietary prompts. |

---

## 8. What we will not do this quarter

- Hire a marketing agency.
- Spend on paid ads.
- Launch a Discord before we have 1k MAU.
- Publish thought-leadership content in the abstract ("the future of AI").
- Take enterprise-deal RFPs that take more than 10 hours of somdipto’s time.
- Re-brand. The brand is "Dan Lab" (or whatever somdipto confirms in week 1).

---

## 9. Open Questions for somdipto (carry from research doc)

1. Brand naming — DanLab for research, "Dan" for consumer? Or one brand?
2. Twitter handle availability — @danaboratory vs @danlab_dev vs @somdipto?
3. Are we OK publishing EigenCloud pricing on the landing page now, or wait?
4. Who is the public face for press — somdipto, or do we want a second co-founder on-camera?
5. Press embargo window — what is the next real milestone we can anchor a Show HN to?

---

*Strategy complete. Tactical artifacts (content calendar, Twitter content, landing copy, README suggestions) live in sibling v110 files.*
