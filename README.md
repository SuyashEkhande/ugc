# AI Creative Studio

Guided AI workflow that turns brand context into approved UGC-style marketing videos.

## Monorepo Layout

| Path | What |
| --- | --- |
| `apps/web` | Next.js frontend (guided workflow UX) |
| `apps/api` | FastAPI backend (workflow state, validation, persistence, orchestration) |
| `apps/worker` | Celery worker (async research, generation, publish jobs) |
| `packages/contracts` | Generated OpenAPI-derived TypeScript types and enums |
| `packages/api-client` | Typed, auth-aware fetch helpers for the frontend |
| `infra` | Local infrastructure: `compose.yaml`, env examples |
| `docs` | Canonical documentation root (specs, plan, task docs) |

## Prerequisites

- Node.js 20+
- uv (Python package manager)
- Docker (only for local infrastructure, not required for app dev)

## Quick Start

### Shared JS packages

```sh
npm install          # installs all workspace packages
npm run dev:web      # Next.js dev server
```

### Backend

```sh
cd apps/api
uv sync
uv run uvicorn app.main:app --reload
# health check: GET http://localhost:8000/health
```

### Worker

```sh
cd apps/worker
uv sync
uv run celery -A worker_app.celery:celery_app worker --loglevel=info
```

### Local infrastructure (Postgres, Redis, MinIO)

See `docs/tasks/e1-local-infra/task.md` and `infra/` for the compose setup.

## Documentation

Start at [`docs/index.md`](docs/index.md). Task plans live in `docs/tasks/<task-id>/`.

## Quality Gates

Run the same checks CI runs before opening a PR:

```sh
# backend (apps/api, apps/worker)
uv run ruff check . && uv run ruff format --check .
uv run mypy app scripts
uv run pytest

# frontend
npm run lint:web
npm run build:web

# contracts (regenerates OpenAPI types and fails on drift)
npm run contracts:check
```

CI (`.github/workflows/ci.yml`) blocks merges on: backend lint/typecheck/tests, frontend lint/build, and contract drift. A nightly `compose-smoke` job boots the local stack.

## Governance

- Trunk-based development on short-lived branches; one PR per task.
- Use the `gh` CLI for all GitHub activity.
- Task lifecycle and decision records live in `docs/` (see [AGENTS.md](AGENTS.md)).
