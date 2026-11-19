"""Regression guard for the issue #34 task-surface decision and task lookup."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
from catalog.core.discovery import load_tasks, validate_tasks
from find_concept import lookup


class TaskSurfaceDecisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.tasks = load_tasks(ROOT)
        validate_tasks(cls.tasks, cls.entries)

    def test_scenario_and_each_intent_retrieve_canonical_owner(self):
        matching = [task for task in self.tasks if task["id"] == "choose-one-record-task-surface"]
        self.assertEqual(len(matching), 1)
        task = matching[0]
        self.assertEqual(task["primary_id"], "pattern.master-detail")
        for phrase in (task["title"], *task["intent_phrases"]):
            with self.subTest(phrase=phrase):
                result = lookup(self.entries, phrase, limit=1)
                self.assertTrue(result, phrase)
                self.assertEqual(result[0]["id"], "pattern.master-detail")

    def test_modal_depth_and_recovery_contract_remains_canonical(self):
        path = ROOT / "specifications/patterns/master-detail-exploration.md"
        source = path.read_text(encoding="utf-8").casefold()
        for expected in (
            "## Choose one task surface across detail, edit and history",
            "inline expansion/edit", "in-place detail subview", "single** modal",
            "side drawer/sheet", "dedicated route", "save pending",
            "timeout / acknowledgement lost", "removed invoker",
            "browser Back", "NOT VERIFIED", "## Sources, related concepts"
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected.casefold(), source)
        canonical = [entry for entry in self.entries if entry["id"] == "pattern.master-detail"]
        self.assertEqual(len(canonical), 1)

    def test_cross_links_preserve_ownership_and_no_new_component(self):
        paths = {
            "specifications/patterns/task-flows-and-information-architecture.md": "Master-detail: task-surface choice",
            "examples/collection-to-related-record-journey.md": "Master-detail task-surface chooser",
            "tasks/README.md": "Edit a related record without nested dialogs",
        }
        for rel, expected in paths.items():
            with self.subTest(rel=rel):
                self.assertIn(expected, (ROOT / rel).read_text(encoding="utf-8"))
        self.assertFalse(any("task-surface" in entry["id"] for entry in self.entries))


if __name__ == "__main__":
    unittest.main()
