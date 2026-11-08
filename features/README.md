# Feature reference specifications

**Purpose:** define catalog-owned, reusable **reference experiences** that compose existing canonical controls and interaction patterns. This directory holds specifications and safe integration boundaries, **not** production application logic, deployed services or publishable packages.

**Status:** taxonomy approved for proposal within Phase 1; feature entry candidates remain **unregistered and unreviewed** until their own reuse/discovery audit and canonical specification exist. No feature implementation, live preview, or user-validation outcome is claimed by this README.

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

## Proposed feature candidates (NOT registered)

- **Review workspace:** inspect queue item evidence, choose approve/return/reject, handle uncertain outcome and restore focus. Refer to `patterns/agentic-actions-and-approvals.md` for *agent-initiated* consequential approvals, and `patterns/interaction-states-and-recovery.md` for generic outcome semantics. The human administrative review domain is not equivalent to AI-agent approvals.
- **Data workspace:** searchable/filterable records, paging, detail view and bounded bulk actions; extend `patterns/data-tables.md` and `patterns/search-and-filter.md`.
- **Settings center:** executable subset of `patterns/account-and-settings-portal.md`; do **not** duplicate its extensive normative settings lifecycle and section guidance.
- **Onboarding journey:** configurable progress, recovery and draft steps; reuse `patterns/task-flows-and-information-architecture.md` and forms/recovery contracts.
- **Analytics overview:** accessible representation of synthetic metrics; reuse `guidance/data-visualization-and-dashboards.md`; no real data accuracy claim.

**Decision:** Phase 1 does not register these IDs or create premature `spec.md` placeholders. Phase 7 starts with the first end-to-end audited reference concept; expansions require separate substantiation.

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
