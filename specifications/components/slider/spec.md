# Slider and bounded range control

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and fit

Allow approximate or stepped numeric value selection on a known scale, with a readable current value and an alternate way to input precise values when needed.

**Use when:** The relationship between minimum, maximum, and relative position matters and pointer adjustment is useful.

**Avoid when:** Exact entry of a critical value is required, the scale is misleading, or the user must compare discrete named options better served by radios.

## Ownership and decision rules

The control owns thumb, track, value display, constraints and keyboard semantics; the feature owns units, business limits and consequences of value updates.

- Declare min, max, step, current value, units and direction; never use arbitrary non-linear scales without explicit explanation.
- Prefer native range inputs where practical. Expose a nearby exact-value input if precision or motor access requires it.
- Define whether updates are immediate previews or committed on release; debounce heavy effects without making state ambiguous.
- For RTL, verify physical arrow-direction expectations for this specific scale and platform rather than blindly mirroring meaning.

## States and anatomy

Expose a persistent or programmatically associated name, meaningful control and content slots, visible focus, and semantic token-based visual states; do not invent product-side behavior in the component.

| State | Visible behavior | Semantic / accessibility expectation |
| --- | --- | --- |
| Default/value | Thumb location and formatted value agree | Name, value and range exposed |
| Focused/dragging | Visible focus and current value | Keyboard and pointer alternatives |
| Boundary/invalid | No unannounced values outside limits | Explicit min/max/step |
| Disabled/pending | Reason or pending effect understandable | State consistent with actual ability |

## Keyboard, focus and inclusive operation

- Arrows adjust by defined increments; Home/End reach bounds as appropriate.
- PageUp/PageDown can adjust larger increments when sensible; do not require dragging.
- Touch, keyboard and assistive input must reach equivalent settings.

Test at narrow widths and high zoom, with long translated labels, mixed LTR/RTL text, available input methods, high contrast and reduced-motion preferences. Use scoped styling and stable semantic design tokens rather than fixed positioning and raw values.

## Example / anti-example

**Illustrative example:** A noncritical visual density preview offers a slider and editable numeric value with labeled range.

**Anti-example:** A price slider with no numeric labels that makes it impossible to enter an exact budget.

## Evidence and verification

| Scenario | Expected observation | Status |
| --- | --- | --- |
| Min/max/step, units and displayed value consistency | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |
| Keyboard and screen reader value changes; pointer cancellation | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |
| RTL, zoom, touch target and high contrast | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |

The contract is guidance only: no runnable implementation, tested cross-browser interoperability, editorial approval, or WCAG conformance is claimed.

## Sources, limitations and related concepts

- Behavior reference: [platform or WAI guidance](https://www.w3.org/WAI/ARIA/apg/patterns/slider/); confirm edition, browser support and applicability before adopting custom semantics.
- Accessibility target: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), not an assertion of conformance.
- Related canonical sources: [Component contracts](../../../knowledge/architecture/component-contracts.md), [Accessibility](../../../knowledge/guidance/accessibility.md), [Design tokens](../../../knowledge/foundations/design-tokens-and-themes.md), [Interaction recovery](../../patterns/interaction-states-and-recovery.md).

## Decision example and verification boundary

**Illustrative scenario (not a user study):** Set a coarse value with arrow keys and switch to explicit numeric entry for precision beyond the slider step. The consumer owns product data and permissions; the shared specification owns semantic behavior, presentation and focus. Choose simpler native controls where they satisfy the user task.

**Acceptance evidence to collect:** Check range/value text, increment semantics, Home/End, touch alternative, number entry and error states. Record tool/browser, owner, expected versus observed behavior, locale and unresolved cases; actual runtime results remain **NOT VERIFIED** until executed.

**Source applicability:** [Relevant W3C guidance](https://www.w3.org/WAI/ARIA/apg/patterns/slider/) informs the interaction choices, not production conformance or independent review. Keep implementation-specific details with the consumer.

