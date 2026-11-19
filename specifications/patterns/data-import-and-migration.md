# Data import and migration

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Bring external structured data into a product with understandable mapping, preview, validation, duplicate handling, commit and recovery. The user must know whether existing records will be created, merged, replaced or skipped before changes are committed.

**Use when:** Users transfer datasets, configurations or legacy records into a new system and need to evaluate the resulting changes.

**Avoid when:** The user only attaches a file to a form; use File Upload. Low-level offline schema migrations without a user-facing decision belong in an engineering migration plan.

**Ownership:** This pattern owns the human import journey and consequence explanations. The consuming service owns schema interpretation, permissions, transactional guarantees, deduplication, storage and rollback capabilities. A client-side preview cannot guarantee the eventual import result.

## Journey and state contract

| Stage | User-facing decision and state | Failure and recovery expectation |
| --- | --- | --- |
| Prepare | Explain accepted source types, sample template, target workspace, eligible record types and privacy scope. | No access / wrong target: preserve selected source safely and explain available alternatives. |
| Select and parse | Show source name, encoding/delimiter where relevant, record count if known, parse warnings and the next step. | Corrupt file / wrong format: offer replacement without silently discarding valid work. |
| Map and validate | Match source columns to target fields; distinguish required, optional, unmapped and incompatible values. | Allow correction or removal of invalid rows; show actual examples rather than ambiguous success icons. |
| Preview changes | Summarize additions, updates, skips, conflicts and potentially destructive replacements, with representative rows. | Stale target data must trigger a revised preview rather than silently importing with old assumptions. |
| Commit and reconcile | Request an explicit confirm action; show queued, processing, confirmed, partial, failed or unknown result from the service. | Offer idempotent safe retry, a results file, and rollback only if the backend actually supports it. |

## Decision rules and tradeoffs

- Separate uploading bytes from interpreting data; success at transfer is not success at import.
- State the matching key used for duplicates and whether repeated imports create new records. Show skip/merge/replace choices only if supported.
- Preview must disclose conflicts, irreversible mutations, skipped fields and approximate counts; warn when preview is sampled rather than exhaustive.
- Preserve the mapping and input on recoverable failure, but revalidate authority and dataset freshness before committing.
- Differentiate partial import from complete success, with item-level outcomes; never fabricate rollback, atomicity or restoration guarantees.
- Use persistent progress for long-running work, support leaving and returning only when a durable job actually exists.

## Interaction, accessibility, layout and localization

- Mapping controls are labeled, keyboard operable and give unambiguous field relationships; drag-and-drop reordering needs a non-drag alternative.
- Use a stable multi-step structure with back/edit and a review summary before irreversible operations. Error summaries link to correction contexts.
- Keep source field names, sample values and target-field labels readable under long translations, zoom, narrow containers and RTL. Redact sensitive preview values.
- Use subdued status announcements for step changes; announce important import outcomes without narrating every row.

Use semantic status tokens for state, warning, focus and affordances rather than color alone. Verify platform and assistive-technology behavior, reduced motion, dark/high-contrast themes, translated growth and RTL in actual consuming products. State pending, confirmed and uncertain outcomes honestly.

## Example and anti-example

**Illustrative example:** An administrator imports customer contacts from CSV, maps Email to the existing email field, previews 28 additions and 7 updates, fixes three invalid rows, then confirms a server-validated import.

**Anti-example:** An Upload button reports 'Imported successfully' when the file was only transferred, then overwrites existing customer records without a preview.

## Evidence and verification

| Scenario | Evidence required | Status |
| --- | --- | --- |
| CSV with missing required field, duplicate keys, encoding issues, and incompatible rows | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |
| Stale permission / target changed between preview and commit | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |
| Partial success, retry after acknowledgement loss, and truthful rollback availability | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |
| Keyboard mapping, error summary, responsive table and sensitive-data redaction | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |

No backend contract, human evaluation, released component, security guarantee, performance baseline or accessibility certification is verified by this documentation-only pattern. The consuming team must validate actual data effects and permission decisions.

## Sources, applicability and related concepts

- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) — contextual reference; confirm current edition and applicability.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual reference; confirm current edition and applicability.
- Related canonical concepts: [File upload and attachments](file-upload-and-attachments.md), [Forms](forms.md), [Offline synchronization](offline-sync-and-conflicts.md), [Interaction recovery](interaction-states-and-recovery.md).
- **Scope limit:** Authoritative business rules and real integrations remain product-owned. Maintain a human review record before raising status beyond proposed.

## Representative task verification case

**Scenario to specify (illustrative, not tested):** Verify partial-error preview and duplicate reconciliation against sample data. Define user intent, initial and resulting authoritative state, invalid/unknown outcomes and an explicit recovery path. Preserve permission boundaries, reversible actions and the meaning of existing canonical components.

**Evidence rule:** State the success/failure observation, keyboard focus return, error announcement, small screen, text expansion and locale/RTL requirements that are relevant to the task. Collect actual environment, reviewer, observable results and limitations before marking a real implementation check complete. See [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for applicable accessibility criteria; this source alone is not product or research evidence. No unexecuted check is PASS.

