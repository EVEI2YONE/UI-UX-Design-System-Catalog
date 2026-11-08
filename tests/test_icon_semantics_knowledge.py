"""Batch 1: semantic icon guidance discoverability and documentation safeguards.

These tests exercise metadata and knowledge retrieval, not rendered accessibility.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402

QUERIES = {
    "semantic icon registry": "foundation.icon-semantics",
    "icon-only button": "foundation.icon-semantics",
    "icon button loading state": "foundation.icon-semantics",
    "decorative status icon": "foundation.icon-semantics",
    "button action": "component.button",
}

class IconSemanticsRetrievalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_task_retrieval(self):
        for query, expected in QUERIES.items():
            with self.subTest(query=query):
                results = lookup(self.entries, query, limit=1)
                self.assertTrue(results, f"no results for {query}")
                self.assertEqual(results[0]["id"], expected)

    def test_canonical_entry_and_links(self):
        entry = self.by_id["foundation.icon-semantics"]
        self.assertEqual(entry["status"], "proposed")
        self.assertIsNone(entry["reviewed_at"])
        self.assertEqual(entry["owner"], "unassigned")
        self.assertTrue((ROOT / entry["path"]).is_file())
        text = (ROOT / entry["path"]).read_text(encoding="utf-8")
        for phrase in ("CKG-01", "CKG-02", "CKG-03", "NOT VERIFIED", "component.button"):
            self.assertIn(phrase, text)
        self.assertIn("iconography-and-semantics.md", (ROOT / "foundations/README.md").read_text(encoding="utf-8"))
        self.assertIn("foundation.icon-semantics", (ROOT / "AGENTS.md").read_text(encoding="utf-8"))

    def test_no_duplicate_ids(self):
        ids = [entry["id"] for entry in self.entries]
        self.assertEqual(len(ids), len(set(ids)))

if __name__ == "__main__":
    unittest.main()
