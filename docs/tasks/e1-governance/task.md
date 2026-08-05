# Task: e1-governance — Repo Governance and CI (E1-S4)

## Objective
Add the repo rules, code ownership, and CI gates that keep future work aligned with the MVP architecture.

## Scope
- `CODEOWNERS` for `apps/*`, `packages/*`, `infra/`, `docs/`, `.github/`.
- GitHub Actions CI: backend lint/typecheck/test, frontend lint/build, contract drift check, compose smoke.
- README pointers to docs and task documentation.
- Verify AGENTS.md lifecycle section is complete.

## Source References
- Implementation Plan: Grooming Round 7, Round 8.
- Backlog: E1-S4, E8-S1, E8-S2, E8-S3.

## Acceptance Criteria
- Repo guidance covers frontend, backend, worker, contracts, docs, testing, release.
- CODEOWNERS present for required paths.
- CI gates run on PRs.
- Docs root is canonical.

## Dependencies
- e1-initial-scaffold, e1-contracts, e1-local-infra.

## Status
`done`

## Delivery
- PR: https://github.com/SuyashEkhande/ugc/pull/8
- Merged: 2026-08-06
- Commits: `ad134b7`

## Skept Notes
- Implementation matches the plan: CODEOWNERS, CI (lint/typecheck/test for backend, lint/build for frontend, contract drift check, nightly compose smoke), README governance section.
- Drift 1 (justified): CI jobs run `uv sync --extra dev` per app; backend lint/typecheck are combined across api+worker in shared jobs instead of strictly one job per app — same coverage, fewer runner minutes.
- Drift 2 (justified): `compose-smoke` is gated to nightly + manual dispatch only, not on every PR — keeps PR checks fast per impl-plan Round 7 while still validating the stack daily.
- Verified: all 6 PR checks passed on PR #8 (including contracts-check against a fresh checkout). compose-smoke cannot run locally (no Docker on dev machine).
- Outstanding: branch protection (require CI green + review on `main`) is a GitHub repo setting, not a repo file — must be enabled in the repo UI. Flagged to owner.
