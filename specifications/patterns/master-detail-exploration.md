# Master-detail exploration

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Let people move between a collection and item details while preserving selection, orientation, filtering context and next-action continuity.

**Use when:** A list of records, messages, products or documents supports repeated inspection and contextual actions.

**Avoid when:** A single record has no meaningful collection context or a static article list works with standard links.

**Ownership:** The pattern owns composed collection/detail presentation and selection semantics. Each feature owns record retrieval, authorization, mutations and route state.

**One-minute task-surface chooser:** (1) If the action is brief, low risk and needs no new destination, favor inline edit; (2) if the person inspects peer Overview/Edit/History views, retain one stable detail context; (3) if a brief interruption truly needs exclusive attention, use a single Dialog; (4) if a supporting side task must preserve surrounding context, consider a drawer only after zoom/focus checks; (5) if work is long, high stakes, resumable or shareable by URL, choose a named route. **Then** specify save outcome, draft lifetime, Back/Cancel/Escape and return focus before implementation. This ordering is a proposed cross-source decision model, not a platform mandate.

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

| Trigger | Preserve and communicate | Resume / focus |
| --- | --- | --- |
| Open record or change Overview/Edit/History peer view | Stable ID, list filters and the appropriate draft; distinguish view state from browser history | Heading or active peer view; return to initiating record |
| Internal Back, browser Back, Cancel, Escape or backdrop | Define the owning surface and a keep/discard choice for dirty edits; no silent loss | Keep editing or return to detail/list by an explicit route policy |
| Save pending, invalid/denied/conflicting or timeout / acknowledgement lost | Distinguish pending/error/**outcome unknown** from confirmed success; do not duplicate a write on retry | Keep draft and cursor; reconcile backend truth; focus linked error or stable detail target |
| Confirmed save or removed invoker / filtered or archived record | Update only after authoritative confirmation; explain why the original target disappeared | Focus a surviving relevant record or collection heading rather than a detached node |
| Deep link / refresh / unavailable item | No required prior list/history entry; recheck permissions and provide a safe not-found return | Focus a descriptive heading and usable recovery route |

**Wide/compact alternatives (illustrative):** A wide surface can retain the filtered collection beside detail with peer Overview/Edit/History views. At 320 CSS px equivalent, choose a detail route rather than a cramped split pane; a drawer is only suitable if its content and actions reflow. Deep-linkable or resumable edit tasks warrant a dedicated route on either width. Real behavior is **NOT VERIFIED**.

### Source-to-decision provenance and scope

These sources justify **specific parts** of the choice; no single external source establishes a universal hierarchy of inline edits, drawers, tabs and routes. The composite chooser is a **proposed catalog synthesis** and must be validated for a particular application's tasks, platform and users.

| Source (consulted 2026-11-19) | Supported decision | Limit / product-owned judgment |
| --- | --- | --- |
| [USWDS Modal](https://designsystem.digital.gov/components/modal/) | A modal intentionally interrupts; consider non-modal alternatives, especially for multi-step or complex forms | USWDS guidance is for its design-system context, not a prohibition on all modal editing |
| [WAI-ARIA APG Dialog (Modal)](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) | The active modal contains keyboard focus; on close, use the invoker or a logical workflow fallback when removed | APG defines dialog semantics, not which task deserves a dialog or whether a route is preferable |
| [WAI-ARIA APG Tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/) | Use tabs for peer panels with a defined keyboard/selection model; avoid automatic activation when remote loading causes noticeable latency | Tabs are not an arbitrary back stack, stepper or answer to unsaved data ownership |
| [GOV.UK Back link](https://design-system.service.gov.uk/components/back-link/) and [Check answers](https://design-system.service.gov.uk/patterns/check-answers/) | Give multi-page tasks a predictable route back, preserve earlier form values and allow targeted editing without replaying subsequent steps | These are government service patterns; route model, local drafts and browser history remain feature decisions |
| [WCAG 2.2, Understanding Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) | Check content at 320 CSS px equivalent without loss of function or two-dimensional scrolling except justified exceptions | Reflow does not require drawers or forbid split panes at other widths; content and user agent must be tested |

**Source-to-claim boundary:** WAI-ARIA and WCAG address applicable interaction/accessibility conditions; USWDS and GOV.UK provide design-system guidance and tradeoffs. None of them demonstrates that this catalog's synthetic workflow improved user outcomes. Permission, server truth, transactional integrity, undo and draft persistence are owned by consuming products and their relevant canonical patterns.

### Worked decision and expected task observations

**Synthetic scenario (NOT VERIFIED):** From a collection filtered to `status: active`, open record A, edit related record B, view its history, return to record A and then to the collection. The design **chooses a shared detail subview** on wide screens because overview/edit/history are peers and list context should remain visible. It **chooses a detail route** on a compact viewport when dual panes cannot reflow. If record B requires a resumable multi-page edit or deep link, a named edit route wins on either width. This is a decision illustration, **not** observed user research.

| Step / condition | Expected visible result and explicit focus/return target |
| --- | --- |
| 1. Open A from a filtered collection | A's stable identity and heading appear; filter, sort, scroll anchor and source identity are retained. Keyboard focus moves to the detail heading or deliberate first control |
| 2. Open B's Edit in the same surface | Edit heading/peer view is identified; a related record does not create a second independent modal. Draft is scoped to B's stable ID |
| 3. Inspect History, then return to Edit | No unsaved fields are silently lost; restore edit context, cursor/section where appropriate; do not confuse the History peer view with a required step |
| 4. Save confirmed, or save pending/unknown | Remain in edit until authoritative reconciliation; announce pending or unknown. Never duplicate a non-idempotent request on lost acknowledgement. On success, focus a stable detail target |
| 5. Cancel / Escape / Back on a dirty edit | Keep editing or explicitly discard via a comprehensible choice; browser Back and internal Back follow documented, distinct policies; no invisible editor is left holding focus |
| 6. Return, or A/B becomes unavailable | Show the collection with preserved query and meaningful scroll. If the invoker is removed or permission is revoked, explain the change and focus the nearest surviving item or collection heading, never another item by array index |

**Anti-example and repair:** Three modal layers—Details -> Manage -> Edit—disagree about Escape, Save and the focus owner; the parent list remount silently deletes B's draft. Replace them with **one** stable detail task context (or directly linked routes) and put an exceptional consequential confirmation in an explicitly controlled interruption, retaining the parent draft and an unambiguous return.

### Executable acceptance specification (tests NOT VERIFIED in a consuming product)

Run these checks against an **actual** consumer revision, not a Markdown render. For each case capture the build/route, role, record IDs, initial data, interaction sequence, expected/observed result, browser/OS, viewport/zoom, language/direction, assistive technology where applicable, owner and evidence URL. Mark each PASS, FAIL or NOT VERIFIED individually; do not infer a product pass from catalog CI.

| Case | Setup and action | Expected result | Status |
| --- | --- | --- | --- |
| MD-01 / keyboard navigation | With two visible records, Tab/Enter to open A, switch Edit/History and return | No nested active focus trap; correct headings/selected peer view; focus survives return | NOT VERIFIED |
| MD-02 / compact and reflow | Repeat MD-01 at 320 CSS px equivalent, 400% zoom where applicable, long translated labels and RTL | No required action clipped or unreachable; detail route works; Back reaches the filtered collection | NOT VERIFIED |
| MD-03 / dirty draft | Change B, invoke internal Back, browser Back, Escape, Cancel and backdrop where present | Each exit has a defined keep/discard policy; input remains intact unless explicitly discarded | NOT VERIFIED |
| MD-04 / save recovery | Delay acknowledgement; simulate validation failure, timeout-after-commit and revision conflict | Pending/unknown/errors are distinguishable; draft retained; reconcile truth before retry; no duplicate command | NOT VERIFIED |
| MD-05 / absent invoker | Archive A, filter A out or revoke access while B's edit or return is pending | Explain unavailable context; no focus on a removed node; fallback chooses a surviving record or collection heading | NOT VERIFIED |
| MD-06 / direct URL and history | Open A's deep link from a new tab, refresh, navigate Edit and browser Back | No assumption of prior invoker; direct route and safe return remain meaningful; authorization rechecked | NOT VERIFIED |
| MD-07 / screen reader and touch | Repeat the edit and return using screen reader+keyboard, touch, high contrast and reduced motion | Labels, status, instructions, focus, actions and close paths remain usable without hover or color alone | NOT VERIFIED |

**Evidence maturity:** These are expected observations only. Real application/server, assistive technology, locale and usability tests are **NOT VERIFIED**; no independent human review is logged. Standards sources do not certify the catalog or any consumer.

## Inclusive operation, content, theming and locale

Apply the MD-01–MD-07 checks to keyboard, screen reader, mobile, high zoom, long translations, RTL, high contrast and reduced motion. Preserve clear headings, user-visible current view, status beyond color, focus and real return paths; a static example does not validate interaction behavior.

## Example and anti-example

**Illustrative:** A filtered inbox opens message A, switches a related item's Edit/History views, and restores the list query and meaningful focus on return. The MD-01–MD-07 cases above define expected observations, not product results.

**Anti-example:** Choosing a record by array index after sorting can display the wrong person's details; a stack of Details/Manage/Edit modals loses draft and focus ownership. Use stable IDs and one coherent surface or named routes. See the [collection-to-related-record journey](../../examples/collection-to-related-record-journey.md) for a broader synthetic composition.

## Sources, related concepts and limitations

- [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/patterns/) — contextual reference, not a universal implementation prescription.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual reference, not a universal implementation prescription.
- Related canonical guidance: [Task flows](task-flows-and-information-architecture.md), [Forms](forms.md), [Interaction recovery](interaction-states-and-recovery.md), [Accessibility](../../knowledge/guidance/accessibility.md), and [UX measurement](../../knowledge/guidance/ux-measurement.md).
- Review domain, locale, security, legal and service constraints separately before adoption.
