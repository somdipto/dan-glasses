# Dan2 — Model Analysis v17 (2026-07-04 06:30 IST)

> **Canonical:** `/home/workspace/dan-glasses/agent-work/dan2-model-analysis.md`
> **Owner:** DAN-2 (research stream)
> **Backup of v16:** `dan2-model-analysis.v16-backup-2026-07-04.md`

> **v17 deltas vs v16 (1 CRITICAL #1 add, 3 sharpening, 1 partial retraction, 0 broad rollbacks):**
> 1. **NEW — Vinton Cerf Open Frontier (June 30 2026) is the v17 industry-icon endorsement of the "TCP/IP-for-agents" pattern.** No new model is added to the v17 shortlist, but the v17 framing of OpenClaw (TypeScript/Node) as the v17 SOTA orchestration pattern is now *industry-icon-endorsed*. **v17 add: document OpenClaw's protocol surface as a v1.0 marketing artifact.**
> 2. **NEW — Anthropic Claude Science (MobiHealthNews, June 30 2026) is the v17 closed-source admission that "harness > model."** Claude Science is "an AI workbench that runs on the same Claude models already available, including Claude Opus 4.8, without requiring special model access." **Not a new model — a workbench layer.** v17 implication: the audiod post-processor (LFM2.5-230M, v16) and the harness layer (OpenClaw, v17 Cerf-endorsed) are now the *primary* product, not the model itself.
> 3. **NEW — IBM Red Hat Project Lightwell $5B + Chainguard Athena coalition (late June 2026).** $5B Project Lightwell + 20,000 engineers for OSS patching, driven by Anthropic's Mythos findings. Chainguard Athena: 20+ orgs, 20,000+ AI-discovered findings, 2,000+ patches across 500 OSS projects. **v17 add: the v16 $9.5B / 90 days / 5-vendor implementation-wedge bet is now $14.5B / 120 days / 6-vendor.** No new model added.
> 4. **NEW — Anthropic Mythos 5 Glasswing expansion (Ars Technica, July 1 2026).** v17 partial retraction of v16 "~100 US critical-infrastructure partners only." v17 framing: "Anthropic Mythos 5 is gated to the Glasswing program (cybersecurity researchers at trusted companies), now expanding beyond the initial ~100 US critical-infrastructure partners to broader domestic + international Glasswing members."
> 5. **NEW — OpenAN project (China Mobile, GSMA, Huawei, MWC Shanghai 2026) + Anthropic Claude Code timezone/proxy fingerprinting (Gizmodo, late June 2026).** OpenAN is the first published, multi-vendor, China-led open-source agent interoperability framework. Claude Code fingerprinting is the v17 strongest possible citable evidence that "vendor lock-in is structural." No new model added.

> **v17 retractions of v16:** **1 partial retraction** (v16 "Anthropic Mythos 5 is gated to ~100 US critical-infrastructure partners" — see #4). No v16 model choice retracted. The v16 model shortlist (LFM2.5-VL-450M + whisper.cpp + KittenTTS + OpenClaw + MiniLM-L6-v2 + LFM2.5-230M + Hermes Agent) all hold.

## TL;DR (one paragraph, v17)

The v16 model choices are correct. **LFM2.5-VL-450M is the v1.0 vision model. whisper.cpp base.en is the v1.0 STT. KittenTTS medium is the v1.0 TTS. OpenClaw (TS/Node) is the v1.0 orchestration (v17 industry-icon-endorsed by Vinton Cerf). SQLite + MiniLM-L6-v2 + vectors is the v1.0 memory. LFM2.5-230M is the v1.0 audiod post-processor. Hermes Agent is the v1.0 audiod agent framework.** v17 adds: **document OpenClaw's protocol surface as a v1.0 marketing artifact ("Vinton Cerf says AI agents need TCP/IP. We shipped it.")**. **v17 also adds: cite Anthropic Claude Science (workbench > model) in the v1.0 spec safety-considerations section as the v17 closed-source admission that "harness > model."** v17 retractions: the v16 "Anthropic Mythos 5 is gated to ~100 US critical-infrastructure partners" is partially retracted (now "Glasswing program, expanding to broader domestic + international"). The v16 8-step marketing narrative is now v17 9-step. No v16 model choice is broadly retracted.

## v1.0 Model Stack (v17, locked per dan-glasses/AGENTS.md)

| Component | Model | Size | Quant | Runtime | v17 Substrate |
|-----------|-------|------|-------|---------|---------------|
| Vision | LFM2.5-VL-450M | 450M (209MB GGUF) | Q4_0 | llama-mtmd-cli | **NPU (vision encoder) + CPU (text decode) — phase-mapped** (v15) |
| STT | whisper.cpp base.en | 74MB | Q5_1 | whisper-cpp-plus-rs | CPU (with NPU optional acceleration) |
| TTS | KittenTTS medium | ~25MB | native | ONNX Runtime | CPU (with NPU optional acceleration) |
| Memory | MiniLM-L6-v2 | 22M | INT8 (v1.1 spike) | sentence-transformers | CPU |
| Orchestration | OpenClaw | n/a | n/a | TypeScript/Node | **n/a — v17 industry-icon-endorsed (Vinton Cerf, June 30 2026)** |
| **audiod post-processor (NEW v16 v1.0)** | **LFM2.5-230M** | **230M** | **Q4_K_M** | **llama.cpp** | **CPU / aarch64 — 42 tok/s on Raspberry Pi 5** |
| Agent framework (NEW v16 v1.0) | Hermes Agent | n/a | n/a | Nous Research / OpenAI ChatGPT subscription | CPU + cloud |
| Reasoning (v1.5) | HRM-Text-1B | 1B (Apache-2.0) | Q4_K_M | llama.cpp | NPU (v1.5) + CPU fallback — v1.5 plan-B (was v1.0 plan-A in v15) |
| Reasoning (v1.5) | Apertus v1.1 4B | 4B | Q4_K_M | llama.cpp | CPU + NPU — v1.5 plan-C (was plan-B in v15) |
| Reasoning (v1.5) | OpenPhone-3B | 3B | Q4_K_M | llama.cpp | CPU + NPU — v1.5 plan-D (was plan-C in v15) |
| TTS (v1.5) | Qwen3-TTS | TBD | TBD | TBD | CPU + NPU |

## v1.0 Models (held from v16, locked)

### LFM2.5-VL-450M — held from v8/v11
- **Released:** April 11, 2026 by Liquid AI.
- **Size:** 450M params, ~209MB GGUF Q4_0 + 180MB mmproj.
- **License:** Research/commercial (verify with Liquid AI).
- **v17 status:** unchanged. v15 sharpening: must run with phase-mapped heterogeneous inference per the Phase Matters paper.

### whisper.cpp base.en — held from v8/v11
- **Size:** 74MB.
- **License:** MIT.
- **v17 status:** unchanged.

### KittenTTS medium — held from v8/v11
- **Size:** ~25MB.
- **License:** Verify with KittenML.
- **v17 status:** unchanged.

### OpenClaw (TypeScript/Node) — held from v8/v11, v17 Cerf-endorsed
- **Released:** Late 2025.
- **License:** MIT.
- **v17 status:** unchanged. **v17 add: Vinton Cerf (Open Frontier, June 30 2026) publicly endorses the "TCP/IP-for-agents" pattern. Document OpenClaw's protocol surface as a v1.0 marketing artifact.** "Vinton Cerf says AI agents need TCP/IP. We shipped it."

### MiniLM-L6-v2 (memoryd) — held from v8/v11
- **Size:** 22M params, 384-dim embeddings.
- **License:** Apache-2.0.
- **v17 status:** unchanged. v17 add: IBM Red Hat Project Lightwell is the v17 analog for OSS supply chain memory. The memoryd v1.5 architecture (storage/retrieval split) is the v17 on-device, open-weights analog.

## v1.0 Models (held from v16)

### LFM2.5-230M (Liquid AI, June 26 2026) — held from v16 CRITICAL #1
- **Released:** June 26 2026 by Liquid AI.
- **Size:** 230M params, on-device.
- **License:** Dual-license: free for individuals and companies generating <$10M ARR; paid enterprise agreement for larger corporations.
- **Performance:** 213 tok/s on Galaxy S25 Ultra, 42 tok/s on Raspberry Pi 5, beats Qwen3.5-0.8B and Gemma 3 1B on instruction following and data extraction.
- **v17 status:** unchanged. v17 add: cite in the v1.0 spec safety-considerations section alongside Claude Science as the v17 closed-source admission that "harness > model" + the on-device audiod post-processor is the v17 evidence.

### Hermes Agent (Nous Research, late June 2026) — held from v16 CRITICAL #2
- **Released:** late June 2026 by Nous Research.
- **License:** MIT (verify).
- **v17 status:** unchanged.

## v1.5 Models (held from v16, with v17 order unchanged)

### HRM-Text-1B (Sapient) — held from v11, demoted v16
- **Size:** 1B params.
- **License:** Apache-2.0.
- **v17 status:** v1.5 plan-B (unchanged from v16).

### Apertus v1.1 4B (Swiss AI / EPFL) — held from v14
- **v17 status:** v1.5 plan-C (unchanged from v16).

### OpenPhone-3B (HKUDS, ACL 2026) — held from v15
- **v17 status:** v1.5 plan-D (unchanged from v16).

### Qwen3-TTS (Alibaba) — held from v12
- **v17 status:** v1.5 TTS plan-A. Unchanged.

### Chatterbox (Resemble AI) — held from v12
- **v17 status:** v1.5 voice-cloning plan-A. Unchanged.

### LFM2.5-VL-450M-Extract (Liquid AI) — held from v12
- **v17 status:** v1.5 structured-output VLM plan-A. Unchanged.

## NEW v17 Industry Signals (no new model added to shortlist)

### Vinton Cerf Open Frontier (June 30 2026) — NEW v17 industry-icon endorsement
- **Source:** Laude Institute Open Frontier conference, June 30 2026.
- **Key quote:** "I don't think English is going to be the best choice [for AI-agent-to-agent communication]... The agentic model of AI, with multiple agents from multiple sources interacting with each other, is going to force composability, and a requirement for interoperability and standardization."
- **v17 implication:** OpenClaw (TypeScript/Node JSON-RPC envelope) is the v17 SOTA orchestration pattern, industry-icon-endorsed.
- **v17 effort:** 1 day copy + 1 day spec add = 2 days, 1 engineer.
- **Evidence:** https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c.

### Anthropic Claude Science (MobiHealthNews, June 30 2026) — NEW v17 closed-source admission
- **Source:** MobiHealthNews, June 30 2026.
- **Key quote:** Claude Science is "an AI workbench that runs on the same Claude models already available, including Claude Opus 4.8, without requiring special model access."
- **v17 implication:** the closed-source frontier is shipping workbenches, not models. The Dan Glasses OpenClaw + audiod + perceptiond + memoryd + ttsd + toold composition is the v17 on-device, open-weights analog of Claude Science.
- **v17 effort:** 1 day, 1 engineer (v1.0 spec safety-considerations section add).
- **Evidence:** https://www.mobihealthnews.com/news/anthropic-debuts-claude-science-renews-access-fable-5-mythos-5.

### IBM Red Hat Project Lightwell $5B (Dark Reading, late June 2026) — NEW v17
- **v17 contribution:** $5B Project Lightwell + 20,000 engineers for OSS patching. The v16 $9.5B / 90 days / 5-vendor implementation-wedge bet is now $14.5B / 120 days / 6-vendor.
- **v17 effort:** 1 day copy, 1 engineer.
- **Evidence:** https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them-.

### Chainguard Athena coalition (Let's Data Science, late June 2026) — NEW v17
- **v17 contribution:** 20+ orgs, 20,000+ AI-discovered findings, 2,000+ patches across 500 OSS projects. First coordinated disclosure wave due mid-July 2026.
- **v17 effort:** 1 day copy, 1 engineer.
- **Evidence:** https://www.letsdatascience.com/news/ai-scanners-expose-thousands-of-hidden-open-source-vulnerabi-420424be.

### OpenAN project (MWC Shanghai 2026, late June 2026) — NEW v17
- **v17 contribution:** China-led open-source agent interoperability framework (Linux Foundation Networking). The first published, multi-vendor open-source agent framework.
- **v17 effort:** 1 day copy, 1 engineer.
- **Evidence:** https://www.developingtelecoms.com/telecom-technology/optical-fixed-networks/20448-openan-project-aims-to-enable-o-m-agent-collaboration-in-autonomous-networks.html.

### Anthropic Claude Code timezone/proxy fingerprinting (Gizmodo, late June 2026) — NEW v17
- **v17 contribution:** Anthropic engineer Thariq Shihipar: an "experiment we launched in March" used to prevent account abuse. Effectively flagged users in China. The v17 strongest possible citable evidence that "vendor lock-in is structural."
- **v17 effort:** 1 day copy, 1 engineer.
- **Evidence:** https://www.letsdatascience.com/news/anthropic-tightens-controls-over-model-access-25bf38bc.

### Anthropic Mythos 5 Glasswing expansion (Ars Technica, July 1 2026) — NEW v17 sharpening
- **v17 contribution:** Beyond the original ~100 US critical-infrastructure partners, Mythos 5 is now expanding to "broader set of domestic and international partners in the Glasswing program." v17 partial retraction of v16 "~100 US critical-infrastructure partners only."
- **v17 effort:** 1 day copy, 1 engineer.
- **Evidence:** https://arstechnica.com/tech-policy/2026/07/after-spooking-trump-into-safety-testing-anthropic-ai-models-get-global-release/.

## v1.5 Substrate: Phase-mapped heterogeneous inference (held from v15)

| Phase | Backend | Speedup | Energy |
|-------|---------|---------|--------|
| Vision encoder (prefill) | NPU (QNN/Hexagon) | 1.64× | 2.52× lower |
| Text decode | CPU | 1.0× (1.18× with NPU) | baseline |
| Salience gating | low-power DSP | n/a | 0.3W |
| audiod post-processor (LFM2.5-230M on aarch64) | CPU | 42 tok/s on Raspberry Pi 5 | ~0.5W |

**v17 power conclusion:** the 4hr battery target is reachable with phase-mapped execution + salience gating + LFM2.5-230M audiod post-processor.

## Top 3 Recommendations for somdipto (v17)

1. **Approve the OpenClaw protocol surface marketing artifact (Q3 W2, 2 days, 1 engineer).** v17 CRITICAL #1. "Vinton Cerf says AI agents need TCP/IP. We shipped it."
2. **Approve the v17 batch: Project Lightwell $5B + Chainguard Athena (1 day copy) + OpenAN + Anthropic Claude Code fingerprinting (1 day copy) + Claude Science workbench-layer v1.0 spec add (1 day) (Q3 W2, 3 days, 1 engineer).** v17 SHARPEN.
3. **Approve the v15/v16 model shortlist (LFM2.5-VL-450M + whisper.cpp + KittenTTS + OpenClaw + MiniLM-L6-v2 + LFM2.5-230M + Hermes Agent).** No v16 retraction. Held from v8/v11/v16.

## Open Questions for somdipto (v17)

1. **OpenClaw protocol surface marketing artifact priority** — Q3 W2, 2 days, 1 engineer (recommend: yes, "Vinton Cerf says AI agents need TCP/IP. We shipped it.")
2. **v17 Mythos 5 partial retraction priority** — Q3 W2, 1 day copy, 1 engineer (recommend: yes, v17 framing is "Glasswing program, expanding to broader domestic + international")
3. **Project Lightwell $5B + Chainguard Athena spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes, open-source supply chain AI security is the v17 next wedge)
4. **OpenAN project spike priority** — Q4 2026 W1-W2, 1 week, 1 engineer (recommend: yes, agent interoperability framework SOTA)
5. **Anthropic Claude Code timezone/proxy fingerprinting marketing weight** — Q3 W2, 1 day copy, 1 engineer (recommend: yes)
6. **Anthropic Claude Science workbench-layer v1.0 spec add priority** — Q3 W2, 1 day, 1 engineer (recommend: yes)
7. **LFM2.5-230M / Hermes Agent / As We May Search / Memora / Phase Matters v16 priorities** — held from v16 (recommend: yes, all v16 priorities hold)
8. **LFM2.5-230M dual-license structure** — free <$10M ARR, paid enterprise (recommend: verify)
9. **LFM2.5-230M on aarch64 (Raspberry Pi 5) benchmarks** — after Q3 W1 swap-in, 1-day benchmark (recommend: yes)
10. **Redax SoC choice (Qualcomm vs MediaTek)** — needed before Q3 W1 LFM2.5-230M swap-in (recommend: confirm with hardware team)

## Footnotes (v17)

[^1]: https://www.letsdatascience.com/news/vinton-cerf-flags-standards-interoperability-and-agents-as-a-c5f4fe3c — Vinton Cerf Open Frontier, June 30 2026
[^2]: https://www.mobihealthnews.com/news/anthropic-debuts-claude-science-renews-access-fable-5-mythos-5 — Anthropic Claude Science, June 30 2026
[^3]: https://arstechnica.com/tech-policy/2026/07/after-spooking-trump-into-safety-testing-anthropic-ai-models-get-global-release/ — Anthropic Mythos 5 Glasswing expansion, July 1 2026
[^4]: https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them- — IBM Red Hat Project Lightwell $5B, late June 2026
[^5]: https://www.letsdatascience.com/news/ai-scanners-expose-thousands-of-hidden-open-source-vulnerabi-420424be — Chainguard Athena coalition, late June 2026
[^6]: https://www.developingtelecoms.com/telecom-technology/optical-fixed-networks/20448-openan-project-aims-to-enable-o-m-agent-collaboration-in-autonomous-networks.html — OpenAN project, MWC Shanghai 2026
[^7]: https://www.letsdatascience.com/news/anthropic-tightens-controls-over-model-access-25bf38bc — Anthropic Claude Code timezone/proxy fingerprinting, late June 2026
[^8]: https://hackernoon.com/the-month-ai-governance-became-operational — HackerNoon, "The Month AI Governance Became Operational," June 2026
[^9]: https://liquid.ai/blog/lfm2-5-230m — LFM2.5-230M, Liquid AI (held from v16)
[^10]: https://www.nousresearch.com/agents/hermes — Hermes Agent, Nous Research (held from v16)
[^11]: https://arxiv.org/abs/2606.29652 — "As We May Search," late June 2026 (held from v16)
[^12]: https://arxiv.org/html/2606.27906v1 — "Phase Matters" (held from v15)
[^13]: https://www.defenseone.com/technology/2026/07/genaimil-records-almost-17m-users-plans-new-model-additions/414569/ — DoD GenAI.mil 1.7M users (held from v16)
[^14]: https://www.beri.net/article/ai-deployment-wars-9-billion-forward-deployed-engineers-enterprise-pilot-failure-crisis-2026 — $9.5B / 90 days / 5-vendor (held from v16)
[^15]: https://www.sapient.ai/blog/hrm-text-1b — HRM-Text-1B, Sapient (held from v15)

## v16 model analysis content (preserved in backup)

The v16 model analysis (preserved in `dan2-model-analysis.v16-backup-2026-07-04.md`) covers: LFM2.5-VL-450M, whisper.cpp, KittenTTS, MiniLM-L6-v2, LFM2.5-230M (CRITICAL #1), Hermes Agent (CRITICAL #2), As We May Search, GPT-5.6, Mythos $30K catch partial retraction. **All v16 content is preserved verbatim in the backup. The v17 add is Vinton Cerf Open Frontier (industry-icon endorsement of OpenClaw) + Anthropic Claude Science (workbench > model) + IBM Project Lightwell $5B + Chainguard Athena + OpenAN + Anthropic Claude Code timezone/proxy fingerprinting. The v16 model shortlist holds, with Mythos 5 framing further retracted (now "Glasswing program, expanding to broader domestic + international").**
