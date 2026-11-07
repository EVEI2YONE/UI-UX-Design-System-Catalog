# Governance and evidence

The catalog needs stable identity, accountable decisions, evidence and planned deprecation—not unreviewed accumulation.

- [Lifecycle and decisions](lifecycle-and-decisions.md): reuse/extend/create/merge/deprecate, ownership, review status and version notes.
- [Quality gates](quality-gates.md): contract completeness, accessibility, localization, responsive, token, testing and catalog checks.
- [References](references.md): authoritative standards starting points and source status.

For changes see [Contributing](../CONTRIBUTING.md) and the [PR template](../.github/pull_request_template.md).

**Agent retrieval:** use `governance.lifecycle` for reuse decisions, ownership, promotion or deprecation; use `governance.quality` for evidence, review and release checks. Their canonical IDs, lifecycle statuses and references live in the [registry](../catalog/index.json). Documentation checks are not proof of a production component or accessible UX. See [AGENTS.md](../AGENTS.md).

**Batch 12 DesignOps delivery:** reuse [lifecycle and decisions](lifecycle-and-decisions.md) for ownership/versioning, [quality gates](quality-gates.md) for release evidence, [component contracts](../architecture/component-contracts.md) for design-to-code handoff, and [design tokens](../foundations/design-tokens-and-themes.md) for DTCG interchange. No parallel governance ID is created. See [Batch 12 context and gap audit](../planning/batch-12-context-and-gap-ledger.md).
