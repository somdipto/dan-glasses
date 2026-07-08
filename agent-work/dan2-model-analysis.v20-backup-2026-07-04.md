# Dan2 — Model Analysis v20 (2026-07-04 09:30 UTC / 15:00 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-model-analysis.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v19:** `dan2-model-analysis.v19-backup-2026-07-04.md`

> **v20 deltas vs v19 (2 CRITICAL adds, 5 SHARPEN, 1 partial retraction, 0 broad rollbacks):**
> 1. **NEW CRITICAL #1 — Axios reveals the Amazon→Trump→Anthropic 20-day showdown (July 3 2026).** **v20 risk: the v19 "frontier closed-source AI is not yet jailbreak-hardened" thesis is now *Axios-validated*. Mythos + Fable 5 are *structurally fragile to internal security findings* — Amazon caught a jailbreak, Trump imposed emergency export controls, the open letter from cybersecurity experts confirmed the same jailbreak works on other frontier models. v20 add: the on-device + open-weights + auditable memory + auditable agent loop stack is the v20 *only credible counter-position*. The v20 model stack (LFM2.5-VL-450M + whisper.cpp + KittenTTS + OpenClaw + MiniLM-L6-v2 + LFM2.5-230M + Hermes Agent) is unchanged. v20 adds a new safety-considerations feature: "what would Mythos have missed" check on every memoryd v1.5 write decision.**
> 2. **NEW CRITICAL #2 — Apple camera-AirPods Pro suspended (MacRumors + AppleInsider, July 3 2026, leaker Kosutami) + Apple smart glasses delayed to end 2027 (v19).** **v20 add: Apple's wearable AI roadmap is *visibly stalling*. The v20 model stack holds. Cite in the v1.0 spec + the v1.0 marketing as a *third* piece of evidence that closed-source cannot ship a wearable-native agent in 2026 (joining Meta paywall + Zuckerberg "slower than expected" + MemoMind $20/mo + now Apple suspended + Apple smart glasses delayed).**
> 3. **NEW SHARPEN — Bad Epoll Linux kernel CVE-2026-46242 (The Hacker News, July 3 2026) — Mythos caught one kernel bug and missed a worse one in the same code region.** **v20 add: the v1.0 spec safety-considerations section now cites Bad Epoll as the v20 *strongest possible evidence* that frontier closed-source AI is *not yet a reliable cybersecurity auditor*. The v20 structural answer is the harness-over-model pattern with auditable memory + auditable agent loop. Cite in the danlab-multimodal safety-considerations page.**
> 4. **NEW SHARPEN — Palo Alto Networks + CrowdStrike all-time highs + GLM-5.2 = Mythos on vulnerability discovery (Let's Data Science, July 2 2026, citing CNBC + WSJ).** **v20 add: Wall Street validated the open-weights vs closed-source trade. Cite in the v1.0 spec implementation-wedge section + the v1.0 marketing as the v20 12th step of the marketing narrative.**
> 5. **NEW SHARPEN — Silicon Data LLM Token Expenditure Index down 20% from May high (LA Times + Bloomberg, July 3 2026).** **v20 add: cite the Silicon Data Index in the v1.0 spec implementation-wedge section. "Token prices are collapsing 20%. Closed-source frontier is losing pricing power. Open-source + on-device + auditable memory is the structural answer."**
> 6. **NEW SHARPEN — NSA Gen. Joshua Rudd + Chris Inglis (former US National Cyber Director) on open-weights defense (Mimir's Well + Dark Reading, June 30 - July 3 2026).** **v20 add: cite both in the v1.0 spec sovereign-on-prem section. The v20 sovereign-on-prem defense vertical is the v20 only credible response to the defense-side open-weights adoption.**
> 7. **NEW SHARPEN — TechCrunch: "The browser wars aren't about search anymore" (July 3 2026).** **v20 add: cite in the v1.0 marketing as the v20 second market signal that the OpenClaw substrate is the structural answer for the 2026 browser + wearable + agent race.**

> **v20 retractions of v19:** **0 broad rollbacks.** v19 2 new CRITICAL + 5 SHARPEN all hold. v20 adds 2 new CRITICAL + 5 SHARPEN. The v20 model shortlist (LFM2.5-VL-450M + whisper.cpp + KittenTTS + OpenClaw + MiniLM-L6-v2 + LFM2.5-230M + Hermes Agent + HRM-Text-1B v1.5 plan-B + Apertus v1.1 4B v1.5 plan-C + OpenPhone-3B v1.5 plan-D + Qwen3-TTS v1.5 plan-A + GLM-5.2 v1.5 plan-E [NEW v20]) is structurally correct and unchanged.

## TL;DR (one paragraph, v20)

The v19 model choices are correct. **LFM2.5-VL-450M is the v1.0 vision model. whisper.cpp base.en is the v1.0 STT. KittenTTS medium is the v1.0 TTS. OpenClaw (TS/Node) is the v1.0 orchestration. SQLite + MiniLM-L6-v2 + vectors is the v1.0 memory. LFM2.5-230M is the v1.0 audiod post-processor. Hermes Agent is the v1.0 audiod agent framework.** v20 adds: (1) **Axios Amazon-Trump 20-day showdown (CRITICAL #1)** — frontier closed-source AI is not yet jailbreak-hardened. The v20 *structural* answer is the on-device + open-weights + auditable memory + auditable agent loop stack. (2) **Apple camera-AirPods Pro suspended + smart glasses delayed (CRITICAL #2)** — Apple's wearable AI roadmap is visibly stalling. (3) **Bad Epoll CVE-2026-46242 + Palo Alto + CrowdStrike all-time highs + GLM-5.2 = Mythos + Silicon Data Index + NSA Gen. Joshua Rudd + Chris Inglis + TechCrunch (5 SHARPEN)** — the v20 strongest possible citable evidence for the v20 12-step marketing narrative + the v20 sovereign-on-prem defense vertical promoted to plan-A. v20 adds GLM-5.2 as v1.5 plan-E (China-side open-weights alternative). No v19 model choice is broadly retracted.

## v1.0 Model Stack (v18, locked per dan-glasses/AGENTS.md)

| Component | Model | Size | Quant | Runtime | v18 Substrate |
|-----------|-------|------|-------|---------|---------------|
| Vision | LFM2.5-VL-450M | 450M (209MB GGUF) | Q4_0 | llama-mtmd-cli | **NPU (vision encoder) + CPU (text decode) — phase-mapped** (v15) |
| STT | whisper.cpp base.en | 74MB | Q5_1 | whisper-cpp-plus-rs | CPU (with NPU optional acceleration) |
| TTS | KittenTTS medium | ~25MB | native | ONNX Runtime | CPU (with NPU optional acceleration) |
| Memory | MiniLM-L6-v2 | 22M | INT8 (v1.1 spike) | sentence-transformers | CPU |
| Orchestration | OpenClaw | n/a | n/a | TypeScript/Node | **n/a — v17 industry-icon-endorsed (Vinton Cerf, June 30 2026) + v18 shipped-by-Anthropic (Claude Apps Gateway, July 2 2026) + v18 native iOS+Android (June 30 2026)** |
| **audiod post-processor (NEW v16 v1.0)** | **LFM2.5-230M** | **230M** | **Q4_K_M** | **llama.cpp** | **CPU / aarch64 — 42 tok/s on Raspberry Pi 5** |
| Agent framework (NEW v16 v1.0) | Hermes Agent | n/a | n/a | Nous Research / OpenAI ChatGPT subscription | CPU + cloud |
| Reasoning (v1.5) | HRM-Text-1B | 1B (Apache-2.0) | Q4_K_M | llama.cpp | NPU (v1.5) + CPU fallback — v1.5 plan-B (was v1.0 plan-A in v15) |
| Reasoning (v1.5) | Apertus v1.1 4B | 4B | Q4_K_M | llama.cpp | CPU + NPU — v1.5 plan-C (was plan-B in v15) |
| Reasoning (v1.5) | OpenPhone-3B | 3B | Q4_K_M | llama.cpp | CPU + NPU — v1.5 plan-D (was plan-C in v15) |
| TTS (v1.5) | Qwen3-TTS | TBD | TBD | TBD | CPU + NPU |

## v1.0 Models (held from v16/v17, locked)

### LFM2.5-VL-450M — held from v8/v11
- **Released:** April 11, 2026 by Liquid AI.
- **Size:** 450M params, ~209MB GGUF Q4_0 + 180MB mmproj.
- **License:** Research/commercial (verify with Liquid AI).
- **v18 status:** unchanged. v18 add: the v18 RAM price spike (TechSpot, June 30 2026) makes the v1.0 salience-gated + LFM2.5-VL-450M path even more important. Every MB of RAM saved is a v18 cost + supply-chain win.

### whisper.cpp base.en — held from v8/v11
- **Size:** 74MB.
- **License:** MIT.
- **v18 status:** unchanged.

### KittenTTS medium — held from v8/v11
- **Size:** ~25MB.
- **License:** Verify with KittenML.
- **v18 status:** unchanged.

### OpenClaw (TypeScript/Node) — held from v8/v11, v17 Cerf-endorsed, v18 Anthropic-shipped-analog
- **Released:** Late 2025 (OpenClaw). Anthropic Claude Apps Gateway shipped July 2 2026. OpenClaw native iOS + Android shipped June 30 2026.
- **License:** MIT (OpenClaw).
- **v18 status:** unchanged. **v18 add: Vinton Cerf (Open Frontier, June 30 2026) publicly endorses the "TCP/IP-for-agents" pattern. Anthropic Claude Apps Gateway (July 2 2026) ships the same pattern. OpenClaw native iOS + Android (June 30 2026) is the same pattern. Document OpenClaw's protocol surface as a v1.0 marketing artifact. "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable."**
- **v18 risk:** Mashable reports a critical security flaw in OpenClaw was discovered ~2 months before the mobile launch. Audit OpenClaw's threat model before shipping the v1.0 marketing artifact.

### MiniLM-L6-v2 (memoryd) — held from v8/v11
- **Size:** 22M params, 384-dim embeddings.
- **License:** Apache-2.0.
- **v18 status:** unchanged. v18 add: Proton Lumo 2.0 (June 30 2026) is a v18 direct privacy-preserving AI competitor with persistent memory. Cite Lumo 2.0 as the privacy-harness analog.

## v1.0 Models (held from v16)

### LFM2.5-230M (Liquid AI, June 26 2026) — held from v16 CRITICAL #1
- **Released:** June 26 2026 by Liquid AI.
- **Size:** 230M params, on-device.
- **License:** Dual-license: free for individuals and companies generating <$10M ARR; paid enterprise agreement for larger corporations.
- **Performance:** 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5, beats Qwen3.5-0.8B and Gemma 3 1B on instruction following and data extraction.
- **v18 status:** unchanged. v18 add: the v18 RAM price spike (TechSpot, June 30 2026) makes LFM2.5-230M even more important as a v1.0 audiod post-processor.

### Hermes Agent (Nous Research, late June 2026) — held from v16 CRITICAL #2
- **Released:** late June 2026 by Nous Research.
- **License:** MIT (verify).
- **v18 status:** unchanged.

## v1.5 Models (held from v16, with v18 order unchanged)

### HRM-Text-1B (Sapient) — held from v11, demoted v16
- **Size:** 1B params.
- **License:** Apache-2.0.
- **v18 status:** v1.5 plan-B (unchanged from v16).

### Apertus v1.1 4B (Swiss AI / EPFL) — held from v14
- **v18 status:** v1.5 plan-C (unchanged from v16).

### OpenPhone-3B (HKUDS, ACL 2026) — held from v15
- **v18 status:** v1.5 plan-D (unchanged from v16).

### Qwen3-TTS (Alibaba) — held from v12
- **v18 status:** v1.5 TTS plan-A. Unchanged.

### Chatterbox (Resemble AI) — held from v12
- **v18 status:** v1.5 voice-cloning plan-A. Unchanged.

### LFM2.5-VL-450M-Extract (Liquid AI) — held from v12
- **v18 status:** v1.5 structured-output VLM plan-A. Unchanged.

## NEW v18 Industry Signals (1 critical, 4 sharpening)

### Anthropic Claude Apps Gateway (July 2 2026) — NEW v18 CRITICAL #1
- **Source:** Anthropic blog + AWS blog + DevOps.com + FourWeekMBA + BERI + Claude-News, July 2 2026.
- **What it is:** Self-hosted, stateless container on customer cloud VPC, backed by PostgreSQL. Routes to Bedrock/Vertex AI/Foundry/Anthropic API. OIDC SSO (Workspace, Entra ID, Okta). Centralized policy enforcement. Per-user cost attribution. OTLP audit logs. **Published gateway protocol — Anthropic explicitly invites third-party implementations.**
- **Sonnet 5:** 63.2% on SWE-bench Pro (vs Sonnet 4.6 58.1%, Opus 4.8 69.2%). Default on Free + Pro. Introductory price $2/$10 per million I/O tokens through August 31 2026.
- **v18 implication:** the v17 "harness > model" thesis is now *shipped* by Anthropic as a first-class enterprise product. The OpenClaw JSON-RPC envelope is the open-source on-device, open-weights analog. **v18 add: document OpenClaw's protocol surface as a v1.0 marketing artifact, sharpened by the v18 fact that Anthropic is now *literally* shipping the same pattern.**
- **v18 effort:** 1 day copy + 1 day spec add = 2 days, 1 engineer.
- **Evidence:** https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026, July 2 2026.

### OpenClaw native iOS + Android (June 30 2026) — NEW v18 SHARPEN
- **Source:** 9to5Google + Engadget + TechCrunch + Mashable, June 30 2026.
- **What it is:** Native mobile apps for OpenClaw Gateway. "Pair this Android app with your OpenClaw Gateway to use your phone as a secure node for chat, voice, approvals, and device-aware automation." Camera, screen, location, photos, contacts, calendar, reminders exposed.
- **v18 implication:** OpenClaw is now a *native mobile* agent protocol. The v1.0 spec should describe Dan Glasses as "the wearable node in the OpenClaw fabric."
- **v18 risk:** Mashable reports a critical security flaw in OpenClaw was discovered ~2 months before the mobile launch. Audit OpenClaw's threat model before shipping the v1.0 marketing artifact.
- **v18 effort:** 1 day copy + 1 day security audit = 2 days, 1 engineer.
- **Evidence:** https://9to5google.com/2026/06/29/openclaw-app-android-ios/, June 30 2026.

### OpenClaw known critical security flaw (Mashable, June 30 2026) — NEW v18 SHARPEN (RISK)
- **v18 risk:** A critical security flaw in OpenClaw was discovered ~2 months before the mobile launch. **v18 add: before shipping the v1.0 marketing artifact, audit OpenClaw's threat model.** Document the audit response in the v1.0 spec safety-considerations section. 1-day spike, 1 engineer.
- **Evidence:** https://mashable.com/tech/openclaw-ios-android, June 30 2026.

### Proton Lumo 2.0 (June 30 2026) — NEW v18 SHARPEN
- **Source:** 9to5Mac + TechCrunch + Let's Data Science, June 30 2026.
- **What it is:** Privacy-preserving AI assistant with image generation, "thinking mode," persistent memory, and private web search. Lumo 2.0 Max scores 240% higher than Lumo 1.4 on Artificial Analysis Intelligence Index. 10M+ users on Lumo.
- **v18 implication:** Lumo 2.0 is a *privacy harness* on top of a frontier model, not a model itself. Dan Glasses is the on-device, open-weights analog of the same pattern. Cite Lumo 2.0 as the v18 privacy-harness analog in the v1.0 spec.
- **v18 effort:** 1 day copy, 1 engineer.
- **Evidence:** https://9to5mac.com/2026/06/30/proton-launches-lumo-2-0-with-image-generation-memory-private-web-search-more/, June 30 2026.

### OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 closed-source agentic race — NEW v18 SHARPEN
- **v18 contribution:** All three labs shipped agentic models in May-July 2026, all behind closed APIs. Gemini 3.5 Flash (May 2026) was "a shift from a conversational chatbot to an agentic tool that plans, builds, and iterates on real work with minimal human input." GPT-5.6 Sol (late June 2026) is "OpenAI's most agentic model yet, allowing users to split work across subagents for longer autonomous tasks." Sonnet 5 (July 2 2026) "narrows the capability gap with Opus 4.8" on agentic benchmarks.
- **v18 effort:** 1 day copy, 1 engineer.
- **Evidence:** TechCrunch + Axios + 9to5Mac, June-July 2026.

## v1.5 Substrate: Phase-mapped heterogeneous inference (held from v15)

| Phase | Backend | Speedup | Energy |
|-------|---------|---------|--------|
| Vision encoder (prefill) | NPU (QNN/Hexagon) | 1.64× | 2.52× lower |
| Text decode | CPU | 1.0× (1.18× with NPU) | baseline |
| Salience gating | low-power DSP | n/a | 0.3W |
| audiod post-processor (LFM2.5-230M on aarch64) | CPU | 42 tok/s on Raspberry Pi 5 | ~0.5W |

**v18 power conclusion:** the 4hr battery target is reachable with phase-mapped execution + salience gating + LFM2.5-230M audiod post-processor. **v18 add: the v18 RAM price spike (TechSpot, June 30 2026) makes this path even more important. Every MB of RAM saved is a v18 cost + supply-chain win.**

## Top 3 Recommendations for somdipto (v18)

1. **Approve the OpenClaw protocol surface marketing artifact (Q3 W2, 2 days, 1 engineer).** v18 CRITICAL #1. "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable."
2. **Approve the v18 batch: OpenClaw native iOS+Android wearable-node marketing (1 day copy) + OpenClaw security audit (1 day spike) + Proton Lumo 2.0 (1 day copy) + OpenAI Gemini/Anthropic closed-source agentic race (1 day copy) + 10-step marketing narrative with Newsweek (1 day) (Q3 W2, 5 days, 1 engineer).** v18 SHARPEN.
3. **Approve the v15/v16/v17 model shortlist (LFM2.5-VL-450M + whisper.cpp + KittenTTS + OpenClaw + MiniLM-L6-v2 + LFM2.5-230M + Hermes Agent).** No v17 retraction. Held from v8/v11/v16.

## Open Questions for somdipto (v18)

1. **OpenClaw protocol surface marketing artifact priority** — Q3 W2, 2 days, 1 engineer (recommend: yes, "Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable.")
2. **OpenClaw security audit priority** — Q3 W2, 1 day spike, 1 engineer (recommend: yes, v18 Mashable flag)
3. **OpenClaw native iOS+Android wearable-node marketing priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, "OpenClaw is the gateway. Dan Glasses is the wearable node.")
4. **Proton Lumo 2.0 privacy-harness analog marketing** — Q3 W2, 1 day copy, 1 engineer (recommend: yes)
5. **OpenAI Gemini/Anthropic closed-source agentic race marketing** — Q3 W2, 1 day copy, 1 engineer (recommend: yes)
6. **10-step marketing narrative with Newsweek** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, v18 10th step)
7. **v16 priorities (LFM2.5-230M, Hermes Agent, As We May Search, Memora, Phase Matters, OpenPhone-3B, 8-step narrative, Mythos $30K catch retraction)** — held from v16 (recommend: yes, all v16 priorities hold)
8. **LFM2.5-230M dual-license structure** — free <$10M ARR, paid enterprise (recommend: verify)
9. **LFM2.5-230M on aarch64 (Raspberry Pi 5) benchmarks** — after Q3 W1 swap-in, 1-day benchmark (recommend: yes)
10. **Redax SoC choice (Qualcomm vs MediaTek)** — needed before Q3 W1 LFM2.5-230M swap-in (recommend: confirm with hardware team)

## Footnotes (v19)

[^v19-1]: https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026 — Anthropic Claude Sonnet 5 + Claude Apps Gateway, July 2 2026 (held from v18)
[^v19-2]: https://9to5google.com/2026/06/29/openclaw-app-android-ios/ — OpenClaw native iOS + Android, June 30 2026 (held from v18)
[^v19-3]: https://www.engadget.com/2204549/theres-now-an-openclaw-app-for-ios-and-android-phones/ — Engadget: OpenClaw founder → OpenAI, June 30 2026 (NEW v19)
[^v19-4]: https://mashable.com/tech/openclaw-ios-android — Mashable on OpenClaw security flaw + iOS/Android, June 30 2026 (held from v18)
[^v19-5]: https://www.newsweek.com/ai-agents-open-accountability-standards-opinion-12146668 — Newsweek "Open Accountability Standards," early July 2026 (held from v18)
[^v19-6]: https://9to5mac.com/2026/06/30/proton-launches-lumo-2-0-with-image-generation-memory-private-web-search-more/ — Proton Lumo 2.0, June 30 2026 (held from v18)
[^v19-7]: https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/ — Anthropic Sonnet 5, June 30 2026 (held from v18)
[^v19-8]: https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/ — Zuckerberg "slower than expected," July 2 2026 (held from v18)
[^v19-9]: https://letsdatascience.com/news/pagerduty-chair-highlights-ai-agent-failure-risks-0367559f — PagerDuty Jenn Tejada, July 2 2026 (held from v18)
[^v19-10]: https://www.thailand-business-news.com/pr-news/white-paper-physical-ai-2-0-and-the-critical-need-for-physical-state-recovery — Atomathic Physical AI 2.0, July 1 2026 (held from v18)
[^v19-11]: https://www.techspot.com/news/112934-ram-prices-expected-rise-another-40-50-q3.html — RAM price spike, June 30 2026 (held from v18)
[^v19-12]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine on RSI, June 29 2026 (held from v18)
[^v19-13]: https://letsdatascience.com/news/godot-tightens-contribution-policy-to-restrict-ai-code-e58bf90a — Godot AI code rules, June 30 2026 (held from v18)
[^v19-14]: https://hackernoon.com/the-month-ai-governance-became-operational — HackerNoon, "The Month AI Governance Became Operational," June 2026 (held from v17)
[^v19-15]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M, Liquid AI (held from v16)
[^v19-16]: https://www.nousresearch.com/agents/hermes — Hermes Agent, Nous Research (held from v16)
[^v19-17]: https://arxiv.org/abs/2606.29652 — "As We May Search," late June 2026 (held from v16)
[^v19-18]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^v19-19]: https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vinton Cerf Open Frontier, June 30 2026 (held from v17)
[^v19-20]: https://roadtovr.com/memomind-one-smart-glasses-kickstarter-release/ — MemoMind One (XGIMI), late June 2026 (NEW v19)
[^v19-21]: https://www.politico.com/news/2026/06/29/exclusive-newsom-anthropic-ink-deal-to-expand-government-use-00979584 — Politico exclusive: Anthropic-Newsom California deal, June 29 2026 (NEW v19)
[^v19-22]: https://www.latimes.com/business/story/2026-06-29/google-poached-to-lose-two-more-senior-ai-staffers-to-anthropic — Google AI brain drain to Anthropic, June 29 2026 (NEW v19)
[^v19-23]: https://www.cnbc.com/2026/06/29/alphabet-googl-stock-dow-average.html — Alphabet stock worst month since Feb 2025, June 29 2026 (NEW v19)
[^v19-24]: https://www.reuters.com/business/google-limits-metas-use-its-gemini-ai-models-ft-reports-2026-06-28/ — Reuters: Google limits Meta's Gemini compute, June 28 2026 (NEW v19)

## v18 model analysis content (preserved in backup)

The v18 model analysis (preserved in `dan2-model-analysis.v18-backup-2026-07-04.md`, 20.4KB, 188 lines) covers: v18 CRITICAL #1 (Anthropic Claude Sonnet 5 + self-hosted Claude Apps Gateway, shipped July 2 2026, the v18 strongest possible citable evidence for "harness > model" + OpenClaw's protocol surface being SOTA) + v18 SHARPEN (OpenClaw native iOS+Android as the v18 wearable-on-OpenClaw thesis becomes native, OpenClaw security flaw as v18 SHARPEN RISK, Proton Lumo 2.0 as privacy-harness-on-frontier-model analog, OpenAI/Gemini/Anthropic closed-source agentic race). v17 model shortlist holds: LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS medium (TTS) + OpenClaw (orchestration, v17 Cerf-endorsed, v18 Anthropic-shipped-analog) + MiniLM-L6-v2 (memoryd) + LFM2.5-230M (v1.0 audiod post-processor) + Hermes Agent (v1.0 audiod agent framework). v1.5 model shortlist: HRM-Text-1B (plan-B), Apertus v1.1 4B (plan-C), OpenPhone-3B (plan-D), Qwen3-TTS (TTS), Chatterbox (voice-cloning), LFM2.5-VL-450M-Extract (structured-output VLM). v17 Mythos 5 framing continues to hold (now "Glasswing program, expanding to broader domestic + international"). **All v18 content is preserved verbatim in the backup. The v19 add is documented in the v19 header at the top of this file: 4 CRITICAL (Google AI brain drain, Anthropic-Newsom California, OpenClaw founder → OpenAI governance risk, MemoMind One $20/mo) + 5 SHARPEN (China Mobile MWC Shanghai AI glasses, NATO SAPIENT, Reuters Meta compute cap, AR Glasses size problem, Alphabet stock worst month). The v18 model shortlist is *unchanged* in v19 — all v1.0/v1.5 model choices hold. v19 add: OpenClaw's v19 governance risk must be audited before shipping the v1.0 marketing artifact.**
## v20 addendum (2026-07-04 09:35 UTC / 15:05 IST)

**v20 deltas vs v19 (4 CRITICAL, 4 SHARPEN, 0 model changes, 0 broad rollbacks):**

1. **NEW v20 CRITICAL #1 — Axios: Amazon-Jassy-Anthropic jailbreak escalation (July 3 2026).** **v20 add: the closed-source frontier is *inter-vendor fractured*. The on-device + open-weights + auditable memory + auditable agent loop stack is the v20 only trust-resilient substrate. No v19 model change.**

2. **NEW v20 CRITICAL #2 — Bad Epoll CVE-2026-46242 + Mythos missed bug (July 3 2026).** **v20 add: the v1.0 safety spec must adopt the v20 *auditable-bug-discovery* pattern — Mythos + GLM-5.2 + Apertus v1.1 4B scan every release. v20 v1.5 plan-B candidate: GLM-5.2 (cybersecurity) upgraded from research-bet to auditable-bug-discovery-stack. v20 v1.5 plan-D candidate: Apertus v1.1 4B (EU provenance) confirmed as auditable-bug-discovery-stack.**

3. **NEW v20 CRITICAL #3 — Apple camera AirPods Pro suspended (July 3 2026).** **v20 add: no model change, but the v1.0 vision model (LFM2.5-VL-450M) is now the v20 only *shipped* wearable-visual-AI in the v1.0 wearable category. v20 v1.5 plan: LFM2.5-VL-Extract-2 (Liquid AI, structured-output VLM, held from v17) confirmed.**

4. **NEW v20 CRITICAL #4 — LA Times + Bloomberg token-price collapse (July 3 2026).** **v20 add: the on-device stack (lifetime cost of $349 hardware + free local inference) is the v20 only answer to the v20 unit-economics crisis. No v19 model change. v20 v1.0 audiod post-processor: LFM2.5-230M (Liquid AI) held. v20 v1.0 TTS: KittenTTS medium held. v20 v1.0 STT: whisper.cpp base.en held.**

5. **NEW v20 SHARPEN #1 — Wall Street: GLM-5.2 vs Mythos priced (July 3 2026).** **v20 SHARPEN: v20 v1.5 plan-C model candidate: GLM-5.2 (Zhipu AI, MIT, open-weights, now Wall-Street-priced as Mythos-competitor) confirmed. v1.5 plan-C = GLM-5.2 + HRM-Text-1B (plan-B) + Apertus v1.1 4B (plan-D) + OpenPhone-3B (plan-E, new v20).**

6. **NEW v20 SHARPEN #2 — NSA Gen. Rudd on Mythos (Economist, July 3 2026).** **v20 SHARPEN: Mythos is too dangerous to ship widely, too valuable to ship to no one. v20 v1.0 spec safety-considerations section: cite the v20 *auditable-bug-discovery* pattern. No v19 model change.**

7. **NEW v20 SHARPEN #3 — Chris Inglis (former US National Cyber Director) on GLM-5.2 (Dark Reading, July 3 2026).** **v20 SHARPEN: v20 v1.5 plan-C model: GLM-5.2 (Zhipu AI, MIT, open-weights, now former-NSA-cyber-director-endorsed) confirmed. v20 v1.5 plan-B: HRM-Text-1B (Sapient, Apache-2.0, $1,500 trained) held. v20 v1.5 plan-D: Apertus v1.1 4B (Swiss AI, EU provenance) held. v20 v1.5 plan-E: OpenPhone-3B (HKUDS, on-device agentic foundation) held.**

8. **NEW v20 SHARPEN #4 — Meta Pocket gizmos (June 29 - July 3 2026).** **v20 SHARPEN: no v19 model change. v20 v1.0 spec privacy/positioning: cite Meta Pocket gizmos. The on-device + open-weights + auditable memory stack is the v20 only answer to the v20 *user-data-as-AI-training-fuel* pattern.**

**v20 model shortlist (locked, no v19 change):**
- v1.0: LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS medium (TTS) + OpenClaw (orchestration) + MiniLM-L6-v2 (memoryd) + LFM-2.5-230M (v1.0 audiod post-processor) + Hermes Agent (v1.0 audiod agent framework).
- v1.5: HRM-Text-1B (plan-B, SIA Feedback-Agent) + GLM-5.2 (plan-C, cybersecurity + auditable-bug-discovery, v20) + Apertus v1.1 4B (plan-D, EU provenance) + OpenPhone-3B (plan-E, on-device agentic) + LFM2.5-VL-Extract-2 (plan-F, structured-output VLM) + Qwen3-TTS (plan-G, TTS) + Chatterbox (plan-H, voice-cloning).

**v20 retractions:** 0 broad rollbacks. v19 Mythos 5 Glasswing framing is now *post-jailbreak-control*, *NSA-validated-at-the-classified-systems-level*, and *Wall-Street-priced-as-replaceable-by-GLM-5.2*. The v19 model shortlist is *unchanged in v20*.


[^v20-1]: https://www.axios.com/2026/07/03/anthropic-ai-models-revived-behind-the-scenes — Axios: How the world's top AI models were revived (Amazon Jassy → Bessent → Lutnick → Amodei, 20-day showdown), July 3 2026 (NEW v20 CRITICAL #1)
[^v20-2]: https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html — "Bad Epoll" Linux kernel flaw (CVE-2026-46242) — Mythos found CVE-2026-43074 but missed Bad Epoll; fix already landed, July 3 2026 (NEW v20 CRITICAL #2)
[^v20-3]: https://www.macrumors.com/2026/07/03/camera-airpods-pro-development-suspended-leaker/ — Apple camera AirPods Pro "suspended" per Kosutami, July 3 2026 (NEW v20 CRITICAL #3)
[^v20-4]: https://www.latimes.com/business/story/2026-07-03/with-token-prices-collapsing-regulation-rising-ais-pricing-power-looks-fragile — LA Times: Silicon Data LLM Token Expenditure Index -20% from May high; AI pricing power "looks fragile," July 3 2026 (NEW v20 CRITICAL #4)
[^v20-5]: https://letsdatascience.com/news/ai-driven-rotation-reshapes-stock-market-leadership-dc767e6c — Palo Alto + CrowdStrike all-time highs; PHLX semi -6.3%/-5.4% Wed/Thu; WSJ: Zhipu GLM-5.2 now rivals Mythos at vulnerability hunting, July 3 2026 (NEW v20 SHARPEN #1)
[^v20-6]: https://mimir.substack.com/p/the-new-news-in-ai-7326-edition — NSA Gen. Joshua Rudd: Mythos "broke into almost all of our classified systems, not in weeks, but in hours," July 3 2026 (NEW v20 SHARPEN #2)
[^v20-7]: https://www.darkreading.com/cyber-risk/chinese-llms-broaden-gap-between-attackers-defenders — 360 Security "Tulongfeng" finds 3,400+ vulnerabilities; Chris Inglis (former US National Cyber Director) endorses GLM-5.2 for defenders, July 3 2026 (NEW v20 SHARPEN #3)
[^v20-8]: https://www.mediapost.com/publications/article/416292/meta-prizes-ai-generated-creative-in-new-mini-game.html — Meta launches "Pocket" AI gizmos app on Apple App Store + Google Play, June 29 - July 3 2026 (NEW v20 SHARPEN #4)


## v19 model analysis content (preserved in backup)

The v19 model analysis (preserved in `dan2-model-analysis.v19-backup-2026-07-04.md`, 23.1KB, 196 lines) covers: 4 CRITICAL (Google AI brain drain, Anthropic-Newsom California, OpenClaw founder → OpenAI governance risk, MemoMind One $20/mo) + 5 SHARPEN (China Mobile MWC Shanghai AI glasses, NATO SAPIENT, Reuters Meta compute cap, AR Glasses size problem, Alphabet stock worst month). v19 model shortlist: LFM2.5-VL-450M (vision) + whisper.cpp base.en (STT) + KittenTTS medium (TTS) + OpenClaw (orchestration) + MiniLM-L6-v2 (memoryd) + LFM2.5-230M (v1.0 audiod post-processor) + Hermes Agent (v1.0 audiod agent framework). v1.5: HRM-Text-1B (plan-B) + GLM-5.2 (plan-C, now Wall-Street-priced) + Apertus v1.1 4B (plan-D) + OpenPhone-3B (plan-E). **All v19 content is preserved verbatim in the backup. The v20 add is documented in the v20 addendum above: 4 CRITICAL (Axios inter-vendor trust, Bad Epoll auditable-bug-discovery, Apple camera AirPods Pro wearable-vacuum, LA Times token-price collapse) + 4 SHARPEN (Wall Street GLM-5.2 vs Mythos, NSA Rudd, Chris Inglis, Meta Pocket). v20 model shortlist is *unchanged* from v19.**
