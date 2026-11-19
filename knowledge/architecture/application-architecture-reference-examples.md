# Application architecture reference implementations and migrations

**Kind:** example · **Status:** proposed · **Primary layer:** cross-cutting · **Owner:** unassigned · **Review:** pending

## Context and applicability

The [architecture selection guide](application-architecture.md) defines four profiles; [module boundaries](module-boundaries-and-developer-navigation.md) owns import and code-sharing decisions; [architecture evolution](architecture-evolution.md) owns safe migrations; [framework-aware guidance](framework-aware-application-structure.md) protects router-specific files; and [enforcement](architecture-enforcement-and-ci.md) owns lint/graph/CI configuration. Those chapters contain isolated file-tree sketches and abstract rules, but not **complete developer-task examples** showing where code belongs before and after a change. This page provides three connected, small **illustrative TypeScript/React-oriented reference scenarios**, not production starter repositories or benchmarked results.

For an actual repository, first gather a pinned commit, installed framework and routing mode, user journeys, import/dependency graph, team ownership, existing tests, deployment boundaries, performance and accessibility requirements. Treat paths as examples rather than required naming.

## Choosing the right reference

| Verified situation | Use | First test before adopting |
| --- | --- | --- |
| One task, uncertain requirements, one owner | Reference A: prototype | Keep data and UI local; avoid an invented package/release burden |
| Several routes reuse stable interaction but not domain transactions | Reference B: modular MVP | Public entrypoint, feature ownership and focus/state preservation |
| Two real applications share domain or UI contracts | Reference C: enterprise | Multiple consumers, versioning, integration tests and rollback |
| Unknown framework/router or no source snapshot | Do **not** copy a tree | Inspect current source and [framework-aware structure](framework-aware-application-structure.md) |

**Authority boundary:** these are **synthetic reference architectures**, not deployable starters. The tables illustrate allowed responsibility; [module boundaries](module-boundaries-and-developer-navigation.md) owns import constraints, [component contracts](component-contracts.md) owns UI behavior and [architecture evolution](architecture-evolution.md) owns migration risks. Do not reuse example paths as actual repository evidence.

## Reference A: prototype — route-local workflow, minimal abstraction

**User task:** test whether people can create and rename a project. One screen, one engineer, uncertain requirements. No proven sharing.

```text
src/
 main.tsx
 screens/
 ProjectsScreen.tsx
 ProjectsScreen.test.tsx
 components/
 Button.tsx # use only if this is already a shared accessible control
 lib/
 project-storage.ts # app-local persistence adapter, not a domain package
 styles/
 base.css
```

A simple screen can own its form state and task feedback. The storage adapter persists records; it does not belong in a global `services/` directory just because it performs I/O. Test a named input, submission, pending/failure feedback and keyboard use. If browser-only local storage is used, show a clear prototype limitation; do not imply tenant isolation, multiuser synchronization, server authorization or backup.

**Allowed import:**
```ts
// screens/ProjectsScreen.tsx
import { saveProject } from "../lib/project-storage";
```

**Avoid:** `packages/domain-projects/`, `apps/web/` and a versioned design-system package before they have an actual consumer. **Promotion trigger:** a second durable workflow needs the same project invariant, or there is a repeated UI contract with compatible states. A few hundred lines of code is not itself such a trigger.

## Reference B: MVP → growing modular product — one project editor, multiple routes

**User task:** edit a project's name from a list and from its details page, using the same validation and error recovery. Before extraction, both pages duplicate the editor's domain rules and request handling.

**Before (illustrative duplication):**
```text
src/
 app/
 routes/
 ProjectListPage.tsx # validates + saves + renders form
 ProjectDetailsPage.tsx # repeats validation + save + form
 components/
 ProjectForm.tsx # unclear ownership and growing Boolean props
```

**After (feature ownership; adjust route placement to the actual router):**
```text
src/
 app/
 routes/
 ProjectListPage.tsx
 ProjectDetailsPage.tsx
 features/
 projects/
 components/
 ProjectEditor.tsx
 ProjectEditor.test.tsx
 api/
 update-project.ts
 model/
 validate-project-name.ts
 validate-project-name.test.ts
 index.ts # approved public API
 shared/
 ui/
 TextField.tsx # shared only if more than one context needs same contract
```

**One public entrypoint:**
```ts
// features/projects/index.ts
export { ProjectEditor } from "./components/ProjectEditor";
export { validateProjectName } from "./model/validate-project-name";
```

**A pure, feature-local validation rule:**
```ts
// features/projects/model/validate-project-name.ts
export function validateProjectName(value: string): string | null {
 const name = value.trim;
 if (!name) return "Enter a project name.";
 if (name.length > 80) return "Use 80 characters or fewer.";
 return null;
}
```

**Illustrative route consumer:**
```ts
// app/routes/ProjectDetailsPage.tsx
import { ProjectEditor } from "../../features/projects";
// ProjectDetailsPage handles route parameters and composition;
// ProjectEditor owns feature-level edit behavior.
```

This does **not** mean client-side validation replaces server-side authorization or data validation. The example is a placement contract; a real editor must handle accessible error descriptions, pending states, server errors, focus return, localization and successful persistence according to the product.

**Boundary decision:** `ProjectEditor` remains a feature component because it knows project semantics. `TextField` may become shared UI only if multiple unrelated features use its stable accessibility and visual states. Do not export every private file through `index.ts`.

**Incremental migration walk-through:**

1. Capture existing list/details URLs and behavior, form error states, unsaved draft policy, focus and a representative automated test.
2. Extract the pure name-validation function; update both routes to call it and compare test outcomes.
3. Extract `ProjectEditor` as a feature-owned workflow; keep route adapters thin and ensure both pages use the same public export.
4. Consolidate request orchestration only when the two consumers truly share retry, optimistic update and authorization expectations.
5. Run typecheck, feature tests, route integration, keyboard/screen-reader and locale/theme checks; record what was actually executed.
6. Remove obsolete duplicated functions/components after confirming imports and behavior; retain compatibility re-exports temporarily if needed.

**Example policy violations:** importing `specifications/experiences/projects/components/ProjectEditor` directly from a sibling feature, or importing project state into `shared/ui/TextField`. Those conflict with [module-boundary guidance](module-boundaries-and-developer-navigation.md). Use [enforcement recipes](architecture-enforcement-and-ci.md) to implement tests against the target's actual aliases.

## Reference C: enterprise / multi-application — share stable contracts, not entire screens

**User task:** customer and admin applications display project information and accept related commands, but their permissions, layouts and release cadence differ.

```text
apps/
 customer-web/
 src/
 app/ # framework-owned routes
 features/
 project-overview/
 admin-web/
 src/
 app/ # framework-owned routes
 features/
 project-moderation/
packages/
 design-system/
 src/
 ui/
 Dialog.tsx
 TextField.tsx
 tokens/
 domain-projects/
 src/
 project-id.ts
 project-name.ts
 index.ts
 platform/
 src/
 http/
tooling/
docs/
```

The shared domain package holds stable, platform-independent project types/rules with real consumers; **it does not grant permission**. The admin moderation approval action remains within admin-owned application/service code, with server-side authorization. The design-system package contains semantic controls and tokens, not an `AdminProjectApprovalDialog` that would leak business actions to the customer app.

**Approved dependency example:** `apps/admin-web → packages/domain-projects` and `apps/customer-web → packages/design-system`. **Disallowed:** `packages/design-system → apps/admin-web`; `packages/domain-projects → apps/customer-web/router`.

**Why not microfrontends by default?** A monorepo can host multiple app deployables without independent in-page microfrontend runtimes. Require evidenced independent runtime delivery needs before introducing runtime composition, duplicated dependencies, cross-team navigation integration and focus/session complexity. Read [enterprise topology choices](enterprise-and-multiapp.md).

**Migration approach:** identify one truly shared domain invariant and two real consuming apps; define public API, owner and version/compatibility contract; extract an adapter-backed package; migrate one consumer at a time; run cross-app contract, integration, and critical accessibility tests; retain rollback and supported-version policies.

## Acceptance experiment: detect the wrong owner before migration

A reference example becomes useful when it predicts *where a change belongs* and makes a wrong placement observable. Exercise all three example topologies with these **illustrative** assertions:

| Sample request | Correct owner | Incorrect placement to reject |
| --- | --- | --- |
| Add field-level validation and recovery in a project editor | Projects feature form, with reusable Field semantics | Shared Button contains project API or authorization |
| Change shared Dialog keyboard behavior | Generic Dialog contract and each consuming app's integration tests | Route-local CSS overrides focus handling per app |
| Restrict who can approve a payment | Backend/domain permission owner and feature representation | Published design-system component asserts authorization |
| Change a theme semantic alias | Token owner plus affected consumer snapshots | Direct feature hex overrides that silently break dark mode |

**Verification method:** make a reviewer list the exact file, responsible owner, expected tests, allowed import and forbidden import for each task *before* showing the suggested mapping. Log lookup time, incorrect owner choices, missing paths and stated uncertainty; only call a measured result "faster" when comparing representative attempts with a controlled baseline. Use the import-boundary checks in [architecture enforcement](architecture-enforcement-and-ci.md) and public-interface rules in [module boundaries](module-boundaries-and-developer-navigation.md).

### Negative contract fixture (source-level only)

| Simulated import edge | Expected | Why |
| --- | --- | --- |
| `app/routes/projects` → `features/projects` | ALLOW | Route composes feature entry |
| `features/projects` → `shared/ui/Dialog` | ALLOW | Feature consumes generic contract |
| `shared/ui/Dialog` → `features/projects/projectApi` | REJECT | Shared control must not own feature service |
| `features/settings` → `features/projects/ProjectForm` | REJECT | Sibling feature internals are private |

A source-level regression test can check that these fixture expectations and canonical references remain present. It **cannot** prove a live application's import graph follows them. For such proof, execute an actual project's lint/dependency graph and feature integration tests, and log the repo SHA, tool version, runtime and result.

## Task → file location exercises

| Requested change | Prototype | Modular MVP | Multi-application platform |
| --- | --- | --- | --- |
| Rename a project field | Local screen and storage adapter | `specifications/experiences/projects` model/editor | App feature plus shared domain rule only if both apps use it |
| Update focus ring on a reusable button | Existing `specifications/components/Button` | `shared/ui` and semantic tokens | `packages/design-system` with consumer checks |
| Fix authorization for moderation | Not assumed to exist | Owning feature plus trusted server-side service | Admin service/authorization boundary, never a generic UI package |
| Add a new project dashboard route | Framework route/screen | Framework route adapter + feature | Owning app's routes + optional packages |
| Add an import-boundary check | Usually not needed | Scoped lint/graph checks if observed coupling | Project/package graph constraints with owners and CI |

**Discoverability exercise:** give an engineer each task without the table, ask for the first directory/file they would inspect, measure actual lookup time, misplacement and confidence, and compare before/after for that team. Do not invent improvement percentages.

## Acceptance worksheet for a real migration

| Check | Target evidence | Docs-only status |
| --- | --- | --- |
| Architecture fit | Repo revision, actual framework/route rules, users and owned features | NOT VERIFIED |
| Code consolidation | Before/after duplicated implementations, stable semantics, affected consumers | NOT VERIFIED |
| Dependency health | Resolved graph, forbidden imports, cycles, positive/negative fixtures | NOT VERIFIED |
| UX safety | Keyboard/focus, errors, pending, drafts, deep links, zoom, locale and theme tests | NOT VERIFIED |
| Delivery | Build/integration/contract checks, rollout owner and rollback | NOT VERIFIED |
| Developer navigation | Repeated, task-based file-location exercise and observed outcome | NOT VERIFIED |

### Avoid claiming an implementation from this document

**Source relevance:** [Node.js package entry points](https://nodejs.org/api/packages.html#package-entry-points) defines supported public exports; [TypeScript project references](https://www.typescriptlang.org/docs/handbook/project-references.html) constrains compiler projects when that tooling is in use; [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) informs accessible shared component behavior. These are scoped platform references, not evidence that the listed folder trees work in a user's application.

The examples are **not runnable standalone applications**, and they have not been tested against a consuming app. An implementation review requires exact framework/router, consumers, build and keyboard/RTL/zoom/async results with explicit `NOT VERIFIED` for unrun checks. **A synthetic negative fixture is not a passing customer journey.**


All trees and code fragments are **illustrative**, deliberately small and not runnable standalone applications. They are reference decisions, not executable templates, validated benchmarks or published production packages. A real code migration must follow the installed framework rules and its security/data contracts. The canonical concept IDs and ownership decisions live in [selection](application-architecture.md), [module boundaries](module-boundaries-and-developer-navigation.md), [evolution](architecture-evolution.md), [enterprise choices](enterprise-and-multiapp.md) and [quality gates](../../governance/quality-gates.md).
