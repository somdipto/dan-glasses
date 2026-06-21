# Dan1 Marketing Strategy — v66 (canonical)

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 07:30 IST (02:00 UTC)
**Status:** ✅ Canonical. Supersedes v65.
**Read first:** `dan1-marketing-research.md` v66.

> **v66 thesis — ride the category wave without claiming the wave.** v65 shipped the public surface and the cadence. v66 is the pass that lands in the same news cycle as Snap Specs ($2,195), Google Android XR + Warby Parker + Gemini, Qualcomm Snapdragon Reality Elite, Apple AI glasses + AirPods, and Illinois HB4843. The strategy doesn't change: three pillars, daily cadence, receipts > narrative. The timing just got louder. audiod v0.7 (Tauri client) is the new receipt. The Snap-week framing is the new timing. **We don't pretend to be Snap. We say: here is the open-source, MIT-licensed, India-priced proactive alternative. audiod v0.7 is live today.**

---

## 1. The strategic shift (v65 → v66)

| Dimension | v65 framing | v66 framing |
|---|---|---|
| Headline claim | "It's all public. Clone it." | "It's all public, and the category just exploded. The cost is the receipt." |
| Primary proof | Public GitHub + refreshed danlab.dev + Show HN in the can | + audiod v0.7 Tauri client + Snap Specs $2,195 price-anchor + on-device compliance posture |
| Audience priority | Developer-early-adopter | Same. The Snap-week news cycle reaches a new audience: the "I'm not paying $2,199 for Spiegel's new era of computing" audience. |
| Channel priority | GitHub + LinkedIn + X + Telegram + Show HN | Same. **v66 add:** Reddit r/LocalLLaMA gets a Snap-week post. HackerNoon gets a Snap-week essay. |
| Tone | Receipt-led | Receipt-led + "the category is in the news cycle; we're the cost." |
| CTA | "Star the public repo. Star the second one. Run a daemon. Drop a Show HN comment." | "While Snap ships $2,195 AR glasses with two Snapdragons, we ship audiod v0.7 on a $300 laptop. Clone it. Run it. Star it." |
| New in v66 | — | Snap-week thread. audiod v0.7 announcement. Compliance-posture file (v67). KittenTTS swap post (v67 week 1). |

**Why the shift:** The category got louder. The strategy doesn't change. The *timing* has to match the news cycle. v66 is the pass that lands the public surface in the same week as Snap Specs unveiled + Google I/O XR reveal + Qualcomm chip announcement + Apple AI AirPods report + Illinois HB4843.

---

## 2. Three pillars (do not edit, unchanged from v65)

These three messages are the only three we say, in three different orders, every week:

1. **Proactive, not reactive.** The loop runs continuously. audiod listens. perceptiond watches. memoryd remembers. We surface only when salience justifies it.
2. **On-device, MIT, modular.** Seven daemons. All MIT. All inspectable. No cloud lock-in. No black boxes.
3. **From India to the world.** Cost base + geopolitical hedge + a real frontier signal. Building toward AGI from the other side of the planet.

**Why three, not five:** Three is the number a person can remember after one read.

**Why these three:** They map to (1) the architectural wedge, (2) the integrity wedge, (3) the narrative wedge. Drop any one and the story collapses.

**v66 sharpened one sub-line under pillar 2:** "MIT + on-device + proactive + India-priced — the only one with all four. Snap is $2,195 + ad-supported + phone-tethered. Google is Warby Parker + Gemini. Apple is 14 months later. We are audiod v0.7 with 101/101 tests, MIT, today." Don't put this in the pillars. Put it in conversations and DMs.

**v66 sharpened one sub-line under pillar 1:** "While Snap Specs waits for a prompt, our audiod is already listening. The loop runs continuously. The proactive wedge is the architecture, not a feature." Use sparingly — once a week, max.

---

## 3. Audience prioritization (90-day plan, v66)

**Tier 1 — developer-early-adopter (target: 50 by 2026-09-21):**

- Channels: GitHub, X, Reddit (r/MachineLearning, r/LocalLLaMA, r/indianstartups), Hacker News (Show HN).
- Content: weekly ship-log, monthly deep dive, ad-hoc reply-to-tweets.
- Success metric: 50 stars across public repos + 100 unique clones/week + 10 external issues.
- CTA: `git clone somdipto/dan-glasses && cd dan-glasses && ./scripts/start-all.sh`
- **v66 add:** Hacker News is now a primary channel, not a tertiary one. Show HN for DanClaw Phase 1 is week 26 (06-30 14:00 PT). Show HN for audiod v0.7 is week 28.

**Tier 2 — accessibility / cognitive-load community (target: 200 by 2026-12-21):**

- Channels: HackerNoon essay, IndiaAI dispatch, YourStory, Substack.
- Content: 1 longform/month on audiod + memoryd as a "remember for me" stack.
- Success metric: 1 Tier 2 press mention + 200 mailing-list signups + 50 desktop installs.
- CTA: "Try the desktop companion. Free. MIT. Yours."
- **v66 add:** Named competition in this tier = Oculosense. Differentiation: companion-first, not visually-impaired-first.

**Tier 3 — enterprise pilots (target: 5 by 2027-03-21):**

- Channels: direct outreach, conferences (KCD India, PyCon India).
- Content: 1 case study/quarter from a Tier 1 user who crosses over.
- Success metric: 5 paid pilots with monthly retention ≥ 80%.
- CTA: "Book a 30-min call with somdipto." (NOT a sales form.)
- **v66 add — compliance posture is the v67+ Tier 3 wedge:** Illinois HB4843 + Bartone v. Meta are the first of multiple on-device-vs-cloud mandates. Pitch Tier 3 in 2027, not 2026. The architecture is already there; the regulatory pressure isn't.
- **Don't pitch Tier 3 publicly in 2026.** Enterprise pilots come from Tier 1 users crossing over. They don't come from cold outbound.

---

## 4. Channel playbook (v66)

**GitHub (PRIMARY — every Monday):**
- Release note per merged PR > 50 LOC.
- `gh release create` with `## What's Changed` + `## Verify` sections.
- Pin: audiod, perceptiond, memoryd, danclaw-phase1, danlab-multimodal.
- Repo topics: `ai-companion`, `wearable`, `on-device`, `mit-license`, `india`, `proactive-agent`.
- Every repo README must end with: `Built at danlab.dev 🇮🇳`
- **v66 priority (this week):** push 3 repos public: `somdipto/dan-glasses`, `somdipto/danlab-multimodal`, `somdipto/danclaw` (or danclaw-phase1). Tag `v0.7.0-audiod` on dan-glasses (the new audiod Tauri client).

**X / Twitter (DAILY — 09:00 IST):**
- One ship-log tweet (image or 4-line status).
- One insight tweet (1-sentence, contrarian if possible).
- One reply to a relevant account (AR/AI/multimodal/open-source).
- One thread / week (Friday 18:00 IST).
- **v66 priority:** claim @danlab_dev this week. Cross-post to @danlab_bot Telegram.
- **v66 new thread:** Snap-week post-mortem, 7 tweets, Friday 06-27 18:00 IST.

**LinkedIn (WEEKLY — Tuesday 11:00 IST):**
- Longform (400-800 words) from somdipto.
- Cross-post the weekly ship-log + 1 insight.
- Tag relevant people once / month.
- **v66 add:** Week 26 post-mortem includes the Snap-week framing. "While Snap ships $2,195 AR glasses, we ship audiod v0.7 on a $300 laptop." somdipto's voice, not Dan1's.

**Telegram (DAILY — v66 priority, carried from v65):**
- @danlab_bot is already live via OpenClaw.
- v66 action item: flip channel to public, set channel username, set pinned message to v66 pinned tweet.
- Use for: short ship-logs, demo links, direct dev chat.
- Don't use for: longform (LinkedIn is for that).

**Hacker News (v66 elevated to primary — first Wednesday of each month, then more):**
- Show HN: danclaw-phase1 in week 26 (06-30 14:00 PT).
- Show HN: audiod v0.7 (the production-tested one + the Tauri client) in week 28.
- Ask HN: "What would make a wearable AI companion trustworthy to you?" in week 30.
- **v66 new:** Comment thoughtfully on the Snap Specs HN thread if it surfaces. Don't self-promote; add substance. "audiod v0.7 is the open-source alternative: audiod v0.7, 101/101 tests, MIT, github.com/somdipto/dan-glasses." (One sentence. One link. Don't spam.)

**YouTube (BIWEEKLY — Sunday 10:00 IST):**
- 2-min demo of `audiod + perceptiond` running on a $300 laptop.
- 5-min essay: "Why we shipped a 50g wearable against Snap's 132g one."
- Asciinema-style screen recording (we already ship this for danlab-multimodal).

**arXiv / Blog (QUARTERLY — every 12 weeks):**
- One preprint from danlab-multimodal: "Pre-RL Scaffold."
- One essay on audiod/perceptiond architecture.
- **v66 new:** "Why we're swapping KittenTTS for Orca" — 500-word technical post in week 27 (from dan2's model analysis). The swap is a 10× perceived-latency win. Worth a post.

**Reddit (WEEKLY):**
- r/indianstartups: weekly update from somdipto.
- r/MachineLearning: monthly paper / preprint.
- r/LocalLLaMA: monthly danlab-multimodal update. **v66 add:** Snap-week post on r/LocalLLaMA Wednesday 06-25.
- r/singularity: one longform AMA / quarter.

**India cohort media (v66 secondary tier, unchanged from v65):**
- YourStory, Inc42, IndiaAI dispatch, MediaNama, FactorDaily.
- Hook: "AGI from India — the indie's roadmap."
- Don't pitch until we have 50 stars + 100 weekly clones.

---

## 5. Brand voice rules (v66, sharpened)

**Do:**
- Use bullet points and short sentences.
- Use code blocks in tweets when the claim is technical.
- Use tables for comparisons.
- Be specific: "101/101 tests" beats "well-tested." "PID 10887" beats "live."
- Use 🇮🇳 once per post, not five times.
- Use 👾 in the byline.
- When the receipt is curl-able, paste the curl.
- When the artifact is on GitHub, paste the link with the first 6 chars of the SHA.
- "v0.7.0-audiod" beats "the latest version." Specific tags beat vague claims.
- **v66 new:** When the competitor is named, name the price. "Snap: $2,195. Dan Glasses: $145–180 BOM." The number is the wedge.
- **v66 new:** When the category is in the news, ride it. "Snap just launched $2,195 AR glasses. We're audiod v0.7 with 101/101 tests, MIT, today." Don't trash; price-anchor.

**Don't:**
- No "revolutionary," "game-changing," "next-generation," "cutting-edge."
- No exclamation marks except in headlines.
- No stock photos. Ever.
- No "AI-powered" as a standalone adjective.
- No mention of competitors by name unless the comparison is technical and substantiated. *Exception (carried from v65):* in the India cohort context, name Oculosense + Sarvam to position the wedge. *New v66 exception:* in the Snap-week context, name Snap + Google + Qualcomm + Apple to price-anchor.
- No "DM us to partner" CTAs.
- **v66 new:** No "Snap-killer" framing. We are not killing Snap. We are the cost.
- **v66 new:** No "AGI from India" until v67. Snap-week is not the time to claim AGI.

**Tone examples (v66 sharpened):**

✅ "audiod v0.7 is live. Tauri integration client. 101/101 tests. `curl http://localhost:8741/health` → ok. PID 10887. MIT. https://github.com/somdipto/dan-glasses/releases/tag/v0.7.0-audiod"

❌ "We're thrilled to announce audiod v0.7 — our revolutionary new audio daemon that changes everything!"

✅ "302MB combined. SmolVLM-256M + mmproj. ~32s per image on CPU. MIT. `python3 src/demo.py demo`."

❌ "Our cutting-edge multimodal AI pipeline delivers unprecedented performance in an industry-leading compact form factor!"

✅ "Snap just unveiled $2,195 AR glasses with two Snapdragons. audiod v0.7 is live on a $300 laptop. Same proactive loop. MIT. The category is confirmed; the cost is not. https://github.com/somdipto/dan-glasses"

❌ "Unlike Snap's overpriced AR glasses, our solution offers a unique combination of features that sets us apart from the competition."

**v66 new tone example — the compliance posture (file for v67 press, not v66 social):**

✅ "Illinois just introduced HB4843 to ban smart glasses while driving. On-device is going to be a compliance requirement in 2027. Dan Glasses is already on-device by default. audiod v0.7 is live. https://github.com/somdipto/dan-glasses"

❌ "While other AI glasses makers struggle with privacy concerns, our platform is already privacy-first because we built it that way from day one."

---

## 6. v66 weekly cadence (carried from v65 + Snap-week additions)

**Monday 09:00 IST:** GitHub release + ship-log tweet (X + Telegram).
**Tuesday 11:00 IST:** LinkedIn longform.
**Wednesday 09:00 IST:** Reddit post (r/LocalLLaMA in week 26 — Snap-week).
**Thursday 21:00 IST:** Open office hours (Zoom, public — start when 10 public users).
**Friday 18:00 IST:** X thread (Snap-week post-mortem in week 26, 7 tweets).
**Sunday 10:00 IST:** Week-in-review LinkedIn longform + YouTube short.

**Daily 09:00 IST:** One ship-log tweet (X + Telegram @danlab_bot).
**Daily 09:30 IST:** Reply to one relevant account.
**Daily 23:00 IST:** Save 1 insight to the content backlog.

**v66 monthly anchor (last Wednesday):** Hacker News — Show HN, Ask HN, or thoughtful comment.

**v66 Snap-week additions (week 26 only):**
- **Mon 06-23 09:30 IST:** Tweet on Snap Specs $2,195 + audiod v0.7 price-anchor. (Anchor the public surface to the news cycle.)
- **Wed 06-25 09:00 IST:** r/LocalLLaMA post: "Snap's $2,195 AR glasses vs. a $300 laptop running danlab-multimodal." (See content calendar v66.)
- **Fri 06-27 18:00 IST:** 7-tweet thread: "What Snap's $2,195 Specs means for the open-source alternative." (See content calendar v66.)

---

## 7. Metrics we care about (v66, unchanged from v65)

**North star:** Weekly active clones (`gh api repos/{owner}/{repo}/traffic/clones`).
**Input 1:** GitHub stars across all public repos.
**Input 2:** X followers (post-impressions).
**Input 3:** LinkedIn post impressions.
**Input 4:** Telegram @danlab_bot subscribers.
**Input 5:** Hacker News points + comments on Show HN posts.
**Input 6:** Reddit post upvotes on r/LocalLLaMA, r/MachineLearning, r/indianstartups.

**Don't care about (yet):**
- DAU on a product we haven't shipped.
- App Store ranking (no app).
- Press mentions (until we have 100 stars).
- Waitlist signups (no waitlist — we ship).
- Telegram "channel views" (viral ≠ valuable).
- **v66 add:** Snap Specs download numbers. We don't compete with Snap on downloads. We compete on architecture.

---

## 8. v66 risks and mitigations

| Risk | Probability | Mitigation |
|---|---|---|
| Press calls us "AGI from India" and overhypes | High | "What we are NOT" block on landing page + every blog post. **v66 add:** in the Snap-week context, "AGI" framing is double-loaded — don't say it. |
| Snap-week thread turns negative on the underdog framing | Medium | Don't frame as underdog. Frame as "open-source alternative at the cost of audiod v0.7." Receipts, not narrative. |
| HN thread turns negative on the India-origin framing | Medium | Lead with the substance (audiod test count, danlab-multimodal reproducible), not the origin |
| Competitor (Oculosense, Sarvam) announces same proactive loop | Medium | We shipped audiod v0.7 first; receipts matter; we cite 101/101 tests |
| somdipto burns out doing daily tweets + Snap-week thread | Medium | Rotate with @danlab_dev handle; ship-log is templated; office hours is weekly, not daily. **v66 add:** Snap-week thread is one-time; daily cadence stays daily, not triple-daily. |
| Tier 1 enterprise pilot arrives before Tier 1 community exists | Low | Politely defer; ask them to wait for v1 desktop |
| Telegram channel goes public and gets spammed | Medium | Use invite-link-only, approve-join mode, public read-only |
| Show HN for DanClaw Phase 1 gets <50 points | Medium | Title is everything. Test 3 titles on day-job Slack first. Have a backup post ready. |
| Public repos reveal under-tested or broken daemons | High | Tag only audiod v0.7 as stable. perceptiond/memoryd as "spec'd, runnable, tests pending." Don't oversell. |
| **v66 new:** Snap Specs ships to early reviews and the press turns on them (battery, weight, $2,195) | Medium-High | We don't pile on. We price-anchor. "Snap at $2,195. audiod v0.7 at the cost of a $300 laptop." |
| **v66 new:** Illinois HB4843 passes and gets politicized | Low | We don't opine on legislation. We file the compliance angle for v67+ when we have a press list. |
| **v66 new:** Google announces an open-source Gemini-lite before our Show HN | Low | We don't compete with Gemini. We compete on the loop. Our Show HN draft doesn't mention Google. |

---

## 9. What v66 does NOT do (carried from v65 + additions)

- Does not run ads. (No budget, no team.)
- Does not pitch investors. (Bootstrapping; that's a separate track.)
- Does not publish a podcast. (No bandwidth.)
- Does not sponsor events. (No budget.)
- Does not promise hardware dates. (BOM is a target, not a date.)
- Does not ship a landing page that overstates. (v66 landing copy is honest.)
- Does not claim RL. (danlab-multimodal README already disclaims.)
- Does not claim AGI. (We are aspirational. We say so once / quarter, max.)
- Does not name competitors in the README. (The comparison table lives on the landing page and in the India-cohort press pitches, not the README.)
- **v66 new:** Does not pile on Snap. (Price-anchor; don't trash.)
- **v66 new:** Does not claim "Snap-killer." (We are the cost, not the campaign.)
- **v66 new:** Does not opine on Illinois HB4843. (File for v67+ press list.)
- **v66 new:** Does not say "AGI" in the Snap-week thread. (Snap-week is not the time.)

---

## 10. v66 → v67 transition

**v67 will be the "first 50 stars" pass.** Once audiod + danlab-multimodal together cross 50 GitHub stars, v67 will:
1. Open a public mailing list.
2. Open the waitlist for v1 desktop companion.
3. Plan the AWE 2027 application.
4. Draft a press list with somdipto's short bio.
5. Open the danlab.dev refresh to public beta (collect email).
6. Spin up a Discord/Matrix per daemon.
7. **v66 file:** "On-device compliance posture" press pitch — Illinois HB4843 + Bartone v. Meta as the lede. Targeted at Uploadvr, Road to VR, Mixed News, HackerNoon, IndiaAI dispatch, YourStory.
8. **v66 file:** "TTS swap" technical post — KittenTTS → Orca, 10× perceived latency. Targeted at HackerNoon + r/MachineLearning.

**Don't do any of those now.** v66 is "ride the category wave, ship the public surface, post daily, count clones."

---

## 11. v66 action items (this week)

1. **Push 3 public repos:** `somdipto/dan-glasses` (tag `v0.7.0-audiod`), `somdipto/danlab-multimodal` (tag `v0.1.0`), `somdipto/danclaw` (or `danclaw-phase1`, real repo at `/home/workspace/danclaw/`).
2. **Claim @danlab_dev** on X. Cross-post first 10 tweets (see v66 twitter content).
3. **Flip @danlab_bot to public** on Telegram. Set channel username. Pin v66 pinned tweet.
4. **Refresh danlab.dev** with v66 landing copy. (Push to zo.space or build a Site — confirm with somdipto.)
5. **Show HN draft for DanClaw Phase 1**, scheduled 2026-06-30 14:00 PT.
6. **First YouTube demo:** 2-min audiod + perceptiond screen cast, schedule 2026-06-29.
7. **Commit the v66 READMEs** to the public repos.
8. **Snap-week thread** for Friday 06-27 18:00 IST (drafted in v66 content calendar).
9. **Snap-week Reddit post** for r/LocalLLaMA Wednesday 06-25 (drafted in v66 content calendar).
10. **Confirm or shift** the open questions in `dan1-marketing-research.md` v66 §14.

---

**Filed under:** `agent-work/dan1-marketing-strategy.v66.md`
**Next:** `agent-work/dan1-content-calendar.v66.md`
