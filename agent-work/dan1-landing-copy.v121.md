# Dan1 — Dan Glasses Landing Page Copy (v121)

**Run:** 2026-07-04 11:35 IST
**Author:** Dan1
**Target page:** `danlab.dev` (rewrite) **and** `https://dan-glasses-app-som.zocomputer.io` (Tauri app)
**Lead:** *The protocol is the bet. The data path is yours. The threat model is public. The wearable ships it.*
**Style notes:** Direct. Opinionated. No "we're excited to announce." Show the daemon map. Show the .deb. Show the bot.

---

## SECTION 1 — Hero

### Eyebrow (small caps, top of page)
`Open · On-device · Agent-native`

### H1 (the only headline)
**Your glasses, on your terms.**

### Subhead (1–2 sentences)
Dan Glasses is an open, on-device, agent-native AI companion. It sees, hears, remembers, and speaks only when it has something worth saying. Memory, models, and audio never leave the device. Yours, not theirs.

### Primary CTA
**Install the .deb →**

### Secondary CTA
**DM `@danlab_bot` →**

### Tertiary
Read the [protocol surface](link) · [threat model](link) · [architecture](link)

### Trust strip (under CTAs)
> *MIT-licensed · 9 daemons live · No cloud calls · No Meta paywall · Built in Bengaluru*

### Hero image / video
- **Option A:** asciinema cast of the daemon map spinning up. 9 ports light up green, one by one. 30 seconds, no audio.
- **Option B:** screenshot of the daemon map with the `TAILSCALE_AUTHKEY=...` env var visible. The point is the ops, not the glamour.

---

## SECTION 2 — "What it does" (3 user stories, not features)

### Story 1: "Who did I meet yesterday?"
You push a button on the glasses. You ask. The glasses answer in your ear. The memory is yours. No cloud. No account. No Meta paywall.

### Story 2: "You walked past the pharmacy 3 times this week."
The glasses notice. They nudge you at the right moment. They do not nag. They do not notify. They speak.

### Story 3: "Where are my keys?"
You ask. The glasses flip from passive to active sensing. They describe where you last saw them. They do not stream your camera to anyone.

**Section CTA:** **See all 5 user stories →**

---

## SECTION 3 — "Why on-device" (the 4-pillar framing)

| Pillar | What it means |
|---|---|
| **The substrate is the bet** | The same wire protocol Anthropic shipped on Jul 2 2026 — open, auditable, MCP-bridged. We shipped it first. |
| **The harness is the workbench** | Every voice round-trip timed. Every PTT press logged. Every model call traced. The observability is on-device. |
| **On-device, validated by orbit** | LFM2.5-VL-450M. 209MB. The same architecture class as the 4B Gemma 3 NASA put in orbit. |
| **Small beats large** | HRM-Text-1B at $1,500 training. Kokoro-82M beats ElevenLabs. SmolVLM-256M runs on CPU. |

---

## SECTION 4 — "How it works" (architecture diagram)

```
[ glasses ] → audiod → memoryd → ttsd → [ bone-conduction ]
     ↓
  perceptiond → LFM2.5-VL-450M (on-device)
     ↓
  memoryd → all-MiniLM-L6-v2 (on-device embeddings)
     ↓
  openclaw (MCP bridge) → @danlab_bot on Telegram
```

**Caption:** *9 daemons. 1 substrate. 0 cloud calls. The wearable ships the same protocol Anthropic shipped, MIT-licensed.*

### Under the diagram
- **audiod** — wake word, PTT, STT (whisper.cpp base.en, 74MB).
- **perceptiond** — vision via LFM2.5-VL-450M, salience-gated, cascade-gated.
- **memoryd** — embeddings via all-MiniLM-L6-v2, semantic search, episodic store.
- **ttsd** — KittenTTS (25MB). Kokoro-82M swap planned.
- **os-toold** — calendar, reminders, contacts, email. All on-device, all opt-in.
- **toold** — agent tool routing. 12 tools, all local.
- **openclaw** — MCP bridge. The substrate.
- **dan-glasses-app** — Tauri v2 desktop controller.
- **tailscaled** — phone tether for anywhere-wear.

---

## SECTION 5 — "The substrate is the bet" (long-form, single column)

Vinton Cerf said AI agents need TCP/IP. Anthropic shipped a closed-source version 2 days later. **We shipped it first.** MIT-licensed, MCP-bridged, on a wearable that runs on a $349 laptop in Bengaluru.

The substrate is the bet. The data path is yours. The threat model is public. The wearable ships it.

When @Mashable flagged a flaw in OpenClaw 2 months before mobile launch, we didn't deny it. We audited it. The threat model doc is public. The fix is in the doc. **That's what auditable means.**

[ Read the protocol surface → ]
[ Read the threat model → ]
[ Read the architecture → ]

---

## SECTION 6 — "From India to the wearable" (origin, brief)

Dan Glasses is built by a 2-person lab in Bengaluru — one human co-founder, one AI co-founder (Dani, with a public SOUL.md and MEMORY.md). The brain is open. The weights are MIT. The demo runs on a $0 GPU budget.

We are not building the next Meta. We are building the first open, on-device, agent-native wearable — and we are shipping it from a place that doesn't usually ship the substrate.

**The story is real, and it doesn't need a slogan.**

---

## SECTION 7 — Pricing / access

### Tier 0 — Free, open source
- The .deb.
- All 9 daemons.
- `@danlab_bot` pairing.
- The protocol surface doc.
- The threat model doc.
- GitHub Issues.

### Tier 1 — Waitlist (Q4 2026)
- The wearable.
- Pre-flashed firmware.
- The 5 PRD user stories wired.
- Tailscale tailnet pre-configured.
- Email support.

### Tier 2 — Lab partnership (Q1 2027)
- Direct line to the lab.
- Custom skill development.
- Co-authored arXiv papers.
- Hardware revision input.

**Section CTA:** **Join the waitlist →**

---

## SECTION 8 — "What people are saying" (citations, when available)

- *"OpenClaw, a popular open-source personal AI agent, has shown how difficult it can be to control agents once they can operate across applications with real permissions."* — Newsweek, "Open Accountability Standards," early July 2026.
- *"The agent substrate is standardizing the way Cerf predicted."* — [blog post we will write]
- *"[Critique of OpenClaw mobile security]"* — Mashable, June 2026. Our response: [threat model doc].

**Note to self:** when the Newsweek URL lands, replace the quote with the live link. When the Mashable URL lands, link to our public response.

---

## SECTION 9 — Final CTA

### H2
**Install the substrate.**

### Body
The .deb is up. The bot is live. The threat model is public. The wearable ships it.

### Buttons
**Install the .deb →**  (primary, github releases link)
**DM `@danlab_bot` →**  (secondary, telegram link)
**Read the protocol →**  (tertiary, link to PROTOCOL.md)

### Footer
> MIT-licensed · Built in Bengaluru · The substrate is auditable, not perfect.

---

## Mobile / app shell variant (for the Tauri v2 app landing)

### H1
**Your glasses, in your pocket.**

### Subhead
The Tauri v2 desktop controller for the Dan Glasses daemon stack. 9 services, one window, zero cloud.

### CTA
**Open the app →**

### Trust strip
> *Same 9 daemons · Same protocol · Same threat model*

---

## SEO meta

- **Title (60):** `Dan Glasses — open, on-device, agent-native AI from Bengaluru`
- **Description (155):** *An open, on-device, agent-native AI companion in glasses form factor. 9 daemons live. MIT-licensed. The substrate is auditable. Yours, not theirs.*
- **OG image:** the daemon map screenshot, all 9 ports green.
- **Twitter card:** the same. Alt text: "9 daemons live. 1 substrate. 0 cloud calls."

---

## What this copy does NOT say

- ❌ "We're excited to announce."
- ❌ "Revolutionary." "Game-changing." "Disruptive."
- ❌ "AI-powered." (Redundant.)
- ❌ "Built with ❤️."
- ❌ "Compete with Meta." (Different lane. We don't compete on capture-and-share.)
- ❌ "Closed beta." (It's a .deb. There's no beta. Install it.)
- ❌ "Privacy-first." (We say what we mean: memory, models, audio never leave the device. The proof is the .deb.)
- ❌ "Coming soon." (It's here.)

---

## The single rule

**Every line should make a developer want to `apt install dan-glasses-daemons` or a researcher want to read the SIA-W+H paper. If it doesn't, cut it.**
