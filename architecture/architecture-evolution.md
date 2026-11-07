# Application architecture evolution, refactoring and fitness

**Kind:** guideline · **Status:** proposed · **Owner:** unassigned · **Review:** pending

## Context and coverage at batch start

[Application selection](application-architecture.md) now outlines complexity-aware profiles; [module boundaries](module-boundaries-and-developer-navigation.md) defines ownership and imports. The existing [component model](component-model.md) already describes one-workflow-at-a-time UI extraction, and [quality gates](../governance/quality-gates.md) cover regressions and rollback. The remaining gap is a repeatable **application-wide transition and evidence** protocol. Reuse the existing checks rather than creating a conflicting release process.

Before recommending migration, capture the pinned repo version, framework/routing, affected user journeys and URLs, file/import graph, hot spots from actual change history, duplicate implementations, build and tests, teams and package ownership, deployment and rollback constraints. Mark missing telemetry or user research UNKNOWN.

## Architecture transitions: triggers, not file counts

| Transition | Evidence-based trigger | Guard against |
| --- | --- | --- |
| Prototype → MVP | repeated product journeys and independently understandable feature ownership | creating every potential domain folder in advance |
| MVP → modular product | cross-feature invariants, cycles, duplicate business operations or recurring edit conflicts | extracting a domain solely because it has a type/interface |
| Modular app → packages | stable consumers across apps, distinct ownership/testing or delivery needs | needless version coordination and package build costs |
| Monolith → independently delivered UI | proven autonomous deployments and integration contracts | distributed UX inconsistency, large runtime overhead and duplicated shared state |

An enterprise team can use an MVP-style tree if its product complexity remains low. A small team may need strict contracts when it handles sensitive data or a complex regulated domain.

## Migration playbook

1. **Baseline**: identify one high-value vertical user journey and capture entry, loading/empty/error/success, keyboard/focus, deep link, viewport, theme, locale, permissions and data contract.
2. **Dependency inventory**: list consumers of affected exports, styles, routes and state hooks; distinguish real usage from installed component-library files.
3. **Define target boundary**: decide keep-local, compose, reuse, promote, merge, remove or defer. State module owner and public interface.
4. **Extract one slice**: move presentation, feature request orchestration and optional domain invariants to their owners without changing behavior. Use temporary compatibility re-exports where needed.
5. **Verify**: import boundary, type/build/test, visual and keyboard/screen-reader behavior, network/error paths, mobile/reflow and locale/theme scenarios.
6. **Roll out and retire**: compare metrics and error monitoring where instrumented, document rollback, then remove dead exports, duplicate CSS and obsolete components after consumer checks.

Keep data/schema changes, UI extraction and visual redesign in separate reviewable steps unless an unavoidable dependency is documented.

## Architecture fitness indicators

Record a measured baseline, target context, evaluation cadence and owner. Do not impose arbitrary industry-wide thresholds.

| Indicator | Interpretation | Limitation |
| --- | --- | --- |
| Dependency cycles / forbidden imports | boundaries violated | a clean import graph does not prove usability |
| Cross-feature edit footprint | too many unrelated modules touched for routine change | shared platform updates legitimately have broad effects |
| Duplicate implementations | code consolidation opportunity | similar code may encode different behavior |
| Developer task-to-file lookup | discoverability and product vocabulary | results depend on experience and task sample |
| Module change coupling | independent ownership or test boundary problems | feature complexity and workload confound comparisons |
| Build/test duration and failures | packaging friction and feedback loop | environment and cache affect runs |
| Critical task completion/errors | whether the refactor protected UX | only meaningful with valid cohorts and baseline |
| Accessibility/locale/theme regressions | inclusive usability safety | static scans do not substitute for manual tests |

## Quality and rollback contract

Define owner, affected routes/consumers, tests executed (PASS/FAIL/NOT VERIFIED), new dependency graph, compatibility and deprecation plan, rollout mechanism, rollback trigger, and limitations. Capture user task success before optimizing the raw number of files. Critical safety/privacy, data-loss and accessibility failures override architectural tidiness. Follow [quality gates](../governance/quality-gates.md).

**Anti-example:** moving a thousand files, replacing all CSS, changing app state and approving every screenshot diff in a single commit. **Better:** one flow at a time, explicit integration evidence, staged retirement and an independently tested rollback.

## Evidence status

These are proposed migration practices, not proof a specific repo needs restructuring. Framework-specific recommendations require current official docs and actual source inspection.
