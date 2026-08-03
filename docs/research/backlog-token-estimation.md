# Backlog Implementation Token Estimation

## Executive Summary
This document provides a token budget estimation for building the complete MVP backlog of **AI Creative Studio** (8 Epics, 30 Stories across a Next.js frontend, FastAPI backend, Celery worker, OpenAPI contracts package, and shared API client).

It accounts for initial spec prompting, code generation, refactoring, test writing, lint/type checks, and the feature skepting cycle required by `AGENTS.md`.

---

## 1. Project Codebase Scale Estimation

Based on the architecture defined in [mvp-technical-spec.md](../mvp-technical-spec.md) and [implementation-plan.md](../implementation-plan.md):

| Component | Target Stack | Estimated Lines of Code (LOC) | Estimated Tokens in Code |
|---|---|---|---|
| **`apps/api`** | FastAPI, SQLAlchemy 2.0, Pydantic v2, Alembic, Service layer | 5,000 – 7,000 | ~150,000 |
| **`apps/worker`** | Celery, Redis, Task handlers, Provider adapters | 2,000 – 3,000 | ~60,000 |
| **`apps/web`** | Next.js 14/15, Vanilla CSS, React State/Hooks, App Router | 6,000 – 9,000 | ~180,000 |
| **`packages/contracts`** | Generated TypeScript types & OpenAPI schemas | 1,000 – 1,500 | ~30,000 |
| **`packages/api-client`** | Auth-aware fetch transport, request helpers | 800 – 1,200 | ~25,000 |
| **`infra` & Tests** | Docker Compose, Pytest, Playwright, CI workflows | 1,500 – 2,500 | ~45,000 |
| **Total Target Codebase** | Monorepo Full Stack | **16,300 – 24,200 LOC** | **~490,000 Tokens** |

---

## 2. Token Lifecycle Breakdown Per Story

When an AI coding assistant (Cursor, Antigravity, Claude, DeepSeek) works on a story, each turn includes the active context window (system prompt + relevant files + schema definitions + conversation history).

### Average Cost Per Story (30 Stories Total):
1. **Context Payload per Request Turn**: ~25,000 – 45,000 tokens (reading 2–5 existing files, schemas, and instructions).
2. **Output Payload per Request Turn**: ~1,500 – 3,500 tokens (generated code, diffs, explanations).
3. **Turn Breakdown per Story**:
   - **Phase 1: Spec & Design Prompting**: ~3 turns (~100k input / 6k output tokens).
   - **Phase 2: Core Implementation**: ~5 turns (~180k input / 12k output tokens).
   - **Phase 3: Testing, Linting & Type Checking**: ~3 turns (~100k input / 6k output tokens).
   - **Phase 4: Skepting & Plan Verification**: ~2 turns (~70k input / 4k output tokens).
   - **Story Total**: **~450,000 Input Tokens + ~28,000 Output Tokens = ~478,000 Total Tokens per Story**.

---

## 3. Total MVP Implementation Token Budget

| Category | Input Tokens | Output Tokens | Total Tokens |
|---|---|---|---|
| **Base Implementation (30 Stories)** | 13,500,000 | 840,000 | 14,340,000 |
| **Reiterations & Refactoring Buffer (+35%)** | 4,725,000 | 294,000 | 5,019,000 |
| **Bug Fixes, Schema Shifts & Integration Loops (+20%)** | 2,700,000 | 168,000 | 2,868,000 |
| **Standard Total Estimated Budget** | **20,925,000** | **1,302,000** | **~22,227,000 Tokens** |

---

## 4. Token Reduction with Developer Harness Tooling (`rtk` & `headroom`)

By integrating CLI/Context compression tools into the developer harness:
- **RTK (`rtk-ai/rtk`)**: Compresses terminal command outputs (git diffs, test suite logs, linter results) by **60% – 90%** by stripping boilerplate, ANSI codes, and log noise.
- **Headroom (`headroomlabs-ai/headroom`)**: Compresses file contexts and RAG chunks with reversible caching (Content Compression & Retrieval).

### Impact on Developer Token Budget:
- **Context Reduction**: Cuts terminal & file context payload from ~35,000 tokens/turn down to **~12,000 tokens/turn**.
- **Adjusted Total Token Budget with RTK/Headroom**: **~8.5 Million to 10 Million Tokens** (over **55% total token savings**!).
