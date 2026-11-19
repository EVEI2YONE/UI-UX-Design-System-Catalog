# UI/UX Design System Catalog

> **Status:** proposed, **guidance-only** knowledge catalog. It contains design concepts, specifications and decision frameworks—not an installable component library, runnable UI examples or evidence of product accessibility conformance.

## Start with the user's task

Use the [task discovery index](tasks/README.md) for finding, comparing, completing, confirming and recovering. Each task points to a canonical pattern and related guidance; it is not a second set of normative instructions. The [web reference](site/README.md) renders the same registry and source Markdown.

## Browse by concept type

| Area | Purpose |
| --- | --- |
| [Foundations](knowledge/foundations/README.md) | Visual hierarchy, tokens, icon semantics and design craft |
| [Guidance](knowledge/guidance/README.md) | Accessible, localized, measurable, evidence-aware UX |
| [Architecture](knowledge/architecture/README.md) | Reusable component boundaries and application structure |
| [Component specifications](specifications/components/README.md) | Control contracts, state and focus semantics |
| [Interaction patterns](specifications/patterns/README.md) | Search, forms, navigation, recovery, settings, approvals |
| [Experience specifications](specifications/experiences/README.md) | Cross-pattern reference journeys |
| [Governance](governance/README.md) | Lifecycle, quality gates and source review |
| [Research](research/README.md) | Methods and source provenance (no completed studies claimed) |
| [Examples](examples/README.md) | Written illustrative scenarios and design comparisons (not runnable components) |

## How to use a concept

1. Search by task or [concept ID](catalog/README.md) with `python3 scripts/find_concept.py "form submission failed" --json`.
2. Read the canonical page's **use when**, **avoid when**, variants, states, accessibility, content and verification requirements.
3. Check the registry's **kind**, **status**, **owner** and **reviewed_at** before treating the entry as established practice. Today all entries are proposed and no editor review is recorded.
4. Follow `related` and `depends_on` as needed. Component specifications document meaning, states and accessibility; they are not shipped UI code.
5. Check cited standards and evidence for applicability. Record independent user research, accessibility and product outcomes before claiming improvements.

## Repository contracts

[The canonical catalog](catalog/index.json) owns IDs and status; Markdown at each `path` owns the actual guidance. [Task mappings](tasks/index.json) are retrieval pointers, not authority. The [catalog application shell](catalog/core/README.md) handles task lookup and route stability; [site shell components](site/shell/README.md) render task lists, cards, metadata and navigation. Current provenance and evidence belong with the concept, not in a development timeline.

Contribute through [the concept-first policy](CONTRIBUTING.md). Run `python3 scripts/validate_catalog.py`, `python3 scripts/check_editorial.py`, `python3 -m unittest discover -s tests -v`, and `python3 site/build.py`. No production release or UX study is implied by passing repository tests.
