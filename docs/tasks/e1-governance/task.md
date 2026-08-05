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
`planned`

## Delivery
- PR: _link_
- Merged: _date_
- Commits: _range or hashes_

## Skept Notes
_To be filled at close-out._
