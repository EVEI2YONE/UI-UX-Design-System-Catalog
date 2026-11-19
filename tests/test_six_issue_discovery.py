"""Regression guard for the six cross-pattern catalog task entrances."""
import json
import unittest
from pathlib import Path

from catalog.core.discovery import load_tasks, task_relevance, validate_tasks

ROOT = Path(__file__).resolve().parents[1]


class SixIssueTaskDiscoveryTests(unittest.TestCase):
    def test_each_issue_has_a_canonical_primary_retrieval_phrase(self):
        tasks = load_tasks(ROOT)
        index = {task["id"]: task for task in tasks}
        expected = {
            "select-or-create-multiple-categories": ("guidance.content-architecture", "select or create multiple category tags"),
            "manage-record-card-actions": ("pattern.collection-views", "manage an item from a card"),
            "archive-or-restore-related-record": ("pattern.advanced-interactions", "archive versus delete a record"),
            "save-dependent-record": ("architecture.component-contracts", "save a dependent item without losing form state"),
            "manage-related-items-from-collection": ("pattern.master-detail", "manage related records from a collection card"),
            "drill-into-scoped-activity": ("guidance.data-visualization", "drill down from KPI card"),
        }
        for task_id, (concept_id, phrase) in expected.items():
            with self.subTest(task_id=task_id):
                task = index[task_id]
                self.assertEqual(concept_id, task["primary_id"])
                self.assertIn(phrase, task["intent_phrases"])
                self.assertEqual(85, task_relevance(concept_id, phrase, tasks))
        catalog = json.loads((ROOT / "catalog" / "index.json").read_text(encoding="utf-8"))
        validate_tasks(tasks, catalog["entries"])

    def test_reference_journey_is_illustrative_not_a_new_registered_feature(self):
        journey = (ROOT / "examples" / "collection-to-related-record-journey.md").read_text(encoding="utf-8")
        self.assertIn("**NOT VERIFIED**", journey)
        self.assertIn("## State and permission matrix", journey)
        self.assertIn("## Anti-patterns and repairs", journey)
        catalog = json.loads((ROOT / "catalog" / "index.json").read_text(encoding="utf-8"))
        self.assertFalse(any(item["path"] == "examples/collection-to-related-record-journey.md" for item in catalog["entries"]))


if __name__ == "__main__":
    unittest.main()