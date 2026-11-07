# Component architecture

The reusable hierarchy is [foundations/tokens → primitives → components → patterns/features → pages/modal flows](component-model.md). Use this as a decision model, not an instruction to create a separate package for every level.

- [Component model](component-model.md): boundaries, examples, and reuse/adapt/create checks.
- [Component contracts](component-contracts.md): anatomy, public API, states, inclusive behavior and verification.

A shared `Dialog` owns focus behavior and an overlay; a feature's account-deletion dialog owns confirmation language, domain data and product telemetry. Related: [interaction states](../patterns/interaction-states-and-recovery.md), [governance](../governance/lifecycle-and-decisions.md).
**For agents:** use `architecture.component-model` for placement/reuse decisions and `architecture.component-contracts` for state/API contracts. Both resolve through [the canonical registry](../catalog/index.json); see [AGENTS.md](../AGENTS.md).


For independent proposed control specifications, see the [core components index](../components/README.md). A component specification is not an implementation or approval to use it without consumer tests.

**Batch 12 handoff:** [Component contracts](component-contracts.md) now require a versioned design-to-code trace, state matrix, token mapping, visual/interaction evidence, affected consumers and rollback. The specification can be reviewed independently from a runtime implementation; a docs-only catalog check never proves a shipped component.


## Batch 9 — incremental component extraction

[Component model](component-model.md) now defines a source inventory and vertical-slice migration from concentrated page orchestration into feature presentation and appropriate shared controls. Review the [Batch 9 context ledger](../planning/little-wins-batch-9-context-and-gap-ledger.md) before presuming installed UI components are in use. Existing [component contracts](component-contracts.md) remain authoritative.
