# Interaction states and recovery

**Kind:** guideline · **Status:** proposed · **Primary layer:** behavior

## Purpose

Make system status and user control clear during input, asynchronous work, empty results and failure. States are part of the interaction contract, not optional polish.

## State model

| State | Guidance | Recovery / accessibility |
| --- | --- | --- |
| Default / focus / active | Controls visibly communicate availability and action | Keyboard and focus semantics |
| Disabled / readonly | Distinguish not-allowed from uneditable | Explain unavailable actions when needed |
| Loading / progress | Preserve context; prevent duplicate destructive actions | Appropriate status announcements; avoid excess noise |
| Empty | Explain why content is absent and how to begin | Actionable next step rather than blame |
| Validation error | Identify the field and how to correct it | Associate error with control; preserve input |
| Offline / timeout / partial error | State what succeeded and failed, retry safely | Idempotence and resumption as appropriate |
| Destructive confirmation | Explain permanence, consequences and alternatives | Deliberate confirmation and cancel path |
| Success | Confirm outcome and subsequent path | Announce important updates unobtrusively |

## Dialog/focus example

On opening a modal dialog, define an appropriate initial focus target; keep background interaction inaccessible when truly modal; provide an understandable close path. On close, restore focus to a sensible invoking element or next workflow target. Test special cases such as the invoker being removed. Consult [accessibility guidance](../guidance/accessibility.md).

**Avoid:** losing form data after a server error; spinners without status; a disabled button with no explanation; trapping focus after modal closure.

## Verification

Test real request failures, latency, translated errors, retry, touch and keyboard, screen reader notices, reduced motion and narrowed/reflowed containers. A documented state is not proof the app implements it.

## Recovery decision table

| Failure condition | Explain | Preserve | Safe next step |
| --- | --- | --- | --- |
| Client validation | Which input failed and how to fix it | Other entered values | Focus or link to invalid input |
| Network timeout | Outcome may be unknown | Current task and request context | Verify status before retrying non-idempotent operations |
| Permission denied | Action is unavailable in this context | Non-sensitive navigation state | Return or request authorized access |
| Partial success | Explicitly identify completed and pending items | Successful results | Retry only failed work when safe |
| Destructive action | Consequence and permanence | Relevant audit/confirmation context | Offer cancel; undo only when truly supported |

**State transitions:** specify idle → validating → pending → success/failure, cancellation, and retry. Avoid optimistic success messages for irreversible operations before confirmation. When a pending control is unavailable, do not remove the user's focus without a meaningful next destination. When an error replaces content, ensure the new message is discoverable to keyboard and screen-reader users.

**Test scenarios:** delayed response, double activation, lost connection after submission, server validation, expired permission, translated error, interrupted modal, and retry from the recovery state. Report actual run status; guidance is not proof of implementation.
