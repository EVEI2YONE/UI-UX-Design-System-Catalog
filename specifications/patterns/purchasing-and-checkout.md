# Purchasing and checkout journeys

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Support deliberate purchasing decisions from basket review through payment, confirmation and recovery without hidden fees or misleading transaction status.

**Use when:** A user commits money, selects a plan or completes a purchase with financial consequences.

**Avoid when:** Subscription settings only need plan-management guidance without an initial transaction journey.

**Ownership:** The pattern owns review of terms, inputs and trustworthy feedback. Server/payment services own price authority, payment capture, fraud and refund rules.

## Journey and state contract

| Stage | User-visible decisions and states | Recovery / evidence requirement |
| --- | --- | --- |
| Review items | Present quantities, total, taxes, delivery and recurring terms where relevant | Allow corrections before commitment |
| Collect details | Ask only needed shipping, contact and payment information | Accessible fields and validation preserve input |
| Confirm choice | Clearly show final amount, currency, merchant, renewal and consequences | Explicit intentional purchase command |
| Process payment | Mark pending and uncertain outcomes truthfully | Avoid blind re-submission after timeout |
| Receipt/recovery | Show authoritative order/payment result, receipt and support path | Safe retry, refund or dispute routes |

## Design decisions

- Do not hide mandatory fees, recurring charges, trial conversion or cancellation terms in secondary disclosure.
- Separate authorization, capture, pending and confirmed payment; a spinner completing does not prove payment succeeded.
- Provide full accessible input descriptions and error recovery without losing non-sensitive form data.
- Avoid duplicate financial charges: confirm outcome before retrying uncertain submission and use server-side idempotency.
- Show available payment methods and policies without inventing regulatory compliance or security certification.

## Inclusive operation, content, theming and locale

Provide keyboard and assistive-technology routes through each stage, visible headings and state feedback, and deliberate focus restoration after context changes. Support zoom/reflow, localized labels and units, RTL and high-contrast themes, touch alternatives and reduced motion. Use semantic tokens and make unavailable or irreversible outcomes understandable beyond color. Never treat a mock preview as proof of a real service outcome.

## Example and anti-example

**Illustrative example:** After reviewing an order and full total, a shopper submits once, sees Payment pending, then a server-confirmed receipt or a safe unresolved state.

**Anti-example:** On network timeout, the page invites repeated Pay clicks without checking whether the first payment completed.

## Verification and research handoff

| Scenario | Expected evidence | Current status |
| --- | --- | --- |
| Final totals/terms comprehension and confirmation | Record actual observed result, relevant cohort and environment | NOT VERIFIED |
| Payment timeout, duplicate retry, decline and partial fulfillment | Record actual observed result, relevant cohort and environment | NOT VERIFIED |
| Keyboard, autofill, text expansion, locale currency formatting and secure display | Record actual observed result, relevant cohort and environment | NOT VERIFIED |

Measure task completion, user error severity, abandonment and comprehension before asserting improvement. No baseline study, real back-end behavior or accessibility conformance is supplied by this concept.

## Sources, related concepts and limitations

- [GOV.UK check answers](https://design-system.service.gov.uk/patterns/check-answers/) — contextual reference, not a universal implementation prescription.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual reference, not a universal implementation prescription.
- Related canonical guidance: [Task flows](task-flows-and-information-architecture.md), [Forms](forms.md), [Interaction recovery](interaction-states-and-recovery.md), [Accessibility](../../knowledge/guidance/accessibility.md), and [UX measurement](../../knowledge/guidance/ux-measurement.md).
- Review domain, locale, security, legal and service constraints separately before adoption.

## Applied decision and verification case

**Illustrative decision case (not observed):** Validate duplicate prevention and unknown payment result recovery. Name the initiating task, what becomes unavailable or uncertain, how the user learns the truthful state and which continuation is safe. Distinguish user-visible feedback from server authority and explain when the simpler existing pattern should be reused.

**Acceptance boundary:** Specify an observable expected result for primary action, keyboard/focus recovery, relevant locale/RTL and small-screen conditions and a negative or failure state. Link the selected test to the concept's existing canonical owner instead of introducing an overlapping shared control. A [WCAG 2.2](https://www.w3.org/TR/WCAG22/) reference supports applicable web accessibility criteria but does not verify an implementation, independent review or actual task completion. Unexecuted checks remain **NOT VERIFIED**.

