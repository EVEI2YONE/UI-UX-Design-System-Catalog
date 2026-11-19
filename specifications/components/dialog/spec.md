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

**Illustrative:** An account-deletion feature composes Dialog with clear consequences, a cancel path and a feature-owned destructive handler. **Anti-example:** Shared Dialog invokes `deleteAccount` internally or leaves focus trapped after it closes.

## Evidence, scope and adoption

| Check | Status | Notes |
| --- | --- | --- |
| Design and focus contract review | NOT VERIFIED | Owner unassigned |
| Screen reader, keyboard, Escape and focus recovery | NOT VERIFIED | Real platform test needed |
| Modal background/inertness and scroll | NOT VERIFIED | Implementation test needed |
| Narrow/zoom/long text/RTL/themes | NOT VERIFIED | Implementation test needed |

**Canonical ID:** `component.dialog` · **Owner:** unassigned · **Review date:** not reviewed

Related: [component contracts](../../../knowledge/architecture/component-contracts.md), [interaction recovery](../../patterns/interaction-states-and-recovery.md), [accessibility](../../../knowledge/guidance/accessibility.md). Authoritative interaction guidance: [WAI-ARIA APG](../../../governance/references.md), with native semantic controls preferred where appropriate.

## Native dialog integration and task continuity

**Example context:** A native `<dialog>` may contain an unsaved form and be opened with `showModal()`, dismissed through a `cancel` event, or closed by a parent-controlled state change. These are distinct lifecycle paths that require defined draft-preservation and focus-return behavior; mounting a native dialog does not itself verify them.

**Decision contract:** for a stateful modal, specify an invocation focus target, initial focus strategy, `cancel`/Escape path, close-button path, backdrop behavior, save/discard/cancel policy, post-commit focus destination and fallback when the invoker disappears. Make the handling of the native `cancel` event explicit; if the app denies dismissal to protect unsaved work, use an accessible confirmation flow and state-based close policy, not a broken Escape key. Confirm that backdrop clicks cannot silently destroy a draft. Use the platform's dialog focus/inert behavior where supported; do not assume a custom mount/unmount wrapper implements every return-focus case.

**Implementation verification:** (1) open with keyboard and pointer, inspect actual initial focus; (2) Tab/Shift+Tab, Escape, Cancel and backdrop; (3) modify input, attempt dismissal, verify truthful loss warning and resumption; (4) complete async save with success/error, verify status plus focus after close; (5) remove initiating row on approval/filter and verify fallback focus; (6) repeat at narrow/zoomed view, with long translated content and screen reader. Record PASS/FAIL/NOT VERIFIED per scenario, browser and assistive technology.

**Good:** dialog closes after confirmed success and focus moves to the refreshed review list heading or next item if the original action disappeared. **Anti-example:** a modal unmounts on backdrop without checking edits, or assumes the browser will restore focus to a now-removed row.

## Decision scenario, evidence and acceptance

**Decision:** Dialog is a reusable modal shell; business confirmation, authorization and data mutations remain feature-owned.

**Illustrative scenario (not a completed study):** Open confirmation from a list row, press Escape, and restore focus to that row. If the triggering row was removed, focus the nearest surviving task context.

**Acceptance:** Verify initial focus, background inertness, Escape policy, exit focus, narrow-screen scroll and long translated content with actual keyboard/AT checks. Record the environment, owner, expected/actual results and evidence links; until executed, runtime outcomes remain **NOT VERIFIED**.

**Source scope:** [Applicable reference](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) informs the design decision. APG is a design reference; host runtime behavior is NOT VERIFIED. A reference is not proof of adoption, conformance or an independent review.

