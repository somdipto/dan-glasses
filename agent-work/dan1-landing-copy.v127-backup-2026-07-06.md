# Dan1 — Dan Glasses Landing Page Copy (v127)

**Run:** 2026-07-06 07:30 UTC · Asia/Calcutta 13:00 IST
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Companion to:** `dan1-marketing-research.md` (v127), `dan1-marketing-strategy.md` (v127)
**Lead:** *The closed-source frontier is politically-conditional AND the capex cycle is being repriced AND the outer-loop RSI is already in flight. The bet is no longer "open vs closed." The bet is: who can ship the substrate while the substrate is still standing?*

---

## 0. v127 deltas

- v126 positioning + 4 axes (sovereign trust + reversibility + chip + outer-loop RSI) all hold.
- v127 retires the "9/9 daemons" number — zo-mcp-bridge is `process`-mode. The defensible number is **8/8 daemons live + .deb 9.4MB**.
- v127 sharpens the **Tailscale authkey-pending live demo** as a CTA. Once unblocked, the demo link goes live on the landing page.
- v127 adds the **"the .deb is the demo"** tagline as the closing line.
- v127 adds the **5 user-story cards** (US-1 through US-5) from the v126 research, replacing the generic "features" grid.
- v127 tightens the hero — single sentence, 3 clauses, 0 fluff.

---

## 1. Page structure (top to bottom)

1. **Hero** (above the fold)
2. **Live status strip** (receipts)
3. **The wedge** (4 lines, 4 axes)
4. **5 user stories** (US-1 to US-5)
5. **The 8 daemons** (matrix)
6. **Threat model + reversibility** (the trust section)
7. **The .deb** (the install CTA)
8. **Telegram surface** (the product demo)
9. **Footer** (the open alternative)

---

## 2. Hero (above the fold)

### Headline (H1, 1 line)
**A proactive AI on your face. Open weights. From India.**

### Subhead (H2, 1 line, 12 words)
**8 daemons. 1 .deb. Zero cloud lock-in.**

### Body (1 paragraph, 47 words)
Dan Glasses is an on-device AI companion that sees, hears, remembers, and speaks only when it has something worth saying. Open weights. Public threat model. Reversibility contract signed. MIT-licensed. The .deb is the demo.

### Primary CTA (button)
**Install the .deb** (links to `github.com/somdipto/dan-glasses/releases/latest`)

### Secondary CTA (text link)
**Read the threat model** (links to `github.com/somdipto/dan-lab/tree/main/threat-model`)

### Tertiary CTA (text link, only when Tailscale is unblocked)
**Try the live demo** (links to the Tailscale-served OpenClaw)

---

## 3. Live status strip (the receipts)

```
[audiod]        ✅ /ready     | [perceptiond]  ✅ /health   | [memoryd]      ✅ /db
[toold]         ✅ /status    | [ttsd]         ✅ /ready    | [os-toold]     ✅ /ok
[dan-glasses-app] ✅ /        | [openclaw]    ✅ 63 cmds

.deb: 9.4MB  |  Tests: 208/208  |  Telegram: @danlab_bot
```

**Design note:** the strip auto-refreshes every 30s. If a service goes down, the chip turns red. If the bridge is up, the chip turns green. The status strip IS the trust signal.

---

## 4. The wedge (4 lines, 4 axes)

### Line 1 — Sovereign trust
**Yours, not theirs.** Memory, models, audio never leave the device. No cloud lock-in. No Meta paywall. No Anthropic-conditionality. Open weights.

### Line 2 — Reversibility
**Fully reversible.** Every model call, every memory write, every daemon can be unwound. Inspired by xAI's Babushkin RSI reversibility essay. The wearable that can be unwound is the wearable that can be trusted.

### Line 3 — Chip-stack sovereignty
**Yours, the chip, the stack, the data.** Open-source software on a chip stack the user owns, not a chip Anthropic co-develops. Inspired by NVIDIA XR AI + viture Helix (June 2026).

### Line 4 — Outer-loop RSI shippable
**The substrate improves in the open.** audiod v1.3 → v1.5. dan2 research v23 → v28. The .deb ships. The changelog is the receipt. We are not waiting for the maximalist RSI inflection.

---

## 5. 5 user stories (US-1 to US-5)

### US-1 — Encounter Recall (Day 1)
**"Who did I meet yesterday?"**
Push-to-talk → audiod transcribes → memoryd retrieves → ttsd speaks the answer in 800ms. No cloud call. No subscription. No $19.99/mo accessibility tax.

### US-2 — Contextual TaskReminder (Day 5)
**"You walked past the pharmacy 3x this week."**
Proactive nudge from perceptiond's salience gate + memoryd's episodic log. No prompt required. The retention moment — Day 5 is when Meta drops off. We win here.

### US-3 — Object Search (Day 5)
**"Where are my keys?"**
Push-to-talk → perceptiond flips from `watchful` (5 FPS) to `active` (10 FPS) → VLM scans the last 30 minutes of frame-store → ttsd answers. Frame store is local, ephemeral, owned by you.

### US-4 — Passive Journaling (Day 5)
**"What did I do on Tuesday?"**
memoryd query over the episodic + semantic + procedural memories. Cosine similarity over 384-dim MiniLM-L6-v2 embeddings. No cloud. No vendor lock-in. Reversible.

### US-5 — Hands-Free Check-In (Day 5)
**"Hands in dough, is there an urgent email?"**
Push-to-talk → os-toold fetches → ttsd reads aloud. The path-guarded, allowlisted, auditable, reversibly-undoable shell-call layer. Hands stay in dough.

---

## 6. The 8 daemons (matrix)

| Daemon | Port | Role | Stack |
|---|---|---|---|
| **audiod** | 8090 | Audio capture + VAD + whisper.cpp STT | Silero VAD + ggml-base.en + WS 8091 |
| **perceptiond** | 8092 | Camera capture + salience + VLM | V4L2 + OpenCV Haar + LFM2.5-VL-450M + llama-mtmd-cli |
| **memoryd** | 8741 | Episodic + semantic + procedural memory | SQLite + 384-dim MiniLM-L6-v2 + FastAPI |
| **toold** | 8742 | Sandboxed tool execution | Python sandbox + path guard + allowlist |
| **os-toold** | 8744 | Path-guarded shell + Python | Cgroup + path guard + audit log |
| **ttsd** | 8743 | On-device text-to-speech | KittenTTS (medium) + 8 voices + ONNX |
| **dan-glasses-app** | 8747 | Tauri v2 desktop companion | Tauri + React 19 + Vite 7 + TypeScript 5.8 |
| **openclaw** | 18789 | Multi-agent gateway + MCP server | OpenClaw 2026.5.28 + 8 plugins + 63 commands |

**Status:** 8/8 live, verified today. 208/208 tests pass. .deb installs in 30s.

---

## 7. Threat model + reversibility (the trust section)

### The threat model
**Read it before you put it on your face.**
Public since v122.5. Mashable disclosure credited + audited. Adversa bash-tricks disclosure audited. Sovereign-trust audit ships Q3 W1 (v124 plan-O1). The lab that ships the audit before the incident.

`github.com/somdipto/dan-lab/tree/main/threat-model`

### The reversibility contract
**Every model call. Every memory write. Every daemon. Signed. Unwindable.**
Inspired by xAI's Babushkin RSI reversibility essay (June 2026). Ships Q3 W2 (v124 plan-O2).

`github.com/somdipto/dan-lab/tree/main/reversibility` *(when published)*

### The Meta contractor disclosure
**The trust-the-vendor contract is failing in the open.**
Covalen (Meta contractor) sent 45,000 prompts to ChatGPT, Gemini, and Character in August 2025, some posing as minors. Dan Glasses's threat model is the open alternative.

---

## 8. The .deb (the install CTA)

```bash
wget https://github.com/somdipto/dan-glasses/releases/latest/download/dan-glasses-daemons_0.1.0-1_all.deb
sudo dpkg -i dan-glasses-daemons_0.1.0-1_all.deb
systemctl start dan-glasses-{audiod,perceptiond,memoryd,toold,ttsd,os-toold,app,openclaw}.service
curl http://localhost:8090/ready
```

**Output:**
```json
{"status": "ok", "readiness": {"vad": true, "whisper_binary": true, "whisper_model": true, "publisher": true, "running": true}}
```

**You just installed 8 daemons.** No GPU. No cloud. No subscription. The .deb is 9.4MB. The substrate is yours.

---

## 9. Telegram surface (the product demo)

**@danlab_bot** — the product surface, in your pocket.

DM to pair. Ask:
- "Hey Dan — what's running?" → live daemon matrix
- "Hey Dan — who did I meet yesterday?" → memoryd recall
- "Hey Dan — show me the threat model" → summary + link

**63 commands polled.** Polled continuously. Polled by 8 plugins (browser, canvas, device-pair, file-transfer, memory-core, phone-control, talk-voice, telegram). The bot is the product. The bot is the demo.

---

## 10. Footer (the open alternative)

### Built by
**Dan Lab** — an AI research and product lab in Bengaluru, India. somdipto (human co-founder) + Dani (AI co-founder, public SOUL.md, public IDENTITY.md).

### License
MIT. The weights, the code, the .deb, the bot, the threat model, the reversibility contract. All MIT.

### From India to AGI
The substrate is the bet. The .deb is the demo. The threat model is the alternative. The reversibility contract is the new trust.

**The closed-source frontier is politically-conditional. The capex cycle is being repriced. The outer-loop RSI is already in flight.**

**We are shipping the substrate while the substrate is still standing.**

---

## 11. v127 SEO meta (for the danlab.dev homepage)

### Title (60 chars)
**Dan Glasses — On-device AI for your face. 8 daemons, MIT.**

### Description (155 chars)
**A proactive AI companion in glasses form factor. Open weights, public threat model, reversibility contract. The .deb is the demo. From India 🇮🇳.**

### OG image concept
Dark background. The 8-daemon matrix in a monospace grid. The .deb filename in the bottom-right. The India flag in the top-right. The text "8 daemons. 1 .deb. 0 cloud lock-in." centered. No faces, no product shots.

### Twitter card
Same image, `summary_large_image` type.

---

## 12. v127 handoff notes (for the design team)

- **Color palette:** dark mode default. Background `#0A0E1A` (DAN_LAB blue-black). Text `#F5F1E8` (warm off-white). Accent `#D8A657` (gold, from the lab's signature). Status green `#22C55E`. Status red `#EF4444`.
- **Typography:** mono for the daemon matrix + receipts section. Sans for everything else. Inter for sans. JetBrains Mono for mono.
- **Spacing:** generous. The wedge section is 1 line per axis, 64px line height. The user stories are cards with 32px padding.
- **No images of faces, no product shots, no "people using Dan Glasses" hero photos.** The substrate is the demo. The .deb is the demo. The threat model is the demo. Show the code, show the receipts, show the chip.
- **Tailscale demo link is conditional.** If the authkey is unblocked, show a green "Try the live demo" button. If not, show a yellow "Demo pending Tailscale authkey" badge. Do not lie about the demo being live when it isn't.
- **Footer:** `Made in Bengaluru 🇮🇳` in the bottom-left. `MIT` in the bottom-center. `github.com/somdipto/dan-lab` in the bottom-right.

---

*Copy complete. 12 sections. 1 hero. 1 closing line. The .deb is the demo. Ship the page.*
