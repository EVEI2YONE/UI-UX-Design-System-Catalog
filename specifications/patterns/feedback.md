# Feedback and status messaging

**Kind:** specification · **Status:** proposed · **Primary layer:** patterns

## Purpose and use boundary

Compose inline messages, status regions, banners and optional transient notifications that help users understand outcomes and recover. **Use** to signal pending work, success, warnings, partial failure and validation results. **Avoid** making a short-lived toast the only record of a consequential error or hiding required actions behind transient UI.

## Composition and ownership

The pattern decides **where and how** to communicate a product outcome; it may use a reusable alert/status control when available. [Field](../components/field/spec.md) owns field-level message association, [Dialog](../components/dialog/spec.md) owns modal shell behavior. A feature owns status meaning, message content, retry/undo behavior and event outcomes. Do not make global notifications mutate domain state.

| Condition | Recommended communication | User recovery |
| --- | --- | --- |
| Local validation | Persistent inline message by the affected control | Actionable correction; input retained |
| Global service interruption | Prominent persistent banner or page-level state | Explanation, retry/status path |
| Background success | Concise non-blocking status where appropriate | Clear result; optional undo only when supported |
| Partial success | Explicit completed versus failed items | Retry failed portion when safe |
| Destructive outcome | Persistent confirmation and next step | Never promise reversible action unless true |
| Long-running work | Progress or understandable pending status | Cancellation/continuation where supported |

Avoid duplicate competing announcements. Use status/live-region semantics judiciously, differentiating urgent from nonurgent messages and avoiding a flood of speech. When content is removed or focus target disappears, define a sensible focus destination. A toast must not require a fast response to prevent data loss.

## Inclusive and localized behavior

Use text, icon and structure rather than color alone; test contrast, zoom/reflow, focus order, pause/dismiss where applicable, reduced motion and long translated text. Use localized tense, number/date formatting and logical positioning for RTL. Avoid announcements that repeat entire pages.

## Examples and verification

**Illustrative good:** An async save shows pending status, then persistent corrective guidance on failure without clearing the form. **Anti-example:** A toast disappears after a few seconds, leaving no information about why an irreversible action failed.

| Check | Status | Evidence needed |
| --- | --- | --- |
| Message semantics and priority | NOT VERIFIED | User-task review |
| Screen reader/live region and keyboard | NOT VERIFIED | Implementation tests |
| Timeout/partial/error/undo paths | NOT VERIFIED | Feature behavior |
| Locale, RTL, themes, reduced motion | NOT VERIFIED | Supported platform matrix |

**Canonical ID:** `pattern.feedback` · **Owner:** unassigned · **Review date:** not reviewed · **Migration:** unify messaging semantics while preserving critical persistent feedback. This is proposed guidance, not a shipped toast implementation.

Related: [interaction recovery](interaction-states-and-recovery.md), [form composition](forms.md), [accessibility](../guidance/accessibility.md), [UX measurement](../guidance/ux-measurement.md). Standards: [WCAG 2.2 and WAI-ARIA APG](../governance/references.md).

## Batch 9 boundary — notification delivery vs in-task feedback

Keep this canonical pattern focused on **presenting** inline errors, banners, statuses and transient in-app messages. For event *selection*, urgency, timing, cross-device delivery, user-controlled push/email preferences and permission prompts, use [notifications and attention management](notifications-and-attention.md). Do not imply a successful push delivery is evidence of task completion. A security event may require a persistent record as well as a policy-approved notification; do not expose sensitive data through a lock-screen preview.
