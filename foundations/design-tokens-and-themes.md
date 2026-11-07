# Design tokens and themes

**Kind:** guideline · **Status:** proposed · **Primary layer:** tokens

## Purpose

Make recurring visual decisions explicit, semantic, themeable, accessible and portable. Token values are data; a component contract decides how to use them.

## Layers

1. **Reference:** raw reusable palette or scale (for example `reference.blue.600`).
2. **Semantic:** intent (`color.text.primary`, `color.action.primary`, `focus.ring`, `space.content.gap`).
3. **Component:** optional stable alias (`button.primary.background`), used only when component-specific requirements are genuine.
4. **Mode and density:** mappings for light, dark, high contrast, brand and compact/comfortable variants.

Conceptual mapping, **not a shipped token file**:

```text
reference.blue.600 -> color.action.primary.background
color.action.primary.background -> button.primary.background
light: color.action.primary.background = reference.blue.600
dark:  color.action.primary.background = reference.blue.300
```

For interoperable exports, consider the [DTCG 2025.10 typed format](../governance/references.md) with `$type`, `$value` and aliases. It is a W3C Community Group report, **not a W3C Recommendation**.

## Design rules

- Define named roles for typography, color, spacing, radius, borders, elevation, motion and focus.
- Avoid unowned raw hex/pixel duplication and arbitrary z-index or duration escalation.
- Keep token aliases acyclic and resolvable; detect unused and conflicting tokens.
- Test every relevant theme's contrast, focus, disabled/error state, and reduced motion behavior.
- Use content-driven responsive rules and CSS logical properties instead of device-name-specific values.
- Keep public customization small (`size`, `variant`, `density`, theme aliases); avoid unconstrained style overrides.

## Example / anti-example

**Good:** a button consumes `color.action.primary.background` so a theme can change the mapping centrally. **Poor:** every button copy uses its own hard-coded brand hex and a different focus ring.

## Verification

Check alias resolution, a sample of component states across modes, reflow, translated labels and reduced motion. Token values alone do not establish accessibility compliance. Related: [component contracts](../architecture/component-contracts.md) and [accessibility](../guidance/accessibility.md).

## Token authoring and migration contract

A token record should state **name, type, value or alias, purpose, owner, supported modes, consumers and status**. Resolve aliases before use and reject cycles. Distinguish a semantic role from a particular brand color: changing a reference palette should not require edits across controls.

Illustrative, **not an importable token export**:

```json
{
  "color": {
    "text": {
      "primary": {
        "$type": "color",
        "$value": "{palette.neutral.900}"
      }
    }
  }
}
```

The example omits the referenced palette by design; it cannot pass alias-resolution checks on its own. A real export must define the referenced token and follow its toolchain's supported DTCG syntax.

**Migration sequence:** inventory repeated literals and contexts; map to a small semantic role set; define mode mappings; migrate one representative component; compare all states and narrow/zoom layouts; then expand consumers incrementally. Keep app-specific values local until a repeated semantic role is established.

| Gate | Evidence required |
| --- | --- |
| Alias integrity | Every alias resolves, no cycles or ambiguous duplicates |
| Theme behavior | Text, action, focus, status and disabled roles reviewed in every supported mode |
| Styling | Component styles use owned aliases; justified dynamic exceptions recorded |
| Compatibility | Old-to-new token map, affected consumers, rollback method |

Avoid encoding success/error only by color. A palette comparison alone does not establish contrast or accessible interaction.

## Batch 12 extension — token interchange and release checks

Keep **one reviewed semantic token source** with explicit schema version, types, aliases, purpose, ownership and platform/mode mappings. As of 2026-11-07, the Design Tokens Community Group Format Module **2025.10 is stable**, but it is a W3C **Community Group report, not a W3C Recommendation**. Newer 2026 preview drafts must not be treated as authoritative release specifications.

| Decision | Evidence and risk |
| --- | --- |
| Source | Named token repository/export, pinned format version, changelog and maintainers |
| Types and references | Compatible typed values, all aliases resolve, no cycles, type/format mismatch or invalid references |
| Semantic intent | Shared meaning and role before literal values or app-specific colors |
| Themes | Explicit light/dark/high-contrast/brand/density mappings; no accidental missing tokens |
| Platform transform | Test generated CSS/native tokens in actual consumers, including units and color-space support |
| Compatibility | Document renamed tokens, migration aliases, affected components, release version and rollback |
| Experience | Verify real focus/disabled/error contrast, responsive modes, RTL and content extremes; screenshots are supplementary |

**Illustrative workflow:** a reviewed semantic color role changes, a pinned converter exports CSS/native values, tests validate aliases and usage, visual snapshots are compared for representative states, and keyboard/focus/contrast are manually checked before a versioned rollout. The token's own metadata does not certify accessibility.

**Anti-example:** overwrite exported raw values, rename widely used aliases without notice, accept every regenerated screenshot and declare all themes compliant.

Sources consulted 2026-11-07: [DTCG Format Module 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/), [DTCG spec status and caveats](https://www.designtokens.org/faq/) and [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots). No actual token transform or test occurred as part of this docs-only addition.

Related: [component contracts](../architecture/component-contracts.md), [quality gates](../governance/quality-gates.md), [lifecycle](../governance/lifecycle-and-decisions.md).


## Batch 9 — legacy global CSS to scoped semantic styling (proposed, 2026-11-07)

**Observed migration trigger:** Little Wins imports Tailwind but also relies on a large `app/globals.css` with compact global selectors, raw hex custom properties (`--ink`, `--paper`, `--sidebar`, `--purple`) and repeated breakpoint overrides. The source includes a shadcn-style configuration and a separate UI component collection. Neither that configuration nor a Tailwind import proves product-specific classes already follow the library's token and component conventions.

**Inventory contract:** for each recurring visual intent, record the existing CSS selector/source, resolved color/space/font/motion value, light/dark/high-contrast behavior, affected components, owner and proposed semantic token. Distinguish a **reference value**, a **semantic role**, a **component-scoped override** and an **intentional one-off**. Collect selector dependencies before renaming; generic class names such as `.button`, `.card` or `.status` can have a broad blast radius.

**Migration order:** (1) keep current appearance as a recorded baseline; (2) map raw values into reviewed semantic aliases, preserving aliases during transition; (3) scope feature styling to owned components (CSS modules, documented namespacing or another existing supported approach); (4) replace one workflow at a time; (5) remove old global selectors only when consumers and visual/interactive regressions are checked. The catalog does not mandate Tailwind, CSS modules, CSS-in-JS or a new design-system package.

**Safeguards:** preserve cascade order, specificity, focus-visible treatment, reduced-motion preferences, responsive breakpoints, font loading and translated text expansion. Do not change accessibility semantics merely to match a screenshot. Unknown modes remain unverified; do not introduce an untested dark theme or claim token adoption before runtime evidence.

**Illustrative mapping only:** `--ink` might map to a reviewed `color.text.primary` role and `--paper` to `color.surface.canvas`, but do not equate raw colors with roles without checking uses, contrast and theme behavior. CSS variable names and values in the source are not universal standards.

**Verification:** documented before/after selector and token map; light/dark only where implemented; responsive snapshots at supported breakpoints, keyboard focus, dialog/backdrop layering, reduced motion, high zoom, long/RTL copy, font fallback and performance measurements where available. Compare component consumers incrementally and keep a revert path.
