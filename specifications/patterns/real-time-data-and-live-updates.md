# Real-time data and live updates

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Keep users oriented when information changes independently of their current action, balancing freshness, stability, notifications and attention. Live presentation is separate from offline write synchronization.

**Use when:** A dashboard, queue, feed or shared workspace receives new, changed or removed records while being viewed.

**Avoid when:** The source only updates on explicit refresh or the task is primarily resolving locally saved edit conflicts.

**Ownership:** The pattern owns visible freshness, background-update policy, change summaries, focus preservation and pause/resume controls. Backend owns event validity, authorization, ordering, snapshots and reconnect reconciliation.

## Journey and state contract

| Stage | User-facing decision and state | Failure and recovery expectation |
| --- | --- | --- |
| Load baseline | Show the latest known snapshot and when its freshness can be trusted. | Differentiate loading from an actual empty collection. |
| Receive changes | Show new/changed/removed items without silently replacing selected content. | Keep active selection, input drafts, focus and current reading location stable. |
| Show unseen updates | Indicate accumulated changes, e.g. '5 new items', with an explicit review action where useful. | Avoid auto-inserting large batches at the top while someone reads or uses a screen reader. |
| Disconnect/reconnect | Expose stale, reconnecting, recovered and unavailable states as appropriate. | Reconcile with an authoritative snapshot after missed events rather than assuming gap-free delivery. |
| Resume or pause | Allow a predictable refresh/apply action for disruptive lists; preserve user preferences if actually stored. | Explain what paused means and when critical warnings still require attention. |

## Decision rules and tradeoffs

- Define data freshness vocabulary: current, last-known, stale, reconnecting and unverified. A heartbeat is not proof every item is current.
- Decide which changes update silently, which need a nonintrusive count and which warrant an important interrupt based on user consequences.
- Maintain stable IDs and ordering; avoid scroll jumps, lost focus and unexpected route changes when list order shifts.
- Handle superseded, duplicate or late events and permission revocation in the authoritative model; avoid displaying data from an old workspace.
- Separate content change notifications from save-status and conflict-resolution semantics already owned by Offline Sync.
- Use reduced announcement frequency: summarize meaningful changes rather than sending a live-region update for every field.

## Interaction, accessibility, layout and localization

- New-item banners, refresh controls and staleness labels are keyboard operable and accessible even without color/animation.
- Never auto-submit or activate actions on incoming updates. Preserve draft content and validate stale decisions before committing.
- Design explicit thresholds for accumulating changes, and compare mobile/desktop interruptions under reduced motion.
- Use locale-formatted timestamps, relative time with precise alternative, and RTL-aware placement for change indicators.

Use semantic tokens, clear text, explicit focus and status behavior instead of color-only or motion-only cues. Validate actual keyboard and screen-reader behavior, reduced motion, high contrast, text growth and RTL with representative users and integrations before claiming success.

## Example and anti-example

**Illustrative example:** A ticket queue shows '4 new tickets' while a reviewer examines a record. Opening the updates preserves the current ticket, restores position, and reports any revoked access safely.

**Anti-example:** Every incoming event re-sorts the queue instantly, moves keyboard focus to the top and announces each row, making review impossible.

## Evidence and verification

| Scenario | Evidence required | Status |
| --- | --- | --- |
| Out-of-order/duplicate events and reconnect with a missed interval | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |
| Active reading/editing during insert, sort, deletion and permission revocation | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |
| Live region announcement volume, reduced motion, focus and scroll stability | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |
| Staleness comprehension under unreliable connectivity and cross-time-zone timestamps | Record test method, system authority, user context, observed result and remaining gaps | NOT VERIFIED |

This documentation does not verify real users, moderation outcomes, backend access control, transactional safety, accessibility conformance, or production reliability. Product-specific policies and consent requirements need separate review.

## Sources, applicability and related concepts

- [WCAG Status Messages Understanding](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) — supporting context; verify applicability and current edition.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — supporting context; verify applicability and current edition.
- Related canonical sources: [Offline sync](offline-sync-and-conflicts.md), [Notifications](notifications-and-attention.md), [Data tables](data-tables.md), [Interaction recovery](interaction-states-and-recovery.md).
- **Scope limit:** This is a proposed UX contract, not a complete backend or security design.
