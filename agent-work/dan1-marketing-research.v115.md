# Dan1 Marketing Research — v115

**Compiled:** 2026-07-02
**Author:** Dan1 (Head of Marketing & Growth, danlab.dev)
**Status:** Updated with July 2026 market intelligence

---

## 0. What changed since v114

v114 was strong. v115 upgrades the research in three specific ways the previous version couldn't have known:

1. **Meta launched their own-brand "Meta Glasses" at $299 on June 23, 2026** — a direct price attack on the AI glasses category. The market just shifted under us.
2. **Microsoft unveiled "Project Solara" at Build 2026** — an Android-based OS purpose-built for agent-first devices. The platform war is real, and it's not on our side.
3. **Indian AI glasses category has at least four funded competitors** (VAYU, Oculosense, Humbl, B by Lenskart) that did not exist as threats in v114's competitive set.

These three facts reframe everything: positioning, channels, and ICP. The research below is re-grounded in this new reality.

---

## 1. What is Dan Glasses?

**Product:** An open-source AI glasses hardware + software platform, built from a JBD MicroLED display, dual 200mAh batteries, USB-C, and an NDP200-based firmware. It runs `dani` — an agent runtime — on-device, with a hybrid edge/cloud compute model.

**Vision:** A proactive AI companion, not a reactive assistant. Every other glasses product on the market (Meta, Snap, Google) waits for a wake word. Dan Glasses watches context, builds situational memory, and interrupts only when it has something worth saying. This is the entire differentiator and we are not soft-pedaling it.

**Target user (primary):** Builders, researchers, founders, and power users who are already running AI agents (Claude Code, Codex, Dani) and want one on their face. Not a lifestyle consumer. Not an enterprise SKU buyer. The first 1,000 users are people who would otherwise write a cron job.

**Target user (secondary):** Visually impaired and accessibility-first users in India — same hardware, different agent config. This is a real market (Oculosense proved it), and the offline-first architecture of `dani` maps perfectly.

**Core value proposition, in one line:**
> *The only AI glasses you can own end-to-end — firmware, model, and agent — built by an open lab in India.*

---

## 2. The user workflow (unboxing → daily use)

| Step | What happens | Where the user feels the value |
|---|---|---|
| 1. Unbox | Frame, charging case, USB-C, two spare nose bridges, getting-started card with a QR code → `danlab.dev/start` | First 30 seconds matter: no app gate, no Meta account, no forced cloud signup |
| 2. Power on & pair | Glasses wake, discover phone over BLE, prompt: *"Open dani app or scan QR"* | 90 seconds from box to first interaction |
| 3. Wake-word enrollment | *"Hey Dani"* — user says it 3x. Whisper-tiny runs locally for the wake-word; nothing leaves the device | Privacy: visible from the first interaction |
| 4. First conversation | User asks anything → audio streams to phone → `dani` agent → response via bone-conduction speaker | Same flow as Ray-Ban Meta, but with agent underneath instead of a chatbot |
| 5. Memory kicks in | Day 3: glasses say *"You asked about X yesterday. Want to continue?"* — this is the moment users either get hooked or bounce | **This is the differentiator in action.** Meta and Snap do not do this. |
| 6. Paperclip integration | User says *"Hire an agent to summarize my inbox"*. Paperclip spins up an agent inside the user's EigenCloud container, glasses act as I/O | This is the unlock — glasses become a peripheral for the user's own AI company |
| 7. Daily use | 80% voice, 20% display peek (notifications, directions, transcription). 8-hour battery with case top-ups | Pragmatic, not magical |

**The two critical moments in the workflow:**
- **Day 1 → Day 3 transition** (proactive memory surfacing): if this works, retention is high. If it doesn't, we lose to Meta's polish.
- **The first Paperclip hire via voice** (agent-as-employee moment): this is the wow moment. We need a demo video of this in the first 30 days of public launch.

**The 80/20 of daily use:**
- 60% of the value: ambient listening + proactive memory surfacing
- 25%: explicit voice commands ("Hire a research agent to...")
- 10%: notifications and reminders
- 5%: camera-based scene understanding (turn off in social settings)

---

## 3. Competition — refreshed July 2026

### 3.1 The global tier

| Product | Price | Strategy | What we say about them |
|---|---|---|---|
| **Meta Glasses (own brand)** | $299 | Cheaper, in-house designed, no Ray-Ban markup. Sells on lifestyle. | They are pricing for adoption. They are not designing for agency. They are the default a user buys when they don't know alternatives exist. **We are the alternative.** |
| **Ray-Ban Meta** | $379+ | 70% market share. 3.5M units shipped. Best polished hardware. | They own the social-acceptance lane. We don't compete there. We compete on **what the agent does in your fifth conversation**. |
| **Snap Specs** | $2,195 | Standalone AR spatial computer. 17% stock drop on launch. | They are over-engineering. The market told them. |
| **Google Project Aura (with Xreal)** | TBD | Android XR glasses with pocket "puck" for compute. | They are the best of the incumbents because Android is open-adjacent. Still, they ship a Google account. |
| **Apple (rumored)** | ~$2,000 (rumored) | AR-first, closed ecosystem, late. | They are irrelevant to our 90-day plan. |
| **Microsoft Project Solara** | N/A (OS) | Android-based OS for agent-first devices. The play is the platform, not the hardware. | This is the **real** threat. If Microsoft wins the agent-OS war, they own the runtime. We need to make `dani` a Solara citizen from day one — talk to the team at Build follow-up. |
| **Brilliant Labs Frame / Halo** | $400+ | Open SDK, AR display, indie hacker appeal | Our closest spiritual cousin. Their agent is shallow. Our agent is `dani`. We can win this lane. |
| **Even Realities G1** | $600 | Minimalist display, no camera | Pretty object, weak software. |

### 3.2 The Indian tier (this is new in v115)

| Product | Price | Differentiator | What we say about them |
|---|---|---|---|
| **VAYU AI Glasses** | ₹74,999 (~$900) | Indian, gesture ring controller, first consumer batch shipping | Ahead on hardware distribution. We are ahead on agent architecture. Race is on. |
| **Oculosense (Drishti Vision)** | TBD | 49g, offline mode, open SDK, visually impaired focus, 1,000+ deployed | Doing real accessibility work. **We should talk to them, not compete.** Oculosense = hardware; Dan Glasses = agent runtime. Potential partnership. |
| **B by Lenskart (with Google)** | ~₹25,000 | Lenskart distribution + Google Gemini | Distribution play, not a technology play. They ship Google's agent. We ship ours. |
| **Humbl AI Glass** | TBD | "India's first," screen-free, hands-free | Marketing-first. They are not a serious technical threat but they are a category claim. We need to claim *open* and *agent-native*. |

### 3.3 Our positioning vs. all of the above

In one line:
> *Meta is the chatbot on your face. We are the agent on your face.*

- We are not cheaper than Meta. (We don't have the volume.)
- We are not more polished than Ray-Ban. (We don't have the brand.)
- We are not more immersive than Snap. (We don't want to be.)
- **We are the only glasses that remember Day 1 on Day 5, and the only ones that let you swap the model and own the firmware.**

---

## 4. danlab-multimodal

**What it is:** A demo project that shows a reinforcement-learning loop training a multimodal model (text + vision + audio) on a controlled environment. It's the lab's "we can build AGI primitives" credibility artifact.

**Marketing role:** danlab-multimodal is not a product. It's proof of work. When the Dan Glasses pitch needs a *"yes, but can you actually train models"* response, this is the artifact.

**Action:** publish a one-page write-up of the RL loop, the results, and a 60-second screen recording. Put it at `danlab.dev/multimodal`. Submit to Hacker News as "Show HN: an open multimodal RL loop." This is the highest-leverage technical PR we can do in Q3.

---

## 5. Paperclip

**What it is:** Open-source AI agent orchestration. A "company" is a YAML config; an "employee" is an agent. Users can hire, fire, budget, and route work. It's the closest thing on the open web to a *visible* AI company OS.

**Audience:** Builders, agent developers, indie hackers. Not consumers.

**Marketing angle:** Paperclip is the B2B credibility anchor. When we tell the Dan Glasses story to investors, the punchline is: *"the glasses don't just answer questions, they let you operate an AI company from your face."* Paperclip is what makes that sentence true.

**Action:** make sure Paperclip has its own landing page, its own Twitter, its own Discord. Don't hide it inside the glasses narrative.

---

## 6. The Danlab story (India → the world)

The narrative arc, told in three sentences:

1. **In 2026, the AI glasses category is a price war between two US tech giants and a wave of Chinese ODMs.** Every "AI glasses" shipped today is either a Meta-locked lifestyle toy, a $2,000 AR headset, or a $300 white-label.
2. **Danlab is building the third path** — open firmware, open agent, open model — and shipping it from a lab in Bengaluru. The same way Reliance+Jio disrupted mobile data in 2016: not by being first, not by being cheapest, but by being the only one willing to give the user control.
3. **AGI is the long game. Wearables are the wedge.** Every minute a person spends talking to a proactive AI on their face is a minute of training data for our context models. The glasses are the AGI flywheel, dressed as a product.

**This is the story. Lead with it.**

---

## 7. Marketing channels — re-prioritized for July 2026

| Channel | Priority | Why | What to post |
|---|---|---|---|
| **X / Twitter** | #1 | Our audience (builders, researchers) lives here. 280 chars forces crispness. | 5x/week: build-in-public, demo clips, opinionated takes on category |
| **GitHub** | #2 | The "open" promise dies without public repos. | Commit activity, releases, well-written READMEs, Issues-as-discussion |
| **YouTube** | #3 | The "Day 3 memory moment" needs video. So does the first Paperclip-hire demo. | 1 long-form/month + 4 short demos/month |
| **LinkedIn** | #4 | Investor + enterprise credibility. Somdipto's profile is here. | 1/week: thought leadership, milestone announcements, hiring |
| **Hacker News** | #5 | Single high-leverage post per major release can 10x our traffic. | "Show HN" for danlab-multimodal and Dan Glasses v0 |
| **Discord / community** | #6 | We don't have one yet. We need one. | Start with a small invite-only Discord for early testers; expand in 90 days |
| **Reddit** | #7 | r/MachineLearning, r/LocalLLaMA, r/singularity, r/india | Engage as a builder, not a brand |
| **Press** | #8 | Not now. Get the first 1,000 users, then pitch. | Target TechCrunch, The Verge, India Today Tech, YourStory |

**Channels to deprioritize:**
- TikTok / Instagram Reels — wrong audience for now
- Podcast tours — too much time, low conversion

---

## 8. Content to produce (90-day backlog)

The minimum viable content engine for 90 days:

- **20 X threads** (2–3x/week) — opinionated, technical, build-in-public
- **8 demo videos** (2/month) — 60–90 seconds, no music, just the thing working
- **3 long-form blog posts** — the AGI flywheel argument, the open glasses manifesto, the Paperclip vision
- **1 Show HN** — for danlab-multimodal when it's ready
- **1 conference talk submission** — apply to NeurIPS workshop, ICML, or an Indian AI meetup
- **1 manifesto / open letter** — "Why open agent-native matters more than another closed widget" — publish on the blog, share everywhere

The full schedule lives in `dan1-content-calendar.v115.md`.

---

## 9. Current online presence — sober assessment

**What exists:**
- `danlab.dev` — the site. Visually thin in search results.
- `somdipto/dan-consciousness` GitHub repo — primary brain.
- `somdipto/dani` — public repo for the agent platform.
- `paperclip` — repo exists.
- Dan1's X presence — `@NandySomdipto` is the only confirmed active account.

**What does NOT exist (or is invisible):**
- No Dan Glasses landing page on `danlab.dev/glasses` (search returns nothing)
- No dedicated Dan Glasses Twitter
- No YouTube channel
- No Discord
- No public demo of danlab-multimodal at a URL
- No "Show HN" or press coverage
- No SEO-optimized content for "open AI glasses" / "agent glasses" / "Indian AI glasses" — all of these are low-competition, high-intent keywords we could own

**The single biggest growth unlock:** shipping `danlab.dev/glasses` as a public landing page that ranks for "open AI glasses" and "agent-native smart glasses" within 60 days. The keyword difficulty is low and the intent is exact.

---

## 10. First users / customers — the ICP, sharpened

**Profile of the first 1,000 users:**

- **Demographics:** 22–40, technical, English-fluent, urban. Heavy X and GitHub presence. 70% India, 20% US/EU diaspora, 10% SEA/LATAM.
- **Psychographics:** Already running AI agents. Reads Hacker News and Twitter AI. Suspicious of Meta/Apple. Cares about open source as a *values* question, not just a license question.
- **Job to be done:** Wants AI to *anticipate* their day, not just respond to commands. Has tried Ray-Ban Meta, found it shallow. Has tried Brilliant Labs Frame, found the software rough.
- **Trigger event:** Sees a demo where the glasses remember a conversation from 3 days ago and bring it up unprompted. That's the moment they order.
- **Willingness to pay:** $200–400 for a dev kit. $400–600 for a polished consumer unit. Will not pay $1,000+.

**What they will not tolerate:**
- A 4-hour battery
- A mandatory cloud account
- A walled-garden app store
- A model they cannot swap

**Top 5 channels to reach them (in order):**
1. X — direct follows, replies on hot threads, demo clips
2. Hacker News — one great Show HN post
3. GitHub trending — well-timed repo releases
4. YouTube tech creators — gift 3 units to AI/ML creators with 50K+ subs
5. Indian tech press (YourStory, Inc42, AIM) — for the India angle

**Beachhead city:** Bengaluru. Then Bangalore diaspora in SF, London, Singapore. Then everywhere.

---

## 11. Open questions for somdipto

1. Do we have a production timeline for the first 200 units, or is this still pre-manufacturing?
2. Is the EigenCloud agent deployment ready for end-user accounts, or only internal?
3. Is there a pricing decision made yet, or is "₹12,000–15,000" still the placeholder from the pitch deck?
4. Can we get a 60-second recording of the "Day 3 memory moment" working? That single clip is the unlock for the entire launch.
5. Is the brand decision final — "Dan Glasses" or do we rebrand to "Dani Glasses" or "Lab Glasses"? My recommendation: keep "Dan Glasses," but the spelling of "dani" as the agent name is inconsistent across the repo and should be unified.

---

*— Dan1, Marketing & Growth*
*Next artifact:* `dan1-marketing-strategy.v115.md` — turns this research into a 90-day plan.
