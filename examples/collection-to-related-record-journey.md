# Collection to related-record management: composed reference journey

**Type:** illustrative, reusable journey; **status:** proposed; **runtime / user testing:** **NOT VERIFIED**. This example demonstrates how to combine existing canonical concepts without creating a new component, route requirement or `feature.*` ID. Product terminology and all data are synthetic.

## Purpose, object model and starting context

A coordinator viewing a filtered collection needs to inspect a record, create or edit a related item, optionally classify it with reusable labels, inspect history, archive/trash/restore when permitted, and return to their original place. Success means **confirmed** persistence or a truthful unresolved state, with draft, filter and focus continuity. Avoid this structure for a one-step command that does not require details or relationships.

Conceptual relationships: `Workspace -> Collection -> Record -> Related item`; `Label definition` is scoped by workspace and can be referenced by many related items, while a `Membership` associates a particular related item with a stable label ID. Authorization, domain invariants, retention and persisted state remain feature/service responsibilities, not component props.

## Screen anatomy and key decisions

| Surface | Purpose and content | Preferred action and owner |
| --- | --- | --- |
| Collection | Search/filter, scope breadcrumb, card/list of records, selected context | Title link opens detail; [Collection views](../specifications/patterns/collection-and-feed-views.md) owns card anatomy |
| Record detail | Record identity, status, meaningful summary, bounded related preview, contextual actions | [Master-detail](../specifications/patterns/master-detail-exploration.md) owns return/focus semantics |
| Related-item editor | Explicit Add/Edit, owned draft, label selection, validation and Save/Cancel | [Forms](../specifications/patterns/forms.md) and [taxonomy](../knowledge/guidance/content-architecture-and-taxonomy.md) own interaction choices |
| History/lifecycle | Readable event attribution, Archive/Trash/Restore choices when authorized | [Advanced interactions](../specifications/patterns/advanced-interactions-and-reversible-actions.md) and [activity history](../specifications/patterns/activity-timelines-and-history.md) own decision guidance |
| Recovery | Pending/partial/unknown explanation, status lookup, safe retry and return | [Recovery](../specifications/patterns/interaction-states-and-recovery.md) and [component contracts](../knowledge/architecture/component-contracts.md) own state/coordination |

**Decision before rendering:** The user must distinguish **navigation** (title link), **selection** (select control), **expansion** (preview button) and **commands** (Add, Edit, more menu). A card-wide clickable wrapper must not contain nested links or controls. Don't duplicate an "Open" action beside an already clear title link. Use one coherent foreground task surface instead of stacking dialogs for detail, edit and history.

## End-to-end journey with confirmation and recovery

| Step | Trigger and primary path | Branch, failure and return invariant |
| --- | --- | --- |
| 1. Locate | Filter collection, activate the record title link | Keep query/sort/page/scope and originating focus target in the navigation state |
| 2. Inspect | Read status, related preview and permitted actions | Zero related items: explain empty state and offer Add only if authorized; many items: show count and View all |
| 3. Edit | Explicitly choose Add related item or Edit existing item; preserve a stable draft | Narrow route or wide in-place subview; Escape/Back/Cancel have distinct non-mutating semantics |
| 4. Classify | Search/reuse labels or explicitly create a new definition | Creation waits for confirmed stable ID; remove token only unlinks membership, never deletes library definition |
| 5. Save | Validate, submit prerequisite if needed, reconcile it, then save dependent item | Partial success: name what saved; timeout: "outcome unknown" and look up authoritative ID before retry |
| 6. Review/history | Inspect timestamped history and permitted Archive/Trash/Restore action | Archived parent may retain active children; deep links and restore paths respect domain policy |
| 7. Return | Confirmed result refreshes collection at safe boundary | Restore filter, selection, scroll and focused link, or a surviving-neighbor/heading fallback if record disappeared |

## State and permission matrix

| State | What is shown / permitted | Acceptance observation |
| --- | --- | --- |
| Loading or no records | Stable context, labeled loading; distinguish truly empty from zero filtered results | No phantom success or unavailable actions |
| Active with related items | Identity, bounded preview, direct detail and allowed commands | No event collision; keyboard and screen reader expose names |
| Archived | Clear archived status and policy-defined visibility/child access | No action on a disabled parent without explanation |
| Trashed | Recoverable location and retention when supported | Restore only when authorized and parent exists |
| Pending save or lifecycle change | Precise operation, preserved draft and focus, duplicate activation guarded | No premature saved/removed announcement |
| Failed or partial | Targeted errors, known saved subset and supported recovery | No unintended duplicate, no lost child fields |
| Unknown outcome | "Not confirmed" with status lookup and stable request identity | No blind non-idempotent replay |
| Permission denied / parent missing | Explain unavailable record and safe alternate destination | No inaccessible child action, historical context retained as allowed |
| Concurrent revision | Show conflict with re-evaluate/merge path | No silent overwrite |
| Return after item removal | List scope, prior query and safe focus fallback | No focus stranded on an unmounted trigger |

## Small and wide alternatives

**Compact route (narrow/zoom):** collection page -> record route -> related item editor route -> confirmed result -> record/collection route. Use ordinary browser history where it matches task expectations; an unsaved draft guard must explain the consequence of Back. Identity, error summary and primary action precede secondary metadata; 320px reflow and translated labels must remain readable.

**Wide task surface:** collection and side-by-side record detail may coexist; use a single coherent in-place editor or one modal for an interruptive task. Tabs or peer subviews can switch detail/edit/history within a single surface when their state and focus are explicit. Do not put a second modal inside the first to select labels or inspect history. A specialized confirmation can interrupt for a genuinely irreversible decision, with safe focus return and draft retention.

## Anti-patterns and repairs

- **Nested hit targets:** clickable card wrapping title link, Add and menu -> use a clear title link and separately labeled commands.
- **Nested modal stack:** detail dialog -> edit dialog -> choose label dialog -> use one task context with peer subviews or a dedicated route.
- **Premature refresh:** parent list invalidates and unmounts editor after category creation but before child save -> keep feature/controller state alive, reconcile both writes, then refresh.
- **False Undo:** archive/delete only hides a row while toasting "Undo" -> use a real persisted reversal and durable recovery location, or do not promise Undo.
- **Silent scope change:** choosing a project silently rewrites global totals -> label scope and period per metric, preserve the prior context on return.

## Acceptance record for an actual consumer

Run one happy path and the branches above with real read/write authority in a test environment. Record **preconditions, action, expected state, observed state, browser/device and AT, scope and locale, mutation IDs (redacted), responsible reviewer and limitations**. Include keyboard Tab/Enter/Escape, menu focus after removal, spoken pending/unknown messages, touch targets, 320px/200% zoom, reduced motion where relevant, long translated text and RTL. For saved outcomes check both UI and authoritative read-back; for task completion capture a declared eligible population and errors/abandonment, not an invented success rate. All these tests remain **NOT VERIFIED** in this catalog example. [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) inform applicable accessibility expectations, not evidence of conformance or user task success.

**Other relevant canonical sources:** [Data visualization and dashboards](../knowledge/guidance/data-visualization-and-dashboards.md) for scoped overview-to-detail, [task flows](../specifications/patterns/task-flows-and-information-architecture.md) for scope/context, [Dialog](../specifications/components/dialog/spec.md) for modal focus, [Menu button](../specifications/components/menu-button/spec.md) for commands. Do not copy their normative behavior into this example.