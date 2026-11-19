# Static UI/UX knowledge browser

This is a locally built, responsive documentation browser generated from the canonical [registry](../catalog/index.json) and source Markdown. It is not a deployable UI package, a production authorization implementation or a claim of accessibility conformance.

## Run and validate

Requires Python 3.10+ to generate the site; Node.js 18+ for the small documentation search-helper tests.

```bash
python3 scripts/validate_catalog.py
python3 scripts/check_editorial.py
python3 site/build.py
python3 -m unittest discover -s site/tests -v
node --test site/tests/*.test.cjs
python3 -m http.server 8000 --directory site/dist
```

Open `http://localhost:8000/`. Generated output lives under ignored `site/dist/`, with root-relative URLs; deploy only after base-path and security review. No public deployment is established by this repository.

## Presentation and interaction architecture

| Area | Responsibility |
| --- | --- |
| [`site/shell/`](shell/README.md) | View shell: navigation, task cards, concept cards, metadata. Static HTML, semantic markup and escaped content |
| [`site/static/shell/`](static/shell/query.js) | Progressive search helpers and task layout styles. No backend or persistent side effects |
| `site/build.py` | Static composition, Markdown rendering and safe canonical source links |
| `site/static/search.js` | Progressive client-side filtering and URL/history state; the full catalog remains available without JavaScript |
| `site/tests/` | Static build, source consistency, browser navigation and automated accessibility smoke checks |

The [catalog shell](../catalog/core/README.md) separately owns route stability and task-intent resolution. The website uses those helpers; it does not create a second authoritative copy of guidance. The browser prioritizes exact canonical ID, alias, title and primary task-intent matches over related or broad matches; clear/reset and URL history remain unchanged. Validate ranking with `node --test site/tests/shell-query.test.cjs` and the browser audit.

## Reading an entry

Review **artifact type**, **editorial status**, owner, source references and related concepts. The generated documentation site is a reading and discovery tool; it does not host runnable component or pattern previews. For research and source provenance start with [references](../governance/references.md). Every user-facing concept is sourced from current canonical Markdown, not historical process records.
