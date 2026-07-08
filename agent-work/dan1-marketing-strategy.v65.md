# Dan1 Marketing Strategy — v65 (canonical)

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 06:30 IST (01:00 UTC)
**Status:** ✅ Canonical. Supersedes v64.
**Read first:** `dan1-marketing-research.md` v65.

> **v65 thesis — ship the public surface, then keep shipping.** v64 framed the receipts as the brand. v65 *publishes* the surface that proves them: danlab.dev gets a 2026 homepage, dan-glasses gets a real public README, danlab-multimodal gets a release tag, and the Show HN for DanClaw is in the can. After that, the strategy is the same: weekly cadence, daily ship-logs, three pillars, no filler.

---

## 1. The strategic shift (v64 → v65)

| Dimension | v64 framing | v65 framing |
|---|---|---|
| Headline claim | "audiod v0.6 is live. Curl it." | "It's all public. Clone it." |
| Primary proof | audiod v0.6 + Tauri shell + OpenClaw | + public GitHub + refreshed danlab.dev + Show HN in the can |
| Audience priority | Developer-early-adopter | Same. With Sarvam/Oculosense in the market, we sharpen to "MIT + on-device + proactive" |
| Channel priority | GitHub + LinkedIn + X + Telegram | + Show HN (DanClaw Phase 1) + public repo discovery |
| Tone | Receipt-led | Receipt-led + "ship the receipts in a way that survives first contact" |
| CTA | "Clone the repo. Run the daemon. Tell us what broke." | "Star the public repo. Star the second one. Run a daemon. Drop a Show HN comment." |
| New in v65 | — | Claim @danlab_dev. Flip @danlab_bot to public. Push 3 repos public. Refresh danlab.dev. |

**Why the shift:** v64 made the receipts visible *internally*. v65 makes them visible *externally*. Everything else is detail.

---

## 2. Three pillars (do not edit)

These three messages are the only three we say, in three different orders, every week:

1. **Proactive, not reactive.** The loop runs continuously. audiod listens. perceptiond watches. memoryd remembers. We surface only when salience justifies it.
2. **On-device, MIT, modular.** Seven daemons. All MIT. All inspectable. No cloud lock-in. No black boxes.
3. **From India to the world.** Cost base + geopolitical hedge + a real frontier signal. Building toward AGI from the other side of the planet.

**Why three, not five:** Three is the number a person can remember after one read.

**Why these three:** They map to (1) the architectural wedge, (2) the integrity wedge, (3) the narrative wedge. Drop any one and the story collapses.

**v65 sharpened one message:** Against the new India cohort (Oculosense, Sarvam), we add a fourth sub-line under pillar 2: "MIT + on-device + proactive + India-priced — the only one with all four." Don't put this in the pillars. Put it in conversations and DMs.

---

## 3. Audience prioritization (90-day plan)

**Tier 1 — developer-early-adopter (target: 50 by 2026-09-21):**

- Channels: GitHub, X, Reddit (r/MachineLearning, r/LocalLLaMA, r/indianstartups), Hacker News (Show HN).
- Content: weekly ship-log, monthly deep dive, ad-hoc reply-to-tweets.
- Success metric: 50 stars across public repos + 100 unique clones/week + 10 external issues.
- CTA: `git clone somdipto/dan-glasses && cd dan-glasses && ./scripts/start-all.sh`
- **v65 add:** Hacker News is now a primary channel, not a tertiary one. Show HN for DanClaw Phase 1 is week 26 (06-30 14:00 PT). Show HN for audiod v0.6 is week 28.

**Tier 2 — accessibility / cognitive-load community (target: 200 by 2026-12-21):**

- Channels: HackerNoon essay, IndiaAI dispatch, YourStory, Substack.
- Content: 1 longform/month on audiod + memoryd as a "remember for me" stack.
- Success metric: 1 Tier 2 press mention + 200 mailing-list signups + 50 desktop installs.
- CTA: "Try the desktop companion. Free. MIT. Yours."
- **v65 add:** Named competition in this tier = Oculosense. Differentiation: companion-first, not visually-impaired-first.

**Tier 3 — enterprise pilots (target: 5 by 2027-03-21):**

- Channels: direct outreach, conferences (KCD India, PyCon India).
- Content: 1 case study/quarter from a Tier 1 user who crosses over.
- Success metric: 5 paid pilots with monthly retention ≥ 80%.
- CTA: "Book a 30-min call with somdipto." (NOT a sales form.)
- **Don't pitch Tier 3 publicly.** Enterprise pilots come from Tier 1 users crossing over. They don't come from cold outbound.

---

## 4. Channel playbook (v65)

**GitHub (PRIMARY — every Monday):**
- Release note per merged PR > 50 LOC.
- `gh release create` with `## What's Changed` + `## Verify` sections.
- Pin: audiod, perceptiond, memoryd, danclaw-phase1, danlab-multimodal.
- Repo topics: `ai-companion`, `wearable`, `on-device`, `mit-license`, `india`, `proactive-agent`.
- Every repo README must end with: `Built at danlab.dev 🇮🇳`
- **v65 priority (this week):** push 3 repos public: `somdipto/dan-glasses`, `somdipto/danlab-multimodal`, `somdipto/danclaw` (or danclaw-phase1).

**X / Twitter (DAILY — 09:00 IST):**
- One ship-log tweet (image or 4-line status).
- One insight tweet (1-sentence, contrarian if possible).
- One reply to a relevant account (AR/AI/multimodal/open-source).
- One thread / week (Friday 18:00 IST).
- **v65 priority:** claim @danlab_dev this week. Cross-post to @danlab_bot Telegram.

**LinkedIn (WEEKLY — Tuesday 11:00 IST):**
- Longform (400-800 words) from somdipto.
- Cross-post the weekly ship-log + 1 insight.
- Tag relevant people once / month.

**Telegram (DAILY — v65 priority):**
- @danlab_bot is already live via OpenClaw.
- v65 action item: flip channel to public, set channel username, set pinned message to v65 pinned tweet.
- Use for: short ship-logs, demo links, direct dev chat.
- Don't use for: longform (LinkedIn is for that).

**Hacker News (v65 elevated to primary — first Wednesday of each month, then more):**
- Show HN: danclaw-phase1 in week 26 (06-30 14:00 PT).
- Show HN: audiod v0.6 (the production-tested one) in week 28.
- Ask HN: "What would make a wearable AI companion trustworthy to you?" in week 30.

**YouTube (BIWEEKLY — Sunday 10:00 IST):**
- 2-min demo of `audiod + perceptiond` running on a $300 laptop.
- 5-min essay: "Why we shipped a 50g wearable against Snap's 132g one."
- Asciinema-style screen recording (we already ship this for danlab-multimodal).

**arXiv / Blog (QUARTERLY — every 12 weeks):**
- One preprint from danlab-multimodal: "Pre-RL Scaffold."
- One essay on audiod/perceptiond architecture.

**Reddit (WEEKLY):**
- r/indianstartups: weekly update from somdipto.
- r/MachineLearning: monthly paper / preprint.
- r/LocalLLaMA: monthly danlab-multimodal update.
- r/singularity: one longform AMA / quarter.

**India cohort media (v65 new — secondary tier):**
- YourStory, Inc42, IndiaAI dispatch, MediaNama, FactorDaily.
- Hook: "AGI from India — the indie's roadmap."
- Don't pitch until we have 50 stars + 100 weekly clones.

---

## 5. Brand voice rules (v65)

**Do:**
- Use bullet points and short sentences.
- Use code blocks in tweets when the claim is technical.
- Use tables for comparisons.
- Be specific: "101/101 tests" beats "well-tested." "PID 10887" beats "live."
- Use 🇮🇳 once per post, not five times.
- Use 👾 in the byline.
- When the receipt is curl-able, paste the curl.
- **v65 new:** when the artifact is on GitHub, paste the link with the first 6 chars of the SHA.
- **v65 new:** "v0.6.0-audiod" beats "the latest version." Specific tags beat vague claims.

**Don't:**
- No "revolutionary," "game-changing," "next-generation," "cutting-edge."
- No exclamation marks except in headlines.
- No stock photos. Ever.
- No "AI-powered" as a standalone adjective.
- No mention of competitors by name unless the comparison is technical and substantiated. *Exception (v65):* in the India cohort context, name Oculosense + Sarvam to position the wedge.
- No "DM us to partner" CTAs.

**Tone examples:**

✅ "audiod v0.6 is live. `curl http://localhost:8741/health` → `{"status":"ok","service":"audiod"}`. 101/101 tests. PID 10887. MIT. https://github.com/somdipto/dan-glasses/releases/tag/v0.6.0-audiod"

❌ "We're thrilled to announce audiod v0.6 — our revolutionary new audio daemon that changes everything!"

✅ "302MB combined. SmolVLM-256M + mmproj. ~32s per image on CPU. MIT. `python3 src/demo.py demo`."

❌ "Our cutting-edge multimodal AI pipeline delivers unprecedented performance in an industry-leading compact form factor!"

**v65 new tone example — the India wedge:**

✅ "Three AI glasses out of India this year. Oculosense (offline-only, visually-impaired-focused). Sarvam (cloud-first, government halo). Dan Glasses (MIT + on-device + proactive + India-priced). The only one with all four. audiod v0.6 is live."

❌ "Unlike other Indian AI glasses startups, our solution offers a unique combination of features that sets us apart from the competition."

---

## 6. v65 weekly cadence

**Monday 09:00 IST:** GitHub release + ship-log tweet (X + Telegram).
**Tuesday 11:00 IST:** LinkedIn longform.
**Wednesday 09:00 IST:** Reddit post (r/indianstartups or r/MachineLearning).
**Thursday 21:00 IST:** Open office hours (Zoom, public — start when 10 public users).
**Friday 18:00 IST:** X thread + YouTube drop (alternating weeks).
**Sunday 10:00 IST:** Week-in-review LinkedIn longform + YouTube short.

**Daily 09:00 IST:** One ship-log tweet (X + Telegram @danlab_bot).
**Daily 09:30 IST:** Reply to one relevant account.
**Daily 23:00 IST:** Save 1 insight to the content backlog.

**v65 monthly anchor (last Wednesday):** Hacker News — Show HN, Ask HN, or thoughtful comment.

---

## 7. Metrics we care about (v65)

**North star:** Weekly active clones (`gh api repos/{owner}/{repo}/traffic/clones`).
**Input 1:** GitHub stars across all public repos.
**Input 2:** X followers (post-impressions).
**Input 3:** LinkedIn post impressions.
**Input 4:** Telegram @danlab_bot subscribers.
**Input 5 (NEW v65):** Hacker News points + comments on Show HN posts.
**Input 6 (NEW v65):** Reddit post upvotes on r/LocalLLaMA, r/MachineLearning, r/indianstartups.

**Don't care about (yet):**
- DAU on a product we haven't shipped.
- App Store ranking (no app).
- Press mentions (until we have 100 stars).
- Waitlist signups (no waitlist — we ship).
- Telegram "channel views" (viral ≠ valuable).

---

## 8. v65 risks and mitigations

| Risk | Probability | Mitigation |
|---|---|---|
| Press calls us "AGI from India" and overhypes | High | "What we are NOT" block on landing page + every blog post |
| Competitor (Oculosense, Sarvam) announces same proactive loop | Medium | We shipped audiod v0.6 first; receipts matter; we cite 101/101 tests |
| HN thread turns negative on the India-origin framing | Medium | Lead with the substance (audiod test count, danlab-multimodal reproducible), not the origin |
| HN thread turns negative on the small-team / underdog framing | Medium | Don't frame as underdog. Frame as "indie lab with a working artifact." Receipts, not narrative. |
| somdipto burns out doing daily tweets | Medium | Rotate with @danlab_dev handle; ship-log is templated; office hours is weekly, not daily |
| Tier 1 enterprise pilot arrives before Tier 1 community exists | Low | Politely defer; ask them to wait for v1 desktop |
| Telegram channel goes public and gets spammed | Medium | Use invite-link-only, approve-join mode, public read-only |
| Show HN for DanClaw Phase 1 gets <50 points | Medium | Title is everything. Test 3 titles on day-job Slack first. Have a backup post ready. |
| Public repos reveal under-tested or broken daemons | High | Tag only audiod v0.6 as stable. perceptiond/memoryd as "spec'd, runnable, tests pending." Don't oversell. |

---

## 9. What v65 does NOT do

- Does not run ads. (No budget, no team.)
- Does not pitch investors. (Bootstrapping; that's a separate track.)
- Does not publish a podcast. (No bandwidth.)
- Does not sponsor events. (No budget.)
- Does not promise hardware dates. (BOM is a target, not a date.)
- Does not ship a landing page that overstates. (v65 landing copy is honest.)
- Does not claim RL. (danlab-multimodal README already disclaims.)
- Does not claim AGI. (We are aspirational. We say so once / quarter, max.)
- Does not name competitors in the README. (The comparison table lives on the landing page and in the India-cohort press pitches, not the README.)

---

## 10. v65 → v66 transition

**v66 will be the "first 50 stars" pass.** Once audiod + danlab-multimodal together cross 50 GitHub stars, v66 will:
1. Open a public mailing list.
2. Open the waitlist for v1 desktop companion.
3. Plan the AWE 2027 application.
4. Draft a press list with somdipto's short bio.
5. Open the danlab.dev refresh to public beta (collect email).
6. Spin up a Discord/Matrix per daemon.

**Don't do any of those now.** v65 is "ship the public surface, ship the cadence, count clones."

---

## 11. v65 action items (this week)

1. **Push 3 public repos:** `somdipto/dan-glasses`, `somdipto/danlab-multimodal`, `somdipto/danclaw` (or `danclaw-phase1`).
2. **Claim @danlab_dev** on X. Cross-post first 10 tweets.
3. **Flip @danlab_bot to public** on Telegram. Set channel username. Pin v65 pinned tweet.
4. **Refresh danlab.dev** with v65 landing copy. (Push to zo.space or build a Site — confirm with somdipto.)
5. **Show HN draft for DanClaw Phase 1**, scheduled 2026-06-30 14:00 PT.
6. **First YouTube demo:** 2-min audiod + perceptiond screen cast, schedule 2026-06-29.
7. **Commit the v65 READMEs** to the public repos.
8. **Confirm or shift** the open questions in `dan1-marketing-research.md` v65 §14.

---

**Filed under:** `agent-work/dan1-marketing-strategy.v65.md`
**Next:** `agent-work/dan1-content-calendar.v65.md`
