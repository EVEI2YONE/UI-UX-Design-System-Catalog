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
