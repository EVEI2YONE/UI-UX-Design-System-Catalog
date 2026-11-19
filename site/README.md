# Static UI/UX knowledge browser

This is a locally built, responsive documentation browser generated from the canonical [registry](../catalog/index.json) and source Markdown. It is not a deployable UI package, a production authorization implementation or a claim of accessibility conformance.

## Run and validate

Requires Python 3.10+ to generate the site; Node.js 18+ for reference checks.

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
| `site/build.py` | Static composition, Markdown rendering, safe source links and preview embedding |
| `site/static/search.js` | Progressive client-side filtering and URL/history state; the full catalog remains available without JavaScript |
| `site/src/implementations/` | Source-matched synthetic example implementations, fixtures and styles |
| `site/src/previews/` | Isolated iframe scenarios and preview host |
| `site/tests/` | Static build, source parity, keyboard, browser and automated accessibility regressions |

The [catalog shell](../catalog/core/README.md) separately owns route stability and task-intent resolution. The website uses those helpers; it does not create a second authoritative copy of guidance.

## Reading an entry

Review **artifact type**, **editorial status**, **implementation availability**, source references and related concepts independently. Interactive references have explicit synthetic/test limits; no runnable reference is indicated honestly. For research and source provenance start with [references](../governance/references.md). Every user-facing concept is sourced from current canonical Markdown, not historical process records.
