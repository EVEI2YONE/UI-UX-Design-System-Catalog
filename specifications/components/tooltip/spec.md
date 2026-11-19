# Tooltip

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and fit

Offer short, noninteractive supplementary information on hover or keyboard focus without turning it into a required step.

**Use when:** A concise clarification helps interpret an already understandable labeled control and can be dismissed without interaction.

**Avoid when:** The content contains buttons, links, warnings or essential instructions; use persistent text, disclosure or popover instead.

## Ownership and decision rules

The tooltip owns appearance, associated description, dismissal and placement; the consumer owns the wording and whether the hint is actually optional.

- Do not use a tooltip as the sole accessible name of an icon-only control unless the naming contract is explicitly implemented.
- Tooltip text is plain supporting content, not a mini-dialog. Interactive content requires a different pattern.
- Expose on keyboard focus as well as hover, keep it available when pointer moves over it as needed, and permit Escape dismissal.
- Avoid obscuring controls or content at small viewports and zoom; do not assume touch hover is possible.

## States and anatomy

Expose a persistent or programmatically associated name, meaningful control and content slots, visible focus, and semantic token-based visual states; do not invent product-side behavior in the component.

| State | Visible behavior | Semantic / accessibility expectation |
| --- | --- | --- |
| Hidden | Control meaning remains understandable | Accessible name intact |
| Visible | Short supplemental description readable | Description association not duplicated noisily |
| Dismissed | Escape/blur hides without changing control value | Focus remains on trigger |
| Clipped/narrow | Alternate placement or persistent content fallback | No essential instruction lost |

## Keyboard, focus and inclusive operation

- Tab focuses the triggering element; no separate tab stop belongs in a noninteractive tooltip.
- Escape dismisses without activating or moving focus.
- Hover alone must never be the only route to critical information.

Test at narrow widths and high zoom, with long translated labels, mixed LTR/RTL text, available input methods, high contrast and reduced-motion preferences. Use scoped styling and stable semantic design tokens rather than fixed positioning and raw values.

## Example / anti-example

**Illustrative example:** A clearly labeled export action has an optional tooltip describing the generated file format.

**Anti-example:** Placing the only explanation of a dangerous Delete action in a hover-only tooltip.

## Evidence and verification

| Scenario | Expected observation | Status |
| --- | --- | --- |
| Focus/hover/Escape and descriptive relationship | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |
| Screen reader announcement behavior, touch fallback | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |
| Overflow, text expansion, zoom and motion preferences | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |

The contract is guidance only: no runnable implementation, tested cross-browser interoperability, editorial approval, or WCAG conformance is claimed.

## Sources, limitations and related concepts

- Behavior reference: [platform or WAI guidance](https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/); confirm edition, browser support and applicability before adopting custom semantics.
- Accessibility target: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), not an assertion of conformance.
- Related canonical sources: [Component contracts](../../../knowledge/architecture/component-contracts.md), [Accessibility](../../../knowledge/guidance/accessibility.md), [Design tokens](../../../knowledge/foundations/design-tokens-and-themes.md), [Interaction recovery](../../patterns/interaction-states-and-recovery.md).
