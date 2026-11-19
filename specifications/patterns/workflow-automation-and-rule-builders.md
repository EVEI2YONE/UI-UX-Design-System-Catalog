# Workflow automation and rule builders

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Help a person configure repeatable event-based or scheduled actions with understandable triggers, conditions, scope, simulation, activation and safe execution history.

**Use when:** Users define rules for automated actions across records, participants, systems or schedules.

**Avoid when:** A fixed built-in workflow, a simple notification preference or an AI agent approval flow can satisfy the task without user-authored rules.

**Ownership:** The pattern owns rule editing, validation, activation and observable outcomes. Services own trigger semantics, enforcement, concurrency, rate limits, retries, permissions, logging and emergency stop.

## Journey and state contract

| Stage | User-facing decision and state | Failure and recovery expectation |
| --- | --- | --- |
| Define intent | Describe the goal, eligible objects and target scope in natural task language. | Provide a safe default and an explanation of prerequisites. |
| Specify rule | Choose trigger, conditions and ordered actions; show missing/invalid references clearly. | Do not enable a rule with unresolved permissions or mutually incompatible conditions. |
| Test/preview | Show a dry run or sample evaluation with explicit limits and the inputs that would match. | Mark simulations as non-executing and avoid claiming they predict all future events. |
| Enable | Summarize effect, frequency, recipients, costs and risk; require approval where material. | Verify real authorization and distinguish enabling from having executed. |
| Monitor/manage | Show enabled, paused, blocked, failed, running and disabled states, with execution history and safe retry. | Allow users to pause future execution and understand whether already-running tasks continue. |

## Decision rules and tradeoffs

- Specify whether conditions are all/any, nested and ordered; never leave Boolean grouping implicit when it changes who or what is affected.
- Constrain repeated triggers, circular automations and duplicate side effects using server controls; UI must disclose plausible consequences.
- Offer visible validation, a clear rule summary and safe preview before activation, especially for bulk, financial or external actions.
- Distinguish one-time execution from recurring schedules and time-zone-aware triggers; show true frequency and external side effects.
- Keep execution history observable but restrict sensitive payloads and personal data by permission.
- Define which changes are reversible, what Pause actually interrupts, and how retry differs from re-running an already-successful action.

## Interaction, accessibility, layout and localization

- Rule-builder inputs need labeled operators, groups and error summaries; drag-and-drop grouping always has an equivalent keyboard path.
- The rule's human-readable summary must update consistently and be understandable to screen readers, not only expressed as connecting lines.
- Preserve draft editing state while testing; confirmation should include affected scope and consequences without manipulative urgency.
- Narrow screens can use sequential steps instead of a complex spatial canvas; localization of condition language and RTL must preserve logical precedence.

Use semantic tokens, clear text, explicit focus and status behavior instead of color-only or motion-only cues. Validate actual keyboard and screen-reader behavior, reduced motion, high contrast, text growth and RTL with representative users and integrations before claiming success.

## Example and anti-example

**Illustrative example:** An operations manager configures 'When ticket priority becomes Urgent AND team is Support, assign the escalation queue and notify its owner,' previews matches and enables after confirmation.

**Anti-example:** A visual rule builder silently interprets AND as OR and enables unbounded repeated notifications without a pause or execution history.

## Evidence and verification

| Scenario | Evidence required | Status |
| --- | --- | --- |
| Condition precedence, empty groups, inaccessible targets and unauthorized actions | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |
| Dry run versus real execution, duplicate triggers and safe pause behavior | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |
| Lost acknowledgement, partial external failure and reconciled execution history | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |
| Keyboard editing/reordering, semantic rule summaries, narrow layout and RTL | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |

This documentation does not verify real users, moderation outcomes, backend access control, transactional safety, accessibility conformance, or production reliability. Product-specific policies and consent requirements need separate review.

## Sources, applicability and related concepts

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — supporting context; verify applicability and current edition.
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — supporting context; verify applicability and current edition.
- Related canonical sources: [Agentic actions](agentic-actions-and-approvals.md), [Advanced interactions](advanced-interactions-and-reversible-actions.md), [Scheduling](scheduling-and-availability.md), [Interaction recovery](interaction-states-and-recovery.md).
- **Scope limit:** This is a proposed UX contract, not a complete backend or security design.
