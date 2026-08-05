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
`planned`

## Delivery
- PR: _link_
- Merged: _date_
- Commits: _range or hashes_

## Skept Notes
_To be filled at close-out._
