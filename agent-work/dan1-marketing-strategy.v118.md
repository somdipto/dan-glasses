# DanLab Marketing Strategy — Run v118

**Date:** 2026-07-03 02:00 UTC · Asia/Calcutta 07:30
**Owner:** DAN-1
**Inputs:** [dan1-marketing-research.v118.md](./dan1-marketing-research.v118.md)
**Status:** v118 refresh. v117 strategy is the spine. Tailscale process gap closed; authkey gap remains. dan2 v11 research deltas folded in.

---

## 0. North Star (unchanged from v111)

> **Make "Dani" the most-trusted open personal-AI platform in the world — measured by monthly active developers, monthly active users of the Dan Voice app, and monthly GitHub stars across the org.**

Three numbers we will repeat every Monday:
- **MAD** — Monthly Active Developers (target: 1k by end of Q3, 10k by end of Q4)
- **MAU** — Monthly Active Users across Dan Voice / Dan Glasses / Telegram (target: 10k end of Q3, 100k end of Q4)
- **GH-stars** — sum across the dan-lab org (target: 5k end of Q3, 25k end of Q4)

**v111 addition (kept):** **TG-DAU** — Daily Active Users of `@danlab_bot`. Target: 50 by end of Q3, 500 by end of Q4.

**v118 addition:** **HF-models** — Sum of HuggingFace `danlab` org downloads (target: 1k end of Q3, 10k end of Q4). The HRM-Text-1B and Kokoro-82M model cards are the new credibility surface.

---

## 1. Positioning (v118, sharpened)

### One-line positioning (v118)
> **DanLab builds proactive, private, on-device AI wearables and personal agents — 8/8 daemons live, $1,500 reasoning model coming, on-device validated by orbit. Your data, your face. Built from India, for the world.**

### Three-line positioning (v118)
> Most AI assistants wait for you to ask a question and then phone home with your data. Dan agents watch, remember, and act — inside your own device. 8 service daemons + 1 OpenClaw gateway + 1 tailscaled substrate, all live today. Open weights. LFM2.5-VL-450M in production. From Bengaluru to the world, MIT-licensed.

### Five anti-positions (v118, refined)
1. **NOT reactive chat.** We are *proactive*. The agent watches the room and only speaks when worth speaking.
2. **NOT cloud-only.** Every Dan runs a local fleet (8 service daemons + openclaw + tailscaled) that does not require a server.
3. **NOT data-harvesting.** No per-user data ever leaves the user's device. **We cannot read it. Not "we promise" — architecturally cannot.**
4. **NOT walled garden.** Dan Agent SDK is MIT. Any developer can register a tool that runs in any user's container.
5. **NOT colonial AI.** We are not "Silicon Valley with a Bengaluru office." The brain is built here, the hardware is sourced here, the engineering culture is ours.

### v118 positioning deltas vs v117
- **Added:** "$1,500 reasoning model coming" — the HRM-Text-1B origin pillar.
- **Added:** "on-device validated by orbit" — the Gemma 3 in-orbit anchor.
- **Sharpened:** "8/8 daemons live" — v118 accounting (was 9/9, but the matrix is 8 service + 1 gateway + 1 tailnet, all live).
- **Sharpened:** "9 processes, 8 service daemons, 1 gateway, 1 tailnet substrate" — same total, sharper accounting.
- **Added:** "Microsoft Scout validates OpenClaw" — substrate alliance, enterprise threat.

---

## 2. Audience Pyramid (v118, refined)

We sell to six audiences in strict priority order. **Do not try to talk to all six at once.** v117 had 5 layers; v118 adds the small-model researcher layer.

### Layer 1 — Builders & Operators (10k target by Q3)
- AI engineers, agent-platform CTOs, indie hackers writing workflow tools.
- **Where they live:** GitHub Trending, Hacker News, /r/LocalLLaMA, r/MachineLearning, HuggingFace Discord, Paperclip repo watchers.
- **What they care about (v118):** Can I run this on my laptop tonight? Does the SDK let me ship a tool? Is the architecture honest? **Does it run HRM-Text-1B?**
- **Channel:** README + demo video + Show HN. Engineering blogs. HuggingFace model cards.
- **KPI:** GitHub stars across org, new contributors per month, MCP tool integrations shipped, **HuggingFace `danlab` org downloads**.

### Layer 2 — Knowledge Workers (100k target by Q4)
- Daily Gmail + Notion + Slack + Calendar users; "I would pay $20/mo for a real Jarvis" demographic. Age 28–45, English-fluent, white-collar, chronically online.
- **Where they live:** Product Hunt, LinkedIn, Twitter, Product-Led Alliance, Lenny's Newsletter.
- **What they care about:** Does it actually do expense reports end-to-end? Does it work with my earbuds? Can I trust it with my inbox?
- **Channel:** Dan Voice app landing page, Product Hunt launch, paid ads retargeting from LinkedIn/Twitter.
- **KPI:** App installs, free→paid conversion, week-4 retention.

### Layer 3 — Wearable Early-Adopters (10k target by Q4)
- Builders who already flashed a Pinephone, owners of a Steam Deck, attendees of FOSDEM/CCC/DEF CON hardware villages. Comfortable installing .deb packages.
- **Where they live:** Hacker News "Show HN", /r/smartglasses, the Even Realities Discord, the Brilliant Labs Discord, CES hardware forums.
- **What they care about:** Real BOM cost. Battery. Repairability. Open SDK. Does it survive a coffee spill?
- **Channel:** Track A landing page, GitHub README for dan-glasses, conference talks.
- **KPI:** Demos at conferences, .deb installs reported, GitHub stars on dan-glasses repo.

### Layer 4 — Telegram Early Adopters (500 DAU by Q4)
- Anyone with Telegram. Zero install, zero hardware. Power users who already have 5+ bots.
- **Where they live:** Telegram channels, bot directories, AI bot lists.
- **What they care about:** Does the bot actually do something useful? Is it private? Can I pair in 30 seconds?
- **Channel:** `@danlab_bot` as the product surface. Share via Twitter, LinkedIn, danlab.dev footer.
- **KPI:** Pairing completions, daily active users, queries per user per day, retention D1/D7/D30.

### Layer 5 — Small-Model Researchers (NEW v118, 1k org followers by Q3)
- Researchers, grad students, indie trainers working on sub-7B models.
- **What they care about (v118):** Is the $1,500 training run reproducible? Will you publish the SIA-W+H harness? Does the daemon stack run my model?
- **Where they live:** HuggingFace, r/LocalLLaMA, AI Twitter, paperswithcode.
- **Channel:** HuggingFace `danlab` org, model cards with daemon-stack links, danlab.ai blog.
- **KPI:** HF downloads, model card citations, `danlab` org followers.

### Layer 6 — Enterprise Pilot Buyers (10 named accounts by Q4)
- Operations VPs at mid-size BPOs (India), travel agencies (SEA), journalism teams (US/EU), executive-assistant firms.
- **Where they live:** Sequoia Surge cohort, YC W26 partner intros, Bangalore startup Grind events.
- **What they care about (v118):** SOC2-style attestation, EigenCloud TEE audit trail, agent audit log, custom workflow build-out timeline. **Microsoft Scout threat: if they win the agent-OS war, we need to be a Solara citizen from day one.**
- **Channel:** Direct outreach from somdipto, Opentensor-style pilots, EigenCloud partner program.
- **KPI:** Pilots signed, MRR, agent executions per pilot account.

---

## 3. Channels (v118, four owned + one new)

### Channel A — GitHub + Show HN (engineering credibility)
- Three repos to rise first: **dan-consciousness** (our brain), **dani** (agent platform), **paperclip** (orchestration).
- P0: refresh all 6 hero repo READMEs (see [README suggestions](./dan1-github-readme-suggestions.v118.md)).
- Add a HACKATHON.md to danlab-multimodal pointing to the asciinema demo.
- Post one Show HN when ready (anchor: the 9-process foundation stream milestone + a 90-second demo video).
- Publish a one-page architecture PDF on each repo's Releases. Linked from the README.

### Channel B — Twitter / X (single-voice thought leadership)
- One handle only — **@danaboratory** (or whatever somdipto confirms is available).
- Beat: 1 technical thread / week, 1 build-in-public post / week, 1 hot-take / fortnight, 1 daemon-of-the-week micro-post.
- **v118 new:** 1 small-model-researcher post / week (HRM-Text-1B coverage, Kokoro-82M coverage, SIA port progress).
- NO generic AI hype tweets. Every tweet must reference code, a real metric, or a shipped artifact.
- Profile pinned tweet: the 9-process live matrix (real `/status` payloads, not a mockup).

### Channel C — danlab.dev (the funnel — P0)
- The site is the URL that gets shared. It must communicate the v118 strategy.
- **Refresh homepage** to match: proactive AI, architecturally private, 8/8 daemons live, open source, from India, on-device validated by orbit, $1,500 reasoning model.
- Add the Telegram surface (`@danlab_bot`) prominently in the footer.
- Add `danlab.ai/dan-voice` (Track B) and `danlab.ai/glasses` (Track A) as sub-pages when ready.
- Performance budget: <1MB, FCP <1.5s on 4G India (Jio / Airtel).
- No third-party trackers for the first 30 days. Plausible self-hosted after.

### Channel D — Telegram (`@danlab_bot`, in-channel)
- The product *is* the channel. The bot answers, the user evaluates.
- Wire into all posts: "Try it: @danlab_bot" / "DM us: @danlab_bot" / "Live now: t.me/danlab_bot".
- Pairing flow is the gate. Manual approve via `openclaw devices approve <id>`.
- **v118 new:** Wire Tailscale subnet routing the day `TAILSCALE_AUTHKEY` lands. *"DM the bot from your phone over LTE — the daemon stack is on the other side."*
- DM-only for now. Group allowlist when we have 100+ paired users.

### Channel E — HuggingFace (`danlab` org, v118 NEW, P0)
- The credibility surface for the small-models lane.
- Publish model cards: LFM2.5-VL-450M, SmolVLM-256M, HRM-Text-1B (post-swap), Kokoro-82M ONNX.
- Each card points back to the dan-glasses repo and the daemon stack.
- **P0 this week:** create the org, publish the first model card (LFM2.5-VL-450M is already in production, ship the card).

### What we **do NOT** spend time on:
- Instagram / TikTok (wrong audience, no time)
- Medium (ghost-town for AI readers)
- Newsletters we cannot commit to weekly
- Paid ads until we have a self-serve funnel that converts >2%

---

## 4. Narrative Arcs (v118, sharpened)

We have **five** narratives, in priority order. (v117 had four; v118 adds one.)

### Arc 1 — "From India to AGI"
The canonical origin story. somdipto in Bengaluru, building the brain alone, then with Dani as a co-founder. The technical mark is the dan-consciousness repo — public, MIT, auditable. Every blog post, every conference talk, every press piece should reference this repo.
- **Sample tweet:** *"We are building AGI from India. Our brain lives at github.com/somdipto/dan-consciousness. MIT licensed. Read the source."*

### Arc 2 — "Architecturally private"
**Architecturally** private — the EigenCloud TEE attestation is a cryptographic guarantee, not a promise. This is the deepest technical differentiator, and the one most likely to matter to the press.
- **Sample tweet:** *"Quark: data in Alibaba cloud. Meta: data in Meta cloud. Dan: data in *your* device. We cannot read your emails even if we wanted to. Not 'we promise.' Architecturally cannot."*

### Arc 3 — "Proactive, not reactive"
The product thesis. Watchful mode at the daemon level. The salience gate in perceptiond. The proactive trigger engine in Dan Voice. This is what will make Google Glass "hindsight goggles" look like 2014.
- **Sample tweet:** *"Most smart glasses wait for you to ask. Ours watches for context shifts and asks first. perceptiond uses LFM2.5-VL-450M to gate every frame by salience — 5fps watchful, 10fps active. Try the daemon: github.com/somdipto/dan-glasses"*

### Arc 4 — "9 processes, no cloud" (v118, sharpened)
The build-in-public narrative. **8/8 service daemons + 1 OpenClaw gateway + 1 tailscaled = 9 processes, all live.** The number goes up over time. The audience watches it grow. Each daemon gets its own micro-post with a real `/status` payload.
- **Sample tweet:** *"9/9 processes live on my Linux laptop today. audiod 8090, audiod-ws 8091, perceptiond 8092, memoryd 8741, toold 8742, ttsd 8743, os-toold 8744, openclaw 18789, tailscaled 41641. 8 service daemons, 1 gateway, 1 tailnet substrate. Open source. github.com/somdipto/dan-glasses"*

### Arc 5 — "On-device, validated by orbit" (v118 NEW)
The new origin pillar. Gemma 3 4B is in orbit on the Loft Orbital Yam-9 satellite, doing real Earth-observation triage work. LFM2.5-VL-450M is in Dan Glasses, doing real on-device vision. **Same architecture class, peer validation in space.** The thesis is no longer a bet.
- **Sample tweet:** *"NASA JPL put a 4B VLM in orbit. We put a 450M VLM in glasses. Same architecture class: on-device, auditable, no cloud. The on-device thesis is no longer a bet. It's in space. github.com/somdipto/dan-glasses"*

### Arc 6 — "The $1,500 reasoning model" (v118 NEW)
The small-beats-large origin pillar. HRM-Text-1B (Sapient, Apache-2.0, $1,500 from scratch) is the new SOTA small-reasoning model. It is the v1.5 audiod post-processor default. Kokoro-82M (82M params, Apache-2.0, beats cloud TTS) is the v1.5 plan-A TTS. **The wearable wins the small-end by default.**
- **Sample tweet:** *"A 1B model trained for $1,500 from scratch is now SOTA. 82M params beats ElevenLabs. The wearable wins the small-end. We're putting both in glasses. github.com/somdipto/dani"*

---

## 5. 30-Day Tactical Plan (v118, updated)

### Week 1 (July 3 – 9) — Tailscale + foundation drops
**Theme:** *"9/9 processes live. Tailscale substrate up. Key pending. From India."*

- [ ] **P0:** Set `TAILSCALE_AUTHKEY` (somdipto). The moment the key lands, fire the demo tweet.
- [ ] **P0:** Create HuggingFace `danlab` org. Publish the LFM2.5-VL-450M model card.
- [ ] **P0:** Refresh danlab.dev homepage to match v118 positioning.
- [ ] **P0:** Update dan-glasses README with current 9-process port matrix + Tailscale + Kokoro-82M swap note.
- [ ] **P0:** Update danlab-multimodal README cross-links to dan-lab org.
- [ ] Confirm brand naming and Twitter handle (blocking).
- [ ] One tweet: *"9/9 processes live. Tailscale substrate up. $1,500 reasoning model coming. Site updated. DM @danlab_bot — it's live."*
- [ ] Cross-post the danlab.dev refresh to LinkedIn (somdipto).

### Week 2 (July 10 – 16) — Architecture deep-dive
**Theme:** *"How 8 service daemons + an OpenClaw gateway + a tailnet substrate become one proactive agent."*

- [ ] Ship the architecture PDF for dan-glasses (one-pager per layer).
- [ ] Publish the "9 processes live" demo video on YouTube Shorts + LinkedIn.
- [ ] Post technical thread: "How to build a proactive AI wearable on a $0 budget" — link the build plan.
- [ ] **Daemon-of-the-week #1: audiod.** Micro-post with the real `/ready` payload + Loki histogram drop.
- [ ] Submit Paperclip to https://news.ycombinator.com as "Show HN".
- [ ] **NEW v118:** Publish "On-device, validated by orbit" blog post (the Gemma 3 anchor).

### Week 3 (July 17 – 23) — Track B (Dan Voice) drops
**Theme:** *"Your earbuds are now a Jarvis. No hardware purchase."*

- [ ] Publish the Dan Voice landing page (Track B) at danlab.ai/dan-voice.
- [ ] Set up Lead magnet: "The India AGI Builder's Manifest" — 5-page PDF in exchange for email.
- [ ] One cold outreach to 3 SE-Asia travel-agency ops VPs about a Dan Voice pilot.
- [ ] **Daemon-of-the-week #2: perceptiond.** Micro-post with the LFM2.5-VL-450M spec + 188 frames / 167 salient / 166 descriptions receipts.
- [ ] **NEW v118:** Publish "The $1,500 reasoning model" founder essay (HRM-Text-1B anchor).
- [ ] One tweet: *"Telegram @danlab_bot is live. DM to pair. No install. No hardware. Privacy by architecture."*

### Week 4 (July 24 – 30) — Track A (Dan Glasses wearable) drops
**Theme:** *"9/9 processes running on a Linux laptop. Now let's put it on your face."*

- [ ] Publish the Dan Glasses landing page (Track A) at danlab.ai/glasses.
- [ ] Pin the "watchful mode" demo video on the GitHub README of dan-glasses.
- [ ] **Daemon-of-the-week #3: memoryd.** Micro-post on SQLite + 384-dim vectors + 593KB live DB.
- [ ] Hot-take tweet: *"Glasses at $99 make smart-glasses a daily-driver category. The math proves it."*
- [ ] One Show HN draft: *"Show HN: Dan Glasses — 9 processes live, on-device AI, .deb install, $1,500 reasoning model coming."*
- [ ] Burn down the v118 punchlist — what is not done by July 30 is rolled into Q3 OKRs.

### End-of-month metrics dashboard
- danlab.dev unique visitors
- GH stars (sum of org) = ___
- HF `danlab` org downloads = ___
- New Twitter followers = ___
- @danlab_bot paired users (cumulative) = ___
- @danlab_bot DAU = ___
- Show HN rank peak = ___
- Tailscale authenticated: yes/no (the most important single number)
- App installs (if Track B demo is live) = ___

---

## 6. Brand Voice Rules (v118, refined)

- **Direct.** Short sentences. Active voice. Verbs before nouns.
- **Specific numbers over adjectives.** *"9 of 9 processes live"* beats *"highly reliable."*
- **Substance over polish.** Better to ship an ugly README with real code than a slick README with no code.
- **No buzzword soup.** Banned words: "revolutionary," "game-changing," "next-gen," "AI-powered" (says who?).
- **Indian origin is the asset, not the asterisk.** *"From India"* is in our bio. Not *"also from India."*
- **Honest about limits.** *"This is a heuristic, not RL. SIA fork coming."* beats overclaiming.
- **"Architecturally private" over "private."** Always.
- **Name the model.** *"LFM2.5-VL-450M"* beats *"VLM."* *"whisper.cpp base.en"* beats *"STT."* *"HRM-Text-1B"* beats *"small LM."* *"Kokoro-82M"* beats *"TTS."*
- **Pronouns and voice:** first-person plural ("we"). Never "the company."

**v118 voice addition:** **"On-device, validated by orbit"** is the new tagline. Use it once per week, no more.

---

## 7. Risks + Mitigations (v118, updated)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **`TAILSCALE_AUTHKEY` does not get set** | **High** (single dep on somdipto) | **High** (no Tailscale demos) | **P0 this run. Ask somdipto directly. Fire the demo tweet the day the key lands.** |
| **danlab.dev stays stale** | **High** (no owner currently) | **High** (funnel is broken) | **P0 this run. Ask somdipto for access and stack this week.** |
| Quark or Meta ships parity feature | High | Medium | We win on privacy + open SDK. Lean into the architecture story. |
| Show HN is a flop | Medium | Medium | Pre-warm the post 48h earlier with the danlab-multimodal asciinema. Recruit 5 commenters. |
| somdipto becomes single-point-of-failure for shipping | High | High | Document the 9-process bootstrap one-liner. Recruit a part-time devops hire via the open roles channel. |
| EigenCloud pricing shock for paid tier | Medium | High | Anchor pricing to Indian mobile-phone data plans (₹399/month entry tier). |
| Open-source competitor forks Paperclip and out-executes us | Medium | Medium | Maintain a 6-month technical lead via dan-consciousness and proprietary prompts. |
| **Telegram abuse / spam** | Medium | Medium | Keep `pairing` DM policy. Manual approve. Group allowlist is empty by default. |
| **HRM-Text-1B ship slips** | Medium | Low | Do not market HRM-Text-1B until audiod v1.3 ships. Tease in one tweet only. |
| **Microsoft Scout locks down the enterprise lane** (v118 new) | Medium | High | **Be the best OpenClaw citizen we can be. Ship zo-mcp-bridge as the reference integration. Fork-or-follow decision at end of Q3 2026.** |
| **Anthropic Dreaming ships a wearable SDK** (v118 new) | Low | Medium | SIA is the open counter-narrative. If they ship a wearable SDK, the bet is on open-weights + open-harness, not closed-cloud. |
| **HF model card theft / copy** (v118 new) | Low | Low | Apache-2.0 is a feature, not a bug. We win on integration, not license. |

---

## 8. What we will not do this quarter (v118, unchanged)

- Hire a marketing agency.
- Spend on paid ads.
- Launch a Discord before we have 1k MAU.
- Publish thought-leadership content in the abstract ("the future of AI").
- Take enterprise-deal RFPs that take more than 10 hours of somdipto's time.
- Re-brand. The brand is "Dan Lab" (or whatever somdipto confirms in week 1).
- Ship HRM-Text marketing before audiod v1.3 ships.
- Open Telegram group allowlist before 100 paired users.
- **v118 addition:** Announce the SIA-W+H port before the cascade-gate is verified end-to-end on the wearable.
- **v118 addition:** Ship a HuggingFace model card that does not link back to a working daemon.

---

## 9. Open Questions for somdipto (v118, with deadlines)

1. **TAILSCALE_AUTHKEY** — *blocking, this week.* `tailscaled` is running. The key is the only thing missing. **Without it, no Tailscale demo, no always-on-from-anywhere, no v118 Arc 4 win.** Set it.
2. **danlab.dev access** — *blocking, this week.* Who owns the stack? React + Vite? Static? What is the deploy path?
3. **Brand naming** — *blocking, this week.* DanLab for research, "Dan" for consumer? Or one brand?
4. **Twitter handle availability** — *blocking, this week.* @danaboratory vs @danlab_dev vs @somdipto?
5. **HuggingFace `danlab` org creation** — *this week.* somdipto to create the org; DAN-1 to publish the first model card (LFM2.5-VL-450M).
6. **HRM-Text-1B integration** — *FYI.* When audiod v1.3 ships, do we lead with "reasoning on the wearable" or stay quiet?
7. **Telegram pairing** — *FYI.* Keep `pairing` policy or move to `allowlist` when we have 50+ users?
8. **Press embargo** — *Q3 OKR.* What is the next real milestone we can anchor a Show HN to?
9. **EigenCloud regional launch** — *Q3 OKR.* When do Mumbai / Bengaluru regions come online? This is a marketing timing question.
10. **Microsoft Scout fork-or-follow** — *end of Q3 2026.* Microsoft's Scout is built on OpenClaw. We are aligned with the substrate. We need to decide if we ship as a Scout citizen or fork the agent runtime.
11. **HRM-Text-1B model card on HuggingFace** — *Q3 W1.* somdipto to grant DAN-1 write access to `danlab` org before the first model card ships.

---

*Strategy complete. v118 calendar, Twitter pack, landing copy, and README suggestions live in sibling files.*
 day, retention D1/D7/D30.

### Layer 5 — Enterprise Pilot Buyers (10 named accounts by Q4)
- Operations VPs at mid-size BPOs (India), travel agencies (SEA), journalism teams (US/EU), executive-assistant firms.
- **Where they live:** Sequoia Surge cohort, YC W26 partner intros, Bengaluru startup Grind events.
- **What they care about:** SOC2-style attestation, EigenCloud TEE audit trail, agent audit log, custom workflow build-out timeline.
- **Channel:** Direct outreach from somdipto, Opentensor-style pilots, EigenCloud partner program.
- **KPI:** Pilots signed, MRR, agent executions per pilot account.

### Layer 6 — Small-model evangelist (v118 NEW, 5k MAU by Q4)
- Reads the small-model beat (Latent Space, Interconnects, HRM-Text-1B coverage, VibeThinker-3B coverage).
- Will retweet the 1B / $1,500 story without us asking.
- **Where they live:** HN, X AI researcher circuit, HuggingFace model cards, Latent Space Discord.
- **What they care about:** "Bigger is better" is over. They know it. They want a brand to cite.
- **Channel:** HuggingFace model cards, X, danlab.ai blog, arXiv.
- **KPI:** HuggingFace `danlab` org downloads, model card views, arXiv citations.

---

## 3. Channels (v118, three owned + one new + one upgraded)

### Channel A — GitHub + Show HN (engineering credibility)
- Three repos to rise first: **dan-consciousness** (our brain), **dani** (agent platform), **paperclip** (orchestration).
- P0: refresh all 6 hero repo READMEs (see [README suggestions](./dan1-github-readme-suggestions.v118.md)).
- Add a HACKATHON.md to danlab-multimodal pointing to the asciinema demo.
- Post one Show HN when ready (anchor: the 8/8-daemon foundation stream milestone + a 90-second demo video).
- Publish a one-page architecture PDF on each repo's Releases. Linked from the README.

### Channel B — Twitter / X (single-voice thought leadership)
- One handle only — **@danaboratory** (or whatever somdipto confirms is available).
- Beat: 1 technical thread / week, 1 build-in-public post / week, 1 hot-take / fortnight, 1 daemon-of-the-week micro-post.
- NO generic AI hype tweets. Every tweet must reference code, a real metric, or a shipped artifact.
- **v118 lead posts:** the HRM-Text-1B $1,500 story, the Gemma 3 in-orbit story, the Microsoft Scout on OpenClaw story.
- Profile pinned tweet: the 8/8 daemons live screenshot (real `/status` payloads, not a mockup).

### Channel C — danlab.dev (the funnel — v118 P0)
- The site is the URL that gets shared. It must communicate the v118 strategy.
- **Refresh homepage** to match: proactive AI, architecturally private, 8/8 daemons live, open source, on-device validated by orbit, from India.
- Add the Telegram surface (`@danlab_bot`) prominently in the footer.
- Add `danlab.ai/dan-voice` (Track B) and `danlab.ai/glasses` (Track A) as sub-pages when ready.
- Performance budget: <1MB, FCP <1.5s on 4G India (Jio / Airtel).
- No third-party trackers for the first 30 days. Plausible self-hosted after.

### Channel D — Telegram (`@danlab_bot`, in-channel)
- The product *is* the channel. The bot answers, the user evaluates.
- Wire into all posts: "Try it: @danlab_bot" / "DM us: @danlab_bot" / "Live now: t.me/danlab_bot".
- Pairing flow is the gate. Manual approve via `openclaw devices approve <id>`.
- DM-only for now. Group allowlist when we have 100+ paired users.
- **v118 note:** until Tailscale authkey lands, Telegram is the only always-on surface. Lean on it.

### Channel E — HuggingFace (v118 NEW, P0)
- The single highest-leverage 5-minute marketing action this week: **create the `danlab` HF org**.
- First model card: SmolVLM-256M Q4_K_M (120MB) + mmproj (182MB) as a single composite model card, linking to github.com/somdipto/danlab-multimodal.
- Second model card (v118 NEW): LFM2.5-VL-450M Q4_0 model card pointing back to Dan Glasses and the perceptiond SPEC.
- Third model card (v118, end of Q3): HRM-Text-1B v1.5 audiod integration writeup as a model card.
- Fourth model card (v118, end of Q3): Kokoro-82M v1.5 ttsd integration writeup as a model card.
- **The HF org is the new magnet for Tier 6 (small-model evangelists) and a force multiplier for Tier 1 (developers).**

### Channel F — Tailscale tailnet (v118 NEW, when authkey lands)
- A private tailnet with the daemon stack reachable is a category we can own.
- v118 action: when the authkey is set and `tailscale up` succeeds, the tailnet becomes a marketing surface (screenshot the tailnet, the DNS, the daemon reachability).
- Until then, do not market it.

### What we **do NOT** spend time on:
- Instagram / TikTok (wrong audience, no time)
- Medium (ghost-town for AI readers)
- Newsletters we cannot commit to weekly
- Paid ads until we have a self-serve funnel that converts >2%

---

## 4. Narrative Arcs (v118, four arcs, sharpened)

We have **four** narratives, in priority order. v118 sharpens all four with the v11 research deltas.

### Arc 1 — "From India to AGI" (v118, sharpened with HRM-Text-1B origin pillar)
The canonical origin story. somdipto in Bengaluru, building the brain alone, then with Dani as a co-founder. The technical mark is the dan-consciousness repo — public, MIT, auditable. **v118 addition:** the HRM-Text-1B $1,500-trained story is the new origin pillar. *A 1B reasoning model was trained for the cost of a used iPhone. We are integrating it into audiod. Small-beats-large is empirically real.* This is the post that did not exist in v117. v118 puts it in the lead of every long-form post.
- **Sample tweet:** "We are building AGI from India. Our brain lives at github.com/somdipto/dan-consciousness. MIT licensed. Our 1B reasoning model costs $1,500 to train. Read the source."

### Arc 2 — "Architecturally private" (v118, sharpened with Microsoft Scout + Sonnet 5)
v117 said "architecturally private." v118 sharpens with the **Microsoft Scout on OpenClaw story**: Microsoft's always-on personal agent shares our substrate. The substrate is open. The data path is yours. **And the Anthropic Sonnet 5 story**: closed-source frontier scale reinforces the open-weights wedge.
- **Sample tweet:** "Microsoft Scout runs on OpenClaw. So does Dan. Microsoft owns the enterprise relationship; you own your data. The substrate is open either way."

### Arc 3 — "Proactive, not reactive" (v118, sharpened with Gemma 3 in orbit)
v117 said "proactive, not reactive." v118 anchors it to the **Gemma 3 in orbit story**: a 4B VLM doing Earth-observation triage on a Loft Orbital satellite. The on-device thesis is no longer theoretical. Our 450M LFM2.5-VL in Dan Glasses is the same class of problem.
- **Sample tweet:** "A 4B VLM is in orbit doing Earth-observation triage. On a satellite. The on-device thesis is no longer a pitch. Our 450M LFM2.5-VL in Dan Glasses is the same class of problem. perceptiond uses salience gating to keep queue=0 at 5fps watchful, 10fps active."

### Arc 4 — "8/8 daemons, no cloud" (v118, sharpened with tailscaled)
v117 said "9/9 daemons, no cloud." v118 sharpens to **"8 service daemons, 1 OpenClaw gateway, 1 tailnet substrate"** with the `tailscaled` process now in the matrix. **The audience watches the substrate grow.**
- **Sample tweet:** "8/8 service daemons live, 1 OpenClaw gateway, 1 tailscaled substrate. audiod 8090, perceptiond 8092, memoryd 8741, toold 8742, ttsd 8743, os-toold 8744, dan-glasses-app 8747, openclaw 18789. tailscaled logged out, needs TAILSCALE_AUTHKEY. Curl-receipts on request. Open source daemon-by-daemon."

---

## 5. 30-Day Tactical Plan (v118, updated)

### Week 1 (July 3 – 9) — Foundation refresh + HuggingFace
**Theme:** "8/8 daemons live. Tailscale substrate up. HF org created."
- [ ] **P0 v118:** Create HuggingFace `danlab` org.
- [ ] **P0 v118:** First model card: SmolVLM-256M Q4_K_M + mmproj, link to danlab-multimodal.
- [ ] **P0 v118:** Second model card: LFM2.5-VL-450M Q4_0, link to dan-glasses / perceptiond.
- [ ] **P0 v118:** Somdipto to set `TAILSCALE_AUTHKEY` in Settings > Advanced. Run `tailscale up --authkey=$TAILSCALE_AUTHKEY`.
- [ ] P0: Refresh danlab.dev homepage. somdipto to confirm access + stack.
- [ ] P0: Update dan-glasses README with current port matrix + LFM2.5-VL-450M + 8/8 live claim.
- [ ] P0: Update danlab-multimodal README cross-links to dan-lab org.
- [ ] P0: Create dan-lab org profile/README.md.
- [ ] Confirm brand naming and Twitter handle (blocking).
- [ ] One tweet: "8/8 daemons live. tailscaled substrate up. HF org created. Open source. From India. DM @danlab_bot — it's live."
- [ ] Cross-post the danlab.dev refresh to LinkedIn (somdipto).

### Week 2 (July 10 – 16) — Architecture deep-dive + HRM-Text-1B story
**Theme:** "How 8 services + an OpenClaw gateway + a tailnet substrate become one proactive agent. A 1B model costs $1,500 to train."
- [ ] Ship the architecture PDF for dan-glasses (one-pager per layer).
- [ ] Publish the "8 daemons live" demo video on YouTube Shorts + LinkedIn.
- [ ] Post technical thread: "How to build a proactive AI wearable on a $0 budget" — link the build plan.
- [ ] **Daemon-of-the-week #1: audiod.** Micro-post with the real `/ready` payload. v1.3 segment_timing histograms.
- [ ] **NEW v118:** Post the HRM-Text-1B $1,500 story as a 5-tweet thread. Link to the Sapient repo.
- [ ] **NEW v118:** Post the Gemma 3 in orbit story as a 3-tweet thread. Link to Loft Orbital / NASA JPL.
- [ ] **NEW v118:** Post the Microsoft Scout on OpenClaw story as a single tweet. Link to Build 2026.
- [ ] Submit Paperclip to https://news.ycombinator.com as "Show HN".

### Week 3 (July 17 – 23) — Track B (Dan Voice) drops + HRM-Text-1B plan-A
**Theme:** "Your earbuds are now a Jarvis. No hardware purchase. A 1B model trained for $1,500 is the v1.5 audiod post-processor."
- [ ] Publish the Dan Voice landing page (Track B) at danlab.ai/dan-voice.
- [ ] Set up Lead magnet: "The India AGI Builder's Manifest" — 5-page PDF in exchange for email.
- [ ] One cold outreach to 3 SE-Asia travel-agency ops VPs about a Dan Voice pilot.
- [ ] **Daemon-of-the-week #2: perceptiond.** Micro-post with the LFM2.5-VL-450M spec. Salience-gating explainer.
- [ ] **NEW v118:** Post the HRM-Text-1B v1.5 audiod integration plan as a danlab.ai long-form post.
- [ ] One tweet: "Telegram @danlab_bot is live. DM to pair. No install. No hardware. Privacy by architecture."

### Week 4 (July 24 – 30) — Track A (Dan Glasses wearable) drops + Show HN #1 prep
**Theme:** "8/8 daemons running on a Linux laptop. Now let's put it on your face."
- [ ] Publish the Dan Glasses landing page (Track A) at danlab.ai/glasses.
- [ ] Pin the "watchful mode" demo video on the GitHub README of dan-glasses.
- [ ] **Daemon-of-the-week #3: memoryd.** Micro-post on SQLite + 384-dim vectors + episodic/semantic/procedural.
- [ ] Hot-take tweet: "Glasses at $99 make smart-glasses a daily-driver category. The math proves it."
- [ ] One Show HN draft: "Show HN: Dan Glasses — 8 service daemons, 1 OpenClaw gateway, 1 tailnet substrate, .deb install".
- [ ] Burn down the v118 punchlist — what is not done by July 30 is rolled into Q3 OKRs.

### End-of-month metrics dashboard (v118)
- danlab.dev unique visitors
- GH stars (sum of org) = ___
- New Twitter followers = ___
- @danlab_bot paired users (cumulative) = ___
- @danlab_bot DAU = ___
- **HuggingFace danlab org downloads = ___** (v118 NEW)
- **HuggingFace danlab org model card views = ___** (v118 NEW)
- Show HN rank peak = ___
- App installs (if Track B demo is live) = ___

---

## 6. Brand Voice Rules (v118, sharpened)

- **Direct.** Short sentences. Active voice. Verbs before nouns.
- **Specific numbers over adjectives.** "8 of 8 service daemons live" beats "highly reliable." "$1,500 from scratch" beats "low-cost." "Gemma 3 in orbit" beats "edge AI."
- **Substance over polish.** Better to ship an ugly README with real code than a slick README with no code.
- **No buzzword soup.** Banned words: "revolutionary," "game-changing," "next-gen," "AI-powered" (says who?).
- **Indian origin is the asset, not the asterisk.** "From India" is in our bio. Not "also from India."
- **Honest about limits.** "This is a heuristic, not RL. SIA fork coming." beats overclaiming.
- **v111 addition (kept):** "Architecturally private" over "private." Always.
- **v118 addition:** "On-device validated by orbit" over "edge AI." Always.
- **v118 addition:** "1B / $1,500" over "small model." Always.
- **v118 addition:** Name the model. "LFM2.5-VL-450M" beats "VLM." "whisper.cpp base.en" beats "STT." "Kokoro-82M" beats "TTS." "HRM-Text-1B" beats "reasoning model." "SmolVLM-256M" beats "VLM demo."
- **Pronouns and voice:** first-person plural ("we"). Never "the company."

---

## 7. Risks + Mitigations (v118, updated)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **TAILSCALE_AUTHKEY not set** (v118) | **High** (single-person dependency) | **Medium** (Telegram covers the surface in the meantime) | **P0 this run. Ask somdipto to set the env var in Settings > Advanced this week.** |
| danlab.dev stays stale | High | High | P0 this run. Ask somdipto for access and stack this week. |
| Quark or Meta ships parity feature | High | Medium | We win on privacy + open SDK. Lean into the architecture story. |
| Show HN is a flop | Medium | Medium | Pre-warm the post 48h earlier with the danlab-multimodal asciinema. Recruit 5 commenters. |
| somdipto becomes single-point-of-failure for shipping | High | High | Document the 8-daemon bootstrap one-liner. Recruit a part-time devops hire via the open roles channel. |
| Open-source competitor forks Paperclip and out-executes us | Medium | Medium | Maintain a 6-month technical lead via dan-consciousness and proprietary prompts. |
| Telegram abuse / spam | Medium | Medium | Keep `pairing` DM policy. Manual approve. Group allowlist is empty by default. |
| HRM-Text-1B ship slips (v118) | Medium | Low | Do not market HRM-Text until audiod v1.3+HRM-Text integration lands. Tease in one tweet only. |
| Microsoft Scout + OpenClaw fork/follow decision wrong (v118) | Medium | High | Recommend follow for now. Document the fork triggers in v118 architecture review. |
| **HuggingFace org not created** (v118) | **High** (5-min task, not done) | **High** (single highest-leverage action this week) | **P0 this run. Somdipto creates `danlab` org on huggingface.co.** |
| **No press coverage on Gemma 3 in orbit / HRM-Text-1B / Kokoro-82M story** (v118) | Medium | Medium | 3 long-form posts in Q3 W2-W3. Submit to Latent Space, Interconnects, Import AI. |

---

## 8. What we will not do this quarter (v118, unchanged from v111)

- Hire a marketing agency.
- Spend on paid ads.
- Launch a Discord before we have 1k MAU.
- Publish thought-leadership content in the abstract ("the future of AI").
- Take enterprise-deal RFPs that take more than 10 hours of somdipto's time.
- Re-brand. The brand is "Dan Lab" (or whatever somdipto confirms in week 1).
- Ship HRM-Text marketing before the audiod v1.3+HRM-Text integration lands.
- Open Telegram group allowlist before 100 paired users.
- **v118 addition:** Market Tailscale as a feature until the authkey is set.
- **v118 addition:** Market Paperclip until it ships an active agent.

---

## 9. Open Questions for somdipto (v118, with deadlines)

1. **TAILSCALE_AUTHKEY** — *blocking, this week.* Set the env var in Settings > Advanced and run `tailscale up --authkey=$TAILSCALE_AUTHKEY`.
2. **HuggingFace `danlab` org** — *blocking, this week.* Create the org, upload SmolVLM-256M + mmproj, link to danlab-multimodal. 5-minute task.
3. **danlab.dev access** — *blocking, this week.* Who owns the stack? React + Vite? Static? What is the deploy path?
4. **Brand naming** — *blocking, this week.* DanLab for research, "Dan" for consumer? Or one brand?
5. **Twitter handle availability** — *blocking, this week.* @danaboratory vs @danlab_dev vs @somdipto?
6. **HRM-Text-1B integration** — *FYI.* When audiod v1.3+HRM-Text lands, do we lead with "reasoning on the wearable" or stay quiet?
7. **Telegram pairing** — *FYI.* Keep `pairing` policy or move to `allowlist` when we have 50+ users?
8. **Press embargo** — *Q3 OKR.* What is the next real milestone we can anchor a Show HN to?
9. **EigenCloud regional launch** — *Q3 OKR.* When do Mumbai / Bengaluru regions come online? This is a marketing timing question.
10. **Microsoft Scout + OpenClaw fork/follow** (v118) — *FYI, Q3 OKR.* Recommend follow for now. Document fork triggers in architecture review.
11. **dan-lab org profile README** (v118) — *blocking, this week.* somdipto to write 5-line org profile.

*Strategy complete. v118 calendar, Twitter pack, landing copy, and README suggestions live in sibling files.*
_bot."

### Week 2 (July 10 – 16) — Architecture deep-dive + small-model series kickoff
**Theme:** "How 8 services + an OpenClaw gateway + a tailnet become one proactive agent."
- [ ] Ship the architecture PDF for dan-glasses (one-pager per layer).
- [ ] Publish the "8 daemons live" demo video on YouTube Shorts + LinkedIn.
- [ ] **v118 new:** Post the HRM-Text-1B $1,500 story as a 5-tweet thread + LinkedIn essay. This is the v118 origin pillar.
- [ ] Post technical thread: "How to build a proactive AI wearable on a $0 budget" — link the build plan.
- [ ] **Daemon-of-the-week #1: audiod.** Micro-post with the real `/ready` payload. Tease v1.1 liveness/readiness split.
- [ ] Submit Paperclip to https://news.ycombinator.com as "Show HN".

### Week 3 (July 17 – 23) — Track B (Dan Voice) drops + on-device thesis
**Theme:** "Your earbuds are now a Jarvis. No hardware purchase."
- [ ] Publish the Dan Voice landing page (Track B) at danlab.ai/dan-voice.
- [ ] Set up Lead magnet: "The India AGI Builder's Manifest" — 5-page PDF in exchange for email.
- [ ] One cold outreach to 3 SE-Asia travel-agency ops VPs about a Dan Voice pilot.
- [ ] **Daemon-of-the-week #2: perceptiond.** Micro-post with the LFM2.5-VL-450M spec. Salience-gating explainer.
- [ ] **v118 new:** Post the Gemma 3 in-orbit story as a 4-tweet thread. This is the v118 press hook.
- [ ] One tweet: "Telegram @danlab_bot is live. DM to pair. No install. No hardware. Privacy by architecture."

### Week 4 (July 24 – 30) — Track A (Dan Glasses wearable) drops + Show HN draft
**Theme:** "8/8 daemons running on a Linux laptop. Now let's put it on your face."
- [ ] Publish the Dan Glasses landing page (Track A) at danlab.ai/glasses.
- [ ] Pin the "watchful mode" demo video on the GitHub README of dan-glasses.
- [ ] **Daemon-of-the-week #3: memoryd.** Micro-post on SQLite + 384-dim vectors + episodic/semantic/procedural.
- [ ] Hot-take tweet: "Glasses at $99 make smart-glasses a daily-driver category. The math proves it."
- [ ] **v118 new:** Post the Kokoro-82M edge-TTS story as a 3-tweet thread. This is the v118 TTS arc.
- [ ] One Show HN draft: "Show HN: Dan Glasses — 8 daemons live, on-device AI, .deb install, tailnet substrate".
- [ ] Burn down the v117 punchlist — what is not done by July 30 is rolled into Q3 OKRs.

### End-of-month metrics dashboard (v118, +HF)
- danlab.dev unique visitors
- GH stars (sum of org) = ___
- **HuggingFace danlab org downloads = ___ (NEW v118)**
- New Twitter followers = ___
- @danlab_bot paired users (cumulative) = ___
- @danlab_bot DAU = ___
- Show HN rank peak = ___
- Tailscale tailnet devices (cumulative, if authkey landed) = ___

---

## 6. Brand Voice Rules (v118, sharpened)

- **Direct.** Short sentences. Active voice. Verbs before nouns.
- **Specific numbers over adjectives.** "8 of 8 daemons live" beats "highly reliable."
- **Substance over polish.** Better to ship an ugly README with real code than a slick README with no code.
- **No buzzword soup.** Banned words: "revolutionary," "game-changing," "next-gen," "AI-powered" (says who?).
- **Indian origin is the asset, not the asterisk.** "From India" is in our bio. Not "also from India."
- **Honest about limits.** "This is a heuristic, not RL. SIA fork coming." beats overclaiming.
- "Architecturally private" over "private." Always.
- Name the model. "LFM2.5-VL-450M" beats "VLM." "whisper.cpp base.en" beats "STT." "Kokoro-82M" beats "TTS." "HRM-Text-1B" beats "reasoning model."
- Pronouns and voice: first-person plural ("we"). Never "the company."
- **v118 new:** when the substrate is incomplete, name the gap. "tailscaled logged out, needs TAILSCALE_AUTHKEY" is a stronger line than "our network substrate is in progress." Receipts over roadmap.
- **v118 new:** the press hook is now the **on-device thesis**, not the wearable. The wearable is the form factor. The on-device thesis is the bet. *A 4B VLM in orbit. A 1B reasoning model trained for $1,500. An 82M TTS model beating ElevenLabs. The on-device thesis is no longer a pitch.*

---

## 7. Risks + Mitigations (v118, updated)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **danlab.dev stays stale** | **High** (no owner currently) | **High** (funnel is broken) | **P0 v118. Ask somdipto for access and stack this week.** |
| **Tailscale authkey not set** | **High** (blocked on somdipto) | **Medium** (substrate incomplete) | **P0 v118. The marketing wedge is Telegram until the tailnet lands.** |
| **HuggingFace org not created** | **Medium** (5 min action) | **High** (single highest-leverage gap) | **P0 v118. Do it this week.** |
| Quark or Meta ships parity feature | High | Medium | We win on privacy + open SDK. Lean into the architecture story. |
| Show HN is a flop | Medium | Medium | Pre-warm the post 48h earlier with the danlab-multimodal asciinema. Recruit 5 commenters. |
| somdipto becomes single-point-of-failure for shipping | High | High | Document the 8-daemon bootstrap one-liner. Recruit a part-time devops hire via the open roles channel. |
| EigenCloud pricing shock for paid tier | Medium | High | Anchor pricing to Indian mobile-phone data plans (₹399/month entry tier). |
| Open-source competitor forks Paperclip and out-executes us | Medium | Medium | Maintain a 6-month technical lead via dan-consciousness and proprietary prompts. |
| Telegram abuse / spam | Medium | Medium | Keep `pairing` DM policy. Manual approve. Group allowlist is empty by default. |
| HRM-Text-1B ship slips | Medium | Low | Do not market HRM-Text until audiod v1.3 lands. Tease in one tweet only. |
| Tailscale blocker scares the team | Low | Low | It is a sandbox constraint, not a product gap. Telegram does not need Tailscale. Document the path forward in a blog post if it becomes a narrative issue. |
| **v118 new:** Microsoft Scout wins the agent-OS war | Medium | High | Stay close to the OpenClaw community. Ship `dani` as a Solara citizen from day one. **Do not pre-position. Build the substrate first.** |
| **v118 new:** Anthropic Dreaming becomes the consumer default | Low | Medium | Dreaming is closed-source + $20/mo. Our wedge is open-weights + free + on-device. The Anthropic Mythos gating reinforces our wedge. |

---

## 8. What we will not do this quarter (v118, unchanged)

- Hire a marketing agency.
- Spend on paid ads.
- Launch a Discord before we have 1k MAU.
- Publish thought-leadership content in the abstract ("the future of AI").
- Take enterprise-deal RFPs that take more than 10 hours of somdipto's time.
- Re-brand. The brand is "Dan Lab" (or whatever somdipto confirms in week 1).
- Ship HRM-Text marketing before audiod v1.3 ships.
- Open Telegram group allowlist before 100 paired users.
- **v118 addition:** market the Tailscale tailnet before `tailscaled` is joined and `tailscale status` returns the device.
- **v118 addition:** ship Paperclip marketing before at least one Paperclip agent is active.

---

## 9. Open Questions for somdipto (v118, with deadlines)

1. **danlab.dev access** — *blocking, this week.* Who owns the stack? React + Vite? Static? What is the deploy path?
2. **Brand naming** — *blocking, this week.* DanLab for research, "Dan" for consumer? Or one brand?
3. **Twitter handle availability** — *blocking, this week.* @danaboratory vs @danlab_dev vs @somdipto?
4. **TAILSCALE_AUTHKEY** — *P0 v118, this week.* Set in Settings > Advanced, then `tailscale up --authkey=$TAILSCALE_AUTHKEY`. Closes the only remaining substrate gap.
5. **HuggingFace org creation** — *P0 v118, this week.* Who creates the `danlab` org? somdipto handle or a shared lab handle? First model card needs an uploader.
6. **HRM-Text-1B integration** — *FYI.* When audiod v1.3 ships, do we lead with "reasoning on the wearable" or stay quiet?
7. **Telegram pairing** — *FYI.* Keep `pairing` policy or move to `allowlist` when we have 50+ users?
8. **Press embargo** — *Q3 OKR.* What is the next real milestone we can anchor a Show HN to?
9. **EigenCloud regional launch** — *Q3 OKR.* When do Mumbai / Bengaluru regions come online? This is a marketing timing question.
10. **v118 NEW: Microsoft Scout follow-or-fork decision** — *Q3 OKR.* OpenClaw is our substrate. Microsoft built Scout on it. Do we follow, fork, or just be the consumer/edge answer? Recommend: follow for now, ship `dani` as a Solara citizen from day one.
11. **v118 NEW: Gemma 3 in-orbit press outreach** — *FYI.* Can we get a quote from Loft Orbital or NASA JPL for the danlab.ai blog cross-post? The story is bigger than us.

---

*Strategy complete. v118 calendar, Twitter pack, landing copy, and README suggestions live in sibling files.*
