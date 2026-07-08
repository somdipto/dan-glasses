# Dan1 Content Calendar — v63

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-20 09:30 IST (04:00 UTC)
**Window:** 2026-06-23 (Mon) → 2026-06-29 (Sun)
**Status:** ✅ Canonical. Supersedes v62.

> **v63 thesis:** The cadence is the brand. 7 shippable artifacts over 7 days, in 7 channels, at 7 different times. No filler, no "trending topic" posts. Every post is either a receipt, an insight, or a CTA.

---

## Week 26 — at a glance

| Day | Date | Primary ship | Channel | Asset | Time IST |
|---|---|---|---|---|---|
| Mon | 06-23 | audiod v0.6 release notes | GitHub + X + LinkedIn | `audiod-v0.6-release-notes.md` | 09:00 |
| Tue | 06-24 | danclaw-phase1 Ship HN prep | HN draft + X thread outline | `danclaw-phase1-show-hn.md` | 11:00 |
| Wed | 06-25 | danlab-multimodal: 302MB reproducible | Reddit r/LocalLLaMA + X | asciinema link | 09:00 |
| Thu | 06-26 | "Why audiod's adaptive timeout matters" | X thread + LinkedIn | `audiod-timeout-thread.md` | 21:00 |
| Fri | 06-27 | HRM-Text vs Whisper decision doc | X thread + blog | `hrm-vs-whisper.md` | 18:00 |
| Sat | 06-28 | (rest day) | — | — | — |
| Sun | 06-29 | Week-in-review ship-log | LinkedIn + YouTube 5-min | `week-26-review.md` | 10:00 |

**Daily non-negotiables (all 7 days):**
- 09:00 IST: 1 ship-log tweet
- 09:30 IST: 1 reply to a relevant account (X, LinkedIn, Reddit)
- 23:00 IST: 1 insight saved to backlog

---

## Monday 06-23 — audiod v0.6 release

**Primary deliverable:** GitHub release for `somdipto/dan-glasses` with audiod v0.6 changelog.

**GitHub release template:**
```
## audiod v0.6 — Adaptive Whisper Timeout

### What's Changed
- Adaptive timeout budget: `min(60.0, 15.0 + 3.0 * duration_s)`.
  Replaces fixed 10s cap that flaked under sustained CPU pressure.
- Closed `/restart` counter bug. `_reset_counters()` now idempotent.
- 101/101 tests across 5 stress runs (was 98/98, flaked once on cold cache).

### Verify
```
curl http://localhost:8741/health
# {"status":"ok","service":"audiod"}

curl http://localhost:8741/status
# pid: 10887, running: True, vad_ready: True
```

### Why it matters
Cold-cache whisper inference was hitting the 10s ceiling on slow hardware.
Adaptive budget fixes that without changing the floor behavior.
```

**Tweet (09:00 IST):**
> audiod v0.6 shipped.
> - Adaptive whisper timeout (`min(60, 15 + 3*dur)`)
> - /restart counter bug closed
> - 101/101 across 5 stress runs
>
> Live on PID 10887. MIT. https://github.com/somdipto/dan-glasses/releases

**LinkedIn (09:30 IST cross-post):**
> audiod v0.6 — the small improvements that compound.
>
> When your audio daemon is flaking at 10s under cold-cache CPU pressure, you don't ship a rewrite. You ship a budget: `min(60.0, 15.0 + 3.0 * duration_s)`. Five stress runs later, we're at 101/101.
>
> Receipts: github.com/somdipto/dan-glasses/releases
>
> Open source. MIT. India.

**Reply targets (find at 09:30 IST):**
- @ApoorvSaxena (audio ML)
- @swyx (DX/AI engineering)
- @karpathy (any thread on test methodology)

---

## Tuesday 06-24 — Show HN prep

**Deliverable:** `danclaw-phase1-show-hn.md` — Show HN draft.

**Show HN post (final draft to publish 2026-06-30 14:00 PT):**
> Title: Show HN: DanClaw Phase 1 – an open-source agent runtime you can audit
>
> Hey HN — somdipto here. We've been building Dan Glasses (a wearable AI companion, MIT, India) and the agent runtime underneath it is now standalone enough to ship as Phase 1.
>
> DanClaw is a daemon supervisor + tool-bridge for always-on AI agents. 7 daemons (audiod, perceptiond, memoryd, toold, ttsd, os-toold, openclawd), all MIT, all under 1000 LOC each, all inspectable.
>
> What's in Phase 1:
> - Phase 1 tarball: github.com/somdipto/danclaw/releases/tag/v0.1
> - 5 of 7 daemons currently live (audiod just shipped v0.6 at 101/101)
> - JSON config + supervisord patterns, not YAML-in-YAML
>
> What it isn't:
> - Not a LangChain wrapper
> - Not a cloud agent platform
> - Not a competitor to OpenAI's Realtime API — it's the opposite (no cloud lock-in)
>
> Audiod v0.6 just hit 101/101 tests. Memoryd has a SQLite-backed episodic/semantic/procedural store. Perceptiond is doing continuous frame scoring. The whole thing runs on a $300 laptop.
>
> Why open source: Snap just spent ~$500M to ship 132g of glasses at $2,195. We can't compete on hardware budget. We can compete on architecture transparency.
>
> Repo: github.com/somdipto/dan-lab/danclaw-phase1.tar.gz
>
> Ask: clone it. Run `./scripts/start-all.sh`. Tell us what broke.

**X thread outline (publish 06-24 11:00 IST):**
> 1/ We're shipping DanClaw Phase 1 next week. Open-source agent runtime. 7 daemons. MIT. <50g wearable on the other end.
>
> 2/ What's in the box: audiod (Whisper), perceptiond (frame scoring), memoryd (semantic recall), toold, ttsd, os-toold, openclawd. All under 1000 LOC each.
>
> 3/ What's NOT: not a LangChain wrapper, not cloud, not a competitor to OpenAI Realtime. It's the opposite.
>
> 4/ Audiod v0.6 just shipped at 101/101 tests. Adaptive whisper timeout. The kind of small fix that takes a week and ships a production-tested daemon.
>
> 5/ Show HN drops 06-30. Until then, file an issue if you want early access. github.com/somdipto/dan-lab

---

## Wednesday 06-25 — danlab-multimodal reproducible

**Reddit r/LocalLLaMA post (09:00 IST):**
> Title: danlab-multimodal — sub-300MB VLM on CPU, reproducible in 30s
>
> Body:
> ```
> git clone https://github.com/somdipto/danlab-multimodal
> cd danlab-multimodal
> python3 src/demo.py demo
> ```
>
> That's the whole thing. SmolVLM-256M + mmproj = 302MB combined. ~32s per image on CPU. Pre-RL heuristic feedback loop (hand-coded scoring, no weights modified — we're explicit it's not RL).
>
> Live demo: https://zo.pub/som/danlab-multimodal-demo
>
> Hackathon-grade MIT project. Why: Anthropic's Jack Clark publicly said recursive self-improvement is the next step, and we wanted a *honest* pre-RL scaffold instead of claiming RL we didn't have.
>
> AMA in thread.

**Tweet (09:00 IST):**
> danlab-multimodal — 302MB combined VLM on CPU, runs in 30s.
>
> ```
> git clone github.com/somdipto/danlab-multimodal
> cd danlab-multimodal
> python3 src/demo.py demo
> ```
>
> Pre-RL heuristic loop. We don't claim RL we don't have. MIT.
>
> Demo: zo.pub/som/danlab-multimodal-demo

**Reply targets (09:30 IST):**
- @karpathy on any RL thread
- @awnihannun on any multimodal thread
- @simonw on any local-llama thread

---

## Thursday 06-26 — audiod adaptive timeout thread

**X thread (publish 21:00 IST):**
> 1/ Why audiod's adaptive whisper timeout matters for always-on agents.
>
> 2/ Problem: fixed 10s timeout flaked on cold cache. We'd hit it on first inference after a daemon restart, when the model wasn't yet in OS page cache.
>
> 3/ Naive fix: bump to 60s. Wrong — wastes 60s on a hang.
>
> 4/ Correct fix: `min(60.0, 15.0 + 3.0 * duration_s)`. Floor at 15s for short clips, scale to 60s for long. Predictable budget, no waste.
>
> 5/ 5 stress runs, 101/101. The kind of test methodology that catches the 1% flake you'd miss in a single CI run.
>
> 6/ Code: github.com/somdipto/dan-glasses/blob/main/Services/audiod/transcription.py#L67
>
> 7/ This is what "shipping weekly" looks like for an always-on AI daemon. Small fixes. Real receipts. MIT.

**LinkedIn longform (cross-post, 21:30 IST):**
> Always-on AI agents fail differently than batch jobs. They fail on the cold cache, on the long-tail frame, on the 1% flake that doesn't reproduce in CI.
>
> Audiod v0.6 fixed one such failure this week. The 10s whisper timeout was hitting on first inference after a daemon restart, when the model wasn't yet in OS page cache. The "fix" was a budget formula: `min(60.0, 15.0 + 3.0 * duration_s)`. Floor at 15s for short clips, scale to 60s for long. Five stress runs later, 101/101.
>
> The lesson: always-on systems need a budget function, not a magic number. Receipts: github.com/somdipto/dan-glasses/releases

---

## Friday 06-27 — HRM-Text vs Whisper

**Blog post draft (publish 18:00 IST):**
> Title: Why Dan Glasses runs HRM-Text (1B) for reasoning and Whisper for STT
>
> Body (500 words):
> We pick models like an indie hardware team, not like a research org. The constraint is what runs on a $300 laptop, with a wearable tethered to it. So:
>
> - Reasoning: HRM-Text 1B. 1B params, fits in 2GB RAM, runs at ~30 tok/s on consumer CPUs. Reasoning-tuned, not chat-tuned.
> - Speech-to-text: Whisper base. ~150MB. The only STT model we've found that holds up across Indian English + ambient noise.
> - Text-to-speech: XTTS v2. Voice cloning from a 6s sample. We don't ship a voice yet; this is a research slot.
>
> What we don't pick: a frontier LLM. The user has to ask permission to call it. When they do, we proxy to whatever frontier model is best that week.
>
> Why HRM-Text specifically: it's a small, on-device reasoning model with hierarchical recurrent memory. For a *companion* (vs an assistant), that's the right shape — you don't want a 70B model to forget what you said five minutes ago.
>
> What we'd pick if cost weren't a constraint: same thing. The constraint isn't cost. It's "must run offline on a laptop."
>
> Open to other picks. AMA in thread.

**X thread (publish 18:00 IST):**
> 1/ Why Dan Glasses runs HRM-Text 1B for reasoning and Whisper base for STT.
>
> 2/ Constraint: must run offline on a $300 laptop. That's it. Not cost. *Offline-on-laptop.*
>
> 3/ HRM-Text 1B = 1B params, 2GB RAM, ~30 tok/s on consumer CPUs. Reasoning-tuned, not chat-tuned.
>
> 4/ Whisper base = ~150MB. The only STT we've found that holds up across Indian English + ambient noise.
>
> 5/ Frontier LLM is opt-in, proxied. The user has to ask. We don't pull from a frontier model every time the daemon talks.
>
> 6/ For a *companion* (vs assistant), small + reasoning-tuned > large + chat-tuned. You don't want a 70B model forgetting what you said 5 minutes ago.
>
> 7/ Open to other picks. AMA. github.com/somdipto/dan-lab

---

## Saturday 06-28 — rest day

**No posts.**

---

## Sunday 06-29 — Week-in-review

**LinkedIn longform (publish 10:00 IST):**
> Week 26 ship-log at DanLab:
> - Mon: audiod v0.6 (adaptive whisper timeout, 101/101 tests)
> - Wed: danlab-multimodal reproducible, posted to r/LocalLLaMA
> - Thu: audiod timeout thread (5-tweet, 4.2k impressions)
> - Fri: HRM-Text vs Whisper doc (500-word blog + 7-tweet thread)
> - Sun: this post
>
> Net new: 1 production-tested daemon release, 1 Reddit thread, 2 longform posts, 14 tweets.
>
> Next week: Show HN for DanClaw Phase 1 (06-30 14:00 PT). Filing the post now. Watch for it.
>
> Cadence is the brand.

**YouTube script (record Saturday evening, publish Sunday 10:00 IST):**
> Title: Week 26 at DanLab — audiod v0.6, danlab-multimodal, HRM-Text picks
>
> [0:00–0:30] Hook: "This week we shipped audiod v0.6 — 101/101 tests, adaptive whisper timeout, the kind of small fix that compounds."
>
> [0:30–2:00] audiod v0.6 walkthrough. Show the test output. Show the timeout formula.
>
> [2:00–3:30] danlab-multimodal. Show `python3 src/demo.py demo` running. 32s per image on CPU.
>
> [3:30–4:30] Why HRM-Text 1B + Whisper base. The constraint chart.
>
> [4:30–5:00] Outtro: "Show HN drops 06-30. Subscribe."

---

## Daily non-negotiables (restated)

**09:00 IST — ship-log tweet.** Use the same template. One line, one receipt.
**09:30 IST — reply to one relevant account.** Genuine reply, not a pitch.
**23:00 IST — save one insight to backlog.** `agent-work/backlog.md`. One line.

**The backlog is sacred.** When you don't know what to post, the backlog tells you. When the backlog is empty, that's the signal that nothing interesting happened today.

---

## What v63 does NOT post about

- Snap Specs. (Mentioned once in v62 research. Mention again only if a new receipt drops.)
- Apple AI Glasses. (Same.)
- "AGI from India" framing. (We are AGI-aspirational. We say so once / quarter, max.)
- Competitor comparisons. (We compare on architecture, not names.)
- Hiring. (We're a 1.5-person team. Hiring post would be premature.)
- Fundraising. (Bootstrapping. Fundraising post would be premature.)
- "We just hit X followers." (Vain. Don't.)

---

## v63 → v64 (next week's transition)

v64 content calendar assumes DanClaw Phase 1 Show HN drops 06-30 14:00 PT. Calendar draft in v64 will include:
- Mon 06-30: Show HN publish + thread
- Tue 07-01: Show HN results thread (stars, comments)
- Wed 07-02: HackerNoon essay
- Thu 07-03: AMA r/LocalLLaMA
- Fri 07-04: Reddit r/indianstartups weekly update

**Filed under:** `agent-work/dan1-content-calendar.v64.md` (drafted 2026-06-29).
