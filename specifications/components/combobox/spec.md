# Combobox and autocomplete

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and fit

Select an option from an associated suggestion popup while optionally entering a query. This contract covers the relationship between typed text, suggested items, and committed value; it does not own the product search service.

**Use when:** A constrained option set is large enough that typing improves finding a choice, and suggestions have clear selection semantics.

**Avoid when:** A native Select meets the task, a free-text Input is sufficient, or a search-results page is more appropriate.

## Ownership and decision rules

The component owns input, popup, active-option semantics and visual state. The consuming feature owns suggestions, remote ranking, option identity, permissions and result validation.

- Define whether the value must match a listed option, permits a custom value, or selects a committed object; do not silently equate typed text with selection.
- Specify listbox, grid, tree or dialog popup behavior before building custom ARIA; reuse a native control whenever it adequately meets requirements.
- Keep query, active descendant, highlighted option, selected value, no-results and pending states independent.
- For remote suggestions, debounce judiciously, cancel stale responses, preserve typed text and never report an unconfirmed option as selected.

## States and anatomy

Use a visible label, relevant description/error association, semantic control surface and theme-backed focus indicator. Expose only task-justified variants.

| State | Visible behavior | Semantic / accessibility expectation |
| --- | --- | --- |
| Closed | Editable query or committed value remains legible | Name and expanded state clear |
| Open | Popup shows current suggestions and active option | Keyboard active descendant follows the chosen APG model |
| Loading or no results | Status distinguishes pending from empty | Non-disruptive status announcement |
| Invalid or unavailable | Keep entry and explain correction | Error linked to input |

## Keyboard, focus and inclusive operation

- Tab enters and exits the control without forcing a choice; Escape closes the popup without discarding a committed value.
- Arrow and Enter behavior follows the selected APG combobox variant; avoid simultaneous DOM focus in both input and listbox.
- Do not hijack text-editing shortcuts or rely on hover for the active choice.

Use semantic tokens for text, surface, border, spacing and focus. Test long translations, locale-sensitive formatting where applicable, RTL, narrow containers, pointer/touch alternatives, high contrast, zoom/reflow and reduced motion. Never infer compliance from this document.

## Example / anti-example

**Illustrative example:** In an employee directory, typing a name surfaces matching people; selection commits a stable person identifier, while an unmatched string remains a query.

**Anti-example:** Treating the first suggestion as automatically selected and submitting its identifier when the user typed only a partial query.

## Evidence and verification

| Scenario | Expected observation | Status |
| --- | --- | --- |
| Keyboard/screen reader with empty, filtered and loading states | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |
| Stale response and no-results handling; focus and Escape restoration | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |
| Long translated options, zoom/reflow, touch and RTL | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |

No executable component, browser test result, product user study or accessibility certification is delivered by this specification. Before adoption, identify a reviewer, record tested platforms and link implementation evidence.

## Sources, limitations and related concepts

- Primary behavior reference: [authoritative platform guidance](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/); apply the exact pattern that fits the chosen implementation, rather than copying ARIA into native controls.
- Accessibility target: [WCAG 2.2](https://www.w3.org/TR/WCAG22/); compatibility and conformance require independent checks.
- Existing canonical guidance: [Component contracts](../../../knowledge/architecture/component-contracts.md), [Accessibility](../../../knowledge/guidance/accessibility.md), [Design tokens](../../../knowledge/foundations/design-tokens-and-themes.md), and [Forms](../../patterns/forms.md).
- Review applicability, browser/assistive technology support, and any documented APG variants before implementing. Guidance is proposed and may change after expert review.
