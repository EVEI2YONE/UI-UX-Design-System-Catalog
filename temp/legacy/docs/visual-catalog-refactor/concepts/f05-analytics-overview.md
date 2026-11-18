# F-05 — Analytics Overview

**Record type:** candidate concept brief — NOT a canonical catalog specification  
**Proposed identifier:** `feature.analytics-overview` (reserved in this decision ledger only; not registered)  
**Disposition:** `deferred` — concept preserved, not approved for implementation or adoption  
**Source:** [Concepts and content expansion plan](../02-concepts-and-content-plan.md), Stage 3 F-05  
**Recorded:** 2026-11-08 · **Owner:** unassigned · **Reviewer approval:** not recorded

## User job and scope

Understand a small set of metrics and trends with an accessible numerical alternative and clear context.

**Potential reuse contexts / confidence:** Potential operations dashboard and product-usage overview are candidate contexts, not verified use.

**Illustrative states and interaction shape:** Metric cards, accessible chart/table pairs, time filter, empty/loading/partial/error data, uncertainty, comparison periods, long labels and small screens.

## Boundary between reusable reference and product

Applications own metric definitions, data provenance, sampling, permissions, calculations, freshness and decisions based on results.

**Non-goals:** No fabricated trustworthy analytics, metric calculations, population inference or production data integration.

## Existing canonical knowledge and overlap decision

- `guidance.data-visualization` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `pattern.data-tables` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `guidance.ux-measurement` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `guidance.accessibility` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `guidance.internationalization` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.

**Decision rationale:** Data visualization and measurement guidance is already canonical; a reference feature would only add a reusable filter/state/overview interaction and should not duplicate chart accuracy rules.

## Evidence needed for promotion

Two real task contexts, defined source/time-range semantics, text equivalents, ambiguity tests and visual/AT/RTL and data correctness checks.

Before any registry addition, confirm no equivalent ID/alias/task owner exists; document at least two independent credible applications or another approved strategic need, obtain a named owner and explicit human reviewer decision, author a complete feature/interaction specification and testable synthetic scenarios, and validate normative and preview boundaries. If evidence fails, keep this candidate deferred or merge it into the existing canonical guidance. Do not fabricate implementation paths, review dates or approval.

## Traceability and next action

- **Origin:** [Stage 2/3 concept plan](../02-concepts-and-content-plan.md)
- **Decision registry:** [durable concept inventory and decisions](../17-concept-inventory-and-decisions.md)
- **Canonical catalog:** `catalog/index.json` remains the only approved ID registry; this is a **noncanonical** record.
- **Next review action:** Catalog/design owner should review the overlap and evidence criteria above; no implementation or promotion is authorized by this document.
