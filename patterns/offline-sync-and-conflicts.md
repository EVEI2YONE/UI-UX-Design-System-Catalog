# Offline work, synchronization and conflict recovery

**Kind:** guideline · **Status:** proposed · **Primary layer:** experiences

## Purpose and boundary

Help people continue work safely across network loss, retries, delayed synchronization, session changes and concurrent edits. **Use when** a product supports offline reading/editing, local drafts, delayed submission, optimistic updates, or synchronization across devices. **Avoid when** promising offline support or automatic background synchronization the actual platform does not implement.

[Interaction states and recovery](interaction-states-and-recovery.md) owns generic pending/timeout and retry states. This page owns **local-vs-server status, queuing, conflict choices, authorization and consistency guarantees**. Engineering owns durable storage, idempotency, security, sync protocol, merge rules and data retention.

## Data and task status contract

| State | Meaning shown to user | Next step and safety |
| --- | --- | --- |
| Online / saved | Server has confirmed accepted state | Normal continuation; do not equate button press with persistence |
| Editing locally | Changes not yet confirmed remotely | Explain whether work will survive reload, sign-out or device loss |
| Offline draft stored | Local write confirmed, server not yet updated | Accurate “Saved on this device” language; retry/sync status |
| Queued for sync | Pending request recorded; delivery not yet confirmed | Show queue and safe cancellation where supported |
| Syncing | Upload in progress | Keep task context and indicate pending outcome |
| Synced / confirmed | Server confirms version accepted | Clear completion with timestamp/version only if grounded |
| Conflict detected | Local and remote edits differ | Offer review, safe choices, preservation and reversal |
| Sync rejected | Auth expired, record deleted, permission lost or request invalid | Do not silently overwrite; explain recovery and protect sensitive data |

**Crucial distinction:** “Saved locally,” “Queued,” and “Synced” are not interchangeable. An unreliable network or background task scheduler cannot justify a confident “All changes saved.”

## Failure and conflict decision rules

1. Choose **offline read-only**, **draft editing** or **full queued actions** explicitly according to sensitivity and business risk; distinguish by feature.
2. Show offline availability in a persistent, low-noise state. Avoid disabling navigation or hiding already-available content without reason.
3. Preserve drafts with clearly described storage scope and limits. Do not promise local persistence across private browsing, storage eviction, logout, device loss or cache clearing.
4. For consequential operations, determine idempotency and verify server outcome before retrying an ambiguous submission. Avoid duplicate payments or repeated destructive actions.
5. When a remote record changes, prefer a human-understandable difference/review if material facts conflict; never silently apply “last write wins” to safety-, finance- or trust-sensitive data.
6. Identify records that can be merged automatically vs those requiring product-specific conflict rules. Show a preview or recovery copy when meaningful, with usable keyboard and screen-reader support.
7. Session/role/tenant revocation must protect queued data and cached records. Do not sync stale privileged actions after authorization changes.
8. Support degraded network, intermittent connectivity, multiple tabs/devices and partial service failure; distinguish retryable from permanent errors.
9. Background Sync is **not universally supported**; use feature detection and a foreground/manual fallback. Never imply a guaranteed sync deadline.
10. Respect privacy/data lifecycle: sensitive cached information, deletion, encryption and retention need engineering/privacy review.

## Illustrative example and anti-example

**Example:** During a train journey, a notes editor shows “Saved on this device — waiting to sync.” Upon reconnect, a conflicting remote edit appears. The user can compare changes, choose a version or preserve both if supported, with a clear synced confirmation only after server acknowledgement.

**Anti-example:** A payment request timed out, so the app automatically reissues a non-idempotent charge multiple times and displays “Completed” before confirmation.

## Accessibility and localization

- Distinguish status using explicit text, not only icon color or spinner. Maintain focus and input on transitions.
- Ensure conflict review offers keyboard-equivalent controls and usable text summaries; do not rely on drag-only or side-by-side tiny diffs.
- Time and timestamps must be locale-appropriate; display time zone where relevant and preserve direction of mixed-script identifiers.
- Avoid excessive announcements when network flaps; communicate changes relevant to the current task.
- Long offline banners, zoomed/narrow layouts and RTL must preserve editing and exit actions.

## Verification scenarios

| Scenario | Status | Expected evidence |
| --- | --- | --- |
| Offline local draft vs remote persistence | NOT VERIFIED | Reload, kill/restore, storage eviction and session tests |
| Ambiguous submit / duplicated retry | NOT VERIFIED | Backend idempotency, delayed response and reconnection |
| Concurrent changes and conflict choice | NOT VERIFIED | Multi-device user task + merge-policy tests |
| Revoked access during offline work | NOT VERIFIED | Security/cache/queue revocation tests |
| Assistive technology, locale, narrow/reflow | NOT VERIFIED | Manual product checks |

## Sources and limits

- [MDN Background Synchronization API](https://developer.mozilla.org/en-US/docs/Web/API/Background_Synchronization_API) (consulted 2026-11-07): browser API and limitations; **limited availability**, not a cross-browser guarantee.
- [MDN IndexedDB API](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) (consulted 2026-11-07): client-side structured storage technology; does not guarantee persistence under all conditions.
- [MDN Storage quotas and eviction criteria](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria) (consulted 2026-11-07): storage availability/eviction tradeoffs.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) (Recommendation): applicable accessibility criteria, product tests required.

**Canonical ID:** `pattern.offline-sync` · **Owner:** unassigned · **Reviewed:** null · **Drafted:** 2026-11-07.

Related: [interaction recovery](interaction-states-and-recovery.md), [form composition](forms.md), [service recovery](service-recovery-and-support.md), [authentication lifecycle](authentication-and-account-lifecycle.md), [privacy/trust](../guidance/privacy-consent-and-trust.md).


## Versioned aggregate migrations and safe restore (Batch 6 — proposed, 2026-11-07)

**Context:** Some small pilots persist one revisioned aggregate per account rather than normalized rows. Little Wins demonstrates compare-and-swap retries and legacy project normalization; it also performs sample-group archival in a workspace read path. This is evidence of a migration approach, **not** proof of backup, restored history, or production concurrency capacity.

**Decision rules:**
1. Separate read-time *presentation normalization* from durable schema migration. If GET can cause a write, document why and test revision changes, repeated reads, partial failure, idempotency and concurrent writers; avoid unannounced history changes on apparently read-only navigation.
2. Define schema version, migration ownership, forward/backward compatibility, backup snapshot and rollback before altering stored historical records. Preserve original IDs, attribution and ledger references; never invent data to satisfy a new UI.
3. For a revision conflict, explain whether user changes were rejected or retried and whether a refreshed view is authoritative. Do not treat optimistic state as saved until the server confirms its revision.
4. Treat backup, restore, import and export as different capabilities. A database snapshot alone does not imply a user-facing restore journey; document recovery-point limits and operational responsibility.
5. Test simultaneous updates to independent projects within one aggregate, payload growth/limits, bounded retries and interrupted migrations. When data volume or collaboration grows, determine whether aggregate contention or export costs justify incremental restructuring, rather than recommending normalization without measurements.

**Example:** show a conflict notice with safely retained user input and a refresh/review option; migration tests confirm two runs produce the same data and no duplicated points.

**Anti-example:** a GET request silently migrates records repeatedly, or a stale tab overwrites a newer group configuration while displaying “Saved”.

**Verification:** old/new fixture comparisons, repeated migration idempotency, no missing/duplicated ledger entries, revision collisions, interrupted restore, authorized cross-scope export, and keyboard/screen-reader conflict recovery. All application verification remains NOT VERIFIED.
