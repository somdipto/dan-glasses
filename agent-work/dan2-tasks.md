# DAN-2 Sprint Tasks

## P0 — Get DanClaw Live on Railway

### Railway Auth (NEEDS SOM INPUT)
- [ ] Som: Go to railway.app → connect GitHub repo `somdipto/paperclip`
- [ ] Som: Add GitHub secrets `RAILWAY_TOKEN` + `RAILWAY_SERVICE_ID`
- [ ] Verify `RAILWAY_TOKEN` and `RAILWAY_SERVICE_ID` in GitHub secrets
- [ ] GitHub Actions auto-deploy on master push OR manual `railway up`

### Post-Deploy Verification
- [ ] UI loads at root URL
- [ ] `/api/health` returns 200
- [ ] No startup errors in Railway logs

### Alternative (no Railway creds needed)
- [ ] GHCR package: `ghcr.io/somdipto/paperclip:latest` auto-built by docker.yml on master push
- [ ] Run with Docker directly (see dan2.md for command)

## P1 — Fix Rebrand References ✅ DONE

### CLI Name Hardcoding ✅
- [x] `cli/src/index.ts` → `paperclipai` → `danclaw`
- [x] `cli/src/client/command-label.ts` → return `danclaw`
- [x] `cli/src/checks/config-check.ts` → fix hints
- [x] `cli/src/commands/onboard.ts` → fix CLI name in prompts
- [x] `cli/src/commands/run.ts` → fix hints
- [x] `cli/src/commands/configure.ts` → fix hints
- [x] `cli/src/commands/client/auth.ts` → fix command refs
- [x] `cli/src/commands/doctor.ts` → fix hints
- [x] `cli/src/prompts/storage.ts` → was already danclaw

### UI Strings ✅
- [x] `ui/src/App.tsx` → `pnpm paperclipai` → `pnpm danclaw`
- [x] `ui/src/pages/CliAuth.tsx` → `paperclipai cli` → `danclaw cli`
- [x] `ui/src/pages/CompanyExport.tsx` → `pnpm paperclipai` → `pnpm danclaw`
- [x] `ui/src/pages/CompanySettings.tsx` → `pnpm paperclipai` → `pnpm danclaw`

### Server Strings ✅
- [x] `server/src/startup-banner.ts` → `pnpm paperclipai onboard` → `pnpm danclaw onboard`
- [x] `server/src/routes/access.ts` → fix all `paperclipai` refs
- [x] `server/src/middleware/private-hostname-guard.ts` → fix `paperclipai` refs
- [x] `server/src/services/board-auth.ts` → fix `paperclipai cli` label

### README / Docs ✅
- [x] `RAILWAY.md` → `paperclip.danlab.dev` → `danclaw.danlab.dev`
- [x] `DEPLOY.md` → domain + repo refs fixed

### Remaining (non-blocking, internal use)
- `docs/` folder: many `paperclipai` refs (user-facing docs need full update)
- `.agents/skills/` and `skills/`: reference original Paperclip ecosystem
- Test files: reference `paperclipai` (intentional - test original behavior)

## P2 — Polish

### Startup Banner Art
- [ ] Replace ASCII "PAPERCLIP" banner with "DANCLAW"
- [ ] Keep cyan color scheme

### Favicon / Branding
- [ ] DanClaw-specific SVG favicon (current uses Paperclip SVG)

## Notes
- ✅ Build passes after all rebrand changes
- ✅ Committed and pushed: abc66ac5 (rebrand), 88ad461b (docs fix)
- Railway deploy needs Som to set up Railway app + GitHub secrets