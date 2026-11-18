"""B5 retrieval regression: documentation QA only, not rendered-image inspection."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402


class WireframeVisualQATests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {e["id"]: e for e in cls.entries}

    def test_image_quality_queries_preserve_canonical_owner(self):
        for query in ("wireframe visual QA", "image based wireframe review",
                      "wireframe image quality checklist", "generated wireframe copy fidelity",
                      "wireframe clipping inspection", "static mockup evidence review"):
            with self.subTest(query=query):
                self.assertEqual(lookup(self.entries, query, limit=1)[0]["id"], "governance.quality")

    def test_existing_retrieval_ownership(self):
        for query, expected in (
            ("wireframe methodology", "guidance.wireframe-methodology"),
            ("task to screen composition", "pattern.task-flows"),
            ("wireframe state coverage", "pattern.interaction-recovery"),
            ("wireframe text expansion", "guidance.internationalization"),
            ("visual hierarchy", "principle.visual-hierarchy"),
        ):
            with self.subTest(query=query):
                self.assertEqual(lookup(self.entries, query, limit=1)[0]["id"], expected)

    def test_image_evidence_contract_is_proposed_not_a_runtime_claim(self):
        entry = self.by_id["governance.quality"]
        self.assertEqual(entry["status"], "proposed")
        self.assertIsNone(entry["reviewed_at"])
        self.assertEqual(entry["owner"], "unassigned")
        content = (ROOT / entry["path"]).read_text(encoding="utf-8").lower()
        for phrase in ("static wireframe visual qa", "legibility", "clipping",
                       "truthfulness", "source and decision trace", "not verified",
                       "anti-example", "artifact_id", "rendered image"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, content)

    def test_no_new_concept_id(self):
        # No duplicate concept ID or parallel wireframe owner; global catalog grows.
        self.assertEqual(len(self.entries), len({e["id"] for e in self.entries}))
        self.assertEqual([e["id"] for e in self.entries if "wireframe" in e["id"]],
                         ["guidance.wireframe-methodology"])


if __name__ == "__main__":
    unittest.main()
