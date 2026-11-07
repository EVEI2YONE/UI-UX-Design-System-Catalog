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
