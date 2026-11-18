# C-02 — Responsive Information Dashboard

**Record type:** candidate concept brief — NOT a canonical catalog specification  
**Proposed identifier:** `composition.responsive-dashboard` (reserved in this decision ledger only; not registered)  
**Disposition:** `deferred` — concept preserved, not approved for implementation or adoption  
**Source:** [Concepts and content expansion plan](../02-concepts-and-content-plan.md), Stage 2 row 2  
**Recorded:** 2026-11-08 · **Owner:** unassigned · **Reviewer approval:** not recorded

## User job and scope

Scan a read-only overview of relevant indicators with understandable numeric context.

**Potential reuse contexts / confidence:** A potential read-only analytics overview; not validated as a separate feature.

**Illustrative states and interaction shape:** Responsive cards, accessible chart/tabular presentation, loading and missing values, time filter and long descriptions.

## Boundary between reusable reference and product

Applications own metric semantics and trusted underlying data, privacy and authorization.

**Non-goals:** No duplicated F-05 feature, fake authoritative metrics or inaccessible chart-only outcomes.

## Existing canonical knowledge and overlap decision

- `guidance.data-visualization` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `guidance.accessibility` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `guidance.mobile-adaptive` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.

**Decision rationale:** Visualization and mobile guidance exists; overlaps F-05 analytics. Keep as composition experiment, do not create a competing concept.

## Evidence needed for promotion

Validate overlap with F-05, document independent task and distinct reusable interaction before any promotion.

Before any registry addition, confirm no equivalent ID/alias/task owner exists; document at least two independent credible applications or another approved strategic need, obtain a named owner and explicit human reviewer decision, author a complete feature/interaction specification and testable synthetic scenarios, and validate normative and preview boundaries. If evidence fails, keep this candidate deferred or merge it into the existing canonical guidance. Do not fabricate implementation paths, review dates or approval.

## Traceability and next action

- **Origin:** [Stage 2/3 concept plan](../02-concepts-and-content-plan.md)
- **Decision registry:** [durable concept inventory and decisions](../17-concept-inventory-and-decisions.md)
- **Canonical catalog:** `catalog/index.json` remains the only approved ID registry; this is a **noncanonical** record.
- **Next review action:** Catalog/design owner should review the overlap and evidence criteria above; no implementation or promotion is authorized by this document.
