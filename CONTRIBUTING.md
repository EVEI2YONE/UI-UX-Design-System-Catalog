# Contributing concept-first guidance

This is a reusable UI/UX knowledge base. Its normative pages must explain the concept itself: applicability, decisions, states, alternatives, examples, source limitations, accessibility/localization and verification. **Do not include past commits, PR numbers, batch/phase labels, context ledgers or the chronology of authoring in concept text.** Git history is sufficient for change history.

## Before editing

1. Search [the registry](catalog/index.json) and [task index](tasks/index.json) for an existing owner. Reuse or extend before minting new identities.
2. Define the user/design decision, when the advice helps or harms, and the evidence sources and limits.
3. Use [the concept template](templates/concept-entry.md) and current headings. Merge supplementary rules into the appropriate concept section instead of appending dated extensions.
4. Keep canonical IDs and public URLs stable. Link reusable semantics and patterns by ID instead of duplicating paragraphs.
5. Distinguish proposed contracts, illustrative prose, researched findings and independently verified product behavior. Do not register or add executable component demos, preview fixtures or installable packages.

## Verify and review

```bash
python3 scripts/validate_catalog.py
python3 scripts/check_editorial.py
python3 -m unittest discover -s tests -v
python3 site/build.py
python3 -m unittest discover -s site/tests -v
node --test site/tests/*.test.cjs
```

For browser and assistive-technology checks, document the exact tool, environment, observed result and limitations. Record unexecuted checks as `NOT VERIFIED`. No fabricated participant findings, approvals or successful deployments.

Each change must state why the concept is improved, links to its source evidence, affected consumers/IDs, accessibility and localization implications, test results and review owner. Only a human reviewer may record a completed editorial review or approve a merge. `proposed` does not mean production-ready.
