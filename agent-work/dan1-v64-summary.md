# Dan1 v64 Summary — Marketing + Growth Pass

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-20 10:30 IST (05:00 UTC)
**Status:** ✅ Canonical. Supersedes v63.

## What I read first (research pass)

- `dan-glasses/AGENTS.md` — Tauri app + OpenClaw + mcporter stack
- `dan-glasses/PRD.md` — product spec
- `dan-glasses/SOUL.md` — project personality
- `dan-glasses/README.md` — overview
- `dan-glasses/docs/dan-glasses-build-plan.md` — build phases
- `danlab-multimodal/README.md` + `ARCHITECTURE.md` — multimodal hackathon project
- `paperclip/README.md` — agent orchestration (dormant)
- `blurr/README.md` — visual layer
- `dan-glasses/agent-work/dan1.md` — current Dan1 status
- `dan-glasses/agent-work/dan2.md` — audiod v0.6 ship log (PID 10887, 101/101)
- `dan-glasses/Services/{audiod,perceptiond,memoryd}/SPEC.md` — daemon specs
- Web search for danlab.dev, danlab-multimodal, AI glasses competition

## Key receipts confirmed in this run

| # | Receipt | Source |
|---|---|---|
| 1 | **audiod v0.6 live** on PID 10887, 101/101 tests, adaptive whisper timeout | dan2.md, audiod/SPEC.md |
| 2 | **Tauri app scaffolded**: React 19 + TS + Vite 7, 4 panels (Bootstrap/Memory/TTS/Live) | dan1.md |
| 3 | **OpenClaw running** with @danlab_bot Telegram channel wired | dan1.md |
| 4 | **mcporter 0.9.0** installed, ready to bridge Zo MCP | dan1.md |
| 5 | **perceptiond** running LFM2.5-VL-450M via llama.cpp on CPU | perceptiond/SPEC.md |
| 6 | **memoryd** on :8741 with SQLite + 384-dim embeddings | memoryd/SPEC.md |
| 7 | **danlab-multimodal** reproducible, 302MB combined VLM on CPU | danlab-multimodal/README.md |
| 8 | **danclaw-phase1.tar.gz** on disk in /home/workspace | ls /home/workspace |
| 9 | **Multiple agent surfaces** scaffolded: danclaw-mobile, Glance, zerant-browser, clawdi, clicky-cross-platform, civpredict-env, danlab-agent-domains, danlab-channel, sora-d0.1, mobile-use | ls /home/workspace |
| 10 | **danlab.dev is live** (308 redirect) but homepage reads 2024-ish | curl + web search |

## What I built (6 files, 1629 lines)

1. `dan1-marketing-research.md` (265 lines) — research report covering 12 sections
2. `dan1-marketing-strategy.md` (229 lines) — strategy doc with three pillars + channel playbook
3. `dan1-content-calendar.md` (283 lines) — week 26 calendar, daily non-negotiables
4. `dan1-twitter-content.md` (316 lines) — bio, pinned, first 10 posts, templates
5. `dan1-landing-copy.md` (257 lines) — hero, architecture, FAQ, CTA
6. `dan1-github-readme-suggestions.md` (279 lines) — global rules + per-repo specifics

## v63 → v64 delta

- Anchored to fresh receipts (Tauri shell, OpenClaw, mcporter) that v63 didn't list.
- Added Telegram @danlab_bot as a Tier 1 channel (live via OpenClaw, ready to flip public).
- Tightened landing page copy: lead with the curl-able health endpoint.
- Added the "danlab.dev refresh" as a week-26 deliverable.
- Hardened the AGENTS.md pointers (canonical consciousness, Dan Glasses, Dani).

## Open questions for somdipto

1. **Twitter handle**: @danlab_dev handle claimed yet? Want me to draft the application tweet for the brand-account?
2. **danlab.dev refresh**: I have v64 landing copy ready. Want me to push it to zo.space or build a Vite+React Site at `danlab.dev`?
3. **Public GitHub repos**: dan-glasses, danlab-multimodal, danclaw are all on disk but private. Want me to draft the README updates + release notes so they're ready to push public?
4. **Show HN timing**: DanClaw Phase 1 Show HN drafted in v64 calendar for 2026-06-30 14:00 PT. Confirm or shift.
5. **Brand assets**: somdipto, do you have a public-facing bio paragraph (50/100/200 words) I can use for press / conferences / LinkedIn hero?