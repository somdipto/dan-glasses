# Dan1 v66 Summary — Ride the Category Wave

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 07:30 IST (02:00 UTC)
**Status:** ✅ Canonical. Supersedes v65.

## What I read this run (v66 deltas vs v65)

**Re-read (carried):**
- `dan-glasses/AGENTS.md`, `PRD.md`, `SOUL.md`, `README.md`, `docs/dan-glasses-build-plan.md`
- `danlab-multimodal/README.md`, `docs/ARCHITECTURE.md`
- `paperclip/README.md`, `blurr/README.md`
- `Services/{audiod,perceptiond,memoryd}/SPEC.md`
- v65 deliverables: `dan1-marketing-research.v65.md`, `dan1-marketing-strategy.v65.md`, `dan1-content-calendar.v65.md`, `dan1-twitter-content.v65.md`, `dan1-landing-copy.v65.md`, `dan1-github-readme-suggestions.v65.md`
- v65 punchlist + v65 summary

**New receipts in v66:**
- `agent-work/dan2.md` — audiod v0.7 (Tauri integration client, ship log)
- `Services/audiod/client.py` — new file (audiod v0.7 deliverable, real on disk)
- `agent-work/dan2-model-analysis.md` — v0.7 model strategy (KittenTTS → Orca swap, Moonshine v2 pilot, LFM2.5-1.2B-Thinking)
- `agent-work/dan2-architecture-review.md` — v0.6 → v0.7 architecture review
- `agent-work/dan2-agi-roadmap.md` — v0.7 AGI roadmap (2026–2028)
- `ls /home/workspace/danclaw/` — confirmed real monorepo (bun + turbo + convex + packages)
- `ls /home/workspace/dan-glasses/Services/audiod/` — confirmed `client.py` exists alongside `audiod.py`

**Web (new receipts, the category explosion):**
- Snap Specs unveiled 06-16 at $2,195 — NPR, NY Post, Yahoo Finance
- Google Android XR + Warby Parker + Gentle Monster (I/O 05-19)
- Qualcomm Snapdragon Reality Elite (06-16)
- Illinois HB4843 — smart glasses while driving ban
- Apple AI AirPods + glasses — Bloomberg via NY Post (06-16)

**Critical new file detected:** `Services/audiod/client.py` — audiod v0.7 Tauri integration client is on disk and shipped.

## Key receipts confirmed in v66 (delta vs v65)

| # | Receipt | Source | v66 implication |
|---|---------|--------|------------------|
| 1 | **Snap Specs at $2,195** — Spiegel "new era of computing," 132g, two Snapdragons, ad-supported | NPR/NY Post/Yahoo 06-16/19 | Price ceiling now confirmed. $145–180 BOM is 12× cheaper. **Price-anchor IS the hero.** |
| 2 | **Google Android XR + Warby Parker + Gemini** | Glass Almanac + I/O recap | Category confirmed by Google. We are the open-source OS, not a Google partner. |
| 3 | **Qualcomm Snapdragon Reality Elite** | CNBC 06-16 | Chip is solved by Qualcomm. We don't fight on chip. We don't need a custom chip for v1. |
| 4 | **Illinois HB4843** — smart-glasses driving ban | govtech.com 06-20 | On-device is going to be compliance, not marketing. Already on-device by default. |
| 5 | **Apple AI AirPods + glasses** — Bloomberg via NY Post | NY Post 06-16 | Apple is in the category. 14-month indie window unchanged. |
| 6 | **audiod v0.7 ships** — Tauri integration client on disk | `Services/audiod/client.py` + `dan2.md` | New receipt for week-26 marketing. Monday 06-23 ship is v0.7.0-audiod, not v0.6.0. |
| 7 | **KittenTTS swap → Orca/Piper** (10× latency, 10× RAM win) | `dan2-model-analysis.md` | New substance for week-27 technical post. |
| 8 | **Moonshine v2 STT pilot** (vs whisper.cpp) | `dan2-model-analysis.md` | Future technical post (week 28+). |
| 9 | **LFM2.5-1.2B-Thinking for tool planning** | `dan2-model-analysis.md` | Substance for the toold daemon roadmap. |
| 10 | **danclaw is a real repo** — bun + turbo + convex monorepo | `ls /home/workspace/danclaw/` | Show HN points to real repo, not tarball. |

**Net v66 change:** The category exploded in the last 7 days. Snap, Google, Qualcomm, Apple, Illinois — all in. We don't move. We narrate. Every v66 artifact now leads with a price-anchor and rides the Snap-week news cycle without overclaiming.

## What I built (6 files, ~2,298 lines)

1. **`dan1-marketing-research.md`** (333 lines, 14 sections) — refreshed with post-Snap-week competitor table (Snap, Google, Qualcomm, Apple, Illinois HB4843), audiod v0.7 anchor, dan2 v0.7 model analysis, danclaw real-repo update
2. **`dan1-marketing-strategy.md`** (292 lines, 11 sections) — "ride the category wave without claiming it" thesis, price-anchor as the new headline claim, v66 tone examples (Snap, Illinois)
3. **`dan1-content-calendar.md`** (504 lines, 15 sections) — week 26 calendar with audiod v0.7 ship, Snap-week Reddit post-mortem, Snap-week X thread, Illinois HB4843 thread, week 27 preview (KittenTTS swap post)
4. **`dan1-twitter-content.md`** (405 lines, 11 sections) — v66 pinned tweet (price-anchor), first 10 posts (Monday 06-23 = audiod v0.7, not v0.6)
5. **`dan1-landing-copy.md`** (329 lines, 14 sections) — hero with price-anchor line under headline, v0.7 audiod row in status strip, v66 price-anchor block, FAQ updated for audiod v0.7 + Snap-week
6. **`dan1-github-readme-suggestions.md`** (435 lines, 34 sections) — global rules + per-repo READMEs updated for audiod v0.7, v0.7.0-audiod release template, price-anchor line in dan-glasses README

Total: ~2,298 lines, ~95KB of marketing artifacts (v65 was ~2,032 lines, ~85KB).

## v65 → v66 delta

- **Thesis shift:** "ship the public surface" → "ride the category wave without claiming it."
- **Hero shift:** "audiod v0.6 is live. Curl it." → "Snap is $2,195. We are $145–180 BOM. audiod v0.7 ships a Tauri client. The category is confirmed; the cost is not. We're the cost."
- **audiod shift:** v0.6 → v0.7 (Tauri client on disk, 8+ integration tests, 4 stubbed-transport tests).
- **danclaw shift:** `danclaw-phase1.tar.gz` → real monorepo at `/home/workspace/danclaw/`.
- **New competitor intel:** Snap Specs $2,195, Google Android XR + Warby Parker, Qualcomm Reality Elite, Apple AI AirPods, Illinois HB4843.
- **Compliance posture:** New v66 narrative layer (file for v67 press, not v66 social).
- **New week-27 hooks:** KittenTTS swap post (Orca/Piper), Moonshine v2 STT pilot post, audiod v0.7.1 release tag.
- **Open questions still open:** Twitter handle, public GitHub push, danlab.dev refresh, brand bio (third pass), Telegram public flip, Show HN timing.

## v66 action items (this week — see v66 punchlist)

1. **Push 3 public repos:** `somdipto/dan-glasses` (tag `v0.7.0-audiod`), `somdipto/danlab-multimodal` (tag `v0.1.0`), `somdipto/danclaw`.
2. **Claim @danlab_dev** on X. Post the v66 pinned tweet first (price-anchor, audiod v0.7).
3. **Flip @danlab_bot to public** on Telegram.
4. **Refresh danlab.dev** with v66 landing copy.
5. **Show HN draft for DanClaw Phase 1** (now pointing to real repo), scheduled 2026-06-30 14:00 PT.
6. **Ship the Snap-week post-mortem thread** on Friday 06-27 18:00 IST (7 tweets).
7. **Ship the Illinois HB4843 thread** on Thursday 06-26 21:00 IST (v67-compliant frame, file for press).
8. **Commit the v66 READMEs** to the public repos.

## What v66 does NOT do (carried from v65, hardened)

- Does not run ads.
- Does not pitch investors.
- Does not publish a podcast.
- Does not sponsor events.
- Does not promise hardware dates.
- Does not ship a landing page that overstates.
- Does not claim RL.
- Does not claim AGI.
- Does not name competitors in the README (except the price-anchor line in `dan-glasses/README.md` hero).
- Does not use "Snap-killer" framing. We are the cost, not the killer.
- **v66 new:** Does not lead with origin. Lead with architecture. Origin is the punctuation, not the sentence (especially in the Show HN post).

## What I will NOT do without your sign-off (carried from v65)

- Push anything to a public GitHub repo.
- Refactor danlab.dev.
- Submit a Show HN post (first HN submission from this account).
- Send the application tweet for @danlab_dev.
- Flip @danlab_bot Telegram channel to public.
- **v66 new:** Send the v66 pinned tweet (it price-anchors against Snap and Google; first impression sets the brand voice).
- **v66 new:** Post the Illinois HB4843 thread (it asserts a compliance posture — careful framing).

## Open questions for somdipto (v66 — third pass on some)

1. **Twitter handle:** Claim @danlab_dev this week? Want me to draft the application tweet? (v65 + v64 asked.)
2. **danlab.dev refresh:** v66 landing copy ready. Push to zo.space or build a Vite+React Site? (v65 + v64 asked.)
3. **Public GitHub repos:** Push 3 repos this week with v66 READMEs and tags? (v65 + v64 asked.)
4. **Show HN timing:** DanClaw Phase 1 Show HN on 2026-06-30 14:00 PT — confirm or shift? (v65 + v64 asked.)
5. **Brand assets:** somdipto, do you have a public-facing bio paragraph (50/100/200 words) for press / conferences / LinkedIn hero? **Third pass asking. This won't die until we get it.**
6. **Telegram @danlab_bot:** Flip to public this week?
7. **Snap-week thread:** Ship the "What Snap's $2,195 Specs means for the open-source alternative" 7-tweet thread on Friday 06-27? Or is it too reactive?
8. **KittenTTS swap post:** v66 calendar has a 500-word technical post on the KittenTTS → Orca swap in week 27. Want me to draft now or wait for code?
9. **Show HN repo:** v66 draft points to `/home/workspace/danclaw/` (real monorepo). Confirm or use the tarball?
10. **Illinois HB4843 thread:** Post Thursday 06-26? It sets a compliance posture that you'll be quoted on.

## v66 → v67 transition

v66 will run again on 2026-06-28 (Sunday) with a one-week re-read of:
- Show HN results (points, comments, new accounts reached)
- Repo stars across the 3 public repos
- @danlab_dev traction (if handle claimed)
- Telegram @danlab_bot subscribers
- Reddit thread upvotes
- HackerNoon / Substack / Medium inbound

v67 will be the "first 50 stars" pass — same triggers as v66 → v67, but with v66 numbers attached. If audiod + danlab-multimodal cross 50 GitHub stars by 07-04, v67 will:
1. Open the public mailing list.
2. Open the waitlist for v1 desktop companion.
3. Plan the AWE 2027 application.
4. Draft the press list with somdipto's short bio (THIRD PASS STILL).
5. Open the danlab.dev refresh to public beta (collect email).
6. Spin up a Discord/Matrix per daemon.
7. **v66 new:** Submit the KittenTTS swap post to HackerNoon + IndiaAI dispatch + YourStory.
8. **v66 new:** Draft a "compliance posture" 1-pager for Tier 1 press (Bartone v. Meta + Illinois HB4843 framing).

**Filed under:** `agent-work/dan1-v66-summary.md`