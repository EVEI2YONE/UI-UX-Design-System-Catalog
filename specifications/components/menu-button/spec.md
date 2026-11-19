# Menu button and action menu

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and fit

Expose a compact group of actions through an explicitly labeled button and an associated menu. This is a command surface, not a generic list of links masquerading as an application menu.

**Use when:** A related set of infrequent actions belongs to one object or toolbar and visible buttons would overwhelm the primary task.

**Avoid when:** The choices are form values (use Select, Radio Group or Combobox), or primary navigation should remain visible as links.

## Ownership and decision rules

The menu-button component owns trigger, open state, item focus and dismissal; the feature owns command availability, authorization, mutation outcome and confirmation.

- Keep high-consequence actions discoverable and distinguish destructive actions by text, not only icon/color.
- Define whether menu items are commands, links, checkable items or nested submenus; do not mix roles without the corresponding keyboard model.
- Close on Escape, outside interaction when appropriate, and after action confirmation; preserve trigger and focus return.
- Prefer a plain set of visible buttons where there are only a few frequent actions. Avoid arbitrary menu nesting.

## States and anatomy

Expose a persistent or programmatically associated name, meaningful control and content slots, visible focus, and semantic token-based visual states; do not invent product-side behavior in the component.

| State | Visible behavior | Semantic / accessibility expectation |
| --- | --- | --- |
| Closed | Trigger names the action group | Expanded state false when exposed |
| Open | Menu and relevant enabled actions visible | Menu and item semantics match actual behavior |
| Unavailable item | Explain why command cannot be used when useful | Disabled state does not masquerade as a permission check |
| Command pending/failed | Maintain context or show status after menu dismissal | Focus and recovery are intentional |

## Keyboard, focus and inclusive operation

- Enter/Space/appropriate Arrow opens the menu according to chosen APG menu-button pattern.
- Arrow keys navigate menu items, Home/End optionally jump, Escape returns focus to trigger.
- Menu items perform commands; ordinary site navigation often needs regular links instead of application-menu semantics.

Test at narrow widths and high zoom, with long translated labels, mixed LTR/RTL text, available input methods, high contrast and reduced-motion preferences. Use scoped styling and stable semantic design tokens rather than fixed positioning and raw values.

## Example / anti-example

**Illustrative example:** A record's More actions button exposes Rename, Duplicate and Archive; Archive opens a consequence-aware confirmation.

**Anti-example:** A hamburger icon opens unlabelled divs whose hover handlers are the only way to activate actions.

## Evidence and verification

| Scenario | Expected observation | Status |
| --- | --- | --- |
| Keyboard open/navigation/close and focus return | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |
| Dynamic disabled items, destructive confirmations and async failures | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |
| Long labels, RTL placement, touch alternatives and zoom | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |

The contract is guidance only: no runnable implementation, tested cross-browser interoperability, editorial approval, or WCAG conformance is claimed.

## Sources, limitations and related concepts

- Behavior reference: [platform or WAI guidance](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/); confirm edition, browser support and applicability before adopting custom semantics.
- Accessibility target: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), not an assertion of conformance.
- Related canonical sources: [Component contracts](../../../knowledge/architecture/component-contracts.md), [Accessibility](../../../knowledge/guidance/accessibility.md), [Design tokens](../../../knowledge/foundations/design-tokens-and-themes.md), [Interaction recovery](../../patterns/interaction-states-and-recovery.md).
