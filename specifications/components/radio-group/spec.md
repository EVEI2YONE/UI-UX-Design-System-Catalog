# Radio group

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and fit

Choose exactly one option from a set of mutually exclusive options. Native radios in a named group are the default implementation.

**Use when:** The choices are few, understandable together, and selecting one excludes all others.

**Avoid when:** Independent multiple selection needs Checkboxes, or an on/off setting needs an explicit Switch contract.

## Ownership and decision rules

The group owns label, description, mutually exclusive checked state, and focus semantics; the feature owns meaning, requiredness and submission.

- Use a fieldset and legend for related native radios when practical; associate help and error text with the group.
- Choose a safe default only when user intent is established; a forced preselection can bias consequential choices.
- Make entire labels operable, maintain consistent order, and keep disabled reasons understandable.
- Reserve custom radio widgets for a proven layout constraint and follow the APG roving-focus/checked model.

## States and anatomy

Use a visible label, relevant description/error association, semantic control surface and theme-backed focus indicator. Expose only task-justified variants.

| State | Visible behavior | Semantic / accessibility expectation |
| --- | --- | --- |
| Unselected | No choice made, when optional or awaiting intent | Group label and requiredness identifiable |
| Selected | Exactly one choice is checked | Checked state programmatically exposed |
| Disabled choice | Unavailable without suggesting it can be selected | Preserve meaning and explain as needed |
| Invalid group | Error points to the choice group, not a generic page | Recovery works without losing other answers |

## Keyboard, focus and inclusive operation

- Native radio groups use standard Tab and arrow-key interactions; do not replace them with clickable divs.
- Custom groups must document orientation, arrow navigation, Space activation and focus management.

Use semantic tokens for text, surface, border, spacing and focus. Test long translations, locale-sensitive formatting where applicable, RTL, narrow containers, pointer/touch alternatives, high contrast, zoom/reflow and reduced motion. Never infer compliance from this document.

## Example / anti-example

**Illustrative example:** A form asks whether the address is home, work, or other; one choice can be selected at a time.

**Anti-example:** Rendering independent checkboxes for mutually exclusive answers or preselecting agreement by default.

## Evidence and verification

| Scenario | Expected observation | Status |
| --- | --- | --- |
| Mutual exclusivity, labels/legend and group errors | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |
| Keyboard-only navigation, long text and high contrast | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |
| RTL order and touch-target clarity | Demonstrated in an actual consuming application or independently tested reference | NOT VERIFIED |

No executable component, browser test result, product user study or accessibility certification is delivered by this specification. Before adoption, identify a reviewer, record tested platforms and link implementation evidence.

## Sources, limitations and related concepts

- Primary behavior reference: [authoritative platform guidance](https://www.w3.org/WAI/ARIA/apg/patterns/radio/); apply the exact pattern that fits the chosen implementation, rather than copying ARIA into native controls.
- Accessibility target: [WCAG 2.2](https://www.w3.org/TR/WCAG22/); compatibility and conformance require independent checks.
- Existing canonical guidance: [Component contracts](../../../knowledge/architecture/component-contracts.md), [Accessibility](../../../knowledge/guidance/accessibility.md), [Design tokens](../../../knowledge/foundations/design-tokens-and-themes.md), and [Forms](../../patterns/forms.md).
- Review applicability, browser/assistive technology support, and any documented APG variants before implementing. Guidance is proposed and may change after expert review.

## Decision scenario, evidence and acceptance

**Decision:** Use Radio Group when one of several visible options is required; keep selection constraints at the form level.

**Illustrative scenario (not a completed study):** Submit a required delivery-choice group empty; expose a group-level error, move to the group without surprise selection, then clear the error after explicit choice.

**Acceptance:** Check native fieldset/legend or equivalent, Arrow/Space behavior where applicable, focus order and long localized labels. Record the environment, owner, expected/actual results and evidence links; until executed, runtime outcomes remain **NOT VERIFIED**.

**Source scope:** [Applicable reference](https://www.w3.org/WAI/ARIA/apg/patterns/radio/) informs the design decision. APG offers interaction patterns; native semantics and actual behavior depend on platform. A reference is not proof of adoption, conformance or an independent review.

