# Reporting, moderation and appeals

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Give affected people a trustworthy route to report harmful content or conduct, submit allowed evidence, understand available outcomes and appeal eligible decisions. The reporting experience is distinct from the staff moderation tool.

**Use when:** A product permits reports, policy enforcement or user appeals with an actual receiving and review service.

**Avoid when:** A generic support ticket with no policy decision, reporting eligibility or protected evidence is sufficient.

**Ownership:** This pattern owns reporter and appellant flows, status and disclosure. Enforcement staff own investigation, safety decisions, evidence retention, legal process and permissioned communication. Internal review workspaces have their own specification.

## Journey and state contract

| Stage | User-facing decision and state | Failure and recovery expectation |
| --- | --- | --- |
| Recognize and report | Offer a discoverable report action, plain categories, immediate safety guidance where appropriate and optional context. | Do not force a person to re-view harmful content to complete a report. |
| Describe and review | Collect proportionate facts, attachments and privacy choices; explain what recipients may see. | Handle sensitive evidence and avoid exposing third-party data beyond legitimate need. |
| Submit and acknowledge | Show acceptance status and a case/reference identifier only after confirmed receipt. | If a network timeout occurs, check for an existing report before encouraging duplicate submission. |
| Track outcome | Distinguish received, under review, awaiting information, action taken/no action and closed where disclosure is allowed. | Do not reveal confidential moderation details or imply a specific decision will be made. |
| Appeal/reconsider | Explain eligible grounds, any actual deadline, evidence requirements and final decision status. | If appeals are unavailable, communicate the limitation without inventing a path. |

## Decision rules and tradeoffs

- Separate an immediate block/mute/protect action from the slower report and review process; do not promise instantaneous enforcement.
- Do not expose reporter identities to the reported party or to unrelated participants by default; follow actual risk policy.
- Use precise but neutral categories and allow uncertainty or an 'other' path where appropriate, without forcing unsupported allegations.
- Explain what report acknowledgment means and what outcomes may remain undisclosed; no fake transparency about private enforcement.
- Avoid infinite appeals, inaccessible deadlines or recurring requests for traumatic information; policy owners determine eligibility.
- Prioritize safety and anonymity requirements when the context involves vulnerable users, minors or harassment; specialist review remains necessary.

## Interaction, accessibility, layout and localization

- Report and appeal forms must have descriptive labels, safe attachment handling, keyboard access and a clear exit.
- When the content becomes unavailable, retain report context if policy permits instead of blocking submission.
- Show status in text and time information in the user's locale, without color-only meaning or overwhelming live announcements.
- For urgent threats, product guidance must use actual configured support/emergency routes; never invent a 24/7 moderator or response window.

Use semantic tokens, clear text, explicit focus and status behavior instead of color-only or motion-only cues. Validate actual keyboard and screen-reader behavior, reduced motion, high contrast, text growth and RTL with representative users and integrations before claiming success.

## Example and anti-example

**Illustrative example:** A member reports abusive comments, gets a confirmed receipt, blocks the author separately, and later sees a limited case outcome with an appeal option only if policy supports it.

**Anti-example:** A form promises immediate removal and publicly displays the reporter's name alongside the allegation before moderation occurs.

## Evidence and verification

| Scenario | Evidence required | Status |
| --- | --- | --- |
| Report intake, duplicate submits, spam/abuse safeguards and authoritative acknowledgement | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |
| Sensitive evidence/identity redaction in report and appeal states | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |
| Outcome disclosure limits, appeal eligibility, expired eligibility and closed cases | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |
| Keyboard completion, mobile/RTL, trauma-informed copy and assistive status | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |

This documentation does not verify real users, moderation outcomes, backend access control, transactional safety, accessibility conformance, or production reliability. Product-specific policies and consent requirements need separate review.

## Sources, applicability and related concepts

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — supporting context; verify applicability and current edition.
- [OWASP Access Control Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — supporting context; verify applicability and current edition.
- Related canonical sources: [Review Workspace](../experiences/review-workspace/spec.md), [Service recovery](service-recovery-and-support.md), [Privacy and trust](../../knowledge/guidance/privacy-consent-and-trust.md), [File upload](file-upload-and-attachments.md).
- **Scope limit:** This is a proposed UX contract, not a complete backend or security design.

## Representative task verification case

**Scenario to specify (illustrative, not tested):** Verify restricted visibility and appeal handoff with scenario-specific evidence. Define user intent, initial and resulting authoritative state, invalid/unknown outcomes and an explicit recovery path. Preserve permission boundaries, reversible actions and the meaning of existing canonical components.

**Evidence rule:** State the success/failure observation, keyboard focus return, error announcement, small screen, text expansion and locale/RTL requirements that are relevant to the task. Collect actual environment, reviewer, observable results and limitations before marking a real implementation check complete. See [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for applicable accessibility criteria; this source alone is not product or research evidence. No unexecuted check is PASS.

