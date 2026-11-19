# Commenting and annotations

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Attach feedback, questions or discussion to a stable object or selected content region and manage replies, mentions and resolution without losing the original context.

**Use when:** People review, negotiate or discuss changes to shared records, documents, designs or media.

**Avoid when:** Simple one-time feedback submission or broad broadcast chat has no meaningful anchored discussion context.

**Ownership:** The pattern owns thread creation, display, context anchoring, participation and resolution UX. The product owns visibility, authorization, moderation, notification routing, version history and authoritative storage.

## Journey and state contract

| Stage | User-facing decision and state | Failure and recovery expectation |
| --- | --- | --- |
| Choose anchor | Select a document, field, range or coordinate with a readable anchor description. | When content is later changed, show a stale or detached anchor rather than silently moving discussion. |
| Compose | Show editor label, recipients/mentions and audience before posting. | Preserve drafts on recoverable errors and clarify whether mentions will notify others. |
| Post/reply | Distinguish sending, confirmed, failed and unknown posting outcomes. | Prevent duplicate comments on retry after acknowledgement loss. |
| Review/resolve | Show reply order, authorship, edit markers and resolution status. | Make resolved threads discoverable and allow reopen only when authorized. |
| Change context | Handle deleted objects, moved text, private versions and lost collaborator permissions. | No accidental disclosure of comment content through previews or notifications. |

## Decision rules and tradeoffs

- Define anchor identity separately from visible selection: range offsets alone are fragile across document revisions.
- Clarify who can view, reply, edit, delete, resolve and reopen a thread, with service-enforced permissions.
- Distinguish edit history from raw comment text and display whether a reply was altered when relevant.
- Mention suggestions must use safe disambiguation and should not reveal users or channels beyond the author's authorized audience.
- Do not delete discussion context when the referenced content is removed; show a policy-appropriate orphaned/resolved state.
- Coordinate notifications with user preferences; an in-thread mention is not proof a notification was delivered.

## Dense-review triage and annotation discovery

A few discussions can be displayed next to anchors. A document with hundreds of overlapping comments needs a **task-driven discovery model** so users can find actionable feedback without losing document context.

| Condition | Recommended presentation | Avoid |
| --- | --- | --- |
| Few threads | Anchored marker and readable thread panel with stable identity | Covering text or moving an anchor when viewport changes |
| Many markers in the same region | Cluster markers with thread count; allow an accessible list of threads in the cluster | Hiding overlap or equating pixel position with importance |
| Reviewer needs to complete work | Offer **unresolved**, **assigned to me** (if supported), **mentions**, and **action required** filters, visible counts and reset | Treating newest-first as priority or deleting resolved discovery |
| Filtered or hidden anchor | Provide text-first results with excerpt, author, status and anchor context | Making the visual marker map the only discovery method |
| Changed or detached content | Preserve thread identity and explicitly show detached anchors and safe reattach options | Silently snapping a thread onto another sentence |
| Restricted thread | Enforce visibility at source, including counts, search and notifications | Leaking thread existence or participants in cluster totals |

**Priority is not recency.** Use explicit criteria such as addressed-to-me, unresolved blocker or required decision. If priority is inferred, disclose the rule and allow predictable ordering. Product permissions and ranking inputs remain app-owned. Connect to [attention management](notifications-and-attention.md) for notification batching and [cognitive-load guidance](../../knowledge/guidance/cognitive-load-and-decisions.md) for progressive disclosure.

**Keyboard and list alternative:** Each result has a descriptive name (for example, “Unresolved comment on heading ‘Payment terms’”), status, context and reachable filter. Opening a thread has a predictable focus destination; closing returns focus to a surviving list item or anchor. Announce settled result-count changes without narrating every marker movement.

**Illustrative review task:** A document contains 120 comments. A reviewer selects “Unresolved” and “Assigned to me,” opens a thread by keyboard, identifies the exact sentence and permitted audience, resolves it and returns to the next result. A deleted paragraph appears as a detached thread instead of vanishing. This is a synthetic scenario, not observed user research.

**Verification plan:** Test dense/sparse documents, zero results, cluster expansion, RTL and translated excerpts, screen-reader navigation, focus round-trip, permission boundaries and anchor detachment. Record implementation revision and observations; none is verified by the prose specification.

## Interaction, accessibility, layout and localization

- Compose/reply controls use labeled inputs, error summaries, meaningful send states and keyboard-friendly mention suggestions.
- Keyboard users must be able to locate an anchor, open its thread, read replies, and return to their previous reading/editing point.
- Unresolved/resolved states need text and semantics beyond color. Avoid automatically scrolling the document while another person types.
- Support long replies, quoted text, translations, bidi names and narrow comment sidebars without clipping.

Use semantic status tokens for state, warning, focus and affordances rather than color alone. Verify platform and assistive-technology behavior, reduced motion, dark/high-contrast themes, translated growth and RTL in actual consuming products. State pending, confirmed and uncertain outcomes honestly.

## Example and anti-example

**Illustrative example:** A reviewer selects a paragraph, comments on unclear wording, the author replies, and the reviewer resolves the thread; after the paragraph changes, the thread retains a valid anchor or explicitly notes that it is detached.

**Anti-example:** A comment is pinned only to a screen pixel, so a responsive layout change silently attaches the discussion to another sentence.

## Evidence and verification

| Scenario | Evidence required | Status |
| --- | --- | --- |
| Anchor stability after version edits and responsive reflow | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |
| Mention permissions, duplicate submission, resolution and deleted content | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |
| Notification scope, privacy and audit-of-edits policy | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |
| Keyboard navigation between anchor/thread, zoom and RTL text | Observe in a real integration or representative moderated task test; record device, role, source/version and limitations | NOT VERIFIED |

No backend contract, human evaluation, released component, security guarantee, performance baseline or accessibility certification is verified by this documentation-only pattern. The consuming team must validate actual data effects and permission decisions.

## Sources, applicability and related concepts

- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — contextual reference; confirm current edition and applicability.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual reference; confirm current edition and applicability.
- Related canonical concepts: [Collaboration and sharing](collaboration-and-sharing.md), [Content publishing](content-creation-and-publishing.md), [Notifications](notifications-and-attention.md), [Interaction recovery](interaction-states-and-recovery.md).
- **Scope limit:** Authoritative business rules and real integrations remain product-owned. Maintain a human review record before raising status beyond proposed.

## Representative task verification case

**Scenario to specify (illustrative, not tested):** Evaluate a representative dense-document task, including permission isolation, screen-reader navigation, filter recovery and detached anchors. Define user intent, initial and resulting authoritative state, invalid/unknown outcomes and an explicit recovery path. Preserve permission boundaries, reversible actions and the meaning of existing canonical components.

**Evidence rule:** State the success/failure observation, keyboard focus return, error announcement, small screen, text expansion and locale/RTL requirements that are relevant to the task. Collect actual environment, reviewer, observable results and limitations before marking a real implementation check complete. See [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for applicable accessibility criteria; this source alone is not product or research evidence. No unexecuted check is PASS.

