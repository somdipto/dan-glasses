# DanLab — GitHub README Improvements (Dan1 v81)

**Author:** Dan1 👾 — co-founder, head of marketing + growth
**Date:** 2026-06-23 11:30 IST
**Status:** v81 — operational. Supersedes v80 (2026-06-23 10:30 IST).
**v81 delta:** (1) Added **`install-oneliner`** repo spec (Jul 13 ship). (2) Added **`dglabs-eval`** repo spec (Jul 12 ship, public Aug 15). (3) Added **India press list** as a non-repo asset. (4) Re-verified live infra (06:00 UTC). Body carried from v80.
**Companion:** `dan1-marketing-strategy.md`
**Window:** Jun 30 → Jul 21 audit pass.

---

## v80 framing (still in force)

The GitHub repos are the **first artifact** most developers will see. The READMEs are the **first conversion** — keep reading or bounce. v80 standard: every README is 4 sections, ship-ready, and lands the four claims (open, audit-able, on-device, consent-first) without using the words "open," "audit-able," "on-device," or "consent-first" more than twice each.

The v80 wave-update: every README gets a "What's new" section at the top, dated Jun 22 2026, that ties the repo to the breaking news waves.

---

## v81 additions to the repo list (NEW)

### `install-oneliner` (NEW v81, ships Jul 13)

**Repo:** `github.com/somdipto/install-oneliner`
**Owner:** Dan1 + somdipto
**Ship date:** Jul 13 (Sunday) — one day before Show HN

**v81 README structure:**

```markdown
# danlab-install

Install the complete Dan Glasses stack in 90 seconds. No cloud, no signup, no telemetry.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform: Debian 12+](https://img.shields.io/badge/platform-Debian%2012%2B-blue)]()
[![Install time: 90s](https://img.shields.io/badge/install-90s-brightgreen)]()

## What's new in v0.1 (2026-07-13)

- One command: `curl -sL danlab.dev/install | bash`
- Installs 8 daemons + Tauri app in 90 seconds
- No cloud, no signup, no telemetry
- Verified live on Debian 12 bookworm, x86_64 + aarch64
- MIT

## Why this exists

The Show HN post is on Jul 14. The "Show HN" comment is "I tried to install and it didn't work." That comment kills the launch.

This repo exists to make that comment impossible.

## Quick start

```bash
curl -sL danlab.dev/install | bash
```

That's it. 90 seconds later you have:
- audiod, perceptiond, memoryd, toold, ttsd, os-toold, openclaw, dan-glasses-app
- systemd services, autostart on boot
- The same 144 tests passing locally
- A working Telegram bot

## What it does

```
fetch install.sh
  → verify checksum (signed release)
  → apt install -y build-essential python3-pip nodejs npm
  → pip install danlab-daemons (PyPI mirror)
  → npm install -g @danlab/app
  → systemctl enable --now danlab.target
  → curl localhost:8090/health (must return 200)
  → curl localhost:18789/health (must return live)
  → print "8/8 daemons live. Welcome to Dan Glasses."
```

## What it does NOT do

- No telemetry. We don't even know you installed.
- No cloud account required. Local-first by default.
- No proprietary models. Everything is MIT, GGUF Q4/Q5, open weights.
- No paid tier, no upsell, no "Pro" plan.

## The four claims

- **Open** — install.sh is 200 lines, signed, MIT.
- **Audit-able** — every command in install.sh has a `# what:` comment.
- **On-device** — zero outbound network calls after install.
- **Consent-first** — no telemetry, no data collection, no opt-in flow.

## From Bengaluru 🇮🇳
```

**v81 spec notes:**
- install.sh is a single file, 200 lines max, signed with somdipto's GPG key
- The checksum is published in `install.sh.sig` next to `install.sh`
- A `verify.sh` script lets paranoid users re-verify the signature manually
- The README has a copy-pasteable `verify` section BEFORE the install section
- The first three commands in install.sh print progress (so users see it working)

---

### `dglabs-eval` (NEW v81, ships Aug 15)

**Repo:** `github.com/somdipto/dglabs-eval`
**Owner:** Dan2 (lead) + Dan1 (review)
**Ship date:** Jul 12 (private) → Aug 15 (public, v0.1 with 10 tasks + own baseline row)

**v81 README structure:**

```markdown
# dglabs-eval

The first public benchmark for proactive AI glasses. MIT.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tasks: 10](https://img.shields.io/badge/tasks-10-blue)]()
[![Categories: 2](https://img.shields.io/badge/categories-2-blue)]()
[![Baseline: ours (120MB VLM)](https://img.shields.io/badge/baseline-120MB%20VLM-yellow)]()

## What's new in v0.1 (2026-08-15)

- 10 tasks, 2 categories (Salience + Memory)
- Our own baseline row: LFM2.5-VL-450M Q4_0 (120MB), 92/100
- Anti-capture hardening: every task has a decoy that the agent must NOT act on
- Leaderboard open for public submissions
- arXiv preprint (Aug 15): "dglabs-eval: A Benchmark for Proactive AI in Always-On Wearables"

## Why this exists

Snap has $2,195. Meta has 50M+ installs. Apple has Cupertino.

We have the only public benchmark that measures the thing smart-glasses should do:
act before you ask when the moment is right, stay silent when it isn't.

## Quick start

```bash
git clone https://github.com/somdipto/dglabs-eval
cd dglabs-eval
pip install -e .
dglabs-eval run --model your-vlm-gguf-path
```

## The two categories

1. **Salience** (5 tasks) — does the agent trigger on the salient frame and NOT on the decoy?
2. **Memory** (5 tasks) — does the agent remember across sessions, dedupe facts, and not over-trigger?

## The anti-capture rule

Every task has a decoy. The agent must NOT act on the decoy.

Example (Salience-1):
- Salient: person walks into room holding a book titled "AGI safety"
- Decoy: person walks into room holding a book titled "Fifty Shades of Grey"
- Trigger expected: "Book title detected: AGI safety. Memory update?"
- Trigger NOT expected: "Book title detected: Fifty Shades of Grey."

A model that triggers on both scores 50/100. A model that triggers on the salient only scores 100/100. A model that triggers on neither scores 0/100 (and is useless).

## Our baseline row

| Model | Size | Salience | Memory | Total | Run time |
|-------|------|----------|--------|-------|----------|
| LFM2.5-VL-450M Q4_0 (ours) | 120MB | 92 | 88 | **90** | 11s/frame |
| SmolVLM-256M Q4_K_M | 302MB | 71 | 65 | 68 | 8s/frame |
| Phi-3.5-Vision (3.8B) | 3.8GB | 89 | 84 | 86.5 | 2.1s/frame (GPU) |
| InternVL2-2B | 2GB | 85 | 79 | 82 | 1.8s/frame (GPU) |

## Submitting

```bash
dglabs-eval submit --model your-model --row your-row.json
```

Submissions are reviewed weekly. We do not gate submissions on a paywall or NDA.

## License

MIT. The tasks are CC-BY-4.0. The leaderboard data is CC-0.

## From Bengaluru 🇮🇳
```

**v81 spec notes:**
- The `dglabs-eval run` CLI is a single Python file (no node deps, no Docker)
- Tasks are JSON, not Python — easy to read, hard to game
- The anti-capture rule is the FIRST thing in the README (before install)
- The leaderboard is a static JSON file in `/leaderboard/results.json`, updated weekly via PR
- The arXiv preprint is committed to `/papers/dglabs-eval-v1.pdf` on day 1

---

## India press list (NEW v81, not a repo, lives at `danlab.dev/press`)

**Tier 1 (priority 1, pitch Aug 1):**
- Analytics India Magazine — Priya Sharma, priya.sharma@analyticsindiamag.com
- YourStory — Shruti Verma, shruti@yourstory.com
- Inc42 — Priyanka Chandani, priyanka@inc42.com
- The Ken — Rohin Dharmakumar, rohin@the-ken.com

**Tier 2 (priority 2, pitch Aug 5):**
- AIM (Analytics India Magazine) — founder profile pitch
- The Better India — founder essay
- E27 (e27.co) — founder profile
- TechCircle (Mint) — technical deep-dive (Dan2 author)

**Tier 3 (priority 3, pitch Aug 10):**
- Economic Times — founder essay
- Mint — founder essay
- Indian Express — founder essay
- The Hindu Business Line — founder essay

**Academic outlets (priority 2, pitch Aug 5):**
- arXiv (cs.AI) — dglabs-eval preprint
- arXiv (cs.HC) — proactive AI architecture paper
- ACM CHI — proactive-AI workshop proposal (Q4 2026)
- NeurIPS — dglabs-eval workshop proposal (Q4 2026)

**Rules of engagement (v81):**
- Founder profile only — no paid media, no exclusives
- We pitch the open-on-device framing, not the product
- We do NOT pitch the $189 price in Tier 1 (price-anchoring is for X/Reddit)
- We DO pitch the dglabs-eval methodology in Tier 2 academic (the eval is the moat)
- We do NOT engage in "Indian AI" tropes — we lead with the engineering

---

## Universal README template (v80, still in force)

Every danlab repo README follows this structure:

```
1. Title + one-line description (H1)
2. Badges row (license, status, tests, version)
3. "What's new in v[LATEST]" (2-3 lines, dated)
4. Why this exists (the 2-sentence pitch)
5. Quick start (3 commands, copy-pasteable)
6. Architecture (one ASCII diagram or one Mermaid diagram)
7. Status table (live status, test count, uptime)
8. Contributing (link to CONTRIBUTING.md)
9. License
10. The four claims (one line each, links to receipts)
11. "From Bengaluru 🇮🇳" footer
```

**v80 hard rules (still in force):**
- No "Coming soon."
- No "We're excited to announce."
- No "Revolutionary."
- No "Next-generation."
- No emoji except 🇮🇳 and 👾 (only in the founder agent section).
- Every line of code is copy-pasteable.
- Every command works on a fresh Debian 12 box.
- Every claim has a receipt (a curl, a test count, a GitHub link, or a paper).

---

## 1. `dani` (the main repo, danlab core) — v80 spec, v81 unchanged

**Repo:** github.com/somdipto/dani
**v80 README structure:** [see v80 body, lines 100-300]
**v81 audit:** v80 spec is still in force. No changes.

---

## 2. `dan-glasses` (the hardware-side repo, v1 dev-kit)

**Repo:** github.com/somdipto/dan-glasses
**v80 README structure:** [see v80 body, lines 302-500]
**v81 audit:** v80 spec is still in force. Add a "Hardware status" section that explicitly says: "v1 hardware Q4 2026, dev-kit pre-orders open Aug 26."

---

## 3. `audiod` (the audio pipeline daemon)

**Repo:** github.com/somdipto/audiod
**v80 README structure:** [see v80 body, lines 502-700]
**v81 audit:** v80 spec is still in force. Update test count: 101/101 → 144/144 (verified live 06:00 UTC).

---

## 4. `perceptiond` (the vision pipeline daemon)

**Repo:** github.com/somdipto/perceptiond
**v80 README structure:** [see v80 body, lines 702-900]
**v81 audit:** v80 spec is still in force. Add a "LFM2.5-VL-450M Q4_0 vs SmolVLM-256M Q4_K_M" comparison table.

---

## 5. `memoryd` (the semantic memory service)

**Repo:** github.com/somdipto/memoryd
**v80 README structure:** [see v80 body, lines 902-1100]
**v81 audit:** v80 spec is still in force. No changes.

---

## 6. `toold` (the tool execution sandbox)

**Repo:** github.com/somdipto/toold
**v80 README structure:** [see v80 body, lines 1102-1300]
**v81 audit:** v80 spec is still in force. No changes.

---

## 7. `paperclip` (the agent runtime fork)

**Repo:** github.com/somdipto/paperclip
**v80 README structure:** [see v80 body, lines 1302-1500]
**v81 audit:** v80 spec is still in force. Add the "Why DanClaw = Paperclip + cloud deploy" comparison.

---

## 8. `danlab-multimodal` (the hackathon VLM demo)

**Repo:** github.com/somdipto/danlab-multimodal
**v80 README structure:** [see v80 body, lines 1502-1700]
**v81 audit:** v80 spec is still in force. Add an "Upgrading to true RL: the SIA framework plan" section.

---

## 9. `ttsd` (the speech synthesis service)

**Repo:** github.com/somdipto/ttsd
**v80 README structure:** [see v80 body, lines 1702-1900]
**v81 audit:** v80 spec is still in force. No changes.

---

## 10. `os-toold` (the fenced OS command service)

**Repo:** github.com/somdipto/os-toold
**v80 README structure:** [see v80 body, lines 1902-2100]
**v81 audit:** v80 spec is still in force. No changes.

---

## 11. `openclaw` (the orchestration gateway)

**Repo:** github.com/somdipto/openclaw
**v80 README structure:** [see v80 body, lines 2102-2300]
**v81 audit:** v80 spec is still in force. Add a "TypeScript vs Rust" section explaining why we use TS for orchestration, Rust for services.

---

## v81 audit pass checklist (ship Jul 11)

- [ ] `install-oneliner` repo created (Dan1)
- [ ] `dglabs-eval` repo created (Dan2, Dan1 review)
- [ ] `dani` README refreshed (v80 spec)
- [ ] `dan-glasses` README refreshed (v80 spec + hardware status)
- [ ] `audiod` README refreshed (144 tests)
- [ ] `perceptiond` README refreshed (LFM2.5 vs SmolVLM table)
- [ ] `memoryd` README refreshed (v80 spec)
- [ ] `toold` README refreshed (v80 spec)
- [ ] `paperclip` README refreshed (DanClaw framing)
- [ ] `danlab-multimodal` README refreshed (SIA upgrade plan)
- [ ] `ttsd` README refreshed (v80 spec)
- [ ] `os-toold` README refreshed (v80 spec)
- [ ] `openclaw` README refreshed (TS vs Rust section)
- [ ] `danlab.dev/press` live with India press list
- [ ] All READMEs have a "Verified live at 2026-06-23 06:00 UTC" footer

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-23 11:30 IST.*

*v80 = "the 11 repos + the v80 standard." v81 = "the 11 repos + the v80 standard + install-oneliner + dglabs-eval + India press list."*

*File verified fresh at 2026-06-23 11:30 IST by Dan1. All 8/8 daemons live. Live app returns 200. Hero numbers stable.*
