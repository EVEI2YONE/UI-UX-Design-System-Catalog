# B03 context gate — icon state transitions, focus continuity and sequential workflows

**Date:** 2026-11-07 · **Branch:** `knowledge/icon-interaction-system-b01-b06` · **Catalog main SHA:** `00df3f2055396e586fbb5ffa07e4a80dc8312e8e` · **Little Wins reference:** `main` SHA `5adf7fe16fa84426d32e3cb08b7c953cbc19fccb`. **PR:** deferred until B06.

## Repository context collected before drafting

- Checked `AGENTS.md`, `CONTRIBUTING.md`, `catalog/index.json` (53 entries on working branch vs 52 on main, with one B01 `foundation.icon-semantics` addition), `patterns/README.md`, `patterns/interaction-states-and-recovery.md`, `patterns/task-flows-and-information-architecture.md`, `foundations/iconography-and-semantics.md`, and `architecture/component-contracts.md`.
- Existing `pattern.interaction-recovery` already owns loading, errors, confirmation, cancellation, focus after dialogs, uncertain outcomes and backend-confirmed state. Its existing human review and value-changing transaction section must remain authoritative for review, points and ledger correctness.
- Existing `pattern.task-flows` owns entry → task → pending → outcome → recovery/exit, information architecture, authorized context and task continuity.
- B01 `foundation.icon-semantics` owns icon identity/host semantics; B02 `architecture.component-contracts` owns event source, controlled state, sibling projection and domain-outcome separation.
- Existing `pattern.advanced-interactions` covers bulk/reorder/undo; B04 will add action grouping and effort measurement. Do not move those concerns into B03.

## Source limitations and hypotheses

- Little Wins B06 documents the **source-observed** review queue's separate selection step, no evidenced automatic next selection, potential form-context remount, and uncertainty reconciliation. B07 proposes an acknowledged-and-reconciled sequential review flow; B08 proposes context retention, focus destination and eligibility checks. These are *design hypotheses*, not measured user friction, user testing or verified browser behavior.
- The catalog already describes focus and recovery *generally*. Missing **specific cross-component handoff rules** for icon status timing (CKG-09), focus when active item changes or disappears (CKG-10), spatial continuity/next-action positioning (CKG-11), and conditional next-item progression (CKG-12).
- Scope-safe choice: **extend existing canonical pages** (`pattern.interaction-recovery`, `pattern.task-flows`) and cross-link icon semantics, rather than create a new `SequentialTaskController` component or duplicate a state-management package. Names such as `nextEligibleItem` are conceptual, not product APIs.
- Risk boundary: authoritative mutation and permission checks remain backend-owned. UI must never advance or show verified success from optimistic icon swap, an unconfirmed request or an unexamined queue item. Distinguish *loaded subset exhausted* from *all eligible work complete*.
- References: [WCAG 2.2](https://www.w3.org/TR/WCAG22/) keyboard/focus/name-role-value, [WAI-ARIA APG Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) and [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/). Accessibility conformance requires application/browser testing.

## Gap disposition and planned ownership

| Gap | Classification | Canonical owner | Deliverable |
| --- | --- | --- | --- |
| CKG-09 icon-to-state synchronization | Incomplete | `pattern.interaction-recovery` + `foundation.icon-semantics` cross-link | Verified-result vs pending/unknown state matrix |
| CKG-10 focus and pointer continuity after mutation | Incomplete | `pattern.interaction-recovery` | Focus fallback decision and dynamic-list state |
| CKG-11 pointer travel and stable next-action placement | Incomplete | `pattern.task-flows` | Spatial continuity review without universal pixel thresholds |
| CKG-12 sequential task controller | Incomplete | `pattern.task-flows` / recovery state machine | Conditional next selection with safe stops/branches |

## B03 acceptance and evidence

- State diagram covers selected → pending → acknowledged → reconciled → announced → optional next item, and failed/conflicted/uncertain/cancel/empty-more alternatives.
- Icon, text, focus, action availability, selection and server state remain synchronized without conflating draft/pending/confirmed.
- Stable action region and context retention recommendations include keyboard/mobile/reflow caveats; no unsupported distance target is treated as mandatory.
- All examples label authoritativeness and async boundaries; no new general event bus or Little Wins API invented.
- Update registry aliases/relationships, pattern index, root/agent guidance, changelog, lookup tests and progress ledger. Run checks only when execution is available. If unavailable, record `NOT VERIFIED`.
- No PR before B06; do not merge or modify Little Wins target code.
