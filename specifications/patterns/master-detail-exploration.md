# Master-detail exploration

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Let people move between a collection and item details while preserving selection, orientation, filtering context and next-action continuity.

**Use when:** A list of records, messages, products or documents supports repeated inspection and contextual actions.

**Avoid when:** A single record has no meaningful collection context or a static article list works with standard links.

**Ownership:** The pattern owns composed collection/detail presentation and selection semantics. Each feature owns record retrieval, authorization, mutations and route state.

## Journey and state contract

| Stage | User-visible decisions and states | Recovery / evidence requirement |
| --- | --- | --- |
| Find | Browse, search, sort and filter a list | Clear selected item and result context |
| Select | Open item detail by stable identity, not list position | Selected/focused items remain distinguishable |
| Inspect | Show relevant detail and contextual actions | Preserve access to list context |
| Change collection | Handle delete/archive/new result while item is selected | Choose safe next focus/selection fallback |
| Return | Restore useful list position, query and filters where appropriate | Deep links and back behavior remain predictable |

## Design decisions

- At narrow widths, choose a clear list-to-detail route rather than shrinking both panels until text is unreadable.
- Avoid coupling selected data to array index: sorting or filtering must not expose another person's record.
- When a selected item disappears, announce the change and choose a visible, relevant fallback.
- If details update asynchronously, distinguish stale cached content from confirmed changes; never silently jump contexts.
- Use navigation links for destinations and buttons for actions, keeping selection separate from command activation.

## Choose one task surface across detail, edit and history

**Start with the task hierarchy, not an overlay hierarchy.** Map collection -> selected record -> overview / edit / history -> confirmed outcome -> return. Choose **one foreground task surface** that supports those transitions. The feature owns authorization, route state, persistence and draft lifetime; this pattern owns the composition and context-preservation decision. [Dialog](../components/dialog/spec.md), [Tabs](../components/tabs/spec.md), [Navigation](navigation.md), [Forms](forms.md) and [Interaction recovery](interaction-states-and-recovery.md) own their respective behavior contracts.

| Task scope and constraints | Prefer | Avoid / escalate when |
| --- | --- | --- |
| A brief, low-risk field change or local extra detail | Inline expansion/edit, preserving collection orientation | Input is lengthy, consequential or independently deep-linkable |
| Repeated overview, edit and history for one selected record | In-place detail subview or peer tabs **inside the same stable detail surface** | The steps must be completed in sequence, or the user needs a shareable route |
| One short, focused choice or bounded edit | A **single** modal dialog with an explicit dismissal and draft policy | Child management or history turns the modal into a stack of independent tasks |
| Supporting work benefits from visible collection context | Side drawer/sheet, only when content, keyboard focus and scroll remain usable | A narrow/zoomed viewport is cramped or task depth warrants browser history |
| Long, resumable, high-input-risk or directly addressable task | Dedicated route with heading, return destination and normal history behavior | The task is small enough to handle without a disruptive route change |
| Exceptional destructive confirmation while an editor is foregrounded | A brief, explicitly reviewed interruption; prefer in-surface confirmation or sequential replacement when possible | Stacked modals would confuse Escape, focus ownership or the parent draft |

**Decision rule:** Choose the least complex surface meeting the actual task's depth, risk, focus, save, resumption and URL needs. A mobile drawer is not automatically better than a route. Model view/edit/history as peer subviews only if they truly are peers; [Tabs](../components/tabs/spec.md) are not a substitute for a mandatory sequence. A surface switch is not automatically a browser-history entry: state explicitly which navigation is internal and which is a durable route.

### Back, state and focus matrix

| Transition / condition | Navigation and visible outcome | State and focus expectation |
| --- | --- | --- |
| Collection -> record | Keep selected identity and source list context, or navigate to a named route | Capture stable invoker/record ID, filters and useful scroll; focus detail heading or first meaningful control |
| Overview -> edit / history | Switch a peer subview in the **same** detail surface when appropriate | Preserve editing draft across peer views, identify the active view and set an intentional focus target |
| Internal Back, Cancel or Escape with clean state | Internal Back returns to detail; Cancel exits edit; Escape dismisses the **owning** overlay if appropriate | Do not confuse internal Back with browser Back; return focus to a surviving relevant target |
| Back / Cancel / Escape / backdrop with dirty draft | Offer Keep editing / Discard before destroying work, including when product-supported browser navigation would leave the route | Preserve draft and selection; do not silently discard values or trap users in an uncloseable surface |
| Save pending | Report pending state; do not close, double-submit or unmount the active editor | Keep draft, caret/focus context and status perceivable; defer parent refresh to a safe boundary |
| Save confirmed | Reconcile authoritative saved state, then change surface/refresh intentionally | Focus updated detail, surviving related action or collection context; do not claim success early |
| Invalid input / denied access / revision conflict | Stay in the task with specific recovery options | Retain valid values and focus a linked error or meaningful summary |
| Timeout / acknowledgement lost | Say **outcome unknown**; check authoritative state before retrying a non-idempotent write | Keep editor and draft intact without automatic duplicate creation |
| Removed invoker / filtered or archived record | Explain why the original action or selected row disappeared | Focus a surviving relevant item or collection heading, never a detached element or another record by array index |
| Deep link / browser refresh | Restore the authorized route, record and permitted view, or a safe not-found/denied return | Show clear heading and recovery even without a previous invoker or meaningful browser-history entry |

**Wide-screen illustration (NOT VERIFIED):** The collection and stable detail region appear side by side. Within the selected detail, a user switches Overview -> Edit -> History, saves a related item, then returns with list filters and selection intact. If edit/history must be shareable or resumable, choose dedicated routes instead of forcing everything into a pane.

**Compact/zoom illustration (NOT VERIFIED):** The collection opens a detail route with a visible Back-to-results link; Edit has its own Back-to-detail control. A single full-height dialog is an alternative only for a short, bounded task with a supported focus and draft policy. A drawer must still work at 320 CSS px equivalent, with large text, translations, touch and RTL; its visual form alone does not solve those needs.

**Anti-example:** Collection -> Details modal -> Manage modal -> Edit modal creates three independent Escape paths, conflicting focus traps and unclear draft ownership. If the parent list refresh unmounts the editor while Save is pending, the last changes disappear. **Repair:** keep the related work in one stable detail surface, or route to a named edit page; interrupt separately only for a justified consequential confirmation and return to the preserved parent task.

### Source limits and acceptance checks

- [WAI-ARIA APG Modal Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) describes modal focus containment, initial focus and logical return when an invoker no longer exists. It does **not** prescribe which task surface to choose or prohibit every nested dialog.
- [WAI-ARIA APG Tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) applies when peer tabs are the selected control, not to sequential tasks.
- [WCAG 2.2 Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) informs narrow/zoom checks. Choosing a surface, browser-history policy and draft lifetime are proposed catalog synthesis, not empirically established standards.

| Representative consuming-product test | Expected outcome | Status |
| --- | --- | --- |
| Keyboard + screen reader: list -> detail -> edit -> history -> return | Controls and headings named, no inaccessible layer, clear selected view and meaningful return focus | NOT VERIFIED |
| Dirty draft: internal Back, browser Back, Escape, Cancel and backdrop | No silent input loss; only the owning surface dismisses and the choice is understandable | NOT VERIFIED |
| Save pending/error/unknown; invoker removed; permission revoked | Editor lifetime and honest outcomes preserved, safe focus fallback and no duplicate mutation | NOT VERIFIED |
| Direct link, refresh, compact/320px, zoom, long translation, RTL, touch and theme | No unreachable action or clipped content; route and recovery semantics consistent | NOT VERIFIED |

For any executed test, record task, browser/OS, assistive technology, locale, viewport/zoom, exact product revision, expected and observed result, owner and limitations. **Runtime behavior, user-task success and accessibility conformance remain NOT VERIFIED** in this catalog.

## Inclusive operation, content, theming and locale

Provide keyboard and assistive-technology routes through each stage, visible headings and state feedback, and deliberate focus restoration after context changes. Support zoom/reflow, localized labels and units, RTL and high-contrast themes, touch alternatives and reduced motion. Use semantic tokens and make unavailable or irreversible outcomes understandable beyond color. Never treat a mock preview as proof of a real service outcome.

## Example and anti-example

**Illustrative example:** An email inbox retains query and scroll location after opening a message and returning; deleting it selects the next available message with focus explained.

**Anti-example:** Selecting row 4 by array index so a sort instantly shows a different person's private details.

For a worked cross-pattern composition using a card, detail, related-record editor, classification, recovery and return, see the [illustrative collection-to-related-record journey](../../examples/collection-to-related-record-journey.md). Use the canonical card, form, lifecycle and recovery contracts for normative decisions; the reference journey is **NOT VERIFIED** in a consuming product.

## Verification and research handoff

| Scenario | Expected evidence | Current status |
| --- | --- | --- |
| Deep link, browser back and responsive list-detail transitions | Record actual observed result, relevant cohort and environment | NOT VERIFIED |
| Filter/sort/selection stability, record deletion and empty states | Record actual observed result, relevant cohort and environment | NOT VERIFIED |
| Keyboard/assistive focus, RTL reading order, long details and data privacy | Record actual observed result, relevant cohort and environment | NOT VERIFIED |

Measure task completion, user error severity, abandonment and comprehension before asserting improvement. No baseline study, real back-end behavior or accessibility conformance is supplied by this concept.

## Sources, related concepts and limitations

- [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/patterns/) — contextual reference, not a universal implementation prescription.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual reference, not a universal implementation prescription.
- Related canonical guidance: [Task flows](task-flows-and-information-architecture.md), [Forms](forms.md), [Interaction recovery](interaction-states-and-recovery.md), [Accessibility](../../knowledge/guidance/accessibility.md), and [UX measurement](../../knowledge/guidance/ux-measurement.md).
- Review domain, locale, security, legal and service constraints separately before adoption.

## Applied decision and verification case

**Illustrative decision case (not observed):** Add an item-to-list return and focus restoration scenario. Name the initiating task, what becomes unavailable or uncertain, how the user learns the truthful state and which continuation is safe. Distinguish user-visible feedback from server authority and explain when the simpler existing pattern should be reused.

**Acceptance boundary:** Specify an observable expected result for primary action, keyboard/focus recovery, relevant locale/RTL and small-screen conditions and a negative or failure state. Link the selected test to the concept's existing canonical owner instead of introducing an overlapping shared control. A [WCAG 2.2](https://www.w3.org/TR/WCAG22/) reference supports applicable web accessibility criteria but does not verify an implementation, independent review or actual task completion. Unexecuted checks remain **NOT VERIFIED**.

