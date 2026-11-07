#!/usr/bin/env python3
"""Validate canonical entries, section indexes and relative markdown links."""
import json
import datetime
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / 'catalog/index.json'
SECTIONS = ('catalog', 'foundations', 'architecture', 'components', 'patterns', 'guidance', 'governance', 'templates')
LAYERS = {'context','principles','behavior','tokens','foundations','primitives','components','patterns','experiences','intelligence','cross-cutting'}
KINDS = {'guideline', 'contract', 'policy', 'checklist', 'specification', 'example'}


def main() -> int:
    errors = []
    registry = json.loads(INDEX.read_text(encoding='utf-8'))
    entries = registry.get('entries', [])
    statuses = set(registry.get('status_model', []))
    seen = set()
    paths = set()
    for item in entries:
        missing = {'id','title','path','layer','kind','status','summary','aliases','domains'} - item.keys()
        if missing:
            errors.append(f"entry missing fields: {sorted(missing)}")
            continue
        ident = item['id'].casefold()
        if ident in seen:
            errors.append(f'duplicate ID: {item["id"]}')
        seen.add(ident)
        if item['status'] not in statuses:
            errors.append(f'{item["id"]}: unknown status {item["status"]}')
        if item['layer'] not in LAYERS or item['kind'] not in KINDS:
            errors.append(f'{item["id"]}: unknown layer/kind')
        if not isinstance(item['aliases'], list) or not isinstance(item['domains'], list):
            errors.append(f'{item["id"]}: aliases and domains must be arrays')
        for field in ('id', 'title', 'path', 'summary'):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{item.get('id', '<missing>')}: invalid {field}")
        if item['path'] in paths:
            errors.append(f'{item["id"]}: duplicate canonical path {item["path"]}')
        paths.add(item['path'])
        path = (ROOT / item['path']).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            errors.append(f'{item["id"]}: missing/outside path {item["path"]}')
            continue
        text = path.read_text(encoding='utf-8')
        if f'# {item["title"]}' not in text:
            errors.append(f'{item["id"]}: page heading does not match registry title')

    # Validate the agent retrieval contract against a documented JSON Schema
    # without introducing a third-party dependency into the standard validator.
    schema = json.loads((ROOT / 'catalog/schema.json').read_text(encoding='utf-8'))
    required = set(schema['$defs']['entry']['required'])
    allowed = set(schema['$defs']['entry']['properties'])
    ids = {entry.get('id') for entry in entries}
    dependencies = {}
    for entry in entries:
        ident = entry.get('id', '<missing id>')
        unknown = set(entry) - allowed
        if unknown:
            errors.append(f'{ident}: unknown registry fields {sorted(unknown)}')
        if required - set(entry):
            errors.append(f'{ident}: missing schema fields {sorted(required - set(entry))}')
        for field in ('aliases', 'domains', 'use_when', 'avoid_when', 'related', 'depends_on'):
            if field in entry and (not isinstance(entry[field], list) or
                                   not all(isinstance(x, str) and x.strip() for x in entry[field])):
                errors.append(f'{ident}: {field} must contain nonempty strings')
            elif len({x.casefold() for x in entry[field]}) != len(entry[field]):
                errors.append(f'{ident}: {field} contains duplicate values')
        for field in ('related', 'depends_on'):
            if isinstance(entry.get(field, []), list):
                for target in entry.get(field, []):
                    if target not in ids or target == ident:
                        errors.append(f'{ident}: invalid {field} reference {target}')
        dependencies[ident] = entry.get('depends_on', [])
        if 'owner' in entry and (not isinstance(entry['owner'], str) or not entry['owner'].strip()):
            errors.append(f'{ident}: invalid owner')
        if entry.get('reviewed_at') is not None:
            try:
                datetime.date.fromisoformat(entry['reviewed_at'])
            except (TypeError, ValueError):
                errors.append(f'{ident}: invalid reviewed_at')

    visited = set()
    visiting = set()
    def visit(node):
        if node in visiting:
            errors.append(f'dependency cycle involving {node}')
            return
        if node in visited:
            return
        visiting.add(node)
        for dep in dependencies.get(node, []):
            if isinstance(dep, str) and dep in ids and dep not in visited:
                visit(dep)
        visiting.remove(node)
        visited.add(node)
    for node in ids:
        if isinstance(node, str):
            visit(node)

    for section in SECTIONS:
        if not (ROOT / section / 'README.md').is_file():
            errors.append(f'missing {section}/README.md')
    link_pattern = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
    checked_links = 0
    for src in ROOT.rglob('*.md'):
        text = src.read_text(encoding='utf-8')
        for target in link_pattern.findall(text):
            target = target.strip().split(' ', 1)[0].strip('<>')
            if not target or target.startswith(('https://','http://','mailto:','#')):
                continue
            target_path = unquote(target.split('#', 1)[0].split('?', 1)[0])
            destination = (src.parent / target_path).resolve()
            checked_links += 1
            if not destination.is_relative_to(ROOT) or not destination.exists():
                errors.append(f'{src.relative_to(ROOT)}: missing relative link {target}')
    if errors:
        for error in errors:
            print('FAIL:', error)
        print(f'{len(errors)} issue(s); {len(entries)} entries; {checked_links} relative links checked.')
        return 1
    print(f'PASS: {len(entries)} unique concepts, {len(SECTIONS)} section READMEs, {checked_links} relative links checked.')
    print('NOTE: external links, accessibility, manual UX tests and factual content were NOT VERIFIED by this script.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
