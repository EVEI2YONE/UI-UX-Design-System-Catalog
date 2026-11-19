# Popover and non-modal overlay

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and fit

Present contextual interactive content without modal background blocking. This differs from both a tooltip and a dialog.

**Use when:** A nearby control needs a compact form, selection surface or contextual explanation that may contain interactive elements.

**Avoid when:** The task requires isolated attention and blocked background interaction (use Dialog) or only short noninteractive text (use Tooltip).

## Ownership and decision rules

The overlay owns trigger, relationship, positioning, dismissal and focus rules; the consumer owns commands, validation, persistence and permission state.

- Explicitly choose non-modal versus modal behavior and do not apply dialog-style focus trapping to all popovers.
- Determine whether content remains in the DOM on close and where focus moves when the trigger or popover is removed.
- Keep overlay readable at zoom and narrow width, avoiding clipping by scroll containers; support direction-aware placement.
- Treat outside click, Escape, navigation and successful command dismissal as separate decisions; do not discard unsaved data silently.

## States and anatomy

Expose a persistent or programmatically associated name, meaningful control and content slots, visible focus, and semantic token-based visual states; do not invent product-side behavior in the component.

| State | Visible behavior | Semantic / accessibility expectation |
| --- | --- | --- |
| Closed | Trigger remains discoverable | Expanded/controls relationship truthful |
| Open | Content positioned and interactive | Focus enters only where intended |
| Validation error | Open overlay retains entered data | Error connected to input |
| Dismissed/trigger removed | Focus returns to viable context | No keyboard trap or orphaned focus |

## Keyboard, focus and inclusive operation

- Trigger activation opens with pointer or keyboard; Escape closes when appropriate.
- Tab follows document/focus policy for non-modal content; Arrow behavior only for an actual composite widget.
- Avoid click-away dismissal while focus is in the overlay or an associated nested surface.

Test at narrow widths and high zoom, with long translated labels, mixed LTR/RTL text, available input methods, high contrast and reduced-motion preferences. Use scoped styling and stable semantic design tokens rather than fixed positioning and raw values.

## Example / anti-example

**Illustrative example:** A Filter button opens a non-modal panel with checkboxes and Apply/Reset actions; the page remains navigable.

**Anti-example:** Implementing a popover with a global focus trap while claiming that users can continue interacting with the page.

## Evidence and verification

| Scenario | Expected observation | Status |
| --- | --- | --- |
| Open/close, outside interaction and Escape | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |
| Focus on nested input, validation error and trigger removal | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |
| RTL positioning, zoom/reflow, screen reader and touch | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |

The contract is guidance only: no runnable implementation, tested cross-browser interoperability, editorial approval, or WCAG conformance is claimed.

## Sources, limitations and related concepts

- Behavior reference: [platform or WAI guidance](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API); confirm edition, browser support and applicability before adopting custom semantics.
- Accessibility target: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), not an assertion of conformance.
- Related canonical sources: [Component contracts](../../../knowledge/architecture/component-contracts.md), [Accessibility](../../../knowledge/guidance/accessibility.md), [Design tokens](../../../knowledge/foundations/design-tokens-and-themes.md), [Interaction recovery](../../patterns/interaction-states-and-recovery.md).
