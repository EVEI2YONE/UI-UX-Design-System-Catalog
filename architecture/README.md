# Application and component architecture

The reusable hierarchy is [foundations/tokens → primitives → components → patterns/features → pages/modal flows](component-model.md). Use this as a decision model, not an instruction to create a separate package for every level.

- [Component model](component-model.md): boundaries, examples, and reuse/adapt/create checks.
- [Component contracts](component-contracts.md): anatomy, public API, states, inclusive behavior and verification.

A shared `Dialog` owns focus behavior and an overlay; a feature's account-deletion dialog owns confirmation language, domain data and product telemetry. Related: [interaction states](../patterns/interaction-states-and-recovery.md), [governance](../governance/lifecycle-and-decisions.md).
**For agents:** use `architecture.component-model` for placement/reuse decisions and `architecture.component-contracts` for state/API contracts. Both resolve through [the canonical registry](../catalog/index.json); see [AGENTS.md](../AGENTS.md).


For independent proposed control specifications, see the [core components index](../components/README.md). A component specification is not an implementation or approval to use it without consumer tests.

**Batch 12 handoff:** [Component contracts](component-contracts.md) now require a versioned design-to-code trace, state matrix, token mapping, visual/interaction evidence, affected consumers and rollback. The specification can be reviewed independently from a runtime implementation; a docs-only catalog check never proves a shipped component.


## Batch 9 — incremental component extraction

[Component model](component-model.md) now defines a source inventory and vertical-slice migration from concentrated page orchestration into feature presentation and appropriate shared controls. Review the [Batch 9 context ledger](../planning/little-wins-batch-9-context-and-gap-ledger.md) before presuming installed UI components are in use. Existing [component contracts](component-contracts.md) remain authoritative.

## Application code organization (Batch 13)

Before choosing a feature/domain/package tree, use [application architecture and scalability selection](application-architecture.md) for context-first prototype, MVP, modular-product and multi-app profiles. This is application-level guidance; the existing [component model](component-model.md) remains canonical for UI component placement. Subsequent batches cover module boundaries, migration, and enterprise topology.

## Application scalability guidance — Batches 14–16

- [Module boundaries and developer navigation](module-boundaries-and-developer-navigation.md): feature, domain, shared ownership, one-way imports and task-to-code discoverability.
- [Architecture evolution and fitness](architecture-evolution.md): context-led migration, vertical slices, baseline and rollback.
- [Enterprise and multi-application architecture](enterprise-and-multiapp.md): modular monolith, monorepo, multirepo and microfrontends; team/package governance.

The [per-batch context and gap ledger](../planning/application-architecture-batches-13-16-context-and-gaps.md) records overlap with earlier knowledge and unverified claims. Use canonical registry IDs rather than treating these as runtime libraries.

## Batch 17 — framework-aware application structure

- [Framework-aware application structure and route ownership](framework-aware-application-structure.md): preserve Next.js, Angular and React Router conventions while choosing between route-local and feature-owned UI.

Start with the [Batch 17 context and sources ledger](../planning/application-architecture-batch-17-context-and-gaps.md). Routes and module boundaries are different concerns; verify actual framework/version before applying any tree.

## Batch 18 — enforceable architecture boundaries

- [Architecture enforcement and CI guardrails](architecture-enforcement-and-ci.md): compare scoped ESLint import restrictions, dependency-cruiser path/cycle rules and Nx project tags, with known blind spots and staged CI rollout.

Read the [Batch 18 context and source ledger](../planning/application-architecture-batch-18-context-and-gaps.md). These are illustrative implementation recipes; this documentation repository has no application import graph to validate.
