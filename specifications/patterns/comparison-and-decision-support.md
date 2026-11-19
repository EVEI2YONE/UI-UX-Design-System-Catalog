# Comparison and decision support

**Kind:** specification · **Status:** proposed · **Primary layer:** experiences · **Owner:** unassigned · **Review:** NOT VERIFIED

## Purpose and boundaries

Help people make informed choices between offerings or configurations using consistent criteria, interpretable tradeoffs and accessible explanations.

**Use when:** Two or more meaningful alternatives have multiple criteria and users need to understand consequences rather than simply choose the most visually prominent option.

**Avoid when:** A simple mutually exclusive choice is clear with Radio Group; a data table already supports factual inspection with no additional decision support.

**Ownership:** The pattern owns comparison structure, transparent explanation and selection/confirmation. Product owners provide current facts, eligible options, policy and outcome.

## Journey and state contract

| Stage | User-visible decisions and states | Recovery / evidence requirement |
| --- | --- | --- |
| Frame decision | State the user goal, alternatives and relevant constraints | Do not substitute sales rankings for eligibility |
| Compare | Keep aligned criteria, units, dates and limitations | Accessible values independent of color |
| Explore tradeoffs | Allow relevant filters and explanation of material differences | No hidden material negatives |
| Choose | Identify selected option and consequences | Permission and irreversible impacts explicit |
| Reconsider | Support changes, opt-out or revision where possible | No manipulative urgency |

## Design decisions

- Use comparable fields with consistent denominators, time windows and units; mark missing data explicitly rather than inventing zeroes.
- Prioritize criteria from user needs; do not make the sponsor-preferred option appear objectively best without evidence.
- Allow side-by-side reading but provide a narrow-screen sequential comparison that preserves labels and values.
- If recommendations or scoring are used, explain what is optimized and what evidence limits the claim.
- Keep accessibility needs, long translated labels, currency/date differences and decision errors in the verification plan.

## Inclusive operation, content, theming and locale

Provide keyboard and assistive-technology routes through each stage, visible headings and state feedback, and deliberate focus restoration after context changes. Support zoom/reflow, localized labels and units, RTL and high-contrast themes, touch alternatives and reduced motion. Use semantic tokens and make unavailable or irreversible outcomes understandable beyond color. Never treat a mock preview as proof of a real service outcome.

## Example and anti-example

**Illustrative example:** A service plan comparison shows total annual cost, renewal policy, feature limits and data restrictions with aligned, labeled rows.

**Anti-example:** A featured plan is highlighted as 'Most suitable' with hidden recurring costs and no criteria for the recommendation.

## Verification and research handoff

| Scenario | Expected evidence | Current status |
| --- | --- | --- |
| Decision comprehension and criterion comparability | Record actual observed result, relevant cohort and environment | NOT VERIFIED |
| Narrow-screen responsive comparison and missing-data transparency | Record actual observed result, relevant cohort and environment | NOT VERIFIED |
| Keyboard, screen reader header relationships, locale units, anti-manipulation review | Record actual observed result, relevant cohort and environment | NOT VERIFIED |

Measure task completion, user error severity, abandonment and comprehension before asserting improvement. No baseline study, real back-end behavior or accessibility conformance is supplied by this concept.

## Sources, related concepts and limitations

- [GOV.UK patterns](https://design-system.service.gov.uk/patterns/) — contextual reference, not a universal implementation prescription.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — contextual reference, not a universal implementation prescription.
- Related canonical guidance: [Task flows](task-flows-and-information-architecture.md), [Forms](forms.md), [Interaction recovery](interaction-states-and-recovery.md), [Accessibility](../../knowledge/guidance/accessibility.md), and [UX measurement](../../knowledge/guidance/ux-measurement.md).
- Review domain, locale, security, legal and service constraints separately before adoption.
