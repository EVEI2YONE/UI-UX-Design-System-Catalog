# F-04 — Onboarding Workflow

**Record type:** candidate concept brief — NOT a canonical catalog specification  
**Proposed identifier:** `feature.onboarding-flow` (reserved in this decision ledger only; not registered)  
**Disposition:** `deferred` — concept preserved, not approved for implementation or adoption  
**Source:** [Concepts and content expansion plan](../02-concepts-and-content-plan.md), Stage 3 F-04  
**Recorded:** 2026-11-08 · **Owner:** unassigned · **Reviewer approval:** not recorded

## User job and scope

Complete a multi-stage introduction or setup task with clear progress, backtracking and recoverable incomplete input.

**Potential reuse contexts / confidence:** Potential workspace setup and general product introduction are hypotheses requiring independent validation.

**Illustrative states and interaction shape:** Stages, progress, required fields, back/cancel/restart, long text, step errors, optional simulated resume after interruption and unknown save outcome.

## Boundary between reusable reference and product

Applications own identity, consent, data retention, eligibility, persistent drafts, onboarding personalization and completion truth.

**Non-goals:** No credential creation, durable identity, saved draft or consent claim from a fixture.

## Existing canonical knowledge and overlap decision

- `pattern.task-flows` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `pattern.forms` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `pattern.interaction-recovery` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `guidance.accessibility` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `guidance.internationalization` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.

**Decision rationale:** Existing task-flow and form contracts already describe individual stages; a feature should exist only if reusable progress and recovery orchestration cannot be expressed by those patterns.

## Evidence needed for promotion

Comparative reuse study across two tasks, canonical flow/state spec, adapter with simulated resume only, verified keyboard focus and recoverability.

Before any registry addition, confirm no equivalent ID/alias/task owner exists; document at least two independent credible applications or another approved strategic need, obtain a named owner and explicit human reviewer decision, author a complete feature/interaction specification and testable synthetic scenarios, and validate normative and preview boundaries. If evidence fails, keep this candidate deferred or merge it into the existing canonical guidance. Do not fabricate implementation paths, review dates or approval.

## Traceability and next action

- **Origin:** [Stage 2/3 concept plan](../02-concepts-and-content-plan.md)
- **Decision registry:** [durable concept inventory and decisions](../17-concept-inventory-and-decisions.md)
- **Canonical catalog:** `catalog/index.json` remains the only approved ID registry; this is a **noncanonical** record.
- **Next review action:** Catalog/design owner should review the overlap and evidence criteria above; no implementation or promotion is authorized by this document.
