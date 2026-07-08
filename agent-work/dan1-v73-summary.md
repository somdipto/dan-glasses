# Dan1 v73 Summary — Sell the Moat

**Author:** Dan1 👾
**Date:** 2026-06-22 15:00 IST (09:30 UTC)
**Status:** shipped — all 7 artifacts in `dan-glasses/agent-work/`
**Carry from:** v72 (post-hackathon) + dan2 v37 research

---

## TL;DR

v73 = **"sell the moat, not the wedge."** Snap closed the proactive-AI wedge with their Jul 1 launch. The moat we build in v73 is **open + audit-able + on-device + safety-gated + India-first distribution.** Every artifact ships receipts (8/8 daemons live, 121/121 audiod tests, 7.08s wizard roundtrip, World Model Hackathon win, dream-danlab live).

**The single most important v73 fact:** OpenClaw is **live again** (v72 said down — wrong, now `{"ok":true,"status":"live"}` at port 18789 since 14:42 IST 2026-06-22). v73 corrects this in the pinned tweet, in STATUS.md, and in every artifact.

---

## What I read (12 must-reads)

| # | File | Lines | Key takeaway |
|---|---|---|---|
| 1 | `dan-glasses/AGENTS.md` | 60 | Locked decisions + service decomposition + Redax risk |
| 2 | `dan-glasses/PRD.md` | 320+ | Proactive AI companion, not assistant. v1 = desktop, v2 = Redax wearable |
| 3 | `dan-glasses/SOUL.md` | 30 | "From India to the world. Salience over completeness." |
| 4 | `dan-glasses/README.md` | 90 | Track A (laptop x86_64) start now. Track B (Redax) blocked. |
| 5 | `dan-glasses/STATUS.md` | 130 | **8/8 daemons live (corrected v72).** 121/121 tests. wizard roundtrip 7.08s |
| 6 | `dan-glasses/docs/dan-glasses-build-plan.md` | 325+ | 10-step build, audit + hardware risk called out |
| 7 | `danlab-multimodal/README.md` + `docs/ARCHITECTURE.md` | 270 | SmolVLM-256M pipeline + heuristic feedback loop (NOT RL). SIA path noted. |
| 8 | `paperclip/README.md` | 90 | Background service runtime (renamed → DanClaw in v73) |
| 9 | `blurr/README.md` | 200 | Android wallpaper app (different lane, future surface) |
| 10 | `agent-work/dan1.md` | 200 | v72 audit, the prior version of "me" |
| 11 | `agent-work/dan2.md` | 7400+ | v37 research, the v73 thesis source |
| 12 | `Services/{audiod,perceptiond,memoryd}/SPEC.md` | 150 each | Daemon contracts: audiod v0.7, perceptiond watchful, memoryd SQLite+v |

---

## What I built (7 artifacts)

| # | File | Lines | Bytes | Purpose |
|---|---|---|---|---|
| 1 | `dan1-marketing-research.md` | 319 | 24,230 | 10 research questions + v37 deltas + v73 thesis |
| 2 | `dan1-marketing-strategy.md` | 196 | 10,762 | 4-week strategy, channel mix, moat story |
| 3 | `dan1-content-calendar.md` | 173 | 7,167 | 28-day posting plan, weekly receipts |
| 4 | `dan1-twitter-content.md` | 338 | 8,847 | Bios, pinned tweet, 10 first posts, threads |
| 5 | `dan1-landing-copy.md` | 262 | 8,031 | danlab.dev hero, features, CTA, dev-kit section |
| 6 | `dan1-github-readme-suggestions.md` | 473 | 12,628 | 5 repo READMEs + org README + 8-sec test |
| 7 | `dan1-punchlist.md` | 281 | 9,621 | 22 actionable commands + Day 1-21 calendar |

---

## v73 deltas vs v72

| # | v72 said | v73 corrects |
|---|---|---|
| 1 | OpenClaw down | **OpenClaw live since 14:42 IST** — corrected in pinned tweet + STATUS |
| 2 | 7/8 daemons | **8/8 daemons** (live now) |
| 3 | 121/121 audiod tests in v72 punchlist | **Confirmed live, kept in v73** |
| 4 | "OpenClaw-as-default wedge" | **Wedge closed by Snap.** Moat = open + audit-able + safety-gated + dglabs-eval |
| 5 | Hardware: Redax (unfinalized) | **Hardware pivot decision due 2026-06-28.** Default v73: Quest Global Neprion |
| 6 | 500 first users expected | **775 first users expected** (+150 world-model researchers, +50 India builders, +75 safety researchers) |
| 7 | v72 → v73: "scale the spike" | **v73 → v74: "ship the moat"** — Show HN 2026-07-14, dglabs-eval 2026-07-21 |

---

## v73 thesis in one line

> **"8/8 daemons live. 121/121 audiod tests. Open + audit-able + safety-gated proactive AI. dglabs-eval Q3. SIA fork this week. OSS, MIT, India 🇮🇳."**

---

## v73 → v74 transition

- **Show HN:** 2026-07-14 (Mon)
- **dglabs-eval v0.1:** 2026-07-21 (Mon)
- **SIA fork v0.2:** 2026-07-08 (Tue)
- **Safety subset v0.1:** 2026-06-26 (Thu)
- **Hardware pivot commit:** 2026-06-28 (Sat)
- **MIT Tech Review pitch:** 2026-07-02 (Wed)
- **Newsletter #22:** 2026-07-11 (Fri)

**v74 thesis:** scale the spike. 775 → 7,500 first users. 0 → 1,000 GitHub stars. 1 → 5 Tier-1 press pickups.

---

## Open questions for somdipto (5)

1. **Hardware pivot decision:** can you commit to 2026-06-28?
2. **dglabs-eval leadership:** Dan2 authors, I review — confirm?
3. **MIT Tech Review pitch:** want me to draft, or do you?
4. **Show HN title:** ship "OSS AI glasses from India. 8/8 daemons. dglabs-eval. SIA-fork." — sharpen?
5. **NeoSapien + Quest Global Neprion:** partner / monitor / compete — default v73: monitor.

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-22 15:00 IST. v71 = OpenClaw-as-default. v72 = post-AWE receipts. v73 = sell the moat.*
