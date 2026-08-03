# Docs Index

**Project:** AI Creative Studio

**Purpose**
This folder is the canonical documentation root for the MVP. It contains the product vision, UX definition, technical architecture, implementation sequencing, and the execution backlog.

**Current Doc Set Version:** 1.0
**Last Updated:** 2026-08-04
**Status:** Active MVP documentation

## Reading Order
If you are new to the project, read the docs in this sequence:
1. [PRD](prd.md)
2. [UX Spec](ux-spec.md)
3. [MVP Technical Spec](mvp-technical-spec.md)
4. [MVP Implementation Plan](implementation-plan.md)
5. [MVP Backlog](mvp-backlog.md)

That order moves from product intent, to experience design, to technical architecture, to delivery sequencing, and finally to sprint-ready work items.

## Document Map

### [PRD](prd.md)
**What it contains:** the product vision, goals, non-goals, target audience, core user journey, product principles, business model, risks, and success metrics.

**Use it for:** understanding what the product is, who it is for, and what the MVP must and must not include.

**Versioning note:** this document has an explicit version field in its header and should be updated when product scope or positioning changes.

### [UX Spec](ux-spec.md)
**What it contains:** the information architecture, guided workflow, key screens, loading and error states, mobile and desktop behavior, and interaction tone.

**Use it for:** building the experience so the product feels like a guided creative workflow instead of a generic AI tool.

**Versioning note:** treat this as a living design spec. Update the file date and keep the content aligned with the PRD when UX changes.

### [MVP Technical Spec](mvp-technical-spec.md)
**What it contains:** the selected stack, orchestration model, provider boundary, module structure, data model draft, API surface, workflow rules, and acceptance criteria.

**Use it for:** implementing the backend and frontend architecture without re-litigating the product decisions.

**Versioning note:** treat changes to architecture, contracts, workflow state, or storage as versioned decisions and update this file alongside implementation changes.

### [MVP Implementation Plan](implementation-plan.md)
**What it contains:** the phased delivery plan, grooming decisions, locked architecture calls, and sequencing for the MVP build.

**Use it for:** understanding what should be built first, what depends on what, and which stack choices are already settled.

**Versioning note:** keep this synchronized with the technical spec whenever architecture or sequencing changes.

### [MVP Backlog](mvp-backlog.md)
**What it contains:** the epic and story breakdown, story bodies, acceptance criteria, sprint split, and grooming standards.

**Use it for:** turning the MVP plan into execution-ready work items that can be picked up in sprint planning.

**Versioning note:** update this file whenever stories are split, reordered, or re-estimated.

## Canonical Artifact Rules
- `prd.md` is the source of truth for product vision and scope.
- `ux-spec.md` is the source of truth for the user experience.
- `mvp-technical-spec.md` is the source of truth for architecture and product/tech boundaries.
- `implementation-plan.md` is the source of truth for sequencing and architecture decisions.
- `mvp-backlog.md` is the source of truth for sprint-ready epics and stories.

## Update Discipline
- Update the relevant doc first when scope, UX, architecture, sequencing, or backlog priorities change.
- Keep cross references aligned across all docs.
- Prefer one source of truth per decision instead of duplicating the same decision in multiple places.
- Use the file headers and commit history for version tracking; use this index to understand the document set at a glance.

## Notes
- The old `_docs` folder was consolidated into `docs/`.
- The HTML wiki was not kept as a canonical artifact.
- This index should stay lightweight and should only describe the documentation set, not duplicate the full content of other files.
