# Information architecture validation

**Kind:** guideline · **Status:** proposed · **Primary layer:** intelligence · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundary

Test whether labels, categories, menu structures and content relationships let people find items and predict their locations. This is a method-specific complement to broader UX research and content architecture.

**Use when:** A proposed navigation or taxonomy needs evidence before costly implementation or migration.

**Avoid when:** Using one informal teammate test to assert all user groups can navigate a hierarchy.

**Accountability:** Researchers own methods and interpretation; content/IA owners own taxonomy decisions; product teams own regression checks.

## Decision rules and tradeoffs

- Define the real findability question and representative user cohorts before choosing a method.
- Use open card sorting to explore vocabulary and grouping hypotheses, closed sorting to evaluate existing categories, and tree testing to test findability without visual presentation.
- Write neutral tasks that do not contain the target navigation label; distinguish familiarity from legitimate wayfinding.
- Record first path, final destination, wrong turns, backtracking, time and confidence, keeping incomplete attempts visible.
- Triangulate quantitative routing results with participant explanations and tested interface behavior; do not confuse category agreement with validated information architecture.

## Decision matrix

| Context | Question | Decision support |
| --- | --- | --- |
| Open card sort | What groupings feel meaningful? | Candidate names and clusters, not final taxonomy |
| Closed sort | Which established categories are ambiguous? | Confusion pairs and missing buckets |
| Tree test | Can users find a specific destination? | Success, wrong paths and backtracking |
| Live navigation | Does UI presentation affect retrieval? | Keyboard and product-task observations |

## Example and anti-example

**Illustrative example:** Before renaming the component documentation sections, a team tests whether designers and engineers locate a Dialog focus spec under the proposed headings.

**Anti-example:** One team member finds a page quickly, so the entire navigation hierarchy is declared validated.

## Inclusive operation and verification

Check semantic headings, readable language, focus order, user control and error recovery. Consider long translation strings, RTL, zoom/reflow, reduced motion, multiple input methods, privacy and high contrast as applicable. No screenshot or documentation test substitutes for meaningful user-task evaluation.

| Check | Evidence needed | Status |
| --- | --- | --- |
| Task prompts do not reveal the target label | Recorded product or study evidence with explicit limitations | NOT VERIFIED |
| Sampling, failure paths and segments documented | Recorded product or study evidence with explicit limitations | NOT VERIFIED |
| Keyboard, screen-reader and translation considerations for live navigation | Recorded product or study evidence with explicit limitations | NOT VERIFIED |

The concept is a proposed, unreviewed reference; no production implementation, measured improvement or independent compliance is claimed. Record owner and review evidence before promotion.

## Sources and related concepts

- [GOV.UK patterns](https://design-system.service.gov.uk/patterns/) — contextual reference; check version and applicability.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual reference; check version and applicability.
- Related canonical sources: [Research methods](ux-research-methods.md), [Mental models](mental-models-and-journeys.md), [Task flows](../../specifications/patterns/task-flows-and-information-architecture.md).
