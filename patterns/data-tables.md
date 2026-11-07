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
