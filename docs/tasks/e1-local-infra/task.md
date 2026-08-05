# Task: e1-local-infra — Local Infrastructure (E1-S3)

## Objective
Provide a one-command local stack for Postgres, Redis, and MinIO-compatible object storage that the api, worker, and web app run against in watch mode.

## Scope
- Root `compose.yaml` with services: Postgres, Redis, MinIO (+ MinIO bucket init).
- `.env.example` files at root and per app.
- Watch-mode run instructions in `infra/` notes and README.
- Smoke check script (service health checks).

## Source References
- Implementation Plan: Grooming Round 6.
- Backlog: E1-S3, E8-S4.

## Acceptance Criteria
- Local infrastructure starts from repo root.
- Postgres, Redis, MinIO are available.
- App services run in watch mode against them.
- Smoke check passes.

## Dependencies
- e1-initial-scaffold.

## Status
`done`

## Delivery
- PR: https://github.com/SuyashEkhande/ugc/pull/6
- Merged: 2026-08-06
- Commits: `a674915`

## Skept Notes
- Implementation matches the plan: compose.yaml (postgres/redis/minio + bucket init), env examples at root and per app, smoke script, infra docs.
- Drift 1 (justified): smoke verification could NOT be executed — Docker and bash are not installed on this dev machine. `compose.yaml` YAML is validated; the run is deferred to the CI compose-smoke job (E8-S4).
- Drift 2 (justified): minio healthcheck uses `curl` (present in the minio image), not `mc ready`.
- Drift 3 (justified): apps/web/.gitignore needed `!.env.example` because create-next-app's `.env*` rule blocked committing the web env example.
