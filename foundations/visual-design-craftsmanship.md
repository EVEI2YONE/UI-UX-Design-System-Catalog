# Visual design craftsmanship: composition, typography, color, spacing and art direction

**Kind:** guideline · **Status:** proposed · **Primary layer:** foundations · **Owner:** unassigned · **Review date:** not reviewed

## Purpose and scope

Use this reference to create a coherent aesthetic language for an interface **after establishing the user's task, content, brand constraints, accessibility needs and supported platforms**. It complements [design principles](design-principles.md) (task hierarchy) and [design tokens](design-tokens-and-themes.md) (semantic implementation). These are heuristics and illustrative recipes, **not experimentally validated universal preferences** or a production-ready theme.

**Use when:** a page is functionally organized but lacks a clear visual direction; designing a new brand or adapting a UI system; reviewing inconsistent typography, color or whitespace. **Avoid when:** copying another brand's distinctive design without rights, pursuing visual novelty over task success, or declaring a style universally superior without user evidence.

## KG-01 — Composition and optical balance

1. Write a **focal-point sentence**: “On this screen, the eye should find [information] first and [action] second.” Keep required safety, price, and status information discoverable.
2. Divide into **dominant, supporting and quiet** areas. Establish dominance with a deliberate difference in scale, contrast, position or whitespace; do not maximize every dimension simultaneously.
3. Choose a grid based on **content constraints** (reading width, form field grouping, cards or data comparison), not a fashionable column count. Use a stable alignment spine; permit asymmetry where it helps scanning.
4. Check **optical balance**, not just numerical centering: large dark blocks, saturated accents, photographs and bold headlines carry more visual weight than pale whitespace.
5. At narrow widths, define the meaningful reading order first; decorative repositioning must not scramble semantics or keyboard focus.

**Good example:** a project overview uses a left-aligned heading, short status summary, one prominent next action and a subdued details panel on a shared alignment grid. **Anti-example:** equal-size colorful cards, centered long paragraphs and three equally bold actions create a noisy entry point.

**Review exercise:** shrink a screenshot until details are unreadable. Can a reviewer still distinguish the intended first, second and background emphasis? Then verify with actual content and representative users; the squint test is only a critique aid.

## KG-02 — Typography craftsmanship

- Start with content roles: display/hero, page title, section heading, body, label, caption, code/numerals. Define a **small role-based type system** with size, weight, line height and responsive adjustments; do not invent a role for every screen.
- Select faces for task and language coverage: readability at real body sizes, distinctive-but-clear headings, glyph support, variable-weight behavior and stable font fallbacks. A restrained single-family system is preferable to an unjustified pairing.
- For a contrasting pair, assign **jobs** (e.g. expressive editorial heading + neutral body), not two competing display families. Test with real product copy.
- Adjust optical spacing: headings may need different tracking and line-height than body text. Avoid tight tracking on small labels and long multilingual text.
- Keep long-form lines comfortably scannable using a max inline measure appropriate to type size and audience; there is no universal character count. Avoid fixed heights that clip translated text.
- Compare heading wrap at multiple widths and 200–400% zoom. Use tabular numerals where aligned values need stable comparison.

**Good example:** a readable sans-serif body with one confident display style, consistent section jumps, and no tiny low-contrast metadata. **Anti-example:** three display faces, letter-spaced body copy, arbitrary weight jumps and headings clipped at mobile widths.

## KG-03 — Color composition and palette formation

1. Choose an **emotional and functional direction** informed by brand and audience (calm, energetic, editorial, technical), then make an initial palette hypothesis.
2. Build a restrained **neutral tonal ramp** for text, page, surfaces and dividers; add one primary action family and only purposeful secondary accents. A token scale is not a reason to expose every swatch at once.
3. Control saturation by relative emphasis: a highly saturated primary action on a quiet surface will attract attention; several equally saturated cards compete.
4. Assess nearby color relationships at the **component and whole-page level**. Use distinguishable states and non-color cues for error, success, selection and focus.
5. Map chosen values to semantic roles, then evaluate light/dark/high-contrast modes independently. Do not mechanically invert a palette or assume the same accent works on every surface.
6. Validate applicable text/non-text contrast using [accessibility guidance](../guidance/accessibility.md), not only perceived harmony.

**Illustrative, untested direction:** warm ivory canvas + deep charcoal text + cool blue action + a restrained warm accent used for noncritical highlights. This is a stylistic starting point, not a universally appropriate palette or an accessibility-verified value set.

**Anti-example:** assigning unrelated saturated colors to every card and treating color alone as status.

## KG-04 — Spatial rhythm, density and whitespace

- Decide the product's **density intent** (comfortable reading, dense operational scanning, touch-first entry) based on user tasks and evidence, not taste alone.
- Design spacing by **relationship**: within-label/control, within-component, between related groups, between sections, between major page regions. Stronger separation should generally communicate a stronger conceptual boundary.
- Choose a compact spacing scale then define semantic roles and documented exceptions. Do not “fix” awkward layouts by accumulating unowned pixel values.
- Use whitespace to clarify grouping, but inspect scroll distance and compare performance on content-heavy screens. Excess negative space can conceal critical information below the fold.
- Check typography and spacing together: line-height, paragraph gaps, heading adjacency, grid gutters and container width form one rhythm.
- Verify at content extremes: zero/one/many rows; long headings; dense form errors; translated strings; small and zoomed viewports.

**Good:** a settings form has tight label-to-control grouping, moderate field separation and a clearly larger section break. **Poor:** equal gaps everywhere make unrelated sections appear connected while compact help text becomes illegible.

## KG-05 — Art direction and visual identity

Before choosing tokens or components, create a **one-page direction brief**:

| Field | Question |
| --- | --- |
| Audience and context | Who uses the UI, on what device, for what consequential task? |
| Brand traits | Pick 2–3 differentiating adjectives, plus an explicit “not this” adjective |
| Visual metaphor | Editorial, utilitarian, warm, premium, playful, data-dense, etc.—a hypothesis, not a mandate |
| Core moves | State specific type contrast, palette character, spacing rhythm and shape/surface style |
| Non-goals | Which fashionable effects would harm trust, performance or usability here? |
| Reference provenance | For each reference, record URL, creator/license if known, what principle is borrowed, and what is **not** copied |
| Validation | How will representative users and reviewers assess task clarity, distinctiveness and fit? |

Explore **two or three meaningfully different directions** at the same content fidelity and workflow, rather than slight hue changes. Compare their readability, brand fit, implementation effort, localization, performance and accessibility. Preserve task ordering across variants to avoid confounding appearance with functionality.

**Illustrative contrast:** a financial operations tool might use compact numerals, restrained neutral surfaces and clear status markers; an arts publication might use expansive typography and expressive editorial crops. Neither style is inherently better; the user's context determines fit.

## Starter acceptance checklist for Batch 1

- [ ] One explicit screen focal point and clear secondary hierarchy; comparable content and states across alternatives.
- [ ] Typography roles defined with rationale, long-copy and fallback tests; no clipped critical text.
- [ ] Color roles map to semantic tokens, with color not the sole status cue; contrast **tested in implementation**, or labeled NOT VERIFIED.
- [ ] Spacing relationship hierarchy, density and responsive reflow documented.
- [ ] Art-direction brief records brand rationale, comparison alternatives, reference provenance and tradeoffs.
- [ ] Reviewer can identify a concrete example and anti-example for each of KG-01–KG-05.
- [ ] Manual visual, screen reader, zoom, keyboard, localization, and real-user checks remain **NOT VERIFIED** unless executed on a rendered product.

## Evidence and limitations

This is synthesis of the catalog's existing design principles, tokens, accessibility and UX measurement policies; composition and art-direction prescriptions are **design heuristics**, not normative W3C standards or proven conversion gains. Validate against context and representative users. For normative accessibility criteria see [WCAG 2.2](https://www.w3.org/TR/WCAG22/); for language and bidirectional layout see [W3C Internationalization Quick Tips](https://www.w3.org/International/quicktips/); for token interchange see [DTCG 2025.10](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/), a Community Group report rather than W3C Recommendation. External reference availability and rendered UI behavior were not verified in this documentation-only batch.

**Related:** [design principles](design-principles.md), [tokens and themes](design-tokens-and-themes.md), [component contracts](../architecture/component-contracts.md), [accessibility](../guidance/accessibility.md), [quality gates](../governance/quality-gates.md).
