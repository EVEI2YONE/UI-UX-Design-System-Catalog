# Agent lookup protocol

This repository is a **reference catalog of proposed UI/UX knowledge**, not a shipped component package. Begin with [the canonical registry](catalog/index.json), not a recursive read of all Markdown.

1. Search by exact canonical ID or task: `python3 scripts/find_concept.py "loading button" --json`. For aliases, the resolver ranks exact IDs first, then exact aliases, then title/text. Its ranking is a convenience, not a guarantee that a result fits the task.
2. Read the returned `path` and check `status`, `kind`, `owner`, `reviewed_at`, `use_when` and `avoid_when` where present. `proposed` is not approved or implemented.
3. Follow `related` and `depends_on` canonical IDs only as needed. The registry is the **single** source of identity and retrieval metadata; Markdown pages own guidance and examples.
4. Cite the canonical ID and relative path when using guidance. Distinguish catalog rules from evidence about a target application. Do not claim tested accessibility, production code or benchmarked UX without independent proof.
5. Prefer reuse/extension before creating a new concept. If introducing one, update `catalog/index.json`, the relevant section README, sources/verification, and tests.

**Batch 1 starting points:** [Design principles](foundations/design-principles.md), [tokens and themes](foundations/design-tokens-and-themes.md), [component model](architecture/component-model.md), and [component contracts](architecture/component-contracts.md).

For humans, see [README](README.md). For schema and lookup behavior, see [catalog lookup](catalog/README.md). Validate with `python3 scripts/validate_catalog.py` and `python3 -m unittest discover -s tests -v`.

Do not edit the default branch directly or treat a documentation specification as an executable component.

**Batch 2 starting points:** [Task flows and information architecture](patterns/task-flows-and-information-architecture.md), [interaction states and recovery](patterns/interaction-states-and-recovery.md), [accessibility](guidance/accessibility.md), and [internationalization](guidance/internationalization.md). Example queries: `python3 scripts/find_concept.py 'information architecture' --json`, `python3 scripts/find_concept.py 'network timeout' --json`, `python3 scripts/find_concept.py 'keyboard navigation' --json`, `python3 scripts/find_concept.py 'text expansion' --json`. Validate fit against the canonical page before adopting a result.

**Batch 3 starting points:** [UX measurement](guidance/ux-measurement.md), [catalog lifecycle](governance/lifecycle-and-decisions.md), and [quality gates](governance/quality-gates.md). Example queries: `python3 scripts/find_concept.py 'task completion rate' --json`, `python3 scripts/find_concept.py 'catalog promotion' --json`, `python3 scripts/find_concept.py 'documentation checks' --json`. For measurement, distinguish unknown baselines from zero. For governance, distinguish documentation status from shipped code; use actual test evidence, not assumptions.

**Batch 4 core components:** Search `component.button`, `component.input`, `component.select`, `component.checkbox`, `component.dialog` and `component.field` through the canonical registry; use [component index](components/README.md) for navigation. Read `related` and `depends_on` selectively. All are proposed specification documents without runnable code; the generic [component contract](architecture/component-contracts.md) remains the cross-component rule source.

**Batch 5 composed patterns:** Use `pattern.forms`, `pattern.navigation`, `pattern.search-filter`, `pattern.data-tables` or `pattern.feedback` for an end-to-end composition decision; use [patterns index](patterns/README.md) for links. Prefer these exact IDs to broad search when possible, and inspect component dependencies before implementing anything. A pattern does not authorize application routing, network requests, or claims of tested accessibility.
