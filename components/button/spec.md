# Button

**Kind:** specification · **Status:** proposed · **Primary layer:** components

## Purpose and fit

A Button initiates an immediate action in the current task. Consumers include forms, dialogs and toolbars. **Use** for submit, retry, save and explicit commands. **Avoid** using a button for navigation to another resource (prefer a link) or making a generic clickable container act like a button.

## Ownership and contract

The shared Button owns action semantics, presentation, focus, state affordances and activation. The feature owns business effects, permissions, confirmation and request outcomes. Illustrative platform-neutral API: `label` or accessible name, `onActivate`, semantic `variant` (`primary`, `secondary`, `danger`), `size`, `disabled`, `loading`, optional leading/trailing decoration. Keep variant sets deliberately small; no required icon.

| State | Behavior | Accessibility / verification |
| --- | --- | --- |
| Default, hover, pressed | Action appears operable, one clear primary emphasis per task context | Use native `button` where possible |
| Focus-visible | Strong visible focus distinct from hover | Keyboard Tab and Shift+Tab |
| Loading | Prevent duplicate activation while indicating in-progress action | Announce meaningful status; preserve task context |
| Disabled | Cannot activate; nearby explanation if reason matters | Do not rely on disabled button tooltip alone |
| Error or success | Parent flow presents result and recovery | Button does not own network retry policy |

**Invalid combinations:** A pending action must not activate twice. A danger variant must not obscure destructive consequences. A link-looking button must not silently change semantics.

## Tokens, responsiveness and localization

Consume semantic action/text/focus tokens from [tokens guidance](../../foundations/design-tokens-and-themes.md). Support light/dark/high-contrast mappings and reduced motion. Allow long translated labels to wrap; use logical padding and avoid fixed-width assumptions. RTL does not invert a label or a universally meaningful icon.

## Example and anti-example

**Illustrative:** A Save button enters a pending state, prevents duplicate submit, and leaves the form values intact if the parent flow returns an error. **Anti-example:** The button internally calls a hard-coded account API and displays "Saved" before server confirmation.

## Evidence, scope and adoption

| Check | Status | Notes |
| --- | --- | --- |
| Contract and documentation review | NOT VERIFIED | Awaiting owner and review |
| Keyboard/focus and assistive technology | NOT VERIFIED | No implementation provided |
| Reflow/translation/theme and contrast | NOT VERIFIED | Verify in each consuming app |
| Runtime error, pending and duplicate-submission tests | NOT VERIFIED | Test parent flow and component together |

**Canonical ID:** `component.button` · **Owner:** unassigned · **Review date:** not reviewed · **Migration:** reuse existing semantic buttons; audit duplicated CTA variants before adoption. This is a **documentation specification**, not shipping code.

Related: [component model](../../architecture/component-model.md), [component contracts](../../architecture/component-contracts.md), [interaction recovery](../../patterns/interaction-states-and-recovery.md), [accessibility](../../guidance/accessibility.md). Primary standards starting point: [WCAG 2.2 and WAI-ARIA APG](../../governance/references.md), applicability to be reviewed per platform.
