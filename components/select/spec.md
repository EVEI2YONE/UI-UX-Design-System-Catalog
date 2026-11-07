# Select

**Kind:** specification · **Status:** proposed · **Primary layer:** components

## Purpose and fit

Choose one item from a bounded set of known options. **Use** a native select when it meets user needs and platform behavior. **Avoid** making a custom combobox merely for visual novelty, and avoid Select when all choices should remain visible (radio group) or free text is appropriate (Input).

## Ownership and contract

The shared Select owns option presentation, selected value, labels, disabled state, focus and keyboard semantics. The feature owns option sourcing, permissions, dependent-field behavior and validation. Illustrative API: `id`, `name`, `value`, `options` with stable value/label, `onChange`, `required`, `disabled`, accessible description/error linkage. An empty prompt option is not automatically a valid selection.

| State | Behavior | Verification |
| --- | --- | --- |
| Default / selected | Current selection and available choices understandable | Native keyboard and screen reader |
| Focus / open | Selection remains keyboard-operable | Platform keyboard behavior |
| Disabled option | Reason conveyed when important | No misleading selectable affordance |
| Invalid / empty | Corrective message and clear next step | Error association and form submit |
| Loading options | Explain unavailable choices; avoid false choices | Pending, stale and empty data |

**Custom widget exception:** Only with evidence native controls cannot meet the task; then specify roles, active option, typeahead, arrows, Escape, focus return, touch and screen-reader behavior against the WAI-ARIA APG. Do not assume native and custom controls have identical behavior.

## Tokens, responsiveness and localization

Use semantic surface/border/text/focus/error tokens and logical spacing. Do not truncate the essential selected value; test long localized options and mixed LTR/RTL content. A direction icon may mirror only when it represents navigation/direction and is reviewed for locale.

## Example and anti-example

**Illustrative:** A country field uses a labeled native select with an explicit unselected prompt and linked error. **Anti-example:** A custom div dropdown traps focus, cannot be controlled with a keyboard, and loses selection on network refresh.

## Evidence, scope and adoption

| Check | Status | Notes |
| --- | --- | --- |
| Contract review | NOT VERIFIED | No owner assigned |
| Keyboard, screen reader, touch | NOT VERIFIED | Platform-specific testing required |
| Options loading, invalid/empty and RTL | NOT VERIFIED | Consumer-specific |
| Theme/reflow and long labels | NOT VERIFIED | Consumer-specific |

**Canonical ID:** `component.select` · **Owner:** unassigned · **Review date:** not reviewed · **Migration:** prefer existing native behavior and consolidate divergent visual wrappers before introducing complex custom behavior. Proposed specification only.

Related: [Input](../input/spec.md), [Field](../field/spec.md), [accessibility](../../guidance/accessibility.md), [component contracts](../../architecture/component-contracts.md). Primary reference: [WAI-ARIA APG](../../governance/references.md), when applicable to custom widgets.
