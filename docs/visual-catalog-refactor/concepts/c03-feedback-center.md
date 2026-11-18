# C-03 — Feedback Center

**Record type:** candidate concept brief — NOT a canonical catalog specification  
**Proposed identifier:** `composition.feedback-center` (reserved in this decision ledger only; not registered)  
**Disposition:** `deferred` — concept preserved, not approved for implementation or adoption  
**Source:** [Concepts and content expansion plan](../02-concepts-and-content-plan.md), Stage 2 row 3  
**Recorded:** 2026-11-08 · **Owner:** unassigned · **Reviewer approval:** not recorded

## User job and scope

Understand errors, confirmations, inline feedback and notices without losing important information.

**Potential reuse contexts / confidence:** Potential content moderation and settings interactions, not proven as a standalone feature.

**Illustrative states and interaction shape:** Inline field error, persistent banner, status confirmation, notification grouping and recovery from transient failure.

## Boundary between reusable reference and product

Applications own message truth, persistence, notification policy, channel permissions and durable recovery actions.

**Non-goals:** No disposable toast as the only critical error notice; no duplicate feedback pattern.

## Existing canonical knowledge and overlap decision

- `pattern.feedback` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `pattern.interaction-recovery` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `pattern.notifications-attention` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.
- `component.field` — look up this **existing** canonical registry ID and read its Markdown; the candidate must extend, not replace, that owner.

**Decision rationale:** These existing guidance entries already own individual status patterns; only a demonstrated cross-channel orchestration gap warrants a distinct entry.

## Evidence needed for promotion

Map existing feedback and notification owner contracts, quantify a reusable multi-step user need, and verify announcement timing/AT and no transient-only critical message.

Before any registry addition, confirm no equivalent ID/alias/task owner exists; document at least two independent credible applications or another approved strategic need, obtain a named owner and explicit human reviewer decision, author a complete feature/interaction specification and testable synthetic scenarios, and validate normative and preview boundaries. If evidence fails, keep this candidate deferred or merge it into the existing canonical guidance. Do not fabricate implementation paths, review dates or approval.

## Traceability and next action

- **Origin:** [Stage 2/3 concept plan](../02-concepts-and-content-plan.md)
- **Decision registry:** [durable concept inventory and decisions](../17-concept-inventory-and-decisions.md)
- **Canonical catalog:** `catalog/index.json` remains the only approved ID registry; this is a **noncanonical** record.
- **Next review action:** Catalog/design owner should review the overlap and evidence criteria above; no implementation or promotion is authorized by this document.
