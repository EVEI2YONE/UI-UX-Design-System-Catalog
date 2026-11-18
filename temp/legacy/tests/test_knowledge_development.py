"""Verify five knowledge contracts are canonical, cross-linked and not approvals.

Does not claim research, browser accessibility or production security verification.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "docs/visual-catalog-refactor"
DELIVERY = PACK / "20-knowledge-development-batches.md"

CASES = {
    "KG-08": ("architecture/component-model.md",
              "## Executable reference maintainability and composition contract",
              ["state ownership", "token", "readability"]),
    "KG-07": ("guidance/accessibility.md",
              "## Reference-state accessibility, theme and performance acceptance matrix",
              ["200%", "RTL", "NOT VERIFIED"]),
    "KG-11": ("architecture/component-contracts.md",
              "## Source exploration, reuse and distribution contract",
              ["Copy and download", "license", "NOT VERIFIED"]),
    "KG-12": ("guidance/ux-measurement.md",
              "## Catalog discoverability and source-trust study protocol",
              ["First-hit relevance", "participant", "NOT VERIFIED"]),
    "KG-10": ("governance/quality-gates.md",
              "## Static visual catalog hosting, supply-chain and preview security gate",
              ["frame-ancestors", "npm ci", "NO", "NOT VERIFIED"]),
}

class KnowledgeDevelopmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))
        cls.delivery = DELIVERY.read_text(encoding="utf-8")
        cls.index = (PACK / "README.md").read_text(encoding="utf-8")

    def test_each_gap_has_a_real_canonical_contract_and_evidence_boundary(self):
        for gap, (path, heading, must_have) in CASES.items():
            with self.subTest(gap=gap):
                text = (ROOT / path).read_text(encoding="utf-8")
                self.assertEqual(text.count(heading), 1, path)
                block = text.split(heading, 1)[1]
                self.assertGreater(len(block), 1300, gap)
                for phrase in must_have:
                    self.assertIn(phrase.casefold(), block.casefold())
                self.assertIn(gap, self.delivery)
                self.assertIn(path, self.delivery)

    def test_all_five_independent_context_snapshots_recorded(self):
        heads = re.findall(r"\*\*Before editing, repository head:\*\* `([a-f0-9]{40})`", self.delivery)
        self.assertEqual(len(heads), 5)
        self.assertEqual(len(set(heads)), 5)
        for gap in CASES:
            self.assertIn("## " + gap, self.delivery)
        self.assertIn("research", self.delivery.lower())
        self.assertIn("NOT VERIFIED", self.delivery)

    def test_does_not_mint_new_catalog_entries_or_promote_review_status(self):
        entries = self.registry["entries"]
        self.assertEqual(len(entries), 54)
        self.assertEqual(sum(bool(e.get("implementation")) for e in entries), 12)
        self.assertTrue(all(e["status"] == "proposed" for e in entries))
        self.assertIn("20-knowledge-development-batches.md", self.index)

if __name__ == "__main__":
    unittest.main()
