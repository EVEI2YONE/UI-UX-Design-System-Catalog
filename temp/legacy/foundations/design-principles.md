# Design principles

**Kind:** guideline · **Status:** proposed · **Primary layer:** principles

## Purpose

Improve user task success, comprehension and trust through a coherent visual grammar. Design decisions should start with a user's goal, entry point, context, friction, desired next action and success criterion. Unknown user needs remain hypotheses until tested.

## Use and avoid

**Use** these rules when structuring a screen, composing a pattern, reviewing navigation, or critiquing a new component. **Avoid** applying uniformity mechanically when context genuinely requires a different affordance or when cosmetic consistency compromises accessibility or task completion.

## Core principles

| Principle | Decision rule | Failure to avoid |
| --- | --- | --- |
| Visual hierarchy | Make the current primary task and next action distinguishable | Competing primary CTAs |
| Consistency | Keep navigation, labels, interaction semantics and feedback predictable | Same-looking controls with different behavior |
| Whitespace and proximity | Group related items, separate unrelated tasks, preserve scanning | Overdense forms or excessive empty scroll |
| Affordances and signifiers | Make action targets and states recognizable | A decorative surface that looks clickable |
| Progressive disclosure | Reveal advanced detail when useful without hiding critical risk | Concealing destructive consequences |
| Feedback and recovery | Explain pending work, errors and next steps; retain user input | Generic errors that discard entered data |
| User-centered priority | Improve high-value journeys before cosmetic polish | Styling a secondary screen while core tasks fail |

## Example / anti-example

**Good:** one clear form submit action, context-specific help, and an error message beside the invalid field describing how to recover. **Poor:** three equally emphasized actions, validation appearing only after loss of input, and a visually prominent link with no destination.

## Verification

Inspect the primary action in each viewport, keyboard order, long translated labels, semantic headings, empty/error/loading variants and the user's ability to recover. Define a task-level success measure before claiming improvement. See [task flows](../patterns/task-flows-and-information-architecture.md) and [UX measurement](../guidance/ux-measurement.md).

## Operational review rubric (illustrative, not user-tested)

For each screen, annotate: **user and task**, entry point, expected next step, competing actions, content groupings, state feedback, and a recoverable exit. Review in this order: (1) can users recognize where they are, (2) can they identify the primary action, (3) can they predict consequences, (4) can they recover from failure? Capture the observable evidence for each judgment rather than assigning an aesthetic score.

| Decision | Prefer | Reconsider when |
| --- | --- | --- |
| Primary action | One dominant action within the current task context | Multiple equally frequent next steps genuinely exist |
| Grouping | Labels near fields, related items in one visual group | Grouping hides necessary comparisons |
| Disclosure | Advanced options remain discoverable | Safety, price, privacy or destructive consequences would be hidden |
| Feedback | Persistent result or inline validation when users must act | A transient toast is the only explanation of failure |

**Review example:** In a multi-step settings form, keep Save identifiable, show unsaved edits, preserve input on validation failure and expose a Cancel path. Do not replace evidence from task tests with internal design preference. Compare representative first-time and returning users; record unexpected behavior as a hypothesis for research.

**Acceptance evidence:** annotated states at narrow and wide widths; keyboard order; long-label and translated content; task success definition and baseline availability; design reviewer and review date. A prose review is not a production accessibility test.


## Wireframe screen hierarchy and action priority (proposed Batch 2, 2026-11-07)

**Use when** converting a task into a screen or comparing two proposed compositions. **Avoid** starting from a fashionable component layout, treating a large visual element as proof of priority, or imposing one primary CTA when the task genuinely has several equivalent safe choices. This extends `principle.visual-hierarchy`; [task flows](../patterns/task-flows-and-information-architecture.md) own sequence and alternatives, while [wireframe methodology](../guidance/wireframe-methodology.md) owns fidelity and prototype escalation.

For each proposed screen, write a compact **hierarchy contract**: (1) context and location; (2) user goal and the decision required *now*; (3) prerequisite information and risk/price/privacy disclosures; (4) one prominent primary next action where appropriate; (5) secondary/back/cancel/support affordances; (6) resulting state and next screen. Rank content by its role in safe task completion, not visual novelty. Include visible scope and status when data is filtered or permissions matter. Copy and grouping should allow users to predict action consequences. A static drawing only illustrates that order; real affordance and focus behavior still require implementation tests.

**Good synthetic example:** an appointment-selection screen leads with service and date context, then available slots, then “Continue to review”; change service and back remain discoverable. **Anti-example:** promotional cards dominate, “Confirm” appears before a time is chosen, and no exit or recovery route is visible. A visually balanced screen may still be task-incomplete.

**Verification expectation:** review annotation against the user's task brief; compare context-to-action scan order, action label/outcome consistency, safe exit, meaningful grouping and omission of known critical information. Check narrow/reflow and translated labels on rendered implementations when available, recording unexecuted checks as **NOT VERIFIED**. Distinct composition variants must retain the same user/task context for a fair comparison. See [Task-to-screen composition](../patterns/task-flows-and-information-architecture.md).

## Visual composition cross-reference — craftsmanship Batch 1 (proposed)

This page owns **user-task and action priority**. For optical balance, composition, visual weight, focal-point treatment and practical contrast among visual regions, use [Visual design craftsmanship](visual-design-craftsmanship.md) (KG-01). Do not infer user success from visually attractive hierarchy; verify the actual journey separately.
