# Visual craftsmanship — integrated design-to-review workflow (KG-18)

**Status:** proposed · **Kind:** non-canonical integration guide · **Owner:** unassigned · **Reviewed:** pending · **Scope:** catalog-level method, not a shipped skill, design application or component implementation.

## Purpose, entry and exit

**Use** when a user asks to design, restyle, critique or polish a feature/page and the team needs a repeatable path from product context to verified visual execution. **Avoid** applying this sequence as ceremony for a trivial text/icon fix, adopting unreviewed images as product evidence, or treating an attractive screenshot as proof of accessibility or successful interaction. Start with the **user task and constraints**; design value and safety take precedence over decorative novelty.

**Entry condition:** task/audience/context, available product screens/code and canonical design guidance; identify what is observed versus assumed. **Exit condition:** reviewable design decision, implementation or proposed design with accurate evidence status, visual QA findings, acceptance/disposition and follow-up owner. It is acceptable to exit at a documented, unimplemented design if implementation was not requested.

## Before each new design request: context intake

1. **Resolve sources:** target application (if any), branch/revision and design catalog revision independently. Read its README/CONTRIBUTING, the relevant component/style owners, [canonical registry](../catalog/index.json), and only the related concepts. An agent instruction registry is not automatically the catalog.
2. **Search synonyms and related IDs:** design direction, typography, brand tone → `foundation.visual-craftsmanship`; layout, surfaces, imagery and motion → `foundation.practical-styling`; screenshot critique and verification → `governance.quality`. Check local README links before claiming new knowledge is missing.
3. **Specify decision inputs:** primary user task, content/data and required disclosures; brand traits and existing assets; user segment/platform; design-system tokens/components, existing styling stack, affected locales/directions, theme and responsive targets, accessibility requirements, performance/resource limits, owners and available testing evidence.
4. **Mark evidence:** `OBSERVED` (source/screen), `INFERRED` (reasoned hypothesis), `PROPOSED` (draft guidance) and `NOT VERIFIED` (not run). Record baseline task outcomes only if measured.
5. **Choose proportional output:** minor fixes use the affected component and an acceptance note; a new visual identity uses a direction brief/alternatives; an implemented redesign also requires rendered QA and runtime checks. Do not force three alternatives for a fixed branded design.

## Reusable execution path

| Stage | Required decision/output | Canonical guidance | Gate to proceed |
| --- | --- | --- | --- |
| 0. Product/task framing | User/goal, critical flow and non-negotiable content, constraints, success event | [Design principles](../foundations/design-principles.md); [task flows](../patterns/task-flows-and-information-architecture.md) | Missing task-critical data is resolved or an explicit assumption |
| 1. Reference research | Rights-aware evidence cards, observed traits vs inferred intentions | [Visual craftsmanship, KG-11/12](../foundations/visual-design-craftsmanship.md#batch-3--art-direction-research-exploration-and-selection-kg-1114-proposed) | Transferable rules documented; no wholesale copying |
| 2. Art direction | Direction brief, visual grammar, comparable alternatives and reasoned choice | [Visual craftsmanship, KG-01–05, KG-13/14](../foundations/visual-design-craftsmanship.md) | Primary task and hard constraints protected |
| 3. Style and composition | Content-driven layout, tokens/type/palette, surfaces, images/icons and motion by component owner | [Styling recipes, KG-06–10](../foundations/practical-ui-styling-recipes.md); [tokens](../foundations/design-tokens-and-themes.md); [component contracts](../architecture/component-contracts.md) | No unexplained arbitrary overrides, missing states or unlawful assets |
| 4. Prototype/implementation | Appropriate static/interactive representation or small safe code slice with all key states | [Wireframe method](../guidance/wireframe-methodology.md); [component contracts](../architecture/component-contracts.md) | Never claim unimplemented interaction, focus or data persistence |
| 5. Visual critique | Actual image or render, repeatable environment, observation log, severity and precise remedy | [Quality gates, KG-15/16](quality-gates.md#visual-craftsmanship-review-and-corrective-iteration--batch-4-kg-15-and-kg-16-proposed-2026-11-07); [synthetic examples, KG-17](../foundations/visual-refinement-examples.md) | Re-render after correction; no unresolved blocking visible defects |
| 6. Inclusive + outcome verification | Keyboard, screen reader, zoom/reflow, themes, locale/RTL, reduced-motion and task-success evidence where applicable | [Accessibility](../guidance/accessibility.md); [i18n](../guidance/internationalization.md); [research](../guidance/ux-research-methods.md); [quality gates](quality-gates.md) | Record actual PASS/FAIL; otherwise NOT VERIFIED, never inferred from visuals |
| 7. Delivery and adoption | Traceable decision, review status, owner, design-to-code mapping, rollout/rollback or explicit nonimplementation | [Lifecycle decisions](lifecycle-and-decisions.md); [quality gates](quality-gates.md) | No unapproved default-branch changes, fabricated tests or unmerged-guidance promotion |

**Dependency rule:** stages are a decision map, not an obligatory waterfall. Build minimal reusable tokens early to support a core-flow improvement, or revisit the direction after observed failures. Critical accessibility/privacy/safety/data-loss issues remain P0, independent of aesthetic stage.

## One-page handoff contract

```text
Project/task and affected workflow:
Target repo, ref, key components; catalog ref/PR status:
Audience, task success, real content and constraints:
Evidence: observed / inferred / proposed / unverified:
Design direction: words, reference provenance, alternatives and reasons:
Visual grammar: type roles, colors, spacing, geometry, imagery and motion:
Implementation: owners, semantic tokens, components, breakpoints/containers:
States: default, focus, disabled, loading, empty, error, success (as applicable):
Visual QA: artifact IDs + revisions, conditions, issues and re-render disposition:
Functional QA: keyboard/AT, zoom, theme, locale/RTL, reduced-motion, responsive:
Success/guardrail metrics: definitions, known baseline or missing baseline:
Rollout, compatibility, rollback; owner and review date:
Open risks / NOT VERIFIED / next decision:
```

Do not put application-specific screenshots, asset binaries, user details or code into this catalog. Link to the canonical implementation or reviewed design artifact when one exists.

## Coverage crosswalk: all 18 originally proposed knowledge gaps

| Gap | Coverage | Canonical owner / example | Reusable acceptance question |
| --- | --- | --- | --- |
| KG-01 | Composition | `foundation.visual-craftsmanship` | Is focal priority deliberate and coherent? |
| KG-02 | Typography | `foundation.visual-craftsmanship` | Are type roles readable across copy and locale extremes? |
| KG-03 | Color/palettes | `foundation.visual-craftsmanship` + `foundation.design-tokens` | Are accent, neutrals and semantic states coherent and tested? |
| KG-04 | Spacing/density | `foundation.visual-craftsmanship` | Do spatial relationships express grouping and fit content? |
| KG-05 | Visual identity | `foundation.visual-craftsmanship` | Is the aesthetic tied to brand/task, not random fashion? |
| KG-06 | Layout recipes | `foundation.practical-styling` | Does layout adapt to content, container and reading order? |
| KG-07 | Surfaces/depth | `foundation.practical-styling` | Are borders, radius and elevation purposeful? |
| KG-08 | Iconography/imagery | `foundation.practical-styling` | Are assets consistent, licensed, meaningful and accessible? |
| KG-09 | UI archetypes | `foundation.practical-styling` | Was the archetype adapted to task instead of copied wholesale? |
| KG-10 | Motion craft | `foundation.practical-styling` | Does motion clarify state and honor reduced-motion? |
| KG-11 | Inspiration research | `foundation.visual-craftsmanship` | Are source, suitability, rights and limitations explicit? |
| KG-12 | Reference translation | `foundation.visual-craftsmanship` | Did reference observations become transferable rules without imitation? |
| KG-13 | Visual exploration | `foundation.visual-craftsmanship` | Are alternatives materially different and fairly comparable? |
| KG-14 | Tradeoff choices | `foundation.visual-craftsmanship` | Were hard constraints checked before aesthetic preference? |
| KG-15 | Visual critique | `governance.quality` | Are flaws recorded as specific, evidenced findings? |
| KG-16 | Render/iterate | `governance.quality` | Was the changed artifact re-rendered and compared in equivalent conditions? |
| KG-17 | Before/after cases | `governance.quality`; noncanonical [example bank](../foundations/visual-refinement-examples.md) | Do examples show a repair hypothesis and honest verification limits? |
| KG-18 | Workflow integration | **This integration guide**, discoverable through `governance.quality` | Can a consumer go from task → direction → styling → QA → evidenced decision? |

The crosswalk records **documented proposed coverage**, not evidence that any product or agent is improved.

## Catalog acceptance and evidence checklist

- [ ] All KG-01–18 map to an existing stable canonical ID or an explicitly labeled non-canonical supporting page; no duplicate IDs.
- [ ] Root/nested READMEs and `AGENTS.md` route requests to this workflow and canonical pages.
- [ ] `catalog/index.json` metadata resolves relationships, follows schema and has no duplicate IDs or cycles.
- [ ] `python3 scripts/validate_catalog.py` and `python3 -m unittest discover -s tests -v` run in an actual complete checkout, with results recorded. If impossible, mark NOT RUN and retain draft status.
- [ ] Examples are identifiable as synthetic, sources scoped, no fake screenshot or measured gains.
- [ ] Manual browser, contrast/focus, responsive, translation/RTL and user tests remain NOT VERIFIED until actually performed.
- [ ] PR status is accurately described as draft/open/merged, with separately authorized target implementation.

## Limitations and review provenance

Proposed workflow synthesized from existing catalog guidance and its visual-craftsmanship Batches 1–4, not a new external normative standard. It includes design heuristics; actual research and product constraints can change decisions. [WCAG 2.2](https://www.w3.org/TR/WCAG22/) is the relevant external normative source for applicable web accessibility requirements. The [W3C Internationalization Quick Tips](https://www.w3.org/International/quicktips/) cover language/direction concerns; neither defines aesthetic quality. Review source currency, brand/asset rights and implementation platform before use. No end-to-end product implementation, visual regression, task study or accessibility audit occurred solely by writing this guide.
