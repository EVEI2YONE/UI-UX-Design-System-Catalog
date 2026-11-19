"""Task pointers connect existing specifications; they do not mint duplicate norms."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TaskPointersTests(unittest.TestCase):
    def test_all_tasks_point_to_canonical_concepts(self):
        tasks = json.loads((ROOT / "tasks/index.json").read_text(encoding="utf-8"))["tasks"]
        concepts = {e["id"] for e in json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]}
        self.assertGreaterEqual(len(tasks), 7)
        self.assertEqual(len({t["id"] for t in tasks}), len(tasks))
        for task in tasks:
            with self.subTest(task=task["id"]):
                self.assertIn(task["primary_id"], concepts)
                self.assertTrue(task["intent_phrases"])
                self.assertTrue(all(r in concepts for r in task["related_ids"]))
