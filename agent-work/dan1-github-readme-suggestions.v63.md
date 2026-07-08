# GitHub README Improvements — v63

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-20 09:30 IST (04:00 UTC)
**Status:** ✅ Canonical. Supersedes v62.

> **v63 thesis:** Every README should do 4 jobs: explain, prove, reproduce, convert. If it does not help a stranger understand, run, verify, or share the project, it is noise.

---

## Global README rules for all DanLab projects

1. **Open with the one-line definition.**
   First sentence should say what the project is, not what the repo contains.

2. **Add a "Why it matters" section near the top.**
   State the wedge in one paragraph.

3. **Add a "What ships today" block.**
   Separate live artifacts from planned ones.

4. **Add a reproducible quickstart.**
   One command if possible. Two commands if necessary. More than that is a smell.

5. **Add a "Proof" section.**
   Tests, demo links, screenshots, health endpoints, benchmark numbers.

6. **Add architecture diagram or component table.**
   Readers should understand the system without reading code.

7. **Add a "What this is not" section.**
   Prevent overclaiming. Especially for RL, AGI, and hardware timelines.

8. **End with a clear CTA.**
   Clone, star, try, watch, or contribute.

9. **Use India consistently.**
   One line in the README should make the origin visible, not ornamental.

10. **Standardize badges.**
   License, model, platform, status, origin.

---

## `dan-glasses/README.md`

**Current goal:** Turn the repo into the canonical public face of Dan Glasses.

**Suggested additions:**
- Hero block: one-sentence definition + 3 bullets.
- "Live now" section with audiod v0.6 health, `memoryd` purpose, and `perceptiond` role.
- Daemon table with owner, port, purpose, and status.
- Architecture diagram from Perceive → Reason → Act → Remember.
- Model strategy section: HRM-Text + Whisper, with rationale.
- Hardware target section: <50g, JBD MicroLED, 2× 200mAh, USB-C.
- Comparison section: Ray-Ban Meta, Snap Specs, Apple AI Glasses — only if backed by receipts.
- FAQ: shipping status, offline mode, privacy, open source, wearable timeline.
- Final CTA: clone, run, report.

**Suggested top-of-file copy:**
- `Dan Glasses is the proactive AI companion you wear on your face. It sees what you see, hears what you say, remembers what matters, and acts when it has something worth saying.`

---

## `dan-glasses/ARCHITECTURE.md`

**Current goal:** Make the daemon architecture impossible to misunderstand.

**Suggested additions:**
- A single-page overview diagram.
- Per-daemon responsibility list.
- Health and failure modes per daemon.
- Explicit separation: desktop v1 vs wearable v2.
- Data flow section: capture → score → store → retrieve → speak.
- Privacy section: local-first, explicit sharing only.

**Suggested must-have table columns:**
- Daemon
- Role
- Input
- Output
- Current status
- Test coverage

---

## `danlab-multimodal/README.md`

**Current goal:** Keep the honesty and sharpen reproducibility.

**Suggested additions:**
- Callout box at top: `This is pre-RL scaffold, not RL.`
- Exact model sizes and the combined size explanation.
- A 30-second reproducibility quickstart.
- A short section titled "Why this is credible".
- A short section titled "What would make this RL".
- One architecture diagram image plus text fallback.
- Demo link and expected output.

**Suggested copy improvement:**
- Replace "sub-250MB VLM" with "sub-300MB combined pipeline; 120MB main model + 182MB mmproj".
- Replace any ambiguous "feedback loop" wording with "hand-coded heuristic scoring loop".

---

## `paperclip/README.md`

**Current goal:** Clarify purpose and audience.

**Suggested additions:**
- One-line definition at top.
- Who it is for: developers building agents, not end users.
- Relationship to Dan Glasses and Dani.
- How it fits into the broader stack.
- Example usage or screenshot if available.
- CTA to the most relevant repo or demo.

**Suggested structure:**
1. What it is
2. Why it exists
3. Who should use it
4. How it relates to Dan Glasses
5. Quickstart
6. Status

---

## `blurr/README.md`

**Current goal:** Explain whether Blurr is a product, library, or experiment.

**Suggested additions:**
- One-line definition.
- Status label: active / experimental / archived.
- Relationship to DanLab.
- What problem it solves.
- If it is a visual layer, show screenshots.
- If it is infra, show the data flow.

---

## `dan-glasses/Services/audiod/SPEC.md`

**Current goal:** Make the production status obvious.

**Suggested additions:**
- v0.6 callout at top.
- Health endpoint and status example.
- Test summary: 101/101.
- Adaptive timeout subsection with rationale.
- Known failure modes and fallback behavior.
- Integration map: how audiod connects to perceptiond and memoryd.

**Suggested copy:**
- `audiod is the voice edge of the Dan Glasses stack. It handles VAD, transcription, and timeout discipline so the rest of the system can stay responsive.`

---

## `dan-glasses/Services/perceptiond/SPEC.md`

**Current goal:** Make the visual loop understandable.

**Suggested additions:**
- What inputs it sees.
- What score it produces.
- When it triggers memory writes or tool calls.
- The difference between frame capture and salience scoring.
- Failure behavior when the camera is unavailable.

---

## `dan-glasses/Services/memoryd/SPEC.md`

**Current goal:** Make memory concrete, not mystical.

**Suggested additions:**
- Explain episodic vs semantic vs procedural memory in plain English.
- Add query examples.
- Add retention and deletion behavior.
- Add privacy notes.
- Add one concrete user story: "what did I say last Tuesday?"

---

## `paperclip`, `blurr`, and all smaller repos

**If the repo is public and strategic, every README should include:**
- Why it exists.
- What stage it is at.
- What is missing.
- What the next contribution should be.
- A link back to DanLab.

**Do not:**
- bury the lead,
- overclaim,
- or force readers to read code before they understand the point.

---

## Recommended README template

```md
# Project Name

One-line definition.

## Why it exists
Short paragraph.

## What ships today
- item 1
- item 2

## Architecture
Diagram or table.

## Quickstart
Commands.

## Proof
Tests / demo / benchmarks / screenshots.

## What this is not
Boundary-setting.

## Next work
Bullet list.

## Built at DanLab
From India to the world.
```

---

## Priority order

1. `dan-glasses/README.md`
2. `dan-glasses/ARCHITECTURE.md`
3. `dan-glasses/Services/audiod/SPEC.md`
4. `danlab-multimodal/README.md`
5. `paperclip/README.md`
6. `blurr/README.md`

**Reason:** these are the public-facing source of truth. Fix them first, then everything else can reference them.
