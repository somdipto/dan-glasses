# Dan1 — Marketing + Growth Cycle, Run 2026-06-28 (v105)

**Mission:** Marketing + research agent. Deep ecosystem research → marketing infrastructure build.
**Status:** ✅ v105 supersedes v104. All 6 canonical artifacts re-cut + this summary.
**Run timestamp:** 2026-06-28 10:30 IST (05:00 UTC), Bengaluru, India 🇮🇳

---

## Live infra verified (this run, v105)

| # | Daemon | Port | v104 status (Jun 28 10:00 IST) | v105 status (Jun 28 10:30 IST) | Δ |
|---|--------|------|--------------------------------|--------------------------------|---|
| 1 | audiod | 8090 | ✅ | ✅ | unchanged |
| 2 | perceptiond | 8092 | ✅ (5/3/2 after host restart) | ✅ **(4/3/2 — steady state, no further restart)** | unchanged |
| 3 | memoryd | 8741 | ✅ (0 memories — /tmp/memoryd.db fresh after 03:59 UTC host restart) | ✅ **(0 memories — bug confirmed at 14th cycle)** | **🐛 BUG CONTINUES** |
| 4 | toold | 8742 | ✅ | ✅ | unchanged |
| 5 | ttsd | 8743 | ✅ | ✅ | unchanged |
| 6 | os-toold | 8744 | ✅ | ✅ | unchanged |
| 7 | openclaw | 18789 | ✅ | ✅ | unchanged |
| 8 | dan-glasses-app | 8747 | ✅ | ✅ | unchanged |

**8/8 daemons live.** **14th honest-accounting cycle.** **9 consecutive cycles (v97 → v105) without false alarms.**

### v105 honest read

- **memoryd bug is structural, not transient.** `/tmp/memoryd.db` reopens fresh at every host restart. 14 cycles now carry this finding. **Monday Transparency #1 (Jun 29) is content-locked.** The 1-line fix is `MEMORYD_DB=/home/workspace/dan-glasses/Services/memoryd/memory.db` in the supervisord config + the spec patch documenting `DB_PATH` and `MEMORYD_DB`. **The structural finding is the brand promise in action.**
- **perceptiond counters steady.** 4/3/2 at v105, same as v104 end-state. No new restart cycle. Confirms v104's "honest reset, then steady state" pattern.
- **All other daemons unchanged.** audiod uptime ~60 min, all green.

---

## v105 artifacts (6 files in `dan-glasses/agent-work/`)

1. `dan1-marketing-research.v105.md` — v105 research with **Karpathy "3rd UI paradigm" framing (Jun 23)** + **Apple Vision Pro VP → OpenAI hardware (Jun 27)** + **Forbes OpenAI IPO delay confirmation (Jun 28)** + **14th honest-accounting cycle**
2. `dan1-marketing-strategy.v105.md` — v105 strategy with **6-pillar wedge** (auditable + on-device + open-source + sovereign-stack-compatible + Karpathy-paradigm-aligned + IPO-optional) + **10 personas** + **Show HN top-10 anticipated questions**
3. `dan1-content-calendar.v105.md` — v105 calendar with **Karpathy reply slot (Jul 1)** + **Aug 18 LinkedIn essay on the 3rd paradigm** + **arXiv Related Work Karpathy citation (by Jul 8)** + **15 Monday Transparency receipts (Jun 29 → Sep 29)**
4. `dan1-twitter-content.v105.md` — v105 X bio + 10 posts + **Post 1 (v105 announcement)** + **Post 3 (Karpathy reply)** + **Post 4 (Apple hardware pivot)** + **5 thread drafts A–E** + **launch-day burst pack for Aug 15 / Aug 25**
5. `dan1-landing-copy.v105.md` — v105 landing copy with **3rd LLM UI paradigm hero** + **Karpathy quote** + **simplified comparison table** + **5-step workflow** + **5-question FAQ**
6. `dan1-github-readme-suggestions.v105.md` — v105 README pattern with **per-repo audit checklist** + **MEMORYD_DB env-var callout** + **v103 no-covert-updates clause preserved as law**
7. `dan1-v105-summary.md` — this file

---

## v105 deltas from v104 (the 4 things)

1. **Karpathy Jun 23 thread is the new paradigm anchor.** Andrej Karpathy publicly described the 3rd LLM UI paradigm as "a self-contained, persistent, asynchronous entity with org-wide tools and context, working alongside teams of humans." **Danlab has been shipping that for 9 months on a $400 Linux laptop, open-source.** v105 promotes this to the top-of-funnel reference: arXiv Related Work opens with the Karpathy quote, Show HN opens with it, LinkedIn Aug 18 essay opens with it, X Post 1 opens with it.
2. **Apple Vision Pro VP Paul Meade → OpenAI hardware (Jun 27).** TechCrunch confirms the Apple wearable team's lead is leaving for OpenAI's hardware team. v105 sharpens the "Apple not in the race" claim: it's no longer "Apple is slow" — it's "Apple's wearable team is bleeding."
3. **Forbes confirms v104's OpenAI IPO delay + Anthropic overtake.** OpenAI → 2027 IPO. Anthropic $965B overtook OpenAI. Mythos 5 partially unblocked, Fable 5 still suspended. v105 promotes this to the **IPO-optional pillar** of the 6-pillar wedge: "AGI infrastructure that ships today on a Show HN budget, no IPO required."
4. **14th honest-accounting cycle.** memoryd bug continues. **Monday Transparency #1 (Jun 29) content-locked.** Brand promise in action.

---

## What I did NOT do (intentionally)

- No code changes. No service restarts. No edits to AGENTS.md.
- No GitHub push.
- No live X posts (scheduled agent run; Telegram summary at cycle end).

---

## Hand-off to next Dan1 cycle (v106, target Jun 29 05:00 UTC)

- **Monday Transparency #1** (Jun 29 10:30 IST = 05:00 UTC) — memoryd bug disclosure, 1-line fix, spec patch, audit trail. **Content-locked at v105.**
- **@danlab_dev X handle reservation** by Jul 1 — needs somdipto's sign-in to X.
- **Karpathy Jun 23 thread reply** by Jul 1 — thoughtful, not sycophantic.
- **arXiv Related Work** — Karpathy citation locked by Jul 8.
- **memoryd spec patch** — propose `MEMORYD_DB` env var documentation + default `DB_PATH` change.
- **arXiv co-authors lock** by Jul 8 — somdipto + Dan1 + Dan2 + ???

---

## Open questions for somdipto (v105)

1. **memoryd spec patch ownership.** The fix is one line (`MEMORYD_DB=...`) but the spec needs to document `DB_PATH` and `MEMORYD_DB`. Do you want me to draft the PR, or do you want to do it yourself?
2. **@danlab_dev handle reservation.** I need either (a) your X sign-in via the Zo browser, or (b) the X API access token, to reserve the handle by Jul 1. Which path?
3. **Karpathy reply tone.** Aug 15 paper and Show HN both lead with the Karpathy quote. Should the Jul 1 reply be a quote-tweet with a thoughtful one-liner, or a longer thread? My recommendation: short, technical, non-sycophantic — something like "We built that on a Linux laptop from India."
4. **arXiv co-authors.** Somdipto + Dan1 + Dan2 + ???. Confirm by Jul 8.
5. **Monday Transparency Cadence.** Every Monday, for 15 weeks. Are you OK with the cadence + the bug-of-the-week slot being non-negotiable?
6. **Show HN headline options (v105 has 3):**
   - "Show HN: the auditable AI glasses for the 80%-Meta era"
   - "Show HN: the only open-source reference implementation of the 3rd LLM UI paradigm"
   - "Show HN: 8 daemons, 144 tests, 0 cloud, MIT — built from India"
   My recommendation: option 2 (leads with the Karpathy paradigm, captures both Show HN crowd and Karpathy followers).

---

**v105 promise:** *From India 🇮🇳, with 8/8 daemons up (14 consecutive cycles, 9 without false alarms), 144 tests, 0 cloud, the memoryd bug disclosed + 1-line fix + spec patch queued, the on-device agent memory lane claimed against Perplexity Brain + Engram, the sovereign-stack-compatible lane claimed via Sarvam-Models 24B, the Karpathy-paradigm-aligned lane claimed via the Jun 23 thread, the Apple Vision Pro VP → OpenAI hardware moment captured, the IPO-optional lane claimed against OpenAI's 2027 delay, the Monday Transparency Cadence launching, an arXiv-bound audiod calibration paper (Related Work: Karpathy), a 6-pillar wedge, a 5-reasoning-adapter stack, a 10-persona map, a ₹4,999 student tier, a ₹12K sovereign-stack bundle, and a ₹12K wearable — we ship the auditable, on-device, open-source, sovereign-stack-compatible, Karpathy-paradigm-aligned, IPO-optional alternative. arXiv: Aug 15. Show HN: Aug 25. Eval: Jul 25. Monday Transparency #1: Jun 29. MIT forever.* 👾

*v105 summary.*

*Dan1 — Bengaluru, India 🇮🇳 — 2026-06-28 10:30 IST (05:00 UTC).*