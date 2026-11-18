# 04 — Registry, agent search and visual discovery contract

## Objective

Humans browse a responsive site; agents search the same canonical registry and retrieve docs, source, scenarios, and preview provenance directly. Neither group must use a specific application runtime to discover a concept.

## Observed current contract

`catalog/index.json` is the authoritative ID registry. The current `catalog/schema.json` defines strict entries and denies unknown properties. `AGENTS.md` directs agents to `scripts/find_concept.py` and then the returned canonical `path`. Existing `related` and `depends_on` contain canonical IDs and should remain valid. This is the compatibility baseline.

## Proposed optional extensions — not a replacement schema

Add optional fields to the existing per-entry schema after review; **keep all existing required fields**:

```json
{
  "id": "component.button",
  "path": "components/button/spec.md",
  "implementation": {
    "status": "reference",
    "source_path": "site/src/implementations/components/button/Button.tsx",
    "preview_path": "/catalog/components/button",
    "scenario_manifest": "site/src/implementations/components/button/scenarios.ts",
    "evidence_path": null
  },
  "capabilities": ["action", "pending-state", "keyboard-activation"]
}
```

Only the `implementation` and `capabilities` fields are *new illustrative additions*; all existing ID/path fields remain authoritative. Actual schema must enumerate valid statuses (e.g., `none|reference|experimental|verified`), restrict paths, and accept optional properties without weakening unrelated validation. Avoid declaring `verified` merely because code or unit tests exist.

## Required invariants

1. **One canonical identity:** `id` never derives from title, route, filename, or website wording.
2. **Documentation continuity:** the existing Markdown `path` remains stable even if visual implementation changes.
3. **No second hand-curated index:** `site/src/previews/preview-registry.ts` is a *typed mapping of executable renderers keyed by canonical IDs*; it must not duplicate descriptions, owners, aliases or relations. The root registry remains the only metadata source.
4. **Deterministic discovery:** existing lookup ranking for exact ID and aliases remains stable; add new fields to search only with regression tests and an intentional ranking rule.
5. **Path safety:** registry file references resolve within the repo, not remote arbitrary URLs; no dynamic import of user-provided paths.
6. **Explicit absence:** a spec-only entry returns `implementation.status = none` or omits the implementation object, and website displays 'Specification only.'
7. **Static readability:** documentation content and essential navigation render server-side/statistically, without requiring browser execution.
8. **Agent-oriented affordance:** expose canonical ID, source path, scenario names, status, content last-reviewed information, and related IDs in static page metadata.
9. **Source provenance:** source viewer uses the actual maintained implementation file, not a manually transcribed copy. Support attributions and licensing where third-party code is present.
10. **Version compatibility:** schema changes are versioned; old consumers receive unchanged required properties and old lookup calls retain expected results.

## Website flow

```text
user or agent query
    -> catalog/index.json
    -> stable canonical ID + text metadata
    -> Markdown specification (normative)
    -> optional executable source + scenario fixture
    -> visual preview or explicit spec-only fallback
    -> links to related and dependent concepts
```

## Search behavior acceptance cases

| Query | Expected result | Regression guard |
| --- | --- | --- |
| `component.button` | Exact canonical Button entry | Exact ID ranks above alias |
| `loading button` | Button contract, then related recovery guidance | No new preview card displaced exact established match |
| `review decision uncertain result` | Relevant recovery/approval guidance and reference feature if registered | Pending vs confirmed semantics visible |
| `table selection and bulk edit` | Data table / advanced interaction pattern, feature if applicable | No misleading grid semantics |
| `accessibility high contrast dialog` | Dialog + accessibility + token guidance | Relations preserved |
| Unknown concept | Empty/no match with next-step search suggestions | No invented entry |
| Spec-only existing entry | Detail and guidance load, preview unavailable | No broken iframe or 'interactive' claim |

## CI expectations

- Validate `catalog/index.json` with expanded schema and existing Python catalog checks.
- Detect duplicate IDs, missing Markdown, unresolved related IDs, invalid implementation/source paths, dead preview routes, missing scenario exports, forbidden path traversal.
- Assert each registered preview imports the intended *real* implementation, rather than a stand-in visual mock.
- Test existing `find_concept.py` canonical IDs and aliases before and after schema migration.
- Generate site static search assets from the index and ensure parity.
- Test no-JS documentation/search fallback and representative keyboard navigation.
- Do not infer production security or full accessibility from these automation checks.

## Future options deliberately deferred

Semantic vector indexing, an MCP server, public search API, GitHub Actions publishing, downloadable bundles and npm packages are optimization choices after validating that structured index search and direct repo retrieval meet user and agent needs.
