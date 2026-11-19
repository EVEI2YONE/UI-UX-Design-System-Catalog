# Collaboration and sharing

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Help people grant, understand, change and revoke access to shared resources while accurately representing live collaboration and conflict states.

**Use when:** More than one participant needs access, visibility, comments or editing privileges for the same item.

**Avoid when:** Personal-only workflows where sharing controls would expose unnecessary access surfaces.

**Ownership:** The experience owns invitations, sharing comprehension and collaborator presence. The backend owns authorization, membership state, audit, concurrent mutation and revocation.

## Journey and state contract

| Stage | User-visible decisions and states | Recovery / evidence requirement |
| --- | --- | --- |
| Invite | Specify person, resource scope and exact access level | Review identity and prevent unintended disclosure |
| Pending | Differentiate invitation sent, accepted, expired and revoked | Do not imply access before acceptance |
| Work together | Show edit ownership, presence and meaningful change cues | No invented live presence or last-saved state |
| Conflict | Explain stale edits, merge options or preserved drafts | Explicit compare/retry for consequential changes |
| Remove access | Confirm effects and authoritative revocation outcome | Avoid residual access claims without verification |

## Design decisions

- Design readable role labels and effective permissions, not ambiguous icons or colors.
- Separate private/public links from named-member invitations and explain link lifespan and forwarding risks.
- Presence and typing indicators are hints, not permission proofs; do not expose personal data without justification.
- Coordinate with existing Offline Sync guidance for conflict/unknown outcomes instead of redefining synchronization mechanics.
- Provide a keyboard-accessible route to view sharing scope, accept/decline invitations and leave a resource.

## Inclusive operation, content, theming and locale

Keep each stage reachable by keyboard and screen reader with understandable headings, action labels, error associations and focus continuation. Make destructive or irreversible effects explicit; use semantic status tokens rather than color alone. Check content-driven reflow, long translation strings, RTL and locale-specific formats, high contrast, reduced motion, narrow devices and interrupted network states. Separate simulated UI from verified service behavior.

## Example and anti-example

**Illustrative example:** A document owner invites a reviewer with Comment permission, sees Pending, then confirms the accepted role before sharing sensitive content.

**Anti-example:** The interface shows a green Shared badge immediately after sending an invitation, obscuring whether the recipient actually gained access.

## Verification and research handoff

| Scenario | Expected evidence | Current status |
| --- | --- | --- |
| Invite/accept/revoke lifecycle with server-confirmed state | Record observed result, applicable cohort and environment | NOT VERIFIED |
| Role/scope changes, conflict recovery and access denied | Record observed result, applicable cohort and environment | NOT VERIFIED |
| Keyboard, locale-sensitive identities, live region noise and privacy | Record observed result, applicable cohort and environment | NOT VERIFIED |

Primary outcome: task success on the full journey, with errors, recovery and abandonment measured using explicit denominators. Research baselines and product usage are unknown; no human study, backend integration or accessibility compliance is claimed.

## Sources, related concepts and limitations

- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — contextual source, not evidence that this workflow has been tested.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual source, not evidence that this workflow has been tested.
- Related canonical guidance: [Task flows](task-flows-and-information-architecture.md), [Interaction recovery](interaction-states-and-recovery.md), [Accessibility](../../knowledge/guidance/accessibility.md), [UX measurement](../../knowledge/guidance/ux-measurement.md) and [Content design](../../knowledge/guidance/content-design-and-ux-writing.md).
- Follow product-specific legal, privacy, security and lifecycle constraints; this is a reusable reference pattern, not a production service.

## Applied decision and verification case

**Illustrative decision case (not observed):** Test revoke visibility and unauthorized re-entry after the change. Name the initiating task, what becomes unavailable or uncertain, how the user learns the truthful state and which continuation is safe. Distinguish user-visible feedback from server authority and explain when the simpler existing pattern should be reused.

**Acceptance boundary:** Specify an observable expected result for primary action, keyboard/focus recovery, relevant locale/RTL and small-screen conditions and a negative or failure state. Link the selected test to the concept's existing canonical owner instead of introducing an overlapping shared control. A [WCAG 2.2](https://www.w3.org/TR/WCAG22/) reference supports applicable web accessibility criteria but does not verify an implementation, independent review or actual task completion. Unexecuted checks remain **NOT VERIFIED**.

