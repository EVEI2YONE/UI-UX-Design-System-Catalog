# Application architecture and scalability selection

**Kind:** guideline · **Status:** proposed · **Primary layer:** cross-cutting · **Owner:** unassigned · **Review:** pending

## Purpose and boundaries

Select the least complex application source organization that supports user journeys, code ownership, discoverability and expected change. This document concerns *application code*, not the UI catalog's directory structure, and complements [component placement](component-model.md). Profiles are starting points, not mandatory progression stages. Repository size or engineer count alone does not justify a migration.

## Context-first assessment

Before recommending an architecture, record: repository URL and pinned revision; runtime/framework and routing model; one or several apps; key user journeys; team and release ownership; current source tree, import graph and duplication; shared domain rules; build/test and deployment boundaries; accessibility/i18n needs; observed change friction, and unknown evidence. Do not assume React, Next.js, microfrontends or monorepos.

| Signal | Lightweight choice | Stronger boundary justified when |
| --- | --- | --- |
| Features | Few volatile screens | Cohesive workflows have distinct ownership or frequent change |
| Repetition | A few local components | Same semantics/states recur with proven consumers |
| Business rules | Screen-local logic | Invariants span several workflows |
| Contributors | Coordinated changes | Cross-team changes and collisions recur |
| Delivery | One deployable | Applications need materially different release/toolchain lifecycles |
| Dependencies | Readable direct imports | Cycles and deep cross-feature imports recur |

## Four adaptable reference profiles

These are **illustrative TypeScript/web layouts**, not framework-specific mandates. Native/mobile/backend stacks should map the same ownership rules to their conventions.

### A. Prototype or exploration
```text
src/
  screens/
  components/
  lib/
  styles/
```
Use when the experience and technical assumptions are still changing. Colocate simple screen-specific behavior; extract shared code only for genuine repetition. Avoid a speculative domain layer, package hierarchy or several empty directories. Preserve accessible semantics and data-safety even in a prototype.

### B. MVP or focused product
```text
src/
  app/                  # composition, routes and providers
  features/
    projects/           # UI + feature-owned logic; expand subfolders as needed
    onboarding/
  shared/
    ui/                 # truly cross-feature controls
    lib/
  styles/
```
Use when recurring product workflows have clear names and developers need task-oriented navigation. Put route entry points in the framework's required routes directory (e.g. Next.js app router); do not move framework-conventional special files merely to match this sketch.

### C. Growing modular product
```text
src/
  app/
  features/
    projects/
      components/
      api/
      model/
      index.ts           # explicit public API
  domains/               # only cross-feature business concepts
  shared/
    ui/
    api/
    lib/
  design-system/         # when tokens/styles require separate ownership
```
Use when multiple workflows share durable business invariants and change coordination is costly. Enforce one-way dependencies and public feature entrypoints; avoid importing deep internals of a sibling feature.

### D. Multi-application platform
```text
apps/
  web/
  admin/
packages/
  design-system/
  platform/
  domain-projects/
tooling/
docs/
```
Use only when multiple applications have proven shared contracts and benefit from coordinated builds, ownership or versioning. A monorepo is optional, not synonymous with enterprise architecture; a single large app may be better served as a modular monolith.

## Decision process

1. Identify current primary user journeys and painful developer changes; collect examples before drawing a new tree.
2. Choose the simplest profile accommodating *observed* ownership and dependency needs. Do not use LOC thresholds as a proxy.
3. Draw an import/ownership map: app composition → features → optional domains and shared infrastructure. Lower reusable layers never import feature-specific routes or business commands.
4. Define each module's public surface, owner, allowed dependency direction and criteria for promotion to shared code.
5. Introduce one representative vertical slice, measure change locality and regressions, then decide whether broader migration is worth it.

## What not to do

- **Folder per architecture word:** Do not create empty `services/`, `repositories/`, `models/`, `hooks/` directories without actual responsibility.
- **Global components dumping ground:** A component used by one feature remains feature-local even if it looks generic.
- **Large universal widget:** Do not turn every workflow into a Boolean-heavy `UniversalForm` or `UniversalPage`.
- **Premature package split:** Packages introduce version, tooling and cross-package coordination costs.
- **One-shot migration:** Do not combine route, state, API and CSS rewrites in a single unverified change.

## Verification and unknowns

Measure path-to-change discoverability (task-to-owner lookup), dependency cycles and forbidden imports, duplicate implementation consolidation (with semantics checked), change locality, build/test performance, accessibility keyboard/focus and locale/theme regression on representative workflows. Compare measured baselines, not assumed percentage improvements. Document rollback and compatibility exports. Use [quality gates](../governance/quality-gates.md), [lifecycle](../governance/lifecycle-and-decisions.md), and [component model](component-model.md).

## Source status

Grounded in existing catalog architecture and governance contracts. These profiles are **proposed design heuristics**, not a normative industry standard or an empirically validated optimum. Before recommending specific framework layout, consult its current official routing/build documentation; validate with the application's own dependency graph and usability tests.
