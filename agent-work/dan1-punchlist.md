# Dan1 v84 — Punchlist (12 P0 items, by Show HN → Pre-orders)

**Author:** Dan1 👾 — co-founder, head of marketing + growth, DanLab
**Date:** 2026-06-24 15:00 IST (09:30 UTC)
**Companion:** `dan1-marketing-research.md`, `dan1-marketing-strategy.md`, `dan1-content-calendar.md`, `dan1-twitter-content.md`, `dan1-landing-copy.md`, `dan1-github-readme-suggestions.md`
**Status:** v84. Supersedes v83 punchlist (which was a section of the strategy doc, not a standalone file).

---

## v84 TL;DR

- **v84 is a v83-punchlist-promoted-to-standalone refresh.** All 12 v83 P0 items still apply. v84 adds **3 new items** (13, 14, 15) for the Muse Spark coverage window + the dev-kit FAQ + the founder essay tertiary CTA.
- **The 5-min install benchmark is the v84 critical path.** If we don't hit it by Jul 13, the Show HN launch is at risk. Currently 7m08s.
- **Show HN is 32 days away (Aug 25, 2026).** The single highest-leverage launch lever in 2026.

---

## Phase 1: Before Show HN (Aug 25) — 9 items

### 1. `danlab.dev/install` — install-oneliner live + sub-5min
- **Owner:** Dan2 (technical) + Dan1 (copy + badge)
- **Due:** Jul 13 (Sunday) — sub-5min benchmark; Aug 18 — fully polished
- **Definition of done:** `curl -fsSL danlab.dev/install | bash` runs on a fresh Debian 12 x86_64 + aarch64 box, installs 8 daemons, prints "you're in", and exits 0. **Sub-5min install-to-talking-to benchmark hit (currently 7m08s).**
- **Counter for failure:** The single biggest risk in v84. If the oneliner breaks on Show HN, the comment "I tried to install and it didn't work" kills the launch. Dan2 owns uptime + rollback.

### 2. `danlab.dev/dan-glasses` — product page live
- **Owner:** Dan1 (copy per `dan1-landing-copy.md` v84) + Dan2 (technical FAQ)
- **Due:** Jul 5
- **Definition of done:** Live at `danlab.dev/dan-glasses` with the 12-section structure from `dan1-landing-copy.md` v84. Live infra ticker auto-refreshes every 30s.
- **Counter for failure:** v81 missed this. v83 made it critical-path. v84 confirms the Jul 5 deadline and the 12-section structure.

### 3. `danlab.dev/blog/from-9-to-5-to-agi` — founder essay
- **Owner:** somdipto (author) + Dan1 (edit)
- **Due:** Jul 7
- **Definition of done:** 2,000-3,000 words. Founder voice. India angle. The honesty-about-pre-RL moment. The Meta-Stella-surrender moment. The ₹12K-and-₹4,999 moment. The "Apple ships late 2027" moment.
- **Counter for failure:** The essay is the share-link. If it's generic, no one shares it.

### 4. `github.com/somdipto/dan-glasses` — README rewrite
- **Owner:** Dan1 (per `dan1-github-readme-suggestions.md` v84) + Dan2 (technical accuracy)
- **Due:** Jul 10
- **Definition of done:** Universal template applied. Hero GIF (30s loop). Install-oneliner as primary CTA. Comparison table (vs Ray-Ban Meta, Even Realities G2, Apple Vision Pro). 8-daemons list. Footer with founder credit + India flag + signed releases + no covert updates.
- **Counter for failure:** The README is the first-conversion surface. If it's corporate, the launch loses.

### 5. `github.com/somdipto/dglabs-eval v0.1` — open eval repo
- **Owner:** Dan2 (technical) + Dan1 (framing)
- **Due:** Jul 12 (private); Jul 25 (public)
- **Definition of done:** Repo is private Jul 12, public Jul 25 (post-Show-HN). README explains the eval design. 5 baseline rows seeded (Dan Glasses, SmolVLM-256M, Moondream2, GPT-4V, Claude 3.5 Sonnet). Anyone can submit a row via PR (48-hour SLA).
- **Counter for failure:** The eval is the moat. If we ship it late or with no baselines, we lose the "open" claim.

### 6. `danlab.dev/show` — Show HN landing
- **Owner:** Dan1
- **Due:** Jul 10 (first cut); Aug 18 (final)
- **Definition of done:** One-page. Curl command visible above the fold. 60-second demo GIF embedded. "What ships first" comparison table. "What's next" roadmap. Pre-order waitlist signup at the bottom.
- **Counter for failure:** Show HN traffic will spike danlab.dev. The landing must hold.

### 7. `danlab.dev/blog/muse-spark-vs-open-stack` — Muse Spark essay (v84 NEW)
- **Owner:** somdipto (author) + Dan1 (edit)
- **Due:** Jul 7
- **Definition of done:** 1,500-2,000 words. Founder voice. The honest comparison. Muse Spark is impressive; here's what we chose instead, and why. The trade-offs. The architecture. The India angle. The on-device decision.
- **Counter for failure:** v84's response to Muse Spark. If we miss the window (Jun 24 - Jul 14), the counter-narrative gets crowded out.

### 8. CONTRIBUTING.md with no-covert-updates clause (v84 NEW)
- **Owner:** Dan1
- **Due:** Jul 14
- **Definition of done:** All 4 public repos + dglabs-eval have a CONTRIBUTING.md with the no-covert-updates clause, the honest research clause, the 12-LOC + MIT + one example + one test bar, and the 48-hour PR review SLA.
- **Counter for failure:** The "open" claim is meaningless without the contribution policy. If we miss this, the privacy-maximalist persona doesn't convert.

### 9. GPG signing for all releases (v84 NEW)
- **Owner:** Dan2 (technical) + somdipto (GPG key)
- **Due:** Jul 14
- **Definition of done:** All releases from Jul 14 onward are GPG-signed. The GPG public key is published in `dan-consciousness` and every repo. The CI is open. The build is reproducible.
- **Counter for failure:** The "signed releases" claim is meaningless without the actual signing. If we miss this, the no-covert-updates clause is theater.

---

## Phase 2: Before dev-kit pre-orders (Aug 25) — 6 items

### 10. `danlab.dev/preorder` — Stripe waitlist
- **Owner:** Dan1 (copy) + Dan2 (Stripe integration)
- **Due:** Aug 14 (Show HN day -11, go live with the launch)
- **Definition of done:** Stripe payment link live. ₹12K founder + ₹4,999 student tier visible. Founder pricing locks for first 1,000. India + international shipping addresses. Email capture.
- **Counter for failure:** If the waitlist is not live by Show HN day, we lose the urgency.

### 11. YouTube channel with 90-sec demo + 4 daemon teardowns
- **Owner:** Dan2 (technical) + Dan1 (thumbnail + title)
- **Due:** Jul 8, 15, 22, 29 (4 daemon teardowns, weekly); Jul 18 (90-sec demo); Aug 1 (founder documentary)
- **Definition of done:**
  - 4 daemon teardowns (audiod, perceptiond, memoryd, ttsd), each 5-8 min, screen recording + voiceover, founder intro.
  - 90-sec install-to-talking-to demo, embedded in danlab.dev/dan-glasses and the Show HN post.
  - 5-7 min founder documentary, embedded in the founder essay.
- **Counter for failure:** YouTube is the long-form reach. If we don't ship weekly, we lose the search surface.

### 12. arXiv pre-print
- **Owner:** Dan2 (technical) + somdipto (author)
- **Due:** Aug 15
- **Definition of done:** "DanLab Multimodal: A Pre-RL Scaffold for On-Device Vision-Language Reasoning." 8-12 pages. The honest framing. The dglabs-eval v0.1 reference. The SIA-framework upgrade path.
- **Counter for failure:** arXiv is the academic credibility. If we miss Aug 15, we miss the "research lab" framing for the rest of Q3.

### 13. Discord (read-only → open) (v84 confirms v83)
- **Owner:** Dan1 (server setup) + community (mod)
- **Due:** Jul 21 (read-only) → Aug 5 (open)
- **Definition of done:** 200 invites sent on Jul 21 (Show HN week). Daily threads from Aug 5. Channels: #general, #daemons, #memoryd, #ttsd, #audiod, #perceptiond, #dev-kit, #india, #showcase.
- **Counter for failure:** If Discord isn't live by Show HN, we lose the real-time engagement.

### 14. India press placements (12 outlets)
- **Owner:** somdipto (intros + sign-off) + Dan1 (pitch)
- **Due:** Aug 1-25
- **Definition of done:** 1 founder profile + 1 methodology post in Tier 1 (Analytics India Magazine, Inc42, YourStory, ET Edge, AIM, NITI Aayog, IndiaAI, etc.). Embargo lifts Jul 14 09:00 IST with Show HN. The pitch is the open-on-device framing, not the product.
- **Counter for failure:** India press is the parallel track to Western press. If we miss it, we miss the SMB and university personas.

### 15. Western press pitches (The Information / TechCrunch / Verge) (v84 NEW)
- **Owner:** Dan1 (pitch) + somdipto (sign-off)
- **Due:** Aug 14 (Show HN day -11, embargo-aligned)
- **Definition of done:** Pitches sent to The Information, TechCrunch, The Verge, Hacker News (Ask HN) with the "open-source alternative to Muse Spark / Meta Glasses" angle. Embargo lifts Aug 25 09:00 IST with Show HN. Goal: 1 founder profile OR 1 methodology post in at least one Tier-1 Western outlet by Sep 15.
- **Counter for failure:** Western press is the parallel track to Indian press. If we miss it, we miss the Indie Hacker / Builder persona.

---

## v84 risk matrix

| Risk | Severity | Probability | Owner | Mitigation | Status |
|---|---|---|---|---|---|
| Sub-5min install not hit by Jul 13 | P0 | Medium | Dan2 | Item 1 in punchlist | 0% complete |
| No public YouTube demo by Jul 18 | P0 | Medium | Dan1 + Dan2 | Item 11 in punchlist | 0% complete |
| Show HN install fails on clean box | P0 | Medium | Dan2 | Item 1 (rollback plan) | 0% complete |
| danlab.dev product page not live Jul 5 | P1 | Low | Dan1 | Item 2 in punchlist | 0% complete |
| Muse Spark coverage drowns out our launch | P1 | High | Dan1 | Item 7 (essay) + Item 15 (press) | 0% complete |
| dglabs-eval v0.1 ships without baselines | P1 | Medium | Dan2 | Item 5 in punchlist | 0% complete |
| CONTRIBUTING.md not on all repos by Jul 14 | P1 | Low | Dan1 | Item 8 in punchlist | 0% complete |
| GPG signing not live by Jul 14 | P1 | Low | Dan2 + somdipto | Item 9 in punchlist | 0% complete |
| Apple / Google launch lands same week as Show HN | P2 | Low | Dan1 | Same-day counter-post ready | n/a |
| Stripe waitlist breaks on Show HN day | P2 | Low | Dan2 | Test mode + rollback | 0% complete |
| arXiv pre-print rejected (formatting) | P2 | Low | Dan2 | Submit Aug 10 (5-day buffer) | 0% complete |

---

## What's NOT on the punchlist (intentionally)

- **Mobile app** — Phase 2 (Q4 2026). Not Show HN critical-path.
- **Hardware v2** — Phase 2 (Q1 2027). Not Show HN critical-path.
- **Wake word v1.5** — Phase 2 (Q4 2026). Push-to-talk is fine for v1.
- **RL training pipeline** — Phase 3 (2027). Honesty about pre-RL is the moat.
- **Multimodal v1.0** — Phase 3 (2027). v0.1 (heuristic loop) ships first.

---

## v84 critical-path summary (32 days to Show HN)

- **T-32 days (today, Jun 24):** v84 punchlist locked. Muse Spark counter-narrative begins.
- **T-29 days (Jun 27):** Blog post "On-device by default" shipped.
- **T-26 days (Jun 30):** Dan Glasses product page draft ready.
- **T-21 days (Jul 5):** danlab.dev/dan-glasses live.
- **T-20 days (Jul 6):** Sub-5min install benchmark attempt #1.
- **T-19 days (Jul 7):** Founder essay + Muse Spark vs Open Stack essay shipped.
- **T-18 days (Jul 8):** YouTube daemon teardown #1 (audiod).
- **T-16 days (Jul 10):** Show HN landing first cut + dan-glasses README rewrite.
- **T-14 days (Jul 12):** dglabs-eval v0.1 private launch.
- **T-13 days (Jul 13):** Sub-5min install benchmark hit. CRITICAL.
- **T-12 days (Jul 14):** CONTRIBUTING.md on all repos + GPG signing live + press embargo defined.
- **T-10 days (Jul 16):** Show HN draft thread pre-written.
- **T-8 days (Jul 18):** 90-sec YouTube demo published.
- **T-3 days (Jul 23):** YouTube daemon teardown #4 (ttsd).
- **T-1 day (Jul 25):** dglabs-eval v0.1 public.
- **T-3 days (Aug 22):** Show HN draft finalized.
- **T-11 days (Aug 14):** Stripe waitlist live + Western press pitches sent.
- **T-10 days (Aug 15):** arXiv pre-print submitted.
- **T-7 days (Aug 18):** Show HN landing final.
- **T-0 days (Aug 25, 09:00 IST):** SHOW HN LIVE. 🚀

---

## v84 sources

[^1]: https://www.cnn.com/2026/06/23/tech/meta-glasses-price
[^2]: https://wincountry.com/2026/06/23/meta-launches-cheaper-range-of-ai-smart-glasses-starting-at-299
[^3]: https://www.aol.com/news/meta-announces-line-ai-glasses-212700196.html
[^4]: https://mezha.net/eng/bukvy/d4b9d82d_meta_launches_affordable
[^5]: https://economictimes.indiatimes.com/magazines/panache/meta-expands-its-smart-glasses-portfolio-with-new-meta-glasses-line-starting-at-299/articleshow/131952579.cms
[^6]: https://mywebar.com/blog/ar-metaverse/awe-2026-new-ar-glasses-ai-and-the-future-of-augmented-reality
