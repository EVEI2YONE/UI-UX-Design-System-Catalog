#!/usr/bin/env python3
"""Check canonical concept Markdown for historical build commentary.

Only canonical entries and their section navigation READMEs are concept content;
tests, workflows and Git metadata are not subject to this content lint.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from catalog.core.editorial import findings


def main():
    records = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
    checked = sorted(set(row["path"] for row in records))
    checked += [str(path.relative_to(ROOT)) for path in sorted((ROOT / "knowledge").rglob("README.md"))]
    checked += [str(path.relative_to(ROOT)) for path in sorted((ROOT / "specifications").rglob("README.md"))]
    checked += ["README.md", "AGENTS.md", "catalog/README.md", "site/README.md",
                "CONTRIBUTING.md", "tasks/README.md"]
    errors = []
    for name in sorted(set(checked)):
        path = ROOT / name
        if not path.is_file():
            errors.append(f"{name}: file does not exist")
            continue
        for number, excerpt in findings(path.read_text(encoding="utf-8")):
            errors.append(f"{name}:{number}: process history in concept content: {excerpt}")
    for message in errors:
        print("FAIL:", message)
    print(f"{'PASS' if not errors else 'FAIL'}: concept-only editorial check, "
          f"{len(set(checked))} files, {len(errors)} issue(s)")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
