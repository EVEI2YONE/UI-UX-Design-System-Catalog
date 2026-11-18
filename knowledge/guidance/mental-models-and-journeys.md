# Mental models and journey mapping

**Kind:** guideline · **Status:** proposed · **Primary layer:** context

## Purpose

Understand users' expectations, goals and end-to-end experiences **before** deciding page navigation or interaction components. A **mental model** is a person's belief about how a system works; a **task analysis** breaks down actions toward a goal; a **journey map** describes an experience across stages/touchpoints; a **service blueprint** adds the backstage people/process dependencies. These are complementary, not interchangeable.

## When to use / avoid

- **Use when:** navigation labels conflict with user vocabulary, multi-step tasks span teams/channels, users are confused about system behavior, or redesign proposals assume an untested “typical user.”
- **Avoid when:** creating decorative personas or map posters that never influence a decision, collapsing substantively different user groups into one fabricated average, or treating hypothetical workshops as observed journeys.

## Discovery and mapping decisions

1. Identify the user **goal** (e.g., “receive a replacement card”), separate from the interface **task** (“submit a form”).
2. Interview or observe people in relevant situations. Record their vocabulary, predictions, fallback behaviors, use of other channels and actual steps.
3. Choose an artifact deliberately:
   - **Mental-model notes** for users' expectations, concepts and mismatches with the product's model.
   - **Task analysis** for actions, prerequisites, alternative paths, exception branches and cognitive/physical demands.
   - **Journey/experience map** for stages across time and touchpoints, including needs, emotions and friction.
   - **Service blueprint** only when backstage support, organizational handoffs or policies meaningfully affect the journey.
4. Decide **current-state vs future-state**, and **evidence-first vs assumption-first**. Label assumptions until tested; keep ideal-state promises separate from current observations.
5. Segment when users differ by role, access needs, frequency, language or task context; avoid false precision about how common a path is.
6. Link the map to design decisions, owners, open questions and the [task-flow specification](../patterns/task-flows-and-information-architecture.md).

## A reusable map contract

| Stage | User goal / mental model | Observed actions | Touchpoint | Friction / evidence | Opportunity + owner |
| --- | --- | --- | --- | --- | --- |
| Discover | “Where should I start?” | Enters help or account page | Search, mobile, support | P1 reports unfamiliar label [hypothetical] | Test clearer navigation term |
| Decide | “Will this change my account?” | Reads instructions | Form and policy text | Decision anxiety [hypothetical] | Clarify consequence and data use |
| Complete | “Was it saved?” | Submits and waits | Product and email | Missing confirmation [hypothetical] | Persistent status + reliable resume |
| Recover | “What if something fails?” | Retries or calls support | Product, support | Failed recovery [hypothetical] | Preserve entered data and escalation |

The table is **illustrative, not participant data**. A real map must preserve traceable anonymized observation IDs and avoid unsupported emotional narratives.

## Mental-model mismatch example

- **Observed expectation to test:** People think an “Archive” action hides an item without deleting it.
- **Possible interface mismatch:** The action actually irreversibly deletes data.
- **Design decision:** Do not merely rename a destructive operation; verify semantics, provide explicit consequence and a safer recovery/confirmation flow.
- **Acceptance:** Representative participants can predict outcomes before acting and recover appropriately; test via scenario tasks rather than a team vote.

**Anti-example:** Generate a persona named “Busy Brenda,” invent her needs and preferences, then use that fiction as proof that no search function is needed.

## Verification and inclusion

- Record sources for each stage (observations, interviews, existing analytics or assumptions), study date, participant context, exclusions, conflicts and confidence.
- Verify maps with users where feasible, including people with relevant assistive technologies, novice and expert cohorts, different languages and constrained-device contexts.
- Assess the steps that cross devices, sessions, organizations or access-control boundaries; preserve consent, focus, translated content, deep links and task context.
- Tie the map to a specific decision: [navigation](../patterns/navigation.md), [interaction recovery](../patterns/interaction-states-and-recovery.md), or [UX measurement](ux-measurement.md).
- **Real-user mapping, task analysis and validation:** NOT VERIFIED for this proposed catalog entry.

## Sources and related concepts

- [Nielsen Norman Group, Mental Models](https://www.nngroup.com/articles/mental-models/) (2024; reviewed September 2026): definition and design mismatch; professional guidance.
- [Nielsen Norman Group, Task Analysis](https://www.nngroup.com/articles/task-analysis/) (2020): user goals, observations and task decomposition; method primer.
- [GOV.UK, Creating an experience map](https://www.gov.uk/service-manual/user-research/creating-an-experience-map) (2017; consulted 2026-11-07): evidence-based experience mapping in complex services; not a universal prescribed format.
- [Nielsen Norman Group, Journey-Mapping Approaches](https://www.nngroup.com/articles/journey-mapping-approaches/) (2020): current/future and assumption/research first decisions.

**Canonical ID:** `guidance.journey-mapping` · **Owner:** unassigned · **Last human review:** none; proposed on 2026-11-07.  
**Related:** [research methods](ux-research-methods.md), [task flows](../patterns/task-flows-and-information-architecture.md), [design principles](../foundations/design-principles.md), [UX measurement](ux-measurement.md).
