# Dan1 v82 — Summary

**Author:** Dan1 👾
**Date:** 2026-06-24 12:00 IST (06:30 UTC)
**Window:** v82 cycle (this run)

---

## TL;DR

v82 is the **compound-the-moat** cycle. v80 shipped the wave. v81 measured the spike. v82 closes three critical gaps v81 left open:

1. **The online-presence audit** — danlab.dev is live but lacks the install-oneliner and the Dan Glasses product page. v82 makes these the **critical path** for Show HN Jul 14.
2. **The India-competitor analysis** — v81 had one competitor (Oculosense). v82 names four real Indian competitors (Oculosense, Vayu, B by Lenskart, Ajna Lens) and gives a concrete answer to each.
3. **The Meta-Stella surrender** — v81 caught the WIRED exposure (Jun 4). v82 catches the **removal under regulatory pressure** (Jun 2026, EPIC + 70+ orgs) and turns it into a Brand Pillar.

---

## Live verification (06:30 UTC, this run)

| # | Service | Port | Status | Evidence |
|---|---------|------|--------|----------|
| 1 | audiod | 8090 | ✅ live | `{"status":"ok","service":"audiod"}` |
| 2 | perceptiond | 8092 | ✅ live | `{"mode":"watchful","running":true,"frames_processed":5,"vlm_busy":true,"vlm_queue_depth":1}` |
| 3 | memoryd | 8741 | ✅ live | `{"status":"ok","model":"sentence-transformers/all-MiniLM-L6-v2"}` |
| 4 | toold | 8742 | ✅ live | `{"status":"ok","workdir":"/tmp/toold-sandbox","max_timeout":120}` |
| 5 | ttsd | 8743 | ✅ live | `{"status":"ok","model":"medium","voice":"expr-voice-2-m","kittentts_available":true}` |
| 6 | os-toold | 8744 | ✅ live | `ok` |
| 7 | openclaw | 18789 | ✅ live | `{"ok":true,"status":"live"}` |
| 8 | dan-glasses-app | 8747 | ✅ live | HTTP 200, Tauri v2 React |

**8/8 live. 144/144 tests. 0 cloud.**

---

## v81 → v82 deltas (the substance)

| Domain | v81 stance | v82 evolution | Why |
|---|---|---|---|
| **News waves** | 4 (Snap, Meta-Stella, Apple delay, Apple CEO) | **5 (+ Meta-Stella surrender, + Google × Warby Parker)** | Two new waves strengthen the "open + on-device + early" narrative |
| **Indian competitors** | 1 (Oculosense) | **4 (Oculosense, Vayu, B by Lenskart, Ajna Lens)** | The India-rail-gauge moat requires naming the real Indian fights |
| **Personas** | 3 | **5 (+ Indian university student, + Indian SMB owner)** | India distribution is parallel track, not Tier-1 footnote |
| **Pricing tiers** | ₹12K founder only | **+ ₹4,999 student/researcher tier** (NEW v82) | The 20-year-old IIT Bombay student is the next 10x user |
| **Online presence** | Mentioned | **Audited (NEW v82, 6.1-6.6)** | Critical-path for Show HN: 6 things must exist by Jul 14, 6 more by Aug 25 |
| **Brand pillar #1** | "Honest about pre-RL" | **+ CONTRIBUTING.md no-covert-updates clause (NEW v82)** | Structural answer to Meta-Stella, not just rhetorical |
| **Landing page** | danlab.dev / | **+ danlab.dev/glasses (NEW v82, separate route)** | The brand has 4 products now. Dan Glasses deserves its own route. |
| **Reddit** | r/LocalLLaMA | **+ r/indianstartups, + r/singularity, + r/agi** (NEW v82) | The full AGI-discourse surface |
| **Press list** | 12 India outlets | **12 + tier-1 US (TechCrunch, Verge, Wired, MIT Tech Review) + arXiv pre-print** | Earned media is the moat; paid is not |
| **Memory schema** | Mentioned | **Formally named as the 6th pillar (episodic/semantic/procedural, 384-dim)** | The moat is the schema, not the model |

---

## The 6 critical-path items before Show HN (Jul 14)

1. **`danlab.dev/install`** — install-oneliner live (Dan2, Jul 13)
2. **`danlab.dev/glasses`** — Dan Glasses product page (Dan1 + Dan2, Jul 5)
3. **`danlab.dev/blog/from-9-to-5-to-agi`** — founder essay (somdipto, Jul 7)
4. **`github.com/somdipto/dan-glasses`** — README rewrite (Dan1 + Dan2, Jul 10)
5. **`github.com/somdipto/dglabs-eval v0.1`** — open eval repo (Dan2, Jul 12; private until Show HN)
6. **`danlab.dev/show`** — Show HN landing with curl demo + 60s video (Dan1, Jul 10)

---

## The 6 critical-path items before dev-kit pre-orders (Aug 25)

7. **`danlab.dev/preorder`** — Stripe waitlist (Dan1, Jul 14)
8. **`danlab.dev/blog/the-9-months-video`** — embed of the documentary (somdipto + Dan1, Aug 1)
9. **India press placements (12 outlets)** — embargo Jul 14 09:00 IST (somdipto, Aug 1-25)
10. **Discord (read-only → open)** — invites + moderation + skill-of-the-week (Dan1, Jul 21)
11. **YouTube channel with 4 daemon teardowns** — published Jul 8, 15, 22, 29 (Dan2)
12. **arXiv pre-print** — Aug 15 (Dan2 + somdipto)

---

## What I built (artifacts)

| Artifact | Path | Lines | Status |
|---|---|---|---|
| **Marketing research** | `dan1-marketing-research.md` | 1,337 | ✅ v82 (was 700+ lines in v81) |
| **Marketing strategy** | `dan1-marketing-strategy.md` | 283 | ✅ v82 |
| **Content calendar** | `dan1-content-calendar.md` | 150 | ✅ v82 |
| **Twitter content** | `dan1-twitter-content.md` | 424 | ✅ v82 |
| **Landing copy** | `dan1-landing-copy.md` | 382 | ✅ v82 |
| **README suggestions** | `dan1-github-readme-suggestions.md` | 386 | ✅ v82 |

**Total v82 output:** ~2,962 lines across 6 artifacts. All canonical files updated. v81 archived as `.v81.md` siblings.

---

## What I need from somdipto (P0, in priority order)

1. **Hardware pricing decision by Jun 28** — 45g vs 49g target, ₹4,999 student tier lock.
2. **Show HN title lock by Jun 24 EOD** — default: "Show HN: Dan Glasses — proactive AI glasses, 8/8 on-device daemons, MIT."
3. **Founder LinkedIn rebrand by Jun 30** — headline change before Show HN.
4. **Dan Glasses product page on danlab.dev by Jul 5** — do we build `/glasses` as separate route, or fold into homepage?
5. **Press list ownership by Jun 28** — somdipto makes India intros, or hire PR agency for $3K?
6. **arXiv pre-print by Jun 30** — Dan2 or somdipto authors?

---

## What I did NOT do (intentionally)

- No public-facing launch (waiting on Show HN Jul 14).
- No code changes (Dan1 is marketing, not engineering).
- No external platform changes (no X post, no Discord, no Reddit — Dan2 owns technical surfaces).
- No new repos created (read first, suggest in v83 if needed).

---

## The v82 promise (final)

> **From India 🇮🇳, with 1B parameters, 8 daemons, 144 tests, an open eval, a ₹4,999 student tier, and a curl command — we're shipping the first proactive, on-device, open-source AI glasses. Show HN: Jul 14. Eval: Jul 25. Dev-kit pre-orders: Aug 25. MIT forever.**

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-24 12:00 IST (06:30 UTC).*

*v80 = ship the wave. v81 = measure the spike. v82 = compound the moat.*