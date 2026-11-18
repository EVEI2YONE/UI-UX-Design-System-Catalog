# 03 — Evidence-backed knowledge-gap audit

**Snapshot:** `main` at `3b933abea778122dece31af7496f409028ed6198`, inspected 2026-11-08.  
**Scope:** conceptual guidance vs executable visual catalog requirements.  
**Interpretation:** lack of a running implementation is **not** evidence that the associated design guidance is missing.

## Observed evidence baseline

- The root README describes a **proposal scaffold**, not a shipped component library. It explicitly distinguishes Markdown contracts from executable implementations, and says all initial concepts are proposed.
- `catalog/index.json` uses `schema_version: 0.1.0` and records ID, path, layer, kind, status, summary, aliases, domains, when-to-use, avoid, related, dependencies, owner and review date.
- `catalog/schema.json` has `additionalProperties: false`, so blindly adding preview fields will fail schema validation.
- `components/README.md` enumerates six existing specs: Button, Input, Select, Checkbox, Dialog and Field/Error. These are expressly **not** runtime implementations.
- The repository contains guidance for task flows, search/filter, tables, forms, recovery, accessibility, content writing, visual hierarchy, token themes, performance and UX metrics.
- `AGENTS.md` specifies a canonical registry-first retrieval protocol using `scripts/find_concept.py`; `CONTRIBUTING.md` requires alias/index search before new entries.
- `governance/quality-gates.md` already distinguishes documentation checks from browser/a11y/runtime evidence.

## Gap classification

**Missing** = genuinely absent reusable contract; **Incomplete** = existing canonical guidance lacks a requirement; **Undiscoverable** = content exists but query/routes do not surface it; **Implementation absent** = guidance exists but no running example; **Unverified** = intended behavior has no accepted test evidence; **Unknown** = further inspection required. These categories must not be conflated.

| ID | Candidate gap | Classification | Evidence in catalog | Proposed action | Priority / confidence |
| --- | --- | --- | --- | --- | --- |
| KG-01 | Explicit contract linking canonical ID to executable preview/source/scenario | **Incomplete** registry/website metadata | `catalog/schema.json` lacks visual implementation fields; `AGENTS.md` defines text retrieval only | Add optional typed binding fields and registry validation; preserve original `path` | P1 / high |
| KG-02 | Canonical rule that UI site renders the actual implementation rather than duplicated examples | **Missing implementation governance** | General design-to-code trace present in `governance/quality-gates.md`, but no site-specific source-of-truth rule | Add site source/preview contract and CI parity checks | P1 / high |
| KG-03 | Visual catalog IA and no-preview fallback design | **Missing site-specific pattern** | Task-flow/navigation guidance exists; no site routes or catalog UI implementation | Document static entry page/search/preview fallback; implement a pilot | P1 / high |
| KG-04 | Deterministic, isolated feature demo data and reset contract | **Incomplete** for executable demos | `patterns/interaction-states-and-recovery.md` explains recovery; `governance/quality-gates.md` covers real runtime checks | Define synthetic adapter, scenario lifecycle, no-write isolation and visible simulated-result labeling | P1 / high |
| KG-05 | Feature-level specifications for complete, configurable reference workflows | **Missing specific canonical entries**, not missing pattern guidance | Existing `patterns/data-tables.md`, forms, navigation, recovery, account/settings already cover ingredients | Introduce one feature spec only after checking synonyms and proving cross-product relevance | P2 / medium |
| KG-06 | Executable previews for six core component specifications | **Implementation absent** | `components/README.md` explicitly says specs, not code | Implement minimally, mapping each to existing component IDs | P1 / high |
| KG-07 | Implemented theme/contrast and performance evidence | **Unverified**, not conceptual gap | `guidance/performance-and-perceived-speed.md`; `guidance/accessibility.md`; quality gates | Actual browser/test evidence required before claiming pass | P1 / high |
| KG-08 | Readability and code maintainability guidance | **Already covered in part** | Content writing, design principles, typography/tokens and component architecture | Extend only if site tests identify a real reusable missing decision | P3 / medium |
| KG-09 | Agent discovery for visual example status, preview URL and capabilities | **Incomplete integration** | Alias/relationship-aware text lookup already exists | Extend retrieval to resolve preview/source references without reducing existing matches | P1 / high |
| KG-10 | Complete site deployment/security/performance configuration | **Unknown / design dependency** | No runtime site inspected; only proposal-level source documents | Choose host/framework, privacy/csp rules, rendering budgets after pilot | P2 / medium |
| KG-11 | Searchable source snippets and downloadable packages | **Not a mandatory gap** | User preference is site-embedded implementations rather than published packages | Provide source viewer with copy and attribution; defer distributions | P3 / high |
| KG-12 | Real user research validating catalog discoverability | **Unverified outcome** | UX measurement/research guidance exists | Task-test human and agent lookup, record baseline before claiming benefit | P2 / high |

## Coverage matrix — don't manufacture gaps

| Domain | Canonical source exists? | Runtime evidence? | Audit judgment |
| --- | --- | --- | --- |
| Visual hierarchy & typography | Yes: `foundations/design-principles.md`, `visual-design-craftsmanship.md` | No site implementation inspected | Guidance present |
| Design tokens/themes | Yes: `foundations/design-tokens-and-themes.md` | No embedded site theme tested | Guidance present |
| Component semantics | Yes: `architecture/component-contracts.md`; six `components/*/spec.md` | No executable controls in audited catalog | Implementation absent |
| Task flows/IA | Yes: `patterns/task-flows-and-information-architecture.md` | Catalog site IA absent | Site-specific implementation gap |
| Responsive/zoom/RTL | Yes: accessibility, internationalization and mobile guidance | No site browser evidence | Unverified |
| Forms/errors/recovery | Yes: `patterns/forms.md`, interaction recovery | No runtime feature previews | Implementation absent |
| Performance/readability | Yes: performance and content writing | No site metric baseline | Unverified |
| Agent search/index | Yes: index, schema, `AGENTS.md`, lookup script | Site display integration missing | Extend existing |
| Feature reference contracts | Related general guidance exists | No candidate multi-step feature demonstrated | Potential new feature-specific specs |
| Governance/lifecycle | Yes: contribution policy and quality gates | Website implementation gate not yet in place | Extend selectively |

## Source and standards ledger

These authoritative documents are **relevant review sources**, not proof the catalog satisfies them. Verify applicability and editions when writing implementation PRs:

| Source | Link | Supports |
| --- | --- | --- |
| WCAG 2.2 Recommendation | https://www.w3.org/TR/WCAG22/ | Focus, keyboard, contrast, reflow, target size and text spacing |
| WAI-ARIA APG | https://www.w3.org/WAI/ARIA/apg/ | Dialog, tabs, composite keyboard behaviors |
| W3C i18n quick tips | https://www.w3.org/International/quicktips/ | Language, RTL and internationalization |
| Core Web Vitals | https://web.dev/articles/vitals | Field LCP, INP and CLS definitions, not per-component guarantees |
| Playwright test snapshots | https://playwright.dev/docs/test-snapshots | Reproducible visual regression approach |
| JSON Schema draft 2020-12 | https://json-schema.org/draft/2020-12 | Strict registry schema extension |

## Unverified claims and research needed

No site screenshots, interaction benchmarks, real-user study, production metrics, or WCAG conformance results were produced in this planning audit. A proposal to make previews interactive is not evidence that such previews exist. Re-run the coverage scan against the exact implementation base before opening each feature PR, since repository contents can evolve.

## Acceptance before declaring knowledge gap resolved

A proposal may be marked **documented** when a canonical source is linked and reviewed. It may be marked **implemented** only when the site path and actual code resolve, and **verified** only when required runtime tests/evidence are recorded. Do not use a single `status` string to conceal these separate dimensions.

## Evidence-based reassessment and durable concept preservation (2026-11-08)

This page is the **historical baseline audit**. The separate [KG-01–KG-12 closure matrix and ten-concept decision inventory](17-concept-inventory-and-decisions.md) records current implementation evidence and remaining human/security/measurement gaps. Four deferred feature candidates and five Stage 2 compositions now have individual, **noncanonical** Markdown briefs, linked from the ledger and [machine-readable decision manifest](concepts/decision-manifest.json). That closes the *documentation-preservation* omission, **not** the unverified release/accessibility/research requirements. The 54-entry canonical registry and ranker are unchanged.
