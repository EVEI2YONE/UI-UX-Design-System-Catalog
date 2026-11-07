# Account/settings knowledge expansion — batch progress

**Prepared:** 2026-11-07. **Base:** `main` at `de4a290fc062267fb0ede14f53601036378a4e91`. **Branch:** `docs/account-settings-knowledge-batches`. **Review:** proposed; PR not merged. **Source product:** no specific target application was selected; observations refer to existing catalog, not a tested account portal.

## Context-first methodology and batch disposition

| Batch | Candidate gaps | Catalog context reviewed before editing | Canonical action and batch commit | Status |
| --- | --- | --- | --- | --- |
| 1 — Portal/profile | KG-001–006 | Registry, root/nested indexes, task flows, form and interaction recovery, authentication, privacy, role-aware access, contribution rules | Create [account/settings portal](../patterns/account-and-settings-portal.md) for cross-section architecture, overview, profile and contact changes; defer identity and data policy to related owners · `6e8ca76` | Committed; index integration in final commit |
| 2 — Security/privacy | KG-007–013 and KG-023 | Auth lifecycle, privacy/data lifecycle, managed profile vs login, role-aware server authorization, NIST/OWASP and jurisdictional limits | **Extend** [authentication](../patterns/authentication-and-account-lifecycle.md), [privacy](../guidance/privacy-consent-and-trust.md) and [role-aware](../patterns/role-aware-workspaces-and-context-switching.md) contracts · `323958a` | Committed; domain owner review pending |
| 3 — Preferences/billing/QA | KG-014–022 and KG-024 | Notifications, themes, localization and quality pages, catalog structure, payment vs form/state boundaries | **Extend** notifications/themes/i18n/quality; **create** [billing/subscription](../patterns/billing-and-subscription-settings.md) for distinct payment/plan/invoice tasks · `ba382b7` | Committed; provider/legal review pending |

## Candidate-by-candidate coverage decisions

| Candidate | Decision | Canonical owner |
| --- | --- | --- |
| KG-001 Settings IA | New composed portal guidance | `pattern.account-settings-portal` |
| KG-002 Account overview | New composed portal guidance | `pattern.account-settings-portal` |
| KG-003 Save/dirty/conflict | Extend composition, reuse forms/offline | `pattern.account-settings-portal` |
| KG-004 Profile editing | New composed portal guidance, reuse forms | `pattern.account-settings-portal` |
| KG-005 Verified email/phone | Extend authenticated contact journey | `pattern.account-settings-portal` + `pattern.authentication-lifecycle` |
| KG-006 Account export | Reuse existing data lifecycle; add portal state | `guidance.privacy-trust` + `pattern.account-settings-portal` |
| KG-007 Credentials | Extend existing auth | `pattern.authentication-lifecycle` |
| KG-008 MFA/passkeys | Extend existing auth | `pattern.authentication-lifecycle` |
| KG-009 Device sessions | Extend existing auth | `pattern.authentication-lifecycle` |
| KG-010 Connected provider/apps | Extend existing auth | `pattern.authentication-lifecycle` |
| KG-011 Privacy preference center | Extend existing privacy | `guidance.privacy-trust` |
| KG-012 Personal data rights | Extend existing privacy | `guidance.privacy-trust` |
| KG-013 Closure/deletion | Extend existing privacy + auth | `guidance.privacy-trust` |
| KG-014 Notification taxonomy | Extend existing notifications | `pattern.notifications-attention` |
| KG-015 Quiet hours/digest | Extend existing notifications | `pattern.notifications-attention` |
| KG-016 Appearance controls | Extend tokens/theme rules | `foundation.design-tokens` |
| KG-017 Accessibility preferences | Extend theme/system preference constraints | `foundation.design-tokens` |
| KG-018 Language switch | Extend existing i18n | `guidance.internationalization` |
| KG-019 Regional settings | Extend existing i18n | `guidance.internationalization` |
| KG-020 Billing methods | New specialized lifecycle | `pattern.billing-subscription-settings` |
| KG-021 Plan/subscription changes | New specialized lifecycle | `pattern.billing-subscription-settings` |
| KG-022 Invoices/history | New specialized lifecycle | `pattern.billing-subscription-settings` |
| KG-023 High-risk authorization | Extend role-aware access rules | `pattern.role-aware-workspaces` |
| KG-024 Portal-wide verification | Extend existing quality gate | `governance.quality` |

**Disposition summary:** 24 candidates reviewed; 2 new canonical concepts; 7 existing concept documents extended; 0 intentionally duplicated component contracts. The original 24 candidates were prompts, **not 24 verified missing catalog pages**. All additions remain proposed and require accountable owner, design, security, privacy/legal and real-product review as applicable.

## Source applicability and review limits

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) — normative accessibility standards and practical widget patterns; product testing required.
- [NIST SP 800-63B-4](https://csrc.nist.gov/pubs/sp/800/63/b/4/final) and [OWASP Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html), [Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — identity/security guidance, not evidence of implementation.
- [ICO data protection by design](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/guide-to-accountability-and-governance/data-protection-by-design-and-by-default) and [FTC Dark Patterns](https://www.ftc.gov/reports/bringing-dark-patterns-light) — jurisdiction-specific and advisory privacy/choice context, not a legal determination.
- [W3C Internationalization Quick Tips](https://www.w3.org/International/quicktips/) — language/RTL considerations; product support depends on locale scope.
- [PCI SSC document library](https://www.pcisecuritystandards.org/document_library/) — payment security reference requiring expert applicability assessment; no claim of compliance or provider behavior.

**Verification at drafting:** catalog source review PASS; catalog validator/unit/CI checks PENDING; actual product flow, payment, authentication, deletion, browser delivery, keyboard/assistive technology and locale tests NOT VERIFIED. Report real checks and results in PR before review. There is no target-app implementation PR.
