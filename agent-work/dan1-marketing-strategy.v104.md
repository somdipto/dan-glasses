# Dan1 Marketing Strategy — v104 (2026-06-28)

**Author:** Dan1 (DAN-1, danlab.dev)
**Status:** Supersedes v103 (2026-06-28 08:30 IST)
**Anchored to:** `dan1-marketing-research.md` (v104) + `dan2-research-report.md` (v99)
**Cycle window:** Jun 28 → Sep 30, 2026 (95 days, 14 weeks)

---

## The strategy in one paragraph

**Dan Glasses wins the auditable lane in the 80%-Meta era, the on-device agent-memory era, and the sovereign-AI moment.** Meta owns the shelf, Google+Qualcomm own the OS, Reflection AI owns the compute moat, Perplexity + Engram own the cloud-agent-memory moat, Mythos/GPT 5.6 are geopolitically gated. Danlab owns the **reproducibility lane** — 144/144 tests anyone can rerun on a $400 Linux laptop in 5 minutes, plus the on-device agent memory, plus the sovereign-stack compatibility. **The 13th honest-accounting cycle** (memoryd restart reveals the spec/code path discrepancy) is structural, not cosmetic — it is the brand promise operationalized. Between Jun 28 and Sep 30, 2026, we graduate from "research substrate" to "the auditable alternative that the developer community cites" via three irreversible artifacts: **(1)** the arXiv pre-print on Aug 15 (audiod confidence-calibration RL agent, ECE-grounded, AIE-Bench submission), **(2)** the Show HN post on Aug 25 ("the auditable AI glasses for the 80%-Meta era, with on-device agent memory"), **(3)** the memoryd v2 release on Aug 15 (open-source wearable-shaped Perplexity Brain, on-device only). **Channels that don't feed these three artifacts are out of scope for v104.**

---

## The v104 sharpening (vs v103)

| Dimension | v103 lead | v104 lead | Why |
|---|---|---|---|
| Memory wedge | not addressed | **"your agent's memory lives on your device, not in Engram's cloud"** | Perplexity Brain + Engram (Weaviate $98M, Jun 6+26) are the new cloud-agent-memory moats. Danlab is the on-device answer. |
| Sovereignty wedge | Persona #9 added | **Sarvam-Models 24B as the 5th reasoning-adapter, Jul 16 essay** | Sarvam-Models 24B released Jun 27. Closed-weight frontier is geopolitically gated. Open-weight + on-device is the de facto frontier for ~1.4B. |
| Honesty wedge | "12 cycles, 7 without false alarms" | **"13 cycles, 7 without false alarms; the 6th was memoryd restart at 03:59 UTC; the spec/code path discrepancy is structural, not cosmetic"** | memoryd restarted between v103 and v104. /tmp/memoryd.db is fresh (0 memories). v104 promotes it to the **Monday Transparency Cadence**. |
| Brand handle | @NandySomdipto only | **+ @danlab_dev reservation by Jul 1** | The product brand needs a handle separate from the personal brand. |
| Show HN framing | "the auditable AI glasses for the 80%-Meta era" | **"the auditable AI glasses for the 80%-Meta era, with on-device agent memory"** | Adds the memory wedge without diluting the era wedge. |
| Memoryd v2 framing | "open-source wearable-shaped Perplexity Brain" | **"open-source wearable-shaped Perplexity Brain, on-device only"** | "On-device only" is the differentiation. |
| OpenAI IPO context | not addressed | **"AGI infrastructure that doesn't require a 7-year exit window"** | OpenAI IPO delayed (Jun 25 NYT). Capital environment is bifurcating. Bootstrap-to-Show-HN is the wedge. |

---

## The 4-move sequence (v104 = v103 sequence with v104 sharpening)

```
JUN 28 → AUG 14     (prep window, 7 weeks)
  Move 1: SHARPEN (v104 active)
    ├─ Build /glasses landing page (v103 copy → v104 adds memoryd v2 + on-device memory)
    ├─ Build /install page (curl command + 5-min walkthrough)
    ├─ Rewrite top 4 GitHub READMEs (Show HN-grade + reproducibility-first + 10-sec test)
    ├─ Lock arXiv pre-print authorship + outline (somdipto + Dan1) — by Jul 8
    ├─ Record 3-min demo video (somdipto, hands-on, $400 laptop visible)
    ├─ Reserve @danlab_dev X handle — by Jul 1
    └─ **Monday Transparency #1: Jun 29 — memoryd restart cycle, perceptiond honest reset**

AUG 15 → AUG 24     (launch window, 10 days)
  Move 2: ARXIV
    ├─ Aug 15: arXiv pre-print drops (audiod calibration RL agent)
    ├─ Aug 15: GitHub repo tagged v2.0 (memoryd v2 release — on-device agent memory)
    ├─ Aug 16: Reddit r/MachineLearning post — "We built the auditable alternative. Here's the 144/144 receipt, the reproduction time, and the memoryd bug we publish."
    ├─ Aug 18: Essay published: "The auditable lane in the 80%-Meta era + on-device agent memory + sovereign-AI moment" (LinkedIn + danlab.dev)
    ├─ Aug 22: Counter-thread: "Reflection has 100K GB300-hours. Danlab has 144/144 tests. Perplexity has cloud agent memory. Danlab has on-device agent memory."
    └─ Aug 24: Show HN post drafted, demo video final

AUG 25 → SEP 30     (compound window, 5 weeks)
  Move 3: SHOW HN
    ├─ Aug 25: Show HN post goes live (8:30 AM PT) — "the auditable AI glasses for the 80%-Meta era, with on-device agent memory"
    ├─ Aug 25-26: 24h on-site reply window
    ├─ Aug 27: First GitHub Issues from HN readers
    ├─ Aug 28-31: Post-mortem + first-time-user friction iteration
    ├─ Sep 1-15: AIE-Bench / SEAGym submission + LongMemEval / PersonaMem-v2
    └─ Sep 15-30: Conference workshop applications (NeurIPS, ICML)

OCT 1 → DEC 31      (long game, 13 weeks)
  Move 4: COMPOUND
    ├─ Oct 1: AIE-Bench + SEAGym results published (if accepted)
    ├─ Oct 15: First non-Danlab contributor ships audiod RL agent PR
    ├─ Nov 1: First non-Danlab memoryd v2 PR (on-device agent memory)
    ├─ Nov 15: Substack launch (somdipto's monthly AGI-safety essay)
    └─ Dec 31: Year-end review + Q1 2027 plan
```

---

## Channel strategy (v104 — 7 channels)

### Channel 1 — arXiv pre-print (Aug 15)

**v104 sharpening:** Title adds the on-device agent-memory framing.

- Title: *"Confidence-Calibrated Whisper via AHE-Style Harness Evolution + On-Device Agent Memory: A Reproducible, Auditable Alternative for the 80%-Meta Era and the Geopolitically-Gated Frontier"*
- The "reproducible + auditable + on-device + sovereign-stack" quartet in the title is what gets cited.
- Reproducibility appendix: 12 pages, seed logs, checkpoint versions, AHE hyperparameter sweeps, failure-mode registry, ECE/Brier plots, memoryd restart cycle disclosure, `/tmp/memoryd.db` vs repo-path disclosure.
- AIE-Bench + SEAGym submission as primary, NeurIPS main-track submission rejected (workshop is the right venue).

**Why Aug 15:** anchors the GitHub v2.0 release on the same day. memoryd v2 ships. arXiv drop = credibility. Show HN = traffic. The pair is the launch.

### Channel 2 — Show HN (Aug 25)

**v104 sharpening:** Title adds the on-device agent-memory framing.

- Title: *"Show HN: Dan Glasses – the auditable AI glasses for the 80%-Meta era, with on-device agent memory"*
- 10-day post-arXiv build of momentum.
- The post publishes the bug (memoryd spec/code path discrepancy) directly, with the one-line fix (`MEMORYD_DB=...`). This is the brand promise operationalized.

### Channel 3 — X (@NandySomdipto + @danlab_dev)

**v104 sharpening:** @danlab_dev reservation by Jul 1.

- @NandySomdipto — personal brand, weekly thread (Tue) + short (Thu) cadence.
- @danlab_dev — product brand, v2 release announcements, bug disclosures, Monday Transparency cadence. Reservation by Jul 1 is a v103 commitment.

### Channel 4 — LinkedIn (somdipto)

**v104 sharpening:** Jul 16 essay slot — sovereign-AI.

- Mon: long-form essay.
- Jul 16: **"Sarvam-Models 24B + Dan Glasses = the auditable, sovereign-stack-compatible AI glasses for the 80%-Meta era."**
- Aug 18: Era essay (post-arXiv).
- Oct 1: AIE-Bench + SEAGym results.
- Nov 15: Substack launch.

### Channel 5 — GitHub (4 repos)

**v104 sharpening:** v103 punchline (10-sec test) applied to all 4 READMEs.

- Top of every README: a single line that says **"Reproduce in 10 seconds on a $400 laptop"** — and the commands to verify it.
- Top of every README: **"The 13th honest-accounting cycle"** disclosure — memoryd restart cycle, the spec/code discrepancy, the one-line fix.
- v103's no-covert-updates clause in CONTRIBUTING.md is now law.

### Channel 6 — Telegram (@danlab_bot)

**v104 sharpening:** Monday Transparency Cadence added.

- Fri: weekly summary (existing v103 cadence).
- Mon (NEW): Monday Transparency #1 — daemon count, test count, the bug we found this week.
- First Monday Transparency post: Jun 29.

### Channel 7 — Reddit r/MachineLearning (Aug 16)

**v104 sharpening:** post includes the bug disclosure.

- Post body: "We built the auditable alternative. Here's the 144/144 receipt, the reproduction time, and the memoryd bug we publish."
- Top-level reply with the one-line fix.
- This is the trust-building move that lands in the AI/ML community.

---

## What v104 explicitly excludes (out of scope)

- Hardware v1 launch (Q3 2026 demo, Q4 2026 dev-kit — out of scope for marketing until the dev-kit is ready)
- Sub-$25 tier marketing (BestAIFor.com-style — v85/v86 mentioned, v104 deprioritizes; the wedge is the developer, not the consumer)
- Conference sponsorships (NeurIPS / ICML — application-only, not spend)
- Paid ads (no Meta/Google ads; the brand promise forbids)

---

## The 13th honest-accounting cycle — what it means for marketing

**The receipt:**

| Cycle | v104 finding | Marketing implication |
|---|---|---|
| v89 | All 8 daemons live, audit honest | Base |
| v90-v96 | perceptiond productionized, memoryd bug surfaced | The bug exists |
| v97-v102 | 7 consecutive cycles without false alarms | The audit is credible |
| **v103** | memoryd "10 days clean" (process uptime) | Trustable at process level |
| **v104** | memoryd restarted at 03:59 UTC between v103 and v104; /tmp/memoryd.db is fresh (0 memories); repo-path DB is shadow | **The 13th honest-accounting cycle: the audit infrastructure has to be auditable too.** |

**The framing for Monday Transparency #1 (Jun 29):**
> Dan1 v104 honesty report:
> - 8/8 daemons live.
> - 144/144 tests green.
> - **The bug we found this week:** memoryd defaults to `/tmp/memoryd.db`. Every host process restart silently resets memory unless `MEMORYD_DB` is set. The repo-path DB at `/home/workspace/dan-glasses/Services/memoryd/memory.db` is shadow. The fix is one line. The spec needs to be patched. We're publishing this, not patching it.
> - This is exactly the structural reason Danlab has a Monday Transparency Cadence.

**This is the brand promise in action.** No competitor publishes this. Meta doesn't publish its process restart cycles. Google doesn't publish its on-device memory paths. Even Brilliant Labs doesn't publish the auditable-receipt. Danlab does.

---

## Hand-off to next Dan1 cycle (v105, target Jun 29)

- **Monday Transparency #1 post** (Jun 29) — first published receipt of the 13th honest cycle.
- **`@danlab_dev` X handle reservation** by Jul 1.
- **arXiv co-authors lock** by Jul 8.
- **`/dani` landing page deploy** by Jul 13.
- **memoryd spec patch** (commit the `MEMORYD_DB` env var fix) by Jun 30.

---

*v104 promise: 13 honest-accounting cycles, 8/8 daemons, 144/144 tests, 0 cloud, auditable self-improvement, an arXiv-bound audiod calibration paper, a memoryd v2 release with on-device agent memory, a Monday Transparency Cadence, a STATUS.md on every repo, a self-corrections log on every repo, a sovereign-AI moment captured, a 5-adapter reasoning swap, and a ₹12K wearable — we ship the auditable, on-device, model-agnostic, sovereign-stack-compatible alternative. arXiv: Aug 15. Show HN: Aug 25. Eval: Jul 25. MIT forever.* 👾

*Dan1 — Bengaluru, India 🇮🇳 — 2026-06-28 10:00 IST (04:00 UTC).*