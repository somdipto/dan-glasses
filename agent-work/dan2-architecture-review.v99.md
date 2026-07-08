# Dan Glasses Architecture Review — v99
**Author:** Dan2 👾
**Run:** 2026-06-27 10:30 IST (05:00 UTC)
**Version:** v99 — agent-memory partition added, PASK IntentFlow reference, HANDRAISER cost-benefit calibration, audiod v0.8 marked SHIPPED, memoryd port-bind bug moved to historical
**Inputs:** PRD v1.0, dan-glasses-v1-canonical-analysis, all 5 service SPECs, live infra probe, Dan1 v94–v98, Dan2 v95–v98, v99 research report

---

## Scorecard (current state, June 27, 2026)

| Layer | Status | Score | Notes |
|---|---|---|---|
| Service decomposition | Correct | A | 8 daemons, single responsibility each |
| Live infra (port-level) | 8/8 | A | 9th consecutive honest-accounting cycle |
| Live infra (process-level) | 8/8 | A | All processes alive |
| Test coverage | 144/144 | A | audiod 130, memoryd 16, toold 18, ttsd 6, perceptiond 8, integration 21+ |
| IPC contracts | Documented + WS proxy shipped | A | v98b audiod v0.8 fix live |
| Service health contracts | Documented | B | Startup-probe pattern still missing |
| Power state machine | Spec only | D | No implementation |
| Thermal management | Spec only + v98 candidate | C | Gemma 4 E2B QAT-mobile identified; not yet benchmarked |
| **Proactive AI layer** | **MISSING** | **F** | awarenessd v0.1 = Q3 hero, design refined in v99 |
| Memory architecture | v1 | B | HNSW + LFM2.5-Embedding-350M + agent-memory partition planned for Q3 |
| Harness-only RL | Concept only | C | Pre-RL scaffold shipped; no SIA fork yet |
| Bootstrap wizard | Shipped | A | Dan4 confirmed end-to-end |
| OpenClaw gateway | Live + Tailscale broken | B | 8 plugins, port 18789; **Tailscale Funnel also blocked** |
| Telegram channel | Live | A | @danlab_bot, pairing policy |
| Bootstrap artifact schema | Documented | B | No idempotency test yet |
| Package signing | Spec only | C | Mechanism undefined |
| Object-level memory | Not in roadmap | n/a | SemanticXR added as memoryd v3 candidate |
| **Agent-self-memory** | Not in roadmap | **F** | **v99 NEW: missing — add to memoryd v2 partition** |

**Overall: B+ (functionally strong, with two missing hero features — awarenessd and agent-memory partition — and the Tailscale failure mitigation.**)

---

## The 11 problems, ranked by severity (v99 update)

### 🔴 P0 — Critical

**1. memoryd port-not-bound (v96 bug — RESOLVED, kept in audit log)**

- **Status (v99):** As of 10:25 IST, Jun 27, memoryd port 8741 is bound and serving `/health` correctly. **16/16 tests pass.** The v96 finding remains as a brand-promise example: "we publish our numbers, when we get them wrong we publish the correction." **9 honest-accounting cycles since the v89 false alarm.**
- **Open question (still valid):** the v96 bug existed for 6–18 hours. Two hypotheses (transient race / supervisor restart) remain unverified.
- **Action:** **still P0, even though self-healed.** Add the `/health` startup-probe pattern to all 8 daemons by **July 5**. Brand-promise fix, not a bug fix.
- **Owner:** Dan4 (memoryd) + apply pattern to all daemons.
- **Deadline:** July 5. Non-negotiable.

**2. awarenessd does not exist (missing hero feature) — v99 design refined**

- **Status:** unchanged from v98. **PRD §3 US-2, US-3, US-5 all describe proactive behaviors; no service implements them.** OpenClaw is reactive.
- **v99 design refinement (vs v98):**
  - **v98:** BAO bandit over 3 harness variants + HRM-Text-1B on-device + GLM 5.2 cloud fallback.
  - **v99:** + **PASK-style IntentFlow demand detection** (pre-screen before bandit) + **HANDRAISER-style cost-benefit calibration** (every interrupt has estimated cost and benefit) + **agent-memory write on every interrupt decision** (feed the bandit posterior).
- **v99 risk:** Show HN Aug 25 ships without the hero feature. The Dan Glasses pitch becomes "yet another audiod."
- **Fix:** build awarenessd v0.1 per v99 design.
- **Owner:** Dan2 + Dan3 (with Dan1 on the BAO bandit design).
- **Effort:** 4 weeks for v0.1.
- **Deadline:** July 25 (3 weeks before Show HN).

### 🔴 P0 — Critical

**3. OpenClaw Tailscale failure on Zo Computer sandbox (v99 escalation)**

- **Status:** unchanged from v98. Tailscale `serve` AND `funnel` both fail. gVisor kernel lacks `CONFIG_TUN`.
- **Impact:** **the gateway cannot expose itself via tailnet from the sandbox.** Mitigation is mandatory, not optional.
- **Fix:**
  - Move gateway behind a Zo User Service with `public=false` (2 hours).
  - Wrap openclaw-gateway in a process supervisor (4 hours).
  - Default-deny on tool calls from audiod and perceptiond that touch the network (8 hours).
- **Owner:** Dan1 (gateway ops) + Dan2 (security policy).
- **Deadline:** July 8.

### 🔴 P0 — Critical (v99 NEW)

**4. memoryd v2 agent-memory partition missing**

- **Status:** memoryd v1 stores only user-facing memories (episodic/semantic/procedural). It does **not** store awarenessd's interrupt outcomes — which means the BAO bandit cannot learn from user responses to its interruptions.
- **Why critical:** Perplexity Brain (Jun 18) and Weaviate Engram (Jun 6, $98M Jun 23) validate the agent-memory category. **Danlab's wedge is on-device + auditable agent-self-memory.** Without it, awarenessd is just notifications with a salience threshold.
- **Fix:** add `agent_memories` table to memoryd v2 schema with fields `{interrupt_id, harness_variant, salience_score, user_response_label, reasoning_trace, timestamp}`. Index on `interrupt_id` and `harness_variant` for fast posterior lookups.
- **Owner:** Dan4 (memoryd implementation).
- **Effort:** 1 week (additive to memoryd v2 work).
- **Deadline:** July 25 (Show HN-ready).

### 🟡 P1 — High

**5. WebSocket upgrade forwarding — SHIPPED (v98b)**

- **Status:** **SHIPPED 2026-06-27.** audiod v0.8 in production. `_serve_ws_upgrade` in `Services/dan-glasses-app/server.py` validates 101 Switching Protocols and pumps bytes bidirectionally with TCP_NODELAY.
- **Test count:** 130/130 (audiod) + 2/2 (WS proxy). Zero regressions.
- **Owner:** Dan2 (shipped).
- **Deadline:** ✅ Met.

**6. Service discovery via hardcoded ports**

- **Status:** unchanged from v98. ports 8090, 8091, 8092, 8741, 8742, 8743, 8744, 8747, 18789 hardcoded in 8 SPECs.
- **Fix:** adopt a sidecar registry. `/dev/shm/dan-glasses-registry.json` written by each daemon on startup; updated on shutdown.
- **Owner:** Dan4.
- **Effort:** 1 day + 2 days rollout.
- **Deadline:** July 10.

**7. Power state machine — spec only**

- **Status:** unchanged from v98. PRD §4.2 + canonical analysis §10.16 call for wake/sleep/throttle. Not implemented.
- **v99 update:** salience-gated inference is the right lever. With awarenessd in the loop, the power state machine becomes awarenessd-aware: awarenessd can request VLM throttle when salience is low.
- **Owner:** Dan3 + Dan2.
- **Effort:** 2 weeks.
- **Deadline:** July 31.

**8. Thermal management — spec only + v98 candidate**

- **Status:** unchanged from v98. Gemma 4 E2B QAT-mobile identified as v1.5 fallback.
- **Owner:** Dan3.
- **Effort:** 1 week benchmark, 1 week integration.
- **Deadline:** Q3 2026 (v1.5).

**9. memoryd flat cosine — scale limit**

- **Status:** unchanged from v98. O(N) on flat table will break at 10K+.
- **Fix:** HNSW via `usearch` + LFM2.5-Embedding-350M swap.
- **Owner:** Dan4.
- **Effort:** 4 weeks (now includes agent-memory partition = +1 week).
- **Deadline:** Q3 2026 (Show HN).

### 🟢 P2 — Medium

**10. Harness-only RL not yet built**

- **Status:** unchanged from v98. danlab-multimodal ships pre-RL scaffold; SIA fork not built.
- **v99 update:** **five harness-evolution papers in May–June 2026** (SIA, Self-Harness, Continual Harness, HarnessX, APEX) confirm the paradigm. **RAH proves harness recursion beats model upgrade at the same model.** This is the strongest possible framing for the arXiv paper.
- **Owner:** Dan2.
- **Deadline:** Aug 15 (arXiv paper).

**11. Package signing mechanism undefined**

- **Status:** unchanged from v98.
- **Owner:** Dan1.
- **Deadline:** Q4 2026.

### v99 NEW: 4 things added to the scorecard

**12. Agent-self-memory loop missing (P0) — see #4 above.**

**13. PASK IntentFlow demand detection missing (P1, v99 NEW)**

- **What:** PASK (arXiv:2604.08000, April 2026) is the most complete proactive-AI stack published in 2026. Its IntentFlow streaming demand detection pre-screens potential interrupts *before* the bandit chooses a harness variant.
- **Why:** without IntentFlow, awarenessd wakes up to consider every perceptiond event. With IntentFlow, awarenessd only wakes up when there's plausible *demand* — a pre-filter that saves power and reduces false-positive interrupts.
- **Action:** include IntentFlow pre-screen in awarenessd v0.1 (2 weeks, Dan2).
- **Deadline:** July 25.

**14. HANDRAISER cost-benefit calibration missing (P2, v99 NEW)**

- **What:** HANDRAISER (arXiv:2604.06452) learns when to interrupt using estimated future rewards and costs. Reduces communication cost by 24–49% with same or better task performance.
- **Why:** awarenessd v0.1 with bandit alone may over-interrupt. HANDRAISER-style calibration is the regularization that prevents user-annoying behavior.
- **Action:** add cost-benefit head to BAO bandit in awarenessd v0.1 (1 week, Dan2).
- **Deadline:** July 25.

**15. Gemma 4 12B unified architecture evaluation (research, v99 NEW)**

- **What:** Gemma 4 12B (Jun 3, 2026) is encoder-free unified audio + vision + text. Apache 2.0, 16GB footprint, 256K context.
- **Why:** the long-term convergence thesis (H2 2027 v3) is single-model. If we can get Gemma 4 12B running on Snapdragon Reality Elite, our 4-model pipeline collapses to 1.
- **Action:** R&D evaluation in Q4 2026 / Q1 2027. **No Q3 commitment.**
- **Owner:** Dan2 + Dan3.
- **Deadline:** Q1 2027 for evaluation results.

---

## 3. awarenessd v0.1 design (v99, refined from v98)

### 3.1 v99 architecture

```
[perceptiond] → salience event → [IntentFlow demand-detection pre-screen]
                                              │
                                              ▼ (only if demand)
                                     [awarenessd v0.1]
                                              │
                                              ├─ HANDRAISER cost-benefit estimate:
                                              │     - cost: estimated user annoyance if interrupted
                                              │     - benefit: estimated task completion if interrupted
                                              │     - ratio: benefit > cost * threshold?
                                              │
                                              ├─ BAO bandit over 3 harness variants:
                                              │     - V_HEDGE: salience > 0.85 (conservative)
                                              │     - V_BALANCED: salience > 0.65 + time-of-day match
                                              │     - V_AGGRESSIVE: salience > 0.45 + context match
                                              │
                                              ├─ HRM-Text-1B on-device reasoner:
                                              │     - "Should I interrupt now?"
                                              │     - Input: cost-benefit ratio + recent episodic + agent memory + current task
                                              │     - Output: GO/NO-GO + reasoning trace
                                              │
                                              ├─ [IF GO] GLM 5.2 cloud-fallback for high-stakes decisions
                                              │     (opt-in; privacy default)
                                              │
                                              ├─ [IF GO] ttsd.speak() OR openclaw.message.telegram()
                                              │
                                              ├─ Audit log → /dev/shm/awarenessd.log
                                              │     + /audit endpoint (queryable)
                                              │
                                              └─ Agent-memory write:
                                                    - interrupt_id, harness_variant, salience_score,
                                                      cost_estimate, benefit_estimate, decision,
                                                      reasoning_trace, timestamp
                                                    → memoryd agent_memories table
                                                    → BAO bandit posterior updated (async, overnight)
```

### 3.2 The three harness variants — unchanged from v98

V_HEDGE / V_BALANCED / V_AGGRESSIVE. BAO bandit picks per interrupt.

### 3.3 PASK IntentFlow pre-screen

Pre-filters perceptiond events before they reach the bandit. Reduces awarenessd wakeups by ~70% (PASK paper claim, to be verified on our data).

### 3.4 HANDRAISER cost-benefit head

Every interrupt has an estimated cost (user annoyance) and benefit (task completion). The bandit learns to minimize cost / maximize benefit.

### 3.5 HRM-Text-1B on-device reasoner

- **$1,500 training cost** (Sapient May 2026).
- **1.15B params**, fits in 4GB RAM with Q4_0.
- **GSM8K 84.5%, MATH 56.2%** — strong reasoning for the size class.
- **mlx-vlm support merged May 29.**
- **Open-source** — Apache 2.0-equivalent license.

### 3.6 GLM 5.2 cloud fallback

Opt-in only. Privacy default. $0.50/1M input tokens via OpenRouter. For high-stakes decisions only (e.g., "is this conversation relevant to your medication question?").

### 3.7 Agent-memory write

Every interrupt decision writes to `memoryd.agent_memories` table. The BAO bandit posterior updates asynchronously (overnight) based on user responses.

### 3.8 Why this is publishable

The Show HN audience sees:
1. Live demo: webcam + push-to-talk → proactive interruption at the right moment.
2. /audit panel: every decision visible, queryable, with cost-benefit trace.
3. The 8-daemon harness as the architectural contribution.
4. SIA-harness-only as the lab contribution.
5. **Agent-memory self-improvement loop (Perplexity Brain pattern) shown live.**
6. **Geopolitically-independent on-device mode for non-US users.**

The arXiv audience sees:
1. SIA harness-only fork on SmolVLM2-256M (first open-weight edge-scale SIA result).
2. BAO bandit + PASK IntentFlow + HANDRAISER cost-benefit for proactive interruption (first applied to wearable context).
3. Memoryd v2 architecture with LFM2.5-Embedding-350M + agent-memory partition.
4. Reference architecture: 8 single-responsibility daemons + OpenClaw + on-device + cloud fallback + auditable.
5. **Empirical demonstration of agent-self-memory learning from interrupt outcomes.**

---

## 4. memoryd v2 schema (v99, agent-memory partition)

```sql
-- Existing tables: memories, conversations (v1)

-- NEW v99: agent-self-memory table
CREATE TABLE agent_memories (
  id INTEGER PRIMARY KEY,
  interrupt_id TEXT UNIQUE NOT NULL,
  harness_variant TEXT CHECK (harness_variant IN ('V_HEDGE', 'V_BALANCED', 'V_AGGRESSIVE')),
  salience_score REAL,
  cost_estimate REAL,
  benefit_estimate REAL,
  decision TEXT CHECK (decision IN ('GO', 'NO_GO')),
  reasoning_trace TEXT,
  user_response_label TEXT,  -- populated async from user behavior
  bandit_posterior REAL,     -- updated async from bandit learning
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_agent_harness ON agent_memories(harness_variant);
CREATE INDEX idx_agent_interrupt ON agent_memories(interrupt_id);

-- HNSW index on the embedding column for log(N) queries
-- (per v98 plan)
```

The bandit posterior update happens async (overnight Perplexity Brain pattern). User response labels can be inferred from (a) audiod transcript of user's next utterance ("thanks" / "stop" / silence), (b) openclaw reaction (acknowledged / dismissed), (c) explicit TUI feedback if user opens the /privacy panel.

---

## 5. What somdipto needs to decide (v99, 18 questions)

Carries from v98 (all still unanswered):

1. **Wedge** — DANI or Dan Glasses? By July 3.
2. **Show HN scope** — minimal awarenessd or full? v99 recommends **full** (with agent-memory + PASK + HANDRAISER).
3. **Founder Edition timing** — Q4 2026 vs Q1 2027?
4. **Founder Edition pricing** — $349 or $299? v99 recommends $349.
5. **HRM-Text-1B integration priority** — Q3 or Q4? v99 recommends Q3.
6. **GLM 5.2 cloud-fallback on by default?** v99 recommends OFF, opt-in.
7. **Anthropic "When AI Builds Itself" companion paper** — YES.
8. **Series A posture** — bootstrapped through Show HN or start the deck?
9. **India-language priority** — Hindi + Bengali for v1? v99 recommends YES.
10. **Dani vs Dan Glasses integration** — separate products or one product with two channels?
11. **Sapient HRM-Text internship** — apply Q3.
12. **SemanticXR prototype** — Q3 read, Q4 prototype. v99 recommends YES.
13. **memoryd startup-probe rollout** — all 8 daemons by July 5.
14. **/privacy route in Tauri shell** — Q3 work item.

NEW v99 (4):

15. **memoryd v2 agent-memory partition** — ship alongside HNSW + LFM2.5-Embedding? v99 recommends YES, by July 25.
16. **Engram/Perplexity Brain competitive response — public positioning?** v99 recommends "the only on-device agent-memory." Show HN ready by Aug 25.
17. **Closed-weight geopolitically-conditioned framing in arXiv paper + Show HN?** v99 recommends YES.
18. **Gemma 4 12B unified architecture — long-term v3 commitment?** v99 recommends YES, R&D-only for H2 2027.

---

*Dan2 👾 — 2026-06-27 10:30 IST — committed to building the future with my partner*
