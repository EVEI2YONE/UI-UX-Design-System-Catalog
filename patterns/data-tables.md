# Data tables and collection actions

**Kind:** specification · **Status:** proposed · **Primary layer:** patterns

## Purpose and use boundary

Present comparable structured records with understandable headings, actions and navigation. **Use** when users need to scan columns, compare entries or perform row actions. **Avoid** using tables for purely decorative layout or forcing dense grids onto workflows better served by a list or individual detail page.

## Composition and ownership

Use a semantic HTML table for read-only tabular content where applicable, with header associations, optional captions and clear row actions. Sorting, filtering, pagination, selection and bulk mutation are **independent feature decisions**; a generic table should not own product API calls. For editing, define explicit interaction and validation contracts rather than assuming spreadsheet-like behavior.

| Scenario | Behavior | Accessible/recovery consideration |
| --- | --- | --- |
| Data present | Column headers and row context recognizable | Header association, actionable row labels |
| Empty | Explain absence and next action | Distinguish filtered zero from no dataset |
| Sorting | Direction and sort key remain visible | Button semantics for sort controls |
| Pagination / large data | Position and total context communicated | Focus/reading order after page change |
| Row selection / bulk action | Scope and consequences explicit | Checkbox labels, count, cancellation |
| Fetch error / partial data | Identify stale/failed portions | Retry or recover without losing selection unexpectedly |

Do not assign complex grid keyboard semantics to an ordinary table. If interactive spreadsheet navigation is a true user task, specify a separately reviewed grid pattern with arrow-key/focus model and full manual assistive-technology tests.

## Responsive, themes and locale

Prefer responsive overflow or alternate summaries that preserve essential comparisons; avoid arbitrary truncation or hiding key columns without a clear route to their content. Test zoom, narrow width, keyboard horizontal scrolling and sticky headers. Localize numerical/date/currency formatting and sorting; ensure bidirectional cells and direction-sensitive identifiers remain readable. Use semantic typography, divider, status and focus tokens.

## Examples and verification

**Illustrative good:** A sortable records table announces the chosen sort column, retains a stable row label for action buttons and provides an accessible no-results state. **Anti-example:** A clickable `<div>` grid lacks row/column semantics and hides actions on hover only.

| Check | Status | Evidence needed |
| --- | --- | --- |
| Data task and representation | NOT VERIFIED | Comparison and action requirements |
| Header semantics, keyboard and focus | NOT VERIFIED | Real table implementation |
| Sorting, empty/error, pagination | NOT VERIFIED | Integration tests |
| Reflow, formats, RTL and themes | NOT VERIFIED | Supported locales/viewport matrix |

**Canonical ID:** `pattern.data-tables` · **Owner:** unassigned · **Review date:** not reviewed · **Migration:** preserve row action paths, sort state and data correctness. Proposed documentation, not a table library.

Related: [search/filtering](search-and-filter.md), [task flows](task-flows-and-information-architecture.md), [accessibility](../guidance/accessibility.md), [internationalization](../guidance/internationalization.md). Standards: [WCAG 2.2](../governance/references.md).

## Batch 10 extension — dense records, editing and visualization

**Representation choice:** Use a semantic data table for row/column comparison; use a [chart and narrative](../guidance/data-visualization-and-dashboards.md) for trends and distributions; use a detailed edit flow when validation, permission or explanation would become confusing in a compact grid. Do not substitute a visual dashboard for needed record-level actions.

### Dense table decision matrix

| Scenario | Contract | Verification |
| --- | --- | --- |
| Many columns | Prioritize task-critical columns with user-visible access to hidden detail; scrolling or adaptable summaries may be appropriate | Zoom/reflow, row identity, keyboard scroll and mobile comparison |
| Sticky headers/first column | Preserve alignment, contrast and actual header associations; avoid obstructing focus | Narrow window, zoom, long translated headers |
| Select all | Explicitly distinguish visible page, filtered result set and all eligible records | Filter/page changes, disabled items and permissions |
| Bulk action | Count and scope, consequence, true progress and partial failure reconciliation | Server auth, rollback/undo claims and focus return |
| Inline editing | Define start/edit/save/cancel/validation states, tab/arrow behavior, concurrency and row context | Keyboard/screen reader, lost focus, conflicting remote edit |
| Large or virtualized data | Preserve row identification, position, accessible announcements and deterministic updates | Screen-reader navigation, pagination and scroll position |
| Data export | Match filter/sort/scope and server-side authorization; name file format and timestamp when known | Permission changes, sensitive fields and export progress |

### Table vs interactive grid

A read-only sortable table should remain a semantic HTML table. Do **not** apply `role=grid` merely because it looks spreadsheet-like. If task research justifies cell navigation and editing, specify keyboard arrows, Enter/F2 behavior, Tab, selection, active descendant, undo/cancel, virtualized row handling and assistive-technology acceptance **as a separately reviewed interactive grid**. The [WAI-ARIA APG grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/) is an implementation reference, not a license to invent shortcuts.

Related decisions: [advanced interactions and undo](advanced-interactions-and-reversible-actions.md), [visualization](../guidance/data-visualization-and-dashboards.md), [mobile and adaptive layout](../guidance/mobile-and-adaptive-platform-ux.md). Test actual integrated behavior; this is proposed documentation.
