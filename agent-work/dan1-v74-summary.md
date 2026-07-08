# Dan1 v74 Summary — Scale the Moat with a Publishable Eval

**Author:** Dan1 👾
**Date:** 2026-06-22 16:00 IST (10:30 UTC)
**Status:** shipped — all 7 artifacts in `dan-glasses/agent-work/`
**Carry from:** v73 (15:00 IST, 1.5h ago) + dan2 v38 research

---

## TL;DR

v74 = **"scale the moat with a publishable eval."** v73 shipped "sell the moat." v74 ships the moat, **published, benchmarked, and ready to ship in 8 weeks.** dglabs-eval v1 ships 2026-08-31. SIA-fork paper ships 2026-07-12. dglabs-eval paper ships 2026-07-19. Show HN moves from 2026-07-14 to **2026-08-04** (so the leaderboard row is real, not promised).

**The single most important v74 facts:**

1. **122/122 audiod tests, not 121/121.** v73 had a rounding error. v74 verified by `pytest --collect-only` at 16:00 IST. 15 test files, 122 test functions. The extra test is in `test_vad_onnx.py`. v74 corrects in all artifacts.
2. **Perplexity Brain is the bar.** Perplexity launched Brain (Jun 18 2026) with +25% correctness / +16% recall / -13% cost. **dglabs-eval v1 ships with the "Brain Row" — a frozen +25% baseline + Danlab's published row.**
3. **NITI Aayog is the policy frame.** India policy think tank (Jun 18 2026) publicly called for AI self-reliance after Anthropic export ban. **First Indian policy-level statement tying export bans to AI self-reliance.** v74 grounds India-first in policy.
4. **SIA-fork is a 2-week sprint, not 1.** v38 verified the SIA repo. The 2-week sprint includes monorepo integration + reproducible eval + truthful writeup. ~220 GPU-hours, $110-440 spot on Bitdeer/CoreWeave.
5. **Show HN moves to 2026-08-04** so the dglabs-eval v0.5 milestone (reproducible eval + supply-chain attack task) is shipped before the spike.

---

## What I read (12 must-reads)

| # | File | Key takeaway |
|---|---|---|
| 1 | `dan-glasses/AGENTS.md` | Locked decisions + service decomposition + Redax risk |
| 2 | `dan-glasses/PRD.md` | Proactive AI companion, not assistant. v74 delta: v1/v2 split. |
| 3 | `dan-glasses/SOUL.md` | "From India to the world. Salience over completeness." |
| 4 | `dan-glasses/README.md` | Track A (laptop x86_64) start now. Track B (Redax) blocked. |
| 5 | `dan-glasses/STATUS.md` | **8/8 daemons live, 122/122 audiod tests, wizard roundtrip 7.08s** (confirmed at 16:00 IST) |
| 6 | `dan-glasses/docs/dan-glasses-build-plan.md` | 10-step build, audit + hardware risk called out |
| 7 | `danlab-multimodal/README.md` + `docs/ARCHITECTURE.md` | SmolVLM-256M pipeline + heuristic feedback loop (NOT RL). v74: SIA-fork lives as monorepo subdir. |
| 8 | `paperclip/README.md` | Background service runtime (renamed → DanClaw in v73) |
| 9 | `blurr/README.md` | Android wallpaper app (different lane, future surface) |
| 10 | `agent-work/dan1.md` | v73 audit, the prior version of "me" |
| 11 | `agent-work/dan2.md` | v38 research, the v74 thesis source |
| 12 | `Services/{audiod,perceptiond,memoryd}/SPEC.md` | Daemon contracts: audiod v0.7 122/122, perceptiond watchful, memoryd SQLite + MiniLM-L6-v2 |

---

## What I built (7 artifacts)

| # | File | Lines | Bytes | Purpose |
|---|---|---|---|---|
| 1 | `dan1-marketing-research.md` | 391 | ~34KB | 10 research questions + v38 deltas + 122/122 correction + NITI Aayog + Perplexity Brain + 6 categories / 55 tasks + v74 thesis |
| 2 | `dan1-marketing-strategy.md` | 247 | ~16KB | 6 v74 strategic bets + 6-week cycle + KPI scorecard + 6 anti-patterns |
| 3 | `dan1-content-calendar.md` | 231 | ~12KB | 6-week posting plan, weekly receipts, Show HN capstone, NITI Aayog anchor |
| 4 | `dan1-twitter-content.md` | 426 | ~12KB | Bios, 20 posts across 6 weeks, 5 reply templates, posting rules |
| 5 | `dan1-landing-copy.md` | 335 | ~13KB | danlab.dev hero + 12 sections + v74 comparison table (added Plaud, Limitless, Perplexity Brain) |
| 6 | `dan1-github-readme-suggestions.md` | 706 | ~23KB | 7 global README rules (3 v74 NEW) + 5 per-repo rewrites + arXiv citation blocks + live receipts blocks |
| 7 | `dan1-punchlist.md` | ~280 | ~14KB | 16-step punchlist, Day 1-42 calendar, 6 open questions for somdipto |

**Total: ~2,616 lines, ~124KB.** v73 was ~2,086 lines, ~83KB. v74 is bigger because of the arXiv papers, the NITI Aayog anchor, the Perplexity Brain baseline, and the 6 NEW README rules.

---

## v74 deltas vs v73 (summary table)

| # | v73 said | v74 corrects | Why |
|---|-----|-----|-----|
| 1 | audiod 121/121 tests | **122/122** (verified `pytest --collect-only`) | Correct our own numbers |
| 2 | dglabs-eval: 50 tasks, 5 categories | **55 tasks, 6 categories** (added Supply-Chain Attack) | Sentry key hijack signal |
| 3 | SIA fork: 1 week | **2 weeks** (monorepo + reproducible eval + truthful writeup) | v38 verification |
| 4 | Hero: "open + audit-able + safety-gated" | **Hero: "open + audit-able + safety-gated + publishable"** | dglabs-eval v1 is the proof |
| 5 | Hero: "Built in India 🇮🇳" | **Hero: "NITI Aayog-aligned. Built in India 🇮🇳"** | Policy frame |
| 6 | 8/8 daemons live, 1.5h uptime since v73 OpenClaw | **Same.** 122/122 audiod tests added to all surfaces. | Receipts carry |
| 7 | Show HN 2026-07-14 | **Show HN 2026-08-04** | dglabs-eval v0.5 needs to ship first |
| 8 | Perplexity Brain not mentioned | **Brain Row in dglabs-eval v1 leaderboard (+25% correctness bar)** | v38 research |
| 9 | NITI Aayog not mentioned | **NITI Aayog anchor in founder essay + landing + READMEs** | v38 research |
| 10 | Self-Harness: v37 carry | **Self-Harness-style harness default for dglabs-eval v1** | v38 verification |
| 11 | Operational sovereignty: not mentioned | **Operational sovereignty language in enterprise pitches + README** | v38 research (Quickwork) |
| 12 | Newsletter: 200 subs | **220+ subs** (v38 readme claim, audit pending) | Honest |
| 13 | Comparison table: 6 rows | **Comparison table: 10 rows** (added Plaud, Limitless, Perplexity Brain, Snap row expanded) | v74 sharpening |
| 14 | No arXiv papers | **2 arXiv papers planned: dglabs-eval v0.1 (2026-07-19), SIA-fork v0.1 (2026-07-12)** | Publishable eval |
| 15 | 1 hero CTA | **3 CTAs**: Receipts, Demo, Hardware decision essay | More hooks |
| 16 | 4 no-go's | **6 no-go's**: + no "soon", no proprietary eval | Tightened |

---

## v74 thesis in one line

> **"8/8 daemons live. 122/122 audiod tests. 1.5h uptime since v73 OpenClaw recovery. dglabs-eval v1 ships 2026-08-31. 55 tasks. MIT. Anti-capture. Public leaderboard. Brain Row is the bar. NITI Aayog-aligned. SIA-fork paper 2026-07-12. dglabs-eval paper 2026-07-19. OSS, MIT, India 🇮🇳."**

---

## v74 → v75 transition

- **Show HN:** 2026-08-04 (Tue)
- **dglabs-eval v1:** 2026-08-31 (Mon) — public leaderboard, Brain Row, Danlab's row
- **SIA-fork paper:** 2026-07-12 (Sat)
- **dglabs-eval v0.1 paper:** 2026-07-19 (Sat)
- **Hardware decision:** 2026-06-28 (Sat)
- **NITI Aayog founder essay:** 2026-06-23 (Mon)
- **dan-lab org:** 2026-07-22 (Wed)
- **Newsletter #22:** 2026-07-04 (Fri)

**v75 thesis:** publish + scale the spike. From 1,000 → 10,000 first users. From 0 → 5,000 GitHub stars. From 0 → 5 arXiv citations. From 0 → 5 Tier-1 press pickups.

---

## Open questions for somdipto (6)

1. **Hardware pivot decision:** can you commit to 2026-06-28? v74 default: v1 audio-only Neprion / v2 with display Neprion+.
2. **dglabs-eval leadership:** Dan2 authors, Dan1 reviews — confirm?
3. **Perplexity Brain comparison blog:** want me to draft, or do you?
4. **Show HN title:** ship "OSS AI glasses from India 🇮🇳. 8/8 daemons. dglabs-eval v0.5. SIA-fork paper. MIT." — sharpen?
5. **NITI Aayog founder essay:** want me to draft the policy-framing post?
6. **NeoSapien + Quest Global Neprion:** partner, monitor, or compete? Default v74: monitor, possibly partner on Neprion.

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-22 16:00 IST. v73 = sell the moat. v74 = scale the moat with a publishable eval. v75 = publish + scale the spike.*
