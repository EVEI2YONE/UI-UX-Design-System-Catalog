# Component model

**Kind:** guideline · **Status:** proposed · **Primary layer:** components

## Purpose

Preserve coherent, reusable interfaces without placing every app feature in one shared library. Reuse must improve maintenance and task quality, not merely reduce file counts.

| Level | Owns | Must not own | Examples |
| --- | --- | --- | --- |
| Foundations/tokens | Color intent, typography, spacing, motion | Product business state | `color.text.primary` |
| Primitives | Semantic layout and presentation building blocks | Requests/workflow orchestration | `Stack`, `Text` |
| Components | Stable presentation or interaction contracts | App-specific API calls | `Button`, `Select`, `Dialog` |
| Patterns/features | Composition, task logic, contextual validation | Reimplemented shared primitives | Search panel, account form |
| Pages/modal flows | Routes, user journey, page-level information architecture | Separate ad-hoc component system | Settings, onboarding |

## Reuse decision: one canonical route

Decide from **observed semantics and consumers**, not the number of files. This page owns *where reuse belongs*; [component contracts](component-contracts.md) own the API, focus and state contract, while [lifecycle](../../governance/lifecycle-and-decisions.md) owns versioning and retirement.

| Evidence about the requested UI | Decision | Minimum proof before sharing |
| --- | --- | --- |
| An existing component already expresses the same name, role, states and behavior | **Reuse** its public contract | Inspect actual rendered consumers, not merely installed/exported files |
| Several stable controls together satisfy a domain task | **Compose** a feature | Keep authorization, data mutations and business copy in the feature |
| One semantic variation is necessary for credible consumers | **Extend** a documented variant or slot | List supported/invalid states and compatibility implications |
| Only one changing product workflow needs it | **Keep app-local** | Record an owner and reconsider if new consumers genuinely emerge |
| No equivalent exists and stable cross-product demand is demonstrated | **Create shared** | Name owner, public API, a11y states, token dependencies and consumer tests |
| Two implementations are behaviorally equivalent, or the old one is unused | **Merge / deprecate** | Confirm import graph, migration window, fallback and removals after tests |

**Decision example:** A modal shell already supports appropriate focus entry, Escape behavior and focus return; reuse it. A "Delete account" dialog adds identity confirmation, permission checks and a transaction: compose those in the account feature. Similar geometry does **not** justify one giant `UniversalForm` with dozens of Boolean props.

**Publication gate:** document public name/role, supported states, keyboard/touch, event ownership, localization/RTL, theme/zoom, consuming contexts and release plan. A catalog Markdown page never proves a runtime component passes those checks. [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) provides pattern-specific keyboard/focus expectations; [React's UI breakdown guidance](https://react.dev/learn/thinking-in-react) is a React composition method, not an architecture mandate for every platform.

## Incremental extraction from a concentrated page

When a route mixes presentation, requests and task orchestration, **do not redesign every control at once**. Preserve representative journeys, state transitions and source revision first. The Little Wins `app/page.tsx` example is an *earlier source observation*, not a fresh repo audit or proof of a defect.

1. **Inventory** rendered and imported components, their owners, request boundaries, design tokens and duplicated semantics; distinguish `installed`, `exported`, `imported` and **observed rendered use**.
2. **Baseline** an actual user task across loading, success, validation failure, timeout, permission loss, keyboard/focus, narrow viewport and supported locale/theme. Record unrun states as **NOT VERIFIED**.
3. **Move one vertical slice**: route chooses screen; feature owns task state and service orchestration; domain owns validated invariants; shared UI owns stable accessible interaction. Use compatibility exports only with an owner and expiry condition.
4. **Compare** before/after task paths, imports, behavior, visual states and bundle/runtime data if collected. Do not infer faster task completion from fewer files.
5. **Roll back** on data loss, broken focus, unauthorized access, missing translation or failed consumer contracts; retire duplicates only after the consumers and replacement are verified.

**Illustrative migration:** extract a contribution-review Dialog's generic shell while keeping moderation rules and async commands in the feature. This example does not assert any application was migrated. For source-specific topology and dependency enforcement use [module boundaries](module-boundaries-and-developer-navigation.md) and [architecture evolution](architecture-evolution.md).

## Component inventory to canonical contract mapping

Before writing new UI, record one line per **observed** candidate and map it to exactly one disposition above.

| Inventory evidence | Record |
| --- | --- |
| Identity and availability | Canonical ID, package/export/file, version, owner; installed vs imported vs rendered consumers |
| Functional equivalence | Accessible role/name, keyboard and focus, events, pending/failed/unknown state, permissions boundary |
| Presentation compatibility | Supported variants, density, themes, tokens, zoom, translated content and RTL |
| Adoption risk | Actual consumers, forbidden imports, contract changes, deprecation alias and rollback |
| Decision | Reuse / compose / extend / app-local / create / retire, with a one-sentence rationale |

**Failure cases:** two visually identical controls with different keyboard behavior must **not** be merged; unused starter-library files do not count as application adoption; a feature component whose API takes an entire app service is not a generic primitive. If evidence is missing, choose **defer or keep local**, not "share by default."

**Acceptance exercise:** For an existing Button, Dialog and one feature form, trace route → feature → component contract and identify where a proposed permission fix belongs. Record incorrect owner placement, actual source paths, runnable consumer tests, theme/RTL and focus observations, and a reversion step. Catalog-only evaluation establishes the written decision paths; runtime results remain **NOT VERIFIED**.

## Knowledge-only concept boundaries

The foundations → primitives → components → patterns/experiences → pages hierarchy is a **decision and reuse taxonomy**, not a directory of installable UI code. Every registered item owns one canonical Markdown source, status, ID, use/avoid conditions, relations and verification limits. The documentation website displays those sources; it is not the runtime product whose interfaces the specifications describe.

| Concept tier | Guidance owns | Consuming application owns |
| --- | --- | --- |
| Foundation | Visual/semantic token intent, contrast and responsive principles | Resolved theme values and real platform rendering |
| Component | Semantic control purpose, states, focus and interaction rules | Framework implementation, public API, unit/AT tests, deployment |
| Pattern | Composition of controls, task context and recoverable outcomes | Product data flow, server validation, authorization and storage |
| Experience | Complete multi-stage task journey and cross-pattern tradeoffs | Product-specific roles, domain outcomes, persistence and routing |
| Documentation browser | Task search, canonical links and Markdown source discoverability | No business action or component library responsibility |

**Promotion checklist:** a new concept must justify a distinct reusable user decision, pass an alias/duplicate search, name credible use and avoid cases, document accessible behavior and failure recovery, and remain `proposed` until independent review. A feature/experience specification documents a bounded multi-step task rather than introducing runnable mock adapters. Reuse the [experience authoring template](../../templates/feature-reference-spec.md) and [experience index](../../specifications/experiences/README.md).

**Dependency invariant:** foundations inform component semantics; components inform pattern compositions; patterns inform multi-stage experiences. These are documentation relationships (`related` and `depends_on`), not actual JavaScript import graphs. No source file in this repository is a deployable implementation of Button, Form, Navigation or Review Workspace.

## Executable reference maintainability in consuming applications

This is **guidance for an independently maintained product codebase**, not an instruction to add executable references to this repository. Consumers can apply the following decisions while preserving the catalog as concepts-only:

1. **State ownership:** identify the one owner of editable, pending, confirmed, known-failure and unknown-outcome states; keep service authority distinct from local presentation.
2. **Semantic reuse:** adopt native behavior where suitable, and compose typed controls only when they meet the documented role, names, focus and keyboard requirements.
3. **Event contracts:** define inputs, outputs, cancellation, error and duplicate-activation policy without conflating a UI click with an authorized mutation.
4. **Token intent:** use semantic color, spacing, typography and focus roles, with actual light/dark/high-contrast and RTL verification in the consumer.
5. **Source exploration and quality:** keep the consumer's code and tests discoverable; verify one ordinary state and at least one failure/unknown path, using browser and assistive-technology tests where applicable.
6. **Service boundary:** authorization, persistence, concurrency, idempotency and private data remain app-specific. This knowledge catalog cannot certify them.
7. **Extraction decision:** only move consumer code into an owned shared library when actual reuse, compatibility, maintenance and testing justify it. That library must live **outside** this guidance repository.

| Consumer situation | Default decision | Evidence for a different choice |
| --- | --- | --- |
| Similar-looking controls with different behavior | Keep separate implementations | Verified common interaction and state contract |
| Shared focus/keyboard/event behavior across tasks | Compose around a stable contract | Tests in each actual consumer and assigned owner |
| App-specific API and permissions | Keep service adapter in app | Reviewed integration/authorization contract |
| Repeated styles or token roles | Reuse semantic design tokens | Theme/locale/contrast evidence and compatible migration |
| A general UI package is proposed | Do not add it here | Separate repository, lifecycle owner and real adopters |

**Evidence state:** these are design principles only. Code quality, runtime accessibility, product adoption and successful migrations are **NOT VERIFIED** by the existence of a canonical knowledge page.

## Source scope and quality boundary

[WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) informs accessible web widget behavior, but does not dictate package layering. [Node.js package entry points](https://nodejs.org/api/packages.html#package-entry-points) can enforce an exported Node package surface, while [TypeScript project references](https://www.typescriptlang.org/docs/handbook/project-references.html) apply to TypeScript compiler project boundaries. Neither source establishes product usability or mandates a framework. Record which is applicable in each migration. **Evidence status: proposed guidance; no real consumer verification is claimed.**
