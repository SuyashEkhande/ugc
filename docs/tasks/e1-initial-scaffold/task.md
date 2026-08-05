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
`planned`

## Delivery
- PR: _link_
- Merged: _date_
- Commits: _range or hashes_

## Skept Notes
_To be filled at close-out._
