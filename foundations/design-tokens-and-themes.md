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