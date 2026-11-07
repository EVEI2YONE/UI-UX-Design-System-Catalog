# Account and settings portal composition

**Kind:** guideline · **Status:** proposed · **Layer:** experiences · **Owner:** unassigned · **Reviewed:** null

## Purpose and ownership

Use this pattern when users need a coherent place to understand and change account identity, contact details, preferences, security, privacy, notifications or billing. Avoid treating a generic settings screen as a substitute for authoritative permission, identity, privacy or payment policy. This page owns **cross-section composition, navigation, account overview, profile editing and save behavior**; specialized security, billing and consent rules remain with their respective canonical pages.

### Navigation and overview contract (KG-001, KG-002)

- Group by user mental model and consequence: **Profile**, **Security**, **Privacy & data**, **Notifications**, **Appearance & language**, **Billing & plan** where supported. Do not render unavailable or inapplicable groups merely to complete a template.
- Put account identifier and status in an understandable overview; show actionable alerts and last successful state only when supported by reliable data. Do not display secrets, full payment instruments or sensitive identifiers in dashboards.
- Use stable named routes and deep links, distinguish current section in navigation, preserve back/forward and meaningful headings. On small screens, use an accessible list-to-detail navigation instead of forcing a cramped desktop sidebar.
- Treat cross-workspace/global settings explicitly. Display which account, user, team or tenant will be changed; do not silently apply a personal preference to all workspaces.
- Place destructive account actions in an intentionally separated section with descriptive consequences, not adjacent to routine profile edits.

### Profile and contact information (KG-004, KG-005, KG-006)

- Separate editable display information from verified identity claims. Label what is public, shared internally or private; indicate server-managed or locked fields and explain why they cannot be edited.
- For avatar/photo changes, provide preview, cropping alternative, accessible text, size/type validation, cancellation and a recoverable upload failure; do not assume an image is mandatory.
- Changing a verified email or phone is a **pending verification journey**, not an ordinary text-save. Distinguish requested, challenge sent, verified, expired, rejected and reverted states. Keep current verified contact available until policy-defined transfer completes.
- Data export is a separate asynchronous request with eligible scope, request time, ready/expired/failed status and a private authenticated download route. Legal and retention obligations require product-specific review; never promise instant export or universal portability.

### Settings persistence (KG-003)

| State | User-facing contract | Verification |
| --- | --- | --- |
| Pristine | Display effective server-backed value and source (account, workspace or device) | Reload and compare |
| Dirty | Mark what has changed; expose save/cancel or clearly explained autosave | Back/close with dirty input |
| Saving | Disable conflicting repeated changes only as necessary; preserve focus and inputs | Slow network and repeated action |
| Saved | Confirm persistence at the actual scope, not simply click receipt | Refresh, second device and fresh session |
| Validation failure | Put specific errors next to fields and provide summary for complex forms | Keyboard and screen reader |
| Conflict | Explain another editor/device changed the value; offer safe reload/compare/reapply when possible | Concurrent edits |
| Offline or unknown outcome | Do not imply remote save succeeded; distinguish draft and synchronized value | Offline, timeout, server retry |
| Permission revoked | Explain why change is no longer permitted without leaking other users' data | Server authorization and stale page |

Prefer an explicit save for high-consequence or multi-field forms; autosave may fit independent, reversible settings when effective state, failure and rollback are clear. Use [forms](forms.md), [offline conflicts](offline-sync-and-conflicts.md) and [interaction recovery](interaction-states-and-recovery.md) rather than creating unique controls for every setting.

## Composition example

`/settings` account overview -> `/settings/profile` editable fields -> validation -> submit -> verified persisted result. A separate `/settings/security` high-risk action first asks for server-approved step-up verification, then returns focus and navigational context. On mobile, the section list precedes the detail view; deep links still open directly with a clear back route.

**Anti-example:** a single giant tab panel mixes cancel subscription, theme toggle and email change with one global Save button; changing email appears successful before address verification, and navigating away silently discards data.

## Inclusive operation and review

- Use semantic sections, a single main landmark, descriptive headings, active navigation state and focus management when changing views. Keep touch, keyboard, zoom/reflow and 200% text-equivalent scenarios operable.
- Externalize labels, errors and date/number formats. Test long translations and RTL; do not use left/right wording to describe settings controls.
- Test unsaved-change dialogs without trapping users; safe exit must remain possible. Honor reduced motion, all supported themes, contrast and persistent focus indicators.
- Measure settings task completion, form corrections and failure recovery; do not claim adoption, task success or WCAG conformance without product tests.

## Existing canonical ownership and sources

- [Task flows and information architecture](task-flows-and-information-architecture.md): wayfinding, hierarchy, deep links.
- [Forms](forms.md): input, validation and save mechanics.
- [Authentication and account lifecycle](authentication-and-account-lifecycle.md): identity proof, factors and verification.
- [Privacy and trust](../guidance/privacy-consent-and-trust.md): audience, rights requests and deletion.
- [Role-aware workspaces](role-aware-workspaces-and-context-switching.md): tenant/member permission boundaries.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) (Recommendation; consulted 2026-11-07): applicable accessibility criteria, not product certification.
- [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) (consulted 2026-11-07): accessible navigation/widget patterns; prefer native HTML.
- [Nielsen Norman Group, Settings](https://www.nngroup.com/articles/) (general practitioner reading; applicability must be reviewed, not a normative standard).

## Evidence matrix

| Check | Status |
| --- | --- |
| Existing catalog ownership and aliases inspected | PASS (documentation review) |
| Portal navigation, persistence and concurrency tested in product | NOT VERIFIED |
| Keyboard, assistive technology, responsive/RTL, cross-device | NOT VERIFIED |
| Identity verification and data portability policy approved | NOT VERIFIED |

**Canonical ID:** `pattern.account-settings-portal` · **Drafted:** 2026-11-07.


## Workspace configuration foundation — Settings knowledge Batch 1 (proposed, 2026-11-07)

**Scope:** generalizable settings *knowledge* for applications with personal and workspace configuration. This section extends `pattern.account-settings-portal`; it does not create a new Settings component, implement a server, or grant permissions. The Little Wins F20 source-code review motivated the gap, but its product-specific feature names, values, and route contracts remain in the product repository. Re-check the catalog and target at the start of each subsequent batch.

### KG-001 — Authoritative setting registry

Define one reviewed contract per setting before exposing its control. Keep a single authoritative backend/domain owner for workspace rules, while client-side-only presentation preferences can have a separate explicit storage owner. Required fields:

| Field | Decision or acceptance question |
| --- | --- |
| `key`, `description`, `type`, `allowedValues` | Is the setting uniquely named, documented and type-validated at its authority boundary? |
| `scope`, `targetId`, `source` | Is this device, person, workspace, project or system state? Which exact target changes? |
| `default`, `effectiveValue`, `inheritance` | What happens before first save? Is a value inherited, overridden, unavailable, or locked? |
| `readCapability`, `writeCapability`, `authority` | Who may read/change the setting, and which server policy decides? |
| `storageOwner`, `schemaVersion`, `migration` | Where is the canonical value persisted, and how do old records migrate safely? |
| `validation`, `dependencies`, `impact` | Which combinations are invalid, which downstream tasks change, and what persists unchanged? |
| `saveMode`, `reversibility`, `auditClass` | Autosave or explicit save; can change be undone, and should it be logged? |
| `status`, `owner`, `evidence` | Proposed/implemented/verified, accountable reviewer, and actual test evidence. |

**Example (illustrative, not deployed):**
```yaml
key: workspace.activityReviewRequired
scope: workspace
type: boolean
default: true
source: workspace_policy
readCapability: workspace.settings.read
writeCapability: workspace.settings.manage
storageOwner: server
validation: verify_workspace_and_permission_on_every_write
dependencies: [activity_submission, review_queue]
impact: future submissions only unless an explicit migration is approved
saveMode: explicit
reversibility: requires_policy_transition_review
status: proposed
```

**Avoid:** storing permissions in browser preferences, creating one untyped `settings` object shared by all features, or treating a disabled UI control as proof of server policy.

### KG-003 — Scope, authority, and permission boundaries

1. Always show the *effective target* (e.g. current workspace) and separate personal/device preferences from workspace-wide rules. Avoid invisible scope changes across accounts or tenants.
2. Authorize **read and write independently** on the server for each request and object; a route guard, hidden tab or disabled switch is only UI guidance. Bind updates to the currently authorized target ID and reject stale/revoked access.
3. Distinguish owner-managed member profiles from independently authenticated and authorized principals. A displayed role label is not a capability grant. Do not fabricate delegation, impersonation, billing, or export features from generic settings IA.
4. For unsupported or denied updates, show a clear explanatory read-only state or no-access state without leaking restricted values. Keep the current identity/workspace legible after a failed switch.
5. Record who owns changes to each setting and who reviews security-sensitive additions. Step-up authentication, if required, is a domain/security decision and not implemented by the settings page itself.

**Acceptance scenarios:** unauthorized direct API write, cross-workspace identifier edit, old browser tab after permission revocation, user with view-only rights, and changes from multiple devices. Every unauthorized mutation must fail on the server and leave persisted values unchanged.

### KG-006 — Save, propagate, and recover

Use the existing persistence-state table above as the **canonical UI state reference**; implement the following cross-feature process without inventing a second form component:

```text
load effective setting + scope + version
-> edit local draft (no server assertion yet)
-> validate permitted type / local dependencies
-> server authorizes target and capability
-> server validates dependencies and expected version
-> commit atomically or reject without partial mutation
-> return authoritative effective value / version
-> invalidate dependent views and reconcile presentation
-> announce saved scope, or preserve draft with recovery guidance
```

- **Low-consequence, reversible personal settings:** autosave may be appropriate if failures are visible, persisted state is distinguishable from draft state, and prior value can be restored.
- **Workspace-wide, dependent or destructive settings:** default to explicit Save and a consequence summary; require confirmation only where consequences are material, not for every minor edit.
- **Conflict:** report the new server value/version and let the user safely compare, reload or reapply. Never silently overwrite other editors.
- **Timeout/unknown result:** ask the server for the operation outcome before retrying non-idempotent mutations. A local acknowledgement is not durable success.
- **Revoked permission:** keep the user's edits only when safe, explain the denial, and block further writes rather than masking failures.
- **Dependency propagation:** separately identify UI cache refresh, server command enforcement, historic record retention, and downstream calculations. Do not imply turning off a feature deletes or recalculates its history.
- **Navigation away:** warn on unresolved drafts; preserve focus and provide a safe leave/stay choice.
- **Accessibility/i18n:** associate controls with persistent labels, descriptions and validation errors; announce save status without excessive live-region updates; test keyboard, screen reader, zoom/reflow, long translations, RTL, high contrast and reduced motion.

**Acceptance matrix (documentation, not executed product tests):**

| Scenario | Expected outcome |
| --- | --- |
| Load then refresh | Effective value and scope are accurate; no phantom pending save |
| Valid edit | Persisted response is reflected across affected screens |
| Invalid value/dependency | No partial write; actionable field or rule explanation |
| Permission revoked during edit | Write denied at server; no privileged data revealed |
| Concurrent editor | Version conflict is visible and recoverable |
| Offline or ambiguous timeout | Draft retained; no false “Saved” claim |
| Leave with unsaved changes | Explicit leave/stay path and preserved context |
| Keyboard/RTL/zoom | Operable controls and visible, correctly announced errors |

### Sources, owners and verification boundary

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) — W3C Recommendation; keyboard, focus, errors, reflow and status messages (consulted 2026-11-07).
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — use native controls first; dialog/switch patterns only when appropriate (consulted 2026-11-07).
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — server-side access checks and least privilege; engineering security review required (consulted 2026-11-07).
- Existing canonical: [role-aware workspace boundaries](role-aware-workspaces-and-context-switching.md), [forms](forms.md), [offline conflicts](offline-sync-and-conflicts.md), and [interaction recovery](interaction-states-and-recovery.md).

**Knowledge state:** proposed; catalog reviewer unassigned; product-specific authorization, persistence, user-testing, accessibility/runtime behavior and security checks **NOT VERIFIED**. Revisit on a real target implementation and record the actual owner and results.

### Shared batch-PR protocol

This section is Batch 1 of a cumulative settings-knowledge PR. At the **start of each later batch**, re-fetch `main`, this PR branch, the canonical catalog registry, relevant linked concepts, and the latest available target code/decision context; log differences, existing ownership, evidence limitations and applicable standards before changing guidance. Do not overwrite unrelated changes, silently use old target assumptions, or mark proposed guidance as merged. Batch 2 concerns feature/capability dependencies and policy transitions; Batch 3 time and personalization; Batch 4 auditability; Batch 5 catalog validation and crosswalk. Subsequent changes remain reviewed separately inside the same draft PR until it is ready for approval.


## Settings knowledge Batch 2 — feature and policy configuration (proposed, 2026-11-07)

**Fresh-context check:** Compared `main` against cumulative PR #12, inspected the canonical registry and existing [task-flow capability matrix](task-flows-and-information-architecture.md#batch-8--capability-dependencies-and-configuration-state-journeys-2026-11-07), [paused-work recovery](interaction-states-and-recovery.md#batch-8--paused-capabilities-and-work-already-in-progress-2026-11-07), and current available Little Wins F20 review-policy contracts. The existing catalog **already documents** feature-flag combinations, server-command gating, retained history and paused-task recovery. This batch adds the missing *settings-specific authoring and policy-transition contract*; it does not duplicate or replace that matrix.

### KG-002 — Configuration-to-capability UX contract

A settings switch changes a **stored preference or policy**, not automatically every dependent user capability. Use the canonical [task-flow feature/capability matrix](task-flows-and-information-architecture.md#batch-8--capability-dependencies-and-configuration-state-journeys-2026-11-07) to define valid state combinations, direct-command constraints, and historical continuity.

Before rendering a workspace toggle, complete this checklist:

| Requirement | Question the setting contract must answer |
| --- | --- |
| Scope and actor | Which workspace/project changes; who may read and save? |
| Stored flag vs effective capability | Which actions actually require this flag and which *other* policies or features? |
| Dependency disclosure | Will another enabled feature become unusable? Does its stored value remain enabled but ineffective? |
| Pre-save consequences | Which new actions pause, which existing requests may finish, and what remains visible or editable? |
| Transition timing | Is the change immediate for future commands? What if a command is already in flight? |
| Navigation and recovery | Can the owner still reach outstanding requests and historical records when primary navigation is hidden? |
| Re-enable behavior | Are previous settings and history preserved; are new capabilities revalidated without retroactive award? |
| Safety evidence | Have server-side checks, all relevant flag combinations, stale-tab races and direct URL/API requests been tested? |

**Illustrative policy choice, not universal behavior:** disabling points may pause *new* reward requests that require points while preserving existing requests and ledger history; the product owner must specify whether fulfillment of previously requested rewards remains available. Do not silently change one flag when another is toggled, delete historic records, or claim that turning a feature back on automatically recreates past credits.

**Settings UI pattern:** show the effective state and a concise dependency explanation adjacent to the control; for consequential changes show a review summary identifying affected capabilities and preserved data before explicit Save. Confirm *persisted* changes and refresh affected navigation and task views. Preserve access to authorized management of outstanding work even if a primary feature is paused. If action is unsupported, distinguish "paused by configuration" from "no permission" and "no data."

**Anti-example:** "Rewards: On" is presented as immediately available while Points is off, without explaining the effective disabled capability, and the only path to existing reward requests disappears.

**Verification:** enumerate full flag-state table and each transition, authorization denial, in-flight operations, pending-work management, refresh/second session, re-enable, accessibility announcements, mobile navigation and long translated labels. Mark untested states **NOT VERIFIED**.

### KG-005 — Review/approval policy transition contract

Review policy should be modeled as an **authorized, versioned workflow policy**, not as a purely visual toggle. Before implementation the product must define its mode names, default, effective time, actor capabilities, existing pending submissions, accepted/rejected/returned history and points/entitlement effects. [Interaction recovery](interaction-states-and-recovery.md#human-review-and-value-changing-transaction-lifecycle-2026-11-07) remains canonical for submission and review *states*.

| Configuration situation | Required decision and presentation |
| --- | --- |
| Default review mode | State current effective mode; never infer an "automatic" mode from the presence of an enum |
| Eligible editor | Server authorizes workspace ownership or explicitly granted policy-change capability |
| Change to a more permissive mode | Verify recorder authorization and gate activation; identify whether only **new** submissions are affected |
| Change to approval-required mode | New submissions follow the new requirement; define handling of already accepted, pending or in-flight submissions |
| Pending requests at transition | Choose explicit grandfather, migrate, or separate administrative decision; no silent approval/rejection |
| Concurrent decisions and mode edit | Use persisted version/sequence and atomic server checks; no duplicate approvals, awards or lost reviewer input |
| Previously approved or rejected history | Preserve immutable decision and award provenance; corrections require a separate reviewed workflow |
| Paused points or feature | Approval and crediting are separate consequences; specify whether credit is withheld, delayed or amended (never assume backfill) |
| Unsupported policy capability | Explain why mode is unavailable; do not offer a selectable but nonfunctional option |
| Reversal and audit | Explain whether changing mode back affects only future work, and record high-impact policy changes appropriately |

**Illustrative transition:** `approval_required` → `trusted_recorder_acceptance` can be offered *only after* the server has an independently authenticated trusted-recorder capability and the product has decided how queued submissions are handled. An owner-managed profile label is not authentication or authorization. If the capability is unimplemented, display the current policy read-only or omit the unavailable mode rather than implying it works.

**Illustrative user-facing warning:** "Changing review policy affects future submissions. Pending reviews will remain pending under the current rules." Use such wording **only if the domain contract actually guarantees it**; otherwise specify the true transition behavior before shipping.

**Acceptance tests:** direct mutation with insufficient capability, flag gate off, stale policy version, pending submission race, approval/rejection/return transitions, duplicate processing, points-off award, policy reversal, preserved history, long text, keyboard and screen reader status. Manual/runtime outcomes remain **NOT VERIFIED**.

**Scope and sources:** Reuse [role-aware workspace authorization](role-aware-workspaces-and-context-switching.md) and [Batch 1 setting registry](#workspace-configuration-foundation--settings-knowledge-batch-1-proposed-2026-11-07). The generic requirements above draw on the catalog's canonical task/recovery guidance, [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) (reference review date 2026-11-07; external URL reachability not verified in this batch). Little Wins F20 source evidence: `server/modules/reviews/index.ts` declares modes `approval_required` and `trusted_recorder_acceptance`, and gates acceptance on a distinct capability; its README states the latter is proposed and not activated in legacy routes. `docs/little-wins/03_DECISIONS_AND_OPEN_QUESTIONS.md` still flags review atomicity (DEC-009) as open. This product snapshot is not the authoritative catalog and is not proof of deployment.

**Status:** proposed knowledge on draft PR #12; catalog owner unassigned; product policy approval, live behavior, accessibility and authorization tests **NOT VERIFIED**. Batch 3 must re-gather context before proceeding.


## Settings knowledge Batch 3 — time and personal preferences (proposed, 2026-11-07)

**Context refresh and coverage disposition:** Re-read current `main` and the cumulative branch, canonical registry, [design tokens/themes](../foundations/design-tokens-and-themes.md), [internationalization](../guidance/internationalization.md), and [accessibility](../guidance/accessibility.md). Their semantic token, mode/density, locale formatting, and reduced-motion requirements **already exist**. This addition specifies how a settings page exposes *effective preferences* and how a workspace timezone decision affects period-based tasks; it does not duplicate token implementation. In the available cleaned Little Wins F20 ZIP, `shell/context/display-preferences.ts` defines `light`/`high-contrast` and `comfortable`/`compact` with browser-local storage, while `server/modules/history/index.ts` reports periods as UTC. Its decision register `DEC-010` still leaves timezone and activity-versus-award date semantics open. No live user behavior, deployments, or changed target implementation are verified.

### KG-004 — Reporting timezone and calendar-period configuration

**Use when** a configurable timezone changes which business dates or reporting periods contain a record. **Avoid** assuming that changing how a date is *displayed* authorizes rewriting timestamps or reassigning historical awards.

A timezone setting must not be editable until the following domain decisions have an accountable owner:

| Decision | Required contract |
| --- | --- |
| Authority and scope | Is the reporting timezone fixed by deployment, workspace, project, or user? Who may edit it? |
| Identifier and default | Specify an explicit valid IANA timezone identifier, default, and fallback; avoid fixed UTC offsets for DST-sensitive civil periods. |
| Date types | Distinguish activity occurrence date, submission date, review/award instant, redemption/request instant, and correction date. |
| Period definition | Define calendar boundary inclusivity, start/end instants, month/week numbering, locale calendar assumptions and DST behavior. |
| Historical semantics | Decide whether a timezone change re-buckets past records for reports, affects only future periods, or requires a versioned migration. Never silently alter underlying event timestamps. |
| In-flight and concurrent edits | Define effective version/time, report cache invalidation, stale editors and permission handling. |
| Display vs computation | Format a time using locale for readability, but compute authoritative period boundaries with the selected workspace policy, not the device's implicit timezone. |
| Rollout compatibility | Identify API/contract versioning, legacy UTC queries, migrations and rollback before enabling a selectable control. |

**Example (illustrative):** A stored UTC instant shortly after midnight UTC may belong to the prior local calendar day in `America/New_York`. A monthly report must consistently apply the selected timezone to its period boundaries; merely relabeling the UTC result with a local date would be misleading. The decision about **which event timestamp** determines the period remains product-owned.

**Default when unresolved:** show current reporting basis explicitly as read-only (for example, “Reports currently use UTC”), link an explanation if supported, and do not expose a functional-looking timezone selector. There is no evidence that Little Wins F20 implements configurable reporting timezones.

**Verification cases:** UTC day/month rollover; spring-forward missing local hour and fall-back repeated hour; timestamps around period boundaries; date-only activity input; locale date display different from period computation; stale cached report after authorized change; historical export; unauthorized edit; concurrent edit; invalid timezone and tzdb update. Tests must compare authoritative aggregation outputs, not only formatted labels.

### KG-008 — Preference scope, effective mode and safe fallback

Use [design tokens and themes](../foundations/design-tokens-and-themes.md#appearance-preferences-as-a-product-journey--account-batch-3-kg-016017) as canonical ownership for semantic themes, modes, density and contrast; [accessibility](../guidance/accessibility.md) owns platform-level accessibility requirements. The settings page owns *the user journey and scope disclosure*, not an independent theme engine.

| Preference decision | Settings experience requirement |
| --- | --- |
| Scope | Label browser/device versus signed-in account or workspace sync, with explicit persistence claims only where implemented. |
| Available options | Show only supported modes and density values; a hypothetical “system”, “dark” or language mode is not a functioning setting. |
| Effective value | Explain default, manual override, system influence when supported, and storage-blocked fallback. |
| Preview and save | Apply reversible visual preferences immediately when safe; distinguish session-only changes from durable persistence and offer a clear reset. |
| Reconciliation | On hydration or account switch, avoid false synced-state claims, unwanted theme flashes, and cross-workspace overrides. |
| Accessibility | All supported themes require usable focus, status/error/disabled states, reflow and zoom; user toggles cannot be prerequisites for accessible operation. |
| Localized content | Language selection (if actually supported) must update document language and translated UI, independent of calendar timezone; long labels, RTL and mixed-direction input need tests. |

**Illustrative reuse:** a Settings appearance panel consumes an existing display-preference provider to set `theme` and `density`; it does not persist them again as workspace business settings or create a second provider. A local-storage write failure may leave an effective session preference, but must not be presented as a guaranteed saved account preference.

**Avoid:** conflating timezone, locale and theme into a single “region” selector; exposing nonexistent dark/system modes; persisting business authority to browser storage; or using “high contrast” as a substitute for accessible default styling.

**Acceptance cases:** reload with valid/invalid stored value, disabled storage, hydration first paint, preference reset, second device expectations, light/high-contrast focus and errors, compact density at touch/zoom, browser reduced-motion override, untranslated text and mixed RTL strings. Record actual run results separately from the proposed checks.

### Batch 3 evidence and unresolved decisions

- **Reusable sources:** [IANA Time Zone Database](https://www.iana.org/time-zones) (tzdb, consulted 2026-11-07; political/DST revisions occur), [MDN `Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat) (locale-aware display and explicit `timeZone`, consulted 2026-11-07), [W3C Internationalization](https://www.w3.org/International/quicktips/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/).
- **Little Wins source snapshot:** cleaned F20 archive provided by the user; direct inspection of `docs/little-wins/03_DECISIONS_AND_OPEN_QUESTIONS.md`, `shell/context/display-preferences.ts`, `shell/context/display-preferences-provider.tsx`, and `server/modules/history/index.ts`. Source inspection supports only those observed claims, not deployed behavior.
- **Open product decision:** `DEC-010` is unresolved. Do not infer the workspace timezone or choose activity versus award date semantics on behalf of the product owner.
- **Status:** proposed catalog guidance; owner/review assignment outstanding; catalog validator, runtime timezone correctness, browser preference behavior, accessibility and internationalization tests **NOT VERIFIED**. Next batch must re-collect current context before modifying guidance.


## Settings knowledge Batch 4 — configuration governance and audit (proposed, 2026-11-07)

**Fresh-context and reuse check:** At the start of Batch 4, compared current `main` and PR #12 branch, inspected `catalog/index.json`, this portal, [role-aware audit visibility](role-aware-workspaces-and-context-switching.md#batch-10-extension--enterprise-approvals-delegation-and-audit-visibility), [privacy/retention](../guidance/privacy-consent-and-trust.md), [interaction recovery](interaction-states-and-recovery.md), and [governance decisions](../governance/lifecycle-and-decisions.md). Existing pages already own permission-aware audit viewing, data lifecycle, and general recovery. This extension owns only the **workspace settings change-event contract and its management journey**. Do not equate catalog decision/changelog records with runtime administrative audit events.

### KG-007 — Configuration-change history contract

**Use when:** a setting changes who can act, which workflows execute, how reports are grouped, how data is retained, or other consequential workspace behavior. **Avoid:** logging every ephemeral personal theme selection as an administrative change or promising a tamper-proof audit trail without backend guarantees.

Before implementation, assign the product/security owners and determine which changes warrant an audit event. Use the existing Batch 1 `auditClass` registry field to document whether each setting is `none`, `operational` or `sensitive` (illustrative classification names, not a mandated schema).

| Event field / behavior | Minimum contract |
| --- | --- |
| Event identity | Durable event ID, event type, operation/request ID, schema version and correlation to the accepted mutation |
| Actor and authority | Authenticated actor ID, validated role/capability, and delegated actor versus subject when applicable; do not treat UI role labels as evidence |
| Target and scope | Setting key, effective workspace/tenant ID, scope, affected configuration version and policy mode |
| Time and ordering | Server-generated UTC instant and stable ordering/revision; format display in the viewer's locale with explicit timezone |
| Before and after | Safe old/new **effective** values or redacted summaries; for secrets/tokens record presence/rotation, never the raw secret |
| Outcome | Authorized attempted vs committed vs rejected/failed; distinguish security telemetry from the history of **successful configuration changes** |
| Reason and approval | Required business reason or approver only where the product policy mandates it; do not fabricate universal justification or approval workflows |
| Integrity and retention | Write path, access controls, retention schedule, archival/redaction/deletion exceptions and operational monitoring owned by engineering/compliance |

**Atomicity:** for high-impact settings, define how the committed configuration and corresponding event are durably associated. A UI success message is not an audit event. On partial failure, the authoritative mutation outcome must be independently recoverable; do not claim perfect event completeness unless the actual persistence architecture supports it. Never silently remove prior events when a setting is later changed again.

### Authorized audit viewing and correction UX

- Show an **administrative settings activity** view only to authorized roles, scoped to the current workspace; independently authorize both event queries and export/download if implemented. Omit or redact fields the viewer is not entitled to see.
- Display the **setting, actor (where permitted), effective timestamp, scope, change summary and outcome**; separate proposed/draft values from confirmed persisted changes. Use accessible semantic tables or timelines with labels and readable empty/filter/error states.
- For conflicting updates, link the event or configuration revision to the safe [Batch 1 save recovery](#workspace-configuration-foundation--settings-knowledge-batch-1-proposed-2026-11-07) flow. A log entry explains what changed but does not itself restore access or guarantee undo.
- **Revert policy:** decide separately whether the *setting* can be restored and whether downstream effects can be reversed. Reverting `reviewRequired` may change future submissions without undoing prior approvals or points transactions. When reversal is unsafe, provide an authorized compensating workflow and explain the consequences rather than a misleading one-click “Undo.”
- **Retention and privacy:** choose a justified retention schedule and disclosure policy with product/security/legal owners; consider minors, member identities, sensitive values, access revocations, account/group deletion, and exports. Do not hardcode a universal retention duration or claim immutable retention that conflicts with legitimate deletion processes.
- **Presentation and localization:** use explicit timestamps and timezone, translated actor/action labels and error text, long-name reflow, keyboard-accessible filters and focus, readable contrast and status announcements. Audit history must remain usable without relying on colors or icons alone.

**Example (illustrative, no production schema):**

```json
{
  "eventId": "evt-example",
  "kind": "workspace.settings.changed",
  "workspaceId": "workspace-example",
  "actorId": "authenticated-actor",
  "settingKey": "workspace.reviewRequired",
  "previousSummary": "approval required",
  "newSummary": "trusted mode (capability gated)",
  "revision": 17,
  "recordedAtUtc": "2026-11-07T16:00:00Z",
  "outcome": "committed"
}
```

The event illustrates audit semantics only. The specific setting and trusted mode are **not** evidence of an implemented Little Wins configuration capability.

**Anti-examples:** a settings switch saves but the only audit trace is a client console message; a “Revert” button promises to erase awards granted while a permissive review policy was active; a settings export exposes secret values or unrelated workspaces.

### Verification and accountable decisions

| Scenario | Required evidence |
| --- | --- |
| Authorized committed change | One correctly scoped, queryable change event linked to the persisted revision |
| Unauthorized or rejected write | No false committed event; separate security logging only if required |
| Concurrent/stale update | Accurate winner revision and no misleading or duplicate committed changes |
| Event-write/store outage | Documented durable handling and truthful recovery, no fabricated audit completion |
| Cross-workspace access | Server denies event read, mutation and export across unauthorized boundaries |
| Sensitive value change | Redaction works in stored event, API, UI, export and telemetry |
| Revert after downstream transaction | Setting change does not silently rewrite historic ledger or reviewer outcomes |
| Retention/erasure request | Product-specific lawful policy is applied without unsupported automatic promises |
| Keyboard, screen reader, RTL, long labels | Usable and localized history filters, timestamps, detail and error states |

**Sources and boundaries:** This knowledge reuses [role-aware audit and delegation](role-aware-workspaces-and-context-switching.md), [privacy/data lifecycle](../guidance/privacy-consent-and-trust.md), [interaction recovery](interaction-states-and-recovery.md), [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html), [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), and [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) (reference review: 2026-11-07; link reachability not independently verified).

**Little Wins F20 evidence boundary:** the inspected product snapshot provides contribution/review/reward history and owner-managed configuration; it is **not proof of an implemented configuration-change event stream, viewer, export, retention policy or undo function**. No event schema, retention duration or audit-authorized role is approved by this guidance.

**Status:** proposed catalog guidance; product/security/legal ownership and implementation choices pending. Source/catalog review completed; validator, security tests, browser/a11y checks, event integrity and actual retention enforcement **NOT VERIFIED**. Batch 5 must gather fresh context, run catalog-wide validation where available, and record the remaining product-specific decisions.
