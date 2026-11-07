# Governance and evidence

The catalog needs stable identity, accountable decisions, evidence and planned deprecation—not unreviewed accumulation.

- [Lifecycle and decisions](lifecycle-and-decisions.md): reuse/extend/create/merge/deprecate, ownership, review status and version notes.
- [Quality gates](quality-gates.md): contract completeness, accessibility, localization, responsive, token, testing and catalog checks.
- [References](references.md): authoritative standards starting points and source status.

For changes see [Contributing](../CONTRIBUTING.md) and the [PR template](../.github/pull_request_template.md).

**Agent retrieval:** use `governance.lifecycle` for reuse decisions, ownership, promotion or deprecation; use `governance.quality` for evidence, review and release checks. Their canonical IDs, lifecycle statuses and references live in the [registry](../catalog/index.json). Documentation checks are not proof of a production component or accessible UX. See [AGENTS.md](../AGENTS.md).

**Batch 12 DesignOps delivery:** reuse [lifecycle and decisions](lifecycle-and-decisions.md) for ownership/versioning, [quality gates](quality-gates.md) for release evidence, [component contracts](../architecture/component-contracts.md) for design-to-code handoff, and [design tokens](../foundations/design-tokens-and-themes.md) for DTCG interchange. No parallel governance ID is created. See [Batch 12 context and gap audit](../archive/planning/batch-12-context-and-gap-ledger.md).


## Hosted-app assurance extension (2026-11-07)

[Quality gates](quality-gates.md) now describe deployment identity boundary checks, tenant authorization, transactional replay and concurrency, draft recovery, browser accessibility, and negative API tests. A passing isolated domain suite is not equivalent to a production integration test. Checks not run remain **NOT VERIFIED**.


## Batch 6 — data lifecycle validation

[Quality gates](quality-gates.md) now defines export/retention, legacy migration, read-side effects, backup/restore and aggregate concurrency acceptance scenarios. The [Batch 6 evidence ledger](../archive/planning/little-wins-batch-6-context-and-gap-ledger.md) distinguishes source observations and unverified deployment requirements.


## Batch 7 — table-to-dialog regression checks

[Quality gates](quality-gates.md) include native action semantics, focus lifecycle, unsaved-draft cancellation and post-review focus fallback. Evidence is recorded in [Batch 7 context ledger](../archive/planning/little-wins-batch-7-context-and-gap-ledger.md); runtime tests remain NOT VERIFIED.


## Batch 8 — feature dependency validation

[Quality gates](quality-gates.md) now checks flag-combination coverage, server versus UI capability agreement, historical preservation, outstanding requests and toggle races. [Batch 8 evidence ledger](../archive/planning/little-wins-batch-8-context-and-gap-ledger.md) separates code-observed facts from deployment tests.


## Batch 9 — refactor safety evidence

[Quality gates](quality-gates.md) now checks existing component adoption, public compatibility, staged CSS/token migration, vertical-slice regressions and rollback before calling an app modernization successful. [Batch 9 evidence](../archive/planning/little-wins-batch-9-context-and-gap-ledger.md) is a source audit, not product test evidence.


## Batch 10 — final cumulative coverage audit

The [Batch 10 ledger](../archive/planning/little-wins-batch-10-context-and-gap-ledger.md) maps Batches 1–10 to canonical IDs, evidence and outstanding product verification. Registry lookup [regression tests](../tests/test_little_wins_knowledge_coverage.py) cover ambiguous human-versus-agent approval and other task queries; the full catalog validator remains the source of documentation-integrity results.

**Wireframe Batch 5:** [Quality gates](quality-gates.md) (`governance.quality`) now owns visual inspection of rendered wireframe imagery, including legibility, clipping, source-copy accuracy, hierarchy, invented capabilities and artifact-specific issue logs. This does not establish runtime or WCAG conformance; see [wireframe methodology](../guidance/wireframe-methodology.md) for prototype escalation.
