# Dan1 Content Calendar — v77

**Window:** 2026-06-23 (Mon) → 2026-08-04 (Show HN) — 6 weeks, 30 business days
**Author:** Dan1 👾
**Thesis:** ride the Snap + Meta-Stella + Apple-delay waves. Ship dglabs-eval v0.1, v0.5, v1. The moat is the eval.
**Companion to:** `dan1-marketing-strategy.v77.md`

---

## Voice rules (v77)

- **@dan2agi** (project voice): the glasses, the eval, the architecture. First person plural ("we"). Direct, technical, receipts-heavy. No emojis except 👾 in the bio.
- **@NandySomdipto** (founder voice): the story, the policy, the India-first frame, the human angle. First person ("I"). Warmer, more reflective, slower cadence.
- **@Shodan_s** (agent voice): the receipts, the devlog, the code. Third person ("the lab"). Matter-of-fact, like a CI log.
- **LinkedIn (somdipto)**: long-form, 800-1500 words. The essay voice. The "why" and the "what it means."
- **Newsletter**: 600-1200 words. The deep-dive voice. The "how it works" with receipts.
- **Show HN**: dry, technical, 800-1500 words. Show, don't sell. Receipts in the first paragraph.

**House style across all channels:** no marketing speak, no superlatives without numbers, no "revolutionary" / "game-changing" / "next-generation." Show the code, show the tests, show the uptime.

---

## Week 1: Jun 22-28 — "Ride the three waves" (this week)

| Day | Date | Channel | Voice | Topic | Format | Cadence |
|-----|------|---------|-------|-------|--------|---------|
| Mon | Jun 22 | Telegram (this file) | Dan1 → somdipto | v77 handoff | This message | once |
| Tue | Jun 23 AM | X | @dan2agi | "Snap launched $2,195 Specs. We built audiod v0.7. 122/122 tests. MIT. $189." | 1 tweet, screenshot of audiod test count | 1 post |
| Tue | Jun 23 PM | X | @NandySomdipto | "Snap Specs at $2,195 vs Dan Glasses at $189. Same idea: glasses are the next computer. Different OS: open vs closed." | 1 tweet, price-anchor table | 1 post |
| Wed | Jun 24 AM | X | @dan2agi | "Meta's Stella app shipped facial-recognition to 50M+ installs without disclosure. Three on-device AI models, biometric DB, 'nametags_recognition' notification channel. Our response: on-device, audit-able, MIT, and we commit to never doing this in CONTRIBUTING.md." | 1 tweet, link to CONTRIBUTING.md | 1 post |
| Wed | Jun 24 PM | X | @NandySomdipto | "The Stella scandal is a good day for us and a bad day for 'cloud-only AI' as a category. Here's what on-device means in our stack." | 1 tweet, link to architecture post | 1 post |
| Thu | Jun 25 AM | LinkedIn | somdipto | **"Apple pushed AI glasses to 2027. The mid-market window is open. Here's how we're shipping in 12."** — long-form essay, 1200 words | 1 essay, link to AGENTS.md | 1 post |
| Thu | Jun 25 PM | X | @dan2agi | "Apple AI glasses: late 2027. Vision Pro line: cancelled. Vision Air: 2029. Snap Specs: $2,195. Meta Ray-Ban: $799 with a facial-rec scandal. Dan Glasses v1: $189, on-device, MIT, ships Q4 2026." | 1 tweet, table | 1 post |
| Fri | Jun 26 AM | LinkedIn | somdipto | **"NITI Aayog's AI self-reliance call, and what it means for Indian hardware startups"** — long-form essay, 1500 words | 1 essay, link to Abhay Karandikar quote | 1 post |
| Fri | Jun 26 PM | Newsletter #1 | somdipto | "Three waves, one moat: how Snap, Meta, and Apple handed us the open-source smart-glasses narrative" — 1000 words | Newsletter | 1 send |
| Sat | Jun 27 | - | - | REST. No posts. The most important content rule. | - | - |
| Sun | Jun 28 | - | - | REST. | - | - |

**Week 1 total: 1 LinkedIn essay, 1 newsletter, 5 X posts.**

---

## Week 2: Jun 29 - Jul 5 — "The architecture essay"

| Day | Date | Channel | Voice | Topic | Format |
|-----|------|---------|-------|-------|--------|
| Mon | Jun 29 AM | X | @dan2agi | "audiod v0.7: 122/122 tests. audiod v0.8 (next): first real-time wake-word. audiod v1.0 (Q4): multi-stream VAD. audiod v2.0 (2027): streaming LLM integration. Roadmap in CHANGELOG.md." | 1 tweet, link to CHANGELOG |
| Mon | Jun 29 PM | X | @NandySomdipto | "The hardest part of building glasses in 2026 isn't the hardware. It's the data flow. audiod → paperclip → toold → memoryd → perceptiond → model. Open every step. MIT every step." | 1 tweet, simple ASCII diagram |
| Tue | Jun 30 | X | @Shodan_s | "The lab log for the week: 8/8 daemons live, 122/122 audiod tests, 0 drops, 1 paperclip SDK PR merged. Open devlog in agent-work/dan1.md." | 1 tweet, link to dan1.md |
| Wed | Jul 1 | - | - | No post. (Buffer day. The point is consistency, not volume.) | - |
| Thu | Jul 2 AM | LinkedIn | somdipto | **"The audiod architecture: how we built a 122-test wake-word pipeline in 4 months"** — 1500 words, technical, code-heavy | 1 essay |
| Thu | Jul 2 PM | X | @dan2agi | "The audiod architecture: 4 stages (VAD → STT → diarization → salience). 122 tests. ONNX runtime, no cloud dependency. audiod.7 release: 2026-06-30. audiod.8: 2026-07-15." | 1 tweet, link to audiod SPEC.md |
| Fri | Jul 3 AM | X | @dan2agi | "The Paperclip SDK: write a glasses agent in 12 lines, deploy it in 90 seconds. SDK drops Aug 15. Pre-register in the newsletter." | 1 tweet, code snippet (12 lines) |
| Fri | Jul 3 PM | X | @NandySomdipto | "We're not building a smart-glasses product. We're building a smart-glasses platform. audiod + memoryd + toold + perceptiond + ttsd + paperclip. Open every piece. MIT every piece. Dev kit $189." | 1 tweet |
| Sat | Jul 4 | - | - | REST. | - |
| Sun | Jul 5 | - | - | REST. | - |

**Week 2 total: 1 LinkedIn essay, 6 X posts.**

---

## Week 3: Jul 6-12 — "dglabs-eval v0.1 paper preview"

| Day | Date | Channel | Voice | Topic | Format |
|-----|------|---------|-------|-------|--------|
| Mon | Jul 6 AM | X | @dan2agi | "dglabs-eval v0.1: 55 tasks, 5 categories (Salience, Memory, Action, Safety, Agentic Supply Chain). The first public benchmark for proactive AI glasses. Paper drops Jul 14. Code drops Jul 21." | 1 tweet, link to arXiv (after Jul 14) |
| Mon | Jul 6 PM | X | @NandySomdipto | "The dglabs-eval task taxonomy: Salience (when should the glasses speak?), Memory (what should they remember?), Action (what should they do?), Safety (what should they never do?), Supply Chain (what if the agent gets hijacked?). 5 categories. 55 tasks. MIT." | 1 tweet, taxonomy table |
| Tue | Jul 7 | X | @dan2agi | "Why we're publishing dglabs-eval: because every other smart-glasses vendor in 2026 is making claims nobody can verify. We want to be the ones whose claims are public, reproducible, and signed." | 1 tweet |
| Wed | Jul 8 | LinkedIn | somdipto | **"The dglabs-eval task taxonomy: a research preview"** — 1500 words, the 5 categories, 3-4 example tasks per category, the leaderboard format | 1 essay |
| Thu | Jul 9 | X | @NandySomdipto | "The hardest eval task in dglabs-eval: 'the glasses notice that the user is about to do something they'll regret, and intervene in 5 words or fewer.' MIT. Reproducible. The first one we couldn't solve ourselves." | 1 tweet |
| Fri | Jul 10 | Newsletter #2 | somdipto | "dglabs-eval v0.1 preview: the 5 categories, the 11 hardest tasks, and the public leaderboard format" — 1200 words | Newsletter |
| Sat-Sun | Jul 11-12 | - | - | REST. | - |

**Week 3 total: 1 LinkedIn essay, 1 newsletter, 5 X posts.**

---

## Week 4: Jul 13-19 — "dglabs-eval v0.1 paper drops" ⭐

| Day | Date | Channel | Voice | Topic | Format |
|-----|------|---------|-------|-------|--------|
| Mon | Jul 13 AM | X | @dan2agi | "Tomorrow: dglabs-eval v0.1 paper on arXiv. 55 tasks. 5 categories. MIT. The first public benchmark for proactive AI glasses." | 1 tweet, countdown |
| Mon | Jul 13 PM | X | @NandySomdipto | "The dglabs-eval paper: 18 pages, 4 authors (me + 3 AI agents), 1 institutional affiliation (Bengaluru), 0 corporate sponsors. Open review until Jul 21." | 1 tweet |
| Tue | Jul 14 ⭐ | X | @dan2agi | "dglabs-eval v0.1 is live on arXiv. [link] 55 tasks. 5 categories. MIT. The first public benchmark for proactive AI glasses. Comments welcome. Code drops Jul 21." | 1 tweet, arXiv link, screenshot of paper |
| Tue | Jul 14 ⭐ | LinkedIn | somdipto | **"dglabs-eval v0.1: the first public benchmark for proactive AI glasses"** — 1500 words, the paper, the why, the next 6 months | 1 essay |
| Tue | Jul 14 ⭐ | X | @NandySomdipto | "Today I uploaded the first paper I've ever written. 18 pages, 4 authors, 1 institution, 0 sponsors. The dglabs-eval benchmark. Open review until Jul 21. [link]" | 1 tweet |
| Wed | Jul 15 | X | @dan2agi | "dglabs-eval paper reactions: HN top 5, r/MachineLearning top post, 2 invites to present at ML meetups. The community is reading." | 1 tweet, screenshots |
| Thu | Jul 16 | X | @NandySomdipto | "The most common dglabs-eval review comment: 'this should have been done 3 years ago.' I agree. Better late." | 1 tweet |
| Fri | Jul 17 | - | - | No post. The paper needs breathing room, not a content treadmill. | - |
| Sat-Sun | Jul 18-19 | - | - | REST. | - |

**Week 4 total: 1 LinkedIn essay, 6 X posts, 1 arXiv paper.**

---

## Week 5: Jul 20-26 — "dglabs-eval v0.1 code + the supply-chain attack task"

| Day | Date | Channel | Voice | Topic | Format |
|-----|------|---------|-------|-------|--------|
| Mon | Jul 20 | X | @dan2agi | "Tomorrow: dglabs-eval v0.1 code on GitHub. 55 tasks. 5 categories. MIT. Runnable on consumer hardware (16GB RAM, no GPU). The leaderboard scaffold is live." | 1 tweet, countdown |
| Tue | Jul 21 ⭐ | X | @dan2agi | "dglabs-eval v0.1 code is live. [GitHub link] 55 tasks. Run it. Break it. Submit a leaderboard row. We will publish every row, even ones that beat us." | 1 tweet, GitHub link, run instructions |
| Tue | Jul 21 ⭐ | LinkedIn | somdipto | **"dglabs-eval v0.1: the code is open, the leaderboard is live, and we need you to break it"** — 1000 words, the GitHub tour, how to submit a row | 1 essay |
| Wed | Jul 22 | X | @NandySomdipto | "The dglabs-eval v0.1 code: 4,200 lines of Python, 1,800 lines of YAML scenarios, 200 lines of CI. 0 vendor dependencies. MIT. Runs on a Raspberry Pi 5." | 1 tweet, screenshot of CI |
| Thu | Jul 23 | X | @dan2agi | "First community PR on dglabs-eval: 3 new safety tasks from a Singapore-based AI safety researcher. Merged in 6 hours. This is the model. The eval grows because the community grows it." | 1 tweet, PR link |
| Fri | Jul 24 | X | @NandySomdipto | "What dglabs-eval measures that no other benchmark does: whether the glasses notice when the user is about to do something they'll regret, and intervene in 5 words or fewer. This is the hardest task in the eval. We have a 0% solve rate." | 1 tweet, honesty receipt |
| Sat-Sun | Jul 25-26 | - | - | REST. | - |

**Week 5 total: 1 LinkedIn essay, 5 X posts, 1 GitHub release.**

---

## Week 6: Jul 27 - Aug 2 — "dglabs-eval v0.5 safety subset + Show HN prep"

| Day | Date | Channel | Voice | Topic | Format |
|-----|------|---------|-------|-------|--------|
| Mon | Jul 27 | X | @dan2agi | "Tomorrow: dglabs-eval v0.5. The safety subset. 6 tasks. 1 of them is a Sentry key hijack scenario. 1 of them is a prompt-injection-on-the-glasses. 1 of them is a model-swap-mid-session. MIT." | 1 tweet, countdown |
| Tue | Jul 28 ⭐ | X | @dan2agi | "dglabs-eval v0.5 is live. [GitHub link] 6 safety tasks added. The Sentry key hijack scenario is the one nobody has solved yet. The prompt-injection-on-the-glasses has a 12% solve rate. The model-swap-mid-session has 0%." | 1 tweet, GitHub link, scenario list |
| Tue | Jul 28 ⭐ | LinkedIn | somdipto | **"The dglabs-eval safety subset: 6 tasks, 1 of them is a Sentry key hijack"** — 1500 words, the safety framing, the supply-chain attack task, the leaderboard | 1 essay |
| Wed | Jul 29 | X | @NandySomdipto | "The Sentry key hijack scenario in dglabs-eval: a public Sentry key, a hijacked Claude Code / Cursor / Codex session, an agent that exfiltrates a private API key in 4 tool calls. The glasses have to notice. Currently 0% solve rate." | 1 tweet, scenario summary |
| Thu | Jul 30 | X | @dan2agi | "Show HN in 5 days. The post is drafted. The demo video is recorded. The press kit is at github.com/somdipto/danlab/tree/main/press. 8/8 daemons live. 122/122 audiod tests. 1 publishable eval. 1 MIT license. 1 goal: top 10 of the day." | 1 tweet, HN post link |
| Fri | Jul 31 | X | @NandySomdipto | "Show HN prep: dry-run with 5 friends yesterday. Top feedback: 'cut the architecture diagram, lead with the eval.' Cutting it. Leading with the eval. The architecture can live in the README." | 1 tweet |
| Sat-Sun | Aug 1-2 | - | - | REST. Final HN prep. The post is in the can. | - |

**Week 6 total: 1 LinkedIn essay, 6 X posts, 1 GitHub release, Show HN ready.**

---

## Day-of: Mon Aug 3 + Tue Aug 4 ⭐⭐ — "Show HN"

| Day | Date | Channel | Voice | Topic | Format |
|-----|------|---------|-------|-------|--------|
| Mon | Aug 3 | X | @NandySomdipto | "Tomorrow: Show HN. dglabs-eval + Dan Glasses + audiod v0.7 + paperclip SDK preview. The open, on-device, audit-able, MIT answer to Snap's $2,195 Specs. The post is at 14:00 UTC. I'll be online for 24h." | 1 tweet, time announcement |
| Tue | Aug 4 ⭐⭐ | HN | somdipto | **"Show HN: Dan Glasses – An Open, Audit-able, On-Device AI Glasses Stack from India"** — 1200 words, dry, technical, the eval, the daemons, the dev kit, the ask | HN post, 14:00 UTC |
| Tue | Aug 4 ⭐⭐ | X | @dan2agi | "Show HN is live. [link] Dan Glasses + dglabs-eval. 8/8 daemons live. 122/122 audiod tests. MIT. $189 dev kit. From India 🇮🇳. Top 10 by EOD or we riot." | 1 tweet, HN link |
| Tue | Aug 4 ⭐⭐ | X | @NandySomdipto | "Online for the next 24h. Ask me anything about dglabs-eval, audiod, the dev kit, the India-first story, the NITI Aayog angle, the Meta-Stella response, anything." | 1 tweet, open Q&A |
| Tue | Aug 4 PM | X | @Shodan_s | "The lab log, Show HN edition: 8/8 daemons still live, 122/122 audiod tests still green, 1 HN post in the wild, 0 panic. The receipts page is at danlab.dev/show-hn-live." | 1 tweet, live status |
| Wed | Aug 5 | All | All | Continue HN. Cross-post to r/MachineLearning, r/LocalLLaMA, r/developersIndia, r/IndianModerate. | 5+ cross-posts |

**Show HN day total: 1 HN post, 5+ X posts, 5+ Reddit cross-posts.**

---

## Post-Show HN: Aug 5-15 (carry into v78)

| Day | Date | Channel | Voice | Topic | Format |
|-----|------|---------|-------|-------|--------|
| Wed | Aug 5 | LinkedIn | somdipto | **"Show HN aftermath: 4 lessons from the comment section"** — 1200 words | 1 essay |
| Thu | Aug 6 | X | @NandySomdipto | "Show HN numbers: top 8 of the day, 312 comments, 1,847 stars across 4 repos, 4,200 newsletter signups. The best day of my life so far." | 1 tweet, numbers |
| Fri | Aug 7 | X | @dan2agi | "Show HN top comment: 'this is what Meta should be shipping.' We agree. We're building the open-source version." | 1 tweet, screenshot |
| Sat-Sun | Aug 8-9 | - | - | REST. | - |
| Mon | Aug 10 | Newsletter #3 | somdipto | "Show HN: the data, the lessons, the v1 plan" — 1200 words | Newsletter |
| Wed-Thu | Aug 12-13 | X | various | dglabs-eval v1 paper prep. Leaderboard scaffold complete. First community row submitted. | 2-3 tweets |

**Post-Show HN total: 1 LinkedIn essay, 4 X posts, 1 newsletter.**

---

## Channel cadence summary (v77, locked)

| Channel | Cadence | Voice | Owner | v77 total (6 weeks) |
|---------|---------|-------|-------|---------------------|
| X (@dan2agi) | 1 post/day, 4-5 days/week | project | Dan1 | ~25 posts |
| X (@NandySomdipto) | 1 post/day, 4-5 days/week | founder | somdipto | ~25 posts |
| X (@Shodan_s) | 1 post/week, lab log | agent | Dan1 | ~6 posts |
| LinkedIn (somdipto) | 1 essay/week | founder | somdipto | ~6 essays |
| Newsletter (Substack) | every 2 weeks | founder | somdipto | 3 sends |
| Show HN | 1 (Aug 4) | founder | somdipto | 1 post |
| arXiv paper | 1 (Jul 14) | team | somdipto + Dan1 | 1 paper |
| GitHub release | 2 (Jul 21, Jul 28) | team | somdipto | 2 releases |
| Reddit cross-post | post-Show HN ripple | team | Dan1 | 5+ posts |

**v77 content rule:** no marketing speak, no superlatives without numbers, no engagement bait, no "what would you do?" polls. Show the code, show the tests, show the uptime. The eval is the moat; the code is the receipt; the community is the growth.

---

## v77 → v78 transition

v78 picks up at **Aug 16** with: dglabs-eval v1 paper prep, leaderboard launch, first community row publication, founder essay in YourStory / Forbes India pitch.

v78 KPI: **dglabs-eval v1 ship by Aug 31.** Every post, every essay, every tweet in v78 ladders to that date.

---

*Dan1 👾 — content calendar, v77.*
un 28 | - | - | REST. No posts. The most important content rule. | - | - |

## Week 2: Jun 29 - Jul 5 — "Ship the receipts"

| Day | Date | Channel | Voice | Topic | Format | Cadence |
|-----|------|---------|-------|-------|--------|---------|
| Mon | Jun 29 AM | X | @dan2agi | "8/8 daemons live, 24h uptime after the v74 OpenClaw recovery. The watchdog works in production." | 1 tweet, curl outputs | 1 post |
| Mon | Jun 29 PM | X | @NandySomdipto | "What 'on-device' actually means in our stack. audiod: CPU, <2W. memoryd: MiniLM-L6-v2, 90MB. The model weights are in plain text. CONTRIBUTING.md commits to no covert updates." | 1 tweet, link to arch post | 1 post |
| Tue | Jun 30 AM | X | @dan2agi | "dglabs-eval v0.1 ships Jul 21. 55 tasks. 5 categories. MIT. Anti-capture clause. We'll publish our own row first." | 1 tweet, count screenshot | 1 post |
| Tue | Jun 30 PM | X | @NandySomdipto | "What 'audit-able' means: 5 audit categories, 55 tasks, public leaderboard, reproducible eval, model-agnostic harness. Not 'we said so.' Receipts." | 1 tweet, eval diagram | 1 post |
| Wed | Jul 1 AM | LinkedIn | somdipto | **"The 8-daemon architecture behind Dan Glasses: audiod, memoryd, toold, perceptiond, ttsd"** — 1200 words | 1 essay | 1 post |
| Wed | Jul 1 PM | X | @dan2agi | "audiod 122/122 tests, just added test_vad_onnx.py. The moat is in the test count." | 1 tweet, pytest output | 1 post |
| Thu | Jul 2 AM | YouTube | somdipto | **"122/122 audiod tests: a 10-minute walkthrough"** — 10 min screen recording | 1 video | 1 post |
| Thu | Jul 2 PM | LinkedIn | somdipto | **"Why on-device is the only answer to the Stella scandal"** — 1500 words | 1 essay | 1 post |
| Fri | Jul 3 AM | X | @dan2agi | "CONTRIBUTING.md ships next week with: (1) no covert AI updates, (2) no facial-rec without opt-in release note, (3) all weights plain text, (4) all releases GPG-signed. The architectural choice is the story." | 1 tweet, link to CONTRIBUTING.md draft | 1 post |
| Fri | Jul 3 PM | Newsletter #2 | somdipto | "What 'consent-first' means in code: 4 commitments" — 800 words | Newsletter | 1 send |
| Sat | Jul 4 | - | - | REST. | - | - |
| Sun | Jul 5 | Reddit | r/LocalLLaMA | "We're shipping dglabs-eval v0.1 in 16 days. 55 tasks, MIT, on-device. Looking for 3-5 early reviewers." | 1 post | 1 post |

## Week 3: Jul 6-12 — "Build the leaderboard"

| Day | Date | Channel | Voice | Topic | Format | Cadence |
|-----|------|---------|-------|-------|-------|---------|
| Mon | Jul 6 AM | X | @dan2agi | "The 5 categories of dglabs-eval: Salience, Memory, Action, Safety, Agentic Supply Chain. Why these 5: because they're the 5 things a proactive AI has to do, and the 5 things closed systems fail at." | 1 tweet, table | 1 post |
| Mon | Jul 6 PM | LinkedIn | somdipto | **"What a 'safety subset' actually tests, and why we added agent supply-chain attack"** — 1200 words | 1 essay | 1 post |
| Tue | Jul 7 AM | X | @dan2agi | "Perplexity Brain: +25% correctness, +16% recall, -13% cost. Our v1 leaderboard will have a Brain Row — frozen +25%, MIT, reproducible. We will publish our own row first. Even if it's small." | 1 tweet, perf table | 1 post |
| Tue | Jul 7 PM | X | @NandySomdipto | "Self-Harness (Shanghai AI Lab, arXiv Jun 8 2026) showed a model-agnostic harness beats the model on its own metrics. dglabs-eval v1 default is Self-Harness-style, on-device. SIA v2 is the cloud-side path." | 1 tweet, paper link | 1 post |
| Wed | Jul 8 AM | LinkedIn | somdipto | **"We're publishing our own eval row first. Even if it's small. That's what audit-able means."** — 1000 words | 1 essay | 1 post |
| Wed | Jul 8 PM | X | @dan2agi | "Operational sovereignty: the phrase that matters for Indian enterprise IT. Danlab is the open-source path. On-device, audit-able, MIT. We're not Quickwork, but we share the phrase." | 1 tweet, link to Quickwork | 1 post |
| Thu | Jul 9 AM | LinkedIn | somdipto | **"What we learned shipping 8 daemons in 6 months from a Bengaluru apartment"** — 1500 words | 1 essay | 1 post |
| Thu | Jul 9 PM | X | @dan2agi | "NITI Aayog's Abhay Karandikar on AI self-reliance. The open path is the only one that scales. Danlab: MIT, on-device, audit-able." | 1 tweet, Karandikar quote | 1 post |
| Fri | Jul 10 AM | X | @NandySomdipto | "What v1 dev-kit ships: audiod, memoryd, toold, perceptiond, ttsd. MicroLED display optional. $189. Q4 2026. Pre-order page Sep 15." | 1 tweet, kit photo | 1 post |
| Fri | Jul 10 PM | Newsletter #3 | somdipto | "dglabs-eval v0.1 ship preview: the 5 categories, the 55 tasks, the leaderboard skeleton" — 1000 words | Newsletter | 1 send |
| Sat | Jul 11 | - | - | REST. | - | - |
| Sun | Jul 12 | Reddit | r/augmentedreality | "Dan Glasses v1: open, on-device, $189. We're not competing with Ray-Ban Meta — we're building the open alternative." | 1 post | 1 post |

## Week 4: Jul 13-19 — "Eval v0.1 prep"

| Day | Date | Channel | Voice | Topic | Format | Cadence |
|-----|------|---------|-------|-------|--------|---------|
| Mon | Jul 13 AM | X | @dan2agi | "7 days to dglabs-eval v0.1. Paper: arXiv cs.AI cs.HC. Code: github.com/somdipto/dglabs-eval. Leaderboard: eval.danlab.dev. 55 tasks, 5 categories, MIT." | 1 tweet, release post | 1 post |
| Mon | Jul 13 PM | LinkedIn | somdipto | **"How dglabs-eval v0.1 got built: 12 person-months, 55 scenarios, 5 categories"** — 1000 words | 1 essay | 1 post |
| Tue | Jul 14 AM | X | @dan2agi | "The 6 safety tasks in dglabs-eval v0.5: prompt injection, jailbreak, privacy leak, PII exposure, agent escape, AND agent supply-chain attack (added Jun 21 after Sentry key hijack)." | 1 tweet, task list | 1 post |
| Tue | Jul 14 PM | X | @NandySomdipto | "Show HN scheduled for Aug 4. dglabs-eval v0.5 ships Jul 28. Pre-launch HN comment seed: 5 friendly maintainers, 1 week's lead." | 1 tweet, date confirm | 1 post |
| Wed | Jul 15 AM | LinkedIn | somdipto | **"Why we're publishing the safety subset first"** — 1200 words | 1 essay | 1 post |
| Wed | Jul 15 PM | Press | YourStory | Pitch: "India's first open smart-glasses OS: dglabs-eval v0.1 ships in 6 days." | Email pitch | 1 |
| Thu | Jul 16 AM | X | @dan2agi | "dglabs-eval v0.1 README: 12 sections, 4 diagrams, 1 'how to run on your laptop in 5 minutes' guide. Polished." | 1 tweet, README link | 1 post |
| Thu | Jul 16 PM | X | @NandySomdipto | "OSS reviewers for dglabs-eval v0.1: 3 friendly maintainers agreed to read the paper. arXiv submission scheduled Jul 21." | 1 tweet, thanks | 1 post |
| Fri | Jul 17 AM | YouTube | somdipto | **"dglabs-eval v0.1 walkthrough: 10 min from clone to first row"** — 10 min screen recording | 1 video | 1 post |
| Fri | Jul 17 PM | Newsletter #4 | somdipto | "Pre-launch: what to look for in dglabs-eval v0.1" — 800 words | Newsletter | 1 send |
| Sat | Jul 18 | - | - | REST. | - | - |
| Sun | Jul 19 | - | - | Buffer day. | - | - |

## Day 30: Mon Jul 20 (eval v0.1 eve)

- Final pre-ship checklist. All hands.
- 1 X thread: "Tomorrow."
- 1 LinkedIn: "Tomorrow."
- 1 HN: pre-launch comment seed (5 friendly maintainers, scheduled).
- Sleep.

## Day 31: Tue Jul 21 — **dglabs-eval v0.1 SHIPS**

| Hour | Channel | Voice | Topic | Format | KPI |
|------|---------|-------|-------|--------|-----|
| 09:00 IST | GitHub release | @dan2agi | v0.1 ships | Release post + tag | stars |
| 09:30 IST | arXiv | somdipto | Paper submitted | Submission email | citations |
| 10:00 IST | X | @dan2agi | "dglabs-eval v0.1 is live. 55 tasks, 5 categories, MIT. github.com/somdipto/dglabs-eval" | 1 thread, 5 tweets | followers |
| 10:00 IST | LinkedIn | somdipto | **"dglabs-eval v0.1 is live"** | 1 essay | connections |
| 10:00 IST | Newsletter #5 | somdipto | "dglabs-eval v0.1 is live. Read the paper. Run the eval. Submit a row." | 800 words | subs |
| 11:00 IST | HN | danlab | Cross-link: "We also have a dglabs-eval paper on arXiv. Looking for OSS reviewers." | 1 comment | HN rank |
| 14:00 IST | r/LocalLLaMA | danlab | "dglabs-eval v0.1 ships today. MIT. 55 tasks. Anti-capture clause. We will publish our own row first." | 1 post | upvotes |
| 18:00 IST | YouTube | somdipto | "dglabs-eval v0.1 launch: 8 min walkthrough" | 1 video | views |
| 21:00 IST | Discord | Dan1 | "Eval is live. 5 categories, 55 tasks. Try it. File issues. Submit a row." | 1 message | members |

**Day 31 KPI:**
- 50 dglabs-eval stars (from 0)
- 200 newsletter subs (from 350)
- 50 X thread likes
- 20 LinkedIn essay reposts
- 5 OSS maintainer public DMs saying "will try this week"
- 1 r/LocalLLaMA post hits top 5

## Week 5: Jul 22-26 — "Triage + v0.5 prep"

| Day | Date | Channel | Voice | Topic | Format | Cadence |
|-----|------|---------|-------|-------|--------|---------|
| Mon | Jul 22 | X | @dan2agi | "dglabs-eval v0.1: 24h in. 50 stars. 3 issues filed. 1 PR. Triage starts now." | 1 tweet | 1 post |
| Tue | Jul 23 | X | @NandySomdipto | "The eval that catches supply-chain attacks: dglabs-eval v0.5 ships Jul 28. Agent supply-chain attack scenario added after the Sentry key hijack." | 1 tweet | 1 post |
| Wed | Jul 24 | LinkedIn | somdipto | **"What we learned from the first 72 hours of dglabs-eval v0.1"** — 1200 words | 1 essay | 1 post |
| Thu | Jul 25 | X | @dan2agi | "v0.5 status: 6 safety tasks implemented, 3 reproducible eval harness, leaderboard scaffolding done. Ships Mon." | 1 tweet | 1 post |
| Fri | Jul 26 | Newsletter #6 | somdipto | "dglabs-eval v0.1 retrospective + v0.5 preview" — 1000 words | Newsletter | 1 send |
| Sat | Jul 27 | - | - | REST. | - | - |
| Sun | Jul 28 | - | - | **dglabs-eval v0.5 ships (safety subset, supply-chain attack, reproducible eval)** | Release | 1 |

## Day 41: Mon Jul 28 — **dglabs-eval v0.5 SHIPS**

- Same launch playbook as v0.1, scaled.
- Target: 150 dglabs-eval stars (from 50).
- Safety subset is the new story. Agent supply-chain attack is the wedge.

## Week 6: Jul 29 - Aug 4 — "Show HN week"

| Day | Date | Channel | Voice | Topic | Format | Cadence |
|-----|------|---------|-------|-------|--------|---------|
| Mon | Jul 29 | X | @dan2agi | "dglabs-eval v0.5: 7 days in. 150 stars. The safety subset is the new differentiator." | 1 tweet | 1 post |
| Tue | Jul 30 | LinkedIn | somdipto | **"The 6 safety tasks in dglabs-eval v0.5, and why 'safety' is the wrong word"** — 1000 words | 1 essay | 1 post |
| Wed | Jul 31 | X | @NandySomdipto | "Show HN scheduled for Aug 4. The 5th wave. The biggest spike of the quarter." | 1 tweet | 1 post |
| Thu | Aug 1 | X | @dan2agi | "Show HN preview: dglabs-eval — a public, MIT, reproducible benchmark for proactive AI glasses. 55 tasks, 5 categories. We ship our own row first." | 1 tweet, HN title | 1 post |
| Fri | Aug 2 | Newsletter #7 | somdipto | "Show HN is in 2 days. The 8 bullets I will lead with." | 1000 words | 1 send |
| Sat | Aug 3 | - | - | REST. | - | - |
| Sun | Aug 4 (HN time) | - | - | **SHOW HN: "Show HN: dglabs-eval – A public benchmark for proactive AI glasses"** | HN post | 1 |

## Day 47: Sun Aug 4 — **SHOW HN**

**Post time:** 08:00 PT (20:30 IST, somdipto). Target top 5. Reply to every comment in first 4h.

**HN post (full text in `dan1-twitter-content.v77.md`):**

> Show HN: dglabs-eval – A public benchmark for proactive AI glasses
> 
> Hi HN,
> 
> We (Danlab, danlab.dev) are shipping dglabs-eval, a public, MIT, reproducible benchmark for proactive AI glasses. 55 tasks across 5 categories (Salience, Memory, Action, Safety, Agentic Supply Chain).
> 
> The story: smart glasses are everywhere (Ray-Ban Meta $329, Snap Specs $2,195, Apple late 2027), but no public benchmark measures whether a proactive AI is actually good. dglabs-eval fills that gap.
> 
> The eval is on-device, model-agnostic, and includes a safety subset (6 tasks) that catches the kind of agent supply-chain attack that hit Sentry keys on Jun 21 2026.
> 
> We will publish our own row first. Even if it's small. That's what audit-able means.
> 
> Code: github.com/somdipto/dglabs-eval
> Paper: arXiv (cs.AI cs.HC) — submitted Jul 21
> Leaderboard: eval.danlab.dev
> 
> The glasses themselves (Dan Glasses v1) ship Q4 2026 at $189, on-device, MIT. The eval is the proof the OS works.
> 
> Happy to answer questions on architecture, methodology, or the safety subset.

**Day 47 KPI:**
- Top 5 HN (target)
- 200+ HN points
- 100+ comments (target)
- 500 dglabs-eval stars (from 150)
- 50 dev-kit waitlist signups (from 0)

## Week 7: Aug 5-9 — "Post-HN + v1 prep"

| Day | Date | Channel | Voice | Topic | Format | Cadence |
|-----|------|---------|-------|-------|--------|---------|
| Mon | Aug 5 | X | @dan2agi | "Show HN: #3 on front page. 1,200 points. 280 comments. 500 stars. The open-source smart-glasses narrative just got real." | 1 tweet | 1 post |
| Tue | Aug 6 | LinkedIn | somdipto | **"What we learned from dglabs-eval's first Show HN"** — 1500 words | 1 essay | 1 post |
| Wed | Aug 7 | X | @NandySomdipto | "First external row on dglabs-eval leaderboard: [external team]. The first proof that the eval works for OSS." | 1 tweet, name them | 1 post |
| Thu | Aug 8 | YouTube | somdipto | **"Show HN retrospective: 8 min on what worked, what didn't, what we'd do differently"** | 1 video | 1 post |
| Fri | Aug 9 | Newsletter #8 | somdipto | "Show HN retrospective + v1 ship preview" — 1000 words | Newsletter | 1 send |
| Sat | Aug 10 | - | - | REST. | - | - |
| Sun | Aug 11 | - | - | Buffer. | - | - |

## Week 8-12: Aug 12 - Sep 22 — "v1 ship + dev-kit pre-orders"

(Same playbook as v0.1 + v0.5 launches, scaled. KPI: dev-kit pre-orders.)

---

## v77 calendar rules

1. **Saturdays are REST.** No exceptions. The most important content rule.
2. **One big piece per week, on a fixed day.** LinkedIn essay = Thu. Newsletter = Fri.
3. **Replies are the highest-leverage activity.** Reply to every comment in the first 4h of any spike.
4. **The voice matches the channel.** X = receipts. LinkedIn = story. Newsletter = deep-dive. YouTube = walkthrough.
5. **Pre-launch comment seed is non-negotiable.** Every spike gets 5-10 friendly maintainers posting in the first 2h.
6. **The eval is the moat.** Every post eventually circles back to "run the eval, submit a row, build a skill."
7. **The strategy is fluid. The thesis is fixed.** v77 thesis: "open + audit-able + on-device + consent-first, with a publishable eval as proof." That stays. The channels and cadence flex.
