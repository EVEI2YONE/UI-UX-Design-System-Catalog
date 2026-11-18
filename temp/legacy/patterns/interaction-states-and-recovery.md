# Interaction states and recovery

**Kind:** guideline · **Status:** proposed · **Primary layer:** behavior

## Purpose

Make system status and user control clear during input, asynchronous work, empty results and failure. States are part of the interaction contract, not optional polish.

## State model

| State | Guidance | Recovery / accessibility |
| --- | --- | --- |
| Default / focus / active | Controls visibly communicate availability and action | Keyboard and focus semantics |
| Disabled / readonly | Distinguish not-allowed from uneditable | Explain unavailable actions when needed |
| Loading / progress | Preserve context; prevent duplicate destructive actions | Appropriate status announcements; avoid excess noise |
| Empty | Explain why content is absent and how to begin | Actionable next step rather than blame |
| Validation error | Identify the field and how to correct it | Associate error with control; preserve input |
| Offline / timeout / partial error | State what succeeded and failed, retry safely | Idempotence and resumption as appropriate |
| Destructive confirmation | Explain permanence, consequences and alternatives | Deliberate confirmation and cancel path |
| Success | Confirm outcome and subsequent path | Announce important updates unobtrusively |

## Dialog/focus example

On opening a modal dialog, define an appropriate initial focus target; keep background interaction inaccessible when truly modal; provide an understandable close path. On close, restore focus to a sensible invoking element or next workflow target. Test special cases such as the invoker being removed. Consult [accessibility guidance](../guidance/accessibility.md).

**Avoid:** losing form data after a server error; spinners without status; a disabled button with no explanation; trapping focus after modal closure.

## Verification

Test real request failures, latency, translated errors, retry, touch and keyboard, screen reader notices, reduced motion and narrowed/reflowed containers. A documented state is not proof the app implements it.

## Recovery decision table

| Failure condition | Explain | Preserve | Safe next step |
| --- | --- | --- | --- |
| Client validation | Which input failed and how to fix it | Other entered values | Focus or link to invalid input |
| Network timeout | Outcome may be unknown | Current task and request context | Verify status before retrying non-idempotent operations |
| Permission denied | Action is unavailable in this context | Non-sensitive navigation state | Return or request authorized access |
| Partial success | Explicitly identify completed and pending items | Successful results | Retry only failed work when safe |
| Destructive action | Consequence and permanence | Relevant audit/confirmation context | Offer cancel; undo only when truly supported |

**State transitions:** specify idle → validating → pending → success/failure, cancellation, and retry. Avoid optimistic success messages for irreversible operations before confirmation. When a pending control is unavailable, do not remove the user's focus without a meaningful next destination. When an error replaces content, ensure the new message is discoverable to keyboard and screen-reader users.

**Test scenarios:** delayed response, double activation, lost connection after submission, server validation, expired permission, translated error, interrupted modal, and retry from the recovery state. Report actual run status; guidance is not proof of implementation.

## Batch 9 boundary — offline/sync and authentication

This page continues to own generic pending, timeout, retry, error and cancellation states. For **Saved on this device → Queued → Syncing → Synced** distinctions, divergent edits, concurrent conflict review and rejected offline work, use [offline work, synchronization and conflicts](offline-sync-and-conflicts.md). For expired sessions, safe reauthentication and legitimate account recovery, use [authentication lifecycle](authentication-and-account-lifecycle.md). Never automatically retry a consequential, potentially non-idempotent mutation after an ambiguous network failure. Describe verified local versus remote state; do not show “All saved” before backend confirmation.


## Human review and value-changing transaction lifecycle (2026-11-07)

**Evidence trigger:** Little Wins supports drafts, submitted contributions, returned-for-changes, approvals/rejections, item-level reviewer edits, points and reward reservation/fulfillment. Generic AI agent approvals are a different concept; do not reuse AI-specific automation assumptions for human-to-human moderation.

**Reusable state contract:** draft -> submitted -> returned -> resubmitted -> approved/rejected, with explicit permitted transitions and reasons. Maintain an immutable record of **who acted**, **for which subject**, **what version**, **when**, and **what changed** for consequential decisions, subject to a product retention/privacy policy. Display item-level differences and totals before commit; allow explanation and resubmission without silently replacing previous versions. Once value is awarded, use an authorized corrective entry with a reason rather than rewriting historical ledger entries; do not imply a correction UI exists when only accounting rules exist.

**Transactional UX:** surface pending/confirmed/failed/unknown outcomes; rely on authoritative backend confirmation, not optimistic points or a toast. Prevent duplicate credits/redemptions on replay; maintain balance/reservation consistency. For unknown outcomes, re-fetch transaction status before retry. Hide no state transitions merely because optional challenges/points/rewards are disabled; historical data may still require display and export.

**Positive example:** review screen shows submitted value, proposed edits, reviewer identity, calculated award, confirmation and a durable post-approval record. **Anti-example:** repeated Approve clicks award twice, or resubmission overwrites the sole preserved original.

**Tests:** valid/invalid transitions, concurrent reviewers, replay/idempotency, correction history, reward reservation/decline/refund, keyboard focus and announcements, timezone/locale-safe timestamps, recoverable validation errors. All product checks remain NOT VERIFIED unless actually executed.


## Batch 8 — paused capabilities and work already in progress (2026-11-07)

Do not conflate **paused**, **unauthorized**, **empty**, **disabled**, **unsupported** and **completed**. A capability paused by group configuration should identify what stopped, what remains preserved, what existing requests can still be managed, and how an eligible user resumes it. Do not show “No rewards” when redemptions are merely unavailable or hidden.

For feature-sensitive transactions, verify the authoritative configuration again when committing the action. When a setting changes between opening and submitting a form, preserve entered data where safe and explain the new state without claiming the action was saved. Existing requests and fulfilled outcomes may require management even when new actions are blocked; design an explicit route for authorized owners rather than relying on a hidden navigation item or browser history.

**Example:** “Rewards are paused. Existing requests are preserved. You can review pending requests in Group history.” The destination and permissions must actually exist before shipping such copy. **Anti-example:** “Your reward was redeemed” shown optimistically after the server rejects it because points were disabled.

**Check:** disable during pending request, failed direct command, refresh while editing, re-enable and accurate feedback; record actual persistence and keyboard/screen reader announcements. Source review is not a runtime PASS.


## Wireframe state-coverage and recovery annotations (proposed Batch 3, 2026-11-07)

**Use when:** preparing a static wireframe, screen sequence or design review of a task with async operations, empty data, permission limits, errors, success or reversible/irreversible actions. **Avoid when:** a polished default-state image is treated as the complete flow, state changes are implied to execute in an image, or speculative server permissions/outcomes are presented as observed behavior.

This is the canonical owner of **generic state and recovery semantics**. [Wireframe methodology](../guidance/wireframe-methodology.md) owns fidelity and static-to-interactive escalation; [task flows](task-flows-and-information-architecture.md) owns screen sequence and meaningful alternatives; [feedback](feedback.md) owns persistent/inline/transient message presentation; [forms](forms.md) owns field validation details; [offline/sync](offline-sync-and-conflicts.md) owns device/server sync states; [accessibility](../guidance/accessibility.md) owns implementation-level semantic and assistive checks. Avoid duplicate policy or invented application capabilities.

### Minimum state inventory: select by task, not a fixed count

Before illustrating, enumerate every **applicable** state and mark each `SHOWN`, `ANNOTATED`, `NOT SHOWN`, or `NOT APPLICABLE` with rationale. Do not label an unknown state `NOT APPLICABLE` simply to avoid designing it. The initial inventory is:

| State / transition | Wireframe must communicate | Critical annotation / verification boundary |
| --- | --- | --- |
| **Ready / default** | Current user task, meaningful content, available primary action | Screen ID, entry condition and intended next step |
| **Empty / first use / no results** | Why there is no content; constructive create, reset or help path | Distinguish first use from filtered no-results, deleted data and no permission |
| **Loading / pending / long wait** | Work in progress, retained context, available cancel/escape or safe continuation | Originating action, whether a retry is safe, outcome still unknown |
| **Field / submission validation error** | What failed, where and how to fix it, while preserving unrelated input | Intended association, error summary/focus destination; actual behavior NOT VERIFIED |
| **Network / service error and partial failure** | What completed versus failed; safe next action | Never assert failure if the result might be unknown; verify server outcome before replay |
| **Permission denied / expired session / unavailable capability** | Action unavailable, non-sensitive reason and legitimate way out or back | UI visibility is not authorization; avoid invented access escalation or data disclosure |
| **Success / confirmed outcome** | Which action completed, what changed and what to do next | Distinguish simulated success screen from actually confirmed product transaction |
| **Destructive or consequential confirmation** | What will change, permanence, scope and safe cancel | Undo only if supported; no optimistic promise about irreversible outcomes |
| **Recovery / return / retry** | Preserved task context, corrected input, return route and clear pending state | Focus/keyboard sequence and retained data need an interactive or runtime test |

A minimal default screen is not sufficient evidence of complete state coverage. A static set need not render all states as separate full screens: a labeled inset, reduced detail variant or state table may be appropriate when a screen-level interaction question is not being tested. **Do not substitute annotation for a prototype when transition behavior is the design question.**

### State-to-screen annotation contract

Keep a companion text table that survives image generation and contains:

`screen_id | task_step | trigger / precondition | from_state -> to_state | visible message + user action | information preserved | safe exit/retry | evidence (KNOWN / ASSUMED / ILLUSTRATIVE) | depiction (SHOWN / ANNOTATED / NOT SHOWN / NOT APPLICABLE) | behavior_test (NOT VERIFIED unless executed)`.

Use stable screen IDs (for example `S2-pending`, `S2-error`, `S2-confirmed`) and visible callout numbers matching the companion table. Show copy in editable text; image-rendered text can be distorted. Label fake result counts, messages, names, permissions and status as `ILLUSTRATIVE`. Describe **intended** focus return/announcement in the table, but do not claim they happened from a screenshot.

**Example (synthetic report export; capability not verified in any product):**

| Screen ID | Trigger | Depiction and user path | Continuity / evidence |
| --- | --- | --- | --- |
| `S3-ready` | Permitted export is *assumed* | Selected report, export scope, primary “Request export”, safe return | Permission is `ASSUMED`; do not label as authorized |
| `S3-pending` | User requests export | Progress/awaiting confirmation, action cannot silently duplicate | Request ID and persistence `NOT VERIFIED` |
| `S3-unknown` | Connection drops after request | “Status unknown”; option to check verified status, not blindly repeat | Preserve selection; server outcome `NOT VERIFIED` |
| `S3-failed` | Server definitively rejects request | Reason and safe recoverable edit/exit | Error source `ILLUSTRATIVE`; no claim of actual retry policy |
| `S3-confirmed` | Server confirms output | Confirmed result plus view/download **only if it truly exists** | Static mock is `ILLUSTRATIVE`, real confirmation `NOT VERIFIED` |

**Anti-example:** depict only `S3-ready` and a green “Export completed” toast, then declare error recovery, permissions and duplicate-prevention complete. That illustrates styling, **not** a tested state machine. An entirely different empty-results or permission-denied design should not be shown as the same loading state.

### Review and escalation checklist

1. Check applicability and coverage of ready, empty, pending, validation/error, partial/unknown outcome, unavailable/permission, success, consequential confirmation and return/retry. Mark omissions explicitly.
2. Compare primary actions and state language: pending must not appear confirmed; disabled/paused must not look empty; unknown outcome must not invite unsafe replay.
3. Preserve entered values or list filters where appropriate; identify exit, undo only where supported, and recovery when source data is stale or the trigger disappears.
4. Annotate intended live-region announcements, semantic errors, focus after opening/closing a dialog, keyboard paths, narrow viewport and localized strings; never treat static markup as observed assistive-technology behavior.
5. Escalate to a task-complete interactive prototype for transitions and to product/service tests for authorization, idempotence, persistence, focus, announcements and real outcome verification.

**Evidence:** this is repository-derived synthesis from existing proposed state, form, offline, feedback, accessibility and quality concepts, with [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) as implementation-oriented references. Standards are not proof of any illustration's conformance. Static wireframe state coverage can be *document-reviewed*; user studies, browser testing, server confirmation, keyboard/screen reader, RTL and zoom remain **NOT VERIFIED** unless separately performed. No canonical status or owner is promoted by these additions.


## B03 — icon/state synchronization and post-mutation focus continuity (CKG-09/10; proposed 2026-11-07)

**Purpose:** make transitions from component intent to authoritative outcome legible across icons, status text, action availability, selection and focus. Existing [icon semantics](../foundations/iconography-and-semantics.md) owns icon meaning; [component contracts](../architecture/component-contracts.md) owns event emission and sibling-state coordination; this pattern owns *when a workflow may present an outcome and how it recovers focus when content changes*. This is reusable guidance, not a new UI primitive or a claim that any app has implemented it.

### CKG-09 — synchronized icon, label and domain-state contract

| State/source | Icon and adjacent text | Action and data behavior | Do not do |
| --- | --- | --- | --- |
| Ready/idle (local) | Action icon and explicit verb/object; no outcome text | Allow an authorized action; preserve selected item | Use a checked/status icon to imply completion |
| Draft changed (local) | "Unsaved changes" where useful; optional pencil/dot | Keep inputs and dirty state; enable explicit Save as appropriate | Call a draft "submitted" or "synced" |
| Request pending (workflow) | Stable-width spinner or pending signifier with accessible working status | Prevent duplicate consequential submission; leave context and meaningful cancellation route when supported | Remove focused control without a fallback; swap to a success check on click |
| Confirmed, reconciled (authoritative) | Verified success text; optional success icon | Update item state, totals and dependent controls from authoritative results; consider continuation | Infer points/approval from previous suggestion or optimistic row styling |
| Definitely failed | Error text plus optional error icon, actionable correction/retry rule | Retain input, selection and intended object; retry only when known safe | Clear a form, collapse error content or display "No results" |
| Outcome uncertain / timeout | "Outcome unknown—check status" or equivalent; uncertainty icon secondary | Block blind duplicate write and reconcile by stable identity/version | Treat timeout as definitely failed or definitely committed |
| Stale/conflicted state | "Changed since you opened it" with current-context explanation | Refresh/reconcile, preserve non-conflicting draft where possible, revalidate permissions | Silently apply stale action or automatically move to another record |
| Item no longer eligible | Explain state/permission change; status text | Remove unsafe command; provide safe queue/navigation destination | Hide all explanation and strand focus |

**Rules:** visual icon swaps must not trigger data mutations; state changes flow from the owning controller's validated state. A status icon and colored badge are never the sole signal. Keep control dimensions stable across idle/pending/confirmed to avoid pointer-target movement; announce material asynchronous changes sparingly via appropriate status regions without repeatedly stealing focus. An icon-only control retains an accurate accessible name; if its underlying action changes, ensure that new purpose is deliberate and discoverable rather than silently overloading the same target. Recheck server authority before consequential transitions. Status badge typography, accessible labels and icon meaning remain localizable and theme/forced-color resilient.

### CKG-10 — focus and contextual continuity after a changing collection

Before each mutation, identify: **invoking control, active item ID and revision, current list/filters/sort/pagination, editable draft, focus origin and expected focus destination.** Preserve or intentionally revise these based on the observed outcome—not on a guessed successful click.

| Result | Post-transition focus/selection | Feedback/recovery |
| --- | --- | --- |
| Validation error, item remains | Usually keep focus or direct to the specific failed field / linked summary as warranted | Retain values and in-context error |
| Network error or uncertain outcome | Keep current task and stable focused action/error destination; do not auto-advance | Explain safe reconcile vs retry; do not reset selection |
| Confirmed mutation, original trigger still exists | Preserve focus on meaningful existing control when doing so remains useful | Announce confirmation without forced navigation |
| Confirmed removal or filtering-out of selected row | Select a logical next eligible item only if workflow contract permits; otherwise focus stable queue heading/status/toolbar | Do not attempt to restore focus to an unmounted or hidden row |
| Dialog closes while its invoking item disappears | Restore focus to remaining logical task target, stable list heading or explicit return control | Announce changed state; do not trap focus in removed overlay |
| Queue subset exhausted but more pages may exist | Focus stable "Load more" or queue-summary control, not a false "All done" declaration | Distinguish loaded subset empty from globally complete queue |
| Permission revoked / scope changed | Focus authorized fallback heading/action; drop disallowed action controls | Explain access change without exposing inaccessible data |

**Pointer and keyboard parity:** a stable action position may reduce mouse movement, but DOM reading order and keyboard focus targets determine whether a layout remains usable. Do not move focus just because background data refreshed, never force focus to a newly appearing toast by default, and test reflow at narrow widths/zoom. When success changes what is currently focused, choose a meaningful announced target and test it using keyboard and assistive technologies. `aria-live` status is for relevant updates; it cannot repair a missing focus destination.

### Worked example — review decision and conditional continuation (illustrative)

```text
item_selected
  -> decision_input_ready
  -> submitting (current item locked; no repeat)
  -> server_acknowledged
  -> authoritative_read_reconciled
  -> confirmed_result_announced
  -> next_eligible_selected OR queue_navigation OR user_stop

submitting
  -> validation_error (preserve selection + notes)
  -> definitely_failed (safe retry if contract allows)
  -> result_uncertain (reconcile first; never blind replay)
  -> stale_revision / permission_changed (refresh, revalidate, explain)
```

A server acknowledgment is not automatically proof that all dependent read models are reconciled; the appropriate consistency contract is application-specific. Only advance when the task's authoritative completion condition is met. Never select a different item merely because a local optimistic cache removed the old one. The [task-flow contract](task-flows-and-information-architecture.md#b03--spatial-continuity-and-sequential-task-progress-ckg-1112-proposed-2026-11-07) owns when and whether to auto-select the next eligible item.

**Counterexample:** a reviewer clicks Approve, spinner instantly becomes a green check, pending item is removed from the DOM and focus disappears; a timeout later leaves the actual decision uncertain, yet the UI opens another contribution. Correct behavior leaves the outcome unsettled, retains context and offers authoritative verification before advancing.

### B03 verification (all application checks NOT VERIFIED)

| Scenario | Required observable evidence | Status |
| --- | --- | --- |
| Delayed, failed and ambiguous write | No premature success icon/label or unsafe duplicate; current task remains recoverable | NOT VERIFIED |
| Authoritative result with changed dependent data | Status, counts, permitted actions and item detail agree | NOT VERIFIED |
| Row removal and modal trigger disappearance | Logical focus destination for pointer, keyboard and screen reader | NOT VERIFIED |
| Queue subset/permission changes | No false completion or unauthorized next item; clear recovery and focus | NOT VERIFIED |
| Narrow/zoom/RTL/long labels and reduced motion | Stable action identity, readable feedback, practical hit targets | NOT VERIFIED |
| Live-region and focus announcement behavior | Relevant updates announced once without excessive focus jumps | NOT VERIFIED |

**References:** [WAI-ARIA APG Dialog (Modal)](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [WAI-ARIA APG patterns](https://www.w3.org/WAI/ARIA/apg/patterns/) (consulted 2026-11-07). Motivating source: [Little Wins B06/B07/B08 proposed interaction knowledge](https://github.com/EVEI2YONE/Little_Wins/tree/main/docs/little-wins/ui-knowledge/); observed source behavior does not certify UX benefit, accessibility or implementation.

## Phase 6 executable pattern reference (2026-11-08)

The visual catalog now includes an actual [Interaction recovery implementation](../site/src/implementations/patterns/recovery/Recovery.js), its [deterministic synthetic scenarios](../site/src/implementations/patterns/recovery/scenarios.js), and [scoped demonstration styles](../site/src/implementations/patterns/recovery/Recovery.css). The executable source used by the sandboxed preview is displayed verbatim in the site's source inspector. This is a **reference demonstration**, not a product backend, a verified end-to-end integration or a published package. Canonical review status remains `proposed`. Actual keyboard/AT behavior, responsive visuals, localization, measured performance and authoritative service integration are **NOT VERIFIED** by the Node/Python source tests. See the [Phase 6 evidence ledger](../docs/visual-catalog-refactor/12-phase-6-composed-patterns.md).
