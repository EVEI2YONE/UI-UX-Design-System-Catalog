# 02 — Concepts and content expansion plan

## Purpose

Identify *new visualized assets and feature-level reference contracts* without reporting mature design guidance as absent. The reviewed catalog already contains extensive principles, core control contracts, data tables, forms, navigation, performance, accessibility and research guidance. The primary addition is **executable evidence and representative compositions**, not another encyclopedia.

## Content taxonomy and scope

| Tier | Catalog owner | Website content | Promotion trigger |
| --- | --- | --- | --- |
| Foundations | `foundations/` | Token/theme/typography demonstration | Reusable roles, readable and tested examples |
| Primitives | `architecture/component-model.md` plus future specs if justified | Stack/Container/Text implementations | Repeated stable layout need |
| Controls | `components/*/spec.md` | Real Button/Input/Select/Checkbox/Dialog/Field state previews | Clear contract, semantics, testable behavior |
| Patterns | `patterns/*.md` | Working composed scenarios | Cross-feature recurrence, no product services |
| Feature references | new `features/*/spec.md` | Multi-step reference flows and adapters | Specific reusable job with credible reuse |
| Product pages | consuming app | Optional case study only | Never promote product-specific permissions or domain logic |

## Stage 1 — highest-value demonstrations

| ID / linkage | Existing guidance | Reference implementation | Acceptance |
| --- | --- | --- | --- |
| `component.button` | `components/button/spec.md` | Variants, pending, disabled reasoning, icons, focus | Native action semantics; no duplicate activation |
| `component.input` / `component.field` | existing specs | Labels, help, inline validation, long text, focus | Programmatic association and error recovery |
| `component.dialog` | existing spec | Confirmation, unsaved edits, async close, return focus | Escape, modality and restored focus tested |
| `pattern.forms` | `patterns/forms.md` | Small validated async form with retry and save-uncertain scenario | No false success, values preserved |
| `pattern.navigation` | `patterns/navigation.md` | Mobile and desktop labeled nav | Keyboard, active page, reflow |
| `pattern.interaction-recovery` | existing guidance | Pending/unknown result, read-only verify then proceed | Safe failure state and status announcement |
| `foundation.design-tokens` | existing guidance | Token/theme playground | Legible light/high-contrast; no raw divergence |

## Stage 2 — richer compositions

| Candidate | Reuse case | Already related | Guardrail |
| --- | --- | --- | --- |
| Search/filter collection | Customer records, inventory, admin lists | `pattern.search-filter`, `pattern.data-tables` | Preserved query state, pagination, empty/no-result distinction |
| Responsive information dashboard | Read-only analytics overview | `guidance.data-visualization` | Numerical meaning shown in text, no deceptive metrics |
| Feedback center | Inline errors, banners, confirmations, toast routing | `pattern.feedback`, `pattern.interaction-recovery` | No important announcement accessible only briefly |
| Workspace navigation shell | Multi-area productivity products | `pattern.navigation`, role-aware workspace guidance | Context, focus and permissions stay explicit |
| Onboarding composition | Step forms with save-and-resume | task-flows, forms, recovery | Do not imply persistence when mock-only |

## Stage 3 — feature-complete reference candidates

### F-01: Review and approval workspace (first feature candidate)

**New knowledge entry only if missing after registry search:** `feature.review-workspace`, under `features/review-workspace/spec.md`. Link rather than replace `pattern.agentic-actions`, `pattern.interaction-recovery`, `pattern.data-tables`, `architecture.component-contracts`.

**Reference implementation:** collection -> detail evidence -> reason capture -> approve/return/reject -> pending -> server-like verification -> advance/restore focus. Fake adapters must support loaded, empty, failure, uncertain outcome, permission-denied, stale revision and long-item scenarios. **Not included:** real auth, ledger, points or backend mutation guarantees.

**Why first:** exercises composition, state orchestration, explicit outcome confidence, responsive details, and agent discovery. It is also structurally relevant to Little Wins while remaining domain-agnostic.

### F-02: Data management workspace

**Candidate ID:** `feature.data-workspace`. Search, filter, sort, pagination, row details, selection and scoped bulk actions using synthetic data. Link `pattern.data-tables`, search/filter and advanced interactions. Avoid prematurely implementing spreadsheet/grid keyboard models.

### F-03: Settings center

**Candidate ID:** `feature.settings-center`. Preference categories, save/dirty indicators, conflict resolution, asynchronous persistence and safe exit. Link existing account/settings, offline/conflict, forms and privacy guidance. Security settings and account deletion are specialist variants and require separate authorization boundaries.

### F-04: Onboarding workflow

**Candidate ID:** `feature.onboarding-flow`. Configurable stages, validation, progress, back/cancel/restart and optional simulated resume. Avoid claiming storage or identity guarantees from the preview.

### F-05: Analytics overview

**Candidate ID:** `feature.analytics-overview`. KPI cards, accessible charts/tables, time filter and full numerical context. Data correctness, uncertainty and sampling rules must be documented.

## What should NOT be added yet

- An alternative Button, Dialog or Field primitive when existing specs already own the semantics.
- Product-specific `LittleWinsReviewWorkflow`, points ledger, redemption calculation, or server-authentication implementation.
- Multiple competing themes or unlimited ungoverned variants.
- Custom rich grids, drag-only rearrangement or animation-heavy widgets solely to make the catalog look impressive.
- Installable npm packages, framework adapters, a theme marketplace or backend-driven site CMS before proven need.

## Content contract for each new feature specification

1. Canonical ID; task; audience; non-goals; reuse evidence and links to existing pattern IDs.
2. Information architecture; steps; entry/exit; empty/loading/error/permission/conflict/unknown states.
3. Presentation composition and permissible variants; responsive and density behavior; readability.
4. Adapter interface with synthetic scenario matrix and server boundary.
5. Keyboard/focus/AT semantics; zoom, high contrast, reduced motion; locale/RTL decision.
6. Performance expectations (large data, lazy load, layout stability), verification method and baseline availability.
7. Preview ID; implementation source location; fixtures; tests; lifecycle status and owner.

## Definition of sufficient catalog coverage

Prefer *one canonical control*, *one composed pattern per reusable task*, and *one representative feature reference per independently reusable job*. Count quality and demonstrated applicability, not the number of cards or folders. Expansion requires a justified gap, named reviewer and a way to validate its runtime behavior.

## Durable disposition follow-up (2026-11-08)

This document preserves the **original proposal context**. Each Stage 2 composition and Stage 3 feature now has a durable cross-linked record in [the concept inventory and decisions](17-concept-inventory-and-decisions.md), with [machine-checkable manifest](concepts/decision-manifest.json), non-duplication reasoning, an original F/C ID, explicit disposition and promotion requirements. Only F-01 is registered; the remaining F-02–F-05 concepts and Stage 2 ideas are not newly minted canonical IDs. No record implies review approval or adoption.
