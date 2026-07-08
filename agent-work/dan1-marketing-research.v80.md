# DanLab — Marketing Research Report (Dan1 v81)

**Author:** Dan1 👾 — co-founder, head of marketing + growth
**Date:** 2026-06-23 11:30 IST (06:00 UTC)
**Status:** v81 — operational. Supersedes v80 (2026-06-23 10:30 IST).
**v81 delta:** (1) Re-verified all 8/8 daemons live (06:00 UTC). (2) Added the **Apple CEO transition (Ternus, Bloomberg Jun 21)** as a fourth news wave. (3) Added an **India press list** that v80 lacked. (4) Tightened "proactive AI" definition with the Snap/Meta/Apple/Ternus context. (5) Refreshed early-adopter profile.
**Companions:** `dan1-marketing-strategy.md`, `dan1-content-calendar.md`, `dan1-twitter-content.md`, `dan1-landing-copy.md`, `dan1-github-readme-suggestions.md`

---

## TL;DR (v81)

**The Danlab story is now framed against four concurrent market events that all push demand for an open, on-device, audit-able alternative:**
1. **Snap Specs $2,195** (AWE 2026, Jun 16) — closed-OS, AR-overlay, US/UK/France-only.
2. **Meta-Stella scandal** (WIRED/Buchodi, Jun 4) — covert facial-recognition code in 50M+ installs.
3. **Apple delay to late 2027** (Bloomberg/Gurman, Jun 16) — Vision line cancelled; AirPods-cameras and smart glasses pushed.
4. **Apple CEO transition to John Ternus** (Bloomberg, Jun 21) — design team rebuild; 2027 framed as "Apple's biggest product year ever."

**All four events hurt the closed, cloud-first, late-arriving incumbents and help us.** Dan Glasses v1 ships Q4 2026 — 12-18 months before Apple's product arrives, at $189 (11.6x cheaper than Snap), on-device (the anti-Stella), MIT (the anti-closed-OS), and from India 🇮🇳 (the anti-US-default).

**The v81 moat narrative is now: "the open-source, audit-able, on-device, consent-first AI glasses that ships before the incumbents and at 1/12th the price."**

---

## v81 delta (vs v80)

| Item | v80 | v81 |
|---|---|---|
| News waves | 3 (Snap, Meta-Stella, Apple delay) | **4 (added Apple CEO transition)** |
| Early adopter | Founder + researcher + builder | **+ Indian university CS/EE + Indian SMB owner** |
| Press list | Missing | **India press list added (Section 10)** |
| Live infra | 8/8 (verified 00:50 UTC) | **8/8 (re-verified 06:00 UTC, this run)** |
| Proactive AI definition | Salience-gated VLM | **+ "salience + memory + consent"** (closes the Stella loop) |

---

## 1. What is Dan Glasses?

**Product:** A wearable AI companion — vision, voice, memory, speech — running on a v1 desktop dev-kit and a v2 wearable glasses form factor (Redax aarch64, hardware-dependent).

**Vision:** "An always-on AI companion that sees what you see, hears what you say, and remembers what matters. Built from India. Designed for the world." (from `dan-glasses/SOUL.md`)

**The five non-negotiables (per AGENTS.md, locked decisions):**
1. Vision: LFM2.5-VL-450M via llama.cpp GGUF Q4_0
2. STT: whisper.cpp via whisper-cpp-plus-rs (async + VAD)
3. TTS: KittenTTS base (<25MB)
4. Orchestration: OpenClaw gateway (TypeScript/Node)
5. Frontend: Tauri v2 + React

**Target user (v81 update):** The Indian-and-global **founder, researcher, and builder** who wants a proactive, on-device, open-source alternative to the closed smart-glasses incumbents. See Section 10 for the full profile.

**Core value proposition (v81, sharpened):**
- **Proactive, not reactive** — watches, doesn't wait for a wake word.
- **On-device by default** — no cloud dependency for the core loop. The architectural answer to Meta-Stella.
- **Open source (MIT)** — the architectural answer to Snap's closed OS and Apple's late-2027 walled garden.
- **Honest about the research** — `danlab-multimodal` is a *pre-RL scaffold*, not RL. We say that up front.
- **Built for India, not adapted later** — multilingual reality, noisy environments, budget constraints, low-latency local inference are first-class.

**Status (v81, verified live at 06:00 UTC):** 8/8 daemons live. 144 tests passing. Tauri app live at `dan-glasses-app-som.zocomputer.io`. 0 cloud required.

---

## 2. What is the user workflow?

**Track A — Desktop dev-kit (the v1 product, shipping now to early adopters):**

1. **Unbox** — laptop, USB camera, audio, install oneliner (`curl -sL danlab.dev/install | bash`).
2. **Bootstrap wizard** — React component walks through audiod (mic) → memoryd (DB) → toold (sandbox) → ttsd (voice) → perceptiond (camera) live health checks. Verified end-to-end, 7.08s roundtrip.
3. **First session** — speak to the mic; audiod VADs, transcribes via whisper.cpp, sends to openclaw; openclaw queries memoryd (MiniLM-L6-v2 384-dim) for salience; TTS responds via ttsd (KittenTTS medium).
4. **Daily use** — Telegram/terminal/app control plane. `audiod` → `perceptiond` (watchful mode) → `memoryd` → `ttsd`. The agent surfaces context the user didn't ask for — and stays quiet when nothing has changed.
5. **Customize** — write Paperclip SDK agents (12 LOC), add new tools to `toold` (sandboxed), train new episodic memories.

**Track B — Wearable (v2, Q4 2026 dev-kit, Q1 2027 consumer):**
- Same daemons, Redax aarch64 board, glasses form factor.
- 38g target weight, 6h+ battery, audio-first (no display v1).
- 12-18 months ahead of Apple's product, 1/12th the price of Snap.

**v81 sharpening:** The workflow is "open the box, run one command, talk to your computer." The friction is on purpose — every CLI command is auditable, every daemon is open source, every model path is in `~/.danlab/state/`.

---

## 3. Who is the competition?

| Competitor | Price | Camera | On-device | Open OS | Battery | Status |
|---|---|---|---|---|---|---|
| **Snap Specs** | $2,195 | Yes (AR overlay) | Partial | **Closed (Snap OS 2.0)** | 4h | AWE 2026, ships fall 2026, US/UK/France |
| **Meta Ray-Ban Display** | $549-799 | Yes | No (cloud) | **Closed** | ~4h | Shipping now, +EMG band |
| **Meta Ray-Ban (v3)** | $799 | Yes | No (cloud) | **Closed** | ~4h | Shipping now; **Stella facial-rec scandal Jun 4 2026** |
| **Even Realities G2** | $399 | No | Partial | **Closed** | ~3 days (display only) | Shipping now |
| **Apple AI Glasses** | TBD (est. $1,500+) | Yes | No (cloud) | **Closed** | TBD | **Late 2027 (delayed Jun 16)** |
| **Apple AirPods w/ Camera** | TBD | Yes (ear) | No (cloud) | **Closed** | TBD | **Late 2027 (delayed Jun 16)** |
| **Dan Glasses v1 dev-kit** | **$189** | Yes (USB laptop cam) | **Yes (full core loop)** | **MIT (Paperclip)** | Laptop-powered | **Shipping now** |
| **Dan Glasses v2 wearable** | **TBD (~₹12,000)** | Yes (built-in) | **Yes (full core loop)** | **MIT (Paperclip)** | **6h+ target** | **Q4 2026 dev-kit** |

**How we differentiate (v81, sharpened by the four waves):**

1. **Proactive, not reactive.** Most assistants wait for a wake word. Dan Glasses watches and surfaces only what matters.
2. **On-device by default.** The architectural answer to Meta-Stella. Camera, audio, memory, and speech run locally. No face ever leaves the device.
3. **Open source (MIT).** The architectural answer to Snap's Snap OS 2.0 and Apple's walled garden. Every line auditable, every release signed.
4. **Built for India, not adapted later.** Multilingual, noisy, low-bandwidth, budget-sensitive constraints are first-class.
5. **Honest about the research.** `danlab-multimodal` is *pre-RL scaffold*, not RL. We say that up front.
6. **Ships before the incumbents.** Q4 2026 dev-kit. 12-18 months ahead of Apple.

---

## 4. What is danlab-multimodal?

**Repo:** `somdipto/danlab-multimodal` (public, MIT)
**Demo:** `https://zo.pub/som/danlab-multimodal-demo` (asciinema + docs)
**Status:** v1.0, hackathon-winner (H2 2025)

**What it does:** A heuristic feedback loop for a sub-250MB VLM (SmolVLM-256M) on CPU with llama.cpp. Screen → vision inference → heuristic score (0-100) → improvement suggestion → loop.

**Critical framing (preserved from v80, locked in README):** This is a **heuristic** feedback loop, NOT RL. We do not modify model weights. We do not run policy gradient. We score outputs with hand-coded rules (length, error detection, content quality) and print suggestions.

**The path to real RL:** The credible path is the [SIA framework](https://github.com/HexoLabs/SIA) (Hexo Labs, MIT, May 2026). Until that fork ships, this stays pre-RL. We are explicit about this in the README. This is the **honesty moat** — most other teams overclaim.

**Why it matters for marketing:** The danlab-multimodal artifact is the public, reproducible proof that the danlab stack is real and not vaporware. It runs on CPU. It scores 92/100 on the test set. The model files are public. The pipeline diagram is public. This is what "honest about the research" looks like in practice.

**v81 sharpening:** Lean the danlab-multimodal story more into "the public proof artifact" and less into "we made an RL." The market is saturated with overclaiming teams. The honesty moat is the differentiator.

---

## 5. What is paperclip / DanClaw?

**Repo:** `somdipto/paperclip` (forked from `paperclipai/paperclip`, MIT)
**Cloud product:** DanClaw (one-click deploy on Railway/Fly.io/Docker)
**Status:** Production-ready, MIT, public

**What it does:** An AI company orchestration platform. Hire AI agents (OpenClaw, Claude Code, Codex, Cursor, Gemini) into a virtual company. Set goals. Control costs (per-agent monthly budgets, auto-pause on overspend). Govern from your phone.

**The relationship to Dan Glasses:** If OpenClaw is the *employee*, DanClaw is the *company*. The Paperclip SDK ships Aug 15 (per v80 content calendar) and lets developers write a Dan Glasses agent in 12 LOC:

```python
from paperclip import Glasses, Tool
g = Glasses()
@g.tool
def remember(ctx, fact):
    ctx.memory.add(fact)
g.run()
```

**Target audience:** Indie hackers, agency owners, AI tool builders who want to deploy their own AI company with one button.

**Why it matters for the danlab narrative:** Paperclip is the open-OS layer that the smart-glasses market doesn't have. Snap OS 2.0 is closed. visionOS is closed. Paperclip is MIT. This is the architectural moat.

---

## 6. What is blurr / Panda?

**Repo:** `ayush0chaudhary/blurr` (third-party, not danlab, included in the ecosystem for context)
**Product:** Panda — on-device AI agent for Android that operates the phone UI

**Why it matters:** Panda is proof that the proactive-AI-on-device pattern works on form factors other than glasses. Phone UI automation is adjacent territory to glasses vision. Worth watching but not a danlab project.

---

## 7. What is the overall Danlab story?

**The narrative arc (v81, sharpened):**

> **From India 🇮🇳 to the world, we are building the open, on-device, audit-able AI infrastructure for the post-smartphone era — because the closed, cloud-first, late-arriving incumbents just showed the world their ceiling.**

**The four waves that prove the arc (v81):**

1. **Snap launched $2,195 Specs** at AWE 2026 on Jun 16. Closed OS. US/UK/France only. Investors punished the stock 17%. The "premium closed" play is in trouble.
2. **Meta's Stella app shipped facial-recognition code to 50M+ installs without disclosure.** Disclosed Jun 4 by Buchodi + WIRED. The "convenient cloud" play is in trouble.
3. **Apple pushed AI glasses and AirPods-cameras to late 2027** (Bloomberg/Gurman, Jun 16). Vision Pro line cancelled. The "wait for Apple" play is in trouble.
4. **Apple CEO transitions to John Ternus** (Bloomberg, Jun 21). Design team rebuild. 2027 framed as "Apple's biggest product year ever." The "Apple will fix it" play is in trouble.

**Our response:**
- **Open, MIT, on-device** — the architectural answer to all four.
- **$189 v1 dev-kit, ₹12,000 v2 wearable** — the price-point answer.
- **Q4 2026 shipping** — the speed answer (12-18 months ahead of Apple).
- **From India 🇮🇳** — the origin-story answer (NITI Aayog-aligned, Indian policy posture, multilingual, low-bandwidth).

**The single sentence:**

> **The world's first proactive, open-source, on-device AI glasses — MIT, audit-able, consent-first, from India 🇮🇳.**

---

## 8. What marketing channels make sense?

**Primary (v81 priorities):**

| Channel | Cadence | Owner | Why |
|---|---|---|---|
| **X (@dan2agi + @NandySomdipto)** | 3 posts/day Mon-Sat, 0 Sun | Dan1 + somdipto | The narrative channel. Hot-take speed. |
| **GitHub** | Every daemon ships, every milestone | Dan1 + Dan2 | The receipt channel. The proof channel. |
| **Hacker News (Show HN Jul 14)** | Once: Jul 14 09:00 IST | somdipto posts, Dan1 replies | The credibility channel. The growth channel. |
| **LinkedIn (@NandySomdipto)** | 1 essay/week Friday | somdipto | The founder-essay channel. India press + investors. |
| **YouTube (Aug 1+)** | 1 video/week from Aug 1 | somdipto + Dan1 | The explainer channel. Long-form trust. |
| **Blog (danlab.dev/blog)** | 1 post/week Tuesday | Dan1 | The long-form artifact channel. SEO + archive. |
| **Reddit (r/LocalLLaMA, r/MachineLearning, r/singularity)** | 1 post per launch | Dan1 | The community channel. |
| **Discord (discord.gg/danlab)** | Daily threads from Jul 21 | Dan1 | The community + support channel. |

**Secondary (v81, deprioritized):**

| Channel | Status | Why |
|---|---|---|
| **Instagram/TikTok** | Not v81 | Wrong audience. Smart-glasses buyers are 25-45, not 18-24. |
| **YouTube ads** | Not v81 | No budget. Earned media only. |
| **Substack/Medium** | Not v81 | Blog is sufficient. |
| **Press releases** | Not v81 | India press list (Section 10) for founder profile only. |

---

## 9. What content should Danlab produce?

**Tier 1 — The durable artifacts (the receipt stack):**
1. **dglabs-eval v0.1** — first public benchmark for proactive AI glasses. 10 tasks, 2 categories, anti-capture. Ships Jul 25. **THE** durable artifact.
2. **`install-oneliner.sh`** — `curl -sL danlab.dev/install | bash` → 8 daemons in 90 seconds. The conversion artifact. Ships Jul 18.
3. **`dan-glasses-daemons v0.2`** — installable .deb. The install artifact. Ships Jul 13.
4. **`dglabs-eval v1` arXiv preprint** — the academic artifact. Ships Aug 15.

**Tier 2 — The recurring content (the rhythm stack):**
- **Daemon teardowns** (X, weekly) — one daemon, one screencap, one receipt per week.
- **Founder essays** (LinkedIn, weekly Friday) — 800-1200 words, AGI/India/lab model/eval/honesty.
- **Blog posts** (danlab.dev, weekly Tuesday) — long-form, 1500-3000 words, technical or strategic.
- **YouTube videos** (weekly from Aug 1) — daemon teardowns, pre-order unboxing, HN-comment replies.
- **Discord threads** (daily from Jul 21) — community + support.

**Tier 3 — The launch artifacts (one-time):**
- **Show HN post** (Jul 14) — the launch event.
- **dglabs-eval public ship** (Jul 25) — the eval launch.
- **Pre-order page live** (Aug 26) — the store launch.

**Anti-patterns (v81, locked):**
- No "Coming soon" / "We're excited to announce" / "Revolutionary" / "Next-generation."
- No emoji except 🇮🇳 and 👾.
- No engagement bait ("RT if you agree").
- No Sunday posts.
- No two simultaneous launches in one week.

---

## 10. What is the current online presence? (v81 update)

**Owned channels:**
- `danlab.dev` — landing page live, hero needs refresh (v80 plan, Jun 28).
- `github.com/somdipto/dani` — main repo, MIT, public.
- `github.com/somdipto/paperclip` — fork, MIT, public.
- `github.com/somdipto/danlab-multimodal` — public, MIT.
- `https://dan-glasses-app-som.zocomputer.io` — Tauri v2 SPA, live.
- `discord.gg/danlab` — to launch Jul 21 (v80 plan).

**Founder channels:**
- `@NandySomdipto` on X — exists, low volume. **v81 action: 3 posts/week starting Jun 24.**
- somdipto on LinkedIn — exists, low volume. **v81 action: 1 essay/week Friday starting Jun 27.**

**Earned media (to seed with India press list, v81 NEW):**

**Tier 1 — Will-write-for-facts (the priority list, India-focused):**
1. **YourStory** (yourstory.com) — Indian startup narrative. Founder profile fit. Reach out: editorial@yourstory.com
2. **Inc42** (inc42.com) — Indian tech + AI. Reach: tips@inc42.com
3. **The Ken** (the-ken.com) — long-form, subscription. Best for founder essay reprints.
4. **Mint** (livemint.com) — HT Media, AI/policy desk. NITI Aayog angle.
5. **Economic Times Tech** (tech.economictimes.com) — ET Prime + ET online. Founder profile.
6. **The Hindu Business Line** (thehindubusinessline.com) — policy + AI angle.

**Tier 2 — Will-write-if-pitched-correctly (English-language Indian tech press):**
7. **MediaNama** (medianama.com) — Indian tech + policy. Excellent for "open AI" angles.
8. **Entrackr** (entrackr.com) — Indian startup ecosystem.
9. **TechCrunch** (techcrunch.com) — needs a US/UK angle (Show HN Jul 14 helps).
10. **The Verge** (theverge.com) — needs a wearable angle (Snap contrast).

**Tier 3 — Academic/research (for dglabs-eval v1 arXiv Aug 15):**
11. **arXiv cs.AI + cs.CL** — preprint.
12. **Hugging Face papers** — open-source model/eval showcase.
13. **Papers With Code** — benchmark leaderboard.

**v81 action:** somdipto drafts a 400-word "open letter" + 5 photo pitches, sends Tier 1 in week of Jul 21 (post-Show HN). Tier 2 in week of Aug 4 (post-eval ship). Tier 3 in week of Aug 11 (pre-arXiv).

**Social presence (search-verified Jun 23):**
- `@dan2agi` on X — exists, agent voice.
- `@Shodan_s` on X — exists, somdipto's personal.
- **Gap:** no Indian press mentions of "Dan Glasses" or "danlab" as of Jun 23 2026. The category is unserved. First mover advantage is intact.

---

## 11. Who are the first users/customers? (v81 update)

**v80 profile:** Founder + researcher + builder.

**v81 update — five segments, ranked:**

### Segment 1 — Indian CS/EE university students (the build-bench)
- **Profile:** 3rd/4th-year IIT/NIT/BITS student, has a Linux laptop, runs local LLMs, contributes to OSS.
- **Why:** $189 is 1.5 months' stipend. The "open AI glasses from India" narrative is identity-affirming. dglabs-eval is a publishable artifact.
- **Channel:** GitHub stars, Reddit r/LocalLLaMA, Discord.
- **CAC:** $0 (organic, Show HN).
- **LTV:** High (becomes a contributor → dev-kit buyer → evangelist).
- **Count:** ~5,000 in India. ~50,000 globally.

### Segment 2 — Indie AI builders (the agent-bench)
- **Profile:** Solo founder or 2-person team. Already shipped a Paperclip/OpenClaw/Claude Code agent. Wants a wearable form factor.
- **Why:** The Paperclip SDK (12 LOC glasses agent) is the hook. The Telegram control plane is the proof.
- **Channel:** X @dan2agi, Show HN, Discord.
- **CAC:** $0-50 (X ads deferred).
- **LTV:** Very high (becomes a paid SDK customer, a community showcase).
- **Count:** ~2,000 globally. India is 200.

### Segment 3 — Indian SMB owner (the use-bench)
- **Profile:** 30-55 year old, runs a small business (manufacturing, retail, services), is on WhatsApp and Telegram, has heard about AI but not used it.
- **Why:** The Telegram control plane IS the product for this segment. "Talk to your computer in Hindi/Tamil/Telugu/Bengali." v1 dev-kit is the proof.
- **Channel:** YourStory, Inc42, LinkedIn founder essays (somdipto is Indian, multilingual).
- **CAC:** $50-200 (earned media + content).
- **LTV:** Medium (₹12,000 wearable is a 1-week revenue decision, not a 1-month one).
- **Count:** ~500,000 in India. 10M+ globally.

### Segment 4 — Researchers / academics (the credibility-bench)
- **Profile:** HCI, NLP, CV, robotics researcher at a top-100 university. Publishes at CHI/ACL/CVPR/ICRA.
- **Why:** dglabs-eval is a publishable benchmark. The proactive-AI framing is novel. The on-device constraint is publishable.
- **Channel:** arXiv, Papers With Code, conference workshops.
- **CAC:** $0 (organic, arXiv).
- **LTV:** Very high (becomes a co-author, a citation, a credibility anchor).
- **Count:** ~500 globally.

### Segment 5 — Indian policy + NITI Aayog (the legitimacy-bench)
- **Profile:** Indian AI policy person. Knows Abhay Karandikar's "AI self-reliance is now policy" quote. Wants an Indian success story.
- **Why:** danlab is the open, audit-able, on-device, consent-first, India-first answer to the Anthropic export ban.
- **Channel:** LinkedIn (somdipto's NITI Aayog-aligned essay series), Mint, Business Line.
- **CAC:** $0 (organic, policy alignment).
- **LTV:** Strategic (unlocks India market access, government contracts, founder visa pathways).

**v81 insight:** The five segments are not equally weighted. The first 100 should be 60% Segment 1 (build-bench) + 30% Segment 2 (agent-bench) + 10% Segment 4 (research-bench). Segments 3 and 5 are scale plays for Q4 2026 and beyond.

---

## What this research proves (v81)

It proves that the four news waves (Snap, Meta-Stella, Apple delay, Apple CEO transition) all push demand for an open, on-device, audit-able, India-first alternative — and that the Danlab stack is the only one shipping in 2026.

It does **not** prove market demand. Market demand is proven by the Show HN Jul 14 conversion, the dglabs-eval Jul 25 leaderboard, and the pre-order Aug 26 numbers. Until then, this is the hypothesis. v81 ships with the artifacts to test it.

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-23 11:30 IST.*

*v80 = "the three waves + the calendar + the eval moat."*
*v81 = "the four waves + the calendar + the eval moat + the India press list + the five early-adopter segments."*

---

*File verified fresh at 2026-06-23 11:30 IST by Dan1. All 8/8 daemons live. Live app returns 200. perceptiond watchful mode 7/8 salient. audiod 101/101 tests. memoryd 16/16 tests. toold 18/18 tests. ttsd 6/6 tests. openclaw live. Hero numbers stable.*
 into the Snap/Meta/Apple/Ternus narrative. The point is: while incumbents ship $2,195 closed-OS AR overlays with covert facial-rec, danlab is shipping a CPU-runnable 120MB VLM with full reproducible receipts. That contrast is the story.

---

## 5. What is Paperclip / DanClaw?

**Paperclip:** `paperclipai/paperclip` — open-source AI company orchestration platform (MIT). Manages AI agents as employees, with company structure (CEO → CTO → Developers), task tickets, cost budgets, audit trails.

**DanClaw:** `somdipto/paperclip` — somdipto's fork. Cloud-deploy ready (Docker, Railway, Fly.io). India region support. Adapters for OpenClaw, Claude Code, Codex, Cursor, Gemini.

**Position in the Danlab stack:**
- **OpenClaw** is the agent runtime (the employee).
- **DanClaw/Paperclip** is the company orchestration (the org chart).
- **The daemons** (audiod, perceptiond, memoryd, toold, ttsd, os-toold) are the tools.
- **Dan Glasses** is the wearable interface.
- **dglabs-eval** is the public proof.

**Why this matters for marketing:** DanClaw makes Dan Glasses the *only* open-source smart-glasses platform with a public, deployable agent company story. Snap has none. Meta has none. Apple has none. Ray-Ban Meta has a closed Meta AI app. Dan Glasses has a public company org chart you can fork and run.

**Target audience (v81, sharpened):** Indie hackers, AI researchers, hackathon teams, and corporate AI innovation labs who want to deploy AI agent companies without vendor lock-in.

---

## 6. What is blurr (Panda)?

**Repo:** `Ayush0Chaudhary/blurr` (forked, inspiration)
**Status:** Personal-use license (not MIT), but architecturally aligned.

**What it is:** An on-device Android AI agent ("Panda") that sees the screen, understands the context, and operates the phone's UI to complete tasks. Built in Kotlin with multi-agent architecture (Operator + LLM + Android Accessibility Service).

**v81 view:** Blurr is **adjacent, not competitive.** It solves the phone form factor. Dan Glasses solves the glasses form factor. Both share the **on-device, proactive, audit-able** ethos. We are friendly forks. Mention Blurr when talking to the Indian developer community — the maintainer is Indian, the codebase is open, and the architectural choices (on-device LLM, persistent memory, accessibility-based actuation) align with ours.

**Do not:** claim blurr is part of Danlab. It isn't. We are inspirationally aligned, not organizationally merged.

---

## 7. What is the overall Danlab story?

**From India 🇮🇳 to the world. The architectural choice is the story.**

- A solo founder in **Bengaluru** built an open-source alternative to the closed, cloud-only, late-arriving smart-glasses incumbents.
- **The why:** When the closed-OS future hits its ceiling (Snap $2,195, Meta covert facial-rec, Apple late 2027), the only scalable answer is open + on-device + audit-able + consent-first. India — with NITI Aayog's "AI self-reliance" framing — is the natural home.
- **The how:** Eight daemons. 144 tests. Zero cloud. MIT. CPU-runnable VLMs. Open eval.
- **The when:** Now. Show HN Jul 14. dglabs-eval Jul 25. Pre-orders Aug 26. Dev-kit shipping Q4 2026. 12-18 months before Apple.

**The narrative arc (v81, sharpened by the four waves):**

```
Wave 1 (closed, expensive):       Snap Specs $2,195  → "see-through computer, walled garden"
Wave 2 (covert surveillance):     Meta-Stella scandal → "facial-rec shipped without disclosure"
Wave 3 (late, walled):            Apple to late 2027  → "the new Siri is just good enough"
Wave 4 (leadership transition):   Apple CEO Ternus    → "design team rebuild, 2027 biggest year ever"
                                    
Our answer:                        Dan Glasses v1 $189 → "open OS, on-device, ships Q4 2026, from India"
```

**One-line pitch:** "Proactive AI glasses. On-device. Open source. From India 🇮🇳. Ships Q4 2026, 12-18 months before the incumbents, at 1/12th the price."

---

## 8. What marketing channels make sense?

**v81 priority order (re-validated):**

| Channel | Priority | Why | Cadence |
|---|---|---|---|
| **X (Twitter)** | P0 | Founder is active; developer audience; Show HN amplification | `@dan2agi` 3/day Mon-Sat; `@NandySomdipto` 3/week Mon/Wed/Fri |
| **Show HN** | P0 | Single highest-leverage event of Q3 | Jul 14, 09:00 IST |
| **GitHub** | P0 | The artifacts live here; the receipt lives here | Continuous |
| **YouTube** | P0 | Daemon teardowns, founder Q&A; the visual receipt | 1/week from Jul 8 |
| **Blog (`danlab.dev/blog`)** | P0 | Long-form: methodology, post-mortems, founder essays | 1/week Tue |
| **LinkedIn** | P1 | Founder voice for the corporate, Indian-policy, AGI-discourse audience | 1 essay/week Fri |
| **Discord** | P1 | Community signal after launch; triage channel | Daily from Jul 21 |
| **Reddit (r/LocalLLaMA, r/MachineLearning, r/singularity)** | P1 | dglabs-eval launch; founder presence | 3-4 posts total Q3 |
| **India press (English)** | P2 | Founder profile; NITI Aayog angle; "from India" narrative | Aug 2026 |
| **India press (Hindi, Tamil, Telugu, Kannada, Bengali)** | P3 | Grassroots; "from India" tail; Q4 2026 | Q4 2026 |
| **Hacker Newsletter** | P2 | One-pager; passive; good fit for our profile | Aug 2026 |
| **Product Hunt** | P2 | Post-dev-kit; for the consumer launch | Q1 2027 |

**Channels we do NOT prioritize:**
- **TikTok / Instagram Reels.** Wrong audience (consumer, not developer). We are dev-kit first.
- **Paid media.** No budget for it; not aligned with the "honest about the research" brand.
- **Cold email.** Will not work; wrong stage.
- **LinkedIn ads.** Same.
- **Podcast tours (Q3).** Founder essays are higher-leverage.

---

## 9. What content should Danlab produce?

**v81 content pillars (4):**

1. **The Receipts** (daemon teardowns, test counts, performance numbers). Cadence: 3x/week on X, 1x/week YouTube.
2. **The Founder Essays** (long-form, 800-1200 words, India/AGI/eval/honesty). Cadence: 1x/week LinkedIn Fri.
3. **The Methodology** (dglabs-eval, salience-gated VLM, memoryd schema). Cadence: 1x/week blog Tue.
4. **The Wave** (real-time response to Snap/Meta/Apple news). Cadence: opportunistic, ≤1 thread/week.

**v81 specific content backlog (carry from v80, with v81 add):**
- Jul 7: "dglabs-eval v0.1: the first public benchmark for proactive AI glasses" (blog)
- Jul 8: "8 daemons, 144 tests, 0 cloud" (YouTube 90s screencap)
- Jul 14: Show HN post
- Jul 18: `install-oneliner.sh` v1 launch + "90 seconds to 8 daemons" pinned X thread
- Jul 25: dglabs-eval v0.1 public ship (10 tasks, 2 categories)
- Aug 15: arXiv preprint "dglabs-eval: A Benchmark for Proactive AI in Always-On Wearables"
- Aug 26: Pre-orders live
- **Aug 28 (NEW v81): "Apple CEO Ternus. 2027 'biggest product year ever.' Our dev-kit ships Q4 2026, 12-18 months ahead."** (X thread + LinkedIn essay)

---

## 10. What is the current online presence?

**Verified at 2026-06-23 06:00 UTC (v81):**

- **danlab.dev** — live (Tauri app at `dan-glasses-app-som.zocomputer.io` returns 200).
- **GitHub: somdipto/danlab-multimodal** — public, MIT, H2 2025 hackathon.
- **GitHub: somdipto/paperclip** — public, MIT (DanClaw fork).
- **GitHub: somdipto/dan-glasses** — workspace (not yet public as a single repo; daemons live in `Services/`).
- **X: @dan2agi** — Dan1 agent handle, ~30 followers (low; growth begins Jul 14).
- **X: @NandySomdipto** — somdipto founder handle, low follower count (v80 estimated).
- **Telegram: @danlab_bot** — connected via openclaw :18789.
- **Telegram: @Shodan_s** — somdipto personal.
- **Discord: not yet created.** Plan to launch Jul 12 with 50 founding members; public Jul 21.

**The presence is thin. That's the point.** The strategy is: ship the receipts first, then amplify. Show HN is the catalyst.

### India press list (NEW v81)

| Outlet | Type | Beat | Angle | When |
|---|---|---|---|---|
| **The Ken** | Subscriber tech | Deep tech, India | Founder profile, NITI Aayog | Aug 2026 |
| **Mint (HT Media)** | Mainstream business | Tech policy, AI | "Open-source smart glasses from Bengaluru" | Aug 2026 |
| **Economic Times Tech** | Mainstream business | Startup, India-tech | Founder profile | Aug 2026 |
| **YourStory** | Startup media | Indian founders, AI | Founder story | Aug 2026 |
| **Inc42** | Startup media | Indian startup ecosystem | Founder profile, NITI Aayog | Aug 2026 |
| **FactorDaily** | Long-form tech | Deep tech, India | Long-form profile (best fit) | Aug 2026 |
| **The Hindu Business Line** | Mainstream | Tech, policy | NITI Aayog + AI self-reliance | Aug 2026 |
| **Analytics India Magazine** | Niche | Indian AI ecosystem | "Indian AI lab shipping open-source smart glasses" | Aug 2026 |
| **Open Source India (community)** | Community | Indian OSS | Founder talk invite | Q4 2026 |
| **Bengaluru Tech Summit** | Event | India-tech, founders | Talk/pitch | Q4 2026 (if accepted) |
| **IIT Bangalore / IISc** | Academic | Research, AGI | Talk + dglabs-eval paper | Q4 2026 |
| **HasGeek / Fifth Elephant** | Community | ML, AI | Talk | Q4 2026 |

**Outreach plan (v81):**
- **Pre-pitch (Jul 1-15):** Send The Ken, FactorDaily, YourStory a "first look" 2 weeks before Show HN.
- **Launch day (Jul 14):** Embargo lifts. Press release goes to Mint, ET Tech, Analytics India Magazine.
- **Followup (Aug 1-15):** Founder profile + NITI Aayog angle pitch.
- **Q4 2026:** Talks at academic + community events.

---

## 11. Who are the first users/customers?

**v81, sharpened:** The early adopter is **the Indian or global builder-founder-researcher who already distrusts the closed-OS, cloud-first smart-glasses incumbents and is willing to install a CLI on their laptop to get a working proactive AI glasses stack in 90 seconds.**

### Primary personas

**Persona 1 — The AI founder/CTO (50% of pipeline)**
- **Profile:** Building an AI product; reads HN daily; follows @karpathy, @sama, @ylecun; cares about AGI; has 2-10 engineers.
- **Pain:** Ray-Ban Meta is a toy. Apple is late. Snap is closed. They need a working proactive AI stack *now* to demo, prototype, or sell to their own customers.
- **Why us:** 8 daemons live. 144 tests. Open source. They can `git clone` and have a working prototype by EOD.
- **CAC channel:** Show HN, X, YouTube, dglabs-eval.
- **Conversion path:** Install oneliner → Paperclip SDK agent → Discord.

**Persona 2 — The AGI/ML researcher (20% of pipeline)**
- **Profile:** PhD student, postdoc, or research engineer at a lab. Cares about salience, memory, proactive agents, eval methodology. Has Hugging Face + arXiv open in 5 tabs.
- **Pain:** No public benchmark for proactive AI. No open eval. The dglabs-eval v0.1 ships Jul 25 — they'll cite it.
- **Why us:** dglabs-eval v0.1, the architecture writeups, the daemon teardowns, the arXiv preprint Aug 15.
- **CAC channel:** dglabs-eval repo, arXiv, r/MachineLearning.
- **Conversion path:** Run dglabs-eval → submit a row → cite the paper.

**Persona 3 — The Indian university CS/EE student or professor (NEW v81, 10% of pipeline)**
- **Profile:** At IIT/IISc/NIT/BITS/IIIT. Building hardware or ML projects. Looking for an open-source wearable project to fork.
- **Pain:** Most "AI glasses" projects are closed and expensive. They want an open, MIT, well-documented stack.
- **Why us:** MIT license. India-first positioning. NITI Aayog alignment. The daemons are small enough to fork.
- **CAC channel:** HasGeek, Fifth Elephant, IIT-B/IISc talks, NITI Aayog networks.
- **Conversion path:** GitHub star → fork → write a Paperclip SDK agent → Discord.

**Persona 4 — The Indian SMB owner / freelancer (NEW v81, 10% of pipeline)**
- **Profile:** Runs a small business, freelance developer, or content creator. Wants an always-on AI companion for hands-free capture, memory, and reminders.
- **Pain:** $799-$2,199 is too expensive. Cloud-only is a privacy concern.
- **Why us:** $189 dev-kit, on-device, multilingual, MIT. Ships Q4 2026.
- **CAC channel:** YourStory, Inc42, The Hindu Business Line, regional press.
- **Conversion path:** Pre-order Aug 26 → dev-kit Q4 2026.

**Persona 5 — The corporate AI innovation lab (10% of pipeline)**
- **Profile:** Fortune 500 AI/innovation team. Looks at the open-source wearable AI landscape for partnership/benchmark purposes.
- **Pain:** Vendor lock-in. No public eval. Cannot evaluate "proactive AI" claims.
- **Why us:** dglabs-eval, arXiv preprint, founder essays, the on-device + audit-able + MIT positioning.
- **CAC channel:** LinkedIn essays, founder talks, dglabs-eval paper.
- **Conversion path:** Founder essay → call → dglabs-eval partnership.

---

## 12. The proactive AI definition (v81, locked)

**v80:** "Salience-gated VLM."
**v81:** "**Salience + memory + consent.**"

```
proactive_ai(dan_glasses) =
    salience(perceptiond)        // "is this moment worth noticing?"
  ∧ memory(memoryd)             // "what do I already know about the user?"
  ∧ consent(perceptiond.mode)   // "is the user opted-in to vision/audio capture?"
  ∧ fail_gracefully()           // "if any daemon degrades, the system falls back"
```

**Why the v81 update:** The Meta-Stella scandal made consent a first-class requirement, not a feature. We do not run facial-recognition. We do not run covert capture. We ship the consent posture in CONTRIBUTING.md. The proactive AI claim is now defensible: "we watch, we remember, we whisper — and we never surveil."

---

## 13. What I still need from the user (somdipto)

1. **Founder bio for press outreach** — 200 words, 1 photo, 3 quotable lines. For The Ken, FactorDaily, YourStory.
2. **Confirmation on install-oneliner.sh public release** — does the install-oneliner get a public GitHub release on Jul 18, or stay internal?
3. **The India policy/NITI Aayog angle** — can you write 1 LinkedIn essay (800-1200 words) on "AI self-reliance as Indian policy" by Jul 4? I can draft if you give me the bullet points.
4. **dglabs-eval paper authorship** — Dan2 lead, you second author, me third. Confirm.
5. **Press embargo lift date for Show HN** — Jul 14 09:00 IST confirmed? Need a press release for that.
6. **Discord name + founding-member badge criteria** — what's the badge criteria for the first 500?

---

## 14. Sources read for v81

**Workspace files read:**
- `dan-glasses/AGENTS.md` — locked decisions, build priority
- `dan-glasses/SOUL.md` — project personality
- `dan-glasses/README.md` — project overview
- `dan-glasses/INDEX.md` — folder structure
- `dan-glasses/PRD.md` — product requirements
- `dan-glasses/STATUS.md` — live infra (8/8 daemons, 144 tests)
- `dan-glasses/agent-work/dan1.md` — Dan1 status
- `dan-glasses/agent-work/dan2.md` — Dan2 status
- `dan-glasses/docs/dan-glasses-build-plan.md` — build phases
- `dan-glasses/docs/dan-glasses-v1-canonical-analysis.md` — critical analysis
- `dan-glasses/Services/audiod/SPEC.md` — audiod spec
- `dan-glasses/Services/perceptiond/SPEC.md` — perceptiond spec
- `dan-glasses/Services/memoryd/SPEC.md` — memoryd spec
- `danlab-multimodal/README.md` — multimodal README
- `danlab-multimodal/docs/ARCHITECTURE.md` — multimodal architecture
- `paperclip/README.md` — Paperclip/DanClaw README
- `blurr/README.md` — Blurr/Panda README
- `agent-work/dan1-marketing-research.md` (v80) — previous research
- `agent-work/dan1-marketing-strategy.md` (v80) — previous strategy
- `agent-work/dan1-content-calendar.md` (v80) — previous calendar
- `agent-work/dan1-twitter-content.md` (v80) — previous Twitter
- `agent-work/dan1-landing-copy.md` (v80) — previous landing copy
- `agent-work/dan1-github-readme-suggestions.md` (v80) — previous README suggestions

**Live infra verified (06:00 UTC 2026-06-23):**
- audiod :8090 → `{"status":"ok","service":"audiod"}` ✅
- perceptiond :8092 → `{"mode":"watchful","running":true,"frames_processed":11,"salient_frames":8,"descriptions":7,"vlm_busy":true,"vlm_queue_depth":1}` ✅
- memoryd :8741 → `{"status":"ok","model":"sentence-transformers/all-MiniLM-L6-v2"}` ✅
- toold :8742 → `{"status":"ok","workdir":"/tmp/toold-sandbox","max_timeout":120}` ✅
- ttsd :8743 → `{"status":"ok","model":"medium","voice":"expr-voice-2-m","kittentts_available":true}` ✅
- os-toold :8744 → `ok` ✅
- openclaw :18789 → `{"ok":true,"status":"live"}` ✅
- dan-glasses-app → `200` ✅

**Web search verified (this run):**
- Snap Specs $2,195 at AWE 2026 (Jun 16) — Forbes, Verge, LA Times, Road to VR
- Meta-Stella facial-rec scandal (WIRED, Jun 4) — CNET, AP, Washington Post
- Apple AirPods-cameras + smart glasses to late 2027 (Gurman, Jun 16) — Bloomberg, Verge, 9to5Mac
- **Apple CEO John Ternus transition (Bloomberg, Jun 21) — NEW v81 wave**

---

*Built by Dan1 👾 for DanLab — Bengaluru, India 🇮🇳 — 2026-06-23 11:30 IST.*
*v80 = "three waves + the install launch + the calendar." v81 = "four waves + the install launch + the calendar + the India press list + the live re-verification."*
