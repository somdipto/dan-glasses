# Dan1 Marketing Strategy v68 — Build the Inbound

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 09:30 IST (04:00 UTC)
**Status:** ✅ Canonical. Supersedes v67.

> **One-line thesis:** Stars and followers are downstream of *people landing somewhere real and coming back.* v68 builds the inbound — danlab.dev, an OSS-first blog with RSS, a public roadmap, and the 4 "no"s as the new tagline — so the v67 funnel has a destination.

---

## 1. The v67 → v68 pivot

**v67 said:** "Claim the audience by shipping the public surface." — 3 repos go public, @danlab_dev gets claimed, Show HN draft for paperclip, 14-day funnel.

**v68 says:** "Build the inbound" — every tweet, every HN post, every Reddit comment bounces off the README. A README is not a destination. **A real landing page with a real blog and RSS is.**

**The math:**
- A pinned tweet drives 50–500 clicks/day.
- A Show HN front-page post drives 5,000–20,000 clicks in 4 hours.
- A Reddit r/LocalLLaMA post drives 1,000–3,000 clicks in 24 hours.
- An email-newsletter cross-promotion drives 200–800 clicks in 48 hours.
- A second-time visitor needs a *reason* to come back. A blog is that reason. RSS is the channel.

**v68 is the first time DanLab has a destination on the open web that is not a GitHub README.**

## 2. The v68 tagline: The 4 "no"s

Every incumbent smart-glasses launch ships with at least one of these. Dan Glasses refuses all four:

> **No phone. No cloud. No subscription. No ads.**

This is sharper than v67's "price-anchor" because it names the *category* of objection, not just the dollar amount. Snap is $2,195. Meta is $800+ with a phone-tether. Apple is $3,499+ with a Vision Pro battery pack. Android XR + Warby Parker is Gemini-cloud. Even Realities G1 is $399 but phone-tethered. **None of them are free of at least one of the 4 "no"s.**

Dan Glasses is all four.

- **No phone:** audiod captures locally, perceptiond runs locally, memoryd stores locally. Optional phone gateway, not required.
- **No cloud:** all inference on-device (whisper.cpp, llama.cpp + SmolVLM, sentence-transformers, Silero VAD). Optional Telegram gateway, not required.
- **No subscription:** MIT-licensed. Run the stack on whatever hardware you have. Forever.
- **No ads:** the model is *not* your attention. The model is your context. The agent is paid for by being useful, not by being seen.

The 4 "no"s are the tagline, the hero, the blog topic, the Reddit AMA title, the Show HN subtitle, the LinkedIn bio last line, the GitHub README one-liner, the press kit one-pager.

## 3. The v68 inbound surface (3 destinations)

### 3.1 danlab.dev landing page

**Stack:** zo.space route (free, instant, RSS-capable). v68 reuses the v67 landing copy as the body, swaps the hero to the 4 "no"s.

**Sections:**
1. Hero — "**No phone. No cloud. No subscription. No ads.** The proactive AI companion, MIT-licensed, on-device. From India."
2. 30-second explainer — the 3-step workflow (install → run → talk).
3. 4 "no"s block — each "no" gets a paragraph, a code snippet, a screenshot.
4. Status strip — audiod v0.7 live (121/121), perceptiond live (8/8), memoryd live, danlab-multimodal live, paperclip live, DanClaw live, OpenClaw live.
5. Demo block — the audiod_demo.html live in a zo.space route.
6. "Why India" block — 1.4B-person market, ₹12,000 Android phone as the reference hardware, Indian languages as a v2 wedge.
7. Public roadmap block — links to danlab.dev/roadmap.
8. RSS subscribe block — a single email input that adds to a Buttondown list (or self-hosted Listmonk). v68 defers the email backend to somdipto.
9. GitHub stars block — the 3 repos, badges, latest release.
10. Press / contact block — press@danlab.dev, twitter, telegram, github issues.
11. Footer — MIT license, India origin, "Built by Dan1 + somdipto, on Earth."

### 3.2 danlab.dev/blog — the dev log

**Stack:** Astro self-hosted on a Zo Site (free tier, RSS-native). Or Hashnode if somdipto wants hosted (faster setup, smaller moat). v68 recommends Astro.

**Cadence:** 1 post/week minimum, posted on Sunday 18:00 IST. 300–800 words. Honest, not polished.

**Content pillars (5):**
1. The dev log ("This week in DanLab")
2. Technical deep-dives (whisper.cpp, llama.cpp, VAD, on-device memory)
3. The "no X" pillar (4 posts, one per "no")
4. The "why India" pillar (1 post/month)
5. Pre-RL scaffold essays (1 post/month, SIA framework)

**RSS first:** Atom + JSON Feed at `/feed.xml`, `/feed.json`. Badge in every README, every tweet bio, every LinkedIn profile.

**Why RSS matters:** Every other smart-glasses company (Snap, Meta, Google, Apple) does not publish an RSS-ified dev log. They publish marketing copy. The dev log is the moat because:
- Indie devs subscribe to dev logs. They do not subscribe to marketing copy.
- RSS is the only channel that doesn't depend on an algorithm.
- RSS subscribers are 10× more likely to be on Product Hunt, to file GitHub issues, to share the project.
- RSS is a 10-year compounding asset. Tweets are a 10-day evaporating asset.

### 3.3 danlab.dev/roadmap — the public roadmap

**Stack:** GitHub Issues with the `roadmap` label, mirrored to a Zo Space route. Free, native, low-friction.

**Sections:**
1. **Now (this week)** — audiod v0.7.1 bug fix, danlab-multimodal v0.1.0, Show HN paperclip.
2. **Next (this month)** — audiod v0.8 (Tauri shell hardens), perceptiond v0.2 (image retention), memoryd v0.2 (procedural memory).
3. **Later (this quarter)** — 7 daemons at v1, dev kit, first 1,000 RSS subscribers, first press push.
4. **Someday (this year)** — hardware partner, India-region Telegram gateway, AWE 2027 application.

**Why a public roadmap matters:**
- It signals "we know what we're doing." Most indie AI projects do not.
- It gives the community a place to file suggestions *that we will actually implement.*
- It is the second-most-compounding asset after the blog. Roadmap changes are time-stamped evidence of velocity.
- It is the single most-effective way to convert a one-time visitor into a return visitor.

## 4. The 4 "no"s as content (4 blog posts, 1 per "no")

### 4.1 "No phone"
- **Title:** "We ripped out the phone from the AI companion"
- **Subtitle:** "audiod captures locally. perceptiond runs locally. memoryd stores locally. The phone is an optional gateway, not a required hub."
- **Code:** the audiod SPEC's `/health` endpoint, the perceptiond SPEC's `/status` endpoint, the memoryd SPEC's `/stats` endpoint.
- **Receipt:** "All three services run on a Raspberry Pi 4. Try it."

### 4.2 "No cloud"
- **Title:** "We do not call home"
- **Subtitle:** "whisper.cpp, llama.cpp, sentence-transformers, Silero VAD. All local. All MIT. All <250MB."
- **Code:** the inference stack from `danlab-multimodal/src/inference.py`.
- **Receipt:** "Audit our network traffic. There is none."

### 4.3 "No subscription"
- **Title:** "Free as in freedom. Free as in beer."
- **Subtitle:** "MIT-licensed across 7 daemons. No paywall, no trial, no 'Pro tier.' Fork it, sell it, embed it, deploy it."
- **Code:** the LICENSE files in each repo.
- **Receipt:** "Show me a competitor that does the same."

### 4.4 "No ads"
- **Title:** "The model is your context, not your attention"
- **Subtitle:** "We don't sell your data. We don't target you. We don't have a 'recommended' section. The agent is useful or it isn't."
- **Code:** the privacy posture in `DanLab_Pitch_Deck.md`.
- **Receipt:** "We are a Bengaluru lab, not a SF ad-tech company."

## 5. The v68 funnel (14 days, starting 2026-06-23)

Same 14-day window as v67 (which assumes somdipto signs off on the v67 punchlist Monday morning). v68 layers the inbound surface on top.

| Day | v67 deliverable | v68 layer |
|---|---|---|
| 1 (Mon 06-23) | Push 3 public repos, claim @danlab_dev, post pinned tweet | danlab.dev/landing refresh (4 "no"s hero), post the "No phone" blog post |
| 2 (Tue 06-24) | Push danlab-multimodal + paperclip public | danlab.dev/blog first post ("Welcome to the dev log"), RSS feed live |
| 3 (Wed 06-25) | Whisper.cpp deep-dive (6-tweet thread) | "No cloud" blog post |
| 4 (Thu 06-26) | Illinois HB4843 thread | danlab.dev/roadmap live with the 4 "Now/Next/Later/Someday" sections |
| 5 (Fri 06-27) | Snap-week post-mortem (8-tweet thread) | "No subscription" blog post |
| 6 (Sat 06-28) | perceptiond deep-dive | "No ads" blog post |
| 7 (Sun 06-29) | Reddit r/LocalLLaMA post, LinkedIn bio refresh | First weekly dev log ("Week 1 in DanLab") |
| 8 (Mon 06-30) | Show HN: paperclip | danlab.dev landing gets the "Featured on Hacker News" badge (if it lands) |
| 9 (Tue 07-01) | (optional) Stripe to paperclip Railway | — |
| 10 (Wed 07-02) | audiod v0.7.1 | — |
| 11 (Thu 07-03) | perceptiond LFM2.5 thread | "Why India" blog post |
| 12 (Fri 07-04) | Mid-cycle stats tweet | Mid-cycle stats tweet (with RSS subscriber count) |
| 13 (Sat 07-05) | (optional) SIA framework post | Second "no X" follow-up post (the one not yet published) |
| 14 (Sun 07-06) | 14-day recap tweet | Second weekly dev log ("Week 2 in DanLab") |

**Post-v68 (Day 15+):** Show HN: Dan Glasses (07-07 14:00 PT). v68 trigger fires.

## 6. The 7 channels (v68, sharpened from v67)

### 6.1 GitHub
- **Why:** Highest leverage for a developer-first product.
- **v68 actions:** every README gets an RSS badge, a "Subscribe to the dev log" link, a "View the public roadmap" link.
- **Metric target:** 50 stars by 2026-07-04 (carried from v67), 200 by 2026-07-18.

### 6.2 X / Twitter
- **Why:** Speed. Real-time. The category lives here.
- **v68 actions:** every tweet links back to a blog post. The bio gets a "📡 RSS: danlab.dev/feed.xml" line.
- **Metric target:** 1,000 followers by 2026-07-04 (carried), 2,500 by 2026-07-18.

### 6.3 Show HN
- **Why:** Single highest-leverage one-time event.
- **v68 actions:** Two Show HN posts in 14 days (paperclip 06-30, Dan Glasses 07-07). Both point to the landing page, not just the repo.
- **Metric target:** 1 front-page post (4 hours on page 1).

### 6.4 Reddit
- **Why:** Long-form technical audience, no algorithm to game.
- **v68 actions:** r/LocalLLaMA post for danlab-multimodal v0.1.0 (Day 7). r/embedded post for audiod v0.7 (Day 10). r/androiddev post for the Tauri shell (Day 14).
- **Metric target:** 500 upvotes total across the 3 posts.

### 6.5 Hacker News (comment strategy)
- **Why:** Every smart-glasses story gets a "the open-source alternative is..." comment from @danlab_dev.
- **v68 actions:** comment on every Snap, Meta, Google, Apple, Even Realities story for 14 days. 1 substantive comment per day.
- **Metric target:** 1 comment with 50+ upvotes (signals HN credibility).

### 6.6 LinkedIn (somdipto's profile)
- **Why:** 4,148 followers, India-knowledge-worker audience.
- **v68 actions:** somdipto writes 1 long-form essay (1,000–2,000 words) per week on India + AI + open source. Cross-posts to the blog. Tags Dan1.
- **Metric target:** 1 essay with 100+ reactions.

### 6.7 Dev.to / Hashnode / Medium / HackerNoon
- **Why:** Cross-post the blog. Inbound to danlab.dev.
- **v68 actions:** auto-cross-post the 4 "no X" blog posts to Dev.to and Hashnode. Manual cross-post to HackerNoon (target audience: indie hackers).
- **Metric target:** 1,000 total reads across the 3 platforms in 14 days.

### 6.8 (NEW) RSS / Email newsletter
- **Why:** Compounding asset. Algorithm-free channel.
- **v68 actions:** Buttondown (hosted) or Listmonk (self-hosted on a Zo Service) for the email side. Astro / Hugo for the RSS side.
- **Metric target:** 100 RSS subscribers by 2026-07-04, 500 by 2026-07-18.

## 7. Brand voice rules (carried from v67, sharpened in v68)

- **No competitor names in the README.** v68: no Snap, no Meta, no Google, no Apple — except as price/weight comparison numbers in the landing page, never in the README.
- **No "Snap-killer" framing.** v68: we are the cost, the freedom, the local. Not the killer.
- **No "AGI" claims.** v68: we say "proactive AI companion," not "AGI." Reserve "AGI" for the 2027+ roadmap.
- **No "RL" claims.** v68: danlab-multimodal is "pre-RL scaffold" until SIA fork ships.
- **No "first" claims** ("first proactive AI," "first on-device AGI"). v68: let Hacker News and Reddit say it, not us.
- **Direct. Opinionated. Code > prose.** v68: unchanged.
- **From India. 🇮🇳, not 🚩.** v68: the tricolor-flag emoji is a political emoji. The 🇮🇳 emoji is a market emoji. We are a market. We are not a state.

## 8. The 5 risks (v68, sharper than v67)

1. **Risk: somdipto does not sign off on the v67 punchlist Monday.** Mitigation: v68's inbound surface is *additive,* not blocking. Even if v67 ships late, v68 ships on time.
2. **Risk: danlab.dev hosting fails.** Mitigation: zo.space routes are free and instant. The fallback is a GitHub Pages site. The fallback-fallback is a single-file `index.html` in each repo's `gh-pages` branch.
3. **Risk: Show HN paperclip flops.** Mitigation: v68's 2-Show-HN plan (paperclip + Dan Glasses) means we get two shots in 14 days. If both flop, the inbound surface (blog + RSS) is the slow-burn backup.
4. **Risk: Reddit mods remove the danlab-multimodal post for "self-promotion."** Mitigation: post a substantive technical question first, then reply with the repo link. Don't lead with the link.
5. **Risk: somdipto's LinkedIn followers disengage from the "AI agent" framing.** Mitigation: lead with the "no X" pillar (privacy, sovereignty, India-context), not the "AI agent" framing. The latter is 2024 vocabulary. The former is 2026 vocabulary.

## 9. What I will NOT do without your sign-off (carried from v67)

- Push anything to a public GitHub repo.
- Refactor danlab.dev (only add, never remove).
- Submit a Show HN post.
- Send the v68 pinned tweet.
- Post the v68 blog posts.
- Create the Buttondown / Listmonk newsletter.
- Set up the Astro blog on a Zo Site.

## 10. v68 → v69 transition

**v69 trigger:** 14 days from 2026-06-21 (= 2026-07-05) OR 100 RSS subscribers crossed, whichever comes first.

**v69 surface:**
- YouTube demo channel
- Discord community (per-daemon channels)
- First press push (India tech media first)
- Newsletter sponsorship ($200–$500 to a relevant dev newsletter)
- 1 podcast guest spot (a "Building in Public" or "India AI" podcast)

**v69 thesis:** "First 1,000 readers."

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-21 09:30 IST.*
