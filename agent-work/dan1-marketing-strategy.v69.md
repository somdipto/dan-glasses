# Dan1 Marketing Strategy v69 — First 1,000 Readers

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 11:00 IST (05:30 UTC)
**Status:** ✅ Canonical. Supersedes v68.

> **v69 thesis:** v68 shipped the inbound (landing, blog, RSS, public roadmap, 9 blog posts). v69 ships the **community** — Discord, YouTube, press, podcast, newsletter sponsorship, the 1,000-reader mark. Every Friday = a weekly dev log. Every Wednesday = a YouTube demo. Every other Tuesday = a podcast guest spot.

---

## 1. The v69 strategy in one page

**Goal (one line):** Turn 50 inbound readers (v68 target) into **200 RSS + 50 Discord + 200 YouTube + 1 press + 1 podcast** by Day 28.

**The 3 v69 moves:**

1. **Reply > broadcast.** v68 made every tweet link to a blog post. v69 makes every tweet start a conversation — replies, quote-tweets, threads that ask questions. Cadence: 2 broadcasts/day + 5 replies/day.
2. **Community > content.** v68 shipped 9 blog posts in 14 days. v69 ships 10 blog posts + 4 weekly dev logs + 4 LinkedIn essays + 2 YouTube demos + 1 podcast transcript + 1 community spotlight in 28 days. The community generates content (Discord #showcase → blog post), so Dan1 doesn't have to write it all.
3. **Distribution > creation.** v68's distribution was "post and pray." v69's distribution is **sponsored** — $300 to a focused dev newsletter, 2 podcast guest spots, India tech press first. Distribution is paid, but minimal.

**The 5 v69 anti-patterns (vs v68):**

1. **Don't ship a landing page without a Discord.** The Discord is the CTA target. v68's "Subscribe to RSS" CTA is the warm target. v69's "Join the Discord" is the hot target.
2. **Don't ship a YouTube channel with <3 videos.** First 3 videos = audiod in 90s, perceptiond in 90s, paperclip Show HN follow-up. Don't ship a channel with 1 video.
3. **Don't pitch press before the Dan Glasses Show HN.** Press reads Show HN. Show HN drives press. Don't pitch before the proof.
4. **Don't sponsor a newsletter without a landing page.** v68 already shipped the landing page. v69 sponsorships are gated on the inbound being live.
5. **Don't post to Discord more than 1×/day.** Discord punishes over-posters. The seed team (somdipto, Dan1) posts 1 message/day each. Members post organically.

---

## 2. The 7 principles of v69

1. **Reply > broadcast** — 5 replies/day, 2 broadcasts/day.
2. **Community > content** — community generates 30% of v69 content (Discord #showcase → blog posts).
3. **Distribution > creation** — paid distribution: $300 newsletter, 2 podcasts, India tech press.
4. **Cadence > polish** — every Friday = a weekly dev log. Every Wednesday = a YouTube demo. Cadence wins.
5. **Show, don't tell** — every claim has a `curl` receipt or a `dan-gateway status` line.
6. **India as origin, not gimmick** — 🇮🇳 emoji on the avatar, "from India" in every press release, the "Why India" blog post is one of the 10.
7. **MIT as commitment, not accident** — LICENSE file, badge in README, footer in every blog post. MIT is the price. The price is the position.

---

## 3. The 28-day v69 calendar (week-by-week)

| Week | Theme | Major events | Blog posts | LinkedIn essays | YouTube | Other |
|---|---|---|---|---|---|---|
| **W1 (06-23 → 06-29)** | Inbound + Ship day | Day 1: 3 repos public + landing + blog. Day 5: Snap-week post-mortem. | 5 | 1 | 0 | Show HN draft for paperclip |
| **W2 (06-30 → 07-06)** | Show HN + Discord prep | Day 8: Show HN paperclip. Day 10: audiod v0.7.1. Day 12: mid-cycle stats. | 3 | 1 | 1 (paperclip follow-up) | Stripe for paperclip paid tier |
| **W3 (07-07 → 07-13)** | Show HN: Dan Glasses + Discord launch | Day 15: Show HN Dan Glasses. Day 16: Discord launch + first office hours. Day 17: first press release. | 1 | 1 | 1 (audiod in 90s) | India tech press pitch |
| **W4 (07-14 → 07-20)** | Community + first dollar | Day 22: Discord 100 members. Day 23: first podcast goes live. Day 24: $300 newsletter sponsorship. | 1 | 1 | 0 | Paperclip paid tier launch |

**Total: 10 blog posts + 4 LinkedIn essays + 2 YouTube demos + 1 podcast in 28 days.**

---

## 4. The 5 new v69 channels — execution detail

### 4.1 Discord (NEW)

**Launch:** 2026-07-12 (Day 16, post Show HN Dan Glasses).

**Channels:**
- `#announcements` (read-only) — somdipto + Dan1 only
- `#general` — open
- `#audiod` — audiod-specific
- `#perceptiond` — perceptiond-specific
- `#memoryd` — memoryd-specific
- `#toold` — toold-specific
- `#ttsd` — ttsd-specific
- `#os-toold` — os-toold-specific
- `#zo-mcp-bridge` — zo-mcp-bridge-specific
- `#showcase` — community-contributed builds (the v69 blog fuel)
- `#help` — support
- `#press` — journalist asks (private, somdipto-curated)
- `#jobs` — hiring + collaboration

**Seed members (Day 16):**
- somdipto + Dan1 + Dan2 (the AI team)
- 30 somdipto's-network engineers
- 5 invited journalists
- 5 invited OSS peers

**Cadence:**
- somdipto: 1 message/day in #general for the first 14 days
- Dan1: 1 message/day in #announcements, replies to threads
- Members: organic

**Office hours:** every other Tuesday, 30 min, voice channel, recorded → YouTube.

### 4.2 YouTube (NEW)

**Launch:** 2026-07-05 (Day 8, post paperclip Show HN).

**Channel name:** "DanLab Build" (carried from v68 strategy doc).

**First 3 videos (gating channel launch):**
1. **"audiod in 90 seconds"** — 90-second screen-cast, `pip install dan-glasses`, `dan-gateway start`, `curl localhost:8090/health`. Voiceover.
2. **"perceptiond in 90 seconds"** — 90-second screen-cast, LFM2.5-VL-450M loading, image classification, local-only.
3. **"Show HN: paperclip — what got built in 4 hours"** — Day 8 follow-up. 5-min vlog.

**Cadence after launch:**
- 1 video/week (every Wednesday)
- 90s demos: 1/week (every Wednesday)
- Build-in-public vlog: 1/week (every Saturday)

**Monetization:** none in v69. v70: optional sponsor slot in video descriptions (after 1k subs).

### 4.3 Press outreach (NEW)

**Launch:** 2026-07-08 (Day 11, post Show HN paperclip + Dan Glasses prep).

**Tier 1 (India tech press first):**
- YourStory (yourstory.com) — pitched Day 11
- Inc42 (inc42.com) — pitched Day 11
- The Ken (the-ken.com) — pitched Day 11
- MediaNama (medianama.com) — pitched Day 11
- TechCrunch India (techcrunch.com/tag/india) — pitched Day 13

**Tier 2 (US tech press, Day 18+):**
- TechCrunch (techcrunch.com)
- The Verge (theverge.com)
- WIRED (wired.com) — Dan Ackerman is the smart-glasses editor
- UploadVR (uploadvr.com)

**Press kit (`/press`):**
- 100-word elevator pitch
- 5 things to know about audiod
- 5 things to know about Dan Glasses
- 5 things to know about paperclip
- Founder bio (somdipto)
- High-res screenshots, logos
- "Why India?" essay
- `dan-gateway status` receipts (live)

**Pitch format:**
```
Subject: DanLab — open-source proactive AI companion from India

Body:
Hi [name],

Quick pitch. DanLab is an Indian AI lab building the proactive AI companion — open-source, on-device, MIT-licensed. 7 modular daemons, audiod v0.7 shipped, paperclip shipping next. Show HN yesterday: [link]. Live demo: danlab.dev.

Best,
somdipto
```

### 4.4 Podcast guest spots (NEW)

**Launch:** Day 11 (07-08) outreach, Day 18–28 recordings.

**Target list:**
1. **Latent Space** (swyx + a16z) — 90 min, deep technical, audience: AI engineers
2. **The Pragmatic Engineer** (Gergely Orosz) — 60 min, audience: software engineers + VCs
3. **YourStory's "The Startup"** — 30 min, audience: Indian tech founders
4. **The Daily by NYT** (India desk) — 5 min, audience: mainstream
5. **Pragmatic AI** (Barkha Furman) — 30 min, audience: India AI builders

**Pitch format:**
```
Subject: somdipto from DanLab — MIT-licensed AI companion from India

Hi [host],

Quick pitch. I run DanLab, an Indian AI lab building open-source proactive AI companions. We just shipped audiod v0.7 + Show HN'd paperclip. [link] danlab.dev

Happy to come on for 30 min. I can talk about: building AGI from India, why we bet on-device, why we MIT'd everything, what the 7 daemons are.

— somdipto
```

### 4.5 Newsletter sponsorship (NEW)

**Launch:** Day 24 (07-16).

**Target:** 1 slot, $300, on a focused dev newsletter (prigozhin, Console, TLDR AI, etc.).

**Selection criteria:**
- Audience: AI engineers / open-source builders / India tech
- Subscribers: <10k (focused, not generic)
- Open rate: >30%
- Format: sponsor slot in body, not banner

**CTA in sponsorship:**
- "Read the DanLab dev log → danlab.dev/feed.xml"
- "Star on GitHub → github.com/somdipto/dan-glasses"

**Expected conversion:** 50–200 RSS subscribers per slot. Target: 200 new RSS subs in W4.

---

## 5. The carried v68 channels (executed in v69)

### 5.1 GitHub
- v68: every README gets an RSS badge, blog link, roadmap link.
- v69: every README adds a **Discord badge** (`[![Discord](https://img.shields.io/discord/...)](https://discord.gg/danlab)`).

### 5.2 X / Twitter
- v68: every tweet links to a blog post.
- v69: every tweet starts a conversation. The bio adds a **Discord link**.

### 5.3 Show HN
- v68: 1 post (paperclip 06-30).
- v69: 2 posts (paperclip 06-30 + Dan Glasses 07-07).

### 5.4 Reddit
- v68: 3 subs.
- v69: 4 subs (added r/singularity), weekly thread format.

### 5.5 HN comments
- v68: 1/day.
- v69: 1/day + reply-bait hooks (post a question that smart-glasses stories answer).

### 5.6 LinkedIn
- v68: 1 essay/week.
- v69: 1 essay/week, long-form, cross-posted to blog + Dev.to + Hashnode.

### 5.7 Dev.to / Hashnode / HackerNoon
- v68: auto-cross-post.
- v69: same + manual cross-post to HackerNoon.

### 5.8 RSS / Email newsletter
- v68: 100 RSS subs target.
- v69: 200 RSS subs target + sponsored slot.

---

## 6. The v69 conversion funnel

```
[Impression] → [Tweet / HN / Reddit / Press / Podcast]
       ↓
[Inbound] → [danlab.dev landing]
       ↓
[Hot CTA] → [Discord invite]
       ↓
[Cold CTA] → [RSS subscribe / GitHub star]
       ↓
[Community] → [Discord #showcase / GitHub PR / Show HN comment]
       ↓
[Returning reader] → [Weekly dev log / YouTube demo]
       ↓
[Brand] → [Next impression, higher trust]
```

**v69 conversion target:**
- Day 28: 5,000 impressions → 500 inbound clicks → 200 Discord joins → 50 RSS subs → 10 #showcase posts.

(These numbers are aspirational; v70 will measure actuals.)

---

## 7. The 5 v69 risks + mitigations

1. **Risk: Discord becomes a ghost town.** Mitigation: somdipto + Dan1 post 1 message/day each for the first 14 days. Office hours call on Day 16 is the first big moment.
2. **Risk: YouTube demos take too long.** Mitigation: first 2 demos are 90s raw screen-casts, not edited videos. 2 hours/demo, not 10.
3. **Risk: India tech press ignores us.** Mitigation: lead with paperclip (already shipping) + audiod v0.7 (121/121 tests), not Dan Glasses hardware (still in firmware).
4. **Risk: somdipto is the bottleneck.** Mitigation: Dan1 (the AI agent) handles 80% of v69 execution. somdipto gets **2 high-leverage asks/week** (1 LinkedIn essay + 1 podcast or press quote).
5. **Risk: Newsletter sponsorship doesn't convert.** Mitigation: pick a focused <10k-sub newsletter, not a generic 50k-sub one. $300 spent on a focused list beats $500 on a generic one.

---

## 8. What v69 will NOT do (without somdipto's sign-off)

- Push to a public GitHub repo (carried from v68).
- Refactor danlab.dev (only add, never remove).
- Submit a Show HN post.
- Send the v69 pinned tweet.
- Post the v69 blog posts.
- Create the Discord server.
- Create the YouTube channel.
- Pitch press.
- Book a podcast slot.
- Sponsor a newsletter.
- Open a Stripe account on paperclip.

---

## 9. v69 → v70 transition

**v69 trigger:** 28 days from 2026-06-21 (= 2026-07-19) OR 100 RSS + 50 Discord + 200 YouTube + 1 press + 1 podcast (whichever comes first).

**v70 surface:**
- SIA framework fork (the weights-and-harness self-improvement loop)
- First paying customer on paperclip ($49/mo or $499/yr tier)
- First dev-kit order for Dan Glasses reference hardware
- First YouTube video at >10k views
- First press pickup in a Tier-1 outlet
- First sponsor slot sold on the DanLab newsletter

**v70 thesis (preview):** "First dollar." Turn the community into revenue.

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-21 11:00 IST.*
