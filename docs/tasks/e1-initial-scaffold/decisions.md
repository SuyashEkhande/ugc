# Decisions — e1-initial-scaffold

## 2026-08-06 — JS/TS monorepo tooling

- **Context:** The monorepo needs a workspace manager for `apps/*` and `packages/*`. The implementation plan leaves the choice open.
- **Options considered:** pnpm workspaces; npm workspaces; Turborepo on top of either.
- **Chosen option:** npm workspaces, no task runner.
- **Reason:** npm is already installed (node 24); pnpm is not. npm workspaces cover two apps and two packages with zero new tooling. Turborepo is YAGNI until build/script orchestration actually repeats.

## 2026-08-06 — Python env and project tooling

- **Context:** The api and worker are separate Python packages in the monorepo.
- **Options considered:** uv; poetry; pip + venv.
- **Chosen option:** uv with per-app `pyproject.toml`.
- **Reason:** uv is installed and fast; keeps each Python app a self-contained package; matches the repo default of running app services locally in watch mode.

## 2026-08-06 — Shared code must not import across app boundaries

- **Context:** `apps/web` (TS) and `apps/api`/`apps/worker` (Python) cannot share code directly.
- **Options considered:** hand-authoring duplicated types; generating TS from the API's OpenAPI output.
- **Chosen option:** FastAPI OpenAPI is the contract source of truth; TS types are generated into `packages/contracts`.
- **Reason:** Matches the locked decision in Grooming Round 4/5 and removes the drift risk of hand-maintained duplicates.
