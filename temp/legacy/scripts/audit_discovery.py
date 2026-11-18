#!/usr/bin/env python3
"""Emit a derived, reproducible Phase 9 retrieval/provenance evidence report.

This is a CI report only; catalog/index.json remains canonical. Nonzero exit
means an acceptance query, registered source or generated route is broken.
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"site"))
from build import route
from find_concept import lookup

def audit(root=ROOT):
    registry=json.loads((root/"catalog/index.json").read_text(encoding="utf-8"))
    entries=registry["entries"]
    cases=json.loads((root/"tests/fixtures/phase9_retrieval_cases.json").read_text(encoding="utf-8"))
    ids={e["id"] for e in entries}
    errors=[]
    cases_out=[]
    for kind in ("positive","negative","ambiguous"):
        for case in cases[kind]:
            result=lookup(entries,case["query"])
            actual=[x["id"] for x in result[:3]]
            ok=(bool(result) and result[0]["id"]==case["expected_id"]) if kind=="positive" else (
                not result if kind=="negative" else case["expected_contains"] in {x["id"] for x in result})
            cases_out.append({"kind":kind,"query":case["query"],"top_three":actual,"pass":ok})
            if not ok: errors.append("Retrieval "+kind+": "+case["query"]+" -> "+str(actual))
    references=[]
    for e in entries:
        path=root/e["path"]
        relationships=e.get("related",[])+e.get("depends_on",[])
        if not path.is_file(): errors.append("Missing canonical document "+e["path"])
        for relation in relationships:
            if relation not in ids: errors.append("Unresolved relation "+e["id"]+" -> "+relation)
        implementation=e.get("implementation")
        if implementation:
            source=root/implementation["source_path"]
            scenario=root/implementation["scenario_manifest"]
            if not source.is_file() or not scenario.is_file():
                errors.append("Missing source/scenarios "+e["id"])
            if implementation["preview_path"]+"/" !=route(e):
                errors.append("Route mismatch "+e["id"])
        references.append({"id":e["id"],"path":e["path"],"route":route(e),
                           "implementation":implementation["source_path"] if implementation else None,
                           "scenario":implementation["scenario_manifest"] if implementation else None,
                           "review_status":e["status"],
                           "implementation_status":implementation["status"] if implementation else None})
    return {"schema_version":1,"generated_at_utc":datetime.now(timezone.utc).isoformat(),
            "canonical_count":len(entries),"reference_count":sum(bool(e.get("implementation")) for e in entries),
            "spec_only_count":sum(not e.get("implementation") for e in entries),
            "query_checks":cases_out,"provenance":references,"errors":errors,"pass":not errors}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    report=audit()
    result=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(result,encoding="utf-8")
    print("Discovery audit:", "PASS" if report["pass"] else "FAIL",
          "| concepts:",report["canonical_count"],
          "| executable:",report["reference_count"],
          "| retrieval checks:",len(report["query_checks"]),
          "| errors:",len(report["errors"]))
    for error in report["errors"]:
        print("FAIL:",error)
    return 0 if report["pass"] else 1

if __name__=="__main__":
    raise SystemExit(main())
