# Hierarchical tree view

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and fit

Explore or select items in a nested hierarchy with expandable branches and a coherent focused-item model.

**Use when:** Users need to work with a large meaningful hierarchy such as folders or categories and nested levels matter.

**Avoid when:** A small hierarchy is clearer as nested headings/links, or a data table/treegrid is required for columns and edits.

## Ownership and decision rules

The tree view owns hierarchy exposure, expansion, active item and keyboard navigation; the feature owns loading, selection meaning, drag/move permission and destination.

- Choose navigation tree versus selection tree; clarify whether focus and selection are the same.
- Provide accurate level, position, set-size and expanded states, especially for lazy-loaded branches.
- Keep selected descendant context visible when collapsing a parent; handle focus when branches are removed or filtered.
- Avoid drag-only reparenting: offer accessible move controls or another equivalent workflow.

## States and anatomy

Expose a persistent or programmatically associated name, meaningful control and content slots, visible focus, and semantic token-based visual states; do not invent product-side behavior in the component.

| State | Visible behavior | Semantic / accessibility expectation |
| --- | --- | --- |
| Collapsed branch | Children hidden; parent still available | Expansion and level exposed |
| Expanded branch | Children in correct logical order | Treeitem hierarchy and ownership correct |
| Loading branch | Pending children not mistaken for empty | Status available without focus loss |
| Selected/removed | Focus/selection recover to visible item | No orphaned active descendant |

## Keyboard, focus and inclusive operation

- Arrows navigate visible treeitems, Right expands/moves into a branch, Left collapses/moves to parent according to APG.
- Home/End reach first/last visible item; Enter/Space activation/selection is explicitly specified.
- Typeahead behavior is optional but, if provided, must not interfere with assistive technology.

Test at narrow widths and high zoom, with long translated labels, mixed LTR/RTL text, available input methods, high contrast and reduced-motion preferences. Use scoped styling and stable semantic design tokens rather than fixed positioning and raw values.

## Example / anti-example

**Illustrative example:** An archive explorer exposes folder hierarchy, preserves expanded branches and offers keyboard-accessible selection.

**Anti-example:** Presenting dozens of nested clickable divs with no expanded states, no focus indicator and drag-only moves.

## Evidence and verification

| Scenario | Expected observation | Status |
| --- | --- | --- |
| Expand/collapse, selection versus focus, lazy loading | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |
| Keyboard/APG tree traversal and screen reader structure | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |
| Deep hierarchy, long RTL names, virtualization and zoom | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |

The contract is guidance only: no runnable implementation, tested cross-browser interoperability, editorial approval, or WCAG conformance is claimed.

## Sources, limitations and related concepts

- Behavior reference: [platform or WAI guidance](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/); confirm edition, browser support and applicability before adopting custom semantics.
- Accessibility target: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), not an assertion of conformance.
- Related canonical sources: [Component contracts](../../../knowledge/architecture/component-contracts.md), [Accessibility](../../../knowledge/guidance/accessibility.md), [Design tokens](../../../knowledge/foundations/design-tokens-and-themes.md), [Interaction recovery](../../patterns/interaction-states-and-recovery.md).

## Decision example and verification boundary

**Illustrative scenario (not a user study):** Type ahead to an expanded tree item, collapse its parent and move focus to a visible ancestor. The consumer owns product data and permissions; the shared specification owns semantic behavior, presentation and focus. Choose simpler native controls where they satisfy the user task.

**Acceptance evidence to collect:** Check Arrow keys, typeahead, expansion, virtualized items and focus persistence. Record tool/browser, owner, expected versus observed behavior, locale and unresolved cases; actual runtime results remain **NOT VERIFIED** until executed.

**Source applicability:** [Relevant W3C guidance](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/) informs the interaction choices, not production conformance or independent review. Keep implementation-specific details with the consumer.

