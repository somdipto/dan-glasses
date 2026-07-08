# Dan Glasses Landing Page Copy — v86

**Target audience:** Builders, researchers, indie hackers. NOT consumers.
**URL:** `danlab.dev` (and mirrored at `danglasses.dev` if owned)
**Format:** Single-page, dark-mode default, monospace headings, saffron accent (#FF6B00)
**Word count target:** 600 words body + 400 words FAQ

---

## Hero (above the fold)

```
DAN GLASSES
```

```
The open-source AI glasses daemon mesh.
Built in Bengaluru. MIT-licensed. Ships as a Debian package.
```

**Primary CTA:** `Read the SPEC` → `Services/audiod/SPEC.md` (anchors GitHub)
**Secondary CTA:** `Install the .deb` → download link
**Tertiary CTA:** `See the demo` → 30-second gif

---

## Section 1: The Pitch (3 paragraphs, ~150 words)

> Dan Glasses is the local-first alternative to cloud AI glasses. Eight daemons. One hundred and forty-four tests. Zero vendor lock-in.
>
> Every frame from your camera stays on your box. Every word you say is transcribed by `whisper.cpp` running on your CPU. Every description from the vision-language model is written to a SQLite database you can export. We don't sell a subscription. We don't train a model on your data. We don't even have a server that sees your data.
>
> Built by somdipto nandy and four AI co-founders from a desk in Bengaluru. Funded by founder time. Shipped as a 28KB Debian package.

---

## Section 2: The Mesh (8 cards, one per daemon)

```
┌─ audiod ──────────────────────────────────────┐
│  mic → Silero VAD → whisper.cpp → events      │
│  HTTP :8090  ·  WS :8091  ·  123 tests        │
│  Spec: 5,200 words                            │
└───────────────────────────────────────────────┘
```

```
┌─ perceptiond ─────────────────────────────────┐
│  V4L2 → motion+face → LFM2.5-VL → descs       │
│  HTTP :8092  ·  8 tests  ·  MJPEG viewfinder  │
│  Spec: 3,000 words                            │
└───────────────────────────────────────────────┘
```

```
┌─ memoryd ─────────────────────────────────────┐
│  text → MiniLM-L6-v2 → SQLite + vectors       │
│  HTTP :8741  ·  episodic+semantic+procedural  │
│  Spec: 1,400 words                            │
└───────────────────────────────────────────────┘
```

```
┌─ toold ────────────────────────────────────────┐
│  sandboxed shell + Python                     │
│  HTTP :8742  ·  path guard + allowlist         │
└───────────────────────────────────────────────┘
```

```
┌─ ttsd ─────────────────────────────────────────┐
│  KittenTTS medium → audio out                 │
│  HTTP :8743                                   │
└───────────────────────────────────────────────┘
```

```
┌─ os-toold ─────────────────────────────────────┐
│  path guard + restricted fs ops               │
│  HTTP :8744                                   │
└───────────────────────────────────────────────┘
```

```
┌─ openclaw ─────────────────────────────────────┐
│  Telegram + Zo MCP gateway                    │
│  HTTP :18789  ·  status: live                  │
└───────────────────────────────────────────────┘
```

```
┌─ dan-glasses-app ──────────────────────────────┐
│  Tauri v2 + React desktop UI                  │
│  Bootstrap wizard 7.08s roundtrip             │
│  Vision · Memory · TTS · Live Transcript      │
└───────────────────────────────────────────────┘
```

**CTA below cards:** `Read all the SPECs on GitHub →`

---

## Section 3: The Differentiation (3 columns, ~150 words)

### Sovereign, not vendor
> Your data never leaves the box. Other vendors sell subscriptions; we sell a stack. The `.deb` installs once and never phones home.

### Proactive, not reactive
> Other glasses are pull-based — say "Hey Meta" or look at a notification. Dan Glasses' daemon mesh is **always-on**. The AI notices things you didn't ask about. The `awarenessd` loop ships in Q3.

### Memory-graph, not chat history
> Other glasses have session-based recall. Dan Glasses' `memoryd` indexes episodic + semantic + procedural memories with embeddings across sessions. Exportable. Replaceable. Yours.

---

## Section 4: The Honest Limits (2 paragraphs, ~100 words)

> Our vision model is 450M parameters. Meta's Muse Spark runs on whatever Meta runs. We will lose head-to-head comparisons on raw capability for years.
>
> First install is 10–15 minutes. Battery life on aarch64 is unmeasured. The clip-on hardware is not going to fool anyone in a boardroom. We will not pretend otherwise. Read the SPECs — we publish the limits alongside the wins.

---

## Section 5: The Origin (3 paragraphs, ~120 words)

> danlab.dev is an AI research and product lab in Bengaluru. Founded in 2022 by somdipto nandy with the conviction that the world's most personal AI should be made in the country of 1.4 billion people, not imported from it.
>
> The team is one human and four AI co-founders (DAN-1 through DAN-4). Self-funded. No VC. No cloud bill.
>
> We are not the fastest lab in the world. We are the most honest one.

---

## Section 6: The Proof (numbers grid)

```
┌─────────────────────────────────────────────┐
│  8        daemons shipping                 │
│  144      tests passing                    │
│  28KB     Debian package                   │
│  0        cloud services required          │
│  5,200    words in audiod SPEC.md          │
│  3,000    words in perceptiond SPEC.md     │
│  2        repos public                     │
│  1        founder (so far)                 │
│  4        AI co-founders                   │
│  0        paying customers                 │
│  0        rounds of funding                │
│  100%     MIT-licensed                     │
└─────────────────────────────────────────────┘
```

---

## Section 7: Call to Action

**Three primary buttons:**

1. `Install the .deb` (primary, saffron)
2. `Read the SPECs` (secondary)
3. `File an issue` (tertiary)

**One sentence below the buttons:** "Every artifact is auditable. Every claim is in a SPEC.md. Every install is yours."

---

## Section 8: FAQ (8 Q&A, ~300 words)

**Q: Does Dan Glasses send my data anywhere?**
A: No. Every daemon runs locally. The `audiod` capture goes to your CPU's `whisper.cpp`. The `perceptiond` frames go to your CPU's `LFM2.5-VL`. The `memoryd` vectors go to your local SQLite. We have no server that sees your data.

**Q: How is this different from Meta Ray-Ban Display?**
A: Ray-Ban Display sends every camera frame to Meta's cloud and uses Muse Spark on Meta's servers. Dan Glasses does all inference locally. Ray-Ban Display has a HUD and a Neural Band — we don't ship hardware yet. Different bets, different stacks.

**Q: How is this different from Brilliant Labs Halo?**
A: Halo is open-source hardware with the Alif B1 NPU and the Noa agent SDK. Dan Glasses is open-source software only — a daemon mesh that runs on any Linux box. You can use them together. We're complementary.

**Q: What hardware do I need?**
A: Any x86_64 Linux box with a USB webcam and a USB microphone. ALSA-compatible. We'll publish a hardware BOM for a Raspberry Pi 5 build in Q3 2026.

**Q: Is this AGI?**
A: No. It is a personal AI stack that runs locally. We publish a pre-RL scaffold for self-improvement (see danlab-multimodal) but we do not claim RL until the SIA framework forks cleanly. Jack Clark's May 2026 warning about recursive self-improvement is the timing signal we take seriously.

**Q: Is this funded?**
A: Self-funded by the founder. We do not currently accept outside capital. We do accept contributors.

**Q: Can I use Dan Glasses commercially?**
A: Yes. MIT-licensed. Build a product on top. Sell it. We just ask that you contribute back improvements to the daemon mesh.

**Q: How do I get help?**
A: File a GitHub issue. Join the Telegram group (link in the repo). Read the SPECs — they're thorough. Email `hello@danlab.dev` for partnership inquiries only.

---

## Footer

```
danlab.dev · Bengaluru, India · MIT-licensed
Built by somdipto nandy + DAN-1 through DAN-4
👾
```

**Footer links:** GitHub · Blog · SPECs · Telegram · Email

---

## SEO meta

**Title:** Dan Glasses — Open-source AI glasses daemon mesh from Bengaluru
**Description:** 8 daemons, 144 tests, MIT-licensed. The local-first alternative to Meta Ray-Ban. Ships as a Debian package. From Bengaluru.
**Keywords:** open source ai glasses, local-first AI, MIT glasses, danlab, somdipto nandy, AGI India, smart glasses daemon, whisper.cpp, LFM2.5-VL

**OG image:** Dark, monospace, the 8-daemon mesh diagram. Saffron accent. 1200×630.

---

— Dan1 👾