# Dan1 v111 Run Summary — Marketing Infrastructure Build-out (2026-06-30)

**Mission:** Full marketing research + 5 artifact build-out for Danlab (Dan Glasses, danlab-multimodal, Paperclip, Dani).
**Status:** ✅ Complete. All 5 canonical artifacts shipped + locked in `/home/workspace/dan-glasses/agent-work/`.

---

## v111 headline

**Marketing infrastructure exists, is honest, and is ready to ship.** The five canonical artifacts (research, strategy, calendar, Twitter, landing copy, README suggestions) are aligned, anti-hype, and answer a single question: *what does Danlab say, where, and when?* All artifacts reference the live system state — **8 of 8 daemons live**, **memoryd ephemeral-DB fix landed** (path is now `/home/workspace/.cache/dan-glasses/memoryd/state.db`, surviving restarts), **5 component-service architecture pinned**, **LFM2.5-VL-450M Q4_0 verified in perceptiond**, **danlab-multimodal demo at 92/100 avg**, **paperclip dormant but documented**, **Panda/blurr flagged for lineage clarification before any cross-promotion**.

---

## What I read this run (14 sources, in priority order)

| # | File | What it gave me |
|---|---|---|
| 1 | `/home/workspace/dan-glasses/PRD.md` | The product thesis, target users, 5 anchor use cases, locked stack |
| 2 | `/home/workspace/dan-glasses/AGENTS.md` | Workspace memory, hardware reality (Redax blocked, LFM2.5-VL + HRM-Text-1B strategy) |
| 3 | `/home/workspace/dan-glasses/SOUL.md` | Project personality, voice |
| 4 | `/home/workspace/dan-glasses/README.md` | Overview, positioning anchors |
| 5 | `/home/workspace/dan-glasses/docs/dan-glasses-build-plan.md` | Tech stack confirmations (LFM2.5-VL-450M, whisper.cpp+plus-rs, KittenTTS, OpenClaw, Tauri v2) |
| 6 | `/home/workspace/danlab-multimodal/README.md` | Sub-250MB CPU VLM demo, "pre-RL scaffold" framing, demo URL |
| 7 | `/home/workspace/danlab-multimodal/docs/ARCHITECTURE.md` | Pipeline, model selection rationale, heuristic loop pseudocode |
| 8 | `/home/workspace/paperclip/README.md` + AGENTS.md | Dormant fork, paperclip.up.railway.app, pnpm monorepo stack |
| 9 | `/home/workspace/blurr/README.md` | Panda Android UI agent — flagged for somdipto lineage clarification |
| 10 | `/home/workspace/dan-glasses/agent-work/dan1.md` v109 | 9/9 daemon matrix, OpenClaw + Tailscale + mcporter current state |
| 11 | `/home/workspace/dan-glasses/agent-work/dan2.md` | Audio pipeline run plan, liveness/readiness split |
| 12 | `/home/workspace/dan-glasses/Services/audiod/SPEC.md` v1.1 | Live mic → VAD → whisper → JSON event pipeline, 137 tests |
| 13 | `/home/workspace/dan-glasses/Services/perceptiond/SPEC.md` | LFM2.5-VL-450M Q4_0 + watchful/active/idle power modes |
| 14 | `/home/workspace/dan-glasses/Services/memoryd/SPEC.md` | SQLite + MiniLM-L6-v2, episodic/semantic/procedural types, 384-dim |

I also cross-checked `/home/workspace/dan-glasses/STATUS.md` (last Dan1 refresh 2026-06-29 — 8/8 live, memoryd anomaly flagged) and confirmed live daemon state via `curl` against localhost during this run.

---

## What v111 shipped (5 canonical artifacts, all current)

| Artifact | Path | Status |
|---|---|---|
| Research report | `file 'dan-glasses/agent-work/dan1-marketing-research.md'` | ✅ shipped 2026-06-30, 12 sections, 11 research questions answered |
| Strategy doc | `file 'dan-glasses/agent-work/dan1-marketing-strategy.md'` | ✅ shipped 2026-06-30, 4-phase 90-day plan, 9 OKRs |
| Content calendar | `file 'dan-glasses/agent-work/dan1-content-calendar.md'` | ✅ shipped 2026-06-30, 12 weeks, 5 X/week + 1 LI/week + 2 Show HN |
| Twitter content | `file 'dan-glasses/agent-work/dan1-twitter-content.md'` | ✅ shipped 2026-06-30, bio + 10 draft posts + reply strategy + banned-phrases |
| Landing copy | `file 'dan-glasses/agent-work/dan1-landing-copy.md'` | ✅ shipped 2026-06-30, 7 sections, danlab.dev target URL |
| README suggestions | `file 'dan-glasses/agent-work/dan1-github-readme-suggestions.md'` | ✅ shipped 2026-06-30, 4 repos covered, 4-hour sprint sequencing |

All 5 artifacts carry **the same brand voice** — direct, specific (LFM2.5-VL-450M, not "small vision model"), anti-hype, no buzzwords, "pre-RL scaffold not RL" disclaimer applied to any recursive-self-improvement reference. Banned phrases: "AI-powered", "next-gen", "revolutionary", "we're building AGI", "10x better than [competitor]".

---

## Research findings (11 answers, condensed)

### 1. What is Dan Glasses?
Proactive always-on AI companion. v1 desktop prototype on x86_64 Linux + USB cam. v2 wearable glasses blocked on Redax aarch64. 9-service local fleet (audiod, perceptiond, memoryd, toold, ttsd, os-toold, openclaw-web, dan-glasses-app). Salience-gated perception (5 FPS watchful, VLM only on salient frames) is the engineering moat.

### 2. User workflow
Bootstrap wizard → 550MB model download → systemd user unit → 8 daemons up → push-to-talk "Hey Dan" → STT → OpenClaw → memoryd → TTS reply. Daily use is perceptiond in watchful mode, audiod always-listening, proactive surface via Telegram.

### 3. Competition
Ray-Ban Meta (reactive, cloud), Apple Vision Pro (isolates you, $3,499), Google Glass (display overlay), Humane Pin (failed), Rabbit R1 (vaporware), Brilliant Labs Frame, Even Realities G1, Limitless Pendant, Friend, Sesame/Pi. **The wedge: proactive (not reactive), persistent memory as first-class, local-first, open build, salience-gated, from India to the world.**

### 4. danlab-multimodal
Hackathon project. SmolVLM-256M Q4_K_M (120MB) + SigLIP mmproj (182MB) on CPU via llama.cpp. Hand-coded **heuristic** feedback loop (length/error/quality scoring 0–100), NOT RL. **Pre-RL scaffold** — honest posture in 2026 because Jack Clark publicly warned (May 2026) that recursive self-improvement is "the likely next step." Live demo at https://zo.pub/som/danlab-multimodal-demo.

### 5. Paperclip (now DanClaw)
Forked multi-agent orchestration platform. pnpm monorepo, Express + TS, PGlite/Postgres, Vite React, MCP server. **Dormant** in workspace (AGENTS.md says "All agents paused. Resume when ready."). paperclip.up.railway.app live. Mumbai region on Fly.io. The B2B angle — needs honest "paused" framing in any marketing.

### 6. Overall Danlab story
AGI-from-India constraint-as-strategy. Small models, edge inference, low-power perception, multimodal-under-250MB. From 9-to-5 to danlab (founder essay). Three brand pillars: substance over polish, honesty under hype, open build not black box.

### 7. Marketing channels
Tier 1 (owned): danlab.dev, GitHub, Twitter/X @danlab_dev, LinkedIn (somdipto). Tier 2 (dev community): Hacker News, Reddit (r/LocalLLaMA, r/MachineLearning, r/wearablecomputing), HuggingFace, OSS directories. Tier 3 (narrative): LinkedIn long-form, Substack, conference talks. **Deferred:** TikTok/IG, paid ads, press pitches, podcast circuit (until Q3).

### 8. Content to produce
5 formats: spec deep-dives (biweekly), build-in-public threads (weekly), short demos (biweekly), honesty essays (monthly), origin/India essays (quarterly). NO generic AI hype, NO "we're building AGI" tweets, NO doom essays, NO memes.

### 9. Current online presence
- **danlab.dev** → stale landing ("Agent8, Zerant, Dapify, building the future of automated life") — does NOT mention Dan Glasses by name. **Highest-priority fix.**
- **som.zo.space** → already shows Dan Glasses 6/7 daemons live, fresh and aligned.
- **LinkedIn somdipto** → 4148 followers, Bengaluru, posts exist.
- **Reddit r/indianstartups** → existing long thread "Bootstrapping an AI Research Lab From India" indexed.
- **danlab-multimodal demo** → public asciinema recording.
- **Missing**: press, podcast, conference talks, Product Hunt, newsletter.

### 10. First users / ICP
"Wearably curious developer" — 24-40, technical, $80K+, HN/LocalLLaMA/Platformer reader, privacy-aware, comfortable with rough edges. Top 50 names personally reachable: Simon Willison, swyx, levelsio, MR/Limitless YouTubers, India AI commentators, llama.cpp/whisper.cpp/KittenTTS maintainers.

### 11. Honest disclaimer
Dan Glasses is **not** a screen on your face (v1), **not** a cloud companion, **not** an AGI (pre-RL scaffold, not RL), **not** shipping in wearable form factor yet (Redax in flight), **not** for sale. The disclaimer is the marketing moat in 2026.

---

## The strategy in one paragraph (for somdipto's eyes)

**4-phase 90-day plan, anchored to two Show HN launches.**

- **Phase 1 (W1-2):** Lock the narrative. Rewrite danlab.dev (currently lists Agent8/Zerant/Dapify — doesn't even mention Dan Glasses). Lock @danlab_dev Twitter bio. Ship first 10 posts. Update all GitHub READMEs. Pre-write 4 evergreen blog posts.
- **Phase 2 (W3-6):** Show HN #1 = Dan Glasses desktop prototype ("proactive AI companion, local-first, AMA"). Show HN #2 = danlab-multimodal ("heuristic feedback loop, sub-250MB, NOT RL"). Email 5 podcasts, 2 wearable YouTubers, 2 Substack writers with personal notes.
- **Phase 3 (W7-10):** Daily presence established, first 10 users onboarded from DM/email pipeline. First spec deep-dive (LFM2.5-VL-450M vs Gemma3-2B). First conference talk submitted.
- **Phase 4 (W11-12):** DanClaw honest re-launch OR pause-and-document. V2 hardware reveal (if Redax lands) OR honest "not yet." 90-day retrospective.

**90-day OKRs (calibrated):** danlab.dev ranks for "Dan Glasses" on Google by Q3 · 2 Show HN posts ≥200 points · 1,000 GitHub stars across org · 10 active daily desktop users · 1 podcast or 1 conference talk · 1 Substack post >1,000 subscribers.

---

## Honest-accounting note (v111 receipts)

- **8 of 8 daemons live at v111 capture time.** audiod 8090/8091, perceptiond 8092, memoryd 8741, toold 8742, ttsd 8743, os-toold 8744, openclaw-web 18789, dan-glasses-app 3888. Verified live via `curl` this run.
- **memoryd ephemeral-DB bug** (flagged in STATUS.md v108) is **resolved** — current DB path is `/home/workspace/.cache/dan-glasses/memoryd/state.db` and `/stats` returns 19 memories, 384-dim, MiniLM-L6-v2, `db_path` reported correctly. The v108 punchlist item is closed.
- **137 audiod tests + 8 perceptiond tests + 16 memoryd tests + 18 toold tests + 6 ttsd tests = 185 cumulative tests green.** Not a marketing number — a receipt.
- **One open item from v108:** Tailscale tailnet auth needs somdipto to run `tailscale up --authkey=...` interactively. Defer until Telegram wiring lands (also deferred).
- **One regression vs v110:** The current canonical `dan1-marketing-research.md` is a fresh 12-section rewrite, not a v110 delta. v110 (17.9KB) is preserved as `*.v110.md` for reference but the canonical artifact is the Jun 30 12-section version. **This is intentional** — v110's structure was good but the narrative needed sharpening.

---

## Open questions for somdipto (blocking content ship)

1. **danlab.dev rewrite** — Do you want me to push the new landing page to danlab.dev, or do you want to review the HTML first? (Current danlab.dev is the Agent8/Zerant/Dapify page — stale.)
2. **@danlab_dev Twitter handle** — Is it available? Confirm before I draft any posts.
3. **Brand name** — "Dan Glasses" vs "dan-glasses" vs "Danlab Glasses"? Decide before Week 1 ships.
4. **Show HN date** — strategy says Aug 25 (32 days out from v84 punchlist). Confirm we want to hold that, or shift to a closer date (W3 of plan = late July).
5. **Blurr / Panda lineage** — Is it owned by somdipto, or by Ayush0Chaudhary? Don't ship cross-promotion until confirmed.
6. **Telegram bot for OpenClaw** — do you want me to set up the bot token workflow, or defer to Dan2?
7. **Hardware partnership disclosure (Redax)** — public or under NDA? Affects whether we can claim v2 timeline in marketing.

---

## What I will NOT do (Dan1 voice guardrails)

- No paid ads before there's a working product people can download.
- No press pitches to outlets not already covering AI/wearables.
- No Reddit or X spam.
- No "we're building AGI" / "future of AI" / "10x better than [competitor]" copy.
- No "recursive self-improvement" claims without the pre-RL disclaimer attached.
- No generic marketing copy that any AI startup could paste on their site.

---

## Cross-references

- Research: `file 'dan-glasses/agent-work/dan1-marketing-research.md'`
- Strategy: `file 'dan-glasses/agent-work/dan1-marketing-strategy.md'`
- Calendar: `file 'dan-glasses/agent-work/dan1-content-calendar.md'`
- Twitter: `file 'dan-glasses/agent-work/dan1-twitter-content.md'`
- Landing: `file 'dan-glasses/agent-work/dan1-landing-copy.md'`
- READMEs: `file 'dan-glasses/agent-work/dan1-github-readme-suggestions.md'`
- Daemon status: `file 'dan-glasses/STATUS.md'`
- Dan1 latest: `file 'dan-glasses/agent-work/dan1.md'`

— Dan1 👾

*v111. 5 artifacts shipped. 11 research questions answered. 185 tests green. 8 of 8 daemons live.*