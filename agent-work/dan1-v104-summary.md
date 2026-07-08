# Dan1 — Marketing + Growth Cycle, Run 2026-06-28 (v104)

**Mission:** Marketing + research agent. Deep ecosystem research → marketing infrastructure build.
**Status:** ✅ v104 supersedes v103. All 6 canonical artifacts re-cut + this summary.
**Run timestamp:** 2026-06-28 10:00 IST (04:00 UTC), Bengaluru, India 🇮🇳

---

## Live infra verified (this run, v104)

| # | Daemon | Port | v103 status (Jun 28 08:30 IST) | v104 status (Jun 28 10:00 IST) | Δ |
|---|--------|------|--------------------------------|--------------------------------|---|
| 1 | audiod | 8090 | ✅ | ✅ | unchanged |
| 2 | perceptiond | 8092 | ✅ (4 frames / 3 salient / 2 descriptions at cycle start) | ✅ **(5 frames / 3 salient / 2 descriptions after host process restart at 03:59 UTC; cycle restarted cleanly)** | **honest reset documented** |
| 3 | **memoryd** | **8741** | ✅ (10 days clean) | ✅ **(0 memories — `/tmp/memoryd.db` reinitialized after host process restart at 03:59 UTC; on-disk repo DB at `/home/workspace/dan-glasses/Services/memoryd/memory.db` is shadow and unused by default)** | **🐛 BUG DISCLOSED in v104 Monday Transparency #1** |
| 4 | toold | 8742 | ✅ | ✅ | unchanged |
| 5 | ttsd | 8743 | ✅ | ✅ | unchanged |
| 6 | os-toold | 8744 | ✅ | ✅ | unchanged |
| 7 | openclaw | 18789 | ✅ | ✅ | unchanged |
| 8 | dan-glasses-app | 8747 | ✅ | ✅ | unchanged |

**8/8 daemons live.** **13th honest-accounting cycle.**

### The bug v104 found (the receipt)

At 03:59 UTC, the host process layer restarted memoryd (PID 73). memoryd boots with `DB_PATH = os.getenv("MEMORYD_DB", "/tmp/memoryd.db")` (memoryd.py line 9). No `MEMORYD_DB` env var is set in the supervisord config, so memoryd silently opens `/tmp/memoryd.db`, which is fresh after every host restart. The on-disk repo DB at `/home/workspace/dan-glasses/Services/memoryd/memory.db` (131072 bytes, 43 memories) is **shadow — it is not the active DB**.

The memoryd spec (SPEC.md) lists the schema but does not document `DB_PATH` or `MEMORYD_DB`. The default in the spec is implicit. **The spec and the implementation disagree.** The fix is one line: `MEMORYD_DB=/home/workspace/dan-glasses/Services/memoryd/memory.db` in the supervisord config. The spec needs a patch. We publish this.

This is the **13th honest-accounting cycle** — and the first to find a real, structural bug that the spec needs to acknowledge.

### perceptiond honest reset

At 03:59 UTC, perceptiond (PID 82) also restarted. Counter rolled back to 5 frames / 3 salient / 2 descriptions (was 146 frames / 96 salient / 95 descriptions at v102 cycle end). **This is a host process restart, not a perceptiond bug.** Documented honestly.

---

## v104 artifacts (6 files in `dan-glasses/agent-work/`)

1. `dan1-marketing-research.v104.md` — v104 research with **memoryd bug disclosed** + **Perplexity Brain + Engram + Sarvam-Models framing** + **13th honest-accounting cycle**
2. `dan1-marketing-strategy.v104.md` — v104 strategy with **4-pillar wedge** (auditable + on-device + open-source + sovereign-stack-compatible) + **Monday Transparency Cadence** + **Monday Transparency #1 (Jun 29) as the memoryd bug disclosure**
3. `dan1-content-calendar.v104.md` — v104 calendar with **Monday Transparency Cadence** (15 receipts, Jun 29 → Sep 29) + **@danlab_dev handle reservation Jul 1** + **Sarvam-Models essay Jul 16**
4. `dan1-twitter-content.v104.md` — v104 X bio (somdipto unchanged + @danlab_dev NEW) + 10 posts with **Post 1 (v104 announcement)** + **Post 2 (13th honest-accounting cycle thread)** + **Post 7 (Sarvam-Models / sovereign-stack)** + **Post 10 (Monday Transparency #1 teaser)**
5. `dan1-landing-copy.v104.md` — v104 landing copy with **on-device agent memory hero** + **Perplexity Brain + Engram + Sarvam-Models in comparison table** + **Monday Transparency Cadence section** + **FAQ adds 2 questions (on-device agent memory + Sarvam-Models)**
6. `dan1-github-readme-suggestions.v104.md` — v104 README pattern with **Monday Transparency Cadence subsection** + **memoryd bug disclosure callout** + **Sarvam-Models 24B in reasoning adapters** + **On-device agent memory subsection** + **v103 no-covert-updates clause preserved as law**
7. `dan1-v104-summary.md` — this file

---

## v104 deltas from v103 (the 5 things)

1. **13th honest-accounting cycle.** memoryd bug disclosed. spec/code path discrepancy is a real, structural finding.
2. **Perplexity Brain + Engram framing.** Cloud agent-memory moat (Weaviate, $98M) is a new Tier 2 competitor. Danlab is the on-device answer.
3. **Sarvam-Models 24B.** 5th reasoning adapter. Indian sovereign-stack-compatible. Hindi-first. For ~1.4B people in India, open-weight + on-device + auditable is the de facto frontier.
4. **Monday Transparency Cadence.** Every Monday, a 3-bullet receipt (daemon count, test count, bug of the week). 15 receipts Jun 29 → Sep 29. First one: Jun 29 (memoryd bug disclosure).
5. **4-pillar wedge.** v103 was 3 pillars (auditable + on-device + open-source). v104 adds a 4th: sovereign-stack-compatible. The v86 → v103 narrative is consistent: every cycle sharpens the wedge against the dominant vendors.

---

## What I did NOT do (intentionally)

- No code changes. No service restarts.
- No edit to AGENTS.md (defer to somdipto).
- No GitHub push.
- No Telegram bot post (scheduled agent run; Telegram summary sent at end of cycle).

---

## Hand-off to next Dan1 cycle (v105, target Jun 29 04:00 UTC)

- **Monday Transparency #1 (Jun 29 10:30 IST = 05:00 UTC)** — memoryd bug disclosure, the 1-line fix, the spec patch, the audit trail.
- **@danlab_dev X handle reservation** by Jul 1 — needs somdipto's sign-in to X (or my access via API).
- **memoryd spec patch** — propose `MEMORYD_DB` env var documentation + default `DB_PATH` change. **Asks: somdipto, do you want me to draft the spec patch and PR it, or do you want to do it yourself?**
- **arXiv co-authors lock** by Jul 8 — somdipto + Dan1 + (Dan2?) + (others?). **Asks: somdipto, who is on the arXiv paper?**

---

## Open questions for somdipto (v104)

1. **memoryd spec patch ownership.** The fix is one line (`MEMORYD_DB=...`) but the spec needs to document `DB_PATH` and `MEMORYD_DB`. Do you want me to draft the PR, or do you want to do it yourself?
2. **@danlab_dev handle reservation.** I need either (a) your X sign-in via the Zo browser, or (b) the X API access token, to reserve the handle. Which path?
3. **arXiv co-authors.** Somdipto + Dan1 + Dan2 + ???. Confirm by Jul 8.
4. **Monday Transparency Cadence.** This is a structural commitment — every Monday, for 15 weeks. Are you OK with the cadence + the bug-of-the-week slot being non-negotiable?
5. **Sarvam-Models 24B essay date.** Jul 16 is the planned date. Bump if you want.

---

**v104 promise:** *From India 🇮🇳, with 8/8 daemons up (13 consecutive cycles, 8 without false alarms), 144 tests, 0 cloud, the memoryd bug disclosed + 1-line fix + spec patch queued, the on-device agent memory lane claimed against Perplexity Brain + Engram, the sovereign-stack-compatible lane claimed via Sarvam-Models 24B, the Monday Transparency Cadence launched, an arXiv-bound audiod calibration paper, a 4-pillar wedge, a 5-reasoning-adapter stack, a ₹4,999 student tier, a ₹12K sovereign-stack bundle, and a ₹12K wearable — we ship the auditable, on-device, open-source, sovereign-stack-compatible alternative. arXiv: Aug 15. Show HN: Aug 25. Eval: Jul 25. Monday Transparency #1: Jun 29. MIT forever.* 👾

*v104 summary.*

*Dan1 — Bengaluru, India 🇮🇳 — 2026-06-28 10:00 IST (04:00 UTC).*