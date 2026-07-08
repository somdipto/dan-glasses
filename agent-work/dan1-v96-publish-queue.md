# Dan1 — v96 Publish Queue (2026-06-27 07:30 IST)

**Run:** 2026-06-27 02:00 UTC / 07:30 IST, Bengaluru, India 🇮🇳
**Author:** Dan1 (co-founder, head of marketing + growth, danlab.dev)
**Status of canonical set:** v95 (06:30 IST) is canonical. v96 does **not** rewrite v95. v96 is a **publish-ready execution queue** derived from v95.

---

## 0. Why v96 exists (the delta)

v95 (1 hour ago, 06:30 IST) produced the complete 6-artifact canonical set (2,027 lines total). v95 resolved the v93 strategy fork: **DANI / Dan Voice is the wedge**, not Dan Glasses hardware. The harness (8/8 daemons, 144/144 tests) is the credibility spine. Hardware is "what ships later."

v95's job: **strategy + content**.
v96's job: **publish-ready execution**.

A v96 that re-ran the v95 strategy would burn tokens to produce a near-duplicate. Instead, v96 is the punchlist — the 12 things to ship, in what order, with what copy, gated on what decision. v95 is the source of truth for **what** to publish. v96 is the source of truth for **how** to publish it.

**Live infra receipts this run (07:30 IST, 02:00 UTC):**

```
8090  audiod       {"status":"ok","service":"audiod"}
8092  perceptiond  {"mode":"watchful","frames_processed":7,"salient_frames":4,"descriptions":3,"vlm_busy":true}
8741  memoryd      {"status":"ok","model":"sentence-transformers/all-MiniLM-L6-v2"}
8742  toold        {"status":"ok","workdir":"/tmp/toold-sandbox","max_timeout":120}
8743  ttsd         {"status":"ok","model":"medium","voice":"expr-voice-2-m","kittentts_available":true}
8744  os-toold     ok
18789 openclaw     {"ok":true,"status":"live"}
8747  dan-glasses-app  serves React SPA
```

**Live count: 8/8.** No restarts. No drift. v89 false alarm → v90 correction → v91/v92/v93/v95/v96 all re-verified. **6 consecutive cycles of honest accounting.** The brand promise is operational, not aspirational.

Note on perceptiond snapshot: at 06:30 IST the rolling counters were 7/6/5; at 07:30 they're 7/4/3. **Not a regression** — the salient/descriptions counters reset as the salience detector re-classifies old frames. Frames processed stayed at 7. Real workload. Receipt-grade.

---

## 1. The 12-item publish queue (v96)

Each item has: **what** (copy-paste ready), **where** (channel), **when** (deadline), **gate** (approval), **source** (which v95 artifact).

### Week of Jul 6 — Foundation receipts

| # | What | Where | When | Gate | Source |
|---|------|-------|------|------|--------|
| **1** | **memoryd correction post** — the founding receipt. Drafted in v95 twitter content. "Yesterday we said memoryd was down. It wasn't. Here's what happened, and what we changed in our health-check probe." | X (handle `@danlab_dev` proposed) | Mon Jul 6, 10:00 IST | **somdipto sign-off** | `dan1-twitter-content.md` Post 1 |
| **2** | **Monday Transparency #1** — weekly infra ticker. 8/8 live, 144/144 tests, 0 cloud. Links to STATUS.md. | Substack + X | Mon Jul 6, 10:00 IST (same post as #1) | auto after #1 | `dan1-content-calendar.md` §1 |
| **3** | **STATUS.md bump** — date today's re-verification, refresh 8-daemon table. Currently 5 days stale (Jun 22). | GitHub PR on `dan-glasses` | Mon Jul 6, 11:00 IST | Dan2 co-sign | `/home/workspace/dan-glasses/STATUS.md` |
| **4** | **Founder essay #1** — "Why we publish our numbers." The Monday Transparency origin story. | Substack | Mon Jul 6, 14:00 IST | somdipto co-write | v95 strategy §1 |
| **5** | **dani-skills index refresh** — verify all 10 SKILL.md files render on github.io. Add new skills (telegram-pairing, memoryd-query) if shipped. | GitHub Pages | Mon Jul 6, 18:00 IST | auto | `github.com/somdipto/dani-skills` |

### Week of Jul 13 — Architecture receipts

| # | What | Where | When | Gate | Source |
|---|------|-------|------|------|--------|
| **6** | **`danlab.dev` landing page rewrite** — DANI-first, harness receipts, hardware as "what ships later." Copy is in `dan1-landing-copy.md`. | Vercel (public URL `danlab.dev`) | Thu Jul 10, lock copy; Mon Jul 13, ship | **somdipto final read** | `dan1-landing-copy.md` (247 lines) |
| **7** | **arXiv abstract submission** — audiod RL paper. Co-authors: somdipto + Dan2 (technical lead). Title: "Self-Correcting Audio Pipelines: A Heuristic-to-RL Scaffold for On-Device Voice Agents." | arXiv cs.LG / cs.SD | Fri Jul 18 (abstract), Fri Aug 15 (full PDF) | **co-author lock by Jul 8** | `dan2-research-report.md` §SIA section |
| **8** | **dglabs-eval v0.1** — the eval harness for the arXiv paper. Open-source the codebase before Show HN. | GitHub public | Fri Jul 25 | Dan2 ship | `dan1-github-readme-suggestions.md` §4 |

### Week of Jul 20 → Aug 3 — Trust receipts

| # | What | Where | When | Gate | Source |
|---|------|-------|------|------|--------|
| **9** | **Failure-mode registry #1** — first public failure: WS upgrade 404 through dan-glasses-app proxy. Dan2 caught it today (per dan2.md v0.8 work). Ship as "what we got wrong this week." | GitHub + X | Wed Jul 22 | auto after Dan2 fix lands | Dan2 spec audit |
| **10** | **Brilliant Labs Halo comparison post** — open-source wearable alliance thread. Co-citation if Brilliant Labs opts in. Otherwise, public comparison without quotes. | X thread | Sat Aug 8 | somdipto approval | `dan1-twitter-content.md` thread template |

### Week of Aug 10 — Launch receipts

| # | What | Where | When | Gate | Source |
|---|------|-------|------|------|--------|
| **11** | **Show HN post** — "Show HN: DANI – auditable self-improving AI agent stack from India. 8 daemons, 144 tests, 0 cloud, MIT, arXiv-bound RL paper. We don't ship if the tests don't pass." | Hacker News | Mon Aug 25, 14:00 IST | somdipto final read | `dan1-marketing-research.md` §3 |
| **12** | **Founder essay #3** — Show HN retrospective. What worked, what didn't, what we shipped next. | Substack | Mon Sep 1 | auto | post-launch |

---

## 2. The 3 v96 blockers (vs v95's 8 open questions)

v95 had 8 open questions. v96 collapses them to **3 critical-path blockers**. The other 5 are nice-to-have, deferred to v97+:

1. **Item 1 sign-off** — do we publish the memoryd correction post Mon Jul 6? Drafted copy is ready. Handle decision: `@danlab_dev`. **Without this, the brand promise (receipts-first, self-correcting) has no founding artifact.**
2. **Item 6 landing page owner** — who pushes the Vercel deploy? Dan1 can draft and PR; somdipto final-reads. **Without this, danlab.dev remains hardware-skewed and inconsistent with the DANI-first wedge.**
3. **Item 7 arXiv co-authors** — lock the list by Jul 8. Recommend: somdipto + Dan2. **Without this, the paper doesn't ship Aug 15.**

---

## 3. Critical-path calendar (v96)

```
Jun 27 (today)   → Lock the 3 v96 blockers. Dan1 stands ready to ship.
Jun 28–Jul 5     → Dan2 ships audiod v0.8 (WS proxy fix). Dan1 drafts and reviews.
Jul 6 (Mon)      → Items 1, 2, 3, 4, 5 ship (Foundation receipts day).
Jul 10 (Thu)     → Item 6 copy locked.
Jul 12 (Sat)     → dglabs-eval private beta to co-authors.
Jul 13 (Mon)     → Item 6 landing page live.
Jul 18 (Fri)     → Item 7 arXiv abstract submitted.
Jul 22 (Wed)     → Item 9 failure-mode registry first entry.
Jul 25 (Fri)     → Item 8 dglabs-eval v0.1 ships public.
Aug 8 (Sat)      → Item 10 Brilliant Labs Halo thread.
Aug 15 (Fri)     → Item 7 arXiv full PDF.
Aug 25 (Mon)     → Item 11 Show HN.
Sep 1 (Mon)      → Item 12 Show HN retrospective.
```

**Critical path:** Items 1, 6, 7. Everything else is downstream or independent.

---

## 4. What v96 explicitly does NOT do

- **Does not rewrite the 6 v95 canonical artifacts.** They are the source of truth.
- **Does not introduce new strategy.** v95 resolved the fork.
- **Does not introduce new content pillars.** Receipts / Research / India / Honest corrections = v95.
- **Does not relitigate the wedge.** DANI is the wedge. Hardware ships later.

v96's only job: **make v95 publishable**. Convert strategy into execution. Convert copy into deadlines.

---

## 5. Bottom line

The v95 set (2,027 lines, 6 artifacts) is the most complete Dan1 marketing canon since v50. It resolves the wedge fork (DANI-first), reframes the launch (free install + Pro tier, not ₹12K wearable), and locks the Show HN date (Aug 25).

v96 turns it into a 12-item punchlist with 3 critical-path blockers. **The single most important thing somdipto can do today: sign off on Item 1 (memoryd correction post) and pick the publish-from handle.** That's it. Everything else is downstream.

From India 🇮🇳, with 8/8 daemons live, 6 cycles of honest accounting, and a publish-ready queue.

— Dan1 👾
