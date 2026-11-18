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

For real application releases, document the owner and allowed dependency contract, installed tool/version, alias and relative-import resolution, positive/negative fixture results, existing-versus-new violations, CI check results, approved exception expirations, and cross-feature consumer impact. A green static import check alone does not establish that relative imports, dynamic imports or other languages are covered. The catalog's document validator **cannot** prove application architecture enforcement. Follow [architecture enforcement recipes](../architecture/architecture-enforcement-and-ci.md) and the [Batch 18 context ledger](../archive/planning/application-architecture-batch-18-context-and-gaps.md).


## Account/settings acceptance matrix — batch 3 (KG-024)

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

Related: [account portal](../patterns/account-and-settings-portal.md), [quality gates](quality-gates.md), [measurement](../guidance/ux-measurement.md), [WCAG 2.2](https://www.w3.org/TR/WCAG22/).


## Static wireframe visual QA and evidence rubric (proposed Batch 5, 2026-11-07)

**Use when:** reviewing generated or manually drafted image-based wireframes before presenting a design direction or advancing to interactive prototyping. **Avoid when:** visual neatness substitutes for task outcomes, a screenshot is treated as proof of implementation, or a claimed automated score has no repeatable method and inspected evidence.

This extends `governance.quality` for **visual inspection and evidence reporting**. [Visual hierarchy](../foundations/design-principles.md) owns the principles of action priority; [task composition](../patterns/task-flows-and-information-architecture.md) owns screen alternatives; [wireframe methodology](../guidance/wireframe-methodology.md) owns fidelity/interaction escalation; [interaction recovery](../patterns/interaction-states-and-recovery.md) owns state semantics; [accessibility](../guidance/accessibility.md) owns web/assistive conformance expectations. Do not replicate those concepts as competing standards.

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

1. **Brief check:** compare screen IDs, tasks, source text and constraints to the [B2 brief contract](../patterns/task-flows-and-information-architecture.md); label assumptions and synthetic content.
2. **Image check:** inspect each delivered raster/vector page at native and presentation scale; capture concrete visual defects. Re-render after corrections and re-inspect the changed version, not an earlier screenshot.
3. **Coverage check:** map each depicted state to [B3 state inventory](../patterns/interaction-states-and-recovery.md) and each depicted viewport/locale to [B4 adaptive and locale guidance](../guidance/mobile-and-adaptive-platform-ux.md). List all unshown variants.
4. **Traceability check:** ensure review notes link a stable artifact ID, revision, reviewer/date and the applicable registry IDs. Use a human text transcript/source of truth for content that an image generator may distort.
5. **Escalation check:** if the question requires clicking, real resize, screen-reader behavior, data persistence, authorization, successful transactions or task performance, require an actual prototype/product test; label these **NOT VERIFIED** until run.

**Synthetic good example:** a two-screen appointment selection mock is inspected at presentation scale; text is cross-checked against approved labels; an invented appointment time is marked **ILLUSTRATIVE**; a loading-state inset is **SHOWN**; keyboard behavior is **NOT VERIFIED**. **Anti-example:** a beautiful payment success mock contains a fictitious “payment processed” badge and clipped fee disclosure, yet is reported “production ready and WCAG compliant” because an image looked polished.

### Evidence boundaries and source applicability

The rubric is a **proposed synthesis** of existing catalog hierarchy, UX writing, interaction-state and verification guidance. W3C [WCAG 2.2](https://www.w3.org/TR/WCAG22/) informs *applicable actual web-content evaluation* but is not an image-only certification. [W3C WAI Easy Checks](https://www.w3.org/WAI/test-evaluate/preliminary/) offers preliminary inspection prompts, not complete accessibility assurance. Actual generated images were **not** produced or visually inspected in this documentation batch, so **visual artifact QA: NOT VERIFIED**. Human-user, keyboard, screen reader, browser/device, localization and backend behavior checks are also **NOT VERIFIED**.

## Settings configuration propagation assurance — PR #13 Batch 2 (proposed, 2026-11-07)

For a consequential setting, trace one intent from edited draft through authorized revisioned persistence to **every named affected consumer**. The canonical [Settings Batch 2 contract](../patterns/account-and-settings-portal.md#settings-knowledge-batch-2--propagation-and-integration-verification-kg-010-kg-013-proposed-2026-11-07) defines the consumer/invariant matrix and recovery behavior. Do not duplicate it in each feature. Check authoritative value/version, dependent navigation and direct API enforcement, stale/failed read refreshes, multi-tab conflicts, tenant isolation, in-flight work, retained history, and rollback. Passing field-level tests or the catalog validator does not establish end-to-end correctness; unexecuted target tests remain **NOT VERIFIED**.


## Visual craftsmanship review and corrective iteration — Batch 4 (KG-15 and KG-16; proposed, 2026-11-07)

**Use when:** judging a high-fidelity mock, rendered webpage, component story, or implementation screenshot for *aesthetic coherence and execution quality*. **Avoid when:** replacing the existing [static-wireframe visual QA](#static-wireframe-visual-qa-and-evidence-rubric-proposed-batch-5-2026-11-07), calling a pleasing still image accessible, or claiming animation, keyboard behavior or user success from pixels. The existing image QA still owns literal text fidelity, clipping and screenshot-evidence boundaries; this extension adds **aesthetic craftsmanship** and an iterative correction protocol. [Visual foundations](../foundations/visual-design-craftsmanship.md) own the aesthetic principles; [practical recipes](../foundations/practical-ui-styling-recipes.md) own implementation options.

### KG-15 — Reproducible visual critique rubric

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

### KG-16 — Render → inspect → diagnose → adjust → re-render

1. **Establish the comparison baseline:** task, visual-direction brief, authoritative content, route/component and revision; selected viewports, theme, locale, state, browser, font loading, device scale and capture method. Never compare unrelated states as visual improvements.
2. **Render real artifacts** with the available stack. Capture representative narrow/wide, long-copy, empty/error/loading, light/dark and focus/reduced-motion variants when applicable. Record any unrendered scenarios as `NOT VERIFIED`; screenshots alone cannot validate actual focus or motion behavior.
3. **Inspect at presentation and native pixel scale** against the dimensions above. Separate observed pixels from inferred causes; if a font fails to load, first fix the environment before redesigning typography.
4. **Log findings** in this minimum format: `VIS-# | artifact path + revision | viewport/state | observation | lens + severity | suspected cause | proposed smallest fix | owner | verification needed | status`.
5. **Fix highest-impact issues first**: comprehension and clipping, then hierarchy, spacing/alignment, type and palette, surfaces, decorative polish. Preserve interactions and constraints; prefer token/component-owned changes to one-off global overrides.
6. **Re-render the exact changed state** after each coherent correction set; compare original and new renders under equivalent conditions and check adjacent states for regressions. Do not auto-approve all screenshot baseline diffs.
7. **Stop intentionally:** no blocking/major unresolved issue in the evaluated scope; remaining preference disagreements are documented; applicable runtime tests and user studies are performed or explicitly pending. “Looks polished” alone is not a release condition.

**Troubleshooting example (synthetic):** a screenshot shows the call-to-action cramped against a card edge. Determine if the cause is card inset, button sizing, misapplied token, or a text-wrap edge case. Fix the owning component/style rule, re-render compact and wide versions, then check its disabled and loading variants rather than adding a local negative margin.

**Before/after evidence contract:** capture IDs and same-task comparison with context/state, one specific hypothesis per meaningful change, diffs or annotated observations, side-effect check, reviewer decision and any unverified behavior. See [the synthetic visual-refinement examples](../foundations/visual-refinement-examples.md) (KG-17). Illustrative written examples are **not real screenshots, executed tests or validated user outcomes**.

**Evidence boundary:** Playwright [visual comparisons](https://playwright.dev/docs/test-snapshots) and [Storybook visual testing](https://storybook.js.org/docs/writing-tests/visual-testing) describe potential tooling; neither is declared installed here. Screenshot rendering can detect visual drift but cannot establish WCAG compliance, task completion, font licensing or causal UX improvements. Continue using [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and platform/manual tests for relevant accessibility evidence.

### Batch 4 acceptance

- [ ] Critique identifies concrete aesthetic observations rather than general preference scores.
- [ ] Evidence IDs, viewport/state, browser/font inputs, affected owner and severity are explicit.
- [ ] Every high-impact fix has a before/after same-condition re-render or is `NOT VERIFIED`.
- [ ] Actual responsive, long copy, themes, focus/error/disabled, locale/RTL and reduced-motion behavior checked where applicable, or marked `NOT VERIFIED`.
- [ ] Critical workflows remain usable; image QA, component contract and release/accessibility gates remain separately applicable.
- [ ] Change log and canonical lookup map KG-15/16 to `governance.quality`, KG-17 to a non-canonical example bank.

## Integrated visual craftsmanship workflow — Batch 5 (KG-18, proposed)

To apply visual direction, styling and critique as a connected process, use the [end-to-end visual craftsmanship workflow](visual-craftsmanship-workflow.md). This document remains the canonical owner of review and evidence requirements; the linked guide is **non-canonical orchestration** only. It maps KG-01–18 to existing owners, defines proportionate intake and handoff, and requires accurate `PASS`, `FAIL`, `NOT VERIFIED`, or `NOT APPLICABLE` checks. Do not infer visual quality or accessibility from documentation alone.

## B06 — interaction-state test evidence and catalog retrieval assurance (CKG-18/19; proposed 2026-11-07)

**Scope:** define what a reviewer must observe for proposed component/interaction contracts and how an agent must retrieve their canonical owner. This extends existing quality gates rather than shipping a test framework or replacing actual end-user trials. A passing Markdown validator can verify only catalog structure; **it cannot verify accessibility, implemented interactions or task outcomes.**

### CKG-18 — interaction-state test matrix

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

### CKG-19 — retrieval and documentation regression

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


## Static visual catalog hosting, supply-chain and preview security gate

This checklist applies to a potential **public release** of the source-derived visual catalog. It extends the existing documentation and product quality gates; it does not assert a deployment, provide a security certification or set an unreviewed production hosting policy.

### Hosting decisions before publication

| Decision | Required contract | Current catalog limitation |
| --- | --- | --- |
| Origin/base path | Decide root versus repository subpath; verify every page, search URL, CSS/JS asset, iframe, source URL and redirect on the target host | Generated links and assets currently assume origin-root hosting |
| Immutable provenance | Bind published source links to a reviewed branch/tag/commit, ideally an immutable commit | CI already supports validated `CATALOG_SOURCE_REF`; default local builds use `main` |
| Build artifact and release | Name artifact digest, build commit, verification status, responsible approver, deploy/revert commands | No public deployment exists |
| Cache and indexability | Define cache invalidation, redirects, robots/indexing, sitemap and handling of removed/deprecated concepts | No deployment-specific cache/header controls are evidenced |
| Privacy and telemetry | Declare any analytics, consent, data retention, no production user records in synthetic preview, artifact access | CI-generated accessibility reports and screenshots should be reviewed for accidental sensitive content |

For root-to-subpath publishing, tests must exercise `/catalog/`, `/search/`, all references and `/previews/` from that *actual path*. Changing a host configuration alone does not rewrite root-absolute URLs. Do not ship to GitHub Pages subpath unless a verified base-path strategy exists.

### Threat boundaries and CSP review

The site must use **trusted, checked-in** reference source—not code typed by visitors or unreviewed remote scripts. The compiler verifies source paths under `site/src/implementations/` and copies them into a sandboxed iframe. The iframe's `allow-scripts` permission supports the demo; its omission of `allow-same-origin` makes its origin opaque and blocks ordinary access to parent-origin cookies/storage. Do not add `allow-same-origin`, `allow-top-navigation`, `allow-popups` or `allow-forms` for convenience without a threat-model review. **This isolation is defense in depth**, not authorization or proof that every JS source is secure.

Before choosing any CSP, enumerate all necessary assets/scripts/styles/iframes, then test a server-delivered **enforcing** policy plus a reporting rollout. The policy must distinguish top-level pages from preview routes where needed; do not copy a globally strict `frame-ancestors 'none'` rule onto preview documents that intentionally need to be embedded. A possible *review starting point*, **not a ready-to-deploy header**, is:

```text
Content-Security-Policy: default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self' data:; frame-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors 'self'
```

Validate whether `data:` is necessary and remove it if not; limit frame ancestry and resource origins to actual host needs. The real server sets headers; a Markdown document or static HTML meta tag does not establish them. Check CSP enforcement and console violations in Chromium, Firefox and Safari, and explicitly test iframe bootstrap, scenario selection and source disclosure. Keep any approval tied to a tested host/environment.

### Supply chain, dependency and license gate

The Python static builder uses the standard library, while **CI only** currently installs Playwright and axe with pinned top-level versions through `npm install --no-package-lock`. That does *not* guarantee transitive resolution reproducibility. Before release:

1. Record a reviewed toolchain version and project-level package manifest with exact direct dependencies and a committed integrity-bearing lockfile.
2. Change CI to `npm ci` using that lockfile; verify clean installation from scratch. The npm documentation specifies that `npm ci` requires a matching lock and does not rewrite dependency declarations.
3. Run dependency vulnerability and license review on the locked tree; record reviewed advisories, exceptions, affected paths and decision owners. `npm audit` alone does not constitute license clearance or a full threat model.
4. Pin or review third-party GitHub Actions usage and their transitive dependencies; keep minimum workflow permissions and avoid secrets in preview sources.
5. Verify no vendored fonts, customer data, unknown image licenses or runtime network requests are silently introduced. If including third-party code, record license and attribution requirements.
6. Repeat after any material dependency/host change; do not re-use old approvals for new revisions.

### Decision, acceptance and rollback

| Gate | PASS evidence | FAIL / NOT VERIFIED handling |
| --- | --- | --- |
| Site routes under actual host | Automated crawl plus manual navigation at deployment path | No publication; fix and rerun |
| CSP/framing | Enforcing response headers, no unexpected blocked assets, iframe isolation tests | No publication; document policy adjustment |
| Dependencies/licenses | Lockfile, reproducible install, audit and approved license inventory | Do not describe site as supply-chain reviewed |
| Data/privacy | Synthetic-only fixture inspection, artifact/access review, no secret leakage | Remove or replace unsafe evidence before publishing |
| Accessibility | Human task + AT evidence and automated reports, clear scope | No WCAG certification without applicable evidence |
| Performance | Lab and production field metrics with environment/cohort/percentile | Do not replace real-user measurements with static size budgets |
| Approval | Named design, security and maintainer decision plus release SHA | Keep PR draft/no-go; never treat Git mergeability as approval |
| Rollback | Previous artifact/source revision, reversible switch, owner and verification | Stop release until an executable revert path exists |

**Provenance:** [OWASP Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html) describes CSP as defense in depth and host-specific framing rules; [MDN iframe sandbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe#sandbox) warns against combining `allow-scripts` and `allow-same-origin` for same-origin embedders; [npm ci](https://docs.npmjs.com/cli/commands/npm-ci/) documents reproducible clean installs with a lockfile. These are reference sources, not evidence that this repository has satisfied the controls.

**Current disposition:** the release checklist is authored knowledge, but hosting, CSP enforcement, locked CI dependencies, license review and named security signoff remain **NOT VERIFIED**. The [release decision record](../docs/visual-catalog-refactor/16-phase-10-release-readiness.md) documents the original blockers; merging PR #16 did not establish security approval or deployment authorization.
