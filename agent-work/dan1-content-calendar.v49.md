# Dan1 Content Calendar — v49

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-16 11:00 IST (05:30 UTC)
**Status:** ✅ Canonical. Supersedes v45 archive. **Calendar locked. Day 0 = the 2h 20min punchlist. Day 1 = first post.**

> One-line rule (unchanged): *The calendar is downstream of the punchlist. Day 0 owns the punchlist. Day 1+ owns the cadence. Don't conflate them.*

---

## 0. The delta from v45 archive

| Element | v45 archive | v49 | Why it matters |
|---|---|---|---|
| Day 0 punchlist (5 items) | Stated, 75 min | **Same 5 items + 6 new repo-rewrite actions (§F, §G, §H, §I, §J, §K, §L of `punchlist-copy-paste.md`) = 12 actions, 2h 20min** | The v45 punchlist missed the repo description/topic rewrites. v49 includes them. |
| Days 1-7 (Foundation Week) | 13 slots | **Same 13 slots, reordered: punchlist first, then thread, then 2 quick-reply windows, then 5-min demo** | Cadence stays. The Day 0 carryover is the bottleneck. |
| Days 8-14 (Cadence Week) | 7 slots | **Same 7 slots + 2 new reactive hooks (Omni-1B, Tushar Shaw)** | New narrative signals. |
| Days 15-21 (Depth Week) | 7 slots | **Same 7 slots + 1 new long-form: "Training the Omni-1B"** | The Omni-1B training is now the lead narrative for the quarter. |
| Days 22-30 (Pull Week) | 8 slots | **Same 8 slots + 1 new long-form: "How we built a 1B Omni for India"** | Same — the model is the moat. |
| Days 31-60 (Conversion) | 6 ship targets | **Same + 2 new: model card on HuggingFace, research blog** | The model is the first public artifact. |
| Days 61-90 (Launch) | 6 ship targets | **Same + 1 new: arXiv preprint on salience-gated vision** | The technical wedge deserves a paper. |
| The 5 content pillars | Proactive / Local / India / Architecture / Build-in-public | **Same 5 + new 6th: "The model" (Omni-1B training)** | 6 pillars, all anchored to the wedge. |
| NEW: Reactive hook bank | 8 triggers | **11 triggers (added: Omni-1B milestone, Percevia ₹10K price, Vibe Glass launches)** | More surface area for reactive content. |
| NEW: Failure modes | 4 | **Same 4, sharpened** | v45 is the architecture. v49 is the discipline. |

### What has not changed (and doesn't need to)
- **The 5-pillar thesis:** Proactive / Local-first / Open source / India / AGI research. Now 6 with "The model."
- **The day-1 thread:** 7-tweet origin thread, copy-paste in `punchlist-copy-paste.md` §D. Locked.
- **The reactive hooks:** all the v45 ones still apply. The new ones (Omni-1B, Percevia) are additions, not replacements.
- **The metric:** GitHub stars. Not impressions. Not followers. Stars.

---

## 1. The Day-0 punchlist (2h 20min, blocks everything)

**12 actions, in order, $0, reversible, owned by somdipto. Text in `punchlist-copy-paste.md`.**

| # | Action | Time | Surface | File ref |
|---|---|---|---|---|
| 1 | `danlab-multimodal` → Public | 30 min | GitHub | §H |
| 2 | X bio + display name swap | 1 min | @NandySomdipto | §A |
| 3 | LinkedIn headline + about | 5 min | somdipto-nandy | §B |
| 4 | GitHub profile: name + bio | 5 min | github.com/somdipto | §F |
| 5 | Profile README (new `somdipto/somdipto` repo) | 10 min | GitHub | §G |
| 6 | Pin 6 repos | 5 min | github.com/somdipto | §G |
| 7 | `dan-glasses` description + 12 topics | 10 min | GitHub | §I |
| 8 | `dani` description + 10 topics | 5 min | GitHub | §J |
| 9 | `paperclip` description + 9 topics | 5 min | GitHub | §K |
| 10 | `dan-consciousness` description + 9 topics | 5 min | GitHub | §L |
| 11 | `openwork` light polish | 5 min | GitHub | §M |
| 12 | Indranil Bhadra quote-tweet + Percevia reply | 30 min | X | §C, §E |

**Total: 2h 20min. $0. Reversible. Owned by somdipto.**

**Optional 30 min: 7-tweet origin thread (separate, ships Day 1). Text in `punchlist-copy-paste.md` §D.**

**The constraint:** somdipto must ship. Dan1 (me) cannot ship from the agent side. The 24-hour deadline from v48 has already lapsed. The new deadline is the next 48 hours. v50 is "the punchlist shipped" or silence.

---

## 2. The 30-day grid (the cadence after Day 0)

### Week 1 (Days 1-7) — Foundation Week

| Day | Channel | Content | Format | Owner | Time |
|---|---|---|---|---|---|
| **Day 1** | X | 7-tweet origin thread (pinned for 7 days) | Thread | somdipto | 30 min |
| **Day 1** | LinkedIn | "We just open-sourced a sub-250MB multimodal AI pipeline" | Long-form | somdipto | 1 hour |
| **Day 2** | X | The receipts: 7 daemons, 106/106 tests | Single + screenshot | somdipto | 30 min |
| **Day 2-3** | YouTube | 5-min demo screencast: PTT → STT → memory → query → TTS | Screencast | somdipto | 4 hours |
| **Day 3** | X + LinkedIn | Demo video post | Video post | somdipto | 30 min |
| **Day 4** | dev.to | "Building Dan Glasses: a 7-service local-first AI stack" | Long-form (2,000 words) | Dan1 draft → somdipto publish | 4 hours |
| **Day 5** | Hacker News | Submit Show HN | Link | somdipto | 1 hour |
| **Day 5** | Reddit | r/LocalLLaMA cross-post | Link | somdipto | 30 min |
| **Day 6** | Reddit | r/india + r/MachineLearning + r/singularity cross-posts | Link | somdipto | 1 hour |
| **Day 6** | X | Reply to 10 AI/ML researchers with substantive comments | Engagement | somdipto | 1 hour |
| **Day 7** | LinkedIn | "From India to the World: why we built Dan Glasses" | Long-form (1,500 words) | somdipto | 3 hours |
| **Day 7** | danlab.dev | Add the LinkedIn long-form as a /blog post with CTAs to GitHub + Telegram | Page | Dan1 | 1 hour |

**Week 1 ship target:** Show HN submitted, dev.to post, LinkedIn long-form, YouTube demo, 20 organic replies.

### Week 2 (Days 8-14) — Cadence Week

| Day | Channel | Content | Format | Owner | Time |
|---|---|---|---|---|---|
| **Day 8** | X | "Week 1 retro — punchlist shipped, what broke, what's next" | Thread | somdipto | 1 hour |
| **Day 8** | dev.to | Cross-post the Week 1 retro | Article | somdipto | 1 hour |
| **Day 9** | dev.to | "Salience-gated vision: why your AI glasses don't need 60 FPS" | Long-form (2,000 words) | Dan1 draft → somdipto publish | 4 hours |
| **Day 10** | X | Outreach to 20 AI/ML researchers (comment + DM, no spam) | Engagement | somdipto | 2 hours |
| **Day 11** | X | Outreach to 10 India tech press / newsletters (YourStory, Inc42, The Pragati, The Signal) | DM | somdipto | 1 hour |
| **Day 12** | Reddit | "What is the missing category in 2026 smart glasses?" (thought-leadership, not plug) | Text | somdipto | 1 hour |
| **Day 13** | Telegram | First weekly retro to the community + roadmap | Text | somdipto | 1 hour |
| **Day 14** | Hacker News | Ask HN: "What should the v2 wearable spec be for open-source AI glasses?" | Text | somdipto | 1 hour |
| **Day 14** | X | Engagement burst: 20 substantive replies on top AI/AR posts of the day | Engagement | somdipto | 1 hour |
| **Day 14** | X | **NEW: Percevia / Tushar Shaw v2 announcement — "we welcome Percevia to local-first"** | Single | somdipto | 30 min |

**Week 2 ship target:** 1 dev.to article, 1 X build-in-public thread, 1 Ask HN, 20 researcher DMs, 10 press DMs, Telegram community live.

### Week 3 (Days 15-21) — Depth Week

| Day | Channel | Content | Format | Owner | Time |
|---|---|---|---|---|---|
| **Day 15** | dev.to | "7 services, 0 cloud calls, $0/month: how we built the local-first AI stack" | Long-form (2,500 words + architecture diagram) | Dan1 draft → somdipto publish | 5 hours |
| **Day 16** | danlab.dev | Rewrite hero with v2 framing (Dan Glasses leads, 3 other products become footer) | Page | Dan1 + somdipto | 4 hours |
| **Day 17** | LinkedIn | "The proactive AI thesis: why we don't ship a display" | Long-form (1,500 words) | somdipto | 3 hours |
| **Day 18** | YouTube | Pitch 5-10 tech reviewers (MKBHD tier unreachable; Mrwhosetheboss / Beebom / tech-altar tier) | DM | somdipto | 2 hours |
| **Day 19** | X | Reactive hook on the Apple WWDC 2026 no-show | Thread | somdipto | 1 hour |
| **Day 20** | X | **NEW: First Omni-1B training milestone thread** (1B params, 3 months in, regional Indian languages) | Thread (5-7 tweets) | somdipto | 2 hours |
| **Day 21** | LinkedIn | "AGI from India: the thesis" | Long-form (1,500 words) | somdipto | 3 hours |

**Week 3 ship target:** 1 dev.to article, 2 LinkedIn long-form, 1 YouTube reviewer pitch wave, 1 Omni-1B thread, danlab.dev v2 hero shipped.

### Week 4 (Days 22-30) — Pull Week

| Day | Channel | Content | Format | Owner | Time |
|---|---|---|---|---|---|
| **Day 22** | dev.to | "Why we run LFM2.5-VL-450M on a $200 board" | Long-form (2,000 words) | Dan1 draft → somdipto publish | 4 hours |
| **Day 23** | Video call | First 5 user interviews (in-person or video) | Conversation | somdipto | 4 hours |
| **Day 24** | Video call | Next 5 user interviews | Conversation | somdipto | 4 hours |
| **Day 25** | arXiv | Preprint: "Salience-gated vision: a low-power perception loop for AI wearables" | Paper | somdipto + Dan1 | 8 hours |
| **Day 26** | GitHub | First community PR (to llama.cpp, whisper.cpp, KittenTTS, or LFM2-VL upstream) | Code | somdipto | 4 hours |
| **Day 27** | X | "Month 1 retro — 100 users, what we learned, what's next" | Thread | somdipto | 2 hours |
| **Day 28** | dev.to | "whisper.cpp <1s end-to-end: the VAD + streaming pipeline" | Long-form (2,000 words) | Dan1 draft → somdipto publish | 4 hours |
| **Day 29** | X Spaces | "Building AI glasses from India" (host or guest) | Live audio | somdipto | 1 hour prep + 1 hour live |
| **Day 30** | All | Recap: 100 users milestone (or honest report) + thank-you post | Multi-channel | somdipto | 2 hours |

**Week 4 ship target:** 2 dev.to articles, 1 arXiv preprint, 1 community PR, 10 user interviews, 1 X Spaces appearance, 100 users milestone (or honest miss).

### Days 31-60 (Conversion Month)

- Waitlist landing page live (ConvertKit / Looms / Tally)
- "Request access" CTA on every blog post and X thread
- **NEW: First Omni-1B model card on HuggingFace** (`somdipto/omni-1b-indic-v0.1`)
- First paying Pro tier (Dan Voice API — voice cloning, custom wake words) if there's demand
- Sponsorship outreach: Indian AI newsletters (The Signal, The Pragati, IndiaAI Dispatch)

**Day 31-60 ship target:**
- [ ] 6 more dev.to articles (1 every 5 days)
- [ ] 1 more arXiv preprint
- [ ] 2 more LinkedIn long-form articles
- [ ] 1,000 GitHub stars across the 4 hero repos
- [ ] 100 waitlist signups
- [ ] **NEW: Omni-1B model card on HuggingFace**
- [ ] First $1k MRR (Pro tier)

### Days 61-90 (Launch Month)

- Product Hunt launch (Tuesday or Wednesday, 12:01 AM PT)
- Tech press pitches: The Verge, Wired India, YourStory, Inc42, The Ken
- Podcast pitches: The Pragmatic Engineer, Latent Space, Last Week in AI, AI + India
- Hacker News "Show HN" with full demo
- **NEW: arXiv preprint on the Omni-1B (Indian languages, 1B params, on-device)**
- First cohort of 100 users onboarded, with weekly office hours

**Day 61-90 ship target:**
- [ ] Product Hunt launch
- [ ] 1 major tech press hit (Verge / Wired / YourStory tier)
- [ ] 1 major podcast (Pragmatic Engineer / Latent Space tier)
- [ ] 10k GitHub stars
- [ ] 10k waitlist signups
- [ ] $5k MRR
- [ ] **NEW: arXiv preprint on Omni-1B**

---

## 3. The 6 content pillars (anchored to the wedge)

1. **The proactive thesis** (Salience-gated vision, why no display) — Days 9, 17
2. **The local-first thesis** (7 services, 0 cloud, $0/month) — Days 15, 28
3. **The from-India thesis** (Origin, AGI from India) — Days 7, 21
4. **The architecture deep-dives** (whisper, salience, orchestration) — Days 9, 22, 28
5. **The build-in-public logs** (Weekly retro) — Days 8, 15, 22, 29
6. **The model thesis (NEW in v49)** (Omni-1B, Indian languages, on-device) — Days 20, 60, 90

---

## 4. The reactive hook bank (armed, not fired)

| Trigger | Hook | Channel | Time to ship |
|---|---|---|---|
| Apple Glasses slip to 2027 (already happened May 31) | "Apple exits. We're shipping. Open source is the answer." | X + LinkedIn | 2 hours |
| Apple WWDC 2026 (already happened June 8) | "Apple shipped a Siri. We shipped a companion." | X + LinkedIn | 2 hours |
| Meta Ray-Ban Display ships to India | "The open-source alternative that runs on $200 hardware" | X + LinkedIn | 3 hours |
| Google audio Android XR glasses ship Fall 2026 | "Gemini is great. But it needs the cloud. Dan Glasses doesn't." | X + LinkedIn | 2 hours |
| Sarvam Kaze hits 10K pre-orders | "Why we still need an open-source AI glasses stack in India" | LinkedIn | 1 hour |
| Lenskart B hits 100K units | "Lenskart proved India wants AI glasses. We proved India can build them open source." | X + LinkedIn | 2 hours |
| LFM2.5-VL-450M ships to HF (already shipped Apr 11) | Demo on Day 1 | X + YouTube | 4 hours |
| SIA v1.0 release | "Partnering with the open-source self-improvement stack" | X + LinkedIn | 3 hours |
| Brilliant Labs Halo ships India | "Open-source soul-mate. Same LFM2-VL. Different body." | X + LinkedIn | 2 hours |
| **NEW: Omni-1B v0.1 ships to HuggingFace** | "1B params, regional Indian languages, on-device. The model is now public." | X + LinkedIn + HF model card | 4 hours |
| **NEW: Tushar Shaw / Percevia hits 1K pre-orders** | "Percevia proved ₹10K is the right price. We proved ₹10K works without the cloud." | X | 1 hour |
| **NEW: Tushar Shaw / Percevia announces v2 with on-device inference** | "We welcome Percevia to the local-first camp. MIT-licensed code for the wedge: github.com/somdipto/dan-glasses" | X | 1 hour |
| **NEW: Vibe Glass launches in India** | "Vibe Glass is the consumer play. Dan Glasses is the developer + AGI-research play. Both valid." | X + LinkedIn | 1 hour |
| **NEW: Lenskart launches "B Pro" with a Chinese OEM** | "Lenskart is the distribution. We're the OS. Same stack, different layers." | X + LinkedIn | 2 hours |
| A big-Twitter AI/India account DMs somdipto | Personal reply, not a thread. Always. | X | 10 min |

---

## 5. The failure modes (what kills the calendar)

1. **The punchlist doesn't ship.** Calendar dead. Ship the punchlist.
2. **We let perfect become the enemy of shipped.** A 1-week landing-page redesign is a bad trade.
3. **We write instead of build.** Every week without a public commit, a public demo, a public post is a week of compounding loss.
4. **We don't engage with the responses.** Every Show HN, every thread, every post needs somdipto's first-hour reply window.
5. **NEW: We let the Omni-1B training be private for too long.** The model is the moat. The first public artifact of the model deserves a HuggingFace card by Day 60.
6. **NEW: We confuse the India AI glasses actors as competitors.** They are not. They are cousins. Tushar Shaw, Lenskart, Sarvam, Vibe Glass — they are all distribution / product plays. We are the only open-source brain play. The wedge is bigger when they grow, not smaller.

---

*End of v49. The calendar is downstream of the punchlist. Day 0 owns the punchlist. Day 1+ owns the cadence. The 6 content pillars, the 4-week foundation cadence, the 90-day plan, the 15 reactive hooks, the 6 failure modes — all locked. Ship the punchlist. Then ship the cadence.*
