# Authentication and account lifecycle

**Kind:** guideline · **Status:** proposed · **Primary layer:** experiences

## Purpose and boundary

Define comprehensible account entry, enrollment, authentication, factor enrollment, reauthentication, session expiry, account recovery and sign-out. **Use when** an experience verifies a person's identity or manages access to an existing account. **Avoid when** treating the UI as the authority for authentication strength or using a shared control to enforce server security policy.

Identity/security owners define authentication assurance, session timeouts, permitted authenticators and recovery controls. [Role-aware workspaces](role-aware-workspaces-and-context-switching.md) owns selection among already authorized roles and tenants, not identity proofing or authentication.

## Journey contract

| State | User-facing expectation | Test case |
| --- | --- | --- |
| Sign up | Show only necessary inputs, purpose and next step; differentiate registration from identity proofing | Input, validation, confirmation, alternate routes |
| Sign in | Identify supported methods; permit password-manager and paste mechanisms when applicable; provide accessible errors | Password manager, keyboard, assistive technology |
| Passkey | Use supported browser/OS flows and explain device or authenticator choices without mimicking secure prompts | Supported browser/device, unavailable credential, canceled ceremony |
| Step-up / MFA | Explain what additional verification is needed and why; keep context after successful return | High-risk action, lost factor, expiry |
| Session expires | Explain interruption and reauthentication; restore a **safe** destination and draft only if truly retained | Timer, unsaved work, old tabs and access revocation |
| Account recovery | Reveal an authorized recovery/fallback path without bypassing identity assurance | Lost device or recovery method, account enumeration |
| Sign out | Confirm session end and clear sensitive local context according to security policy | Browser back, shared-device, second tab |
| Account closure | Explain access/data effects, exceptions, cancellation and actual completion state | Distinguish sign-out, deactivate and delete account |

## Decision rules and tradeoffs

1. Apply product-specific authentication risk and NIST/OWASP recommendations with security owners; do **not** introduce arbitrary password, OTP or timeout numbers in generic UI patterns.
2. Favor standards-based native passkey/WebAuthn experiences where supported. Explain supported choices without faking OS authentication dialogs or promising that passkeys work on every device.
3. Support accessible authentication under WCAG 2.2 SC 3.3.8. Do not prevent credential manager autofill or copy/paste unless an independently conforming alternative applies. Review *every* required factor and recovery step.
4. Public error messages should help a legitimate user recover while avoiding unnecessary exposure of another user's account existence or private data. Exact security wording requires review.
5. Before redirect or sign-in expiry, preserve safe return context, authorization checks and draft status. Never promise unsaved data was restored if storage and backend do not support it.
6. Account recovery should not silently weaken assurance. Provide support contact only if there is a real authorized recovery mechanism.
7. Distinguish sign-out, remove a passkey, switch workspace and delete account; each has different consequences and must have distinct labels.
8. After factor/role revocation, re-evaluate authorization server-side and prevent stale sensitive content from rendering through browser history or caches.

## Illustrative example and anti-example

**Example:** A user starts a lengthy application; their session expires. The interface explains the timeout, shows a sign-in route and preserves a draft **only if** a confirmed safe draft exists. After reauthentication, the user returns to an authorized place in the flow.

**Anti-example:** “Password reset complete” is shown immediately after clicking an email link while the request is still pending, or a lost second factor creates a permanent loop with no legitimate recovery option.

## Accessibility, localization and verification

- Test keyboard focus after redirects and modal close; label instructions and errors programmatically, and do not require visual puzzle-only challenges.
- Support translations, long messages, mixed-direction account identifiers, reflow and reduced motion.
- Ensure security-sensitive changes have discoverable persistent confirmation; a transient toast alone is not sufficient.
- Include actual supported browsers, passkey/device ecosystem, fallback and session states in the test matrix.

| Test | Status | Evidence |
| --- | --- | --- |
| Sign-up/sign-in/passkey and MFA fallbacks | NOT VERIFIED | Supported device, factor and browser test matrix |
| Account recovery and no-enumeration policy | NOT VERIFIED | Security engineering review, failure simulations |
| Session expiry/reauth/draft preservation | NOT VERIFIED | Integrated authentication and persistence tests |
| Keyboard/assistive technology/locale/RTL | NOT VERIFIED | Manual product task tests |
| Session revocation, cross-role authorization | NOT VERIFIED | Backend security tests |

## Sources and limits

- [NIST SP 800-63B-4](https://csrc.nist.gov/pubs/sp/800/63/b/4/final) (final July 2025, NIST; consulted 2026-11-07): U.S. federal digital identity assurance guidance; not a universal mandatory standard for all products.
- [W3C WCAG 2.2, Accessible Authentication Minimum](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) (Level AA explainer; consulted 2026-11-07): describes accessible login requirements; live conformance still requires testing.
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) (maintained security guidance; consulted 2026-11-07): implementation guardrails rather than proof of usability.
- [FIDO Passkeys](https://fidoalliance.org/passkeys/) (consulted 2026-11-07): conceptual platform reference; recheck device/browser capability.

**Canonical ID:** `pattern.authentication-lifecycle` · **Owner:** unassigned · **Reviewed:** null · **Drafted:** 2026-11-07.

Related: [role-aware workspaces](role-aware-workspaces-and-context-switching.md), [forms](forms.md), [interaction recovery](interaction-states-and-recovery.md), [privacy](../guidance/privacy-consent-and-trust.md), [offline and sync](offline-sync-and-conflicts.md).


## Hosted-platform identity boundary — Little Wins evidence-led extension (2026-11-07)

**Context before guidance:** The Little Wins source README describes a Sites-native private owner-operated pilot; `app/api/workspace/route.ts` derives workspace ownership from `oai-authenticated-user-id`, scopes D1 queries by that owner, and supplies a development-only preview identity. The README warns that its raw Worker must not be exposed outside trusted Sites authentication. This is **source-observed configuration**, not an independently tested guarantee about every deployment.

**Decision rule:** Inventory the hosting platform and its existing authentication before recommending sign-up, passwords, MFA, or a second identity system. Separate: (1) identity proof by the hosting platform, (2) trustworthy delivery of identity to the backend, (3) app-specific membership and roles, and (4) server-authorized operations. Do not treat a user-provided header, cookie, route, or UI role label as authorization; verify trusted proxy/header stripping, direct-origin reachability, session revocation and owner isolation with the actual deployment owner.

**When to use:** hosted apps, delegated identity, managed workspaces, embedded/portal apps. **Avoid:** assuming a platform identity proves access to every group or that a member profile is an independently authenticated person.

**Example:** retain existing managed sign-in, bind a verified subject to an internal workspace membership, authorize each protected action against the membership, and show an intelligible access-denied state.

**Anti-example:** recommend a new login UI solely because the app has owner-managed member profiles, or claim the identity header is secure without testing whether clients can spoof it at the deployed boundary.

**Verification (NOT VERIFIED for Little Wins):** authenticated/unauthenticated direct API requests; forged identity header through every reachable endpoint; cross-owner workspace IDs; revoked membership; session expiry; private-site audience policy; development-identity isolation; no sensitive cache/history leakage. Report deploy-specific findings separately from reusable design guidance.


## Account security settings journey — account/settings batch 2 (KG-007–010)

**Scope:** extends existing sign-in/recovery guidance to **authenticated account maintenance**, not a new authentication component. Identity and security owners must confirm available actions and policies; no credential factor, session or API is assumed to exist.

| User task | States and controls | Required recovery / evidence |
| --- | --- | --- |
| Change password or credentials (KG-007) | Method available/unavailable, step-up required, current value verification when policy requires, processing, success, denial | Preserve account recovery, password-manager compatibility and error privacy; never echo secrets or claim change before server confirmation |
| Add, replace or remove MFA/passkey (KG-008) | Eligible, enrollment pending, platform prompt, challenge verified, backup/recovery method offered, factor active, factor revocation | Do not strand users with no authorized factor; require risk-approved recovery and reauthentication; verify active factors server-side |
| View sessions/devices (KG-009) | Device/session inventory, current vs other, last activity with timezone/uncertainty, revoke pending/completed, stale/unknown | Never present approximate device geolocation as exact; require policy controls on revoke-all/current session and test stale tabs |
| Link/unlink external provider or app (KG-010) | Provider identity and scopes, pending authorization, linked, conflict, expired, unlink pending/completed | Explicitly distinguish identity provider link from delegated app permissions; explain consequences, keep a usable sign-in route and handle callback errors |

**Flow:** enter security section → inspect effective server-side status → optional step-up → disclose impact → initiate action → confirm authoritative result → show durable, accessible history/next step. A successful OAuth redirect, passkey dialog close or request receipt does **not** imply account state changed.

**Anti-example:** the settings page offers a “Remove last sign-in method” link without warning, hides recovery routes, and updates device inventory optimistically without a revocation result.

**Verification (NOT VERIFIED):** current/revoked sessions from multiple browsers; MFA enrollment and factor loss; passkey/browser unsupported/cancel paths; reauthentication expiry; external-provider callback timeout; keyboard/focus and localized recovery messages; no enumeration, session fixation or privilege escalation. Security tests must be executed against the actual identity provider and backend.

**Sources:** [NIST SP 800-63B-4](https://csrc.nist.gov/pubs/sp/800/63/b/4/final) (2025 digital identity guidance, applicability determined by security owner); [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) and [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) (maintained engineering guidance; consulted 2026-11-07); [WCAG 2.2 SC 3.3.8](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) (applicable accessible authentication tests). Related portal composition: [Account/settings portal](account-and-settings-portal.md).
