# Privacy, consent and trustworthy UX

**Kind:** guideline · **Status:** proposed · **Primary layer:** cross-cutting

## Purpose and boundaries

Design privacy-related choices so people understand what data is used, why, with whom, and what control they have. **Use when** gathering personal information, asking permissions, requesting optional consent, showing sensitive content, changing visibility, or deleting an account. **Avoid when** using this design guidance as proof of compliance with law or replacing an actual security/privacy impact assessment. Product legal, data-protection and engineering teams own jurisdiction-specific requirements and technical enforcement.

Consent is **not** the lawful basis for every processing activity. Identify the actual basis and obligations with the responsible team before designing a consent screen.

## Decision and state contract

| Situation | Expected user-facing behavior | Risk to avoid |
| --- | --- | --- |
| Request personal data | Explain purpose and required/optional fields before input; minimize collection | Collecting data merely because a field exists |
| Ask device permission | Explain the in-task benefit; show a viable decline path where feasible | Contextless repeated prompts or forcing permission |
| Optional consent | Clearly separate purposes and allow meaningful accept/decline choices where required | Deceptive prominence, preselection or bundled choices that negate valid consent |
| Change privacy preferences | Show effective status, update confirmation and any delayed effects | Claiming that a UI toggle has already deleted stored data |
| Publish/share content | Disclose audience and consequences before sharing, with suitably protective defaults | Unexpected public exposure or ambiguous “Continue” |
| Delete/download data | Distinguish draft deletion, account closure and subject rights; explain consequences and verified status | Promising immediate total erasure when retention obligations apply |
| Shared devices | Reduce unnecessary sensitive previews and stale personal information | Private account data visible after sign-out or context switch |

## Permission/choice flow

```text
User need -> clear reason and scope -> choice / decline or applicable alternative
  -> processing / permission result -> truthful persisted state
  -> discoverable adjustment or withdrawal where applicable -> confirmed outcome
```

A browser/device permission is not the same thing as an app-category preference. Withdrawal, deletion and purpose restrictions may have asynchronous effects; display **pending vs completed** accurately. For potentially irreversible choices, include a consequence summary, explicit action label, safe cancellation, and a trustworthy confirmation.

**Illustrative example:** Before displaying a profile image publicly, a clearly labeled setting names the audience, defaults to a privacy-conscious visibility where justified, and confirms when that saved setting takes effect.

**Anti-example:** A bright “Accept all” option next to a disguised decline control, with unrelated optional tracking required to complete a basic task.

## Content, access and internationalization

- Use plain language and user-research terminology; do not rely on icon/color alone to distinguish accept and decline.
- Support comparable keyboard and screen-reader access, visible focus, translated labels and RTL/reflow.
- Protect sensitive user-visible data in screenshots, browser notifications, previews, caches and support handoffs.
- Reconsider friction and urgency: avoid countdowns, shame copy, misleading scarcity or intentional cancellation obstacles.
- Only claim that a request or preference was completed after the relevant product system confirms it.

## Verification matrix

| Check | Status | Required evidence |
| --- | --- | --- |
| Data purpose, necessity and legal basis agreed with owner | NOT VERIFIED | Processing inventory and privacy review |
| Consent/permission choice, decline and later changes | NOT VERIFIED | Tested product flows and jurisdiction review |
| Deletion/export state truthful | NOT VERIFIED | Backend and support lifecycle tests |
| Keyboard, screen reader, text expansion, RTL | NOT VERIFIED | Manual task-based checks |
| Users understand audience/consequence | NOT VERIFIED | User research |

## Source ledger and applicability

- [UK ICO, data protection by design and by default](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/guide-to-accountability-and-governance/data-protection-by-design-and-by-default) (updated 2026-02-05; consulted 2026-11-07): UK GDPR-oriented duties and default protections, not universal law.
- [FTC, Bringing Dark Patterns to Light](https://www.ftc.gov/reports/bringing-dark-patterns-light) (staff report, 2022): examples of deceptive design, not a substitute for jurisdiction-specific legal advice.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) (Recommendation): web accessibility criteria; this documentation is not a conformance assessment.

**Canonical ID:** `guidance.privacy-trust` · **Owner:** unassigned · **Reviewed:** null · **Drafted:** 2026-11-07.

Related: [content design](content-design-and-ux-writing.md), [authentication lifecycle](../patterns/authentication-and-account-lifecycle.md), [notifications](../patterns/notifications-and-attention.md), [accessibility](accessibility.md), [service recovery](../patterns/service-recovery-and-support.md).
