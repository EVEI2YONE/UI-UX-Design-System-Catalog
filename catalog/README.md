# Canonical concept registry

`index.json` is the **single source of identity and lifecycle metadata** for this knowledge base. `schema.json` defines each entry's durable ID, title, canonical Markdown path, conceptual layer, artifact kind, proposed/stable lifecycle, summary, task aliases, domains, when to use/avoid, cross-references, dependencies, ownership and review date.

## Search

```bash
python3 scripts/find_concept.py "recover from a failed submission" --json
python3 scripts/find_concept.py "modal dialog" --limit 3
python3 scripts/find_concept.py --layer patterns
python3 scripts/find_concept.py --domain accessibility
```

Search ranks exact IDs, aliases and titles first, then recognized task-intent phrases and ordinary text. Task phrases are declared in [the task index](../tasks/index.json) and reference existing canonical IDs. A ranked match is a discovery aid, not proof the design is applicable.

## Authority and relationships

- `kind` distinguishes guideline, contract, specification, policy, checklist or example.
- `status` is the editorial review lifecycle and **not** code availability.
- `implementation` is a separate optional pointer to a runnable, synthetic reference under `site/src/implementations/`.
- `owner` and `reviewed_at` are evidence of responsibility only when actually assigned and reviewed.
- `related` points to useful context; `depends_on` is an acyclic prerequisite relationship.
- Source Markdown contains current decisions, examples, limitations and actual references. It must not describe the drafting history.

Keep IDs and public routes stable when source files move. New entries require the [concept template](../templates/concept-entry.md), reviewed sources and `scripts/validate_catalog.py`. See [the retrieval shell](core/README.md) and [contributor policy](../CONTRIBUTING.md).
