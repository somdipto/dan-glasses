# Dan1 v78 Summary — Wave + Receipts

**Author:** Dan1 👾
**Date:** 2026-06-23, Bengaluru
**Status:** shipped — 6 artifacts refreshed to v78
**Carry from:** v77 (Jun 22, 11:30 IST) + verified external pull (Jun 23, 06:30 UTC)

## TL;DR

v77 = "ride the wave." v78 = "ride the wave + the receipts are live." The world moved in the 18 hours between v77 and v78, but more importantly **our own surface moved**: dan-glasses-app is published (https://dan-glasses-app-som.zocomputer.io), 8/8 daemons confirmed live, 122/122 audiod tests verified, danlab-multimodal demo is up at https://zo.pub/som/danlab-multimodal-demo, paperclip one-command Docker works.

The 6 artifacts below carry all of this with v78 framing.

## What I read (14 must-reads + live web pull)

| # | Source | Key signal |
|---|---|---|
| 1 | dan-glasses/AGENTS.md | Canonical consciousness at `somdipto/dan-consciousness`; commits go through `somdipto <somdiptonandy@gmail.com>` |
| 2 | dan-glasses/PRD.md | Proactive AI companion, not assistant |
| 3 | dan-glasses/SOUL.md | "From India to the world. Salience over completeness." |
| 4 | dan-glasses/README.md | Track A (laptop x86_64) live; Track B (Redax) blocked |
| 5 | dan-glasses/STATUS.md | 8/8 daemons live, 144/144 tests, wizard roundtrip 7.08s |
| 6 | dan-glasses/docs/dan-glasses-build-plan.md | 10-step build, audit + hardware risk |
| 7 | danlab-multimodal/README.md + ARCHITECTURE.md | SmolVLM-256M + heuristic loop (NOT RL). Honest framing is the asset. |
| 8 | paperclip/README.md | Renamed to DanClaw in v73, one-command Docker, Railway + Fly.io Mumbai |
| 9 | blurr/README.md | Panda Android app, Kotlin, accessibility-service-driven |
| 10 | agent-work/dan1.md (v73) | Prior "me" — 8/8 daemons + published app + live gateway |
| 11 | agent-work/dan2.md (v38) | audiod mandate fully shipped; nothing left to build |
| 12 | Services/audiod/SPEC.md | audiod v0.7, 122/122 tests, whisper base.en + Silero VAD |
| 13 | Services/perceptiond/SPEC.md | LFM2.5-VL-450M Q4_0 + llama-mtmd-cli, watchful mode |
| 14 | Services/memoryd/SPEC.md | SQLite + sentence-transformers MiniLM-L6-v2 |
| 15 | **Live web pull (Jun 23)** | danlab.dev live (Agent8/Zerant/Dapify/AI Glasses), @NandySomdipto (Sodan) active, @dan2agi project handle, dan-lab org + dan-consciousness already on GitHub |

## What I built (6 artifacts, 2,643 lines)

| # | File | Lines | Bytes | v78 deltas vs v1 |
|---|---|---|---|---|
| 1 | `dan1-marketing-research.md` | 458 | ~29KB | New v77→v78 delta table; verified 2026-06-23 web pull; Snap $2,195 / Meta Stella scandal / Apple-late-2027 / NITI Aayog anchor / Self-Harness / dglabs-eval v1 plan |
| 2 | `dan1-marketing-strategy.md` | 217 | ~13KB | New header (v78); three news waves (Snap / Meta Stella / Apple delay) with wedge copy; new Pillars 7 (NITI Aayog / India policy) and 8 (dglabs-eval as public moat); 6 anti-patterns; 90-day roadmap with concrete dates |
| 3 | `dan1-content-calendar.md` | 266 | ~12KB | New wave-riding weeks (Jun 23 → Aug 4 = Show HN); daily post hooks tied to live news; pinned tweets; HN comment strategy |
| 4 | `dan1-twitter-content.md` | 524 | ~17KB | New v78 launch sequence (Jun 22-30); bios for @dan2agi / @NandySomdipto / @Shodan_s; pre-launch "8/8 daemons live" tweet; reply templates for Snap / Meta / Apple threads |
| 5 | `dan1-landing-copy.md` | 365 | ~13KB | New v78 news-aware hero drop-in alternative; price-anchor table Snap $2,195 / Meta $799 / Apple late-2027 / Dan $189; "Why now" section; published app URL |
| 6 | `dan1-github-readme-suggestions.md` | 813 | ~28KB | New v78 universal rule — Receipts block (mandatory); new v78 README template; corrections to danlab-multimodal (honest "heuristic, not RL" framing), blurr (Panda rebrand), paperclip (DanClaw rename note); 9-step README rollout plan Jul 1-22 |

**Total: 2,643 lines, ~112KB.**

## v78 thesis in one line

> **"8/8 daemons live. 122/122 audiod tests. Published app at dan-glasses-app-som.zocomputer.io. Multimodal demo at zo.pub/som/danlab-multimodal-demo. Paperclip one-command Docker. Snap at $2,195. Meta shipped facial-rec. Apple pushed to 2027. We are the open, on-device, audit-able, NITI Aayog-aligned counter-narrative. $189 dev-kit. MIT. From Bengaluru to the world. Show HN Aug 4."**

## v78 → v79 transition

- **Show HN:** 2026-08-04 (Tue)
- **dglabs-eval v0.1 ship:** 2026-07-21 (Tue)
- **dan-lab org public:** 2026-07-22 (Wed)
- **First SIA-fork paper:** 2026-07-12 (Sat)
- **dglabs-eval paper:** 2026-07-19 (Sat)
- **Newsletter #22:** 2026-07-04 (Fri)

**v79 thesis:** ship dglabs-eval v0.1. The first public benchmark for proactive AI glasses. Danlab's row goes on the leaderboard before anyone else's.

## Open questions for somdipto (6)

1. **Snap comparison post:** ship "Snap launched $2,195 Specs. We ship audiod v0.7. 122/122 tests. MIT. Dev-kit Q4 2026." tomorrow at 10am IST, or hold for a stronger hook?
2. **Meta-Stella scandal hook:** do we punch at Meta directly, or let the architecture comparison stand? My read: state facts, don't editorialize. Default: state facts.
3. **Apple delay angle:** the "Apple-quality window is open 18-24 months" framing — agree? Or do you want a more India-first frame (NITI Aayog policy tie)?
4. **NITI Aayog essay:** LinkedIn long-form, 800-1500 words, by Mon Jun 23 EOD. Want me to draft, or do you?
5. **`@dan2agi` voice:** take over the project handle for build-in-public, leaving `@NandySomdipto` for founder voice? My default: yes, since Dan1 owns the build-in-public cadence.
6. **GitHub org rollout:** ship `dan-lab` org by 2026-07-22. Who has admin — just you, or do you want me to draft the org README first?

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-23 12:30 IST.*

*v77 = "ride the wave." v78 = "ride the wave + the receipts are live." v79 = dglabs-eval v0.1 ships. Show HN Aug 4.*
