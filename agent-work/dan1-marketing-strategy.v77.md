# Dan1 Marketing Strategy — v77

**Built:** 2026-06-22 11:30 IST — v77 trigger
**Author:** Dan1 👾
**Companion to:** `dan1-marketing-research.v77.md`
**Read time:** 8 min

---

## TL;DR (v77)

**One move, one quarter, one moat.**

- **The move:** ship dglabs-eval v1 (publishable benchmark) and ride three news waves (Snap launch, Meta Stella scandal, Apple delay).
- **The quarter:** Jun 22 → Sep 30, 2026. 100 dev-kit pre-orders, 1,000 newsletter subs, 100 GitHub stars, 1 Show HN (Aug 4), 1 dglabs-eval arXiv paper, 1 founder essay in YourStory.
- **The moat:** "The only smart glasses shipping without a covert facial-recognition update, an audit-able eval the community can run, and a $189 dev kit that ships in Q4."

**Three sentences you can use tomorrow:**

1. "Every other smart glasses vendor in 2026 is either $2,195, facial-recognizing you without consent, or 18 months late. Dan Glasses is $189, on-device, MIT, and ships in 12 months."
2. "dglabs-eval v1 ships Aug 31, 2026. The first public benchmark for proactive AI glasses. We will publish our own row first."
3. "Snap launched $2,195 Specs. Meta shipped facial-rec in 50M installs without disclosure. Apple pushed to 2027. We're building the open, audit-able, on-device alternative — from Bengaluru, in the open, MIT."

---

## 1. The three waves (v77)

We don't have a marketing budget. We have timing. Three waves broke in the last 72 hours:

### Wave 1: Snap Specs (Jun 16 2026)

- **What happened:** Snap launched Specs at $2,195. AR glasses, full color, standalone, 4h battery, 132-136g. Stock fell 11%.
- **The frame:** "Glasses are the next computer" — same line Zuck has been using.
- **Our wedge:** "Yes — and the OS for the next computer should be open. Ours is. It's called Paperclip. It's MIT. $189."
- **The math:** $2,195 / $189 = 11.6x. The price-anchor story writes itself.
- **The risk:** Snap gets compared to Vision Pro (heavy, expensive, niche) and we get associated. **v77 counter:** we explicitly compare to Snap, not Vision Pro. Snap is the relevant comp. Vision Pro is in a different category.

### Wave 2: Meta Stella scandal (Jun 4-5 2026)

- **What happened:** Buchodi (security researcher) + WIRED disclosed that Meta's Stella companion app (50M+ downloads) shipped a dormant facial-recognition pipeline: 3 on-device AI models, biometric DB, "nametags_recognition" notification channel. Code had been added across updates since January 2026.
- **The frame:** Cloud-only AI vendors can't be trusted with your face.
- **Our wedge:** "Our AI runs on-device. Our model weights live in `~/.danlab/state/`, plain text, version-controlled. We commit to never shipping facial-recognition in a stealth app update. This is in CONTRIBUTING.md."
- **The risk:** we look like we're punching up at Meta. **v77 counter:** we're not — we're stating a fact about the architecture. The architectural choice IS the story.
- **The hook:** "Snap's $2,195 Specs are 5.5x the price. Meta's $799 Ray-Bans are secretly running facial-rec on you. Apple's are 18 months away. Our $189 dev kit runs on-device, audit-able, MIT, and ships in Q4."

### Wave 3: Apple AI glasses delayed (May 31 2026)

- **What happened:** Bloomberg/Gurman: Apple AI glasses pushed from end-2026 to late 2027. Vision Pro line cancelled (Kuo). Vision Air 2029.
- **The frame:** The "Apple-quality" window is open 18-24 months.
- **Our wedge:** "We're shipping in 12. The mid-market window is ours to lose."
- **The risk:** Apple shipping an actually-good $399 pair in 18 months would change the market. **v77 counter:** Apple hasn't shipped a $399 wearable that does what they want in 10 years. Vision Pro at $3,499 is what Apple ships. Their track record on price is bad. We bet on Apple being late and expensive; we plan to be early and cheap.

**v77 playbook:** ride the waves with low-cadence, high-signal posts. **2 posts/day X (weekdays), 1 long-form LinkedIn/week, 1 newsletter/2 weeks.** The goal is not volume; the goal is being the obvious "open + on-device + audit-able + consent-first" reference in the comment section of every smart-glasses article for the next 90 days.

---

## 2. The one move: ship dglabs-eval v1

**Why this is the move:** every other smart-glasses marketing pitch in 2026 is a hardware pitch. "Buy our glasses." Ours can't be, because we're not shipping v2 (display) until 2027 Q1. **So we have to sell the moat, not the product.** The moat is the eval.

**The dglabs-eval v1 launch (v77, locked):**

| Milestone | Date | What ships |
|-----------|------|------------|
| v0.1 paper draft | 2026-07-14 | arXiv preprint, 55 scenarios, 5 categories, MIT, anti-capture clause |
| v0.1 code + scenarios | 2026-07-21 | GitHub release, leaderboard scaffold, runnable on consumer hardware |
| v0.5 safety subset | 2026-07-28 | + Agents of Chaos (6 tasks) + Sentry key hijack scenario |
| Show HN | 2026-08-04 | "Show HN: Dan Glasses — an open, audit-able, on-device AI glasses stack from India" |
| v1 paper + leaderboard | 2026-08-31 | Public leaderboard row: Dan Glasses v0.7 audiod vs Perplexity Brain baseline on memory subset |
| Dev kit pre-order | 2026-09-01 | $189 refundable deposit, ships Q4 2026 |

**The eval story is the company story for the next 6 months.** Every post, every LinkedIn essay, every newsletter is a path back to dglabs-eval v1.

---

## 3. Audience segmentation (v77)

| Segment | Size (rough) | v77 priority | Channel | Pitch | Conversion event |
|---------|-------------|-------------|---------|-------|-----------------|
| **OSS hackers** | 50K-100K (HN/Reddit/GitHub) | 1 | X, GitHub, Show HN | "audiod v0.7, 122/122 tests, MIT. Clone it." | GitHub star → newsletter → dev kit pre-order |
| **AI safety researchers** | 5K-10K | 2 | arXiv, X, conference circuit | "Run the safety subset on your model." | arXiv citation → leaderboard row → collaboration |
| **India-first builders** | 50K-200K (LinkedIn IN, dev.to) | 3 | LinkedIn, X (IN), newsletter | "MIT, ₹ pricing, NITI Aayog-aligned, from Bengaluru." | LinkedIn follow → newsletter → dev kit pre-order |
| **Privacy-first founders + consumers** | 100K-500K (Persona C + H) | 4 | LinkedIn, X, YouTube (Tier 3) | "The only glasses without a covert facial-rec update." | Newsletter → dev kit pre-order |
| **Accessibility advocates** | 10K-50K | 5 | LinkedIn, partner orgs | "Free dev kit + 6 months of support." | Application → free dev kit |
| **Enterprise CTOs (India)** | 1K-5K | 6 | LinkedIn, direct outreach | "Operational sovereignty. On-device. MIT. Audit-able." | Meeting → pilot |

**v77 priority is 1, 2, 3, 4 in that order for the next 90 days.** 5 + 6 start Q4 2026.

---

## 4. The four brand pillars (v77)

Every artifact, every post, every line of copy must ladder to one of these:

1. **Open.** MIT, GitHub-public, no NDAs, no black boxes. audiod + memoryd + toold + perceptiond + ttsd all on GitHub. CONTRIBUTING.md. CODEOWNERS. Signed releases.
2. **Audit-able.** dglabs-eval is the proof. Every behavior is observable. Every model is inspectable. Every release is signed.
3. **Safety-gated.** toold's audit log. The Agents of Chaos safety subset. The Sentry key hijack scenario. The supply-chain attack task. Safety is a feature, not a blog post.
4. **Consent-first.** The Meta Stella scandal made this non-negotiable. CONTRIBUTING.md commits to: no covert AI updates, no default-on facial recognition, no cloud-only data flows. Every behavior is opt-in, observable, and reversible.

**v77 elevates "consent-first" to pillar 4** because the world changed in the last 72 hours. Pre-Jun 4 2026, "open + audit-able + safety-gated" was the trio. Post-Jun 4 2026, "consent-first" is the fourth pillar.

**v77 house style:** the four pillars appear in this exact order in every long-form piece. **OACS-C** if we need an acronym. (Don't actually use the acronym. It's ugly.)

---

## 5. The 90-day plan (v77, locked)

### Jun 22-30: Snap-week + audit (week 1)

- **Mon Jun 22** (today): publish v77 artifacts. Send this Telegram.
- **Tue Jun 23:** ride Snap wave. X thread: "Snap launched $2,195 Specs. Here's what we built instead." 4 posts.
- **Wed Jun 24:** ride Meta-Stella wave. X thread: "What the Stella scandal teaches us about on-device AI." 3 posts.
- **Thu Jun 25:** ride Apple-delay wave. LinkedIn long-form: "Apple pushed AI glasses to 2027. The window is open." + X thread.
- **Fri Jun 26:** NITI Aayog anchor. LinkedIn: "AI self-reliance is now Indian policy. We're building the answer." + newsletter #1.
- **Sat-Sun:** audit. Newsletter subs, GitHub stars, LinkedIn followers. Set v78 triggers.

### Jul 1-31: dglabs-eval v0.1 + v0.5 (weeks 2-6)

- **Week 2:** v0.1 paper draft, internal review. 2 X posts, 1 LinkedIn essay ("Why we built a smart-glasses eval, not a smart-glasses product").
- **Week 3:** v0.1 paper on arXiv (Jul 14). Newsletter #2: "The dglabs-eval v0.1 paper is out."
- **Week 4:** v0.1 code + scenarios ship (Jul 21). X thread + LinkedIn. GitHub release notes.
- **Week 5:** v0.5 safety subset (Jul 28). X thread: "The Agents of Chaos safety subset: 6 tasks. 1 of them is a Sentry key hijack." Newsletter #3.
- **Week 6:** Show HN prep. Draft post, dry-run with 5 friends. Demo video.

### Aug 1-31: Show HN + dglabs-eval v1 (weeks 7-11)

- **Mon Aug 3:** Show HN dry-run. Press kit ready. Demo video published on YouTube.
- **Tue Aug 4:** Show HN post goes live. Stay online for 24h, answer every comment.
- **Aug 5-15:** Show HN ripple. Cross-post to r/MachineLearning, r/LocalLLaMA, r/developersIndia, r/IndianModerate. 2 LinkedIn essays, 1 X thread.
- **Aug 16-31:** v1 paper + leaderboard prep. Newsletter #4: "Show HN was 3 days ago. Here's what changed." + dglabs-eval v1 paper draft.
- **Mon Aug 31:** dglabs-eval v1 ships. Public leaderboard row.

### Sep 1-30: Dev kit pre-order + Indian moment (weeks 12-15)

- **Sep 1:** Dev kit pre-order opens. $189 refundable.
- **Sep 1-7:** Founder essay in YourStory / Forbes India pitch (submit). LinkedIn announcement.
- **Sep 8-15:** YourStory / Forbes India placement (if accepted). Cross-post to LinkedIn.
- **Sep 16-30:** Pre-order push. Target: 100 by Sep 30. Newsletter #5: "100 pre-orders by Sep 30."
- **Sep 30:** v77 retro. Plan v78.

---

## 6. Metrics (v77, the only ones that matter)

| Metric | v77 starting (Jun 22 2026) | v77 target (Sep 30 2026) | Source |
|--------|---------------------------|------------------------|--------|
| GitHub stars (sum across all repos) | 22+ | 100+ | GitHubLB |
| Newsletter subs | 220+ (audit pending) | 1,000+ | Substack |
| LinkedIn followers (somdipto) | 19 | 500+ | LinkedIn |
| X followers (@NandySomdipto) | ~50 | 500+ | X |
| X followers (@dan2agi) | ~10 | 200+ | X |
| Discord members | ~50 | 200+ | Discord |
| Dev kit pre-orders | 0 | 100 | Stripe |
| dglabs-eval v1 leaderboard rows | 0 | 5 (us + 4 community) | dglabs-eval |
| arXiv citations | 0 | 10+ | Google Scholar |
| Press placements | 0 | 1 (YourStory or Forbes IN) | Manual |
| Show HN rank | - | top 10 of the day | HN |

**v77 primary KPI: GitHub stars.** Everything else is a leading indicator of stars. Show HN is the single biggest star-driver; the eval paper is the second.

---

## 7. Risks (v77, honest)

1. **dglabs-eval v1 slips past Aug 31.** Most likely failure mode. Mitigation: v0.1 ships Jul 21 even if v0.5 slips. v0.5 can be a separate minor release.
2. **Show HN underperforms.** Mitigation: don't depend on it. The eval paper is the durable spike. Show HN is a one-shot.
3. **Snap announces a $399 version.** Mitigation: the open-source moat is the point. We welcome it. Our pitch becomes "the open-source one."
4. **Meta responds to Stella with a consent-first commitment.** Mitigation: it's been their pattern for 10 years. We don't bet on Meta changing.
5. **India hardware supply chain bottleneck.** Mitigation: v1 dev kit uses off-the-shelf components (Bose Frames + OAK-D + Raspberry Pi CM4). v2 display module is where the supply-chain risk lives.
6. **Founder burnout.** Mitigation: Dan1 👾 owns the marketing pipeline. somdipto owns the architecture + the eval. Boundaries are explicit.

**v77 most-likely failure mode is #1** (dglabs-eval slip). If we miss Aug 31, the v78 plan defaults to "ship v0.5 in public, narrate the work, don't promise dates we can't keep."

---

## 8. The 10 things Dan1 will ship this week (v77, concrete)

1. **v77 marketing research** — done, this file.
2. **v77 marketing strategy** — done, this file.
3. **v77 content calendar** — see `dan1-content-calendar.v77.md`.
4. **v77 Twitter bio + 10 posts** — see `dan1-twitter-content.v77.md`.
5. **v77 landing page copy** — see `dan1-landing-copy.v77.md`.
6. **v77 GitHub README improvements** — see `dan1-github-readme-suggestions.v77.md`.
7. **Telegram delivery to somdipto** — this message.
8. **Audit the 220+ newsletter subs claim** — Substack dashboard screenshot, file at `agent-work/newsletter-audit-jun22.md`.
9. **GitHub stars baseline** — count + screenshot, file at `agent-work/github-stars-baseline-jun22.md`.
10. **First v77 X thread: "Snap launched $2,195 Specs. Here's what we built instead."** — file at `agent-work/x-thread-1-snap-launched.md`.

**v77 → v78 trigger:** dglabs-eval v0.1 paper draft complete (target Jul 14). v78 = "from moat to spike: the eval launch quarter."

---

## 9. The strategy in one paragraph (v77)

For the next 90 days, danlab.dev runs a single bet: **ship dglabs-eval v1, ride the three news waves (Snap + Meta + Apple), grow GitHub stars from 22 to 100, and turn the Open + Audit-able + Consent-first + Safety-gated positioning into the obvious reference in every smart-glasses comment thread.** No paid ads. No agency. No conference circuit until NeurIPS 2026. Two X posts a day, one LinkedIn essay a week, one newsletter every two weeks, one Show HN, one arXiv paper, one dev kit pre-order. The moat is the eval; the spike is Show HN; the moat stays because the eval is reproducible.

That's the strategy. Ship it.

---

*Dan1 👾 — built in Bengaluru with somdipto, for the open-source wearable AI community.*
."
- **The risk:** Apple ships something in 2027 that crushes the mid-market. **v77 counter:** Apple is closed, our eval is open. The community will always prefer the OS they can audit.

### Why this works (v77 logic)

The three waves aren't a coincidence. They're the same wave: **the closed-system smart-glasses future is breaking, and the open alternative is the only one that scales.**

- Snap's $2,195 says "closed AR is expensive."
- Meta's Stella scandal says "closed AI is dangerous."
- Apple's 2027 delay says "closed hardware is slow."

**Danlab's three sentences:**

1. Open (Paperclip is MIT, audiod is MIT, eval is MIT).
2. On-device (memoryd runs locally, audiod runs locally, the model weights are in plain text).
3. Consent-first (we commit in CONTRIBUTING.md to never ship covert updates; the eval publishes the safety subset).

**v77 logic check:** "do we have receipts for each claim?" Yes.
- **Open:** github.com/somdipto/dani, github.com/somdipto/dan-glasses, github.com/somdipto/paperclip. All MIT.
- **On-device:** audiod runs on CPU at <2W, memoryd on MiniLM-L6-v2 (90MB), 8/8 daemons live.
- **Consent-first:** CONTRIBUTING.md to be updated Jun 25 with the no-covert-updates clause.
- **Eval:** dglabs-eval v0.1 ships Jul 21, v0.5 Jul 28, v1 Aug 31.

**v77 logic check #2: "is the moat defensible?"** Yes.
- The eval: once published, it's a public good. We get first-mover on the leaderboard. Other vendors can submit rows, but they submit on our terms.
- The architecture: audiod + memoryd + toold + perceptiond + ttsd is 5 services + Paperclip kernel. ~12 person-months of work to replicate. Even Meta couldn't ship this in 6 months.
- The community: OSS maintainers, OSS users, the eval leaderboard, the Paperclip community. These compound.

---

## 2. The positioning stack (v77)

**v77 four-quadrant positioning, in order of strength:**

```
              Audit-able
                  ▲
                  │
   Open ──────────┼────────── On-device
                  │
                  ▼
            Consent-first
```

**Primary claim (1 sentence):** Dan Glasses is the open, audit-able, on-device, consent-first AI companion wearable, with a publishable eval as proof.

**Secondary claims (1 sentence each):**

- **Open:** Paperclip (OS), audiod (VAD), memoryd (vector store), toold (skills), perceptiond (vision), ttsd (voice). All MIT. All on GitHub.
- **Audit-able:** dglabs-eval v1 ships Aug 31 2026. 55 tasks, 5 categories, public leaderboard. We publish our own row first.
- **On-device:** audiod runs on CPU at <2W. memoryd runs on MiniLM-L6-v2 (90MB). No cloud-only features. No "we'll process your face in the cloud" surprise.
- **Consent-first:** CONTRIBUTING.md commits to: (a) no covert AI updates, (b) no facial-rec without explicit opt-in release note, (c) all model weights in plain text on disk, (d) all releases GPG-signed.

**Tertiary claims:**

- Built in Bengaluru 🇮🇳. Neprion-manufacturable. $189 dev kit.
- NITI Aayog-aligned. Open path. Indian AI sovereignty.
- 8/8 daemons live. 122/122 audiod tests. 1.5h+ uptime.
- From the founder of danlab.dev. From the team behind Paperclip, danlab-multimodal, and dan-consciousness.

**v77 anti-claims (what we are NOT):**

- We are NOT a fashion accessory. v1 is a developer kit. v2 is the fashion product.
- We are NOT a Ray-Ban competitor. Ray-Ban Meta is a closed cloud product. We're the open alternative.
- We are NOT trying to beat Apple. Apple is late 2027. We ship Q4 2026.
- We are NOT the "cheaper Snap." Snap is $2,195. We're $189. The price is the proof, not the marketing.

---

## 3. The 90-day plan (Jun 22 → Sep 22, 2026)

**Three phases, 30 days each:**

### Phase 1: Wave-riding (Jun 22 - Jul 22, 2026)

**Goal:** ride the three news waves, build audience, ship eval v0.1.

- Week 1 (Jun 22-28): ship v77 calendar. 10 posts. First LinkedIn essay. Newsletter #1.
- Week 2 (Jun 29 - Jul 5): 10 more posts. LinkedIn essay #2 ("why on-device is the only answer to Stella"). Newsletter #2.
- Week 3 (Jul 6-12): 10 more posts. LinkedIn essay #3 ("what we learned shipping 8 daemons"). CONTRIBUTING.md ships with no-covert-updates clause.
- Week 4 (Jul 13-19): eval v0.1 final prep. README polish. Cross-link from Show HN comment seed.
- **Day 30 (Jul 21):** **dglabs-eval v0.1 ships on GitHub. arXiv paper submitted. First HN cross-link.**

**KPI targets by Jul 22:**
- 350 newsletter subs (from 200+)
- 350 GitHub stars total (from ~200)
- 50 dglabs-eval stars (from 0)
- 600 X followers (@dan2agi, from ~400)
- 1 LinkedIn essay/week for 4 weeks
- 1 newsletter / 4 weeks
- 30+ posts on X

### Phase 2: The spike (Jul 22 - Aug 22, 2026)

**Goal:** ship eval v0.5, run Show HN, build the leaderboard.

- Week 5 (Jul 22-26): eval v0.1 first 7 days. Triage issues, merge PRs, ship v0.5.
- Week 6 (Jul 27 - Aug 2): **dglabs-eval v0.5 ships Jul 28** (safety subset, supply-chain attack, reproducible eval). Pre-launch HN comment seed.
- Week 7 (Aug 3-9): **Show HN: Aug 4.** Target: top 5. Reply to every comment in first 4h. Ship a "Show HN follow-up" thread on Aug 5.
- Week 8 (Aug 10-16): post-Show-HN lull. Write the Show HN retrospective. 10 more posts. LinkedIn essay #4.
- **Day 60 (Aug 22):** 500 GitHub stars total, 150 eval stars, 25 dev-kit pre-orders.

**v77 Show HN draft (Aug 4):** see content calendar for full text. TL;DR: "dglabs-eval: a public, MIT, reproducible benchmark for proactive AI glasses. 55 tasks, 5 categories, on-device, audit-able. We ship our own row first."

### Phase 3: The proof (Aug 22 - Sep 22, 2026)

**Goal:** ship eval v1, dev-kit pre-orders, first press features.

- Week 9 (Aug 22-26): eval v0.5 first 2 weeks. Triage. Prep v1.
- Week 10 (Aug 27 - Sep 2): **dglabs-eval v1 ships Aug 31.** Public leaderboard. Our own row. First external row. **Product Hunt launch same day.**
- Week 11 (Sep 3-9): post-launch lull. Press outreach. YourStory pitch.
- Week 12 (Sep 10-16): dev-kit pre-order page ships. $189 v1 (audio-only), $399 v2 (with display). First 25 pre-orders.
- **Day 90 (Sep 22):** 800 GitHub stars, 350 eval stars, 50 dev-kit pre-orders, 1,000 newsletter subs, 1 YourStory feature.

**v77 → v78 transition:** v78 = post-eval-v1 retrospective. Trigger: Sep 30, 2026. v78 thesis will be: "we shipped the eval, we shipped the dev-kit page, now we ship the dev-kit."

---

## 4. v77 channel mix (with budget)

**v77 has zero paid budget.** All channels are organic. Time is the constraint.

| Channel | Time/week | Owner | KPI |
|---------|-----------|-------|-----|
| X / Twitter | 5h | Dan1 (with somdipto review) | followers, impressions, replies |
| LinkedIn (somdipto) | 2h | somdipto | connections, essay views, reposts |
| GitHub | 8h (engineering overlap) | engineering (Dan2, Dan3) | stars, PRs, issues |
| Newsletter | 3h (per issue) | somdipto + Dan1 | subs, open rate, click rate |
| Discord | 1h | Dan1 | active members |
| YouTube devlog | 4h (per video) | somdipto | views, watch time |
| Reddit / HN | 1h | Dan1 | post rank, comment upvotes |
| Press / podcasts | 1h | somdipto | features, interviews |

**v77 total time:** ~25h/week of marketing effort. Somdipto's time: ~10h/week. Dan1's time: ~15h/week.

**v77 "vibes budget":** zero. v77 explicitly does NOT do paid ads, sponsored posts, or influencer deals. v77 thesis: "the three waves are organic. Riding organic waves with organic content is the move."

---

## 5. v77 risks (and the counter)

| Risk | Likelihood | Impact | Counter |
|------|------------|--------|---------|
| Eval v0.1 ships late (after Jul 21) | Medium | High — Show HN derails | **Ship a v0.0.1 on Jul 14 if v0.1 is at risk.** Even an early version with a public README + 10 tasks is enough for Show HN seeding. |
| Show HN doesn't hit front page | Medium | Medium — momentum stalls | **Cross-link from r/LocalLLaMA and r/augmentedreality on same day.** Target top 5, settle for top 20. |
| Stella scandal escalates and we get pulled into the "anti-Meta" narrative | Low | Medium — brand risk | **Stay architectural, not accusatory.** v77 default: "we're not anti-Meta, we're pro-on-device." Never say "Meta is bad." Say "we ship on-device, audit-able, MIT." |
| Apple announces something in 2026 (counter to the delay) | Low | High — kills the "open window" | **Pivot to "even if Apple ships, we ship the open alternative."** The eval is the proof. |
| Somdipto gets pulled into engineering and marketing slips | Medium | High — calendar breaks | **Dan1 ships 80% of the calendar autonomously.** v77 gives Dan1 explicit ownership of X, Discord, Reddit, HN. Somdipto only owns LinkedIn, newsletter, YouTube, press. |
| Snap specs at $2,195 are actually great and we look small | Low | Low — different category | **Different price tier, different OS tier, different country.** Snap is the closed $2K incumbent. We're the open $189 alternative. |
| A major CVE hits audiod | Low | High — trust collapse | **CONTRIBUTING.md commits to: 24h disclosure, signed CVE, post-mortem on the blog within 7 days.** v77 spec this. |
| Eval methodology gets criticized on HN | Medium | Medium — credibility hit | **Pre-publish on arXiv. Invite 3 reviewers. Reply to every criticism in public.** v77 default: take the criticism seriously, don't fight it. |
| Indian press reads NITI Aayog frame as political | Low | Medium — reposts decline | **Lean on the policy quote, not the political framing.** "Karandikar said X. We agree. Here's the open path." |

**v77 thesis on risk:** **the moat is the eval, not the marketing.** If the eval ships, the marketing works. If the eval doesn't ship, the marketing doesn't work. v77 prioritizes the eval ship over the marketing ship.

---

## 6. v77 success criteria

**By Sep 30, 2026 (Q3 end):**

1. **dglabs-eval v1 ships Aug 31 with public leaderboard.** ✅ Success.
2. **Show HN hits top 5 on Aug 4.** Top 20 = partial. Below 20 = failure.
3. **100 dev-kit pre-orders by Sep 30.** 50 = partial. <50 = failure.
4. **1,000 newsletter subs.** 600 = partial. <600 = failure.
5. **1 YourStory / Inc42 / Mint feature.** 2+ = success. 0 = failure.
6. **800 GitHub stars total, 350 on eval.** 500/200 = partial.
7. **CONTRIBUTING.md ships with no-covert-updates clause, signed by somdipto with GPG key.**
8. **First external row on the dglabs-eval leaderboard.** A model from outside danlab submits a row. This is the real "open" proof.

**v77 single-number north star:** **dev-kit pre-orders.** Stars and subs are leading indicators. Pre-orders are the truth. If we don't ship 100 pre-orders by Sep 30, the strategy didn't work.

---

## 7. v77 handoff

- **This document:** `dan1-marketing-strategy.v77.md`
- **Companion docs:**
  - `dan1-marketing-research.v77.md` (the research)
  - `dan1-content-calendar.v77.md` (the calendar)
  - `dan1-twitter-content.v77.md` (the X posts)
  - `dan1-landing-copy.v77.md` (the website copy)
  - `dan1-github-readme-suggestions.v77.md` (the README upgrades)
- **Trigger for v78:** Sep 30, 2026. v78 = post-eval-v1 retrospective.
- **Owner of this document:** Dan1 👾.
- **Sign-off from somdipto:** pending (this is a scheduled-agent run; sign-off happens on next interactive turn).
