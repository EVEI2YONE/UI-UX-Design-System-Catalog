# B04 context gate — action consolidation and interaction-effort evidence

**Collected:** 2026-11-07, before B04 canonical edits. **Catalog main:** `00df3f2055396e586fbb5ffa07e4a80dc8312e8e`; **shared branch:** `knowledge/icon-interaction-system-b01-b06`. The working branch contains B01–B03 and retains one deferred PR after B06. No Little Wins code changes are authorized.

## Catalog sources inspected

- `AGENTS.md` and `CONTRIBUTING.md`: search canonical IDs first; extend before creating duplicate concepts; do not equate proposed guidance with implementation.
- `catalog/index.json`: `pattern.advanced-interactions` covers bulk actions, shortcuts, undo, drag and reversible operations. `guidance.ux-measurement` covers task completion, time on task, errors, abandonment, consent/privacy, eligible cohorts and instrumentation. Both are proposed and unreviewed.
- `pattern.task-flows`: B03 spatial continuity and safe next-item task state; **not** action-selection heuristics or a measurement specification.
- `architecture.component-contracts`: B02 UI event vs feature command vs authoritative domain outcome; **not** a reusable rule for choosing visible buttons versus overflow/split controls.
- `patterns/README.md`, `guidance/README.md`, and batch progress ledger: ownership and retrieval paths checked.
- Little Wins B06 (`batch-06-interaction-efficiency.md`) and B07 (`batch-07-action-consolidation.md`): source observations and candidate heuristics for review queues, action grouping, and pointer travel. They explicitly lack user-behavior baselines; no production UX outcomes inferred.

## Gap assessment and disposition

| Gap | Existing coverage | Reusable missing decision | Owner/action |
| --- | --- | --- | --- |
| CKG-13 — action consolidation | `pattern.advanced-interactions` already defines consequential operations, batch and keyboard access | Choice matrix for labeled primary/secondary, peer outcomes, contextual toolbar, overflow, split button, shortcuts and confirmation; misuse criteria | **Extend** `pattern.advanced-interactions`; no new ID |
| CKG-14 — interaction cost | `guidance.ux-measurement` defines TCR/time/error/privacy; B03 `pattern.task-flows` mentions spatial continuity | Task-defined pointer/scroll/selection/re-entry/time-to-next metrics, comparable input modality baselines, denominators and outcome guardrails | **Extend** `guidance.ux-measurement`; no new ID |

**Boundary:** Neither entry should specify product-specific permissions, prices, point awards or server mutation APIs. Minimized clicks are not an independent acceptance condition. Uncertain server outcomes and sequential progression remain under `pattern.interaction-recovery` and `pattern.task-flows`. UI controls do not authorize their own actions.

## Evidence and standards

Reference sources already linked from canonical pages: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/), [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). Review actual menu-button, toolbar and dialog implementations against the relevant APG pattern; native semantics preferred. Pointer travel and time-to-next-item are **proposed observational measures**, not established universal benchmarks.

**Not observed:** task attempts, click counts, pointer trajectories, keyboard paths, touch interaction, TCR/error/time baselines, user comprehension, accessibility conformance, real improvement from split buttons or action consolidation. No CI result is inferred from documentation.

## Batch acceptance

1. Explain when to use visible action groups, contextual menus, split buttons, toolbars, shortcuts and explicit confirmation; document misuse and risk boundaries.
2. Provide interaction effort worksheet with precise units/denominators and caution for missing/nonpointer data.
3. Include positive/negative examples, keyboard/touch/RTL/reflow/AT considerations and safety outcome guardrails.
4. Update existing canonical entries and registry aliases, README discoverability and regression tests; preserve original IDs.
5. Write actual verification disposition in shared ledger; no PR until B06.
