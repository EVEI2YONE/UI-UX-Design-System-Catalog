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

## Batch 1 extension — icon-only and icon-bearing action contract (proposed, 2026-11-07)

[Icon semantics](../../foundations/iconography-and-semantics.md) owns the cross-product icon intent/role policy. A Button owns **activation and host semantics**; its optional icon is decorative when the visible button text already names the action. An icon-only button is justified only when discoverability is reasonable in context and the host provides a localized contextual accessible name (e.g., `aria-label="More actions for quarterly report"`), visible focus and an operable target. Tooltip-only naming is insufficient. A bare SVG `onClick` is not a button and an icon must not become an independent interactive descendant of an interactive Button or Link.

**Icon-only state matrix:** `default` (name and meaningful icon); `hover` (optional pointer affordance); `focus-visible` (visible independent of hover); `pressed` (transient, not persistent toggle state); `loading` (stable layout, duplicate activation prevented, status text/announcement where needed); `disabled` (meaningful reason visible when relevant); `success/error` (owned by feature after authoritative response). Do not render an approved/saved icon merely because a click occurred. Do not rename a pending action to imply a confirmed success. If the host is a toggle/disclosure, expose the appropriate *host* state rather than relying on icon rotation.

**Geometry:** icon glyph dimension and clickable target are distinct. Verify the final hit target under WCAG 2.2 SC 2.5.8 Target Size (Minimum), including applicable exceptions; do not claim every small glyph is nonconforming. Larger practical touch targets may be appropriate. Test high contrast, zoom/reflow, long translated labels, logical leading/trailing icon slots and RTL-aware directional graphics. All checks remain `NOT VERIFIED` until run in an actual consumer.

## Phase 4 reference implementation (2026-11-08; executable, not certified)

The visual catalog now provides a **working reference example** in [Button.js](../../site/src/implementations/components/button/Button.js), with [deterministic synthetic scenarios](../../site/src/implementations/components/button/scenarios.js) and a [theme-aware stylesheet](../../site/src/implementations/components/button/Button.css). The code uses a native `button`, prevents activation while pending/disabled, and exposes a status message for pending state. The reference source is rendered inside an isolated preview frame and displayed verbatim by the source viewer. This **does not change** the canonical specification's `proposed` status or establish real-screen-reader or WCAG conformance. The feature owns whether an action is truly saved, authorized or retried; the preview intentionally performs no backend mutation.

**Verification distinction:** Node source-behavior tests and Python site/registry validation run in CI. Actual keyboard/focus, assistive technology, responsive rendering, visual hierarchy and performance on devices remain **NOT VERIFIED** pending Phase 8 inspection. The original evidence table above describes the pre-implementation snapshot and should not be read as a current absence of all source code.
