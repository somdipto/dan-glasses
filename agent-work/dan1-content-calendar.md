# Dan1 Content Calendar — v66 (canonical)

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 07:30 IST (02:00 UTC)
**Window:** Week 26 (2026-06-23 Mon → 2026-06-29 Sun) + Show HN 2026-06-30, with week 27 preview
**Status:** ✅ Canonical. Supersedes v65.

> **v66 thesis — ride the category wave without claiming it.** The week of 2026-06-16 to 2026-06-19 was the biggest week in smart-glasses history: Snap Specs at $2,195, Google Android XR + Warby Parker + Gemini, Qualcomm Snapdragon Reality Elite, Apple AI AirPods + glasses, Illinois HB4843. The category is confirmed. Week 26 is when we ride that wave with the receipts: audiod v0.7 (Tauri client, 101/101 tests), the 3 public repos, the danlab.dev refresh, the Show HN in the can. Every post is anchored to one of those artifacts. The category doesn't make our claim for us — the receipts do.

## Week 26 — at a glance

| Day | Date | Primary ship | Channel | Asset | Time IST |
|---|---|---|---|---|---|
| Mon | 06-23 | **Push `somdipto/dan-glasses` to public GitHub (v0.7.0-audiod tag)** + **Snap-week price-anchor tweet** | GitHub + X + LinkedIn + Telegram | `v0.7.0-audiod` tag + release notes | 09:00 |
| Tue | 06-24 | **Push `somdipto/danlab-multimodal` to public** + **refresh danlab.dev** | GitHub + X + LinkedIn | `v0.1.0` tag + 2026 homepage | 09:00 |
| Wed | 06-25 | **Reddit r/LocalLLaMA — Snap-week post-mortem** + r/indianstartups | Reddit + X | "Snap $2,195 vs. $300 laptop" post | 09:00 |
| Thu | 06-26 | Flip @danlab_bot to public + HackerNoon draft + Illinois HB4843 thread | Telegram + Medium | channel config + essay draft + compliance thread | 21:00 |
| Fri | 06-27 | **Snap-week post-mortem X thread (7 tweets)** + LinkedIn cross-post | X + LinkedIn | 7-tweet thread | 18:00 |
| Sat | 06-28 | (rest day) | — | — | — |
| Sun | 06-29 | Week-in-review + Show HN prep | LinkedIn + YouTube | 5-min essay + HN post draft | 10:00 |
| Mon | 06-30 | **Show HN: DanClaw Phase 1** | Hacker News | Show HN post (drafted below) | 14:00 PT |

**Daily non-negotiables (all 7 days):**
- 09:00 IST: 1 ship-log tweet (X + Telegram @danlab_bot)
- 09:30 IST: 1 reply to a relevant account (X, LinkedIn, Reddit)
- 23:00 IST: 1 insight saved to backlog (`agent-work/backlog.md`)

**v66 Snap-week additions (week 26 only):**
- **Mon 06-23 09:30 IST:** Snap Specs $2,195 + audiod v0.7 price-anchor tweet.
- **Wed 06-25 09:00 IST:** r/LocalLLaMA post-mortem.
- **Fri 06-27 18:00 IST:** 7-tweet thread: "What Snap's $2,195 Specs means for the open-source alternative."

---

## Monday 06-23 — Push `somdipto/dan-glasses` to public (v0.7.0-audiod) + Snap-week anchor

**Primary deliverable:** Public GitHub release. audiod v0.7.0 ships the **Tauri integration client** (`Services/audiod/client.py` + tests). The Tauri Rust port is a mechanical 1:1 translation. This is the first end-to-end "audiod on the desktop" receipt.

**Pre-flight checklist:**
- [ ] v66 README is in `/home/workspace/dan-glasses/README.md` (see `dan1-github-readme-suggestions.md` v66)
- [ ] `LICENSE` (MIT) at repo root
- [ ] `STATUS.md` with daemon-by-daemon status (audiod v0.7 ✅ with Tauri client, others spec'd)
- [ ] `.github/ISSUE_TEMPLATE/` and `CONTRIBUTING.md` (basic)
- [ ] No secrets, no `.env` files, no `node_modules` committed
- [ ] `Services/audiod/client.py` + `Services/audiod/tests/test_client_*.py` committed
- [ ] SPEC.md bumped to v0.7 with "Client integration" section
- [ ] Tag created: `v0.7.0-audiod`

**Release template:**
```
## v0.7.0-audiod — Tauri Integration Client

### What's Changed
- New: `Services/audiod/client.py` — `AudiodClient` (HTTP + WebSocket).
  - HTTP: start, stop, restart, reload, ptt(on|off), health, status
  - WS: `transcripts()` async iterator with backoff reconnect
  - Zero new system dependencies (stdlib urllib + websockets already in deps)
- New: `tests/test_client_integration.py` — 8+ tests against live audiod
- New: `tests/test_client_unit.py` — 4 stubbed-transport tests (retry + reconnect)
- Bump: SPEC.md → v0.7 with "Client integration" section
- Tauri Rust port sketch documented for the future desktop shell

### Verify
\\`\\`\\`
# Start audiod
python3 Services/audiod/audiod.py

# In another terminal
python3 -c "from Services.audiod.client import AudiodClient; c = AudiodClient(); print(c.health())"
# {\"status\":\"ok\",\"service\":\"audiod\"}

curl http://localhost:8741/health
# {\"status\":\"ok\",\"service\":\"audiod\"}
\\`\\`\\`

### Why it matters
The Tauri shell is the future of the desktop client. The audiod client is the
typed contract the Rust shell will mirror 1:1. Shipping the Python client first
gave us end-to-end integration tests against the live service. The Rust port
becomes a mechanical translation, not a design exercise.

### Known limitations
- Requires Python 3.11+ (no 3.10 backport yet).
- Tauri app build requires Rust ≥ 1.77 (see apps/dan-glasses-app/README).
- Other 6 daemons are spec'd but not yet at audiod's test coverage.

Built at danlab.dev 🇮🇳
```

**Tweet (09:00 IST, also cross-post to @danlab_bot):**
> audiod v0.7 is public. v0.7.0-audiod tag.
>
> The Tauri integration client. Typed HTTP + WebSocket contract for the desktop shell.
>
> - `AudiodClient` (HTTP + WS, stdlib only)
> - 8+ integration tests against live audiod
> - 4 stubbed-transport tests (retry + reconnect)
> - Tauri Rust port = 1:1 mechanical translation
>
> `curl localhost:8741/health` → ok. 101/101 tests. MIT.
>
> github.com/somdipto/dan-glasses 🇮🇳

**LinkedIn (09:30 IST cross-post):**
> audiod v0.7 is now public on GitHub.
>
> The Tauri integration client. The typed contract the desktop shell will mirror 1:1.
>
> - HTTP: start, stop, restart, reload, ptt(on|off), health, status
> - WS: `transcripts()` async iterator with backoff reconnect
> - 8+ integration tests against the live daemon
> - 4 stubbed-transport tests for retry/reconnect
>
> The full daemon stack: audiod + perceptiond + memoryd + ttsd + toold + os-toold + openclawd. MIT. India.
>
> github.com/somdipto/dan-glasses

**v66 Snap-week anchor tweet (09:30 IST, second tweet of the day):**
> Snap just unveiled $2,195 AR glasses with two Snapdragons. Spiegel called it "a new era of computing."
>
> audiod v0.7 is live on a $300 laptop. Same proactive loop. MIT. 101/101 tests.
>
> The category is confirmed. The cost is not. We're the cost.
>
> github.com/somdipto/dan-glasses 🇮🇳

**Reply targets (find at 09:30 IST):**
- @ApoorvSaxena (audio ML)
- @swyx (DX/AI engineering)
- @karpathy (any thread on test methodology)
- @joannastern (NPR tech journalist who covered Snap Specs)

---

## Tuesday 06-24 — Push `somdipto/danlab-multimodal` to public + refresh danlab.dev

**Two deliverables:** public GitHub + 2026 danlab.dev homepage.

**GitHub release for danlab-multimodal:**
```
## v0.1.0 — First public release

### What's in the box
- SmolVLM-256M + mmproj = 302MB combined
- llama.cpp backend, CPU-only
- Heuristic feedback loop (length penalty, error detection, UI element ID)
- Pre-RL scaffold. NOT reinforcement learning. README disclaims.
- Reproducible in 30s: `python3 src/demo.py demo`

### Verify
\\`\\`\\`
git clone https://github.com/somdipto/danlab-multimodal
cd danlab-multimodal
python3 src/demo.py demo
# ~32s per image on a $300 laptop
\\`\\`\\`

### Why
Hackathon-grade MIT project. Anthropic's Jack Clark publicly said recursive
self-improvement is the next step; we wanted an honest pre-RL scaffold
instead of claiming RL we didn't have.

### Post-Snap framing (v66)
Snap just sold $2,195 AR glasses. We ship a 302MB multimodal loop on a $300
laptop. The category is confirmed; the cost is not. We're the cost.

Built at danlab.dev 🇮🇳
```

**danlab.dev refresh — push v66 landing copy:**
- Use the v66 landing copy in `dan1-landing-copy.md`.
- Replace "AI Glasses" with "Dan Glasses."
- Replace Agent8 / Zerant / Dapify section with the 7 daemons table.
- Add the live status strip with audiod v0.7 ports.
- Cross-link to the 3 public GitHub repos.
- Lead with the curl-able health endpoint.
- **v66 new:** add the Snap-week line: "Snap just launched $2,195 AR glasses. Dan Glasses target BOM: $145–180."

**Tweet (09:00 IST):**
> danlab-multimodal is public. v0.1.0.
>
> 302MB combined. SmolVLM-256M + mmproj. ~32s per image on CPU.
>
> \\`\\`\\`
> git clone github.com/somdipto/danlab-multimodal
> cd danlab-multimodal
> python3 src/demo.py demo
> \\`\\`\\`
>
> Pre-RL. Heuristic. MIT. We don't claim RL we don't have.
>
> The category just got $2,195 AR glasses. We ship 302MB on a $300 laptop.
>
> github.com/somdipto/danlab-multimodal

**LinkedIn cross-post (11:00 IST):**
> danlab-multimodal is public today.
>
> The world's smallest working VLM-on-CPU loop. 302MB combined. Pre-RL. Heuristic. MIT.
>
> We don't claim RL we don't have. We built a heuristic feedback scaffold instead, with hand-coded scoring rules, and made the whole thing reproducible in 30 seconds. Hackathon-grade but production-shaped.
>
> This week Snap launched $2,195 AR glasses with two Snapdragons. We ship a 302MB multimodal loop on a $300 laptop. The category is confirmed; the cost is not. We're the cost.
>
> github.com/somdipto/danlab-multimodal

**Reply targets:** @awnihannun, @simonw, @karpathy, @joannastern.

---

## Wednesday 06-25 — Reddit r/LocalLLaMA — Snap-week post-mortem

**Reddit r/LocalLLaMA post (09:00 IST):**
> **Title:** Snap's $2,195 Specs vs. a $300 laptop running danlab-multimodal
>
> **Body:**
>
> \\`\\`\\`
> git clone https://github.com/somdipto/danlab-multimodal
> cd danlab-multimodal
> python3 src/demo.py demo
> \\`\\`\\`
>
> That's the whole thing. SmolVLM-256M + mmproj = 302MB combined. ~32s per image on CPU. Pre-RL heuristic feedback loop (hand-coded scoring, no weights modified — we're explicit it's not RL).
>
> **This week in context:**
> - Snap unveiled Specs at $2,195 with two Snapdragons
> - Google announced Android XR + Warby Parker + Gemini
> - Qualcomm launched Snapdragon Reality Elite for 40+ AI wearables
> - Apple prepping AI AirPods + glasses
>
> The category is confirmed. The cost is not. We're the cost.
>
> danlab-multimodal runs on a $300 laptop with 302MB of weights. Pre-RL. Heuristic. MIT. Reproducible in 30 seconds. Live demo: https://zo.pub/som/danlab-multimodal-demo
>
> If you're building a real RL multimodal pipeline, this is the floor. Fork it. Replace the heuristic with a learned policy. Make it RL.
>
> AMA in thread.

**Reddit r/indianstartups post (09:30 IST):**
> **Title:** Week 26 update — open-sourced 2 repos, danlab.dev refreshed, Snap launched $2,195 Specs
>
> **Body:**
>
> Three years into bootstrapping an AI lab from Bengaluru. This week we shipped:
>
> - **somdipto/dan-glasses** — 7 daemons, audiod v0.7 with 101/101 tests + Tauri client, MIT. The proactive AI companion.
> - **somdipto/danlab-multimodal** — 302MB VLM on CPU, reproducible in 30s. Pre-RL scaffold.
> - **danlab.dev** — refreshed from 2024 to 2026. Live status strip. Real receipts.
>
> And this week the category exploded: Snap Specs at $2,195. Google Android XR + Warby Parker + Gemini. Qualcomm Snapdragon Reality Elite. Apple AI AirPods + glasses.
>
> Three AI glasses out of India this year. Oculosense (offline-only, visually-impaired-focused). Sarvam (cloud-first, government halo). Dan Glasses (MIT + on-device + proactive + India-priced). The only one with all four.
>
> The category is confirmed. The cost is not. We're the cost.
>
> AMA on the indie's path: how we ship weekly, what works, what doesn't.

**Tweet (09:00 IST, also @danlab_bot):**
> 2 repos public this week:
>
> github.com/somdipto/dan-glasses — audiod v0.7 + Tauri client, 7 daemons, MIT
> github.com/somdipto/danlab-multimodal — 302MB VLM on CPU
>
> danlab.dev refreshed from 2024 to 2026.
>
> Snap launched $2,195 Specs. We ship audiod v0.7 with 101/101 tests on a $300 laptop.

**Reply targets (09:30 IST):** @karpathy on any RL thread, @awnihannun on any multimodal thread, @simonw on any local-llama thread.

---

## Thursday 06-26 — Flip @danlab_bot to public + HackerNoon draft + Illinois HB4843 thread

**Telegram channel action:**
- Flip @danlab_bot channel to public.
- Set channel username: `@danlab_dev` (or `@danlab_bot` if username already taken).
- Pin the v66 pinned tweet as the channel description.
- Set channel description: "Open-source AI from Bengaluru 🇮🇳. Dan Glasses + danlab-multimodal. MIT. github.com/somdipto/dan-glasses"
- Approve-join mode ON; read-only for non-admins.

**HackerNoon essay draft (publish 2026-06-30 12:00 UTC, after Show HN):**
> **Title:** Why we shipped a <50g wearable against Snap's $2,195 one
>
> **Body outline:**
> 1. The closed-source bar (Snap Specs $2,195, 132-136g, two Snapdragons, ad-supported, Spiegel's "new era")
> 2. The category exploded in one week (Google Android XR + Warby Parker + Gemini, Qualcomm Snapdragon Reality Elite, Apple AI AirPods + glasses)
> 3. The India cohort (Oculosense, Sarvam, Focally) — all real, all distinct
> 4. Dan Glasses: <50g, $145-180 BOM, MIT, 7 daemons, audiod v0.7 with 101/101 tests + Tauri client
> 5. The proactive vs reactive wedge (audiod v0.7 with 101/101 tests as receipt)
> 6. On-device is going to be a compliance requirement in 2027 (Illinois HB4843, Bartone v. Meta)
> 7. Why MIT + on-device is the moat (not the model)
> 8. What we are NOT claiming (RL, AGI, hardware dates)
> 9. Try it: github.com/somdipto/dan-glasses

**Illinois HB4843 thread (09:00 IST, 5 tweets):**
> 1/ Illinois just introduced HB4843 — the first US state bill to ban smart glasses while driving. The category is being regulated. govtech.com/question-of-the-day/which-state-wants-to-ban-wearing-smart-glasses-while-driving
>
> 2/ The first wave of AR glasses regulation is here. On-device is going to be a compliance requirement in 2027, not a marketing claim.
>
> 3/ Dan Glasses is already on-device by default. audiod v0.7 runs locally. perceptiond runs locally. memoryd is SQLite + vectors on disk. No cloud lock-in.
>
> 4/ Bartone v. Meta is the first of multiple on-device-vs-cloud class actions in 2026–27. The compliance posture is "on-device by default." We have that. Today.
>
> 5/ We are 1.5 people in Bengaluru. We are not the answer. But we are the open-source floor for the answer. github.com/somdipto/dan-glasses

**Tweet (09:00 IST):**
> @danlab_bot is now public on Telegram.
>
> Daily ship-logs. Demo links. Dev chat.
>
> t.me/danlab_dev
>
> Same content as the X feed, but the conversation lives in Telegram.

---

## Friday 06-27 — X thread "What Snap's $2,195 Specs means for the open-source alternative"

**X thread outline (publish 18:00 IST):**
> 1/ Snap just unveiled $2,195 AR glasses with two Snapdragons. Spiegel called it "a new era of computing." Same week: Google Android XR + Warby Parker + Gemini. Qualcomm Snapdragon Reality Elite. Apple AI AirPods + glasses. The category exploded.
>
> 2/ Snap is the price ceiling. $2,195. 132-136g. Ad-supported. Fully standalone with two Snapdragons. Spiegel's "new era" costs $2,195.
>
> 3/ Google is the platform play. Warby Parker + Gentle Monster + Gemini. Voice-first AR on Android XR. Closed model. Closed platform.
>
> 4/ Apple is the same thing 14 months later. Bloomberg via NY Post 06-16. AI AirPods + glasses. Visual Intelligence. External cloud-send indicator lights.
>
> 5/ The category is confirmed. The cost is not. Our BOM target: $145–180. audiod v0.7 with 101/101 tests is live today. github.com/somdipto/dan-glasses
>
> 6/ We're not the answer. We're the floor. MIT. 7 daemons. audiod v0.7 + Tauri client. perceptiond. memoryd. ttsd. toold. os-toold. openclawd. All inspectable. All runnable. All from a 1.5-person team in Bengaluru.
>
> 7/ The next step is yours. Clone it. Run it. Break it. Or fork it and ship a better version. The category needs a price floor. github.com/somdipto/dan-lab 🇮🇳

**LinkedIn cross-post (18:30 IST):**
> What Snap's $2,195 Specs means for the open-source alternative.
>
> 7-tweet thread. The category exploded this week. Snap is the price ceiling. We're the floor. audiod v0.7 with 101/101 tests. MIT. From Bengaluru.
>
> Receipts > narrative.

---

## Saturday 06-28 — rest day

**No posts.** Recharge.

---

## Sunday 06-29 — Week-in-review + Show HN prep

**LinkedIn longform (publish 10:00 IST):**
> Week 26 ship-log at DanLab:
> - Mon: somdipto/dan-glasses public, v0.7.0-audiod tag (Tauri client)
> - Tue: somdipto/danlab-multimodal public, v0.1.0 tag + danlab.dev refresh
> - Wed: 2 Reddit threads (r/LocalLLaMA, r/indianstartups)
> - Thu: @danlab_bot flipped to public + Illinois HB4843 thread
> - Fri: 7-tweet thread "What Snap's $2,195 Specs means for the open-source alternative"
> - Sun: this post
>
> Net new: 2 public repos, 1 2026 homepage, 1 public Telegram, 14 tweets, 1 Show HN in the can.
>
> The category exploded: Snap Specs at $2,195, Google Android XR + Warby Parker + Gemini, Qualcomm Snapdragon Reality Elite, Apple AI AirPods + glasses, Illinois HB4843. We rode the wave. We didn't claim the wave.
>
> Next week: Show HN for DanClaw Phase 1 (06-30 14:00 PT). Subscribe to the channel to catch the thread.

**YouTube script (record Saturday evening, publish Sunday 10:00 IST):**
> **Title:** Week 26 at DanLab — audiod v0.7, Snap Specs at $2,195, danlab.dev refreshed
>
> [0:00–0:30] Hook: "This week we pushed 2 repos to public GitHub. audiod v0.7 with a Tauri client + danlab-multimodal. Both MIT. Both from a 1.5-person team in Bengaluru. The same week Snap launched $2,195 AR glasses."
>
> [0:30–2:00] dan-glasses walkthrough. Show the README. Show the live status strip with audiod v0.7 ports. Show audiod on :8741. Show the Tauri client integration test results.
>
> [2:00–3:30] danlab-multimodal walkthrough. Show the demo. Show the 302MB. Show the disclaimer.
>
> [3:30–4:30] danlab.dev refresh. Show the old (2024) vs new (2026) homepage. Show the live status strip.
>
> [4:30–5:00] Outtro: "Snap is the ceiling. We're the floor. Show HN drops Monday 06-30 14:00 PT. Subscribe."

---

## Monday 06-30 — Show HN: DanClaw Phase 1

**Show HN post (publish 14:00 PT = 02:30 IST Tue 07-01):**

> **Title:** Show HN: DanClaw – A multi-agent orchestration system for one-person companies
>
> **Body:**
>
> Hey HN,
>
> We're somdipto + Dan from danlab.dev in Bengaluru, India. We're building a multi-agent orchestration system called DanClaw. Today we're open-sourcing Phase 1.
>
> **What is it?**
>
> DanClaw is a Node.js + TypeScript system for running a "one-person company" — a fleet of AI agents with org charts, budgets, governance, and goal alignment. You bring your own agents (we tested with Claude Code + Codex). DanClaw gives you the company.
>
> **What's in Phase 1?**
>
> - 7-agent org chart with delegation
> - Per-agent budgets with cost governance
> - Goal alignment from task → project → company
> - Audit log + observability
> - Mobile dashboard (Flutter)
> - Telegram integration via OpenClaw
>
> **Why?**
>
> Most "AI company" tools stop at chat. We needed something that runs the actual ops — tickets, budgets, escalation paths, audit trails — for a 1.5-person team that's trying to ship hardware, firmware, and ML simultaneously.
>
> **Receipts:**
>
> - Repo: github.com/somdipto/danclaw
> - License: MIT
> - Demo: danlab.dev/danclaw
> - Architecture: github.com/somdipto/danclaw/blob/main/ARCHITECTURE.md
>
> **What it is NOT:**
>
> - Not a SaaS. Self-hosted.
> - Not a replacement for a human team. It's for the case where the team is 1.5 humans.
> - Not finished. Phase 1 is the foundation. Phase 2 is on the roadmap.
>
> **The post-Snap context:**
>
> This is not an AR-glasses post. The smart-glasses category just exploded (Snap Specs $2,195, Google Android XR + Warby Parker + Gemini, Qualcomm Snapdragon Reality Elite, Apple AI AirPods + glasses). DanClaw is a separate product. It's the orchestration layer that lets the 1.5-person team that's building the smart glasses actually ship.
>
> Happy to answer any questions about the architecture, the agent selection, or why we built it in India. 🇮🇳
>
> — somdipto + Dan

**Tweet (post HN, 02:30 IST Tue 07-01):**
> Show HN just went live: DanClaw Phase 1.
>
> github.com/somdipto/danclaw
>
> A multi-agent orchestration system for one-person companies. 7 agents. Per-agent budgets. Goal alignment. MIT. From Bengaluru.
>
> Drop a comment if you have questions — we'll be in the HN thread all day.

---

## Week 27 preview (v66 → v67 transition)

**Mon 07-07:** GitHub release — audiod v0.7.1 (or whatever dan2 ships next)
**Tue 07-08:** LinkedIn longform — "What the AGI roadmap looks like from India" (from dan2-agi-roadmap)
**Wed 07-09:** Reddit r/MachineLearning — audiod v0.7 post-mortem
**Thu 07-10:** HackerNoon essay: "Why we shipped a <50g wearable against Snap's 132g one" (v66 draft ships)
**Fri 07-11:** X thread: "The audiod Tauri client — what we learned shipping a daemon to a desktop shell"
**Sun 07-13:** Week-27 review

**v67 content calendar (next iteration) will include:**
- 500-word technical post: "Why we're swapping KittenTTS for Orca" (from dan2-model-analysis.md)
- Show HN results thread (stars, comments, follow-up posts)
- First YouTube demo (2-min audiod + perceptiond)
- HackerNoon essay publish
- v67 "first 50 stars" plan if audiod + danlab-multimodal together cross 25 stars

---

## Daily non-negotiables (restated)

**09:00 IST — ship-log tweet (X + Telegram @danlab_bot).** Use the same template. One line, one receipt.
**09:30 IST — reply to one relevant account.** Genuine reply, not a pitch.
**23:00 IST — save one insight to backlog.** `agent-work/backlog.md`. One line.

**The backlog is sacred.** When you don't know what to post, the backlog tells you. When the backlog is empty, that's the signal that nothing interesting happened today.

---

## What v66 does NOT post about

- Snap Specs by name outside the price-anchor context. (Mention once with the price, then move on.)
- Apple AI AirPods / Apple N50 by name. (Same.)
- Qualcomm Snapdragon Reality Elite by name. (Same — we don't fight on chip.)
- Google Android XR + Warby Parker + Gemini by name. (Same — we don't fight on platform.)
- "AGI from India" framing. (Snap-week is not the time to claim AGI. File for v67.)
- Competitor comparisons by name outside the wedge paragraph. (Architecture comparison, not name comparison.)
- Hiring. (We're a 1.5-person team. Hiring post would be premature.)
- Fundraising. (Bootstrapping. Fundraising post would be premature.)
- "We just hit X followers." (Vain. Don't.)
- "Snap-killer" framing. (We are not killing Snap. We are the cost.)

---

## v66 → v67 (next week's transition)

v66 content calendar assumes:
- Show HN drops 06-30 with ≥50 points
- danlab-multimodal crosses 25 stars by 07-04
- somdipto's bio paragraph is in hand (third pass asking)
- Telegram @danlab_bot has 50+ subscribers
- audiod v0.7 announcement tweet gets ≥100 likes

v66 → v67 will include:
- Mon 06-30: Show HN publish + thread
- Tue 07-01: Show HN results thread (stars, comments)
- Wed 07-02: HackerNoon essay publish
- Thu 07-03: AMA r/LocalLLaMA
- Fri 07-04: Reddit r/indianstartups weekly update
- Sun 07-05: Week-27 review

**Filed under:** `agent-work/dan1-content-calendar.v66.md`
**Next:** `agent-work/dan1-twitter-content.v66.md`
