# Collection and feed views

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Choose and compose a collection representation—list, card grid, gallery, timeline-like feed or virtualized stream—based on the user's comparison, scanning and action needs while maintaining identity, selection and reading context.

**Use when:** People browse heterogeneous records, updates, products, messages or other repeated items that need more than a plain data table.

**Avoid when:** Structured row/column comparison is primary (use Data Tables), hierarchical folder navigation needs Tree View, or one record is the only focus.

**Ownership:** The pattern owns item anatomy, density, grouping, ordering, loading strategy and collection-to-detail interaction. Data services own filtering, rankings, cursors, freshness, permissions and mutation effects.

## Journey and state contract

| Stage | User-facing decision and state | Failure and recovery expectation |
| --- | --- | --- |
| Choose representation | Identify the user's primary job: scan, compare, identify, select, read updates or act on items. | Avoid implying cards are always better than a semantic list or table. |
| Load collection | Show loading, loaded, genuinely empty, filtered-empty and permission-limited states. | Do not call stale cached content current or an outage 'No items'. |
| Navigate / refine | Display stable item identity, summaries, optional facets, sort/filter and position context. | Keyboard focus follows logical order; maintain route and filter state where justified. |
| Act / inspect | Clearly separate selection from navigation and item-level commands. | Preserve selection and detail context through updates, sorting and async failures. |
| Extend / refresh | Choose pagination, load more, virtualized scrolling or feed updates from task evidence. | Avoid scroll jumps, lost position and inaccessible content loaded beyond the viewport. |

## Decision rules and tradeoffs

- Select semantic list, table, grid or feed structure based on task and data relationships. Visual cards do not mandate ARIA grid semantics.
- Define minimal item anatomy: unique label, distinguishing attributes, status, actions and optional imagery with truthful fallbacks.
- Make sorting, filtering and recommendation criteria understandable; disclose when feed order changes due to personalization rather than chronology.
- Use stable item IDs and preserve focus, scroll and selected record when new results arrive or items are deleted.
- Choose pagination/load more/infinite scroll deliberately: consider footer access, keyboard cost, history restoration, memory and screen-reader navigation.
- Use virtualization only with verified item count/position semantics and focus recovery; a fast demo is not evidence of accessible traversal.

## Interaction, accessibility, layout and localization

- A collection must have an accessible name, meaningful item labels and a predictable reading order independent of card decoration.
- Links navigate to detail; buttons act; selection controls declare scope. Avoid making an entire clickable card contain nested conflicting buttons.
- Provide keyboard-accessible loading and end-of-results behavior; do not unexpectedly move focus when new items arrive or content is removed.
- Support narrow layouts, images with relevant alternatives, bidi text, long localized metadata, flexible density and contrast without hiding actions on hover alone.

Use semantic tokens for text, status, surfaces and focus; verify theme/high contrast, reduced motion, text growth, zoom and RTL in consuming products. All asynchronous success claims must reflect authoritative outcomes rather than purely optimistic presentation.

## Example and anti-example

**Illustrative example:** A product library defaults to a list for scanning titles, offers an optional gallery for visual browsing, retains filters and scroll after inspection, and uses Load more with a clear result count.

**Anti-example:** An infinite feed constantly inserts new cards above the current focus, hides navigation to the footer and uses unlabeled card tiles with several nested click handlers.

## Evidence and verification

| Scenario | Evidence required | Status |
| --- | --- | --- |
| List/grid mode choice, visual density and content hierarchy comprehension | Document executed task, device/assistive technology, product authority, result and limitations | NOT VERIFIED |
| Filtering/sorting/pagination transitions and stable selected item behavior | Document executed task, device/assistive technology, product authority, result and limitations | NOT VERIFIED |
| Virtualization, keyboard order, end-of-results and responsive images | Document executed task, device/assistive technology, product authority, result and limitations | NOT VERIFIED |
| Permission-limited records, real-time insert/remove and RTL/zoom | Document executed task, device/assistive technology, product authority, result and limitations | NOT VERIFIED |

This is a proposed conceptual pattern. No released editor, live data service, production behavior, user study or accessibility certification is supplied. Actual capability, legal/data handling and risk limits require review.

## Sources, applicability and related concepts

- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — reference context; verify current edition and applicability.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — reference context; verify current edition and applicability.
- Related canonical concepts: [Data tables](data-tables.md), [Search and filtering](search-and-filter.md), [Master-detail](master-detail-exploration.md), [Real-time updates](real-time-data-and-live-updates.md).
- **Scope limit:** A product-specific feature must own real data persistence, authorization and performance verification.
