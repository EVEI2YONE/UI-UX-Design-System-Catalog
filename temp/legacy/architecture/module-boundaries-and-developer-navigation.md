# Application module boundaries and developer navigation

**Kind:** guideline · **Status:** proposed · **Owner:** unassigned · **Review:** pending

## Context collected at batch start

Existing [component-model](component-model.md) defines the primitive/component/feature boundary, public contracts and incremental extraction. [Component contracts](component-contracts.md) document reusable UI behavior; [lifecycle](../governance/lifecycle-and-decisions.md) covers ownership. Missing at application level: feature vs domain ownership, imports and navigation by developer task. This page extends rather than duplicates component-specific requirements.

Before applying it to a target: record framework/routing, the most-changed user journeys, module imports, repeated behavior vs visual similarity, current file ownership, cross-team changes, testing infrastructure and meaningful examples of slow code lookup. Report unknowns.

## Single-owner module responsibilities

| Module | Owns | Should not own |
| --- | --- | --- |
| App composition | routes, providers, global layout, configuration wiring | duplicated feature business logic |
| Feature | complete user-facing workflow, local state, feature API adapter and contextual UI | arbitrary global primitives and unrelated features' internals |
| Domain (optional) | cross-feature business concepts, rules, validation invariants and domain types | page routing, generic buttons or feature-specific UI |
| Shared UI | stable accessible UI primitives and controls, token-backed styling | requests, business authorization, product analytics decisions |
| Shared infrastructure | generic transport, caching adapters, logging/error utilities | domain decisions disguised as universal helpers |
| Design system (optional separate ownership) | tokens/themes and published UI contracts | app-specific mutation workflows |

A feature often starts as three colocated files. Add components/api/model/hooks subdirectories when there is enough content to justify navigation.

## Dependency rules

- App composition may depend on features, domains and shared modules.
- Features may depend on shared UI/infrastructure and appropriate domain APIs; a feature should not deep-import a sibling feature's private files.
- Domains do not depend on UI, routing or presentation libraries.
- Shared libraries do not depend on feature/domain implementations. Generic interfaces may be implemented by higher layers through dependency inversion.
- Module public entrypoints are preferred for cross-boundary imports; internal relative imports remain fine within a module.
- When domain-to-domain relationships are required, identify a direction or explicit integration contract and reject dependency cycles.

**Example:** `features/projects/index.ts` exports `ProjectsPage` and a stable query hook only when an external consumer genuinely needs it. `features/projects/components/EditProjectDialog.tsx` remains private. `shared/ui/Dialog` owns accessible focus behavior; project validation and save/retry belong in the projects feature/domain.

**Anti-example:** `shared/lib/helpers.ts` imports `features/projects/api`, and a settings feature deep-imports a project modal, making changes propagate unpredictably.

## Promoting reuse without creating a dumping ground

Use the following sequence: (1) identify true repeating behavior and consumers, (2) check semantic/state equivalence, (3) keep volatile app-specific work local, (4) promote a small stable contract, (5) migrate verified consumers, (6) delete obsolete paths only after import and regression checks. Similar JSX is not sufficient to imply the same accessibility semantics or business contract.

Prefer composition and injected callbacks over wide configuration surfaces with many interacting booleans. Share form controls, not a universal form with all domain workflows. Keep utilities named by responsibility; avoid miscellaneous `common/` or `utils/` directories that have no owner.

## Developer discoverability contract

A developer given a user-facing task should be able to move from product vocabulary → route/screen → owning feature → relevant component/API/model/test without searching unrelated folders. Name folders after stable user-facing concepts. Keep tests/stories/styles close to the code when possible. Maintain a short README only for non-obvious module contracts, conventions or integration points. Provide one clear public API, rather than multiple barrel chains that hide dependency direction.

Evaluate with a small task lookup exercise: ask a developer unfamiliar with the feature where they would implement a form change, permission check, API retry and token change. Record lookup time and incorrect placements as baseline observations, not universal benchmarks.

## Enforcement and acceptance

Document allowed imports and owners, then implement boundary lint rules, dependency graph cycle checks and module contract tests in the target's existing tooling. Avoid imposing a specific lint plugin without framework/toolchain assessment. Confirm that route deep links, state/error/loading and keyboard/focus/RTL flows survive extraction. Capture before/after import graph, search-to-edit path and duplicate-code reduction. See [selection](application-architecture.md), [component hierarchy](component-model.md), and [quality gates](../governance/quality-gates.md).

**Scope:** reusable guidance only; no app has been refactored or tested.
