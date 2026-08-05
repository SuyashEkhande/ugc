# Decisions — e1-governance

## 2026-08-06 — CI jobs share api + worker, not one job per app

- **Context:** Grooming Round 7 lists per-app jobs, but the api and worker use the same toolchain (uv, ruff, mypy).
- **Options considered:** separate jobs per app; shared jobs per tool covering both apps.
- **Chosen option:** shared jobs (`api-lint`, `api-typecheck`) that run the tool against both `apps/api` and `apps/worker`.
- **Reason:** identical toolchain and identical gates — splitting costs runner time without adding signal. Tests stay a dedicated `api-test` job because pytest only exists in the api for now.

## 2026-08-06 — Compose smoke runs nightly + manual, not on PRs

- **Context:** compose-smoke boots Docker services and takes minutes; PR checks should stay fast.
- **Options considered:** run on every PR; run on a schedule and manual dispatch.
- **Chosen option:** schedule (`0 3 * * *`) + `workflow_dispatch` only.
- **Reason:** matches impl-plan Round 7 ("nightly smoke test for extra confidence") while keeping the PR loop fast. The same script runs anywhere Docker exists.

## 2026-08-06 — Branch protection is a repo setting, tracked here

- **Context:** "protected main" cannot be expressed as a repo file.
- **Options considered:** ignore it; document it as a required follow-up.
- **Chosen option:** documented in this task's skept notes as an outstanding owner action.
- **Reason:** keeping it visible in the task record (not silently dropped) so the owner enables required checks + review on `main`.
