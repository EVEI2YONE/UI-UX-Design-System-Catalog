"""Verify sequential workflow and focus guidance through canonical concept contracts."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup

QUERIES = {
    "icon state synchronization": "pattern.interaction-recovery",
    "pending confirmed icon": "pattern.interaction-recovery",
    "post mutation focus": "pattern.interaction-recovery",
    "focus after item removal": "pattern.interaction-recovery",
    "sequential task controller": "pattern.task-flows",
    "next eligible item": "pattern.task-flows",
    "stable action region": "pattern.task-flows",
    "pointer travel continuity": "pattern.task-flows",
    "component event ownership": "architecture.component-contracts",
    "semantic icon registry": "foundation.icon-semantics",
}

class InteractionContinuationKnowledgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.index = {entry["id"]: entry for entry in cls.entries}

    def test_discovery_queries_match_existing_concepts(self):
        for query, expected in QUERIES.items():
            with self.subTest(query=query):
                result = lookup(self.entries, query, limit=1)
                self.assertTrue(result)
                self.assertEqual(result[0]["id"], expected)

    def test_recovery_and_task_progress_remain_distinct(self):
        self.assertEqual(sum(e["id"] == "pattern.task-flows" for e in self.entries), 1)
        self.assertEqual(sum(e["id"] == "pattern.interaction-recovery" for e in self.entries), 1)
        topics = {
            "pattern.task-flows": ("next eligible", "NOT VERIFIED", "permission"),
            "pattern.interaction-recovery": ("icon", "focus", "NOT VERIFIED"),
        }
        for identifier, expected in topics.items():
            with self.subTest(concept=identifier):
                item = self.index[identifier]
                self.assertEqual(item["status"], "proposed")
                self.assertIsNone(item["reviewed_at"])
                guidance = (ROOT / item["path"]).read_text(encoding="utf-8")
                for term in expected:
                    self.assertIn(term.casefold(), guidance.casefold())

    def test_navigation_targets_canonical_knowledge(self):
        index = (ROOT / "specifications/patterns/README.md").read_text(encoding="utf-8")
        agent = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        for identifier in ("pattern.task-flows", "pattern.interaction-recovery"):
            self.assertIn(identifier, index)
        self.assertIn("specifications/patterns/README.md", agent)
