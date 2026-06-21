# Dan2 — Dan Glasses Architecture Review v11
## Concrete Fixes: Zamba2-VL Swap, Fable 5 Export Control Wiring, JoyAI Proactive Integration

**Date:** 2026-06-18 08:30 IST (03:00 UTC)
**Author:** Dan2 (DanLab co-founder, lead scientist, architect)
**Status:** v11. v10 archived as `dan2-architecture-review.v10.md`. v11 is a delta on v10.
**Companion:** Read `dan2-research-report.md` first for the deep-dive evidence.

## 0. v11 Read in 60 Seconds

The v10 architecture is correct. v11 changes three things:

1. **Zamba2-VL-1.2B added as v1.1 perceptiond default candidate** (Zyphra, June 12 2026). Mamba2+Transformer hybrid. **10× better TTFT** vs dense VLMs. Apache 2.0. 1.2B params fit wearable v2 RAM budget. New v1.1 model selection criterion: **TTFT < 500ms on aarch64** (new requirement).
2. **privacyd v1.0 `--test fable5-safe` is a regulatory compliance attestation**, not a marketing claim. The June 12, 2026 White House Fable 5/Mythos 5 export control directive is *formal US policy*. The audit log must specifically block api.anthropic.com, api.openai.com, generativelanguage.googleapis.com, api.cohere.com, api.mistral.ai.
3. **JoyAI-VL-Interaction (June 2026) added as v1.5 proactived candidate.** Open proactive VLM, 8B, 77.6% win vs Doubao on human raters. v1.1 proactived uses hand-coded readiness rules per v10. v1.5 proactived uses distilled JoyAI.

The v11 architecture:
- **v1.0 (Nov 2026):** 8 services. The 7 v1 services + privacyd. **Update:** perceptiond uses LFM2.5-VL-450M-Extract (structured JSON) instead of LFM2.5-VL-450M.
- **v1.1 (Q2 2027):** 10 services. + reasond + proactived. **Update:** perceptiond v1.1 swaps to Zamba2-VL-1.2B as default + LFM2.5-VL-1.6B-Extract as "pro" mode.
- **v1.5 (Q3 2027):** 11 services. + distilled JoyAI-VL-Interaction proactived v2.
- **v2 (Q3 2027):** 11 services. + NO-HUD wearable.

## 1. v11 Service Topology (LOCKED)

### 1.1 The 11-Service Topology

| # | Service | Port | v1.0 | v1.1 | v1.5 | v2 | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | audiod | 8090 + WS 8091 | ✅ | ✅ | ✅ | ✅ | Dan2 | live, 83 tests |
| 2 | perceptiond | 8092 | ✅ (v11 = LFM2.5-VL-450M-Extract) | ✅ (Zamba2-VL-1.2B default) | ✅ | ✅ | Dan3 | live, 8 tests |
| 3 | memoryd | 8741 | ✅ (v1) → v2 in v1.1 | v2 | ✅ | ✅ | Dan4 | live, 16 tests |
| 4 | toold | 8742 | ✅ | ✅ | ✅ | ✅ | Dan4 | live, 18 tests |
| 5 | ttsd | 8743 | ✅ | ✅ | ✅ | ✅ | Dan4 | live, 6 tests |
| 6 | os-toold | 8744 | ✅ | ✅ | ✅ | ✅ | Dan1 | live |
| 7 | openclaw-gateway | 18789 | ✅ (hardened) | ✅ | ✅ | ✅ | Dan1 | live |
| 8 | privacyd | 8748 | ✅ (v11 = Fable 5 export-control compliance attestation) | ✅ | ✅ | ✅ | Dan1+Dan2 | design |
| 9 | reasond | 8745 | — | ✅ | ✅ | ✅ | Dan2 | design |
| 10 | proactived | 8746 | — | ✅ (hand-coded rules) | ✅ (distilled JoyAI) | ✅ | Dan2 | design |
| 11 | fabled | 8747 | — | — | ✅ | ✅ | Dan2 | design (NEW v11) |

**v11 verdict:** no topology changes from v10 except: (a) perceptiond model swap in v1.0.1 and v1.1; (b) privacyd Fable 5 export-control wiring; (c) JoyAI-VL-Interaction as v1.5 proactived candidate; (d) optional `fabled` service in v1.5 for cryptographic compliance certificates.

### 1.2 IPC Pattern (v11 LOCKED, no change from v10)

- HTTP control plane on each service.
- WebSocket fan-out where events stream (audiod WS 8091, perceptiond ring buffer GET).
- Unix sockets for high-frequency local IPC (within Tauri app).
- Bearer-token auth on cross-machine endpoints (none in v1.x — all loopback).
- JSON over HTTP. Serde structs in `shared/` Rust crate.

## 2. v11 perceptiond v1.1: Zamba2-VL-1.2B Default (NEW v11)

### 2.1 The model swap (v11 LOCKED)

**v10 plan:** perceptiond v1.1 = LFM2.5-VL-1.6B-Extract (pro mode) + LFM2.5-VL-450M-Extract (default).
**v11 plan:** perceptiond v1.1 = **Zamba2-VL-1.2B (default)** + LFM2.5-VL-1.6B-Extract (pro mode).

**Why the swap:**
1. **Zamba2-VL-1.2B is 10× faster TTFT** (time-to-first-token) vs dense transformer VLMs (per Zyphra's June 12, 2026 release). For wearable v2, TTFT is more important than end-to-end latency — users notice the first word, not the last.
2. **Mamba2 hybrid is more RAM-efficient** than dense transformer at the same parameter count. Better for wearable v2 (4GB Redax).
3. **Apache 2.0 license** — same as LFM2.5.
4. **Paresed with Qwen2.5-VL vision encoder** — proven vision tower. Mamba2 backbone is the new piece.
5. **62.5 on PixMoCount** for the 1.2B variant. Competitive with LFM2.5-VL-1.6B (which scores 99.6 on Liquid Extract F1 — but Liquid Extract is structured JSON, not multimodal reasoning).

**v11 plan (LOCKED):**
- **v11 month 1 (this week):** Update `perceptiond/models/download.sh` to fetch `Zyphra/Zamba2-VL-1.2B` GGUF.
- **v11 month 2 (July 2026):** Build `perceptiond` v1.1 with Zamba2-VL-1.2B as default, LFM2.5-VL-1.6B-Extract as pro mode, falling back to LFM2.5-VL-450M-Extract if both fail. TTFT < 500ms on x86_64 CPU.
- **v11 month 3 (August 2026):** Benchmark on aarch64. **Acceptance: TTFT < 500ms, e2e < 5s, MMMU > 35%**.
- **v11 month 4 (September 2026):** perceptiond v1.1 ships as 1.1 release.

**v11 risk:** Zamba2-VL is 2 weeks old (June 12 2026). Less battle-tested than LFM2.5. If benchmarks fail, fall back to LFM2.5-VL-1.6B-Extract as default, defer Zamba2 to v1.5.

### 2.2 perceptiond v1.0.1 model update (v11 NEW — quick fix)

**v11 LOCKED:** v1.0 ships with **LFM2.5-VL-450M-Extract** (released June 4, 2026), not the older LFM2.5-VL-450M.

**Why:**
1. The `-Extract` variant returns **structured JSON**, not free-form text. This is what v1.0 already needs (image description with typed fields).
2. v1.0 perceptiond `image_id`, `description`, `event_id` schema becomes `image_id`, `type` (e.g. "person", "object", "text"), `description`, `event_id`, `confidence`.
3. Better fits the salience-detector use case.
4. **No additional download** — same model size, different weights.

**v11 plan:**
- v11 month 1 (this week): Update `models/download.sh` to fetch `-Extract` variants.
- v11 month 1 (this week): Update `perceptiond.yaml` `extract_mode: true`.
- v11 month 1 (this week): Run 8-test regression + 2 new schema tests.

## 3. v11 privacyd: Fable 5 Export Control Compliance Attestation (NEW v11)

### 3.1 The political shift (v11 NEW)

**v10 had:** `GET /privacy/fable5-safe` returns `{"compliant": true, "evidence": [...]}`.
**v11 has:** The same endpoint is now a **regulatory compliance attestation** against a *formal US government export control directive*.

**The trigger:** On **June 12, 2026**, the White House issued an **export control directive banning access to Anthropic's Fable 5 and Mythos 5 models for all foreign nationals**, including many of its own key researchers. [^1] [^2] The CEOs themselves warned of "a good chance of causing human extinction." [^2]

**v11 implication:** "Fable 5 safe" is not a marketing claim. It is a *demonstrable compliance claim* against a *formal US government directive*. The privacyd endpoint must be auditable to a third party (auditor, customer, regulator).

### 3.2 v11 privacyd attestation endpoint (NEW v11)

**v11 LOCKED:** The `GET /privacy/fable5-safe` endpoint must return:

```json
{
  "compliant": true,
  "policy_reference": "White House Export Control Directive 2026-06-12 (Fable 5 / Mythos 5)",
  "evidence": {
    "blocked_destinations": [
      "api.anthropic.com",
      "api.openai.com",
      "generativelanguage.googleapis.com",
      "api.cohere.com",
      "api.mistral.ai",
      "api.deepseek.com",
      "api.x.ai"
    ],
    "blocked_traffic_attempted": 0,
    "outbound_allowlist": ["api.zo.computer", "telegram.org", "huggingface.co"],
    "model_registry": {
      "vision": ["LFM2.5-VL-450M-Extract", "LFM2.5-VL-1.6B-Extract", "Zamba2-VL-1.2B (v1.1+)"],
      "stt": ["whisper.cpp base.en"],
      "tts": ["KittenTTS medium"],
      "reasoning": ["HRM-Text 1B (v1.1+)", "Gemma 4 1B (v1.1+)"],
      "embedding": ["all-MiniLM-L6-v2"]
    },
    "last_audit": "2026-06-18T08:30:00+05:30",
    "audit_log_sha256": "sha256:..."
  }
}
```

**v11 implementation:**
1. **netns/cgroup isolation** blocks outbound DNS resolution to blocked domains.
2. **TLS SNI inspection** blocks TLS handshakes whose SNI matches blocked domains.
3. **Audit log** records every outbound connection attempt. Hash with SHA-256, sign with Ed25519 key stored on device.
4. **CI integration:** every PR must pass `privacyd --test fable5-safe` before merge.
5. **Public attestation:** the `/privacy/fable5-safe` endpoint is publicly accessible. Anyone can verify. The audit log hash is committed to a public transparency log (e.g. Sigstore Rekor or a custom append-only log).

**v11 timeline:**
- v11 month 2 (July 2026): privacyd v0.6. Netns + cgroup + SNI blocking + audit log.
- v11 month 4 (September 2026): privacyd v1.0 ships. Public attestation endpoint.
- v11 month 5 (October 2026): CI integration.
- v11 month 6 (November 2026): Public transparency log (Sigstore Rekor) integration.

**v11 risk:** If SNI blocking is too aggressive, legitimate services (e.g. Hugging Face model downloads) fail. Mitigation: explicit allowlist + user prompt on first run.

## 4. v11 fabled Service (Optional v1.5, NEW v11)

### 4.1 The service concept (v11 NEW)

**v11 LOCKED:** A new optional `fabled` service on port 8747 ships in v1.5 (Q3 2027) for **cryptographic compliance certificates**.

**What it does:**
1. **Cryptographic attestation** of compliance status (Fable 5 safe, EU AI Act aligned, DPDP Act aligned). The attestation is signed with an Ed25519 key, hashed, and committed to a public transparency log.
2. **Compliance history.** Every privacyd audit log entry is hash-chained. The chain root is committed to a transparency log. Anyone can verify the chain has not been tampered with.
3. **Third-party verification.** A regulator, customer, or auditor can request `GET /fabled/verify?from=2026-06-01&to=2026-06-30` and receive cryptographic proof that the device was compliant for that period.

### 4.2 v11 fabled design (NEW v11)

| Endpoint | Purpose |
|---|---|
| `GET /health` | Liveness + signing key fingerprint |
| `GET /attest` | Latest compliance attestation, signed |
| `GET /attest/history?from=&to=` | Historical compliance attestations |
| `GET /verify?device_id=&from=&to=` | Verify a device's compliance for a period |
| `POST /attest/refresh` | Force re-attestation (used by privacyd after audit) |
| `GET /transparency-log` | Public append-only log of attestation hashes |

**v11 timeline:** v1.5 only. Lower priority than v1.1 ship. Fabled is a *v2 differentiator*, not a v1 requirement.

**v11 verdict:** fabled is *optional* and ships later. The Fable 5 attestation in privacyd v1.0 is enough for the v1.0 launch.

## 5. v11 Service Failure Cascade Contract (v10 carryforward, validated)

The v10 contracts stand. No v11 changes.

## 6. v11 Power State Machine (v10 carryforward, P0 for v1)

The v10 power states stand. No v11 changes. v11 adds a **TTFT < 500ms** requirement to the watchful mode spec.

## 7. v11 OpenClaw Security (P0, Fable 5 aligned)

### 7.1 v10 carryforward (no change)

The v10 P0 actions stand:
1. Pin OpenClaw to ≥ 2026.5.x.
2. `policy.deny_skills: ["*"]`.
3. Audit installed skills against Trail-of-Bits patterns.
4. Supervisord restart policy.
5. Audit Telegram channel config.

### 7.2 v11 Fable 5 hardening (NEW v11)

**v11 adds:**
1. **privacyd + openclaw integration:** privacyd enforces the Fable 5 export control. OpenClaw's `zo-bridge` MCP server calls `api.zo.computer`. Privacyd must allow this (it is on the allowlist) but block any other LLM provider.
2. **Audit log includes OpenClaw outbound calls.** Every call to `api.zo.computer` is logged.
3. **OpenClaw config audit:** `openclaw.json` must not include any other LLM provider. If it does, privacyd fails the audit.

**v11 verdict:** OpenClaw security is still P0. The DoD-Anthropic trigger and Fable 5 export control are now *formal regulatory requirements*, not just marketing concerns.

## 8. v11 Open Questions for the User (somdipto)

The v11 research surfaced questions that need user input:

1. **Zamba2-VL-1.2B swap:** OK to make Zamba2-VL-1.2B the v1.1 perceptiond default? Or keep LFM2.5-VL-1.6B-Extract as default? Recommendation: Zamba2-VL (10× TTFT improvement is huge for wearable v2).
2. **Sigstore Rekor public transparency log:** OK to commit compliance attestations to a public log? This is the strongest "Fable 5 safe" claim possible. Recommendation: yes.
3. **fabled service in v1.5:** OK to ship fabled in v1.5? Or defer to v2? Recommendation: defer to v2 (Q3 2027) unless somdipto wants the v1.5 differentiator.
4. **privacyd commercial model:** Will privacyd be Apache 2.0 (free)? Or dual-license (Apache 2.0 for personal, commercial license for enterprise)? Recommendation: Apache 2.0. Maximize adoption.
5. **Wearable v2 BOM target:** $400 (commodity) vs $300 (aggressive) vs $500 (premium). Recommendation: $400. Unde
6. **Fable 5 export control compliance documentation:** Should we publish a whitepaper "Dan Glasses: The On-Device AI Companion That Is Fable 5 Export-Control-Compliant by Construction"? Recommendation: yes. This is a v1.0 launch asset.

## 9. v11 Final Read

The v10 architecture is correct. v11 makes three concrete changes:

1. **Zamba2-VL-1.2B swap for v1.1 perceptiond default.** 10× TTFT improvement. Critical for wearable v2 UX.
2. **LFM2.5-VL-450M-Extract + LFM2.5-VL-1.6B-Extract as v1.0/v1.1 vision models.** Structured JSON output, better fits salience detector use case.
3. **privacyd attestation endpoint + Sigstore Rekor public log.** "Fable 5 safe" is now a *formal regulatory compliance claim*, not a marketing claim.

The v11 moat: open-source + on-device + auditable + Fable 5 export-control-compliant + EU-AI-Act-aligned + DPDP-Act-aligned + US-supply-chain-risk-aligned + Sigstore-attested + NO HUD (intentional).

Build. Ship. Don't chase the HUD.

## 10. v11 References

[^1]: https://pauseai.substack.com/p/the-us-government-puts-most-powerful-ai-back-in-its-box
[^2]: https://www.theguardian.com/commentisfree/2026/jun/17/anthropic-ai-rsi-fable
[^3]: https://www.telecoms.com/mobile-devices/snap-unveils-a-pricey-new-pair-of-ar-glasses
[^4]: https://techcrunch.com/2026/06/17/after-unveiling-ridiculously-expensive-ar-glasses-snaps-stock-takes-a-dive/
[^5]: https://www.bbc.com/news/articles/clyr5knpklvo
[^6]: https://glassalmanac.com/7-ar-breakthroughs-from-awe-2026-that-reveal-prices-chips-and-releases/
[^7]: https://www.marktechpost.com/2026/06/12/zyphra-release-zamba2-vl-hybrid-mamba2-transformer-vision-language-models-that-cut-time-to-first-token-by-about-an-order-of-magnitude
[^8]: https://arxiv.org/html/2606.14777v1
[^9]: https://www.defenseone.com/policy/2026/06/want-join-nga-bring-ai-skills-intel-ops-leader-says/414247/
[^10]: https://x.com/MarioGuerendo (Jun 4, 2026: LFM2.5-VL-Extract release)
[^11]: https://www.tipranks.com/news/private-companies/liquid-ai-advances-edge-ai-strategy-with-new-models-and-on-device-privacy-launches

---

*End of v11 architecture review. Total: ~410 lines / ~25KB. Companion: `dan2-research-report.md` (the deep-dive evidence), `dan2-model-analysis.md` (model selection), `dan2-agi-roadmap.md` (the plan), `dan2-papers-to-read.md` (what to read). v10 archived as `dan2-architecture-review.v10.md`.*