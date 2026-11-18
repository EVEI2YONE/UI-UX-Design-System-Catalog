# B05 context gate — utility-first styling, enforcement and component inventory

**Collected before B05 edits:** 2026-11-07. **Catalog main SHA:** `00df3f2055396e586fbb5ffa07e4a80dc8312e8e`. **Shared branch:** `knowledge/icon-interaction-system-b01-b06`; B01–B04 committed; no PR before B06.

## Sources and current ownership

- Read `AGENTS.md`, `CONTRIBUTING.md`, `catalog/index.json`, `foundations/README.md`, `architecture/README.md`, and relevant test/validation guidance. The catalog is proposed knowledge, not executable design system code.
- `foundation.design-tokens` already owns semantic/reference/component token layers, theme modes, alias integrity, legacy-global-CSS migration and compatibility. Do not create a second token definition system.
- `foundation.practical-styling` owns layout/surface recipes, icon craftsmanship, scoped styling illustrations and visual proof requirements. It is incomplete on a *concrete utility-first/shadcn mapping with ownership and example states*.
- `architecture.framework-aware` owns routing-dependent colocation and module placements, not CSS semantics. `architecture.component-model` already owns reuse/extend/deprecate and an incremental extraction method; incomplete on a *component inventory to canonical contract decision worksheet*.
- `architecture.enforcement-ci` already owns scoped ESLint, dependency-cruiser, Nx, staged CI and runtime-evidence caveats, but does not yet document *CSS/utility/style drift guardrails*.
- Little Wins proposed B01/B03 knowledge records real `app/globals.css`, `shared/styles/display-foundations.css`, Tailwind class strings and a canonical shadcn/Radix primitive facade. It explicitly reports sparse sampled React inline `style` use and no full duplicate-class census. Do not invent a CSS-in-JS/inline-style epidemic or claim rendered screenshots.

## Gap disposition

| Gap | Class | Decision | Existing canonical owner |
| --- | --- | --- | --- |
| CKG-15 utility-first styling ownership example | Incomplete example | Extend the existing practical styling recipe, cross-link token/theme migration and framework colocation | `foundation.practical-styling` |
| CKG-16 visual redundancy enforcement | Incomplete enforcement example | Extend existing architecture CI guidance with baseline-aware, ownership-sensitive CSS/utility linting and exception criteria | `architecture.enforcement-ci` |
| CKG-17 inventory-to-contract mapping | Incomplete decision worksheet | Extend existing component model; distinguish installed, exported, imported, used, duplicated and feature-local items | `architecture.component-model` |

**No new canonical ID** or duplicate component library should be added. Preserve existing static/semantic styles, accessible focus states and backend behavior in migrations. These are cross-framework contracts, with a TS/React/Tailwind example only where appropriate.

## Scope and evidence boundary

- Proposed directory examples are illustrative, not required `src/` reshuffles; use installed stack and pinned framework versions. Styling tokens and app-specific visual direction must be decided by a product design review.
- Prevent over-enforcement: code-format similarity alone does not prove a reusable semantic component; raw literal values may be justified; animation/geometry may legitimately use dynamic runtime values. Thresholds must come from a measured repo baseline rather than invented fixed line-count limits.
- References: [Tailwind theme variables](https://tailwindcss.com/docs/theme/), [CSS custom properties on MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties), [ESLint custom rules](https://eslint.org/docs/latest/extend/custom-rules), [WCAG 2.2](https://www.w3.org/TR/WCAG22/) for states, contrast, keyboard and reflow. Implementation syntax and tool version must be checked against the consuming app.
- **Not verified:** executing catalog tests, actual Little Wins visual regressions, whole-code duplicate rate, lint rule accuracy/false positives, human approval, screen-reader or browser behavior.

## B05 acceptance

1. Produce a bounded, utility-first styling ownership matrix and CSS/Tailwind example with variants/states and themeability.
2. Explain lint/check strategy for repeated raw tokens, duplicate primitives, broad selectors and variant explosion with clear exceptions and baseline-first enforcement.
3. Provide a compact inventory-to-contract worksheet and promotion/deprecation criteria with actual use evidence.
4. Update current registry entries, section/root/agent navigation, lookup regression tests, changelog and cumulative progress ledger.
5. Keep canonical IDs and B06 final PR gate; report unexecuted tests as NOT VERIFIED.
