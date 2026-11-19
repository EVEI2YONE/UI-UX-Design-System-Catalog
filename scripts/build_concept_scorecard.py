#!/usr/bin/env python3
"""Validate and render the editorial concept scorecard; standard library only.

Usage:
  python3 scripts/build_concept_scorecard.py --write
  python3 scripts/build_concept_scorecard.py --check

The catalog index remains authoritative for concept IDs/paths. This independent
assessment never modifies an entry's lifecycle status or evidence provenance.
"""
from __future__ import annotations

import argparse
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "catalog" / "concept-scorecard.json"
INDEX = ROOT / "catalog" / "index.json"
REPORT = ROOT / "CONCEPT_SCORECARD.md"
DIMENSIONS = [
    ("purpose", "P", "Purpose and boundaries", "15%", "Clear task, scope and use/avoid boundaries"),
    ("actionability", "A", "Actionable guidance", "20%", "Decisions, conditions and alternatives"),
    ("coverage", "C", "Coverage and inclusion", "10%", "Relevant states, access and locale concerns"),
    ("research", "R", "Research and provenance", "15%", "Sources, applicability and honest evidence limits"),
    ("discoverability", "D", "Discoverability and reuse", "10%", "Canonical identity, retrieval and related guidance"),
    ("verification", "V", "Verification criteria", "10%", "Observable checks for applying the guidance"),
    ("signal_to_noise", "N", "Signal-to-noise", "20%", "Decision-first structure without unnecessary annotation"),
]
BANDS = ((85, "Strong"), (70, "Good draft"), (50, "Needs revision"), (0, "Rework"))


def score_for(entry: dict, weights: dict) -> int:
    total = sum(
        Decimal(str(weights[k])) * Decimal(entry["dimensions"][k]) / Decimal(4)
        for k, *_ in DIMENSIONS
    )
    return int(total.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def band_for(score: int) -> str:
    return next(label for threshold, label in BANDS if score >= threshold)


def escape_cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def validate(index: dict, doc: dict) -> None:
    entries = index["entries"]
    concepts = doc["concepts"]
    canonical = {e["id"]: e for e in entries}
    ids = [e["id"] for e in concepts]
    keys = [v[0] for v in DIMENSIONS]
    assert len(canonical) == len(entries), "Duplicate canonical ID"
    assert len(ids) == len(set(ids)), "Duplicate scorecard ID"
    assert set(canonical) == set(ids), "Missing or extra scorecards: " + str(set(canonical) ^ set(ids))
    assert set(doc["weights_percent"]) == set(keys), "Incorrect rubric dimensions"
    assert sum(doc["weights_percent"].values()) == 100, "Rubric must total 100%"
    assert len(doc["source_commit"]) == 40, "Pin a full source revision"
    assert "human review" in doc["assessment_type"], "Explicit evidence boundary required"
    assert set(doc["evidence_levels"]) == {"E0", "E1", "E2", "E3"}
    reasons = set()
    actions = set()
    for e in concepts:
        cid = e["id"]
        assert e["path"] == canonical[cid]["path"], f"Wrong path for {cid}"
        assert e["title"] == canonical[cid]["title"], f"Wrong title for {cid}"
        assert set(e["dimensions"]) == set(keys), f"Invalid dimension set for {cid}"
        assert all(type(v) is int and 0 <= v <= 4 for v in e["dimensions"].values()), cid
        assert e["score"] == score_for(e, doc["weights_percent"]), f"Incorrect score for {cid}"
        assert e["priority"] in {"P1", "P2", "P3"}, f"Incorrect priority for {cid}"
        assert e["evidence_level"] in doc["evidence_levels"], cid
        assert len(e["explanation"]) >= 35 and len(e["next_action"]) >= 25, f"Vague rationale/action: {cid}"
        assert len(e["explanation"]) <= 300 and len(e["next_action"]) <= 240, f"Verbose notes: {cid}"
        assert e["issue_flag"] and "|" not in e["explanation"] + e["next_action"], cid
        reasons.add(e["explanation"])
        actions.add(e["next_action"])
    assert len(reasons) == len(concepts), "Each concept must have a distinct explanation"
    assert len(actions) == len(concepts), "Each concept must have a distinct next action"


def render(doc: dict) -> str:
    all_concepts = doc["concepts"]
    priority_count = Counter(e["priority"] for e in all_concepts)
    band_count = Counter(band_for(e["score"]) for e in all_concepts)
    evidence_count = Counter(e["evidence_level"] for e in all_concepts)
    mean = sum(e["score"] for e in all_concepts) / len(all_concepts)
    source_short = doc["source_commit"][:12]

    lines = [
        "# Concept quality scorecard",
        "",
        "> **Editorial assessment, not approval or a usability result.** Every score is a source-only judgment about current written guidance. "
        "It does not claim an implemented control, user study, accessibility conformance or an independent human review.",
        "",
        f"**Source:** [`{doc['source_repository']}`](https://github.com/{doc['source_repository']}) "
        f"at commit [`{source_short}`](https://github.com/{doc['source_repository']}/tree/{doc['source_commit']}) "
        f"(current code only; no history assessed). **Assessed:** {doc['assessment_date_utc']} (UTC). "
        f"**Coverage:** {len(all_concepts)} of {len(all_concepts)} canonical concepts.",
        "",
        f"**Snapshot:** {mean:.1f}/100 average; "
        f"{band_count['Strong']} strong, {band_count['Good draft']} good drafts, "
        f"{band_count['Needs revision']} need revision, {band_count['Rework']} need rework. "
        f"Review queue: {priority_count['P1']} P1, {priority_count['P2']} P2 and {priority_count['P3']} P3. "
        f"Evidence: {evidence_count['E0']} E0 entries, meaning no independent review is recorded.",
        "",
        "## How to use the scorecard",
        "",
        "1. Read the explanation before changing a rating; the short action is a suggested starting point, not a substitute for checking current source.",
        "2. Work through **P1** issues first, then P2, then P3. Priority is risk and rework urgency, not a numerical ranking or implementation approval.",
        "3. Re-score the affected dimensions after editing and record an actual human review or scenario test separately. Keep proposal/status metadata in `catalog/index.json` authoritative.",
        "4. Edit `catalog/concept-scorecard.json`; run `python3 scripts/build_concept_scorecard.py --write`, then the optional workbook generator. Run both checks before submitting.",
        "",
        "## Universal criteria",
        "",
        "| Code | Criterion | Weight | Check |",
        "| --- | --- | ---: | --- |",
    ]
    for _, code, name, weight, description in DIMENSIONS:
        lines.append(f"| **{code}** | {name} | {weight} | {description} |")
    lines.extend([
        "",
        "**Rating scale (each dimension):** 0 = missing/misleading; 1 = weak; 2 = developing; "
        "3 = good; 4 = strong. Assess context-relevant requirements rather than mechanically penalizing "
        "a governance document for lacking a component's keyboard state matrix.",
        "",
        "**Total:** `ROUND(25 * SUM(dimension_rating * weight_fraction))`, with weights above. "
        "Bands: **85-100 strong**, **70-84 good draft**, **50-69 needs revision**, **0-49 rework**. "
        "An unassessed dimension must remain blank in a future assessment; it is not a zero.",
        "",
        "**Evidence maturity:** E0 = no recorded independent review; E1 = independent human/source review; "
        "E2 = applied implementation or representative task test; E3 = adoption with documented outcomes and owner. "
        "Evidence does not add points to the editorial score. All entries are E0 in this snapshot, even if well written.",
        "",
        "**Priority:** P1 = immediate editorial contradiction, high-noise or important coverage gap; "
        "P2 = targeted improvement; P3 = polish or representative example. "
        "A security, privacy or accessibility blocker overrides a high numerical score and requires independent handling.",
        "",
        "**Dimension notation:** `P/A/C/R/D/V/N` is the seven 0-4 ratings in the order above.",
        "",
        "## All concept ratings and explanations",
        "",
    ])
    for priority, desc in [
        ("P1", "Address first: contradictory guidance, overloaded documents or a material decision/discovery gap"),
        ("P2", "Targeted improvements: verify, reduce scope, or strengthen source-to-decision connections"),
        ("P3", "Refinements: add a practical example or a small missing edge case"),
    ]:
        group = sorted(
            [e for e in all_concepts if e["priority"] == priority],
            key=lambda e: (e["score"], e["id"]),
        )
        lines.extend([
            f"### {priority} - {desc} ({len(group)})",
            "",
            "| Concept | Score | P/A/C/R/D/V/N | Why it received this score | Next action |",
            "| --- | ---: | :---: | --- | --- |",
        ])
        for e in group:
            v = "/".join(str(e["dimensions"][k]) for k, *_ in DIMENSIONS)
            link = f"[{escape_cell(e['id'])}]({e['path']})"
            lines.append(
                f"| {link} | **{e['score']}** ({band_for(e['score'])}) | `{v}` | "
                f"{escape_cell(e['explanation'])} | {escape_cell(e['next_action'])} |"
            )
        lines.extend(["", ""])
    lines.extend([
        "## Annotation-noise follow-through",
        "",
        "The **signal-to-noise** dimension measures how quickly a reader reaches the governing design decision "
        "without repetitive warnings, stale claims or unrelated scope. The "
        "[commenting and annotations](specifications/patterns/commenting-and-annotations.md) specification now "
        "documents dense-thread filtering, marker clustering and an accessible list alternative. "
        "Those are **proposed design contracts**, not verified product features or user outcomes.",
        "",
        "Applied performance, keyboard navigation and privacy checks remain product-owned. Related guidance: "
        "[attention management](specifications/patterns/notifications-and-attention.md) and "
        "[cognitive load](knowledge/guidance/cognitive-load-and-decisions.md).",
        "",
        "## Revision policy",
        "",
        "This assessment is intentionally independent of lifecycle governance: changes here do not set "
        "`status`, `owner`, or `reviewed_at` in the canonical registry. An E1-E3 upgrade requires recorded "
        "human or implementation evidence; do not promote it based on this file. The spreadsheet "
        "[`CONCEPT_SCORECARD.xlsx`](CONCEPT_SCORECARD.xlsx) is an editable working view; the JSON is "
        "the maintained rating source. Regenerate with `python3 scripts/build_concept_scorecard_workbook.py` "
        "(requires `openpyxl`), and validate it with `--check` whenever JSON changes.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true", help="Regenerate root Markdown scorecard")
    group.add_argument("--check", action="store_true", help="Validate IDs, ratings and generated report")
    args = parser.parse_args()
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    doc = json.loads(SOURCE.read_text(encoding="utf-8"))
    try:
        validate(index, doc)
    except (AssertionError, KeyError, ValueError) as exc:
        print(f"SCORECARD_INVALID: {exc}", file=sys.stderr)
        return 1
    expected = render(doc)
    if args.write:
        REPORT.write_text(expected, encoding="utf-8")
        print(f"WROTE {REPORT.name}: {len(doc['concepts'])} scored concepts")
        return 0
    actual = REPORT.read_text(encoding="utf-8") if REPORT.exists() else None
    if actual != expected:
        print("SCORECARD_STALE: run python3 scripts/build_concept_scorecard.py --write", file=sys.stderr)
        return 1
    print(f"SCORECARD_OK: {len(doc['concepts'])} unique concepts, scores and explanations validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
