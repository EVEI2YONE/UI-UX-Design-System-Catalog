#!/usr/bin/env python3
"""Create the optional editable Excel view of catalog/concept-scorecard.json.

Requires openpyxl (`python3 -m pip install openpyxl`). The Markdown and JSON
are readable without any third-party dependency. The XLSX is generated and
validated so its formulas and cached displays match the canonical scores.

Usage:
  python3 scripts/build_concept_scorecard_workbook.py
  python3 scripts/build_concept_scorecard_workbook.py --check
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZipFile, ZIP_DEFLATED
from xml.etree import ElementTree as ET

try:
    from openpyxl import Workbook, load_workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.worksheet.datavalidation import DataValidation
    from openpyxl.formatting.rule import ColorScaleRule, CellIsRule
    from openpyxl.comments import Comment
    from openpyxl.utils import get_column_letter
except ImportError as exc:
    raise SystemExit("This optional workbook generator requires openpyxl") from exc

from build_concept_scorecard import ROOT, SOURCE, INDEX, DIMENSIONS, score_for, band_for, validate

OUTPUT = ROOT / "CONCEPT_SCORECARD.xlsx"
NAVY, DARK, WHITE, TEAL, BLUE, GREEN, ORANGE = "182942", "1E3654", "FFFFFF", "126B6A", "2368A0", "178257", "AD5B20"
PALE, STRIPE, MUTED = "E9F7F5", "F4F7FA", "637389"
FILL = lambda c: PatternFill("solid", fgColor=c)


def create_workbook(doc: dict):
    entries = sorted(doc["concepts"], key=lambda x: ({"P1": 0, "P2": 1, "P3": 2}[x["priority"]], x["score"], x["id"]))
    wb = Workbook()
    overview = wb.active
    overview.title = "Overview"
    rubric = wb.create_sheet("Rubric")
    ws = wb.create_sheet("Concepts")
    for sheet in wb:
        sheet.sheet_view.showGridLines = False
        sheet.sheet_properties.pageSetUpPr.fitToPage = True
    overview.merge_cells("A1:H2")
    overview["A1"] = "UI / UX CATALOG  |  CONCEPT QUALITY SCORECARD"
    overview["A1"].font = Font(name="Aptos Display", size=19, bold=True, color=WHITE)
    overview["A1"].fill = FILL(NAVY)
    overview["A1"].alignment = Alignment(vertical="center")
    overview.row_dimensions[1].height = 26
    overview.row_dimensions[2].height = 25
    overview.merge_cells("A4:H5")
    overview["A4"] = "Source-only editorial ratings, not approval, UX research results, accessibility conformance or verified implementation quality."
    overview["A4"].font = Font(name="Aptos", color=DARK, size=12)
    overview["A4"].fill = FILL(PALE)
    overview["A4"].alignment = Alignment(wrap_text=True, vertical="center")
    overview.row_dimensions[4].height = 25
    overview.row_dimensions[5].height = 22
    boxes = [
        ("A", "CONCEPTS", "=COUNTA(Concepts!A2:A93)", 92),
        ("C", "SCORED", "=COUNT(Concepts!C2:C93)", 92),
        ("E", "EVIDENCE E0", '=COUNTIF(Concepts!F2:F93,"E0")', 92),
        ("G", "AVERAGE / 100", "=ROUND(AVERAGE(Concepts!C2:C93),1)", round(sum(x["score"] for x in entries)/len(entries), 1)),
    ]
    for col, label, formula, val in boxes:
        for row, value in [(7, label), (8, formula)]:
            c = overview[f"{col}{row}"]
            c.value = value
            c.fill = FILL(STRIPE)
            c.font = Font(name="Aptos", size=10 if row == 7 else 22, bold=True, color=MUTED if row == 7 else TEAL)
            c.alignment = Alignment(horizontal="center")
        overview.row_dimensions[8].height = 35
    overview["A11"] = "REVIEW ORDER"
    overview["A11"].font = Font(bold=True, size=13, color=NAVY)
    instructions = [
        "1. Start with P1 contradictions, overloaded documents and material concept gaps; a high numeric score can still be P1.",
        "2. Read the source, the explanation and next action, then update the 0-4 dimension ratings as you address gaps.",
        "3. All E0 values are independent evidence states, not quality scores. Do not upgrade E1-E3 without real review or testing.",
        "4. Edit catalog/concept-scorecard.json, then rebuild the Markdown and workbook so all views remain synchronized.",
    ]
    for row, instruction in enumerate(instructions, 13):
        overview.merge_cells(start_row=row, start_column=1, end_row=row, end_column=8)
        c = overview.cell(row, 1, instruction)
        c.font = Font(name="Aptos", size=11, color=DARK)
        c.alignment = Alignment(wrap_text=True, vertical="center")
        overview.row_dimensions[row].height = 34
    overview["A19"] = "SOURCE COMMIT"
    overview["A19"].font = Font(bold=True, color=NAVY)
    overview.merge_cells("A20:H20")
    overview["A20"] = doc["source_commit"]
    overview["A20"].font = Font(color=GREEN, size=10)
    overview.merge_cells("A22:H23")
    overview["A22"] = "Ratings reflect source content at a fixed commit; the code history was not assessed. This is a review queue, not an approval or change to catalog lifecycle status."
    overview["A22"].alignment = Alignment(wrap_text=True)
    overview["A22"].font = Font(color=MUTED, size=10)
    for c in "ABCDEFGH":
        overview.column_dimensions[c].width = 18
    overview.freeze_panes = "A11"

    rubric.append(["Code", "Weight", "Dimension", "What to assess"])
    for cell in rubric[1]:
        cell.fill = FILL(NAVY)
        cell.font = Font(color=WHITE, bold=True)
    for i, (name, short, label, weight, check) in enumerate(DIMENSIONS, 2):
        rubric.append([short, doc["weights_percent"][name] / 100, label, check])
        rubric.cell(i, 2).number_format = "0%"
    rubric["A12"] = "0 = Missing or misleading; 1 = Weak; 2 = Developing; 3 = Good; 4 = Strong."
    rubric["A13"] = "Weights sum to 100%; an unassessed dimension stays blank, not zero."
    rubric["A15"] = "EVIDENCE (SEPARATE FROM QUALITY SCORE)"
    for i, (key, value) in enumerate(doc["evidence_levels"].items(), 16):
        rubric.cell(i, 1, key)
        rubric.cell(i, 3, value)
    for col, width in {"A": 12, "B": 15, "C": 29, "D": 62}.items():
        rubric.column_dimensions[col].width = width
    rubric.freeze_panes = "A2"

    headers = ["Concept ID", "Concept", "Score / 100", "Band", "Priority", "Evidence",
               "P", "A", "C", "R", "D", "V", "N", "Why it received this score",
               "Next corrective action", "Issue flag", "Source URL"]
    ws.append(headers)
    for cell in ws[1]:
        cell.fill = FILL(NAVY)
        cell.font = Font(name="Aptos", color=WHITE, size=10, bold=True)
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    ws.row_dimensions[1].height = 34
    for row, e in enumerate(entries, 2):
        dims = [e["dimensions"][name] for name, *_ in DIMENSIONS]
        url = f"https://github.com/{doc['source_repository']}/blob/{doc['source_commit']}/{e['path']}"
        values = [e["id"], e["title"],
                  f'=IF(COUNT(G{row}:M{row})<7,"",ROUND(SUMPRODUCT(G{row}:M{row},Rubric!$B$2:$B$8)*25,0))',
                  f'=IF(C{row}="","Unscored",IF(C{row}>=85,"Strong",IF(C{row}>=70,"Good draft",IF(C{row}>=50,"Needs revision","Rework"))))',
                  e["priority"], e["evidence_level"], *dims, e["explanation"], e["next_action"], e["issue_flag"], url]
        ws.append(values)
        ws.row_dimensions[row].height = 46
        for cell in ws[row]:
            cell.alignment = Alignment(vertical="center", wrap_text=True)
            cell.font = Font(name="Aptos", color=GREEN if cell.column in (1, 2, 17) else DARK, size=10)
            if row % 2 == 0:
                cell.fill = FILL(STRIPE)
        for col in range(7, 14):
            c = ws.cell(row, col)
            c.font = Font(name="Aptos", color=BLUE, bold=True)
            c.alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row, 3).font = Font(name="Aptos", color=NAVY, bold=True, size=13)
        ws.cell(row, 4).font = Font(name="Aptos", color=DARK, bold=True, size=10)
        if e["priority"] == "P1":
            ws.cell(row, 5).font = Font(name="Aptos", bold=True, color=ORANGE)
        ws.cell(row, 17).hyperlink = url
        ws.cell(row, 17).font = Font(name="Aptos", color=GREEN, underline="single", size=9)
    ws.freeze_panes = "G2"
    ws.auto_filter.ref = f"A1:Q{len(entries)+1}"
    for key, width in {"A":36,"B":40,"C":15,"D":18,"E":12,"F":12,"G":7,"H":7,"I":7,"J":7,"K":7,"L":7,"M":7,"N":65,"O":62,"P":22,"Q":54}.items():
        ws.column_dimensions[key].width = width
    dv = DataValidation(type="whole", operator="between", formula1=0, formula2=4, allow_blank=True)
    dv.promptTitle = "0-4 criterion rating"
    dv.prompt = "0 missing, 1 weak, 2 developing, 3 good, 4 strong"
    dv.error = "Choose an integer between 0 and 4"
    dv.showErrorMessage = True
    ws.add_data_validation(dv)
    dv.add(f"G2:M{len(entries)+1}")
    ws.conditional_formatting.add(f"C2:C{len(entries)+1}", ColorScaleRule(start_type="num", start_value=0, start_color="F9D7DC", mid_type="num", mid_value=70, mid_color="FFF1C5", end_type="num", end_value=100, end_color="C8F1DD"))
    for col, label in [(7,"Purpose / boundaries"),(8,"Actionable decisions"),(9,"Coverage / inclusion"),(10,"Research / provenance"),(11,"Discoverability"),(12,"Verification"),(13,"Signal-to-noise")]:
        ws.cell(1,col).comment=Comment(label+"; 0-4 rating", "Catalog Scorecard")
    return wb, entries, boxes


def cache_formulas(path: Path, entries: list[dict], boxes: list[tuple]):
    """Cache calculated values for previews without changing live Excel formulas."""
    ns = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    q = lambda tag: f"{{{ns}}}{tag}"
    cache = {
        "xl/worksheets/sheet1.xml": {f"{col}8": result for col, _, _, result in boxes},
        "xl/worksheets/sheet3.xml": {
            **{f"C{i+2}": e["score"] for i, e in enumerate(entries)},
            **{f"D{i+2}": band_for(e["score"]) for i, e in enumerate(entries)},
        },
    }
    tmp = path.with_suffix(".cached.xlsx")
    counts={}
    with ZipFile(path, "r") as inp, ZipFile(tmp, "w", ZIP_DEFLATED) as out:
        for info in inp.infolist():
            body = inp.read(info.filename)
            if info.filename in cache:
                root = ET.fromstring(body)
                n=0
                for cell in root.findall(f".//{q('sheetData')}/{q('row')}/{q('c')}"):
                    ref = cell.get("r")
                    if ref not in cache[info.filename] or cell.find(q('f')) is None:
                        continue
                    val = cache[info.filename][ref]
                    el = cell.find(q('v'))
                    if el is None:
                        el = ET.SubElement(cell, q('v'))
                    if isinstance(val, str):
                        cell.set("t", "str")
                        el.text = val
                    else:
                        cell.attrib.pop("t", None)
                        el.text = str(val)
                    n += 1
                body = ET.tostring(root, encoding="utf-8", xml_declaration=False)
                counts[info.filename] = n
            out.writestr(info, body)
    assert counts["xl/worksheets/sheet1.xml"] == len(boxes), counts
    assert counts["xl/worksheets/sheet3.xml"] == 2 * len(entries), counts
    tmp.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check cached scores, explanations and source links without writing")
    args = parser.parse_args()
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    doc = json.loads(SOURCE.read_text(encoding="utf-8"))
    validate(index, doc)
    entries = sorted(doc["concepts"], key=lambda x: ({"P1": 0, "P2": 1, "P3": 2}[x["priority"]], x["score"], x["id"]))
    if not args.check:
        wb, _, boxes = create_workbook(doc)
        wb.save(OUTPUT)
        cache_formulas(OUTPUT, entries, boxes)
    check_formulas = load_workbook(OUTPUT, data_only=False)
    check_cached = load_workbook(OUTPUT, data_only=True)
    ws = check_cached["Concepts"]
    assert len(entries) == 92 and ws.max_row == len(entries)+1
    for i, e in enumerate(entries, 2):
        assert ws.cell(i,1).value == e["id"], e["id"]
        assert ws.cell(i,3).value == e["score"], e["id"]
        assert ws.cell(i,4).value == band_for(e["score"]), e["id"]
        assert ws.cell(i,5).value == e["priority"] and ws.cell(i,6).value == e["evidence_level"], e["id"]
        assert [ws.cell(i,c).value for c in range(7,14)] == [e["dimensions"][k] for k,*_ in DIMENSIONS], e["id"]
        assert ws.cell(i,14).value == e["explanation"] and ws.cell(i,15).value == e["next_action"], e["id"]
        assert ws.cell(i,16).value == e["issue_flag"], e["id"]
        assert ws.cell(i,17).value.endswith("/"+e["path"]), e["id"]
        assert check_formulas["Concepts"].cell(i,3).data_type == "f", e["id"]
    expected = [92,92,sum(e["evidence_level"]=="E0" for e in entries),round(sum(e["score"] for e in entries)/len(entries),1)]
    assert [check_cached["Overview"][f"{col}8"].value for col in "ACEG"] == expected
    print(f"XLSX_OK: {len(entries)} scored concepts, formulas, cached values, editable rating inputs: {OUTPUT}")


if __name__ == "__main__":
    main()
