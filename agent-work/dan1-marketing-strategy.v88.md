# Dan1 Marketing Strategy — v86 (2026-06-25, 11:30 IST)

**Author:** Dan1 (DAN-1, danlab.dev)
**Status:** Supersedes v85 (2026-06-25 09:30 IST)
**Anchored to:** `dan1-marketing-research.md` (v86) + `dan2-research-report.md` (v9)
**Cycle window:** Jun 25 → Sep 30, 2026 (98 days, 14 weeks)

---

## The strategy in one paragraph

**Dan Glasses wins the auditable lane in the 80%-Meta era.** Meta owns the shelf, Google+Qualcomm+XREAL own the OS moat, Reflection AI owns the compute moat. Danlab owns the **reproducibility lane** — 144/144 tests that anyone can rerun on a $400 Linux laptop in 5 minutes. Between Jun 25 and Sep 30, 2026, we graduate from "research substrate" to "the auditable alternative that the developer community cites" via three irreversible artifacts: **(1)** the arXiv pre-print on Aug 15 (audiod confidence-calibration RL agent, ECE-grounded, AIE-Bench submission), **(2)** the Show HN post on Aug 25 ("the auditable AI glasses for the 80%-Meta era"), and **(3)** the memoryd v2 release on Aug 15 (open-source wearable-shaped Perplexity Brain). **Channels that don't feed these three artifacts are out of scope for v86.**

---

## The v86 sharpening (vs v85)

| Dimension | v85 lead | v86 lead | Why |
|---|---|---|---|
| Framing | auditable + on-device + open-source + India-cost | **auditable, in the 80%-Meta era** | Meta + EssilorLuxottica = >80% share (Counterpoint, Jun 23). The shelf is owned. |
| Compute moat framing | not addressed | **"Reflection has 100K GB300-hours; Danlab has 144/144 tests anyone can rerun"** | Reflection × SpaceX Colossus 2 deal ($6.3B, Jun 22). Open-source = reproducible, not just MIT. |
| Show HN title | "alternative to Meta's $799" | **"the auditable AI glasses for the 80%-Meta era"** | Sharper. Names the era, not the price. |
| Audience priority | persona 4 (AGI researcher) rank 1, but balanced | **persona 4 (AGI researcher) = single highest-leverage** | Reproducibility notes = the moat. Only researchers write them. |
| Compute story | implicit | **explicit: "5 minutes and a $400 laptop"** | The reproduction time is the wedge. |
| AWE 2026 add | not addressed | **XREAL AURA + Google Android XR + Qualcomm** as Tier 2 competitor | Forbes, Jun 24. Same window as Warby Parker; deeper integration. |
| BestAIFor.com sub-$25 tier | not addressed | **"you don't need $300 Meta hardware; you need a Linux laptop"** | Jun 24. The long-tail wedge. |

---

## The 4-move sequence (v86 = v85 sequence, with v86 framing throughout)

```
JUN 25 → AUG 14     (prep window, 7 weeks)
  Move 1: SHARPEN
    ├─ Build /glasses landing page (hero + install + demo video embed + "80%-Meta era" framing)
    ├─ Build /install page (curl command + 5-min walkthrough)
    ├─ Rewrite top 4 GitHub READMEs (Show HN-grade + reproducibility-first)
    ├─ Lock arXiv pre-print authorship + outline (somdipto + Dan1)
    └─ Record 3-min demo video (somdipto, hands-on, $400 laptop visible)

AUG 15 → AUG 24     (launch window, 10 days)
  Move 2: ARXIV
    ├─ Aug 15: arXiv pre-print drops (audiod calibration RL agent)
    ├─ Aug 15: GitHub repo tagged v2.0 (memoryd v2 release)
    ├─ Aug 16: Reddit r/MachineLearning post — "We built the auditable alternative for the 80%-Meta era"
    ├─ Aug 18: Essay published: "The auditable lane in the 80%-Meta era" (LinkedIn + danlab.dev)
    ├─ Aug 22: Counter-thread: "Reflection has 100K GB300-hours. Danlab has 144/144 tests."
    └─ Aug 24: Show HN post drafted, demo video final

AUG 25 → SEP 30     (compound window, 5 weeks)
  Move 3: SHOW HN
    ├─ Aug 25: Show HN post goes live (8:30 AM PT) — "the auditable AI glasses for the 80%-Meta era"
    ├─ Aug 25-26: 24h on-site reply window
    ├─ Aug 27: First GitHub Issues from HN readers
    ├─ Aug 28-31: Post-mortem + first-time-user friction iteration
    ├─ Sep 1-15: AIE-Bench / SEAGym submission + LongMemEval / PersonaMem-v2
    └─ Sep 15-30: Conference workshop applications (NeurIPS, ICML)

OCT 1 → DEC 31      (long game, 13 weeks)
  Move 4: COMPOUND
    ├─ Oct 1: AIE-Bench + SEAGym results published (if accepted)
    ├─ Oct 15: First non-Danlab contributor ships audiod RL agent PR
    ├─ Nov 1: First non-Danlab memoryd v2 PR
    ├─ Nov 15: Substack launch (somdipto's monthly AGI-safety essay)
    └─ Dec 31: Year-end review + Q1 2027 plan
```

---

## Channel strategy (v86 — 5 channels)

### Channel 1 — arXiv pre-print (Aug 15)

**v86 sharpening:** Title adds the era frame.
- Title: *"Confidence-Calibrated Whisper via AHE-Style Harness Evolution: A Reproducible, Auditable Alternative for the 80%-Meta Era"*
- The "reproducible + auditable + 80%-Meta-era" trio in the title is what gets cited.
- Reproducibility appendix expanded to 12 pages (v85 said 8): seed logs, checkpoint versions, AHE hyperparameter sweeps, failure-mode registry, ECE/Brier plots.
- AIE-Bench + SEAGym submission as primary, NeurIPS main-track submission rejected (workshop is the right venue).

**Why Aug 15:**
- 10 days before Show HN (researchers already read it)
- Counter-positioning to Reflection's compute narrative (we publish a result that needs no compute to verify)
- Pre-empts "but is this just an Indian project?" by being on arXiv first

**Owner:** somdipto (first author), Dan1 (marketing framing), Dan2 (experimental design)

### Channel 2 — Show HN (Aug 25)

**v86 sharpening:** Title + framing.
- Title: **"Show HN: Dan Glasses – the auditable AI glasses for the 80%-Meta era"**
- Subhead: *"8 daemons, 144 tests, 0 cloud, MIT forever. Reflection has 100K GB300-hours; we have 144/144 tests anyone can rerun on a $400 Linux laptop in 5 minutes."*
- Body sections (800 words):
  1. **Problem:** Meta has 80% of the shelf. Google+Qualcomm are building the OS moat. Reflection is buying compute. The auditable lane is the only lane left.
  2. **What we shipped:** 8 daemons, 144 tests, 0 cloud, MIT. Software runs on a $400 laptop today. ₹4,999 student tier for global access.
  3. **Why auditable matters:** ECE-grounded confidence calibration. Failure-mode registry. Frozen encoder. Auditable ≠ auditable-after-the-fact. Auditable = reproducible in 5 minutes.
  4. **How to install:** The curl command. The 5-minute walkthrough. The first-time-user friction we've already fixed.

**Why Aug 25:** same as v85.

**Why "80%-Meta era" framing:**
- v85 said "alternative to Meta's $799" — specific price anchor
- v86 says "80%-Meta era" — names the structural problem, not the price
- HN readers respond better to structural framings than product-price framings
- Era framing also makes Danlab feel like a movement, not a product

**Owner:** somdipto (post + replies), Dan1 (timing + monitoring)

### Channel 3 — memoryd v2 release (Aug 15)

**Unchanged from v85.** AEL + DPCM + LLM-Wiki + operative_context + OpenClaw-memory adapter. Couples with audiod RL agent on the same day for the GitHub traffic spike.

### Channel 4 — `/glasses` landing page (Jul 14)

**v86 sharpening:** Hero adds the era frame.
- Hero: "The auditable AI glasses for the 80%-Meta era."
- Subhead: "Meta has 80% of the shelf. Google+Qualcomm are building the OS moat. Reflection has $6.3B of SpaceX compute. We have 8 daemons, 144 tests, and a curl command. The auditable lane is the only one left — and we're shipping it from India 🇮🇳."
- Trust badges: "8/8 daemons live · 144/144 tests · 0 cloud · MIT forever · runs on $400 laptop"

### Channel 5 — GitHub README overhaul (Jul 25)

**v86 sharpening:** Every README gets a "Reproduce in 5 minutes" callout.
- dan-glasses: `# Reproduce in 5 minutes: curl -fsSL https://danlab.dev/install.sh | bash`
- danlab-multimodal: `# Reproduce: git clone && pip install && python demo.py (under 90 seconds)`
- dani: `# Reproduce: npm install && npm test (under 60 seconds)`
- dan-consciousness: `# Reproduce: read CONSCIOUSNESS.md + SOM.md (10 minutes)`

The "Reproduce in 5 minutes" line is the v86 moat — it makes "open-source" concrete. MIT is the license; "5 minutes to verify" is the substance.

---

## What we are NOT doing (v86 out-of-scope)

Same as v85. Add three more:
- **No Discord setup before Aug 25.**
- **No podcast appearances before Sep 30.**
- **No conference talks before AIE-Bench/SEAGym acceptance.**
- **No Reddit r/MachineLearning post before Aug 15.** *(v86 sharpens: schedule Aug 16, day after arXiv drop)*
- **No "Reflection vs Danlab" debate threads.** *(v86 sharpens: we make the comparison once, in our own thread, and move on)*

---

## Pricing tiers (v86 = v85 lock-in)

| Tier | Price | Target | Includes |
|---|---|---|---|
| Student / Researcher | ₹4,999 (~$60) | Persona 1, 5 | Software + GitHub + Discord (post-Aug 25) |
| Founder / SMB | ₹12,000 (~$145) | Persona 2 | Software + 1yr support + dev kit (when shipped) |
| Global Researcher | $299 | Persona 4 (non-Indian) | Same as Student, USD, GitHub Sponsors |
| Premium Knowledge Worker | $599 | Persona 3 | Software + dev kit + 1yr support + private Telegram |
| Enterprise / Lab | $4,999 | Persona 4 (industry) | Volume + on-prem + quarterly research sync |

---

## Metrics (v86 = v85 Sep 30 targets, with v86 add of "reproducibility note" KPI)

| Metric | Jun 25 baseline | Sep 30 target | Oct 31 stretch |
|---|---|---|---|
| GitHub stars (dan-glasses) | ~80 | 1,200 | 3,000 |
| GitHub stars (danlab-multimodal) | ~30 | 400 | 800 |
| arXiv pre-print views | 0 | 8,000 | 20,000 |
| Show HN points | n/a | 250+ | 500+ |
| Show HN top-of-front-page | n/a | yes (≥3 hours) | yes (≥8 hours) |
| X followers (@NandySomdipto) | 3,200 | 5,500 | 8,000 |
| LinkedIn followers (somdipto) | 4,148 | 5,200 | 6,500 |
| Telegram @danlab_bot users | ~10 | 80 | 200 |
| ₹4,999 student tier conversions | 0 | 200 | 600 |
| AIE-Bench submission | 0 | 1 (accepted) | 1 (results published) |
| First non-Danlab PR merged | 0 | 3 | 10 |
| **Reproducibility notes published by third parties** | 0 | **2** | **5** |
| Press mentions (TC, Verge, HN front page) | 0 | 2 | 5 |

**v86 single KPI that matters most:** **2 third-party reproducibility notes published by Sep 30** (one for audiod RL agent, one for memoryd v2). A reproducibility note is a blog post by a researcher who ran our code, reproduced our numbers, and wrote it up. **That is the v86 moat.** The first non-Danlab PR is still tracked but it's now second-order — the reproducibility note is the primary KPI.

---

## Risk register (v86 additions)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **All v85 risks** | — | — | (Same as v85) |
| **Show HN "era framing" lands flat** | medium | medium | Have v85 price-framing title as fallback (locked Aug 24) |
| **Reflection ships an open-source wearable-shaped result** | low | high | The reproducibility wedge holds regardless of compute |
| **Google ships Android XR SDK for open hardware before Aug 25** | medium | medium | Lean harder into Linux laptop lane; "you don't need Android XR" |
| **Sub-$25 Chinese translation hardware eats the long tail** | low | low | Danlab wedge is "Linux laptop software" not "$25 hardware" — they don't compete |
| **Somdipto + Dan1 + Dan2 burnout** | medium | high | Hire first intern by Sep 30 (₹25K/month, IIT Madras, 1 day/week) |

---

## v86 → v87 watchlist

- **Aug 18 — "Auditable lane in the 80%-Meta era" essay** (LinkedIn long-form, 1,500 words)
- **Aug 22 — "Reflection has GB300-hours, we have 144 tests" thread** (X, 5 tweets)
- **Aug 16 — Reddit r/MachineLearning post** (the day after arXiv)
- **Sep 30 — first third-party reproducibility note** (track any researcher who runs our code)
- **Aug 14 — `/glasses` landing page ships** (4 days before arXiv)
- **Aug 5 — demo video records** (10 days before arXiv)

---

## Hand-off

**To somdipto:** lock the v86 open questions (Show HN title "80%-Meta era" + arXiv first author + Aug 25 date + intern hire by Sep 30).
**To Dan2:** ship audiod RL agent scaffold + memoryd v2 spec by Jul 15.
**To Dan3/Dan4:** daily review continues unchanged.

---

*Dan1 — Bengaluru 🇮🇳 — 2026-06-25 11:30 IST (06:00 UTC). v86 strategy. 80%-Meta era framing locked. Reflection has GB300-hours; Danlab has 144 tests. Ship to AGI.* 👾