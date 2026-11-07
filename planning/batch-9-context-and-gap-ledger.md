# Batch 9 — Context-first catalog gap ledger

**Prepared:** 2026-11-07 · **Branch/PR:** `docs/ux-knowledge-expansion-batches-7-12`, cumulative PR #5 · **Status:** proposed; human/production verification not performed.

## Catalog intake

Before authoring, reviewed `catalog/index.json` (28 concepts after Batches 7–8), root and nested indexes, `CONTRIBUTING.md`, `patterns/interaction-states-and-recovery.md`, `patterns/feedback.md`, `patterns/role-aware-workspaces-and-context-switching.md`, `patterns/forms.md`, `patterns/service-recovery-and-support.md`, `guidance/accessibility.md`, `guidance/internationalization.md`, `guidance/content-design-and-ux-writing.md`, and source/entry conventions.

| Candidate | Existing knowledge | Gap classification | Decision |
| --- | --- | --- | --- |
| Privacy / trust / ethical UX | Privacy cautions in UX measurement, content design and role-based workspaces | Cross-cutting rules incomplete | **Create** `guidance.privacy-trust`; no security/legal compliance claim |
| Sign-in / recovery / session lifecycle | Existing role-aware pattern covers authorized workspace *selection*, not identity proofing; forms cover field behavior | Distinct lifecycle missing | **Create** `pattern.authentication-lifecycle`, reuse workspaces/forms and require security policy |
| Notifications / attention | `pattern.feedback` covers inline/toast presentation, not notification scheduling or preference controls | Cross-channel decision layer missing | **Create** `pattern.notifications-attention`; extend existing feedback with pointer |
| Offline draft / sync / conflict resolution | `pattern.interaction-recovery` describes generic offline errors and retry | Data states and conflict UX incomplete | **Create** `pattern.offline-sync`; extend recovery guidance with pointer |

**Decision boundary:** preserve all existing IDs and contract pages. New entries cover distinct decisions rather than new runtime components.

## External sources and evidence limits

1. [UK ICO, data protection by design and by default](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/guide-to-accountability-and-governance/data-protection-by-design-and-by-default) — updated 2026-02-05, reviewed 2026-11-07; UK-specific privacy requirements, not a global law template.
2. [FTC, Bringing Dark Patterns to Light](https://www.ftc.gov/reports/bringing-dark-patterns-light) — 2022 staff report, reviewed 2026-11-07; deception risks, not a technical design standard.
3. [NIST SP 800-63B-4](https://csrc.nist.gov/pubs/sp/800/63/b/4/final) — final July 2025; auth assurance for relevant digital identity programs, requiring contextual security ownership.
4. [W3C, WCAG 2.2 SC 3.3.8 guidance](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) — accessible authentication, not verified application conformance.
5. [MDN, Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API) — web platform permission and service worker behavior; varies by browser and device.
6. [Apple, web push notifications](https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers) — platform-specific permission and delivery notes.
7. [MDN, Background Synchronization API](https://developer.mozilla.org/en-US/docs/Web/API/Background_Synchronization_API) — limited browser support; not guaranteed delivery.
8. [MDN, IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) — structured local storage; actual retention and quotas depend on browser environment.

## Acceptance/evidence checklist

- [x] Search existing registry and read related canonical pages before drafting.
- [x] Gather externally verified sources, identify normative vs professional/platform guidance, and record applicability.
- [x] Reuse existing feedback, form, role-aware and interaction-recovery guidance rather than duplicate.
- [x] Add proposed entry pages with actions, failure matrices, inclusion and source-ledger details.
- [x] Register durable IDs, related/dependency metadata, discovery paths and changelog.
- [ ] Run full repo validator and lookup tests from an executable checkout or CI; **NOT RUN** unless evidence is reported.
- [ ] Verify actual product keyboard, screen reader, translations, consent/backend behavior, account security, notification delivery and conflict handling; **NOT VERIFIED**.
- [ ] Assign owners and complete human source/semantics review; remains `unassigned`.

**Do not interpret a proposed design page as a shipped feature or a legal/security certification.** Future changes should be committed to cumulative PR #5 after their own context audit.
