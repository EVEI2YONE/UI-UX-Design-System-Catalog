# Master-detail exploration

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Let people move between a collection and item details while preserving selection, orientation, filtering context and next-action continuity.

**Use when:** A list of records, messages, products or documents supports repeated inspection and contextual actions.

**Avoid when:** A single record has no meaningful collection context or a static article list works with standard links.

**Ownership:** The pattern owns composed collection/detail presentation and selection semantics. Each feature owns record retrieval, authorization, mutations and route state.

## Journey and state contract

| Stage | User-visible decisions and states | Recovery / evidence requirement |
| --- | --- | --- |
| Find | Browse, search, sort and filter a list | Clear selected item and result context |
| Select | Open item detail by stable identity, not list position | Selected/focused items remain distinguishable |
| Inspect | Show relevant detail and contextual actions | Preserve access to list context |
| Change collection | Handle delete/archive/new result while item is selected | Choose safe next focus/selection fallback |
| Return | Restore useful list position, query and filters where appropriate | Deep links and back behavior remain predictable |

## Design decisions

- At narrow widths, choose a clear list-to-detail route rather than shrinking both panels until text is unreadable.
- Avoid coupling selected data to array index: sorting or filtering must not expose another person's record.
- When a selected item disappears, announce the change and choose a visible, relevant fallback.
- If details update asynchronously, distinguish stale cached content from confirmed changes; never silently jump contexts.
- Use navigation links for destinations and buttons for actions, keeping selection separate from command activation.

## Inclusive operation, content, theming and locale

Provide keyboard and assistive-technology routes through each stage, visible headings and state feedback, and deliberate focus restoration after context changes. Support zoom/reflow, localized labels and units, RTL and high-contrast themes, touch alternatives and reduced motion. Use semantic tokens and make unavailable or irreversible outcomes understandable beyond color. Never treat a mock preview as proof of a real service outcome.

## Example and anti-example

**Illustrative example:** An email inbox retains query and scroll location after opening a message and returning; deleting it selects the next available message with focus explained.

**Anti-example:** Selecting row 4 by array index so a sort instantly shows a different person's private details.

For a worked cross-pattern composition using a card, detail, related-record editor, classification, recovery and return, see the [illustrative collection-to-related-record journey](../../examples/collection-to-related-record-journey.md). Use the canonical card, form, lifecycle and recovery contracts for normative decisions; the reference journey is **NOT VERIFIED** in a consuming product.

## Verification and research handoff

| Scenario | Expected evidence | Current status |
| --- | --- | --- |
| Deep link, browser back and responsive list-detail transitions | Record actual observed result, relevant cohort and environment | NOT VERIFIED |
| Filter/sort/selection stability, record deletion and empty states | Record actual observed result, relevant cohort and environment | NOT VERIFIED |
| Keyboard/assistive focus, RTL reading order, long details and data privacy | Record actual observed result, relevant cohort and environment | NOT VERIFIED |

Measure task completion, user error severity, abandonment and comprehension before asserting improvement. No baseline study, real back-end behavior or accessibility conformance is supplied by this concept.

## Sources, related concepts and limitations

- [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/patterns/) — contextual reference, not a universal implementation prescription.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual reference, not a universal implementation prescription.
- Related canonical guidance: [Task flows](task-flows-and-information-architecture.md), [Forms](forms.md), [Interaction recovery](interaction-states-and-recovery.md), [Accessibility](../../knowledge/guidance/accessibility.md), and [UX measurement](../../knowledge/guidance/ux-measurement.md).
- Review domain, locale, security, legal and service constraints separately before adoption.

## Applied decision and verification case

**Illustrative decision case (not observed):** Add an item-to-list return and focus restoration scenario. Name the initiating task, what becomes unavailable or uncertain, how the user learns the truthful state and which continuation is safe. Distinguish user-visible feedback from server authority and explain when the simpler existing pattern should be reused.

**Acceptance boundary:** Specify an observable expected result for primary action, keyboard/focus recovery, relevant locale/RTL and small-screen conditions and a negative or failure state. Link the selected test to the concept's existing canonical owner instead of introducing an overlapping shared control. A [WCAG 2.2](https://www.w3.org/TR/WCAG22/) reference supports applicable web accessibility criteria but does not verify an implementation, independent review or actual task completion. Unexecuted checks remain **NOT VERIFIED**.

