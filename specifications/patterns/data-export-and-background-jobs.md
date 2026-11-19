# Data export and background jobs

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Let users request substantial work, leave or monitor it, and retrieve an authorized result with accurate processing, expiration and failure states. Export is the example; the lifecycle also applies to other user-initiated background jobs.

**Use when:** An operation takes too long for a single blocking request, or creates a sensitive output that may later be retrieved.

**Avoid when:** A simple immediate download or nonpersistent operation does not need a job queue, or an import with mapping/validation is the actual task.

**Ownership:** The pattern owns user-visible job lifecycle, scope, progress and result retrieval. Backend services own snapshot consistency, data authorization, redaction, retention, execution and link revocation.

## Journey and state contract

| Stage | User-facing decision and state | Failure and recovery expectation |
| --- | --- | --- |
| Configure | Choose records, filters, date range, permitted fields, format and intended destination. | Show scope and sensitive-data consequences before starting. |
| Request | Provide a durable job identifier if one exists; confirm acceptance rather than completion. | Retry only after checking for an existing request to avoid duplicates. |
| Queue/process | Show queued, running, stalled or verifying states and last-updated information. | If exact progress is unknown, explain stage without inventing a percentage or ETA. |
| Complete | Show confirmed availability, file format/size when known, creation time, expiration and authorized download. | Recheck access at download; do not expose a public permanent URL by default. |
| Fail/expire/cancel | Distinguish failed job, cancelled request, expired file and unavailable service. | Offer safe restart, support or another path; clarify whether cancellation stopped processing. |

## Decision rules and tradeoffs

- Differentiate request acceptance, job execution, result creation and downloaded-file state; each has a separate authoritative outcome.
- Use the same visible filter/selection scope that the backend will enforce; disclose record counts or sampling uncertainty and excluded fields.
- Treat sensitive outputs as time-bounded, permission-checked resources with a clear retention policy; no insecure link sharing promises.
- Support a history of jobs only if the service stores one; on lost acknowledgement, reconcile via job identity before another export.
- Define how data changes during generation affect the result: point-in-time snapshot, eventual contents or other explicit contract.
- Use a progress indicator only for measured progress, and explain if completing the job does not guarantee successful delivery.

## Interaction, accessibility, layout and localization

- Accessible status, cancellation and download controls should be available without keeping the page open; avoid unwanted repeated live announcements.
- Job list rows need stable ID, requested scope, timestamp/timezone, status and permitted actions.
- Never rely on color or an indeterminate spinner alone; support translations, long filenames, narrow screens and large text.
- Provide clear notification preference and privacy boundaries when a job result can be shared or notified externally.

Use semantic status tokens for state, warning, focus and affordances rather than color alone. Verify platform and assistive-technology behavior, reduced motion, dark/high-contrast themes, translated growth and RTL in actual consuming products. State pending, confirmed and uncertain outcomes honestly.

## Example and anti-example

**Illustrative example:** An analyst requests a CSV export of the filtered report. The job is queued, then ready; the interface shows file scope, creation time and a link that expires under server policy.

**Anti-example:** The interface marks an export ready after the user clicks Generate and includes an anonymous, unlimited-access download URL.

## Evidence and verification

| Scenario | Evidence required | Status |
| --- | --- | --- |
| Selected scope and filtered result reconciliation | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |
| Lost submit acknowledgement, stalled/cancelled/expired job, revoked access | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |
| Actual result freshness, redaction and server authorization | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |
| Keyboard job navigation, timestamp locale and status announcement noise | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |

No backend contract, human evaluation, released component, security guarantee, performance baseline or accessibility certification is verified by this documentation-only pattern. The consuming team must validate actual data effects and permission decisions.

## Sources, applicability and related concepts

- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — contextual reference; confirm current edition and applicability.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual reference; confirm current edition and applicability.
- Related canonical concepts: [Data tables](data-tables.md), [Search and filtering](search-and-filter.md), [Privacy and trust](../../knowledge/guidance/privacy-consent-and-trust.md), [Interaction recovery](interaction-states-and-recovery.md).
- **Scope limit:** Authoritative business rules and real integrations remain product-owned. Maintain a human review record before raising status beyond proposed.

## Representative task verification case

**Scenario to specify (illustrative, not tested):** Test an expired download and pending job after sign-out. Define user intent, initial and resulting authoritative state, invalid/unknown outcomes and an explicit recovery path. Preserve permission boundaries, reversible actions and the meaning of existing canonical components.

**Evidence rule:** State the success/failure observation, keyboard focus return, error announcement, small screen, text expansion and locale/RTL requirements that are relevant to the task. Collect actual environment, reviewer, observable results and limitations before marking a real implementation check complete. See [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for applicable accessibility criteria; this source alone is not product or research evidence. No unexecuted check is PASS.

