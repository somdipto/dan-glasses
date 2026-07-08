# Dan1 Content Calendar — v65 (canonical)

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 06:30 IST (01:00 UTC)
**Window:** Week 26 (2026-06-23 Mon → 2026-06-29 Sun), plus Show HN on 2026-06-30
**Status:** ✅ Canonical. Supersedes v64.

> **v65 thesis — public surface this week.** The week 26 priority is to push the public surface that backs every other piece of marketing: 3 public GitHub repos, refreshed danlab.dev, public Telegram channel, claimed Twitter handle, Show HN in the can. Every post this week is anchored to one of those artifacts.

---

## Week 26 — at a glance

| Day | Date | Primary ship | Channel | Asset | Time IST |
|---|---|---|---|---|---|
| Mon | 06-23 | **Push `somdipto/dan-glasses` to public GitHub** | GitHub + X + LinkedIn + Telegram | `v0.6.0-audiod` tag + release notes | 09:00 |
| Tue | 06-24 | **Push `somdipto/danlab-multimodal` to public** + **refresh danlab.dev** | GitHub + X + LinkedIn | `v0.1.0` tag + 2026 homepage | 09:00 |
| Wed | 06-25 | Reddit r/LocalLLaMA + r/indianstartups | Reddit + X | danlab-multimodal reproducible post | 09:00 |
| Thu | 06-26 | Flip @danlab_bot to public + HackerNoon draft | Telegram + Medium | channel config + essay draft | 21:00 |
| Fri | 06-27 | X thread: "We just published 3 repos" | X + LinkedIn | 7-tweet thread | 18:00 |
| Sat | 06-28 | (rest day) | — | — | — |
| Sun | 06-29 | Week-in-review + Show HN prep | LinkedIn + YouTube | 5-min essay + HN post draft | 10:00 |
| Mon | 06-30 | **Show HN: DanClaw Phase 1** | Hacker News | Show HN post (drafted below) | 14:00 PT |

**Daily non-negotiables (all 7 days):**
- 09:00 IST: 1 ship-log tweet (X + Telegram @danlab_bot)
- 09:30 IST: 1 reply to a relevant account (X, LinkedIn, Reddit)
- 23:00 IST: 1 insight saved to backlog (`agent-work/backlog.md`)

---

## Monday 06-23 — Push `somdipto/dan-glasses` to public

**Primary deliverable:** Public GitHub release. This is the *single most important marketing action of the week.*

**Pre-flight checklist:**
- [ ] v65 README is in `/home/workspace/dan-glasses/README.md` (see `dan1-github-readme-suggestions.md` v65)
- [ ] `LICENSE` (MIT) at repo root
- [ ] `STATUS.md` with daemon-by-daemon status (audiod v0.6 ✅, others spec'd)
- [ ] `.github/ISSUE_TEMPLATE/` and `CONTRIBUTING.md` (basic)
- [ ] No secrets, no `.env` files, no `node_modules` committed
- [ ] Tag created: `v0.6.0-audiod-pre-rust-1.77`

**Release template:**
```
## v0.6.0-audiod-pre-rust-1.77 — Adaptive Whisper Timeout

### What's Changed
- Adaptive timeout budget: `min(60.0, 15.0 + 3.0 * duration_s)`.
  Replaces fixed 10s cap that flaked under sustained CPU pressure.
- Closed `/restart` counter bug. `_reset_counters()` now idempotent.
- 101/101 tests across 5 stress runs (was 98/98, flaked once on cold cache).

### Verify
\`\`\`
curl http://localhost:8741/health
# {"status":"ok","service":"audiod"}

curl http://localhost:8741/status
# pid: 10887, running: True, vad_ready: True
\`\`\`

### Why it matters
Cold-cache whisper inference was hitting the 10s ceiling on slow hardware.
Adaptive budget fixes that without changing the floor behavior.

### Known limitations
- Requires Python 3.11+ (no 3.10 backport yet).
- Tauri app build requires Rust ≥ 1.77 (see apps/dan-glasses-app/README).
- Other 6 daemons are spec'd but not yet at audiod's test coverage.

Built at danlab.dev 🇮🇳
```

**Tweet (09:00 IST, also cross-post to @danlab_bot):**
> audiod v0.6 is public. v0.6.0-audiod tag.
>
> - Adaptive whisper timeout (`min(60, 15 + 3*dur)`)
> - /restart counter bug closed
> - 101/101 across 5 stress runs
>
> `curl localhost:8741/health` → ok. PID 10887. MIT.
>
> github.com/somdipto/dan-glasses 🇮🇳

**LinkedIn (09:30 IST cross-post):**
> audiod v0.6 is now public on GitHub.
>
> The small improvements that compound. When your audio daemon is flaking at 10s under cold-cache CPU pressure, you don't ship a rewrite. You ship a budget: `min(60.0, 15.0 + 3.0 * duration_s)`. Five stress runs later, 101/101.
>
> The full daemon stack: audiod + perceptiond + memoryd + ttsd + toold + os-toold + openclawd. MIT. India.
>
> github.com/somdipto/dan-glasses

**Reply targets (find at 09:30 IST):**
- @ApoorvSaxena (audio ML)
- @swyx (DX/AI engineering)
- @karpathy (any thread on test methodology)

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
\`\`\`
git clone https://github.com/somdipto/danlab-multimodal
cd danlab-multimodal
python3 src/demo.py demo
# ~32s per image on a $300 laptop
\`\`\`

### Why
Hackathon-grade MIT project. Anthropic's Jack Clark publicly said recursive
self-improvement is the next step; we wanted an honest pre-RL scaffold
instead of claiming RL we didn't have.

Built at danlab.dev 🇮🇳
```

**danlab.dev refresh — push v65 landing copy:**
- Use the v65 landing copy in `dan1-landing-copy.md`.
- Replace "AI Glasses" with "Dan Glasses."
- Replace Agent8 / Zerant / Dapify section with the 7 daemons table.
- Add the live status strip.
- Cross-link to the 3 public GitHub repos.
- Lead with the curl-able health endpoint.

**Tweet (09:00 IST):**
> danlab-multimodal is public. v0.1.0.
>
> 302MB combined. SmolVLM-256M + mmproj. ~32s per image on CPU.
>
> \`\`\`
> git clone github.com/somdipto/danlab-multimodal
> cd danlab-multimodal
> python3 src/demo.py demo
> \`\`\`
>
> Pre-RL. Heuristic. MIT. We don't claim RL we don't have.
>
> github.com/somdipto/danlab-multimodal

**LinkedIn cross-post (11:00 IST):**
> danlab-multimodal is public today.
>
> The world's smallest working VLM-on-CPU loop. 302MB combined. Pre-RL. Heuristic. MIT.
>
> We don't claim RL we don't have. We built a heuristic feedback scaffold instead, with hand-coded scoring rules, and made the whole thing reproducible in 30 seconds. Hackathon-grade but production-shaped.
>
> github.com/somdipto/danlab-multimodal

**Reply targets:** @awnihannun, @simonw, @karpathy.

---

## Wednesday 06-25 — Reddit r/LocalLLaMA + r/indianstartups

**Reddit r/LocalLLaMA post (09:00 IST):**
> **Title:** danlab-multimodal — sub-300MB VLM on CPU, reproducible in 30s
>
> **Body:**
>
> \`\`\`
> git clone https://github.com/somdipto/danlab-multimodal
> cd danlab-multimodal
> python3 src/demo.py demo
> \`\`\`
>
> That's the whole thing. SmolVLM-256M + mmproj = 302MB combined. ~32s per image on CPU. Pre-RL heuristic feedback loop (hand-coded scoring, no weights modified — we're explicit it's not RL).
>
> Live demo: https://zo.pub/som/danlab-multimodal-demo
>
> Hackathon-grade MIT project. Why: Anthropic's Jack Clark publicly said recursive self-improvement is the next step, and we wanted an *honest* pre-RL scaffold instead of claiming RL we didn't have.
>
> AMA in thread.

**Reddit r/indianstartups post (09:30 IST):**
> **Title:** Week 26 update — open-sourced 2 repos, danlab.dev refreshed
>
> **Body:**
>
> Three years into bootstrapping an AI lab from Bengaluru. This week we shipped:
>
> - **somdipto/dan-glasses** — 7 daemons, audiod v0.6 with 101/101 tests, MIT. The proactive AI companion.
> - **somdipto/danlab-multimodal** — 302MB VLM on CPU, reproducible in 30s. Pre-RL scaffold.
> - **danlab.dev** — refreshed from 2024 to 2026. Live status strip. Real receipts.
>
> Three AI glasses out of India this year. Oculosense (offline-only, visually-impaired-focused). Sarvam (cloud-first, government halo). Dan Glasses (MIT + on-device + proactive + India-priced). The only one with all four.
>
> AMA on the indie's path: how we ship weekly, what works, what doesn't.

**Tweet (09:00 IST, also @danlab_bot):**
> 2 repos public this week:
>
> github.com/somdipto/dan-glasses — audiod v0.6, 7 daemons, MIT
> github.com/somdipto/danlab-multimodal — 302MB VLM on CPU
>
> danlab.dev refreshed from 2024 to 2026.
>
> All receipts: audiod PID 10887, 101/101 tests, `curl localhost:8741/health` → ok.

**Reply targets (09:30 IST):** @karpathy on any RL thread, @awnihannun on any multimodal thread, @simonw on any local-llama thread.

---

## Thursday 06-26 — Flip @danlab_bot to public + HackerNoon draft

**Telegram channel action:**
- Flip @danlab_bot channel to public.
- Set channel username: `@danlab_dev` (or `@danlab_bot` if username already taken).
- Pin the v65 pinned tweet as the channel description.
- Set channel description: "Open-source AI from Bengaluru 🇮🇳. Dan Glasses + danlab-multimodal. MIT. github.com/somdipto/dan-glasses"
- Approve-join mode ON; read-only for non-admins.

**HackerNoon essay draft (publish 2026-06-30 12:00 UTC, after Show HN):**
> **Title:** Why we shipped a <50g wearable against Snap's 132g one
>
> **Body outline:**
> 1. The closed-source bar (Snap Specs 132-136g, $2,195, two Snapdragons, ad-supported)
> 2. The India cohort (Oculosense, Sarvam, Focally) — all real, all distinct
> 3. Dan Glasses: <50g, $145-180 BOM, MIT, 7 daemons, proactive
> 4. The proactive vs reactive wedge (audiod v0.6 with 101/101 tests as receipt)
> 5. Why MIT + on-device is the moat (not the model)
> 6. What we are NOT claiming (RL, AGI, hardware dates)
> 7. Try it: github.com/somdipto/dan-glasses

**Tweet (09:00 IST):**
> @danlab_bot is now public on Telegram.
>
> Daily ship-logs. Demo links. Dev chat.
>
> t.me/danlab_dev
>
> Same content as the X feed, but the conversation lives in Telegram.

---

## Friday 06-27 — X thread "We just published 3 repos"

**X thread outline (publish 18:00 IST):**
> 1/ This week we pushed 2 of 3 repos to public. The third (danclaw-phase1) drops on Show HN Monday. 3 repos. 1 origin: India 🇮🇳
>
> 2/ somdipto/dan-glasses — the proactive AI companion. 7 daemons. audiod v0.6 is live with 101/101 tests. `curl localhost:8741/health` → ok. MIT. github.com/somdipto/dan-glasses
>
> 3/ somdipto/danlab-multimodal — sub-300MB VLM on CPU, reproducible in 30s. Pre-RL heuristic loop. We don't claim RL we don't have. github.com/somdipto/danlab-multimodal
>
> 4/ somdipto/danclaw-phase1 — Show HN Monday 06-30 14:00 PT. A multi-agent orchestration system for one-person companies. Watch this space.
>
> 5/ All MIT. All runnable today. All from a 1.5-person team in Bengaluru.
>
> 6/ Why push to public this week? Because danlab.dev was still reading 2024. First-contact with a stranger should hit a 2026 homepage, not a 2024 one.
>
> 7/ The receipts are public. The cadence is weekly. The origin is India. Fork it. Run it. Break it. github.com/somdipto/dan-lab

**LinkedIn cross-post (18:30 IST):**
> Three repos. One week. One origin: India.
>
> - dan-glasses: audiod v0.6, 7 daemons, MIT
> - danlab-multimodal: 302MB VLM on CPU
> - danclaw-phase1: Show HN 06-30
>
> All MIT. All runnable. All from a 1.5-person team in Bengaluru.
>
> Receipts > narrative. Fork it.

---

## Saturday 06-28 — rest day

**No posts.** Recharge.

---

## Sunday 06-29 — Week-in-review + Show HN prep

**LinkedIn longform (publish 10:00 IST):**
> Week 26 ship-log at DanLab:
> - Mon: somdipto/dan-glasses public, v0.6.0-audiod tag
> - Tue: somdipto/danlab-multimodal public, v0.1.0 tag + danlab.dev refresh
> - Wed: 2 Reddit threads (r/LocalLLaMA, r/indianstartups)
> - Thu: @danlab_bot flipped to public Telegram
> - Fri: 7-tweet thread "We just published 2 repos"
> - Sun: this post
>
> Net new: 2 public repos, 1 2026 homepage, 1 public Telegram, 1 HackerNoon draft, 14 tweets, 1 Show HN in the can.
>
> Next week: Show HN for DanClaw Phase 1 (06-30 14:00 PT). Subscribe to the channel to catch the thread.
>
> Cadence is the brand. Public surface is the proof.

**YouTube script (record Saturday evening, publish Sunday 10:00 IST):**
> **Title:** Week 26 at DanLab — 2 public repos, danlab.dev refreshed
>
> [0:00–0:30] Hook: "This week we pushed 2 repos to public GitHub. audiod v0.6 + danlab-multimodal. Both MIT. Both from a 1.5-person team in Bengaluru."
>
> [0:30–2:00] dan-glasses walkthrough. Show the README. Show the live status strip. Show audiod on :8741.
>
> [2:00–3:30] danlab-multimodal walkthrough. Show the demo. Show the 302MB. Show the disclaimer.
>
> [3:30–4:30] danlab.dev refresh. Show the old (2024) vs new (2026) homepage. Show the live status strip.
>
> [4:30–5:00] Outtro: "Show HN drops Monday 06-30 14:00 PT. Subscribe."

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
> - Repo: github.com/somdipto/danclaw-phase1
> - License: MIT
> - Phase 1 tarball: danclaw-phase1.tar.gz (in the repo)
> - Demo: danlab.dev/danclaw
> - Architecture: github.com/somdipto/danclaw-phase1/blob/main/ARCHITECTURE.md
>
> **What it is NOT:**
>
> - Not a SaaS. Self-hosted.
> - Not a replacement for a human team. It's for the case where the team is 1.5 humans.
> - Not finished. Phase 1 is the foundation. Phase 2 is on the roadmap.
>
> Happy to answer any questions about the architecture, the agent selection, or why we built it in India. 🇮🇳
>
> — somdipto + Dan

**Tweet (post HN, 02:30 IST Tue 07-01):**
> Show HN just went live: DanClaw Phase 1.
>
> github.com/somdipto/danclaw-phase1
>
> A multi-agent orchestration system for one-person companies. 7 agents. Per-agent budgets. Goal alignment. MIT. From Bengaluru.
>
> Drop a comment if you have questions — we'll be in the HN thread all day.

---

## Daily non-negotiables (restated)

**09:00 IST — ship-log tweet (X + Telegram @danlab_bot).** Use the same template. One line, one receipt.
**09:30 IST — reply to one relevant account.** Genuine reply, not a pitch.
**23:00 IST — save one insight to backlog.** `agent-work/backlog.md`. One line.

**The backlog is sacred.** When you don't know what to post, the backlog tells you. When the backlog is empty, that's the signal that nothing interesting happened today.

---

## What v65 does NOT post about

- Snap Specs. (Mentioned once in v64 research. Mention again only if a new receipt drops.)
- Apple AI Glasses. (Same.)
- Oculosense or Sarvam by name outside the India cohort context. (Don't trash competitors in the feed.)
- "AGI from India" framing. (We are AGI-aspirational. We say so once / quarter, max.)
- Competitor comparisons by name. (We compare on architecture, not names. Exception: the wedge paragraph in the India cohort context.)
- Hiring. (We're a 1.5-person team. Hiring post would be premature.)
- Fundraising. (Bootstrapping. Fundraising post would be premature.)
- "We just hit X followers." (Vain. Don't.)

---

## v65 → v66 (next week's transition)

v66 content calendar assumes:
- Show HN drops 06-30 with ≥50 points
- danlab-multimodal crosses 25 stars by 07-04
- somdipto's bio paragraph is in hand
- Telegram @danlab_bot has 50+ subscribers

v66 will include:
- Mon 06-30: Show HN publish + thread
- Tue 07-01: Show HN results thread (stars, comments)
- Wed 07-02: HackerNoon essay
- Thu 07-03: AMA r/LocalLLaMA
- Fri 07-04: Reddit r/indianstartups weekly update
- Sun 07-05: Week-27 review

**Filed under:** `agent-work/dan1-content-calendar.v65.md`
**Next:** `agent-work/dan1-twitter-content.v65.md`
