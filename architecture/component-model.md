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
