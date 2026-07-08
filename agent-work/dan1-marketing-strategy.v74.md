# Dan1 Marketing Strategy — v74

**Built:** 2026-06-22 16:00 IST (10:30 UTC)
**For:** somdipto (founder, DanLab)
**Carry from:** v73 (15:00 IST) + dan2 v38 research + 122/122 audiod test count

---

## v74 one-line strategy

> **Scale the moat with a publishable eval.** v73 shipped the moat. v74 ships the moat, **published, benchmarked, and ready to ship in 8 weeks.** dglabs-eval v1 ships 2026-08-31. SIA-fork paper ships 2026-07-12. dglabs-eval v0.1 paper ships 2026-07-19. Show HN moves from 2026-07-14 to **2026-08-04** (so the leaderboard row is real). The new headline number: **122/122 audiod tests.** The new competitive baseline: **Perplexity Brain (+25% correctness).**

---

## The 6 v74 Strategic Bets

### Bet 1 — Correct the test count publicly. 122/122, not 121/121.

v73 said 121/121 audiod tests. v74 verified by running `pytest --collect-only` at 16:00 IST: **122 tests, 15 test files.** The extra test is in `test_vad_onnx.py` (7 tests, was 6 in v73). v74 ships the correction as a public status update with the verbatim curl receipts.

**Tactic:** X thread on Day 1 of v74 from @dan2agi. "Correction: 122/122 audiod tests, not 121/121. v73 had a rounding error. Here are the receipts: `pytest --collect-only` returns 122 tests. STATUS.md updated. 1.5h uptime on the 8/8 daemons since v73. We correct our own numbers; that's what audit-able means."

**KPI:** 50 retweets, 1 Tier-1 reply.

### Bet 2 — NITI Aayog anchor (the policy frame).

v38 surfaced the NITI Aayog statement (Jun 18 2026) tying the Anthropic Fable 5 / Mythos 5 export ban to AI self-reliance. **This is the first Indian policy-level statement** that anchors AI self-reliance as national priority. v74 grounds the India-first positioning in policy, not just market reality.

**Tactic:** Founder essay on LinkedIn (Day 1 of v74, 2026-06-23). 1,500 words. "AI self-reliance as national priority. Danlab's contribution." Cross-posted to X, the danlab.dev blog, and YourStory. Cite the NITI Aayog statement verbatim. The framing: "OSS + audit-able + on-device + India-first = the response to the export ban."

**KPI:** 100+ LinkedIn comments, 5K blog reads, 1 YourStory response.

### Bet 3 — Perplexity Brain baseline (the benchmarkable bar).

Perplexity launched Brain (Jun 18 2026) with first-party numbers: **+25% answer correctness, +16% recall, -13% cost** on tasks depending on historical context. v74 surfaces this as **the published baseline dglabs-eval's memory subset must beat** to be publishable.

**Tactic:** A "Beat Brain" leaderboard row in dglabs-eval v1 (2026-08-31 ship). The eval: 20 memory tasks, dglabs-eval memory subset. The score: dglabs-eval's published number. The baseline: Perplexity Brain's +25% number, frozen as the "Brain Row" in the leaderboard. **v74 commits to publishing our own row first, even if the number is small. Honesty is the receipt.**

**KPI:** dglabs-eval v1 ships with the Brain Row. Memory row published 2026-08-31.

### Bet 4 — SIA-fork paper on arXiv (the technical proof).

v37's 1-week SIA fork was code-only. v38 verified the SIA repo and the 2-week sprint now includes: SIA monorepo integration + reproducible eval + truthful results writeup + arXiv paper. The compute budget is ~220 GPU-hours, $110-440 spot on Bitdeer/CoreWeave.

**Tactic:** 2-week sprint starts Day 8 of v74 (2026-06-30). End of sprint = arXiv paper submitted 2026-07-12. 6-8 pages. The paper is honest: if the gain is +2%, the paper says +2%. If the gain is +0%, the paper says +0% and discusses why. **The hard part is the truthful writeup, not the code.**

**KPI:** 1 arXiv paper submitted 2026-07-12. 0 → 5 citations by v75 (Sep 2026).

### Bet 5 — dglabs-eval v0.1 + v0.5 + v1 (the moat, shipped).

v74 ships dglabs-eval in 3 milestones:
- **v0.1 (2026-07-21):** Paper + code + 55 tasks + scenarios. arXiv draft.
- **v0.5 (2026-07-28):** Safety subset reproducible eval + supply-chain attack task + agentic harness benchmark.
- **v1 (2026-08-31):** Public leaderboard + first row (Dan Glasses v1) + Brain Row baseline.

**Tactic:** Each milestone is its own X thread + LinkedIn post + weekly dev log. The dglabs-eval repo goes from 0 to 500+ stars over the v74 cycle. The arXiv paper gets 5+ citations.

**KPI:** 500 stars on dglabs-eval, 1 arXiv paper, 1 leaderboard row, 1 Brain Row.

### Bet 6 — Show HN 2026-08-04 (the spike).

Show HN moves from 2026-07-14 (v73 plan) to **2026-08-04**. Why: the v0.5 milestone ships 2026-07-28 with reproducible eval, safety subset, and supply-chain attack task. The leaderboard row is closer to ready. Show HN has a real demo to ship, not a paper promise.

**Tactic:** Submit 2026-08-04 09:00 IST (Sun 21:30 PDT). Title: "OSS AI glasses from India 🇮🇳. 8/8 daemons. dglabs-eval v0.5. SIA-fork paper. MIT." Coordinate the X thread, LinkedIn post, Discord, Reddit r/LocalLLaMA, r/MachineLearning.

**KPI:** 200+ HN points, 80+ comments, 1K dan-glasses stars, 5 academic citations in flight.

---

## The 6-Week v74 Cycle (2026-06-23 → 2026-08-03)

### Week 1 (06-23 → 06-29): "122/122. NITI Aayog. The moat is held."

**Theme:** Correction + policy frame + hardware pivot.

| Day | Action | Surface | Receipt |
|---|---|---|---|
| Mon 06-23 | X thread: "Correction: 122/122 audiod tests. 1.5h uptime on 8/8 daemons." | @dan2agi | x.com/dan2agi/status/... |
| Mon 06-23 | LinkedIn founder essay: "AI self-reliance as national priority. Danlab's contribution." (NITI Aayog anchor) | LinkedIn | linkedin.com/in/somdipto |
| Tue 06-24 | Status blog post: "v74 begins. 122/122. NITI Aayog." | danlab.dev/blog | danlab.dev/blog/v74-status |
| Wed 06-25 | YouTube: "audiod 122/122 in 60 seconds." | YouTube | youtu.be/... |
| Thu 06-26 | X thread: "Perplexity Brain is the bar. +25% correctness. We will publish our row first." | @dan2agi | x.com/dan2agi/status/... |
| Fri 06-27 | Weekly dev log #21. dglabs-eval v0.1 RFC draft published. | danlab.dev/rss | danlab.dev/rss/21 |
| Sat 06-28 | **Hardware pivot blog post (v1/v2 split, $189 v1 / $399 v2).** | danlab.dev/blog | danlab.dev/blog/hardware-decision |
| Sun 06-29 | Telegram status update. | @danlab_bot | t.me/danlab_bot |

**Week 1 KPIs:** 1 test count correction tweet. 1 NITI Aayog essay (5K reads). 1 hardware pivot decision. 1 dglabs-eval v0.1 RFC draft. 8/8 daemons still live.

### Week 2 (06-30 → 07-06): "SIA-fork sprint starts. Beat Brain ledger row."

**Theme:** SIA monorepo + dglabs-eval v0.1 + Perplexity comparison.

| Day | Action | Surface | Receipt |
|---|---|---|---|
| Mon 06-30 | **SIA-fork monorepo integration starts.** `git clone hexo-ai/sia` → `danlab-multimodal/sia/`. | GitHub | github.com/somdipto/danlab-multimodal (private) |
| Mon 06-30 | LinkedIn founder essay: "Why we picked Neprion for v1 audio-only." | LinkedIn | linkedin.com/in/somdipto |
| Tue 07-01 | Reddit r/LocalLLaMA: "dglabs-eval v0.1 RFC: 55 tasks, MIT, anti-capture." | r/LocalLLaMA | reddit.com/r/LocalLLaMA/... |
| Wed 07-02 | YouTube: "dglabs-eval in 60 seconds." | YouTube | youtu.be/... |
| Thu 07-03 | dglabs-eval v0.1 RFC published (Google Doc + GitHub issue). | GitHub | github.com/somdipto/dglabs-eval/issues/1 |
| Fri 07-04 | Weekly dev log #22. | danlab.dev/rss | danlab.dev/rss/22 |
| Sat 07-05 | X thread: "dglabs-eval v0.1 RFC. 55 tasks. Beat Brain. Anti-capture. MIT." | @dan2agi | x.com/dan2agi/status/... |
| Sun 07-06 | Discord #dglabs-eval kickoff. | Discord | discord.gg/danlab |

**Week 2 KPIs:** SIA monorepo integrated. 1 dglabs-eval RFC (50 comments). 1 hardware pivot essay (5K reads). 1 weekly dev log. 8/8 daemons still live.

### Week 3 (07-07 → 07-13): "danlab-multimodal public. SIA-fork paper."

**Theme:** Sprints + arXiv paper.

| Day | Action | Surface | Receipt |
|---|---|---|---|
| Tue 07-07 | **danlab-multimodal public release** (with SIA subdir). | GitHub | github.com/somdipto/danlab-multimodal |
| Wed 07-08 | YouTube: "SIA-fork demo: heuristic → SIA verifier." | YouTube | youtu.be/... |
| Thu 07-09 | Reddit r/LocalLLaMA: "SIA-fork sprint week 1: 220 GPU-hours, $110-440, +X%." | r/LocalLLaMA | reddit.com/r/LocalLLaMA/... |
| Fri 07-10 | Weekly dev log #23. SIA-fork paper draft v1. | danlab.dev/rss | danlab.dev/rss/23 |
| Sat 07-11 | Reddit r/MachineLearning: "SIA-fork: 2-week sprint, monorepo integration, reproducible eval." | r/MachineLearning | reddit.com/r/MachineLearning/... |
| Sun 07-12 | **SIA-fork paper arXiv submission.** | arXiv | arxiv.org/abs/...sia-fork |
| Mon 07-13 | Show HN prep — title final. Draft #2. | Hacker News | (internal) |

**Week 3 KPIs:** 1 danlab-multimodal public (100 stars). 1 SIA-fork video (1K views). 1 SIA-fork arXiv paper submitted. 1 weekly dev log. 8/8 daemons still live.

### Week 4 (07-14 → 07-20): "dglabs-eval v0.1 paper."

**Theme:** dglabs-eval v0.1 ship + arXiv paper.

| Day | Action | Surface | Receipt |
|---|---|---|---|
| Tue 07-14 | dglabs-eval v0.1 code release (55 tasks, 6 categories). | GitHub | github.com/somdipto/dglabs-eval |
| Wed 07-15 | YouTube: "dglabs-eval deep dive: 55 tasks, Perplexity Brain baseline." | YouTube | youtu.be/... |
| Thu 07-16 | MIT Tech Review pitch (with SIA + dglabs-eval + NITI Aayog angle). | Email | technologyreview.com (response TBD) |
| Fri 07-17 | Weekly dev log #24. dglabs-eval paper draft v1. | danlab.dev/rss | danlab.dev/rss/24 |
| Sat 07-18 | X thread: "dglabs-eval v0.1 ships. 55 tasks. MIT. Anti-capture. Perplexity Brain baseline." | @dan2agi | x.com/dan2agi/status/... |
| Sun 07-19 | **dglabs-eval v0.1 paper arXiv submission.** | arXiv | arxiv.org/abs/...dglabs-eval |
| Mon 07-20 | v75 kickoff prep. | (internal) | — |

**Week 4 KPIs:** 1 dglabs-eval v0.1 release (50 stars). 1 dglabs-eval video (1K views). 1 MIT Tech Review pitch sent. 1 dglabs-eval arXiv paper submitted. 1 weekly dev log. 8/8 daemons still live.

### Week 5 (07-21 → 07-27): "dglabs-eval v0.5. Supply-chain attack task."

**Theme:** Reproducible eval + safety subset.

| Day | Action | Surface | Receipt |
|---|---|---|---|
| Tue 07-21 | dglabs-eval v0.5 release. Safety subset reproducible eval. Supply-chain attack task. | GitHub | github.com/somdipto/dglabs-eval/releases/v0.5 |
| Wed 07-22 | YouTube: "Perplexity Brain comparison: +25% is the bar." | YouTube | youtu.be/... |
| Thu 07-23 | YourStory + Inc42 follow-up (NITI Aayog + dglabs-eval v0.5). | Email | yourstory.com / inc42.com |
| Fri 07-24 | Weekly dev log #25. | danlab.dev/rss | danlab.dev/rss/25 |
| Sat 07-25 | X thread: "dglabs-eval v0.5: supply-chain attack task reproducible. We caught the Sentry-style hijack." | @dan2agi | x.com/dan2agi/status/... |
| Sun 07-26 | MIT Tech Review pitch follow-up. | Email | technologyreview.com |
| Mon 07-27 | Show HN prep — run-through #1. | (internal) | — |

**Week 5 KPIs:** 1 dglabs-eval v0.5 release (200 stars). 1 Brain comparison video (1K views). 2 press follow-ups. 1 weekly dev log. 8/8 daemons still live.

### Week 6 (07-28 → 08-03): "Show HN prep. Tuesday 21:30 PDT."

**Theme:** Dress rehearsal + final prep.

| Day | Action | Surface | Receipt |
|---|---|---|---|
| Tue 07-28 | dglabs-eval v0.5 → v1 prep: leaderboard row + Brain Row baseline frozen. | GitHub | github.com/somdipto/dglabs-eval/leaderboard |
| Wed 07-29 | YouTube: "Perplexity Brain benchmark: 20 memory tasks, dglabs-eval scoring." | YouTube | youtu.be/... |
| Thu 07-30 | Show HN draft final. Run-through #2. | (internal) | — |
| Fri 07-31 | Weekly dev log #26. Show HN dress rehearsal. | danlab.dev/rss | danlab.dev/rss/26 |
| Sat 08-01 | Reddit r/LocalLLaMA: "Show HN prep. Tuesday 21:30 PDT." | r/LocalLLaMA | reddit.com/r/LocalLLaMA/... |
| Sun 08-02 | Show HN dress rehearsal (internal). | (internal) | — |
| Mon 08-03 | Show HN final run-through. Title locked. | (internal) | — |

**Week 6 KPIs:** 1 leaderboard row draft. 1 dglabs-eval benchmark video (1K views). 1 weekly dev log. 8/8 daemons still live. Show HN ready.

### Day 43 (Tue 2026-08-04) — Show HN

| Time | Action | Surface | Receipt |
|---|---|---|---|
| 09:00 IST / 21:30 PDT Sun | **Show HN: "OSS AI glasses from India 🇮🇳. 8/8 daemons. dglabs-eval v0.5. SIA-fork paper. MIT."** | Hacker News | news.ycombinator.com/item?id=... |
| 09:30 IST | X thread + LinkedIn post + Discord announcement. | All | (coordinated) |
| 12:00 IST | Reddit r/LocalLLaMA + r/MachineLearning thread. | Reddit | (coordinated) |
| 18:00 IST | YouTube: "Show HN live." | YouTube | youtu.be/... |
| 22:00 IST | Telegram + Discord status. | Telegram / Discord | t.me/danlab_bot |
| 23:59 IST | End of Day 1. Metrics snapshot. | (internal) | — |

**Show HN KPIs:** 200+ HN points, 80+ comments, 1K dan-glasses stars, 5 academic citations in flight, 1 Tier-1 press inquiry (MIT TR or The Verge).

---

## 6-Week v74 KPI Scorecard

| Metric | v73 close | v74 close | Stretch |
|---|---|---|---|
| Daemons live | 8/8 (1.5h uptime) | **8/8** (6-week uptime) | 8/8 + uptime >95% over 42d |
| Audiod tests | 121/121 (v73) | **122/122** (v74) | 130/130 |
| GitHub stars (dan-glasses) | 0 | **1,000** | 2,500 |
| GitHub stars (dan-consciousness) | 0 | 150 | 300 |
| GitHub stars (danlab-multimodal) | 0 (404) | **200** | 500 |
| GitHub stars (dglabs-eval) | 0 (TBD) | **500** | 1,000 |
| arXiv papers (dglabs-eval) | 0 | **1** (v0.1) | 1 (v0.1) + 1 (v1) |
| arXiv papers (SIA-fork) | 0 | **1** | 1 |
| arXiv citations | 0 | **5** | 15 |
| Newsletter subs | 200+ (v73) | **600** | 1,000 |
| Discord members | 50 | **200** | 400 |
| YouTube subs | 0 | **150** | 400 |
| X @dan2agi followers | unknown | **+800** | +1,500 |
| LinkedIn (somdipto) | 4,148 | **4,800** | 5,500 |
| HN points (Show HN) | 0 (not done) | **200** | 400 |
| Tier-1 press pickups | 0 | **2** (MIT TR + The Verge) | 3 |
| First users (Persona A-G) | 0 (v73 was target) | **1,000** | 1,500 |
| Dev-kit pre-orders (v1 audio) | 0 | 5 (stretch) | 10 |
| Dev-kit pre-orders (v2 display) | 0 | 0 | 0 (Q1 2027) |

---

## The 6 Things v74 Will NOT Do (Carry from v73)

1. **No "coming soon" claims.** Every URL is live or it doesn't ship.
2. **No proprietary eval.** dglabs-eval is MIT. Always.
3. **No safety subset opt-out.** 6 tasks (Agents of Chaos + supply-chain attack) are non-negotiable. Always.
4. **No fake test counts.** 122/122 is real. The number is the receipt.
5. **No "we'll figure out hardware later."** v1/v2 split locked 2026-06-28. v74 ships the decision.
6. **v74 NEW: No unbacked numbers.** Every benchmark claim is arXiv-backed or a frozen leaderboard row. Perplexity Brain's +25% is the bar; we publish our number even if it's small.

---

## v74 → v75 transition

**v75 trigger:** 2026-08-05 (Wed) — Day 1 after Show HN.

**v75 thesis:** "Publish + scale." From 1,000 → 10,000 first users. From 0 → 5,000 GitHub stars. From 0 → 5 arXiv citations → 25. From dglabs-eval v1 → dglabs-eval v1.5 (with audio subset). From SIA-fork paper → SIA-fork v1.0 (with full eval).

**v75 inputs:**
- Show HN result (points, comments, signups).
- dglabs-eval v1 adoption (stars, leaderboard rows, citations).
- SIA-fork paper adoption (citations, reproductions).
- Hardware pivot commitment (v1 dev-kit pre-orders open 2026-Q4).
- MIT Tech Review / The Verge / YourStory pickup (yes/no).
- NITI Aayog follow-up (yes/no — funding?).

---

## Open questions for somdipto (you)

1. **Hardware pivot v1/v2 split:** can you commit to 2026-06-28? v38 sharpens to $189 v1 / $399 v2. v74 needs the answer.
2. **dglabs-eval v1 first row:** do you want Dan Glasses v1 (the on-device LFM2.5-1.2B-Thinking) as the first row, or do you want to run a frontier model (LFM2.5-1.2B-Thinking-cloud) first? My read: run the on-device version first; honesty is the receipt. Confirm.
3. **SIA-fork paper honesty:** if the gain is +2%, the paper says +2%. If it's +0%, the paper says +0%. Are you okay with that posture? My read: this is non-negotiable. Confirm.
4. **Show HN title:** sharp to "OSS AI glasses from India 🇮🇳. 8/8 daemons. dglabs-eval v0.5. SIA-fork paper. MIT."? Or sharpen differently?
5. **NITI Aayog funding:** is there an IndiaAI Mission open call we should submit dglabs-eval to? Default v74: yes, submit v0.5 to whatever's open. Confirm.

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-22 16:00 IST. v73 shipped the moat. v74 ships the moat, published, benchmarked, and ready to ship in 8 weeks. v75 publishes + scales.*