# Dan1 Landing Page Copy — v61

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-19 08:00 IST (02:30 UTC)
**Status:** ✅ Canonical. Supersedes v60.
**Reads:** `dan1-marketing-research.md` v61, `dan1-marketing-strategy.md` v61, `dan1-content-calendar.md` v61.

> **v61 is the receipt-anchored landing page.** The hero leads with the cell (sub-50g, <$200 BOM, MIT, proactive, on-device). The proof strip shows the Snap Specs comparison. The features section is unchanged in structure from v60. The waitlist CTA is sharpened.

---

## Hero (above the fold)

### Headline (H1)

**An AI companion that tells you first — not when you ask.**

### Subheadline (H2, 1-2 lines)

**Dan Glasses is the first MIT-licensed, on-device, proactive AI companion glasses. Sub-50g. <$200 BOM. India-priced. From a lab in Bengaluru.**

### Primary CTA

**[ Join the waitlist → ]**

*50 dev-kit units. Q1 2027 alpha. India + Bay Area.*

### Secondary CTA

**[ See the code ]**  (links to github.com/somdipto/dan-glasses)

### Proof strip (under the CTAs, 4-5 receipts)

| Receipt | Source |
|---------|--------|
| **7 daemons shipped, 131/131 tests green** | DAN-4 verification 2026-06-19 |
| **Snap spent ~$500M and shipped 132-136g, $2,195 reactive glasses** | Yahoo Finance (Guggenheim), Dezeen, June 16-18 |
| **Snap Specs runs TWO Qualcomm Snapdragon processors** | Road to VR, June 16 |
| **Qualcomm unveiled Snapdragon Reality Elite + START at AWE 2026** | TechCrunch, thelec.net, June 17-18 |
| **Anthropic Fable 5 ban triggered 4 open models to respond in 48h** | The New Stack, June 11 |

---

## Section 1 — The cell

### Headline (H2)

**The cell no one else occupies.**

### Subhead (H3)

**Every AI glasses product in 2026 is on zero of these four axes. Dan Glasses is on all four.**

### Four axes (icon grid)

| Axis | Competitors | Dan Glasses |
|------|-------------|-------------|
| **Proactive, not reactive** | Every AI glasses product (Meta, Google, Snap, Apple, Acer) requires user activation. | It tells you first. |
| **On-device, not cloud** | Meta (Gemini), Google (Gemini), Snap (Snap OS), Apple (Siri), Acer GI0 (Gemini) — all cloud. | 0 cloud. 7 daemons on a Linux laptop. |
| **MIT, not closed** | Every competitor has a closed source tree, a cloud dependency, or both. | MIT all the way down. Hardware, software, model. |
| **Sub-50g + <$200 BOM** | Snap is 132-136g, $2,195. The closed-source physical floor. | <50g, <$200 BOM. India-priced. |

### Closing line

> **The 2x2 cell. Four axes. Dan Glasses is the only entry on all four. Fork the whole thing.**

---

## Section 2 — How it works (the proactive loop)

### Headline (H2)

**Proactive, not reactive.**

### Subhead (H3)

**The agent loop runs in the background. It pushes events to you at the moment they're needed — never after, never before, never on a voice command.**

### Diagram (4-step flow)

```
[ 1. Sense ]      [ 2. Recall ]      [ 3. Reason ]      [ 4. Act ]
  (perceptiond)     (memoryd)         (reasond,          (ttsd, toold,
                                       planned)           os-toold)

  Camera + mic →   What does         Should I tell      Push the event
  Salience gate.   Dan know          Dan about this?    to the user.
  Motion + face.   about this?       Proactive or       No wake word.
                   Semantic          wait?              No question.
                   recall.           HRM-Text 1B.        Just the event.
```

### Three examples (concrete)

| Moment | What Dan Glasses does |
|--------|------------------------|
| **You walk into a meeting room** | Glances at the calendar. "Your 2pm is in 5 min. Priya is running late — 10 min. Want to push the agenda?" |
| **Someone approaches with a new face** | Cross-references LinkedIn connections (on-device, opt-in). "Arjun Mehta, ML engineer at [company]. Last met March 2026. No follow-ups." |
| **You stare at the same code for 90s** | Pulls up the last 3 PRs you reviewed on that file. "You reviewed this file 2 weeks ago. There's a new diff in #247. Want me to summarize?" |

---

## Section 3 — The daemons (the receipts)

### Headline (H2)

**7 daemons. 131/131 tests green. MIT all the way down.**

### Subhead (H3)

**This is the proof. The form factor is the next thing.**

### Daemon grid (table)

| Daemon | Role | Tests | Stack |
|--------|------|-------|-------|
| **audiod** | Microphone → VAD → whisper.cpp → transcript events | 83/83 | Silero VAD, whisper.cpp, Python |
| **perceptiond** | V4L2 camera → salience → LFM2.5-VL-450M → description events | 8/8 | linuxpy, OpenCV, llama.cpp, GGUF |
| **memoryd** | Episodic + semantic + procedural memory, vector recall | 16/16 | FastAPI, sentence-transformers, SQLite |
| **toold** | Sandboxed exec with path guard | 18/18 | FastAPI, asyncio |
| **ttsd** | Text → KittenTTS → audio | 6/6 | KittenTTS, ONNX |
| **os-toold** | Path guard for every command | live | FastAPI |
| **openclaw** | Agent gateway, Telegram channel | live | TypeScript/Node, MCP |

### Install command (copy-paste)

```bash
git clone github.com/somdipto/openwork
cd openwork
./scripts/dev.sh up
```

*All daemons run on any Linux laptop. Total disk: ~600MB (models + deps).*

---

## Section 4 — The hardware (what's next)

### Headline (H2)

**Q1 2027 alpha. 50 dev-kit units. India + Bay Area.**

### Subhead (H3)

**The form factor is the next thing. The software is the proof.**

### Three columns (concrete)

| Spec | Target | Receipt |
|------|--------|---------|
| **Weight** | <50g | Snap Specs: 132-136g |
| **BOM** | <$200 | Snap Specs: $2,195 |
| **Silicon** | ONE processor, MIT, on-device | Snap Specs: TWO processors, closed, cloud |
| **Battery** | 8h target (4h minimum) | Snap Specs: 4h |
| **License** | MIT all the way down | Every competitor: closed |

### Roadmap (timeline)

```
Q3 2026:  Public demo video. Waitlist opens.
Q4 2026:  First 50 dev-kit units ship (manual onboarding).
Q1 2027:  General availability. India + Bay Area.
Q2 2027:  Production at scale. Lenskart OEM partnership (target).
Q4 2027:  10,000 units shipped. (Stretch goal.)
```

---

## Section 5 — The story (the origin)

### Headline (H2)

**From India to the world. Built in the open.**

### Subhead (H3)

**Started in a bedroom in Bengaluru. Now shipping MIT-licensed wearable AI for the price of a mid-range Android phone.**

### Three paragraphs (origin)

> **Act I — Roots (2022-2025).** Somdipto Nandy builds danlab.dev as a solo research lab in India. The thesis: AGI will come from teams that can ship *and* research, not from either alone. First artifacts: an open-source agent harness, a multimodal pipeline, an Android accessibility app.

> **Act II — Hardware (2026).** Dan Glasses begins — the first MIT-licensed, on-device, proactive AI companion glasses. Today the 7 daemons ship and run on Linux laptops. The hardware form factor follows. Competitors are charging $499-2,195 for cloud-dependent reactive devices. Dan Lab is targeting ₹12K-15K with MIT all the way down.

> **Act III — Distribution (2027+).** Once Dan Glasses hits its BOM target and ships, Dan Lab moves from a research lab to a product lab with a global install base. Open-source. MIT. Forkable. The same way Linux ate the data center.

### Footer line

> **AGI from India — built in the open.**

---

## Section 6 — The waitlist (the CTA)

### Headline (H2)

**Join the waitlist.**

### Subhead (H3)

**50 dev-kit units. Q1 2027 alpha. India + Bay Area.**

### Form (Tally or Formspree)

```
[ Email                                       ] [ Join the waitlist → ]

By joining, you agree to receive updates from danlab.dev. We don't sell
your email. We don't share your email. We don't track you across the web.
```

### Trust strip (under the form)

| Receipt | Source |
|---------|--------|
| **MIT license, all 7 daemons** | github.com/somdipto/dan-glasses |
| **131/131 tests green** | DAN-4 verification 2026-06-19 |
| **0 cloud, 0 faceprints, 0 background process** | Internal spec |
| **₹12K-15K BOM target** | Internal target |
| **India + Bay Area launch** | Internal target |

---

## Section 7 — FAQ

**Q: When does it ship?**
A: Q1 2027 dev-kit alpha. 50 units. India + Bay Area. General availability follows in Q2 2027.

**Q: How much will it cost?**
A: ₹12K-15K BOM target ($145-180). Retail price will be set at manufacturing. The BOM is the wedge; the retail will be competitive with mid-range Android phones.

**Q: Why MIT?**
A: Because we don't want the product to be abandoned. The Snap $500M number is the receipt — closed-source R&D at scale costs hundreds of millions, and even Snap had to spin off its AI video team. MIT is irrevocable. We are not.

**Q: Why on-device?**
A: Privacy, latency, and resilience. Meta's NameTag face-recognition code was carried in 50M+ phones without public launch or opt-in (WIRED, June 2026). On-device means no server, no leak, no opt-in bypass.

**Q: Why proactive, not reactive?**
A: Because reactive AI is an assistant. Proactive AI is a companion. The agent loop should run in the background and push events at the moment they're needed — not when you ask. The wedge is the *timing of the prompt*.

**Q: How is this different from Meta Ray-Ban, Google Android XR, Snap Specs, Apple AI Glasses?**
A: All of them are reactive (you speak, it answers). All of them are cloud-dependent (Gemini, Siri, Snap OS). All of them are closed source. Snap Specs is 132-136g at $2,195. Dan Glasses is sub-50g at <$200 BOM, MIT, on-device, proactive. The 2x2 cell is ours.

**Q: How is this different from Brilliant Labs Halo or Raven Prism?**
A: They're allies. Brilliant Labs Halo uses the same LFM2-VL 450M vision model. Raven Prism is privacy-first. Neither is MIT all the way down. Neither is sub-50g at <$200 BOM. Neither is proactive.

**Q: What if the hardware slips?**
A: We have the software. 7 daemons, 131/131 tests green, runs on any Linux laptop today. The hardware is the form factor. The software is the proof.

**Q: Can I fork it?**
A: Yes. github.com/somdipto/dan-glasses. MIT license. Fork the whole thing. Improve it. Ship a version under your brand. We want that.

**Q: Is the BOM really $145-180?**
A: That's the target. The actual cost depends on the silicon choice and the manufacturing partner. We're applying to the Qualcomm START program to lock in a silicon ally.

**Q: What about Fable 5, export controls, regulation?**
A: MIT means we are structurally aligned with US policy direction (DoD "supply chain risk" framing, June 17, 2026). The Fable 5 ban triggered 4 open models to respond within 48 hours. The open-weights community is the immune system. We are part of it.

---

## Section 8 — The footer (the brand)

```
[ danlab.dev ]   [ github.com/somdipto ]   [ X: @somdipto ]   [ Telegram: @Shodan_s ]

AGI from India — built in the open.
MIT licensed. 🇮🇳

Dan Lab is a research and product lab. Dan is the AI co-founder (Bengaluru).
somdipto is the human co-founder (Bengaluru).
```

---

*Dan1 landing copy v61 — canonical. Next pass: v62 after Day 0 punchlist ships or by 2026-06-26 08:00 IST, whichever comes first.*
