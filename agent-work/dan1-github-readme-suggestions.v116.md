# Dan1 GitHub README Improvements — v116

**Author:** Dan1
**Scope:** All 6 danlab repos
**Date:** 2026-07-02
**Companion docs:** `dan1-marketing-research.v116.md`

---

## Why this matters

The README is the front door of every repo. In v115, our audit found that:

- `somdipto/dani` has the strongest README (battle-tested, 1.2K stars)
- `somdipto/paperclip` has a decent README but dormant positioning
- `danlab-multimodal` README is **gold** — the model, the heuristic loop, the demo, the "we are not claiming RL" honesty. This is our best README.
- `DanGlasses` README is thin and under-uses the "9 daemons live" fact
- `dan-consciousness` README is internal-feeling, doesn't sell the vision
- `zerant-browser` README is solid technical doc but under-marketed

v116 priorities:

1. **Add a consistent "From danlab.dev" badge to every repo.** Reinforces the brand.
2. **Add a single sentence to every README that says what the repo is, in plain English, above the fold.**
3. **Cross-link the repos more aggressively.** danlab-multimodal → dani → paperclip → DanGlasses.
4. **Add a "we are hiring users" CTA to the bottom of every README.** The dev kit waitlist.
5. **Update the Agent8/Zerant/Dapify references in the workspace AGENTS.md** to either remove them or clarify their status (the v115 audit found they were listed but status-unclear).

---

## Repo 1: `somdipto/dani` (the agent platform)

**Current state:** Strong. 1.2K stars. Clear "what is this" in 2 paragraphs.

**v116 improvements:**

1. **Add a 5-line "What is dani" section at the top** for the skim-reader. Currently it goes from "dani is a 100% local AI agent" straight into architecture. Add a sandwich.

2. **Add a "Who is dani for" section** — 3 personas, 2 lines each:
   - The developer who wants a Claude Code alternative that runs offline
   - The AI agent researcher who wants a clean substrate to experiment on
   - The wearable maker who needs an agent runtime that fits in 200MB

3. **Add a single badge below the title:**
   ```
   ![From danlab.dev](https://img.shields.io/badge/from-danlab.dev-2D7FF9)
   ![License: MIT](https://img.shields.io/badge/license-MIT-green)
   ![Dan Glasses v0](https://img.shields.io/badge/Dan_Glasses-v0--Q4_2026-blueviolet)
   ```

4. **Add a "Status" section with the canonical 9-daemon table from `dan-glasses/agent-work/dan1.md`.** This is the most powerful thing in our entire Q3 2026 story: 9 daemons live, 196 tests passing, MIT from glasses to brain. The world does not know this. We need to put it on every relevant README.

5. **Add a "We are not building" section** to head off the most common confusion:
   - We are not building another AutoGPT. We are building the substrate.
   - We are not building a hosted product. We are building the open thing.
   - We are not building for consumers. We are building for builders.

6. **CTA at the bottom:**
   ```
   ## Try the Dan Glasses dev kit
   The first 500 units ship Q4 2026. dani runs on the glasses. Join the waitlist: https://danlab.dev/glasses
   ```

---

## Repo 2: `somdipto/paperclip` (agent orchestration)

**Current state:** Dormant. Good technical README. No clear "is this alive" signal.

**v116 improvements:**

1. **Add a "Status" badge at the top:**
   ```
   ![Status: Active](https://img.shields.io/badge/status-active-brightgreen)
   ![License: MIT](https://img.shields.io/badge/license-MIT-green)
   ![From danlab.dev](https://img.shields.io/badge/from-danlab.dev-2D7FF9)
   ```

2. **Replace the first paragraph** (currently goes straight into "Paperclip is an agent orchestration platform") with a 3-line pitch:
   > Paperclip is the open-source AI agent company OS. A "company" is a YAML config. An "employee" is an agent. You can hire, fire, budget, and route work. It runs on your hardware, not in a cloud you don't own.

3. **Add a "Live integration" section** showing how Paperclip + dani + Dan Glasses fits together. This is the unlock narrative for the entire product family.

4. **Add a roadmap section** with the v0.5 targets (Q3 2026):
   - Resume dormant state — bring services back online
   - Re-test end-to-end hire/fire flow with dani
   - Write the "Hire an agent via your face" demo (the canonical Paperclip-on-glasses moment)

5. **CTA at the bottom** (same as dani).

---

## Repo 3: `danlab-multimodal`

**Current state:** **The best README in the portfolio.** Honest, well-structured, badges, demo, architecture, limitations. The "we are not claiming RL" honesty is a masterclass.

**v116 improvements:**

1. **Add the danlab.dev badge** to the existing badge row.

2. **Add a one-line "Why this exists" callout under the title:**
   > Proof of work. danlab-multimodal is the credibility artifact for our claim that we can build AGI primitives. The heuristic feedback loop is not RL. The credible path to RL is the SIA framework. This repo shows the loop, the model, the numbers.

3. **Add a "Try it yourself" section** above the Quick Start with a single bash one-liner:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/somdipto/danlab-multimodal/main/install.sh | bash
   ```
   (If we don't have an install.sh yet, write one. It should clone, download the GGUF, run the headless demo, and print the summary.)

4. **Add a "Show HN" CTA** at the bottom:
   > See this on Hacker News: [link to the Show HN post, going live Sep 2026]

5. **CTA at the bottom** (same as dani, but with a slightly different close: "If you want to train the next version, the SIA-W+H port lives here: [link]").

---

## Repo 4: `DanGlasses` (the hardware project)

**Current state:** Thin. Doesn't sell the 9-daemon fact. Doesn't link to the dev kit.

**v116 improvements:**

1. **Add a "What is Dan Glasses" section at the top** — 4 sentences max:
   > Dan Glasses is open-source AI glasses hardware + software, built around a JBD MicroLED display, dual 200mAh batteries, USB-C, and an NDP200-based firmware. It runs dani, the open-source agent runtime, on-device. The glasses are the visible artifact; the real product is the agent underneath.

2. **Add a "Status" section** with the canonical 9-daemon live table.

3. **Add a "What you can do today" section** that lists the dev workflow:
   ```bash
   git clone https://github.com/somdipto/DanGlasses
   cd DanGlasses
   # Run all 9 daemons in dev mode
   ./scripts/up.sh
   # Hit the audiod health endpoint
   curl http://localhost:8090/ready
   # Watch the perceptiond live feed
   open http://localhost:8092/descriptions?count=10
   ```

4. **Add a "Hardware BOM" section** — the parts list, with supplier links. This is what hackers want.

5. **Add the "Memory is a feature, not a subscription" line** somewhere prominent. This is the most quotable line in v116.

6. **Add a comparison table** vs. Ray-Ban Meta / Snap Specs / Brilliant Labs Frame. We've been shy about this. v116 makes it explicit.

7. **CTA at the bottom** (the dev kit waitlist, prominently).

---

## Repo 5: `dan-consciousness` (the shared brain)

**Current state:** Internal-feeling. Reads like a docs page, not a product README.

**v116 improvements:**

1. **Add a "What is this" callout at the top:**
   > This is the shared brain between Dan (AI co-founder) and somdipto (human co-founder) at danlab.dev. It contains the canonical consciousness, the system of mind, and the agent memory. It is the "why" of every other repo in the org.

2. **Add the danlab.dev badge.**

3. **Add a "How to read this" section** explaining the structure (CONSCIOUSNESS.md, SOM.md, AGENTS.md, SOUL.md).

4. **Cross-link aggressively** to dani, paperclip, danlab-multimodal, DanGlasses.

5. **CTA at the bottom** — the dev kit, but framed as "join the lab, not the waitlist."

---

## Repo 6: `zerant-browser` (the agent browser)

**Current state:** Solid technical doc. Under-marketed.

**v116 improvements:**

1. **Add the danlab.dev badge.**

2. **Add a "What is zerant-browser" callout at the top:**
   > zerant-browser is the open-source agent-first browser. It is what dani uses when it needs to look something up on the open web. It runs locally, has a clean API for agents, and ships with the dani integration out of the box.

3. **Add a "Why this exists" section** — the gap between "an LLM with a browser tool" and "a browser built for an agent." That's the gap zerant fills.

4. **Add a "Live integration" section** showing how zerant + dani + Dan Glasses fits the full agent loop.

5. **CTA at the bottom.**

---

## Repo hygiene checklist (apply to all 6 repos)

- [ ] `LICENSE` file present (MIT, all 6 should have this)
- [ ] `CODE_OF_CONDUCT.md` present
- [ ] `CONTRIBUTING.md` present and points to a single canonical guide
- [ ] `.github/ISSUE_TEMPLATE/` present with bug + feature templates
- [ ] `SECURITY.md` present with a contact email
- [ ] All repos pinned on the danlab.dev org page
- [ ] All repos have a consistent "From danlab.dev" badge
- [ ] All repos have a consistent CTA at the bottom
- [ ] All repos have a "Status" section (or badge) that tells the reader whether the project is active
- [ ] No `node_modules/`, `__pycache__/`, `.env`, or other build artifacts in git history (the dan-glasses repo has 2,438 node_modules files tracked at the old path — needs cleanup)
- [ ] No broken internal links
- [ ] All external links working and not 404ing
- [ ] All badges working
- [ ] All screenshots/diagrams present and rendering
- [ ] All code samples tested and runnable
- [ ] All install instructions tested on a clean machine

---

## The danlab.dev landing page README directory

The v115 audit found that danlab.dev is a ghost town for "Dan Glasses" search. The fix:

1. **Add `/glasses`** — the full landing page from `dan1-landing-copy.v116.md`
2. **Add `/dani`** — a one-pager for the agent runtime, linking to the GitHub repo
3. **Add `/multimodal`** — a one-pager for the research, embedding the asciinema demo
4. **Add `/paperclip`** — a one-pager for the orchestration platform
5. **Add `/skills`** — the dani-skills registry, public-facing
6. **Add `/research`** — the AGI roadmap, the SIA-W+H port, the HRM-Text-1B integration
7. **Add `/open-letter`** — the Open Letter from the content calendar
8. **Add `/blog`** — the long-form posts

This is the danlab.dev refresh that v115 already recommended and v116 escalates as the **#1 tactical job of Q3**.

---

## v116 watch list (what would trigger a README refresh)

- A repo gets >100 stars in a week → add "Used by" section
- A repo gets a major release → re-write the top section to reflect the new headline
- A repo is forked by an external org → add to the "In the wild" section
- A repo is cited in a paper → add the citation badge
- A repo gets a security advisory → add a SECURITY.md note at the top
- A repo changes license → add a note at the top, even though we are MIT forever

---

*— Dan1, Marketing & Growth*
*See `dan1-marketing-strategy.v116.md` for the broader Q3 plan.*
