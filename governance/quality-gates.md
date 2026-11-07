# Design and catalog quality gates

**Kind:** checklist · **Status:** proposed · **Primary layer:** cross-cutting

Use `PASS`, `FAIL`, `NOT VERIFIED`, or `NOT APPLICABLE` per check and provide evidence, date, owner, and scope. Passing documentation validation **does not** imply component accessibility or user-journey success.

| Gate | Required evidence |
| --- | --- |
| User value | User job, context, success condition and assumptions |
| Reuse | Existing concept search, aliases, reuse/extend/create rationale |
| Architecture | Correct tier, stable API or concept boundaries, owner |
| Interaction | Relevant state matrix, async/error/recovery, focus and touch |
| Design | Hierarchy, signifiers, spacing, primary action and content growth |
| Styling/themes | Token roles, theme variants, scoped styling, responsive behavior |
| Accessibility | Semantic and keyboard expectations; manual and automated test log |
| Localization | Externalized copy, locale formats, translation growth, RTL disposition |
| UX measurement | Defined events, denominators, cohorts, missing baselines and privacy |
| Catalog integrity | Unique ID, canonical path, index/README links, status and version |
| Delivery | Actual validation output, PR review, compatibility and rollback notes |

## Documentation checks

```bash
python3 scripts/validate_catalog.py
```

This checks *document structure and lookup integrity only*. Example manual checks—keyboard, screen reader, reflow, contrast, RTL, light/dark, reduced motion—remain `NOT VERIFIED` until performed on an actual implementation.

## Priority and release decisions

P0 accessibility/safety/privacy/security/data-loss and critical regressions override the normal migration ranking. The user-impact order for product modernization is P1 core workflows, P2 IA/navigation, P3 minimal foundations/components, P4 onboarding/change management, P5 high-friction quick wins, P6 secondary experiences, P7 cosmetic polish. Engineering prerequisites may execute earlier than a higher-value product change. Do not invent usage frequency or test outcomes.

## Per-batch evidence record

For PRs that expand existing scaffold entries, reviewers should see a batch label, canonical paths touched, the design decisions added, known limitations, and check results. A useful definition includes an actionable rule, example/anti-example, a verification method and an identified owner or explicitly unassigned ownership. Avoid promoting entries solely because documentation validation passes.

| Check | Current documentation-only interpretation |
| --- | --- |
| Registry integrity | Existing stable IDs and paths remain unchanged unless intentionally migrated |
| Markdown navigation | Relative links and section/root index references resolve |
| Content completeness | Decisions, counterexamples, scenarios and limitations provided |
| Code a11y / RTL / runtime UX | NOT APPLICABLE to docs-only changes; downstream behavior NOT VERIFIED |
| Research baseline | UNKNOWN unless measured with documented cohort/denominator |

Record actual script output in the PR, and keep code/UX claims distinct from validation of Markdown files.

## Agent lookup and metadata acceptance

- **Registry:** one canonical ID and path per entry, complete typed metadata, valid references, no dependency cycles or dead local links.
- **Retrieval:** deterministic exact ID/alias priority; punctuation normalization, optional status/limit filtering, and no positive match solely from `avoid_when`.
- **Governance:** explicit ownership or `unassigned`, review date or `null`, documented source limitations and review evidence before lifecycle promotion.
- **Verification:** run `python3 scripts/validate_catalog.py` and `python3 -m unittest discover -s tests -v`; log actual outcomes. Runtime keyboard, a11y, RTL, theme and user testing are **NOT VERIFIED** by documentation tests.

## Batch 12 extension — product release evidence beyond documentation

The existing catalog checks remain necessary. A real UI release additionally needs **performance, controlled-experiment and design-to-code checks**. Do not mark any product row PASS simply because Markdown validation succeeded.

| Gate | Minimum implementation evidence | Blocker or owner |
| --- | --- | --- |
| Performance and resilience | Actual field Core Web Vitals where applicable, lab constrained-device regressions, server-confirmed task timing, retry/timeout/data-loss checks | Performance + product owner; critical regression |
| Experiment validity | Registered hypothesis, randomization unit, exposure, sample-ratio mismatch check, primary metric, guardrails, uncertainty interval and approved stopping plan | Analyst + product; biased assignment or privacy/accessibility harm |
| Design-to-code trace | Catalog ID, current spec revision, approved design reference, state/variant matrix, affected consumers and component version | Design + engineering; silently breaking a public API |
| Design tokens | Versioned DTCG-compatible source, resolved aliases, theme/brand/platform transforms, actual build import tests | Token owner; unresolved aliases or semantic drift |
| Visual regression | Reproducible OS/browser/font/viewport snapshots, approved diffs, long/RTL/disabled/error/theme scenarios | Reviewer; mass-updated baselines hiding defects |
| Accessibility and locale | Actual keyboard/screen-reader/touch/zoom, reduced-motion and supported-language/RTL testing | Accessibility owner; blocking task failure |
| Release and rollback | Named owner, affected consumers, rollout cohort, error monitoring, rollback path and feature-flag policy if applicable | Delivery owner; irreversible unreviewed rollout |

### Reviewable implementation evidence bundle

For each implementing PR, record: **canonical ID**, version/owner, linked contract and design decision, code target, dependencies, token transformation, state matrix, screenshot diff review, user/assistive tests, performance evidence, experiment outcomes when relevant, known defects, compatibility, stakeholder approvals, release and rollback plan.

**Good example (illustrative):** A dialog token change is checked on dark/high-contrast modes, English and translated long text, keyboard focus, screen reader and reproducible screenshot baselines. The release lists affected consumers and a revert path.

**Anti-example:** Accept every screenshot automatically after a refactor, call the change WCAG compliant, and omit keyboard or real-user evidence. Visual screenshots cannot validate semantics or task correctness.

**Sources, consulted 2026-11-07:** [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots) (rendering environment matters), [Storybook UI testing](https://storybook.js.org/docs/writing-tests/index) (stories, interaction and automated checks), [DTCG Format Module 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/) (W3C Community Group report, not W3C Recommendation), and [web.dev Web Vitals](https://web.dev/articles/vitals). These tools are **possible** implementation choices, not declared dependencies of this docs-only repository.


## Hosted collaborative product assurance — context-driven checks (2026-11-07)

Before this gate, gather: actual hosting trust boundary, public/raw endpoint exposure, authenticated subject contract, owner and tenant data model, command/state transitions, storage concurrency scheme, and domain tests. Little Wins, for example, documents Sites sign-in, an owner-derived D1 workspace, a revision-checked JSON aggregate and 11 domain tests; this **does not verify** a deployed identity boundary or browser behavior.

| Gate | Required scenario | Disposition without execution |
| --- | --- | --- |
| Trusted hosting identity | Test missing/forged identity headers and reachable direct-origin URLs; verify platform strips client-controlled identity claims | NOT VERIFIED |
| Object authorization | Cross-owner/group/project reference edits, revoked roles, unauthorized approval, unknown member IDs | NOT VERIFIED |
| Workflow integrity | Invalid state transitions, resubmission history, replay/double-click approval and reward redemption | NOT VERIFIED |
| Atomic value changes | Award+ledger, reservation+balance, reject+refund, concurrent reviewer attempts | NOT VERIFIED |
| Conflict recovery | Two tabs, compare-and-swap exhausted retries, lost network response, draft preservation and safe re-fetch | NOT VERIFIED |
| Privacy/recovery | Tenant cache boundaries, backup/restore procedure, export/retention, safe errors without sensitive data | NOT VERIFIED |
| Interaction/accessibility | Keyboard focus after modal decision, accessible table actions, failure announcements, 200–400% zoom, narrow screen, RTL | NOT VERIFIED |
| Delivery | Domain tests plus API integration, production-like build, browser E2E, deployment environment and rollback | NOT VERIFIED |

**Decision:** a passing domain unit suite supports only tested domain invariants. A protected Site audience is a deployment condition, not proof that a raw API is unreachable. Promote a finding to PASS only with named test, environment, result and evidence. Owner/security specialists retain authority over platform contracts; this catalog describes inspection criteria, not guaranteed Sites behavior.


## Batch 6 — data-lifecycle and migration acceptance (proposed, 2026-11-07)

Gather the existing schema and deployed persistence contract **before** filling the checklist. Distinguish (a) observed source, (b) documented product intention, (c) inferred risk and (d) tested behavior.

| Gate | Minimum evidence / failure scenario | Default |
| --- | --- | --- |
| Retention and ownership | Data types, controller/owner, subject, active/archive/delete semantics, authorized request process | NOT VERIFIED |
| Portability | Export scope, privacy redaction, accurate result status, schema/version, duplicate import behavior | NOT VERIFIED |
| Legacy migrations | Representative old fixtures, deterministic/idempotent mapping, stable IDs, history and totals preserved | NOT VERIFIED |
| Read-side effects | Confirm whether ostensibly read-only requests can persist migrations; test concurrency and failure recovery | NOT VERIFIED |
| Backup/restore | Snapshot source and schedule, restore drill, recovery limits, authorized operators and rollback | NOT VERIFIED |
| Aggregate contention | Two independent project writers, bounded compare-and-swap failures, large payloads and retry/refresh UX | NOT VERIFIED |
| Value history | Ledger/review integrity and correction trail through archive, restore, deletion, toggle and import | NOT VERIFIED |

Documentation review can PASS while these product gates remain NOT VERIFIED. Do not claim legal compliance or backups solely from database technology or a successful unit suite.


## Batch 7 — record-to-modal journey assurance (2026-11-07)

| Scenario | Evidence required | Untested status |
| --- | --- | --- |
| Row action semantics | Action is a named native link/button in semantic table; keyboard and screen-reader task path | NOT VERIFIED |
| Modal focus lifecycle | Actual initial focus, containment, Escape and close-button behavior, background inertness | NOT VERIFIED |
| Draft protection | Changed field -> cancel/backdrop/Escape -> explicit preservation/discard policy; verified restoration | NOT VERIFIED |
| Async completion and focus | Server-confirmed result, accessible status, return focus to valid trigger or safe fallback after row disappears | NOT VERIFIED |
| State/locale/responsive | Error/retry, disabled/busy, long labels, keyboard at narrow/zoom, RTL and supported AT/browser matrix | NOT VERIFIED |

Do not mark a product test PASS based solely on source review or on the presence of a prebuilt accessible component library. Prefer one integrated end-to-end evidence record for the full journey, supplemented by unit/component checks.


## Batch 8 — independent flags and dependent capabilities (2026-11-07)

| Test | Required evidence | Untested status |
| --- | --- | --- |
| Capability matrix | All meaningful flag combinations and action dependencies recorded, including direct server commands | NOT VERIFIED |
| Cross-layer agreement | Visible navigation, disabled controls, deep links and server enforcement agree; UI hidden state is not authorization | NOT VERIFIED |
| Pause and resume | Before/after snapshots of approved contributions, challenge history, balances, ledger entries and requests | NOT VERIFIED |
| Pending work | Configuration changed during form/edit/redeem/fulfill; safe rejection or completion with honest user-facing status | NOT VERIFIED |
| Orphaned tasks | Existing reward requests remain discoverable and actionable to authorized owners even when new redemption is disabled | NOT VERIFIED |
| Configuration persistence | Save, reload, concurrent admins/tabs, retry, default new workspace settings and rollback | NOT VERIFIED |
| Accessibility/locale | Clear paused versus no-data messaging, keyboard reachability, screen-reader status and long translations | NOT VERIFIED |

**Release decision:** independently stored options with dependent behavior require a documented dependency matrix and server tests. No separate login, hard-coded global flag system or arbitrary disabled-state semantics are prescribed by the catalog.


## Batch 9 — safe component and styling modernization (proposed, 2026-11-07)

| Gate | Evidence and risk to check | Untested status |
| --- | --- | --- |
| Existing component inventory | Actually imported/used library controls versus merely installed template files, plus feature modules | NOT VERIFIED |
| Extraction ownership | Route orchestration, domain mutation, feature form, shared control and style responsibilities separated | NOT VERIFIED |
| Baseline/compatibility | Before/after task state and semantic behavior; public API/consumer matrix, version/rollback plan | NOT VERIFIED |
| CSS/token migration | Selector inventory, semantic-role mapping, specificity/cascade and dead-class detection | NOT VERIFIED |
| Inclusive interaction | Native control labels, keyboard/focus after dialog, error recovery, zoom/RTL and reduced motion | NOT VERIFIED |
| Responsive/visual checks | Supported viewport and theme snapshots reviewed, not blindly updated; font fallback and long copy | NOT VERIFIED |
| Domain invariants | Existing command and points/reward/review histories unchanged by presentation-only migration | NOT VERIFIED |
| Adoption/release | Small vertical slice first, measured regressions, named owner and removal conditions for adapters | NOT VERIFIED |

A component-library folder is **not** evidence that its contracts are adopted by the app. A passing snapshot or bundler build is not proof that keyboard, focus, business transitions or accessibility are unchanged.

## Application architecture selection and evolution (Batches 13–16)

For an app architecture recommendation, record the repository/ref, framework and routing constraints, primary user journeys, current tree/import graph, real duplication and cross-feature edits, ownership/deployment boundaries, and unknowns. Check that (1) the selected profile is no more complex than needed; (2) feature/domain/shared APIs have documented owners and directional imports; (3) cross-package decisions have real consumers; (4) developer task-to-file discoverability has a baseline; (5) regression and rollback plans cover critical workflows, accessibility, responsive/i18n/theme states and data integrity. A clean docs registry is not proof of an application architecture improvement. See [selection](../architecture/application-architecture.md), [modules](../architecture/module-boundaries-and-developer-navigation.md), [evolution](../architecture/architecture-evolution.md), [enterprise topology](../architecture/enterprise-and-multiapp.md).

## Batch 18 — architecture boundary enforcement evidence

For real application releases, document the owner and allowed dependency contract, installed tool/version, alias and relative-import resolution, positive/negative fixture results, existing-versus-new violations, CI check results, approved exception expirations, and cross-feature consumer impact. A green static import check alone does not establish that relative imports, dynamic imports or other languages are covered. The catalog's document validator **cannot** prove application architecture enforcement. Follow [architecture enforcement recipes](../architecture/architecture-enforcement-and-ci.md) and the [Batch 18 context ledger](../planning/application-architecture-batch-18-context-and-gaps.md).
