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

## Actionable record cards and related-item disclosure

A card is a composition of **one obvious primary task** and optional secondary controls. Decide whether activating the card navigates, selects, expands or executes a command; do not make a parent card clickable when it contains independent buttons or links.

| Structure | Use when | Constraint and alternative |
| --- | --- | --- |
| Title link to detail | Item inspection is primary and card has other controls | Explicit anchor with descriptive name; no redundant "Open" beside it |
| Named detail button | Non-navigation detail subview is the primary action | Explain destination/state and maintain focus on return |
| Whole-card link | Entire card has **one** action and no nested interactive descendants | Never wrap menu, checkbox or nested links in it |
| Inline disclosure | Related preview is short and does not require independent route/edit history | Button communicates expanded state; use [Disclosure](../components/disclosure/spec.md) |
| Visible Add/Edit | Frequent, high-value action | Do not bury it in overflow just to simplify appearance |
| Labeled overflow menu | Infrequent authorized actions such as Archive or Delete | Follow [Menu button](../components/menu-button/spec.md); preserve focus when record vanishes |

**Card anatomy:** identity and current scope -> clear title/detail affordance -> one-line purpose or status -> two or three meaningful metadata items -> optionally a bounded related-record preview with "View all" -> primary/secondary actions. Keep totals labeled with unit/period/scope; no metric or empty preview purely for decoration. Separate navigation, selection, expansion and commands as distinct semantic controls with non-overlapping hit areas. The container may receive hover/focus styling, but hover must not be the only way to discover essential commands.

**Prose variants (illustrative, not rendered):**
- **Compact narrow card:** wrapped title link, status beneath, one high-value action, labeled overflow menu, at most one related-item preview line plus "View all". At 320px and zoom, let actions wrap, avoid truncating the only identifier, and preserve logical focus order.
- **Wide summary card:** title/link and status followed by short summary, count/last activity where meaningful, a bounded list of related items, visible common action and overflow for rarer actions. Preview entries with independent destinations are explicit links, not nested card-wide links.
- **No secondary actions:** one simple title or whole-card link, no empty menu button or duplicate detail control. When many related items exist, show a count and a clear destination rather than a long interactive stack inside the card.

**States:** Loading reserves a readable status without phantom controls; zero related items offers a relevant Add only when authorized; partial/permission-limited counts state the scope; overflow and many-related summaries truncate visually only with a full accessible label or detail route; failed/unknown mutations preserve context and do not imply success. If an item disappears after action, restore focus to a surviving neighbor, collection heading or status, retaining filters and selection. [Master-detail](master-detail-exploration.md) owns item-to-list return; [Component contracts](../../knowledge/architecture/component-contracts.md) owns event/state boundaries; [recovery](interaction-states-and-recovery.md) owns uncertain outcomes.

**Correct route:** Open a title link, update a related record, then return to the filtered collection with focus at the originating item or a sensible fallback. **Anti-example:** A clickable `<article>` card wraps a nested "Open" button, related links and an ellipsis menu; pointer bubbling triggers both navigation and archive.

**Acceptance (product behavior NOT VERIFIED):** Check one primary target, independent actions, keyboard Tab/Enter/Space, menu Escape, focus after removal, target sizing, narrow/zoom/reflow, long locale text and RTL. Record which detail destination is restored and whether no-items, partial, permission-limited, failure and unknown states are distinguishable. [WAI-ARIA APG Menu Button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/) specifies applicable menu semantics; [WCAG 2.2](https://www.w3.org/TR/WCAG22/) informs keyboard, focus and target-size criteria. Neither proves this prose example works in a product.

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

## Representative state and recovery acceptance

**Illustrative decision case:** Test a large collection with focus restoration and meaningful filters. Define what the user intends, when the system has authoritative knowledge, how to distinguish a pending or unknown outcome and what preserves their work and orientation. Avoid promoting this task-specific orchestration into a generic component unless independently reusable.

**Evidence contract:** Verify both the normal route and the failure branch with explicit expected and observed results for applicable keyboard, focus, reflow, language and permission conditions. Record the owner, tested environment, findings and unresolved risks; until run, the check is **NOT VERIFIED**. [WCAG 2.2](https://www.w3.org/TR/WCAG22/) offers applicable accessibility criteria, not proof of task success or certification.

