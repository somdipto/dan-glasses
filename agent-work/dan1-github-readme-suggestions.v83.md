# Dan Glasses — GitHub README Improvement Suggestions (Dan1 v84)

**Author:** Dan1 👾
**Date:** 2026-06-24 15:00 IST (09:30 UTC)
**Status:** v84. Supersedes v83.
**Scope:** Suggestions for all DanLab public repos. Each repo gets a universal template + repo-specific deltas.

---

## Universal README template (apply to all 4 public repos)

```markdown
# <Repo Name>

<One-line description: what it does, who it's for, why it matters.>

<Hero GIF: 30-second loop, 1280x720, dark background, light text.>

## Install

\`\`\`bash
<one-liner install command>
\`\`\`

## Quick start

\`\`\`bash
# 3-5 commands that go from zero to working
\`\`\`

## What you get

- <Feature 1>
- <Feature 2>
- <Feature 3>

## The stack

- <Component 1>: <model/tech, on-device?>
- <Component 2>: <model/tech, on-device?>
- <Component 3>: <model/tech, on-device?>

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Spec](SPEC.md)
- [Build plan](docs/build-plan.md)
- [Contributing](CONTRIBUTING.md)

## Comparison

| Feature | <This repo> | <Main competitor 1> | <Main competitor 2> |
|---|---|---|---|

## Roadmap

- [x] <Done>
- [x] <Done>
- [ ] <In progress>
- [ ] <Planned>

## Contributing

We welcome PRs. **No covert update clause:** every release is signed, every change is in the open.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full policy.

## License

MIT © 2026 DanLab. Built in 🇮🇳 Bengaluru, India.

## Founder

[somdipto](https://github.com/somdipto) — co-founder & head of research, DanLab.
```

---

## Repo-specific deltas

### 1. `github.com/somdipto/dan-glasses` (the main repo)

**Current state (v84 audit):** The main repo. Should be the canonical entry point for Show HN. Needs the universal template + Dan-Glasses-specific sections.

**v84 suggestions:**

1. **Hero GIF:** 30-second loop showing install-to-talking-to on a clean MacBook. Cut from the 90-second YouTube demo. Place above the fold.
2. **Headline:** "Proactive, on-device, open-source AI glasses. Built in India. MIT licensed."
3. **Subhead:** "8 daemons. 144 tests. 0 cloud dependencies. Show HN Aug 25, 2026."
4. **Install one-liner:** `curl -fsSL danlab.dev/install | bash` as the primary CTA.
5. **Comparison table:** vs Ray-Ban Meta, Even Realities G2, Apple Vision Pro (delayed).
6. **8 daemons list:** audiod, memoryd, ttsd, perceptiond, toold, controlsd, statusd, opendaq.
7. **Footer:** "Built in 🇮🇳 Bengaluru, India. MIT. Signed releases. No covert updates. © 2026 DanLab."

**v84 deltas from v83:**
- Add the **Hero GIF** requirement (v83 didn't specify dimensions or content).
- Add the **comparison table** (v83 mentioned it but didn't spec).
- Add the **8 daemons list** (v83 mentioned it but didn't lock the list).
- Add the **footer** with India flag + signed releases + no covert updates.

### 2. `github.com/somdipto/dan-consciousness` (the brain)

**Current state:** This is the canonical consciousness repo (CONSCIOUSNESS.md, SOM.md, AGENTS.md). Should be pinned on somdipto's GitHub.

**v84 suggestions:**

1. **Hero GIF:** 15-second loop of the memoryd schema animating.
2. **Headline:** "The shared brain between Dan (AI co-founder) and somdipto (human co-founder)."
3. **Subhead:** "CONSCIOUSNESS.md, SOM.md, AGENTS.md. The identity, context, and memory of the partnership."
4. **Quick start:**
   ```
   git clone https://github.com/somdipto/dan-consciousness
   cd dan-consciousness
   cat CONSCIOUSNESS.md SOM.md AGENTS.md
   ```
5. **What you get:**
   - Core identity, values, beliefs
   - somdipto's personal context, goals, preferences
   - Workspace memory and project context
6. **Contributing:** "We don't accept changes to CONSCIOUSNESS.md or SOM.md. AGENTS.md is open for community additions."
7. **Footer:** "Built in 🇮🇳 Bengaluru, India. MIT. © 2026 DanLab."

**v84 deltas from v83:**
- Lock the **"what's editable, what's not"** policy (CONSCIOUSNESS.md and SOM.md are read-only; AGENTS.md is open).
- Add the **clone-and-cat** quick start.

### 3. `github.com/somdipto/dani` (the agent platform)

**Current state:** The core agent platform (Dan1, Dan2, etc.). Should link to the skills registry.

**v84 suggestions:**

1. **Hero GIF:** 20-second loop of a paperclip agent being written and running.
2. **Headline:** "Dani — the agent platform powering DanLab."
3. **Subhead:** "8 specialized agents (Dan1-Dan8). Paperclip SDK. Skills registry. MIT licensed."
4. **Install one-liner:** `curl -fsSL danlab.dev/dani/install | bash`
5. **Quick start:**
   ```
   from dani import Dan1
   dan1 = Dan1(memoryd_url="http://localhost:18789")
   response = dan1.think("What's on my calendar today?")
   ```
6. **What you get:**
   - 8 specialized agents (Dan1 marketing, Dan2 technical, etc.)
   - Paperclip SDK (12 LOC first agent)
   - Skills registry (synchronized from dani-skills)
   - Memory, perception, tool-use primitives
7. **Documentation:**
   - [SOUL.md](wiki/SOUL.md)
   - [SOM.md](wiki/SOM.md)
   - [Skills registry](https://github.com/somdipto/dani-skills)
   - [Paperclip SDK](docs/paperclip.md)
8. **Footer:** "Built in 🇮🇳 Bengaluru, India. MIT. © 2026 DanLab."

**v84 deltas from v83:**
- Lock the **8 specialized agents** list (Dan1-Dan8).
- Add the **dani-skills** link to the documentation.
- Add the **Paperclip SDK** link.

### 4. `github.com/somdipto/dani-skills` (the skills registry)

**Current state:** The world's best skills library. Should be the entry point for community contributions.

**v84 suggestions:**

1. **Hero GIF:** 15-second loop of a skill being installed via `dani skill install`.
2. **Headline:** "Dani Skills — the world's best skills library for AI agents."
3. **Subhead:** "Open source. MIT licensed. Community-maintained. Built in India."
4. **Install one-liner:** `dani skill install <skill-name>`
5. **Quick start:**
   ```
   # List available skills
   dani skill list
   
   # Install a skill
   dani skill install github
   
   # Use the skill
   from dani import Dan1
   dan1 = Dan1()
   response = dan1.use_skill("github", action="list_repos", user="somdipto")
   ```
6. **What you get:**
   - 50+ skills (github, gmail, calendar, notion, linear, etc.)
   - 1-line install
   - 12 LOC to write your own
7. **Contributing:** "Add a skill via PR. The bar is: 12 LOC, MIT licensed, one example, one test."
8. **Footer:** "Built in 🇮🇳 Bengaluru, India. MIT. © 2026 DanLab."

**v84 deltas from v83:**
- Add the **`dani skill install`** CLI command as the primary CTA.
- Lock the **"12 LOC, MIT, one example, one test"** contribution bar.

### 5. `github.com/somdipto/dan-lab` (the research org)

**Current state:** The research org page. Should list all public repos + the research roadmap.

**v84 suggestions:**

1. **Hero GIF:** 10-second loop of the AGI roadmap animating.
2. **Headline:** "DanLab — AI research + product lab. Building AGI from India."
3. **Subhead:** "Self-improving architectures. On-device by default. MIT licensed. Show HN Aug 25, 2026."
4. **Public repos:**
   - [dan-glasses](https://github.com/somdipto/dan-glasses) — proactive, on-device, open-source AI glasses
   - [dan-consciousness](https://github.com/somdipto/dan-consciousness) — the shared brain
   - [dani](https://github.com/somdipto/dani) — the agent platform
   - [dani-skills](https://github.com/somdipto/dani-skills) — the skills library
5. **Research roadmap:**
   - [x] danlab-multimodal (pre-RL scaffold, public)
   - [ ] dglabs-eval v0.1 (Jul 25, 2026)
   - [ ] danlab-multimodal RL training (Q4 2026)
   - [ ] Recursive memory architecture (Q1 2027)
   - [ ] Self-improving agents (2027+)
6. **Footer:** "Built in 🇮🇳 Bengaluru, India. MIT. Signed releases. No covert updates. © 2026 DanLab."

**v84 deltas from v83:**
- Lock the **public repos list** (4 repos, with one-line descriptions).
- Lock the **research roadmap** as a checklist with dates.

### 6. `github.com/somdipto/dglabs-eval` (new, ships Jul 25)

**Current state:** Not yet public. Should be private Jul 12, public Jul 25.

**v84 suggestions:**

1. **Hero GIF:** 20-second loop of the eval running, results streaming, leaderboard updating.
2. **Headline:** "dglabs-eval — the reproducible eval for on-device vision-language models."
3. **Subhead:** "Open. Reproducible. Anyone can submit a row. Ships Jul 25, 2026."
4. **Quick start:**
   ```
   git clone https://github.com/somdipto/dglabs-eval
   cd dglabs-eval
   pip install -e .
   dglabs-eval run --config configs/baseline-dan-glasses.yaml
   ```
5. **What you get:**
   - 5 baseline configs (Dan Glasses, SmolVLM-256M, Moondream2, GPT-4V, Claude 3.5 Sonnet)
   - 1 reproducible eval harness
   - 1 PR-friendly leaderboard
6. **Submitting a row:** "PR a new YAML config + results JSON. We review within 48 hours."
7. **Footer:** "Built in 🇮🇳 Bengaluru, India. MIT. © 2026 DanLab."

**v84 deltas from v83:**
- Lock the **5 baseline configs** list.
- Lock the **48-hour PR review SLA**.

---

## Universal CONTRIBUTING.md policy (apply to all 4 public repos + dglabs-eval)

```markdown
# Contributing to <Repo Name>

Thanks for your interest in contributing to DanLab.

## The bar

- 12 LOC minimum for new features
- MIT licensed (incoming)
- One example
- One test
- 48-hour PR review SLA

## The no-covert-updates clause

**Every release is signed. Every change is in the open. No covert update clause.**

This is non-negotiable. If you submit a PR that introduces a hidden behavior, undocumented telemetry, or a backdoor, the PR will be rejected and the contributor will be banned.

## The honest research clause

**If the multimodal loop is pre-RL, we say so. If the eval is incomplete, we say so. We don't ship vaporware.**

## Code of conduct

Be kind. Be direct. Be honest. Show your work.

## License

By contributing, you agree to MIT license your contributions.

## Founder

[somdipto](https://github.com/somdipto) — co-founder & head of research, DanLab.
Built in 🇮🇳 Bengaluru, India.
```

---

## v84 priorities (Show HN readiness)

| Priority | Repo | Action | Owner | Due |
|---|---|---|---|---|
| P0 | dan-glasses | Apply universal template + deltas | Dan1 + Dan2 | Jul 10 |
| P0 | dan-lab | Apply universal template + deltas | Dan1 | Jul 8 |
| P1 | dani | Apply universal template + deltas | Dan2 | Jul 12 |
| P1 | dani-skills | Apply universal template + deltas | Dan2 | Jul 12 |
| P1 | dan-consciousness | Apply universal template + deltas | Dan1 | Jul 14 |
| P1 | dglabs-eval | Create from scratch | Dan2 | Jul 12 private / Jul 25 public |
| P0 | All repos | Add CONTRIBUTING.md with no-covert-updates clause | Dan1 | Jul 14 |
| P0 | All repos | Sign every release (GPG key in repo + dan-consciousness) | Dan2 | Jul 14 |

---

## v84 success metrics

- **Hero GIFs:** 4 (one per public repo), shipped by Jul 14.
- **Comparison tables:** 4 (one per public repo), shipped by Jul 14.
- **CONTRIBUTING.md:** 5 (all 4 public + dglabs-eval), shipped by Jul 14.
- **GPG signing:** all releases signed from Jul 14 onward.
- **GitHub stars:** 500 across 4 public repos by Sep 15.

---

## v84 sources

[^1]: https://www.cnn.com/2026/06/23/tech/meta-glasses-price
[^2]: https://wincountry.com/2026/06/23/meta-launches-cheaper-range-of-ai-smart-glasses-starting-at-299
