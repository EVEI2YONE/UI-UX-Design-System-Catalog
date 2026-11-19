# Scheduling and availability

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Help people choose, review and change appointments or time-bound resources while accurately handling availability, time zones, recurrence and service-confirmed booking.

**Use when:** A task involves reserving a constrained slot, coordinating participants or changing a time-bound commitment.

**Avoid when:** A simple date field has no availability or scheduling rules; reuse Date and Time Input alone.

**Ownership:** The pattern owns browse/compare/review/reschedule interaction, not reservation inventory, time-zone conversion policy, reminders or recurrence storage.

## Journey and state contract

| Stage | User-visible decisions and states | Recovery / evidence requirement |
| --- | --- | --- |
| Choose context | Identify resource, location, timezone and eligibility | No hidden location/zone assumptions |
| Browse | Display available dates and times with truthful freshness | Not offered if fully booked or unknown |
| Select | Explain duration, local date, participant and recurrence conditions | Warn on conflicts or ambiguity |
| Confirm | Validate server-side availability; show pending and confirmed distinctly | Do not promise reservation on optimistic click |
| Modify/cancel | Explain deadline, fee, reminders and authoritative outcome | Retain a clear recovery route |

## Design decisions

- Use the user's intended locale for display and explicit IANA zone/offset context for meaningful instants; daylight-saving gaps and duplicate local times require a deliberate policy.
- Present no availability as a recoverable state with next dates or alternate resources, not as an unlabelled disabled calendar.
- If slot availability becomes stale during review, present alternative and retain relevant selections.
- Differentiate one-time, recurring and timezone-changing arrangements; avoid pretending recurrence is simply duplicating an instant.
- Show cancellation effects and the communication status of changes without claiming calendar updates you cannot verify.

## Inclusive operation, content, theming and locale

Provide keyboard and assistive-technology routes through each stage, visible headings and state feedback, and deliberate focus restoration after context changes. Support zoom/reflow, localized labels and units, RTL and high-contrast themes, touch alternatives and reduced motion. Use semantic tokens and make unavailable or irreversible outcomes understandable beyond color. Never treat a mock preview as proof of a real service outcome.

## Example and anti-example

**Illustrative example:** A clinic appointment flow states '2:30 PM America/New_York', checks the slot at confirmation, and offers nearby alternatives when it expires.

**Anti-example:** Silently converting a recurring 9 AM meeting into fixed UTC time so the local time shifts after daylight-saving changes.

## Verification and research handoff

| Scenario | Expected evidence | Current status |
| --- | --- | --- |
| DST gap/repeat, travel time zones and recurrence | Record actual observed result, relevant cohort and environment | NOT VERIFIED |
| Concurrent booking conflict, full calendar and cancelled slot | Record actual observed result, relevant cohort and environment | NOT VERIFIED |
| Keyboard date entry, accessible scheduling alternatives, long translated month names | Record actual observed result, relevant cohort and environment | NOT VERIFIED |

Measure task completion, user error severity, abandonment and comprehension before asserting improvement. No baseline study, real back-end behavior or accessibility conformance is supplied by this concept.

## Sources, related concepts and limitations

- [W3C internationalization](https://www.w3.org/International/quicktips/) — contextual reference, not a universal implementation prescription.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual reference, not a universal implementation prescription.
- Related canonical guidance: [Task flows](task-flows-and-information-architecture.md), [Forms](forms.md), [Interaction recovery](interaction-states-and-recovery.md), [Accessibility](../../knowledge/guidance/accessibility.md), and [UX measurement](../../knowledge/guidance/ux-measurement.md).
- Review domain, locale, security, legal and service constraints separately before adoption.
