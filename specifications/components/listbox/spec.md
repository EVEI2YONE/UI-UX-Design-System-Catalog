# Listbox and multi-select options

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Present a selectable list of options with a single- or multiple-selection model, distinct focus and selection state, and predictable keyboard interaction. A listbox is a composite widget, not a collection of arbitrary clickable cards.

**Use when:** Options must be selected within a compact list-like widget, and native select behavior cannot meet a demonstrated interaction need.

**Avoid when:** A small exclusive choice set works as Radio Group, independent selections work as Checkboxes, a searchable input needs Combobox, or a rich card grid is required.

**Ownership:** The control owns option semantics, active/focused item, selection model, labels, scrolling and keyboard behavior. The consuming feature owns option identity, availability, permissions, search/ranking and the meaning of committed selections.

## Decision framework and variants

| Variant | Fit | Required behavior | Main risk |
| --- | --- | --- | --- |
| Native select, single | Simple known options | Prefer native semantics, keyboard behavior and platform menu. | Custom listbox adds cost without demonstrated benefit. |
| Native select, multiple | A limited set with a clear platform multi-select interaction | Use only when discoverable and operable for intended users. | Desktop modifier-key patterns may be unfamiliar or inaccessible. |
| Custom single-select listbox | A styled visible list with specific selection behavior | Define whether selection follows focus and whether activation commits immediately. | Avoid accidentally committing on arrow navigation when navigation is expected. |
| Custom multi-select listbox | Many selectable options with explicit multi-selection behavior | Choose APG recommended no-modifier model or clearly document modifier model. | Focus and selected state must be separate. |
| Virtualized or async options | Very large, loading or changing collections | Document real option count/position, focus retention and pending/empty states. | Never let virtualization strand the active descendant. |

## Component contract

- Use native select where practical; custom listbox semantics are justified only after documenting product and accessibility needs.
- Label listbox and option groups; maintain stable option identity, current selection, active/focused option and disabled/unavailable distinction.
- Declare single versus multiple selection and whether focus automatically changes selection, especially when selection causes costly side effects.
- In multiple selection, define Space toggle, optional range selection and Ctrl/Shift behavior according to a coherent APG model; never mix incompatible models.
- Provide typeahead if it meaningfully improves large-list selection, while preserving IME and assistive-technology typing behavior.
- Do not place interactive buttons, links or form controls inside an ARIA option; use a different composite pattern when every row needs actions.
- For long or remote lists, maintain logical item position and keyboard visibility with scrolling; handle options disappearing on data refresh.

## States and semantics

| State | Visible presentation | Programmatic / interaction expectation |
| --- | --- | --- |
| Unfocused, none selected | Clear list label and optional descriptive help | Role/name relationship and proper option semantics |
| Focused active option | Visible focus/active cue distinct from selection | One coherent DOM-focus or active-descendant model |
| Selected option(s) | Visible selection summary and individual state | Correct selected values exposed without relying on color |
| Disabled/unavailable option | Legible, nonselectable, reason when useful | Disabled state and focus policy documented |
| Pending or empty options | Loading and true no-options messages distinguished | No false option selected while fetching |
| Removed/filtered selected option | Safe fallback or preserved authorized selection policy | No orphaned focus or stale committed value |

## Keyboard, focus, accessibility and localization

- Tab enters/exits the widget without forcing a selection. Arrow keys traverse options; Home/End behavior follows selected APG variant.
- Single-select Space/Enter behavior depends on the chosen selection-follows-focus model; distinguish movement from commit.
- Multi-select models require explicit Space to toggle as appropriate, with range and modifier-key behavior documented and discoverable.
- Listbox popup behavior inside a Combobox is governed by Combobox's input/popup focus model; do not apply a standalone listbox policy blindly.

Use semantic tokens for focus, surfaces, text and state, and distinguish meaning beyond color or movement. Validate long translated labels, bidi/RTL content, 200–400% zoom/reflow, high contrast, touch access and reduced motion for the chosen variant. Actual native support and custom assistive-technology behavior must be tested, not inferred from markup alone.

## Example and anti-example

**Illustrative example:** A permissions form offers a visible list of allowed project reviewers with multi-select, keyboard toggling and a clear selected-count summary; disabled reviewers are explained without being selectable.

**Anti-example:** Arrowing down a custom multi-select list silently changes the committed access list, while its accessible selected state remains stale.

## Evidence and verification

| Scenario | Required observation | Status |
| --- | --- | --- |
| Single/multiple APG keyboard models, focus versus selected distinction | Record actual browser, assistive-technology, feature and environment evidence before claiming the contract holds | NOT VERIFIED |
| Disabled, grouped, loaded and dynamic-option behavior | Record actual browser, assistive-technology, feature and environment evidence before claiming the contract holds | NOT VERIFIED |
| Typeahead, IME, long labels, large/virtualized list and narrow/mobile input | Record actual browser, assistive-technology, feature and environment evidence before claiming the contract holds | NOT VERIFIED |
| Screen reader role/name/value, high contrast and RTL | Record actual browser, assistive-technology, feature and environment evidence before claiming the contract holds | NOT VERIFIED |

This document defines a proposed conceptual contract. It does not supply executable source, an independently reviewed design, validated production behavior or accessibility certification.

## Sources, applicability and related concepts

- [WAI-ARIA Listbox pattern](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/) — normative or reference context; verify which behavior applies to the chosen native/custom implementation.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — normative or reference context; verify which behavior applies to the chosen native/custom implementation.
- Related canonical sources: [Select](../select/spec.md), [Combobox](../combobox/spec.md), [Radio group](../radio-group/spec.md), [Checkbox](../checkbox/spec.md), [Accessibility](../../../knowledge/guidance/accessibility.md).
- **Scope limit:** Product data, permission enforcement, persistence and backend lifecycle remain feature-owned, not component-owned.

## Decision example and verification boundary

**Illustrative scenario (not a user study):** Choose multiple items with a defined selection model, type ahead and refresh options without silently changing selection. The consumer owns product data and permissions; the shared specification owns semantic behavior, presentation and focus. Choose simpler native controls where they satisfy the user task.

**Acceptance evidence to collect:** Check typeahead, roving focus, modifier rules, disabled options, selection/focus distinction and announcements. Record tool/browser, owner, expected versus observed behavior, locale and unresolved cases; actual runtime results remain **NOT VERIFIED** until executed.

**Source applicability:** [Relevant W3C guidance](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/) informs the interaction choices, not production conformance or independent review. Keep implementation-specific details with the consumer.

