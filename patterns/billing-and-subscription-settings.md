# Billing, plans, invoices and subscription settings

**Kind:** guideline · **Status:** proposed · **Layer:** experiences · **Owner:** unassigned · **Reviewed:** null · **Drafted:** 2026-11-07.

## Purpose and boundary

Use when a product exposes user or organization billing details, payment methods, plans, subscription status, cancellations or invoices. Avoid inventing payment logic or suggesting that a payment processor's embedded frame grants plan/entitlement permissions. Commerce, finance, tax, legal, security and payment-provider owners establish actual rules; this is a reusable **human-facing journey pattern**, not a payment implementation.

## Billing settings contract (KG-020)

- Make billing scope explicit: personal account, organization, workspace, seat owner and currency. Do not imply all users can edit payment methods merely because invoices are visible.
- Present allowed payment instrument types, brand/last digits or safe processor-supplied summary, current default method and next bill date only if reliable. Never render full payment details or collect raw card data through arbitrary app fields.
- Define add/replace/remove flow with processor authentication when required, pending vs verified vs failed status, and no optimistic “Saved” claim before authoritative result.
- Explain failed charges and next legitimate recovery action, avoiding duplicate retries that could charge twice. Do not reveal private invoices to unauthorized members.

## Plan/subscription lifecycle (KG-021)

| Action | What the user needs before confirmation | Follow-up states |
| --- | --- | --- |
| Upgrade / add seats | Effective price, taxes/fees where relevant, billing period, proration, when entitlement changes | Payment required, pending, confirmed, failure |
| Downgrade | Lost features, seat/storage limits, effective date, data access/retention and reversibility | Scheduled, changed, canceled/reverted, blocked |
| Cancel subscription | Renewal/end date, access effect, policy-based refunds, consequences and real cancellation path | Requested, pending, confirmed, expires at date |
| Renew/reactivate | New price/terms if applicable, eligibility, verification and account scope | Renewed, denied, payment action needed |
| Trial ends | Clear end date, next charges if any, how to avoid renewal charges under actual policy | Active, approaching, expired, converted |

A cancellation or downgrade action is **not the same** as deleting an account. Avoid obstructive cancellation loops, coercive copy, or inaccurate claims about refunds, legal rights or billing dates. Do not treat “payment succeeded” as proof entitlement or invoice delivery completed.

## Invoice/history patterns (KG-022)

- Provide human-readable chronological entries (date, period, description, amount, currency, payment/refund state) with accessible detail and download when offered.
- Distinguish receipt, invoice, credit note, refund and pending payment; retain historic documents according to actual policy. Explain missing, unavailable, delayed or corrected documents.
- Recheck authorization for each invoice link and export. Choose secure authenticated delivery and avoid guessable IDs or caching of private billing documents.

## End-to-end examples and anti-examples

**Example:** an organization owner opens Billing, sees a renewal date and scoped default payment method, previews a downgrade's exact effective date/feature loss, confirms the actual provider result, and can reopen the scheduled change.

**Anti-example:** a disabled Save button with no explanation, cancellation buried behind unrelated upsells, or a “Refund completed” toast when only a request has been queued.

## Inclusive and release checks

Use accessible provider-hosted fields where appropriate; label errors and next actions, preserve keyboard/focus after external authentication, support zoom/reflow, translated tax/payment terms, RTL and reduced motion. Test idempotent server operations, concurrent changes, processor outage, strong customer authentication where applicable, expired payment method, currency consistency, unauthorized invoice access, accessible download and return-to-task.

**Verification status:** product billing, legal, tax, security, payment-provider, user, accessibility and delivery tests **NOT VERIFIED**. Do not claim PCI compliance, consumer-law compliance, successful charge or cancellation from this guidance.

## Sources and existing guidance

- [FTC Bringing Dark Patterns to Light](https://www.ftc.gov/reports/bringing-dark-patterns-light) (2022 staff report; consulted 2026-11-07): deceptive subscription UX concerns; not legal clearance.
- [PCI Security Standards Council](https://www.pcisecuritystandards.org/document_library/) (consulted 2026-11-07): scope and current standards require provider/security validation; this page does not prescribe a compliance path.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) (Recommendation; consulted 2026-11-07): accessibility criteria, not product conformance.
- [Account/settings portal](account-and-settings-portal.md) for navigation and saving, [role-aware workspaces](role-aware-workspaces-and-context-switching.md) for actor/tenant authorization, [forms](forms.md) for validation, [privacy](../guidance/privacy-consent-and-trust.md) for data rights.
 
**Canonical ID:** `pattern.billing-subscription-settings`.
