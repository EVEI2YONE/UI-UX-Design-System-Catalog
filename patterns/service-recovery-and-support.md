# Service recovery and support handoff

**Kind:** guideline · **Status:** proposed · **Primary layer:** experiences

## Purpose and fit

Give people a credible path to continue their task when product-level recovery is exhausted or the service itself is unavailable. This pattern covers the boundary between **in-product error recovery**, **help and support**, and **cross-channel case resolution**. **Use** for repeated failures, support requests, unavailable services, account-access obstacles, and unresolved or ambiguous transaction outcomes. **Avoid** creating a support route for a trivial form typo or using “Contact support” as the sole response to a fixable product defect.

**Ownership boundary:** [Interaction states and recovery](interaction-states-and-recovery.md) owns generic UI error/retry semantics. This pattern owns channel selection, escalation, status continuity, safe information transfer, and the route back into the original user journey. Teams must not promise a support channel, response time or saved state the product cannot actually provide.

## Recovery decision tree

1. **Can the user correct the input?** Show a precise [form error](forms.md); retain valid values and navigate to the field.
2. **Is the service working but this request failed?** Explain status and a safe retry. A timeout after a consequential mutation may have an **unknown outcome**; check transaction state before repeating.
3. **Is the service temporarily unavailable?** Distinguish planned maintenance from unexpected failure. State known availability, what has or has not been saved, and alternative routes if real.
4. **Is the action blocked by permissions or eligibility?** Explain the difference without leaking private account or record details; provide an authorized request path or sign-in correction if supported.
5. **Does the issue require a person or another channel?** Provide an actual reachable support mechanism and what the user should expect, including hours/constraints where known.
6. **How does the user resume?** Provide a confirmed case/reference ID where available, status visibility, context restoration or alternate completion method; never fabricate the ticket or SLA.

## Service failure matrix

| Condition | Explain | Preserve / protect | Next step |
| --- | --- | --- | --- |
| Validation error | Which input to fix | Valid fields and context | Inline error plus summary where appropriate |
| Request timeout after submission | Outcome unconfirmed | User's work, transaction idempotency and privacy | Check status; retry only if safe |
| Planned closure | Service intentionally unavailable and known return time, if any | State of drafts accurately | Alternative service or support if available |
| Unexpected outage | Service currently unable to complete the task | Existing inputs if technically possible | Safe retry or reachable support; no fake ETA |
| Missing permission | Why this action is unavailable at an appropriate disclosure level | Other authorized data, do not reveal private details | Correct account or request access via approved channel |
| Escalated support case | What was submitted, next contact channel and privacy limits | Minimal needed context, user-controlled sensitive details | Track case or return to task when resolved |

## Support handoff contract

When a user needs assistance, specify: **task attempted; what failed and when; what is known about save/transaction status; permitted context to share; actual support channel; case/status tracking if available; expected next user action; route back to the task**. Do not prefill secrets, payment details, health information or credentials into email links or tickets. Support systems and privacy owners determine what is permissible.

Use clear, respectful labels such as “Get help with this request.” If the product supplies self-service status, make it available as an alternative to contacting support. Offer phone/email/chat only when that channel actually exists and is appropriate; do not display invented hours, responsiveness or human availability.

## Accessible and internationalized behavior

- Error and escalation instructions are perceivable in text with heading structure; essential support information cannot be toast-only or hover-only.
- Confirm where keyboard focus goes after an outage screen, support form submission, authentication return and interrupted task.
- Preserve routes and drafts when safe; provide understandable paths for assistive technology and constrained devices.
- Localize date/time/time-zone and response expectations, support hours, contact-format labels, and right-to-left presentation.
- Explain any reliance on external support channels and offer accessible alternatives where feasible.

## Example and anti-example

**Illustrative good:** After an application submit times out, the UI says submission status is unknown, shows a safe “Check application status” action, and offers a genuine help contact. It retains the draft if saved and confirms that fact only when verified.

**Anti-example:** A failed payment displays “Try again now” without verifying whether a charge was created, then links to a support page with no way back to the task.

## Verification

| Check | Status | Evidence needed |
| --- | --- | --- |
| Failure classification and retry safety | NOT VERIFIED | Integration failure simulations and state checks |
| Support availability, ownership and privacy | NOT VERIFIED | Verified channel, data protection review and support-team sign-off |
| Keyboard, screen reader, reflow and language | NOT VERIFIED | End-to-end supported-device and locale testing |
| Return/resumption and context preservation | NOT VERIFIED | Interrupted-flow and resolved-case scenarios |
| Outcome metrics | NOT VERIFIED | Self-service completion, escalation rate, repeat contacts and resolution data with clear denominators |

**Metric caution:** fewer support contacts could also mean support is harder to find. Pair contact volume with task completion, unresolved cases, qualitative evidence and access guardrails.

## Sources, applicability and related concepts

- [GOV.UK service-unavailable pages](https://design-system.service.gov.uk/patterns/service-unavailable-pages/) (accessed 2026-11-07): distinguish intentional closure and describe availability, saved answers and alternatives; adapt government-specific language and platform behavior.
- [GOV.UK service-problem pages](https://design-system.service.gov.uk/patterns/problem-with-the-service-pages/) (accessed 2026-11-07): unexpected failure guidance, not a universal uptime promise.
- [GOV.UK support operations guidance](https://www.gov.uk/service-manual/helping-people-to-use-your-service/set-up-and-manage-user-support) (published 2016; accessed 2026-11-07): channel coordination, follow-up and support telemetry; implementation-specific service considerations.

**Canonical ID:** `pattern.service-recovery` · **Owner:** unassigned · **Human review date:** null. Guidance proposed 2026-11-07; no support-system tests or participant outcomes.  
**Related:** [interaction recovery](interaction-states-and-recovery.md), [form composition](forms.md), [content design](../guidance/content-design-and-ux-writing.md), [feedback](feedback.md), [UX measurement](../guidance/ux-measurement.md).
