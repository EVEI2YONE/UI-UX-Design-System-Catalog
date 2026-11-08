# C-05 — Onboarding Composition

**Record type:** candidate concept brief — NOT a canonical catalog specification  
**Proposed identifier:** `composition.onboarding-steps` (reserved in this decision ledger only; not registered)  
**Disposition:** `deferred` — concept preserved, not approved for implementation or adoption  
**Source:** [Concepts and content expansion plan](../02-concepts-and-content-plan.md), Stage 2 row 5  
**Recorded:** 2026-11-08 · **Owner:** unassigned · **Reviewer approval:** not recorded

## User job and scope

Complete stepwise forms with an understandable state of progress and safe interruption.

**Potential reuse contexts / confidence:** Candidate supporting composition for F-04, not independently verified.

**Illustrative states and interaction shape:** Back/next, cancellation, per-step validation, error summary, simulated save-and-resume, unknown save state.

## Boundary between reusable reference and product

Application owns draft persistence, identity, durable resume tokens and consent/eligibility rules.

**Non-goals:** No claim of real saved draft or duplicated onboarding feature.

## Existing canonical knowledge and overlap decision

- `pattern.task-flows` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `pattern.forms` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `pattern.interaction-recovery` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.

**Decision rationale:** Overlaps proposed F-04 and existing form/task-flow patterns; keep as supporting composition, not a rival feature concept.

## Evidence needed for promotion

First resolve F-04 ownership and demonstrate independent reuse before promoting a separate composition.

Before any registry addition, confirm no equivalent ID/alias/task owner exists; document at least two independent credible applications or another approved strategic need, obtain a named owner and explicit human reviewer decision, author a complete feature/interaction specification and testable synthetic scenarios, and validate normative and preview boundaries. If evidence fails, keep this candidate deferred or merge it into the existing canonical guidance. Do not fabricate implementation paths, review dates or approval.

## Traceability and next action

- **Origin:** [Stage 2/3 concept plan](../02-concepts-and-content-plan.md)
- **Decision registry:** [durable concept inventory and decisions](../17-concept-inventory-and-decisions.md)
- **Canonical catalog:** `catalog/index.json` remains the only approved ID registry; this is a **noncanonical** record.
- **Next review action:** Catalog/design owner should review the overlap and evidence criteria above; no implementation or promotion is authorized by this document.
