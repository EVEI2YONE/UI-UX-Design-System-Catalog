#!/usr/bin/env python3
"""Search the catalog's canonical JSON registry; stdlib only."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run() -> int:
    parser = argparse.ArgumentParser(description='Search catalog IDs, titles, summaries, synonyms and domains.')
    parser.add_argument('query', nargs='*', help='term(s), e.g. "focus recovery"')
    parser.add_argument('--layer', help='filter by primary layer, e.g. components')
    parser.add_argument('--domain', help='filter by domain, e.g. accessibility')
    args = parser.parse_args()
    registry = json.loads((ROOT / 'catalog/index.json').read_text(encoding='utf-8'))
    terms = [q.casefold() for q in ' '.join(args.query).split()]
    matches = []
    for entry in registry['entries']:
        if args.layer and entry['layer'].casefold() != args.layer.casefold():
            continue
        if args.domain and not any(args.domain.casefold() in domain.casefold() for domain in entry['domains']):
            continue
        searchable = ' '.join([entry['id'], entry['title'], entry['summary'], *entry['aliases'], *entry['domains']]).casefold()
        if all(term in searchable for term in terms):
            matches.append(entry)
    if not matches:
        print('No concepts found. Try a synonym or browse catalog/README.md.')
        return 1
    for entry in matches:
        print(f"{entry['id']}  [{entry['layer']}; {entry['status']}]\n  {entry['title']} — {entry['summary']}\n  {entry['path']}")
    print(f'\n{len(matches)} result(s).')
    return 0


if __name__ == '__main__':
    raise SystemExit(run())
