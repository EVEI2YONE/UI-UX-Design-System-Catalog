"""Catalog-only regression checks for Batch 18 architecture enforcement guidance.

These checks verify metadata and example documentation, not real ESLint, Nx,
dependency-cruiser or product runtime behavior.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402

QUERIES = [
    "architecture enforcement",
    "module boundary lint",
    "architecture CI",
    "dependency-cruiser rules",
    "ESLint no-restricted-imports",
    "Nx module boundaries",
    "dependency cycle detection",
]


class ArchitectureEnforcementKnowledgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_retrieval_matches_enforcement_concept(self):
        for query in QUERIES:
            with self.subTest(query=query):
                matches = lookup(self.entries, query, limit=1)
                self.assertTrue(matches)
                self.assertEqual(matches[0]["id"], "architecture.enforcement-ci")

    def test_canonical_entry_links_to_prior_owned_guidance(self):
        concept = self.by_id["architecture.enforcement-ci"]
        self.assertEqual(concept["status"], "proposed")
        self.assertTrue((ROOT / concept["path"]).is_file())
        self.assertIn("architecture.module-boundaries", concept["depends_on"])
        self.assertIn("architecture.evolution", concept["depends_on"])

    def test_source_ledger_and_expected_topics_are_present(self):
        ledger = ROOT / "archive/planning/application-architecture-batch-18-context-and-gaps.md"
        self.assertTrue(ledger.is_file())
        content = (ROOT / self.by_id["architecture.enforcement-ci"]["path"]).read_text(encoding="utf-8")
        for phrase in ["no-restricted-imports", "dependency-cruiser", "@nx/enforce-module-boundaries",
                       "relative imports", "Expected FAIL", "Expected PASS", "CI"]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, content)


if __name__ == "__main__":
    unittest.main()
