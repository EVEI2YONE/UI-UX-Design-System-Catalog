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
