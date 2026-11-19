"""Shell contract checks: static view composition, source-of-truth and task links."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "site"))
from catalog.core.discovery import load_tasks, validate_tasks, terms_by_concept, task_relevance
from catalog.core.navigation import category, route
from shell.components import navigation, concept_card, concept_metadata, task_index


class ShellContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.tasks = load_tasks(ROOT)
        cls.by_id = {e["id"]: e for e in cls.entries}
        validate_tasks(cls.tasks, cls.entries)

    def test_all_task_routes_resolve_only_to_registered_concepts(self):
        self.assertEqual(len(self.tasks), 7)
        markup = task_index(self.tasks, {e["id"]: route(e) for e in self.entries})
        for task in self.tasks:
            self.assertIn(task["title"], markup)
            self.assertIn(route(self.by_id[task["primary_id"]]), markup)
            self.assertEqual(task_relevance(task["primary_id"], task["title"], self.tasks), 85)

    def test_cards_separate_kind_review_and_implementation(self):
        entry = self.by_id["guidance.content-design"]
        html = concept_card(entry, category(entry), route(entry), "content design")
        self.assertIn("Guideline", html)
        self.assertIn("No runnable reference", html)
        self.assertIn("Review status", concept_metadata(entry))
        self.assertIn("proposed", concept_metadata(entry))
        self.assertIn("Content design", html)

    def test_navigation_landmark_and_search_terms(self):
        self.assertIn('aria-current="page"', navigation("tasks"))
        self.assertIn("recover from a failed submission",
                      [x.lower() for x in terms_by_concept(self.tasks)["pattern.forms"]])


if __name__ == "__main__":
    unittest.main()
