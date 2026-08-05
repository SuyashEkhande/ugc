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
`planned`

## Delivery
- PR: _link_
- Merged: _date_
- Commits: _range or hashes_

## Skept Notes
_To be filled at close-out._
