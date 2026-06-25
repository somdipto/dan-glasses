# GitHub README Improvements — All Danlab Repos (Dan1 v87)

**Author:** Dan1 👾
**Date:** 2026-06-25
**Status:** v87. Supersedes v86.
**Companion doc:** `dan1-marketing-research.md`.
**Output format:** Full drop-in rewrites for core repos plus a meta checklist for the rest.

---

## v87 read of the repos (the receipts)

The repos already have serious engineering depth. The gap is still conversion:

1. **The first 10 seconds do not tell the user what the repo is.**
2. **There is no obvious install / try-it-now path.**
3. **The README does not tell the story of the system.**

v87 fixes that with a human-first front door and an agent-first back door.

---

## 1) `github.com/somdipto/dan-glasses`

### What the README must do
- Explain the product in one sentence
- Show the stack in one glance
- Provide a 4-minute install path
- Link to the eval harness and the architecture
- Make the India + open-source story explicit

### Suggested structure
1. Hero line
2. What this is
3. Why it exists
4. Quick start
5. Architecture map
6. Daemons
7. Eval
8. Roadmap
9. Contributing

### Hero copy
> **Dan Glasses is open-source AI for your face — on-device, proactive, and built in India.**

### Must-have badges
- MIT
- tests
- daemons
- cloud = 0
- show hn date

### Install section
- One-line install
- Expected runtime
- What it does
- Troubleshooting link

### Architecture section
- show 8 daemons
- show the relationship between `audiod`, `perceptiond`, `memoryd`, and Dani
- include a tiny mermaid diagram

### Contributing section
- no code without tests
- no PR without screenshots or logs when UI changes
- sign commits if possible
- keep issues small and actionable

---

## 2) `github.com/somdipto/dani`

### What the README must do
- Explain that Dani is the agent framework, not the product
- Show where Dani sits relative to HRM-Text and Dan Glasses
- Make the skill system obvious
- Link to examples

### Hero copy
> **Dani is the open agent framework behind Dan Glasses.**

### Must-have sections
- What Dani does
- How Dani talks to daemons
- Skill creation
- Example workflows
- Safety / tool permissions
- Repo map

### Add a 1-minute architecture sketch
- input → perception → memory → reasoning → action
- clarify the difference between framework and app

---

## 3) `github.com/somdipto/danlab-multimodal`

### What the README must do
- Explain the RL loop in plain language
- State what problem the project solves
- Show the demo artifact first
- Show the evaluation artifact second
- Link to architecture and training notes

### Hero copy
> **A multimodal research loop that turns perception into better behavior.**

### Must-have sections
- What it is
- Why it exists
- The loop
- What is measured
- Demo links
- Architecture links
- Dataset / eval notes
- Known failure modes

### Key recommendation
Do not bury the RL loop. That is the point of the repo.

---

## 4) `github.com/somdipto/paperclip`

### What the README must do
- Clarify whether Paperclip is a product, agent, or research harness
- Explain the target audience
- Make the relation to DanLab explicit

### Hero copy
> **Paperclip is the lightweight agent surface for DanLab workflows.**

### Must-have sections
- What it is
- Who it is for
- What it is not
- How it connects to Dani / Dan Glasses
- Current status
- Roadmap

### Recommendation
If Paperclip is still early, be explicit. Early honesty builds trust.

---

## 5) `github.com/somdipto/blurr`

### What the README must do
- Explain what problem Blurr solves in one sentence
- State the relationship to multimodal work
- Show a quick demo or example usage
- Avoid sounding like a generic AI wrapper

### Hero copy
> **Blurr is a focused utility layer for working with noisy multimodal inputs.**

### Must-have sections
- Problem
- Inputs
- Outputs
- Example
- Where it fits in the stack
- Status

---

## 6) Universal README template for all DanLab repos

### Front matter to add to every README
- one-sentence description
- one-line status
- repo role in the stack
- primary owner
- last updated date

### Standard section order
1. What is this?
2. Why it exists
3. Quick start
4. Architecture / design
5. Examples
6. Tests / evals
7. Roadmap
8. Contributing
9. Related repos

### Anti-patterns to remove
- long mission statements before the one-liner
- AGENTS.md as the only human-facing entry point
- hidden install steps
- vague "coming soon" claims without evidence
- unlabeled screenshots

---

## 7) High-priority README upgrades across the org

1. **Add a one-line purpose statement to every repo.**
2. **Add a visible quick-start path.**
3. **Add a stack map / repo map.**
4. **Add the current status.**
5. **Add proof links where possible.**
6. **Keep the India story explicit where relevant.**
7. **Keep the readme human-first; AGENTS stays agent-first.**

---

## 8) Concrete conversion improvements

These changes matter most:

- **Bad:** a README that starts with architecture jargon.
- **Good:** a README that starts with what the repo does and who it's for.

- **Bad:** "see AGENTS.md for details"
- **Good:** a short human summary, then a link to AGENTS.md for agents

- **Bad:** no install instructions
- **Good:** one command, one expected outcome

- **Bad:** no repo map
- **Good:** list of related repos and why they exist

---

## 9) Suggested universal snippet

```markdown
## Quick start

```bash
curl -sL danlab.dev/install | bash
```

## Related repos
- `dani` — agent framework
- `dan-glasses` — hardware product
- `danlab-multimodal` — research loop
- `paperclip` — lightweight agent surface
```

---

*v87. Locked.* 👾