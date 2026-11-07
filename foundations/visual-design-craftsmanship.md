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

## Practical styling continuation — Batch 2 (proposed)

After selecting a coherent visual direction, use [Practical UI styling recipes](practical-ui-styling-recipes.md) for grid and responsive layout patterns (KG-06), surfaces and depth (KG-07), iconography/imagery (KG-08), interface archetypes (KG-09) and purposeful motion (KG-10). That companion page supplies *implementation hypotheses*; this page remains the canonical owner of composition, typography, palette, spatial rhythm and art-direction choices.


## Batch 3 — Art-direction research, exploration and selection (KG-11–14; proposed)

This section **operationalizes the KG-05 art-direction brief**. Its purpose is a repeatable method for studying visual references and choosing an aesthetic direction **without confusing precedent, brand preference, user research or implemented usability evidence**. Use the existing [UX research](../guidance/ux-research-methods.md) entry for participant studies and [wireframe methodology](../guidance/wireframe-methodology.md) for representation fidelity and prototype escalation. No reference is proof of conversion, accessibility or a universal best practice.

### KG-11 — Inspiration gathering and source appraisal

Start with a documented design question such as *“How could a data-heavy planning application appear calm while retaining obvious priority and status?”* Collect a **small, diverse set of references**, not a bulk moodboard. Search across relevant and intentionally contrasting product categories so that the first famous design system does not become the default answer.

For every source, create a **reference card**:

| Field | Required observation |
| --- | --- |
| Source and provenance | URL or offline source, creator/organization, capture date, license/usage restrictions if known |
| Context | Intended audience, use case, device/viewport and whether this is a live screen, marketing render or concept |
| Observed traits | Specific typography, color balance, shape, density, spacing, imagery, hierarchy and motion visible in the source |
| Proposed transfer | One generalizable principle, explained independently of brand assets |
| Contraindication | When the trait could fail in our product, e.g. translated content, high-density tasks, focus visibility or performance |
| Evidence status | Observed screenshot vs inferred intent vs independently user-tested (only if real study evidence exists) |

**Search and selection rule:** Include at least one reference serving a similar task, one counterpoint with different density/personality, and one example that demonstrates a specific pattern worth evaluating. Source popularity or visual attractiveness alone is not evidence of usability. Avoid retaining third-party screenshots or copyrighted artwork in a distributed catalog without permission; descriptions and source links are usually sufficient.

**Example:** A quiet editorial layout demonstrates a generous heading-to-body gap. Record the grouping principle, then test it against the product's actual content density. **Anti-example:** “Copy this site's homepage, including its distinctive hero illustration and unique brand palette.”

### KG-12 — Translate references into ownable design rules

Use **observe → hypothesize → abstract → adapt → verify**. Keep those five stages separate so neither a screenshot nor a designer's interpretation becomes an unearned requirement.

1. **Observe** measurable features: alignment axis, number and relative weight of type roles, accent placement, corner family, surface grouping and image crop behavior. State when geometry is estimated from an image.
2. **Hypothesize** what job each feature may serve: improving scan order, expressing warmth, indicating interaction, or simplifying hierarchy. Label motivation inferred unless backed by evidence.
3. **Abstract** a transferable rule without copying a signature composition: e.g. *“Reserve saturated color for one decisive action and meaningful state, while keeping data comparisons on quiet surfaces.”*
4. **Adapt** to the target product's design tokens, component contracts, content constraints and brand. Preserve semantic and keyboard order.
5. **Verify** with comparable states and representative content: empty/error/loading, mobile, long text, RTL where supported, supported themes, contrast and focus. If no rendered implementation exists, mark verification **NOT VERIFIED**.

**Reference-to-rule ledger (illustrative):**

| Observation | Generalizable rule | Avoid copying | Verify |
| --- | --- | --- | --- |
| A publication uses high-contrast display type over narrow editorial text | Deliberately distinguish storytelling heading from body reading | Its distinctive font/logotype and exact hero artwork | Headlines, font fallbacks, long translations, zoom |
| A finance UI uses neutral cards and one strong status color | Reserve dominant accent for meaningful action or exception | Exact palette, status colors without labels | Accessible contrast, urgency comprehension, dark mode |
| A creative portfolio uses asymmetrical image blocks | Use asymmetric composition when it directs attention | Exact crop/arrangement tied to original creator | Reading order, keyboard sequence, compact layout |

### KG-13 — Divergent design-direction exploration

Prepare **two or three materially distinct directions** using the *same representative screen, text, tasks and critical states*. Differences should be strategic, not cosmetic hue swaps. Keep priority content and disclosure fixed so stakeholders can judge visual treatment rather than altered functionality.

For each direction record:

- **Name and thesis:** e.g. “Quiet Utility: quick scanning with subdued visual noise.”
- **Brand fit and non-goals:** 2–3 target traits and a rejected trait.
- **Visual grammar:** type roles and pairing, tonal palette/accent, section rhythm, geometry/borders/depth, icon/photo treatment and optional motion.
- **Example frame:** one common task screen, including title, context, primary action, secondary content and error/empty state.
- **Risks and constraints:** density, localization, contrast/focus, performance, third-party assets and implementation complexity.
- **Unknowns:** statements requiring actual participant or implementation checks, not declared truths.

**Illustrative direction set for a project dashboard:**

| Direction | Expressive move | Strength hypothesis | Main risk to test |
| --- | --- | --- | --- |
| Quiet Utility | Restrained neutrals, compact functional typography, minimal elevation | Fast recognition of work items | Feels too sparse or weakly differentiated |
| Warm Editorial | Distinctive display headings, warm background and airy section rhythm | Approachable orientation and storytelling | Slower scanning or excessive scroll on dense workflows |
| Technical Precision | Monospaced numeric accents, clearly ruled grids, crisp status labels | Confident comparison and clear status | Mechanical or overwhelming for novices |

At low fidelity, assess structure; at high fidelity, assess visual fit; use an interactive prototype when the decision involves real navigation, focus, validation or recovery. See [wireframe methodology](../guidance/wireframe-methodology.md). Do **not** treat a static mock as evidence of working accessibility.

### KG-14 — Transparent aesthetic tradeoffs and decisions

Make a decision using a **two-stage gate** rather than a single ungrounded beauty score.

**Gate 1 — hard constraints:** Reject or revise a direction if it obscures critical action/price/privacy information, produces known inaccessible contrast or focus, contradicts brand/legal rights, prevents required localization, breaks the primary task, or exceeds a non-negotiable performance/platform constraint. Unverified criteria must be labelled pending rather than passed.

**Gate 2 — compare surviving directions** using explicit evidence and team priorities:

| Criterion | Question | Evidence / status |
| --- | --- | --- |
| Task legibility | Can a user rapidly locate purpose, current state and next action? | Representative task walkthrough; test pending if not run |
| Brand distinctiveness | Does the grammar express the desired traits without imitating another source? | Design brief and reviewer rationale |
| Cross-screen coherence | Can the grammar extend to forms, tables, dialogs, errors and small widths? | Comparative screen set and state coverage |
| Inclusive resilience | Do type, color and layout remain workable with zoom, focus, themes, translated text and reduced motion? | Actual verification required |
| Maintainability | Can styles be tokenized and owned without unbounded variants or global overrides? | Architecture and component review |
| Delivery risk | What is the asset, font, performance, compatibility and rollback cost? | Owner estimate; unresolved risk explicit |

**Decision record:** chosen direction; alternatives; reasons and supporting observations; design owner; user/research uncertainty; accepted tradeoffs; implementation dependencies; next evaluation trigger and date. Do not assign pseudo-scientific weights unless stakeholders agree what they mean. If two directions are close, prototype the riskiest assumption rather than adding ornamental variants.

**Good decision:** “Choose Quiet Utility provisionally for operational tasks: clearer status grouping and fewer competing accents in expert review; test novice comprehension and compact error states before release.” **Bad decision:** “The Warm Editorial variant is 92% more beautiful, so it must improve conversion,” with no valid instrument, denominator or user study.

### Batch 3 reusable handoff and acceptance

For each actual design request, produce a compact **art-direction decision packet** containing (1) task/brand brief, (2) three or fewer annotated and rights-aware references, (3) extracted principles and contraindications, (4) at least two comparable candidate grammars or a documented rationale for one, (5) constraint checks and evidence status, and (6) selected provisional direction with an explicit revisit trigger.

- [ ] Source provenance and permission/asset limits recorded; no wholesale imitation.
- [ ] Observations and hypotheses distinguished from real user research.
- [ ] Candidate screens share task, content, hierarchy and comparable fidelity.
- [ ] Selection includes accessibility, i18n/RTL, responsive, performance and implementation tradeoffs.
- [ ] Relevant [token architecture](design-tokens-and-themes.md), [styling recipes](practical-ui-styling-recipes.md), [UX research](../guidance/ux-research-methods.md) and [quality gates](../governance/quality-gates.md) identified.
- [ ] Visual, prototype, user and manual accessibility tests remain **NOT VERIFIED** unless actually run.

**Source scope and applicability (reviewed as references 2026-11-07):** [GOV.UK Service Manual — Making prototypes](https://www.gov.uk/service-manual/design/making-prototypes) and [How the alpha phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works) support exploring alternatives and testing uncertain design decisions, not the aesthetic value of any specific palette. [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) provides applicable normative web accessibility criteria, not a measure of attractiveness. Reference-card fields and the direction-comparison rubric above are proposed catalog heuristics, not a claimed W3C or GOV.UK requirement.
