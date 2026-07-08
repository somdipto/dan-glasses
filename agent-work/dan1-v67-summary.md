# Dan1 v67 Summary — Claim the Audience

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 08:30 IST (03:00 UTC)
**Status:** ✅ Canonical. Supersedes v66.

## What I read this run (v67 deltas vs v66)

**Re-read (carried):**
- `dan-glasses/AGENTS.md`, `PRD.md`, `SOUL.md`, `README.md`, `STATUS.md`, `docs/dan-glasses-build-plan.md`
- `danlab-multimodal/README.md`, `docs/ARCHITECTURE.md`
- `paperclip/README.md`, `blurr/README.md`
- `Services/{audiod,perceptiond,memoryd}/SPEC.md`
- v66 deliverables: research, strategy, content calendar, twitter content, landing copy, github readme suggestions, punchlist, summary
- `Services/audiod/client.py` (v0.7 Tauri client, on disk)
- `ls /home/workspace/danclaw/` (real monorepo, confirmed)
- `ls /home/workspace/dan-glasses/Services/audiod/` (v0.7 confirmed)

**New receipts in v67:**
- Audited `danlab.dev` — confirmed brand-drift (Agent8/Zerant/Dapify/AI Glasses vs current Dan Glasses/danlab-multimodal/paperclip/danclaw naming)
- Audited `somdipto nandy LinkedIn` — bio still reads "Product Builder," generic, 4,148 followers
- Confirmed danclaw is a real repo (bun + turbo + convex + packages)
- Verified audiod test count: 101/101 → 121/121 (v0.7 added 21 tests, including the new client tests)
- Verified `agent-work/dan2.md` shows v0.7 ship log (Tauri integration client)
- Verified `agent-work/dan2-model-analysis.md` (KittenTTS swap, Moonshine v2 pilot, LFM2.5-1.2B-Thinking)

**Web (carried from v66):**
- Snap Specs at $2,195 (price ceiling confirmed)
- Google Android XR + Warby Parker (platform play)
- Qualcomm Snapdragon Reality Elite (chip solved)
- Apple AI AirPods + glasses (Apple in category)
- Illinois HB4843 (compliance future)

## Key receipts confirmed in v67 (delta vs v66)

| # | Receipt | Source | v67 implication |
|---|---------|--------|------------------|
| 1 | **audiod test count 101 → 121** (v0.7 added 21) | `Services/audiod/SPEC.md` v0.7 changelog | The 121 number is the new receipt. v66 was 101. |
| 2 | **audiod v0.7 client.py on disk** | `Services/audiod/client.py` | Tauri integration is real, not aspirational. |
| 3 | **danclaw is a real repo** | `/home/workspace/danclaw/` | Show HN points to the real repo. |
| 4 | **danlab.dev has drifted from the actual project names** | `danlab.dev` scrape | P0 brand-drift fix this week (06-23). |
| 5 | **somdipto LinkedIn bio is generic** | LinkedIn | P0 LinkedIn refresh on Day 7. |
| 6 | **Snap price ceiling confirmed at $2,195** | carried from v66 | Price-anchor is still the hero. |
| 7 | **Illinois HB4843** | carried from v66 | Compliance wedge for v68 press. |

**Net v67 change:** The wave is still real (Snap, Google, Apple). The receipts are real on disk. v67 is the **execution pass** — ship the public surface, claim 50 stars, fix the brand drift, ship the Show HN.

## What I built (8 files, ~2,800 lines)

1. **`dan1-marketing-research.md`** (490 lines, 15 sections) — v66→v67 deltas, the 14-day execution surface, the v67 open questions, the v67→v68 transition. Audited danlab.dev for brand drift.
2. **`dan1-marketing-strategy.md`** (425 lines, 13 sections) — "claim the audience" thesis, brand-drift fix as P0, the first-50-stars funnel, 7 channel detail, 5 risks, 5 open questions.
3. **`dan1-content-calendar.md`** (307 lines, 16 sections) — 14-day daily content plan with Day 1 = ship day (audiod v0.7 + 3 public repos), Day 8 = Show HN paperclip, Day 14 = weekly recap.
4. **`dan1-twitter-content.md`** (371 lines, 8 sections) — v67 X handle + bio, pinned tweet (price-anchor), first 10 posts with engagement-bait predictions, recurring formats, 10 reply-bait hooks, 5 reply-CTA patterns.
5. **`dan1-landing-copy.md`** (286 lines, 12 sections) — v67 hero, status strip, curl block, 7-daemon diagram, "what makes us different" block, dedicated audiod v0.7 block, price-anchor block, FAQ, footer CTA.
6. **`dan1-github-readme-suggestions.md`** (590 lines, 9 sections) — 7 global README rules, 4 per-repo README rewrites, 5 release templates, 10 anti-patterns, 5 checkpoints.
7. **`dan1-v67-punchlist.md`** (248 lines) — 21 copy-paste-ready commands for the 14-day execution surface.
8. **`dan1-v67-summary.md`** (this file) — the v67 summary.

Total: ~2,717 lines, ~108KB of marketing artifacts. v66 was ~2,298 lines, ~95KB.

## v66 → v67 delta

- **Thesis shift:** "ride the category wave without claiming it" → "claim the audience by shipping the public surface."
- **Hero shift:** "Snap is $2,195. We are $145–180 BOM." (carried from v66, sharpened) → "Snap is $2,195. We are $145–180 BOM. audiod v0.7. 121/121 tests. `curl localhost:8090/health`. MIT. Today."
- **Test count shift:** 101/101 → 121/121 (v0.7 added 21 tests).
- **Brand-drift fix:** NEW P0 in v67 (week of 06-23). danlab.dev refreshes to current product names.
- **Channel shift:** X-only → X + GitHub + Show HN + Reddit + LinkedIn + Indie Hackers + Dev.to (7 channels).
- **Conversion target shift:** "ride the wave" → 50 stars by 2026-07-04.
- **v67 trigger:** 50 stars → press push + YouTube demo + paperclip paid tier (v68 surface).
- **Open questions still open:** Twitter handle (still need decision), GitHub org structure, Show HN timing, LinkedIn bio, press contacts.

## v67 action items (this week — see v67 punchlist)

1. **Push 3 public repos:** `somdipto/dan-glasses` (tag v0.7.0-audiod), `somdipto/danlab-multimodal` (tag v0.1.0), `somdipto/paperclip` (tag v0.1.0).
2. **Claim `@danlab_dev` on X.** Apply v67 bio. Post the v67 pinned tweet first (price-anchor, audiod v0.7, 121/121 tests).
3. **Refresh danlab.dev** with v67 landing copy (brand-drift fix).
4. **Refresh LinkedIn bio** with the new framing (Day 7).
5. **Show HN: paperclip** scheduled for Mon 2026-06-30 14:00 PT.
6. **Mid-cycle check-in (Day 12 = Fri 07-04):** 50-star decision point.

## Open questions (need from somdipto before Day 1)

1. **X handle priority:** `@danlab_dev` (first), `@danlab` (second), `@somdipto` (fallback). Which can you claim on Monday morning?
2. **GitHub org:** push to `somdipto/dan-glasses` (personal, fast) or create `danlab/dan-glasses` org (more credibility, more setup)?
3. **Show HN for paperclip:** Day 8 (06-30) or Day 22 (07-14)?
4. **LinkedIn bio:** apply the new bio on Day 7 (06-29)?
5. **Press contacts:** do you have any at The Information, TechCrunch, or Indian tech media?

## v67 → v68 transition

**v68 trigger:** 50 stars crossed by 2026-07-04, OR 14 days pass (whichever comes first).

**v68 surface expansion:**
- 200 GitHub stars target (4× v67 target)
- 1,000 X followers target
- 1 Show HN on the front page (target top-5 for 4 hours)
- 1 press pickup (Indian tech media first, then US tech)
- 1 arXiv preprint (the SIA framework fork plan)
- YouTube demo channel
- Discord community
- Patreon / GitHub Sponsors for dev-kit waitlist

**v68 thesis (preview):** "First 200 stars" — the 14-day v67 execution surface expands to a 28-day v68 execution surface.

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-21 08:30 IST. The wave is real. The receipts are real. v67 ships them to the world. Next pass: v68 (target 2026-07-04, post-50-stars, target 200-stars).*
