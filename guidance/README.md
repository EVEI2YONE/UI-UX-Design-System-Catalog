# Cross-cutting UX guidance

This section supplies requirements that should be applied to every appropriate foundation, control, pattern and experience.

- [Wireframe methodology and prototype escalation](wireframe-methodology.md): fidelity, decision questions, image limitations and interaction escalation.
- [Accessibility](accessibility.md): inclusive semantic and interaction expectations and evidence.
- [Internationalization](internationalization.md): translation, formatting, long strings and bidirectional layouts.
- [UX measurement](ux-measurement.md): behavioral and attitudinal outcomes, cohorts and privacy.
- [UX research methods and evidence](ux-research-methods.md): select studies, recruit ethically, distinguish observations and hypotheses.
- [Mental models and journey mapping](mental-models-and-journeys.md): task analysis, experience maps and service blueprints.
- [Cognitive load and decision design](cognitive-load-and-decisions.md): memory, attention and meaningful choices.
- [Content design and UX writing](content-design-and-ux-writing.md): user-needs-first language, error microcopy, labels, content lifecycle.
- [Privacy, consent and trustworthy UX](privacy-consent-and-trust.md): purpose-limited data use, meaningful choice, consent and deletion states.
- [Data visualization and dashboards](data-visualization-and-dashboards.md): task-driven chart choices, honest scales and accessible summaries.
- [Mobile and adaptive platform UX](mobile-and-adaptive-platform-ux.md): adaptive windows, safe areas, native patterns and equivalent inputs.
- [AI-powered experiences, transparency and calibrated trust](ai-powered-experiences-and-trust.md): AI limits, provenance, uncertainty, correction and manual control.
- [Performance, perceived speed and resilient task feedback](performance-and-perceived-speed.md): Core Web Vitals, real-user vs lab data, task readiness and safe pending states.
- [UX experimentation and causal evidence](experimentation-and-causal-evidence.md): preplanned A/B tests, assignment, SRM, guardrails and credible interpretation.

Also see [quality gates](../governance/quality-gates.md) and [sources](../governance/references.md).

**Wireframing lookup:** start with `guidance.wireframe-methodology` for fidelity and static/prototype decisions; follow `pattern.task-flows` for screen composition and `governance.quality` for evidence gates.

**Agent retrieval:** `guidance.accessibility` covers semantics, keyboard, focus and verification; `guidance.internationalization` covers locale formatting, translation growth and RTL. Both are cross-cutting and should be checked against the product's actual supported platforms/locales. Locate canonical paths and lifecycle status in [the registry](../catalog/index.json) or follow the [agent protocol](../AGENTS.md).


**Measurement lookup:** use `guidance.ux-measurement` when defining task success, cohort/denominator, funnel abandonment or survey interpretation. Follow `related` references to the relevant task journey and quality gates. See the [registry](../catalog/index.json) for canonical metadata; missing baselines remain unknown.

**Batch 7 discovery:** `guidance.ux-research`, `guidance.journey-mapping`, and `guidance.cognitive-load` are proposed guidelines. Review the method limits and real-user evidence before using them as design authority.

**Batch 8 discovery:** `guidance.content-design` covers task language and content governance. Use `pattern.forms` and `pattern.search-filter` for the actual interaction composition; `pattern.service-recovery` owns cross-channel support handoffs. All entries remain proposed and untested in a live product.

**Batch 9 discovery:** use `guidance.privacy-trust` for user-facing privacy choices; follow `pattern.authentication-lifecycle`, `pattern.notifications-attention`, or `pattern.offline-sync` for task-specific decisions. These are proposed practices, not legal or security certification.

**Batch 10 discovery:** `guidance.data-visualization` owns chart and KPI narratives; `guidance.mobile-adaptive` owns cross-platform adaptation. The [data tables](../patterns/data-tables.md) and [advanced interactions](../patterns/advanced-interactions-and-reversible-actions.md) entries own record and complex-command behavior.

**Batch 11 discovery:** `guidance.ai-experiences` addresses generated-output trust and evidence. For side-effecting AI tools, use `pattern.agentic-actions`; for voice/chat and modality switching, use `pattern.multimodal-conversation`. All remain proposed.

**Batch 12 discovery:** `guidance.performance-experience` owns perceived/operational performance; `guidance.experimentation` owns controlled comparisons and validity. Continue to use `guidance.ux-measurement` for underlying task events/denominators, and existing [quality gates](../governance/quality-gates.md) for implementation evidence.


## Batch 6 — persisted data lifecycle

[Privacy, consent and trustworthy UX](privacy-consent-and-trust.md) now includes archival, versioned export, retention and correction-history expectations. For synchronization and migration mechanics, follow [offline/sync and conflict recovery](../patterns/offline-sync-and-conflicts.md), with [quality gates](../governance/quality-gates.md) for evidence. These are proposed designs, not verified product capabilities.


## Batch 7 — integrated accessibility tasks

[Accessibility guidance](accessibility.md) now includes record-to-dialog-to-updated-list journey verification and explicit source-observed versus actually tested claims. Pair [table actions](../patterns/data-tables.md) with [dialog focus behavior](../components/dialog/spec.md).

**Wireframe Batch 4 discovery:** use `guidance.mobile-adaptive` for viewport and pane transformations, `guidance.accessibility` for intended zoom/focus/reading-order coverage, and `guidance.internationalization` for text expansion, RTL and mixed-direction content. Static imagery remains a review artifact, not runtime conformance evidence.

## B04 — interaction-effort measurement (proposed, 2026-11-07)

[UX measurement](ux-measurement.md) now includes CKG-14: task-specific pointer travel, focus/keyboard effort, re-entry, target relocations and time to next eligible action, always interpreted alongside task success, errors, safety and privacy. Use canonical ID `guidance.ux-measurement`; the documentation provides no measured product baseline.
