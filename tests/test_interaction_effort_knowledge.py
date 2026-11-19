"""B04 canonical action-choice and effort retrieval knowledge checks.

These tests verify documentation and search, not user task performance.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402

QUERIES = {
    "action consolidation decision matrix": "pattern.advanced-interactions",
    "split button safety": "pattern.advanced-interactions",
    "contextual action toolbar": "pattern.advanced-interactions",
    "control overloading": "pattern.advanced-interactions",
    "pointer travel distance": "guidance.ux-measurement",
    "time to next action": "guidance.ux-measurement",
    "keyboard navigation effort": "guidance.ux-measurement",
    "interaction cost measurement": "guidance.ux-measurement",
    "sequential task controller": "pattern.task-flows",
}

class InteractionEffortKnowledgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {e["id"]: e for e in cls.entries}

    def test_queries_retrieve_correct_canonical_owner(self):
        for query, expected in QUERIES.items():
            with self.subTest(query=query):
                result = lookup(self.entries, query, limit=1)
                self.assertTrue(result)
                self.assertEqual(result[0]["id"], expected)

    def test_no_duplicate_canonical_ids(self):
        ids = [e["id"] for e in self.entries]
        self.assertEqual(len(ids), len(set(ids)))

if __name__ == "__main__":
    unittest.main()
