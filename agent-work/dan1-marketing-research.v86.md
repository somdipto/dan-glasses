# Dan1 Marketing Research — v86

**Agent:** DAN-1 (co-founder, marketing + growth)
**Run:** 2026-06-26 06:30 UTC (12:00 IST)
**Replaces:** v83/v85 — these are sharper, denser, with 2026-06 competitive landscape.
**Read order:** Read once, never again. This is the canon.

---

## 1. What is Dan Glasses?

**The product:** A pair of open-source AI glasses you build yourself — glasses + clip-on camera + on-device daemon mesh that turns your view into structured, searchable memory. The hardware is commodity (V4L2 webcam + mic + optional bone-conduction audio). The value is the **software stack** that ships today and runs as 8 live daemons.

**The vision:** Personal AI that *watches your life with you*, not an assistant you summon. The differentiator is not the glasses. The differentiator is **memoryd** — episodic + semantic + procedural memories with embeddings, retrievable across sessions, with 144/144 tests and a published Tauri v2 desktop UI.

**Target user (NOT mainstream, NOT today):** builders, researchers, and indie hackers who would rather SSH into a daemon than swipe an app. The right ICP is someone who has an LLM subscription, a soldering iron, and a dream.

**Core value proposition (one sentence):** *Build your own AI companion that never stops paying attention, never sends your data to a vendor, and never goes away.*

**Why this framing matters:** the 2026 smart-glasses market is a confusing hype cycle (Meta, Snap, Even Realities, Brilliant Labs, Acer). Dan Glasses is **not** a competitor to Ray-Ban. It's a competitor to the *assumption* that personal AI has to come from a Silicon Valley hyperscaler.

---

## 2. User Workflow — Unboxing to Daily Use

Concrete steps a user takes today with the current `dan-glasses-daemons_0.1.0-1_all.deb` package:

1. **Install** — `sudo dpkg -i dan-glasses-daemons_0.1.0-1_all.deb`. Installs 8 systemd units: audiod (8090+8091 WS), perceptiond (8092), memoryd (8741), toold (8742), ttsd (8743), os-toold (8744), dan-glasses-app (8747), openclaw (18789).
2. **Plug in hardware** — USB webcam (V4L2 `/dev/video0`), USB mic. Anything ALSA-compatible works.
3. **Download models** — `bash Services/perceptiond/models/download.sh` fetches LFM2.5-VL-450M (209MB) + mmproj (180MB). `whisper.cpp` ships with base.en (148MB).
4. **Open Tauri app** — published at `dan-glasses-app-som.zocomputer.io` or built locally. Four tabs: Vision, Memory, TTS, Live Transcript.
5. **Bootstrap wizard** — roundtrip verified at 7.08s. Sets salience mode (idle/watchful/active), runs a 5-second vision check, confirms audiod capture, initializes memoryd.
6. **Daily use loop:**
   - Live Transcript tab shows real-time speech-to-text from audiod WS `:8091` with mean per-token confidence
   - Vision tab streams salient frames through perceptiond, LFM2.5 produces natural-language descriptions to a ring buffer (200 events)
   - Memory tab lets you query `memoryd` semantic search across episodic/semantic/procedural memories — "what did I read about X last week?"
   - **The proactive loop:** `awarenessd` (next service) will subscribe to both audiod + perceptiond, push notifications *without user prompt* ("you've been staring at the same screen for 23 min", "you said 'tired' 4 times in the last hour").
7. **Voice/Telegram out** — OpenClaw gateway (`:18789`) bridges to Telegram `@danlab_bot` + Zo MCP tools via `mcporter`. Your glasses talk to your agents.

**Friction points a marketing piece must NOT hide:**
- VLM inference is ~10–15s/frame on CPU-only x86_64. Watchful mode (5fps, salient-gated) is the realistic default until we have NPU or aarch64 tuning.
- LFM2.5 is *small*. Don't oversell vision quality.
- First install is still 10–15 min (downloads + ALSA setup).

---

## 3. Competition — June 2026 Landscape

| Player | Form | Price | AI | Source | Open? | Threat to Dan Glasses |
|---|---|---|---|---|---|---|
| **Meta Ray-Ban** | Glasses + camera | $299+ | **Muse Spark** (replaced Llama 4 May 2026) | Meta cloud | ❌ | Cultural mindshare. Defines what consumers think "AI glasses" means. |
| **Meta Ray-Ban Display** | Glasses + HUD + Neural Band EMG | $799 | Muse Spark | Meta cloud | ❌ SDK | The "wow" device — HUD + EMG input is genuinely novel. |
| **Snap Specs** | Standalone AR spatial computer | $2,195 | Snap AR OS | Local? | ❌ | Not in same market. Too expensive, too bulky. |
| **Even Realities G2** | Glasses + single-color HUD | $599 | Even AI (limited) | Cloud | ❌ | The "ambient AI" framing. Closest to our vision. 36g, very wearable. **No camera, no speakers** — they bet on a different sensor mix. |
| **Brilliant Labs Halo** | Glasses + microOLED HUD | TBD | **Noa** (private on-device agent) | Local-first | ✅ open HW+SW | **The most direct competitor.** ZephyrOS + Lua scripting, Alif B1 NPU, 14hr battery, "personal AI agent that sees, hears, speaks." |
| **Acer G10** | Glasses + camera + mic | $300 | Acer AI assistant | Cloud | ❌ | Undifferentiated race-to-the-bottom. |
| **Google × Warby Parker** | Glasses + Gemini (rumored late 2026) | TBD | Gemini Live | Cloud | ❌ | Brand + Gemini Live API. Could dominate when shipped. |
| **Apple Glasses** | Glasses (rumored late 2027) | $200–500 | Apple Intelligence | Cloud | ❌ | Cook's "top priority" before Ternus takes over. |
| **Dan Glasses** | DIY clip-on + daemon mesh | ~$200–400 in parts | Local (whisper.cpp + LFM2.5-VL + MiniLM-L6-v2) | 100% local | ✅ MIT | **The only stack that is genuinely open AND genuinely self-hostable AND genuinely local-first.** |

### The wedges where Dan Glasses is genuinely different

1. **Proactive, not reactive.** Ray-Ban Meta, Even Realities, Brilliant Labs — all are *pull-based*. You say "Hey Meta" or look at a notification. Dan Glasses' audiod+perceptiond+memoryd mesh is **always-on**. The AI notices things you didn't ask about. This is the killer wedge but it's not yet shipped (awarenessd is the next service).
2. **Local-first, no vendor.** No cloud dependency. Your frames never leave the box. Brilliant Labs is local but their SDK is the API surface — Dan Glasses is *the whole stack*, including the daemon mesh and the long-term memory graph.
3. **Memory as a primitive.** Even Brilliant Labs' "Noa" agent has memory, but it's their memory. Dan Glasses' memoryd uses OpenAI-compatible embeddings (`POST /v1/embeddings`), exports memories, and lets you query across episodic/semantic/procedural. Other vendors will not give you this.
4. **Replaceable components.** Want a different VLM? Swap the llama.cpp binary. Want a different STT? Swap whisper.cpp. Want a different embedding model? Memoryd already takes any sentence-transformers. The competitor glasses are vertically integrated. Dan Glasses is a **Unix philosophy for the face**.
5. **India origin.** This is a *feature*, not a footnote. Indian English, Indian accents, Indian multilingual environments are underserved by every other vendor. We can name ten things Meta's Muse Spark gets wrong with code-switched Hindi-English speech that audiod's whisper.cpp + Silero VAD pipeline handles correctly.

### Where Dan Glasses loses today (be honest)

- Industrial design. The clip-on is not going to fool anyone in a boardroom.
- Battery life. Unmeasured on aarch64; CPU-only VLM at 5fps is the realistic cap.
- Vision quality. LFM2.5 is 450M params. Even Realities' "AI assistant" is more polished for transcription because they ship *only* transcription.
- App ecosystem. Zero. The mesh is the product.

---

## 4. What is danlab-multimodal?

**The honest framing (from the README):** A hackathon project. Sub-250MB vision-language model on CPU with llama.cpp + SmolVLM-256M. **Not RL.** Hand-coded heuristic feedback loop that scores outputs and prints suggestions for human improvement. They explicitly call this "pre-RL scaffold."

**What problem does it solve?** Proves that **multimodal AI can run on commodity hardware** without a GPU or cloud bill. ~26s inference on CPU. No SaaS. No API keys. This is the *anti-Brent Spiner argument*: AGI does not require $100M of H100s.

**Strategic importance:** danlab-multimodal is the *research arm* proof point. It's the demo we show when someone asks "but you're just wrapping llama.cpp." We are not. We built:
- A heuristic feedback loop (with the explicit pre-RL scaffold framing — Jack Clark's May 2026 warning is the timing signal)
- An asciinema demo live at zo.pub/som/danlab-multimodal-demo
- The reference architecture that perceptiond's production pipeline (`LFM2.5-VL-450M`) descends from

**What marketing should NOT claim:** we have RL. We don't. We are explicit about this. The credible path to genuine RL is the [SIA framework](https://github.com/HexoLabs/SIA) (Hexo Labs, MIT, May 2026). Until that fork ships into our stack, this stays pre-RL.

---

## 5. What is paperclip?

**paperclip** is a separate package in the workspace — monorepo with `cli/`, `server/`, `ui/`, `packages/`, `skills/`. Reads like a developer infrastructure project (Dockerfile, RAILWAY.md, fly.toml, adapter-plugin.md, evals/). It's the layer under Dan Claw / agent runtime.

**For marketing purposes:** paperclip is a *future* product. It is not customer-facing today. Do not promote it on the landing page yet. Reference it only in the deep-docs section.

**Strategic note:** paperclip is the answer to "what is danlab.dev beyond hardware?" If dan-glasses is the body, paperclip is the connective tissue. Treat it as internal for v1 of marketing.

---

## 6. The Danlab Story — From India to the World

**Origin facts:**
- Founded in Bengaluru, India by somdipto nandy
- Solo founder + AI co-founders (Dan1, Dan2, Dan3, Dan4 agents)
- Self-funded (no VC) — this is the AGI-from-India thesis in action
- Domain: `danlab.dev`
- Shipped: `dan-glasses-daemons_0.1.0-1_all.deb` (Debian package), published Tauri SPA, 8 live daemons, 144/144 tests
- Models: LFM2.5-VL-450M (Liquid AI), SmolVLM-256M, all-MiniLM-L6-v2 — all local

**Narrative arc:**

> Most AI labs are building bigger models on bigger clusters and selling access to the API. Danlab is building the other half — the personal, local, sovereign AI layer that doesn't need a hyperscaler to exist. From a desk in Bengaluru, with one founder and four AI co-founders, we've shipped an open-source stack that runs whisper.cpp + a vision-language model + a semantic memory graph on a single box. We didn't raise a Series A. We raised a Debian package.

**The 2026 thesis:** the smart-glasses market is going to bifurcate.
- **Consumer branch:** Meta, Snap, Google, Apple — vertically integrated, cloud-dependent, vendor-locked.
- **Sovereign branch:** Brilliant Labs (open), Dan Glasses (open + local-first + memory-graph + proactive).

The sovereign branch is small. It will be the one that survives the privacy backlash. The 2018 "fb loses 100B on privacy" moment is coming for AI glasses. Dan Glasses is the alternative.

**The India-specific narrative:**
- India's Aadhaar biometric debate has primed the public to think about *data sovereignty*.
- Indian English is the world's largest L2 English population. Every model that isn't trained well on Indian English speech (Hinglish code-switching, Tamil-English, Bengali-English) underperforms here. We can win India by being *actually good* at this.
- Hardware cost sensitivity in India makes a $200 clip-on + $0/month software stack compelling vs. a $799 Meta Ray-Ban Display + Meta AI subscription.
- "Atmanirbhar AI" (self-reliant AI) is a government priority. We're aligned with policy by default.

---

## 7. Marketing Channels — Where Danlab Wins

| Channel | Why | Priority |
|---|---|---|
| **GitHub** | The product IS the marketing. Every README is a landing page. | P0 — fix READMEs first |
| **X / Twitter** | Smart-glasses discourse lives here. Founders + AI researchers + indie hackers are the ICP. | P0 — daily posts |
| **Hacker News (Show HN)** | The Show HN for `dan-glasses-daemons_0.1.0-1_all.deb` is the single highest-ROI marketing event. | P1 — schedule it |
| **Reddit r/smartglasses, r/LocalLLaMA, r/embedded, r/IndiaInvestments** | Niche but high-signal | P1 |
| **YouTube / Loom** | Long-form demos of "build your own AI glasses in 30 min" | P1 |
| **arXiv** | When awarenessd ships + audiod calibration RL paper — that goes on arXiv | P2 |
| **LinkedIn** | For investor/scout visibility, not customer acquisition | P2 |
| **Press (TechCrunch, The Verge, Hacker Newsletter)** | Earned, not paid. Only after organic hits >10k MAU | P3 |
| **Conferences** | NeurIPS, CVPR, FOSSASIA, IndiaFOSS | P2 |

**Channels to deliberately AVOID:**
- Paid ads (no budget, no conversion funnel yet)
- Instagram/TikTok (ICP isn't there)
- Product Hunt (we'd get crushed by Meta noise)

---

## 8. Content Danlab Should Produce

**Tier 1 — ship every week:**
1. **Build log** — short blog post or X thread: "what we shipped this week in the daemon mesh." The dan-glasses STATUS.md format is a perfect template.
2. **Architecture deep dives** — perceptiond's salience gate, memoryd's embedding pipeline, audiod's segment-cap trick.
3. **"Why I open-sourced X" threads** — founder POV, opinionated, India-origin story.

**Tier 2 — ship every month:**
4. **Show HN post** — "Show HN: Open-source AI glasses from India, 8 live daemons, 144 tests." With the .deb link.
5. **Demo video** — "Build your own AI glasses in 30 minutes" — clip-on, daemon install, Tauri app launch, live transcript demo.
6. **Comparison post** — "Dan Glasses vs Meta Ray-Ban vs Brilliant Labs Halo: the local-first wedge."
7. **Research notes** — pre-RL scaffold documentation, SIA framework integration roadmap.

**Tier 3 — when ready:**
8. **arXiv paper** — audiod calibration RL results (Dan2's v11 roadmap target).
9. **Conference talk** — FOSSASIA 2026 or IndiaFOSS 2026.
10. **The big story** — when awarenessd ships, the "proactive AI companion" thesis gets its proof point.

**Content that is NEVER acceptable:**
- Generic AI hype posts
- "We're excited to announce" filler
- Stock photos of people wearing glasses
- Comparison charts that put Dan Glasses above Ray-Ban (we lose that fight on features)

---

## 9. Current Online Presence — Audit

| Surface | Status |
|---|---|
| **danlab.dev** | Domain registered, no live marketing site found. Needs landing page. |
| **GitHub** | Multiple repos (dan-glasses, danlab-multimodal, paperclip, blurr, dan-glasses-app, clawdi, danclaw, danlab-channel). READMEs vary wildly in quality. |
| **zo.pub/som/danlab-multimodal-demo** | ✅ Live — asciinema recording of the heuristic feedback loop demo. |
| **dan-glasses-app-som.zocomputer.io** | ✅ Live — Tauri SPA, port 8747. |
| **X / Twitter** | No known account. Need to create `@danlab_dev` or `@somdiptonandy`. |
| **LinkedIn** | somdipto's personal. No company page. |
| **Hacker News** | No prior submissions. |
| **YouTube** | No channel. |
| **Reddit** | No presence. |
| **arXiv** | No papers. |

**Top-of-funnel gaps:**
1. No landing page (this is the Show HN blocker — without a site, the Show HN fails)
2. No X presence
3. Inconsistent READMEs (one of them is 10228 chars of PRD; another is 15 lines)
4. No founder narrative published anywhere

---

## 10. First Users — Profile of the Ideal Early Adopter

**The 100-person beachhead:**

| Attribute | Value |
|---|---|
| Age | 25–40 |
| Location | Bengaluru, SF, Berlin, Tokyo (cities with strong maker + AI cultures) |
| Job | ML engineer, indie hacker, hardware tinkerer, researcher (PhD/postdoc), CTO of a 5-person AI startup |
| Tools they already use | llama.cpp, Ollama, Home Assistant, arduino/pi, Discord bots, Telegram bots |
| Reads | Hacker News, X AI timeline, Latent Space, r/LocalLLaMA |
| Buys | Ray-Ban Meta *and* has opinions about it; has soldered a Raspberry Pi at least once |
| Pain | "I want AI to remember my life but I don't trust any vendor with my face data" |
| Magic moment | Installs the .deb, opens the Tauri app, sees the live transcript start streaming, queries memoryd for something they said 20 minutes ago, gets it back |

**NOT the early adopter:**
- Consumer looking for turn-key smart glasses
- Enterprise buyer (no procurement story)
- Anyone who needs the glasses to look like Ray-Bans in a meeting

**Acquisition strategy:** The beachhead finds us through (a) Show HN, (b) r/LocalLLaMA post, (c) Brilliant Labs developer community cross-pollination, (d) India AI/ML Discord servers. We don't need 10k users. We need 100 users who each build a tool on top of the daemon mesh.

**The metric that matters:** not downloads. **GitHub stars on `dan-glasses` × number of unique contributors who opened a PR in the first 90 days.** That tells us if the mesh has a community.

---

## Strategic Implications

1. **The landing page is the bottleneck.** Everything else can wait. Ship the landing page from v83 marketing artifacts on danlab.dev or as a zo.space route.
2. **The Show HN is the unlock.** Single highest-ROI marketing event of Q3 2026. Must coordinate with technical readiness — the README, the .deb, the demo all need to be friction-free.
3. **The X thread on Brilliant Labs comparison** is the wedge content. Brilliant Labs' open-source community is the natural pipeline.
4. **The arXiv paper** is the credibility move. Not for marketing, for the founders' personal brand and the "Danlab = research lab, not just product" narrative.
5. **India origin is the moat.** Lean in. Don't soften it.

---

## Open Questions for the User (somdipto)

1. Domain `danlab.dev` — is it pointed at a Zo Site yet? Where should the landing page live?
2. Do we have a company X handle already? If not, what handle? (`@danlab_dev`? `@danlab_?`)
3. Is there a personal X for somdipto we should reference?
4. The pre-RL scaffold framing in danlab-multimodal — should we keep that explicit positioning, or soften for marketing? (My recommendation: keep it. It's a feature, not a bug.)
5. Paperclip — when is it ready to be mentioned on the landing page?
6. Brilliant Labs Halo — have we tested against it? Direct comparison demo would be high-value content.
7. The founder narrative — does somdipto want to be the public face, or stay low-profile with the agents as the public voice? (My recommendation: founder for press, agents for technical content.)
---

## 7. Marketing Channels — Where We Win

**Tier 1 (this quarter):**

| Channel | Why | Metric | Cadence |
|---|---|---|---|
| **GitHub** | Our highest-trust surface. Every daemon has a SPEC.md, a `tests/` dir, a CI badge. We earn credibility from code, not copy. | Stars, PRs, issue depth | Continuous |
| **Hacker News (Show HN)** | One well-written launch post > 6 months of Twitter. The story (open-source AI glasses daemon mesh from India) is HN-native. | Top 24h, comment count | 1 launch post Q3 |
| **X/Twitter (@danlab_dev)** | Founder voice, short and technical. Audiod v0.7, perceptiond v5, the new pre-RL scaffold framing — these are posts, not threads. | Followers, RTs by AI/ML accounts | 3–5 tweets/week |
| **Reddit (r/LocalLLaMA, r/singularity, r/india)** | Where the "self-host your own AI" community lives. Engage authentically. | Upvotes, comment quality | 1 post/week |

**Tier 2 (this quarter, secondary):**

| Channel | Why | Metric | Cadence |
|---|---|---|---|
| **LinkedIn (somdipto + Dan Lab page)** | Founder essay on India-origin AGI thesis. Reach enterprise + Indian diaspora. | Impressions, comments | 1 post/week |
| **YouTube** | 2-min demo of proactive loop (when awarenessd ships). Also: short technical clips of audiod + LFM2.5-VL. | Views, watch time | 1 video/month |
| **Discord (own + community servers)** | Build a `discord.gg/danlab` once GitHub hits 50 stars. | Active members | Daily |

**Tier 3 (do NOT play):**

| Channel | Why not |
|---|---|
| TikTok / Reels | Wrong audience. We sell to builders, not consumers. |
| Paid ads | No budget, wrong stage. |
| Press releases | Premature. Earn press, don't buy it. |
| Apple/Google app stores | Not relevant until we have a mobile client. |

**Channel decision rule:** if a channel does not reach someone who can SSH into a daemon or read a SPEC.md, it's the wrong channel today.

---

## 8. Content to Produce — The 12 Pieces

These are the 12 pieces of content that will define Danlab's external presence over the next 90 days. Each has an owner, a format, a target channel, and a deadline.

| # | Title | Format | Channel | Owner | Deadline |
|---|---|---|---|---|---|
| 1 | "We shipped a Debian package for AI glasses. Here's the SPEC." | Long-form blog post (2000 words) | danlab.dev/blog, HN | somdipto + Dan1 | Jul 5 |
| 2 | "Why Dan Glasses is not a Ray-Ban competitor" | Positioning essay | LinkedIn, X thread | somdipto | Jul 8 |
| 3 | "Pre-RL scaffold: an honest framing of self-improving AI" | Essay (danlab-multimodal README as essay) | HN, X | Dan1 + Dan2 | Jul 10 |
| 4 | The 8-daemon mesh diagram | Single PNG (D2-generated) | All channels | Dan1 | Jul 3 |
| 5 | "8 daemons, 144 tests, $0 cloud cost" | X thread (8 tweets) | X | Dan1 | Jul 12 |
| 6 | Show HN post | HN submission (400 words) | HN | somdipto | Jul 18 (after #1 lands) |
| 7 | "LFM2.5-VL on CPU: here's how slow" | Benchmark blog (1500 words) | danlab.dev/blog | Dan2 | Jul 22 |
| 8 | "What Brilliant Labs Halo gets right (and what it doesn't)" | Comparison post (1800 words) | HN, r/LocalLLaMA | Dan1 | Jul 25 |
| 9 | "The personal AI stack in 2026: a buyer's guide" | Comparison matrix (table + commentary) | danlab.dev/blog | Dan1 | Aug 1 |
| 10 | "Why I'm building AGI from Bengaluru, not Boston" | Founder essay | LinkedIn, X, blog | somdipto | Aug 5 |
| 11 | "Code-switching Hindi-English in audiod: how Silero VAD handles it" | Technical deep-dive | blog, r/LocalLLaMA | Dan2 | Aug 10 |
| 12 | 30-second hero demo video (when awarenessd ships) | MP4, looped | All channels | somdipto + Dan1 | Aug 20 |

---

## 9. Current Online Presence — Audit

**Findings (verified 2026-06-26):**

- ✅ **`danlab.dev`** — domain exists, currently points to an old GitHub Pages-style index. Needs replacement.
- ✅ **`dan-glasses-app-som.zocomputer.io`** — Tauri SPA published, live, 4 tabs working. Not branded as "Dan Glasses" externally.
- ✅ **`zo.pub/som/danlab-multimodal-demo`** — asciinema + pipeline diagrams. **The only piece of marketing collateral that exists today.**
- ✅ **Telegram `@danlab_bot`** — operational, connected to OpenClaw gateway. Not a marketing surface.
- ✅ **Debian package** — `dan-glasses-daemons_0.1.0-1_all.deb` (28KB), built Jun 16.
- ❌ **GitHub org** — public repos do not exist yet. Everything is private/local.
- ❌ **X/Twitter** — no `@danlab_dev` handle registered (or if registered, no posts).
- ❌ **LinkedIn** — no Dan Lab company page.
- ❌ **YouTube** — no channel.
- ❌ **Discord** — no server.
- ❌ **Press coverage** — zero.

**Verdict:** We are essentially invisible. This is normal for a lab that has been heads-down building for 6 months. The fix is a 30-day foundation sprint:

1. **Week 1:** Register `@danlab_dev` on X. Create Dan Lab company page on LinkedIn. Set up GitHub org `danlab-dev`.
2. **Week 2:** Push the three public repos (dan-glasses, danlab-multimodal, paperclip). Wire danlab.dev to the landing page.
3. **Week 3:** Ship content pieces #1, #4, #5 (blog + diagram + tweet thread).
4. **Week 4:** Ship content piece #6 (Show HN). Begin work on pieces #2, #7, #8.

---

## 10. First Users — Profile

**Tier 1 (this month, ~50 people):**
- **Builders** who already own Ray-Ban Meta, Brilliant Labs Frame, or Even Realities G1/G2, are frustrated by cloud lock-in, and want a software-only stack they can self-host.
- **AI researchers** who want a reproducible always-on audio+vision harness for studying proactive AI behavior.
- **Privacy advocates** who refuse to send camera frames to Meta. Find us on r/privacy.

**Tier 2 (this quarter, ~30 more):**
- **Accessibility researchers** — Be My Eyes style use cases. Deaf users getting real-time visual descriptions.
- **Quantified-self / biohackers** — multi-day audio+vision diary.
- **Indie developers in India** — code-switching is the wedge no US vendor owns.

**Tier 3 (next year, ~20):**
- Hardware OEMs looking for an OS for their smart glasses.
- Healthcare, retail, field service — all have ambient-AI use cases that don't fit US vendor data policies.

**The first 100 we want:**
- 50 builders who file real GitHub issues
- 20 researchers who cite the work
- 15 accessibility users with concrete use cases
- 10 journalists who write one honest piece
- 5 enterprise pilots (case studies, not revenue)

**NOT the early adopter:**
- Consumer looking for turn-key smart glasses
- Enterprise buyer (no procurement story)
- Anyone who needs the glasses to look like Ray-Bans in a meeting

**Acquisition strategy:** The beachhead finds us through (a) Show HN, (b) r/LocalLLaMA post, (c) Brilliant Labs developer community cross-pollination, (d) India AI/ML Discord servers.

**The metric that matters:** not downloads. **GitHub stars × unique contributors who opened a PR in the first 90 days.** That tells us if the mesh has a community.

---

## 11. The Honest Limits — What We Won't Claim

Marketing copy that overpromises kills trust. The following are **non-claims** for any external piece until the underlying capability ships:

1. ❌ "Our AI proactively understands your context" — `awarenessd` doesn't ship yet. Say "the architecture supports proactive loops; audiod and perceptiond already stream continuously."
2. ❌ "We do RL/self-improvement" — `danlab-multimodal` is explicitly pre-RL scaffold. Say "we ship the heuristic loop today and document the path to real RL via the SIA framework."
3. ❌ "Privacy-first, nothing leaves your device" — TTS uses cloud TTS in some flows; Telegram bridge sends to Telegram servers. Say "audio and vision frames never leave the device by default; outbound channels are opt-in per service."
4. ❌ "On-device LLM" — whisper.cpp + LFM2.5-VL-450M are local, but toold + openclaw can route to cloud LLMs. Say "the core sensory loop (audiod + perceptiond + memoryd) runs on-device end-to-end."
5. ❌ "All-day battery" — unmeasured on aarch64. Don't claim it.
6. ❌ "Works on any hardware" — audiod requires ALSA, perceptiond requires V4L2, both require x86_64/aarch64 Linux. State the constraint.

The discipline of "what we won't claim" is itself a marketing asset. It's why engineers trust us.

---

## 12. Open Questions for somdipto (consolidated)

These block the 30-day foundation sprint. Pick the defaults or override:

1. **GitHub org name.** My proposal: `danlab-dev`. Confirm or override.
2. **Domain.** Is `danlab.dev` ours? Where does it currently point? Is `danglasses.dev` registered?
3. **X handle.** `@danlab_dev` — register or use alternative?
4. **Founder narrative.** Public face = somdipto (for press/essays) + Dan Lab agents (for technical content)? Confirm.
5. **Pre-RL scaffold framing.** Keep the explicit "this is not RL" honesty on the public page? My strong recommendation: yes, it's the brand.
6. **Paperclip.** Mention on landing page or hide until v1 of marketing? My recommendation: hide for v1.
7. **Brilliant Labs Halo.** Engage publicly or compete quietly? My recommendation: respectful comparison post (content piece #8), no direct confrontation.
8. **Show HN timing.** After awarenessd ships (Q4) or before (Q3)? My recommendation: Q3 with audiod/perceptiond only — proactive story comes as a follow-up.
9. **Funding posture.** Imply seeking capital? My recommendation: no, not until we have revenue or a flagship pilot.

---

## Final Note

This is the **marketing canon** for danlab.dev as of June 2026. The 30-day foundation sprint, the 12-piece content calendar, and the 100-user acquisition strategy are what we execute. Everything else is distraction.

— Dan1 👾

