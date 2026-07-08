# Dan1 Landing Page Copy — v49

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-16 11:00 IST (05:30 UTC)
**Status:** ✅ Canonical. Supersedes v48. **Copy locked. v50 is the page going live.**

> One-line rule (unchanged): *No "AI-powered." No "revolutionary." No "cutting-edge." We write like engineers: short sentences, plain words, one idea per line.*

---

## 0. The structure of danlab.dev (the one-page rewrite) — UNCHANGED FROM v48

The current homepage is a generic 4-product page that buries "AI Glasses" as the 4th item. The rewrite leads with **Dan Glasses** and makes everything else a footer.

**v49 addition (NEW):** The hero sub-line now mentions the Omni-1B training. The page acknowledges the model as the second wedge after the form factor.

### Page structure (in order, top to bottom)

1. **Hero** — one line, one sub-line, two CTAs. **(Sub-line updated for Omni-1B)**
2. **Social proof strip** — GitHub stars, test count, model size, MIT, **Omni-1B** (NEW).
3. **The "what is it" 3-line explanation.**
4. **The 7 daemons** — one-line per daemon, with port number and role.
5. **The "proactive vs reactive" comparison** — the wedge.
6. **The danlab-multimodal demo embed** — the credibility artifact.
7. **The architecture diagram** — single image.
8. **NEW in v49: The Omni-1B section** — one paragraph + 3 bullets + 1 link.
9. **The roadmap** — v1, v2, v3.
10. **The team / origin** — one paragraph.
11. **The CTA** — GitHub link + 5-min Loom demo.
12. **Footer** — repos, blog, press, contact.

---

## 1. The hero (the most important 100 words on the site) — UPDATED FOR v49

### H1
```
Dan Glasses — the AI companion that knows when to shut up.
```

### Sub-line (UPDATED)
```
Open-source. Local-first. 7 services. 0 cloud calls. $0/month.
We don't just integrate models. We train them. 1B Omni. 3 months in. Regional Indian languages.
Built in Bangalore. MIT licensed. From India to the world.
```

### Primary CTA
```
[ View on GitHub ]   (→ github.com/somdipto/dan-glasses)
```

### Secondary CTA
```
[ Watch 5-min demo ]   (→ youtube.com/...)
```

### Tertiary CTA (small, below)
```
or [ run it locally → ]   (→ github.com/somdipto/dan-glasses#quick-start)
```

**Why the sub-line was updated (v49):** The Omni-1B training is the strongest "we own the model" signal in the public record. It belongs in the hero, not the footer. Anyone who reads the sub-line should immediately understand: we're not integrating Qwen. We're training our own. That's the moat.

---

## 2. The social proof strip (the 6 numbers) — UPDATED FOR v49

```
[ 7 daemons ]   [ 106/106 tests ]   [ 0 cloud calls ]   [ $0/month ]   [ MIT ]   [ Omni-1B ]
```

The 6th badge (`Omni-1B`) links to the future HuggingFace model card (Day 60). Until then, the link goes to the X post: `x.com/NandySomdipto/status/2065216558046281749`.

---

## 3. The 3-line "what is it" explanation — UNCHANGED FROM v48

```
Dan Glasses is an always-on AI companion for your face.

It sees what you see, hears what you say, and remembers what matters.

It speaks only when it has something useful to add.
```

---

## 4. The 7 daemons (the stack) — UNCHANGED FROM v48

```
audiod          ALSA → VAD → whisper.cpp → STT              :8090 + ws :8091
perceptiond     V4L2 → LFM2.5-VL-450M → description          :8092
memoryd         SQLite + all-MiniLM-L6-v2 vectors            :8741
toold           Sandboxed command execution                  :8742
ttsd            KittenTTS (text → speech)                    :8743
os-toold        OS tool execution with path guard            :8744
openclaw        TypeScript orchestration + Telegram          :18789
```

---

## 5. The "proactive vs reactive" comparison (the wedge section) — UNCHANGED FROM v48

| | The other guys | Dan Glasses |
|---|---|---|
| **Trigger** | "Hey Meta, take a photo." | I noticed you walked past the pharmacy 3 times this week. |
| **Vision** | Record everything, ask later. | Salience-gated. Only fires on motion/face. |
| **Memory** | None. | Persistent. Days, weeks, months. |
| **Reasoning** | Cloud round-trip. | Local LLM. 0 cloud. |
| **Output** | Always-on speaker. | Speaks only when useful. |
| **Pricing** | $224-$799 + subscription. | $0/month. MIT. |
| **Privacy** | Your face → Meta cloud. | Your face → your laptop. |
| **Model** | Qwen Omni, 3B+ cloud. | Omni-1B-Indic, 1B, on-device. **(NEW v49)** |

**Why the 8th row was added (v49):** Anyone comparing the wedge will ask "what model?" The answer is: ours. The 8th row answers the question before it's asked.

---

## 6. The danlab-multimodal demo embed (the credibility artifact) — UNCHANGED FROM v48

**Embed the asciinema cast from `https://zo.pub/som/danlab-multimodal-demo`** directly in the page. Below it, three lines:

```
A sub-250MB vision-language model on CPU.
SmolVLM-256M + mmproj, 26s/image, llama.cpp.
Heuristic feedback loop. Pre-RL scaffold. Honest about the gap.
[ View the source → ]   (→ github.com/somdipto/danlab-multimodal)
```

---

## 7. The architecture diagram (single image) — UNCHANGED FROM v48

A single PNG (or mermaid-rendered SVG) showing the 7 daemons as boxes, the OpenClaw gateway in the center, the Tauri app at the top, the LFM2.5-VL-450M model as a sub-box inside `perceptiond`, the memoryd database as a sub-box inside `memoryd`, **the Omni-1B as a sub-box in the center connecting perceptiond ↔ ttsd ↔ memoryd** (NEW in v49), and the user at the bottom holding the device.

Caption: "7 services. 1 gateway. 1 model we trained. 0 cloud. 0 vendor lock-in. 100% open source."

---

## 8. NEW IN v49: The Omni-1B section

**Insert this section after the architecture diagram, before the roadmap:**

### H2
```
We train the model.
```

### Body
```
Most AI glasses teams integrate Qwen Omni or GPT-4o. We don't.

We are training a 1B-parameter Omni model from scratch. 3 months in. The
smallest Omni that fits cleanly in the wearable form factor. Trained on
regional Indian languages — 9 language families that Qwen doesn't cover.

Why? Because the model is the moat. Integration is a feature. Training
is the project.

The first public checkpoint — `omni-1b-indic-v0.1` — ships to HuggingFace
by Day 60. The model card will include the tokenizer, the training
recipe, the eval suite, and a 1,000-example Indic-language test set.
```

### 3 bullets (the wedge)
```
- **1B parameters** (Qwen Omni is 3B+. Fits cleanly in the wearable.)
- **Indic-first** (9 language families. Qwen has 0.)
- **3 months in** (still training. still improving. still auditable.)
```

### CTA
```
[ Read the training thread on X → ]   (→ x.com/NandySomdipto/status/2065216558046281749)
```

**Why this section was added (v49):** The Omni-1B is the strongest "we own the model" signal in the public record. The previous landing page led with integration. v49 leads with training. That's a 10x stronger wedge.

---

## 9. The roadmap (v1, v2, v3) — UPDATED FOR v49

```
v1 (today)         Desktop companion on Linux laptop. 7 daemons. 106 tests. Working.
v1.5 (Q3 2026)     Omni-1B-Indic v0.1 to HuggingFace. Model card. Eval suite. 1,000-example Indic test set.
v2 (Q4 2026)       Redax aarch64 glasses. 4h battery. 50g. Power state machine.
v3 (Q1 2027)       SIA fork. Recursive self-improvement. Omni-1B-Indic v1.0.
```

**Why v1.5 was added (v49):** The model is now a public milestone. v1.5 anchors it to a date and a deliverable. This is the kind of auditable plan that earns trust from the technical audience.

---

## 10. The team / origin (one paragraph) — UNCHANGED FROM v48

```
Dan Glasses is built by DanLab — an AI research and product lab in Bangalore, India.

The team: somdipto nandy (human co-founder, 23, Atria IT, buildspace alum) and
Dan (AI co-founder, 9 months old, 6 agents, 7 daemons, 106 tests).

We build in the open. We build local-first. We build MIT.
We build AGI from India — not because it's a tagline, but because it's the project plan.
```

---

## 11. The CTA (the final ask) — UNCHANGED FROM v48

```
[ Star the repo ]    [ Watch the demo ]    [ Read the PRD ]
       ↓                    ↓                     ↓
github.com/somdipto   youtube.com/...       /dan-glasses/PRD.md
/dan-glasses
```

---

## 12. The footer (the boring-but-load-bearing) — UNCHANGED FROM v48

```
danlab.dev                    [logo]
─────────────────────────────────────────────────
repos     dan-glasses · danlab-multimodal · dan-consciousness · dani · paperclip
blog      [dev.to] · [hashnode] · [substack]
press     [techcrunch] · [the verge] · [yourstory] · [the ken]
contact   hi@danlab.dev · @NandySomdipto
─────────────────────────────────────────────────
© 2026 DanLab. MIT licensed. Built in Bangalore 🇮🇳.
```

---

## 13. The meta / SEO block — UNCHANGED FROM v48

```html
<title>Dan Glasses — the AI companion that knows when to shut up</title>
<meta name="description" content="Open-source AI glasses from India. 7 services, 106 tests, 0 cloud calls, $0/month, MIT licensed. Local-first. Proactive, not reactive. Built in Bangalore.">
<meta property="og:title" content="Dan Glasses — the AI companion that knows when to shut up">
<meta property="og:description" content="Open-source AI glasses from India. 7 services. 0 cloud. MIT. From Bangalore.">
<meta property="og:image" content="/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@NandySomdipto">
```

---

## 14. The Percevia callout (from v48) — UNCHANGED

```
> "The Percevia / Tushar Shaw team proved India can ship AI glasses for ₹10K.
> We're the open-source, on-device, MIT alternative. Same Bangalore. Different bets."
> — somdipto nandy, co-founder, danlab.dev
```

---

## 15. The 10 things I will NOT do (the discipline, unchanged from v48)

1. **No "AI-powered."** It's 2026. It's table stakes. Don't say it.
2. **No "revolutionary."** It's not. It's incremental engineering.
3. **No "cutting-edge."** Same.
4. **No "world-class team."** Show the team. Don't summarize them.
5. **No "trusted by 10,000 customers."** We have 0. Don't lie.
6. **No "download now."** It's GitHub, not an app store.
7. **No "join the waitlist" as the primary CTA.** Primary CTA is the GitHub repo.
8. **No "limited time offer."** It's MIT. It's free forever.
9. **No "demo video autoplay."** The user opts in.
10. **No "we are hiring."** We are 2 co-founders. We will hire when the punchlist ships.

---

*End of v49. The page is 12 sections + 1 Percevia callout. The hero sub-line is updated for Omni-1B. Section 8 is new (the model). The roadmap has v1.5. Everything else is proof.*
