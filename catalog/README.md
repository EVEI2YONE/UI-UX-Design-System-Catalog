# Catalog lookup registry

[`index.json`](index.json) is the **canonical metadata inventory**. Each entry has a stable ID, canonical path, summary, synonyms (`aliases`), primary conceptual layer, content kind, status, and multiple topical `domains`.

## Search

```bash
python3 scripts/find_concept.py focus
python3 scripts/find_concept.py "error recovery"
python3 scripts/find_concept.py --layer intelligence
python3 scripts/find_concept.py --domain accessibility
```

An empty query lists all entries. Search matches partial text across titles, IDs, summaries, aliases and domains. Multiple entries may share an alias: this is useful when the same task spans concepts. Registry results point to one canonical page per entry.

## Levels and categories

- `layer` represents the concept's primary position in the **10-layer conceptual taxonomy** (`context`, `principles`, `behavior`, `tokens`, `foundations`, `primitives`, `components`, `patterns`, `experiences`, `intelligence`, or `cross-cutting`).
- `kind` describes the artifact, such as `guideline`, `contract`, `policy`, or `checklist`.
- `domains` are cross-cutting topical search terms; they do not force duplicate copies of a page.
- `status` describes the **catalog entry's review lifecycle**, not a claim that code exists.

The registry is intended for discoverability, not an implementation API. If a concept moves, preserve its ID, update the canonical path, and provide redirects/migration where old links were published. See [Contributing](../CONTRIBUTING.md).
## Agent-oriented lookup

The [JSON Schema](schema.json) describes the registry record. Batch 1–3 scaffold entries additionally provide `use_when`, `avoid_when`, `related`, `depends_on`, `owner`, and nullable `reviewed_at`; other entries can adopt these fields incrementally. The registry remains the only machine-readable metadata source. Related references are canonical IDs, not duplicate Markdown files.

```bash
python3 scripts/find_concept.py 'loading button' --json
python3 scripts/find_concept.py architecture.component-model
python3 -m unittest discover -s tests -v
```

Results are ranked by exact ID, exact alias, exact title, then partial text matches. Read and verify the returned entry; rank is not a recommendation or quality certification. See [agent protocol](../AGENTS.md).


## Measurement and governance queries

```bash
python3 scripts/find_concept.py 'task completion rate' --json
python3 scripts/find_concept.py 'catalog promotion' --json
python3 scripts/find_concept.py 'documentation checks' --json
```

These resolve to canonical guidance, lifecycle policy and quality checklist entries. All remain `proposed`; no observed UX outcomes or implementation conformance are implied.

## Batch 6 — consistent agent retrieval

All entries, including [role-aware workspaces](../patterns/role-aware-workspaces-and-context-switching.md), now provide owner, review date, use/avoid guidance, related IDs and dependencies. The resolver normalizes case/punctuation, ranks exact IDs and aliases first, supports `--status` and `--limit`, and excludes `avoid_when` from positive search scoring. That field still appears in JSON results so agents can interpret contraindications.

```bash
python3 scripts/find_concept.py 'role switching' --json --limit 3
python3 scripts/find_concept.py 'modal-dialog' --status proposed
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
```

The [schema](schema.json) specifies fields; the dependency/reference validator uses the Python standard library rather than a complete JSON Schema engine. Documentation checks do not establish verified accessibility or implemented component quality.


## Batch 10 — task-based retrieval coverage

The existing 40 concepts remain canonical; retrieval metadata now maps user task phrases such as `hosted authentication`, `human approval workflow`, `feature flags`, `data migration`, `clickable row`, `dialog focus return` and `global CSS` to their owning pages. This is alias and `use_when` enrichment, not concept creation or promotion. See [Batch 10 evidence ledger](../planning/little-wins-batch-10-context-and-gap-ledger.md) and [regression tests](../tests/test_little_wins_knowledge_coverage.py). Rank indicates retrieval relevance, not implementation correctness.

## Application architecture task lookup (Batches 13–16)

Use `architecture.application-selection` for profiles and example trees, `architecture.module-boundaries` for feature/domain/shared ownership and developer findability, `architecture.evolution` for migration/fitness, and `architecture.enterprise-multiapp` for monorepo/multirepo/microfrontend selection. These are proposed application-code guidelines rather than a restructuring of the catalog itself. [Batch context and coverage](../planning/application-architecture-batches-13-16-context-and-gaps.md).
