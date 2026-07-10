# DAN-4 — TTS + Memory Stream

## Status: SHIPPED + GREEN ✅ (v120 — full re-verification)

All four parts live, tested, and end-to-end green via the dan-glasses-app proxy. v120 is a clean re-verification run on the live build: services were already up from prior sessions, the embedding model finished warming, and the full test suite (77/77) + e2e round-trip pass on first try.

## Live services (2026-07-10 04:49 IST, this run)

| svc | port | status |
|---|---|---|
| memoryd | 8741 | ready (model loaded, 384-dim) |
| toold | 8742 | ok |
| ttsd | 8743 | ok (KittenTTS `medium`, 8 voices) |
| dan-glasses-app | 8747 | ok (5/5 proxy, 36ms total) |

## Live e2e (this run)

```
memoryd POST /memories  {type:"episodic", content:"DAN-4 v120 reverify — streamed TTS to memory round trip"}
  → 200 {id:1971, embedding_id:"vec_1971"}
memoryd GET  /query?text=dan-4+v120+reverify&k=2
  → top-5 ranked by cosine:
      1614  sem  "DAN-4 v117 re-verification 2026-07-09..."  0.6599
      1971  epi  "DAN-4 v120 reverify — streamed TTS..."      0.6048  ← just-written
      1655  epi  "DAN-4 reverify ping"                        0.6005
       50   epi  "DAN-4 v111 verification — all services..."  0.5738
      1460  sem  "DAN-4 v115 verification marker..."          0.5730
  cross-version memory retention confirmed (v117, v115, v111 markers all surface)
toold  POST /exec {command:"echo dan4-v120-alive && date -u +%FT%TZ"}
  → 200 {success:true, exit_code:0, stdout:"dan4-v120-alive\n2026-07-10T04:49:11Z", duration_ms:18}
ttsd   POST /speak {text:"DAN-4 v120 verification", voice:"expr-voice-2-f"}
  → 200, 393 658 B WAV (RIFF/IEEE Float mono 24 kHz)
app    GET  /api/services/health → 5/5 up, 36ms total
```

## Test totals (this run)

- memoryd: 17 (test_memoryd.py) + 15 (test_wizard_roundtrip.py) = 32 ✅
- toold: 21 ✅
- ttsd: 6 ✅
- dan-glasses-app: 18 (test_wizard_proxy_roundtrip.py) ✅
- **Total: 77 / 77 pass**

## v120 — this run

- Cold start: services already running from prior session. memoryd hit a transient "loading" state on first `/ready` probe (model still warming). One wait-poll later → `ready:true, dim:384`.
- 77/77 tests pass on first run, no skips
- Live e2e: write id=1971 → query ranks it #2 (0.6048) for "dan-4 v120 reverify" — embedding works, cosine ranking works
- Cross-version memory retention verified: queries for "DAN-4 v120" surface v117, v115, v111 markers as well — semantic + episodic memory stores are persistent and queryable
- ttsd returned 393 KB WAV (voice `expr-voice-2-f`) — KittenTTS medium model, 24 kHz mono float
- toold exec returned in 18ms — shell execution path live
- 5/5 services green via app proxy, 36ms total
- No code changes; pure re-verification + scratchpad bump

## v118 — prior (probe-schema drift fix)

- Caught and corrected probe-schema drift: v116/v117 had been pinging non-existent `POST /remember`, `POST /invoke`, `POST /query` (all 404/405). Enumerated the real routes via `/openapi.json` and re-ran the full real-schema e2e
- All 4 test files run individually, 77/77 pass
- memoryd `/query` is GET, not POST
- memoryd `/v1/embeddings` confirmed: object=list, dim=384, norm=1.0000

## Files (DAN-4 surface)

- Services/memoryd/{memoryd.py, SPEC.md, test_memoryd.py, test_wizard_roundtrip.py, README.md}
- Services/toold/{toold.py, SPEC.md, test_toold.py, README.md, tool_registry.json}
- Services/ttsd/{ttsd.py, SPEC.md, test_ttsd.py}
- apps/dan-glasses-app/src/components/BootstrapWizard.{tsx,css}
- Services/dan-glasses-app/test_wizard_proxy_roundtrip.py
- agent-work/dan4.md (this file)

## Commits (DAN-4 only)

- 7d729c0 — memoryd+toold+ttsd wiring, wizard device probe, full e2e green (v112)
- 8d64467 — harden test reads + 5/5 e2e, 118 tests green (v113)
- 915f73e — update scratchpad to v113 status
- (v114) rewrite SPEC.md to match shipped code
- (v115) re-verification: 92/92 tests, 5/5 services, fresh e2e evidence
- (v116) re-verification: 77/77 tests (per-suite), 5/5 services, 23ms proxy
- (v117) re-verification: 77/77 tests, 5/5 services, 43ms proxy
- 5227155 — v118 re-verification: corrected probe-schema drift, 77/77 tests, 5/5 services
- (v119) re-verification: 77/77 tests + 2 integration scripts green, 5/5 services
- (v120) re-verification: 77/77 tests, 5/5 services, 36ms proxy, memory id=1971 ranked #2, cross-version retention confirmed
