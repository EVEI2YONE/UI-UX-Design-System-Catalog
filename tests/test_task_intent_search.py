"""Natural-language task retrieval contract for people and agent clients.

Query fixtures belong to the non-normative task index. The expected result is
the existing canonical concept, not a newly duplicated task specification.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT))
from find_concept import lookup
from catalog.core.discovery import load_tasks, validate_tasks


class TaskIntentSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.tasks = load_tasks(ROOT)
        validate_tasks(cls.tasks, cls.entries)

    def test_all_user_tasks_and_declared_aliases_resolve_to_owners(self):
        self.assertGreaterEqual(len(self.tasks), 7)
        for task in self.tasks:
            for query in (task["title"], *task["intent_phrases"]):
                with self.subTest(task=task["id"], phrase=query):
                    ranked = lookup(self.entries, query, limit=1)
                    self.assertTrue(ranked, query)
                    self.assertEqual(ranked[0]["id"], task["primary_id"])

    def test_unrecognized_queries_do_not_produce_invented_guidance(self):
        for query in ("teleport dashboard holograms", "intergalactic pie export"):
            with self.subTest(query=query):
                self.assertEqual(lookup(self.entries, query), [])

    def test_task_pages_link_only_to_registered_concept_ids(self):
        owners = {e["id"] for e in self.entries}
        for task in self.tasks:
            self.assertIn(task["primary_id"], owners)
            self.assertTrue(set(task.get("related_ids", [])).issubset(owners))
            self.assertNotIn(task["id"], owners)


if __name__ == "__main__":
    unittest.main()
