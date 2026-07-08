# Dan2 — Dan Glasses Architecture Review (v33)
**Date:** 2026-06-20 06:30 UTC (12:00 IST)
**Status:** v33 — sharpened with June 16-20 market changes
**Scope:** Problems, risks, and suggested improvements for the Dan Glasses desktop + wearable architecture

---

## 0. TL;DR

The architecture is **solid as a desktop companion** and **under-specified as a wearable**. The shipped system is now strong: audiod v6, perceptiond v4, memoryd v1, toold v1, ttsd v1, OpenClaw gateway, Tauri v2 frontend. The new 2026 pressure comes from outside the repo: Snap Specs proved that display glasses are real but expensive; Apple shifted Siri AI to watchOS 27; the memory crisis made compute and memory budgets a product constraint; and the self-improving-agent literature matured to the point that the current "pre-RL scaffold" label is no longer defensible for the long-term product path.

The main problems are now **not software correctness**. They are:
1. **No explicit wearable power budget**
2. **No measured sub-1W silicon path**
3. **No memoryd v2 / proactive memory design**
4. **No audited skill evolution path for the agent stack**
5. **No formal security model for model-generated actions in a privacy-sensitive wearable**

---

## 1. What is correct and should stay

| Decision | Status | Why it is correct |
|---|---|---|
| **Tauri v2 + .deb + systemd** | Locked | Correct deployment story for desktop companion. |
| **OpenClaw orchestration (TypeScript/Node)** | Locked | Correct control plane; TS-native integrations matter. |
| **Python daemons on localhost HTTP** | Works | Easier debugging and better fit for the current stack than forcing Rust. |
| **V4L2-first generic camera provider** | Locked | Avoids vendor lock-in. |
| **SQLite + Markdown + vectors** | Locked | Right durability + inspectability tradeoff. |
| **salience-gated VLM** | Shipped | Correct power lever. |
| **whisper.cpp + KittenTTS** | Correct v1 choice | Small, offline, and good enough. |
| **Model download on first run** | Locked | Correct for package size and update flow. |
| **Service health contracts + failure matrix** | Locked | Needed for reliable degraded modes. |

---

## 2. Critical gaps that still block the wearable

### Gap 1: No real wearable power budget
**Severity:** CRITICAL

We still lack a documented envelope for:
- target average watts
- burst watts
- thermal ceiling
- battery capacity
- minimum battery life
- what happens when the budget is exceeded

This is not an academic omission. It determines:
- battery size
- PCB size
- heat spread
- model selection
- whether the product is glasses, a pendant, or a desk companion pretending to be glasses

**Fix:** publish a power table with target / measured / ceiling numbers and tie service modes to it.

---

### Gap 2: No measured sub-1W path
**Severity:** CRITICAL

OpenGlass (GAP9 + event camera) shows the category is possible. But Dan Glasses has not measured:
- LFM2.5-VL-450M on Hailo-10H / Hailo-15
- SmolVLM / LFM2.5 on GAP9-class silicon
- event-camera-based capture
- actual inference power under sustained load

Without this, the wearable plan is aspirational.

**Fix:** buy the dev kits and measure. No more paper architecture.

---

### Gap 3: memoryd v1 is not enough for v2 ambition
**Severity:** HIGH

memoryd v1 is a good prototype. It is not a memory system that can support continual learning, proactive initiation, or audit-grade recall. The current embedding model + SQLite BLOB approach is fine for the desktop, but it will not hold up as the lab's AGI moat.

**Fix:** memoryd v2 needs:
- extraction / reflection / update / search pipeline
- temporal memory
- skill lifecycle governance
- proactive retrieval policy
- traceable consolidation

---

### Gap 4: no formal skill evolution path
**Severity:** HIGH

The danlab-multimodal loop is still hand-coded scoring. The external research now shows the stronger pattern is:
- harness search
- trace-derived skills
- skill governance
- replayable evaluation
- population / verifier-driven selection

**Fix:** treat Dan1/Dan2/Dan3/Dan4 docs as trainable artifacts, but put them through SkillsVote + SkillOpt + SEAGym-style evaluation.

---

### Gap 5: security model is not mature enough for a privacy wearable
**Severity:** HIGH

Smart glasses are controversial because camera + mic devices can be abused. Meta NameTag proves even dormant biometric code is a reputational hazard. Dan Glasses needs a stronger security story than "local-first".

**Fix:**
- default-deny for high-risk actions
- trace IDs for every camera/audio → tool path
- explicit consent gates for capture and action execution
- per-service degraded modes
- auditable logs for all actions

---

### Gap 6: OpenClaw crash recovery is still a single-point-of-failure risk
**Severity:** HIGH

The gateway is the control plane. If it dies, the user experience dies.

**Fix:**
- watchdog + restart policy
- session checkpoint / resume
- heartbeat from all services
- visible reconnect state in UI

---

## 3. Updated architecture recommendations

### 3.1 Desktop companion remains the right v1 surface
Do not force the wearable timeline to block the desktop companion. The desktop app is the best place to validate:
- audiod
- memoryd v2
- skill evolution
- proactive behavior
- MCP / OpenClaw flows

### 3.2 Wearable should be camera+voice first
Snap Specs proved display glasses are real but expensive. Dan Glasses v1 should be:
- no display
- camera + voice + memory + proactive assistant
- auditable behavior
- on-device only

The display can come later once power and thermal are validated.

### 3.3 Move from reactive to proactive
The current stack responds well. It does not initiate enough.

Add a proactive layer that watches:
- time of day
- recent memory deltas
- salient vision events
- user activity gaps
- repeated unresolved tasks

This should trigger:
- memory recall
- reminder generation
- TTS prompts
- safe suggestions

### 3.4 Separate harness evolution from model capability
Use three layers:
1. **Harness / skill docs** — fast, auditable, cheap
2. **Memory / retrieval** — medium-term learning
3. **Weights** — rare, gated, population-based

This is the right engineering compromise between SIA, Meta-Harness, SkillsVote, and safety.

---

## 4. Bottlenecks, ranked

1. **Wearable power budget**
2. **Sub-1W silicon path measurement**
3. **memoryd v2 design and eval harness**
4. **proactive initiation**
5. **gateway recovery**
6. **traceability and consent**
7. **model acceleration / caching**

---

## 5. Suggested improvements

### Week 1
- Define power budget table.
- Buy dev kits.
- Add trace IDs through audiod → memoryd → OpenClaw → TTS.
- Add gateway watchdog.

### Week 2
- Stand up a SEAGym-style eval harness.
- Add skill governance workflow.
- Define proactive trigger rules.

### Month 1
- Measure LFM2.5 and fallback models on real silicon.
- Spike memoryd v2 ingest/retrieve/consolidate architecture.
- Spike VLMCache in perceptiond.

### Month 2-3
- Fork SIA-H / Meta-Harness / SkillsVote style loops.
- Make memoryd v2 the open-source moat.
- Decide whether the wearable uses display or remains camera+voice.

---

## 6. Bottom line

The architecture is good enough to ship the desktop product. It is **not yet enough** to claim a believable wearable future. The next decisive work is not more UI; it is power, memory, eval harnesses, and proactive behavior.
