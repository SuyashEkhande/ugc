# MVP Technical Spec

## Product
AI Creative Studio is a guided, AI-native workflow for emerging D2C brands to turn brand context into approved UGC-style marketing videos without prompt engineering.

## MVP Goal
Ship the smallest usable end-to-end flow that lets a user:
1. Create a brand profile.
2. Create a project.
3. Complete a guided AI creative interview.
4. Run automated research.
5. Review a creative plan.
6. Approve generation.
7. Generate video variations with a selected video model provider.
8. Publish directly or export/download.

## MVP Non-Goals
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

## Target Users
- Founder
- Marketing manager
- Solo creator

## Key Product Principle
Strategy before generation. The system behaves like a creative strategist, not a prompting tool.

## System Overview
### Frontend
- Next.js app
- Primary responsibility: user experience, guided workflows, review surfaces, and state presentation
- Handles onboarding, projects, Brand Brain editing, creative review, generation status, publishing UI, and billing UI

### Backend
- FastAPI service
- Primary responsibility: business logic, workflow state, validation, persistence, credits, provider orchestration, and job execution
- Owns the source of truth for projects, brand data, interview state, research outputs, creative plans, and publishing jobs

### Orchestration Approach
- Keep the orchestration engine inside FastAPI for MVP
- Use explicit state transitions and background jobs for long-running work
- Use a simple ReAct-style agent only as a narrow helper for step-level LLM tasks, not as the product workflow engine

### AI Provider
- Video model provider is intentionally unresolved for MVP
- Used for generation only, not product logic
- Calls must go through backend provider adapters
- Provider selection stays swappable until a concrete provider is integrated

### Shared Contracts
- Request and response schemas
- Workflow states and enums
- Domain DTOs for projects, brand data, plans, generations, and publishing

## Core Modules
### 1. Brand Brain
Persistent brand context used to personalize all future work.

Required minimum fields for MVP:
- Brand name
- Website
- Product details
- Audience/persona
- Brand voice
- Logo/colors/assets
- Competitors

Stored data:
- Brand identity
- Products
- Audience details
- Competitors
- Brand assets
- Voice notes
- Guidelines

### 2. Projects
Each project represents one creative objective.

Project states:
- Draft
- Interviewing
- Researching
- Planning
- Awaiting approval
- Generating
- Ready
- Publishing
- Published
- Failed

Each project stores:
- Objective
- Audience
- Offer
- Messaging
- Creative plan
- Generated assets
- Publishing history
- Credit usage

### 3. AI Creative Interview
A guided, adaptive question flow that extracts structured creative context.

Requirements:
- Dynamic and context-aware
- Max 6 to 8 questions in the first pass
- Avoid empty text boxes where possible
- Questions feel conversational
- Output a structured creative brief

### 4. Research
Automated research based on:
- Public web research
- Uploaded inspiration assets
- User-provided links/files
- Connected social accounts

Research output:
- Competitor context
- Trend signals
- UGC pattern summary
- Audience insight summary
- Reference inspirations

### 5. Creative Plan
The trust-building review screen before generation.

Required sections:
- Objective
- Audience
- Creative angle
- Hook
- Style
- Story
- Scene breakdown
- Reference inspirations
- Confidence score

### 6. Generation
Generation uses a provider abstraction with the concrete video model provider selected through backend configuration when integrated.

Outputs required for MVP:
- Scripts
- Storyboards
- Reference frames
- Final rendered videos

Generation behavior:
- Multiple variations
- Different hooks/openings
- Multiple aspect ratios when possible
- Approval required before generation

Implementation note:
- Keep the video generation provider field empty in the initial system configuration
- The backend exposes a provider interface so the model can be added without changing product flow

### 7. Publishing
Publishing must support direct publish where possible and export fallback.

MVP targets:
- Instagram
- TikTok
- Facebook
- YouTube Shorts

If direct publish is unavailable, the user must still be able to download/export.

### 8. Billing and Credits
Credits are in scope for MVP.

Requirements:
- Track credit balance
- Deduct credits for generation and other billable operations
- Surface low-credit states clearly
- Block generation when credits are insufficient

## Recommended Architecture
### Frontend Responsibilities
- Authentication screens
- Brand onboarding flow
- Project creation flow
- Interview UX
- Research and creative plan review
- Generation status and asset gallery
- Publish/export actions
- Billing and credit views

### Backend Responsibilities
- Authentication/session integration
- Brand Brain persistence
- Project state machine
- Interview orchestration
- Research synthesis
- Creative plan generation
- Provider integration for the selected video generation backend
- Publish job orchestration
- Credit ledger and entitlement checks
- Signed URLs and asset metadata

### Storage
- Relational database for core domain records
- Object storage for uploaded assets and generated media
- Job/state table for asynchronous generation and publishing tasks

## Data Model Draft
### Brand
- id
- user_id
- name
- website
- voice
- audience
- competitors
- created_at
- updated_at

### Product
- id
- brand_id
- name
- description
- benefits
- price_point
- created_at
- updated_at

### Asset
- id
- brand_id
- type
- url
- source
- metadata
- created_at

### Project
- id
- brand_id
- title
- objective
- status
- created_at
- updated_at

### Interview
- id
- project_id
- questions_json
- answers_json
- brief_json
- created_at
- updated_at

### Research
- id
- project_id
- sources_json
- findings_json
- created_at
- updated_at

### CreativePlan
- id
- project_id
- plan_json
- confidence_score
- approved_at
- created_at
- updated_at

### VideoJob
- id
- project_id
- provider
- input_json
- output_json
- status
- created_at
- updated_at

### PublishJob
- id
- project_id
- target_platform
- status
- result_json
- created_at
- updated_at

### CreditLedgerEntry
- id
- user_id
- project_id
- amount
- reason
- created_at

## Key Workflow Rules
1. Brand Brain must exist before the first project can generate.
2. The interview must produce a structured brief before research planning.
3. Research must feed the creative plan.
4. The creative plan must be shown to the user before generation begins.
5. Generation cannot start without approval.
6. Publishing can only use finalized assets.
7. Credits must be checked before expensive actions.

## API Surface Draft
### Brand
- GET /brand
- POST /brand
- PATCH /brand

### Projects
- GET /projects
- POST /projects
- GET /projects/{id}
- PATCH /projects/{id}
- POST /projects/{id}/archive
- POST /projects/{id}/duplicate

### Interview
- POST /projects/{id}/interview/start
- POST /projects/{id}/interview/answer
- GET /projects/{id}/interview

### Research
- POST /projects/{id}/research/run
- GET /projects/{id}/research

### Creative Plan
- POST /projects/{id}/plan/generate
- POST /projects/{id}/plan/approve
- GET /projects/{id}/plan

### Generation
- POST /projects/{id}/generate
- GET /projects/{id}/generations

The generation endpoint routes through a backend provider interface and accepts a provider-agnostic request shape.

### Publishing
- POST /projects/{id}/publish
- GET /projects/{id}/publishing

### Credits
- GET /credits
- GET /credits/ledger

## Acceptance Criteria
- A new user can complete setup and create a project without leaving the guided flow.
- The system can generate a creative plan from the captured brand context.
- Generation is blocked until the user approves the plan.
- The user can publish to supported platforms or export/download.
- The UI clearly explains each AI recommendation.
- State survives refresh and remains visible in project detail views.

## Implementation Notes
- Keep the first release focused on one vertical slice rather than a broad platform.
- Prefer explicit workflow states over implicit UI assumptions.
- Treat the generation provider as an adapter behind backend service boundaries so the provider can be swapped without changing product flow.
- Keep inspiration analysis framed as extract-and-adapt, not clone-and-copy.
