# Search and filtering

**Kind:** specification · **Status:** proposed · **Primary layer:** patterns

## Purpose and use boundary

Let users locate relevant items, refine results and recover from unsuccessful queries. **Use** when a collection or content set needs findability beyond a short visible list. **Avoid** adding search to tiny option sets that are clearer when directly displayed.

## Composition and ownership

Compose a labeled [Input](../components/input/spec.md), optional [Select](../components/select/spec.md)/[Checkbox](../components/checkbox/spec.md) filters and [Button](../components/button/spec.md) actions. Product code owns indexing, search security, query semantics, pagination and server-side filtering. Result cards and tables belong to domain views rather than the search input component.

## Interaction state contract

| State | User-facing behavior | Recovery/measurement |
| --- | --- | --- |
| First use | Describe what can be searched and any relevant defaults | Accessible hint and meaningful submit/clear |
| Pending | Keep current query and filters; indicate updates | Avoid flicker or hiding context |
| Results | Show match count or context, selected filters, clear action | Preserve query in navigation when appropriate |
| No matches | Distinguish valid zero results from system error | Suggest edits and reset filters |
| Error / timeout | State outcome uncertainty and retry option | No filter/query loss |
| Partial / paged results | Expose additional results predictably | Correct result count and position |

Do not assume debounce, autocomplete or fuzzy matching is always needed. If suggestions are implemented, define keyboard/active-descendant and dismissal behavior separately; a custom combobox is not just a decorated Input.

## Inclusive, locale and theme contract

Label search and filter groups, expose active selections beyond color, support keyboard removal of filter chips, and announce meaningful updates without noisy live regions. Normalize/search text in a locale-appropriate way where supported and avoid assuming left-to-right queries. Support reflow, long localized filter labels, semantic focus/surface tokens and reduced motion.

## Examples and verification

**Illustrative good:** A user can filter a results collection, inspect an item, return with filters preserved, and reset from a zero-result state. **Anti-example:** A silent failed request displays an empty list identical to a valid zero-match response.

| Check | Status | Evidence needed |
| --- | --- | --- |
| Query/filter task review | NOT VERIFIED | User need, semantics, query capability |
| Keyboard and announcements | NOT VERIFIED | Search and optional suggestion flows |
| Zero/error/timeout/partial results | NOT VERIFIED | Integration and recovery checks |
| Translation, RTL, narrow layout | NOT VERIFIED | Representative long labels |

**Canonical ID:** `pattern.search-filter` · **Owner:** unassigned · **Review date:** not reviewed · **Migration:** preserve query/deep-link semantics and avoid unnecessary custom widgets. Documentation-only.

Related: [task flows](task-flows-and-information-architecture.md), [recovery](interaction-states-and-recovery.md), [measurement](../guidance/ux-measurement.md), [accessibility](../guidance/accessibility.md). Standards: [WCAG 2.2](../governance/references.md).

## Batch 8 extension — discovery, sorting and result semantics

### Choose the discovery model

**Search** retrieves candidate records from a query. **Filters/facets** constrain a collection using structured attributes; a **sort** changes ordering, not eligibility. Users may need any combination; do not add all controls by default. Identify first whether people begin with an exact identifier, descriptive words, known categories, or browsing. Test vocabulary and domain data before committing to a query model.

| Scenario | Guidance | Failure to avoid |
| --- | --- | --- |
| Known identifier or exact record | Offer a narrow labeled lookup, then show an identifiable, authorized match | Redirecting straight into a sensitive record without context |
| Open-ended discovery | Query matching, understandable relevance, category navigation and optional facets | Undocumented matching or opaque “best” ranking |
| Very large results | Meaningful summary, useful facets and predictable pagination/load-more as justified | Result count that describes a different query/filter state |
| Repeated refinements | Show applied filters as text; allow one-by-one removal and clear-all | Hidden filters or a reset that does not actually clear the query |
| Sorting | Explicit sort label and selected order; stable, documented defaults | Quietly reshuffling results without announcing a new order |
| Zero matches | Distinguish query mismatch, restrictive filters and genuine empty collections | Calling an outage “No results” |
| Error / timeout | Preserve criteria and known previous results without presenting stale data as current | Empty list with no failure explanation |

### Apply filters deliberately

Decide between **explicit Apply** and **live filtering** based on response time, number of controls, accessible announcement load, and evidence from actual users. Explicit Apply is often safer for long/filter-heavy tasks, particularly on mobile. If live filtering is used, keep focus stable, avoid layout shifts and announce the changed results unobtrusively. Preserve a clear distinction between **edited but not applied** and **currently applied** criteria.

Test narrow screens with filter controls closed/open and results visible; make applied conditions perceivable even when a filter panel is collapsed. Persist query and filters in a shareable URL only when doing so does not expose confidential inputs.

### Results and pagination contract

Each result should show enough safe distinguishing context to support selection, not more sensitive information than authorized. Explain why highlights or matches appear when useful and never use color alone. Keep selected sort, result count, page/position and applied criteria coherent. When returning from a detail page, preserve the query context and position when feasible. If the dataset changes during pagination, describe the changed result context instead of misleading totals.

**Example (illustrative):** “24 records. Status: Pending. Sorted: Newest first.” A user removes Pending, sees an updated count, inspects a record and returns to the same search state.

**Anti-example:** Typing triggers five overlapping network requests; an older response overwrites newer results, pagination silently resets, and the UI announces “0 results” after a network error.

### QA and boundaries

- Exact, misspelled, empty and overly broad queries; permission-limited results; multi-filter empty states; clear/reset and sorting transitions.
- Loading/error/cancelled/out-of-order responses; query persistence across refresh and back/forward; long localized terms and RTL.
- Keyboard and touch control operation, accessible names, focus after results change, careful live status announcements.
- Search ranking and performance remain owned by the product backend. No claim of search quality is possible without evaluation on representative data and users.

**Sources (reviewed 2026-11-07):** [USWDS search](https://designsystem.digital.gov/components/search/) and [pagination](https://designsystem.digital.gov/components/pagination/); [DWP filters design notes](https://design-system.dwp.gov.uk/contribute/filters/design-notes) is contextual and research in progress, not universal policy; [Scottish Government search filters](https://designsystem.gov.scot/patterns/search-results/search-filters) demonstrates applied criteria and mobile options.

Related guidance: [content design](../guidance/content-design-and-ux-writing.md), [service recovery](service-recovery-and-support.md).
