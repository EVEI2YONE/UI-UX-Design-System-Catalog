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

**Canonical ID:** `component.select` · **Owner:** unassigned · **Review date:** not reviewed

Related: [Input](../input/spec.md), [Field](../field/spec.md), [accessibility](../../../knowledge/guidance/accessibility.md), [component contracts](../../../knowledge/architecture/component-contracts.md). Primary reference: [WAI-ARIA APG](../../../governance/references.md), when applicable to custom widgets.

## Decision scenario, evidence and acceptance

**Decision:** Prefer native Select for bounded options; use Combobox only when edit/search behavior justifies the added semantics.

**Illustrative scenario (not a completed study):** A country has no available regions. Show a meaningful empty/disabled reason, preserve the country and accommodate a long localized option label.

**Acceptance:** Check keyboard selection, no-option state, disabled choices, accessible name, option refresh and translated text without clipped meaning. Record the environment, owner, expected/actual results and evidence links; until executed, runtime outcomes remain **NOT VERIFIED**.

**Source scope:** [Applicable reference](https://www.w3.org/WAI/tutorials/forms/) informs the design decision. WAI covers form labeling, not the application option source. A reference is not proof of adoption, conformance or an independent review.

