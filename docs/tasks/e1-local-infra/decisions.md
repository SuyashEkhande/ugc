# Decisions — e1-local-infra

## 2026-08-06 — Compose runs only data services; apps run locally

- **Context:** E1-S3 needed local Postgres/Redis/MinIO without forcing container parity on app dev.
- **Options considered:** full compose (apps + data); data-only compose.
- **Chosen option:** data-only `compose.yaml`; apps run locally in watch mode.
- **Reason:** matches the locked Grooming Round 6 decision and keeps the fast `uv`/`next dev` loop.

## 2026-08-06 — Bucket bootstrap via a one-shot init container

- **Context:** MinIO starts empty; the app expects a `ugc-assets` bucket.
- **Options considered:** manual `mc mb` step; entrypoint script in the minio image; one-shot `minio-init` compose service using `minio/mc`.
- **Chosen option:** one-shot `minio-init` service with `depends_on: minio: service_healthy`.
- **Reason:** automatic, idempotent (`--ignore-existing`), and mirrors the "migrations as explicit commands" rule without hidden container magic.

## 2026-08-06 — Smoke test ships as a script, runs where Docker exists

- **Context:** Docker is not installed on the current dev machine, so compose cannot be exercised here.
- **Options considered:** block the task on local verification; ship the smoke script and gate it in CI.
- **Chosen option:** ship `scripts/smoke.sh`, defer execution to the CI compose-smoke job (E8-S4).
- **Reason:** the script is the same artifact CI will run; local verification will happen on a machine with Docker. The gap is tracked in the task skept notes rather than silently dropped.
