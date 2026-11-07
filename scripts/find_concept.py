#!/usr/bin/env python3
"""Rank canonical catalog entries; stdlib only and deterministic."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def normalize(text):
    """Casefold and normalize punctuation to spaces without stripping Unicode words."""
    return ' '.join(re.findall(r'[^\\W_]+', text.casefold(), flags=re.UNICODE))


def score(entry, query):
    """Return relevance or -1. Exact ID > exact alias > exact title > words."""
    q = normalize(query)
    if not q:
        return 0
    if normalize(entry['id']) == q:
        return 100
    if any(normalize(alias) == q for alias in entry['aliases']):
        return 90
    if normalize(entry['title']) == q:
        return 80
    fields = [entry['id'], entry['title'], entry['summary'],
              *entry['aliases'], *entry['domains'],
              *entry.get('use_when', [])]
    search_text = ' '.join(normalize(field) for field in fields)
    terms = q.split()
    if not all(term in search_text for term in terms):
        return -1
    if q in normalize(entry['title']):
        return 70
    if any(q in normalize(alias) for alias in entry['aliases']):
        return 60
    if q in normalize(entry['id']):
        return 55
    if any(q in normalize(item) for item in entry.get('use_when', [])):
        return 50
    return 10


def lookup(entries, query='', layer=None, domain=None, status=None, limit=None):
    ranked = []
    for entry in entries:
        if layer and entry['layer'].casefold() != layer.casefold():
            continue
        if domain and not any(domain.casefold() in d.casefold()
                              for d in entry['domains']):
            continue
        if status and entry['status'].casefold() != status.casefold():
            continue
        relevance = score(entry, query)
        if relevance >= 0:
            ranked.append((relevance, entry))
    ranked.sort(key=lambda pair: (-pair[0], pair[1]['id']))
    results = [entry for _, entry in ranked]
    return results[:limit] if limit is not None else results


def run():
    parser = argparse.ArgumentParser(description='Find canonical UI/UX guidance.')
    parser.add_argument('query', nargs='*', help='task, ID or alias')
    parser.add_argument('--layer', help='filter by primary layer')
    parser.add_argument('--domain', help='filter by domain')
    parser.add_argument('--json', action='store_true', help='machine-readable results')
    parser.add_argument('--status', choices=['proposed', 'experimental', 'stable', 'deprecated', 'removed'])
    parser.add_argument('--limit', type=int, help='positive maximum number of results')
    args = parser.parse_args()
    if args.limit is not None and args.limit <= 0:
        parser.error('--limit must be positive')
    registry = json.loads((ROOT / 'catalog/index.json').read_text(encoding='utf-8'))
    results = lookup(registry['entries'], ' '.join(args.query),
                     layer=args.layer, domain=args.domain, status=args.status, limit=args.limit)
    if args.json:
        print(json.dumps({'results': results}, ensure_ascii=False, indent=2))
    elif not results:
        print('No concepts found. Try a synonym or browse catalog/README.md.')
    else:
        for entry in results:
            print(f"{entry['id']}  [{entry['layer']}; {entry['status']}]")
            print(f"  {entry['title']} — {entry['summary']}")
            print(f"  {entry['path']}")
        print(f"\n{len(results)} result(s).")
    return 0 if results else 1


if __name__ == '__main__':
    raise SystemExit(run())
