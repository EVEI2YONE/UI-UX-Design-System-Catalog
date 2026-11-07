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
