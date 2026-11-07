# Agent lookup protocol

This repository is a **reference catalog of proposed UI/UX knowledge**, not a shipped component package. Begin with [the canonical registry](catalog/index.json), not a recursive read of all Markdown.

1. Search by exact canonical ID or task: `python3 scripts/find_concept.py "loading button" --json`. For aliases, the resolver ranks exact IDs first, then exact aliases, then title/text. Its ranking is a convenience, not a guarantee that a result fits the task.
2. Read the returned `path` and check `status`, `kind`, `owner`, `reviewed_at`, `use_when` and `avoid_when` where present. `proposed` is not approved or implemented.
3. Follow `related` and `depends_on` canonical IDs only as needed. The registry is the **single** source of identity and retrieval metadata; Markdown pages own guidance and examples.
4. Cite the canonical ID and relative path when using guidance. Distinguish catalog rules from evidence about a target application. Do not claim tested accessibility, production code or benchmarked UX without independent proof.
5. Prefer reuse/extension before creating a new concept. If introducing one, update `catalog/index.json`, the relevant section README, sources/verification, and tests.

**Batch 1 starting points:** [Design principles](foundations/design-principles.md), [tokens and themes](foundations/design-tokens-and-themes.md), [component model](architecture/component-model.md), and [component contracts](architecture/component-contracts.md).

For humans, see [README](README.md). For schema and lookup behavior, see [catalog lookup](catalog/README.md). Validate with `python3 scripts/validate_catalog.py` and `python3 -m unittest discover -s tests -v`.

Do not edit the default branch directly or treat a documentation specification as an executable component.

**Batch 2 starting points:** [Task flows and information architecture](patterns/task-flows-and-information-architecture.md), [interaction states and recovery](patterns/interaction-states-and-recovery.md), [accessibility](guidance/accessibility.md), and [internationalization](guidance/internationalization.md). Example queries: `python3 scripts/find_concept.py 'information architecture' --json`, `python3 scripts/find_concept.py 'network timeout' --json`, `python3 scripts/find_concept.py 'keyboard navigation' --json`, `python3 scripts/find_concept.py 'text expansion' --json`. Validate fit against the canonical page before adopting a result.

**Batch 3 starting points:** [UX measurement](guidance/ux-measurement.md), [catalog lifecycle](governance/lifecycle-and-decisions.md), and [quality gates](governance/quality-gates.md). Example queries: `python3 scripts/find_concept.py 'task completion rate' --json`, `python3 scripts/find_concept.py 'catalog promotion' --json`, `python3 scripts/find_concept.py 'documentation checks' --json`. For measurement, distinguish unknown baselines from zero. For governance, distinguish documentation status from shipped code; use actual test evidence, not assumptions.

**Batch 4 core components:** Search `component.button`, `component.input`, `component.select`, `component.checkbox`, `component.dialog` and `component.field` through the canonical registry; use [component index](components/README.md) for navigation. Read `related` and `depends_on` selectively. All are proposed specification documents without runnable code; the generic [component contract](architecture/component-contracts.md) remains the cross-component rule source.

**Batch 5 composed patterns:** Use `pattern.forms`, `pattern.navigation`, `pattern.search-filter`, `pattern.data-tables` or `pattern.feedback` for an end-to-end composition decision; use [patterns index](patterns/README.md) for links. Prefer these exact IDs to broad search when possible, and inspect component dependencies before implementing anything. A pattern does not authorize application routing, network requests, or claims of tested accessibility.

**Batch 6 retrieval safeguards:** Every entry has `use_when`, `avoid_when`, `related`, `depends_on`, `owner` and nullable `reviewed_at`. Use `python3 scripts/find_concept.py 'role switching' --json --limit 3` and optional `--status`. Search normalizes punctuation, never treats negative `avoid_when` text as a positive recommendation, and returns canonical IDs. Verify task fit in the source file; a high rank is not an approval.

**Batch 7 research discovery:** start with `guidance.ux-research` for method selection and credible evidence, `guidance.journey-mapping` for mental models/task analysis/experience maps, or `guidance.cognitive-load` for comprehension and decision burdens. Do not treat illustrative scenarios as participant research. All remain proposed.

**Batch 8 discovery:** use `guidance.content-design` for labels, microcopy and content lifecycle; use `pattern.forms` for validation timing, save/resume, autofill and multi-step correction; use `pattern.search-filter` for query/facet/sort/no-results/position behavior; use `pattern.service-recovery` only when the task needs cross-channel escalation or service-unavailable guidance. Prefer existing canonical form/search entries to creating duplicates. All guidance is proposed, not verified production behavior.

**Batch 9 trust/resilience discovery:** `guidance.privacy-trust` owns human-facing data choices, consent and transparency; `pattern.authentication-lifecycle` owns sign-in, reauthentication and account recovery; `pattern.notifications-attention` owns event delivery and user attention while `pattern.feedback` remains the component-level status presentation; `pattern.offline-sync` owns local-vs-remote status, queues and conflicts while `pattern.interaction-recovery` remains the generic retry contract. Read context-first [gap ledger](planning/batch-9-context-and-gap-ledger.md). All are proposed and require real product/security/legal validation.

**Batch 10 discovery:** start with `guidance.data-visualization` for dashboard KPI/chart choice, narratives and accessible equivalents; `guidance.mobile-adaptive` for window/platform-specific interaction; `pattern.advanced-interactions` for reordering, command palettes, bulk actions and undo. Reuse `pattern.data-tables` for dense records and `pattern.role-aware-workspaces` for authorized enterprise approvals/delegation. Review [Batch 10 context ledger](planning/batch-10-context-and-gap-ledger.md) and do not treat guidance as shipped mobile, chart or authorization code.

**Batch 11 AI/multimodal discovery:** use `guidance.ai-experiences` for model expectation setting, limits, provenance and correction; `pattern.agentic-actions` for tool plans, human approval, audit/status and bounded external side effects; `pattern.multimodal-conversation` for chat/voice capture, barge-in, transcription correction and non-audio pathways. Reuse existing `guidance.privacy-trust`, `pattern.interaction-recovery`, `pattern.advanced-interactions` and `guidance.accessibility` for their general boundaries. Read [Batch 11 context ledger](planning/batch-11-context-and-gap-ledger.md). Proposed guidelines never grant security permissions or replace real model evaluations.

**Batch 12 evaluation and delivery discovery:** `guidance.performance-experience` owns field/lab performance, loading feedback, task readiness and constrained-device evidence; `guidance.experimentation` owns planned A/B assignment, SRM, guardrails and causal interpretation. `guidance.ux-measurement` remains the canonical definition of task events and denominators. **DesignOps and design-to-code are extensions of existing IDs**: `architecture.component-contracts`, `foundation.design-tokens`, `governance.lifecycle` and `governance.quality`; do not create competing entries. Read [Batch 12 gap ledger](planning/batch-12-context-and-gap-ledger.md). None of this authorizes claims of measured performance, experimental lift, deployed components or accessibility conformance.


## Hosted collaborative-app lookup regression (2026-11-07)

At each new audit batch, re-fetch product evidence and canonical catalog entries before writing. For an app hosted behind managed authentication, retrieve `pattern.authentication-lifecycle` before recommending any new sign-in; retrieve `pattern.role-aware-workspaces` for identity-to-membership and tenant scope; retrieve `pattern.interaction-recovery` for human approvals and ledger feedback; retrieve `pattern.task-flows` for nested project/group context; retrieve `guidance.ux-measurement` and `governance.quality` for metrics and negative-path validation. Existing `pattern.agentic-actions` is specific to AI tool delegation, **not** the canonical guide for ordinary human contribution approvals. Differentiate `source-observed`, `inferred`, `NOT VERIFIED` and `deployment-confirmed`. Never equate this agent instruction package with the separately hosted catalog.


## Batch 6 lookup — persisted collaborative data

For an app with aggregate workspace JSON and revisioned storage, inspect the current data model and migration code before proposing data-lifecycle controls. Retrieve `guidance.privacy-trust` for archive, deletion and export UX; `pattern.offline-sync` for concurrent writes and normalization; `governance.quality` for verification. Do not equate private storage with a backup/restore feature, or a hidden sample group with erased data. See [source ledger](planning/little-wins-batch-6-context-and-gap-ledger.md). No new canonical IDs are needed.


## Batch 7 agent lookup — actionable records and modal flows

Before recommending a table redesign, retrieve `pattern.data-tables`, `component.dialog`, `guidance.accessibility` and `governance.quality`; check source markup for native controls, pseudo-interactive rows, backdrop/close behavior and locally held edits. Test the *whole* record -> dialog -> updated record journey, not just the component shell. Source inspection alone cannot prove accessibility failure or compliance. See [Batch 7 ledger](planning/little-wins-batch-7-context-and-gap-ledger.md).


## Batch 8 lookup — configuration-dependent actions

Before recommending new flags or changing feature navigation, inspect the domain command guards, stored configuration, current UI gating and outstanding historical records. Retrieve `pattern.task-flows` for capability truth tables, `pattern.interaction-recovery` for paused states, and `governance.quality` for all-combination and direct-API verification. A hidden nav item is not a security boundary; an independently stored boolean is not necessarily an independent capability. Review [Batch 8 source ledger](planning/little-wins-batch-8-context-and-gap-ledger.md).


## Batch 9 lookup — incremental migration of existing app UI

Inspect the source's actual import graph, reused and bespoke controls, styling entrypoints and deployed themes before proposing component extraction or global CSS changes. Retrieve `architecture.component-model` for feature-vs-shared boundaries, `foundation.design-tokens` for selector/token migration, and `governance.quality` for staged verification. Installed components, a shadcn configuration or a Tailwind import alone do **not** establish runtime reuse, conformance or migration necessity. Record a one-feature baseline and compatibility/rollback plan before recommending broad changes. See [Batch 9 ledger](planning/little-wins-batch-9-context-and-gap-ledger.md).
