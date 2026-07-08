# Dan2 — Model Analysis v18 (2026-07-04 13:00 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-model-analysis.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v17:** `dan2-model-analysis.v17-backup-2026-07-04.md` (17.7KB, 191 lines)

> **v18 deltas vs v17 (1 CRITICAL #1 add, 4 SHARPEN, 0 partial retractions, 0 broad rollbacks):**
> 1. **NEW CRITICAL #1 — Anthropic Claude Sonnet 5 + self-hosted Claude Apps Gateway shipped July 2 2026.** Sonnet 5 scores 63.2% on SWE-bench Pro (vs Sonnet 4.6 58.1%, Opus 4.8 69.2%). Introductory price $2/$10 per million I/O tokens through August 31 2026. **But the bigger story is the Claude Apps Gateway**: a self-hosted, stateless container on customer cloud VPC, backed by PostgreSQL, that routes to Bedrock/Vertex AI/Foundry, with OIDC SSO, per-user cost attribution, OTLP audit logs, and a *published gateway protocol*. **v18 add: the v17 "harness > model" thesis is now *shipped* by Anthropic. Document the OpenClaw + Dan Glasses substrate as the on-device, open-weights, auditable memory + auditable agent loop analog.**
> 2. **NEW SHARPEN — OpenClaw ships native iOS + Android (June 30 2026, 9to5Google + Engadget + TechCrunch + Mashable).** OpenClaw is now a native mobile agent. **v18 add: the v1.0 spec architecture section should now describe Dan Glasses as "the wearable node in the OpenClaw fabric" — OpenClaw is the gateway, Dan Glasses is the wearable.**
> 3. **NEW SHARPEN — OpenClaw has a v18 known critical security flaw (Mashable, June 30 2026).** A critical security flaw was discovered ~2 months before the mobile launch. **v18 risk: OpenClaw's security posture is now a v1.0 marketing liability. Audit OpenClaw's threat model before shipping the v1.0 marketing artifact. 1-day spike, 1 engineer.**
> 4. **NEW SHARPEN — Proton Lumo 2.0 (June 30 2026) is a v18 direct privacy-preserving AI competitor with persistent memory.** Lumo 2.0 Max scores 240% higher than Lumo 1.4 on Artificial Analysis Intelligence Index; "for many use cases, users can no longer perceive a qualitative difference between Lumo 2.0 Max and the latest models from OpenAI and Anthropic." Image generation, "thinking mode," persistent memory, private web search. **v18 add: Lumo 2.0 is a privacy harness on top of a frontier model, not a model itself. Dan Glasses is the on-device analog of the same pattern.**
> 5. **NEW SHARPEN — OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 closed-source agentic race is now industry-validated.** All three labs shipped agentic models in May-July 2026, all behind closed APIs. **v18 add: the on-device + open-weights + auditable memory + auditable agent loop stack is the v18 only credible counter-position.**

> **v18 retractions of v17:** **none.** The v17 model shortlist (LFM2.5-VL-450M + whisper.cpp + KittenTTS + OpenClaw + MiniLM-L6-v2 + LFM2.5-230M + Hermes Agent) all hold. v17 Mythos 5 framing continues to hold (now "Glasswing program, expanding to broader domestic + international").

## TL;DR (one paragraph, v18)

The v17 model choices are correct. **LFM2.5-VL-450M is the v1.0 vision model. whisper.cpp base.en is the v1.0 STT. KittenTTS medium is the v1.0 TTS. OpenClaw (TS/Node) is the v1.0 orchestration (v17 industry-icon-endorsed by Vinton Cerf, v18 shipped by Anthropic as Claude Apps Gateway). SQLite + MiniLM-L6-v2 + vectors is the v1.0 memory. LFM2.5-230M is the v1.0 audiod post-processor. Hermes Agent is the v1.0 audiod agent framework.** v18 adds: **document OpenClaw's protocol surface as a v1.0 marketing artifact ("Vinton Cerf says AI agents need TCP/IP. Anthropic shipped it. OpenClaw shipped it first. Dan Glasses ships it on the wearable.")** + **audit OpenClaw's threat model (v18 known critical security flaw)** + **describe Dan Glasses as "the wearable node in the OpenClaw fabric" in the v1.0 spec** + **cite Proton Lumo 2.0 as the privacy-harness-on-frontier-model analog** + **cite OpenAI GPT-5.6 Sol + Google Gemini 3.5 Flash + Anthropic Sonnet 5 closed-source agentic race as the v18 industry-validated frame for the on-device wedge.** The v18 9-step → 10-step marketing narrative adds Newsweek "Open Accountability Standards" as the v18 10th step. No v17 model choice is broadly retracted.

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

## Footnotes (v18)

[^1]: https://www.beri.net/article/anthropic-claude-code-gateway-self-hosted-enterprise-ai-coding-platform-war-2026 — Anthropic Claude Sonnet 5 + Claude Apps Gateway, July 2 2026 (NEW v18 CRITICAL #1)
[^2]: https://9to5google.com/2026/06/29/openclaw-app-android-ios/ — OpenClaw native iOS + Android, June 30 2026 (NEW v18 SHARPEN)
[^3]: https://mashable.com/tech/openclaw-ios-android — Mashable on OpenClaw security flaw + iOS/Android, June 30 2026 (NEW v18 SHARPEN RISK)
[^4]: https://www.newsweek.com/ai-agents-open-accountability-standards-opinion-12146668 — Newsweek "Open Accountability Standards," early July 2026 (NEW v18 SHARPEN)
[^5]: https://9to5mac.com/2026/06/30/proton-launches-lumo-2-0-with-image-generation-memory-private-web-search-more/ — Proton Lumo 2.0, June 30 2026 (NEW v18 SHARPEN)
[^6]: https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/ — Anthropic Sonnet 5, June 30 2026 (NEW v18 SHARPEN)
[^7]: https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/ — Zuckerberg "slower than expected," July 2 2026 (NEW v18 SHARPEN)
[^8]: https://letsdatascience.com/news/pagerduty-chair-highlights-ai-agent-failure-risks-0367559f — PagerDuty Jenn Tejada, July 2 2026 (NEW v18 SHARPEN)
[^9]: https://www.thailand-business-news.com/pr-news/white-paper-physical-ai-2-0-and-the-critical-need-for-physical-state-recovery — Atomathic Physical AI 2.0, July 1 2026 (NEW v18 SHARPEN)
[^10]: https://www.techspot.com/news/112934-ram-prices-expected-rise-another-40-50-q3.html — RAM price spike, June 30 2026 (NEW v18 SHARPEN)
[^11]: https://time.com/article/2026/06/29/recursive-self-improvement-is-the-human-skill-we-need-in-the-ai-age/ — Time Magazine on RSI, June 29 2026 (NEW v18 SHARPEN)
[^12]: https://letsdatascience.com/news/godot-tightens-contribution-policy-to-restrict-ai-code-e58bf90a — Godot AI code rules, June 30 2026 (NEW v18 SHARPEN)
[^13]: https://hackernoon.com/the-month-ai-governance-became-operational — HackerNoon, "The Month AI Governance Became Operational," June 2026 (held from v17)
[^14]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M, Liquid AI (held from v16)
[^15]: https://www.nousresearch.com/agents/hermes — Hermes Agent, Nous Research (held from v16)
[^16]: https://arxiv.org/abs/2606.29652 — "As We May Search," late June 2026 (held from v16)
[^17]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^18]: https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vinton Cerf Open Frontier, June 30 2026 (held from v17)

## v17 model analysis content (preserved in backup)

The v17 model analysis (preserved in `dan2-model-analysis.v17-backup-2026-07-04.md`) covers: Vinton Cerf Open Frontier, Anthropic Claude Science, Mythos 5 Glasswing expansion, Project Lightwell + Chainguard Athena, OpenAN project, Anthropic Claude Code timezone/proxy fingerprinting, LFM2.5-230M (CRITICAL #1), Hermes Agent (CRITICAL #2), As We May Search, GPT-5.6, Mythos $30K catch partial retraction. **All v17 content is preserved verbatim in the backup. The v18 add is Anthropic Claude Sonnet 5 + Claude Apps Gateway CRITICAL #1 (the v18 strongest possible citable evidence for "harness > model" + OpenClaw's protocol surface being SOTA) + OpenClaw native iOS+Android SHARPEN (the v18 wearable-on-OpenClaw thesis becomes native) + OpenClaw security flaw SHARPEN RISK (Mashable, audit before marketing artifact) + Proton Lumo 2.0 SHARPEN (privacy-harness-on-frontier-model analog) + OpenAI/Gemini/Anthropic closed-source agentic race SHARPEN. The v17 model shortlist holds, with the v17 Mythos 5 framing continuing to hold (now "Glasswing program, expanding to broader domestic + international").**
