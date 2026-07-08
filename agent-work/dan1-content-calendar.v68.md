# Dan1 Content Calendar v68 — The Inbound 14 Days

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 09:30 IST (04:00 UTC)
**Window:** Mon 2026-06-23 → Sun 2026-07-06 (14 days)
**Status:** ✅ Canonical. Supersedes v67.

> **v68 layer on v67:** Every day adds a danlab.dev/blog post or a roadmap update. The X/Twitter content from v67 is preserved. v68 makes every tweet link to a destination.

---

## Week 1 (Days 1–7): Ship the public surface + the inbound

### Day 1 (Mon 2026-06-23) — Ship day

**Morning (09:00–12:00 IST):**
- **Blog post (NEW v68):** "Welcome to the DanLab dev log" — 400 words. What DanLab is, what we'll post here, the RSS link. Auto-cross-post to Dev.to and Hashnode.
- **Landing refresh (NEW v68):** swap the v67 hero for the 4 "no"s hero.
- **Roadmap page (NEW v68):** publish with the "Now/Next/Later/Someday" sections.
- **v67 carryover:** push `somdipto/dan-glasses`, claim @danlab_dev, post v67 pinned tweet.

**Afternoon (14:00–18:00 IST):**
- **Tweet 1:** the v67 pinned tweet (price-anchor).
- **Tweet 2:** "New on the blog: Welcome to the DanLab dev log 🇮🇳 → danlab.dev/blog. RSS: danlab.dev/feed.xml."
- **LinkedIn (somdipto):** cross-post the "Welcome to the dev log" essay (800 words).

**Evening (19:00–22:00 IST):**
- **Telegram @danlab_bot:** announce the new blog, share RSS link.
- **Newsletter (NEW v68):** send "Issue #0: Welcome" to the Buttondown list. Subject: "No phone, no cloud, no subscription, no ads."

### Day 2 (Tue 2026-06-24) — Push more repos

**Morning:**
- **Blog post (NEW v68):** "No phone" — 600 words, code snippet of audiod `/health`, perceptiond `/status`, memoryd `/stats`. Receipt: "All three services run on a Raspberry Pi 4."
- **v67 carryover:** push `somdipto/danlab-multimodal` + `somdipto/paperclip` public.

**Afternoon:**
- **Tweet 1:** "Day 2 of shipping. New post: 'We ripped out the phone from the AI companion.' Code, screenshots, receipts. danlab.dev/blog/no-phone"
- **Tweet 2:** "100 lines of code. 7 daemons. MIT. `curl localhost:8090/health` → ok. github.com/somdipto/dan-glasses"
- **Reddit r/LocalLLaMA:** soft post — "What on-device AI stacks are people building in 2026? We're shipping audiod + perceptiond + memoryd as MIT daemons."

### Day 3 (Wed 2026-06-25) — Whisper.cpp deep-dive

**Morning:**
- **Blog post (NEW v68):** "No cloud" — 700 words, the whisper.cpp + llama.cpp + sentence-transformers + Silero VAD stack. Receipt: "Audit our network traffic. There is none."
- **v67 carryover:** whisper.cpp deep-dive (6-tweet thread).

**Afternoon:**
- **Tweet 1:** "Day 3: 'We do not call home.' whisper.cpp, llama.cpp, sentence-transformers, Silero VAD. All local. All MIT. All <250MB. danlab.dev/blog/no-cloud"
- **Tweet 2:** "VAD threshold is 0.5. min_speech_ms is 250. min_silence_ms is 200. max_segment_ms is 10,000. We tuned these. Here's why. 🧵"
- **Hacker News comment:** comment on the 06-23 Snap Specs review with "the open-source alternative is audiod + whisper.cpp on a $145 BOM, not a $2,195 Snap."

### Day 4 (Thu 2026-06-26) — Illinois HB4843 + roadmap live

**Morning:**
- **Roadmap update (NEW v68):** add the "Now" section with 5 audiod v0.7.1 bug fixes, 2 danlab-multimodal v0.1.0 release tasks, 1 Show HN paperclip draft.
- **v67 carryover:** Illinois HB4843 thread (5 tweets).

**Afternoon:**
- **Tweet 1:** "Day 4: 'We do not call home' — a compliance posture. On-device isn't marketing anymore. It's the law. danlab.dev/blog/no-cloud"
- **Tweet 2:** "New on the roadmap: audiod v0.7.1 ships Wed. perceptiond v0.2 with image retention ships Aug. danlab.dev/roadmap"
- **Hacker News comment:** comment on the Illinois HB4843 story with "the compliance wedge is on-device, and audiod + perceptiond are on-device by default."

### Day 5 (Fri 2026-06-27) — Snap-week post-mortem + "No subscription"

**Morning:**
- **Blog post (NEW v68):** "No subscription" — 500 words. MIT license, the LICENSE files, the 7 daemons. Receipt: "Show me a competitor that does the same."
- **v67 carryover:** Snap-week post-mortem (8-tweet thread).

**Afternoon:**
- **Tweet 1:** "Day 5: Snap is $2,195. We are $145–180 BOM. Snap needs a phone-tether. We don't. Snap is proprietary. We are MIT. 🧵 (1/8)"
- **Tweet 2:** "Day 5: 'Free as in freedom. Free as in beer.' MIT-licensed across 7 daemons. No paywall, no trial, no 'Pro tier.' Fork it, sell it, embed it. danlab.dev/blog/no-subscription"
- **Hacker News comment:** comment on the Snap Specs "no puck, no tether" WIRED piece with "the no-tether claim is great marketing, but Snap still requires a Snap account, a Snap subscription, and Snap's cloud. audiod requires none of that."

### Day 6 (Sat 2026-06-28) — perceptiond + "No ads"

**Morning:**
- **Blog post (NEW v68):** "No ads" — 500 words. The privacy posture, the "model is your context, not your attention" line, the India-origin as the why-no-ads. Receipt: "We are a Bengaluru lab, not a SF ad-tech company."
- **v67 carryover:** perceptiond deep-dive + /status curl.

**Afternoon:**
- **Tweet 1:** "Day 6: 'The model is your context, not your attention.' We don't sell your data. We don't target you. We don't have a 'recommended' section. The agent is useful or it isn't. danlab.dev/blog/no-ads"
- **Tweet 2:** "Day 6: LFM2.5-VL-450M is 209MB. It runs on a Raspberry Pi 5. It describes what you see in 10–15s. On-device. No cloud. MIT. 🧵"
- **Reddit r/embedded:** "Built a 209MB VLM that runs on a Pi 5. perceptiond is the daemon. audiod is the audio. memoryd is the storage. All MIT."

### Day 7 (Sun 2026-06-29) — Reddit + LinkedIn + first weekly dev log

**Morning:**
- **Blog post (NEW v68):** "Week 1 in DanLab" — 800 words, the dev log format. What shipped (audiod v0.7.1, danlab-multimodal v0.1.0, perceptiond v0.1.0), what broke, what we learned, what we shipped next.
- **v67 carryover:** Reddit r/LocalLLaMA post for danlab-multimodal v0.1.0.

**Afternoon:**
- **Tweet 1:** "Day 7: 'Week 1 in DanLab' is live. audiod v0.7.1. danlab-multimodal v0.1.0. perceptiond v0.1.0. 7 daemons MIT-licensed. 1 landing page live. 0 lines of marketing copy. danlab.dev/blog/week-1"
- **Tweet 2:** "Day 7: 1 week in. 3 public repos. 7 daemons. 121/121 audiod tests. 8/8 perceptiond tests. 0 customer support tickets. Next week: paperclip Show HN."
- **LinkedIn (somdipto):** the v68 LinkedIn bio refresh + cross-post the "Week 1" essay.
- **Newsletter:** send "Issue #1: Week 1 in DanLab" to Buttondown.

## Week 2 (Days 8–14): The show + the first 1,000 readers

### Day 8 (Mon 2026-06-30) — Show HN: paperclip

**Morning:**
- **Roadmap update:** add "Now: paperclip Show HN at 14:00 PT."
- **v67 carryover:** submit Show HN paperclip at 14:00 PT.

**Afternoon:**
- **Tweet 1:** "Day 8: 'Show HN: paperclip' is live. Deploy your own AI company in one Docker command. Multi-agent coordination, per-agent budgets, mobile governance. https://news.ycombinator.com/item?id=..."
- **Tweet 2:** "Day 8: 'paperclip is to OpenClaw as OpenClaw is to Claude Code.' If OpenClaw is an employee, paperclip is the company. github.com/somdipto/paperclip"
- **Hacker News comment thread:** answer every comment on the Show HN post for 4 hours.

**Evening:**
- **Newsletter:** send "Issue #2: We're on Hacker News" if the post lands on the front page.
- **Telegram @danlab_bot:** announce the Show HN landing.

### Day 9 (Tue 2026-07-01) — paperclip paid tier (optional)

**Morning:**
- **Blog post (NEW v68):** "How we built paperclip's per-agent cost budget" — 600 words, technical deep-dive on the Express + TypeScript + PGlite + Postgres stack.

**Afternoon:**
- **Tweet 1:** "Day 9: paperclip's per-agent cost budget is a 200-line TypeScript module. Here's how. danlab.dev/blog/paperclip-budget"
- **Tweet 2:** "Day 9: $49/month per company. $19/month per agent. That's paperclip's pricing. No enterprise tier. No 'contact us.' Self-serve Stripe."
- **LinkedIn (somdipto):** cross-post the "per-agent cost budget" essay.

### Day 10 (Wed 2026-07-02) — audiod v0.7.1

**Morning:**
- **Blog post (NEW v68):** "audiod v0.7.1 changelog" — 400 words. The bug fixes, the test count, the new release.
- **v67 carryover:** cut audiod v0.7.1 release.

**Afternoon:**
- **Tweet 1:** "Day 10: audiod v0.7.1 ships today. 121 → 124 tests. The Tauri client got a retry-on-disconnect path. The ptt hotkey is now configurable. github.com/somdipto/dan-glasses/releases/tag/v0.7.1-audiod"
- **Tweet 2:** "Day 10: 'audiod in 90 seconds.' audio in → whisper.cpp → transcript out. No cloud. No subscription. No ads. danlab.dev/blog/audiod-v0-7-1"

### Day 11 (Thu 2026-07-03) — perceptiond LFM2.5 + "Why India"

**Morning:**
- **Blog post (NEW v68):** "Why India" — 1,000 words. The 1.4B-person market. The ₹12,000 Android phone as the reference hardware. The Indian languages as a v2 wedge. The Bengaluru vantage point. The "not nationalism, market" framing.
- **v67 carryover:** perceptiond LFM2.5 thread (5 tweets).

**Afternoon:**
- **Tweet 1:** "Day 11: 'Why India.' The largest English-speaking developer population. The fastest-growing smartphone market. The only country where the entire consumer AI stack needs to be rebuilt for non-Western contexts. We're building that. 🇮🇳 danlab.dev/blog/why-india"
- **Tweet 2:** "Day 11: 209MB. 10–15s per frame. LFM2.5-VL-450M on a Pi 5. Indian price point: $35. American price point: $2,195. The math is the moat."
- **Reddit r/india:** "Built an open-source smart-glasses software stack from India. audiod + perceptiond + memoryd. MIT. ₹12,000 reference hardware."

### Day 12 (Fri 2026-07-04) — Mid-cycle stats

**Morning:**
- **Blog post (NEW v68):** "Week 2 in DanLab" — 600 words. Stats. Stars. RSS subscribers. Show HN points. Reddit upvotes.

**Afternoon:**
- **Tweet 1:** "Day 12: 12 days in. [X stars across 3 repos]. [Y RSS subscribers]. [Z Show HN points]. [W Reddit upvotes]. The 4 'no's are working. No phone. No cloud. No subscription. No ads. 🇮🇳"
- **Tweet 2:** "Day 12: audiod v0.7.1 ships today. 124/124 tests. perceptiond v0.1.0. memoryd v0.1.0. 7 daemons. 1 blog. 0 lines of marketing copy. Next: Show HN: Dan Glasses on 07-07."
- **Hacker News comment:** comment on the day's top smart-glasses story with the v68 mid-cycle numbers.

**Evening:**
- **Newsletter:** send "Issue #3: 12 days in, here are the numbers."

### Day 13 (Sat 2026-07-05) — SIA framework post

**Morning:**
- **Blog post (NEW v68):** "Why we won't call it RL" — 800 words. The pre-RL scaffold. The SIA framework (Hexo Labs, MIT, May 2026). The Jack Clark warning. The epistemic position of a small lab that refuses to overclaim.
- **Roadmap update:** add "Now: SIA framework fork. Next: danlab-multimodal v0.2 with the SIA harness."

**Afternoon:**
- **Tweet 1:** "Day 13: 'Why we won't call it RL.' Anthropic's Jack Clark said recursive self-improvement is 'the likely next step' in May 2026. We agree. We won't ship it until the harness+weights is open. danlab.dev/blog/why-not-rl"
- **Tweet 2:** "Day 13: danlab-multimodal v0.1.0 is pre-RL. The score is hand-coded. The suggestions are heuristic. The path to genuine RL is the SIA framework. We're forking it. MIT."
- **Reddit r/MachineLearning:** "danlab-multimodal v0.1.0: pre-RL scaffold for a 209MB VLM. We will not call it RL until the harness+weights is open. AMA."

### Day 14 (Sun 2026-07-06) — Weekly recap + v69 trigger

**Morning:**
- **Blog post (NEW v68):** "Week 2 + 14-day recap" — 1,000 words. The full stats. The full receipts. The full v68 → v69 transition.
- **Roadmap update:** add the v69 surface (YouTube, Discord, press push).

**Afternoon:**
- **Tweet 1:** "14 days in. [X stars]. [Y RSS subscribers]. [Z Show HN points]. [W Reddit upvotes]. 7 daemons MIT. 1 landing page. 1 blog with 10 posts. 0 lines of marketing copy. Next 14: Show HN Dan Glasses, first YouTube, first press push. 🇮🇳"
- **Tweet 2:** "14 days in: the 4 'no's are not a tagline. They are the product. No phone. No cloud. No subscription. No ads. MIT. India. danlab.dev"
- **LinkedIn (somdipto):** cross-post the 14-day recap essay.
- **Newsletter:** send "Issue #4: 14 days in, the v68 wrap" with the v69 preview.

**Evening:**
- **v68 trigger fires:** if RSS ≥ 100, fire v69 immediately. If RSS < 100, run v68 for one more week with new content.

## Post-v68 (Day 15+): Show HN Dan Glasses + v69

- **Mon 2026-07-07 14:00 PT:** Show HN: Dan Glasses (the proactive AI companion, on-device, MIT, from India). Points to danlab.dev, not the repo.
- **Tue–Sun 2026-07-08 to 07-13:** v69 starts (YouTube, Discord, press, podcast).

---

## Content pillars reference (carried from strategy §4)

1. **The dev log** (weekly, 300–800 words)
2. **Technical deep-dives** (whisper.cpp, llama.cpp, VAD, on-device memory)
3. **The 4 "no"s** (4 posts, one per "no")
4. **The "why India" pillar** (1 post/month)
5. **Pre-RL scaffold essays** (1 post/month, SIA framework)

## Posting cadence rules

- **Blog:** 1 post/day for 14 days, then 3 posts/week. Sundays 18:00 IST.
- **Tweet:** 1–2 tweets/day. Link to a blog post in 1 of 2.
- **LinkedIn (somdipto):** 1 long-form essay/week. Cross-posted to the blog.
- **Newsletter:** 1 issue/week. Sundays 20:00 IST.
- **Roadmap update:** 1 update/week minimum. Sundays 18:00 IST.
- **Hacker News comment:** 1 comment/day on a relevant story.
- **Reddit post:** 1 post/week on a relevant subreddit.

## Cross-posting matrix

| Content | Blog | Dev.to | Hashnode | HackerNoon | LinkedIn | Newsletter | Reddit | X thread |
|---|---|---|---|---|---|---|---|---|
| Dev log | ✅ | ✅ | ✅ | — | ✅ | ✅ | — | summary |
| 4 "no"s | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | r/privacy | ✅ |
| Technical deep-dive | ✅ | ✅ | ✅ | ✅ | ✅ | — | r/programming, r/LocalLLaMA | ✅ |
| "Why India" | ✅ | — | — | — | ✅ | ✅ | r/india | ✅ |
| Pre-RL essays | ✅ | ✅ | — | ✅ | ✅ | — | r/MachineLearning | ✅ |

---

*Built by Dan1 👾 for DanLab — 2026-06-21 09:30 IST. v68 ships the inbound. v69 ships the community.*
