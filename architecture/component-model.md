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

## Reuse decision

- **Reuse** when meaning, states and behavior already match.
- **Extend** when a small semantic variant keeps the contract testable.
- **Compose** when the requirement is a business workflow built from stable parts.
- **Keep app-local** for one-off or fast-changing domain logic.
- **Create shared** after demonstrated repeat use or clear cross-product leverage, with an owner and testable API.
- **Merge/deprecate** competing variants when they are equivalent; provide a migration path.

**Avoid:** `UniversalForm` with dozens of Boolean props and internal business APIs. Prefer shared field, label, error and layout controls composed into task-specific forms.

## Verification

Check existing catalog synonyms and imports before adding a duplicate. Record consumers, ownership, stable public API, token usage, accessibility states, migration impact and expected tests. Related: [component contracts](component-contracts.md), [lifecycle policy](../governance/lifecycle-and-decisions.md).

## Promotion and dependency checklist

Before promoting an app-local piece, identify at least two credible usage contexts **or** a strategic cross-product requirement; record consumers, semantic equivalence, lifecycle owner and migration cost. Similar appearance alone is not sufficient: a link and a button may share visual treatment but differ in meaning and behavior.

**Dependency rule:** foundations are consumed by primitives, components compose primitives, product patterns compose components. A higher-level workflow may pass data and callbacks into lower-level controls; lower-level controls must not import product API clients or route configuration.

| Request | Level / action | Rationale |
| --- | --- | --- |
| An inline text layout helper | Primitive, only if repeated | Owns layout/semantics, not fetch logic |
| A dialog with focus/close behavior | Shared component candidate | Reusable interaction contract |
| Delete-account confirmation | Product feature | Domain copy, authorization and mutation stay app-local |
| Slightly different button padding | Reuse/token or justified variant | Avoid a duplicate component |
| A one-off analytics panel | App-local first | Stabilize before promising a shared API |

**Promotion gate:** contract documented; keyboard and state expectations specified; token compatibility mapped; dependencies remain one-way; examples include content extremes; owner and version assigned. Status remains `proposed` until review; this guidance does not imply any code is already published.


## Batch 9 — incremental extraction from a concentrated page (proposed, 2026-11-07)

**Source trigger:** A product may have a large route file that owns navigation, request orchestration, modal routing and feature rendering while already containing separately maintained UI components. The Little Wins source has a large `app/page.tsx` with a single main `Home` component and an extracted `features/projects/components` boundary; its `components/ui` folder does **not** prove those controls are used everywhere. This is an architecture inspection, not measured evidence of a performance or accessibility defect.

**Adoption decision sequence:**
1. **Inventory before extracting:** list existing shared controls, feature components, duplicated app-local UI, CSS selectors and current consumers; distinguish installed template/library files from imported/used components. Capture representative task screenshots and interaction states only when the running app is available.
2. **Establish a behavioral baseline:** list critical flows, keyboard/focus, async states, breakpoints, themes, translations, domain commands and owner-scoped request behavior. Keep these as acceptance criteria for each extraction.
3. **Choose a vertical slice:** select one cohesive workflow or repeated control; leave product-specific validation, mutation commands and cross-feature decisions in the feature/domain layer. Keep native semantics and data ownership unchanged.
4. **Apply reuse/compose/keep-local:** use existing contracts for Button/Dialog/Input when semantics match; add a stable variant only for an evidenced difference. Do not force every branded card or task panel into the shared library.
5. **Migrate consumers gradually:** permit a temporary compatibility adapter with a named owner and removal condition; avoid simultaneous whole-app JSX/CSS rewrites. Preserve public component APIs, return-focus paths and data transitions. Track use and delete dead CSS/components only after verifying references.
6. **Retire duplicate implementations:** once both old and new paths are compared across task/locale/theme states, remove deprecated styles and wrappers with a rollback plan.

**Useful separation:** route/page orchestrates which group/project and screen is active; feature component owns task-specific form/review presentation; domain layer owns contribution, points and reward invariants; shared component owns generic focus, labels and input behavior. This is an example boundary, not a mandated framework architecture.

**Positive example:** move one contribution-review dialog to a feature module, reuse a shared Dialog shell and retain the existing command and validation behavior with keyboard and visual comparison evidence. **Anti-example:** replace every modal and table in one commit, change CSS global selectors and mutate domain commands while claiming the work is a visual-only refactor.

**Verification:** source import graph, public API consumers, feature route smoke paths, state transition fixture comparisons, keyboard and screen reader focus, mobile/zoom, locale growth, visual snapshots, bundle/layout effects if measured, and rollback rehearsal. Without an implemented baseline, mark runtime outcomes NOT VERIFIED. See [component contracts](component-contracts.md), [tokens](../foundations/design-tokens-and-themes.md), and [quality gates](../governance/quality-gates.md).

## B05 — component inventory to canonical contract mapping (CKG-17; proposed 2026-11-07)

**Purpose:** decide what to **reuse, compose, extend, keep local, create or retire** before a clean-slate visual implementation. The existing reuse model and incremental extraction sequence above remain authoritative; this section supplies a compact, evidence-led inventory worksheet. Similar names or appearances are not proof of interchangeable semantics.

### Inventory fields and evidence levels

For each observed component or repeated UI pattern, record:

| Inventory field | Evidence / decision required |
| --- | --- |
| Source identity | File and export path, known version, owning package/feature and tested consumer |
| Availability | Distinguish **installed**, **exported**, **imported**, **rendered/used**, and **documented only**; do not count all template files as active UI |
| Semantics and interaction | Native role; keyboard/focus behavior; names/labels; component event; async/error states |
| Visual and layout contract | Tokens, variants/sizes, light/dark/high-contrast, responsive composition, styling owner |
| Consumers and scope | Actual import graph, route/workflow, same semantics or merely similar geometry |
| Duplication risk | Equivalent behavior implemented twice, uncontrolled variants, near-identical status labels or conflicting focus handling |
| Decision | Reuse, compose, extend, keep-local, create, deprecate/remove or defer |
| Implementation/review gate | Owner, tests needed, compatibility, migration plan, rollout evidence and rollback |

### Reuse/compose/extend decision table

| What the evidence shows | Default disposition | Why |
| --- | --- | --- |
| Existing Button/Dialog/Input with matching semantics and reliable accessibility | **Reuse** canonical primitive | Avoid a second focus/keyboard implementation |
| Distinct feature data with shared surface and predictable slots | **Compose** existing primitives/patterns | Keep domain commands, permissions and text at feature level |
| One stable semantic difference needed by credible multiple consumers | **Extend** controlled variant/slot contract | Preserve small public API and state-test matrix |
| One task-specific layout or uncommon localized variation | **Keep local** with token-backed styling | Similar CSS alone does not justify a public component |
| Meaningful missing reusable behavior with no existing owner | **Create** a component *after* catalog lookup, contract and consumer proof | Prevent premature abstraction and megacomponents |
| Older competing implementation has mapped equivalent replacement and consumers migrated | **Deprecate/retire** with compatibility and reversal plan | Remove debt without breaking hidden consumers |
| No current backend, authorization, runtime or consumer evidence | **Defer** or document proposal | Avoid claiming a feature or action exists because a design mentions it |

**Example inventory, illustrative (not an audit of the target application):**

| Candidate | Observed evidence required | Decision hypothesis |
| --- | --- | --- |
| Save action with spinner | Existing shared Button supports pending and focus | Reuse Button + feature-owned `saving` state |
| Review decision bar | Several review-specific outcomes, notes and reconciliation | Compose buttons in feature; do not create `approve` prop on Button |
| Status label with icon | Shared status Badge plus consistent pending/approved semantics | Extend generic Badge only if cross-feature needs agree; see [icon semantics](../foundations/iconography-and-semantics.md) |
| Dashboard card and project list item | Both happen to have borders/padding | Keep task-owned unless content, event and layout contracts genuinely match |

### Mapping workflow and anti-patterns

1. **Search existing exports and aliases** via actual imports, public facades and canonical registry before inventing names. Include feature-local wrappers and unused installed packages as separate categories.
2. **Map behavior and state first:** distinguish navigation/link, action/button, form input, role-aware outcome and domain-specific orchestration. Do not equate CSS similarity with semantic equivalence.
3. **Classify scope:** theme token vs primitive vs composed pattern vs feature task vs page shell; document owner and consumers.
4. **Choose the smallest safe change** and identify any variants/slots needing a versioned contract. Avoid a `UniversalCard` or a `MegaDashboard` with dozens of Boolean switches.
5. **Test a vertical slice** for behavior, focus/keyboard, screen reader, pending/error, RTL, responsive, themes and integration correctness. Do not treat documentation or screenshot review as application QA.
6. **Record migration** for every rename/deprecation: old→new API, affected imports, transitional alias, test evidence, owner and removal trigger.

**Acceptance:** the inventory covers relevant *actual* consumers, each promoted component has a coherent reusable behavior and owner, and feature-specific authorization/network rules remain outside shared UI. No arbitrary component count or file-length threshold is a substitute for semantics.

**Verification status:** inventory of the real target app, duplicate usage counts, browser and AT checks, token and theme builds, import graph, promotion effects and human sign-off are **NOT VERIFIED** by this catalog-only documentation.

**Related:** [component contracts](component-contracts.md), [module boundaries](module-boundaries-and-developer-navigation.md), [styling recipes](../foundations/practical-ui-styling-recipes.md), [CI guardrails](architecture-enforcement-and-ci.md), [lifecycle policy](../governance/lifecycle-and-decisions.md). Motivating proposals: [Little Wins B03 component architecture](https://github.com/EVEI2YONE/Little_Wins/blob/main/docs/little-wins/ui-knowledge/batch-03-component-architecture.md).

## Visual catalog representation and feature reference boundary (Phase 1 proposal, 2026-11-08)

The existing foundations → primitives → components → patterns/features → pages hierarchy remains the authoritative **reuse decision model**. The visual catalog introduces a **second, orthogonal classification** for which concepts have executable website examples; it does **not** replace registry `layer` values or reclassify existing `experiences` entries. A knowledge item may have no runtime representation, one component example, or a composed pattern/feature example without changing its canonical ID.

**Canonical knowledge owner:** registry ID plus Markdown contract, with existing paths and `related` relationships retained. **Actual runtime example:** `site/src/implementations/`, optional and directly rendered by the future site. **Browse chrome:** `site/src/catalog-ui/`, not a normative component spec. **Feature reference specification:** `features/<slug>/spec.md` only after a reuse audit, with website implementation under `site/src/implementations/features/<slug>/`. Keep website app routing and scenario machinery separate from these examples.

A **pattern** states reusable interaction rules and compositions (e.g., sorting, form validation, save uncertainty). A **feature reference** demonstrates a bounded, multi-stage job using a coherent state machine, accessible composition and **synthetic adapter**—without application-specific identity, payments, permissions enforcement or persistence guarantees. A **product feature/page** supplies actual domain authority, API integrations, authorization and routing in the consumer application. Feature reference examples are not a reason to clone the complete normative guidance already owned by `patterns/account-and-settings-portal.md` or `patterns/agentic-actions-and-approvals.md`.

**Promotion checklist:** require a distinct multi-step user job; two credible reuse contexts or documented strategic need; concept/alias search; a bounded data/command interface; state, keyboard/focus and recovery contract; no real-product mutations; owner and evidence. Prefer **reuse/extend/compose** before assigning a new `feature.*` ID. Unimplemented candidates remain unregistered and must not advertise live previews. Use [feature reference navigation](../features/README.md), [authoring template](../templates/feature-reference-spec.md) and [Phase 1 evidence ledger](../docs/visual-catalog-refactor/07-phase-1-context-and-decisions.md).

**Dependency invariant:** tokens/primitives ← components ← composed patterns ← feature references, with domain integration only in consuming apps. A reference implementation must import lower-tier controls and fixtures, never a product API client, auth authority or private business state. Keep code/status evidence separate from concept lifecycle; a stable written guideline does not certify an implementation.


## Executable reference maintainability and composition contract

This section applies the existing reuse/extend/compose decision to **actual source-linked examples**. It does not create a parallel component taxonomy or require all reference patterns to be rewritten as package dependencies.

### Source organization and boundaries

| Layer | May own | Must not silently own | Change-review signal |
| --- | --- | --- | --- |
| Catalog renderer | Navigation, registry-derived routes, safe Markdown, preview isolation, source inspection | Implementation-specific domain rules, another canonical concept index | A change to a component must not require editing unrelated navigation chrome |
| Reference control | Semantic element, supported variants, focus/disabled behavior, state-specific markup, scoped styles | Product identity, API calls, persistence, authorization | Public options, events and invalid combinations remain documented/testable |
| Composed pattern | Interaction choreography, local form/collection state, validation presentation, focus recovery | Parallel implementations of all primitive semantics, real server outcome guarantees | Reuse existing contracts where compatible; explicitly document deliberate native control use |
| Feature reference | Multi-step task, view selection, status presentation, synthetic adapter boundary | Real data ownership, access policy or security assertions | Adapter outcome semantics remain inspectable and independently testable |
| Consuming application | Actual adapters, authorization, domain policies, storage and monitoring | Mutation of canonical guidance or unreviewed shared API | Explicit integration acceptance and version plan |

A reference can use native HTML without importing the corresponding catalog component's implementation. That is **not** proof of production component reuse. In particular, the present form, navigation and table patterns demonstrate compositions but do not share a packaged Button/Field runtime. Do not advertise a dependency graph that the code does not have.

### Readability and state ownership

1. Prefer named, single-purpose helpers for state transitions, validation and DOM rendering. Keep pure checks and display wiring independently inspectable; compressing a full workflow onto one line is not a quality goal.
2. Establish a single owner for each mutable state item. For asynchronous decisions, distinguish `idle`, `pending`, `confirmed`, `known failure` and `unknown outcome`; only the authoritative adapter can reconcile uncertainty.
3. Define inputs/outputs and failures for every reference entry point. Reject invalid options deliberately; document whether remounting resets state. Theme changes must preserve the existing task where feasible.
4. Prefer native semantics, explicit names and data-bound text construction over building HTML from untrusted strings. Review `innerHTML` boundaries; synthetic fixture content is not automatically safe to use for production input.
5. Use *semantic* tokens with per-example scoping. Extract shared styling only after identifying actual repetition with stable meaning across two references; avoid global selectors that leak into catalog navigation or other previews.
6. Use fixed deterministic fixtures and explicit pending/error/empty/denied/conflict states, with one reproducible scenario per material branch. A synthetic success announcement must not imply real persistence.
7. Keep reference source, scenario manifest, optional adapter, CSS and tests discoverable in one local subtree; generate inspector text from those same checked-in files rather than rewriting demonstration snippets.

### Change and extraction decision

| Situation | Default choice | Evidence needed to change default |
| --- | --- | --- |
| Two examples merely look alike | Keep scoped implementations | Shared behavior and lifecycle verified, not only identical CSS |
| Two examples share an event contract | Consider composed helper | Tests for keyboard, asynchronous errors, focus and event ownership in both consumers |
| A feature needs an app-specific API | Inject an adapter at the feature boundary | Explicit auth, idempotency and data minimization contract; no UI-only privilege check |
| A new token alias is suggested | Reuse existing semantic role | Demonstrated intent difference, light/dark/contrast mapping and migration compatibility |
| A general reference is proposed as a package | Keep it as source-linked reference | Two actual adopters, public API/version owner, tests, license and support policy |

### Review checklist and performance of maintenance

Record the source path, review commit, owner/reviewer, state coverage, imports and known duplication. Review one ordinary path and at least one error/unknown path before accepting a refactor. Require a source-parity build, syntax/unit tests and browser task test after changes. If actual developer comprehension is the claim, measure a developer lookup/change task rather than treating shorter code or passing CI as proof. Avoid inventing a fixed time-to-change threshold without a baseline.

**Observed baseline:** six controls, five patterns and one feature are registered as source-linked references. The source-level form example currently uses dense inline DOM and validation logic and deserves human readability review; that is an audit candidate, not a demonstrated defect in all twelve sources. Shared theme and token behavior is covered separately by [Design tokens and themes](../foundations/design-tokens-and-themes.md); implementation contract evidence is owned by [Component contracts](component-contracts.md), and module import rules are owned by [Module boundaries](module-boundaries-and-developer-navigation.md).

**Evidence state:** This contract is authored guidance. It does **not** mean that a named engineer has inspected all 12 sources, that duplicate styling was removed, or that any component package is production-ready.
