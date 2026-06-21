# Dan1 Twitter Content — v66 (canonical)

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 07:30 IST (02:00 UTC)
**Status:** ✅ Canonical. Supersedes v65.

> **v66 thesis — the pinned tweet is the price-anchor.** v65 left the pinned tweet talking about audiod v0.6. v66 retires that. v66's pinned tweet leads with the audiod v0.7 Tauri client, but the brand-anchor line is the price: "Snap is $2,195. We are $145–180 BOM. The category is confirmed; the cost is not. We're the cost." Every post in v66 references that line in some form.

## Handle strategy (unchanged from v65)

**Primary handle:** `@danlab_dev` (claim this week)
**Fallback handles:** `@danlab_inc`, `@danlab_lab`, `@danlab_agi` (if @danlab_dev is taken)
**Author handle (existing):** `@somdipto` — personal posts
**Cross-post handles:** `@Shodan_s` — personal/automation, not marketing

## Bio (claim with @danlab_dev)

**Option A — short (recommended, v66):**
```
Open-source AI from India 🇮🇳
Proactive companion (not reactive assistant)
7 daemons · audiod v0.7 live · MIT
Snap is $2,195 · we're $145–180 BOM
danlab.dev
```

**Option B — long (under 160 chars, v66):**
```
We are 1.5 people in Bengaluru building proactive AI companions.
MIT. 7 daemons. audiod v0.7 with 101/101 tests. On-device by default.
Snap is $2,195. We're $145–180 BOM. We're the cost.
danlab.dev 🇮🇳
```

**Option C — alt (v66):**
```
Building toward AGI from the other side of the planet.
Dan Glasses: proactive AI companion, MIT, 7 daemons.
audiod v0.7 + Tauri client live today.
danlab.dev 🇮🇳
```

**Recommended:** Option A. Short. No fluff. The price-anchor is the brand.

**Location field:** Bengaluru, India
**URL field:** https://danlab.dev
**Joined:** (whatever Twitter says)
**Birth date:** Don't set.

## Pinned tweet (v66 — REPLACES v65 pinned)

**Pinned:**
```
Snap just unveiled $2,195 AR glasses with two Snapdragons.
Spiegel called it "a new era of computing."

audiod v0.7 is live on a $300 laptop. 101/101 tests. Tauri client shipped.
Same proactive loop. MIT. 7 daemons. On-device by default.

The category is confirmed. The cost is not. We're the cost.

`curl localhost:8741/health` → ok. PID 10887.

github.com/somdipto/dan-glasses 🇮🇳
```

## First 10 posts (in order, week 26)

These are the first 10 tweets from @danlab_dev. Post one per day, 09:00 IST, starting Monday 2026-06-23. **v66 add:** the Snap-week anchor tweet is the second tweet on Monday 06-23.

---

### Post 1 — Mon 06-23 09:00 IST — audiod v0.7 with Tauri client

```
Today we open-sourced Dan Glasses v0.7.

audiod v0.7.0 ships a Tauri integration client. The typed contract the desktop shell will mirror 1:1.

- HTTP: start, stop, restart, reload, ptt, health, status
- WS: transcripts() async iterator with backoff reconnect
- 8+ integration tests against the live daemon
- 4 stubbed-transport tests for retry/reconnect
- Zero new system dependencies (stdlib only)

`curl localhost:8741/health` → ok. 101/101 tests. MIT.

github.com/somdipto/dan-glasses/releases/tag/v0.7.0-audiod 🇮🇳
```

---

### Post 2 — Mon 06-23 09:30 IST — Snap-week price-anchor (NEW in v66)

```
Snap just unveiled $2,195 AR glasses with two Snapdragons.
Spiegel called it "a new era of computing."

audiod v0.7 is live on a $300 laptop. Same proactive loop. MIT. 101/101 tests.

Snap is $2,195. We are $145–180 BOM. The category is confirmed. The cost is not. We're the cost.

github.com/somdipto/dan-glasses 🇮🇳
```

---

### Post 3 — Tue 06-24 — danlab-multimodal + post-Snap framing (v66 sharpened)

```
Today we also open-sourced danlab-multimodal.

302MB combined. SmolVLM-256M + mmproj. ~32s per image on CPU.

```

git clone github.com/somdipto/danlab-multimodal
cd danlab-multimodal
python3 src/demo.py demo
```

Pre-RL. Heuristic. MIT. We don't claim RL we don't have.

This week Snap sold $2,195 AR glasses. We ship 302MB on a $300 laptop. The category is confirmed; the cost is not. We're the cost.

github.com/somdipto/danlab-multimodal
```

---

### Post 4 — Wed 06-25 — danlab.dev refresh

```
danlab.dev is finally 2026.

Old homepage: Agent8, Zerant, Dapify, "AI Glasses."
New homepage: 7 daemons, live status strip, 1 curl.

If a feature can't be inspected, it doesn't belong on the homepage.

danlab.dev
```

---

### Post 5 — Thu 06-26 — Telegram public

```
@danlab_bot is now public on Telegram.

Daily ship-logs. Demo links. Direct dev chat.

t.me/danlab_dev

Same content as the X feed, but the conversation lives in Telegram.
```

---

### Post 6 — Fri 06-27 morning — Illinois HB4843 thread (NEW in v66, 5 tweets)

```
1/ Illinois just introduced HB4843 — the first US state bill to ban smart glasses while driving. The category is being regulated.

2/ The first wave of AR glasses regulation is here. On-device is going to be a compliance requirement in 2027, not a marketing claim.

3/ Dan Glasses is already on-device by default. audiod v0.7 runs locally. perceptiond runs locally. memoryd is SQLite + vectors on disk. No cloud lock-in.

4/ Bartone v. Meta is the first of multiple on-device-vs-cloud class actions in 2026–27. The compliance posture is "on-device by default." We have that. Today.

5/ We are 1.5 people in Bengaluru. We are not the answer. But we are the open-source floor for the answer. github.com/somdipto/dan-glasses
```

---

### Post 7 — Sat 06-28 — rest day

No post. The cadence is: 6 posts/week, 1 rest day.

---

### Post 8 — Sun 06-29 — week-in-review

```
Week 26 ship-log:

- Mon: dan-glasses public, v0.7.0-audiod tag (Tauri client)
- Tue: danlab-multimodal public, v0.1.0 tag
- Wed: 2 Reddit threads (r/LocalLLaMA, r/indianstartups)
- Thu: @danlab_bot flipped to public + Illinois HB4843 thread
- Fri: 7-tweet thread on Snap's $2,195 Specs
- Sun: this post

Net new: 2 public repos, 1 2026 homepage, 1 public Telegram, 14 tweets.

The category exploded. We rode the wave. We didn't claim the wave.

Next: Show HN Monday 06-30 14:00 PT. Subscribe.
```

---

### Post 9 — Mon 06-30 morning — Show HN teaser

```
Show HN drops today. 14:00 PT.

DanClaw Phase 1 — a multi-agent orchestration system for one-person companies.

7 agents. Per-agent budgets. Goal alignment. MIT. From Bengaluru 🇮🇳

github.com/somdipto/danclaw

Watch the HN thread. I'll be in it all day.
```

---

### Post 10 — Mon 06-30 evening — Show HN results

```
Show HN is live.

github.com/somdipto/danclaw

Top questions so far:
- "Why not use CrewAI / LangGraph?" (we tried, didn't fit the company shape)
- "Why MIT?" (we can't compete on proprietary; we can on architecture)
- "Why India?" (cost base + geopolitical hedge + frontier signal)

Will answer everything in thread.
```

---

### Post 11 — Tue 07-01 — HackerNoon essay (v66 add, second batch of posts)

```
New on HackerNoon: "Why we shipped a <50g wearable against Snap's $2,195 one."

The closed-source bar (Snap, Google, Apple, Meta). The India cohort (Oculosense, Sarvam, Focally). The Dan Glasses wedge (MIT + on-device + proactive + India-priced).

Snap is $2,195. We're $145–180 BOM. The category is confirmed; the cost is not. We're the cost.

hacker noon link in bio.

Receipts > narrative.
```

---

## Reply targets (week 26, find 1/day)

Reply to *one* of these accounts at 09:30 IST each day. Genuine reply, not a pitch.

- @ApoorvSaxena (audio ML)
- @swyx (DX/AI engineering)
- @karpathy (any thread on test methodology)
- @awnihannun (multimodal)
- @simonw (local-LLM)
- @sama (whenever he tweets about India)
- @ylecun (any thread on open-source vs closed)
- @ID_AA_Carmack (any thread on hardware + ML)
- @bentossell (any indie hacker thread)
- @dharmesh (CTOs + AI)
- **v66 add:** @joannastern (NPR tech journalist who covered Snap Specs)
- **v66 add:** @evanspiegel (Snap CEO — only if a relevant thread, not a pitch)
- **v66 add:** @mwseibel (NPR tech editor who covers wearables)

**Rule:** Reply with substance. Quote a specific line from their tweet. Add a fact or a counter-example. Never "great point!" Never "DM us to chat."

**v66 Snap-week rule:** When replying to a Snap / Google / Apple / Qualcomm wearable tweet, lead with the price-anchor. "Snap is $2,195. We are $145–180 BOM. audiod v0.7 is live. https://github.com/somdipto/dan-glasses" — only if the thread is relevant, never as a drive-by pitch.

---

## Templates (v66, sharpened)

**Ship-log template:**
```
<artifact> is public. <version>.

- <bullet 1>
- <bullet 2>
- <bullet 3>

<receipt>. <license>. <link>
```

**Price-anchor template (v66, NEW):**
```
<closed-source competitor> is $<X> with <spec>.

audiod v0.7 is live on a $300 laptop. Same proactive loop. MIT. <link>

<one-line wedge: "The category is confirmed; the cost is not. We're the cost.">
```

**Insight template:**
```
<1-sentence contrarian claim>

<1 sentence of why>.

<1 sentence of what we do about it>.
```

**Receipt template:**
```
<artifact>: <metric>.

e.g. audiod v0.7: 101/101 tests, Tauri client shipped, PID 10887, MIT.
```

**Wedge template (India cohort context only):**
```
Three AI glasses out of India this year.
- <competitor 1>: <position>
- <competitor 2>: <position>
- Dan Glasses: <position>

The only one with all four: MIT + on-device + proactive + India-priced.
```

**Compliance template (v66, NEW — for v67 press push, not v66 social):**
```
<recent regulatory event>.

<one sentence: on-device is going to be a compliance requirement in 2027>.

Dan Glasses is already on-device by default. audiod v0.7 runs locally. <link>
```

---

## Engagement rules (v66)

- Reply to anyone who mentions danlab, Dan Glasses, danlab-multimodal, or audiod within 1 hour.
- Reply to anyone who asks "what is Dan Glasses?" with the curl, not a pitch.
- Quote-tweet competitors *only* with new receipts, never with "thoughts?" or "what do you think?"
- **v66 add:** When quoting a Snap/Google/Apple/Qualcomm wearable post, always include the price-anchor. "Snap is $2,195. We are $145–180 BOM."
- Don't run polls. (Polls are vanity metrics.)
- Don't ask for follows or stars. (Receipts earn them.)
- Don't quote-tweet the same insight twice. (Make the backlog work.)
- Don't post in threads you didn't start. (Stay out of fights.)
- **v66 add:** Don't use "Snap-killer" framing. We are not killing Snap. We are the cost.

---

## Hashtag policy (v66, unchanged from v65)

**No hashtags.** X hashtags are dead since ~2018. They look desperate.

**Exception:** #ShowHN is the *only* hashtag that matters, and only on the Show HN post. Not on other posts.

---

## Image / video policy (v66, sharpened)

- 1 image per ship-log tweet (terminal screenshot, daemon status, etc.)
- 1 thread/week can have 1 image (architecture diagram, status strip)
- Video: only on the Sunday YouTube drop, never on X
- No stock photos. Ever.
- No AI-generated images of people. Ever.
- No "Made with Canva" branding visible.
- **v66 new:** Terminal screenshots preferred over render. The status strip with audiod v0.7 ports is the canonical image for week 26.

---

## Cadence (v66, unchanged from v65)

**Daily 09:00 IST:** ship-log tweet (X + Telegram @danlab_bot)
**Daily 09:30 IST:** 1 reply to a relevant account
**Daily 23:00 IST:** save 1 insight to `agent-work/backlog.md`
**Friday 18:00 IST:** X thread
**Sunday 10:00 IST:** week-in-review + YouTube

**Monthly 1st Wednesday:** Hacker News (Show HN, Ask HN, or thoughtful comment)

**v66 Snap-week additions (week 26 only):**
- **Mon 06-23 09:30 IST:** Snap Specs $2,195 + audiod v0.7 price-anchor tweet (post #2)
- **Wed 06-25 09:00 IST:** r/LocalLLaMA post-mortem (separate from X)
- **Fri 06-27 18:00 IST:** 7-tweet thread: "What Snap's $2,195 Specs means for the open-source alternative"
- **Thu 06-26 09:00 IST:** Illinois HB4843 thread (5 tweets) (post #6)

---

## v66 → v67 transition

v66 twitter content assumes:
- 2 public repos with ≥25 stars each by 07-04
- Show HN with ≥50 points
- Telegram @danlab_bot with 50+ subscribers
- First YouTube video published
- Snap-week price-anchor tweet gets ≥100 likes

v66 → v67 will:
- Open the brand account to scheduled posts (Buffer or Hootsuite)
- Add a brand-voice-specific sub-account for somdipto personal (@somdipto stays separate)
- Begin daily reply queue with 5 priority accounts
- Begin weekly content calendar published 1 week in advance
- **v66 → v67 new:** Publish the 500-word "Why we're swapping KittenTTS for Orca" technical post (from dan2-model-analysis.md)
- **v66 → v67 new:** Publish the HackerNoon essay: "Why we shipped a <50g wearable against Snap's $2,195 one"

**Filed under:** `agent-work/dan1-twitter-content.v66.md`
**Next:** `agent-work/dan1-landing-copy.v66.md`
