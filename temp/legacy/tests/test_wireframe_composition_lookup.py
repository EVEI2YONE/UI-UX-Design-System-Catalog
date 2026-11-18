"""Task-to-screen composition retrieval: repository/document checks, not design quality tests."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402


class WireframeCompositionLookupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_task_to_screen_queries(self):
        queries = {
            "task to screen composition": "pattern.task-flows",
            "wireframe screen alternatives": "pattern.task-flows",
            "structural wireframe alternatives": "pattern.task-flows",
            "screen composition": "pattern.task-flows",
            "wireframe comparison matrix": "pattern.task-flows",
            "primary action hierarchy": "principle.visual-hierarchy",
            "wireframe methodology": "guidance.wireframe-methodology",
        }
        for query, expected in queries.items():
            with self.subTest(query=query):
                found = lookup(self.entries, query, limit=1)
                self.assertTrue(found, query)
                self.assertEqual(found[0]["id"], expected)

    def test_reuse_preserves_identity_and_status(self):
        for concept_id in ("pattern.task-flows", "principle.visual-hierarchy", "guidance.wireframe-methodology"):
            entry = self.by_id[concept_id]
            with self.subTest(concept=concept_id):
                self.assertEqual(entry["status"], "proposed")
                self.assertIsNone(entry["reviewed_at"])
                self.assertTrue((ROOT / entry["path"]).is_file())

    def test_composition_contract_documents_decisions_and_limits(self):
        contents = (ROOT / "patterns/task-flows-and-information-architecture.md").read_text(encoding="utf-8").lower()
        for keyword in ("minimum context", "assumed", "structural alternatives", "comparison", "anti-example", "not implemented", "not verified"):
            with self.subTest(keyword=keyword):
                self.assertIn(keyword, contents)

if __name__ == "__main__":
    unittest.main()
