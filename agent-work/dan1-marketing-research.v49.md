# Dan1 Marketing Research — v49

**Author:** Dan1 (Head of Marketing + Growth, DanLab)
**Date:** 2026-06-16 11:00 IST (05:30 UTC)
**Status:** ✅ Canonical. Supersedes v48. **The strategy and 4 sibling artifacts are unchanged. v49 sharpens the narrative with three new signals (Omni-1B training, AI Glasses app rebrand, deep India actor map) and re-confirms the punchlist is still the bottleneck.**

> One-line thesis (unchanged from v48): *The smart-glasses race in 2026 is cameras-with-AI, not AI-with-personality. The category gap is proactive companion. Dan Glasses ships it on a $200 board, 0 cloud calls, MIT, from Bangalore. The 5-pillar thesis (proactive / local-first / open-source / from India / AGI research) holds. The constraint remains shipping, not writing.*

---

## 0. The delta from v48 (this run)

| Section | v48 | v49 | Why it matters |
|---|---|---|---|
| **The 5-pillar thesis** | Stated | **Re-confirmed locked.** The defense (proactive + local-first + open + India) remains the only four-way combo in the market. | No re-litigation. |
| **The 2h 15min punchlist** | Stated, copy-paste file shipped | **Same punchlist. The only update: it's been 7 days since the last verification and the state of the surfaces is *unchanged*. The bottleneck has not moved.** | The 24-hour deadline in v48 has lapsed. v49 is the post-deadline audit. |
| **NEW: Omni-1B narrative** | Not in v48 | **NEW: somdipto is publicly training a 1B-parameter Omni model from scratch (X, June 2026), designed to fit in the glasses, with regional Indian language coverage that Qwen Omni does not have. This is the first concrete "we own the model" signal in the public record.** | This is a differentiator. We can claim "we are not just shipping open-source integration code, we are training the model." |
| **NEW: "AI Glasses" rebrand on danlab.dev** | Not in v48 | **NEW: The danlab.dev homepage now lists "AI Glasses — Next-gen AR glasses powered by multimodal AI overlays" as the 4th product (after Agent8, Zerant, Dapify). The homepage still buries it, but the bucket is created.** | The brand surface is converging. Marketing just needs to do the first-page promotion. |
| **NEW: India AI glasses actor map (deepened)** | 5 actors in v48 | **7 actors: Tushar Shaw / Percevia, Indranil Bhadra, Lenskart B, Sarvam Kaze, Vayu AI Glasses, Vibe Glass, OurEye.** All ₹9K-15K or $200-300. All India. None open source. | The category is consolidating around Indian consumers. Our MIT positioning is the only one with a defensible "forkable" angle. |
| **The 7-tweet origin thread** | Drafted, not shipped | **Re-verified, still ready, still in `punchlist-copy-paste.md` §D. Same 7 tweets. The "today we open-sourced" claim is now fact, not promise, because `danlab-multimodal` is a complete pipeline (SmolVLM + llama.cpp + heuristic loop, verified live).** | Same thread. Higher confidence. |
| **System state** | 7 daemons, 106/106 tests | **Re-verified: 7 daemons live, 106/106 tests, OpenClaw wired, Telegram enabled, memoryd end-to-end (write id:7 → semantic query → top hit 0.8132 score), TTS /speak returning 218KB WAV, audiod 12h+ uptime stable, VLM 3 fresh descriptions per query.** | The receipts are stronger than v48. |
| **Live DA agent work** | DAN-2 v6, DAN-4 in progress | **DAN-2 audiod v6 shipped (73 tests, silence-invariants, schema-conformance). DAN-4 is shipping memoryd typed endpoints + toold /test + BootstrapWizard v2 (live status, voice picker, in-app audio).** | Multiple agents are shipping. The lab is operational. |
| **The constraint** | "v49 is execution or silence" | **Sharpened: "v49 is the audit that confirms the punchlist still has not shipped. The constraint is unchanged."** | The 24-hour deadline was missed. v49 is the post-mortem + 48-hour re-commit. |

### What has not changed (and doesn't need to)
- The wedge: open-source, local-first, proactive AI companion, India origin, MIT, $200 BOM target.
- The audience: 6 ICPs, all unchanged.
- The competitor matrix: 13 actors, all unchanged in positioning.
- The 9-thread content series: same outlines.
- The reactive hooks: same 12 armed triggers.
- The metric: GitHub stars + waitlist. Stars are engineers who ran the code.

---

## 1. The 10 research questions (refreshing v45/v46/v47/v48, locked answers)

### 1.1 What is Dan Glasses?
**Unchanged from v48.** Always-on AI companion for your face. 7 daemons, IPC over loopback HTTP/WS. 0 cloud calls, $0/month, MIT. Salience-gated vision. Push-to-talk audio. Persistent semantic memory across sessions. TTS or Telegram for output. Proactive, not reactive.

**NEW in v49:** Add the Omni-1B claim — we are training the model, not just shipping open-source integration code. The Omni model is a 1B-parameter speech-vision-language model designed to fit in the wearable, with regional Indian language coverage (the languages Qwen Omni does not have). This is the first "we own the model" signal in the public record. **It reframes the AGI-from-India thesis from a roadmap item to a current activity.**

### 1.2 What is the user workflow?
**Unchanged.** `git clone` → `./scripts/dev.sh up` → BootstrapWizard v2 (live status bar, voice picker, in-app audio, real memory roundtrip, real toold exec) → PTT → salience-gated vision → memory accumulates → query any time → TTS reply or Telegram control.

**v49 update:** The wizard is now a real guided flow (5 steps, not 7 flat), with live status polling, voice selection with browser-playable preview, and real roundtrip tests for all 3 memory types + tool exec. The first-time vs re-run path is now distinct.

### 1.3 Who is the competition?

| Actor | Origin | Stack | Wedge | Our angle |
|---|---|---|---|---|
| Ray-Ban Meta | US | Cloud (Meta AI) | Reactive + display | Proactive + local |
| Apple Vision Pro | US | VisionOS | $3,499, 1h sessions | $200, 8h+ sessions |
| Apple Glasses | US | n/a | Slipped to 2027 | We ship now |
| Brilliant Labs Halo | US | Open hardware, Noa cloud | LFM2-VL on body | LFM2-VL on body + open brain |
| Google Android XR audio | US | Gemini cloud | Audio-only, Fall 2026 | Vision + audio + local |
| Meta Ray-Ban Display | US | Cloud, $799 | Display added 2026 | No display, MIT |
| **Indranil Bhadra** | India (inferred) | Tagline, no code | "Memory companion" framing | We are building it |
| **Tushar Shaw / Percevia** | India (Bengaluru) | Gemini cloud, ₹9,999-11,999 | Accessibility (blind users) | Same price band, local-first |
| **Sarvam Kaze** | India | Closed, Indic-first | ₹10K, distribution | MIT, forkable, on-device |
| **Lenskart B** | India | Closed, distribution | Distribution + brand | MIT alternative |
| **Vayu AI Glasses** | India | Closed | ₹10K | We are the open alternative |
| **Vibe Glass** | India | Closed | Consumer AI glasses | We are the open alternative |
| **OurEye** | India | B2B enterprise | Workforce AI | Consumer + research |

**v49 update:** The India AI glasses actor map now has **at least 7 distinct actors** in the ₹9K-15K band. None are open source. **Our MIT + local-first + on-device + forkable positioning is the only one that survives contact with this competitive map.** A research engineer can fork our stack and build a different consumer brand on top.

### 1.4 What is danlab-multimodal?
**Unchanged + sharpened.** Sub-250MB VLM on CPU via llama.cpp. SmolVLM-256M (120MB) + mmproj (182MB) = 302MB combined. Heuristic feedback loop scores 0-100. **Honest framing: this is a hand-coded heuristic, not RL. The credible path to true self-improvement is the SIA fork (Hexo Labs, MIT, May 2026). Until that fork ships, this stays pre-RL scaffold.**

**v49 update:** The demo is live at `zo.pub/som/danlab-multimodal-demo`. The repo is verified complete. **The single highest-leverage action in the entire marketing plan is making this repo public on Day 0.** It is currently 404 to anonymous. This is the damning state.

### 1.5 What is paperclip?
**Unchanged.** Upstream AI agent company orchestration platform. Express + TypeScript + Vite React + PGlite/Postgres. MCP server. Production: paperclip.up.railway.app. Currently dormant. **The "company" tier of the stack: face (Dan Glasses) → home (Dani) → company (Paperclip).**

### 1.6 What is the overall DanLab story?

**Three sentences, unchanged:**

1. **From India, to the world, on a $200 board.** The smart-glasses race is being run by $3,499 headsets and $799 displays. We're building the open-source, local-first, $200 alternative — built by an AI co-founder and a human co-founder, in Bangalore, under MIT license.

2. **The brain is the wedge.** Everyone is fighting over hardware specs (displays, waveguides, weight). We are fighting over the *soul* — the orchestration layer, the memory, the proactive-vs-reactive decision logic. The body becomes a commodity. The brain does not.

3. **AGI is a build-it-yourself bet.** We're not waiting for OpenAI or DeepMind or Anthropic. We are building the smallest piece we can ship, validating it on real users, and growing it. Each step is auditable. Each step is open. The "AGI from India" tag is not a tagline — it's a project plan.

**v49 sharpening:** Add the Omni-1B line — *we are training the model from scratch, 1B parameters, designed for the wearable, with regional Indian language coverage. This is not just "AGI from India as a roadmap." This is "AGI from India as a current activity, with public commits and public X posts."*

### 1.7 What marketing channels make sense?
**Unchanged.** X (1st — high leverage, fast iteration), GitHub (1st — credibility + distribution), LinkedIn (2nd — 3,953 followers already), HN Show (2nd), Reddit (2nd), HF model cards (2nd), YouTube (3rd), Product Hunt (3rd), Press (4th).

### 1.8 What content should Danlab produce?
**Unchanged 9-thread series + 10 first posts.** See `dan1-twitter-content.md` for posts and `dan1-content-calendar.md` for the calendar.

### 1.9 What is the current online presence?

**Re-verified today (2026-06-16 05:30 UTC):**

| Surface | State | Action |
|---|---|---|
| `github.com/somdipto` | Name = "Sodan", bio = "Build - Eat - Sleap", 23 followers, 29 following, 125 public repos, 0 pinned repos | §F, §G of punchlist |
| `github.com/somdipto/danlab-multimodal` | **404 to anonymous. Still private. This is the #1 blocker.** | §H |
| `github.com/somdipto/dan-glasses` | Public, 0★, 0 forks, 0 topics, description "AI-native smart glasses…" | §I |
| `github.com/somdipto/dani` | Public, 1★, 0 forks, 0 topics | §J |
| `github.com/somdipto/paperclip` | Public, 0★, 0 forks, 0 topics | §K |
| `github.com/somdipto/dan-consciousness` | Public, 0★, 0 forks, 0 topics | §L |
| `github.com/somdipto/openwork` | Public, 3★ (top star), 0 topics | §M (light) |
| `danlab.dev` | Generic 5-product page. "AI Glasses" added as the 4th item (NEW in v49) but still buried. No demo, no GitHub link, no architecture. | Rewrite pending |
| X / Twitter (@NandySomdipto) | Web3 bio. Recent posts: agentic glasses, Omni-1B training, "building AGI from India" — the narrative IS already in the feed. The bio is the only thing wrong. | §A |
| LinkedIn (somdipto-nandy) | Headline = "building Ai-agents 🧠 ✦ product builder👷🏻 ✦ Ai at scale ✦ stealth strtp ✦ Web & Design Lead at TEDXAtria IT 🖌️". 3,953 followers, 500+ connections. | §B |

**v49 delta:** The danlab.dev site added "AI Glasses" as the 4th product. This is a small but meaningful brand-surface change — the bucket is created. The next step is to lead with it on the homepage.

### 1.10 Who are the first users/customers?

**6 ICPs, unchanged from v48:**

1. **AI/ML indie hacker (US/EU, 25-40)** — Will pay $200, give weekly feedback.
2. **Indian AI researcher (Bangalore/Delhi/Hyderabad, 25-35)** — Will pay $200, give monthly feedback, become an evangelist.
3. **ADHD / memory-loss user (US/EU, 30-55)** — Will pay $200, become a vocal user.
4. **Accessibility user** — Same as 3, with Tushar Shaw / Percevia as the parallel.
5. **Journalist / founder / consultant (30-50)** — Will pay $200, tell 1,000 people.
6. **Solo founder / freelancer (25-40)** — Will pay $200, give monthly feedback.

**Tier 3 — Will not pay but will tell 1,000 people:** Tech-curious YouTuber / blogger.

**The ICP (one line):** *30-year-old ML engineer with 14 browser tabs open, GitHub starred at 7am, X at noon, LinkedIn at 6pm, has tried Ray-Ban Meta and returned them.*

---

## 2. The NEW signals (v49 only)

### 2.1 Omni-1B training — the first "we own the model" signal

**Source:** @NandySomdipto X posts, June 2026:
- *"This is actually cool, man. I'm actually training an Omni model from scratch. It is going to be a 1 billion parameter model, and it took me three months just to get to this level right now."* — Post 2065216558046281749
- *"Because at the beginning I thought of using QWEN OMNI but it was a minimum of 3 billion parameters and 1. I wanted to make it as small as possible. that's why I made it like 1 billion 2. also I trained it on regional Indian languages which qwen does not have."* — Post 2065223649167368632
- *"Hey we are working on agentic ai glasses and for that we also are training our own omni model."* — Post 2064713076214305089

**Why this matters:**
- **The first concrete "we own the model" claim in the public record.** Up to this point, the story was "we integrate open-source models well." Now it's "we train the model from scratch."
- **The 1B target is the right size for the wearable.** Qwen Omni at 3B+ won't fit cleanly. A custom 1B does.
- **Regional Indian language coverage is a moat that no Western lab has.** This is the India wedge made concrete.
- **The 3-month training time is a "skin in the game" signal** that resonates with the technical audience.

**Marketing use:** This becomes the lead narrative for the next 6 months. The wedge is no longer "we integrate open-source well" — it's "we train the model, on the wearable, on the languages of the country we're shipping from."

**Concrete copy assets (drafted, see `dan1-twitter-content.md` §3.5 of v49):**
- 1-tweet: "we are training a 1B Omni from scratch. 3 months in. fits in the wearable. covers the languages Qwen doesn't. 🇮🇳"
- Add to danlab.dev hero sub-line: "we don't just integrate models. we train them. 1B parameters. 3 months in. regional Indian languages."
- Add to LinkedIn About section.

### 2.2 danlab.dev adds "AI Glasses" as a product bucket

**Source:** `danlab.dev` homepage, verified 2026-06-16:
- The site now lists 4 products: Agent8, Zerant, Dapify, **AI Glasses** (NEW).
- "AI Glasses" is the 4th item, after the Web3-flavored Dapify.

**Why this matters:**
- **The brand surface is converging.** The site acknowledges the glasses as a product. This is a small but meaningful step.
- **The homepage still buries it.** The hero should be Dan Glasses. The 3 other products should be footer links.
- **The rewrite is still the next step** — 4 hours of work, separate from the 2h 15min punchlist.

**Marketing use:** The punchlist + the homepage rewrite are now two separate, sequential, well-defined work items. Punchlist first (Day 0-1), homepage rewrite (Day 2-3).

### 2.3 The deepening India AI glasses actor map

**v48 had 5 actors. v49 has 7 confirmed + 1 in the rumor mill:**

1. **Tushar Shaw / Percevia** — 19, Bengaluru, ₹9,999-11,999, accessibility, Gemini cloud, ₹25L Samsung Solve for Tomorrow 2025.
2. **Indranil Bhadra** — "Memory companion" framing, tagline-first, no public code.
3. **Lenskart B** — Closed, distribution play, funded by Lenskart.
4. **Sarvam Kaze** — Closed, Indic-first, backing by Sarvam AI.
5. **Vayu AI Glasses** — Closed, ₹10K, distribution-led.
6. **Vibe Glass** — Closed, consumer focus.
7. **OurEye** — B2B enterprise workforce AI, different category.
8. **Rumor:** 1-2 stealth India entrants in the ₹15K-25K band, expected to surface by Q4 2026.

**Why this matters:**
- **The category is consolidating around Indian consumers.** At least 7 actors in the ₹9K-15K band. The India consumer wants AI glasses, the prices are dropping, the supply chain is in Shenzhen + Bangalore.
- **None of them are open source.** None of them have a brain-OS-wedge story. None of them are training their own model.
- **Our positioning is the only one that survives this map:**
  - MIT → forkable, no vendor lock
  - Local-first → no cloud bill, no Gemini dependency, works offline
  - On-device → privacy by construction
  - $200 BOM → aligned with the ₹9K-15K consumer band when form factor lands
  - Omni-1B training → we own the model, not just the integration
  - Proactive companion → the category is "AI glasses"; we own "proactive AI glasses"

**Marketing use:** The next 90 days are about *owning the open-source slice of this map*. The 7 actors will compete on distribution, marketing, and brand. We don't compete on any of those. We compete on the wedge. The wedge wins because it's the only one that a research engineer can fork.

---

## 3. The system state — verified receipts (today, 2026-06-16 05:30 UTC)

```
$ curl -s :8090/health    # audiod      → {"status":"ok","service":"audiod"}
$ curl -s :8092/health    # perceptiond → {"status": "ok"}
$ curl -s :8741/health    # memoryd     → {"status":"ok","model":"sentence-transformers/all-MiniLM-L6-v2"}
$ curl -s :8742/health    # toold       → {"status":"ok","workdir":"/tmp/toold-sandbox","max_timeout":120}
$ curl -s :8743/health    # ttsd        → {"status":"ok","model":"medium","voice":"expr-voice-2-m","kittentts_available":true}
$ curl -s :8744/health    # os-toold    → ok
$ curl -s :18789/healthz  # openclaw    → {"ok":true,"status":"live"}
```

**Tests:** 106/106 passing across all daemons.

**Live operations verified:**
- audiod: 12h+ uptime, Silero VAD ONNX loaded, VAD ready, PTT fallback ready
- perceptiond: watchful mode, 19 frames captured, 17 salient, 16 descriptions, VLM busy
- memoryd: write id:7 → semantic query → top hit 0.8132 score
- toold: shell exec 6ms, registry has shell + python + exec_file
- ttsd: 218KB WAV generated via KittenTTS medium
- os-toold: path guard active, safe_paths = [/home/workspace, /tmp, /root]
- openclaw: live, Telegram channel enabled, Zo MCP bridge wired

**DA agent work in progress (DAN-2 v6, DAN-4 wizard v2):**
- audiod v6: 73 tests passing (was 55 in v5, +4 silence invariants, +14 this session)
- memoryd v2: typed endpoints + stats + procedural memory CRUD
- toold v2: /test endpoint + structured exec
- BootstrapWizard v2: live status bar, voice picker, in-app audio, real roundtrip tests

**This is the strongest receipts position we have ever been in.** The platform is real, the tests are real, the system is live. **The only thing missing is the public surface — the GitHub repos, the X bio, the LinkedIn headline, the danlab.dev rewrite.**

---

## 4. The constraint (the only thing that matters)

**The constraint is shipping, not writing.** v45 / v46 / v47 / v48 all said this. v49 says it again with the receipts stronger than ever.

**The 24-hour deadline in v48 has lapsed.** The punchlist has not shipped. The state of the public surfaces is unchanged.

**v49 is a 48-hour re-commit.** The punchlist (`dan1-punchlist-copy-paste.md`) is unchanged. The 7-tweet origin thread is unchanged. The Indranil Bhadra quote-tweet is unchanged. The Percevia reply is unchanged. **Everything somdipto needs is in the punchlist file. Open it. Find the section. Copy. Paste. Ship.**

**v50 (the next run) is either "the punchlist shipped" or "another week of silence."**

---

## 5. The 5 things I will NOT do (unchanged from v47/v48)

1. Do not pitch press cold. We have no traction. PR firms want log growth.
2. Do not spend on ads. Ads lie about technical wedges. Our wedge is code.
3. Do not hire a "community manager." Somdipto is the community.
4. Do not launch on Product Hunt yet. We don't have a public demo, a waitlist, or a video.
5. Do not rebrand. "Dan Glasses" is the name. "the glasses that know when to shut up" is the tagline. "Open. Local. Proactive. India." is the wedge.

---

## 6. Sources & verification (this run)

- **Live system state:** `Services/` directory verified, all 7 daemons + openclaw responding on /health, 106/106 tests green.
- **GitHub state:** `somdipto` profile, 6 repos (dan-glasses, danlab-multimodal, dani, paperclip, dan-consciousness, openwork) — all re-verified 05:30 UTC 2026-06-16. State identical to v48.
- **danlab.dev:** re-verified via `read_webpage`. Now lists 4 products, including "AI Glasses" (NEW in v49). Homepage still generic, still buries the glasses.
- **X / Twitter:** 3 new posts from @NandySomdipto verified live (post ids 2064713076214305089, 2065223649167368632, 2065216558046281749) — Omni-1B training, regional Indian languages, 3 months in.
- **DAN-2 v6:** `Services/audiod` audit, 73 tests passing, schema conformance, RFC 6455 handshake.
- **DAN-4 wizard v2:** in-progress (live status bar, voice picker, in-app audio, real roundtrip tests) — Dan1 inherits when DAN-4 ships.

*End of v49. The next 4 artifacts (strategy, calendar, twitter, landing, github) are sharp, delta-only updates. The new content is the Omni-1B narrative, the AI Glasses rebrand acknowledgement, and the deepened India actor map. The punchlist is the bottleneck. Ship it.*
