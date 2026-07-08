# Dan1 v82 — Punchlist (12 P0 items, by Show HN → Pre-orders)

**Author:** Dan1 👾
**Date:** 2026-06-24 12:00 IST (06:30 UTC)
**Companion:** `dan1-marketing-research.md`, `dan1-marketing-strategy.md`, `dan1-v82-summary.md`

---

## Phase 1: Before Show HN (Jul 14) — 6 items

### 1. `danlab.dev/install` — install-oneliner live
- **Owner:** Dan2 (technical) + Dan1 (copy + badge)
- **Due:** Jul 13 (Sunday)
- **Definition of done:** `curl -fsSL danlab.dev/install | bash` runs on a fresh Debian 12 x86_64 + aarch64 box, installs 8 daemons, prints "you're in", and exits 0.
- **Counter for failure:** The single biggest risk in v82. If the oneliner breaks on Show HN, the comment "I tried to install and it didn't work" kills the launch. Dan2 owns uptime + rollback.

### 2. `danlab.dev/glasses` — Dan Glasses product page
- **Owner:** Dan1 (copy per `dan1-landing-copy.md`) + Dan2 (technical FAQ)
- **Due:** Jul 5
- **Definition of done:** Live at `danlab.dev/glasses` with the 12-section structure from `dan1-landing-copy.md` v82. Live infra ticker auto-refreshes every 30s.
- **Counter for failure:** v81 missed this. v82 makes it the critical-path.

### 3. `danlab.dev/blog/from-9-to-5-to-agi` — founder essay
- **Owner:** somdipto (author) + Dan1 (edit)
- **Due:** Jul 7
- **Definition of done:** 2,000-3,000 words. Founder voice. India angle. The honesty-about-pre-RL moment. The Meta-Stella-surrender moment. The ₹12K-and-₹4,999 moment.
- **Counter for failure:** The essay is the share-link. If it's generic, no one shares it.

### 4. `github.com/somdipto/dan-glasses` — README rewrite
- **Owner:** Dan1 (per `dan1-github-readme-suggestions.md`) + Dan2 (technical accuracy)
- **Due:** Jul 10
- **Definition of done:** Universal template applied. Hero GIF (30s loop). Install-oneliner as primary CTA. Comparison table. 8-daemons list. Footer with founder credit + India flag.
- **Counter for failure:** The README is the first-conversion surface. If it's corporate, the launch loses.

### 5. `github.com/somdipto/dglabs-eval v0.1` — open eval repo
- **Owner:** Dan2 (technical) + Dan1 (framing)
- **Due:** Jul 12 (private); Jul 25 (public)
- **Definition of done:** Repo is private Jul 12, public Jul 25 (post-Show-HN). README explains the eval design. 5 baseline rows seeded (Dan Glasses, SmolVLM-256M, Moondream2, GPT-4V, Claude 3.5 Sonnet). Anyone can submit a row via PR.
- **Counter for failure:** The eval is the moat. If we ship it late or with no baselines, we lose the "open" claim.

### 6. `danlab.dev/show` — Show HN landing
- **Owner:** Dan1
- **Due:** Jul 10
- **Definition of done:** One-page. Curl command visible above the fold. 60-second demo video embedded. "What ships first" comparison table. "What's next" roadmap. Pre-order waitlist signup at the bottom.
- **Counter for failure:** Show HN traffic will spike danlab.dev. The landing must hold.

---

## Phase 2: Before dev-kit pre-orders (Aug 25) — 6 items

### 7. `danlab.dev/preorder` — Stripe waitlist
- **Owner:** Dan1 (copy) + Dan2 (Stripe integration)
- **Due:** Jul 14 (Show HN day, go live with the launch)
- **Definition of done:** Stripe payment link live. ₹12K founder + ₹4,999 student tier visible. Founder pricing locks for first 1,000. India + international shipping addresses. Email capture.
- **Counter for failure:** If the waitlist is not live on Show HN day, we lose the urgency.

### 8. `danlab.dev/blog/the-9-months-video` — founder documentary embed
- **Owner:** somdipto (subject) + Dan1 (video + edit)
- **Due:** Aug 1
- **Definition of done:** 5-7 minute documentary. Founder voice. India shots (IIT, IISc, Bengaluru). 8 daemons running. The honest-about-pre-RL moment. The ₹12K-₹4,999 moment. Embedded on the founder essay.
- **Counter for failure:** v81 had this on the roadmap. v82 promotes it to a critical-path item.

### 9. India press placements (12 outlets)
- **Owner:** somdipto (intros + sign-off) + Dan1 (pitch)
- **Due:** Aug 1-25
- **Definition of done:** 1 founder profile + 1 methodology post in Tier 1 (Analytics India Magazine, Inc42, YourStory, ET Edge, AIM, NITI Aayog, IndiaAI, etc.). Embargo lifts Jul 14 09:00 IST with Show HN. The pitch is the open-on-device framing, not the product.
- **Counter for failure:** India press is the parallel track to Western press. If we miss it, we miss the SMB and university personas.

### 10. Discord (read-only → open)
- **Owner:** Dan1 (server setup) + community (mod)
- **Due:** Jul 21 (read-only) → Aug 5 (open)
- **Definition of done:** 200 invites sent on Jul 21 (Show HN week). Daily threads from Aug 5. Channels: #general, #daemons, #memoryd, #ttsd, #audiod, #perceptiond, #dev-kit, #india, #showcase.
- **Counter for failure:** If Discord isn't live by Show HN, we lose the real-time engagement.

### 11. YouTube channel with 4 daemon teardowns
- **Owner:** Dan2 (technical) + Dan1 (thumbnail + title)
- **Due:** Jul 8, 15, 22, 29 (weekly cadence)
- **Definition of done:** 4 videos, each 5-8 minutes, walking through one daemon (audiod, perceptiond, memoryd, ttsd). Screen recording + voiceover. Founder intro at the start of each.
- **Counter for failure:** YouTube is the long-form reach. If we don't ship weekly, we lose the search surface.

### 12. arXiv pre-print
- **Owner:** Dan2 (technical) + somdipto (author)
- **Due:** Aug 15
- **Definition of done:** "DanLab Multimodal: A Pre-RL Scaffold for On-Device Vision-Language Reasoning." 8-12 pages. The honest framing. The dglabs-eval v0.1 reference. The SIA-framework upgrade path.
- **Counter for failure:** arXiv is the academic credibility. If we miss Aug 15, we miss the "research lab" framing for the rest of Q3.

---

## What's NOT on the punchlist (intentionally)

- **Mobile app** — Phase 2 (Q4 2026). Not Show HN critical-path.
- **Hardware v2** — Phase 2 (Q1 2027). Not Show HN critical-path.
- **Wake word v1.5** — Phase 2 (Q4 2026). Push-to-talk is fine for v1.
- **RL training pipeline** — Phase 3 (2027). Honesty about pre-RL is the moat.
- **Multimodal v1.0** — Phase 3 (2027). v0.1 (heuristic loop) ships first.

---

## Risk matrix (v82)

| Risk | Likelihood | Impact | Counter |
|---|---|---|---|
| Install-oneliner breaks on Show HN | Medium | Catastrophic | Dan2 owns uptime, status page, rollback. Smoke-test every day Jul 5-14. |
| Meta-Stella 2.0 (another covert update) | Low | High | CONTRIBUTING.md clause. Audit trail. We ship receipts. |
| Show HN flops | Medium | High | Pre-ship to 100 beta users. Founder on top comment. All hands day-of. |
| somdipto burnout | High | High | Build bench (Dan2 tech, Dan1 marketing, future Dan3+ ops). |
| Indian press hostile ("another Indian grift") | Low | High | Lead with the curl command. Lead with the eval. Lead with the open-on-device. |
| Hardware slips | Medium | Medium | ₹12K + ₹4,999 tier lock-in. Pre-orders can be refunded if Q4 slips. |

---

## Success metrics (v82)

| Metric | Target by Jul 14 | Target by Aug 25 | Target by Sep 22 |
|---|---|---|---|
| GitHub stars | 1,000 | 5,000 | 10,000 |
| Install-oneliner runs | 1,000 | 5,000 | 10,000 |
| Show HN rank | Top 5 (4+ hours) | — | — |
| Dev-kit pre-orders | 100 (waitlist) | 1,000 | 1,500 |
| X followers (combined) | 5,000 | 10,000 | 15,000 |
| LinkedIn followers (somdipto) | 5,000 | 6,500 | 8,000 |
| Reddit subscribers (r/danlab) | 500 | 1,500 | 3,000 |
| Discord members | 200 | 500 | 1,000 |
| YouTube subscribers | 1,000 | 3,000 | 5,000 |
| arXiv citations | — | — | 50 (Q4) |
| India press hits | — | 12 | 25 |

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-24 12:00 IST (06:30 UTC).*

*v80 = ship the wave. v81 = measure the spike. v82 = compound the moat.*