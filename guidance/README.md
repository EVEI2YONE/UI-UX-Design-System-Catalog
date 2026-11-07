# Cross-cutting UX guidance

This section supplies requirements that should be applied to every appropriate foundation, control, pattern and experience.

- [Accessibility](accessibility.md): inclusive semantic and interaction expectations and evidence.
- [Internationalization](internationalization.md): translation, formatting, long strings and bidirectional layouts.
- [UX measurement](ux-measurement.md): behavioral and attitudinal outcomes, cohorts and privacy.

Also see [quality gates](../governance/quality-gates.md) and [sources](../governance/references.md).

**Agent retrieval:** `guidance.accessibility` covers semantics, keyboard, focus and verification; `guidance.internationalization` covers locale formatting, translation growth and RTL. Both are cross-cutting and should be checked against the product's actual supported platforms/locales. Locate canonical paths and lifecycle status in [the registry](../catalog/index.json) or follow the [agent protocol](../AGENTS.md).


**Measurement lookup:** use `guidance.ux-measurement` when defining task success, cohort/denominator, funnel abandonment or survey interpretation. Follow `related` references to the relevant task journey and quality gates. See the [registry](../catalog/index.json) for canonical metadata; missing baselines remain unknown.
