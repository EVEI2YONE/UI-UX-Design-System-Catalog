# Permissions and access requests

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Make restricted actions understandable and offer a safe route to request, track and, where allowed, change access. Request status and effective authorization are separate concepts.

**Use when:** A person needs access to a resource or capability they lack and an authorized request/approval process actually exists.

**Avoid when:** A single sign-in error only requires authentication recovery, or disclosure of the resource existence/requester identity would itself violate security policy.

**Ownership:** The pattern governs user-facing request, explanation and status comprehension. Policy, identity, approval routing, least-privilege checks and revocation are enforced by the backend, never by UI visibility alone.

## Journey and state contract

| Stage | User-facing decision and state | Failure and recovery expectation |
| --- | --- | --- |
| Encounter restriction | Explain the blocked task using only information the requester is permitted to see. | For hidden resources, show an appropriate generic denied state instead of revealing existence or owner. |
| Prepare request | Identify resource or role scope, intended duration, optional justification and recipients when disclosure is permitted. | Avoid requesting a broad administrative role when task-specific access is adequate. |
| Submit | Confirm requested scope and consequences; distinguish submitted from approved. | On timeout, check whether the request exists before allowing a duplicate. |
| Pending / decided | Display pending, approved, denied, expired, withdrawn and revoked results, including next permissible action. | Do not expose private reviewer identity, reasons or other members' permissions without authorization. |
| Use / change access | Re-evaluate effective permission when returning to the resource or following a deep link. | If permission is later revoked, stop the action and preserve non-sensitive user context. |

## Decision rules and tradeoffs

- Keep signed-in identity, selected workspace, requested role and effective capability distinct; reauthorization occurs on each protected server action.
- Use task-oriented permission descriptions, such as 'View reports', rather than relying only on opaque role names.
- Never mark a resource accessible until an authoritative permission check confirms it; an accepted request is not a capability grant.
- Design invitation acceptance, access requests and owner-driven sharing as separate tasks with explicit cross-links to their canonical patterns.
- Support withdrawal, renewal or appeals only where policy provides them; explain denial without leaking sensitive context.
- Apply rate limiting, duplicate handling and audit policy in the service; expose user-appropriate feedback without claiming security from interface controls.

## Interaction, accessibility, layout and localization

- Request and revoke controls must have explicit accessible names and clear consequences; status should not be color-only.
- Keyboard focus returns to a meaningful destination after a request dialog, approval-status update or permission revocation.
- Handle long resource names, organization scopes, localized role labels and reduced-width confirmation screens.
- Deep links and stale browser tabs must recover to a valid authorized route without showing protected data.

Use semantic status tokens for state, warning, focus and affordances rather than color alone. Verify platform and assistive-technology behavior, reduced motion, dark/high-contrast themes, translated growth and RTL in actual consuming products. State pending, confirmed and uncertain outcomes honestly.

## Example and anti-example

**Illustrative example:** A teammate opening a restricted planning board sees a safe restricted-state message, requests comment access, and later sees 'Approved'; the product rechecks authorization when they reopen the board.

**Anti-example:** A 'Request sent' toast is followed by an enabled Edit button even though no reviewer has granted access.

## Evidence and verification

| Scenario | Evidence required | Status |
| --- | --- | --- |
| Existence-disclosure-safe denial and cross-tenant direct URL access | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |
| Submit timeout, duplicate request, denial, expiry and revocation | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |
| Request scope/role comprehension and least-privilege alternatives | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |
| Keyboard, focus, privacy, localization and user-facing reasons | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |

No backend contract, human evaluation, released component, security guarantee, performance baseline or accessibility certification is verified by this documentation-only pattern. The consuming team must validate actual data effects and permission decisions.

## Sources, applicability and related concepts

- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — contextual reference; confirm current edition and applicability.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual reference; confirm current edition and applicability.
- Related canonical concepts: [Collaboration and sharing](collaboration-and-sharing.md), [Role-aware workspaces](role-aware-workspaces-and-context-switching.md), [Service recovery](service-recovery-and-support.md), [Authentication lifecycle](authentication-and-account-lifecycle.md).
- **Scope limit:** Authoritative business rules and real integrations remain product-owned. Maintain a human review record before raising status beyond proposed.
