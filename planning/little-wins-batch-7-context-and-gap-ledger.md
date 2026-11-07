# Batch 7 — Accessible record actions and modal continuity: context/gap ledger

**Date:** 2026-11-07 · **Branch:** `docs/little-wins-platform-collaboration-gaps` · **PR:** [#7](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/pull/7) · **Status:** proposed documentation only.

## Context gathered before authoring

**Product source:** user-provided `Little_Wins_Source.zip`; snapshot without a verified target GitHub SHA. `Little_Wins/app/page.tsx` defines `submissionRows`, `Dialog`, and `SubmissionForm`. `submissionRows` renders `<tr onClick ... tabIndex={0} onKeyDown={Enter}>`, while its last column contains a visual chevron. `Dialog` calls `showModal()`, handles backdrop clicks and `onCancel`, and delegates close to parent state; `SubmissionForm` contains locally controlled input and save/submit actions. The ZIP includes `components/ui/dialog.tsx`, other UI primitives and a large global stylesheet. No browser/AT execution was performed in this batch.

**Catalog context read before writing:** `catalog/index.json`, `CONTRIBUTING.md`, `patterns/data-tables.md`, `components/dialog/spec.md`, `guidance/accessibility.md`, `patterns/advanced-interactions-and-reversible-actions.md`, `governance/quality-gates.md`, and existing root/nested indexes. Existing canonical guidance already covers native semantics, tables versus grids, dialog focus and manual accessibility checks; no new catalog concept is justified.

## Gap classification and dispositions

| ID | Existing guidance | Finding | Action |
| --- | --- | --- | --- |
| KG-LW07-01 | `pattern.data-tables` table semantics / interactive grid distinction | **Incomplete** explicit decision rule for clickable `<tr>` vs named action-cell button/link and post-review focus | Extend canonical page |
| KG-LW07-02 | `component.dialog` initial/final focus, Escape, modal semantics | **Incomplete** integration scenario for stateful native dialog, backdrop/unsaved edits, row removal | Extend component spec |
| KG-LW07-03 | `guidance.accessibility` keyboard and modal checks | **Incomplete** cross-component journey acceptance and source-evidence vs verified failure boundary | Extend canonical guidance |
| KG-LW07-04 | `governance.quality` release gates | **Incomplete** record-to-modal integrated negative-path evidence matrix | Extend canonical gate |

**Do not misclassify:** the Little Wins code is a *target-specific implementation candidate for verification*, not proof that a catalog pattern was missing or that a WCAG violation was reproduced. No browser testing means all product outcomes remain NOT VERIFIED.

## References and applicability

- [WAI-ARIA Authoring Practices: Dialog (Modal)](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) — task and focus-model reference; implementation still requires testing.
- [WAI-ARIA APG Grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/) — only for genuinely interactive grid keyboard models, not ordinary data-table rows.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) — applicable normative criteria for web; target AA, no conformance assertion.
- [MDN HTMLDialogElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement) — browser API reference; actual platform-specific behavior must be confirmed.

These are published reference starting points; URLs/editions were not independently live-revalidated during this batch.

## Acceptance and open status

- **Connector-verified:** existing canonical source inspected before edits; changes restricted to current PR branch; reused component and pattern IDs.
- **Pending:** catalog CI `python3 scripts/validate_catalog.py`, unittest suite, internal links on final PR head.
- **NOT VERIFIED:** rendered Little Wins keyboard/screen-reader journey, native dialog focus and cancellation, loss of unsaved edits, responsive behavior and actual WCAG conformance.
- **Owners:** not assigned; require human accessibility/engineering review before making product release claims.

**Scope:** knowledge-base documentation and retrieval only; no application code, independent accessibility certification or PR merge.
