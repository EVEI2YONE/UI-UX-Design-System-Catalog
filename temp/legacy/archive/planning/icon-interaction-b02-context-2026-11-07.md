# B02 context gate — component anatomy, event ownership and coordination (2026-11-07)

**Working branch:** `knowledge/icon-interaction-system-b01-b06`. **Catalog main:** `00df3f2055396e586fbb5ffa07e4a80dc8312e8e`. **Current branch:** read by branch-qualified file SHA. **Target Little Wins:** `main` referenced as `5adf7fe16fa84426d32e3cb08b7c953cbc19fccb`; app-specific B03/B07 knowledge inspected for motivating examples. **No PR yet** per six-batch instruction.

## Catalog lookup and overlapping ownership

- `architecture.component-contracts` already specifies anatomy, state, pointer/keyboard/touch, focus, API constraints and feature-owned business effects. **Incomplete** on explicit event ownership categories, event payload/commit boundaries and cross-component communication contract.
- `component.button` owns activation/pending/disabled states, including B01 icon action guidance. **Do not** create a separate IconButton implementation or domain mutation API.
- `component.field` owns label/help/error association; Input, Select and Checkbox own native value and focus behavior while the feature owns validation and persistence.
- `component.dialog` owns focus/dismissal semantics while the feature owns consequential actions, unsaved input and mutation outcomes.
- `pattern.search-filter` already covers a search/filter/results composition and state preservation, and `pattern.data-tables` covers row context, selection and action accessibility. They can serve as examples without new canonical entries.
- `foundation.icon-semantics` (B01) owns icon meaning and decorative vs interactive roles; it is **not** an event framework.
- `pattern.interaction-recovery` owns asynchronous success/failure/reconciliation and focus recovery in detail; B03 will expand sequential continuation. B02 establishes handoff contracts only.

## CKG-to-owning-concept decisions

| Gap | Class | Decision | Owner |
| --- | --- | --- | --- |
| CKG-04 Icon-bearing composite anatomy | Incomplete | Extend `architecture.component-contracts` with host/slot ownership matrix; link existing icon semantics | Shared component contract |
| CKG-06 Local vs workflow vs domain event | Incomplete | Define event authority taxonomy and payload/outcome boundary | Shared component contract |
| CKG-07 Adjacent component reactions | Incomplete | Define parent-coordinator event graph with two worked examples | Shared component contract |
| CKG-08 Controlled state and nested triggers | Incomplete | Define single source of truth, compositional restrictions, impossible states and verification | Shared component contract |

**No new canonical ID proposed.** Add task-oriented aliases to the existing `architecture.component-contracts` registry entry and update its related references; preserve all existing IDs and file paths.

## Source provenance and applicability

- Existing catalog: `architecture/component-contracts.md`, six `components/*/spec.md` pages, `patterns/search-and-filter.md`, `patterns/data-tables.md`, `patterns/navigation.md`, `guidance/accessibility.md`, `catalog/index.json`, `AGENTS.md` and `CONTRIBUTING.md`.
- Motivating Little Wins: `docs/little-wins/ui-knowledge/batch-03-component-architecture.md` (slots/compound components and state ownership) and `batch-07-action-consolidation.md` (async actions, safe decisions and event orchestration). These are **proposed product knowledge**, not observed UX performance or universal architecture rules.
- Standards: [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) for specific composites, particularly [menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/) and [dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/); [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for keyboard, focus and name/role/value criteria. APG examples are not mandatory implementation libraries; prefer native semantics and existing tested accessible component primitives.
- **Known unknowns:** no target-side browser event traces, task measurements, AT test results or component package runtime verification. Specified examples are illustrative patterns requiring real implementation and tests.

## B02 acceptance and verification plan

1. Document single component event owner, workflow coordinator and server-authoritative outcome.
2. Show why nested interactive controls and duplicate propagation are invalid, and how separate actions can be composed.
3. Document controlled/uncontrolled state and event timing/invalid combinations; avoid a mandatory React-only API design.
4. Provide two platform-neutral examples with error/pending behavior, plus a manual and automated test matrix.
5. Reuse the canonical `architecture.component-contracts` entry and update registry aliases, section README, root/agent navigation and lookup tests. Record actual validator/test outcomes (or `NOT VERIFIED`).
6. Preserve the single-PR-after-B06 rule. No catalog PR or production component shall be claimed in this batch.
