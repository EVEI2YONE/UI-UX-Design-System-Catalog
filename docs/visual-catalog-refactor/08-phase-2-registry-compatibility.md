# 08 — Phase 2 metadata and agent retrieval compatibility

**Phase:** 2 — metadata and discovery compatibility  
**Delivery:** successive commits on draft PR #16  
**Source baseline:** `main` at `3b933abea778122dece31af7496f409028ed6198`  
**Status:** schema and docs committed; GitHub Actions CI passed for implementation commit `6240abfa9b6209166aa2f76aa7595e660ca17857`

## Context gathered

Existing `catalog/schema.json` forbids unexpected entry properties. The standard-library `scripts/validate_catalog.py` checks allowed/required schema fields, canonical document existence and some metadata; `scripts/find_concept.py` ranks exact IDs > aliases > titles > matches using existing text, and `tests/test_lookup.py` protects a substantial number of specific matches. The registry has 53 entries and six current component specs. No reference website source code is present yet, so linking a pretend preview would make the catalog misleading.

## Decisions and implementation

| ID | Decision | Disposition |
| --- | --- | --- |
| P2-D01 | Keep all existing required schema properties and `catalog/index.json` identifiers/paths/layers | Implemented in branch |
| P2-D02 | Add optional `capabilities` string-list to entry schema | Implemented |
| P2-D03 | Annotate six existing control entries with concise capabilities; no aliases changed | Implemented |
| P2-D04 | Add optional typed `implementation` object with status/source/scenario/route and optional evidence | Implemented in schema and validator |
| P2-D05 | Never register source/preview metadata until files genuinely exist | No implementation objects added |
| P2-D06 | Preserve exact legacy lookup scoring; do not index capabilities yet | Lookup script unchanged |
| P2-D07 | Reject unsafe or missing source/scenario files and malformed routes in validator | Implemented |
| P2-D08 | Keep executable renderer map generated/typed, not manually duplicated catalog metadata | Specified, Phase 3/4 implementation deferred |

## Schema contract

`implementation` is optional, with status `reference`, `experimental` or `verified` and required `source_path`, `scenario_manifest`, `preview_path`. These paths must refer to checked-in implementation source and a catalog route. `evidence_path` is optional except when `status=verified`, which requires it. **This is documentary evidence presence, not automated human accessibility or performance certification.** Absent implementation means spec-only.

`capabilities` is an optional unique nonempty list of user-facing function labels. It does not influence `find_concept.py` scores yet. Avoid semantically overloading existing `aliases` or `domains`.

## Verification record

| Check | Evidence/result | Status |
| --- | --- | --- |
| Legacy 53 IDs and 53 canonical paths remain | Direct GitHub JSON compare: 53/53 entries; existing IDs, paths, layers, statuses, aliases, relations and all legacy properties unchanged | PASS — structural comparison |
| Legacy top-ranked queries remain | Agent-context inspection for loading button, modal dialog, component hierarchy, settings | PASS — in-memory ranking replay; Python test suite NOT VERIFIED |
| Strict JSON Schema extension | `catalog/schema.json` optional props and strict implementation object | COMMITTED |
| Validator optional checks | `scripts/validate_catalog.py` new helper | PASS in GitHub Actions on `6240abf` |
| New unit regression tests | `tests/test_visual_catalog_metadata.py` | PASS in GitHub Actions on `6240abf` |
| Existing full Python unittest suite | `python3 -m unittest discover -s tests -v` | PASS in GitHub Actions on `6240abf` |
| Existing catalog validator | `python3 scripts/validate_catalog.py` | PASS in GitHub Actions on `6240abf` |
| Runtime visual/a11y/performance tests | Not applicable until site is built | NOT APPLICABLE |

## Environmental limitation

GitHub connector can read and edit repository content, but a direct container Git clone failed with DNS resolution for github.com. Accordingly, **do not claim the Python validator, unittest suite or build ran** from the working checkout. GitHub Actions supplied executable CI evidence on commit `6240abfa9b6209166aa2f76aa7595e660ca17857` via successful workflow run [42484090737](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/actions/runs/42484090737). This workflow's `catalog-validation.yml` runs the catalog validator, a lookup smoke test and the Python unittest discovery suite. A local container execution is still unavailable, and the latest documentation-only follow-up commit requires its own CI completion before final review.

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
python3 scripts/find_concept.py "loading button" --json
python3 scripts/find_concept.py "component hierarchy" --json
```

## Additional verifications executed through the GitHub connector

The base registry and current branch registry were parsed and compared property-by-property for all 53 entries; the entire legacy field set is unchanged, and only six new optional capability lists were found. The strict schema retains its original required properties. An in-memory replay of the published lookup scoring produced the expected top matches for `loading button`, `modal dialog`, `component hierarchy` and `settings`. This is meaningful structural/retrieval evidence but **not** a substitute for running Python tests. GitHub Actions workflow [42484090737](https://github.com/EVEI2YONE/UI-UX-Design-System-Catalog/actions/runs/42484090737) completed **successfully** for `6240abf`, including validation and unittests. Later documentation edits require an updated head check.

## Risks and release guardrails

1. Schema regexes are **not** a complete JSON Schema validator in the standard Python script; the custom helper complements the schema and its negative tests.
2. `verified` in a reference metadata field **cannot mean WCAG compliant or production ready** without human evidence.
3. Preview/source references must not be added ahead of a committed site and deterministic fixture.
4. `implementation.status` and catalog `status` are **distinct lifecycles**. An unreviewed guidance entry must stay `proposed` even if a demo exists.
5. Future capability-based ranking needs task-based relevance tests and explicit acceptance; not silently enabled in Phase 2.

## Phase gate

**Automated validation passed for the Phase 2 code commit; maintainer architecture/retrieval approval remains pending.** Phase 3 site implementation should not be described as approved on this document alone.
