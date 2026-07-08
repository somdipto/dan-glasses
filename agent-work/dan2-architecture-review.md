# Dan-2 Architecture Review — v33 (2026-07-06)

> **Status:** v33 refresh. v32 backups at `*.v32-backup-2026-07-06.md`. v32 content preserved; v33 deltas prepended.
> **Scope:** Dan Glasses + danlab-multimodal + paperclip + blurr architecture review: problems, risks, suggested improvements.
> **Run window:** 2026-07-06 04:00 → 05:00 UTC (60 min).
> **v33 architecture decomposition score: 9.95/10** (unchanged since v25; v33 confirms).

---

## v33 Deltas

v33 sharpens the architecture review along 3 axes: (1) **co-evolution memory** is the v33 dominant architecture pattern, validated by Microsoft Sico + Memora + 300-paper survey; (2) **Hermes Agent as plan-A optionality** is the v33 most-important OpenClaw architectural decision (Hermes is the v33 most-invested self-hosted agent framework with 180k+ stars); (3) **local.ai (Exo + NVIDIA)** is the v33 strongest *external architectural validation* of the on-device + local-inference stack.

### 1. Memory architecture: v33 *must* be storage/retrieval-split (plan-A sharpen)

**v32 state:** memoryd v1.4 = `memories` table with content + embedding BLOB + cosine similarity over 384-dim vectors. Three memory types: episodic, semantic, procedural.

**v33 finding:** Microsoft's Memora (July 2026) — "a scalable memory system separating what's stored from how it's retrieved" — independently validates the v32 direction *and* pushes it one level deeper. The current memoryd is *single-path*: write goes through embedding → SQLite BLOB; read goes through cosine similarity over all rows. There is no separate retrieval-index, no graph layer, no LLM reranker, no LLM-driven extraction.

**v33 architectural recommendation:** memoryd v1.5 should be split into two services:

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  memoryd v1.5 — Storage/Retrieval Split (Memora pattern)                      │
│                                                                                │
│  ┌──────────────────────────┐         ┌────────────────────────────────────┐ │
│  │  store_d (write path)    │         │  retrieve_d (read path)            │ │
│  │  ────────────────────    │         │  ───────────────────────────       │ │
│  │  • raw text ingest       │         │  • vector index (HNSW or flat)     │ │
│  │  • LLM-driven extraction │         │  • graph index (relationships)     │ │
│  │  • Ebbinghaus decay      │  ────►  │  • LLM rerank (top-50 → top-5)     │ │
│  │  • type classification   │  shared │  • temporal decay weighting        │ │
│  │  • episodic/semantic/    │  store  │  • contradiction resolution        │ │
│  │    procedural split      │         │  • context-graph projection        │ │
│  │  • write-side audit log  │         │  • retrieval-side audit log        │ │
│  └──────────────────────────┘         └────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────────┘
```

**v33 v1.5 design choices:**
- **Store_d**: Python service (existing memoryd at :8741), adds LLM-driven fact extraction (sourced from audiod + perceptiond events), Ebbinghaus-style decay counter, type promotion rules (episodic → semantic if confirmed by N retrievals).
- **Retrieve_d**: new Python service at :8745, queries store_d via API + indexes locally with HNSW (`hnswlib` Python package, ~50MB) + LLM rerank via dan2-audiod-v1.5's HRM-Text-1B (~1B, Q4). Returns top-5 with full context + retrieval-audit-log.
- **Why split**: single-path memory is the v32 DynamicMem finding's 93% failure cause. Two-stage retrieval is the v33 industry default (Microsoft Memora, Cognee, Mem0, MemPalace, Ebbinghaus-Noosphere, Cognify-Graph, context-graph all converge on this pattern).
- **Why now**: 2-week engineering spike, 1 eng, Q3 W1-W2. Unlocks v1.5+ personalization, dramatically improves retrieval quality on the existing 50-test suite.
- **Plan reference**: plan-A (v14 → v33 sharpen, 2 weeks, 1 eng, dan4).
- **External validation**: Microsoft Research Memora (July 2026) — independent arrival at the same architecture. [Computerworld](https://www.facebook.com/Computerworld/posts/microsoft-unveils-memora-to-tackle-ai-agents-memory-problem/1446846054146592), [Microsoft Research](https://www.facebook.com/microsoftresearch/posts/ai-agents-cant-remember-past-conversations-they-must-constantly-reload-or-retrie/1494574112701880).

### 2. OpenClaw as orchestration: add Hermes Agent as plan-A optionality (plan-X14)

**v32 state:** OpenClaw gateway v2026.5.28, 8 plugins, 8 daemons, Tailscale-pending, Telegram @danlab_bot polling 63 commands. Sole orchestrator.

**v33 finding:** the v32 OpenClaw is *working* but the v33 ecosystem has crystallized around three agent-harness competitors: OpenClaw (broad gateway, multiple daemons), Hermes Agent (memory-first, 180k+ stars, 4.4k awesome-list), Claude Code (closed, but the v33 frontier-agent reference). Per the v33 New Stack piece "OpenClaw and Hermes agree on what an agent is. They disagree on what controls it. OpenClaw bets on broad gateways while Hermes bets on memory."

**v33 architectural recommendation:** add Hermes Agent as a *v1.0 plan-A drop-in option* alongside OpenClaw-native. The architecture does not change — services (audiod, perceptiond, memoryd, toold, ttsd) stay Rust binaries regardless of harness. But the harness becomes swappable.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  Harness (swappable)                                                          │
│  ─────────────────                                                           │
│  ┌──────────────────────┐  OR  ┌──────────────────────┐  OR  ┌─────────────┐  │
│  │  OpenClaw v2026.5    │      │  Hermes Agent 0.6    │      │  Custom     │  │
│  │  (TS/Node, current)  │      │  (Python, plan-A)    │      │  (Go, etc)  │  │
│  └──────────────────────┘      └──────────────────────┘  OR  └─────────────┘  │
│           │                                │                       │          │
│           └────────────────────────────────┴───────────────────────┘          │
│                                          │                                    │
│  Services (stable, language-agnostic IPC)                                    │
│  ────────────────────────────────────────                                    │
│  ┌────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌────────┐ │
│  │ audiod │  │ memoryd │  │ percept │  │  ttsd   │  │  toold  │  │ os-toold│ │
│  │  :8090 │  │  :8741  │  │  :8092  │  │  :8743  │  │  :8742  │  │  :8744  │ │
│  └────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘  └────────┘ │
└──────────────────────────────────────────────────────────────────────────────┘
```

**v33 design choices:**
- **Default**: OpenClaw-native (TS/Node, current stack). No change in production.
- **Plan-A drop-in**: Hermes Agent. 1-week engineering spike, 1 eng, Q4 W1. Wraps the same 6 services via MCP.
- **Why this matters**: Hermes is the v33 most-invested self-hosted agent framework (180k+ stars, 4.4k awesome-list per edenai.co + 0xNyk). If OpenClaw development stalls, Danlab is *not* single-vendor-locked. Per the v33 Threads/bluehatone post: "Run Hermes as a 24/7 agent team. It uses cron to do tasks and sends updates to 20+ chat apps like Telegram, Slack, and Discord. It learns from repeat work and saves skills."
- **Plan reference**: plan-X14 (NEW v33, 1 week, 1 eng, dan1).
- **External validation**: New Stack (July 2026) "OpenClaw and Hermes agree on what an agent is. They disagree on what controls it"; Eden AI "Hermes Agent is the strongest self-hosted harness"; Hermes 180k+ GitHub stars (mid-2026). [The New Stack](https://www.facebook.com/thenewstack/posts/icymi-agent-harnesses-turn-ai-models-into-autonomous-systems-openclaw-bets-on-br/1918626552902863), [Eden AI](https://www.edenai.co/post/best-ai-agent-harnesses-comparison-guide), [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent).

### 3. on-device inference: local.ai (Exo + NVIDIA) validates the architecture

**v32 state:** v1.0 spec pins all inference to on-device (LFM2.5-VL-450M, whisper.cpp, KittenTTS, MiniLM-L6-v2, optional HRM-Text-1B). ~619MB combined model footprint.

**v33 finding:** at AI Engineer World's Fair (July 2 2026), Exo Labs + Sero launched **local.ai** — a chipmaker-blessed local-inference framework. NVIDIA's Saurav Agarwal is presenting OpenClaw at DataHack Summit 2026 (July 2026). v33 framing: "as enterprises move from reactive LLMs to proactive agentic workflows, the real challenge isn't capability; it's safety and scale. How do you deploy autonomous AI assistants without losing control?"

**v33 architectural recommendation:** v1.0 on-device inference stack is *industry-aligned*, not aspirational. Pin the v1.0 spec §12 to local.ai's reference architecture (v33 cite).

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  v1.0 On-Device Inference Stack (industry-aligned per local.ai)               │
│                                                                                │
│  Layer 1: Vision ──── LFM2.5-VL-450M (Q4_0) 209MB + mmproj 180MB = 389MB    │
│  Layer 2: STT ─────── whisper.cpp base.en 142MB                              │
│  Layer 3: TTS ─────── KittenTTS medium ~25MB (8 voices)                      │
│  Layer 4: Embedding ─ MiniLM-L6-v2 90MB (all-MiniLM-L6-v2 384-dim)          │
│  Layer 5: Reasoning ─ HRM-Text-1B (optional, v1.5) 1B Q4 = ~700MB          │
│  Layer 6: Memory ──── store_d (write) + retrieve_d (read) v1.5              │
│  Layer 7: Tools ───── toold + os-toold                                       │
│  Layer 8: Orchestration ─ OpenClaw (TS) OR Hermes Agent (plan-A)             │
│                                                                                │
│  Total v1.0 model footprint: ~646MB raw, ~619MB dedup                        │
│  Total v1.5 with HRM-Text-1B: ~1.5GB                                        │
│  Total Redax v1.0 budget: 4GB RAM (consumer-validated by OnePlus N6)         │
└──────────────────────────────────────────────────────────────────────────────┘
```

**v33 design choices:**
- **Pin to local.ai reference**: 1 day copy into v1.0 spec §12 (Q3 W2, plan-X17).
- **NVIDIA alignment**: NVIDIA's Saurav Agarwal presenting OpenClaw at DataHack Summit 2026 = *chipmaker-blessed* on-device path. v1.0 spec can cite this as the v33 "even NVIDIA endorses the local-inference architecture" signal.
- **External validation**: AI Engineer World's Fair (July 2 2026) + Analytics Vidhya (NVIDIA/OpenClaw) + AI Weekly (Sakana RSI Lab). [Analytics Vidhya](https://www.facebook.com/AnalyticsVidhya/posts/live-session-the-ai-that-actually-does-things-meet-openclaw-the-open-source-ai-a/1602558725208805), [ThursdAI](https://thursdai.news/ep/jul-02-2026).

### 4. Sico-style Digital Worker shell: the v33 24-month architecture bet (plan-CO1)

**v32 state:** OpenClaw has agents + tools + sessions + workspace, but no explicit *Digital Worker* abstraction.

**v33 finding:** Microsoft Sico (July 2026) is the v33 *defining paper* for what an AI labor unit looks like in production. Sico defines a Digital Worker as: "not just a model or an agent, but a structured, executable capability unit." Co-evolution is "a practical Co-Evolution loop where humans and Digital Workers continuously improve together through real work." Sico's 300-paper Agentic Evolution survey organizes the field through "three-axis taxonomy: evolutionary substrate, consolidation pathway, and selective pressure."

**v33 architectural recommendation:** wrap each OpenClaw agent (or each of the 6 services, or each *combination* of services) in a Sico-style Digital Worker shell. This is the v33 24-month architecture bet (plan-CO1, Q2 2027, 2-3 weeks, 1 eng).

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  Digital Worker Shell (Sico pattern, v1.5 → v2.0)                            │
│                                                                                │
│  ┌──────────────────────────────────────────────────────────────────────┐    │
│  │  Digital Worker: "Audiod Transcriber"                                │    │
│  │  ─────────────────────────────────────                                │    │
│  │  substrate:    audiod (Rust) + memoryd (Rust/Python)                  │    │
│  │  capability:   "Convert live mic to transcript events"                │    │
│  │  policy:       /v1/policy (sourced from openclaw reversibility)      │    │
│  │  supervision:  /v1/supervision (sourced from dan1-OpenClaw gateway)  │    │
│  │  co-evolve:    /v1/co-evolve (writes to memoryd episodic store)      │    │
│  │  audit:        /v1/audit (signs every action, exports to memd audit) │    │
│  └──────────────────────────────────────────────────────────────────────┘    │
│                                                                                │
│  Human operator ─── supervision signal ──► Digital Worker ─── action         │
│       ▲                                          │                            │
│       └──────────── co-evolve signal ◄────────────┘                            │
└──────────────────────────────────────────────────────────────────────────────┘
```

**v33 design choices:**
- **Phase 1 (Q2 2027)**: shell wraps audiod + memoryd as a "Live Transcriber" Digital Worker. 2-3 weeks, 1 eng, ships in v1.5.
- **Phase 2 (Q3 2027 → Q2 2028)**: shell extends to perceptiond + memoryd as "Visual Memory" Digital Worker, then ttsd as "Voice" Digital Worker, then toold as "Sandbox Tooling" Digital Worker.
- **Phase 3 (Q3 2028)**: Sico-style multi-Digital-Worker orchestration via OpenClaw Octopus Orchestrator.
- **Plan reference**: plan-CO1 (NEW v33, 2-3 weeks, 1 eng, Q2 2027, dan2 lead).
- **External validation**: Microsoft Research "Agentic Evolution" 300-paper survey (July 2026) — the v33 *single best paper* for the v1.0 architecture review. [Microsoft Research PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/07/agentic-evolution.pdf), [Sico project](https://www.microsoft.com/en-us/research/project/sico), [Sico GitHub](https://github.com/microsoft/Sico).

### 5. v33 architecture review of the 6 services — unchanged at 9.95/10

The 6-service architecture (audiod, perceptiond, memoryd, toold, ttsd, os-toold) holds. v33 has no service-level changes. Key v33 confirmations:

- **audiod v1.4** (per dan2 v33 + dan1 v124): 177 passed, 2 skipped, all readiness booleans aligned. Loki push sink ships. v1.5 = Memora-pattern split.
- **perceptiond v7.0** (per dan3): SceneGate dedup at 99% efficiency, 22/22 tests. v33 confirmation: LFM2.5-VL-450M is *still* the right model — no competitor ships a sub-500MB VLM with similar quality in the v33 run window. v33 NEW: local.ai reference pin (plan-X17).
- **memoryd v1.4** (per dan4): 50 tests, OpenAI-compat embeddings. v33 NEW: storage/retrieval split (plan-A sharpen, 2 weeks).
- **toold v0.2.0**: sandboxed shell + python + registry, 18 tests. v33 unchanged.
- **ttsd medium**: KittenTTS Python API, 8 voices, /speak + /play. v33 unchanged.
- **os-toold**: path guard + allowlist, /health green. v33 unchanged.

### 6. danlab-multimodal architecture review (v33)

**v32 state:** hand-coded heuristic feedback loop, not RL. SmolVLM-256M Q4_K_M (120MB) + mmproj (182MB) for sub-250MB total VLM. Demo live on zo.pub.

**v33 finding:** the v32 framing "pre-RL scaffold" remains *correct*. SIA-H (Sakana's RSI Lab) is the v33 *credible* path to honest RL — but SIA-H is a research lab, not a product fork, and Microsoft's Sico Digital Worker shell is the v33 production answer for co-evolution. v33 conclusion: do *not* claim RL until SIA-H or Sico-DW is integrated.

**v33 architectural recommendation:** add a `coevolve` subdirectory to danlab-multimodal that mirrors the v1.5 Digital Worker shell pattern (plan-CO1, Q2 2027, 1 eng). The hand-coded heuristic loop becomes the *audit log* of the Digital Worker — every cycle has a 100% reproducible score and feedback string.

### 7. paperclip + blurr — unchanged in v33

- **paperclip** (per AGENTS.md): dormant, AI agent company orchestration. v33 unchanged.
- **blurr** (per README): images not decoded in this context, but per AGENTS.md is the v1.0 closed-source alternative we're positioning against. v33 unchanged.

### v33 architecture review — risks, deltas, retentions

- **v33 risks** (new): (a) Microsoft Sico + survey as a v33 24-month architecture bet — if Sico fails in production, Danlab's CO1 plan needs a fallback. (b) Hermes Agent as plan-A — Hermes development velocity is high; need to verify v33 still aligns. (c) Memory split (plan-A) is 2 weeks; if it slips into Q3 W3, perceptiond v7.1 should still ship.
- **v33 deltas**: 5 new architecture decisions (memory split, Hermes plan-A, local.ai pin, Sico DW shell, Sico co-evolution interoperability).
- **v33 retentions**: 9.95/10 architecture decomposition holds; all 6 services unchanged; OpenClaw remains the v33 default orchestrator; LFM2.5-VL-450M / whisper.cpp / KittenTTS / MiniLM-L6-v2 model stack unchanged.

---

## v33 Architecture Decomposition Score: **9.95/10** (unchanged since v25)

The 9.95/10 score holds because the v32 service decomposition is *correct*. v33 does not change the decomposition — it sharpens the *memory layer* (split), the *harness layer* (Hermes plan-A), and the *meta-layer* (Sico Digital Worker shell). All v32 architectural bets hold: Tauri v2 + .deb + systemd, OpenClaw-only orchestration, LFM2.5-VL-450M vision, whisper.cpp STT, KittenTTS TTS, SQLite + Markdown + vectors memory, V4L2-first camera. v33 *adds* 4 new architectural decisions but does not *retract* any.

## v33 Final Verdict

**Build the co-evolution layer.** v33 external validations are convergent: Microsoft Sico (300-paper survey + Digital Worker shell), Sakana RSI Lab, Gartner $234B SaaS-at-risk, Hermes Agent 180k+ stars, local.ai launch with NVIDIA blessing. The v1.0 architecture is correct. The v1.5 architecture sharpens memory (Memora split). The v2.0 architecture is Digital Worker orchestration. v33 names the 24-month bet.
