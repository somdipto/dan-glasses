# DAN-2 Scratch Pad

## Context
- Repo: `/home/workspace/paperclip` (fork of paperclipai/paperclip)
- Already rebranded to DanClaw/DanBuddy
- Git remote: `https://somdipto:***@github.com/somdipto/paperclip.git`
- Railway.toml + railway.yaml exist, Railway CLI installed but not authenticated

## What's Done
- ✅ Build passes (`pnpm build` completes)
- ✅ Full paperclipai -> danclaw rebrand (40 files, CLI name, UI strings, server hints)
- ✅ Railway domain refs fixed (danclaw.danlab.dev)
- ✅ Docker compose uses danclaw properly
- ✅ GitHub push triggered (commits abc66ac5, 88ad461b)

## Railway Deployment Status

### What's blocking Railway deploy
1. **No Railway CLI auth** - Can't run `railway login` in this env
2. **No GitHub secrets** - `RAILWAY_TOKEN` and `RAILWAY_SERVICE_ID` not set in GitHub

### What's needed from Som
1. Go to railway.app → connect GitHub repo `somdipto/paperclip`
2. Add GitHub secrets: `RAILWAY_TOKEN`, `RAILWAY_SERVICE_ID`
3. Or: enable Railway GitHub integration (auto-deploys on push)

### Alternative: Docker deploy (no Railway creds needed)
```bash
# GHCR package already built by docker.yml workflow on master push
docker run -d \
  --name danclaw \
  -p 3100:3100 \
  -e DATABASE_URL="postgres://user:pass@host:5432/db" \
  -e BETTER_AUTH_SECRET="$(openssl rand -hex 32)" \
  ghcr.io/somdipto/paperclip:latest
```

## Remaining rebrand items (non-blocking)
- `docs/` folder has many `paperclipai` refs (internal use only,不影响部署)
- `.agents/skills/` and `skills/` reference original Paperclip (intended - these are for the Paperclip ecosystem)
- Test files reference `paperclipai` (tests for original Paperclip behavior)

## Priority
1. Get Railway deployed (P0) — Som needs a live URL
2. Ship and iterate
