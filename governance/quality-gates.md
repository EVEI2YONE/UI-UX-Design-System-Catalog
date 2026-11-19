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

## Evidence record

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

## Product release evidence beyond documentation

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

## Hosted collaborative product assurance — context-driven checks

Before this gate, gather: actual hosting trust boundary, public/raw endpoint exposure, authenticated subject contract, owner and tenant data model, command/state transitions, storage concurrency scheme, and domain tests. A hosted application's design notes or domain tests are insufficient proof of deployed identity isolation or browser behavior; validate the actual environment.

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

## Data-lifecycle and migration acceptance

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

## Record-to-modal journey assurance

| Scenario | Evidence required | Untested status |
| --- | --- | --- |
| Row action semantics | Action is a named native link/button in semantic table; keyboard and screen-reader task path | NOT VERIFIED |
| Modal focus lifecycle | Actual initial focus, containment, Escape and close-button behavior, background inertness | NOT VERIFIED |
| Draft protection | Changed field -> cancel/backdrop/Escape -> explicit preservation/discard policy; verified restoration | NOT VERIFIED |
| Async completion and focus | Server-confirmed result, accessible status, return focus to valid trigger or safe fallback after row disappears | NOT VERIFIED |
| State/locale/responsive | Error/retry, disabled/busy, long labels, keyboard at narrow/zoom, RTL and supported AT/browser matrix | NOT VERIFIED |

Do not mark a product test PASS based solely on source review or on the presence of a prebuilt accessible component library. Prefer one integrated end-to-end evidence record for the full journey, supplemented by unit/component checks.

## Independent flags and dependent capabilities

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

## Safe component and styling modernization

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

## Application architecture selection and evolution

For an app architecture recommendation, record the repository/ref, framework and routing constraints, primary user journeys, current tree/import graph, real duplication and cross-feature edits, ownership/deployment boundaries, and unknowns. Check that (1) the selected profile is no more complex than needed; (2) feature/domain/shared APIs have documented owners and directional imports; (3) cross-package decisions have real consumers; (4) developer task-to-file discoverability has a baseline; (5) regression and rollback plans cover critical workflows, accessibility, responsive/i18n/theme states and data integrity. A clean docs registry is not proof of an application architecture improvement. See [selection](../knowledge/architecture/application-architecture.md), [modules](../knowledge/architecture/module-boundaries-and-developer-navigation.md), [evolution](../knowledge/architecture/architecture-evolution.md), [enterprise topology](../knowledge/architecture/enterprise-and-multiapp.md).

## Architecture boundary enforcement evidence

For real application releases, document the owner and allowed dependency contract, installed tool/version, alias and relative-import resolution, positive/negative fixture results, existing-versus-new violations, CI check results, approved exception expirations, and cross-feature consumer impact. A green static import check alone does not establish that relative imports, dynamic imports or other languages are covered. The catalog's document validator **cannot** prove application architecture enforcement. Follow [architecture enforcement recipes](../knowledge/architecture/architecture-enforcement-and-ci.md) and the .

## Account and settings acceptance matrix

The portal's release gate must validate a **real joined journey**, not just isolated component demos:

| Journey | Minimum release evidence |
| --- | --- |
| Profile and verified contact | Change, verification pending, expiry, rollback, reload, other session |
| Security and authorization | Step-up, lost factor, revoked session, denied endpoint and stale deep link |
| Privacy/data/deletion | Effective purpose choice, asynchronous exports/deletion, legal retention and access boundaries |
| Notifications and locale | Delivery permission vs preference, quiet-hour/DST, switch locale and long RTL copy |
| Appearance | System/manual modes, high contrast, reduced motion, load/reload and zoom |
| Billing and subscription | Trial, card failure, retries, cancellation, downgrade, invoices and account ownership |
| Universal recovery | Keyboard, screen reader, focus return, 400% zoom/reflow where applicable, offline/timeout, no duplicate billing actions |

Measure task completion, error/recovery, abandonment and support contact by user job with defined denominators and privacy-preserving events. Include compatibility, staged rollout, rollback trigger, security/legal reviewers and baseline gaps. **All app runtime, payment, accessibility, analytics and legal verification currently NOT VERIFIED.** Passing catalog lint/links does not imply implemented capabilities or accessibility conformance.

Related: [account portal](../specifications/patterns/account-and-settings-portal.md), [quality gates](quality-gates.md), [measurement](../knowledge/guidance/ux-measurement.md), [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

## Static wireframe visual QA and evidence rubric

**Use when:** reviewing generated or manually drafted image-based wireframes before presenting a design direction or advancing to interactive prototyping. **Avoid when:** visual neatness substitutes for task outcomes, a screenshot is treated as proof of implementation, or a claimed automated score has no repeatable method and inspected evidence.

This extends `governance.quality` for **visual inspection and evidence reporting**. [Visual hierarchy](../knowledge/foundations/design-principles.md) owns the principles of action priority; [task composition](../specifications/patterns/task-flows-and-information-architecture.md) owns screen alternatives; [wireframe methodology](../knowledge/guidance/wireframe-methodology.md) owns fidelity/interaction escalation; [interaction recovery](../specifications/patterns/interaction-states-and-recovery.md) owns state semantics; [accessibility](../knowledge/guidance/accessibility.md) owns web/assistive conformance expectations. Do not replicate those concepts as competing standards.

### Inspect the actual artifact, not the prompt

Review the **rendered image at its intended sharing size**, including every screen and important inset/callout. Compare against the task brief and approved content separately. A statement in the generation prompt does not establish that it appeared correctly in the output. If the image is unavailable, mark all artifact-specific observations **NOT VERIFIED**, rather than inventing a pass.

| Visual QA gate | What to inspect in the image | Example failure / disposition |
| --- | --- | --- |
| **Legibility and content fidelity** | Can headings, labels, critical values and notes actually be read? Does each essential label match source-of-truth text? | Garbled/generated copy, altered monetary value, tiny annotation → **FAIL** until corrected; unknown source copy → **NOT VERIFIED** |
| **Clipping and geometry** | Are controls, text, borders, overlays and screen edges intact at the depicted viewport? | Truncated error or overlapped primary button → **FAIL** for depicted state |
| **Hierarchy and task orientation** | Are current scope, user decision, primary action, supporting context and safe exit identifiable? | Decorative hero dominates task; equal-priority CTAs → revise or justify |
| **Affordance and state consistency** | Do identical patterns look alike across screens? Do loading, empty, error, denied, confirmed and return states differ meaningfully? | “Success” styling on unknown-outcome state → **FAIL**, not a confirmed transaction |
| **Truthfulness and invented behavior** | Are permissions, live availability, payment/export completion, routes, support channels and saving claims backed by input or marked illustrative? | Fake capability displayed as implemented → **FAIL**; unknowns must be labeled |
| **Cross-screen/variant consistency** | Do navigation, terminology, selected item, filter scope, CTA label and data carry coherently across alternatives/viewport images? | Task identity silently changes between compact and wide mock → **FAIL** or documented intentional change |
| **Responsive/locale stress visibility** | Are intended compact/wide, long copy, RTL and error variants depicted or clearly listed as not shown? | Single desktop image claimed to prove reflow/RTL → **FAIL** for the claim; actual behavior **NOT VERIFIED** |
| **Source and decision trace** | Are image ID/version, task, canonical IDs, known/assumed information, reviewer, issue severity and next step recorded? | No way to match criticism to artifact or brief → request evidence |

A static review may establish that an **observed image** visibly includes or omits content. It cannot establish keyboard operation, accessible names, focus, actual reflow, service permissions, server results, or real-user comprehension. Use `NOT APPLICABLE` only when a reviewed task/scope justifies it; use `NOT SHOWN` to describe omitted imagery, not as a test result.

### Lightweight issue log, severity and disposition

For each finding record:
`artifact_id + revision | screen/state/viewport | gate | observed evidence (quote/crop reference) | expected source/requirement | severity | action | owner | status | verification method`.

- **Blocker:** unreadable task-critical content, fabricated material capability or outcome, obscured safety/price/privacy disclosure, or a depiction that would materially mislead the decision. Correct the image/content before presenting it as an approved direction.
- **Major:** broken primary path, confusing state differentiation, clipped error text, inconsistent task context, or missing required view/state without disclosure. Revise or visibly constrain scope.
- **Minor:** cosmetic alignment or decoration that does not hide information or change task meaning. Record for proportionate refinement.

These are **proposed review priorities**, not measured defect frequency or a universal risk rating. Assign `PASS`, `FAIL`, `NOT VERIFIED`, or `NOT APPLICABLE` separately for each inspected gate and explicitly state *which image/revision was inspected*. A visual PASS means only that specified depiction met the documented review expectation, not accessibility or implementation compliance.

### Verification order

1. **Brief check:** compare screen IDs, tasks, source text and constraints to the [B2 brief contract](../specifications/patterns/task-flows-and-information-architecture.md); label assumptions and synthetic content.
2. **Image check:** inspect each delivered raster/vector page at native and presentation scale; capture concrete visual defects. Re-render after corrections and re-inspect the changed version, not an earlier screenshot.
3. **Coverage check:** map each depicted state to [B3 state inventory](../specifications/patterns/interaction-states-and-recovery.md) and each depicted viewport/locale to [B4 adaptive and locale guidance](../knowledge/guidance/mobile-and-adaptive-platform-ux.md). List all unshown variants.
4. **Traceability check:** ensure review notes link a stable artifact ID, revision, reviewer/date and the applicable registry IDs. Use a human text transcript/source of truth for content that an image generator may distort.
5. **Escalation check:** if the question requires clicking, real resize, screen-reader behavior, data persistence, authorization, successful transactions or task performance, require an actual prototype/product test; label these **NOT VERIFIED** until run.

**Synthetic good example:** a two-screen appointment selection mock is inspected at presentation scale; text is cross-checked against approved labels; an invented appointment time is marked **ILLUSTRATIVE**; a loading-state inset is **SHOWN**; keyboard behavior is **NOT VERIFIED**. **Anti-example:** a beautiful payment success mock contains a fictitious “payment processed” badge and clipped fee disclosure, yet is reported “production ready and WCAG compliant” because an image looked polished.

### Evidence boundaries and source applicability

The rubric is a **proposed synthesis** of existing catalog hierarchy, UX writing, interaction-state and verification guidance. W3C [WCAG 2.2](https://www.w3.org/TR/WCAG22/) informs *applicable actual web-content evaluation* but is not an image-only certification. [W3C WAI Easy Checks](https://www.w3.org/WAI/test-evaluate/preliminary/) offers preliminary inspection prompts, not complete accessibility assurance. Actual generated images were **not** produced or visually inspected in this documentation batch, so **visual artifact QA: NOT VERIFIED**. Human-user, keyboard, screen reader, browser/device, localization and backend behavior checks are also **NOT VERIFIED**.

## Settings configuration propagation assurance

For a consequential setting, trace one intent from edited draft through authorized revisioned persistence to **every named affected consumer**. The canonical [Settings contract](../specifications/patterns/account-and-settings-portal.md) defines the consumer/invariant matrix and recovery behavior. Do not duplicate it in each feature. Check authoritative value/version, dependent navigation and direct API enforcement, stale/failed read refreshes, multi-tab conflicts, tenant isolation, in-flight work, retained history, and rollback. Passing field-level tests or the catalog validator does not establish end-to-end correctness; unexecuted target tests remain **NOT VERIFIED**.

## Visual craftsmanship review and corrective iteration

**Use when:** judging a high-fidelity mock, rendered webpage, component story, or implementation screenshot for *aesthetic coherence and execution quality*. **Avoid when:** replacing the existing static-wireframe visual QA, calling a pleasing still image accessible, or claiming animation, keyboard behavior or user success from pixels. The existing image QA still owns literal text fidelity, clipping and screenshot-evidence boundaries; this extension adds **aesthetic craftsmanship** and an iterative correction protocol. [Visual foundations](../knowledge/foundations/visual-design-craftsmanship.md) own the aesthetic principles; [practical recipes](../knowledge/foundations/practical-ui-styling-recipes.md) own implementation options.

### Reproducible visual critique rubric

Record an observation, why it matters, a specific proposed correction and the artifact/view state for **each applicable dimension**. Use `PASS` / `FAIL` / `NOT VERIFIED` / `NOT APPLICABLE` per dimension, with reviewer and evidence. Do not turn taste into an unexplained numerical “beauty” score.

| Lens | Inspect | Illustrative failure → precise correction |
| --- | --- | --- |
| **Focal point and scan path** | Dominant element, first useful information, secondary information and action weight | Four equally saturated CTAs → reserve dominant emphasis for current next action, demote other actions without hiding them |
| **Alignment and proportion** | Shared edges, grid logic, optical (not only geometric) centering, column proportions | Card labels drift across rows → establish common inset and alignment spine |
| **Typographic hierarchy** | Role distinction, scale jumps, line breaks, line length, optical spacing, fallback rendering | Heading wraps awkwardly while captions are too tiny → tune max measure and role-specific line-height/size |
| **Color orchestration** | Relative saturation, neutral surface balance, actionable/status accents, theme coherence | Five bright card backgrounds compete → use quiet surfaces, preserve semantic status cues and single intended accent |
| **Spacing and density** | Repeated spatial rhythm; grouping versus separation; meaningful whitespace at real content length | Every gap is identical → distinguish field, component and section spacing based on relationship |
| **Surface and depth** | Consistent border, radius, elevation levels; overlays distinguish foreground from base | Every card casts an equally dramatic shadow → reserve elevation for actual layering |
| **Image and icon direction** | Consistent crop, illustration style, optical icon size and content relevance | Mixed icon families and random photo crops → choose one family and documented subject framing |
| **States and responsive coherence** | Empty, loading, error, focus, compact and expanded layouts retain visual grammar | Error state introduces entirely new spacing and color rules → reuse existing semantic state grammar |

**Severity:** `BLOCKER` for a visual defect that prevents critical content/action comprehension or conceals required information; `MAJOR` for unclear hierarchy, clipping, severe inconsistency or difficult scanning; `MINOR` for polish such as small optical misalignment; `PREFERENCE` for reasonable stylistic alternatives without supported task impact. Apply actual applicable accessibility failures under their stronger established release gates, not as subjective preferences.

**Good critique:** “At the 375px error-state capture, the second line of the Save error overlaps Cancel; make the message area auto-height, allow wrapping and re-render at 375px/zoom.” **Bad critique:** “Feels off; make it more modern,” without evidence or a change hypothesis.

### Render → inspect → diagnose → adjust → re-render

1. **Establish the comparison baseline:** task, visual-direction brief, authoritative content, route/component and revision; selected viewports, theme, locale, state, browser, font loading, device scale and capture method. Never compare unrelated states as visual improvements.
2. **Render real artifacts** with the available stack. Capture representative narrow/wide, long-copy, empty/error/loading, light/dark and focus/reduced-motion variants when applicable. Record any unrendered scenarios as `NOT VERIFIED`; screenshots alone cannot validate actual focus or motion behavior.
3. **Inspect at presentation and native pixel scale** against the dimensions above. Separate observed pixels from inferred causes; if a font fails to load, first fix the environment before redesigning typography.
4. **Log findings** in this minimum format: `VIS-# | artifact path + revision | viewport/state | observation | lens + severity | suspected cause | proposed smallest fix | owner | verification needed | status`.
5. **Fix highest-impact issues first**: comprehension and clipping, then hierarchy, spacing/alignment, type and palette, surfaces, decorative polish. Preserve interactions and constraints; prefer token/component-owned changes to one-off global overrides.
6. **Re-render the exact changed state** after each coherent correction set; compare original and new renders under equivalent conditions and check adjacent states for regressions. Do not auto-approve all screenshot baseline diffs.
7. **Stop intentionally:** no blocking/major unresolved issue in the evaluated scope; remaining preference disagreements are documented; applicable runtime tests and user studies are performed or explicitly pending. “Looks polished” alone is not a release condition.

**Troubleshooting example (synthetic):** a screenshot shows the call-to-action cramped against a card edge. Determine if the cause is card inset, button sizing, misapplied token, or a text-wrap edge case. Fix the owning component/style rule, re-render compact and wide versions, then check its disabled and loading variants rather than adding a local negative margin.

**Before/after evidence contract:** capture IDs and same-task comparison with context/state, one specific hypothesis per meaningful change, diffs or annotated observations, side-effect check, reviewer decision and any unverified behavior. See [the synthetic visual-refinement examples](../knowledge/foundations/visual-refinement-examples.md). Illustrative written examples are **not real screenshots, executed tests or validated user outcomes**.

**Evidence boundary:** Playwright [visual comparisons](https://playwright.dev/docs/test-snapshots) and [Storybook visual testing](https://storybook.js.org/docs/writing-tests/visual-testing) describe potential tooling; neither is declared installed here. Screenshot rendering can detect visual drift but cannot establish WCAG compliance, task completion, font licensing or causal UX improvements. Continue using [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and platform/manual tests for relevant accessibility evidence.

### Acceptance

- [ ] Critique identifies concrete aesthetic observations rather than general preference scores.
- [ ] Evidence IDs, viewport/state, browser/font inputs, affected owner and severity are explicit.
- [ ] Every high-impact fix has a before/after same-condition re-render or is `NOT VERIFIED`.
- [ ] Actual responsive, long copy, themes, focus/error/disabled, locale/RTL and reduced-motion behavior checked where applicable, or marked `NOT VERIFIED`.
- [ ] Critical workflows remain usable; image QA, component contract and release/accessibility gates remain separately applicable.
- [ ] Change log and canonical lookup map to `governance.quality`, to a non-canonical example bank.

## Integrated visual craftsmanship workflow

To apply visual direction, styling and critique as a connected process, use the [end-to-end visual craftsmanship workflow](visual-craftsmanship-workflow.md). This document remains the canonical owner of review and evidence requirements; the linked guide is **non-canonical orchestration** only. It maps to existing owners, defines proportionate intake and handoff, and requires accurate `PASS`, `FAIL`, `NOT VERIFIED`, or `NOT APPLICABLE` checks. Do not infer visual quality or accessibility from documentation alone.

## Interaction-state test evidence and catalog retrieval assurance

**Scope:** define what a reviewer must observe for proposed component/interaction contracts and how an agent must retrieve their canonical owner. This extends existing quality gates rather than shipping a test framework or replacing actual end-user trials. A passing Markdown validator can verify only catalog structure; **it cannot verify accessibility, implemented interactions or task outcomes.**

### Interaction-state test matrix

Tests must exercise **trigger → component state → workflow coordinator → user-visible response**, including keyboard/pointer/touch paths and error branches where relevant. Prefer the existing consumer application's test toolchain; the names below are test *scenarios*, not imports or a required Playwright/Storybook dependency.

| Scenario | Assertions in a real implementing application | Minimum evidence |
| --- | --- | --- |
| Named icon-only action | Contextual accessible name; focus-visible; native Enter/Space; target geometry; no duplicate SVG activation | Browser keyboard/AT and touch check, target-size applicability |
| Icon status vs task action | Decorative icon hidden from AT when labeled; status meaning visible in text; glyph role not confused with actionable check | Screen-reader and visual/icon registry audit |
| Compound card, overflow and dialog | Row actions identify current record, trigger only once, menu follows appropriate keyboard model and Escape/return focus; no nested interactive conflict | Keyboard, pointer, focus lifecycle and item identity tests |
| Controlled form/select/filter | Parent is state source when controlled; changes, resets and refreshes do not desynchronize visible value, results or errors | Component integration tests, translated/long labels |
| Pending/uncertain consequential command | Pending prevents duplicate activation, failed/unknown status never displays confirmed icon; reconcile by authoritative ID and revision | Service-mocked delay/timeout/conflict plus real API contract review |
| Removed selected row / dialog invoker | Focus moves to a valid logical target; important status announced without stealing focus on every refresh | DOM/focus checks and AT manual inspection |
| Sequential next eligible task | Only advance after confirmed/reconciled result and current authorization; preserve note on failure; Skip/Stop/Load More truthful | End-to-end workflow and server-state tests |
| Responsive, theme and locale matrix | Visible action region remains discoverable at narrow/zoomed widths, RTL, forced-colors, reduced motion and long labels | Rendered state screenshots plus manual keyboard/AT checks |

**Evidence format per test:** `canonicalId`, component/feature consumer, source revision, environment (browser/OS/device/AT/locale/theme/zoom), scenario/trigger, expected result, *observed* result, status `PASS|FAIL|NOT VERIFIED|NOT APPLICABLE`, run timestamp, owner, screenshot/log reference and known limitation. Do not mark PASS from pseudocode or a text assertion alone. For high-impact writes, record backend eligibility, revision, idempotency and reconciliation evidence separately from visible UI testing.

**Negative fixtures matter:** a bare clickable SVG must fail an interactive semantic review; an overflow menu that only opens on hover must fail discoverability; a pending spinner that appears as confirmed success must fail authoritative result correctness; a row removal that strands focus must fail navigation continuity. Do not use CSS-only focus snapshots as proof of actual keyboard operability.

### Retrieval and documentation regression

**Canonical retrieval owner:** `catalog/index.json` declares the unique ID/path/status/aliases; Markdown pages own detailed guidance; `scripts/find_concept.py` supplies deterministic exact-ID/alias priority. Do not duplicate normative contracts as agent-local instructions.

| Retrieval task (example) | Expected canonical owner | Boundary |
| --- | --- | --- |
| `icon consistency audit`, `semantic icon registry` | `foundation.icon-semantics` | Icon meaning/review, not business activation |
| `icon-only button` | `foundation.icon-semantics` + `component.button` | Host Button owns activation |
| `cross component events`, `nested interactive controls` | `architecture.component-contracts` | Feature owns domain outcome |
| `focus after item removal`, `pending confirmed icon` | `pattern.interaction-recovery` | Reconciliation vs optimistic updates |
| `sequential task controller`, `stable action region` | `pattern.task-flows` | No automatic submission |
| `split button safety`, `action consolidation decision matrix` | `pattern.advanced-interactions` | Prefer visible peer decisions when high-risk |
| `pointer travel distance`, `time to next action` | `guidance.ux-measurement` | Measurement, not click-only optimization |
| `utility-first styling ownership`, `visual redundancy enforcement`, `component inventory to contract mapping` | `foundation.practical-styling`, `architecture.enforcement-ci`, `architecture.component-model` respectively | Existing canonical architecture owners |
| `interaction state test matrix`, `catalog retrieval regression` | `governance.quality` | Documentation vs actual browser evidence |

**Required automated catalog checks:** registry/schema validity, unique IDs/paths and no broken internal references; exact ID and task-alias lookup for both legacy and new knowledge; test for inappropriate owner collisions (an icon semantic query should not accidentally resolve to an app-specific workflow). For each affected entry verify its `status`, `owner` and `reviewed_at` metadata rather than automatically promoting proposed guidance. Preserve an intentional alias redirect if a concept ID moves.

**Coverage and evidence matrix:** distinguish (1) repository content verified via GitHub, (2) Python validator/test run completed with actual exit/output, (3) real consumer implementation or manual keyboard/screen-reader/browser checks, and (4) observed user-efficiency evidence. Each has a separate status. The PR should explicitly name any missing category; an unrun test is **NOT VERIFIED**, never PASS.

**Catalog commands when an executable working tree is available:**

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
python3 scripts/find_concept.py "icon consistency audit" --json
python3 scripts/find_concept.py "interaction state test matrix" --json
```

Do not infer a successful run merely from the presence of these commands in documentation. On a GitHub PR, inspect the actual workflow checks before reporting green.

**Illustrative positive:** a catalog PR updates an existing owner and retrieval aliases, then logs actual passing validator/tests and separately marks unperformed screen-reader interaction checks NOT VERIFIED. **Anti-example:** write a retrieval unit test that only asserts a phrase exists in Markdown, mark "Accessible PASS" without rendering a control, then auto-promote every changed entry to stable.

**Review and ownership:** Proposed knowledge, owner unassigned. Human review, observed consumer accessibility, production release and UX metrics remain **NOT VERIFIED** until supported by separate evidence. References (consulted 2026-11-07): [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Playwright testing](https://playwright.dev/docs/intro), [Storybook interaction tests](https://storybook.js.org/docs/writing-tests/interaction-testing), and the catalog's own `scripts/validate_catalog.py` and `scripts/find_concept.py`.

## Static visual catalog hosting and documentation supply-chain gate

This is a publication-readiness checklist for a **read-only documentation browser**. The repository provides a canonical concept registry, Markdown guidance, a small static generator and progressive search; it intentionally does **not** ship executable UI examples, sandboxed demo frames or reusable component packages. Hosting and browser checks do not verify any consuming application's behavior.

### Hosting decisions before publication

| Decision | Required review | Current limitation |
| --- | --- | --- |
| Origin/base path | Verify root-versus-subpath routes, CSS/JS links, search query parameters and source URLs on the target host | The generated site uses root-relative links; subpath deployment needs a tested strategy |
| Source provenance | Tie published Markdown source links to a reviewed commit or known immutable revision | The builder accepts `CATALOG_SOURCE_REF`; default local builds use `main` |
| Build artifact and rollback | Record release commit/digest, authorized approver, deployment and revert procedure | No public deployment or recovery SLO is established here |
| Cache and indexability | Review caching, robots/indexing, redirects and deprecation links | These are host-dependent and NOT VERIFIED |
| Privacy and telemetry | Disclose analytics if introduced and avoid publishing sensitive records or test artifacts | The documentation builder uses repository-authored content; browser audit screenshots still need review |

For public hosting, crawl `/catalog/`, `/search/`, representative concept pages and the task index at the **actual deployment path**. Verify canonical ID-based URLs remain stable, every relative source link resolves and query-state restoration does not expose sensitive data. Do not infer deployment success from a local build.

### Security, content policy and CSP

The documentation site has no preview iframes or injected executable example source. Markdown rendering must escape unsafe markup and reject active unsafe links; generated pages should load only the minimal local navigation/search assets. The repository validator rejects implementation metadata and legacy implementation directories.

Before setting an enforcing Content-Security-Policy, inventory actual scripts, styles, images and links, then test on the serving origin. A **review starting point, not a ready-to-deploy header**, is:

```text
Content-Security-Policy: default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'
```

Confirm the appropriate `img-src`, form and framing requirements with hosting owners. For a stand-alone documentation site, `frame-ancestors 'none'` may be considered; any different embedding requirement demands an explicit threat review. Only real response headers can enforce this policy. Check browser console violations, asset loading and expected network requests in all supported environments; automated tests are not security certification.

### Build dependency and source integrity

The Python static builder uses the standard library; CI installs Playwright and axe for browser checks. The current ad hoc npm install without a checked-in lockfile does not guarantee transitive reproducibility. Before deployment, record dependencies, decide on a supported pinned toolchain and lockfile, review third-party licenses and advisories, and use a reproducible install. The docs-only boundary also requires:

1. No `site/src/implementations/`, `site/src/previews/` or `packages/` content, and no registry `implementation` property.
2. No generated `/previews/` or `/reference/` routes or embedded demo iframes; all 92 canonical IDs and their documentation URLs remain unchanged.
3. No prose or catalog badge suggesting a component is importable, previewable or independently approved.
4. Catalog, editorial, retrieval, static-site and browser documentation tests pass without claiming product UX conformance.
5. Cross-browser, assistive-technology, real user task and consumer integration evidence is recorded separately when someone adopts the guidance.

### Acceptance and rollback

| Gate | Evidence needed | Without evidence |
| --- | --- | --- |
| Canonical catalog | Unique IDs/paths, valid relative links, status and source accuracy | Do not publish broken guidance |
| No shipped library | No executable preview files/metadata/routes, source-only documentation links | Remove unintentional runtime artifacts |
| Accessibility | Browser shell automated tests and manual keyboard/AT review of actual deployment | Do not claim full WCAG conformance |
| Hosting/CSP | Checked response headers, routing and allowed resources | Keep unpublished until validated |
| Supply chain | Reproducible dependencies and license/security review | Do not claim verified dependency safety |
| Rollback | Prior artifact and named release owner | Do not proceed with irreversible rollout |

**Provenance:** [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html) and [web.dev deployment guidance](https://web.dev/) provide context rather than proof this site is secured. The repo's read-only build and checks are documentation infrastructure; runtime component and product security verification belong to consuming applications. All actual deployment conditions remain **NOT VERIFIED** until tested.
