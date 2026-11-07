# Component architecture

The reusable hierarchy is [foundations/tokens → primitives → components → patterns/features → pages/modal flows](component-model.md). Use this as a decision model, not an instruction to create a separate package for every level.

- [Component model](component-model.md): boundaries, examples, and reuse/adapt/create checks.
- [Component contracts](component-contracts.md): anatomy, public API, states, inclusive behavior and verification.

A shared `Dialog` owns focus behavior and an overlay; a feature's account-deletion dialog owns confirmation language, domain data and product telemetry. Related: [interaction states](../patterns/interaction-states-and-recovery.md), [governance](../governance/lifecycle-and-decisions.md).