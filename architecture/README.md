# Application and component architecture

Choose the **developer task first**, then read its canonical guidance. This section concerns both application-code boundaries and reusable UI component contracts; these are different decisions. All catalog entries are proposed knowledge, not installed component libraries or verified app refactors.

## Find the right architecture guidance

| I need to... | Canonical guidance |
| --- | --- |
| Choose a prototype, MVP, modular product or enterprise file structure | [Application architecture selection](application-architecture.md) (`architecture.application-selection`) |
| Place feature, domain, shared UI code and public module APIs | [Module boundaries and developer navigation](module-boundaries-and-developer-navigation.md) (`architecture.module-boundaries`) |
| Preserve Next.js, Angular or React Router route conventions | [Framework-aware structure](framework-aware-application-structure.md) (`architecture.framework-aware`) |
| Compare modular monolith, monorepo, multirepo and microfrontends | [Enterprise and multi-application architecture](enterprise-and-multiapp.md) (`architecture.enterprise-multiapp`) |
| Migrate incrementally or measure architectural fitness | [Architecture evolution](architecture-evolution.md) (`architecture.evolution`) |
| Enforce imports, module boundaries and cycles in CI | [Architecture enforcement](architecture-enforcement-and-ci.md) (`architecture.enforcement-ci`) |
| See prototype/MVP/enterprise before-and-after code placement | [Reference examples](application-architecture-reference-examples.md) (`architecture.reference-examples`) |
| Decide primitive vs component vs task-specific feature | [Component model](component-model.md) (`architecture.component-model`) |
| Define component API, states, semantics and tests | [Component contracts](component-contracts.md) (`architecture.component-contracts`) |

**Fast path:** select an [architecture profile](application-architecture.md) → assign [module owners](module-boundaries-and-developer-navigation.md) → inspect [framework conventions](framework-aware-application-structure.md) → consult [examples](application-architecture-reference-examples.md). Use [enterprise topology](enterprise-and-multiapp.md), [migration](architecture-evolution.md) and [enforcement](architecture-enforcement-and-ci.md) only when the actual task needs them.

**Component versus application boundary:** the [component model](component-model.md) owns reusable component tiers (foundations/tokens → primitives → components → patterns/features → pages/modal flows). A shared `Dialog` owns keyboard and focus semantics, while an account-deletion flow owns its user-facing confirmation, authorization, mutation and telemetry. See [interaction recovery](../patterns/interaction-states-and-recovery.md) and [lifecycle governance](../governance/lifecycle-and-decisions.md). [Core control specifications](../components/README.md) are not runtime implementations.

## Source and verification context

- [Batches 13–16: selection, modules, migration, enterprise](../planning/application-architecture-batches-13-16-context-and-gaps.md)
- [Batch 17: framework routing](../planning/application-architecture-batch-17-context-and-gaps.md)
- [Batch 18: enforcement and CI](../planning/application-architecture-batch-18-context-and-gaps.md)
- [Batch 19: applied examples](../planning/application-architecture-batch-19-context-and-gaps.md)
- [Batch 20: final coverage audit and unresolved evidence](../planning/application-architecture-batch-20-closure-audit.md)
- Earlier work: [Batch 9 component extraction context](../planning/little-wins-batch-9-context-and-gap-ledger.md); Batch 12 component design-to-code trace is documented in [component contracts](component-contracts.md).

For agent retrieval, resolve canonical IDs using [the registry](../catalog/index.json) and [AGENTS.md](../AGENTS.md), then follow `related` and `depends_on` selectively. The [quality gates](../governance/quality-gates.md) distinguish documentation validation from tested accessibility, DX and application behavior. No runtime test can be marked PASS because a Markdown validator succeeded.
