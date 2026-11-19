# Design principles

**Kind:** guideline · **Status:** proposed · **Primary layer:** principles

## Purpose

Improve user task success, comprehension and trust through a coherent visual grammar. Design decisions should start with a user's goal, entry point, context, friction, desired next action and success criterion. Unknown user needs remain hypotheses until tested.

## Use and avoid

**Use** these rules when structuring a screen, composing a pattern, reviewing navigation, or critiquing a new component. **Avoid** applying uniformity mechanically when context genuinely requires a different affordance or when cosmetic consistency compromises accessibility or task completion.

## One-minute screen hierarchy contract

Before choosing a grid or colors, write the screen's **user, entry context, current task, required decision, authoritative state and safe next action**. Map those to:

1. **Location and scope:** where the person is, whose data/permissions are in force, and which filter or stage is selected.
2. **Required information:** facts, price/risk/privacy and prerequisites needed before acting.
3. **Task action:** the clear next step, with secondary/back/cancel alternatives. Several equally valid actions may be peers—never force a fake single CTA.
4. **Recovery and evidence:** what happens on validation error, unknown outcome or loss of permission; what would be observed to judge success.

**Decision test:** Ask a reviewer to identify the *task and next safe action* without prompts, then verify the same ordering survives keyboard navigation, text enlargement and translated/RTL content. A static wireframe verifies proposed grouping only, not focus or task completion. [NN/g's explanation of visual hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/) offers grouping/contrast principles; [WCAG 2.2](https://www.w3.org/TR/WCAG22/) defines applicable web accessibility criteria. Neither supplies evidence for this particular screen.

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

Inspect the primary action in each viewport, keyboard order, long translated labels, semantic headings, empty/error/loading variants and the user's ability to recover. Define a task-level success measure before claiming improvement. See [task flows](../../specifications/patterns/task-flows-and-information-architecture.md) and [UX measurement](../guidance/ux-measurement.md).

## Operational review rubric (illustrative, not user-tested)

Use this checklist after drafting a screen; compare alternatives with the **same task and content**, not different copy or features.

| Question | Acceptance evidence to collect | Flag |
| --- | --- | --- |
| Can users identify location and current scope? | Correct heading, route state, active filters and permission context | Missing or misleading scope |
| Is the task and safe next action discernible? | Predictable label, order and consequence before activation | Competing false-primary actions |
| Are essential details visible in time? | Status, fees, destructive impact, required fields and explanations | Important risk buried in progressive disclosure |
| Can a user recover or exit? | Error, retry safety, cancel/back and draft preservation | Dead-end or irreversible unconfirmed action |
| Does hierarchy survive inclusive contexts? | Narrow/wide, zoom, long/RTL labels, keyboard focus and contrast | Visually prioritized but operationally inaccessible |

**Worked example — appointment selection:** Show chosen service and date; present available slots; enable “Continue to review” only when a valid slot exists. Keep “Change service” and Back discoverable. If the selected slot expires, explain the conflict and preserve other input rather than claiming success. **Anti-example:** large promotions appear above availability, “Confirm” is active before selection, and a failed submission clears answers.

**Verification status:** the example is synthetic. A design review can check annotated structure and content; a rendered browser test can check reflow and focus; a task study can measure comprehension and completion. Report reviewer, revision, scenario, context and **PASS/FAIL/NOT VERIFIED** separately. [Task flows](../../specifications/patterns/task-flows-and-information-architecture.md) own journey sequence and alternatives; [wireframe methodology](../guidance/wireframe-methodology.md) owns fidelity and prototype escalation.

## Visual composition cross-reference — craftsmanship

This page owns **user-task and action priority**. For optical balance, composition, visual weight, focal-point treatment and practical contrast among visual regions, use [Visual design craftsmanship](visual-design-craftsmanship.md). Do not infer user success from visually attractive hierarchy; verify the actual journey separately.
