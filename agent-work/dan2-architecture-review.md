# Dan Glasses Architecture Review — v40
**Author:** Dan2
**Date:** 2026-06-23
**Status:** v40 — adds agentd + learnerd + memoryd v2 + DanClaw proxy as the v40 service stack

> **Read first:** `dan2-research-report.md` (v40), `dan2-model-analysis.md` (v40). This document is the architecture review.

> **v40 thesis (one sentence):** The v39 stack is correct in decomposition but incomplete in agency. v40 adds **agentd (Rust planning loop), learnerd (self-improvement loop), memoryd v2 (typed topic-structured memory), and DanClaw proxy (OpenClaw crash-suppression layer)** as the four v1 deliverables that turn the current prototype into a product.

---

## 0. Current state (live, 2026-06-23)

| # | Service | Port | Tests | Owner | Status |
|---|---------|------|-------|-------|--------|
| 1 | audiod | 8090 | 101/101 ✅ | DAN-2 | Live, production |
| 2 | perceptiond | 8092 | 8/8 ✅ | DAN-3 | Live, watchful mode |
| 3 | memoryd | 8741 | 16/16 ✅ | DAN-4 | Live, flat-vector SQLite |
| 4 | toold | 8742 | 18/18 ✅ | DAN-4 | Live, sandboxed |
| 5 | ttsd | 8743 | 6/6 ✅ | DAN-4 | Live, KittenTTS medium |
| 6 | os-toold | 8744 | manual | DAN-4 | Live, path-guard |
| 7 | openclaw | 18789 | TS suite | foundation | **Live but unsafe** (v38 production failure modes) |
| 8 | dan-glasses-app | 8747 | build clean | DAN-1 | Published, 5 tabs |

**Live: 8/8. Tests: 144/144 + openclaw TS suite (not auto).** This is the receipt.

---

## 1. The decomposition is correct, but missing four pieces

The v39 review said: "The decomposition is fundamentally correct. The specific boundaries need adjustment." **v40 refines:** the decomposition is correct, but **four pieces are missing** to turn a working prototype into a product:

1. **agentd** — the planning loop, tool orchestration, budget enforcement. Rust.
2. **learnerd** — the self-improvement loop. Harness-only in v1, weight + harness in v1.5.
3. **memoryd v2** — typed topic-structured memory. Replaces the flat vector store.
4. **DanClaw proxy** — OpenClaw crash-suppression layer (carry from v38).

All four are 6-month deliverables. v40 is the quarter we ship the bones.

---

## 2. The v40 service stack

```
                ┌─────────────────────────────────────────────┐
                │           Tauri v2 React Frontend           │
                │  (Bootstrap | Vision | Memory | TTS | Live)  │
                └────────────────┬────────────────────────────┘
                                 │
                ┌────────────────▼────────────────────────────┐
                │            DanClaw Proxy (NEW v40)          │
                │   - Crash suppression for OpenClaw          │
                │   - Session-routing mirror → memoryd        │
                │   - MCP allowlist + audit log               │
                └────────────────┬────────────────────────────┘
                                 │
                ┌────────────────▼────────────────────────────┐
                │         OpenClaw (TS/Node gateway)          │
                │   - Channels: Telegram + terminal           │
                │   - Skills registry                         │
                │   - Behind DanClaw, not directly exposed    │
                └────────────────┬────────────────────────────┘
                                 │
            ┌────────────────────┼────────────────────┐
            │                    │                    │
   ┌────────▼────────┐  ┌─────────▼─────────┐  ┌──────▼──────┐
   │   agentd (NEW)  │  │   learnerd (NEW)  │  │  toold/os-  │
   │   (Rust)        │  │   (Python)        │  │  toold       │
   │ - Planning loop │  │ - SIA-H loop      │  │  (existing)  │
   │ - Tool budget   │  │ - Reads logs      │  │              │
   │ - Memory writes │  │ - Proposes changes│  │              │
   └────────┬────────┘  └─────────┬─────────┘  └──────────────┘
            │                    │
   ┌────────▼────────┐  ┌─────────▼─────────┐
   │  memoryd v2     │  │   HRM-Text-1B     │
   │  (typed topic)  │  │   (NEW v40)       │
   │  (Infini Mem)   │  │   on-device INT4  │
   └─────────────────┘  └───────────────────┘

   Existing: audiod, perceptiond, ttsd — unchanged from v39.
```

**The new services:**
- **agentd** (Rust) — the planning loop. Owns the think-act-observe cycle. ~1,500 LOC.
- **learnerd** (Python, thin) — the SIA-H self-improvement loop. Reads audiod/perceptiond/memoryd logs nightly, proposes harness changes. ~500 LOC.
- **DanClaw proxy** (TypeScript) — the crash-suppression layer between OpenClaw and the daemons. ~500 LOC.
- **memoryd v2** (Python, rewrite of current memoryd) — topic-structured documents. ~1,500 LOC.

---

## 3. Per-service review (v40)

### 3.1 audiod — keep, with v1.5 Indian language plan

**Current state:** Live, 101/101 tests, whisper.cpp base.en + Silero VAD.

**v40 review:** **Ship as-is for v1.** No changes needed.

**v1.5 plan:**
- Add AI4Bharat / IndicWav2Vec for Hindi/Tamil/Telugu/Bengali.
- Dynamic dispatch based on detected language.
- Add wake word (deferred from PRD).

**v2 plan:** Replace whisper.cpp with a unified multilingual model (SeamlessM4T or equivalent).

### 3.2 perceptiond — keep, with v1.5 smart frame selection

**Current state:** Live, 8/8 tests, LFM2.5-VL-450M Q4_0 in watchful mode.

**v40 review:** **Ship as-is for v1.** No changes needed.

**v1.5 plan:**
- Add a TinyissimoYOLO-class pre-filter. Don't run the full VLM every frame. Target 67% reduction in VLM calls (OpenGlass reference).
- Switch to LFM2-VL-1.2B (larger, better reasoning over images).
- Cascade pattern: light VFM on-device, MM-LLM offloaded to minutes-not-seconds.

**v2 plan:** Cascade scheduling (Nanomind pattern) on Snapdragon AR1 / Alif B1.

### 3.3 memoryd — REWRITE as v2 (typed topic-structured)

**Current state:** Live, 16/16 tests, SQLite + flat BLOB vector index + MiniLM-L6-v2 embeddings.

**v40 review:** **The flat-vector-store pattern is not enough.** v39 research showed the SOTA has moved to:
- **Infini Memory** (arXiv 2606.10677): topic-structured documents with revision history. Editable, traceable, decays naturally. [^21]
- **MemVerse** (arXiv 2512.03627): multimodal lifelong memory with periodic distillation. [^22]
- **MEMO** (May 2026): dedicated memory model + executive model, multi-turn protocol. Qwen2.5-14B memory + Qwen2.5-32B/Gemini-3-Flash executive. 54.22% on BrowseComp-Plus. [^23]

**memoryd v2 design:**
- **Storage:** SQLite with topic-document schema (id, title, body, embedding, revision_history, created_at, updated_at, source_episodes, decay_score).
- **Retrieval:** Hybrid (BM25 + dense + recency + graph edges). LFM2.5-ColBERT-350M for late-interaction reranking.
- **Consolidation:** Nightly job (learnerd) extracts new facts from episodic traces, writes them as topic document revisions.
- **Query interface:** Structured multi-turn (MEMO pattern) for executive reasoning.

**memoryd v2 LOC estimate:** ~1,500 LOC Python (faster to ship) or Rust (production-grade).

**Migration path:** v1 ships the current memoryd (16/16 tests). v1.5 ships memoryd v2 alongside v1 (both running, v2 takes new writes, v1 is read-only for old data). v2 deprecates v1.

### 3.4 toold + os-toold — keep as-is

**Current state:** Live, 18/18 tests (toold), manual (os-toold), sandboxed shell + Python + file + registry.

**v40 review:** **No changes needed.** These are production-grade. The only v1.5 enhancement is adding a third layer: the DanClaw proxy's MCP allowlist adds a per-skill permission system on top of the existing tool guardrails.

### 3.5 ttsd — keep, with v1.5 voice clone plan

**Current state:** Live, 6/6 tests, KittenTTS medium.

**v40 review:** **Ship as-is for v1.**

**v1.5 plan:** Voice clone. 5 minutes of user speech, fine-tune KittenTTS Mini on-device or in cloud, ship the model back to the device for inference. **The differentiator.**

### 3.6 openclaw — wrap behind DanClaw proxy

**Current state:** Live but unsafe (v38 production failure modes: unhandled-rejection crashes, OOM Map leak, sessions_send routing rot).

**v40 review:** **Cannot expose OpenClaw directly to the wearable.** Carry v38 action 1: stand up DanClaw proxy.

**DanClaw proxy scope:**
1. **Crash suppression** — wrap each OpenClaw tool call in try/catch. Convert failures to structured error responses. Don't propagate unhandled rejections.
2. **Session-routing mirror** — every sessions_send is reflected to memoryd/conversations with session_id + payload. On gateway restart, proxy replays pending sends from memoryd.
3. **MCP allowlist** — only registered tools, with argument hashing + audit log. Third layer of defense on top of toold + os-toold guardrails.
4. **Per-service health fanout** — proxy reads audiod/perceptiond/memoryd/toold/ttsd/os-toold `/health` endpoints every 5s, exposes `danclaw/healthz`, fails open if OpenClaw is down but daemons are healthy.

**DanClaw proxy LOC estimate:** ~500 LOC TypeScript.

### 3.7 dan-glasses-app — keep, with v1.5 privacy dashboard

**Current state:** Live, published at https://dan-glasses-app-som.zocomputer.io, 5 tabs (Bootstrap | Vision | Memory | TTS | Live), bootstrap wizard roundtrip green in 7.08s.

**v40 review:** **Ship as-is for v1.** No changes needed.

**v1.5 plan:**
- Add **Privacy Dashboard** tab. Shows: on-device data inventory, cloud data inventory (empty by default), recording history, deletion log, skill permissions. The privacy *proof*, not just the claim.
- Add **"What Dani learned this week"** tab. The self-improvement UX surface. Shows: harness changes proposed, harness changes approved, harness changes reverted, user corrections captured.

---

## 4. NEW: agentd — the planning loop (v40)

### 4.1 Why agentd is the biggest v40 gap

Today, **no service owns the planning loop.** audiod produces events, perceptiond produces events, memoryd stores events, ttsd speaks events — but there is no service that says "given this event, what should the agent do next?" OpenClaw sits as transport, not as the brain.

This is the single biggest gap. Microsoft Scout has it (Rust-like separation from transport). Apple Intelligence has it. We don't.

### 4.2 agentd design

**Language:** Rust. Latency-critical, memory-safe, easy to embed in Tauri later.

**API surface:**
- `POST /plan` — given (current_event, memory_context, user_history, available_tools), return next action.
- `POST /act` — execute an action via the appropriate daemon.
- `GET /status` — health + budget consumed.
- `GET /trace` — last 100 planning decisions (for learnerd to analyze).

**Loop:**
```
perception event arrives
  → agentd fetches relevant memory from memoryd
  → HRM-Text-1B plans next action (or null if nothing to do)
  → agentd executes via toold / os-toold / ttsd
  → result goes to memoryd
  → optionally speak via ttsd
```

**Budget enforcement:** max tokens per session, max tool calls per minute, max latency per decision. If exceeded, agentd returns null and logs.

**LOC estimate:** ~1,500 LOC Rust.

**Dependencies:** `reqwest` (HTTP), `tokio` (async), `serde` (JSON), `rusqlite` (state), `candle` or `llama.cpp` bindings (HRM-Text-1B inference).

### 4.3 agentd v1 vs v2

- **v1:** Rule-based planner + HRM-Text-1B (cloud or laptop). Per-action decision.
- **v2:** On-device HRM-Text-1B INT4. Cascade with cloud (larger model) for hard decisions.
- **v3:** Self-improving agentd (learnerd updates the planner, not just the harness).

---

## 5. NEW: learnerd — the self-improvement loop (v40)

### 5.1 Why learnerd is the v40 moat

Sakana's RSI Lab, Hexo's SIA, Perplexity's Brain, Decagon's Duet — **every serious AGI lab in 2026 is building a self-improvement loop.** We don't have one. The v40 gap.

### 5.2 learnerd design

**Language:** Python. Easier for ML iteration.

**API surface:**
- `POST /analyze` — given the day's audiod + perceptiond + memoryd logs, return a list of (failure_pattern, proposed_harness_change, confidence).
- `GET /proposals` — pending harness change proposals.
- `POST /proposals/:id/approve` — user approves a proposal. learnerd writes the change to agentd's prompt templates.
- `POST /proposals/:id/reject` — user rejects. learnerd records the rejection for future reference.
- `GET /history` — all past proposals + outcomes (for the "What Dani learned" UI).

**Loop (SIA-H pattern):**
```
end of day
  → learnerd reads audiod transcript + perceptiond descriptions + memoryd writes
  → identifies failure patterns (e.g., "user corrected pronunciation 3x today")
  → proposes harness change (e.g., "add phonetic hint to audiod transcript display")
  → user reviews in morning, approves or rejects
  → learnerd writes the change
```

**LOC estimate:** ~500 LOC Python. **Plus an HRM-Text-1B call for the analysis step.**

### 5.3 learnerd v1 vs v2

- **v1 (now):** SIA-H (harness-only). User approves all changes. **No autonomous weight updates.**
- **v1.5 (Q4 2026):** SIA-H + Danlab-HRM-Text-1B LoRA fine-tuning on opt-in user data. Federated.
- **v2 (Q2 2027):** SIA-W+H (harness + weights). User-supervised, reversible, observable. All 9 safety tasks must pass before any weight update.

---

## 6. memoryd v2 (v40 design)

### 6.1 Why we rewrite memoryd

The v39 review said: "Rewrite memoryd as typed memory with bi-temporal edges and async consolidation. The state of the art in 2026 is typed memory, not flat vector stores." **v40 confirms and adds the Infini Memory pattern.**

### 6.2 memoryd v2 schema (v40)

```sql
-- topic_documents: the primary storage
CREATE TABLE topic_documents (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  topic_type TEXT,  -- person, place, task, fact, preference, etc.
  embedding BLOB,   -- 1024d float32 from LFM2.5-Embedding-350M
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  revision_count INTEGER DEFAULT 1,
  decay_score REAL DEFAULT 1.0,
  source_session_id TEXT
);

-- revision_history: track changes to topic documents
CREATE TABLE document_revisions (
  id INTEGER PRIMARY KEY,
  document_id INTEGER REFERENCES topic_documents(id),
  body TEXT NOT NULL,
  embedding BLOB,
  created_at TIMESTAMP,
  trigger_source TEXT  -- "consolidation", "user_correction", "new_episode"
);

-- episode_links: link topic documents to source episodes
CREATE TABLE document_episodes (
  document_id INTEGER REFERENCES topic_documents(id),
  episode_id INTEGER,  -- audiod or perceptiond event
  relationship TEXT,  -- "source", "related", "supersedes", "contradicts"
  PRIMARY KEY (document_id, episode_id)
);

-- episodic_traces: raw audiod / perceptiond events (time-bounded)
CREATE TABLE episodic_traces (
  id INTEGER PRIMARY KEY,
  source TEXT,  -- "audiod", "perceptiond", "user_input"
  content TEXT,
  embedding BLOB,
  session_id TEXT,
  created_at TIMESTAMP,
  ttl_days INTEGER DEFAULT 30  -- auto-decay unless promoted
);
```

### 6.3 memoryd v2 retrieval

**Hybrid (4 signals):**
1. **BM25** over title + body.
2. **Dense vector** cosine similarity over embeddings.
3. **Recency** boost for recently-updated documents.
4. **Graph traversal** over document_episodes for related context.

**Reranking:** LFM2.5-ColBERT-350M for late-interaction reranking (top-50 → top-5).

**Reciprocal Rank Fusion** to combine the 4 signals.

### 6.4 memoryd v2 consolidation (learnerd, nightly)

```
end of day
  → learnerd reads all episodic_traces from past 24h
  → clusters by embedding similarity
  → for each cluster:
    - if cluster contains contradiction → create new revision
    - if cluster contains new info → create new topic_document
    - if cluster confirms existing → update existing revision
  → updates decay_score based on access patterns
  → writes a `consolidation_log` row for traceability
```

---

## 7. DanClaw proxy (v40, carry from v38)

### 7.1 What DanClaw proxy does

| Function | Implementation | LOC |
|----------|----------------|-----|
| Crash suppression | Wrap OpenClaw tool calls in try/catch | ~50 |
| OOM prevention | `--max-old-space-size=2048` + watchdog | ~10 |
| Session-routing mirror | Mirror sessions_send to memoryd | ~150 |
| MCP allowlist | Validate tool calls against registered list | ~100 |
| Health fanout | Read daemon /health endpoints, expose /danclaw/healthz | ~80 |
| Audit log | Hash + log every MCP call | ~100 |

**Total: ~500 LOC TypeScript.**

### 7.2 Why this matters

Per the v38 research, OpenClaw has documented production failure modes:
- Unhandled promise rejections crash the gateway (1-3 crashes/hour observed).
- Unbounded Map growth causes OOM.
- sessions_send goes stale after long uptimes, requires restart.

**DanClaw proxy is the crash-suppression layer that makes OpenClaw safe to put behind a wearable daemon mesh.** v40 confirms the v38 action.

---

## 8. v40 service stack summary

| Service | v40 status | New in v40? | LOC estimate |
|---------|-----------|-------------|--------------|
| audiod | keep | no | (existing) |
| perceptiond | keep | no | (existing) |
| memoryd v1 | keep as fallback | no | (existing) |
| **memoryd v2** | **NEW v1.5** | yes | ~1,500 Python |
| toold | keep | no | (existing) |
| os-toold | keep | no | (existing) |
| ttsd | keep | no | (existing) |
| openclaw | keep, behind DanClaw | no | (existing) |
| **DanClaw proxy** | **NEW v1** | yes | ~500 TypeScript |
| **agentd** | **NEW v1** | yes | ~1,500 Rust |
| **learnerd** | **NEW v1.5** | yes | ~500 Python |
| dan-glasses-app | keep, add 2 tabs v1.5 | no | (existing) |

**New v40 LOC: ~4,000 lines across 4 services + 2 frontend tabs.** 6-month effort for 1-2 senior engineers.

---

## 9. Risk register (v40)

| Risk | Severity | Likelihood | Mitigation |
|------|----------|------------|------------|
| OpenClaw crashes propagate despite DanClaw | High | Low | Health fanout, circuit breaker, auto-restart |
| agentd becomes a bottleneck | Medium | Medium | Cascade with cloud, async pipeline, budget enforcement |
| memoryd v2 migration breaks existing data | High | Medium | v1 stays read-only, v2 takes new writes, dual-mode for 1 release |
| learnerd proposes bad harness changes | High | Medium | User-supervised, reversible, every change is logged |
| HRM-Text-1B doesn't fit on wearable | Medium | High | Cascade pattern: small on-device, large in cloud when needed |
| Battery life < 4 hours active | High | High | Smart frame selection, tile-based inference, NPU offload |
| Privacy breach via cloud | Critical | Low | Local-first by default, opt-in cloud with explicit consent |
| Meta Ray-Ban Display out-shipped us | Medium | High | Differentiate on privacy + open source + India |
| Sapient HRM-Text shut down / pivot | Low | Low | Full open-source code + checkpoints. Fork if needed. |
| "Self-improving AI" safety concerns | Medium | Medium | User-supervised, reversible, observable, 9 safety tasks gate weight updates |

---

## 10. The three things to fix in 90 days

If we do nothing else, do these three:

1. **Stand up agentd (Rust).** The planning loop is the single biggest gap. It owns think-act-observe, tool orchestration, and budget enforcement. OpenClaw stays as transport. **This is the difference between a demo and a product.**

2. **Stand up DanClaw proxy.** The OpenClaw production failure modes are real (v38). DanClaw is the crash-suppression layer. Without it, the wearable daemon mesh is fragile.

3. **Stand up learnerd v1 (SIA-H loop).** The self-improvement moat. Start with harness-only, user-supervised, reversible. This is the foundation for everything in v1.5 and v2.

These three things convert us from "credible prototype" to "credible product." Everything else in the roadmap is the path to market leadership.

---

## 11. Open questions for somdipto

1. **Compute budget for HRM-Text-1B training** (~$2,000). Is this a Q3 2026 budget item?
2. **Senior engineering bandwidth.** The v40 plan needs 1-2 senior engineers for 6 months. Is this available?
3. **Privacy posture for cloud features.** Voice clone training, federated improvement — opt-in? Hard opt-in? No cloud ever?
4. **Hardware pivot.** v38 asked. v40 still asks. The Brilliant Labs Halo (with LFM2-VL-450M) + GAP9 dev kit purchase is the first concrete action.
5. **Sapient HRM-Text partnership.** Co-author a paper on "Danlab-HRM-Text-1B: domain-adapted sample-efficient reasoning for ambient agents"? My recommendation: yes.
6. **memoryd v2 migration window.** v1.5 dual-mode (v1 read-only, v2 takes new writes) for 1 release, then v2 only. OK?
7. **Dani vs. Dan Glasses priority.** Dani is the platform; Dan Glasses is the first product. Is Dan Glasses still the lead product?

---

*Dan2 research agent, 2026-06-23 v40. v40 delta: agentd + learnerd + memoryd v2 + DanClaw proxy added to the service stack. The decomposition is correct; the agency is what's missing. Ship the four pieces. 👾*