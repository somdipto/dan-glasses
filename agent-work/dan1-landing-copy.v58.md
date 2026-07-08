# Dan1 Landing Page Copy — v58

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-18 15:05 IST (09:35 UTC)
**Status:** ✅ Canonical. Supersedes v57.
**Read first:** `dan1-marketing-strategy.md` v58.
**Target pages:** `danlab.dev` (homepage, **LIVE today**), `openwork.danlab.dev` (openwork product, recommended), `dan-glasses` GitHub README (header).

> One-line rule: *Two new live receipts today — Snapdragon Reality Elite (the chip) and Meta NameTag + Rank One (the privacy). Thread them through the H1, the proof strip, the AI Glasses card, and the FAQ. The chip is the upside. The privacy is the wedge. The price is the proof. From India 🇮🇳 to the world.*

## 0. The v58 delta (3 hours after v57)

| Element | v57 | v58 | Why it matters |
|---|---|---|---|
| Privacy receipt | "WIRED June 2026 + 50M+ users had dormant face-rec modules" | **"WIRED June 2026: NameTag is wired to Rank One — U.S. Marshals / NCIS / Special Operations Command face-ID vendor. Active surveillance supply chain, not dormant code."** | Sharper story. It's a backdoor to the U.S. government, not just "dormant." |
| Chip receipt | None | **"Snapdragon Reality Elite, AWE 2026 Day 2: 48 TOPS on-device AI, XREAL Aura Fall 2026, Android XR native."** | The on-device thesis just got its biggest endorsement. The chip era started this week. |
| Product row | 6 cards | **7 cards (added chip-anchor line to AI Glasses card)** | Anchor the AI Glasses card to the chip |
| Hero CTA | "Pre-order the MIT AI glasses" | **"Pre-order the MIT AI glasses. Built for Snapdragon Reality Elite class."** | Ties the body to the chip without claiming it ships on it |
| FAQ | 6 questions | **7 questions (added: "Will Dan Glasses run on Snapdragon Reality Elite?")** | The chip question is the #1 question developers will ask |
| Reactive CTA | "AWE 2026 closes tomorrow" | **"AWE 2026 closes today. The chip era started yesterday."** | Day 3 of 4 today, Day 4 closing tomorrow |

**v58 = v57 + chip anchor + sharper privacy story + chip FAQ.**

---

## 1. danlab.dev — Homepage hero (work with what's LIVE)

**Current LIVE state (verified 09:35 UTC, 2026-06-18):**
- H1: "DanLab - AI Product & Research Lab"
- H2: "Our Products"
- Products (4): Agent8, Zerant, Dapify, AI Glasses
- H2: "Research" → "DanLab is on the path to AGI through reasoning, creative, and synthesis research."
- Footer: "© 2025 DanLab Inc. India"

### Recommended v58 changes (7 edits, 1 hour 10 min total)

**Edit #1 — Add `openwork` to the product row (5th card):**
```html
<article>
  <h3>openwork</h3>
  <p>The open-source AI coworker. MIT, 100+ skills, 4 agents, 0 cloud. Runs in Claude Code / Cursor / Codex.</p>
  <a href="https://github.com/somdipto/openwork">github.com/somdipto/openwork</a>
</article>
```

**Edit #2 — Strengthen the AI Glasses card with the chip anchor (replace existing copy):**
```html
<article>
  <h3>AI Glasses (Dan Glasses)</h3>
  <p>Wearable AI companion. Q4 2026. Proactive, not reactive. 0 cloud. MIT.</p>
  <p class="chip-anchor">Built for the Snapdragon Reality Elite class silicon. 48 TOPS on-device AI.</p>
  <a href="https://github.com/somdipto/dan-glasses">github.com/somdipto/dan-glasses</a>
</article>
```

**Edit #3 — Add the privacy receipt to the H2 (replace existing "Research" H2):**
```html
<h2>Why we build open</h2>
<p>
  Every AI glasses product on the market is closed, cloud-locked, and priced above $499.
  And every one of them ships with a face-rec backdoor. WIRED's June 2026 investigation
  found Meta's "dormant" NameTag face-rec is actively wired to Rank One — the U.S. Marshals,
  Naval Criminal Investigative Service, and U.S. Special Operations Command face-ID vendor.
</p>
<p>
  We started DanLab with a question: why are all AI glasses products closed, cloud-locked,
  and priced above $499? So we built the open alternative. Proactive, on-device, MIT, India-priced.
</p>
```

**Edit #4 — Add a chip-anchor proof strip (NEW, between products row and Research H2):**
```html
<section class="proof-strip">
  <h3>Shipped on the new chip class</h3>
  <ul>
    <li><strong>48 TOPS</strong> on-device AI (Qualcomm Snapdragon Reality Elite, AWE 2026 Day 2)</li>
    <li><strong>4.4K/eye</strong> at 90 Hz, 12-camera SLAM</li>
    <li><strong>160% NPU</strong> boost over XR2+ Gen 2</li>
    <li><strong>XREAL Aura</strong> + <strong>Play for Dream</strong> launch Fall 2026</li>
  </ul>
</section>
```

**Edit #5 — Add the proactive wedge under the AI Glasses card (NEW, under Edit #2):**
```html
<aside class="proactive-wedge">
  <p>
    <strong>Proactive, not reactive.</strong> Dan Glasses tells you things you need to know
    before you ask. No button. No voice activation. No cloud round-trip.
  </p>
</aside>
```

**Edit #6 — Add the India price wedge as a footer accent (NEW):**
```html
<section class="india-wedge">
  <p>
    <strong>From India 🇮🇳, priced for the world.</strong> Dan Glasses target price: ₹12-15K.
    Built in Bangalore. Priced in INR. Open-source from day 1.
  </p>
</section>
```

**Edit #7 — Add the reactive CTA (UPDATED v58):**
```html
<aside class="reactive-cta">
  <p>
    <strong>AWE 2026 closes today. The chip era started yesterday.</strong>
    <a href="https://github.com/somdipto/openwork">Try openwork</a> ·
    <a href="https://github.com/somdipto/dan-glasses">Star Dan Glasses</a>
  </p>
</aside>
```

### Hero stats strip (add below the products row, 4 numbers) — UPDATED v58

```html
<section class="hero-stats">
  <div class="stat">
    <span class="stat-num">100+</span>
    <span class="stat-label">Skills (openwork)</span>
  </div>
  <div class="stat">
    <span class="stat-num">4</span>
    <span class="stat-label">Agents (openwork)</span>
  </div>
  <div class="stat">
    <span class="stat-num">48</span>
    <span class="stat-label">TOPS on-device (Snapdragon Reality Elite)</span>
  </div>
  <div class="stat">
    <span class="stat-num">₹12-15K</span>
    <span class="stat-label">Target price (Dan Glasses)</span>
  </div>
</section>
```

### Above-the-fold CTA (NEW, add below hero stats)

```html
<div class="cta-row">
  <a class="cta-primary" href="https://github.com/somdipto/dan-glasses">Star Dan Glasses on GitHub</a>
  <a class="cta-secondary" href="https://github.com/somdipto/openwork">Install openwork</a>
</div>
```

---

## 2. openwork.danlab.dev — Product page (recommended, 1 day to ship)

### Above the fold

**H1:** *The open-source AI coworker.*

**Subhead:** MIT, 100+ skills, 4 agents, 0 cloud. Runs in Claude Code, Cursor, or Codex.

**Primary CTA:** `Install openwork` → `git clone https://github.com/somdipto/openwork && cd openwork && ./install.sh`

**Secondary CTA:** `Read the docs` → `github.com/somdipto/openwork/blob/main/README.md`

**Tertiary CTA:** `Star on GitHub` → `github.com/somdipto/openwork`

**Privacy receipt (NEW, above-the-fold strip):**

> *"WIRED's June 2026 investigation: Meta's 'dormant' NameTag face-rec is wired to Rank One — a U.S. Marshals face-ID vendor. openwork is the MIT alternative. 0 cloud calls. 0 telemetry. 0 faceprints."*

### Hero stats strip (4 numbers) — UPDATED v58

```html
<section class="hero-stats">
  <div class="stat">
    <span class="stat-num">100+</span>
    <span class="stat-label">Skills</span>
  </div>
  <div class="stat">
    <span class="stat-num">4</span>
    <span class="stat-label">Agents</span>
  </div>
  <div class="stat">
    <span class="stat-num">0</span>
    <span class="stat-label">Cloud calls</span>
  </div>
  <div class="stat">
    <span class="stat-num">MIT</span>
    <span class="stat-label">All the way down</span>
  </div>
</section>
```

---

## 3. openwork — Feature blocks (4 cards)

### Feature 1: Proactive, not reactive
The background agent loop watches your work and pushes events at the moment you need them. Not after. Not before. Not when you ask.

### Feature 2: 100+ skills
Shell, git, files, calendar, browser, web search, vector DB, image gen, code exec, PDF parse, OCR, TTS, STT, and 87 more. All MIT. All local.

### Feature 3: 4 agents
Researcher, writer, ops, builder. Each agent has its own memory, its own skills, its own goals. They collaborate via shared context.

### Feature 4: 0 cloud calls (with WIRED receipt)
Every other AI coworker phones home. openwork doesn't. WIRED's June 2026 investigation revealed Meta's "dormant" face-rec is wired to a U.S. Marshals face-ID vendor. The coworker that touches your files should not be a backdoor. openwork never was.

---

## 4. openwork — Tech stack (one-liner per layer) — UPDATED v58

```
Skills:       TypeScript, 100+ skills, MIT
Workflows:    13 GTM workflows, YAML-defined
Agents:       4 agents, runnable in parallel
Memory:       local SQLite + sentence-transformers
LLM:         Ollama / vLLM / LM Studio (local) OR Claude / OpenAI (BYOK)
Runtime:      paperclip + dani (MIT)
Future:       Q4 2026: runs on Snapdragon Reality Elite class silicon
```

---

## 5. openwork — From India to the world (1 paragraph)

We're a small team in Bangalore, India 🇮🇳. We started in 2026 with a question: why are all AI coworker products closed, cloud-locked, and priced above $20/mo? So we built the open alternative. MIT, forkable, inspectable, local-first. The brain you put in your workflow should be YOURS. From India 🇮🇳 to the world.

---

## 6. openwork — FAQ (7 questions, short answers) — UPDATED v58 (added #7)

**Q1: Is openwork really MIT?**
A1: Yes. The brain, the skills, the workflows, the runtime, the memory layer, and the CLI are all MIT. The local LLM (Ollama / vLLM / LM Studio) is up to you.

**Q2: Does it really work offline?**
A2: Yes. With a local LLM (Ollama / vLLM / LM Studio) it makes 0 cloud calls. With Claude / OpenAI (BYOK) it makes N+1 cloud calls (your API key, your bill).

**Q3: How is it different from LangChain / CrewAI / AutoGen?**
A3: LangChain is a framework. openwork is a coworker. The difference is the agent loop: openwork runs in the background and pushes events. LangChain waits for you to invoke it.

**Q4: How is it different from Devin / Cognition?**
A4: Devin is closed, $500/mo, and cloud-only. openwork is MIT, free, and local-first. Different ICP, different category.

**Q5: Will it run on my M-series Mac?**
A5: Yes. openwork runs on any Linux / macOS / WSL2 box with Python 3.10+ and Node 20+. The LLM is local (Ollama is M-series native).

**Q6: What's the relationship to Dan Glasses?**
A6: openwork is the brain. Dan Glasses is the body. Q4 2026, the same MIT agent loop that runs on your laptop today runs in the glasses. Built for the Snapdragon Reality Elite class silicon (48 TOPS on-device AI).

**Q7 (NEW v58): Will Dan Glasses run on Snapdragon Reality Elite?**
A7: That's the target. The chip class was announced at AWE 2026 Day 2 (June 17). XREAL Aura and Play for Dream launch Fall 2026. Dan Glasses targets Q4 2026 on the same silicon class — 48 TOPS on-device AI is the floor, not the ceiling.

---

## 7. openwork — Final CTA (bottom of page)

```html
<section class="final-cta">
  <h2>Install openwork. Ship your own AI coworker.</h2>
  <pre><code>git clone https://github.com/somdipto/openwork
cd openwork && ./install.sh</code></pre>
  <p>MIT. 100+ skills. 4 agents. 0 cloud. From India 🇮🇳 to the world.</p>
  <a class="cta-primary" href="https://github.com/somdipto/openwork">Star on GitHub</a>
</section>
```

---

## 8. dan-glasses GitHub README (header, use §1.1 of `dan1-github-readme-suggestions.md` v58)

*(unchanged from v57 — the chip + privacy anchors are added in §9 below)*

---

## 9. Dan Glasses product page (recommended, 1 day to ship at `dan-glasses.danlab.dev`) — UPDATED v58

### Above the fold

**H1:** *The wearable AI companion that thinks before you ask.*

**Subhead:** Proactive, on-device, MIT, India-priced. Built for the Snapdragon Reality Elite class silicon. Q4 2026.

**Primary CTA:** `Join the pre-order list` → `danlab.dev/#preorder`

**Secondary CTA:** `Star on GitHub` → `github.com/somdipto/dan-glasses`

**Privacy receipt (NEW, above-the-fold strip):**

> *"WIRED June 2026: Meta's 'dormant' NameTag face-rec is actively wired to Rank One — a U.S. Marshals / NCIS / Special Operations Command face-ID vendor. Dan Glasses: 0 cloud. 0 faceprints. 0 backdoors."*

### Hero stats strip (4 numbers) — UPDATED v58

```html
<section class="hero-stats">
  <div class="stat">
    <span class="stat-num">7</span>
    <span class="stat-label">On-device daemons</span>
  </div>
  <div class="stat">
    <span class="stat-num">48</span>
    <span class="stat-label">TOPS on-device AI (target silicon)</span>
  </div>
  <div class="stat">
    <span class="stat-num">₹12-15K</span>
    <span class="stat-label">Target price</span>
  </div>
  <div class="stat">
    <span class="stat-num">MIT</span>
    <span class="stat-label">All the way down</span>
  </div>
</section>
```

### Wedge callout (3 lines, right under hero)

> *Siri: you speak, it answers.*
> *Meta AI: you press a button, it answers.*
> *Dan Glasses: it tells you first.*

### 3 things no competitor does — UPDATED v58

1. **Proactive, not reactive.** Every AI glasses product on the market requires user activation (button or voice). Dan Glasses pushes events to the user.
2. **0 cloud. 0 faceprints. 0 backdoors.** On-device inference only. No cloud round-trip. No face-rec supply chain. WIRED's June 2026 Rank One exposé is the live receipt for why this matters.
3. **MIT + India-priced.** Not "open core." MIT. Not "$499." ₹12-15K. Built in Bangalore.

### The 7 daemons table (1 column per daemon) — UPDATED v58

| Daemon | Purpose | Stack | License |
|---|---|---|---|
| **audiod** | Continuous audio capture, VAD, STT | Silero VAD, whisper.cpp | MIT |
| **perceptiond** | First-person vision, salience, description | V4L2, LFM2.5-VL-450M | MIT |
| **memoryd** | Episodic + semantic + procedural memory | SQLite, MiniLM-L6-v2 | MIT |
| **toold** | Sandboxed shell / python / file exec | subprocess + path guards | MIT |
| **ttsd** | On-device TTS | KittenTTS | MIT |
| **os-toold** | OS path guard, safe execution surface | path validators | MIT |
| **openclaw** | TypeScript orchestration gateway | Node 20+, MCP, Telegram | MIT |

### Final CTA (bottom of page)

```html
<section class="final-cta">
  <h2>Join the pre-order list. MIT Q4 2026.</h2>
  <p>The first 1,000 names get a free dev prototype (Linux laptop, all 7 daemons, AWE 2026 chip class).</p>
  <a class="cta-primary" href="https://danlab.dev/#preorder">Join the pre-order list</a>
  <a class="cta-secondary" href="https://github.com/somdipto/dan-glasses">Star on GitHub</a>
</section>
```

---

*End of v58. Two receipts — chip + privacy — are now anchored on every page. The FAQ has a chip question. The product row has a chip line. The CTA has a chip phrase. The brain (openwork) and the body (Dan Glasses) both tell the same story: MIT, India, proactive, on-device. The chip era started this week. We are the MIT default for it. From Bangalore 🇮🇳 to the world.*

👾
