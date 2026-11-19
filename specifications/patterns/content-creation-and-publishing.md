# Content creation and publishing

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Guide authors from draft to review, preview, publish, revise and unpublish with truthful persistence and clear consequences.

**Use when:** A user creates reusable content or a public-facing artifact with meaningful draft, approval or publication states.

**Avoid when:** A brief one-field form or ephemeral message does not need publishing machinery.

**Ownership:** The pattern governs task-visible editing and lifecycle transitions. The app controls content model, moderation, versioning, authorization, storage, public exposure and rollback.

## Journey and state contract

| Stage | User-visible decisions and states | Recovery / evidence requirement |
| --- | --- | --- |
| Create | Name draft, scope and initial requirements | Useful blank state and accessible editing controls |
| Edit | Show dirty, saving, saved, failed and conflict states | Never replace unsaved text silently |
| Preview | Separate draft preview from actual published representation | Communicate publication audience and limitations |
| Review/publish | Show permissions, approval status, consequences and timing | Server-confirmed publication only |
| Revise/unpublish | Explain version history, rollback and external effects | Explicit recovery and irreversible-state policy |

## Design decisions

- Separate draft content from published content in language and status. A preview URL is not proof of public availability.
- If autosave is offered, distinguish local buffering from durable remote persistence and offer recovery after failure.
- Provide understandable publishing controls, including scheduled release, visibility and review gates where relevant.
- Treat deletion or unpublishing as meaningful changes; warn when cached copies or external distribution cannot be undone.
- Use content design and form contracts for field labels, length limits, editorial tone, validation and errors.

## Inclusive operation, content, theming and locale

Keep each stage reachable by keyboard and screen reader with understandable headings, action labels, error associations and focus continuation. Make destructive or irreversible effects explicit; use semantic status tokens rather than color alone. Check content-driven reflow, long translation strings, RTL and locale-specific formats, high contrast, reduced motion, narrow devices and interrupted network states. Separate simulated UI from verified service behavior.

## Example and anti-example

**Illustrative example:** An article editor shows Unsaved changes, Saved draft, In review and Published with dates and truthful authorized transitions.

**Anti-example:** The Publish button closes the editor immediately and declares publication successful before the service responds.

## Verification and research handoff

| Scenario | Expected evidence | Current status |
| --- | --- | --- |
| Draft loss, autosave, concurrency, preview permissions | Record observed result, applicable cohort and environment | NOT VERIFIED |
| Approval, scheduled publish, failed mutation and rollback | Record observed result, applicable cohort and environment | NOT VERIFIED |
| Keyboard editing, translated validation copy and assistive state feedback | Record observed result, applicable cohort and environment | NOT VERIFIED |

Primary outcome: task success on the full journey, with errors, recovery and abandonment measured using explicit denominators. Research baselines and product usage are unknown; no human study, backend integration or accessibility compliance is claimed.

## Sources, related concepts and limitations

- [GOV.UK patterns](https://design-system.service.gov.uk/patterns/) — contextual source, not evidence that this workflow has been tested.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual source, not evidence that this workflow has been tested.
- Related canonical guidance: [Task flows](task-flows-and-information-architecture.md), [Interaction recovery](interaction-states-and-recovery.md), [Accessibility](../../knowledge/guidance/accessibility.md), [UX measurement](../../knowledge/guidance/ux-measurement.md) and [Content design](../../knowledge/guidance/content-design-and-ux-writing.md).
- Follow product-specific legal, privacy, security and lifecycle constraints; this is a reusable reference pattern, not a production service.
