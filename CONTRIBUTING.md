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
