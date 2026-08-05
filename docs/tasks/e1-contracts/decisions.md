# Decisions — e1-contracts

## 2026-08-06 — Contract export runs offline, not against a live server

- **Context:** The generation pipeline needs FastAPI's OpenAPI JSON without manual steps.
- **Options considered:** boot uvicorn and curl `/openapi.json`; import the app and dump `app.openapi()` directly.
- **Chosen option:** offline export via `apps/api/scripts/export_openapi.py`.
- **Reason:** deterministic, fast, no port/process management, and works the same in CI as locally.

## 2026-08-06 — Raw OpenAPI JSON is committed alongside generated types

- **Context:** `contracts:check` must detect drift by diffing regenerated output.
- **Options considered:** fetch at CI time only; commit both the raw `openapi.json` and generated `openapi.d.ts`.
- **Chosen option:** commit `packages/contracts/openapi.json` and `openapi.d.ts`.
- **Reason:** `git diff` needs a committed baseline; committing both makes drift visible and reviewable in PRs.

## 2026-08-06 — Seed contract is project state

- **Context:** The pipeline needs at least one real domain contract to prove end-to-end generation.
- **Options considered:** only `HealthResponse`; `HealthResponse` + `ProjectStatus`/`ProjectSummary`.
- **Chosen option:** `ProjectStatus` (all 10 states from the tech spec) with `ProjectSummary` and `ProjectListResponse`.
- **Reason:** project state is the highest-leverage contract — E3-S2 builds the state machine directly against these generated types.
