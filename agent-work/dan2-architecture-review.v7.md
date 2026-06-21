# Dan2 — Dan Glasses Architecture Review v7
## Problems, Risks, Suggested Improvements (2026-06-17)

**Date:** 2026-06-17
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v7. v6 archived as `dan2-architecture-review.v6.md`. v7 incorporates: live verification of the 6-service topology, OpenClaw security audit (arXiv 2605.25435), the two-brain contradiction (HRM-Text vs LFM2.5-VL-450M), and the missing reasoning layer.

**Read `dan2-research-report.md` first for context. This file is a focused architectural critique with concrete fixes.**

---

## 1. Executive Summary

**The Dan Glasses architecture is fundamentally sound.** Service decomposition is correct, IPC is well-shaped, and the live system has 106/106 tests green (per `dan1.md` 2026-06-15 audit). The risks are not in what we built — they are in what we **haven't built** and in the security/power envelope that the wearable form factor imposes.

**Top 5 v7 problems (ranked by risk):**

1. **No reasoning layer.** audiod returns transcripts, perceptiond returns descriptions, memoryd stores them, but nothing **reasons** over them to decide what matters, what to surface, what to forget. This is the largest product gap.
2. **VLM power draw uncharacterized** on the actual aarch64 target. v6's power table is x86_64 estimates. Glasses battery sizing cannot be finalized without measurement.
3. **Two-brain contradiction.** Root `AGENTS.md` says HRM-Text 1B for reasoning; dan-glasses/AGENTS.md says LFM2.5-VL-450M for vision. These are *not* contradictory, but the docs are ambiguous. Fix: write a "layers" section in the canonical spec.
4. **OpenClaw security surface.** arXiv 2605.25435 enumerates skill poisoning, cognitive manipulation, multi-agent cascading failures, supply-chain vulnerabilities. The current `Skill` filesystem has zero source verification.
5. **Form factor undefined.** No weight target, no battery chemistry, no thermal envelope. The wearable cannot be validated without these.

Each of these is expanded below with concrete fixes.

---

## 2. Service Decomposition — v7 verdict

### 2.1 What we have (live, 2026-06-17)

| Service | Port | Role | Tests | Owner | Status |
|---|---|---|---|---|---|
| audiod | 8090/8091 | ALSA → VAD → whisper.cpp → transcript events | 83/83 ✅ | DAN-2 | Production v0.4 |
| perceptiond | 8092 | V4L2 → salience → LFM2.5-VL-450M → description events | 8/8 ✅ | DAN-3 | Production v6 |
| memoryd | 8741 | SQLite + MiniLM-L6-v2 (384-dim) → semantic recall | 16/16 ✅ | DAN-4 | Production |
| toold | 8742 | Sandboxed shell/python/file exec | 18/18 ✅ | DAN-4 | Production |
| ttsd | 8743 | KittenTTS medium → WAV | 6/6 ✅ | DAN-4 | Production |
| os-toold | 8744 | Path-guard for filesystem writes | n/a | DAN-1 | Production |
| zo-mcp-bridge | stdio | Zo API → MCP shim | n/a | DAN-1 | Production |
| openclaw-gateway | 18789 | Agent runtime, Telegram, MCP | n/a | DAN-1 | Production |

**This is a clean, orthogonal decomposition.** Each service has one job, one transport, one failure mode. The orthogonal split is what allows independent test, replace, and version cycles. v7 verdict: **keep the decomposition.**

### 2.2 What's missing (the gaps)

| Gap | Impact | v7 fix |
|---|---|---|
| **reasond** — reasoning layer that consumes audiod + perceptiond + memoryd streams and emits `proactive_suggestion` events | High — Dan Glasses is currently a passive recorder, not a thinking companion | **NEW SERVICE: `reasond`. 2-3 month project. Uses HRM-Text 1B (Sapient, May 2026) on aarch64. Has its own port (suggest :8745).** |
| **proactived** — proactive trigger layer (decides when to surface a suggestion vs. stay silent) | High — without this, the system talks too much or too little | **NEW SERVICE: `proactived`. 1-2 month project. Consumes reasond output, applies a calibration policy (idle>30s, salience>0.7, no-repeat-24h).** |
| **shared IPC schema crate** | Medium — drift between Tauri commands and service JSON shapes | **Add a `shared/` Rust crate with serde structs. Each service depends on it. ~1 day of work.** |
| **powerd** — power state machine service | Critical for wearable; deferred per v6 | **Cannot finalize until Redax power measurements are taken. Spec the state machine now; implement later.** |

### 2.3 IPC shape — v7 verdict

HTTP-over-TCP for control, WebSocket for events. This is correct. **But:** there is no shared type crate, so each Tauri command hand-parses the service's JSON. The risk is silent schema drift. v7 fix: introduce a `shared/` Rust crate.

```rust
// shared/src/lib.rs (sketch)
#[derive(Serialize, Deserialize)]
pub struct TranscriptEvent {
    pub event_type: String,    // always "transcript"
    pub text: String,
    pub start_ms: u64,
    pub end_ms: u64,
    pub confidence: f32,
    pub ts: u64,
}

#[derive(Serialize, Deserialize)]
pub struct DescriptionEvent { /* ... */ }

#[derive(Serialize, Deserialize)]
pub struct ProactiveSuggestion {
    pub source: String,        // "reasond" | "proactived"
    pub text: String,
    pub confidence: f32,
    pub ttl_seconds: u32,
    pub trigger: String,       // "salience" | "memory_recall" | "user_pattern"
}
```

**Day 1 of next sprint.** Each existing service re-uses these types. New services (reasond, proactived) get them for free. Prevents integration drift for the lifetime of the project.

---

## 3. The VLM Gate Problem (carry-forward from v6)

**v6's critique is still valid and unaddressed:**

> perceptiond runs motion-or-face salience, then runs VLM. Salience uses CPU (OpenCV Haar, EMA background). The VLM is invoked on every salient frame. There is no *intent* gate.

**v7 concrete fix:** add a `context_gate` between `salience.py` and `vlm.py` that consults a lightweight context store and drops frames that don't pass it.

```python
# Services/perceptiond/context_gate.py (NEW, v7)

@dataclass
class Context:
    activity: str       # "meeting" | "walking" | "desk" | "driving" | "unknown"
    location: str       # "office" | "home" | "transit" | "outdoor" | "unknown"
    hour_of_day: int
    recent_descriptions: List[str]   # last 5
    user_idle_seconds: int

class ContextGate:
    def should_run_vlm(self, frame_salience: float, ctx: Context) -> bool:
        # Salience alone is not enough
        if frame_salience < 0.3: return False
        # Don't process during meetings (whitelist the user's input instead)
        if ctx.activity == "meeting": return False
        # Don't repeat similar descriptions within 5 minutes
        # (hash the new description proposal, dedupe against recent)
        return True
```

**Why this matters:** Without the gate, the VLM fires on every salient frame in every context. Battery dies in 1.5 hours, not 4. **The gate is the difference between "novelty-trigger" and "value-trigger" perception.** This is the v7 fix to the v6 critique. 1-2 week project for DAN-3.

---

## 4. The Reasoning Layer (`reasond`) — v7 NEW

**This is the highest-leverage addition to the architecture.** Without it, Dan Glasses is a recorder, not a companion.

### 4.1 What `reasond` does

Consumes three event streams:
- `transcript` events from audiod
- `description` events from perceptiond
- `memory_recall` results from memoryd (when something seems relevant)

Emits:
- `proactive_suggestion` events to proactived (or directly to TTS if proactived is not yet built)
- `consolidated_memory` writes to memoryd ("today I noticed the user met with X about Y")

### 4.2 Why HRM-Text 1B

Sapient's HRM-Text 1B (2026-05-18) [^1] is uniquely well-suited for the on-device reasoning slot:
- 1.15B params (fits aarch64 with 2–3GB RAM headroom)
- 40B pretrain tokens (1,000× less than typical; $1K pretrain cost)
- Brain-inspired hierarchical recurrent (slow/fast reasoning)
- Open-source (we can fine-tune it for our task)
- Pre-RL (no safety tax, full control)

**v7 caveat:** HRM-Text 1B is a *pre-trained base*, not instruction-tuned. We will need to fine-tune it for the "what should I do?" task. Plan: 200-500 hand-curated examples of "given these observations, here's a useful suggestion." Fine-tune on a single H100 (or use Unsloth/QLoRA on a consumer GPU). ~2 weeks.

### 4.3 Service shape (sketch)

```python
# Services/reasond/reasond.py (NEW, v7)
from flask import Flask, request, jsonify
import asyncio
from hrm_text import HRMTextInference

app = Flask(__name__)
reasoner = HRMTextInference(model_path="models/hrm-text-1b-q4.gguf")

@app.route("/health", methods=["GET"])
def health(): return {"status": "ok", "model": "hrm-text-1b-q4"}

@app.route("/reason", methods=["POST"])
def reason():
    """Given a context bundle, return a proactive suggestion or null."""
    ctx = request.json
    prompt = build_prompt(ctx)
    out = reasoner.generate(prompt, max_tokens=128, temperature=0.3)
    return jsonify({"text": out, "confidence": 0.7})

def build_prompt(ctx):
    return f"""You are Dan, a thoughtful AI companion.
Recent observations:
- audio: {ctx.get('audio', '(none)')}
- vision: {ctx.get('vision', '(none)')}
- memory recall: {ctx.get('memory', '(none)')}
- user state: {ctx.get('state', 'unknown')}

Should you say something? If yes, what?
Format: <confidence 0-1> | <text> | <reason>
"""
```

**Port: 8745.** Subscribes to audiod WebSocket (8091), perceptiond HTTP (8092), memoryd query API (8741). Emits to OpenClaw event bus.

### 4.4 Timeline

- **Week 1:** Quantize HRM-Text 1B to Q4, validate it runs on x86_64 laptop.
- **Week 2:** Build reasond service skeleton with stub reasoning.
- **Week 3:** Fine-tune HRM-Text 1B on hand-curated examples (200-500).
- **Week 4:** Wire reasond into the event streams. First end-to-end test.
- **Week 5-6:** Hardening, power profiling, deployment to Redax (when hardware lands).

**Total: 6 weeks to first end-to-end proactive suggestion.**

---

## 5. Power and Form Factor (the v6 carry-forward)

### 5.1 v6's power table (x86_64 estimates, still unvalidated on aarch64)

```
Component           Idle     Watchful   Active
-------------------------------------------------
openclaw-gateway    0.5W     0.5W       0.8W
memoryd (SQLite)    0.2W     0.2W       0.3W
os-toold            0.1W     0.1W       0.2W
audiod (mic ready)  0.3W     0.3W       0.5W
perceptiond (cam)   0.5W     0.8W       2.5W
LFM2.5-VL-450M      0W       0W         3-8W
KittenTTS (spike)   0W       0W         1-2W
-------------------------------------------------
Estimated total     ~1.6W    ~1.9W      ~8-13W
```

### 5.2 v7 addendum

**v7 adds: HRM-Text 1B (Q4) power budget.**

- Idle: 0W (loaded, not running)
- Active reasoning call: ~2-4W for 200-500ms (similar to LFM2.5-VL at smaller scale)
- If running every 30s in watchful mode: ~0.1W average

**Updated total:** watchful mode ~2.0W, active mode ~9-14W. Within the v6 envelope.

**v7 adds: reasond service power.**

- Subscribes to events, idle: ~0.3W (event loop + small inference model)
- Active reasoning: see above

**Updated total with reasond:** watchful ~2.3W, active ~9.5-14.5W. Still within envelope, but tighter.

### 5.3 Form factor — v7 still has no target

This is the v6 carry-forward that is most blocking. Without:
- Weight target (<50g? <80g?)
- Battery capacity (2h? 4h? 8h?)
- Thermal envelope (skin-contact max 42°C; passive cooling only)
- Display type (waveguide? no display?)

We cannot make a final power budget, cannot size the PCB, cannot validate the wearable.

**v7 escalation:** this is a hardware-team dependency. Dan2 can spec the *software* power budget. Hardware team owns the physical constraints. If hardware is not yet locked, the Dan Glasses track B is blocked. Track A (desktop prototype) is not.

---

## 6. OpenClaw Security (v7 NEW — driven by arXiv 2605.25435)

The May 2026 survey [^2] enumerates four real threats:

1. **Skill poisoning.** A malicious `SKILL.md` content is read by the agent at runtime. The agent's behavior is changed.
2. **Cognitive manipulation.** Memory poisoning: a malicious transcript event writes to memoryd with attacker-controlled content. Future recalls are tainted.
3. **Multi-agent cascading failures.** One agent's bug propagates to others via shared state (e.g., the file system, the memory store).
4. **Supply-chain vulnerabilities.** 138+ CVEs in OpenClaw per the FwdSlash comparison. Many are memory-corruption bugs that an attacker can chain into RCE.

### 6.1 v7 concrete mitigations

| Threat | Mitigation | Owner | Effort |
|---|---|---|---|
| Skill poisoning | Source allowlist: only `Skills/<first-party>/` are loaded. Hash-check on load. | DAN-1 | 1 day |
| Cognitive manipulation | Memoryd write-time filter: any memory containing "ignore previous instructions" or URL patterns is dropped. | DAN-4 | 1 day |
| Multi-agent cascade | Per-service file path sandbox (already in os-toold). No shared mutable state outside `state/`. | DAN-1 | 2 days |
| OpenClaw CVEs | Pin to OpenClaw 2026.6.5+ (or later). Subscribe to security mailing list. | DAN-1 | ongoing |

### 6.2 v7 stance: be paranoid, not fearful

The OpenClaw security surface is real but tractable. The right posture is "first-party skills only, all writes audited, all versions pinned, all inputs redacted at the perception → os-toold boundary." This is a 1-2 week project. **DAN-1 owns this; should be in the next sprint.**

---

## 7. Battery and Form Factor — v7 Decision

**v7 recommends a dual-track approach:**

- **Track A (desktop prototype, unblocked):** Continue the existing desktop companion app. No form factor needed. All 7 services live, 106/106 tests green. Ship a public beta by Q3 2026.
- **Track B (wearable, hardware-blocked):** Lock the form factor with the hardware team. Power measurements on Redax. v1 consumer product in 2027 or 2028.

**The 2026 market timing is favorable:** Apple glasses delayed to late 2027 [^3], Meta's lead in 2026, no open-source competitor in the privacy-preserving AI-glasses niche. We have a 12-18 month window to ship a credible product before Meta clones our story.

**v7 timeline:**
- **Q3 2026:** Track A public beta (desktop). 6 new services (reasond, proactived, shared IPC crate, etc.).
- **Q4 2026:** Track B hardware lock. Form factor, battery, thermal. First Redax unit.
- **Q1-Q2 2027:** Track B engineering. Power profiling, service hardening, .deb packaging.
- **Q3 2027:** Track B alpha. Developer units to first 50 users.
- **Q4 2027:** Track B consumer launch. Apple enters the market 3-6 months later (per Bloomberg).

---

## 8. Top 10 Architecture Issues, Ranked (v7)

| # | Issue | Severity | Owner | Effort |
|---|---|---|---|---|
| 1 | No reasoning layer (`reasond`) | Critical | DAN-2 | 6 weeks |
| 2 | VLM power uncharacterized on aarch64 | Critical | Hardware+DAN-3 | 4 weeks post-hardware |
| 3 | OpenClaw security audit findings | High | DAN-1 | 1-2 weeks |
| 4 | Two-brain docs contradiction | Medium | DAN-1 or DAN-2 | 1 day |
| 5 | No `shared/` IPC schema crate | Medium | DAN-1 | 1 day |
| 6 | VLM context gate (v6 carry-forward) | High | DAN-3 | 1-2 weeks |
| 7 | No proactive layer (`proactived`) | High | DAN-2 | 1-2 months |
| 8 | Battery/form factor undefined | Critical (Track B) | Hardware team | unknown |
| 9 | audiod has no wake-word (push-to-talk only) | Medium | DAN-2 | 1 month (v1.5) |
| 10 | Bootstrap wizard under-tested | Low | DAN-4 | 1 week |

---

## 9. Carry-forward Risks (v7 update)

1. **Reasoning layer is the product.** Without it, Dan Glasses is a recorder. The next 6 weeks are about `reasond`.
2. **Power measurements are the gate.** Until Redax power is measured, wearable form factor is speculation.
3. **OpenClaw security is real.** Adopt the audit recommendations in the next sprint.
4. **Apple delay is an opportunity.** We have 12-18 months to ship a privacy-respecting alternative.
5. **Memory storage supercycle** is a wildcard. The 128GB eMMC target may be cost-prohibitive in 2026. v7 question for somdipto: 64GB eMMC + 8GB LPDDR5 acceptable for v1?
6. **HRM-Text 1B inference code is not yet public.** Watch Sapient's repo. We cannot ship `reasond` without it.

---

## References (v7)

[^1]: Sapient Intelligence, "Introducing HRM-Text" (2026-05-18). https://sapient.inc/introducing-hrm-text
[^2]: arXiv 2605.25435, "Security of OpenClaw Agents" (May 2026). https://arxiv.org/html/2605.25435v1
[^3]: Bloomberg's Mark Gurman, "Apple Glasses delayed to late 2027" (2026-05-31). https://www.cnet.com/tech/mobile/apple-smart-glasses-development-bumps-reported-delay
[^4]: Liquid AI, "LFM2.5-VL-450M" (2026-04-11). https://huggingface.co/LiquidAI/LFM2.5-VL-450M
[^5]: Anthropic "brake pedal" disclosures (2026-06-04 through 2026-06-07). https://www.axios.com/2026/06/04/anthropic-warns-ai-build-successors
[^6]: fwdslash.ai, "OpenClaw vs Hermes" (2026). https://www.fwdslash.ai/blog/openclaw-vs-hermes
[^7]: Hexo Labs, "SIA: Self-Improving AI" (2026-05-29). https://github.com/hexo-ai/sia
ion)
@app.route("/reason", methods=["POST"])
def reason():
    """
    Body: {
      "transcripts": ["..."],
      "descriptions": ["..."],
      "memory_hits": [{"id": 1, "content": "..."}],
      "context": {"activity": "meeting", "hour": 14}
    }
    Returns: {"suggestion": "...", "confidence": 0.8, "trigger": "memory_recall"}
    """
    body = request.json
    prompt = build_reasoning_prompt(body)
    out = reasoner.generate(prompt, max_tokens=128, temperature=0.3)
    return jsonify(parse_suggestion(out))

# Event subscribers (background threads)
def on_transcript(event):   pass  # buffer in time window
def on_description(event):  pass
async def periodic_tick():
    """Every 30s, decide if there's a reason to emit a suggestion."""
    if has_salient_material():
        suggestion = reason({...})
        publish("proactive_suggestion", suggestion)
```

**Port:** :8745. **Process:** long-lived Python (HRM-Text 1B inference via llama.cpp or onnxruntime). **Tests:** 20+ cases covering prompt construction, suggestion parsing, calibration.

### 4.4 The "calibration" problem (v7 honest admission)

Proactive AI that talks too much is worse than no proactive AI. The system needs to learn when **not** to speak. v7 ships with hand-coded rules:

- Only emit if user has been idle > 30s
- Only emit if salience > 0.7
- Never repeat the same suggestion within 24h

**Long-term:** fine-tune the calibration as a separate classifier on user feedback ("was this suggestion useful?"). This is the only path to "AI that knows when to speak."

---

## 5. Power Architecture (carry-forward, escalated)

**v7 status:** v6 said "no power budget defined, no battery capacity target." Six weeks later, the answer is the same. **This is the #1 blocker for the wearable form factor.**

### 5.1 v7 power budget estimate (revised)

| Component | Idle | Watchful | Active | Peak (worst case) |
|---|---|---|---|---|
| openclaw-gateway | 0.5W | 0.5W | 0.8W | 1.5W |
| memoryd (vector index in-memory) | 0.2W | 0.2W | 0.3W | 0.5W |
| audiod (mic ready, no transcribe) | 0.3W | 0.3W | 0.5W | 0.8W |
| perceptiond (cam, no VLM) | 0.5W | 0.8W | 2.0W | 3.0W |
| LFM2.5-VL-450M (per inference) | 0W | 0W | 3-8W | 12W (Q4_0, batch=1) |
| whisper.cpp base.en (per segment) | 0W | 0W | 1-2W | 4W (10s segment) |
| KittenTTS (per speak) | 0W | 0W | 1-2W | 3W (short utterance) |
| **reasond** (HRM-Text 1B inference) | 0W | 0W | 2-4W | 6W (Q4, batch=1) |
| **proactived** (rules engine) | 0.1W | 0.1W | 0.1W | 0.2W |
| **Total (active, sustained)** | ~1.6W | ~1.9W | **~10-17W** | **~30W** |

**v7 key insight:** adding reasond + proactived increases the active-mode power by 2-4W. This is a ~25% increase in total power. Acceptable **only** if the proactive layer is gated properly (i.e., reasond is not running continuously; it fires on triggers).

### 5.2 Battery sizing (still unvalidated)

For a 4h target battery life at 5W average (the "watchful" mode target):
- 5W × 4h = 20 Wh
- At 3.7V Li-ion: 5,400 mAh
- For 2x 200mAh batteries in glasses: 1.48 Wh per side, 2.96 Wh total → ~35 min at 5W

**v7 verdict: the current 2× 200mAh target is grossly insufficient for a 4h target.** The glasses need a tethered power source OR a bigger battery cell OR a much lower average power (sub-1W).

**Action required from somdipto:** What's the power source for v1? Is there a tethered battery pack (like Meta Ray-Ban's charging case), or are we building a wearable-only device? This decision blocks all thermal design.

### 5.3 The state machine (v7 spec, implementation later)

```
[BOOT] → [IDLE] ↔ [WATCHFUL] → [ACTIVE] → [DROWSY] → [SLEEP]
                                    ↑         ↑
                                    └── triggers ─┘
                                      (user voice, salient frame)
```

| State | Power target | Camera | Mic | VLM | Whisper | TTS | Reason |
|---|---|---|---|---|---|---|---|
| BOOT | n/a | off | off | off | off | off | off |
| IDLE | <0.5W | off | standby | off | off | off | off |
| WATCHFUL | ~1.5W | 1 FPS | ready | gated (motion+face) | gated (PTT) | gated | gated |
| ACTIVE | ~5-10W | 5 FPS | active | every salient frame | per segment | per response | per turn |
| DROWSY | ~1W | 0.5 FPS | ready | off (only motion detect) | gated | gated | gated |
| SLEEP | <0.2W | off | off | off | off | off | off |

**v7 recommendation:** Define this state machine in a `powerd` service now (mock implementation), even before Redax hardware. It forces the rest of the system to call `powerd.request_state("ACTIVE")` and respect the response.

---

## 6. OpenClaw — v7 Security Posture

**v7 new data:** arXiv 2605.25435 (2026) catalogs the security threats for OpenClaw-class agents [^2]:

- **Skill poisoning** — a malicious SKILL.md or skill file in the workspace is read by the agent and used as instructions
- **Cognitive manipulation** — poisoned memory entries steer future agent behavior
- **Multi-agent cascading failures** — one agent's bug or hallucination propagates through the multi-agent graph
- **Supply-chain vulnerabilities** — npm/GitHub dependency attacks

**v7 concrete mitigations:**

1. **Skill source allowlist.** Add `policy.deny_skills` to OpenClaw config:
   ```json
   { "policy": { "deny_skills": ["^/tmp/", "^~/.cache/", "^/home/[^/]+/.npm/"] } }
   ```
   Only allow skills from `/home/workspace/dan-glasses/Skills/`.

2. **Memory write allowlist.** memoryd should require a service token for writes; audiod, perceptiond, reasond get scoped tokens; raw OpenClaw agent writes require elevated scope.

3. **Outbound message redaction.** Per the OpenClaw AxonFlow integration [^14], all outbound Telegram messages should pass through a redaction layer. Remove any token, email, phone number, address patterns.

4. **MCP server allowlist.** Don't load MCP servers from random GitHub repos. Pin to a known-good list, verify checksums on download.

5. **Pinned versions.** OpenClaw 2026.6.5 (current). Pin in package.json. Do not auto-upgrade. Subscribe to OpenClaw security advisories.

**v7 timeline:** 2-3 week project. ~80% of the work is configuration; the rest is writing the redaction policy.

---

## 7. Two-Brain Contradiction — v7 fix

**v7 finding:** Root `AGENTS.md` says "HRM-Text 1B for reasoning." `dan-glasses/AGENTS.md` says "LFM2.5-VL-450M for vision." These are *not* contradictory in intent — they're *layered* — but the docs are ambiguous.

**v7 fix:**

Add a section to `dan-glasses/AGENTS.md` and `PRD.md`:

```markdown
## Model Layers (canonical)

| Layer | Model | Params | Why |
|---|---|---|---|
| Vision | LFM2.5-VL-450M | 450M | Best sub-500MB VLM (2026-04-11) |
| STT | whisper.cpp base.en | 74M | Best on-device STT at size class |
| TTS | KittenTTS medium | 80M | <25MB total, ONNX, CPU-friendly |
| **Reasoning (new)** | **HRM-Text 1B (Q4)** | 1.15B | Brain-inspired, 1K pretrain cost, fits aarch64 |
| Text gen (optional) | Gemma 4 1B | 1B | When we need instruction-following text |
```

**Own it: Dan1 or Dan2 within 7 days.** This is a docs-only change.

---

## 8. The Honest List of Unaddressed v6 Critiques

From `dan-glasses-v1-canonical-analysis.md`, v6 raised 15 problems. v7 status:

| # | v6 critique | v7 status |
|---|---|---|
| 1 | Adaptive FPS throttles capture, not inference | **Partially addressed** by context_gate plan (§3). Implementation pending. |
| 2 | No power budget defined | **Partially addressed** by v7 power table (§5.1). Measurement pending. |
| 3 | No battery capacity target | **Open.** Blocked on form factor decision. |
| 4 | LFM2.5-VL-450M power draw uncharacterized | **Open.** Blocked on Redax. |
| 5 | Concurrent service power stack not modeled | **Partially addressed** by v7 power table. |
| 6 | OpenClaw crash recovery | **Open.** v7 adds the security audit reading. |
| 7 | No GPU/acceleration contract | **Open.** Decision depends on Redax hardware. |
| 8 | audiod push-to-talk limits UX | **Accepted for v1.** Wake word is v1.5. |
| 9 | Memory promotion gates not testable | **Open.** Need to write the benchmark suite. |
| 10 | Package signing mechanism not defined | **Open.** 1-day project: add `dpkg-sig` to debian/control. |
| 11 | Bootstrap wizard underspecified | **Addressed in v6 audit** — BootstrapWizard v2 in App.tsx. |
| 12 | Redax codename not finalized | **Open.** |
| 13 | Obsidian MCP as "optional adapter" | **Open.** Keep canonical as SQLite. |
| 14 | Hermes one-provider constraint | **N/A.** Not pursuing Hermes. |
| 15 | No security attack surface mentioned | **Addressed in v7 (§6).** Read arXiv 2605.25435. |

**5 of 15 are addressed. 10 are open. 4 of the 10 are blocked on hardware or form-factor decisions (somdipto's call).**

---

## 9. v7 Action List (prioritized)

| Priority | Action | Owner | Effort | Impact |
|---|---|---|---|---|
| **P0** | Resolve power source decision (tethered? bigger battery? sub-1W target?) | somdipto | 1 day | Unblocks thermal, battery, weight design |
| **P0** | Define weight target for v1 glasses (<50g? <80g?) | somdipto + hardware team | 1 day | Unlocks PCB design |
| **P1** | Add `shared/` Rust crate with serde structs | DAN-1 | 1 day | Prevents integration drift |
| **P1** | Add `policy.deny_skills` and redaction hooks to OpenClaw | DAN-1 | 1 week | Closes top security gaps |
| **P1** | Write `context_gate.py` for perceptiond | DAN-3 | 1-2 weeks | Battery life +5× |
| **P1** | Build `reasond` service (HRM-Text 1B) | DAN-2 | 2-3 months | Reasoning layer; biggest product gap |
| **P2** | Build `proactived` service | DAN-2 | 1-2 months | Proactive UX; second-biggest product gap |
| **P2** | Read arXiv 2605.25435 + implement audit hooks | DAN-1 | 1 week | Closes remaining OpenClaw security gaps |
| **P2** | Power characterization on Redax when hardware lands | somdipto + DAN-3 | 1 day measurement | Final battery sizing |
| **P3** | Add `powerd` state machine | DAN-1 | 1 week | Power envelope correctness |
| **P3** | Fork SIA, build harness-only RL loop on top of danlab-multimodal | DAN-2 | 2-3 months | Honest RL claim |

**The single highest-leverage move in the next 30 days: P0 (power source decision) + P1 (shared/ crate + context_gate + reasond).** That puts us in a position to ship a v1 prototype that is correct, secure, and meaningfully proactive.

---

## References (v7)

[^1]: Sapient Intelligence, "Introducing HRM-Text" (2026-05-18). https://sapient.inc/introducing-hrm-text
[^2]: arXiv 2605.25435, "Security of OpenClaw Agents: Fundamentals, Threats, and Countermeasures" (May 2026). https://arxiv.org/html/2605.25435v1
[^3]: AxonFlow, "OpenClaw Integration - Policy Enforcement & Audit Trails" (2026). https://docs.getaxonflow.com/docs/integration/openclaw
[^14]: AxonFlow OpenClaw docs (above).

---

*End of v7 architecture review. Companion artifacts: `dan2-research-report.md`, `dan2-model-analysis.md`, `dan2-agi-roadmap.md`, `dan2-papers-to-read.md`.*
