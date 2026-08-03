# Common Repo Mistakes

This file tracks recurring development mistakes and anti-patterns observed in this repository. Review this checklist before submitting changes.

## Purpose
This is a living document. Update it whenever a pattern of mistakes emerges from code reviews, incident postmortems, or sprint retrospectives. Every item should describe the mistake, why it matters, and how to avoid it.

---

## Contract and Schema Drift
- **Mistake**: Changing a Pydantic schema without regenerating the frontend TypeScript types.
- **Why it matters**: The frontend silently receives wrong types, causing runtime errors instead of compile-time catches.
- **Prevention**: Always run the contract generation script after changing any API schema. CI will catch this, but catching it locally is faster.

## State Transitions Without Tests
- **Mistake**: Adding a new project or job state without adding transition tests.
- **Why it matters**: Invalid transitions can put projects into unrecoverable states, especially around approval gating and credit checks.
- **Prevention**: Every new state or transition edge requires a corresponding test in the module's test suite.

## Frontend Assumes Backend State
- **Mistake**: Using frontend-only state (React state, local storage) as the source of truth for workflow progression.
- **Why it matters**: The backend is the source of truth. Frontend-only state will desync on refresh, navigation, or multi-tab usage.
- **Prevention**: Always fetch workflow state from the backend. Use frontend state only for transient UI concerns like form input.

## Missing Credit Checks
- **Mistake**: Adding a new expensive operation without a corresponding credit check.
- **Why it matters**: Unmetered expensive operations expose the platform to uncontrolled costs.
- **Prevention**: Any new Celery task or generation-related endpoint must include a credit balance check before execution.

## Overly Broad Celery Tasks
- **Mistake**: Putting too much business logic inside a Celery task instead of delegating to service functions.
- **Why it matters**: Celery tasks should be thin wrappers. Business logic in tasks is harder to test, harder to reuse, and couples the logic to the task infrastructure.
- **Prevention**: Keep tasks as thin dispatchers that call service-layer functions.

## Publishing Without Finalized Assets
- **Mistake**: Allowing publish or export actions on assets that are still in a generating or draft state.
- **Why it matters**: Users receive broken or incomplete outputs, and platform API calls may fail with invalid media.
- **Prevention**: The publish and export paths must check asset finalization state in the backend before proceeding.

## Silent Migration Failures
- **Mistake**: Writing Alembic migrations that are not idempotent or that fail on an already-migrated database.
- **Why it matters**: Broken migrations block deployment and can corrupt production data.
- **Prevention**: Test migrations with `alembic upgrade head` from a clean state and from the current production state. CI checks should validate the upgrade path.

## Hardcoded Provider Assumptions
- **Mistake**: Writing generation logic that assumes a specific provider's response format, latency, or capabilities.
- **Why it matters**: The provider is designed to be swappable. Hardcoded assumptions break the adapter pattern.
- **Prevention**: All provider interactions must go through the adapter interface. Provider-specific logic stays inside the adapter implementation.

## Missing Error Context
- **Mistake**: Returning generic error messages like "Something went wrong" to the user.
- **Why it matters**: The UX spec requires errors that explain what happened, why, and what to do next.
- **Prevention**: Every error response must include a user-facing explanation and a suggested next action.

---

## How to Add New Entries
When you identify a recurring mistake:
1. Add a new section with the pattern name as the heading.
2. Include **Mistake**, **Why it matters**, and **Prevention** fields.
3. Keep entries actionable and specific.
4. Reference the relevant doc or code area if helpful.
