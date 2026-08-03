# MVP Scrum Backlog

## Purpose
This backlog converts the product vision, UX, technical spec, and implementation plan into an execution-ready epic/story list for the MVP.

Primary source artifacts:
- [PRD](prd.md)
- [UX Spec](ux-spec.md)
- [MVP Technical Spec](mvp-technical-spec.md)
- [MVP Implementation Plan](implementation-plan.md)

## Scrum Approach for the MVP
The MVP is best run as a tight product scrum with one stable squad and a narrow release goal: ship one complete guided workflow end to end.

Operating model:
- Sprint length: 2 weeks
- Cadence: weekly backlog refinement, daily standup, sprint review, sprint retrospective
- Planning rule: pull the smallest story set that completes one thin vertical slice before expanding breadth
- Release rule: demo working workflow increments every sprint, even if later epics are still partial
- Estimation rule: use relative story points only after stories are vertically sliced and independently testable
- WIP rule: keep one primary epic in focus per sprint unless a dependent infrastructure story is blocking

Backlog ordering principle:
1. Foundation and shared contracts first.
2. Brand Brain and project workflow next.
3. Research and creative plan next.
4. Generation, publishing, billing, and hardening after the workflow is stable.

## Global Story Standards
Every story in this backlog follows the same body structure.

### Epic Body Standard
Each epic includes:
- Epic goal
- Source artifact references
- In-scope outcome
- Dependencies
- Exit criteria
- Notes on what is explicitly out of scope

### Story Body Standard
Each story includes:
- User story statement
- Why it exists
- Source artifact references
- Acceptance criteria
- Implementation notes
- Test notes
- Dependencies

### Definition of Ready
A story is ready for sprint pickup when:
- The user outcome is clear
- The acceptance criteria are testable
- The story fits in one sprint slice or can be split
- The dependent data model or API surface is known
- The story references the correct product and technical artifacts

### Definition of Done
A story is done when:
- The acceptance criteria pass
- The implementation matches the agreed product flow
- The UX and backend state stay aligned
- The relevant tests exist and pass
- The story can be demonstrated end to end where applicable

## Epic 1: Repo Foundation and Shared Contracts

### Epic Body
- Goal: establish the monorepo, base services, shared contracts, and development rules that every other epic depends on.
- Source artifacts: [Implementation Plan](implementation-plan.md) Phase 1, Grooming Round 2, Grooming Round 4, Grooming Round 6, PRD Product Architecture, Technical Spec System Overview.
- In scope: repo scaffold, contracts generation, app shells, local infra, base CI rules, documentation alignment.
- Dependencies: none.
- Exit criteria: the web app, API, and worker can run locally and share versioned contracts.
- Out of scope: feature depth, production deployment hardening, and provider selection.

### Stories
#### E1-S1 - Create the monorepo scaffold
- User story: As a developer, I want a consistent repo layout, so that frontend, backend, worker, and shared packages can evolve together.
- Why it exists: this prevents early drift between app surfaces and shared types.
- Source artifact references: [Implementation Plan](implementation-plan.md) Phase 1 and Grooming Round 2, [AGENTS.md](../AGENTS.md) Repository Defaults.
- Acceptance criteria:
  - The repository contains `apps/web`, `apps/api`, `apps/worker`, `packages/contracts`, `packages/api-client`, `infra`, and `docs`.
  - The folder layout matches the repo governance guidance.
  - The structure is documented for future contributors.
- Implementation notes: keep the scaffold minimal until the first vertical slice is ready.
- Test notes: validate workspace layout and basic app bootstraps.
- Dependencies: none.

#### E1-S2 - Define shared contract generation
- User story: As a developer, I want backend contracts to generate frontend-ready types, so that the API shape stays consistent.
- Why it exists: contract drift is a major risk for a FastAPI plus Next.js stack.
- Source artifact references: [MVP Technical Spec](mvp-technical-spec.md) Shared Contracts, [Implementation Plan](implementation-plan.md) Grooming Round 4 and Decision Log.
- Acceptance criteria:
  - FastAPI OpenAPI output can be transformed into TypeScript types.
  - Shared enums and DTOs live in `packages/contracts`.
  - The generation step is repeatable and documented.
- Implementation notes: keep Pydantic as the backend source of truth.
- Test notes: add a drift check that fails when generated types are stale.
- Dependencies: monorepo scaffold.

#### E1-S3 - Establish local infrastructure composition
- User story: As a developer, I want local services for Postgres, Redis, and object storage, so that I can run the full workflow on my machine.
- Why it exists: the MVP depends on durable jobs, relational state, and file storage.
- Source artifact references: [Implementation Plan](implementation-plan.md) Grooming Round 6 and Decision Log, [MVP Technical Spec](mvp-technical-spec.md) Storage.
- Acceptance criteria:
  - Local infrastructure can be started from the repo root.
  - Postgres, Redis, and MinIO-compatible storage are available.
  - The app services can run in watch mode against those services.
- Implementation notes: keep app services outside Docker for the preferred developer loop.
- Test notes: add a smoke check that the stack boots and services can connect.
- Dependencies: monorepo scaffold.

#### E1-S4 - Add baseline repo governance
- User story: As the team, we want clear repo rules, so that future work stays aligned to the MVP architecture.
- Why it exists: the backlog needs a stable policy anchor for future implementation work.
- Source artifact references: [AGENTS.md](../AGENTS.md), [Implementation Plan](implementation-plan.md) Decision Log.
- Acceptance criteria:
  - Repo guidance covers frontend, backend, worker, contracts, docs, testing, and release conventions.
  - CODEOWNERS guidance is included as a required follow-up.
  - The docs root is treated as canonical.
- Implementation notes: keep this file and the plan aligned.
- Test notes: repo policy checks are documentation-driven for now.
- Dependencies: none.

## Epic 2: Brand Brain and Access

### Epic Body
- Goal: let a user create and persist brand context before any creative workflow begins.
- Source artifact references: [PRD](prd.md) Brand Brain, [PRD](prd.md) Core User Journey, [UX Spec](ux-spec.md) First Time User Experience, Brand Brain, and Empty States, [Implementation Plan](implementation-plan.md) Phase 2.
- In scope: onboarding, brand profile, brand assets, persistence, and gating the workflow on required brand data.
- Dependencies: Epic 1.
- Exit criteria: a brand can be created, edited, and reused across sessions.
- Out of scope: advanced workspace collaboration and multi-brand governance.

### Stories
#### E2-S1 - Create the first-time onboarding path
- User story: As a new user, I want a guided setup flow, so that I can start without learning the product structure first.
- Why it exists: the product promise depends on low-friction first-time setup.
- Source artifact references: [UX Spec](ux-spec.md) First Time User Experience and Home, [PRD](prd.md) Product Principles.
- Acceptance criteria:
  - The onboarding flow introduces the Brand Brain concept.
  - The user can enter the minimum brand context required for later generation.
  - The flow ends in a usable first project entry point.
- Implementation notes: keep the flow linear and avoid extra setup decisions.
- Test notes: cover the happy path and validation failures.
- Dependencies: Epic 1.

#### E2-S2 - Persist Brand Brain core fields
- User story: As a user, I want my brand context saved, so that I do not repeat setup for every project.
- Why it exists: brand memory is a core product differentiator.
- Source artifact references: [PRD](prd.md) Brand Brain, [MVP Technical Spec](mvp-technical-spec.md) Brand Brain and Data Model Draft.
- Acceptance criteria:
  - Brand name, website, product details, audience, voice, assets, and competitors can be stored.
  - The user can update saved brand data.
  - Saved brand data survives refresh and new sessions.
- Implementation notes: keep the data model normalized enough for later growth.
- Test notes: add persistence tests for create and update flows.
- Dependencies: Epic 1.

#### E2-S3 - Enforce Brand Brain readiness before generation
- User story: As the system, I want to block expensive steps until brand context exists, so that generation happens only with enough input.
- Why it exists: this protects quality and prevents wasted compute.
- Source artifact references: [MVP Technical Spec](mvp-technical-spec.md) Key Workflow Rules, [Implementation Plan](implementation-plan.md) Phase 2 Exit Criteria.
- Acceptance criteria:
  - Generation is blocked when required brand fields are missing.
  - The UI explains what is missing.
  - The block is enforced by the backend, not only the frontend.
- Implementation notes: make the backend the source of truth for readiness checks.
- Test notes: verify both UI state and backend rejection behavior.
- Dependencies: E2-S2.

#### E2-S4 - Support brand assets and competitors
- User story: As a user, I want to attach brand assets and competitors, so that creative outputs reflect the market context.
- Why it exists: assets and competitive context feed research and planning.
- Source artifact references: [PRD](prd.md) Brand Brain and Inspiration Import, [UX Spec](ux-spec.md) Brand Brain.
- Acceptance criteria:
  - The user can store logo/colors/assets.
  - The user can store competitor references.
  - These inputs are available to later workflow steps.
- Implementation notes: keep this flexible for future object storage and metadata.
- Test notes: verify asset references persist and are retrievable.
- Dependencies: E2-S2.

## Epic 3: Project Workflow and Interview

### Epic Body
- Goal: let a user create a creative project, capture the objective, and complete the guided interview.
- Source artifact references: [PRD](prd.md) Projects and AI Creative Interview, [UX Spec](ux-spec.md) Creative Projects, Create Project Flow, and AI Interview, [Implementation Plan](implementation-plan.md) Phase 3.
- In scope: project lifecycle, state transitions, interview branching, structured brief persistence.
- Dependencies: Epic 2.
- Exit criteria: a project can be created, interviewed, and reopened after refresh.
- Out of scope: deep autonomous agent behavior and broad campaign management.

### Stories
#### E3-S1 - Create the project shell and list view
- User story: As a user, I want a project list and detail shell, so that each creative objective is organized in one place.
- Why it exists: the project is the unit of work for the MVP.
- Source artifact references: [PRD](prd.md) Projects, [UX Spec](ux-spec.md) Creative Projects.
- Acceptance criteria:
  - The user can create a project.
  - The user can view the project list and project detail shell.
  - The project has a visible status.
- Implementation notes: start with the smallest useful shell and expand later.
- Test notes: cover project creation and page loading.
- Dependencies: Epic 2.

#### E3-S2 - Implement the project state machine
- User story: As the backend, I want explicit project states, so that workflow progression is deterministic and resumable.
- Why it exists: state clarity is required for approvals, jobs, and retries.
- Source artifact references: [MVP Technical Spec](mvp-technical-spec.md) Projects and Key Workflow Rules, [Implementation Plan](implementation-plan.md) Grooming Round 1 Decision Log.
- Acceptance criteria:
  - Project states follow the agreed lifecycle.
  - Invalid transitions are rejected.
  - State changes are persisted and auditable.
- Implementation notes: keep state helpers close to the project module.
- Test notes: add transition tests for valid and invalid edges.
- Dependencies: E3-S1.

#### E3-S3 - Build the guided interview flow
- User story: As a user, I want a conversational interview, so that I can provide strategy input without writing prompts.
- Why it exists: the interview is the main UX bridge between brand context and planning.
- Source artifact references: [PRD](prd.md) AI Creative Interview, [UX Spec](ux-spec.md) AI Interview, [MVP Technical Spec](mvp-technical-spec.md) AI Creative Interview.
- Acceptance criteria:
  - The interview adapts based on prior answers.
  - The first pass stays compact and conversational.
  - The result is a structured brief.
- Implementation notes: keep the UI focused on one question at a time.
- Test notes: cover branching and brief persistence.
- Dependencies: E3-S2.

#### E3-S4 - Persist and reopen the structured brief
- User story: As a user, I want my brief saved, so that I can return to it after refresh or navigation.
- Why it exists: the guided workflow must survive interruption.
- Source artifact references: [UX Spec](ux-spec.md) Creative Projects and Loading/Error States, [MVP Technical Spec](mvp-technical-spec.md) Interview and Data Model Draft.
- Acceptance criteria:
  - Interview answers and the derived brief persist.
  - The project detail view can reopen the brief.
  - The user can continue from the saved point.
- Implementation notes: preserve state explicitly in the backend.
- Test notes: verify persistence and resume behavior.
- Dependencies: E3-S3.

## Epic 4: Research and Creative Plan

### Epic Body
- Goal: transform brand and interview context into a reviewable strategic plan before generation.
- Source artifact references: [PRD](prd.md) AI Research and Creative Planning, [UX Spec](ux-spec.md) Research Phase and Creative Plan Screen, [Implementation Plan](implementation-plan.md) Phase 4.
- In scope: research jobs, source aggregation, creative plan output, confidence framing, approval gating.
- Dependencies: Epic 3.
- Exit criteria: the user can run research and review a plan before generation starts.
- Out of scope: research-heavy agent orchestration and autonomous optimization loops.

### Stories
#### E4-S1 - Run asynchronous research jobs
- User story: As a user, I want research to run in the background, so that I can see progress without blocking the app.
- Why it exists: research is expensive enough to justify job handling.
- Source artifact references: [UX Spec](ux-spec.md) Research Phase, [Implementation Plan](implementation-plan.md) Grooming Round 1 Final Decision.
- Acceptance criteria:
  - Research can be started from a project.
  - Progress is visible in the UI.
  - The job state is stored in the backend.
- Implementation notes: keep research separate from the request lifecycle.
- Test notes: verify job creation and status updates.
- Dependencies: E3-S4.

#### E4-S2 - Capture research sources and findings
- User story: As a user, I want to see the sources and findings used for planning, so that I can trust the output.
- Why it exists: trust is a core product principle.
- Source artifact references: [PRD](prd.md) Inspiration Import and Product Principles, [UX Spec](ux-spec.md) Research Phase.
- Acceptance criteria:
  - The system stores source references and findings.
  - The UI can surface the main insights.
  - The output supports later plan generation.
- Implementation notes: keep source metadata traceable.
- Test notes: verify source persistence and retrieval.
- Dependencies: E4-S1.

#### E4-S3 - Generate the creative plan
- User story: As a user, I want a creative plan before generation, so that I can approve strategy instead of raw output.
- Why it exists: the plan is the core trust-building surface in the workflow.
- Source artifact references: [PRD](prd.md) Creative Planning, [UX Spec](ux-spec.md) Creative Plan Screen, [MVP Technical Spec](mvp-technical-spec.md) Creative Plan.
- Acceptance criteria:
  - The plan includes objective, audience, creative angle, hook, style, story, scene breakdown, reference inspirations, and confidence score.
  - The plan is reviewable before generation.
  - The plan can be edited or regenerated if needed.
- Implementation notes: keep the plan human-readable and explicit.
- Test notes: cover plan content and review states.
- Dependencies: E4-S2.

#### E4-S4 - Require approval before generation
- User story: As the system, I want a plan approval gate, so that generation never starts before human sign-off.
- Why it exists: this is a product policy and cost-control boundary.
- Source artifact references: [PRD](prd.md) Human approval principle, [MVP Technical Spec](mvp-technical-spec.md) Key Workflow Rules.
- Acceptance criteria:
  - Generation remains blocked until the plan is approved.
  - The approved state is persisted.
  - The UI clearly shows approval status.
- Implementation notes: enforce the gate in the backend and the UI.
- Test notes: verify that generation requests fail before approval.
- Dependencies: E4-S3.

## Epic 5: Generation and Provider Adapter

### Epic Body
- Goal: generate scripts, storyboards, reference frames, and final videos through a backend provider adapter.
- Source artifact references: [PRD](prd.md) Video Generation, [UX Spec](ux-spec.md) Video Generation, [MVP Technical Spec](mvp-technical-spec.md) Generation and AI Provider, [Implementation Plan](implementation-plan.md) Phase 5.
- In scope: provider abstraction, generation jobs, credit deduction, outputs, retries.
- Dependencies: Epic 4.
- Exit criteria: a user can approve a plan and generate usable video outputs.
- Out of scope: model benchmarking, provider fan-out, and advanced agent orchestration.

### Stories
#### E5-S1 - Create the generation provider interface
- User story: As the backend, I want a provider interface, so that the concrete video model can change without affecting product flow.
- Why it exists: the provider is unresolved; the system builds against a mock output contract until a real provider is integrated.
- Source artifact references: [MVP Technical Spec](mvp-technical-spec.md) AI Provider and Implementation Notes, [Implementation Plan](implementation-plan.md) Grooming Round 1, Decision Log (Generation Provider Strategy).
- Acceptance criteria:
  - Generation calls route through a provider interface.
  - The request shape is provider-agnostic.
  - A mock provider implementation exists that returns synthetic outputs matching the contract shape.
  - The mock contract covers: script text, storyboard frames (image URLs), rendered video (MP4 URL), metadata (duration, resolution, provider job ID).
  - The implementation can be swapped without changing project logic.
- Implementation notes: keep the adapter narrow and explicit. The mock provider should simulate 30–120 second latency and return realistic synthetic data for development and testing.
- Test notes: add interface, contract, and mock-output tests.
- Dependencies: E4-S4.

#### E5-S2 - Execute generation as a background job
- User story: As a user, I want generation to run asynchronously, so that the app can show progress and remain responsive.
- Why it exists: generation is expensive and may take time.
- Source artifact references: [UX Spec](ux-spec.md) Video Generation and Loading/Error States, [Implementation Plan](implementation-plan.md) Phase 5.
- Acceptance criteria:
  - A generation request creates a job.
  - The UI shows progress states.
  - The job state persists across refresh.
- Implementation notes: keep the worker responsible for heavy execution.
- Test notes: verify job lifecycle and status transitions.
- Dependencies: E5-S1.

#### E5-S3 - Produce variation-rich outputs
- User story: As a user, I want multiple output variations, so that I can compare hooks, openings, and formats.
- Why it exists: variation supports creative discovery and better final selection.
- Source artifact references: [PRD](prd.md) Functional Requirements, [UX Spec](ux-spec.md) Video Generation.
- Acceptance criteria:
  - The system can request multiple variations.
  - The system supports different hooks/openings.
  - The system supports multiple aspect ratios when possible.
- Implementation notes: keep variation metadata attached to each output.
- Test notes: validate variation metadata and selection behavior.
- Dependencies: E5-S2.

#### E5-S4 - Deduct and validate credits for generation
- User story: As the backend, I want to check and deduct credits, so that expensive work is controlled by entitlement rules.
- Why it exists: billing is part of the MVP and protects cost exposure.
- Source artifact references: [PRD](prd.md) Business Model, [MVP Technical Spec](mvp-technical-spec.md) Billing and Credits.
- Acceptance criteria:
  - Credits are checked before generation starts.
  - Credits are deducted when the expensive operation succeeds or reaches the defined billing point.
  - Insufficient credit blocks generation with a clear message.
- Implementation notes: keep the ledger explicit and auditable.
- Test notes: cover success, failure, and insufficient-credit paths.
- Dependencies: E5-S2.

## Epic 6: Publishing and Export

### Epic Body
- Goal: let the user deliver final assets through direct publishing or export fallback.
- Source artifact references: [PRD](prd.md) Publishing, [UX Spec](ux-spec.md) Publish Experience, [Implementation Plan](implementation-plan.md) Phase 6 and Decision Log (Publishing Platform Staging).
- In scope: publish job orchestration, publish history, export/download, finalized asset handling. Direct publish targets are Instagram and TikTok only.
- Deferred: Facebook and YouTube Shorts direct publishing (post-MVP).
- Dependencies: Epic 5.
- Exit criteria: the user can publish to Instagram or TikTok, or export a finalized asset from the project view.
- Out of scope: social scheduling, campaign dashboards, multi-platform automation, Facebook, and YouTube Shorts.

### Stories
#### E6-S1 - Support publish job orchestration
- User story: As a user, I want publishing to run as a job, so that long-running platform actions are tracked clearly.
- Why it exists: publishing can fail independently of generation.
- Source artifact references: [MVP Technical Spec](mvp-technical-spec.md) Publishing and Data Model Draft.
- Acceptance criteria:
  - Publish requests create tracked jobs.
  - Job status is visible in the UI.
  - Publish history is persisted.
- Implementation notes: keep the publish workflow separate from generation.
- Test notes: verify publish state transitions and result storage.
- Dependencies: E5-S3.

#### E6-S2 - Provide export and download fallback
- User story: As a user, I want to download the final asset, so that I always have a usable output even if direct publishing is unavailable.
- Why it exists: fallback delivery is part of the MVP promise.
- Source artifact references: [PRD](prd.md) Publishing, [UX Spec](ux-spec.md) Publish Experience.
- Acceptance criteria:
  - The user can export or download the finalized asset.
  - The download path uses finalized assets only.
  - The UI makes the fallback obvious.
- Implementation notes: keep export metadata traceable.
- Test notes: verify asset access and final-state gating.
- Dependencies: E6-S1.

#### E6-S3 - Record publish targets and history
- User story: As a user, I want publish history, so that I can see where a project was delivered.
- Why it exists: the project view should tell the story of delivery.
- Source artifact references: [PRD](prd.md) Projects and Publishing, [MVP Technical Spec](mvp-technical-spec.md) PublishJob.
- Acceptance criteria:
  - The publish target is recorded.
  - Success or failure is recorded.
  - The history is visible on the project.
- Implementation notes: keep the record immutable where possible.
- Test notes: verify history entries are created and returned.
- Dependencies: E6-S1.

## Epic 7: Billing, Credits, and Safety

### Epic Body
- Goal: add the minimum billing and credit controls required for cost-safe generation.
- Source artifact references: [PRD](prd.md) Business Model and Risks, [MVP Technical Spec](mvp-technical-spec.md) Billing and Credits, [Implementation Plan](implementation-plan.md) Phase 7.
- In scope: credit balance, ledger, low-credit states, entitlement checks, usage blocking.
- Dependencies: Epic 5.
- Exit criteria: the system prevents expensive operations when credits are insufficient and explains why.
- Out of scope: full pricing experimentation, usage analytics dashboards, and enterprise billing complexity.

### Stories
#### E7-S1 - Surface credit balance and ledger
- User story: As a user, I want to see my available credits, so that I understand what I can still generate.
- Why it exists: credit visibility is required for trust and control.
- Source artifact references: [PRD](prd.md) Business Model, [UX Spec](ux-spec.md) Billing and credit-related states, [MVP Technical Spec](mvp-technical-spec.md) CreditLedgerEntry.
- Acceptance criteria:
  - The current balance is visible.
  - Ledger entries are viewable.
  - The data is consistent with generation and publish actions.
- Implementation notes: keep the ledger queryable and auditable.
- Test notes: verify balance calculations and ledger retrieval.
- Dependencies: E5-S4.

#### E7-S2 - Block expensive actions when credits are low
- User story: As the system, I want to block costly work when balance is too low, so that users do not enter a broken flow.
- Why it exists: this protects the product experience and infrastructure spend.
- Source artifact references: [PRD](prd.md) Risks and Mitigation, [MVP Technical Spec](mvp-technical-spec.md) Key Workflow Rules.
- Acceptance criteria:
  - The backend rejects expensive requests when the balance is insufficient.
  - The UI explains the block condition.
  - The user can recover by adding credits or reducing usage.
- Implementation notes: keep the failure explicit and user-friendly.
- Test notes: validate the blocked path and messaging.
- Dependencies: E7-S1.

#### E7-S3 - Add low-credit warnings
- User story: As a user, I want a warning before I run out of credits, so that I can plan the next action.
- Why it exists: proactive warnings reduce friction and failed attempts.
- Source artifact references: [UX Spec](ux-spec.md) Billing UI and Notifications, [PRD](prd.md) Success Metrics.
- Acceptance criteria:
  - Low-credit states are visible in the UI.
  - The warning appears before a hard block if possible.
  - The warning does not obscure the main workflow.
- Implementation notes: keep the warning prominent but not noisy.
- Test notes: cover threshold logic and UI visibility.
- Dependencies: E7-S1.

## Epic 8: Quality, Validation, and Release Readiness

### Epic Body
- Goal: make the MVP reliable enough to ship and evolve without breaking the guided workflow.
- Source artifact references: [Implementation Plan](implementation-plan.md) Grooming Rounds 7 and 8, [AGENTS.md](../AGENTS.md) Testing Expectations and Development Practices, [MVP Technical Spec](mvp-technical-spec.md) Acceptance Criteria.
- In scope: linting, tests, contract checks, migration checks, smoke tests, workflow validation.
- Dependencies: all implementation epics.
- Exit criteria: the team can merge changes with confidence and demo the full flow reliably.
- Out of scope: enterprise-grade observability, full analytics, and heavyweight release automation.

### Stories
#### E8-S1 - Add backend quality checks
- User story: As a developer, I want linting, type checking, and tests, so that backend changes stay safe.
- Why it exists: the backend owns workflow and billing truth.
- Source artifact references: [Implementation Plan](implementation-plan.md) Grooming Round 7 and 8, [AGENTS.md](../AGENTS.md) Testing Expectations.
- Acceptance criteria:
  - Backend linting runs in CI.
  - Backend type checking runs in CI.
  - Backend tests run in CI.
- Implementation notes: keep the suite focused and fast.
- Test notes: make the CI gates fail on real regressions only.
- Dependencies: Epic 1.

#### E8-S2 - Add frontend quality checks
- User story: As a developer, I want frontend linting and tests, so that UI regressions are caught early.
- Why it exists: the guided experience is a major product differentiator.
- Source artifact references: [Implementation Plan](implementation-plan.md) Grooming Round 8, [UX Spec](ux-spec.md) Interaction and loading states.
- Acceptance criteria:
  - Frontend linting runs in CI.
  - Frontend unit or component tests run where they add value.
  - Playwright covers the critical workflow.
- Implementation notes: keep the tests aligned with the product journey.
- Test notes: add one critical end-to-end path before broadening coverage.
- Dependencies: Epic 1.

#### E8-S3 - Add contract and migration validation
- User story: As a developer, I want contract drift and migration checks, so that backend and frontend stay aligned as the schema evolves.
- Why it exists: schema drift and broken migrations are high-risk for this stack.
- Source artifact references: [Implementation Plan](implementation-plan.md) Grooming Round 7, [MVP Technical Spec](mvp-technical-spec.md) Shared Contracts and Data Model Draft.
- Acceptance criteria:
  - Generated contracts are checked in CI.
  - Migration validation runs in CI.
  - Failures are visible before merge.
- Implementation notes: keep the checks deterministic.
- Test notes: deliberately break the generation path in a test branch to verify the gate.
- Dependencies: Epic 1.

#### E8-S4 - Add a compose smoke test
- User story: As the team, we want a smoke test against the local stack, so that the end-to-end environment is known to work.
- Why it exists: this is the simplest integration confidence check for the MVP stack.
- Source artifact references: [Implementation Plan](implementation-plan.md) Grooming Round 6 and 7, [AGENTS.md](../AGENTS.md) Repository Defaults.
- Acceptance criteria:
  - The root stack can boot in a smoke scenario.
  - The services can connect end to end.
  - Failures are easy to interpret.
- Implementation notes: keep the smoke test lightweight and maintainable.
- Test notes: run the smoke test in CI and locally.
- Dependencies: Epic 1.

## Suggested Sprint Split
This is the first-pass scrum order for MVP delivery.

- Sprint 0: Epic 1 foundation stories.
- Sprint 1: Epic 2 brand and access stories.
- Sprint 2: Epic 3 project workflow and interview stories.
- Sprint 3: Epic 4 research and creative plan stories.
- Sprint 4: Epic 5 generation stories.
- Sprint 5: Epic 6 publishing stories and Epic 7 billing stories.
- Sprint 6: Epic 8 quality and hardening stories, plus remaining fixups.

## Notes for Grooming
- Keep each story vertical and demoable.
- Split anything that mixes backend, frontend, and infra into smaller stories if it is too large for a sprint.
- Treat the PRD as the product authority, the UX spec as the interaction authority, the technical spec as the architecture authority, and the implementation plan as the sequencing authority.
- Re-check the docs whenever a story is split so the backlog stays aligned with the product vision.

## Deferred Items
The following items are explicitly deferred from the MVP backlog. They are described in the PRD and UX spec but are not scheduled for the current release.

- **Creative Vault**: The persistent searchable library of inspirations, hooks, concepts, and references. Inspiration inputs are still accepted as part of the research step. The vault as a first-class browsable library is post-MVP.
- **Inspiration Import Flow**: The dedicated share/paste/upload flow with creative pattern extraction. Handled as a research input, not a standalone feature.
- **Facebook Direct Publishing**: Deferred. Instagram and TikTok are the first two direct-publish targets.
- **YouTube Shorts Direct Publishing**: Deferred. Instagram and TikTok are the first two direct-publish targets.

When any deferred item is brought back into scope, it should be specified as a new epic with its own stories, referencing the PRD and UX spec sections that define it.
