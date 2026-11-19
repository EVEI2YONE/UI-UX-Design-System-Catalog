# Visual craftsmanship workflow

A repeatable, evidence-aware way to move from user needs to a polished UI. This describes a design **method**, not a completed product study, software package, or accessibility certification.

## Application context

Use when translating a task brief into layouts, typography, colors, imagery, icons, motion and interactive states. Avoid prescribing an aesthetic before understanding content, platform constraints, user needs and accessibility requirements.

## Design and review sequence

| Step | Practice | Owning guidance | Acceptance evidence |
| --- | --- | --- | --- |
| Understand the task | State the user's goal, operating context, content, constraints and known unknowns | [Task flows](../specifications/patterns/task-flows-and-information-architecture.md), [research methods](../knowledge/guidance/ux-research-methods.md) | Task brief grounded in evidence and explicit assumptions |
| Study references | Record source, licensing, observed traits, inferred intent, context and limitations | [Visual craftsmanship](../knowledge/foundations/visual-design-craftsmanship.md) | Comparable reference cards with rights checks |
| Explore directions | Generate meaningfully different arrangements and visual grammars using the same content | [Visual craftsmanship](../knowledge/foundations/visual-design-craftsmanship.md), [tokens](../knowledge/foundations/design-tokens-and-themes.md) | Alternatives with use/avoid rationale |
| Compose the UI | Establish hierarchy, spacing, type, surfaces, semantic icons and focused calls to action | [Styling recipes](../knowledge/foundations/practical-ui-styling-recipes.md), [icon semantics](../knowledge/foundations/iconography-and-semantics.md) | Responsive layouts, states and token roles |
| Render and inspect | Review real screenshots at identical data, viewport, state and theme conditions | [Quality gates](quality-gates.md) | Observation log and corrected render |
| Validate behavior | Check keyboard, focus, screen reader, contrast, zoom, localization, performance and recovery | [Accessibility](../knowledge/guidance/accessibility.md), [internationalization](../knowledge/guidance/internationalization.md), [interaction recovery](../specifications/patterns/interaction-states-and-recovery.md) | Executed checks and honest unverified boundaries |

## Decision rules

- Keep design intent and verified behavior separate. An attractive screenshot cannot prove comprehension, task completion, screen-reader semantics or security.
- Preserve same content/state conditions when comparing alternatives. Describe the smallest change with plausible benefit, then test it.
- Use source rights and product voice consistently. Do not copy recognizable art direction or brand identity without permission.
- Give priority to functional clarity, data-loss safety, accessibility and trust over decorative polish.
- Maintain clear ownership for design tokens, component behavior, feature state and authoritative outcomes.

## Review prompts

Check focal priority, readable typography, semantic color, whitespace/grouping, responsive layout, truthful feedback, keyboard sequence, error recovery and localized expansion. For a still image, mark interactive and assistive behavior **NOT VERIFIED** until tested on a real implementation.

A reusable review should include artifact/revision, device and viewport, theme, copy/data state, observed issue, severity, relevant concept ID, proposed correction, before/after renders and verification outcomes. Use [synthetic written practice cases](../knowledge/foundations/visual-refinement-examples.md) only as examples, not user research.
