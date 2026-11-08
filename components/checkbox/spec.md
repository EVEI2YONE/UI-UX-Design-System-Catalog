# Checkbox

**Kind:** specification · **Status:** proposed · **Primary layer:** components

## Purpose and fit

Toggle a single independent Boolean choice or select multiple items from a group. **Use** for agreement, optional settings and multi-select choices. **Avoid** for mutually exclusive choices (use radios) or for an action with an immediate side effect unless the consequences are explicit.

## Ownership and contract

The Checkbox owns check state, native keyboard activation, disabled/indeterminate presentation, accessible label and focus. The parent owns group semantics, validation, preference persistence and authorization. Illustrative API: `id`, `name`, `checked`, `onChange`, `disabled`, `required`, `indeterminate`, descriptive text. An indeterminate appearance reflects a mixed group state; it is not a third submitted Boolean value by default.

| State | Behavior | Verification |
| --- | --- | --- |
| Unchecked / checked | State visible and announced | Space toggles native checkbox |
| Focus-visible | Focus indicator distinguishable | Keyboard-only |
| Indeterminate | Mixed state accurately communicates parent selection | Screen-reader and state reset |
| Disabled | Choice is unavailable with context where needed | Touch/keyboard and visual |
| Invalid group | Linked error explains requirement | Group semantics and recovery |

**Invalid combinations:** A decorative check icon without an operable checkbox; label click targeting a different item; silently persisting changes when user expects an explicit Save.

## Tokens, responsiveness and localization

Use semantic border, action, text and focus roles. Maintain a sufficient target and spacing, including narrow/mobile layouts. Place labels beside the control using logical properties; allow long translations and do not mirror check state in RTL. The label and help text remain associated.

## Example and anti-example

**Illustrative:** Selecting "Receive updates" announces checked state, and the preference is saved using the product's documented save behavior. **Anti-example:** An unlabeled custom square looks checked but cannot be toggled by Space.

## Evidence, scope and adoption

| Check | Status | Notes |
| --- | --- | --- |
| Contract/design review | NOT VERIFIED | Owner unassigned |
| Keyboard/touch/assistive technology | NOT VERIFIED | Requires running UI |
| Indeterminate, validation and group behavior | NOT VERIFIED | Parent tests needed |
| RTL, labels, theme/reflow | NOT VERIFIED | Consumer tests needed |

**Canonical ID:** `component.checkbox` · **Owner:** unassigned · **Review date:** not reviewed · **Migration:** favor native semantics; do not replace checkbox groups with untested clickable tiles. Documentation-only.

Related: [Field](../field/spec.md), [component contracts](../../architecture/component-contracts.md), [accessibility](../../guidance/accessibility.md), [internationalization](../../guidance/internationalization.md). Reference: [WCAG 2.2 and WAI-ARIA APG](../../governance/references.md).

## Phase 5 executable reference (2026-11-08; verification scope)

An actual [Checkbox reference implementation](../../site/src/implementations/components/checkbox/Checkbox.js), its [synthetic scenario manifest](../../site/src/implementations/components/checkbox/scenarios.js), and token-aware [preview styles](../../site/src/implementations/components/checkbox/Checkbox.css) now exist in the embedded visual catalog. The catalog renders the checked-in reference source and exposes the same source for inspection. This **does not** promote the specification out of `proposed` or establish production adoption, WCAG conformance, real persistence or business validation. The earlier evidence table records the historical documentation-only state; keyboard/AT, real-browser behavior, long-content and visual performance still require observed review. See [Phase 5 gate](../../docs/visual-catalog-refactor/11-phase-5-core-controls.md).
