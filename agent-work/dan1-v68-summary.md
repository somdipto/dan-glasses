# Dan1 v68 Summary — Build the Inbound

**Author:** Dan1 (Head of Marketing + Growth, DanLab) 👾
**Date:** 2026-06-21 09:30 IST (04:00 UTC)
**Status:** ✅ Canonical. Supersedes v67.

## What I read this run (v68 deltas vs v67)

**Re-read (carried):**
- v67 deliverables: research, strategy, content calendar, twitter, landing copy, github readme, punchlist, summary
- `dan-glasses/AGENTS.md`, `PRD.md`, `SOUL.md`, `README.md`, `STATUS.md`
- `Services/{audiod,perceptiond,memoryd}/SPEC.md` (audiod v0.7 confirmed, 121/121 tests)
- `danlab-multimodal/README.md`, `docs/ARCHITECTURE.md`
- `paperclip/README.md` (DanClaw framing confirmed)
- `blurr/README.md` (Kotlin/Android — appears dormant)
- `DanLab_Pitch_Deck.md` (pre-rebrand naming: "Dan Voice / Dan Glasses / Dan Company")
- `agent-work/dan1.md`, `agent-work/dan2.md` (latest stream statuses)

**New receipts in v68:**
- **Web:** Snap Specs at $2,195 confirmed by TechCrunch, WIRED, Verge, Mashable, UploadVR (06-16 → 06-20). WIRED adds "no puck, no tether" framing (direct jab at Vision Pro). Verge adds 132g/136g weights.
- **Meta Ray-Ban Display with neural band** is a 2026 incumbent (UploadVR). Daily-usage-tripled. Dan Glasses is the *third path* — open-source + on-device.
- **Meta is opening Quest & smart-glasses demo sections in 50 Best Buys** (UploadVR) — distribution play for incumbents.
- **Apple did NOT cancel the Vision headset line** (UploadVR 06-11) — Apple is in the category, just slow.
- **Search for "danlab.dev"** returns zero of our surface. **No danlab.dev search presence yet.** v68's #1 job is to fix that.
- **Search for "Dan Glasses somdipto"** returns zero organic. v67's pinned tweet hasn't shipped (gated on somdipto's sign-off).
- **Pitch deck** uses pre-rebrand naming (Dan Voice / Dan Glasses / Dan Company) — needs reconciliation on the landing page.

## v67 → v68 thesis shift

- **v67 thesis:** "Claim the audience by shipping the public surface." — 3 repos go public, @danlab_dev gets claimed, Show HN draft, 14-day funnel.
- **v68 thesis:** "Build the inbound." — every tweet, every HN post, every Reddit comment bounces off the README. A README is not a destination. **A real landing page with a real blog and RSS is.**

The math:
- Pinned tweet: 50–500 clicks/day.
- Show HN front page: 5,000–20,000 clicks in 4 hours.
- Reddit r/LocalLLaMA: 1,000–3,000 clicks in 24 hours.
- A second-time visitor needs a *reason* to come back. A blog is that reason. RSS is the channel.

**v68 is the first time DanLab has a destination on the open web that is not a GitHub README.**

## v67 → v68 hero shift

- **v67 hero:** "Snap is $2,195. We are $145–180 BOM. audiod v0.7 ships a Tauri client."
- **v68 hero:** "**No phone. No cloud. No subscription. No ads.** The proactive AI companion, MIT-licensed, on-device. From India."

The 4 "no"s name the *category* of objection, not the dollar amount. Snap is $2,195. Meta is $800+ with phone-tether. Apple is $3,499+ with Vision Pro battery. Android XR + Warby Parker is Gemini-cloud. Even Realities G1 is $399 but phone-tethered. **None of them are free of all 4 "no"s.** Dan Glasses is all four.

## What I built (6 files, ~1,920 lines, ~95KB)

1. **`dan1-marketing-research.v68.md`** (226 lines) — v68 research with the 10-question answers, the v67→v68 thesis shift, the 4 "no"s hero, the 132g weight comparison, the v68→v69 transition.
2. **`dan1-marketing-strategy.v68.md`** (233 lines) — "build the inbound" thesis, the 3 destinations (landing/blog/roadmap), the 7 channel detail (refreshed for inbound), the 4 risks, the 5 open questions.
3. **`dan1-content-calendar.v68.md`** (222 lines) — 14-day calendar with every day adding a blog post or a roadmap update. The v67 X content is preserved. v68 makes every tweet link to a destination.
4. **`dan1-twitter-content.v68.md`** (470 lines) — v68 bio with 4 "no"s, v68 pinned tweet (sharpened), 10 first posts (with link to blog in every tweet), recurring formats (blog digest, weekly repo stat), reply-bait hooks.
5. **`dan1-landing-copy.v68.md`** (327 lines) — v68 hero (4 "no"s), 30-second explainer, curl receipts, 7-daemon diagram, "what makes us different" block, 4 "no"s pillar section, FAQ.
6. **`dan1-github-readme-suggestions.v68.md`** (489 lines) — 7 global README rules, 4 per-repo README rewrites, 5 release templates, 10 anti-patterns, 5 checkpoints — all hardened with the 4 "no"s one-liner.

Total: ~1,967 lines, ~95KB. v67 was ~2,717 lines, ~108KB. v68 is leaner because it removes the v67 sprawl and re-anchors to the inbound.

## Key v68 deltas vs v67 (summary table)

| # | v67 | v68 | Why |
|---|-----|-----|-----|
| 1 | Thesis: "claim the audience" | Thesis: "build the inbound" | Stars are downstream of *people landing somewhere real.* |
| 2 | Hero: "Snap is $2,195. We are $145–180 BOM." | Hero: "No phone. No cloud. No subscription. No ads." | The 4 "no"s name the *category* of objection, not the dollar. |
| 3 | audiod v0.7 is the hero | audiod v0.7 is one of 4 demos in a status strip | Receipts belong in §3, not §1. |
| 4 | 14-day funnel, X-only | 14-day funnel, X + GitHub + HN + Reddit + LinkedIn + Dev.to + RSS | Inbound is multi-channel. |
| 5 | Conversion target: 50 stars | Conversion target: 50 stars + 50 RSS subs | Stars alone are vanity. RSS is compounding. |
| 6 | Show HN for paperclip (Day 8) | Show HN for paperclip (Day 8) **+** Dan Glasses (v69) | Two shots, not one. |
| 7 | Blog = optional | Blog = required (RSS-first, Atom + JSON Feed) | RSS is the moat. |
| 8 | Pitch deck naming: "Dan Voice / Dan Glasses / Dan Company" | Pitch deck reconciled on landing to "Dan Glasses / danlab-multimodal / paperclip / danclaw" | Brand-drift fix #2. |
| 9 | Snap weight: not in the comparison | Snap weight: 132g vs Dan Glasses BOM is a *comparable weight, 12× cheaper* claim | Direct comparison is sharper. |
| 10 | 4 "no"s: not used | 4 "no"s: the new tagline | Names the *category* of objection. |

## v68 action items (this week — see v68 punchlist)

1. **Build the inbound surface:**
   - `danlab.dev/` → 4 "no"s hero (replace v67 price-anchor hero).
   - `danlab.dev/blog/` → first 3 posts (welcome, no-phone, no-cloud).
   - `danlab.dev/feed.xml` → RSS feed (Atom + JSON Feed).
   - `danlab.dev/roadmap` → Now/Next/Later/Someday.
2. **Push 3 public repos** (carried from v67): `somdipto/dan-glasses`, `somdipto/danlab-multimodal`, `somdipto/paperclip`.
3. **Claim @danlab_dev** on X (carried from v67). Apply v68 bio. Post the v68 pinned tweet first.
4. **Open the newsletter** (Buttondown or self-hosted) — Issue #0 ships Day 1.
5. **Cross-post to Dev.to and Hashnode** (auto via RSS).
6. **Reconcile the pitch deck** with the new naming (separate task — `danlab.dev/pitch` if somdipto approves).
7. **Show HN: paperclip** (Day 8, 06-30 14:00 PT, carried from v67).

## What v68 does NOT do (carried from v67)

- Does not run ads.
- Does not pitch investors.
- Does not publish a podcast.
- Does not sponsor events.
- Does not promise hardware dates.
- Does not ship a landing page that overstates.
- Does not claim RL.
- Does not claim AGI.
- Does not name competitors in the README (Snap price-anchor line is the only exception, and even that is on the landing page, not the README).
- Does not use "Snap-killer" framing. We are the cost, not the killer.
- Does not use "AGI from India" as a tag in marketing.
- **v68 new:** Does not publish the blog without RSS. RSS-first or it doesn't ship.
- **v68 new:** Does not auto-post to LinkedIn, X, or Reddit. Each post is a manual decision.
- **v68 new:** Does not link the blog to Medium / Substack / Hashnode subdomain. Self-host or it isn't ours.
- **v68 new:** Does not collect email addresses before the privacy policy is on a /privacy page.
- **v68 new:** Does not promise a Discord before 100 GitHub stars across the 3 public repos.

## Open questions for somdipto (v68 — fourth pass on some)

1. **X handle:** Claim @danlab_dev this week? Want me to draft the application tweet? (v66 + v67 + v68 — third pass.)
2. **danlab.dev refresh:** v68 landing copy ready. Push to zo.space or build a Vite+React Site? (v66 + v67 + v68 — third pass.)
3. **Public GitHub repos:** Push 3 repos this week with v68 READMEs and tags? (v66 + v67 + v68 — third pass.)
4. **Show HN timing:** paperclip Show HN on 2026-06-30 14:00 PT — confirm or shift? (v66 + v67 + v68 — third pass.)
5. **Brand assets:** somdipto, do you have a public-facing bio paragraph (50/100/200 words) for press / conferences / LinkedIn hero? **Fourth pass asking. This is now a stuck log.**
6. **Telegram @danlab_bot:** Flip to public this week? (v66 + v67 + v68 — third pass.)
7. **Snap-week thread:** Ship the "What Snap's $2,195 Specs means for the open-source alternative" 7-tweet thread on Friday 06-27? Or is it too reactive? (v66 + v67 + v68 — third pass.)
8. **Newsletter platform:** Buttondown (free, $9/mo paid), Substack (1-click but hosted), or self-hosted (Plunk + Postgres)? (v68 new — first pass.)
9. **RSS feed: full content or summary?** Atom + JSON Feed standard is summary. v68 default = summary, click-through to danlab.dev/blog. (v68 new — first pass.)
10. **Pitch deck reconciliation:** v68 names: Dan Glasses / danlab-multimodal / paperclip / danclaw. Pitch deck names: Dan Voice / Dan Glasses / Dan Company. Reconcile in `danlab.dev/pitch` or rewrite the pitch deck? (v68 new — first pass.)

## v68 → v69 transition

**v68 trigger:** 14 days from 2026-06-21 (= 2026-07-05) OR 100 RSS subscribers crossed, whichever comes first.

**v69 surface expansion:**
- 200 GitHub stars target
- 500 RSS subscribers
- 1 Show HN on the front page (paperclip or Dan Glasses)
- 1 YouTube demo (90-second "audiod in 90 seconds")
- 1 newsletter sponsorship (sponsor a tiny newsletter like prigozhin or similar)
- First press push (India tech media first)
- Discord community (per-daemon channels)

**v69 thesis (preview):** "First 1,000 readers" — turn the inbound into a community.

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-21 09:30 IST. v67 ships the surface. v68 ships the inbound. v69 ships the community.*
