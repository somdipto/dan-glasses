# Danlab AGI Roadmap — v101 (Dan2, 2026-06-29)

**Author:** Dan2 (👾) | **Cycle:** v101 supersedes v100 | **Horizon:** 6 / 12 / 24 months
**Source of truth:** `dan2-research-report.md`, `dan2-architecture-review.md`, `dan2-model-analysis.md`, AGENTS.md locks.

---

## Mission

Build **proactive, persistent, on-device AGI companions** that improve from use, with privacy as the moat. Dan Glasses is v1. AGI is v∞.

---

## 6-month horizon — ship Dan Glasses v1

**Goal:** 50 alpha users wearing working glasses. Prove the service architecture. Establish the harness-improvement loop.

| Track | Owner | Deliverable | Done = |
|---|---|---|---|
| Hardware | Dan1 | JBD MicroLED display, 2×200mAh batteries, USB-C charging, on-device NDP200 firmware | alpha units shippable |
| Audio | Dan2 | audiod live — whisper-cpp-plus-rs, VAD + async decode, mic array in glasses frame | <300ms STT P50 |
| Vision | Dan3 | perceptiond live — LFM2.5-VL-450M Q4_0 GGUF, 512×512 frames, bbox output | <250ms perception P50 |
| Memory | Dan4 | memoryd live — 4-layer (USER.md + MEMORY.md + episodic + skills), sqlite-vss | recall F1 > 0.7 vs Hermes baseline |
| Reasoning | Dan2 | HRM-Text 1B as planner + LFM2.5-1.2B chat head | coherent 5-turn conversation |
| TTS | Dan2 | ttsd live — KittenTTS default, Kokoro-82M quality opt-in | first chunk <200ms |
| **Learning** | **Dan4** | **learningd live — extract Skills from successful interactions, archive variants** | measurable Skill emergence |
| **Proactive** | **Dan2** | **proactived live — event subscription, threshold-based interjection** | interjection precision > 60% |
| Gateway | Dan2 | OpenClaw (Bun) with MCP, protobuf contracts, telemetry | <50ms orchestration overhead |
| Eval | Dan2 | SIA-eval harness, weekly harness-improvement loop, drift dashboard | baseline + 1 improvement cycle run |
| Android client | Dan3 | Tauri v2 + React app, paired to glasses over Bluetooth LE | app store alpha |
| Privacy story | Somdipto | "Yours, not theirs" landing page, reproducible build docs, no-telemetry audit | page live, audit public |

**Beta exit criteria (Month 6):**
- 50 users, 30-day retention > 60%
- p50 conversation latency < 1.2s end-to-end
- 1 documented self-improvement cycle (harness-RL ran, new Skills emerged, eval metrics improved)
- Zero P0 privacy incidents
- Open-source stack: every component reproducible from source

**Don't do in 6 months:** DGM-style self-rewriting (out of scope for v1), weight updates (no on-device training), multilingual beyond English + Hindi (wait for v1.5).

---

## 12-month horizon — make the companion real

**Goal:** Companion-grade proactive behavior, second-order improvement loop, ships to 5K users.

| Track | What changes | Why |
|---|---|---|
| **Second-order improvement** | Hyperagents-style: improve the *selection criteria* of learningd, not just the skills | Mirrors DGM-H, keeps us at the frontier of self-improvement |
| **Proactived v2** | Salience-weighted event triggers; learn what the user actually cares about from their reactions | Moves from "I noticed X" to "I noticed *you'd care about* X" |
| **memoryd v2** | Temporal KG layer (Zep-style). Learn graph structure from interactions. | Required for \"did I tell you about X last week?\" queries |
| **TTS v2** | Stream Kokoro-82M Q4 by default. On-glasses voice cloning (10s sample → personalized voice). | Quality is the difference between \"cool demo\" and \"I use it daily\" |
| **HRM-Text v2** | Distill our harness into HRM-Text weights via DPO on logged interactions | Online improvement without online training |
| **visiond → perceptiond v2** | LFM2.5-VL-1.6B fallback for complex queries; 450M for fast path | Tiered VLM, 4× quality for ~3× latency when needed |
| **MCP server** | Expose `learn`, `memory`, `tools`, `proactive` as MCP endpoints | We become infrastructure for other agent developers |
| **Dan Paperclip** | First-party Paperclip Agent that runs on the glasses phone companion | Memory + perception grounding for general agents |
| **Open release** | Public launch of dan-consciousness harness; reference stack for DIY builders | Community + reproducibility |

**Beta → General exit (Month 12):**
- 5K users, 90-day retention > 40%
- Proactive interjection precision > 75%
- 4 documented self-improvement cycles
- Paperclip Agent in production with at least 3 third-party agents using our MCP endpoints

---

## 24-month horizon — toward AGI

**Goal:** Dan Glasses-level capability crosses over into **general agent infrastructure**. Memory + perception + proactivity become a reusable substrate.

| Track | What changes | Why |
|---|---|---|
| **Self-rewriting harness (DGM-style)** | Promoted out of research. The harness can modify its own prompt + tool catalog + selection criteria with empirical validation | The leap from \"improving\" to \"self-improving\" — empirical, not formal |
| **Continual learning in latent space** | Sleep-time compute for the harness: nightly, we replay the day's interactions through a small student model that distills new heuristics into shared weights. Deploy if eval improves. | The path to Letta Memory Models-style RL-trained memory controllers |
| **Cross-device transfer** | User memory follows them across phone, glasses, watch, car. Local-first sync via CRDTs. | Memoryd becomes infrastructure, not a service |
| **Multimodal AGI eval** | SIA-eval extended to long-horizon tasks (1-week scenarios). Public leaderboard. | Anchors the research agenda in measurable progress |
| **Dani-Skills 2.0** | Procedural memory becomes a published, monetizable, agent-distributed skill library | The \"App Store\" of agent capabilities — open, paid, free tiers |
| **Dani Open-Source AGI** | Open-source weights + harness for a 1B-class model trained with our technique (recursive self-improvement at the harness level) | This is the AGI bet — a reproducible, inspectable, locally-deployable agent that improves from use |

**AGI exit (Month 24):**
- 100K users, > 1M interactions/day
- 1 published self-improvement result: harness-RL beats DPO/GRPO in a public benchmark
- Dani-Skills marketplace: 100+ published skills, 10+ third-party developers
- Open-source stack reproducible from source on commodity hardware
- AGI-eval leaderboard public

---

## Strategic positioning — what makes this possible

| Moat | How it deepens |
|---|---|
| **On-device everything** | No internet dependency → works in airplane mode, in rural India, in privacy-sensitive contexts. Compounds as models get smaller. |
| **Self-improving harness** | The product gets smarter the longer you use it. This is the engagement flywheel. |
| **Privacy / openness** | Open-source + no telemetry = the only AI companion that doesn't sell you out. Defensible against Meta/Google because they're committed to their ad model. |
| **Vertical stack (glasses → OS → harness)** | Most agent companies are SaaS. We're building hardware + OS + agent. Same vertical integration that made Apple beat Windows. |
| **India-born, multilingual-first** | Hindi + Tamil + Bengali at the OS level. The next billion users live here. |

---

## What we're explicitly NOT doing in 24 months

- **Frontier-class LLM training.** We use other people's foundation models.
- **Robotaxis / drones / embodied AI.** Glasses only. Scope creep kills.
- **Cloud-hosted "Dan cloud."** On-device or nothing.
- **Targeted advertising.** Ever.
- **Selling user data.** Ever.

---

## Open questions for somdipto (carried from research report)

1. **HRM-Text chat head.** LFM2.5-1.2B-Instruct vs Phi-4-mini vs fine-tune HRM-Text on chat? Affects v1 latency floor.
2. **Multilingual at launch.** v1 English only, or English+Hindi? Affects TTS/STT choices and the Hindi-language moat.
3. **Proactived aggressiveness.** Conservative (only when clearly important) or aggressive (notice patterns and call them out)? Affects retention curve.
4. **MCP exposure timing.** Ship MCP endpoints in v1 or wait for ecosystem stability?
5. **Brilliant Labs Halo competitive threat.** Their 2026 re-launch is direct competitor. Differentiate on openness+privacy, or on capability?

---

## v101 changes from v100

- Aligned all tracks to **HRM-Text 1B + LFM2.5-VL-450M** stack (per AGENTS.md lock).
- Added **learningd** and **proactived** as explicit 6-month deliverables.
- Promoted **second-order improvement** (Hyperagents-style) to 12-month centerpiece.
- Replaced AGI bet language with **Dani Open-Source AGI** — open weights + harness, recursively improving.
- Tightened exit criteria to measurable metrics.
- Carried open questions forward.
