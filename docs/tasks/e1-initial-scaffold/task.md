# Task: e1-initial-scaffold — Monorepo Scaffold (E1-S1)

## Objective
Create the monorepo layout and minimal, bootable app shells for the frontend, backend, worker, and shared packages that every other epic builds on.

## Scope
- Repo layout: `apps/web`, `apps/api`, `apps/worker`, `packages/contracts`, `packages/api-client`, `infra`, `docs`.
- Root workspace config (npm workspaces) and root scripts.
- Minimal Next.js app, FastAPI app, and Celery worker that boot.
- Root `README.md` and root `.gitignore`.
- No feature logic, no real endpoints beyond health.

## Source References
- Implementation Plan: Phase 1, Grooming Round 2 (Codebase Shape).
- Backlog: E1-S1.

## Acceptance Criteria
- Repo contains `apps/web`, `apps/api`, `apps/worker`, `packages/contracts`, `packages/api-client`, `infra`, and `docs`.
- Folder layout matches repo governance guidance.
- Web, api, and worker each boot locally.
- Structure is documented for contributors.

## Dependencies
- Task 0 (hygiene), Task 1 (docs framework).

## Status
`done`

## Delivery
- PR: https://github.com/SuyashEkhande/ugc/pull/2
- Merged: 2026-08-06
- Commits: `4cb1254`

## Skept Notes
- Implementation matches the plan. Repo layout per Grooming Round 2: `apps/web`, `apps/api`, `apps/worker`, `packages/contracts`, `packages/api-client`, `infra`, `docs`.
- Drift 1 (justified): package manager is **npm workspaces**, not pnpm — pnpm not installed on the dev machine, npm is native and sufficient for 2 apps + 2 packages. Recorded in `decisions.md`.
- Drift 2 (justified): `create-next-app` failed on a missing parent dir, retried after creating `apps/`; generated Next 16.3 + Tailwind v4 defaults kept.
- Drift 3 (justified): compose.yaml deferred to e1-local-infra by design; `infra/` holds a placeholder README only.
