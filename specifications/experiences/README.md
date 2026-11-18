# Feature reference specifications

**Purpose:** define catalog-owned, reusable **reference experiences** that compose existing canonical controls and interaction patterns. This directory holds specifications and safe integration boundaries, **not** production application logic, deployed services or publishable packages.

**Status:** feature-reference taxonomy proposed in Phase 1. **One canonical feature reference is now registered:** [Review Workspace](review-workspace/spec.md), with an executable *synthetic* preview and unreviewed design contract. Further candidate features remain unregistered. No product adoption, user-validation outcome or production integration is claimed.

## When a feature deserves its own entry

Create a `features/<slug>/spec.md` only when all of the following can be demonstrated:

1. A distinct **user job** and multi-step task experience requires composed state, not only one shared control or a single pattern.
2. The job can be reused in at least two credible product contexts or addresses a documented strategic cross-product requirement.
3. Existing `components/` and `patterns/` sources were searched, mapped and reused; no equivalent canonical feature entry already exists.
4. The reference can be shown with **synthetic data** and configurable adapters, without hard-coded product auth, points, money, identity or persistence rules.
5. Ownership, input/output events, error and unknown-result states, accessibility, localization, responsive behavior, performance and evidence can be specified.

When these criteria are not met, **extend an existing pattern** or keep the implementation local to a consuming application. If a candidate overlaps a large experience specification, such as `patterns/account-and-settings-portal.md`, use that page as canonical guidance and create only a clearly scoped executable reference contract if justified. A new reference entry must not rewrite or supplant the established contract.

## Separation of responsibilities

| Layer | Owns | Example | Does not own |
| --- | --- | --- | --- |
| Foundations | Semantic tokens, typography and motion guidance | `foundation.design-tokens` | Authorization, workflow state |
| Primitives | Simple semantic presentation and layout | `Stack`, `Text` examples if repeated | Requests or domain state |
| Components | Stable accessible controls | `component.button`, `component.dialog` | API calls or product-specific validation |
| Patterns | Reusable interaction decisions/compositions | `pattern.forms`, `pattern.data-tables` | Whole product business lifecycle |
| Feature references | Bounded multi-step sample jobs with simulated adapters | Candidate generic review workspace | Real backend/security enforcement |
| Application | Actual pages, identity, domain logic and persistence | Little Wins review task | Redefining canonical shared controls |

The registry `layer` values already classify *knowledge*, including `experiences`; they do **not** currently represent this one-to-one executable directory hierarchy. Preserve the metadata and existing IDs during Phase 1. Any additional representation mapping belongs to Phase 2.

## Feature concept records and registration distinction

- **Review workspace:** [registered canonical specification](review-workspace/spec.md) with a synthetic reference, still `proposed` and not human-approved; human administrative review differs from AI-agent approvals.
- **Data workspace:** [F-02 durable candidate brief](../docs/visual-catalog-refactor/concepts/f02-data-workspace.md) — deferred; existing table and search/filter owners retained.
- **Settings center:** [F-03 durable candidate brief](../docs/visual-catalog-refactor/concepts/f03-settings-center.md) — deferred; must not duplicate the canonical account/settings portal.
- **Onboarding journey:** [F-04 durable candidate brief](../docs/visual-catalog-refactor/concepts/f04-onboarding-flow.md) — deferred; reuse existing task-flow and recovery contracts.
- **Analytics overview:** [F-05 durable candidate brief](../docs/visual-catalog-refactor/concepts/f05-analytics-overview.md) — deferred; no real data accuracy claim.

**Decision history:** Phase 1 deferred feature registration. Phase 7 registered **only** `feature.review-workspace` (canonical status still `proposed`); the other four feature concepts and five Stage 2 compositions now have [individual, noncanonical briefs and an auditable decision ledger](../docs/visual-catalog-refactor/17-concept-inventory-and-decisions.md). They are **documented candidates, not registry entries or approved implementations**. Any promotion requires separate substantiation and named owner review.

## Entry authoring contract

Use [feature reference template](../templates/feature-reference-spec.md). The eventual `spec.md` must describe task boundaries, real source dependencies, stage/state map, semantics, adapters/fixtures, content and layout constraints, exceptional outcomes, applicable tests, ownership, status, source/evidence and reasons **not** to reuse the feature.

The actual JSX/TSX resides under `site/src/implementations/features/<slug>/`; any `site/src/catalog-ui/` code is presentation chrome for browsing, not the canonical reference implementation. The site should display the real source and use a deterministic preview adapter.

## Canonical sources

- [Component model](../architecture/component-model.md)
- [Component contracts](../architecture/component-contracts.md)
- [Module boundaries](../architecture/module-boundaries-and-developer-navigation.md)
- [Account/settings portal composition](../patterns/account-and-settings-portal.md)
- [Agentic approvals](../patterns/agentic-actions-and-approvals.md)
- [Catalog lifecycle policy](../governance/lifecycle-and-decisions.md)
- [Phase 1 discovery ledger](../docs/visual-catalog-refactor/07-phase-1-context-and-decisions.md)

## Phase 7 registered reference

- [Review Workspace](review-workspace/spec.md) — `feature.review-workspace`, a multi-step human review experience with synthetic adapter, inspection, decision reasons, read-only/denied/conflict/error/unknown outcomes and verification-safe handling. The actual implementation is [ReviewWorkspace.js](../site/src/implementations/features/review-workspace/ReviewWorkspace.js) and the separate in-memory source is [mock-adapter.js](../site/src/implementations/features/review-workspace/mock-adapter.js). See [Phase 7 evidence](../docs/visual-catalog-refactor/13-phase-7-review-workspace.md).

**Boundaries:** no real permissions, backend persistence, live product audit logs or customer data. A source-level preview is not evidence of production behavior or a certified accessible feature.
