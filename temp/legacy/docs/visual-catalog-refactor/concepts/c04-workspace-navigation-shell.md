# C-04 — Workspace Navigation Shell

**Record type:** candidate concept brief — NOT a canonical catalog specification  
**Proposed identifier:** `composition.workspace-navigation-shell` (reserved in this decision ledger only; not registered)  
**Disposition:** `covered-existing` — concept preserved, not approved for implementation or adoption  
**Source:** [Concepts and content expansion plan](../02-concepts-and-content-plan.md), Stage 2 row 4  
**Recorded:** 2026-11-08 · **Owner:** unassigned · **Reviewer approval:** not recorded

## User job and scope

Move among workspace areas while retaining user context and understanding permissions.

**Potential reuse contexts / confidence:** Potential multi-area productivity tools; not measured as a standalone shared shell.

**Illustrative states and interaction shape:** Desktop/mobile navigation, current location, context switcher, long labels, role-aware visibility and focus restoration.

## Boundary between reusable reference and product

Applications own authorization, route guards, tenant identity and actual context-switch consequences.

**Non-goals:** No false assumption that hidden links enforce access; no premature full shell package.

## Existing canonical knowledge and overlap decision

- `pattern.navigation` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `pattern.role-aware-workspaces` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `pattern.task-flows` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `guidance.mobile-adaptive` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.

**Decision rationale:** Phase 6 demonstrates semantic navigation. Existing role-aware context guidance covers broader context. Full shell composition is still unverified, not a new canonical entry.

## Evidence needed for promotion

Demonstrate multi-context cross-product need, permission boundary and real routing/keyboard/mobile behavior before promotion.

Before any registry addition, confirm no equivalent ID/alias/task owner exists; document at least two independent credible applications or another approved strategic need, obtain a named owner and explicit human reviewer decision, author a complete feature/interaction specification and testable synthetic scenarios, and validate normative and preview boundaries. If evidence fails, keep this candidate deferred or merge it into the existing canonical guidance. Do not fabricate implementation paths, review dates or approval.

## Traceability and next action

- **Origin:** [Stage 2/3 concept plan](../02-concepts-and-content-plan.md)
- **Decision registry:** [durable concept inventory and decisions](../17-concept-inventory-and-decisions.md)
- **Canonical catalog:** `catalog/index.json` remains the only approved ID registry; this is a **noncanonical** record.
- **Next review action:** Catalog/design owner should review the overlap and evidence criteria above; no implementation or promotion is authorized by this document.
