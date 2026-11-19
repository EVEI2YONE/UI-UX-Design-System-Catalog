# Application module boundaries and developer navigation

**Kind:** guideline · **Status:** proposed · **Owner:** unassigned · **Review:** pending

## Purpose and use boundary

Use module boundaries where distinct features must evolve without importing private implementation or duplicating stable interaction contracts. Start with the smallest ownership structure that makes a real task easy to locate. Do not treat directories, frameworks or import graphs alone as proof of user success.

### Checkable module example — illustrative

```text
app/routes/projects.tsx              # route composition
features/projects/index.ts           # feature public entry point
features/projects/ProjectForm.tsx    # submission and input composition
features/projects/projectApi.ts      # feature service adapter
shared/ui/Dialog/                    # accessible generic overlay
shared/ui/Field/                     # label, help and error composition
domain/project/validation.ts         # only if shared by several feature contexts
```

A route imports a feature's public entry point; the feature imports shared UI and stable domain contracts. Shared UI must not import the project service adapter; a settings feature must not deep-import the project form. Adapt file names to the chosen framework.

**Developer task-location exercise:** Give a developer unfamiliar with the codebase four changes: field help text, a permission invariant, failed-save retry and a theme token. Ask them to identify the owning file and relevant tests. Record time and incorrect locations as actual observations, not assumed benchmarks.

**Sources and limitations:** [TypeScript project references](https://www.typescriptlang.org/docs/handbook/project-references.html) document compiler project boundaries for TypeScript monorepos, not a mandatory folder scheme. [Node.js package exports](https://nodejs.org/api/packages.html#package-entry-points) documents public Node package entry points, not product layering. Use a repo-appropriate import enforcement tool and validate actual paths.

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

**Example:** `specifications/experiences/projects/index.ts` exports `ProjectsPage` and a stable query hook only when an external consumer genuinely needs it. `specifications/experiences/projects/components/EditProjectDialog.tsx` remains private. `shared/ui/Dialog` owns accessible focus behavior; project validation and save/retry belong in the projects feature/domain.

**Anti-example:** `shared/lib/helpers.ts` imports `specifications/experiences/projects/api`, and a settings feature deep-imports a project modal, making changes propagate unpredictably.

## Promoting reuse without creating a dumping ground

Use the following sequence: (1) identify true repeating behavior and consumers, (2) check semantic/state equivalence, (3) keep volatile app-specific work local, (4) promote a small stable contract, (5) migrate verified consumers, (6) delete obsolete paths only after import and regression checks. Similar JSX is not sufficient to imply the same accessibility semantics or business contract.

Prefer composition and injected callbacks over wide configuration surfaces with many interacting booleans. Share form controls, not a universal form with all domain workflows. Keep utilities named by responsibility; avoid miscellaneous `common/` or `utils/` directories that have no owner.

## Developer discoverability contract

A developer given a user-facing task should be able to move from product vocabulary → route/screen → owning feature → relevant component/API/model/test without searching unrelated folders. Name folders after stable user-facing concepts. Keep tests/stories/styles close to the code when possible. Maintain a short README only for non-obvious module contracts, conventions or integration points. Provide one clear public API, rather than multiple barrel chains that hide dependency direction.

Evaluate with a small task lookup exercise: ask a developer unfamiliar with the feature where they would implement a form change, permission check, API retry and token change. Record lookup time and incorrect placements as baseline observations, not universal benchmarks.

## Enforcement and acceptance

Document allowed imports and owners, then implement boundary lint rules, dependency graph cycle checks and module contract tests in the target's existing tooling. Avoid imposing a specific lint plugin without framework/toolchain assessment. Confirm that route deep links, state/error/loading and keyboard/focus/RTL flows survive extraction. Capture before/after import graph, search-to-edit path and duplicate-code reduction. See [selection](application-architecture.md), [component hierarchy](component-model.md), and [quality gates](../../governance/quality-gates.md).

**Scope:** reusable guidance only; no app has been refactored or tested.
