# Application architecture enforcement and CI guardrails

**Kind:** guideline · **Status:** proposed · **Primary layer:** cross-cutting · **Owner:** unassigned · **Review:** pending

## Purpose and context

Turn the ownership decisions in [application module boundaries](module-boundaries-and-developer-navigation.md) into observable, reproducible checks. The [application selection guide](application-architecture.md) determines when added machinery is justified, [framework-aware structure](framework-aware-application-structure.md) protects router conventions, and [architecture evolution](architecture-evolution.md) owns migrations and fitness signals. This page specifies **tool choices and illustrative configuration recipes**, not an installed architecture linter in this documentation-only catalog.

Before choosing a tool or writing a rule, capture **repository and pinned revision**, supported languages, package manager, installed lint/test/CI tooling, framework route aliases and resolution configuration, package or feature ownership map, existing violations, generated/build folders, exception owners and the expected developer feedback loop. Inspect actual resolved imports, not just source-path naming. Mark missing evidence UNKNOWN.

## Choose the smallest enforcement mechanism

| Context | Start with | Move beyond it when |
| --- | --- | --- |
| Prototype or small MVP | A documented owner map, ordinary lint, critical import restrictions | Actual cross-feature imports and change collisions begin to recur |
| Single TypeScript/JavaScript application | Scoped ESLint restrictions for obvious violations; a dependency graph for cycles and relative imports | Imports have aliases, barrel exports or deep paths that defeat string matching |
| Large JS/TS app with many features | Whole-graph checks with explicit from/to module paths; small automated violation fixtures | Ownership expands into separately built project packages |
| Nx-managed multi-project workspace | Project tags and `@nx/enforce-module-boundaries` | Need platform-independent project rules or different language coverage |
| Polyglot multi-app platform | Language-specific checks plus repository-level project/dependency ownership tests | No single tool has reliable resolution across every language |

The objective is **prevent new coupling** at a cost the team can sustain, not to achieve the largest possible ruleset. A passing import rule cannot prove architectural quality, test coverage or user accessibility.

## Recipe 1: scoped ESLint for obvious forbidden imports

**Preconditions:** ESLint flat config; TS/JS source files; path aliases actually defined by the application. This example only checks import specifiers that match the listed strings.

```js
// Fragment for the application's existing eslint.config.mjs array.
// Merge into the existing configuration; do not replace framework presets.
{
  files: ["src/shared/**/*.{ts,tsx,js,jsx}"],
  rules: {
    "no-restricted-imports": ["error", {
      patterns: [
        {
          group: ["@features", "@features/**", "@domains", "@domains/**"],
          message: "Shared code must not import product features or domains."
        }
      ]
    }]
  }
}
```

**Expected FAIL** in `src/shared/lib/format.ts`:
```ts
import { updateProject } from "@features/projects/api";
```

**Expected PASS** in `src/features/projects/ProjectCard.tsx`:
```ts
import { Dialog } from "@shared/ui/Dialog";
```

**Scope limitation:** This rule does **not** automatically detect relative imports (`../../features/projects/api`), differently named aliases, dynamic `import()`, or every form of CommonJS import. It also does not prevent all sibling-feature deep imports. An application with those paths needs a correctly configured graph-based resolver or a more complete rule set. Validate both positive and negative fixtures rather than assuming a pattern is comprehensive. Reference: [ESLint `no-restricted-imports`](https://eslint.org/docs/latest/rules/no-restricted-imports).

## Recipe 2: dependency-cruiser checks for resolved path boundaries and cycles

**Preconditions:** JavaScript/TypeScript application with dependency-cruiser installed as a dev dependency; configure its TypeScript and framework resolver options for the *actual* project before relying on its results. This is an illustrative CommonJS configuration fragment at `.dependency-cruiser.cjs`.

```js
module.exports = {
  forbidden: [
    {
      name: "no-circular",
      severity: "error",
      from: {},
      to: { circular: true },
    },
    {
      name: "shared-must-not-import-features",
      severity: "error",
      from: { path: "^src/shared/" },
      to: { path: "^src/features/" },
    },
    {
      name: "shared-must-not-import-domains",
      severity: "error",
      from: { path: "^src/shared/" },
      to: { path: "^src/domains/" },
    },
    {
      name: "domains-must-not-import-UI",
      severity: "error",
      from: { path: "^src/domains/" },
      to: { path: "^src/(app|features|shared/ui)/" },
    },
  ],
  options: {
    // Add the repository's real tsConfig/module resolution settings here.
  },
};
```

```bash
# Run from the app root, after installing and pinning dependency-cruiser.
npx depcruise --config .dependency-cruiser.cjs --output-type err src
```

**Expected FAIL:** `src/shared/lib/format.ts` imports `../../features/projects/api`, or a module has a detected cycle. **Expected PASS:** a feature imports a generic shared Dialog. Check that alias and extension resolution work correctly; a missing dependency may be an unresolved import rather than a compliant dependency. For sibling-feature isolation, define **explicit per-feature owners** or generated specific constraints; a blanket `features → features` ban could also reject deliberate public integration contracts. References: [dependency-cruiser rules](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md) and [CLI](https://github.com/sverweij/dependency-cruiser/blob/main/doc/cli.md).

## Recipe 3: Nx project tags for multi-project repositories

**Preconditions:** The target already uses Nx and has an ESLint-compatible TypeScript/JavaScript project graph. Add appropriately owned tags to *project* configuration (`type:feature`, `type:domain`, `type:shared`, and product-specific scopes where necessary), then use a rule fragment within the existing Nx/ESLint setup:

```js
"@nx/enforce-module-boundaries": ["error", {
  depConstraints: [
    { sourceTag: "type:shared",
      onlyDependOnLibsWithTags: ["type:shared"] },
    { sourceTag: "type:domain",
      onlyDependOnLibsWithTags: ["type:domain", "type:shared"] },
    { sourceTag: "type:feature",
      onlyDependOnLibsWithTags: ["type:feature", "type:domain", "type:shared"] }
  ]
}]
```

The example enforces broad **project-layer** direction; it does **not** isolate one feature from a different feature because `type:feature` permits other feature-tagged projects. Add scope-specific constraints or a separate feature-isolation rule after documenting actual allowed integrations. This rule applies at Nx project boundaries, not arbitrary subfolders inside one project. The JS/TS lint path does not enforce all non-JS imports; Nx's language-agnostic conformance approach is a separate capability with licensing considerations. See [Nx module-boundary enforcement](https://nx.dev/docs/features/enforce-module-boundaries) and [rule options](https://nx.dev/docs/kb/enforce-module-boundaries).

## Adoption and CI: warning to blocking without a big-bang rewrite

1. **Write an architecture contract:** owners, allowed import direction, public entrypoints, generated code exclusions and justified exceptions.
2. **Baseline the real graph:** list existing violations with affected source/target modules; distinguish unresolvable imports and generated code from clean passes.
3. **Test rules with two fixtures each:** one intentional violation must be rejected and one authorized import must pass. For path alias rules, test alias and relative imports independently.
4. **Introduce nonblocking feedback:** annotate pull requests, fix high-risk issues, and establish a reviewed, time-limited legacy violation baseline. Do not let a baseline silently grow.
5. **Prevent regressions:** fail CI on *new* violations in the covered code; make full enforcement blocking when old exceptions are retired. Ownership and expiration dates are required for exceptions.
6. **Verify user journeys:** continue route integration, API, keyboard/focus, RTL/localization and responsive checks. Architecture lint alone cannot validate UX.
7. **Inspect and refine:** record false positives, unsupported import styles, runtime/build cost and developer feedback. Remove redundant tools if they provide no additional coverage.

An illustrative CI order for an existing JS/TS app is:
```text
install frozen dependencies
  → lint and architecture-boundary check
  → typecheck + unit/integration tests
  → framework production build
  → critical user-journey and accessibility checks where available
```

**Do not add these commands to the catalog's own CI.** This repository validates Markdown and lookup metadata; it has no target application dependency graph to enforce.

## Release evidence and anti-patterns

For every enforcing change, record a pinned tool/version and resolved paths; source policy/owner; new, existing and ignored violations; positive/negative fixture results; CI command and exit status; override/exemption rationale with expiration; impacted consumers and rollback. Use PASS, FAIL, NOT VERIFIED or NOT APPLICABLE accurately.

**Anti-pattern:** add an ESLint alias restriction, declare all architecture boundaries enforced, or suppress violations in CI without an owner and sunset.

**Better:** prove alias coverage and relative-import escape with fixtures; add a graph-level check if needed; freeze the existing baseline and block new violations while resolving old ones incrementally.

## Sources and status

Official tool documentation consulted 2026-11-07 (links above). These configurations are **illustrative**, require adaptation to actual resolver/project versions, and have **not been executed in a target application**. This proposed guide extends [module boundaries](module-boundaries-and-developer-navigation.md), [evolution](architecture-evolution.md) and existing [quality gates](../governance/quality-gates.md) without claiming shipped enforcement.
