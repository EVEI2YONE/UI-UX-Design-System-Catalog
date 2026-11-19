# Activity timelines and history

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Help people understand what happened to a record or shared workspace, when, and by which actor, including corrections and gaps. A user-facing timeline is not automatically a legally sufficient or tamper-proof audit log.

**Use when:** People need a chronological account of edits, access changes, approvals, status changes or task history.

**Avoid when:** A simple 'last updated' field is sufficient, or the need is exclusively a security/forensic audit system with separate legal and technical guarantees.

**Ownership:** This pattern owns readable event lists, grouping, actor labels, filtering, event detail and contextual navigation. Services own event truth, correlation, authorization, redaction, ordering, immutability claims and retention.

## Journey and state contract

| Stage | User-facing decision and state | Failure and recovery expectation |
| --- | --- | --- |
| Open timeline | Name the subject, period and whether only visible events are shown. | An empty timeline must distinguish no activity, unavailable history and missing permission. |
| Scan events | Group by date/period, show event type, actor and target in task-oriented language. | Use unambiguous timestamps and time-zone policies; do not infer exact sequence from display times with equal precision. |
| Inspect details | Reveal what changed, prior/next value where authorized, reason and linked record/version. | Redact personal/sensitive values and clearly indicate partial history or unavailable original. |
| Filter and search | Filter by event types, actors, date range or request ID without losing relevant context. | Show which criteria are applied and when results are incomplete. |
| Correct/reconcile | Display corrections, rollbacks, system-generated events and pending reconciliation accurately. | A later correction should not silently erase the user-visible history where preservation is required. |

## Decision rules and tradeoffs

- Choose a primary ordering source (server sequence, authoritative timestamp or documented approximation) and account for delayed arrival.
- Distinguish actor, subject and system; an automated action must not look like it was done directly by a human.
- State whether an event is 'recorded', 'confirmed', 'pending' or 'unknown' and avoid promising exhaustive audit coverage.
- Collapse noisy repetitive events only if counts and details remain accessible when material to the user's task.
- Expose difference views cautiously: compare fields or versions with clear old/new labels and privacy-limited visibility.
- Respect access changes, archived entities and retention controls; cached timelines must not leak formerly authorized data.

## Interaction, accessibility, layout and localization

- A timeline should be readable as an ordered list with meaningful headings and dates; decorative connectors cannot carry required meaning.
- Event detail disclosure and links need real buttons/anchors, logical focus movement, and meaningful descriptions of the target.
- Support chronological navigation with keyboard and screen reader without focus traps; announcements should not read every new event automatically.
- Locale-format dates/time zones, mixed-direction names, long notes and narrow screens while preserving event order and actor context.

Use semantic tokens, clear text, explicit focus and status behavior instead of color-only or motion-only cues. Validate actual keyboard and screen-reader behavior, reduced motion, high contrast, text growth and RTL with representative users and integrations before claiming success.

## Example and anti-example

**Illustrative example:** A shared document's Activity tab shows creation, edits, approvals and a later correction, each with a localized time, authorized actor and optional change details.

**Anti-example:** A green audit badge claims a guaranteed tamper-proof record while the page displays only a best-effort cache of recent events.

## Evidence and verification

| Scenario | Evidence required | Status |
| --- | --- | --- |
| Out-of-order delivery, duplicate events, equal timestamps and pagination across time | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |
| Role-based redaction, revoked access, deleted actors and missing records | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |
| Change comparisons, correction trails and disclosed retention limits | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |
| Keyboard event navigation, screen-reader ordering and translated time formats | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |

This documentation does not verify real users, moderation outcomes, backend access control, transactional safety, accessibility conformance, or production reliability. Product-specific policies and consent requirements need separate review.

## Sources, applicability and related concepts

- [W3C Internationalization Quick Tips](https://www.w3.org/International/quicktips/) — supporting context; verify applicability and current edition.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — supporting context; verify applicability and current edition.
- Related canonical sources: [Role-aware workspaces](role-aware-workspaces-and-context-switching.md), [Collaboration and sharing](collaboration-and-sharing.md), [Review Workspace](../experiences/review-workspace/spec.md), [Interaction recovery](interaction-states-and-recovery.md).
- **Scope limit:** This is a proposed UX contract, not a complete backend or security design.

## Representative task verification case

**Scenario to specify (illustrative, not tested):** Test grouped events and a keyboard navigable change history. Define user intent, initial and resulting authoritative state, invalid/unknown outcomes and an explicit recovery path. Preserve permission boundaries, reversible actions and the meaning of existing canonical components.

**Evidence rule:** State the success/failure observation, keyboard focus return, error announcement, small screen, text expansion and locale/RTL requirements that are relevant to the task. Collect actual environment, reviewer, observable results and limitations before marking a real implementation check complete. See [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for applicable accessibility criteria; this source alone is not product or research evidence. No unexecuted check is PASS.

