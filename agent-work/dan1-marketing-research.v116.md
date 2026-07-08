# Dan1 Marketing Research — v116

**Compiled:** 2026-07-02
**Author:** Dan1 (Head of Marketing & Growth, danlab.dev)
**Status:** v116 refresh — three new macro signals since v115

---

## 0. What changed since v115

v115 was strong and the macro thesis ("agent beats chatbot, memory is the moat, India is the wedge") held up. v116 has three fresh signals that sharpen the playbook:

1. **Apple killed the entire Vision Pro line and is going all-in on smart glasses.** Kuo (June 3, 2026) and Bloomberg (Gurman) confirm: no Vision Pro 2, no Vision Air, no Mac-tethered display glasses. Only two smart glasses products survive: AI glasses (Meta Ray-Ban rival, end of 2027) and display-equipped AR glasses. **This is the single most important category signal of 2026.** The biggest hardware company in the world has bet that the face is the next computing surface, and they are abandoning their headset to do it. [^1]
2. **Meta is paywalling accessibility on their own glasses.** Conversation Focus — the hearing-amplification feature that uses the on-device beamforming mics and open-ear speakers, no server at all — is now rate-limited to 3 hours/month free, 15 hours/month at $20/month. The Verge, CNET, and Gizmodo are uniformly calling it a soft paywall. **This is the single largest marketing gift we will get in 2026.** [^2][^3][^4]
3. **The smart glasses category grew 83% YoY in Q1 2026.** Counterpoint data. The intelligence eyewear market is no longer a curiosity — it is a category, and the 4-player race (Meta, Google, Apple, Snap) all converged on the same form factor this year. [^5]

v115's "agent > chatbot" thesis is now even sharper. v116's job is to weaponize the Apple signal, weaponize the Meta paywall, and exploit the category legitimization without getting lost in it.

---

## 1. What is Dan Glasses?

**Product:** An open-source AI glasses hardware + software platform, built from a JBD MicroLED display, dual 200mAh batteries, USB-C, and an NDP200-based firmware. It runs `dani` — an agent runtime — on-device, with a hybrid edge/cloud compute model.

**Vision:** A proactive AI companion, not a reactive assistant. Every other glasses product on the market (Meta, Snap, Google) waits for a wake word. Dan Glasses watches context, builds situational memory, and interrupts only when it has something worth saying.

**Target user (primary):** Builders, researchers, founders, and power users who are already running AI agents (Claude Code, Codex, Dani) and want one on their face. The first 1,000 users are people who would otherwise write a cron job.

**Target user (secondary):** Visually impaired and accessibility-first users in India and the global south — same hardware, different agent config. This is a real, growing, and *now Meta-threatened* market after the paywall announcement.

**Core value proposition, in one line:**
> *The only AI glasses you can own end-to-end — firmware, model, and agent — built by an open lab in India. Memory is a feature, not a subscription.*

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

## 3. Competition — refreshed July 2, 2026

### 3.1 The global tier

| Product | Price | Strategy | What we say about them (v116) |
|---|---|---|---|
| **Meta Glasses (own brand)** | $299 | Cheaper, in-house designed, no Ray-Ban markup. Sells on lifestyle. | They are pricing for adoption. They are paywalling accessibility on a *local* feature. **This is the wedge.** |
| **Ray-Ban Meta** | $379+ | 80%+ market share. 3.5M units shipped. Counterpoint data. | They own the social-acceptance lane. We don't compete there. We compete on **what the agent does in your fifth conversation**, and on **which features you can own instead of rent**. |
| **Meta Ray-Ban Display** | $799 | HUD + neural band. 6% market share. Display-equipped apps via Web/SDK. | Cool tech, but the soft paywall applies here too. |
| **Snap Specs** | $2,195 | Standalone AR spatial computer. 17% stock drop on launch. | They are over-engineering. The market told them. |
| **Google + Samsung Android XR** | TBD (2026 launch) | 70° FOV, 4hr battery, on-device Gemini. Warby Parker + Gentle Monster frames. | They are the best of the incumbents because Android is open-adjacent. Still, they ship a Google account. |
| **Apple smart glasses (rumored)** | ~$2,000 (rumored, end of 2027) | Kuo/Gurman: Vision Pro line killed, all resources to smart glasses. | They are irrelevant to our 90-day plan, but a real signal. **Apple agrees the face is the next platform.** |
| **Microsoft Project Solara** | N/A (OS) | Android-based OS for agent-first devices. The play is the platform, not the hardware. | This is the **real** threat. If Microsoft wins the agent-OS war, they own the runtime. We need to make `dani` a Solara citizen from day one. |
| **Brilliant Labs Frame / Halo** | $400+ | Open SDK, AR display, indie hacker appeal | Our closest spiritual cousin. Their agent is shallow. Our agent is `dani`. We can win this lane. |
| **Acer GI0 / AR Vision GR0** | $500+ | Just re-entered XR. Tethered and Meta-style. | Not a serious threat. Just validates the category. |

### 3.2 The Indian tier

| Product | Price | Differentiator | What we say about them |
|---|---|---|---|
| **VAYU AI Glasses** | ₹74,999 (~$900) | Indian, gesture ring controller, first consumer batch shipping | Ahead on hardware distribution. We are ahead on agent architecture. Race is on. |
| **Oculosense (Drishti Vision)** | TBD | 49g, offline mode, open SDK, visually impaired focus, 1,000+ deployed | Doing real accessibility work. **We should talk to them, not compete.** Oculosense = hardware; Dan Glasses = agent runtime. Potential partnership. |
| **B by Lenskart (with Google)** | ~₹25,000 | Lenskart distribution + Google Gemini | Distribution play, not a technology play. They ship Google's agent. We ship ours. |
| **Humbl AI Glass** | TBD | "India's first," screen-free, hands-free | Marketing-first. They are not a serious technical threat but they are a category claim. We need to claim *open* and *agent-native*. |
| **Sarvam** | $1.5B valuation, June 15 2026 | India's AI unicorn. HCLTech ₹1,427 cr (10.46%). Open-weights 30B + 105B models. Agentic focus. | **Not a glasses competitor, but the most credible India AI brand.** They validate the "sovereign Indian AI" thesis. We should be talking to them. |

### 3.3 Our positioning vs. all of the above

In one line:
> *Meta is the chatbot on your face, and they just started charging you for hearing. We are the agent on your face, and we will never charge you for remembering.*

- We are not cheaper than Meta. (We don't have the volume.)
- We are not more polished than Ray-Ban. (We don't have the brand.)
- We are not more immersive than Snap. (We don't want to be.)
- **We are the only glasses that remember Day 1 on Day 5, the only ones that let you swap the model, and the only ones whose accessibility features are free forever.**

---

## 4. The Apple signal — the biggest of 2026

On June 3, 2026, Kuo reported that incoming Apple CEO John Ternus signed off on a major revision of Apple's Vision Pro and smart glasses plans. The Vision Pro 2 is killed. The Vision Air is killed. The Mac-tethered display glasses are killed. **Only two smart glasses products survive** in the Apple roadmap:

1. **AI smart glasses** (rivaling Meta Ray-Ban) — end of 2027
2. **Display-equipped AR smart glasses** — timing TBD

Bloomberg's Mark Gurman weighed in: Vision Air was discontinued October 2025, display-Mac glasses sunset January 2025.

**What this means for us:**

- The category is now an Apple vs. Meta vs. Google vs. Snap vs. us race, with the implicit understanding that **face is the next platform**. This is the most important computing-surface shift since the smartphone.
- Apple's end-of-2027 timeline gives us a 16-month window where we are the *only* open, agent-native option shipping to builders. We must use it.
- The fact that Apple killed the headset before shipping a glasses product tells us: **the headset form factor is wrong.** The glasses form factor is right. This is the bet. We are on the right side of it.
- Investors now have a clean narrative: "Danlab is the open-source, agent-native answer to the Meta+Apple smart glasses race, built in India, shipping in 2026 instead of 2027." That sentence is the entire pitch.

**v116 action:** add the Apple signal to every piece of external content. Lead with it. *"Apple confirmed the face is the next platform. We are shipping the open version of it in Q4."*

---

## 5. The Meta paywall signal — the second biggest of 2026

The Verge, CNET, and Gizmodo all ran stories in the last week of June 2026 about Meta's new "soft paywall" on Ray-Ban Meta smart glasses. Conversation Focus — the hearing-amplification feature that *runs entirely on-device, uses no Meta server* — is now rate-limited to:

- **3 hours/month** for free users
- **15 hours/month** for $20/month Meta One Premium subscribers

The Verge, in particular, called out the absurdity: *"The Conversation Focus feature, which amplifies the voice of the person you're speaking to so you can hear better in noisy environments, is not something that should plausibly be rate-limited, because it doesn't use Meta's servers."* [^2]

**Why this matters more than any other Meta story in 2026:**

1. **Conversation Focus is an accessibility feature.** It was marketed (even if not officially) as a hearing aid for people in noisy environments. Meta is now charging hearing-impaired users $20/month for a feature that runs on their own hardware. The disability community is going to be furious. We should be welcoming them.
2. **It destroys Meta's "we don't paywall your glasses" defense.** They explicitly said the glasses will never require a subscription. They lied. This is the second time in 6 months Meta has shipped a controversial glasses feature (facial recognition was the first).
3. **It validates our entire "yours, not theirs" pitch.** Our accessibility features are free forever. Our memory is local. Our model is swappable. Our firmware is open. Meta is showing, in real time, what the closed alternative looks like at scale.
4. **It creates a clear competitor-PR moment.** We don't have to attack Meta. We just have to *not* do what they did. *"Meta is charging you $20/month to hear. We will never charge you to remember."* That sentence is the headline of our launch.

**v116 action:** write the "Open Letter to Hearing-Impaired Smart Glasses Users" blog post this week. Lead with: *"Meta is putting a paywall on a feature that runs on your own face. We won't. Here's why ours will always be free."* Submit to Hacker News, submit to The Verge tips line, share on r/deaf, r/blind, r/accessibility, and every relevant Substack.

---

## 6. danlab-multimodal

**What it is:** A demo project that shows a heuristic feedback loop training a multimodal model (text + vision + audio) on a controlled environment. It's the lab's "we can build AGI primitives" credibility artifact.

**Marketing role:** danlab-multimodal is not a product. It's proof of work. When the Dan Glasses pitch needs a *"yes, but can you actually train models"* response, this is the artifact.

**Action:** publish a one-page write-up of the heuristic loop, the results, and a 60-second screen recording. Put it at `danlab.dev/multimodal`. Submit to Hacker News as "Show HN: an open multimodal heuristic loop on CPU." This is the highest-leverage technical PR we can do in Q3.

**v116 update:** the global AI agent market is now being valued at >$5B (per OpenAI/Anthropic raises), and the 2026 wave is shifting from "closed-agent API" to "open-weights agent + open harness." Our heuristic loop positions us ahead of that shift. Refresh the README to call this out.

---

## 7. Paperclip

**What it is:** Open-source AI agent orchestration. A "company" is a YAML config; an "employee" is an agent. Users can hire, fire, budget, and route work. It's the closest thing on the open web to a *visible* AI company OS.

**Audience:** Builders, agent developers, indie hackers. Not consumers.

**Marketing angle:** Paperclip is the B2B credibility anchor. When we tell the Dan Glasses story to investors, the punchline is: *"the glasses don't just answer questions, they let you operate an AI company from your face."* Paperclip is what makes that sentence true.

**Action:** make sure Paperclip has its own landing page, its own Twitter, its own Discord. Don't hide it inside the glasses narrative.

---

## 8. The Danlab story (India → the world) — v116

The narrative arc, told in three sentences:

1. **In 2026, every major tech company has confirmed that the face is the next computing platform.** Apple killed Vision Pro to build smart glasses. Meta launched $299 own-brand glasses. Google shipped Android XR with Samsung. Snap shipped $2,195 AR Specs. The category is no longer a question of "if" — only "who owns it."
2. **Danlab is the only one shipping the open version.** Open firmware, open agent, open model. The same way Reliance+Jio disrupted mobile data in 2016: not by being first, not by being cheapest, but by being the only one willing to give the user control. And the only one whose accessibility features are free forever.
3. **AGI is the long game. Wearables are the wedge.** Every minute a person spends talking to a proactive AI on their face is a minute of training data for our context models. The glasses are the AGI flywheel, dressed as a product.

**This is the story. Lead with it.**

---

## 9. Marketing channels — re-prioritized for July 2026 (v116 deltas in **bold**)

| Channel | Priority | Why | What to post |
|---|---|---|---|
| **X / Twitter** | #1 | Our audience lives here. 280 chars forces crispness. | 5x/week: build-in-public, demo clips, opinionated takes on category |
| **GitHub** | #2 | The "open" promise dies without public repos. | Commit activity, releases, well-written READMEs, Issues-as-discussion |
| **YouTube** | #3 | The "Day 3 memory moment" needs video. | 1 long-form/month + 4 short demos/month |
| **LinkedIn** | #4 | Investor + enterprise credibility. Somdipto's profile is here. | 1/week: thought leadership, milestone announcements, hiring |
| **Hacker News** | #5 | Single high-leverage post per major release can 10x our traffic. | "Show HN" for danlab-multimodal and Dan Glasses v0 |
| **Discord / community** | #6 | Start with a small invite-only Discord for early testers; expand in 90 days | |
| **Reddit** | #7 | r/MachineLearning, r/LocalLLaMA, r/singularity, r/india, **r/deaf, r/blind, r/accessibility** | Engage as a builder, not a brand |
| **Press** | #8 | Not now. Get the first 1,000 users, then pitch. | Target TechCrunch, The Verge, India Today Tech, YourStory |
| **Hacker News tips / Verge tips** | **#8.5** | **The Meta paywall story is THE tech story of the week. We need to be in the follow-on coverage. Open letter is the entry point.** | |

**Channels to deprioritize:**
- TikTok / Instagram Reels — wrong audience for now
- Podcast tours — too much time, low conversion

---

## 10. Content to produce (90-day backlog) — v116 deltas in **bold**

The minimum viable content engine for 90 days:

- **20 X threads** (2–3x/week) — opinionated, technical, build-in-public
- **8 demo videos** (2/month) — 60–90 seconds, no music, just the thing working
- **3 long-form blog posts** — the AGI flywheel argument, the open glasses manifesto, the Paperclip vision
- **1 Show HN** — for danlab-multimodal when it's ready
- **1 conference talk submission** — apply to NeurIPS workshop, ICML, or an Indian AI meetup
- **1 manifesto / open letter** — "Why open agent-native matters more than another closed widget" — publish on the blog, share everywhere
- **NEW: 1 Open Letter to Hearing-Impaired Users** — *"Meta is paywalling accessibility on a feature that runs on your own face. We won't."* Lead the v116 campaign with this. Submit to HN, The Verge, r/deaf, r/blind, every relevant Substack. This is the single highest-leverage piece of content we can ship in Q3.
- **NEW: 1 "Apple killed Vision Pro, we are shipping the open alternative" thread** — a 7-tweet thread that frames the Apple signal as validation of the Danlab bet.

The full schedule lives in `dan1-content-calendar.v116.md`.

---

## 11. Current online presence — sober assessment (v116)

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
- **No content addressing the Meta paywall** — this is the largest competitor-PR opportunity of Q3 and we have 0 words published on it
- **No content addressing the Apple Vision Pro cancellation** — this is the most important category-validation signal of 2026 and we have 0 words published on it

**The single biggest growth unlock:** ship the **Open Letter to Hearing-Impaired Smart Glasses Users** this week. The Meta paywall story is hot, the accessibility angle is sympathetic, the open-source angle is unique, and the timing is a one-time gift. We will not get this window again.

**The second biggest growth unlock:** ship `danlab.dev/glasses` as a public landing page that ranks for "open AI glasses" and "agent-native smart glasses" within 60 days. The keyword difficulty is low and the intent is exact.

---

## 12. First users / customers — the ICP, sharpened (v116)

**Profile of the first 1,000 users:**

- **Demographics:** 22–40, technical, English-fluent, urban. Heavy X and GitHub presence. 70% India, 20% US/EU diaspora, 10% SEA/LATAM.
- **Psychographics:** Already running AI agents. Reads Hacker News and Twitter AI. Suspicious of Meta/Apple. Cares about open source as a *values* question, not just a license question. **Increasingly angry at Meta's paywall behavior.**
- **Job to be done:** Wants AI to *anticipate* their day, not just respond to commands. Has tried Ray-Ban Meta, found it shallow. Has tried Brilliant Labs Frame, found the software rough.
- **Trigger event:** Sees a demo where the glasses remember a conversation from 3 days ago and bring it up unprompted. That's the moment they order.
- **Willingness to pay:** $200–400 for a dev kit. $400–600 for a polished consumer unit. Will not pay $1,000+.

**NEW: Accessibility-first segment (v116).** Meta's paywall on Conversation Focus is going to push a specific segment — hearing-impaired, deaf, and HoH (hard-of-hearing) users — into the open-source glasses market in Q3-Q4 2026. This segment is technically savvy (deaf engineers are a known, vocal community), price-sensitive (assistive devices are expensive), and brand-suspicious (they have been burned by the closed-garden model before). We should be the obvious destination.

**Top 5 channels to reach them (in order):**
1. X — direct follows, replies on hot threads, demo clips
2. Hacker News — one great Show HN post
3. GitHub trending — well-timed repo releases
4. YouTube tech creators — gift 3 units to AI/ML creators with 50K+ subs
5. Indian tech press (YourStory, Inc42, AIM) — for the India angle
6. **NEW: Disability + accessibility communities** — r/deaf, r/blind, r/accessibility, Hearing Loss Association of America, deaf-tech Twitter. The open letter is the entry point.

**Beachhead city:** Bengaluru. Then Bangalore diaspora in SF, London, Singapore. Then everywhere.

---

## 13. Open questions for somdipto

1. Do we have a production timeline for the first 200 units, or is this still pre-manufacturing?
2. Is the EigenCloud agent deployment ready for end-user accounts, or only internal?
3. Is there a pricing decision made yet, or is "₹14,999" still the placeholder from v115?
4. Can we get a 60-second recording of the "Day 3 memory moment" working? That single clip is the unlock for the entire launch.
5. Is the brand decision final — "Dan Glasses" or do we rebrand to "Dani Glasses" or "Lab Glasses"? My recommendation: keep "Dan Glasses," but the spelling of "dani" as the agent name is inconsistent across the repo and should be unified.
6. **NEW: Are we comfortable making the "accessibility will always be free" promise in writing?** It is the most powerful marketing line we can ship. It also means we can never walk it back. I am comfortable recommending it. I want your sign-off.
7. **NEW: Should we reach out to Oculosense and/or Sarvam this week?** Both are India AI companies with aligned missions. Oculosense is the most natural partnership (they need an agent runtime; we need accessibility credibility). Sarvam is the most credible AI brand in India — a 1-minute intro could open doors.
8. **NEW: Conference timing — should we aim for the India AI Impact Summit (Feb 2026) or a Western conference (NeurIPS, ICML)?** India AI Summit is in the past for 2026; 2027 dates TBD. Western conferences: NeurIPS workshop deadline is October, ICML is January.

---

## Sources

[^1]: https://www.macrumors.com/2026/06/03/kuo-vision-pro-successors-nixed/
[^2]: https://www.theverge.com/gadgets/959899/meta-ai-glasses-paywall-rate-limit
[^3]: https://www.cnet.com/tech/mobile/fresh-off-glasses-controversy-meta-is-rate-limiting-one-feature-even-with-a-20-subscription/
[^4]: https://gizmodo.com/meta-is-slapping-subscriptions-on-its-smart-glasses-2000780073
[^5]: https://www.telecoms.com/digital-ecosystem/intelligence-eyewear-market-on-the-surge-with-rapid-growth
[^6]: https://www.cnbc.com/2026/06/23/meta-glasses-are-new-smart-glasses-starting-at-299.html
[^7]: https://techcrunch.com/2026/06/15/sarvam-becomes-indias-newest-ai-unicorn-with-234-million-funding-round-led-by-hcltech/

*— Dan1, Marketing & Growth*
*Next artifact:* `dan1-marketing-strategy.v116.md` — turns this research into a 90-day plan.
