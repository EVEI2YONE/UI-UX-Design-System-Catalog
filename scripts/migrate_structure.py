#!/usr/bin/env python3
"""Plan or verify the task-first catalog path migration (stdlib only).

Examples:
  python3 scripts/migrate_structure.py --plan
  python3 scripts/migrate_structure.py --check
  python3 scripts/migrate_structure.py --check --final

Source snapshot: first PR checkpoint under temp/legacy/. This script does
not modify files, delete staging, or declare the migration complete.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIXES = {
    "architecture": "knowledge/architecture",
    "foundations": "knowledge/foundations",
    "guidance": "knowledge/guidance",
    "components": "specifications/components",
    "patterns": "specifications/patterns",
    "features": "specifications/experiences",
}
STAGING = ROOT / "temp" / "legacy"
MANIFEST = ROOT / "docs" / "restructure" / "migration-map.json"


def destination(relative_path):
    relative_path = relative_path.replace("\\", "/")
    top, separator, rest = relative_path.partition("/")
    return PREFIXES[top] + "/" + rest if separator and top in PREFIXES else relative_path


def files_under(base):
    return sorted(p.relative_to(base).as_posix() for p in base.rglob("*") if p.is_file())


def plan():
    if MANIFEST.is_file():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))["entries"]
    if not STAGING.is_dir():
        raise FileNotFoundError("No migration manifest or temp/legacy snapshot.")
    return [{"source": name, "destination": destination(name)}
            for name in files_under(STAGING)]


def validate(final=False):
    issues = []
    for old in PREFIXES:
        if (ROOT / old).exists():
            issues.append("Old canonical directory still exists: " + old)
    inventory = STAGING.is_dir()
    if final and inventory:
        issues.append("Remove temp/legacy from final tree after verifying its staging commit.")
    if MANIFEST.is_file() or inventory:
        expected = {e["destination"] for e in plan()}
        current = {name for name in files_under(ROOT) if not name.startswith("temp/legacy/")}
        missing = sorted(expected - current)
        issues += ["Original file has no migrated destination: " + name for name in missing]
    registry_path = ROOT / "catalog/index.json"
    if not registry_path.is_file():
        issues.append("Missing catalog/index.json")
    else:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        entries = registry["entries"]
        if len({e["id"] for e in entries}) != len(entries):
            issues.append("Duplicate registry IDs")
        paths = [e["path"] for e in entries]
        if len(set(paths)) != len(paths):
            issues.append("Duplicate canonical source paths")
        for entry in entries:
            source = entry["path"]
            if not (ROOT / source).is_file():
                issues.append("Missing canonical source: " + source)
            if source.split("/", 1)[0] in PREFIXES:
                issues.append("Registry still uses old folder: " + source)
            impl = entry.get("implementation")
            if impl:
                for key in ("source_path", "scenario_manifest"):
                    if not (ROOT / impl[key]).is_file():
                        issues.append("Missing executable reference: " + impl[key])
        print("Entries:", len(entries), "References:",
              sum(bool(e.get("implementation")) for e in entries))
    print("Staging snapshot:", "present" if inventory else "absent")
    print("Migration issues:", len(issues))
    for issue in issues:
        print("FAIL:", issue)
    return not issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", action="store_true", help="Print staged source-to-destination map as JSON")
    parser.add_argument("--check", action="store_true", help="Verify migrated paths and registry")
    parser.add_argument("--final", action="store_true", help="Reject temporary staging in the final tree")
    args = parser.parse_args()
    if args.plan:
        print(json.dumps(plan(), indent=2))
    if args.check or not args.plan:
        return 0 if validate(args.final) else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
