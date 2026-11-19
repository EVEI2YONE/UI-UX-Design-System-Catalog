# Role-aware workspaces and context switching

**ID:** `pattern.role-aware-workspaces` · **Kind:** guideline · **Status:** proposed · **Primary layer:** experiences  
**Owner:** Design-system/catalog maintainers (review assignment pending) · **Reviewed:** 2026-11-07

## Purpose and scope

Provide predictable entry points, navigation and safe context changes for people who have one or more authorized roles (customer, administrator, support agent, partner), possibly across organizations/tenants. This is a reusable UX pattern, **not** a shipped switcher or an authorization implementation. Adapt labels and role taxonomy to product user research.

**Use when** roles materially change tasks, navigation, available data or authority. **Avoid** presenting a role switcher to single-role users, offering inaccessible role choices, conflating organization switching with role switching, or inventing a universal role hierarchy.

## Distinguish four different experiences

| Experience | Identity and authority | UX contract |
| --- | --- | --- |
| Role/workspace selection | Same person; selects an **authorized** active role or workspace | Show current role/context, only eligible destinations, understandable transition and return |
| Organization/tenant selection | Same person, different authorized data boundary | Name organization prominently; re-evaluate permissions and data scope on every transition |
| Customer-perspective preview | Authorized administrator sees an approximation of customer UI, typically without customer-specific secrets or mutations | Persistent `Preview mode` banner; explain scope/limitations; make exit clear; prevent misleading active controls |
| Customer impersonation/delegated access | Privileged, separately approved access to a specific customer's context | Explicit target identity, reason/consent policy, time limit, auditable start/end, distinguish actor from subject; never silently inherit superuser powers |

A visual preview is **not** evidence that the customer has the same permissions, entitlements, data, locale, feature flags or experience. Label mock/synthetic preview data; do not claim a read-only rendering is safe unless server-side data and mutation boundaries enforce it.

## Decision flow and routing contract

```text
Sign in -> load authenticated identity and server-authorized memberships/roles
  -> no eligible workspace: clear no-access / request-access path
  -> one eligible workspace: go directly to its appropriate landing page
  -> multiple: preferred eligible workspace OR explicit chooser (product decision)
  -> show persistent, legible current workspace/role/organization
  -> user selects another eligible context
      -> validate authorization and unsaved-work state
      -> apply context server-side / obtain context-bound session as required
      -> clear stale privileged or tenant-scoped data/caches
      -> navigate to valid destination; announce updated context
      -> error: preserve or restore safe prior context and explain recovery
```

A remembered preference is only a navigation preference, never proof of authorization. Deep links must re-check access; a forbidden deep link gets a clear 403/no-permission experience, not data leakage or a misleading empty state. Account, role or tenant revocation must invalidate stale context. Return navigation and browser history must not accidentally re-expose a previous tenant's privileged content.

## UI composition and guidance

- **Placement:** current role/workspace visible in global header or account control; organization scope named wherever confusion is possible. Provide a discoverable `Switch workspace` or `View customer experience` command only to eligible users.
- **Active-context signifier:** text first (`Admin · Acme`, `Customer preview`); color and icon can reinforce, never solely encode authority. Keep the preview/impersonation banner persistent on narrow screens.
- **Navigation:** different roles may legitimately have different menus, homepage priorities, actions and information architecture; reuse underlying accessible components, tokens and terminology. Avoid duplicating whole applications when composition can vary by role.
- **Switcher:** use a native select or simple dialog when suitable; if using a custom menu button, follow WAI-ARIA APG menu-button keyboard/focus guidance. Show current selection, organization distinctions, pending transition, failure, empty/disabled states and access-request route.
- **Transitions:** warn about unsaved changes; do not silently discard forms; indicate loading; on success move focus to the new page heading or another meaningful landmark and provide an accessible status; preserve safe back/exit paths.
- **Preview:** distinguish `Preview as a generic customer` from `View a specific customer's account`; do not place impersonation behind an innocuous `View as customer` label. For preview, disable or replace destructive actions with explicit explanation, not merely non-interactive decorative controls.
- **Impersonation:** require product/security authorization, audit and clear `Return to admin` control. Show **who is acting** and **whose data is being viewed**; avoid accidental outbound customer communication, export or mutation. Sensitive operations may be entirely forbidden or require separate confirmation.

## States and sample scenarios

| Scenario | Visible behavior | Security/UX acceptance |
| --- | --- | --- |
| Customer-only | Customer landing page; no admin switcher | Admin API/route denied server-side |
| Admin-only with preview | Admin landing page; explicit customer preview action | Preview banner, explain fidelity, no privileged mutation |
| Multiple real memberships | Eligible workspace chooser and persistent selected context | Selection authorized at transition and per request |
| Role removed during session | Explain access loss and route to another eligible workspace/login | Cached data cleared; unauthorized calls rejected |
| Switch fails/offline | Explain retry or safe return, preserve unsaved work | No half-switched state or mixed tenant data |
| Direct old-context URL | Valid redirect or access-denied state | No privileged data via URL edits, browser history or stale cache |
| Impersonation (only if separately approved) | Time-bound banner, target + actor, exit action | Audit trail, least privilege, authorization on every request |

## Accessibility, inclusion, locale, and visual requirements

- WCAG 2.2 AA is an applicable **target**, not a claim of passing. Test keyboard-only use, visible focus, focus restoration after chooser close, screen reader announcement of active context, contrast, 200% zoom/reflow, touch targets and reduced motion.
- Prefer semantic button/link/select/dialog. For a true menu widget, document Escape, Enter/Space, arrow keys and focus placement according to WAI-ARIA APG. Do not apply `role=menu` to a plain list of links without implementing its keyboard model.
- Localize role names, workspace labels, no-permission content, warnings and announcements. Handle long organization names, translated strings, RTL and direction-aware affordances.
- Use semantic design tokens; verify light/dark/high-contrast. Never rely only on a badge color to distinguish production, admin or impersonation context.
- On mobile, keep active context and escape/return controls visible and reachable. Avoid making a critical exit available only from a hidden desktop hover menu.

## Reference examples and anti-patterns

**Example:** An admin signs in to the admin dashboard, chooses `Preview customer portal`, sees a clearly persistent `Customer preview (sample data) — Return to admin` banner, and cannot invoke customer mutations. Returning restores admin navigation.  
**Example:** A person who belongs to two organizations chooses an organization in a header selector; the app updates scoped routes and data after fresh authorization.  
**Anti-pattern:** An admin taps `Customer view` and silently assumes a real customer's identity, with no visible banner or audit.  
**Anti-pattern:** Hiding an admin sidebar while APIs still accept administrator actions from forged requests.

## Verification / measurement

- **UX task checks:** accurate landing-page selection, understanding of current role and scope, time/error to reach another authorized workspace, successful return to admin, recovery after denied/expired context. Measure per role and device with actual baselines; do not invent metrics.
- **Security checks (engineering-owned):** deny-by-default and least privilege; server-side object/tenant/role authorization on **every request**; role revocation; direct/deep-link denial; prevention of cross-tenant cache leakage; impersonation audit/start/end; preview mutation restrictions.
- **Regression checks:** keyboard and screen reader, 200% zoom/reflow, mobile, long labels, RTL, high contrast, unsaved changes, offline and concurrent tabs. Record results as PASS/FAIL/NOT VERIFIED, never assume conformance.
- **Rollout:** gate sensitive impersonation separately, feature flag routing changes where practical, retain a reversible path and monitor permission-denied errors, switching abandonment and cross-workspace complaints.

## Tradeoffs and open questions

Do users truly need one shared login and distinct workspaces, or only a role-sensitive sidebar? Do multiple simultaneous roles exist? Which organization boundary applies? Is `customer view` synthetic preview, the admin's own customer account, or delegated access to a specific customer? Which features and actions remain available in preview? These are product-specific decisions, not universal defaults.

## Source ledger (reviewed 2026-11-07)

- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — least privilege, deny by default, per-request authorization; **security guidance**, not a UX validation study.
- [W3C WAI-ARIA APG Menu Button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/) — semantics and keyboard behavior **only if** a custom menu-button pattern is chosen.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) — accessibility criteria; product testing still required.
- [AWS IAM Console Switch Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html) — **illustrative product precedent**, not a universal role/permission model. Shows explicit active role display and switch-back, with role privileges not cumulative.
- [W3C Internationalization Quick Tips](https://www.w3.org/International/quicktips/) — adaptable text/direction guidance.

**Status:** proposed catalog guidance only. No target app, component implementation, security penetration test, or user research was executed.

## Batch 10 extension — enterprise approvals, delegation and audit visibility

Role/workspace *selection* remains the core contract above. Enterprise teams additionally need explicit task state, authorized handoffs and understandable permission boundaries. These are **feature-level workflows**, not reasons to change the authorization model in the UI.

### Approval and delegation state matrix

| State | Show the user | Safety/recovery |
| --- | --- | --- |
| Draft | Owner, destination/approver and material consequences | Edit/cancel; don't imply submission |
| Submitted / pending | Request ID (if real), step/status, next actor or group where disclosure is allowed | Preserve read-only history and correction path |
| Requires changes | Clear reason with safe editable fields | Return to author without losing permitted work |
| Approved | Decision, effective time and any separate execution step | Don't assume approval executed the requested mutation |
| Rejected or withdrawn | Honest status, allowed follow-up, who can act next | Do not expose confidential notes to unauthorized roles |
| Expired / delegated | Expiry, delegated scope, reason and responsible authorized actor | Fresh authorization and safe reassignment |
| Partial execution / conflict | Which actions actually completed, failed or await review | Check backend outcome before retrying |

- **Separation of duties:** where policy requires, ensure requesters cannot approve their own actions. Server-side policy must decide eligibility on *every* transition; hiding an Approve button is not enforcement.
- **Delegation:** label actor vs represented person/organization, effective scope, expiry and revocation. Treat delegated approval and impersonation as different modes; log materially consequential actions.
- **Audit trail:** show trustworthy status history, timestamps/time zones and decision reasons only to authorized viewers. Avoid promising immutable logs or universal access unless backend implements them. Provide a meaningful accessible timeline or table.
- **Permission-change recovery:** if a role, tenant or approval scope changes mid-task, explain what remains actionable and preserve permissible drafts without leaking prior tenant data.
- **Dense operations:** connect selection and bulk approval to [advanced interactions](advanced-interactions-and-reversible-actions.md) and [data tables](data-tables.md). Show item counts/scope, eligibility failures, partial success and bounded undo promises.
- **Multi-actor handoff:** communicate whether notifications are merely delivered vs task truly assigned or acted upon. [Notifications](notifications-and-attention.md) owns channel/attention choices.
- **Accessibility and locale:** verify keyboard roles, headings, error focus, long team names, translated status words, RTL, and clear date/time zone formatting. A status color alone is insufficient.

**Illustrative good:** An employee requests access to a project, sees “Pending approval” and a status page, and can withdraw the request until the product-authorized cutoff; approver sees a scoped decision with audit history.

**Anti-example:** A manager opens another tenant in a stale tab, approves requests hidden behind a client-only role check, and sees “Approved” before the server confirms.

**Verification:** test multiple authorized roles, simultaneous reassignment, revocation, approval vs execution distinction, direct/deep links, denied actions, audit visibility, partial batch completion, narrow/RTL and screen-reader state announcements. No tested workflow or security proof is claimed.

References: [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (server-side access control); [WCAG 2.2](https://www.w3.org/TR/WCAG22/) (web accessibility criteria); [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) only when a matching custom widget is used.


## Managed profiles versus authenticated collaborators (Little Wins learning, 2026-11-07)

**Observed context:** Little Wins documents owner-managed participant profiles within a Sites-authenticated, owner-scoped D1 workspace; profile roles are descriptive and are explicitly **not** independent login identities or security permissions. Do not invent a missing sign-in requirement without asking whether owner-operation is the intended product scope.

**Decision:** inventory actor (authenticated account), represented subject (managed profile), active group/project, membership record, permission and action scope separately. A profile label does not grant reviewer rights. If collaboration is introduced, provision a verified identity-to-membership mapping, explicit invitations/acceptance/revocation, deny-by-default server checks, and safe no-access/removed-member states. Never infer cross-owner sharing from the UI alone.

**Example:** an owner can submit on behalf of a managed participant while the audit record identifies the owner as actor and participant as subject. **Anti-example:** a reviewer dropdown or profile ID is treated as permission to approve another person's submission.

**Acceptance (implementation NOT VERIFIED):** own versus other workspace, group and project ID tampering; revoked/expired membership; member-versus-reviewer actions; session change during an approval; actor/subject audit labeling; keyboard and localized no-access feedback.


## Account-level access and sensitive settings actions — batch 2 (KG-023)

**Owner:** server authorization rules remain with the product, not with a settings component. For each settings operation distinguish **actor**, **subject**, **account/workspace scope**, **permission**, **assurance needed**, **audit visibility** and **effective result**.

- Show the subject and affected scope before any transfer, membership change, administrative override or audit-sensitive action. Denied UI is not proof that an API is protected.
- For high-risk changes, use server-approved step-up and explicit confirmation; preserve task context, handle expired reauthentication, and explain the result without revealing unauthorized account details.
- Separate read access, edit rights, approval and execution. A billing admin may view invoices without necessarily being allowed to delete an account; do not derive permission from navigation visibility.
- Stale deep links, changed membership, two-tab edits and revoked privileges need safe denied/conflict states and no sensitive content leakage.
- **Tests NOT VERIFIED:** direct endpoint calls without UI, cross-account ID tampering, revoked session, role changes mid-submit, multi-workspace context, accessible denied state and audit actor/subject trail.

**Reference:** [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) (maintained security guidance; consulted 2026-11-07); [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/). See [account portal composition](account-and-settings-portal.md).
