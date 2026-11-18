# Task-first catalog reorganization

Source baseline: `71ba62936eb3d0f25f3f63d6757391ee5d3cfdb4` (54 concepts; 12 source-linked examples). This is a reversible draft-PR migration, not approval or an automatic release.

## Ownership boundaries

- `tasks/`: discover canonical patterns by user goal; never duplicate normative concepts
- `knowledge/`: foundations, UX/content/research guidance, architecture
- `specifications/`: component, pattern and experience contracts
- `examples/`: reviewed visuals and composed experience studies; source-linked interactive demonstrations remain under `site/src/implementations`
- `research/`: provenance and actual research artifacts, when available
- `packages/`: future installable libraries, not currently present
- `catalog/`: sole metadata registry; existing IDs never change during folder moves
- `site/`: derived browser and executable preview host

## Migration guarantees

1. Preserve an exact original-tree checkpoint in Git history under `temp/legacy/`.
2. Move every tracked file to an explicit destination, avoid duplicate normative Markdown.
3. Keep IDs, aliases, canonical `implementation.source_path`, and existing public URLs stable.
4. Rewrite and validate links, tests, registry paths, agent lookup, site categories, and source displays.
5. Check CI and manual accessibility status honestly; never claim a preview is a production package.
6. Remove `temp/legacy/` from final branch tree once verification is complete; do not merge an incomplete migration.

Run `python3 scripts/migrate_structure.py --check` after migration to detect files stranded in retired root directories.
