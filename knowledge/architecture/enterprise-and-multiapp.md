# Enterprise and multi-application architecture

**Kind:** guideline · **Status:** proposed · **Owner:** unassigned · **Review:** pending

## Context and prior-knowledge audit

The [application selection guide](application-architecture.md) distinguishes a multi-app profile from a modular single app; [module boundaries](module-boundaries-and-developer-navigation.md) defines feature/domain/shared ownership, and [evolution](architecture-evolution.md) defines migration and fitness. Existing [lifecycle](../../governance/lifecycle-and-decisions.md) already covers component contracts and deprecation. This page adds multi-application topology and multi-team delivery decisions, not a duplicate component lifecycle.

Collect evidence before choosing: app count and platform differences, independent deploy frequency, common consumers, authentication/session and data boundaries, accessibility/brand consistency, API contracts, repository access control, CI/build graph, team ownership, release governance, test and rollback capacity. Never infer a monorepo is needed because an organization calls itself enterprise.

## Topology chooser: independent delivery is a requirement, not a trophy

| Observed context | Prefer to evaluate | Escalate only if evidence shows |
| --- | --- | --- |
| One coherent product, shared release and services | Modular single deployable with enforced feature boundaries | Ownership and release bottlenecks that cannot be solved within the existing architecture |
| Several related applications, stable common contracts | Monorepo with app-local features and versioned shared packages | Incremental build, CODEOWNERS and cross-app integration can be maintained |
| Distinct legal/security/toolchain and truly autonomous release boundaries | Multirepo with explicit consumer contract/version negotiation | Shared changes and security governance remain tractable across repositories |
| Independently deployed parts of **one browser interface** | Microfrontends only after measuring true runtime delivery need | Shell routing, session/permission, navigation, cross-team focus and runtime overhead are acceptable |

**Decision gate:** record app count, distinct platforms, actual deployment cadence, consumer graph, cross-team ownership, regulated boundaries, auth/session integration, localization, accessibility, measured build/deploy pain and rollback capability. Reject a topology for missing prerequisites; do not treat maturity or company size as the primary criterion. [Architecture selection](application-architecture.md) defines app-level starting profiles; [architecture evolution](architecture-evolution.md) owns incremental migration and fitness baselines.

## Architecture topology selection

| Option | Prefer when | Costs and cautions |
| --- | --- | --- |
| Modular monolith (single deployable) | cohesive product, shared release cadence, simpler end-to-end UX | requires rigorous internal boundaries in a growing codebase |
| Monorepo with multiple apps and packages | several related apps benefit from coordinated changes, code sharing and unified tooling | builds, ownership, access controls and dependency graph require governance |
| Multirepo | release/legal/security/tooling isolation dominates shared-code convenience | cross-repo changes, version sync and duplication can be expensive |
| Microfrontends | independently delivered UI ownership is a demonstrated necessity and integration boundaries are stable | runtime integration, consistent auth, navigation, accessibility, performance and UX become harder |

These are alternatives, not an ordered maturity ladder. A large company can remain a modular monolith; microfrontends are not the default enterprise end state.

## Enterprise example: changing a cross-app Dialog contract

**Synthetic context:** Customer Web and Admin Web share a Dialog shell. Admin confirmation contains sensitive authorization, while Customer Web shows ordinary edit forms.

1. Establish a real consumer inventory: which apps import the shared Dialog package at a pinned version, and which feature independently owns authorization, server mutation and recovery.
2. Make the focus/close change in a versioned public API (do not centralize product permissions in Dialog); review both consumer contracts and accessible labels.
3. Test both application shells: opening, Escape/cancel, return focus, async pending/error, zoom, theme, translated copy, RTL and session expiry. A passing package unit test is **not** a passing cross-app journey.
4. Stage release: update one app with compatibility and rollback, then the second app; monitor failures and the cross-app contract, and remove legacy exports only after verified adoption.
5. Reject a microfrontend split merely to resolve Git conflicts; first test clearer ownership, import boundaries and review routing.

**Acceptance:** both apps retain authoritative outcomes and keyboard navigation without requiring synchronized deployments unless explicitly chosen; owner, package version, failing consumer and rollback target are recorded. This is a proposed scenario, **NOT VERIFIED** implementation evidence.

## Reference monorepo layout (illustrative)

```text
apps/
 customer-web/
 admin-web/
packages/
 design-system/ # stable UI contracts + compiled tokens
 platform/ # cross-app technical infrastructure
 domain-projects/ # shared domain rules with real multi-app consumers
tooling/ # build, lint, dependency-rule configuration
docs/ # decisions and consumer migration guides
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

| Source | Directly supports | Does **not** prove |
| --- | --- | --- |
| [Google's monorepo case study (Potvin & Levenberg, 2016)](https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/) | One organization's large-scale repository tooling and tradeoffs | Universal superiority of a monorepo or suitability of this catalog's consumers |
| [Node.js package exports](https://nodejs.org/api/packages.html#package-entry-points) | Encapsulating public entry points in supported Node environments | Module layering, browser UX or access enforcement on the backend |
| [TypeScript project references](https://www.typescriptlang.org/docs/handbook/project-references.html) | Explicit compiler project relationships in TypeScript workspaces | A requirement to divide every app into packages |
| [GitHub CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) | Assigning responsible reviewers and optional required code-owner review in GitHub | That teams have sufficient product knowledge or that a PR is approved |
| [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/) | Web widget interaction expectations across application shells | Automatic accessibility conformance of shared components |

**Review worksheet:** source revision and installed stack; proposed topology and rejected alternatives; named app/package owner; shared consumers; auth/data/UX boundaries; baseline deployment and build costs; allowed/forbidden imports; contract test and integrated-task evidence; migration compatibility; rollback; observed result. Mark each test **PASS, FAIL, NOT VERIFIED** or **NOT APPLICABLE** with a reason, environment and reviewer.

Consult actual platform documentation before prescribing tools; none of these sources establishes a particular product's desired architecture or user outcomes. No implementation or empirical study was performed for this catalog concept.


Consult the target stack's current workspace/build/deployment and browser/platform documentation before prescribing libraries. This is proposed general guidance, not a claim that a monorepo, microfrontend or a specific tool is universally superior. Follow [quality gates](../../governance/quality-gates.md) and [lifecycle](../../governance/lifecycle-and-decisions.md).
