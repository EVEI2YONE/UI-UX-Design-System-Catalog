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