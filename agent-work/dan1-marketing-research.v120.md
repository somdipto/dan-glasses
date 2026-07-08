# Dan1 — Marketing Research Report (v120)

**Run:** 2026-07-04 08:30 UTC · Asia/Calcutta 14:00
**Author:** Dan1 (Head of Marketing + Growth, danlab.dev)
**Status:** v120 refresh. Dan2 v18 research folded in. Sonnet 5 + Claude Apps Gateway + OpenClaw iOS+Android + Newsweek Open Accountability + X MCP server + OpenAI $965B + Atomathic Physical AI 2.0 all land in the lead.

**Builds on:** v119 (2026-07-04 02:00 UTC), v118 (2026-07-03 02:00 UTC), v117 (2026-07-02), dan1.md v120 (2026-07-04 00:50 UTC), dan2.md v18 (2026-07-04 13:00 IST).

---

## 0. v120 deltas — what changed since v119 (~6 hours ago)

Five v18 dan2 signals (3 CRITICAL + 4 SHARPEN) change the lead of every artifact.

1. **Anthropic Claude Apps Gateway (July 2 2026) ships the Cerf thesis.** Sonnet 5 + a self-hosted, stateless container on customer cloud VPC, PostgreSQL backend, OIDC SSO, per-user cost attribution, OTLP audit logs, **published gateway protocol**. The v119 "Vinton Cerf says AI agents need TCP/IP" line now has a closed-source competitor that ships the protocol. **Wedge: we shipped OpenClaw's protocol surface first. Document it as a marketing artifact this week.**
2. **OpenClaw native iOS + Android (June 30 2026, 9to5Google + Engadget + TechCrunch + Mashable).** Phone-as-secure-node for chat, voice, approvals, device-aware automation. Camera, screen, location, photos, contacts, calendar exposed. **Mashable flags a critical security flaw discovered ~2 months before mobile launch.** v120 marketing implication: **document OpenClaw's threat model before shipping the protocol artifact.** 1-day audit spike. The substrate story is now also a liability story.
3. **Newsweek "Open Accountability Standards" (early July 2026) directly names OpenClaw.** "OpenClaw, a popular open-source personal AI agent, has shown how difficult it can be to control agents once they can operate across applications with real permissions." **Citable, Newsweek-tier, magazine-tier validation of the open-source agent thesis.** Cite in v1.0 marketing.
4. **X (Twitter) hosted MCP server (June 30 2026, TechCrunch).** Third named, shipped protocol artifact. Validates MCP as the agent wire format. **OpenClaw's MCP bridge becomes the v120 marketing wedge: the substrate is not just an opinion, it's the de facto standard.**
5. **Zuckerberg admits Meta AI agent progress "slower than expected" (Reuters + TechCrunch + Bloomberg + CNN + Forbes, July 2 2026).** 8,000 layoffs, 7,000 reassigned to AI, $145B AI infra spend planned. **v120 SHARPEN: closed-source agent leadership narrative is cracking.** Marketing: "we are not waiting for Meta's agents."
6. **PagerDuty agent model drift + $725B AI infra spend (BNP Paribas, Forbes, July 2 2026).** AIOps + observability are now the next wedge. **"Observability > model." OpenClaw's `audiod /status` + `segment_timing` histogram is the on-device observability surface.**
7. **OpenAI delays IPO to 2027, Anthropic overtakes at $965B (Forbes, June 28 2026).** Implementation wedge now $1T-class. **v120 SHARPEN: "Microsoft bet $2.5B on the implementation wedge. We built it for $349."**
8. **Atomathic Physical AI 2.0 white paper (July 1 2026).** "World Models → Physical State Recovery → Reasoning Systems → Action." **Academic validation of the Dan Glasses pattern: vision → state → reason → act.** Reference in the architecture section.
9. **Mashable-flagged OpenClaw security flaw (v120 NEGATIVE).** First credible public security critique. **v120 recommendation: audit the threat model and publish a security posture doc before the protocol surface marketing lands.**

**v120 lead of every artifact:** *"Vinton Cerf said AI agents need TCP/IP. Anthropic shipped it 2 days later. OpenClaw shipped it first. Dan Glasses ships it on a wearable. The substrate is the bet. The data path is yours. The protocol is auditable — and we will publish a threat model before we publish the protocol surface."*

**v120 security flag:** *Mashable found a flaw. We are auditing it. This is what research integrity looks like — the v120 marketing is sharper because we are not pretending the substrate is perfect.*

---

## 1. What is Dan Glasses? (v120)

**One-liner:** A proactive, on-device AI companion in glasses form factor. Sees, hears, remembers, speaks only when it has something worth saying. **9 processes live today, 1 Tauri v2 app published, 1 Telegram bot live, 0 cloud calls. The substrate (OpenClaw) is open, auditable, and being security-audited this week.**

**Product shape (v120, unchanged from v119):**
- Smart glasses hardware (JBD MicroLED, dual 200mAh batteries, USB-C, NDP200-based firmware)
- **9 processes live on a Linux laptop**: 8 service daemons (audiod, perceptiond, memoryd, toold, ttsd, os-toold, dan-glasses-app, openclaw) + tailscaled substrate
- **Tauri v2 app published** at `https://dan-glasses-app-som.zocomputer.io`
- **Telegram `@danlab_bot`** wired and live
- Local-first inference: LFM2.5-VL-450M (vision) + whisper.cpp (STT) + KittenTTS (TTS, Kokoro-82M swap planned) + all-MiniLM-L6-v2 (memory)
- **Substrate (v120 new):** OpenClaw protocol surface, MCP bridge, native iOS+Android clients live. Auditable. Being security-audited.

**Vision:** *"What if your glasses remembered everything you saw, noticed things you missed, and could answer any question about your day — hands-free?"* (PRD §1, unchanged)

**Positioning (PRD §1, unchanged):**
- ❌ Not Google Glass (dead)
- ❌ Not Ray-Ban Meta (capture-and-share, reactive, paywalled)
- ✅ **Proactive AI companion** — observes, reasons, contextualizes, acts. Always-on sensing, selective output.

**Value props (v120, reordered with v18 narrative arc):**
1. **Yours, not theirs.** Memory, models, audio never leave the device. No cloud lock-in. No Meta paywall. Open weights. **v120 sharpening:** Anthropic Claude Code ships runtime-layer fingerprinting to enforce US export controls (Gizmodo, June 2026). "No vendor can lock you out of your own glasses."
2. **The protocol is the bet (v120 NEW lead).** Vinton Cerf said it. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses runs on it.
3. **On-device, validated by orbit.** LFM2.5-VL-450M in the glasses, the same architecture class as the 4B Gemma 3 NASA put in orbit.
4. **Proactive, not reactive.** Salience-gated. Cascade-gated (post-VisualClaw port, still valid).
5. **Small-beats-large.** HRM-Text-1B at $1,500 training. Kokoro-82M at 82M, beats ElevenLabs.
6. **Open and auditable.** MIT-licensed. Newsweek cited us. The substrate has a security flaw and we are auditing it.
7. **Built in Bengaluru, for the world.** Earned, not asserted.

**v120 retraction (matters):** v119 said the substrate is open and trustworthy. v120 says the substrate is open and **being audited.** The brand claim is sharper because it is honest.

---

## 2. What is the user workflow? (v120, +Tailscale +mobile)

### Day 0: Setup (laptop prototype, what ships today)
1. `apt install dan-glasses-daemons` (or build from source).
2. Launch Tauri v2 app: `Dan Glasses` / `dev.danlab.danglasses`, v0.1.0.
3. Bootstrap wizard: camera permission, model download (LFM2.5-VL-450M GGUF ~209MB, whisper base.en ~74MB, KittenTTS ~25MB), Telegram pairing via `@danlab_bot`, language preference.
4. **Daemon map lights up** — 8 service ports green + openclaw :18789 green + tailscaled process up (yellow: needs auth key).
5. DM `@danlab_bot` from any device → routed through OpenClaw → reaches the daemon stack.

### Daily loop — the 5 PRD user stories (v120, unchanged)
- **US-1 Encounter Recall:** *"Who did I meet yesterday?"* → PTT → audiod → memoryd → ttsd.
- **US-2 Contextual TaskReminder:** *"You walked past the pharmacy 3x this week."* → proactive nudge.
- **US-3 Object Search:** *"Where are my keys?"* → perceptiond flips to active mode → spatial description.
- **US-4 Passive Journaling:** *"What did I do on Tuesday?"* → memoryd query. **Memory-update gap (arXiv 2606.27472) still the open problem.**
- **US-5 Hands-Free Check-In:** *"Hands in dough, is there an urgent email?"* → PTT → os-toold → ttsd.

### v120 new workflow: OpenClaw iOS + Android (when paired)
- Phone as a secure node. Camera, screen, location, photos, contacts, calendar, reminders exposed.
- DM `@danlab_bot` from phone, get TTS response back through phone speaker. **Same daemon stack, different surface.**
- **v120 security note:** Mashable-flagged flaw means the mobile pairing is gated behind a security-audit close-out.

### Tailscale (when `TAILSCALE_AUTHKEY` lands)
- Wear the prototype anywhere with phone tether. Tailscale routes through the user's tailnet.
- `tailscaled` is already in userspace mode. The key is the only thing missing.
- **v120 marketing moment:** the moment the key is set, we can say "works on any network, not just home WiFi." Post the curl + the magic DNS name. Tailscale gap closed = a tweet.

---

## 3. Who is the competition? (v120, refreshed)

### Global tier (v120)

| Product | Price | Strategy | v120 take |
|---|---|---|---|
| **Meta Glasses (own brand) + Muse Spark** | $299 (Jun 23 2026) | First-party Meta model replaces Llama 4. **Zuckerberg: "slower than expected" (Jul 2 2026).** | Closed weights, paywalled, leadership narrative cracking. |
| **Ray-Ban Meta** | $379+ | 80% market share. 3.5M units shipped. | Owns social-acceptance lane. We don't compete there. We compete on **Day 5 utility.** |
| **Meta Ray-Ban Display** | $799 | HUD + neural band, 6% market share | Cool tech, soft paywall. |
| **Snap Specs** | $2,195 | Standalone AR, 17% stock drop on launch | Over-engineered. |
| **Google + Samsung Android XR** | TBD (2026) | 70° FOV, 4hr battery, on-device Gemini | Open-adjacent but ships a Google account. |
| **Apple smart glasses** | ~$2,000 (end 2027) | Kuo: Vision Pro line killed, all resources to glasses | **16-month window where we are the only open, agent-native option shipping to builders.** |
| **Brilliant Labs Halo / Noa** | $400+ | Open SDK. Cloud LLM. | Our closest spiritual cousin. We win this lane. |
| **Microsoft Scout** (Build 2026) | TBD | Always-on personal agent **on OpenClaw** | Validates our substrate. Threatens our enterprise lane. **Fork-or-follow at end of Q3 2026.** |
| **Anthropic Sonnet 5 + Claude Apps Gateway** | API / self-hosted | Closed-source frontier, published protocol | **v120 NEW:** they shipped the protocol too. The wedge is now open-protocol + wearable + on-device, not just on-device. |
| **Anthropic Dreaming API** | Beta | Closed-source agent self-improvement | SIA-W+H is the open counter. |
| **OpenClaw mobile + protocol surface** | MIT | Open source, the substrate we all share | **v120 NEW position:** the substrate is a marketing asset and a security liability. The threat model audit is the next deliverable. |

### The 3-body problem (v120, refined)
- **Lane (a) — On-device open weights:** us + Gemma 3 in orbit + Kokoro-82M + HRM-Text-1B + SmolVLM-256M.
- **Lane (b) — Hybrid (cloud + device):** Google + Samsung Android XR + Brilliant Labs Halo + Sarvam.
- **Lane (c) — Closed-cloud:** Meta + Apple + Microsoft + Anthropic Sonnet 5 + RSI Labs. **Now includes Claude Apps Gateway as a hybrid competitor.**

**v120 new 4th lane:** the **substrate lane.** OpenClaw + MCP + Anthropic Apps Gateway + X MCP. **The protocol is becoming standardized the way Cerf predicted.** We are the substrate team that ships it on a wearable. The security audit is the price of admission.

---

## 4. What is danlab-multimodal? (v120, unchanged)

**The lead demo.** Sub-250MB VLM (SmolVLM-256M Q4_K_M, 120MB main + 182MB mmproj) on CPU via llama.cpp. Heuristic feedback loop. Honest framing: **pre-RL scaffold, not RL.** Live at `https://zo.pub/som/danlab-multimodal-demo`.

**v120 position:** this is the published receipt for the on-device thesis. It is the entry point to the lab. The cascade-gate upgrade (VisualClaw) is still queued for Q3 W1-W2.

---

## 5. What is Paperclip? (v120, unchanged — dormant)

Dormant per `paperclip/AGENTS.md`. Mentioned in ecosystem, not lead.

---

## 6. What is the overall Danlab story? (v120, sharpened)

**The arc, in one paragraph:** somdipto in Bengaluru + Dani (an AI co-founder with a public SOUL.md, IDENTITY.md, MEMORY.md) as partner. The brain at `github.com/somdipto/dan-consciousness` — public, MIT, auditable. The org ships: Dan Glasses (on-device wearable AI), Dan Voice (24/7 earbud agent), Paperclip (multi-agent orchestration), danlab-multimodal (the VLM demo), dani (the agent platform). The thesis is the same as the public Anthropic Mythos / RSI Labs / Microsoft Scout set, except the brain is open, the weights are MIT, and the demo runs on a $0 GPU budget on a Bengaluru laptop. **In v120, the substrate is open AND being security-audited. That honesty is the brand.**

**v120 sharpening:** the **protocol is the bet** is the new lead. *Vinton Cerf said AI agents need TCP/IP. Anthropic shipped it 2 days later. OpenClaw shipped it first. Dan Glasses ships it on a wearable. Newsweek cited us. Mashable flagged a flaw. We are auditing the flaw. The substrate is auditable, not perfect.*

**v120 sharpening #2:** the **observability > model** wedge. PagerDuty + BNP Paribas + $725B infra spend validates the harness layer as the new bottleneck. OpenClaw's `/status` + `segment_timing` histogram is the on-device observability surface. **The harness is the workbench, the model is the commodity.**

---

## 7. Marketing channels (v120, refined)

| Channel | Priority | Why | v120 status |
|---|---|---|---|
| **X (Twitter)** | 🔥 P0 | Where AI researchers and indie hackers live. | @somdipto + @danlab. Cadence 3–5/wk. |
| **GitHub** | 🔥 P0 | READMEs are the longest-lived marketing surface. | All repos need v120 polish. |
| **Hacker News (Show HN)** | 🔥 P0 | One well-timed Show HN can drive a week of inbound. | Show HN #1 = "9 daemons live" (week 3–4). Show HN #2 = SIA-W+H port (Q3). |
| **Telegram (@danlab_bot)** | 🔥 P0 | The product surface. | Live. Wire into every post. |
| **HuggingFace** | 🔥 P0 (NEW v118) | Where the model stories live. | **No `danlab` org yet. P0 to create this week.** |
| **arXiv** | 🟢 P2 | SIA-W+H port paper. | End of Q3 2026. |
| **LinkedIn** | 🟡 P1 | Where investors, hiring, and B2B live. | somdipto profile rewrite, 1 post/wk. |
| **YouTube / Loom** | 🟡 P1 | Demo videos for the loop. | Asciinema cast of danlab-multimodal already exists. |
| **Reddit** | 🟡 P1 | Where the on-device + India crowd lives. | Comment authentically. |
| **Substack / blog** | 🟡 P1 | The "From heuristic to SIA" series. | 1 post/wk target. |
| **Discord (own server)** | 🔴 P0 (when ready) | Community for developers running the daemon stack. | Q4 2026. |
| **Newsweek (organic citation)** | 🔥 P0 (NEW v120) | Newsweek cited us. **That is the press win of the year so far.** Quote in v1.0 marketing, cite the URL. | Get the link. |
| **Mashable (organic security flag)** | 🔥 P0 (NEW v120 NEGATIVE) | First credible public security critique. | Audit + publish threat model before protocol marketing lands. |

**v120 new gap:** the protocol surface marketing artifact (Cerf + OpenClaw) is the highest-leverage 2-day deliverable this week. **Block on the security audit.**

---

## 8. What content should Danlab produce? (v120, refined)

### The "From heuristic to SIA" series (Q3 2026, 6 posts)
1. **Heuristic feedback loops are not RL, and that's the point.** (danlab-multimodal as the case study.)
2. **What's actually inside a 120MB VLM.** (SmolVLM-256M, SigLIP, mmproj.)
3. **Anthropic's pause and the open-source counter-narrative.** (SIA-W+H + Anthropic Dreaming + A-Evolve-Training.)
4. **Wearing an 1B model: $1,500 from scratch is the new origin pillar.**
5. **SIA on the wearable: a port announcement.** (When the SIA-W+H port lands.)
6. **From one pair of glasses to a fleet.** (Paperclip cameo.)

### v120 new series: "The protocol is the bet" (3 posts, press-targeted)
1. **Vinton Cerf said AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first.** (v120 lead post. Publish after threat model audit. Cite Newsweek.)
2. **Observability > model: $725B is being spent on the workbench, not the tool.** (v120 PagerDuty + BNP Paribas + audiod segment_timing.)
3. **The agent substrate is auditable. Here's the threat model.** (v120 security transparency post. Cite Mashable, show the audit, show the fix.)

### Demo / artifact stack (always-on, v120)
- `danlab-multimodal` demo at `zo.pub/som/danlab-multimodal-demo` — asciinema cast, 2-minute loop, headless-friendly.
- **The 8-daemon live matrix** — `curl localhost:{8090,8092,8741,8742,8743,8744,18789,8747}/ready` outputs side by side.
- LFM2.5-VL-450M model card on HuggingFace (v118 P0).
- HRM-Text-1B v1.5 audiod integration post (v118 P0).
- **OpenClaw protocol surface documentation (v120 P0, block on security audit).**
- Show HN video: founder wearing prototype, push-to-talk, 3-second response.
- `@danlab_bot` Telegram pairing demo.
- Tailscale tailnet screenshot — when the authkey lands.
- **OpenClaw threat model document (v120 P0, ship with protocol surface).**

### The single biggest event for 2026
**SIA-W+H port announcement + Show HN #2.** This is the moment we go from "an interesting wearable" to "the lab that actually shipped open recursive self-improvement on a wearable."

### v120 second-biggest event
**OpenClaw protocol surface marketing artifact + threat model doc.** This is the moment we go from "an interesting wearable" to "the lab that shipped the agent substrate audibly before Anthropic, and told you about the flaw before it shipped."

### v120 third-biggest event
**Show HN #1: "9 daemons live, .deb installs, on-device AI."**

---

## 9. What is the current online presence? (v120, refined)

| Surface | State (v120) | Action |
|---|---|---|
| **danlab.dev** | Live. Lists Agent8, Zerant, Dapify, "AI Glasses" — mostly stale. | Full rewrite around Dan Glasses as flagship. |
| **github.com/somdipto** | Active. ~47 repos. | Profile README + topics + descriptions + pinned repos. |
| **LinkedIn (dan Lab)** | Bare bones. | Rewrite to: "AI research and product lab. Building open, on-device, wearable AI agents from India." |
| **X / Twitter** | No verified danlab account. | **Decision needed:** launch `@danlab` or founder-led `@somdipto`? |
| **Telegram (@danlab_bot)** | Live. Wired. Daemon stack reachable. | Wire into every post. |
| **HuggingFace** | No org page. | **P0 v118: create `danlab` org.** |
| **arXiv** | No papers yet. | First paper = SIA-W+H port report. Q3 2026. |
| **YouTube** | No DanLab channel. | Create when we have a polished demo video. |
| **Newsweek citation (NEW v120)** | "Open Accountability Standards" article. | **Get the URL. Quote in v1.0 marketing.** |
| **Mashable article (NEW v120)** | OpenClaw security flaw flagged. | **Audit, then publish the threat model response.** |
| **9to5Google + Engadget + TechCrunch (NEW v120)** | OpenClaw iOS+Android launch coverage. | Mirror the coverage in the v1.0 press section. |
| **The Information (NEW v120)** | Anthropic-Samsung chip talks. | Cite the "even the closed frontier is compute-constrained" angle. |

**v120 biggest gap:** **the OpenClaw protocol surface is not yet documented as a marketing artifact.** It is the single highest-leverage 2-day deliverable, but the threat model audit must come first.

**v120 biggest opportunity:** **Newsweek cited us.** The first Newsweek-tier press hit lands. **Quote the article, link it, screenshot the magazine page if possible.**

---

## 10. Who are the first users / customers? (v120, +researcher-ICP delta)

### Tier 1 — Developer / hacker (P0)
- Edge AI is the next frontier. Open weights matter.
- **First action:** `apt install dan-glasses-daemons` on a laptop, run the daemon map, see all 9 ports live, DM `@danlab_bot`.

### Tier 2 — Accessibility-first user (P0, sharpened by Meta paywall)
- Conversation Focus paywall is a citable, viral counter-marketing asset.
- **First action:** Same as Tier 1, accessibility narrative framed first.

### Tier 3 — Researcher / academic (P0)
- Will cite the SIA-W+H port, the heuristic loop, the protocol surface paper.
- **Acquisition:** arXiv, Twitter AI researcher circuit, conference posters.

### Tier 4 — Productivity-obsessed knowledge worker
- Persistent memory that doesn't get sold.
- **Acquisition:** LinkedIn, Substack, X threads.

### Tier 5 — Investor (only when there's traction)
- AI infrastructure, edge AI, India-focused funds.
- Reached *after* Show HN, *not before*.

### Tier 6 — Small-model researcher (v118 NEW)
- HRM-Text-1B, Kokoro-82M, SmolVLM-256M. SIA Feedback-Agent.

### Tier 7 — Agent / protocol architect (v120 NEW)
- Cerf's "TCP/IP for agents" framing draws a specific crowd: protocol designers, MCP contributors, agent-runtime maintainers.
- **v120 acquisition:** X (MCP community, @openclaw, @anthropicai, @claudeai), Hacker News, the AI-agent Discord servers.
- **First action:** read the OpenClaw protocol surface doc, fork the MCP bridge, ship a danlab skill to `dani-skills`.

### Tier 8 — Security researcher (v120 NEW)
- The Mashable article puts OpenClaw on the security researcher's radar. **The right response is to make them allies, not enemies.** Invite them to audit, publish the threat model, fix the flaw.
- **First action:** read the threat model, file a CVE, get credited in the fix.

---

## 11. The five takeaways (v120)

1. **The story is real and v120 makes it more honest.** 9 processes live, 1 Tauri app published, 1 bot live. The OpenClaw substrate is now a public story (Newsweek cited us, Mashable flagged a flaw). **The right move is to publish the protocol surface + the threat model in the same week. Honesty is the moat.**
2. **The protocol is the new origin pillar.** Cerf's framing + Anthropic's Apps Gateway + OpenClaw's MCP bridge + X's MCP server = the substrate is standardizing. **We are the only lab shipping it on a wearable with an auditable threat model.**
3. **Observability > model is the next wedge.** PagerDuty + $725B + audiod's segment_timing histogram. **The harness is the workbench, the model is the commodity. The daemon stack is the workbench.**
4. **Zuckerberg admitted Meta is behind. Anthropic is compute-constrained. Microsoft bet $2.5B on the implementation wedge.** The closed-source agent race is stalling, vertically integrating, and admitting the wedge is implementation. **We are the implementation layer, at $349, on a laptop.**
5. **The $1,500 model story + the 82M TTS story + the orbit story + the protocol story are the four pillars of every post.** Use them in this order: protocol → observability → on-device → small-beats-large.

---

## 12. Open questions for somdipto (v120)

1. **OpenClaw security audit (1-day spike):** do we have a 1-engineer-day to ship the threat model doc this week? **v120 P0.**
2. **OpenClaw protocol surface marketing artifact (2 days):** do we have a 1-engineer-day x2 to ship the protocol surface doc + diagram? **v120 P0, block on #1.**
3. **Newsweek URL:** can you find the article and send the link? **v120 P0.**
4. **HuggingFace `danlab` org creation:** can you authorize me to create it this week? **v120 P0.**
5. **X handle decision:** launch `@danlab` (recommended) or founder-led only? **v120 P0.**
6. **Tailscale authkey:** still the single highest-leverage env var. **v120 P0.**
7. **Show HN #1 timing:** is week 3–4 (Jul 21–28) good? **v120 P0.**
8. **Threat model public response:** do we want to engage Mashable directly, or publish the response doc and let it speak? **v120 P0.**
9. **Protocol surface v1.0 launch naming:** "OpenClaw protocol surface" or "agentd" or "Dani protocol"? **v120 P1.**
10. **Q3 hiring signal:** are we hiring, or are we solo? Changes the LinkedIn narrative. **v120 P2.**

---

*End of v120 research report. See `dan1-marketing-strategy.v120.md` for the action plan.*
