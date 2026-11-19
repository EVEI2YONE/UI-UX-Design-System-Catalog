# Onboarding and first-use experiences

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Help a new or returning person reach meaningful first success with the least instruction needed, without making returning experts replay an introduction.

**Use when:** A task has prerequisites, unfamiliar vocabulary or setup steps that benefit from progressive orientation.

**Avoid when:** A clear first action and contextual help already let people succeed, or onboarding blocks access to an urgent task.

**Ownership:** The pattern owns entry-point orientation, progress/resume and learning decisions; application features own real account setup, eligibility, permissions and success signals.

## Journey and state contract

| Stage | User-visible decisions and states | Recovery / evidence requirement |
| --- | --- | --- |
| Before entry | Explain value, prerequisites and expected effort | Plain path to proceed or learn more |
| First action | Present one real task and relevant contextual hints | Skip/defer/restart controls where appropriate |
| Partial setup | Show what is complete and what remains | Safe save/resume and error recovery |
| First success | Confirm an actual task outcome, not just tour completion | Next useful action and optional learning |
| Returning session | Do not force repeat walkthrough | Remember or infer context only from authorized reliable state |

## Design decisions

- Prefer learning in context over an unskippable carousel of feature descriptions.
- Treat empty states as an invitation to perform a meaningful first action; do not manufacture placeholder data that looks real.
- If onboarding asks for sensitive permissions or personal data, explain purpose, alternatives and consequences at the point of request.
- Separate education-complete from task-complete; a tour click is not evidence of user competence.
- Test different prior knowledge, assistive technologies, translated copy and interrupted setup.

## Inclusive operation, content, theming and locale

Keep each stage reachable by keyboard and screen reader with understandable headings, action labels, error associations and focus continuation. Make destructive or irreversible effects explicit; use semantic status tokens rather than color alone. Check content-driven reflow, long translation strings, RTL and locale-specific formats, high contrast, reduced motion, narrow devices and interrupted network states. Separate simulated UI from verified service behavior.

## Example and anti-example

**Illustrative example:** A project workspace welcomes a new member with Create a project, Import existing work and Learn more; setup can be resumed after leaving.

**Anti-example:** A six-screen mandatory tour declares success when the user taps Finish but has never completed the underlying task.

## Verification and research handoff

| Scenario | Expected evidence | Current status |
| --- | --- | --- |
| First-time and returning cohorts complete real tasks without mandatory tours | Record observed result, applicable cohort and environment | NOT VERIFIED |
| Skip, interrupt, resume, no-permission and empty-state branches | Record observed result, applicable cohort and environment | NOT VERIFIED |
| Keyboard/reading order, zoom, translated expansion and task comprehension | Record observed result, applicable cohort and environment | NOT VERIFIED |

Primary outcome: task success on the full journey, with errors, recovery and abandonment measured using explicit denominators. Research baselines and product usage are unknown; no human study, backend integration or accessibility compliance is claimed.

## Sources, related concepts and limitations

- [GOV.UK start service pattern](https://design-system.service.gov.uk/patterns/start-using-a-service/) — contextual source, not evidence that this workflow has been tested.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual source, not evidence that this workflow has been tested.
- Related canonical guidance: [Task flows](task-flows-and-information-architecture.md), [Interaction recovery](interaction-states-and-recovery.md), [Accessibility](../../knowledge/guidance/accessibility.md), [UX measurement](../../knowledge/guidance/ux-measurement.md) and [Content design](../../knowledge/guidance/content-design-and-ux-writing.md).
- Follow product-specific legal, privacy, security and lifecycle constraints; this is a reusable reference pattern, not a production service.

## Applied decision and verification case

**Illustrative decision case (not observed):** Test first-success with a skip and resume path. Name the initiating task, what becomes unavailable or uncertain, how the user learns the truthful state and which continuation is safe. Distinguish user-visible feedback from server authority and explain when the simpler existing pattern should be reused.

**Acceptance boundary:** Specify an observable expected result for primary action, keyboard/focus recovery, relevant locale/RTL and small-screen conditions and a negative or failure state. Link the selected test to the concept's existing canonical owner instead of introducing an overlapping shared control. A [WCAG 2.2](https://www.w3.org/TR/WCAG22/) reference supports applicable web accessibility criteria but does not verify an implementation, independent review or actual task completion. Unexecuted checks remain **NOT VERIFIED**.

