# Repository Agent Instructions

## Mission
This repository is building the MVP for AI Creative Studio: a guided AI workflow that turns brand context into approved UGC-style marketing videos.

## Current MVP Scope
- Brand Brain onboarding and persistence
- Project creation and guided creative interview
- Automated research
- Creative plan review and approval
- Generation using a swappable video model provider behind a backend adapter
- Direct publishing or export/download
- Billing and credits

## Explicit Non-Goals
Do not introduce:
- Campaign management
- Performance analytics
- Budget management
- CRM
- Email marketing
- Team collaboration
- Agency workspaces
- Marketing automation
- AI optimization loops
- A/B testing dashboards
- Content calendars
- Multi-platform scheduling
- Autonomous marketing workflows

## Architecture Rules
- Use Next.js for the frontend experience.
- Use FastAPI for backend business logic, state, validation, persistence, and job orchestration.
- Route all video model calls through backend provider adapters.
- Keep the backend as the source of truth for workflow state.
- Keep shared request/response contracts explicit and versioned.

## Workflow Rules
- Strategy comes before generation.
- The creative plan must be visible before generation begins.
- Human approval is required before expensive generation steps.
- Publishing must use finalized assets only.
- Credits must be checked before expensive operations.
- Inspiration analysis must be framed as extract-and-adapt, not clone-and-copy.

## Development Practices
- Build thin vertical slices before broadening features.
- Prefer explicit workflow states over hidden UI assumptions.
- Keep UI screens focused on one major action at a time.
- Preserve state across refresh and navigation.
- Keep generated and source assets traceable through metadata.

## Repository Defaults
- Use a monorepo.
- Keep `apps/web` as the Next.js frontend, `apps/api` as the FastAPI backend, and `apps/worker` as the Celery worker.
- Keep `packages/contracts` for generated OpenAPI-derived types and enums.
- Keep `packages/api-client` for frontend request helpers and auth-aware transport.
- Use SQLAlchemy 2.0, Alembic, and Pydantic v2 on the backend.
- Use a root `compose.yaml` for local infrastructure, with Postgres, Redis, and MinIO in Docker.
- Run the app services locally in watch mode unless a task explicitly needs container parity.
- Use GitHub Actions for CI with lint, type check, tests, contract drift checks, migrations validation, and smoke tests.
- Use Ruff, Pytest, MyPy, ESLint, Prettier, and Playwright as the default quality stack.
- Add CODEOWNERS for backend, frontend, and infra paths.
- Keep trunk-based development with protected main and short-lived branches.

## Workflow Defaults
- Keep orchestration inside FastAPI as a deterministic workflow engine.
- Use a simple ReAct-style LLM harness only for narrow step-level tasks.
- Run research and creative planning as async jobs with visible progress.
- Use plain enums and module-local transition helpers for workflow state.
- Keep repositories explicit and separate per module only where the persistence logic justifies them.

## Testing Expectations
- Add focused tests whenever a workflow state, contract, or provider boundary changes.
- Validate approval gating before generation.
- Validate credit checks before costly jobs run.
- Validate that publish/export only sees finalized assets.

## Documentation Expectations
- Treat `docs/` as the canonical documentation root.
- Keep the consolidated source docs in `docs/prd.md` and `docs/ux-spec.md`.
- Keep the working technical artifacts in `docs/mvp-technical-spec.md` and `docs/implementation-plan.md`.
- Update docs/mvp-technical-spec.md when product scope or data flow changes.
- Update docs/implementation-plan.md when sequencing or ownership changes.
- Keep architectural decisions in sync with the implementation.

## Technical Decision Culture
- Every technical decision made during development must be recorded in the Decision Log section of `docs/implementation-plan.md`.
- Decisions include technology choices, architectural trade-offs, deferred scope, and provider selections.
- Each decision entry must include the context, the options considered, the chosen option, and the reason.
- Do not overwrite previous decisions. Append new entries or mark superseded decisions with a date and reason.
- When a decision contradicts an earlier one, reference the original and explain what changed.
- Treat the Decision Log as the canonical record of why the codebase looks the way it does.

## Feature Development Lifecycle
- Every feature must begin with a written spec or plan before implementation starts.
- The spec must reference the relevant PRD, UX, and technical spec sections.
- After implementation and testing, the feature must be reviewed and skepted against the original spec and plan.
- Skepting means explicitly checking: does the implementation match what was planned? What drifted? Was the drift justified?
- If the implementation diverges from the plan, the divergence must be documented and the plan updated.
- Do not consider a feature done until the skept pass is complete.

## Common Repo Mistakes
- Track recurring development mistakes and anti-patterns in `docs/common-repo-mistakes.md`.
- Update that file whenever a pattern of mistakes is observed during reviews or retrospectives.
- Use it as a living checklist that developers review before submitting changes.

## Task Lifecycle
- Every task gets a folder `docs/tasks/<task-id>/` with a `task.md` plan written before any code.
- `task.md` follows the template in `docs/tasks/_template/task.md`: objective, scope, source references, acceptance criteria, dependencies, status, delivery (PR link + date), skept notes.
- Track status in `task.md`: `planned` / `in-progress` / `done` / `blocked`.
- Record technical and architecture decisions made during a task in `docs/tasks/<task-id>/decisions.md`, and roll significant ones up into the Decision Log in `docs/implementation-plan.md` (append, never overwrite).
- Keep architecture diagrams for the task in `docs/tasks/<task-id>/architecture.md` using Mermaid.
- When closing a task, flip status to `done`, add the merged PR link and date, and fill the skept notes: does the implementation match the plan, what drifted, was the drift justified.
- Do not mark a task done until its PR is merged and the skept pass is complete.

## GitHub Workflow
- Use the GitHub CLI (`gh`) for all GitHub activity: creating branches, PRs (`gh pr create`), merging (`gh pr merge`), issues, and browsing. Do not bypass it with raw push + manual PR creation.
- Work on short-lived branches off `main` and open one PR per task.
- A task is only `done` after its PR is merged.

## Developer Harness & Token Efficiency
- Developers working with AI CLI tools (Claude Code, Cursor, Aider) should install context compression tools such as **RTK** (`rtk-ai/rtk`) or **Headroom** (`headroomlabs-ai/headroom`).
- `rtk` (Rust Token Killer) compresses shell output (git status, test logs, linter outputs) by 60–90% before it hits the LLM context window.
- Wrap long terminal outputs with `rtk` (e.g. `rtk pytest`, `rtk git status`, `rtk npx tsc`) to optimize token usage across developer sessions.

## Safety and Quality Notes
- Avoid copyright-risky language such as clone, copy, or recreate an existing creator’s work.
- Use consistent terminology: Brand Brain, Creative Vault, Creative Plan, Generation, Publishing.
- Keep the product positioned as an AI Creative Studio, not a generic AI video generator.
