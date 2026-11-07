# Dialog

**Kind:** specification · **Status:** proposed · **Primary layer:** components

## Purpose and fit

Provide an intentionally bounded foreground interaction without losing context. **Use** for tasks requiring focused attention, a brief decision or confirmation. **Avoid** for sprawling multi-page flows, non-modal messages or routine status feedback that should remain inline.

## Ownership and contract

Dialog is the reusable **shell**: accessible name/description, modal semantics, initial/final focus strategy, background interaction control, Escape/close behavior, overflow and responsive presentation. Product features own account deletion, purchase, authorization, copy, data mutations and telemetry.

Illustrative API: `open`, `onRequestClose(reason)`, `title`/accessible label, `description`, `initialFocus`, content/body and action slots, `modal`. Do not expose an unconditional "disable Escape" switch without an explicitly reviewed exceptional workflow.

| State | Behavior | Verification |
| --- | --- | --- |
| Opening | Set appropriate initial focus without jumping unexpectedly | Keyboard and screen reader |
| Modal open | Background cannot receive interaction or focus | Tab/Shift+Tab, click/touch |
| Closing | Return focus to invoker or sensible fallback if removed | Escape, close control, completion |
| Loading / error | Preserve entered data and provide progress/recovery | Network error and retry |
| Narrow/zoom | Content/action areas remain reachable, with safe scrolling | Mobile and zoom/reflow |

**Focus and dismissal:** Determine the first meaningful target from task context; Escape should normally close the dialog, subject to a separately justified exception. Use native dialog support when it fits the platform. Restoring focus is contextual when the trigger is gone. A backdrop click must never cause unexpected loss of a destructive form's input.

## Tokens, responsiveness and localization

Use semantic overlay, surface, typography, border, elevation and focus roles, not random z-index values. Long content and translated labels must reflow; support logical direction, reduced motion and keyboard-visible focus across themes.

## Example and anti-example

**Illustrative:** An account-deletion feature composes Dialog with clear consequences, a cancel path and a feature-owned destructive handler. **Anti-example:** Shared Dialog invokes `deleteAccount()` internally or leaves focus trapped after it closes.

## Evidence, scope and adoption

| Check | Status | Notes |
| --- | --- | --- |
| Design and focus contract review | NOT VERIFIED | Owner unassigned |
| Screen reader, keyboard, Escape and focus recovery | NOT VERIFIED | Real platform test needed |
| Modal background/inertness and scroll | NOT VERIFIED | Implementation test needed |
| Narrow/zoom/long text/RTL/themes | NOT VERIFIED | Implementation test needed |

**Canonical ID:** `component.dialog` · **Owner:** unassigned · **Review date:** not reviewed · **Migration:** unify dialog shells only after focus, dismissal and consumer-impact checks; keep task flows app-local. Documentation-only.

Related: [component contracts](../../architecture/component-contracts.md), [interaction recovery](../../patterns/interaction-states-and-recovery.md), [accessibility](../../guidance/accessibility.md). Authoritative interaction guidance: [WAI-ARIA APG](../../governance/references.md), with native semantic controls preferred where appropriate.
