# Static frontend shell

The site is a generated knowledge browser, not a product application or published UI package. Shell rendering is intentionally free of network actions and domain mutations.

| Shell component | Purpose | Context | Relevance |
| --- | --- | --- | --- |
| `navigation()` | Consistent Home, Tasks, Browse, Search landmarks and active-page state | All pages | Orientation and keyboard navigation |
| `concept_card()` | Summarize canonical entry and searchable wording | Catalog and search grids | Discoverability with clear resource labels |
| `concept_metadata()` | Show identity, type and editorial lifecycle | Concept detail page | Prevent unreviewed guidance from appearing approved or production-ready |
| `task_index()` | User-goal entry cards linking canonical concept IDs | Tasks landing | Task-first discovery without competing spec copies |
| `site/static/shell/query.js` | Small client-side query tokenizer and matcher | Progressive search enhancement | Keeps query logic separately testable and preserves no-JS navigation |

Composition order: canonical registry → task-intent adapter → view components → static page generation → progressive client-side filtering. Visual styles belong in `site/static/shell/shell.css`; global tokens remain in `site/static/styles.css`.
