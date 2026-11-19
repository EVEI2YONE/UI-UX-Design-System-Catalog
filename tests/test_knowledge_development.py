"""Verify concept contracts and evidence limits without development-history ledgers."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS = {
    "architecture.component-model": ("Executable reference maintainability", "state ownership", "token"),
    "guidance.accessibility": ("Reference-state accessibility", "200%", "RTL"),
    "architecture.component-contracts": ("Source exploration", "license", "NOT VERIFIED"),
    "guidance.ux-measurement": ("Catalog discoverability and source-trust", "First-hit relevance", "participant"),
    "governance.quality": ("Static visual catalog hosting", "frame-ancestors", "NOT VERIFIED"),
}


class KnowledgeCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = {e["id"]: e for e in json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]}

    def test_concept_substance_and_evidence_boundaries(self):
        for identifier, required in TOPICS.items():
            with self.subTest(id=identifier):
                entry = self.items[identifier]
                self.assertEqual(entry["status"], "proposed")
                document = (ROOT / entry["path"]).read_text(encoding="utf-8").casefold()
                for phrase in required:
                    self.assertIn(phrase.casefold(), document)

    def test_no_duplicate_concept_registry(self):
        self.assertEqual(len(self.items), 54)
