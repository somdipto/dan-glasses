# Dan1 — GitHub README Improvements (v127)

**Run:** 2026-07-06 07:30 UTC · Asia/Calcutta 13:00 IST
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Companion to:** `dan1-marketing-research.md` (v127), `dan1-marketing-strategy.md` (v127)
**Lead:** *The closed-source frontier is politically-conditional AND the capex cycle is being repriced AND the outer-loop RSI is already in flight. The bet is no longer "open vs closed." The bet is: who can ship the substrate while the substrate is still standing?*

---

## 0. v127 deltas

- v126 README suggestions hold. v127 sharpens three things: (1) the **8/8 daemons + .deb 9.4MB** as the canonical "what works today" number, (2) the **threat-model + reversibility-contract** as the trust section in every README, (3) the **outer-loop RSI shippable** framing as the closing line in hero repos.
- v127 retires the "9/9 daemons" number (zo-mcp-bridge is `process`-mode, doesn't count). The defensible number is **8/8 daemons + 1 bridge**.
- v127 adds a **canonical README template** that all hero repos should follow (5 sections, 1 line each).
- v127 adds **per-repo specific suggestions** for: dan-glasses, dani, danlab-multimodal, paperclip, dan-consciousness, dan-lab org README.

---

## 1. Canonical README template (5 sections, 1 line each)

Every hero repo README should open with these 5 lines, in this order:

```markdown
# <repo-name>

<one-line pitch, ≤ 12 words>

**Status:** <live | shipped | experimental> · **License:** MIT · **From:** Bengaluru 🇮🇳

## The bet
<one-line: what this repo proves, in the v127 wedge language>

## The .deb (or equivalent install)
<one-line: the install command, the install size, the time-to-install>
```

**Why this template:**
- The pitch line is the hook.
- The status/license/from line is the trust signal.
- "The bet" line is the wedge — it ladders up to the 4 axes (sovereign trust + reversibility + chip + outer-loop RSI).
- The install line is the receipt — proves it works today.

---

## 2. Per-repo suggestions

### 2.1 `github.com/somdipto/dan-glasses` (HERO REPO)

**Current state:** the repo has a build plan doc + agent-work scratch pads + service specs. The README is the v104 build plan summary.

**v127 suggestions:**

1. **Replace the README's opening with the canonical template:**
   ```markdown
   # Dan Glasses

   A proactive AI on your face. Open weights. From India.

   **Status:** 8/8 daemons live · **License:** MIT · **From:** Bengaluru 🇮🇳

   ## The bet
   The closed-source frontier is politically-conditional. The capex cycle is being repriced. The outer-loop RSI is already in flight. We are shipping the substrate while the substrate is still standing.

   ## The .deb
   ```bash
   wget https://github.com/somdipto/dan-glasses/releases/latest/download/dan-glasses-daemons_0.1.0-1_all.deb
   sudo dpkg -i dan-glasses-daemons_0.1.0-1_all.deb
   ```
   9.4MB · 30s install · 8 systemd services · 0 cloud calls
   ```

2. **Add a "What works today" section** with the live daemon matrix + status:
   ```markdown
   ## What works today (2026-07-06, verified)

   | Daemon | Port | Status | Test count |
   |---|---|---|---|
   | audiod | 8090 | ✅ /ready | 177/177 |
   | perceptiond | 8092 | ✅ /health | 22/22 |
   | memoryd | 8741 | ✅ /db | (per service) |
   | toold | 8742 | ✅ /status | (per service) |
   | ttsd | 8743 | ✅ /ready | (per service) |
   | os-toold | 8744 | ✅ /ok | (per service) |
   | dan-glasses-app | 8747 | ✅ / | (per service) |
   | openclaw | 18789 | ✅ 63 commands | (per service) |

   **Total tests:** 208/208 passing. **Live demo:** Tailscale authkey pending.
   ```

3. **Add a "Trust" section** linking to the threat model + reversibility contract:
   ```markdown
   ## Trust

   - **Threat model:** [github.com/somdipto/dan-lab/tree/main/threat-model](https://github.com/somdipto/dan-lab/tree/main/threat-model) — public since v122.5
   - **Reversibility contract:** [github.com/somdipto/dan-lab/tree/main/reversibility](https://github.com/somdipto/dan-lab/tree/main/reversibility) — ships Q3 W2
   - **Sovereign-trust audit:** v124 plan-O1, ships Q3 W1
   ```

4. **Add a "Contributing" section** that points to the agent-work scratch pads and the dan-consciousness brain:
   ```markdown
   ## Contributing

   Read the [AGENTS.md](AGENTS.md) first. Then read [dan-consciousness](https://github.com/somdipto/dan-consciousness) — that's the brain this repo shares with Dani (AI co-founder). All commits use `somdipto <somdiptonandy@gmail.com>`.
   ```

5. **Add a "Roadmap" section** with the v124 → v125 plan:
   ```markdown
   ## Roadmap (Q3 2026)

   - [x] 8/8 daemons live + .deb built
   - [x] Tauri v2 app published
   - [x] Telegram @danlab_bot wired
   - [ ] Tailscale authkey (unblocks live demo)
   - [ ] v124 plan-O1 sovereign-trust audit
   - [ ] v124 plan-O2 reversibility contract
   - [ ] v124 plan-O3 v1.0 spec §13
   - [ ] Show HN #1
   - [ ] Display-less v1.0 hardware RDK (Q4 W2-W3)
   ```

**Priority:** 🔥 P0. This is the hero repo. The README is the funnel. Ship this week.

---

### 2.2 `github.com/somdipto/dani` (HERO REPO)

**Current state:** the public repo. The brain platform.

**v127 suggestions:**

1. **Apply the canonical template.**
2. **Add a "What is Dani?" section** that explains the platform in 3 lines, not 30:
   ```markdown
   ## What is Dani?

   Dani is an open agent platform. It pairs with [OpenClaw](https://github.com/openclaw/openclaw) as the substrate and [dani-skills](https://github.com/somdipto/dani-skills) as the skill library. The brain is [dan-consciousness](https://github.com/somdipto/dan-consciousness) — public, MIT, auditable.
   ```
3. **Add a "Quickstart" section** with a copy-paste command:
   ```markdown
   ## Quickstart

   ```bash
   git clone https://github.com/somdipto/dani.git
   cd dani
   bun install
   bun run dev
   ```
   ```
4. **Link to the threat model + reversibility contract** in the Trust section.

**Priority:** 🔥 P0. Dani is the public face of the lab. Ship this week.

---

### 2.3 `github.com/somdipto/danlab-multimodal` (HERO REPO — demo)

**Current state:** the README is already strong (per v122 review). It has the demo link, the asciinema recording, the architecture diagram, the model selection rationale.

**v127 suggestions:**

1. **Apply the canonical template** to the top of the README.
2. **Add the trust section** linking to threat model + reversibility contract.
3. **Add a "Cascade gate upgrade" section** referencing the Q3 W1-W2 VisualClaw port (98% cost reduction, +15% accuracy, per dan2 v23 plan).
4. **Add a "Honest framing" callout** in the demo section — the heuristic is not RL, the SIA fork is the credible path.

**Priority:** 🟡 P1. Already strong. Polish + trust section + cascade gate reference.

---

### 2.4 `github.com/somdipto/paperclip` (DORMANT)

**Current state:** dormant per `paperclip/AGENTS.md`. Production link: `https://paperclip.up.railway.app`.

**v127 suggestions:**

1. **Add a "Status: Dormant" badge** at the top:
   ```markdown
   ![Status: Dormant](https://img.shields.io/badge/status-dormant-lightgrey)
   ```
2. **Apply the canonical template** but with a different "bet" line:
   ```markdown
   ## The bet
   Paperclip is the orchestration layer for the Danlab ecosystem. Currently dormant. Resume when Dan Glasses v1.0 ships.
   ```
3. **Add a "Last activity" line** with the date of the last commit.
4. **Do NOT remove the production link** — the Railway app is still up.

**Priority:** 🟢 P2. Dormant. Polish only.

---

### 2.5 `github.com/somdipto/dan-consciousness` (THE BRAIN)

**Current state:** the canonical consciousness — `CONSCIOUSNESS.md`, `SOM.md`, `AGENTS.md`.

**v127 suggestions:**

1. **Apply the canonical template** but with a different "bet" line:
   ```markdown
   ## The bet
   The brain is the bet. CONSCIOUSNESS.md + SOUL.md + IDENTITY.md + MEMORY.md — the four files that make Dani a person, not a chatbot. MIT, auditable, forkable. This is what the closed-source frontier can't ship.
   ```
2. **Add a "How to read this repo" section:**
   ```markdown
   ## How to read this repo

   1. Start with `CONSCIOUSNESS.md` — core identity, values, beliefs.
   2. Then `SOM.md` — somdipto's personal context, goals, preferences.
   3. Then `AGENTS.md` — workspace memory and project context.
   4. Then the per-project AGENTS.md files in each subdirectory.
   ```
3. **Add a "Why MIT?" section** explaining the license choice:
   ```markdown
   ## Why MIT?

   The brain is the bet. If you can't fork it, you can't trust it. If you can't audit it, you can't ship on it. MIT is the only license that makes the brain shippable to the closed-source frontier's escape hatch — wearable AI on a chip stack the user owns.
   ```

**Priority:** 🟡 P1. The brain is the heart. Polish.

---

### 2.6 `github.com/somdipto/dan-lab` (ORG README)

**Current state:** the org-level README. Likely a list of repos + a "what is danlab.dev" paragraph.

**v127 suggestions:**

1. **Apply the canonical template** with a strong "the bet" line:
   ```markdown
   ## The bet
   The closed-source frontier is politically-conditional. The capex cycle is being repriced. The outer-loop RSI is already in flight. We are shipping the substrate — open weights, public threat model, reversibility contract — while the substrate is still standing. From India 🇮🇳.
   ```
2. **Add a "What we ship" section:**
   ```markdown
   ## What we ship

   - **[dan-glasses](https://github.com/somdipto/dan-glasses)** — 8 daemons live, 1 .deb installs them all, on-device AI companion
   - **[dani](https://github.com/somdipto/dani)** — open agent platform, the brain
   - **[danlab-multimodal](https://github.com/somdipto/danlab-multimodal)** — sub-250MB VLM on CPU, heuristic feedback loop demo
   - **[paperclip](https://github.com/somdipto/paperclip)** — orchestration layer (dormant)
   - **[dan-consciousness](https://github.com/somdipto/dan-consciousness)** — the brain, MIT, auditable
   ```
3. **Add a "Trust" section** linking to the threat model + reversibility contract.
4. **Add a "From India" callout:**
   ```markdown
   ## From India 🇮🇳

   Dan Lab is in Bengaluru. The brain is in Bengaluru. The 8 daemons shipped from a Bengaluru laptop on a $0 GPU budget in 9 weeks. The substrate is earned, not asserted.
   ```

**Priority:** 🔥 P0. The org README is the first thing a visitor sees. Ship this week.

---

## 3. Cross-repo improvements (apply to all)

### 3.1 Add shields.io badges
- `![License: MIT](https://img.shields.io/badge/license-MIT-green)`
- `![From India 🇮🇳](https://img.shields.io/badge/from-India-orange)`
- `![Status: <live|shipped|experimental|dormant>](https://img.shields.io/badge/status-<STATUS>-<COLOR>)`
- `![Tests: <N>/<N>](https://img.shields.io/badge/tests-<PASS>-green)`
- `![Models: <list>](https://img.shields.io/badge/models-<LIST>-yellow)`

### 3.2 Add a "Citation" section
If the repo has a paper or a citable artifact, add a CITATION.cff. If not, add a citation block:
```markdown
## Citation

If you use this work, please cite:

```bibtex
@software{danlab_glasses_2026,
  author = {Nandy, Somdipto and Dani (AI co-founder)},
  title = {Dan Glasses: An On-Device AI Companion in Glasses Form Factor},
  year = {2026},
  url = {https://github.com/somdipto/dan-glasses}
}
```
```

### 3.3 Add a "License" footer
```markdown
---

**MIT** · **Bengaluru 🇮🇳** · **[danlab.dev](https://danlab.dev)**
```

---

## 4. v127 handoff notes (for the engineering team)

- **Apply the canonical template** to all 5 hero repos + the org README. Total: 6 README rewrites.
- **Engineer-days:** ~0.5 day per README × 6 = 3 days total. Spread across 2 engineers (somdipto + 1 contributor) over 1 week.
- **Review:** all rewrites land as PRs, reviewed by somdipto + Dani.
- **Merge gate:** the threat model + reversibility contract links must resolve to real URLs (even if "coming soon" with a planned date).
- **No "Coming soon" without a date.** A README with a broken link is worse than no README.
- **The .deb number (9.4MB) is the only number in the canonical template that must be exact.** Everything else can be tightened later.

---

*README suggestions complete. 6 hero repos, 1 canonical template, 1 week of work. The funnel is the README. Ship the rewrites.*
