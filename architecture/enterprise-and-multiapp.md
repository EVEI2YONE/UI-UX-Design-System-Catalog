# Enterprise and multi-application architecture

**Kind:** guideline · **Status:** proposed · **Owner:** unassigned · **Review:** pending

## Context and prior-knowledge audit (Batch 16)

The [application selection guide](application-architecture.md) distinguishes a multi-app profile from a modular single app; [module boundaries](module-boundaries-and-developer-navigation.md) defines feature/domain/shared ownership, and [evolution](architecture-evolution.md) defines migration and fitness. Existing [lifecycle](../governance/lifecycle-and-decisions.md) already covers component contracts and deprecation. This page adds multi-application topology and multi-team delivery decisions, not a duplicate component lifecycle.

Collect evidence before choosing: app count and platform differences, independent deploy frequency, common consumers, authentication/session and data boundaries, accessibility/brand consistency, API contracts, repository access control, CI/build graph, team ownership, release governance, test and rollback capacity. Never infer a monorepo is needed because an organization calls itself enterprise.

## Architecture topology selection

| Option | Prefer when | Costs and cautions |
| --- | --- | --- |
| Modular monolith (single deployable) | cohesive product, shared release cadence, simpler end-to-end UX | requires rigorous internal boundaries in a growing codebase |
| Monorepo with multiple apps and packages | several related apps benefit from coordinated changes, code sharing and unified tooling | builds, ownership, access controls and dependency graph require governance |
| Multirepo | release/legal/security/tooling isolation dominates shared-code convenience | cross-repo changes, version sync and duplication can be expensive |
| Microfrontends | independently delivered UI ownership is a demonstrated necessity and integration boundaries are stable | runtime integration, consistent auth, navigation, accessibility, performance and UX become harder |

These are alternatives, not an ordered maturity ladder. A large company can remain a modular monolith; microfrontends are not the default enterprise end state.

## Reference monorepo layout (illustrative)

```text
apps/
  customer-web/
  admin-web/
packages/
  design-system/          # stable UI contracts + compiled tokens
  platform/               # cross-app technical infrastructure
  domain-projects/        # shared domain rules with real multi-app consumers
tooling/                  # build, lint, dependency-rule configuration
docs/                     # decisions and consumer migration guides
```

Do not create a package for every directory or tiny feature. Package boundaries require versioned public interfaces, a real maintenance owner and independent consumer tests. Keep app-only features inside the owning app. Choose workspace and build tooling based on existing stack and the actual incremental-build/dependency needs.

## Ownership and dependency governance

- Define one accountable team/owner per app, shared package and public API; use review rules and release notes for breaking changes.
- Preserve one-way dependency layers; forbid upward imports, accidental cross-app internal imports and dependency cycles.
- Design-system packages expose accessible primitives, tokens and styles; product-specific request/permission workflows stay in the app or domain owner.
- Shared domains define stable portable contracts and avoid importing web router/UI implementation. When truly platform-specific, use explicit adapters.
- Treat version policies deliberately: lockstep for tightly coupled consumers, independent versions for independently released contracts. Specify supported versions, deprecation window and rollback.
- Cross-cutting authentication, authorization, localization, analytics and privacy must have explicit integration contracts and responsible owners.

## UX consistency across teams

Cross-app navigation and design consistency require common accessibility/focus, tokens, locale/RTL, content and error conventions, not merely identical visual styling. Verify deep links, keyboard navigation between shells, focus recovery, session expiry, route transitions and responsive performance in integrated environments. A design-system build passing is not evidence an end-to-end journey works.

## Enterprise fitness and migration

Track cross-team change lead time, consumer breakage, duplicate implementations, dependency graph health, build/test feedback, independently deployable changes actually needed, bundle/performance cost and critical task outcomes. Evaluate baseline and confounding factors; no invented universal thresholds.

When splitting an existing app or package, begin with stable high-value consumers, define contract/version ownership, move a narrow slice, preserve compatibility adapters and run integration tests; expand only when deployment or maintenance benefits outweigh coordination costs. Document escape/rollback plan.

**Anti-example:** introduce microfrontends to reduce Git merge conflicts while each frontend separately implements dialogs, permissions and navigation. **Better:** fix module boundaries, ownership and UI contracts first, then justify independent runtime delivery with measured needs.

## Evidence and applicability

Consult the target stack's current workspace/build/deployment and browser/platform documentation before prescribing libraries. This is proposed general guidance, not a claim that a monorepo, microfrontend or a specific tool is universally superior. Follow [quality gates](../governance/quality-gates.md) and [lifecycle](../governance/lifecycle-and-decisions.md).
