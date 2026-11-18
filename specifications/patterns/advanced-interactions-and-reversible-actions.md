# Advanced interactions and reversible actions

**Kind:** guideline · **Status:** proposed · **Primary layer:** patterns

## Purpose and use boundary

Define discoverable, accessible and reversible behavior for reorder, bulk actions, command palettes, shortcuts and undo/redo. **Use** when complex interaction provides meaningful value for frequent work. **Avoid** when native buttons, lists and [data tables](data-tables.md) already solve the task. Features own authorization, data mutation and persistence; this pattern owns interaction decisions, not a universal mega-component.

## Choose the simplest interaction

| Task | Prefer | Constraint |
| --- | --- | --- |
| Reorder a list | Move up/down, position chooser or accessible command; optional drag enhancement | A single-pointer, non-drag alternative and keyboard path as applicable |
| Act on many records | Explicit selected count, scope and named bulk command | Distinguish page selection from all matches |
| Repeat frequent commands | Discoverable shortcut help or command palette *in addition* to regular commands | Avoid OS/browser/AT shortcut conflicts |
| Make a reversible edit | Truthful undo scope and window, ideally with persistent state recovery | Never promise remote undo when impossible |
| Edit an interactive grid | Defined navigation, selection and edit model | Do not give ordinary table `role=grid` semantics without actual behavior |
| Commit consequential changes | Review summary and explicit confirmation | Recheck permissions and result status |

## State matrix and error paths

| State | Visible behavior | Recovery |
| --- | --- | --- |
| Idle | Available actions and how to select/reorder | Keyboard help or conventional controls |
| Item selection | Selected count, identity, and filter/page scope | Deselect one, clear selection |
| Pending command | Outcome still pending and focus preserved | Prevent duplicate conflicting mutations |
| Partial success | Identify succeeded and failed items | Retry eligible failures safely |
| Reordered draft | Explicit unsaved state | Revert or save if supported |
| Confirmed success | Report persisted outcome | True undo only if supported |
| Permission loss / conflict | Clearly describe unavailable action | Preserve safe context, do not leak restricted records |

## Interaction contracts

- **Drag and reorder:** reveal target position before execution and announce new order if useful. Implement a non-drag single-pointer alternative for web dragging under WCAG 2.2 SC 2.5.7, and separately meet keyboard operability. Merely adding keyboard drag does not satisfy the single-pointer requirement.
- **Bulk actions:** selection across pages and filters requires explicit scope and counts. Revalidate eligibility and authorization on the server. A partial mutation must report per-item result or a faithful summary; do not imply every item succeeded.
- **Shortcuts/command palette:** commands need discoverable conventional access, clear names, current context, focus/Escape behavior, empty/disabled states and conflict avoidance with text editing, browser and assistive tech. Provide reconfigurability where justified.
- **Undo/redo:** specify action granularity, side effects, duration and whether remote mutations can be compensated. An irreversible deletion or outbound notification cannot simply be “undone” by restoring a UI row.
- **Focus/status:** preserve focus on moved/updated context; do not steal focus merely to announce background changes. Keep recoverable status persistent for important outcomes.
- **Touch and responsive:** hover or small drag handles cannot be the only access route; support translated labels, RTL, narrow layout, reduced motion and color alternatives.

**Illustrative good:** An authorized administrator selects 12 records across two pages, confirms “Archive 12 records,” then receives “10 archived, 2 failed” with a safe retry path for the failures.

**Anti-example:** A drag-only reorder surface has no move controls; a “Delete selected” action silently targets hidden results after filters change, and an Undo toast promises reversal after the records are irreversibly removed.

## Verification and acceptance

| Check | Status | Evidence needed |
| --- | --- | --- |
| Explicit selection scope and bulk partial errors | NOT VERIFIED | Real feature integration and data tests |
| Single-pointer alternative, keyboard and AT | NOT VERIFIED | WCAG 2.2 dragging + keyboard manual checks |
| Shortcuts and command menu focus/semantics | NOT VERIFIED | OS/browser/AT input matrix |
| Undo claims and consequential operation status | NOT VERIFIED | Backend idempotency and compensating action tests |
| Zoom, locale/RTL, themes and reduced motion | NOT VERIFIED | Responsive and localization tests |

## Sources and limits

- [W3C WCAG 2.2 SC 2.5.7: Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html) (AA; consulted 2026-11-07): requires a non-drag single-pointer alternative unless an exception applies; keyboard accessibility is a separate requirement.
- [WAI-ARIA APG Grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/) (consulted 2026-11-07): grid keyboard behavior only when an actual interactive grid is needed.
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (consulted 2026-11-07): authorization at request/object level, not proof of usable UX.

**Canonical ID:** `pattern.advanced-interactions` · **Owner:** unassigned · **Reviewed:** null · **Drafted:** 2026-11-07.

Related: [data tables](data-tables.md), [role-aware workspaces](role-aware-workspaces-and-context-switching.md), [interaction recovery](interaction-states-and-recovery.md), [accessibility](../guidance/accessibility.md), [mobile UX](../guidance/mobile-and-adaptive-platform-ux.md).

## B04 — action consolidation decision contract (CKG-13; proposed 2026-11-07)

**Purpose:** choose the least complex **discoverable** control arrangement for the user's actual task, without turning one generic control into a business-policy engine. This extends the existing bulk/undo/shortcut guidance. [Task flows](task-flows-and-information-architecture.md) owns sequential task context; [component contracts](../architecture/component-contracts.md) owns event ownership; [interaction recovery](interaction-states-and-recovery.md) owns pending/uncertain outcomes and focus recovery. Use [UX measurement](../guidance/ux-measurement.md) to test effort hypotheses.

### Decision matrix: consolidate proximity, not incompatible meanings

| User need / evidence | Preferred presentation | Avoid or reconsider when |
| --- | --- | --- |
| One clear immediate task | **Visible named primary Button** | Action is unavailable without an explanation, or it actually navigates (use Link) |
| Two distinct high-stakes or mutually exclusive outcomes | **Separate clearly named actions**, with impact/reason/confirmation as warranted | A single "Done" or silent default could approve when user meant reject |
| Several related, frequently used task actions | **Local action toolbar/group** with stable ordering | It obscures scope, crowds touch controls, or creates excessive keyboard traversal |
| One frequent low-risk action plus rare alternatives | **Primary + labeled overflow**, or split button *after user evidence* | Alternative outcomes are destructive, permission-sensitive, or require different mandatory inputs; default could be surprising |
| Secondary actions on an individual row | **Target-named overflow menu** or explicit local actions | Item identity becomes ambiguous after sorting/refresh; menu is discoverable only by hover |
| Repeated expert operations | **Optional keyboard shortcut / command palette** in addition to visible path | Conflicts with text input, OS/browser/assistive technology or isn't discoverable |
| Many independently selected records | **Selection summary + explicit scoped bulk command**, subject to supported API | Heterogeneous unreviewed decisions, unknown eligibility or implied atomicity |
| Materially consequential action | **Explicit consequence review/confirmation** when proportionate to risk | Trying to remove safety friction merely to reduce taps |
| Reversible low-risk action | **Truthful Undo** with actual restoration contract | Undo would only hide a row locally or cannot restore remote side effects |

A **split button** has two distinct activation regions: named default action and a disclosure that opens alternatives. Specify names, focus order, Arrow/Escape behavior according to the actual menu pattern, disabled/pending behavior for both regions, whether default action is stable, and an equally usable touch/keyboard path. Do not select or silently change a destructive default based on inferred recent activity. In the absence of measured task frequency and comprehension, prefer explicit labeled actions.

### Consolidated control specification (decision-time worksheet)

Before replacing visible actions with a menu, single CTA, gesture or compact toolbar, record:

1. **User/task and scope:** who is acting, on which resource and under which verified permission and data state.
2. **Actions and consequences:** verbs, distinct outcome semantics, required input/reason, reversibility, server confirmation and safety checkpoints.
3. **Evidence of priority:** observed task frequency or explicit rationale; never assign a split-button default from intuition alone.
4. **Presentation comparison:** visible separate actions vs toolbar vs contextual overflow vs split vs shortcut; include discoverability cost, reading order and click/key/touch paths.
5. **Interaction contract:** trigger/accessible name, selected target, pending/disabled, keyboard, touch, hover alternative, focus return, menu/dialog cancellation, RTL and localized labels.
6. **Failure and recovery:** duplicate prevention, partial/unknown outcome, stale target, permission loss, explicit stop/exit, and whether a genuine Undo exists.
7. **Measurement and guardrails:** eligible cohort, TCR, error severity, completion time, repeated steps, accessibility/safety regressions, sample limitations, and rollback decision.

**Positive illustrative example:** a records list shows **Open details** and a well-named **More actions for report A** menu containing low-frequency low-risk commands; an authorized high-impact deletion remains explicitly labeled with consequence confirmation, and the selected item ID is revalidated at commit.

**Anti-example:** a review panel replaces **Approve**, **Return for changes** and **Reject** with an ambiguous "Complete" split default; a hover-only trash glyph changes meaning under the pointer and triggers an irreversible operation without a note or a confirmed response. Fewer visible buttons here are not evidence of improved UX.

### Verification — no implementation tested

| Scenario | Acceptance evidence | Status |
| --- | --- | --- |
| Novice action discovery and consequence prediction | Moderated task tests, labels understood, no hidden critical path | NOT VERIFIED |
| Keyboard/menu/split behavior and focus | Relevant WAI-ARIA APG pattern, actual browser/AT test | NOT VERIFIED |
| Touch, small viewport/zoom, translations, RTL | All action regions reachable and named; no overlap/hidden commands | NOT VERIFIED |
| Permission change, failed and uncertain write | Server authorization, stable ID, no unsafe retry or premature confirmation | NOT VERIFIED |
| Efficiency vs correctness | TCR/time/error and [effort metrics](../guidance/ux-measurement.md), not click reduction alone | NOT VERIFIED |

**References:** [WAI-ARIA APG Menu Button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/), [WAI-ARIA APG Toolbar](https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (consulted 2026-11-07). Design motivation: Little Wins B07 proposed action-consolidation guidance; no observed improvement or deployment is claimed.
