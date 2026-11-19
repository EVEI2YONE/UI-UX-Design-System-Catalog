# Date and time input

**Kind:** specification · **Status:** proposed · **Primary layer:** components · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and fit

Collect or edit an unambiguous date, time or interval without conflating localized display with an authoritative instant or calendar period.

**Use when:** The user must enter a date/time, choose a slot, or provide a local date combined with a known time zone.

**Avoid when:** A text search or unconstrained freeform field is clearer, or a calendar visualization is unnecessary for entering a known date.

## Ownership and decision rules

The control owns editable fields, labels, calendar/clock picker affordances if present and feedback; the feature owns validation, availability, daylight-saving interpretation and persistence.

- Choose text fields, native date/time inputs, or a picker based on the task, platform, user research and international format expectations.
- Specify calendar date versus local wall time versus timezone-aware instant; never silently guess an offset across DST gaps or repeats.
- For known dates (e.g., birthdate), allow efficient keyboard entry; avoid forcing people to traverse a distant calendar month by month.
- Specify constraints and invalid dates in human terms; do not disable a date without explaining its eligibility when relevant.
- Use locale-formatted display, explicit unambiguous time zones, and server-validated availability for bookable slots.

## States and anatomy

Expose a persistent or programmatically associated name, meaningful control and content slots, visible focus, and semantic token-based visual states; do not invent product-side behavior in the component.

| State | Visible behavior | Semantic / accessibility expectation |
| --- | --- | --- |
| Empty/entered | Known format and labels for day/month/year or date/time | Control names and relationships explicit |
| Picker open | Selected day/time visible; nearby months navigable | Calendar key model documented if custom |
| Invalid/ambiguous | Explain impossible date, DST ambiguity or unavailable slot | Preserve user input and focus |
| Availability loading | Show pending versus confirmed reservation state | No unverified success claim |

## Keyboard, focus and inclusive operation

- Native date/time controls retain platform keyboard and screen reader behavior.
- Custom grid pickers require documented arrow/Home/PageUp/PageDown behavior and focus return.
- Prevent focus trapping in optional popovers and keep an editable alternative when spatial selection is difficult.

Test at narrow widths and high zoom, with long translated labels, mixed LTR/RTL text, available input methods, high contrast and reduced-motion preferences. Use scoped styling and stable semantic design tokens rather than fixed positioning and raw values.

## Example / anti-example

**Illustrative example:** A booking form presents the location time zone, allows keyboard date entry and reconfirms the exact appointment instant.

**Anti-example:** Storing '02:30' without a time zone and treating ambiguous daylight-saving time as a confirmed appointment.

## Evidence and verification

| Scenario | Expected observation | Status |
| --- | --- | --- |
| Locale date ordering, numeric formats and translated month names | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |
| DST transitions, minimum/maximum dates and invalid values | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |
| Keyboard/calendar alternative, zoom and mobile platform behavior | Document browser, device and assistive-technology evidence before adoption | NOT VERIFIED |

The contract is guidance only: no runnable implementation, tested cross-browser interoperability, editorial approval, or WCAG conformance is claimed.

## Sources, limitations and related concepts

- Behavior reference: [platform or WAI guidance](https://www.w3.org/International/quicktips/); confirm edition, browser support and applicability before adopting custom semantics.
- Accessibility target: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), not an assertion of conformance.
- Related canonical sources: [Component contracts](../../../knowledge/architecture/component-contracts.md), [Accessibility](../../../knowledge/guidance/accessibility.md), [Design tokens](../../../knowledge/foundations/design-tokens-and-themes.md), [Interaction recovery](../../patterns/interaction-states-and-recovery.md).

## Decision example and verification boundary

**Illustrative scenario (not a user study):** Enter 01:30 during an autumn DST fallback and choose one explicit offset; reject nonexistent spring times. The consumer owns product data and permissions; the shared specification owns semantic behavior, presentation and focus. Choose simpler native controls where they satisfy the user task.

**Acceptance evidence to collect:** Check locale formats, ambiguous instants, nonexistent time, translated validation and persisted UTC interpretation. Record tool/browser, owner, expected versus observed behavior, locale and unresolved cases; actual runtime results remain **NOT VERIFIED** until executed.

**Source applicability:** [Relevant W3C guidance](https://www.w3.org/International/quicktips/) informs the interaction choices, not production conformance or independent review. Keep implementation-specific details with the consumer.

