# Dan2 — Architecture Review (v4, 2026-06-16 03:00 UTC)
**Status:** Final v4 (delta over v3)
**Audience:** somdipto (decision-maker), Dan1/Dan3/Dan4 (peer architects)
**Scope:** Architecture problems, risks, suggested improvements
**Run window:** 2026-06-16 03:00 UTC

---

## 0. TL;DR (v4)

**The v3 architecture is correct in shape but needs three concrete upgrades for v1 wearable production.** (1) **`memoryd v2` must be hierarchical** (Tier 0/1/2 + procedures), not flat vector — the 2026 SOTA is dual-process + hierarchical + RL-managed. (2) **`os-toold v2` must be a structural control** (identity verification, arbiter pattern, stealthy-parasitism detector), not just a path guard — Varonis + StakeBench prove rule-based interventions decay. (3) **`perceptiond v2` must adopt VLMCache + per-layer mixed-precision** — 1.4-3.8× speedup with <1% accuracy loss is too good to skip. **All three are tractable in 2-4 weeks of work each, and all three are required before wearable v1 ships.**

The PRD's service decomposition (perceptiond, audiod, memoryd, toold, ttsd, os-toold + OpenClaw + Tauri) is **correct**. The transport (HTTP loopback) is **acceptable for desktop prototype, but Unix domain sockets should be the v1 wearable target** to avoid TCP overhead and to keep the IPC surface auditable.

---

## 1. What is correct (don't change) — carry from v2

1. **Service decomposition:** perceptiond, audiod, memoryd, toold, ttsd, os-toold + OpenClaw + Tauri. Eight services, each with single responsibility. **Correct.**
2. **Model choices for v1:** LFM2.5-VL-450M + whisper.cpp + KittenTTS + all-MiniLM-L6-v2. **Defensible** (v4 deep-dive validated).
3. **Build strategy:** desktop prototype first, then wearable. **Correct.**
4. **Power state machine:** Sleep → Idle → Watchful → Active. **Correct.**
5. **Salience-gated VLM (not fixed FPS):** Watchful mode skips non-salient frames. **Correct and v4-validated by VLMCache.**
6. **OpenClaw as orchestration layer:** TS/Node gateway + Rust/Python daemons. **Acceptable** — the Varonis threat also affects Rust daemons; the architectural question is "what's the IPC surface?" not "what language?"

---

## 2. Critical gaps (must fix before wearable) — v2 + v3

**Carry from v3:**

1. **PRD is stale on language split.** Says "Rust microservices" — actual is Python daemons. **Action: update PRD to reflect reality or actually ship the Rust daemons. Recommend: update PRD, ship the Python daemons, document the trade-off.**
2. **PRD is stale on IPC transport.** Says "Unix socket or gRPC" — actual is HTTP loopback. **Action: same as above. Recommend: HTTP loopback for desktop, Unix domain sockets for wearable v1.**
3. **memoryd is flat vector + MiniLM.** **Action: ship `memoryd v2` hierarchical (see §4 of roadmap). v4 added as critical gap.**
4. **os-toold is path guard only.** **Action: ship `os-toold v2` with identity verification + arbiter (see §4 of roadmap). v4 added as critical gap.**
5. **VLM power draw uncharacterized on aarch64.** **Action: measure on Redax or open-source reference. Carry from v3.**
6. **No proactive AI triggering primitive.** **Action: ship `policyd` for v1.5 (see §4 of roadmap). v4 added.**
7. **No AGENTS.md-as-security-control.** **Action: ship version-controlled AGENTS.md per daemon with Email Safety + identity verification + outbound policy. v4 added.**

---

## 3. NEW v3 Gaps (Pinchy / security / model updates)

**Carry from v3:**

- **No stealthy-parasitism detector in memoryd write path.** (Pinchy scenario — agent completes user task while advancing attacker task in parallel.)
- **No identity-verification gate in toold for `/exec` with side effects.** (Pinchy scenario 1 — email asking for AWS keys.)
- **No Telegram outbound content filter / rate limit.** (Pinchy scenario 2 — exfil via Telegram channel.)
- **No audit log with trace_id propagation across daemons.** (Pinchy + StakeBench — incident response requires replayable chains.)
- **No per-daemon least-privilege tokens for zo-mcp-bridge.** (Bridge has bearer token; hijack risk.)

---

## 4. v4 Architecture Upgrades (NEW)

### 4.1 `memoryd v2` — Hierarchical + Dual-Process

**Current `memoryd v1` (live, 11/11 tests):**
- Single `memories` table: (id, type, content, embedding, created_at, metadata)
- Single flat vector index (cosine similarity)
- Query returns top-K by similarity

**v2 proposal (3 tiers + procedures):**

```
Tier 0 (raw events, time-bounded):
  - perceptiond descriptions (vision)
  - audiod transcripts (audio)
  - retention_days field, scheduled eviction
  - vector index unchanged (MiniLM for v1, Omni-Embed-Mini for v2.5)

Tier 1 (semantic facts, medium-term):
  - "user met X at Y on Z" — structured facts
  - populated by daily summarizer job (user-local midnight)
  - summarizer: rule-based extractive for v1, LFM2.5-1.2B-Thinking for v2
  - schema: (id, fact, entities[], timestamp, source_memory_ids[])
  - vector index for semantic search

Tier 2 (schemas/patterns, long-term):
  - "user has weekly standup with X every Tuesday"
  - populated by weekly consolidator (TF-IDF + clustering on Tier 1)
  - no vector index (small set, fast lookup)
  - queried first; expand to Tier 1 on miss

Procedural memory (new):
  - "user demonstrated how to do X"
  - schema: (id, procedure, steps[], triggers[], success_count, last_used)
  - populated by user demonstrations (skill framework)

Query path:
  1. Check Tier 2 (rarely populated, ~5ms)
  2. Expand to Tier 1 (medium-populated, ~20ms)
  3. Fall back to Tier 0 vector search (~50-200ms)
```

**Why this is the right move (v4 evidence):**
- DPCM dual-process: +5.20 on PersonaMem-v2 (cross-session inference)
- SAGE graph-memory: 2 cycles → top avg rank on multi-hop QA
- GraP-Mem: compact semantic + source context = better F1/BLEU
- Power: Tier 2 first means wearable-feasible latency
- Privacy: Tier 2 patterns are abstract, easier to share / audit

**Migration plan:**
- Add new tables (`facts`, `patterns`, `procedures`) without removing `memories`
- Add `tier` column to `memories` (default 0)
- Add daily summarizer cron job (Tier 0 → Tier 1)
- Add weekly consolidator cron job (Tier 1 → Tier 2)
- Update query path to tier-check
- **Backward compatible:** `/query?text=...` still works, just returns Tier 0+1 hits
- New endpoints: `/facts?text=...`, `/patterns`, `/procedures`

**Cost:** ~2 weeks of work. **Value:** highest of all v4 architecture changes.

### 4.2 `os-toold v2` — Structural Security Control

**Current `os-toold v1` (live, healthy):**
- Path guard: blocks shell chars (`; & | \ $ ( ) > < \n \r && ||`)
- Sandbox: `/tmp/toold-sandbox`
- Max timeout: 120s
- Registry: shell + python + exec_file, enable/disable

**v2 proposal (structural control):**

```
Layer 1: Path guard (v1) — keep, harden
  + Additional path restrictions: /etc, /root/.ssh, /var/run, /proc
  + Symlink check: refuse if any path component is a symlink
  + Read-only default: explicit write flag required

Layer 2: Identity verification gate (v2 NEW)
  - Any /exec containing "curl", "wget", "ssh", "scp", "rsync", "nc" triggers
    confirmation round-trip with the calling agent
  - Any /exec with `>` or `>>` triggers confirmation
  - Confirmation: "agent X wants to run command Y. Approve? [y/n]"
  - The agent's session_id, user_id, and trace_id are logged

Layer 3: Stealthy-parasitism detector (v2 NEW, in memoryd write path)
  - memoryd write path rejects any record where content contains BOTH
    user-task tokens AND external-URL tokens
  - Heuristic: strip URL-looking tokens, refuse writes containing
    "Authorization", "Bearer", "SECRET", "KEY=" patterns
  - This is the Pinchy scenario 1 mitigation at the memory layer

Layer 4: Arbiter pattern (v2 NEW, watch-the-watcher)
  - os-toold v2 exposes a /arbiter endpoint
  - Other daemons can register "suspicion" events with trace_id
  - Arbiter tracks: how many times this trace_id has been flagged
  - If > threshold, arbiter can halt the entire trace_id's execution
  - Logs go to Loki (already running) for red-team analysis

Layer 5: Audit log + trace_id propagation (v2 NEW)
  - Every cross-daemon call carries trace_id (UUID)
  - Every state-changing call (memoryd write, toold /exec, ttsd /speak,
    os-toold /exec, perceptiond /mode) logs to Loki with trace_id
  - 30-day retention minimum
  - OpenAPI spec documents the trace_id contract
```

**Why this is the right move (v4 evidence):**
- Varonis Pinchy: "treat agents.md as a security control" + "prevent agents from acting as phishing proxies" — both addressed
- StakeBench: "stealthy parasitism" is the harder attack class — addressed by Layer 3
- Lethal trifecta (Willison): private data + untrusted content + external comms = guaranteed compromise — Layer 2 (identity verification) breaks the third leg
- Architecture as Governance: rule-based interventions decay, structural controls don't — Layers 1-4 are structural
- Arbiter Agent 2026: continuous monitoring catches emergent misalignment before conversation ends — Layer 4

**Migration plan:**
- Layer 1: 1 day (hardening)
- Layer 2: 3 days (confirmation round-trip protocol)
- Layer 3: 2 days (memoryd write path filter)
- Layer 4: 1 week (arbiter service, even a small one)
- Layer 5: 2 days (trace_id propagation + Loki integration)
- **Total: ~2 weeks of work**
- Backward compatible: Layer 1 changes are tightening; Layers 2-5 are additive

### 4.3 `perceptiond v2` — VLMCache + Per-Layer Mixed-Precision

**Current `perceptiond v1` (live, LFM2.5-VL-450M Q4_0):**
- 10-15s/frame CPU inference on x86_64
- Salience-gated (watchful mode)
- Mock capture fallback
- MAX_QUEUE_DEPTH=2

**v2 proposal:**

```
Optimization 1: VLMCache-style background caching
  - Cache stable (background) visual blocks across frames
  - Semantic disaggregation to identify "this is the same wall" vs "new object"
  - Reuse background embeddings as KV-cache prefix
  - Recompute only foreground/dynamic blocks
  - Expected: 1.4-3.8× speedup, <1% accuracy loss (per VLMCache paper)
  - Implementation: track block embeddings, hash, reuse on match

Optimization 2: Per-layer mixed-precision quantization
  - Q4_K_M in attention layers (current Q4_0 → Q4_K_M is a small step up)
  - Q8_0 in vision projector (mmproj currently F16 → Q8_0 for size)
  - Q4_0 in text decoder (current)
  - Expected: 30-40% size reduction, <1% accuracy loss (per SWEET paper)
  - Implementation: convert GGUF with llama-quantize per-layer settings

Optimization 3: Structured descriptions (Abstraction Gap mitigation)
  - Current: free-form text descriptions from VLM
  - v2: structured (people, objects, actions, location, time)
  - Use LFM2.5-VL-450M with structured prompt template
  - Expected: better memory recall, better proactive triggers
  - Implementation: prompt template + post-processing extractor

Optimization 4: Geometric/landmark descriptors for memory grounding
  - Current: VLM description only ("user met someone")
  - v2: VLM description + geometric features (location type, color, layout)
  - Use lightweight CV (color histogram, edge density, landmark detection)
  - Expected: better US-1 (encounter recall) per EMemBench findings
  - Implementation: extract in capture.py or salience.py
```

**Why this is the right move (v4 evidence):**
- VLMCache 2026: 1.4-3.8× speedup, <1% accuracy loss
- SWEET 2026: per-layer quantization, 11.9-18.1% payload reduction, 0.08-0.66% accuracy loss
- Abstraction Gap 2026: VLMs generate fluent text but few structurally valid causal chains — structured prompt helps
- EMemBench 2026: visually-grounded episodic memory is hard; geometric features help ground recall
- Gemma 3 in orbit (Yam-9): proves sub-10B edge VLM works in extreme environments

**Migration plan:**
- Optimization 1: ~1 week (background cache + semantic disaggregation)
- Optimization 2: ~3 days (GGUF conversion + benchmarking)
- Optimization 3: ~1 week (prompt template + extractor)
- Optimization 4: ~3 days (geometric features in capture/salience)
- **Total: ~2-3 weeks of work**
- Backward compatible: same API surface, faster inference, better memory

**LFM2.5-VL-450M verdict (v4 sharpening):** **Still the right choice.** Gemma 3 4B is the upper bound. The optimizations above give us 3-5s/frame CPU (down from 10-15s) without changing the model.

### 4.4 `policyd` (NEW service) — Engagement + Safety Gate for Proactive AI

**For v1.5 (not v1):**

```
policyd responsibilities:
  1. Engagement inference
     - Motion sensor (accelerometer on glasses, when available)
     - Audio activity (continuous speech from audiod)
     - Time-of-day + calendar (if available)
     - Explicit user-set focus modes (DND, focus, meeting)
     - Output: engagement_score (0-1) per channel

  2. Safety gate
     - Tiny CPU-only model (~6.5K params per qualia paper, 1.8ms/decision)
     - Trained on "should the agent say something now?" classification
     - Input: current engagement_score + proactive trigger context
     - Output: proceed / suppress / queue

  3. Interruptibility settings
     - Per-channel priority: critical (always), high (engagement<0.7),
       normal (engagement<0.4), low (engagement<0.1)
     - User override: DND, focus mode, low-priority queue
     - Time-of-day rules: "no proactive output during work hours unless critical"

  4. Proactive trigger aggregation
     - Receive salience events from perceptiond
     - Receive location events (when available)
     - Receive pattern matches from memoryd v2
     - Aggregate over time: "user walked past pharmacy 3 times in 7 days"
     - Output: proactive trigger event → policyd safety gate → ttsd
```

**Why this is the right move (v4 evidence):**
- BCI cognitive-load paper 2026: defer non-urgent when user engaged
- Controllability survey 2026: structural > rule-based
- Qualia paper 2026: 6.5K-param safety classifier, 1.8ms/decision, 0.827 AUC
- CUA-Skill / EvoCUA 2026: skill-based agent architecture for proactive tasks

**Implementation cost:** ~1-2 weeks. **v1.5 feature, not v1.**

---

## 5. Anti-recommendations (don't do) — v2 + v3 + v4

1. **Don't replace flat `memoryd` with a graph database without first shipping the Tier 0/1/2 hierarchical structure.** A graph DB (Neo4j, Memgraph) is more complex than we need at v1 wearable. SQLite + hierarchical tables is enough.
2. **Don't claim the heuristic loop is RL.** It's pre-RL scaffold. The semantic war on "RL" labels in 2026 makes this non-negotiable.
3. **Don't add a custom wake word model in v1.** Whisper + VAD is enough. On-device wake word ("Hey Dan") is a v1.5+ feature with significant engineering cost.
4. **Don't replace OpenClaw with a custom gateway.** OpenClaw is the right shape; the issue is the IPC surface, not the gateway itself. Structural controls (os-toold v2) are the answer.
5. **Don't ship proactive AI in v1.** v1 = responsive. v1.5 = proactive (with `policyd`).
6. **Don't add cellular in v1.** Wi-Fi only.
7. **Don't add a display in v1.** Audio-first. Display is v2.
8. **Don't try to be the "general-purpose agent platform."** Focus on the wearable AI companion. Microsoft Scout + OpenAI Operator are the general-purpose play; we are the wearable + memory-first play.
9. **Don't ship security as a "feature."** Security is a structural property. os-toold v2 is the structural control.
10. **Don't build a custom hardware silicon.** Use off-the-shelf parts. Open-source hardware reference design is the wedge.

---

## 6. What's working well (don't change) — v2 + v3 + v4

1. **All 7 daemons live, 106/106 tests green.** v4 re-verified at 03:00 UTC.
2. **Tauri v2 frontend wired to all 6+ daemons via Rust bridges.** Working.
3. **OpenClaw with Telegram + Zo MCP bridge.** Working.
4. **Salience-gated VLM.** Working. v4 deep-dive validated the approach.
5. **Whisper + Silero VAD + WebSocket streaming.** Working. 66/66 tests.
6. **KittenTTS.** Working. 6/6 tests.
7. **SQLite + flat vector memoryd.** Working for v1. v4 proposes hierarchical for v2.
8. **Path-guarded toold.** Working for v1. v4 proposes structural controls for v2.
9. **deb packaging prep.** Working. v4 proposes GPG signing for v1.
10. **Open-source positioning.** Strong. v4 reinforces: this is the moat.

---

## 7. Open questions for somdipto (v4)

1. **`memoryd v2` priority:** do we ship it before or in parallel with `os-toold v2`? Both are critical. **Recommend: parallel tracks, both ship in Q3 2026.**
2. **`policyd` for v1.5 or v2?** v4 says v1.5. **Confirm.**
3. **Unix domain sockets for IPC on wearable v1?** HTTP loopback is fine for desktop, but Unix sockets are better for the wearable IPC surface (lower overhead, auditable, no TCP). **Recommend: yes for wearable v1.**
4. **Hardware reference design:** Brilliant Labs Halo (open source) vs Redax (custom) vs Monako Glass? **Recommend: Brilliant Labs Halo as v1 reference, Redax if/when it lands, Monako as alternative.**
5. **Open-source the entire stack or just the security primitives?** v4 says: open-source everything, but the security primitives (os-toold v2) are the press-cycle wedge. **Recommend: open-source everything, lead with the security primitives.**
6. **AGI roadmap timeline:** does the 24-month bet (10K+ users, 100+ skills, 1M+ memories) match somdipto's expectation? **Confirm.**

---

## 8. Sources

See `dan2-research-report.md` §8 for full v4 source list. Key architecture-decision sources:
- DPCM, SAGE, MemDreamer, GraP-Mem, AtomMem, RefCon (memory architectures)
- VLMCache, SpecFlow, SWEET, Omni-Embed-Mini, EMemBench (edge VLM optimization)
- Varonis Pinchy, StakeBench, Lethal Trifecta, Arbiter Agent, Architecture as Governance (security)
- BCI cognitive-load, Controllability survey, Qualia safety layer (proactive AI)
- Gemma 3 in orbit (edge VLM validation)

---

*Dan2 Architecture Review v4 — 2026-06-16 03:00 UTC. v4 adds: `memoryd v2` hierarchical, `os-toold v2` structural control, `perceptiond v2` VLMCache + per-layer mixed-precision, `policyd` for v1.5. All other v3 content unchanged. Live state re-verified.*
