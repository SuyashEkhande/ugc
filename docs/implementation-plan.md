# MVP Implementation Plan

## Objective
Build the fastest demoable vertical slice of AI Creative Studio using:
- Next.js for the frontend
- FastAPI for the backend
- A swappable video generation provider behind a backend adapter

The plan should deliver the full guided workflow end to end while keeping scope strictly MVP.

## Delivery Strategy
The product should ship as one coherent workflow:
Brand Brain -> Project -> Interview -> Research -> Creative Plan -> Approval -> Generation -> Publish/Download

The implementation should avoid broad platform work until the first vertical slice is working.

## Phase 1: Foundation
### Goals
- Create the repo structure for frontend and backend
- Define shared contracts and workflow states
- Establish database and storage conventions
- Add development tooling and repo rules

### Backend Positioning
- Keep FastAPI as the primary backend source of truth
- Keep the backend as the source of truth for workflow state, validation, and orchestration

### Deliverables
- Next.js app scaffold
- FastAPI app scaffold
- Shared DTO/state definitions
- Database schema draft
- AGENTS.md file
- Spec docs in docs/

### Exit Criteria
- Frontend and backend can run locally
- Shared domain concepts are agreed and documented
- The MVP scope is frozen enough to build against

## Phase 2: Brand Brain and Auth
### Goals
- Implement authentication
- Implement Brand Brain persistence
- Capture the minimum brand context needed for generation

### Deliverables
- Login/session flow
- Brand creation and edit screens
- Brand API endpoints
- Database tables for brand, product, audience, assets, and competitors

### Exit Criteria
- A user can create and update Brand Brain data
- Brand Brain data persists across sessions
- The app can block generation until required fields exist

## Phase 3: Project Workflow
### Goals
- Implement project creation and state transitions
- Build the project detail shell
- Add the guided interview flow

### Deliverables
- Project list and detail pages
- Project state machine in backend
- Interview question flow with adaptive branching
- Structured brief persistence

### Exit Criteria
- A user can create a project and complete the interview
- The brief is saved and can be reopened after refresh

## Phase 4: Research and Creative Plan
### Goals
- Automate research from approved sources
- Generate a reviewable creative plan
- Create trust-building UI around the plan

### Deliverables
- Research service and output schema
- Creative plan generation endpoint
- Creative plan review UI
- Confidence score and explanation fields

### Exit Criteria
- The user can run research and see actionable findings
- The creative plan is usable as a pre-generation approval surface

## Phase 5: Generation
### Goals
- Integrate the chosen video generation provider behind backend provider adapters
- Generate scripts, storyboards, reference frames, and final videos
- Track generation jobs and credit usage

### Deliverables
- Video provider adapter
- Generation job execution flow
- Asset storage and metadata handling
- Credit deduction logic

### Exit Criteria
- A user can approve a plan and generate video outputs
- The system records job state, outputs, and credit consumption

## Phase 6: Publishing and Export
### Goals
- Enable direct publish to supported platforms
- Provide download/export fallback
- Record publish history

### Deliverables
- Publish job flow
- Platform-specific publish integrations or stubs
- Export/download UI
- Publish state and history tracking

### Exit Criteria
- A user can publish or export final assets from the project view
- Publish state is visible and persisted

## Phase 7: Billing and Credits
### Goals
- Add credit balance visibility
- Add low-credit warnings and block states
- Add entitlement and usage rules

### Deliverables
- Credit ledger
- Balance UI
- Usage checks before expensive operations
- Low-credit notifications

### Exit Criteria
- The system prevents generation when credits are insufficient
- The user can understand remaining usage at a glance

## Parallel Workstreams
1. Frontend UI and backend API can be scaffolded in parallel after the domain contract is agreed.
2. Database modeling and provider adapter design can proceed alongside the interview/research UI.
3. Generation, publishing, and credit ledger logic can be developed after the project workflow is stable.

## Recommended Build Order
1. Define shared contracts and DB schema.
2. Build Brand Brain and authentication.
3. Build project creation and interview.
4. Build research and creative plan.
5. Add the selected video generation provider behind a backend adapter.
6. Add publish/export.
7. Add billing and credits.
8. Tighten acceptance tests and workflow validation.

## Deployment Note
- Keep deployment choices separate from backend ownership decisions.
- The backend should continue to own workflow state, validation, and provider orchestration.

## Grooming Round 1: Orchestration

### Recommended MVP Choice
- Keep orchestration inside FastAPI as a deterministic workflow engine.
- Use explicit backend state transitions in Postgres.
- Use a background worker for long-running jobs.
- Use a simple ReAct-style LLM harness only inside specific steps, not as the workflow engine itself.

Why this is the best fit for MVP:
- The product is a guided workflow with approval gates, not a general autonomous agent.
- The workflow needs predictable states, resumability, and clear ownership of credits, publishing, and generation.
- FastAPI can remain the source of truth while keeping the model layer swappable.

### Best Fit Option
- FastAPI workflow engine + background jobs + provider adapters.
- Use LangChain `create_agent` only for step-level LLM calls such as interview synthesis or plan writing if helpful.
- Do not introduce Deep Agents as the primary orchestration layer for MVP.

### Decision Rule
- If the step is product workflow, put it in FastAPI state and jobs.
- If the step is a narrow LLM task, wrap it with LangChain.
- If we later need durable graph execution and interrupt/resume across branches, evaluate LangGraph.
- If we later need subagents, filesystem tools, and memory-heavy delegation, evaluate Deep Agents.

### Final Decision
- Use a simple state machine with conditional branching for the interview.
- Run research and creative-plan generation as asynchronous jobs with streamed progress in the UI.
- Use separate Celery queues by domain area instead of one shared heavy-task queue.

## Grooming Round 2: Codebase Shape

### Recommended MVP Choice
- Use a monorepo.
- Generate shared contracts from FastAPI's OpenAPI schema into frontend-consumable types.
- Use Celery with Redis for background jobs.

### Proposed Repo Structure
- `apps/web` for the Next.js frontend
- `apps/api` for the FastAPI backend
- `apps/worker` for background jobs
- `packages/contracts` for shared schemas and enums
- `packages/ui` only if frontend components start repeating enough to justify it
- `infra` for Docker, local env, and deployment helpers
- `docs` for the technical spec, plan, and decisions

### Code Ownership Rules
- Frontend owns screens, interaction state, and presentation logic.
- Backend owns workflow state, validation, persistence, credit checks, and provider orchestration.
- Worker owns asynchronous research, generation, publish jobs, retries, and heavy IO.
- Contracts own schema and enum definitions only.

### Why This Is the Best Fit
- A monorepo keeps shared contracts, CI, and local development simpler for a small team.
- OpenAPI is already produced naturally by FastAPI, so generated contracts reduce drift between backend and frontend.
- Celery gives the best maturity for retries, scheduling, routing, monitoring, and long-running tasks that are more durable than FastAPI background tasks.
- Redis is a good MVP broker because it is straightforward to run locally and supports the expected queue workload.

### Implementation Details
- Let FastAPI remain the OpenAPI source of truth.
- Generate TypeScript client/types for the web app from the API schema.
- Keep Pydantic models as the backend validation layer.
- Use Celery tasks only for asynchronous work that should survive request lifecycles.
- Keep small in-process FastAPI background tasks only for trivial post-response cleanup, if needed.

### Final Decision
- Use a monorepo with one API and one worker.
- Generate shared contracts from OpenAPI rather than hand-authoring duplicate schemas.
- Use Celery for the worker queue and retry model.

## Grooming Round 3: Module Ownership

### Backend Modules
- `auth` owns sessions, tokens, user identity, and workspace access.
- `brands` owns Brand Brain data and brand assets.
- `projects` owns project lifecycle, state transitions, and project summaries.
- `interview` owns question flow, branching, and structured brief output.
- `research` owns source collection, summarization, and research artifacts.
- `plans` owns creative plan generation and approval state.
- `generation` owns provider adapters, generation jobs, outputs, and retries.
- `publishing` owns publish jobs, publish history, and export/download state.
- `billing` owns credits, ledger entries, and entitlement checks.
- `assets` owns upload handling, metadata, and durable file references.

### Frontend Modules
- `app shell` owns navigation, layout, and route structure.
- `onboarding` owns first-time setup and Brand Brain capture.
- `projects` owns the list, detail shell, and workflow progression.
- `interview UI` owns the guided question experience.
- `research UI` owns progress, summaries, and source review.
- `plan review` owns creative plan inspection and approval.
- `generation UI` owns job status, variations, and result previews.
- `publishing UI` owns publish/export controls and status.
- `billing UI` owns credits, low-balance states, and usage visibility.

### Code Design Rules
- Each backend module should expose router, service, schema, repository, and task files.
- Keep services free of framework-specific response details.
- Keep routers thin and validation-heavy.
- Keep Celery tasks thin and delegate logic back to services.
- Keep frontend route components thin and push reusable UI into shared components only when repetition appears.

### Next Review Questions
- Do we want SQLAlchemy or SQLModel for the backend data layer?
- Do we want Alembic migrations from day one?
- Should the web app share a dedicated API client package, or just use generated hooks/types directly in the app?

## Grooming Round 4: Data Layer and Contracts

### Recommended MVP Choice
- Use SQLAlchemy 2.0 as the backend ORM and query layer.
- Use Alembic from day one for migrations.
- Use Pydantic v2 for API schemas and validation.
- Generate frontend-friendly TypeScript types from FastAPI's OpenAPI output.

### Why This Is the Best Fit
- SQLAlchemy 2.0 is the most flexible and production-proven choice for a modular monolith that will likely grow in schema complexity.
- Alembic gives us explicit, reviewable migrations from the start, which matters once credits, jobs, and workflow state become core product data.
- SQLModel is convenient, but it collapses ORM and schema concerns in a way that is less flexible for a system with clear backend/frontend boundaries and evolving domain models.
- OpenAPI-generated types reduce drift without forcing the frontend to depend on backend implementation details.

### Contract Strategy
- Keep Pydantic models as the canonical request/response shapes in FastAPI.
- Generate OpenAPI from FastAPI.
- Use `openapi-typescript` for frontend types.
- Keep a thin frontend API client layer in a shared package or small app-local module, whichever stays simpler after the first slice.

### Module Pattern
- Backend modules should usually contain `models.py`, `schemas.py`, `service.py`, `routes.py`, `repository.py`, and `tasks.py`.
- Use `models.py` for SQLAlchemy tables and relationships.
- Use `schemas.py` for Pydantic request/response DTOs.
- Keep repository functions focused on query and persistence logic only.
- Keep service functions focused on business rules and orchestration.

### Final Decision
- Use SQLAlchemy 2.0 for persistence and query logic.
- Use Alembic from day one.
- Use Pydantic v2 for API schemas and validation.
- Keep the frontend contract generation path centered on OpenAPI.

## Grooming Round 5: API Client and Workflow State

### Recommended MVP Choice
- Put the shared frontend API client in `packages/api-client`.
- Keep `packages/contracts` for generated types and enums.
- Use repositories only where persistence logic is nontrivial, not as a mandatory layer in every module.
- Model workflow state with plain enums plus a small backend transition helper.

### Why This Is the Best Fit
- A dedicated API client package keeps the Next.js app clean and gives us one place for auth-aware fetch logic and error normalization.
- `packages/contracts` stays focused on types and schemas, while `packages/api-client` handles transport concerns.
- A repository layer everywhere adds boilerplate faster than it adds value for this MVP.
- Plain enums plus explicit transition helpers keep workflow rules understandable and easy to test without introducing another abstraction.

### More Options
1. Keep the API client local to `apps/web`.
	- Best for absolute simplicity.
	- Fine if the web app is the only consumer.
	- Less reusable once tests or other tooling need the same request layer.

2. Make repositories mandatory everywhere.
	- Best for very large codebases that need strict persistence abstraction.
	- Can be useful if the team strongly prefers a uniform pattern.
	- Too much ceremony for this MVP.

3. Use a dedicated state machine library.
	- Best if workflow rules become formally complex.
	- Useful later if transitions branch heavily and need visual tooling.
	- Not necessary for the current guided workflow.

### Implementation Details
- Generate API types from OpenAPI into `packages/contracts`.
- Build `packages/api-client` around fetch helpers that consume those generated types.
- Keep auth/session plumbing inside the client package so app code stays simple.
- Add repository files only for modules with real query complexity or cross-table operations.
- Put transition rules in one backend helper per workflow area, such as `projects/transitions.py`.

### Final Decision
- Put the shared frontend API client in `packages/api-client`.
- Use generated types plus hand-written request helpers.
- Keep transition helpers inside each module.
- Keep repositories explicit and separate per module instead of forcing a shared base class.

## Grooming Round 6: Local Dev and Docker

### Recommended MVP Choice
- Use Docker Compose for local development.
- Bring up Postgres, Redis, MinIO-compatible object storage, the FastAPI API, the Celery worker, and the Next.js app.
- Keep the developer loop simple with one command to start infrastructure and one command per app to run in watch mode.

### Why This Is the Best Fit
- The MVP needs a realistic local environment for jobs, object storage, and relational data.
- Docker Compose gives the whole team the same local services without requiring custom machine setup.
- MinIO is a good local stand-in for object storage because it matches the app's upload and generated asset needs.
- Keeping services explicit prevents the team from hiding important runtime dependencies behind in-process mocks.

### Local Stack
- `postgres` for the primary database.
- `redis` for Celery broker and lightweight cache needs.
- `minio` for uploads and generated asset storage.
- `api` for FastAPI.
- `worker` for Celery.
- `web` for Next.js.

### Implementation Details
- Use a root `docker-compose.yml` or `compose.yaml` for shared services.
- Add service-specific `.env.example` files and a root example for shared values.
- Mount source code into containers for live reload in development.
- Keep migrations and seed scripts as explicit commands, not hidden container startup magic.

### Final Decision
- Use a root `compose.yaml` with profiles for local infrastructure.
- Run Postgres, Redis, and MinIO in Docker.
- Run the app services locally in watch mode for the best developer loop.
- Keep an optional admin UI out of the MVP.

## Grooming Round 7: CI and Checks

### Recommended MVP Choice
- Use GitHub Actions as the primary CI system.
- Run lint, type check, tests, contract generation checks, and migration validation on every pull request.
- Add a separate workflow for dependency updates and scheduled maintenance only if needed later.

### Why This Is the Best Fit
- GitHub Actions is the simplest default for a monorepo on GitHub.
- The MVP needs high signal checks that catch workflow, schema, and contract drift early.
- Contract generation and migration validation matter as much as unit tests in a workflow-heavy system.

### Required CI Jobs
1. `web-lint` for frontend linting and formatting checks.
2. `web-test` for frontend unit or component tests.
3. `web-build` for production build validation.
4. `api-lint` for backend lint and static checks.
5. `api-test` for backend tests.
6. `api-typecheck` for backend type checking.
7. `contracts-check` for OpenAPI and generated client/type drift.
8. `migrations-check` for Alembic sanity and upgrade path validation.
9. `compose-smoke` for a minimal integration smoke test against the local stack.

### Implementation Details
- Keep PR checks fast enough that the team actually waits for them.
- Split required and optional jobs so developers can see what blocked merge.
- Cache dependencies aggressively in GitHub Actions.
- Make CI fail if generated contracts are out of date.

### Final Decision
- Block merges on lint, type check, tests, contract drift checks, migrations validation, and compose smoke tests.
- Add a nightly smoke test workflow for extra confidence.
- Keep PR validation and release packaging in the same workflow family, with release-specific triggers as needed.

## Grooming Round 8: Linting, Testing, and Release Conventions

### Recommended MVP Choice
- Backend: Ruff for lint and format, Pytest for tests, and MyPy for type checking if the codebase stays disciplined.
- Frontend: ESLint, Prettier, Vitest or Jest for unit tests, and Playwright for end-to-end tests.
- Release flow: trunk-based development with short-lived feature branches and protected main.

### Why This Is the Best Fit
- Ruff keeps Python tooling fast and simple.
- MyPy is useful if we want stronger backend type discipline around contracts and services.
- The frontend stack is standard and easy for a Next.js team to maintain.
- Protected main plus small PRs keeps workflow and schema changes reviewable.

### Testing Strategy
- Backend unit tests for services, transitions, validation, and provider adapters.
- Backend integration tests for route + DB behavior.
- Frontend component tests for interactive states and validation.
- Playwright tests for the guided end-to-end workflow.
- Contract tests for generated client/type consistency.

### Release and Review Conventions
- Require at least one reviewer for changes outside docs or trivial fixes.
- Require migration review for schema changes.
- Require contract diff review when API shapes change.
- Use conventional commit messages if the team wants automated changelog support later, but don't over-engineer release automation yet.

### Final Decision
- Use Ruff for Python linting and formatting.
- Use Pytest for backend tests.
- Use MyPy in the API package and shared Python packages.
- Use ESLint and Prettier for the frontend.
- Require frontend unit tests where they cover core interactive states, and use Playwright for the end-to-end guided workflow.
- Add CODEOWNERS for backend, frontend, and infra paths.

## Decision Log

### Product Orchestration
- Keep orchestration inside FastAPI as a deterministic workflow engine.
- Use explicit backend state transitions in Postgres.
- Use a background worker for long-running jobs.
- Use a simple ReAct-style LLM harness only inside step-level tasks such as interview synthesis or plan writing.
- Keep the interview as a simple state machine with conditional branching.
- Run research and plan generation as asynchronous jobs with streamed progress updates in the UI.
- Use separate Celery queues by domain area rather than one undifferentiated queue.

### Codebase Shape
- Use a monorepo.
- Generate shared contracts from FastAPI's OpenAPI schema into frontend-consumable types.
- Use Celery with Redis for background jobs.
- Use `packages/contracts` for generated types and enums.
- Use `packages/api-client` for fetch helpers, auth-aware transport, and request utilities.
- Keep repositories only where persistence logic is nontrivial.
- Model workflow state with plain enums plus small module-local transition helpers.
- Keep module repositories explicit and separate per module instead of forcing a shared base class.

### Data Layer and Contracts
- Use SQLAlchemy 2.0 as the backend ORM and query layer.
- Use Alembic from day one for migrations.
- Use Pydantic v2 for API schemas and validation.
- Generate frontend-friendly TypeScript types from FastAPI's OpenAPI output.
- Keep backend transition helpers inside each module, such as `projects/transitions.py`, rather than in a separate shared workflow package.
- Use generated types plus hand-written request helpers for the API client.

### Local Dev and Docker
- Use a root `compose.yaml` with profiles for local infrastructure.
- Run Postgres, Redis, and MinIO in Docker.
- Run the Next.js app and FastAPI app locally in watch mode for the best developer loop.
- Keep an optional admin UI out of the MVP.

### CI and Checks
- Use GitHub Actions as the primary CI system.
- Block merges on frontend lint, backend lint, backend type checking, backend tests, frontend tests where present, contracts drift checks, migrations validation, and compose smoke tests.
- Add a nightly smoke test workflow for extra confidence.
- Keep PR validation and release packaging in the same repository workflow family, with release-specific triggers as needed.

### Linting, Testing, and Release Conventions
- Use Ruff for Python linting and formatting.
- Use Pytest for backend tests.
- Use MyPy in the API package and shared Python packages.
- Use ESLint and Prettier for the frontend.
- Require frontend unit tests for changed UI logic and Playwright for workflow-level changes.
- Add CODEOWNERS for backend, frontend, and infra directories.
- Keep trunk-based development with short-lived feature branches and protected main.

### Summary of Decisions
- The MVP should behave like a guided product workflow, not a general agent platform.
- FastAPI owns workflow state and business logic.
- Celery owns durable async work.
- OpenAPI owns cross-stack contracts.
- SQLAlchemy and Alembic own the backend persistence path.
- The repo should optimize for clarity, speed, and recoverability over abstraction-heavy architecture.

## MVP Guardrails
- Do not add campaign management.
- Do not add analytics dashboards.
- Do not add automation loops or A/B testing.
- Do not add team collaboration.
- Do not broaden the product beyond the guided creative workflow until the first slice works reliably.

## Definition of Done
- The product can take a brand from setup to generated video assets in one guided flow.
- The creative plan is always visible before generation.
- Generation and publishing are persisted and recoverable.
- The implementation honors the PRD and UX constraints.
- The codebase has enough structure for continued development without scope drift.
