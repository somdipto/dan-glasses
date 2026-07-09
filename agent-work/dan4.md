# DAN-4 — TTS + Memory Stream

## Status: SHIPPED + GREEN ✅ (v115 — re-verification pass)

All four parts live, tested, and end-to-end green via the dan-glasses-app proxy. No code changes this run; pure re-verification + scratchpad bump.

## Live services (2026-07-09 10:15 IST, this run)

| svc | port | status |
|---|---|---|
| memoryd | 8741 | ok (model loaded, 1425 memories, 384-dim) |
| toold | 8742 | ok (4 tools) |
| ttsd | 8743 | ok (KittenTTS `medium`, 8 voices) |
| audiod | 8090 | ok (publish: stdout) |
| perceptiond | 8092 | ok |
| dan-glasses-app | 8747 | ok (5/5 proxy, 46–96ms total) |

## Live e2e (this run)

```
memoryd /ready=true  at  t=21s  (cold model load → warm)
memoryd /stats       1425 memories (episodic 1152 / semantic 150 / procedural 123), 34 conversations, 12.96 MB
memoryd POST /memories  →  id=1460  (DAN-4 v115 verification marker)
memoryd GET  /query?text="DAN-4 v115"  →  top-3 hits all green:
  - 50    episodic  0.7754  DAN-4 v111 verification — all services green
  - 1460  semantic  0.7569  DAN-4 v115 verification marker — services online, end-to-end green.
  - 72    episodic  0.6874  DAN-4 verification ping
memoryd /v1/embeddings (OpenAI-compat)  →  idx=0/1 dim=384  ✅
toold    /test    4/4 in 87ms (shell, python, file, registry)
ttsd     /speak   200, 501 658 B RIFF/WAVE IEEE Float mono 24 000 Hz, 11.2s
app      /api/services/health  5/5 up, 96ms total
```

## Test totals (this run)

- memoryd: 17 (test_memoryd.py) + 15 (test_wizard_roundtrip.py) = 32 ✅
- toold: 21 ✅
- ttsd: 6 ✅
- dan-glasses-app: 18 (test_wizard_proxy_roundtrip.py) ✅
- **Total: 92 / 92 pass** (was 91 + 2 skip; no skips this run, all went green)

## Wizard (apps/dan-glasses-app/src/components/BootstrapWizard.tsx)

- 651 LOC TSX + 280 LOC CSS
- Polls `/api/services/health` every 3 s (single round trip)
- 6 steps: memoryd · toold · ttsd · audiod · perceptiond · devices
- TTS step: voice picker + name + `probeKittenTTS()` (voices + models + sample bytes) → `<audio>` via `URL.createObjectURL`
- Memory step: writes 3 memory types + query roundtrip; persists voice pref as `semantic` memory
- Devices step: `enumerateDevices()` + `getUserMedia({audio:true})` → RMS peak
- `localStorage` key `dan-glasses:bootstrap:v1` survives reloads

## v115 — this run

- Re-ran all live probes via :8747 proxy: 5/5 up, 96ms
- Re-ran all 4 test files: 92/92 pass
- Verified `/v1/embeddings` (OpenAI-compat) returns 384-d vectors for batch input
- Verified all 3 memory kinds queryable; new id 1460 (semantic) becomes top-2 hit for "DAN-4 v115" on first query
- Bumped scratchpad to v115; no service code changes

## Files (DAN-4 surface)

- Services/memoryd/{memoryd.py, SPEC.md, test_memoryd.py, test_wizard_roundtrip.py}
- Services/toold/{toold.py, SPEC.md, test_toold.py}
- Services/ttsd/{ttsd.py, SPEC.md, test_ttsd.py}
- apps/dan-glasses-app/src/components/BootstrapWizard.{tsx,css}
- agent-work/dan4.md (this file)

## Commits (DAN-4 only)

- 7d729c0 — memoryd+toold+ttsd wiring, wizard device probe, full e2e green (v112)
- 8d64467 — harden test reads + 5/5 e2e, 118 tests green (v113)
- 915f73e — update scratchpad to v113 status
- (v114) rewrite SPEC.md to match shipped code
- (v115) re-verification: 92/92 tests, 5/5 services, fresh e2e evidence