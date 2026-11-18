# Review Workspace

**Kind:** feature reference specification · **Status:** proposed · **Primary knowledge layer:** experiences  
**Canonical ID:** `feature.review-workspace` · **Owner:** unassigned · **Review date:** not reviewed  
**Implementation evidence:** source-controlled synthetic reference exists; real backend integration, user studies and browser/assistive technology verification **NOT VERIFIED**.

## User job and reuse justification

Help an authorized reviewer inspect a queue of pending records, examine relevant evidence, capture a reason where required, choose a decision, understand the outcome, and continue without losing orientation.

**Credible reuse contexts:** human review of submitted content or quality exceptions in a community product; administrative moderation of user-reported records in another product. These are *proposed scenarios*, not evidence of adoption or validated user research. The reference is intentionally domain-neutral and does not calculate points or define a specific application's approval policy.

**Use when** an application has a bounded human-reviewed queue, row-level context, explicit decision commands, and service-confirmed outcomes. **Avoid** when a lightweight confirm dialog is sufficient, an action is solely an AI tool approval, or a single record form is owned entirely by one application. The [agentic approval pattern](../../patterns/agentic-actions-and-approvals.md) specifically owns AI-agent delegated action approval; this workspace is a **human administrative review** example, not an AI authorization engine.

## Ownership and integration contract

| Catalog reference owns | Consuming application owns |
| --- | --- |
| Queue/detail UI, selection, evidence presentation, reason capture, focus recovery, state labels, safe local interactions | Authentication, server-side permission enforcement, domain decision policy, record visibility, confidential data minimization |
| Typed conceptual adapter contract and synthetic deterministic simulation | API requests, authoritative storage, idempotency keys, revision checking, server audit/event records |
| Explicit pending, denied, conflict, error and uncertain-outcome states | Real status verification before replay, reconciling authoritative results, audit/observability and policy-specific escalation |
| Accessibility and performance test plans | Actual user/role validation, legal/compliance rules, production availability and telemetry |

UI `canDecide` flags express a **display affordance only**. They must not be used to bypass a real server authorization check. The synthetic adapter has no credentials, network calls, persistence or user identity.

## Task flow and states

```text
Queue (loaded / empty / error / loading)
  -> select record -> inspect title, description, status, revision
  -> choose Approve / Return / Reject, optionally explain reason
  -> validate input and local availability
  -> simulated request pending (no duplicate submit)
  -> simulated confirmed | denied | stale revision/conflict | known failure | unknown outcome
  -> confirmed: show truthful result and return to queue
  -> denied/conflict/error: preserve selected record, note and context
  -> unknown: prohibit blind retry; verify authoritative-like status in simulation
  -> verify known outcome: conclude / review again according to actual application policy
```

| Scenario | UI responsibilities | Authorized service responsibilities | Focus and recovery |
| --- | --- | --- | --- |
| Default / selected | Name queue, allow inspection of records, label actions | Filter authorized records | Selected detail heading gets meaningful focus |
| Empty or initial loading | Differentiate empty from pending; provide context | Return authoritative records and loading status | Queue heading and status remain findable |
| Read-only / permission denied | Explain decision controls are unavailable | Enforce real permissions | Keep record details readable where authorized |
| Validation error | Explain actionable missing reason for return/reject | Validate request body and policy | Focus reason label/input; preserve entry |
| Pending | Lock duplicate decision, show progress | Execute scoped/idempotent decision | Keep selected record and status |
| Confirmed | Show confirmed outcome rather than optimistic animation | Supply confirmed status and audit record | Focus queue heading/next record |
| Stale revision | Explain record changed; disable stale repeat | Reject stale mutation; supply current version | Keep selection; offer refreshed inspection |
| Known service failure | Differentiate failure from empty; preserve note | Return known rejection/error | Safe retry only when policy says no commit |
| Unknown outcome | Say state cannot be confirmed; avoid retry | Verify the authoritative operation first | Verification action; no blind resubmit |

## Configuration, data and mock adapter

`ReviewWorkspace.mount(container, options)` accepts a `scenario` object and safe renderer callbacks. The synthetic adapter contract used by the reference is deliberately simple:

```text
list() -> {records: ReviewRecord[]}
get(id) -> ReviewRecord | null
decide({id, revision, action, reason}) ->
  {kind: "confirmed"|"denied"|"conflict"|"error"|"unknown", ...}
verify(id) -> {kind: "confirmed"|"unresolved", ...}
```

Records require stable `id`, visible `title`, plain-text `summary`, `revision`, and `status`. The adapter only reads and updates **in-memory synthetic fixtures**. A real adapter must enforce permissions, validate revisions and returned outcomes, reconcile confirmed vs unknown states, redact evidence, and supply trustworthy audit provenance.

### Initial preview scenarios

Loaded queue, empty, loading, read-only, denied, stale conflict, known failure, unknown/lost acknowledgement, long translated-like text and many records. The same executable source is used by the preview and source viewer. The scenario selector resets synthetic adapter state.

## Composition and guidance dependencies

- [Button](../../components/button/spec.md), [Field](../../components/field/spec.md), [Dialog](../../components/dialog/spec.md) — semantic controls and user focus decisions.
- [Forms](../../patterns/forms.md) — reason validation and preservation.
- [Data tables](../../patterns/data-tables.md), [search/filter](../../patterns/search-and-filter.md) — queue discoverability and selection.
- [Interaction recovery](../../patterns/interaction-states-and-recovery.md) — pending/unknown/retry semantics.
- [Role-aware workspaces](../../patterns/role-aware-workspaces-and-context-switching.md) — context signaling; no UI-only access control.
- [Agentic approvals](../../patterns/agentic-actions-and-approvals.md) — related but different delegation/authorization workflow; **do not duplicate**.
- [Accessibility](../../guidance/accessibility.md), [internationalization](../../guidance/internationalization.md), [performance](../../guidance/performance-and-perceived-speed.md).

## UX, accessibility, readability, responsiveness and performance

The queue and detail must remain distinguishable at narrow widths, with persistent selected-record context, clear action names, non-color-only status, meaningful error text and visible focus. Evidence and note values must wrap; title and command sequence remain logical at zoom and under translation expansion. Important status text must use appropriate live announcements without repeated or deceptive claims. Keyboard users must reach every button, textarea and review item; when an item disappears, focus should move to an appropriate remaining queue target.

Bound rendered rows or paginate larger queues instead of rendering unbounded lists. Confirm that fixture sizes and source loading do not interfere with the catalog's static navigation. Measure browser interaction, resize/reflow, screen reader reading order and real device performance before claiming suitability for production.

## Reference and evidence

- **Implementation:** [ReviewWorkspace.js](../../site/src/implementations/features/review-workspace/ReviewWorkspace.js)
- **Synthetic adapter:** [mock-adapter.js](../../site/src/implementations/features/review-workspace/mock-adapter.js)
- **Scenarios:** [scenarios.js](../../site/src/implementations/features/review-workspace/scenarios.js)
- **Styles:** [ReviewWorkspace.css](../../site/src/implementations/features/review-workspace/ReviewWorkspace.css)
- **Preview route:** `/catalog/features/review-workspace/` when generated and served from the site root. No deployment is claimed.
- **Tests:** [reference source-level tests](../../site/tests/review-workspace-runtime.test.cjs) plus static site/registry tests.
- **Evidence ledger:** [Phase 7](../../docs/visual-catalog-refactor/13-phase-7-review-workspace.md).

| Check | Status |
| --- | --- |
| Canonical contract and cross-context rationale authored | DOCUMENTED; reviewer approval pending |
| Working synthetic reference and source parity | CI verification required |
| Product authorization, persistence, audit, conflict resolution | NOT IMPLEMENTED (consumer-owned) |
| Real browser focus/AT/zoom/RTL/contrast/performance | NOT VERIFIED |
| Actual adoption in other applications | NOT VERIFIED |

A reviewed, executable **reference** does not imply a production-ready feature or an installable package. Preserve `proposed` until the governance review gate is satisfied.
