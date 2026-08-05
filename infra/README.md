# infra

Local infrastructure for AI Creative Studio.

- `compose.yaml` — Postgres, Redis, and MinIO services (added in task e1-local-infra).
- `.env.example` — shared environment variable examples.

Run the app services (`apps/web`, `apps/api`, `apps/worker`) locally in watch mode; Docker hosts only the data services.
