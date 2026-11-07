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

**Scope:** generalizable settings *knowledge* for applications with personal and workspace configuration. This section extends \`pattern.account-settings-portal\`; it does not create a new Settings component, implement a server, or grant permissions. The Little Wins F20 source-code review motivated the gap, but its product-specific feature names, values, and route contracts remain in the product repository. Re-check the catalog and target at the start of each subsequent batch.

### KG-001 — Authoritative setting registry

Define one reviewed contract per setting before exposing its control. Keep a single authoritative backend/domain owner for workspace rules, while client-side-only presentation preferences can have a separate explicit storage owner. Required fields:

| Field | Decision or acceptance question |
| --- | --- |
| \`key\`, \`description\`, \`type\`, \`allowedValues\` | Is the setting uniquely named, documented and type-validated at its authority boundary? |
| \`scope\`, \`targetId\`, \`source\` | Is this device, person, workspace, project or system state? Which exact target changes? |
| \`default\`, \`effectiveValue\`, \`inheritance\` | What happens before first save? Is a value inherited, overridden, unavailable, or locked? |
| \`readCapability\`, \`writeCapability\`, \`authority\` | Who may read/change the setting, and which server policy decides? |
| \`storageOwner\`, \`schemaVersion\`, \`migration\` | Where is the canonical value persisted, and how do old records migrate safely? |
| \`validation\`, \`dependencies\`, \`impact\` | Which combinations are invalid, which downstream tasks change, and what persists unchanged? |
| \`saveMode\`, \`reversibility\`, \`auditClass\` | Autosave or explicit save; can change be undone, and should it be logged? |
| \`status\`, \`owner\`, \`evidence\` | Proposed/implemented/verified, accountable reviewer, and actual test evidence. |

**Example (illustrative, not deployed):**
\`\`\`yaml
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
\`\`\`

**Avoid:** storing permissions in browser preferences, creating one untyped \`settings\` object shared by all features, or treating a disabled UI control as proof of server policy.

### KG-003 — Scope, authority, and permission boundaries

1. Always show the *effective target* (e.g. current workspace) and separate personal/device preferences from workspace-wide rules. Avoid invisible scope changes across accounts or tenants.
2. Authorize **read and write independently** on the server for each request and object; a route guard, hidden tab or disabled switch is only UI guidance. Bind updates to the currently authorized target ID and reject stale/revoked access.
3. Distinguish owner-managed member profiles from independently authenticated and authorized principals. A displayed role label is not a capability grant. Do not fabricate delegation, impersonation, billing, or export features from generic settings IA.
4. For unsupported or denied updates, show a clear explanatory read-only state or no-access state without leaking restricted values. Keep the current identity/workspace legible after a failed switch.
5. Record who owns changes to each setting and who reviews security-sensitive additions. Step-up authentication, if required, is a domain/security decision and not implemented by the settings page itself.

**Acceptance scenarios:** unauthorized direct API write, cross-workspace identifier edit, old browser tab after permission revocation, user with view-only rights, and changes from multiple devices. Every unauthorized mutation must fail on the server and leave persisted values unchanged.

### KG-006 — Save, propagate, and recover

Use the existing persistence-state table above as the **canonical UI state reference**; implement the following cross-feature process without inventing a second form component:

\`\`\`text
load effective setting + scope + version
-> edit local draft (no server assertion yet)
-> validate permitted type / local dependencies
-> server authorizes target and capability
-> server validates dependencies and expected version
-> commit atomically or reject without partial mutation
-> return authoritative effective value / version
-> invalidate dependent views and reconcile presentation
-> announce saved scope, or preserve draft with recovery guidance
\`\`\`

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

This section is Batch 1 of a cumulative settings-knowledge PR. At the **start of each later batch**, re-fetch \`main\`, this PR branch, the canonical catalog registry, relevant linked concepts, and the latest available target code/decision context; log differences, existing ownership, evidence limitations and applicable standards before changing guidance. Do not overwrite unrelated changes, silently use old target assumptions, or mark proposed guidance as merged. Batch 2 concerns feature/capability dependencies and policy transitions; Batch 3 time and personalization; Batch 4 auditability; Batch 5 catalog validation and crosswalk. Subsequent changes remain reviewed separately inside the same draft PR until it is ready for approval.
