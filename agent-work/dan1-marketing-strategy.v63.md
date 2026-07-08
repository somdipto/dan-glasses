# Dan1 Marketing Strategy — v63

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-20 09:30 IST (04:00 UTC)
**Status:** ✅ Canonical. Supersedes v62.
**Read first:** `dan1-marketing-research.md` v63.

> **v63 thesis:** Stop pitching the future. Pitch the shipping log. We are no longer pre-launch; audiod v0.6 is live, danclaw phase 1 is downloadable, danlab-multimodal is reproducible. The marketing job is to make the *cadence* the brand.

---

## 1. The strategic shift (v62 → v63)

| Dimension | v62 framing | v63 framing |
|---|---|---|
| Headline claim | "Indie AI lab shipping the first proactive companion" | "We ship weekly. Here's what shipped this week." |
| Primary proof | AWE 2026 receipts, Snap Specs comparison, Qualcomm START | audiod v0.6 (101/101 tests), danclaw-phase1.tar.gz, danlab-multimodal reproducible |
| Audience priority | Press + early adopters (Tier 1) | Developers on GitHub + LinkedIn (Tier 1) — same priority, different channel |
| Channel priority | Show HN + Twitter threads | GitHub releases + LinkedIn longform + X thread, in that order |
| Tone | Provocative, frame the open-source wedge | Operational, frame the shipping cadence |
| CTA | "Join the waitlist" | "Clone the repo. Run the daemon. Tell us what broke." |
| What we're NOT | Reactive assistant | Reactive press — no media push until danclaw-phase1 has 100 GitHub stars |

**Why the shift:** Audiod v0.6 is the first daemon that someone can curl on a remote machine and see a 200 OK. The story changed from "we're going to build this" to "this is the artifact and it's running." Operational tone matches operational reality.

---

## 2. Three pillars (do not edit)

These three messages are the only three we say, in three different orders, every week:

1. **Proactive, not reactive.** The loop runs continuously. Audiod listens. Perceptiond watches. Memoryd remembers. We surface only when salience justifies it.
2. **On-device, MIT, modular.** Seven daemons. All MIT. All inspectable. No cloud lock-in. No black boxes.
3. **From India to the world.** Cost base + geopolitical hedge + a real frontier signal. Building AGI from the other side of the planet.

**Why three, not five:** Three is the number a person can remember after one read. Five is the number a person forgets before the second read.

**Why these three:** They map to (1) the architectural wedge, (2) the integrity wedge, (3) the narrative wedge. Drop any one and the story collapses.

---

## 3. Audience prioritization (90-day plan)

**Tier 1 — developer-early-adopter (target: 50 by 2026-09-20):**

- Channels: GitHub, X, Reddit (r/MachineLearning, r/LocalLLaMA, r/indianstartups), Hacker News (Show HN).
- Content: weekly ship-log, monthly deep dive, ad-hoc reply-to-tweets from AR / AI tweeters.
- Success metric: 50 stars across all public repos + 100 unique clone/week + 10 issues opened by external users.
- CTA: `git clone somdipto/dan-glasses && cd dan-glasses && ./scripts/start-all.sh`

**Tier 2 — accessibility / cognitive-load community (target: 200 by 2026-12-20):**

- Channels: HackerNoon essay, IndiaAI dispatch, YourStory, Substack.
- Content: 1 longform/month on audiod + memoryd as a "remember for me" stack for ADHD, dementia caregivers, low-vision users.
- Success metric: 1 press mention in a Tier 2 outlet + 200 mailing-list signups + 50 installs of the desktop companion.
- CTA: "Try the desktop companion. It's free. It's MIT. It's yours."

**Tier 3 — enterprise pilots (target: 5 pilots by 2027-03-20):**

- Channels: direct outreach, conferences (KCD India, PyCon India).
- Content: 1 case study / quarter from a Tier 1 user who crosses over (e.g., a doctor, a field tech).
- Success metric: 5 paid pilots with monthly retention ≥ 80%.
- CTA: "Book a 30-min call with somdipto." (NOT a sales form.)

**Don't pitch Tier 3 publicly.** Enterprise pilots come from Tier 1 users crossing over. They don't come from cold outbound.

---

## 4. Channel playbook (concrete)

**GitHub (PRIMARY — every Monday):**
- Release note per merged PR > 50 LOC.
- Use `gh release create` with `## What's Changed` + `## Verify` sections.
- Pin: audiod, danclaw-phase1, danlab-multimodal, dan-glasses.
- Repo topics: `ai-companion`, `wearable`, `on-device`, `mit-license`, `india`, `proactive-agent`.
- Every repo README must end with: `Built at danlab.dev 🇮🇳`

**X / Twitter (DAILY — 09:00 IST):**
- One ship-log tweet (image or 4-line status).
- One insight tweet (1-sentence, contrarian if possible).
- One reply to a relevant account (AR/AI/multimodal/open-source).
- One thread / week (Friday 18:00 IST).

**LinkedIn (WEEKLY — Tuesday 11:00 IST):**
- Longform (400-800 words) from somdipto.
- Cross-post the weekly ship-log + 1 insight.
- Tag relevant people once / month (buildspace alum, Kaggle Bengaluru, etc.).

**Hacker News (MONTHLY — first Wednesday):**
- Show HN: danclaw-phase1 in week 1.
- Show HN: audiod v0.6 (the production-tested one) in week 3.
- Ask HN: "What would make a wearable AI companion trustworthy to you?" in week 4.

**YouTube (BIWEEKLY — Sunday 10:00 IST):**
- 2-min demo of `audiod + perceptiond` running on a $300 laptop.
- 5-min essay: "Why we shipped a 50g wearable against Snap's 132g one."
- Asciinema-style screen recording (we already ship this for danlab-multimodal).

**arXiv / Blog (QUARTERLY — every 12 weeks):**
- One preprint from danlab-multimodal: "Pre-RL Scaffold: A Heuristic Feedback Loop for Sub-300MB VLM Inference on CPU."
- One essay on audiod/perceptiond architecture.

**Reddit (WEEKLY):**
- r/indianstartups: weekly update from somdipto.
- r/MachineLearning: monthly paper / preprint announcement.
- r/LocalLLaMA: monthly danlab-multimodal update.
- r/singularity: one long-form AMA / quarter.

---

## 5. Brand voice rules

**Do:**
- Use bullet points and short sentences.
- Use code blocks in tweets when the claim is technical.
- Use tables for comparisons (Snap Specs vs Dan Glasses, danlab-multimodal vs moondream2).
- Be specific: "101/101 tests" beats "well-tested." "302MB combined" beats "small."
- Use 🇮🇳 once per post, not five times.
- Use 👾 in the byline; this is the persona emoji.

**Don't:**
- No "revolutionary," "game-changing," "next-generation," "cutting-edge."
- No exclamation marks except in headlines.
- No stock photos. Ever.
- No "AI-powered" as a standalone adjective.
- No mention of competitors by name unless the comparison is technical and substantiated.
- No "DM us to partner" CTAs.

**Tone examples:**

✅ "audiod v0.6 shipped. Adaptive whisper timeout. 101/101 tests. New PID 10887. https://github.com/somdipto/dan-glasses/releases"

❌ "We're thrilled to announce audiod v0.6 — our revolutionary new audio daemon that changes everything!"

✅ "302MB combined. SmolVLM-256M + mmproj. ~32s per image on CPU. MIT. Hackathon-grade. `python3 src/demo.py demo`."

❌ "Our cutting-edge multimodal AI pipeline delivers unprecedented performance in an industry-leading compact form factor!"

---

## 6. v63 weekly cadence (this is the operating system)

**Monday 09:00 IST:** GitHub release + ship-log tweet.
**Tuesday 11:00 IST:** LinkedIn longform.
**Wednesday 09:00 IST:** Reddit post (r/indianstartups or r/MachineLearning).
**Thursday 21:00 IST:** Open office hours (Zoom, public).
**Friday 18:00 IST:** X thread + YouTube drop (alternating weeks).
**Sunday:** Plan next week. Read receipts. Update v64.

**Daily 09:00 IST:** One ship-log tweet.
**Daily 09:30 IST:** Reply to one relevant account.
**Daily 23:00 IST:** Save 1 insight to the content backlog.

**This is not negotiable.** The cadence is the brand. If we ship 3 things and tweet 1, the brand is "we shipped 1." If we ship 1 thing and tweet 7, the brand is "we tweet a lot." Ship 1, tweet 1. Compound.

---

## 7. Metrics we care about (and ones we don't)

**Care about (north star + 3 inputs):**
- **North star:** Weekly active clones (`gh api repos/{owner}/{repo}/traffic/clones`).
- **Input 1:** GitHub stars across all public repos.
- **Input 2:** X followers (post-impressions).
- **Input 3:** LinkedIn post impressions.

**Don't care about (yet):**
- DAU on a product we haven't shipped.
- App Store ranking (no app).
- Press mentions (until we have 100 stars).
- Waitlist signups (no waitlist yet — we ship, not waitlist).

**Why "clones" not "users":** We're pre-consumer. The unit of progress is a developer who runs the daemon. Clones are that, observably, on GitHub.

---

## 8. v63 risks and how we mitigate them

| Risk | Probability | Mitigation |
|---|---|---|
| Press calls us "AGI from India" and overhypes | High | Have a 1-paragraph "what we are NOT" block on the landing page and every blog post |
| Competitor announces same proactive loop | Medium | We shipped audiod v0.6 first; receipts matter |
| Hacker News thread turns negative on the India-origin framing | Medium | Lead with the substance (audiod test count, danlab-multimodal reproducible), not the origin |
| somdipto burns out doing daily tweets | Medium | Rotate with @danlab_dev handle; ship-log is templated |
| HackerNoon / YourStory asks for founder photo with brand name | High | Have a single brand-asset folder on disk by week 2 |
| Tier 1 enterprise pilot arrives before Tier 1 community exists | Low | Politely defer; ask them to wait for v1 desktop |

---

## 9. What v63 does NOT do

- Does not run ads. (No budget, no team.)
- Does not pitch investors. (Bootstrapping; that's a separate track.)
- Does not publish a podcast. (No bandwidth.)
- Does not sponsor events. (No budget.)
- Does not promise hardware dates. (BOM is a target, not a date.)
- Does not ship a landing page that overstates. (v63 landing copy is honest.)

---

## 10. v63 → v64 transition (what changes next)

**v64 will be the "first 50 stars" pass.** Once audiod + danclaw-phase1 + danlab-multimodal together cross 50 GitHub stars, v64 will:
1. Open a public mailing list.
2. Open the waitlist for v1 desktop companion.
3. Plan the AWE 2027 application.
4. Draft a press list with somdipto's short bio.

**Don't do any of those now.** v63 is "ship weekly, post daily, count clones."
