# infra

Local infrastructure for AI Creative Studio. Docker hosts only the data services; the app services (`apps/web`, `apps/api`, `apps/worker`) run locally in watch mode.

## Services (root `compose.yaml`)

| Service | Port | Notes |
| --- | --- | --- |
| postgres | 5432 | Primary database (`ugc` db, user/pass `ugc`/`ugc`) |
| redis | 6379 | Celery broker + cache |
| minio | 9000 (API), 9001 (console) | S3-compatible object storage |
| minio-init | — | Creates the `ugc-assets` bucket on startup |

## Usage

```sh
# start infra
docker compose up -d

# verify everything responds
scripts/smoke.sh

# stop infra (keep data volumes)
docker compose down

# stop and wipe data
docker compose down -v
```

## Env

- Root `.env.example` holds shared defaults. Copy to `.env` to override.
- Per-app examples: `apps/api/.env.example`, `apps/worker/.env.example`, `apps/web/.env.example`.
- Docker reads `POSTGRES_*`, `MINIO_*` from the root `.env`. App services read their own `.env`.

## MinIO console

Open http://localhost:9001, sign in with `MINIO_ROOT_USER` / `MINIO_ROOT_PASSWORD` (`ugc` / `ugcsecret` by default).
