"""Visual craftsmanship KG-01..18 catalog routing and documentation regression.

Run: python3 -m unittest discover -s tests -v
These tests only check registry/documentation integrity, not any rendered UI or
accessibility compliance.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402


class VisualCraftsmanshipTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.ids = {e["id"] for e in cls.entries}

    def test_retrieval(self):
        mapping = {
            "visual craftsmanship": "foundation.visual-craftsmanship",
            "inspiration research": "foundation.visual-craftsmanship",
            "design direction selection": "foundation.visual-craftsmanship",
            "styling recipes": "foundation.practical-styling",
            "motion design": "foundation.practical-styling",
            "visual craftsmanship critique": "governance.quality",
            "render inspect refine": "governance.quality",
            "visual craftsmanship workflow": "governance.quality",
        }
        for phrase, expected in mapping.items():
            with self.subTest(phrase=phrase):
                found = lookup(self.entries, phrase)
                self.assertTrue(found, f"no result for {phrase}")
                self.assertEqual(found[0]["id"], expected)

    def test_existing_canonical_owners_and_no_duplicate_ids(self):
        self.assertEqual(len(self.entries), len(self.ids))
        for ident in ("foundation.visual-craftsmanship", "foundation.practical-styling",
                      "governance.quality", "foundation.design-tokens",
                      "guidance.accessibility", "guidance.wireframe-methodology"):
            with self.subTest(ident=ident):
                self.assertIn(ident, self.ids)

    def test_coverage_kgs_01_to_18(self):
        workflow = (ROOT / "governance/visual-craftsmanship-workflow.md").read_text(encoding="utf-8")
        for n in range(1, 19):
            with self.subTest(kg=n):
                self.assertIn(f"KG-{n:02d}", workflow)
        self.assertIn("NOT VERIFIED", workflow)
        self.assertIn("synthetic", workflow.lower())

    def test_canonical_content_ownership(self):
        expected = {
            "foundation.visual-craftsmanship": ("foundations/visual-design-craftsmanship.md",
                                                  [1, 2, 3, 4, 5, 11, 12, 13, 14]),
            "foundation.practical-styling": ("foundations/practical-ui-styling-recipes.md",
                                               [6, 7, 8, 9, 10]),
            "governance.quality": ("governance/quality-gates.md", [15, 16]),
        }
        for ident, (path, covered) in expected.items():
            entry = next(e for e in self.entries if e["id"] == ident)
            self.assertEqual(entry["path"], path)
            text = (ROOT / path).read_text(encoding="utf-8")
            for n in covered:
                with self.subTest(ident=ident, kg=n):
                    self.assertIn(f"KG-{n:02d}", text)
        examples = (ROOT / "foundations/visual-refinement-examples.md").read_text(encoding="utf-8")
        self.assertIn("KG-17", examples)

    def test_discovery_and_related_ids(self):
        root = (ROOT / "README.md").read_text(encoding="utf-8")
        governance = (ROOT / "governance/README.md").read_text(encoding="utf-8")
        agent = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("governance/visual-craftsmanship-workflow.md", root)
        self.assertIn("visual-craftsmanship-workflow.md", governance)
        self.assertIn("visual-craftsmanship-workflow.md", agent)
        for entry in self.entries:
            for rel in [*entry.get("related", []), *entry.get("depends_on", [])]:
                with self.subTest(entry=entry["id"], related=rel):
                    self.assertIn(rel, self.ids)


if __name__ == "__main__":
    unittest.main()
