# Task: e1-contracts — Shared Contract Generation (E1-S2)

## Objective
Make FastAPI's OpenAPI output the source of truth for cross-stack contracts and generate TypeScript types into `packages/contracts` with a repeatable, drift-checked pipeline.

## Scope
- Seed a first domain contract (health DTO + `ProjectStatus` enum from the technical spec).
- Generate TS types from FastAPI OpenAPI via `openapi-typescript` into `packages/contracts`.
- Thin `packages/api-client` fetch helper typed against generated contracts.
- Contract regeneration script with drift check (`git diff --exit-code`).

## Source References
- MVP Technical Spec: Shared Contracts, Projects (state list).
- Implementation Plan: Grooming Round 4, Round 5.
- Backlog: E1-S2, E8-S3.

## Acceptance Criteria
- FastAPI OpenAPI transforms into TypeScript types.
- Shared enums and DTOs live in `packages/contracts`.
- Generation step is repeatable and documented.
- Drift check fails when generated types are stale.

## Dependencies
- e1-initial-scaffold.

## Status
`done`

## Delivery
- PR: https://github.com/SuyashEkhande/ugc/pull/4
- Merged: 2026-08-06
- Commits: `396bc41`

## Skept Notes
- Implementation matches the plan. FastAPI OpenAPI is the source of truth; `openapi-typescript` generates `packages/contracts/src/openapi.d.ts`; `contracts:check` gates drift.
- Drift 1 (justified): the seed contract is `HealthResponse` + `ProjectStatus`/`ProjectSummary`/`ProjectListResponse`, surfaced via a minimal `GET /projects` scaffold endpoint (backlog API surface lists `GET /projects`). No real persistence yet — the endpoint returns an empty list.
- Drift 2 (justified): export runs offline via `scripts/export_openapi.py` (imports the app and dumps `app.openapi()`), not by booting a live server. Faster and deterministic for CI.
- Note: `openapi.d.ts` may show a CRLF/LF warning under `core.autocrlf`; harmless — stored as LF, normalized on checkout.
