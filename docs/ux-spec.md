# UX Specification
## AI Creative Studio
Version 1.0

## UX Philosophy
The product should never feel like an AI tool. It should feel like hiring a creative strategist. Users should never think "How do I prompt this?" Instead they should think "This platform understands my business."

The experience should optimize for low cognitive load, guided workflows, clear progress, fast decisions, and confidence before generation.

## UX Principles
1. Guide instead of asking. Avoid empty text boxes; ask contextual questions.
2. One major action per screen. Avoid dashboards full of cards and metrics.
3. Always explain recommendations. Every AI suggestion should answer "Why?"
4. Generate only after confidence. Show users what they are about to receive before spending GPU resources.
5. Every interaction should reduce work. Never increase it.

## Product Navigation
Sidebar: Home, Creative Projects, Creative Vault, Brand Brain, Settings. The navigation should remain intentionally small and everything should be reachable within one or two clicks.

## Information Architecture
Workspace:
- Home
- Creative Projects -> Project -> Interview, Research, Creative Plan, Generated Videos, Publishing
- Creative Vault -> Inspirations, Saved Hooks, Saved Concepts, References
- Brand Brain -> Brand, Products, Audience, Competitors, Assets
- Settings

## First Time User Experience
1. Landing page with primary CTA: Create Brand
2. Authentication: Google, Email, GitHub
3. Welcome: small explanation and estimated setup time of 5-7 minutes
4. Build Brand Brain with progress indicator: Brand, Products, Audience, Competitors, Assets, Done
5. Success screen: AI now understands your business. CTA: Create First Project

## Home
Purpose: quick access. Contains recent projects, continue project, import inspiration, create project, and recently generated videos. No analytics, charts, or clutter.

## Creative Projects
This becomes the heart of the application. Each project card shows title, status, created date, last edited, generated videos, publish status, and a Continue action.

Projects support create, duplicate, archive, and delete.

## Create Project Flow
Create Project -> AI Interview -> Research -> Creative Plan -> Generate -> Publish

Never expose unnecessary settings upfront.

## AI Interview
Treat the interview like interactive onboarding rather than ChatGPT. Ask a question, get an answer, and adapt the next question. Questions should feel conversational and never exceed 6-8 in the first pass.

## Research Phase
The user should never feel like the system is loading. Narrate the thinking process using messages like understanding your business, researching competitors, finding successful UGC patterns, identifying customer psychology, planning creative direction, and preparing video concepts. Avoid spinners; use animated progress and estimated remaining time.

## Creative Plan Screen
The most important screen. Layout should include Objective, Audience, Creative Angle, Hook, Style, Story, Scene Breakdown, Reference Inspirations, Confidence Score, Edit, and Generate. It should feel like reviewing work from a creative agency, not AI.

## Video Generation
After approval, display progress messages such as Preparing Scripts, Generating Storyboards, Creating Reference Frames, Generating Videos, and Rendering Final Assets. Users should always know what is happening.

## Generated Videos
Card layout: Thumbnail, Variation Name, Hook, Length, Aspect Ratio, Preview, Publish, Download, Regenerate. Batch generated videos should appear together.

## Publish Experience
Primary CTA: Publish. Secondary CTA: Download. Publishing should support Instagram, TikTok, Facebook, and YouTube Shorts. If not connected, prompt connection. Never force downloads.

## Inspiration Import Flow
Entry points: Mobile Share, Link Paste, Upload.
Processing: Receiving Video -> Analyzing Structure -> Extracting Creative Pattern -> Matching Brand -> Generating New Concept -> Ready.
The UX language should always say Inspired by or Adapted from, never Clone.

## Creative Vault
Grid layout where each item displays Preview, Hook, Tags, Date, Source, Saved From. Supports Search, Filters, Collections, and Favorites.

## Brand Brain
Sections: Brand, Products, Audience, Competitors, Assets, Voice, Guidelines. Every section is editable and versioned.

## Empty States
- Home: No creative projects yet. CTA: Create Project
- Vault: No inspirations saved. CTA: Import Inspiration
- Projects: Your creative workspace starts here. CTA: New Project
- Videos: No videos generated yet. CTA: Generate First Video

## Loading States
Avoid spinners. Narrate AI thinking with messages like researching, understanding audience, planning hooks, choosing styles, building storyboard, and generating scenes.

## Error States
Errors should explain what happened, why, and what next. Example: We couldn't generate this variation. Try changing the hook or regenerate using another style.

## Notifications
Keep notifications minimal: Project Generated, Publishing Complete, Publishing Failed, Brand Brain Updated, Credits Low. No promotional notifications.

## Mobile Experience
Mobile is primarily for inspiration capture. Capabilities: share, preview, approve, generate, publish. Editing remains desktop-first.

## Desktop Experience
Desktop is the primary workspace. It supports projects, generation, publishing, brand management, and vault.

## Design Language
Minimal, modern, professional. Avoid AI aesthetics and robotic language. The design should resemble Linear, Notion, Vercel, and Raycast with clean spacing, large typography, minimal colors, and heavy emphasis on whitespace.

## Voice & Tone
Never say prompt. Use describe, explain, tell us, share, guide, plan, recommend, create. Never expose technical AI terminology. Users should not care which model generated their video.

## UX Success Metrics
Success is achieved when users can complete Brand Brain in under 10 minutes, create a new Creative Project in under 2 minutes, reach a Creative Plan with fewer than 8 questions, generate videos with a single approval step, and publish directly without leaving the platform.

Every screen should answer one question: How do we help the user reach production-ready videos with the least possible effort? If a screen, interaction, or setting does not contribute to that goal, it should be removed or postponed to a future version.
