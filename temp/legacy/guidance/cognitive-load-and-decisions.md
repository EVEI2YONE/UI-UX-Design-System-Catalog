# Cognitive load and decision design

**Kind:** guideline · **Status:** proposed · **Primary layer:** principles

## Purpose

Reduce unnecessary demands on attention, working memory, comprehension and decision-making **without** oversimplifying important user choices. This is practical inclusive design guidance, not an assertion that a specific UX “law” predicts a user's response.

## When to use / avoid

- **Use when:** multi-step experiences require remembering prior information, dense screens obscure the next action, repeated re-entry or confusing terminology causes errors, or people report losing context.
- **Avoid when:** reducing visible options would conceal safety, price, privacy, authorization or irreversible consequences; do not optimize for fewer clicks at the expense of informed decisions.

## Design decisions

| Risk | Preferred pattern | Failure / tradeoff |
| --- | --- | --- |
| Recall burden | Keep essential state, instructions, prior answers and selection visible or recoverable | Forcing users to memorize identifiers from another screen |
| Decision complexity | Group meaningful choices, provide descriptive labels, sensible reversible defaults and contextual help | Arbitrary option caps or artificial urgency |
| Information density | Establish purpose, stable hierarchy, scannable headings and clear control/content relationships | Low density can also hide comparison information and increase navigation |
| Multistep continuity | Show progress where meaningful, preserve data, offer review/edit and resume paths | More steps can sometimes increase confidence; don't minimize blindly |
| Interruptions | Preserve unsaved work, explain pending status, allow safe return to task | Modal or notification that destroys context |
| Novice vs expert needs | Provide accessible progressive disclosure and shortcuts with learnable alternatives | Hide a core action behind gesture-only interactions |
| Different cognitive access needs | Prefer familiar patterns, plain wording, error prevention and multiple ways to understand | Assuming one presentation works for everyone |

## Review questions

1. Can a person identify where they are, what changed and what action is possible **without remembering a prior screen**?
2. Are labels grounded in user language rather than internal jargon, and are data entry demands justified?
3. Can a person tell which choice is reversible, costly, destructive or private before committing?
4. Does visual grouping clarify which controls affect which content?
5. Can people recover from interruptions, errors and timeouts without repeating unnecessary work?
6. Has the team validated the design with relevant cognitive and access needs rather than inferring success from heuristic agreement?

## Example and anti-example

**Illustrative scenario:** A multi-step application requires an account number from page 1 on page 4. Display the validated value or an accessible “Review details” path; preserve it on errors; make the editable state and save outcome clear.

**Anti-example:** Replace a comparison table with a single “Recommended” option to reduce choice complexity, concealing material costs and removing an informed comparison.

## Inclusive validation

Test at appropriate widths and zoom levels, with keyboard and assistive tech, language expansion, changed orientation and interrupted flows. Include participants with relevant attention, memory and comprehension needs when possible. Observe errors, task completion, aid use and ability to predict consequences. Do not equate the absence of an axe violation with cognitive usability or WCAG compliance.

**Status:** Design rubric only; participant research and product testing **NOT VERIFIED**.

## Standards and research context

- [W3C, Making Content Usable for People with Cognitive and Learning Disabilities](https://www.w3.org/TR/coga-usable/) (Working Group Note, 2021): supplemental non-normative patterns for comprehension, familiarity, orientation, focus and mistake prevention; **not** an additional WCAG conformance requirement.
- [W3C WAI, Cognitive Accessibility](https://www.w3.org/WAI/cognitive/) (consulted 2026-11-07): overview of cognitive disability considerations.
- [Nielsen Norman Group, Mental Models](https://www.nngroup.com/articles/mental-models/) (2024; reviewed September 2026): user expectations and mismatches.

**Canonical ID:** `guidance.cognitive-load` · **Owner:** unassigned · **Last human review:** none; proposed on 2026-11-07.  
**Related:** [design principles](../foundations/design-principles.md), [research methods](ux-research-methods.md), [journey mapping](mental-models-and-journeys.md), [accessibility](accessibility.md).
