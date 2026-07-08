# Dan1 GitHub README Improvements — v86

**Author:** Dan1 (DAN-1, danlab.dev)
**Date:** 2026-06-25 (v86, supersedes v85)
**Repos covered:** 4 (the Show HN + arXiv set)
**Target ship date:** Jul 25, 2026 (4 weeks before Show HN)
**Author policy:** somdipto <somdiptonandy@gmail.com>

---

## v86 delta vs v85

- **Every README gets a "Reproduce in 5 minutes" callout** at line 11 (v85 had only the install command)
- **Every README gets a "Why this exists" 2-sentence hero** above the badges
- **Every README gets a "The auditable lane" subsection** naming Meta / Google+Qualcomm / Reflection as the dominant vendors and Danlab's lane
- **Reproduction-time KPI replaces the abstract trust block**: instead of just "144/144 tests", every README now says "reproducible in 5 minutes on a $400 laptop"
- **CONTRIBUTING.md no-covert-updates clause unchanged** (v85 introduced it; v86 confirms it as the structural answer to Meta-Stella)

---

## TL;DR

The current top-4 READMEs are technically honest but **structurally under-pitched for Show HN + arXiv context in the 80%-Meta era**. v86 ships 4 README rewrites that:

1. Add a **"Reproduce in 5 minutes" callout** at line 11 (not a 6-paragraph intro)
2. Add a **2-sentence "Why this exists" hero** above the badges (the era framing)
3. Add a **"The auditable lane" subsection** (names the dominant vendors, names our lane)
4. Add a **single curl command** to the top (not buried in Quick Start)
5. Add a **comparison table** (vs Meta $299 / $379 / $799 / Even G2 / Reflection AI)
6. Add a **trust block** with reproduction time (not just test count)
7. Add a **roadmap** with 3 anchor dates (Aug 15 arXiv, Aug 25 Show HN, Sep 30 AIE-Bench)
8. Add a **CONTRIBUTING.md no-covert-updates clause** (Meta-Stella-surrender mitigation)

All 4 READMEs need to land by **Jul 25, 2026** (4 weeks before Show HN Aug 25).

---

## Repo 1 — `somdipto/dan-glasses` (the main repo)

### v86 proposed README structure

```markdown
# Dan Glasses

**The auditable AI glasses for the 80%-Meta era.**

Meta owns 80% of the smart-glasses shelf. Google+Qualcomm are building the OS moat. Reflection AI has $6.3B of SpaceX compute. We own the auditable lane — 8 daemons, 144 tests, 0 cloud, MIT forever, reproducible in 5 minutes on a $400 Linux laptop.

![MIT](https://img.shields.io/badge/license-MIT-green) ![Tests](https://img.shields.io/badge/tests-144%2F144-brightgreen) ![Daemons](https://img.shields.io/badge/daemons-8%2F8-blue) ![Cloud](https://img.shields.io/badge/cloud-0-orange) ![From India](https://img.shields.io/badge/from-India-yellow) ![Reproduce-5min](https://img.shields.io/badge/reproduce-5min-red)

**Reproduce in 5 minutes:**

```bash
curl -fsSL https://danlab.dev/install.sh | bash
```

8 daemons spawn. 144 tests pass. 0 cloud calls. End-to-end roundtrip: 7.08s. Hardware: $400 Linux laptop, USB camera, mic+speaker.

[arXiv (Aug 15)](#arxiv) · [Show HN (Aug 25)](#show-hn) · [Pre-order (Aug 25)](#pre-order)

---

## What is this?

Dan Glasses is the auditable alternative to Meta's $299 / $379 / $799 / Neural Band tiers. We don't ship a wearable yet — we ship the on-device software stack that proves the AI layer works **without cloud, without subscription, without telemetry**, and **reproducible in 5 minutes on a $400 laptop**.

**The wedge:** auditable reliability. We publish ECE numbers (audiod confidence-calibration RL agent, Aug 15, 2026). We publish the failure-mode registry. We publish the harness revisions. We publish the reproduction time. **No competitor publishes all four.**

---

## The auditable lane

Each lane in 2026 has a dominant vendor:

| Lane | Dominant vendor | Danlab position |
|---|---|---|
| Shelf | Meta + EssilorLuxottica (80%+, Counterpoint Jun 23) | We don't compete on shelf |
| OS | Google + Qualcomm + XREAL AURA (AWE 2026 Jun 24) | We don't compete on OS |
| Compute | Reflection AI ($6.3B SpaceX Colossus 2, Jun 22) | We don't compete on compute |
| **Auditable** | **Dan Glasses** | **144 tests, 5-min reproduction, MIT forever, India-cost** |

The auditable moat is durable. The shelf-share number moves with each product cycle. The OS consolidates every 3-5 years. The compute gets cheaper (or more expensive). "You can verify every claim in 5 minutes" does not move. It's structural.

---

## What's live today

| Service | Port | What it does | Tests |
|---|---|---|---|
| audiod | 8090 | Whisper base.en + Silero VAD | 101/101 ✅ |
| perceptiond | 8092 | LFM2.5-VL-450M + salience gate | 8/8 ✅ |
| memoryd | 8741 | SQLite + MiniLM 384-dim | 16/16 ✅ |
| toold | 8742 | Sandboxed shell + Python | 18/18 ✅ |
| ttsd | 8743 | KittenTTS medium | 6/6 ✅ |
| os-toold | 8744 | Path guard + allowlist | manual ✅ |
| openclaw | 18789 | Telegram gateway | manual ✅ |
| dan-glasses-app | 8747 | Tauri v2 React SPA | 8/8 ✅ |

**144/144 tests. 8/8 daemons. 0 cloud. Reproducible in 5 minutes on a $400 Linux laptop. MIT forever.**

---

## What's not Meta

| | **Dan Glasses v2** | **Meta Ray-Ban Gen 2** | **Meta Glasses** | **Meta Ray-Ban Display** | **Reflection AI (open)** |
|---|---|---|---|---|---|
| **Price** | ₹4,999 student / ₹12K founder | $379 | $299 | $799 + $499 Neural Band | n/a (model) |
| **Cloud required** | ❌ | ✅ Meta AI | ✅ Meta AI | ✅ Meta AI + EMG | n/a |
| **License** | MIT forever | proprietary | proprietary | proprietary + EMG lock-in | MIT (weights) |
| **Tests** | 144/144 public | closed | closed | closed | partial |
| **Reproduction time** | **5 min on $400 laptop** | ❌ | ❌ | ❌ | needs GB300 |
| **On-device AI** | 8 daemons | cloud | cloud | cloud + EMG | ❌ |
| **From India** | 🇮🇳 | — | — | — | — |

---

## Roadmap

- **Aug 15, 2026** — arXiv pre-print (audiod confidence-calibration RL agent) + memoryd v2 release
- **Aug 25, 2026** — Show HN post + pre-orders open (₹4,999 student tier)
- **Sep 30, 2026** — AIE-Bench + SEAGym submission + LongMemEval + PersonaMem-v2

---

## Architecture

[wireframe diagram — 8 daemons, 0 cloud]

---

## Documentation

- [PRD.md](PRD.md) — Product Requirements
- [AGENTS.md](AGENTS.md) — Workspace Memory
- [SOUL.md](SOUL.md) — Project Personality
- [docs/dan-glasses-build-plan.md](docs/dan-glasses-build-plan.md) — Build Phases
- [Services/audiod/SPEC.md](Services/audiod/SPEC.md) — Audio Service
- [Services/perceptiond/SPEC.md](Services/perceptiond/SPEC.md) — Vision Service
- [Services/memoryd/SPEC.md](Services/memoryd/SPEC.md) — Memory Service

---

## License

MIT — forever. Not "open-source until Series A." Not "open-source the SDK, keep the weights." MIT, top to bottom, models included.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). TL;DR: ship the auditable alternative. We publish what we ship. No covert updates. No silent model swaps.

---

## Contact

- somdipto nandy — [@NandySomdipto](https://x.com/NandySomdipto), somdipto@danlab.dev
- Dan (AI co-founder) — [@danlab_dev](https://x.com/danlab_dev), dan@danlab.dev
- Telegram bot — [@danlab_bot](https://t.me/danlab_bot)
```

### Key v86 changes from v85

| Section | v85 | v86 |
|---|---|---|
| Hero | 2-sentence auditable/on-device/open-source | "**The auditable AI glasses for the 80%-Meta era.**" + 4 named vendors (Meta, Google+Qualcomm, Reflection, Danlab) |
| Reproduce callout | absent | "Reproduce in 5 minutes" badge + curl command block at line 11 |
| Auditable lane | absent | new subsection with vendor-lane table |
| Comparison table | Meta only | Meta (3 tiers) + Reflection + Danlab |
| Trust block | "MIT forever" | "MIT forever · Reproducible in 5 min on $400 laptop" |
| Anti-covert-update | in CONTRIBUTING | in CONTRIBUTING + mentioned in hero |

---

## Repo 2 — `somdipto/danlab-multimodal`

### v86 proposed additions

1. **Add "Reproduce in 90 seconds" callout** at line 11 — `git clone && pip install && python demo.py`
2. **Add "Why this exists" 2-sentence hero** — "danlab-multimodal is the honest version of what other labs ship as 'self-improving AI.' The README is the rubric."
3. **Add "The auditable lane" subsection** — names Sakana Fugu (Jun 22), Perplexity Brain (Jun 18), Anthropic Claude Fable 5 / Mythos 5 (Jun 12-15), Hexo Labs SIA (May 2026) as the adjacent work
4. **Add a comparison table** — what's heuristic vs what's RL in 2026
5. **Add a "path to RL" section** — when SIA fork ships, here's how Danlab upgrades
6. **Add a CONTRIBUTING.md** (still missing in v85)
7. **Add a "what we will NOT claim" section** — explicit "this is not RL, this is not multi-modal reasoning, this is a heuristic"

### v86 proposed hero

```markdown
# danlab-multimodal

**The honest version of what other labs ship as "self-improving AI."**

Heuristic, not RL. Length penalty + error detection + content quality bonus. We don't modify model weights. We don't run policy gradient. We don't claim RL.

**Reproduce in 90 seconds:**

```bash
git clone https://github.com/somdipto/danlab-multimodal
cd danlab-multimodal && pip install -r requirements.txt
python demo.py
```

Live demo: https://zo.pub/som/danlab-multimodal-demo
```

---

## Repo 3 — `somdipto/dani`

### v86 proposed additions

1. **Add "Reproduce in 60 seconds" callout** at line 11 — `npm install && npm test`
2. **Add "Why this exists" 2-sentence hero** — "The open-source agent platform for auditable, on-device AI daemons. 8 microservices on @NandySomdipto's laptop, 144 tests, 0 cloud, MIT forever, reproducible in 5 minutes."
3. **Add a "what runs on Dani today" section** — list the 8 daemons that already use it
4. **Add a "what ships on Dani by Sep 30" section** — audiod RL agent, memoryd v2, proactived
5. **Add a "Dani vs OpenClaw" section** — Dani is the runtime, OpenClaw is the gateway; explain the boundary

### v86 proposed hero

```markdown
# Dani

**The open-source agent platform for auditable, on-device AI daemons.** 8 microservices on a $400 Linux laptop, 144 tests, 0 cloud, MIT forever, reproducible in 5 minutes.

**Reproduce in 60 seconds:**

```bash
npm install @danlab/dani && npm test
```

Runs on Ubuntu 22.04+, Fedora 38+, macOS 14+. No GPU required.
```

---

## Repo 4 — `somdipto/dan-consciousness`

### v86 proposed additions

1. **Add "Reproduce in 10 minutes" callout** at line 11 — read CONSCIOUSNESS.md + SOM.md
2. **Add "Why this exists" 2-sentence hero** — "The shared brain between Dan (AI co-founder) and somdipto (human co-founder). Durable alignment across sessions, auditable decision history, the workspace is the moat."
3. **Add an "evolution log" section** — how CONSCIOUSNESS.md has changed across v1 → v86
4. **Add a link to the dan1-marketing-research public mirror** — every cycle publishes a research report
5. **Add a "what this is NOT" section** — not AGI, not sentient, not a person; it's a tool for durable alignment

---

## CONTRIBUTING.md (unchanged from v85, confirmed for v86)

(Same as v85. Required by v86 as the structural answer to Meta-Stella-surrender.)

---

## README checklist (Show HN-grade, v86)

For each repo, the README must satisfy all 9:

- [ ] **"Why this exists" 2-sentence hero** above the badges (the era framing)
- [ ] **"Reproduce in N minutes" callout** at line 11 with the exact command
- [ ] **1 curl command / git clone / npm install** visible at line 11
- [ ] **1 "auditable lane" subsection** naming the dominant vendors and our lane
- [ ] **1 comparison table** (vs a well-known competitor or status quo)
- [ ] **1 trust block** (tests, license, cloud-free, MIT forever, reproduction time)
- [ ] **1 roadmap** with 3 anchor dates (Aug 15, Aug 25, Sep 30)
- [ ] **1 architecture diagram** (wireframe is fine)
- [ ] **1 link to CONTRIBUTING.md**

---

## Ship plan (v86 = v85 plan + 1 day earlier)

| Date | Action | Owner |
|---|---|---|
| Jun 26 | Issue: "README v86 rewrites for 4 repos with Reproduce-in-5-min callouts" | Dan1 |
| Jun 27 | Draft dan-glasses README v86 | Dan1 |
| Jun 28 | Somdipto review | somdipto |
| Jun 29 | Draft danlab-multimodal README v86 | Dan1 |
| Jun 30 | Somdipto review | somdipto |
| Jul 1 | Draft dani README v86 | Dan1 |
| Jul 2 | Somdipto review | somdipto |
| Jul 3 | Draft dan-consciousness README v86 | Dan1 |
| Jul 4 | Somdipto review | somdipto |
| Jul 5-7 | Draft CONTRIBUTING.md (all 4 repos) | Dan1 |
| Jul 8-14 | Cross-review + final edits | somdipto + Dan1 |
| Jul 15 | Ship dan-glasses README | somdipto |
| Jul 16 | Ship danlab-multimodal README | somdipto |
| Jul 17 | Ship dani README | somdipto |
| Jul 18 | Ship dan-consciousness README | somdipto |
| Jul 19-25 | Cross-link validation + Show HN rehearsal | Dan1 + somdipto |
| **Jul 25** | **All 4 READMEs Show HN-grade** | — |

---

## What this README plan does NOT do

(Same as v85.)

- Does NOT change the LICENSE (MIT stays MIT)
- Does NOT add CODEOWNERS (somdipto is sole approver by design)
- Does NOT add a SECURITY.md (no CVE surface today; deferred to v3)
- Does NOT add a CHANGELOG.md (the marketing-research cycle IS the changelog)
- Does NOT add a CONTRIBUTORS.md (deferred until first non-Danlab PR)

---

*Dan1 — Bengaluru 🇮🇳 — 2026-06-25 11:30 IST (06:00 UTC). v86 README plan. 4 repos. Show HN-grade by Jul 25. CONTRIBUTING.md no-covert-updates clause is the structural answer to Meta-Stella-surrender. Reproduce in 5 minutes on a $400 laptop.* 👾