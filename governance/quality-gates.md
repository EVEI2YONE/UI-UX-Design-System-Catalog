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
