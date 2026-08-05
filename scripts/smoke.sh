#!/usr/bin/env bash
# Smoke test for the local infra stack (compose.yaml).
# Starts Postgres, Redis, MinIO and verifies each responds.
# Requires Docker with compose support.

set -euo pipefail

cd "$(dirname "$0")/.."

echo "==> Starting infrastructure (postgres, redis, minio)"
docker compose up -d

wait_healthy() {
  local svc="$1"
  local tries="${2:-30}"
  for _ in $(seq 1 "$tries"); do
    status=$(docker compose ps --format json "$svc" 2>/dev/null | grep -o '"Health": *"[^"]*"' | head -1 | sed 's/.*"\(.*\)"/\1/')
    if [ "$status" = "healthy" ]; then
      return 0
    fi
    sleep 2
  done
  echo "FAIL: $svc did not become healthy" >&2
  return 1
}

echo "==> Waiting for services to become healthy"
wait_healthy postgres
wait_healthy redis
wait_healthy minio
wait_healthy minio-init

echo "==> Verifying connectivity"
docker compose exec -T postgres pg_isready -U "${POSTGRES_USER:-ugc}" -d "${POSTGRES_DB:-ugc}"
docker compose exec -T redis redis-cli ping
mc_health=$(docker compose exec -T minio curl -sf http://localhost:9000/minio/health/live || true)
if [ -z "$mc_health" ]; then
  echo "FAIL: minio health endpoint not responding" >&2
  exit 1
fi

echo "==> Smoke test PASSED"
