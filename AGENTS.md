# Agent lookup protocol

This repository is a **reference catalog of proposed UI/UX knowledge**, not a shipped component package. Begin with [the canonical registry](catalog/index.json), not a recursive read of all Markdown.

1. Search by exact canonical ID or task: `python3 scripts/find_concept.py "loading button" --json`. For aliases, the resolver ranks exact IDs first, then exact aliases, then title/text. Its ranking is a convenience, not a guarantee that a result fits the task.
2. Read the returned `path` and check `status`, `kind`, `owner`, `reviewed_at`, `use_when` and `avoid_when` where present. `proposed` is not approved or implemented.
3. Follow `related` and `depends_on` canonical IDs only as needed. The registry is the **single** source of identity and retrieval metadata; Markdown pages own guidance and examples.
4. Cite the canonical ID and relative path when using guidance. Distinguish catalog rules from evidence about a target application. Do not claim tested accessibility, production code or benchmarked UX without independent proof.
5. Prefer reuse/extension before creating a new concept. If introducing one, update `catalog/index.json`, the relevant section README, sources/verification, and tests.

## Current retrieval guidance

Use the canonical index and exact IDs first, then read task-relevant source pages. For application structure use [architecture navigation](architecture/README.md); for component contracts use [component navigation](components/README.md); for tasks and journeys use [patterns](patterns/README.md); for UX research, accessibility and cross-cutting rules use [guidance](guidance/README.md).

All catalog entries are currently proposed. Do not infer a published component, tested deployment, accessibility certification or approved standard from registry metadata or the documentation validator. Product-specific case studies and historical batch context live in the [archive](archive/README.md); follow the current canonical pages instead of applying historic PR assumptions.

Before contributions, validate the registry and run the Python test suite. Preserve IDs, update links and lookup assertions when renaming/moving files, and record unexecuted manual or product tests as NOT VERIFIED.
