# Practical UI styling recipes: layout, surfaces, imagery, archetypes and motion

**Kind:** guideline · **Status:** proposed · **Primary layer:** foundations · **Owner:** unassigned · **Reviewed:** not yet · **Batch:** visual craftsmanship 2 (KG-06–10)

## Purpose, boundaries and adoption

Turn an approved [visual direction](visual-design-craftsmanship.md) into scoped, token-backed, adaptable interface styling. **Use when** implementing or critiquing a page whose structure and task are known but visual execution is inconsistent or generic. **Avoid when** applying a preset look without checking user tasks, introducing global overrides to imitate screenshots, or presenting these illustrative CSS snippets as a production component library.

**Context contract before selecting a recipe:** task and information priority; content type and extremes; brand traits; responsive containers and platforms; component system and styling approach; supported themes/locales; accessibility constraints. Favor the existing application stack (CSS Modules, scoped CSS, utilities, or native styles) and its established tokens. Illustrative CSS below uses custom properties as aliases—**not a complete executable theme**, so consumers must define those properties and validate their actual colors and spacing.

## KG-06 — Layout and composition recipes

Choose from the **content relationship**, not a rigid device preset.

| Recipe | Best for | Composition move | Avoid / inspect |
| --- | --- | --- | --- |
| Editorial reading | Article, documentation, narrative onboarding | Bounded text measure, intentional heading hierarchy, optional wider figures | Overly narrow content for tables, giant display text hiding the first paragraph |
| Application workspace | Editing, administration, task dashboards | Stable navigation zone, contextual heading/action bar, flexible primary work area | Fixed sidebar consuming compact screens, disconnected action placement |
| Comparison grid | Plans, product choices, service options | Equal semantic fields and scan lines; emphasize differences instead of decorating every tile | Different card heights obscuring comparable values, color-only recommendations |
| Data-dense overview | Monitoring, records, operational metrics | Group by question/action, stable number alignment, controlled density | Unlabeled KPI cards, decorative graphs without units or usable alternatives |
| Split view | List/detail, inspector, authoring | Primary item area and a subordinate contextual pane; preserve selection as layout changes | Pane focus loss, content hidden when the split collapses |

**Practical grid example (illustrative):**

```css
.workspace {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: var(--space-section, 1.5rem);
}
@media (min-width: 64rem) {
  .workspace {
    grid-template-columns: minmax(0, 1fr) minmax(16rem, 22rem);
    align-items: start;
  }
}
.workspace__main { min-width: 0; }
.workspace__aside { min-width: 0; }
```

**Decision notes:** This breakpoint is *illustrative*, not a catalog standard; change layout when content fails, not when a particular device name is reached. Keep DOM and reading order meaningful as visual columns change. For reusable cards, [container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_size_and_style_queries) may better reflect placement than global viewport media queries. [Mobile/adaptive guidance](../guidance/mobile-and-adaptive-platform-ux.md) owns navigation, safe areas and focus behavior.

**Good:** a report page keeps its title, scope and actions aligned while a supplemental summary relocates below content in compact mode. **Bad:** a decorative three-column dashboard truncates action labels and rearranges screen-reader order independently of its visual order.

## KG-07 — Surfaces, borders, shadows and layered depth

Use the smallest visual cue that conveys a semantic boundary or interaction, in this order: **space/proximity → subtle tonal surface → border → elevation**. Shadows alone must not carry critical state.

| Surface role | Treatment hypothesis | Check |
| --- | --- | --- |
| Canvas | Quiet base; coherent with text and navigation | Avoid competing with content; accessible contrast |
| Group/card | One restrained border or elevation level; consistent inset spacing | Distinguishable from canvas without ornamental clutter |
| Interactive/selected | Intentional state cue (border, label/checkmark and/or change in surface) | Focus visible; selected not color-only |
| Popover/dialog | Clear foreground/background separation, layering and focus rules | Overlay semantics belong to actual Dialog implementation |
| Destructive/alert | Semantic affordances and explanatory copy, not merely red tint | Color contrast and action consequence |

**Illustrative CSS (token aliases must be defined):**

```css
.summaryCard {
  background: var(--color-surface-raised);
  color: var(--color-text-primary);
  border: 1px solid var(--color-border-subtle);
  border-radius: var(--radius-card);
  box-shadow: var(--elevation-card);
  padding: var(--space-card);
}
.summaryCard:focus-within {
  border-color: var(--color-border-focus);
}
/* This does not replace a visible :focus-visible indicator on each interactive child. */
```

A shadow should express **actual layering** (raised cards or temporary overlays), not be added to every rectangle. Limit competing radius families. In high-contrast/forced-colors environments, inspect whether borders and focus survive; decorative backgrounds may disappear. **Bad:** floating shadow on every field, three unrelated radii and a faint border used as the only selection signal. **Good:** quiet data panels with one distinct raised overlay and independently visible button focus.

## KG-08 — Iconography, illustration and photography

- **Icons:** choose one coherent family (stroke, fill, corner behavior and optical size). Define a small size set; align icons optically with text rather than forcing strict mathematical centering. Preserve recognizable metaphors and use accompanying labels for unclear actions. Accessible names should reflect *actions*, not an icon's shape.
- **Photography:** choose consistent subject, lighting, crop, perspective, color temperature and visual treatment. Prefer deliberate crops with safe subject framing over arbitrary background cover. Specify aspect ratio and focal region; test responsive crops and translated overlays.
- **Illustration:** establish line quality, shape vocabulary, texture, palette and figurative representation; do not mix unrelated stock styles. Avoid decorative noise that masks task status.
- **Assets:** record source, license, attribution obligations, permissions and optimization ownership; don't copy recognizable brand assets by default. Provide useful alternative text for informative images and empty alt for purely decorative ones.
- **Performance and accessibility:** reserve dimensions or aspect ratio to limit layout shift; deliver appropriate sizes/formats; ensure overlaid text remains readable on every supported crop. Animated imagery needs reduced-motion consideration and must not be the only carrier of important information.

**Good:** clear action labels with consistent lightweight icons, relevant photo with predictable focal crop, and alternative text conveying content meaning. **Bad:** five icon packs, image-heavy card UI with mismatched crops and white copy placed directly over an unpredictable photograph.

Illustrative asset contract: `role=informative|decorative; source/license; subject; aspectRatio; objectPosition; alt; mobileCrop; loadingPriority; themeBehavior`. The exact attributes depend on platform and implementation.

## KG-09 — Recipes by interface archetype

These are **starting hypotheses**, not compulsory industry styles. Choose based on user expectations and real tasks.

| Archetype | Visual baseline | Critical deviation to avoid |
| --- | --- | --- |
| Enterprise operations | Restrained neutrals, crisp labels, consistent table density, sparse status accents | Over-minimal forms hiding permissions, errors or bulk actions |
| SaaS workspace | Contextual actions, stable navigation, calm cards and deliberate information grouping | Card-only presentation for records better handled as tables |
| Editorial / learning | Strong typographic identity, reading rhythm, restrained accent, meaningful imagery | Giant hero forcing useful content below repeated decorative sections |
| Commerce / comparisons | Clear images, visible price/terms, comparable specifications, trusted call-to-action hierarchy | Visual urgency or promotional treatment obscuring price, shipping or consent |
| Creative portfolio | Expressive display typography, intentional negative space and strong media art direction | Unpredictable navigation, inaccessible contrast, slow/heavy interaction |

**Worked miniature recipe — operational dashboard:** 
1. Begin with the user's decision (“What needs action today?”).
2. Put current scope, date/freshness and one relevant next action in the header.
3. Group 2–4 salient signals using stable numeral alignment; use smaller supporting labels.
4. Put records that require comparison in a labeled table, not mismatched decorative cards.
5. Reserve strong accent for actionable exceptions and meaningful selection; pair statuses with text/icons.
6. Test empty, stale, loading, narrow viewport, translated labels and keyboard operation.

**Anti-example:** a wall of equal-sized saturated KPI tiles with no scope or dates looks energetic but does not support reliable decisions. [Data-visualization guidance](../guidance/data-visualization-and-dashboards.md) owns truthful metrics, axes and accessible chart alternatives.

## KG-10 — Motion and microinteraction craftsmanship

Every motion decision must document **trigger → what changes → why the movement helps → interruption/exit → reduced-motion fallback**. Begin with useful feedback: state acknowledgment, orientation, hierarchy, or continuity. Avoid animation that delays the primary task or implies a server save succeeded before confirmation.

| Motion use | Prefer | Avoid |
| --- | --- | --- |
| Hover/press | Subtle feedback reinforcing an existing affordance | Hover-only functionality; excessive displacement |
| Panel transition | Short predictable transition that preserves context | Full-screen sweeps for routine actions |
| Loading | Honest progress and cancellability where possible | Fake progress, distracting perpetual motion |
| Success/error | Precise state and content update, optional restrained transition | Celebratory movement for serious/destructive tasks |
| Reordering | State-preserving movement and understandable focus | Visual motion that contradicts DOM/keyboard order |

**Illustrative CSS:**

```css
.action {
  transition: background-color var(--motion-fast) var(--easing-standard),
              transform var(--motion-fast) var(--easing-standard);
}
.action:active { transform: translateY(1px); }
@media (prefers-reduced-motion: reduce) {
  .action { transition: none; transform: none; }
}
```

Values are deliberately semantic; durations and easing must be resolved in a real theme. Verify whether opacity/transform effects are appropriate for each interaction and whether reduced-motion fallback retains essential feedback. [MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) explains platform preference matching; [WCAG 2.2](https://www.w3.org/TR/WCAG22/) governs applicable accessibility requirements. Do not equate this snippet with comprehensive motion accessibility.

## Batch 2 quality and delivery gates

For every adopted recipe record: **task and visual direction; selected archetype/layout; token roles and styling owner; state matrix; accessibility/locale requirements; reference provenance; viewport/container behavior; screenshot checks; alternate considered; measured or unknown outcomes**.

- [ ] Design extends existing canonical concepts, and token aliases are defined by the consumer.
- [ ] Layout responds to real content constraints and preserves semantic navigation and keyboard order.
- [ ] Surface depth and state cues remain distinguishable in relevant themes and high contrast.
- [ ] Icons and images have consistent art direction, usable accessible labels, rights and crop checks.
- [ ] Motion has a purpose, non-motion fallback and honest async state reporting.
- [ ] Include narrow/wide, long text, loading/empty/error, zoom, locale/RTL and reduced-motion variants in implementation review.
- [ ] Docs/registry/internal links validated; **actual rendered visual, performance, user and accessibility tests NOT VERIFIED unless performed**.

## Sources, applicability and related concepts

The prescriptions above are catalog-level design heuristics. Supporting platform references (check current browser support before implementing): [MDN CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout), [MDN CSS Container Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_size_and_style_queries), [MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion), [web.dev responsive images](https://web.dev/learn/images/responsive-images), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [W3C internationalization quick tips](https://www.w3.org/International/quicktips/). Links describe mechanisms and applicable constraints; they do not prove these recipe aesthetics increase usability or conversion.

**Related canonical owners:** [Visual craftsmanship](visual-design-craftsmanship.md) (visual direction), [Design principles](design-principles.md) (task hierarchy), [Tokens and themes](design-tokens-and-themes.md) (role naming/modes), [Component contracts](../architecture/component-contracts.md) (states and APIs), [Mobile/adaptive](../guidance/mobile-and-adaptive-platform-ux.md) (platform behavior), [Dashboard semantics](../guidance/data-visualization-and-dashboards.md), [Accessibility](../guidance/accessibility.md), [Internationalization](../guidance/internationalization.md), [Quality gates](../governance/quality-gates.md).
