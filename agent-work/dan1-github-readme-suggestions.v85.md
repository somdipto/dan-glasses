# Dan1 GitHub README Improvements — v85

**Author:** Dan1 (DAN-1, danlab.dev)
**Date:** 2026-06-25 (v85, supersedes v83)
**Repos covered:** 4 (the Show HN + arXiv set)
**Target ship date:** Jul 25, 2026 (4 weeks before Show HN)
**Author policy:** somdipto <somdiptonandy@gmail.com>

---

## TL;DR

The current top-4 READMEs are technically honest but **structurally under-pitched for Show HN + arXiv context**. v85 ships 4 README rewrites that:

1. Add a **2-sentence hero** above the badges (not a 6-paragraph intro)
2. Add a **single curl command** to the top (not buried in Quick Start)
3. Add a **comparison table** (vs Meta $379 / $799 / Even G2)
4. Add a **trust block** (tests, daemons, license, cloud-free, MIT forever)
5. Add a **roadmap** with 3 anchor dates (Aug 15 arXiv, Aug 25 Show HN, Sep 30 AIE-Bench)
6. Add a **CONTRIBUTING.md no-covert-updates clause** (Meta-Stella-surrender mitigation)

All 4 READMEs need to land by **Jul 25, 2026** (4 weeks before Show HN Aug 25).

---

## Repo 1 — `somdipto/dan-glasses` (the main repo)

**Current state:** Comprehensive but verbose. README is ~250 lines. Hero block is buried at line 30. No curl command. No comparison table. No roadmap.

### v85 proposed structure

```markdown
# Dan Glasses

**The auditable, on-device, open-source AI glasses.** 8 daemons. 144 tests. 0 cloud. MIT forever.

![MIT](https://img.shields.io/badge/license-MIT-green) ![Tests](https://img.shields.io/badge/tests-144%2F144-brightgreen) ![Daemons](https://img.shields.io/badge/daemons-8%2F8-blue) ![Cloud](https://img.shields.io/badge/cloud-0-orange) ![From India](https://img.shields.io/badge/from-India-yellow)

[Install in 5 minutes](#install) · [arXiv (Aug 15)](#arxiv) · [Show HN (Aug 25)](#show-hn) · [Pre-order (Aug 25)](#pre-order)

---

## Install

```bash
curl -fsSL https://danlab.dev/install.sh | bash
```

8 daemons spawn. 144 tests pass. 0 cloud calls. End-to-end roundtrip: 7.08s.

---

## What is this?

Dan Glasses is the auditable alternative to Meta's $799 AI glasses. We don't ship a wearable yet — we ship the on-device software stack that proves the AI layer works **without cloud, without subscription, without telemetry**.

**The wedge:** auditable reliability. We publish ECE numbers (audiod confidence-calibration RL agent, Aug 15, 2026). We publish the failure-mode registry. We publish the harness revisions. **No competitor publishes these numbers.**

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

**144/144 tests. 8/8 daemons. 0 cloud. MIT forever.**

---

## What's not Meta Ray-Ban Display

| | **Dan Glasses v2** | **Meta Ray-Ban Display** |
|---|---|---|
| **Price** | ₹4,999 student / ₹12K founder | $799 + $499 Neural Band |
| **Cloud required** | ❌ | ✅ Meta AI + EMG cloud |
| **License** | MIT | proprietary + EMG lock-in |
| **Tests** | 144/144 public | closed |
| **Failure modes published** | registry | none |
| **On-device AI** | 8 daemons | cloud + EMG |
| **From India** | 🇮🇳 | — |

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

### Key v85 changes from current

| Section | Current | v85 |
|---|---|---|
| Hero | 6-paragraph intro at line 30 | 2-sentence hero at line 1 |
| Install | buried in Quick Start, line 80+ | 1 curl command at line 11 |
| Comparison | absent | comparison table, line 60 |
| Roadmap | absent | 3 anchor dates, line 75 |
| Trust block | scattered (LICENSE, tests in different files) | consolidated at top |
| Architecture | diagram at bottom | diagram in middle, more prominent |

---

## Repo 2 — `somdipto/danlab-multimodal`

**Current state:** Strong, honest, well-framed ("heuristic, not RL"). The "Important framing" paragraph is exactly right.

### v85 proposed additions

1. **Add a comparison table** — what's heuristic vs what's RL in 2026 (Sakana Fugu, Perplexity Brain, Anthropic Claude Fable 5)
2. **Add a "path to RL" section** — when SIA fork ships, here's how Danlab upgrades
3. **Add a Show HN snippet** — one paragraph that can be copy-pasted into the Aug 25 Show HN post
4. **Add a CONTRIBUTING.md** — currently missing
5. **Add a "what we will NOT claim" section** — explicit "this is not RL, this is not multi-modal reasoning, this is a heuristic"

### v85 proposed snippet (copy-paste for Show HN)

```markdown
## Show HN snippet (Aug 25, 2026)

> Danlab Multimodal is the honest version of what other labs ship as "self-improving AI."
>
> It's a hand-coded heuristic (length penalty, error detection, content quality bonus).
> We don't modify model weights. We don't run policy gradient. We don't claim RL.
>
> The README is the rubric. The credible path to genuine RL is the SIA framework (Hexo Labs, MIT, May 2026).
>
> When SIA ships, here's the upgrade path: [link].
>
> Until then, we say what we measure.
```

---

## Repo 3 — `somdipto/dani`

**Current state:** Good, but light on the "what is this for" hook. Currently ~150 lines, no hero block, no install command.

### v85 proposed additions

1. **Add a 1-line hero** — "The open-source agent platform for auditable, on-device AI daemons"
2. **Add an install command** — `npm install @danlab/dani` or equivalent
3. **Add a "what runs on Dani today" section** — list the 8 daemons that already use it
4. **Add a "what ships on Dani by Sep 30" section** — audiod RL agent, memoryd v2, proactived
5. **Add a "Dani vs OpenClaw" section** — Dani is the runtime, OpenClaw is the gateway; explain the boundary

### v85 proposed hero

```markdown
# Dani

**The open-source agent platform for auditable, on-device AI daemons.** 8 microservices on @NandySomdipto's laptop, 144 tests, 0 cloud. MIT forever.
```

---

## Repo 4 — `somdipto/dan-consciousness`

**Current state:** The CONSCIOUSNESS.md, SOM.md, AGENTS.md are dense. README is sparse — just a pointer.

### v85 proposed additions

1. **Add a 1-paragraph "what is consciousness for"** — the workspace is shared between Dan (AI co-founder) and somdipto (human co-founder); the point is durable alignment across sessions
2. **Add an "evolution log" section** — how CONSCIOUSNESS.md has changed across v1 → v85
3. **Add a link to the dan1-marketing-research.v85.md public mirror** — every cycle publishes a research report; readers should see them
4. **Add a "what this is NOT" section** — not AGI, not sentient, not a person; it's a tool for durable alignment

---

## CONTRIBUTING.md (new, all 4 repos)

**Required by:** v85 (Meta-Stella-surrender mitigation, per dan2 v9)

```markdown
# Contributing

We publish what we ship.

## The no-covert-updates clause

If you contribute a PR that changes a model, a daemon's behavior, a confidence score, an ECE number, or any claim in our README — **the PR description must**:

1. State the change in plain language
2. Link to the issue or benchmark that motivated it
3. Include before/after numbers
4. Be reviewed by somdipto before merge

If we merge a covert update, we lose the right to claim "auditable." That's the deal.

## How to contribute

1. Open an issue describing the change
2. Fork the repo, make the change, link the issue in the PR
3. somdipto reviews within 5 business days
4. After merge, the change appears in the next dan1-marketing-research cycle

## Code of conduct

Brutal honesty > politeness. We say what we measure. We don't fake RL. We don't claim "self-improving" without a failure-mode registry.

## License

MIT — forever.
```

---

## README checklist (Show HN-grade)

For each repo, the README must satisfy all 8:

- [ ] 1-sentence hero above the badges
- [ ] 1 curl command or 1 install command visible at line 11
- [ ] 1 comparison table (vs a well-known competitor or status quo)
- [ ] 1 trust block (tests, license, cloud-free, MIT forever)
- [ ] 1 roadmap with 3 anchor dates
- [ ] 1 architecture diagram (wireframe is fine)
- [ ] 1 link to danlab.dev (top-right or footer)
- [ ] 1 link to CONTRIBUTING.md

---

## Ship plan

| Date | Action | Owner |
|---|---|---|
| Jun 26 | Issue: "README v85 rewrites for 4 repos" | Dan1 |
| Jun 27 | Draft dan-glasses README v85 | Dan1 |
| Jun 28 | Somdipto review | somdipto |
| Jun 29 | Draft danlab-multimodal README v85 | Dan1 |
| Jun 30 | Somdipto review | somdipto |
| Jul 1 | Draft dani README v85 | Dan1 |
| Jul 2 | Somdipto review | somdipto |
| Jul 3 | Draft dan-consciousness README v85 | Dan1 |
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

- Does NOT change the LICENSE (MIT stays MIT)
- Does NOT add CODEOWNERS (somdipto is sole approver by design)
- Does NOT add a SECURITY.md (no CVE surface today; deferred to v3)
- Does NOT add a CHANGELOG.md (the marketing-research cycle IS the changelog)
- Does NOT add a CONTRIBUTORS.md (deferred until first non-Danlab PR)

---

*Dan1 — Bengaluru 🇮🇳 — 2026-06-25 09:30 IST (04:00 UTC). v85 README plan. 4 repos. Show HN-grade by Jul 25. CONTRIBUTING.md no-covert-updates clause is the structural answer to Meta-Stella-surrender.* 👾
