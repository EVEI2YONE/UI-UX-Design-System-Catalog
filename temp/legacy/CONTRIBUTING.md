# Contributing to the UI/UX Design System Catalog

We favor **small, evidence-led, canonical guidance** over volume. The catalog contains reusable knowledge; product-specific defects, unreviewed screenshots, and tool-specific agent prompts generally belong elsewhere.

## Before drafting

1. Search [the index](catalog/index.json) using `python3 scripts/find_concept.py "term"`, aliases, and nested READMEs.
2. Document the intended users, decisions supported, and why existing guidance cannot be reused or extended.
3. Choose **reuse, expand, merge, create, deprecate, or defer**. Keep app-local workflow details out of shared components.
4. Link authoritative source(s), edition/date, applicability, tradeoffs and known unknowns. For UX outcomes, distinguish observations from hypotheses.

## Add or modify a concept

- Start with [the concept entry template](templates/concept-entry.md). Every canonical page should explain purpose, use and anti-use, contract/behavior where applicable, inclusive and locale requirements, examples, tests, owner/status, and related concepts.
- Add or update one entry in [`catalog/index.json`](catalog/index.json): unique durable `id`, `title`, `summary`, `path`, `layer`, `kind`, `status`, `aliases`, `domains`.
- Update relevant section README and root README discovery path **when navigation changes**. Prefer links to canonical text rather than copying paragraphs into multiple pages.
- Treat working code, a design spec, a guideline, and a reference illustration as different deliverables. Do not mark any asset as production-ready without corresponding implementation evidence.
- Preserve stable IDs and URLs. Renames should retain an alias/redirect and explain migration; breaking API changes need version and consumer impact notes.
- Avoid unowned components, arbitrary variants, mega-components, repeated raw tokens, unbounded styling escape hatches, and framework assumptions.

## Pull request checklist

- [ ] Searched existing concepts and aliases; explained reuse or new-entry decision.
- [ ] Added purpose, when to use/avoid, examples, limitations and review owner.
- [ ] Explicit accessible behavior, states, keyboard/focus, reflow and responsive expectations where relevant.
- [ ] Considered translation growth, locale formats, RTL, themes and reduced motion where relevant.
- [ ] Updated registry, nested/root navigation and changelog as needed.
- [ ] Linked current primary references with scope and review date.
- [ ] Ran `python3 scripts/validate_catalog.py` and recorded actual output.
- [ ] Recorded manual checks as `PASS`, `FAIL`, `NOT VERIFIED`, or `NOT APPLICABLE`.
- [ ] Listed affected consumers, compatibility changes, rollout or deprecation as appropriate.

## Review and lifecycle

`proposed` → `experimental` → `stable` is a possible path, not an automatic promotion. `deprecated` and `removed` require migration notice and owner review. A conceptual page can become stable without a published coded component, but must always describe which type of artifact it represents.

Open focused PRs from a branch. **Do not push catalog changes directly to the default branch or merge without review/approval.** If the repository has no initial commit, an owner must first initialize the default branch as a separately reviewed bootstrap operation.

## Agent retrieval and lifecycle maintenance

Keep metadata in the single [canonical registry](catalog/index.json) with [schema](catalog/schema.json). Define task-positive `use_when` and real contraindications in `avoid_when`, not keyword stuffing. Use canonical IDs in `related` and cycle-free `depends_on`; record `unassigned` until an owner accepts responsibility. Leave `reviewed_at` null until a human review happens. If a new dedicated concept supersedes a generic match, update lookup regression tests intentionally. Run the validator and lookup tests before review; mark missing manual evidence `NOT VERIFIED`.


## Visual catalog contribution and release-evidence workflow (Phase 9)

The site at `site/` is a source-derived documentation browser and **trusted, synthetic reference runtime**, not an installable design-system package. The canonical ID and review lifecycle remain exclusively in `catalog/index.json`. Each concept's normative content remains in its Markdown `path`.

For a new or changed **reference implementation**, preserve the associated canonical ID, link a real `source_path` and colocated `scenario_manifest` only after those files exist, provide matching CSS and deterministic fixtures, and ensure the preview route matches its canonical entry. When a synthetic `mock-adapter.js` exists, keep its data in-memory and reviewed, and explicitly distinguish UI affordances from server authorization. The static builder renders **exactly the source that it displays**, and all other concepts must remain clearly specification-only. Do not add or publish a package merely to show an example.

For a **new concept**, first search the registry by exact ID, aliases, task and related capability. Include a documented reuse/extend/merge/create decision, user job and anti-use, provenance, independent credible reuse contexts for a feature, canonical path, relationships, and ownership. Do not register feature concepts before the ownership/reuse decision, and do not copy a product-specific workflow into shared rules.

For a **metadata or search change**, update [task acceptance cases](tests/fixtures/phase9_retrieval_cases.json) only if the relevance change is deliberate, review its effects on ambiguous and negative queries, and preserve all existing IDs and migration paths. The lookup algorithm intentionally does not score `capabilities` or `avoid_when` positively. Do not force an ambiguous query to a single entry without evidence. Run:

```sh
python3 scripts/validate_catalog.py
python3 scripts/audit_discovery.py --output site/artifacts/phase9/discovery-audit.json
python3 -m unittest discover -s tests -v
python3 site/build.py
python3 -m unittest discover -s site/tests -v
```

CI also runs the actual Node source-behavior suites and Chromium/axe checks. Attach the workflow link and artifact IDs. State what **was** and **was not** checked; axe's automated findings, simulated DOM tests, static payload budgets and screenshot generation are not a manual screen-reader, zoom, visual design, security signoff or production field-performance result.

**Release/rollout responsibility:** An approved reference does not automatically promote the canonical guidance lifecycle. Any move from `proposed` needs explicit owner/reviewer evidence; `reviewed_at` must not be fabricated. Before requesting ready-for-review or merging a broad refactor, finish the [Phase 10 release checklist](docs/visual-catalog-refactor/06-migration-pr-roadmap.md), reconcile with `main`, confirm deployment/base-path and licensing decisions, assess security/CSP and inspect the uploaded browser evidence. Revert individual optional implementation mappings first if a preview blocks the release, retaining canonical Markdown and IDs.

See [Phase 9 source trace and handoff](docs/visual-catalog-refactor/15-phase-9-agent-governance-handoff.md) for known retrieval gaps and outstanding named approvals.
