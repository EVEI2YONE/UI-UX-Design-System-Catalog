# Design-system adoption and change management

**Kind:** policy · **Status:** proposed · **Primary layer:** cross-cutting · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundary

Support teams as they discover, evaluate, migrate to and maintain reusable concepts, with accountable review, clear communication and reversible rollout.

**Use when:** A catalog introduces changed guidance, variants, deprecations or shared behaviors across independent teams.

**Avoid when:** Forcing a big-bang rewrite when incremental adoption preserves working critical journeys and reduces risk.

**Accountability:** Catalog maintainers own guidance and status; consuming application owners own migration; human reviewers approve normative promotion.

## Decision rules and tradeoffs

- Identify consumers, migration boundaries, dependency versions and one accountable owner before changing a shared contract.
- Publish the reason to adopt, when not to adopt, differences from prior patterns, source limitations and representative examples.
- Pilot high-value workflows, verifying user task success and accessibility before expanding; do not equate package imports with UX improvements.
- Keep aliases and redirects for deprecated guidance until consumers have safe migration, including compatibility or rollback decisions.
- Provide contribution, issue triage and reviewer paths so teams report real mismatches instead of inventing parallel conventions.

## Decision matrix

| Context | Question | Decision support |
| --- | --- | --- |
| Discover | Can teams find the concept? | Task aliases and clear nested indexes |
| Evaluate | Can teams judge fit and maturity? | Use/avoid, owner, status and evidence |
| Migrate | Can critical user journeys remain safe? | Versioned contract, pilot, compatibility tests |
| Sustain | Who responds to defects and drift? | Owner, review cadence and deprecation process |

## Example and anti-example

**Illustrative example:** A revised Form validation contract is piloted in one service, tested with keyboard and screen reader, then rolled out with migration notes.

**Anti-example:** A visual demo is called a stable library and every app is required to rewrite its forms immediately.

## Inclusive operation and verification

Check semantic headings, readable language, focus order, user control and error recovery. Consider long translation strings, RTL, zoom/reflow, reduced motion, multiple input methods, privacy and high contrast as applicable. No screenshot or documentation test substitutes for meaningful user-task evaluation.

| Check | Evidence needed | Status |
| --- | --- | --- |
| Human review, source and owner recorded before status promotion | Recorded product or study evidence with explicit limitations | NOT VERIFIED |
| Core-task regression, localization and rollback checked during migration | Recorded product or study evidence with explicit limitations | NOT VERIFIED |
| Catalog aliases, indexes and canonical links remain intact | Recorded product or study evidence with explicit limitations | NOT VERIFIED |

The concept is a proposed, unreviewed reference; no production implementation, measured improvement or independent compliance is claimed. Record owner and review evidence before promotion.

## Sources and related concepts

- [GOV.UK patterns](https://design-system.service.gov.uk/patterns/) — contextual reference; check version and applicability.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual reference; check version and applicability.
- Related canonical sources: [Lifecycle](lifecycle-and-decisions.md), [Quality gates](quality-gates.md), [Component model](../knowledge/architecture/component-model.md).

## Decision scenario, evidence and acceptance

**Decision:** The catalog owner owns reusable guidance; each consumer owns pilot scope, task outcomes, support and rollback.

**Illustrative scenario (not a completed study):** A team trials new Field errors in one consequential form. If error recovery or keyboard success regresses, restore the old view and keep valid entries.

**Acceptance:** Record accountable owner, eligible pilot cohort, task completion/error baseline, fallback and sunset decision; do not use import counts as UX impact. Record the environment, owner, expected/actual results and evidence links; until executed, runtime outcomes remain **NOT VERIFIED**.

**Source scope:** [Applicable reference](https://www.w3.org/WAI/test-evaluate/) informs the design decision. Accessibility checks are only one guardrail; adoption outcome needs product evidence. A reference is not proof of adoption, conformance or an independent review.

