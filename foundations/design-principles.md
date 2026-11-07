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