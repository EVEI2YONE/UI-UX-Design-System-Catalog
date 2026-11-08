# 01 — Recommended folder and file restructuring

## Design premise

The site is **the working visual demonstration of the existing catalog**, not a separate component product. Keep canonical concept prose at the repository root and render it through a lightweight, mostly static frontend. Examples in the website should themselves be real code, with deterministic scenario states. No `packages/` tree or distributed component releases are required in phase one.

## Existing inventory: preserve, not duplicate

| Current root | Evidence of existing role | Decision |
| --- | --- | --- |
| `catalog/index.json`, `catalog/schema.json` | Canonical IDs, relations, aliases, statuses and strict metadata schema | **Keep**, add optional display bindings compatibly |
| `components/{button,input,select,checkbox,dialog,field}/spec.md` | Six platform-neutral contracts | **Keep** specifications; link each to site implementation when real |
| `patterns/*.md` | Task flow, navigation, forms, search, data tables, recovery etc. | **Keep** normative guidance |
| `foundations/`, `architecture/`, `guidance/`, `governance/` | Tokens, visual principles, contracts, quality and performance | **Keep** canonical knowledge |
| `AGENTS.md`, `scripts/find_concept.py`, `scripts/validate_catalog.py` | Agent lookup / integrity gates | **Keep**; extend regression coverage |
| `templates/`, `archive/`, section READMEs | Contribution entrypoints and historical provenance | **Keep** and add links when navigation changes |
| `site/`, `features/` | Not established as implementation directories in the reviewed tree | **Add gradually**, do not move existing pattern guidance indiscriminately |

## Target tree (proposed additions are annotated `+`)

```text
UI-UX-Design-System-Catalog/
├── README.md
├── AGENTS.md
├── CONTRIBUTING.md
├── foundations/                  # existing canonical knowledge
├── architecture/                 # existing canonical knowledge
├── guidance/                     # existing canonical knowledge
├── governance/                   # existing canonical knowledge
├── components/                   # existing spec.md per concept
├── patterns/                     # existing specifications and guidance
├── templates/                    # existing canonical concept template
├── catalog/
│   ├── index.json                # existing sole identity/search registry
│   ├── schema.json               # existing strict registry schema
│   └── README.md
├── features/                     # + feature reference SPECIFICATIONS, not app backends
│   ├── README.md
│   ├── review-workspace/
│   │   ├── spec.md
│   │   └── integration.md
│   ├── data-workspace/
│   │   ├── spec.md
│   │   └── integration.md
│   └── settings-center/
│       ├── spec.md
│       └── integration.md
├── site/                         # + actual working reference website
│   ├── README.md
│   ├── package.json
│   ├── tsconfig.json
│   ├── app/                      # framework routing (Next.js is a proposal)
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── globals.css
│   │   ├── catalog/
│   │   │   ├── page.tsx
│   │   │   └── [layer]/
│   │   │       └── [slug]/page.tsx
│   │   ├── guidance/[...slug]/page.tsx
│   │   └── search/page.tsx
│   ├── src/
│   │   ├── catalog-data/         # adapter over existing canonical registry
│   │   │   ├── load-index.ts
│   │   │   ├── resolve-entry.ts
│   │   │   ├── search.ts
│   │   │   ├── relations.ts
│   │   │   └── source-loader.ts
│   │   ├── catalog-ui/           # chrome ONLY, not cataloged examples
│   │   │   ├── SiteShell.tsx
│   │   │   ├── SearchBox.tsx
│   │   │   ├── EntryCard.tsx
│   │   │   ├── EntryDetail.tsx
│   │   │   ├── PreviewFrame.tsx
│   │   │   └── SourceView.tsx
│   │   ├── implementations/      # actual executable reference code
│   │   │   ├── foundations/
│   │   │   │   └── tokens.css
│   │   │   ├── primitives/
│   │   │   ├── components/
│   │   │   │   ├── button/
│   │   │   │   │   ├── Button.tsx
│   │   │   │   │   ├── Button.module.css
│   │   │   │   │   ├── scenarios.ts
│   │   │   │   │   ├── preview.tsx
│   │   │   │   │   └── Button.test.tsx
│   │   │   │   └── field/
│   │   │   ├── patterns/
│   │   │   │   └── async-form/
│   │   │   └── features/
│   │   │       └── review-workspace/
│   │   │           ├── ReviewWorkspace.tsx
│   │   │           ├── mock-adapter.ts
│   │   │           ├── scenarios.ts
│   │   │           ├── preview.tsx
│   │   │           └── ReviewWorkspace.test.tsx
│   │   ├── previews/
│   │   │   ├── preview-registry.ts
│   │   │   ├── scenario-contract.ts
│   │   │   ├── PreviewHost.tsx
│   │   │   └── fixtures/
│   │   ├── styles/
│   │   │   ├── site-theme.css
│   │   │   └── preview-isolation.css
│   │   └── lib/
│   ├── public/
│   └── tests/
│       ├── discovery/
│       ├── interactions/
│       ├── accessibility/
│       ├── visual/
│       └── performance/
├── scripts/                      # existing, extend only as needed
├── tests/                        # existing Python catalog tests
└── docs/
    └── visual-catalog-refactor/   # this planning pack
```

## Ownership rules

1. **Canon:** `catalog/index.json` defines unique IDs, aliases, related concepts, ownership and discovery. `*.md` files own normative guidance.
2. **Routing:** `site/app/` maps canonical IDs to URLs. Framework folders do not create IDs or infer permanent identity from slug.
3. **Implementation:** `site/src/implementations/` owns executable UI; no product-specific API, authorization rule, or real credential.
4. **Catalog chrome:** `site/src/catalog-ui/` owns browsing UI; it can consume a shared button internally but must not silently override the button's reference behavior.
5. **Preview isolation:** `site/src/previews/` owns fixture determinism, reset, theme, viewport and error scenario control.
6. **Styles:** semantic tokens derive from `foundations/design-tokens-and-themes.md`; no second ungoverned token ontology. Keep site chrome and showcased UI styling isolated.
7. **Quality:** root Python catalog checks remain authoritative for metadata; site checks add browser/runtime evidence. Neither substitutes for the other.

## Do not move yet

Do **not** move existing `patterns/*.md` into `features/` merely to match folder symmetry. A feature requires a concrete, multi-step, configurable workflow with a spec and integration boundary. The pattern documents already cover many related concepts; link them, don't duplicate. Also do not move `components/*/spec.md` under `site/`; source guidance should survive a frontend rewrite.

## Site entry contract

An entry page resolves `id -> registry entry -> canonical Markdown -> optional implementation -> optional scenario manifest -> optional source excerpt`. If no implementation exists, render a labeled **Specification only** state, not a broken or misleading preview. Navigation, filter, and searchable text work from statically generated content wherever feasible. Client-side code loads only for interactive examples.

## Migration and URL stability

- Preserve registered paths and IDs. Use explicit `preview_path` and `implementation_path` metadata rather than deriving them from titles.
- Prefer `/catalog/:layer/:slug` for humans, with canonical-ID resolution and redirects for renamed slugs.
- Static documentation should remain readable and crawlable without needing preview hydration.
- Keep generated search artifacts out of the manual source of truth. Document any build-derived index and compare it to root registry.
- Before moving anything: inventory inbound relative links, archive anchors, current `find_concept.py` matches and prior URL stability.

## Architecture options and choice

| Option | Advantage | Cost | Decision |
| --- | --- | --- | --- |
| Docs-only catalog | Fast search | No working visual demo | Retain as source, not full outcome |
| Monorepo packages | Consuming-app distribution | Versioning/build/publish overhead | **Defer** |
| Static site + embedded reference implementations | Visual + accessible source + low operational overhead | Needs site build and preview isolation | **Preferred** |
| Browser-only dynamic DB catalog | Editable runtime entries | Risks duplicate truth and retrieval lock-in | **Reject** at this stage |

**Next acceptance gate:** implementation starts only after schema review, minimum preview contract and a route/ID resolution test are approved.
