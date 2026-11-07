# Patterns and experiences

Patterns explain how multiple components support a task in context. Pages and user journeys are composed experiences, not replacements for reusable controls.

- [Task flows and information architecture](task-flows-and-information-architecture.md): navigation, task-to-screen composition, meaningful structural wireframe alternatives and comparison, progressive disclosure and wayfinding.
- [Role-aware workspaces and context switching](role-aware-workspaces-and-context-switching.md): multiple authorized roles, workspace routing, customer previews, privileged impersonation boundaries.
- [Interaction states and recovery](interaction-states-and-recovery.md): loading, empty, error, offline, destructive actions, retry and focus recovery.

Related: [design principles](../foundations/design-principles.md), [accessibility](../guidance/accessibility.md), [measurement](../guidance/ux-measurement.md).

**Agent retrieval:** use `pattern.task-flows` for task/navigation design and `pattern.interaction-recovery` for error, pending and retry behavior. Read their canonical paths from [the registry](../catalog/index.json); follow `related` IDs for accessibility and metrics only as relevant. See [AGENTS.md](../AGENTS.md).

## Batch 5 composed patterns

These are **proposed composition specifications**, not runtime implementations. Start with the canonical IDs in [the registry](../catalog/index.json), then follow dependency contracts.

- [Form composition and validation](forms.md) — `pattern.forms`, fields, validation, async submit and recovery
- [Navigation and wayfinding](navigation.md) — `pattern.navigation`, active routes, landmarks, deep links and keyboard menus
- [Search and filtering](search-and-filter.md) — `pattern.search-filter`, queries, selected filters, no-results and failed requests
- [Data tables and collection actions](data-tables.md) — `pattern.data-tables`, semantics, sorting, selection and pagination
- [Feedback and status messaging](feedback.md) — `pattern.feedback`, banners, inline status, transient notices and announcements
- [Service recovery and support handoff](service-recovery-and-support.md) — `pattern.service-recovery`, escalations, outages, case status and resuming tasks
- [Authentication and account lifecycle](authentication-and-account-lifecycle.md) — `pattern.authentication-lifecycle`, sign-in, MFA, sessions and recovery
- [Notifications and attention management](notifications-and-attention.md) — `pattern.notifications-attention`, event priority, delivery choices and permissions
- [Offline work and synchronization](offline-sync-and-conflicts.md) — `pattern.offline-sync`, local drafts, queue status and conflicting edits
- [Advanced interactions and reversible actions](advanced-interactions-and-reversible-actions.md) — `pattern.advanced-interactions`, accessible reorder, bulk scope, command shortcuts and undo
- [Agentic actions, approvals and reversible workflows](agentic-actions-and-approvals.md) — `pattern.agentic-actions`, scoped tools, reviewable plans, approvals and verified outcomes
- [Conversational, voice and multimodal UX](conversational-voice-and-multimodal-ux.md) — `pattern.multimodal-conversation`, turn taking, transcript correction, voice and accessible alternatives

Use the existing [task-flow](task-flows-and-information-architecture.md) and [interaction-recovery](interaction-states-and-recovery.md) guidance as the shared decision layer rather than copying it into every pattern.

**Batch 8 extension:** [Forms](forms.md) now describes data collection, validation timing, multi-step forms, review, autosave, autofill and error handling; [search/filtering](search-and-filter.md) covers discovery strategy, facets, sorting, pagination and no-result/error distinction. Use [content design](../guidance/content-design-and-ux-writing.md) for copy standards; these are documentation patterns, not implemented controls.

**Batch 9 boundary:** [role-aware workspaces](role-aware-workspaces-and-context-switching.md) remains the authoritative pattern for *authorized* role/tenant context, [feedback](feedback.md) for inline/toast presentation, and [interaction recovery](interaction-states-and-recovery.md) for generic timeout/retry states. The new pages address separate lifecycle, channel and synchronization concerns.

**Batch 10 extensions:** [Data tables](data-tables.md) now distinguishes read-only tables from interactive grids and defines bulk operations. [Role-aware workspaces](role-aware-workspaces-and-context-switching.md) now includes enterprise approvals, delegation and authorized audit visibility. For charts see [data visualization](../guidance/data-visualization-and-dashboards.md), and for mobile behavior see [adaptive platform UX](../guidance/mobile-and-adaptive-platform-ux.md).

**Batch 11 boundary:** AI disclosure, source provenance and uncertainty live under [AI experience guidance](../guidance/ai-powered-experiences-and-trust.md). [Agentic actions](agentic-actions-and-approvals.md) governs AI-specific tool approval and action states rather than replacing [advanced interactions](advanced-interactions-and-reversible-actions.md) or [role-aware workspaces](role-aware-workspaces-and-context-switching.md). [Voice and multimodal UX](conversational-voice-and-multimodal-ux.md) uses existing accessibility, content and privacy contracts.


## Little Wins context-first extensions (2026-11-07)

For hosted identity and managed-profile boundaries use [authentication](authentication-and-account-lifecycle.md) plus [role-aware workspaces](role-aware-workspaces-and-context-switching.md). For **human** submission reviews, value changes and irreversible history use [interaction recovery](interaction-states-and-recovery.md); AI agent approvals remain a separate pattern. For group/project scope and independently toggled features use [task flows](task-flows-and-information-architecture.md). All extensions remain proposed and require runtime-specific verification.


## Batch 6 — versioned workspace migration

[Offline work and synchronization](offline-sync-and-conflicts.md) now distinguishes safe read-time normalization from durable migration, backup, import/restore, version conflicts and aggregate contention. See [privacy lifecycle](../guidance/privacy-consent-and-trust.md) for archive/retention/export UX, and [Batch 6 context ledger](../archive/planning/little-wins-batch-6-context-and-gap-ledger.md) for the Little Wins source basis.


## Batch 7 — record actions and dialog continuity

[Data tables](data-tables.md) now gives an explicit native action-cell control versus clickable-row decision. Combine with the [Dialog contract](../components/dialog/spec.md) and [accessibility journey criteria](../guidance/accessibility.md), rather than treating a keyboard-focusable `<tr>` as a full grid. [Batch 7 ledger](../archive/planning/little-wins-batch-7-context-and-gap-ledger.md) records the source context.


## Batch 8 — configuration and capability dependencies

[Task flows](task-flows-and-information-architecture.md) now distinguishes independently stored feature flags from dependent user capabilities and requires an explicit configuration/action matrix. [Interaction recovery](interaction-states-and-recovery.md) covers paused-feature transitions and pending work. Review the [Batch 8 evidence ledger](../archive/planning/little-wins-batch-8-context-and-gap-ledger.md) before drawing conclusions about any particular application.

## Account and settings knowledge batches

- [Account and settings portal](account-and-settings-portal.md) — `pattern.account-settings-portal`; IA, profile/contact verification, effective save states, concurrent edits and data export. Follow existing canonical identity, privacy and form guidance.
- [Billing and subscription settings](billing-and-subscription-settings.md) — `pattern.billing-subscription-settings`; payment methods, renewal, downgrade/cancellation and invoice access. Payment and legal outcomes require real product verification.
- [Batch progress and gap disposition](../archive/planning/account-settings-batch-progress.md) — three context-first batches, same PR, with known scope boundaries.

**Wireframe Batch 2:** retrieve `pattern.task-flows` for screen sequence and alternatives; `principle.visual-hierarchy` for within-screen priority; `guidance.wireframe-methodology` for fidelity and interactive-prototype escalation. All content is proposed; illustrated screens do not establish implementation.

**Wireframe Batch 3:** use [interaction states and recovery](interaction-states-and-recovery.md) (`pattern.interaction-recovery`) to inventory and annotate applicable ready, empty, loading, validation, error, permission, success and retry states. Mark a still image as intended design rather than verified transition behavior. Use [wireframe methodology](../guidance/wireframe-methodology.md) for interaction escalation and existing forms/feedback/offline concepts for specialized details.

**Settings knowledge Batch 1 (cumulative draft):** [Account and settings portal](account-and-settings-portal.md#workspace-configuration-foundation--settings-knowledge-batch-1-proposed-2026-11-07) now includes a per-setting registry, scope/authority checks, and save/propagation/recovery contract. Do not duplicate canonical form, conflict, or authorization patterns. Product implementation and manual checks remain NOT VERIFIED.
