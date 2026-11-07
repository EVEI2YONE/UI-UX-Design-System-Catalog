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