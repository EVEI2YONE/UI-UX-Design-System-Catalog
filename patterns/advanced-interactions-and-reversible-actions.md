# Advanced interactions and reversible actions

**Kind:** guideline · **Status:** proposed · **Primary layer:** patterns

## Purpose and use boundary

Define discoverable, accessible and reversible behavior for reorder, bulk actions, command palettes, shortcuts and undo/redo. **Use** when complex interaction provides meaningful value for frequent work. **Avoid** when native buttons, lists and [data tables](data-tables.md) already solve the task. Features own authorization, data mutation and persistence; this pattern owns interaction decisions, not a universal mega-component.

## Choose the simplest interaction

| Task | Prefer | Constraint |
| --- | --- | --- |
| Reorder a list | Move up/down, position chooser or accessible command; optional drag enhancement | A single-pointer, non-drag alternative and keyboard path as applicable |
| Act on many records | Explicit selected count, scope and named bulk command | Distinguish page selection from all matches |
| Repeat frequent commands | Discoverable shortcut help or command palette *in addition* to regular commands | Avoid OS/browser/AT shortcut conflicts |
| Make a reversible edit | Truthful undo scope and window, ideally with persistent state recovery | Never promise remote undo when impossible |
| Edit an interactive grid | Defined navigation, selection and edit model | Do not give ordinary table `role=grid` semantics without actual behavior |
| Commit consequential changes | Review summary and explicit confirmation | Recheck permissions and result status |

## State matrix and error paths

| State | Visible behavior | Recovery |
| --- | --- | --- |
| Idle | Available actions and how to select/reorder | Keyboard help or conventional controls |
| Item selection | Selected count, identity, and filter/page scope | Deselect one, clear selection |
| Pending command | Outcome still pending and focus preserved | Prevent duplicate conflicting mutations |
| Partial success | Identify succeeded and failed items | Retry eligible failures safely |
| Reordered draft | Explicit unsaved state | Revert or save if supported |
| Confirmed success | Report persisted outcome | True undo only if supported |
| Permission loss / conflict | Clearly describe unavailable action | Preserve safe context, do not leak restricted records |

## Interaction contracts

- **Drag and reorder:** reveal target position before execution and announce new order if useful. Implement a non-drag single-pointer alternative for web dragging under WCAG 2.2 SC 2.5.7, and separately meet keyboard operability. Merely adding keyboard drag does not satisfy the single-pointer requirement.
- **Bulk actions:** selection across pages and filters requires explicit scope and counts. Revalidate eligibility and authorization on the server. A partial mutation must report per-item result or a faithful summary; do not imply every item succeeded.
- **Shortcuts/command palette:** commands need discoverable conventional access, clear names, current context, focus/Escape behavior, empty/disabled states and conflict avoidance with text editing, browser and assistive tech. Provide reconfigurability where justified.
- **Undo/redo:** specify action granularity, side effects, duration and whether remote mutations can be compensated. An irreversible deletion or outbound notification cannot simply be “undone” by restoring a UI row.
- **Focus/status:** preserve focus on moved/updated context; do not steal focus merely to announce background changes. Keep recoverable status persistent for important outcomes.
- **Touch and responsive:** hover or small drag handles cannot be the only access route; support translated labels, RTL, narrow layout, reduced motion and color alternatives.

**Illustrative good:** An authorized administrator selects 12 records across two pages, confirms “Archive 12 records,” then receives “10 archived, 2 failed” with a safe retry path for the failures.

**Anti-example:** A drag-only reorder surface has no move controls; a “Delete selected” action silently targets hidden results after filters change, and an Undo toast promises reversal after the records are irreversibly removed.

## Verification and acceptance

| Check | Status | Evidence needed |
| --- | --- | --- |
| Explicit selection scope and bulk partial errors | NOT VERIFIED | Real feature integration and data tests |
| Single-pointer alternative, keyboard and AT | NOT VERIFIED | WCAG 2.2 dragging + keyboard manual checks |
| Shortcuts and command menu focus/semantics | NOT VERIFIED | OS/browser/AT input matrix |
| Undo claims and consequential operation status | NOT VERIFIED | Backend idempotency and compensating action tests |
| Zoom, locale/RTL, themes and reduced motion | NOT VERIFIED | Responsive and localization tests |

## Sources and limits

- [W3C WCAG 2.2 SC 2.5.7: Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html) (AA; consulted 2026-11-07): requires a non-drag single-pointer alternative unless an exception applies; keyboard accessibility is a separate requirement.
- [WAI-ARIA APG Grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/) (consulted 2026-11-07): grid keyboard behavior only when an actual interactive grid is needed.
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (consulted 2026-11-07): authorization at request/object level, not proof of usable UX.

**Canonical ID:** `pattern.advanced-interactions` · **Owner:** unassigned · **Reviewed:** null · **Drafted:** 2026-11-07.

Related: [data tables](data-tables.md), [role-aware workspaces](role-aware-workspaces-and-context-switching.md), [interaction recovery](interaction-states-and-recovery.md), [accessibility](../guidance/accessibility.md), [mobile UX](../guidance/mobile-and-adaptive-platform-ux.md).
