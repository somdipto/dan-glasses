# DAN-4 — TTS + Memory Stream

## Status: SHIPPED + GREEN ✅ (v118 — re-verification pass)

All four parts live, tested, and end-to-end green via the dan-glasses-app proxy. No code changes this run; pure re-verification + scratchpad bump. v118 fixes a probe-typo regression from v116/v117: I had been curl-ing `POST /remember` (404) and `POST /invoke` (404) instead of the real `POST /memories` and `POST /exec` routes, and using `POST /query` (405 — it's GET) — every one of those 404/405s was a probe bug, not a service bug. The OpenAPI enumeration below confirms the real routes, and the probes against the real routes all return 200 with the expected payloads.

## Live services (2026-07-09 22:18 IST, this run)

| svc | port | status |
|---|---|---|
| memoryd | 8741 | ok (model loaded, 384-dim) |
| toold | 8742 | ok |
| ttsd | 8743 | ok (KittenTTS `medium`, 8 voices) |
| dan-glasses-app | 8747 | ok (5/5 proxy, 154ms total) |

## Real routes (OpenAPI enumerated, this run)

- memoryd (8741): GET /health /ready, GET /query, POST /memories /conversations /v1/embeddings, GET /memories /memories/{id} /memories/by-type/{type} /stats, DELETE /memories/{id}
- toold  (8742): GET /health /ready /version /test /registry, POST /exec /exec/python /exec/file /exec/with-tool /registry/{name}/{enable,disable} /registry/tools
- ttsd   (8743): GET /health /voices /models, POST /speak /play

## Live e2e (this run)

```
memoryd POST /memories  {type:"episodic", content:"DAN-4 reverify ping"}  → 200 {id:1655, embedding_id:"vec_1655"}
memoryd GET  /query?text=dan-4+ping&k=3  → top: 1655 (0.868)  ← the memory I just wrote, surfaces immediately
memoryd POST /v1/embeddings {input:["hello world","goodbye world"]}
  → object=list count=2 dim=384 norm=1.0000 cos01=0.5341 ✅
toold  POST /exec {command:"echo dan4-alive && date -u +%FT%TZ"}
  → 200 {success:true, exit_code:0, stdout:"dan4-alive\n2026-07-09T16:48:48Z", duration_ms:4}
ttsd   POST /speak {text:"DAN-4 verification ping"} → 200, 235 258 B WAV (RIFF/IEEE Float mono 24 kHz, 1.85s)
app    GET  /api/services/health → 5/5 up, 154ms total
```

## Test totals (this run)

- memoryd: 17 (test_memoryd.py) + 15 (test_wizard_roundtrip.py) = 32 ✅
- toold: 21 ✅
- ttsd: 6 ✅
- dan-glasses-app: 18 (test_wizard_proxy_roundtrip.py) ✅
- **Total: 77 / 77 pass** — memoryd 32 + toold 21 + ttsd 6 + app 18

## v118 — this run

- Caught and corrected probe-schema drift: v116/v117 had been pinging non-existent `POST /remember`, `POST /invoke`, `POST /query` (all 404/405). Enumerated the real routes via `/openapi.json` and re-ran the full real-schema e2e
- All 4 test files run individually, 77/77 pass: memoryd 32, toold 21, ttsd 6, app 18
- memoryd `/query` is GET, not POST — fixed; the new id=1655 I just wrote now ranks #1 (cosine 0.868) for "dan-4 ping"
- memoryd `/v1/embeddings` confirmed: object=list, dim=384, norm=1.0000, two distinct vectors
- toold `/exec` confirmed: real `{command, timeout?}` schema, exit 0, 4ms
- ttsd `/speak` confirmed: 235KB WAV for short sentence, valid RIFF header
- 5/5 services green via app proxy, 154ms total
- Committed scratchpad bump; no service code changes

## v117 — re-verification pass (prior)

- 77/77 tests pass; 5/5 services green via :8747 proxy
- All claims above are for the live build, not test mocks

## Files (DAN-4 surface)

- Services/memoryd/{memoryd.py, SPEC.md, test_memoryd.py, test_wizard_roundtrip.py}
- Services/toold/{toold.py, SPEC.md, test_toold.py}
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
- (v118) re-verification: corrected probe-schema drift, 77/77 tests, 5/5 services, 154ms proxy, real routes enumerated via OpenAPI
