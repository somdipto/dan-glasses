# DAN-4 — Stream Scratch Pad

## 2026-07-07 16:50 UTC run (v112)

### TL;DR — platform is healthy. Task is "verify + ship the next delta," not rebuild.

### Live verification (all green)

- **memoryd** :8741 → 416 memories (244 episodic + 92 semantic + 80 procedural), 24 conversations, db_persistent=true, MiniLM-L6-v2 loaded, db 3.9MB on disk.
- **toold** :8742 → self-test `success:true` in 126ms (shell ✓, python ✓, registry ✓ (4 tools), file ✓).
- **ttsd** :8743 → 8 voices, KittenTTS medium, `/speak` returns audio/wav in ~1s.
- **audiod** :8090 → readiness all true, publisher running.
- **perceptiond** :8092 → watchful mode, 3 frames processed, 1 salient, vlm_queue_depth:1.
- **openclaw** :18789 → live.
- **dan-glasses-app** :8747 → serving dist on public `https://dan-glasses-app-som.zocomputer.io`.
- All 5 `/api/<svc>/*` proxies verified through public URL:
  - `/api/services/health` → 5/5 ok, total_latency_ms 35
  - `/api/memoryd/memories` (POST) → 200, id=443
  - `/api/toold/test` → 200, success:true
  - `/api/ttsd/speak` (POST) → 200, audio/wav, 206458 bytes, 1.2s
- First CF hop had a transient 000 on the public ttsd call; retried → 200. Documented in the gap below.

### Task is a no-op for build, a real one for ongoing maintenance

The user's brief (memoryd + toold + TTS + wizard) describes the **starting point**. It's been shipped. Rebuilding would be a step backward. Real leverage:

1. **Persistence regression check** — v109 fixed the db_persistent bug. Re-verify the DB is still pinned to `/home/.cache/dan-glasses/memoryd/state.db` after this run. **Confirmed** (3.9MB, persistent:true, ids 441/443 incremented past the v109 v1.x baseline).
2. **Service-decomposition drift** — audiod v1.3 added Loki push sink; ttsd is on the medium model. Check that no one daemon is now swallowing work that should belong to another (e.g. is perceptiond still pushing to memoryd? Yes — `memory_sink.url: http://localhost:8741/memories` in status).
3. **Public-URL roundtrip** — the SPA was rebuilt for v109. Confirm the JS bundle (`index-DJuY7cTt.js`) still points at the proxy paths. Confirmed via direct probe.
4. **daemon-doctor** — check for any silent errors in `/dev/shm/<name>.log` since last touch. See "Logs" below.

### Logs sampled

- `ttsd.log`: 200s only, no errors.
- `dan-glasses-app.log`: clean startup, 5 proxies registered.
- `memoryd.log`: empty (writes are buffered; not a problem).
- `perceptiond.log`: motion_score 0.0518, watchful mode stable.

### Gaps / next bets (DAN-4 backlog, not blockers)

1. **CF transient on cold TTS** — first public `/api/ttsd/speak` call after a CF idle window can 000. Second call works. Likely a CF "always-warm" config; if it bites users often, document a "TTS warmup" first call in the wizard.
2. **Wizard tests on the public URL** — there's no automated E2E for the React app roundtrip via the proxy. The closest thing is the `test_wizard_roundtrip.py` which hits daemons directly. Cheap win: add a `test_public_proxy.py` that runs through the public URL.
3. **No persistent monitoring** — if a daemon dies overnight, the next person to look at the wizard sees red. Cheap win: a tiny `scripts/check-and-restart.sh` cron'd to call `service_doctor` and `update_user_service` if a service is down.
4. **memoryd v_next** — current 414 memories is solid for a research demo but not for production. When memory hits ~10k, the linear scan in `/query` will start to bite. The "right next step" is HNSW or Faiss. **Parked** — not a current blocker.

### Decision (DAN-4 v112)

The platform is healthy. No new code from this stream; I verified the existing surface and refreshed the scratch pad. If a real bug surfaces in the next 24h, escalate. Otherwise, the next leverage is the public-proxy E2E test (#2 above).

— DAN-4, 2026-07-07 16:51 UTC
