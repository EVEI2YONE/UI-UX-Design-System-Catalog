# Catalog application shell

This is the minimal, read-only application boundary around the canonical catalog. The registry remains `catalog/index.json` and concept Markdown remains normative. No new component library or second registry is introduced.

| Module | Purpose | Context | Relevance |
| --- | --- | --- | --- |
| `navigation.py` | Stable categories and URLs | Web publishing and bookmarks | Physical paths can evolve without breaking published concept routes |
| `discovery.py` | Validate task-to-canonical-ID references and resolve intent phrasing | CLI and website search | People can find guidance in their own words without duplicate rules |
| `editorial.py` | Enforce concept-only documentation policy | CI and contributor review | Development-history notes cannot leak into guidance |

Inputs: `catalog/index.json`, `tasks/index.json`, canonical Markdown. Outputs: read-only categorization, search aliases, lint findings. Ownership: catalog maintainer for APIs; concept reviewers for semantic accuracy. Never interpret keyword ranking as a normative recommendation.
