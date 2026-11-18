"""B05: retrieval and documentation coverage for styling, CI and reuse inventory.

These are catalog metadata tests; they cannot prove target-app CSS or UX quality.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402

QUERIES = {
    "utility-first styling ownership": "foundation.practical-styling",
    "tailwind shadcn component styling": "foundation.practical-styling",
    "token-backed utility classes": "foundation.practical-styling",
    "visual redundancy enforcement": "architecture.enforcement-ci",
    "CSS ownership lint": "architecture.enforcement-ci",
    "variant explosion lint": "architecture.enforcement-ci",
    "component inventory to contract mapping": "architecture.component-model",
    "installed versus used components": "architecture.component-model",
    "duplicate primitive audit": "architecture.component-model",
    "design tokens and themes": "foundation.design-tokens",
}

class StylingArchitectureKnowledgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {e["id"]: e for e in cls.entries}

    def test_lookup_targets_canonical_owners(self):
        for query, expected in QUERIES.items():
            with self.subTest(query=query):
                matches = lookup(self.entries, query, limit=1)
                self.assertTrue(matches, f"No catalog result: {query}")
                self.assertEqual(matches[0]["id"], expected)

    def test_b05_content_and_proposal_boundary(self):
        cases = {
            "foundation.practical-styling": ["CKG-15", "utility-first", "NOT VERIFIED"],
            "architecture.enforcement-ci": ["CKG-16", "false-positive", "NOT VERIFIED"],
            "architecture.component-model": ["CKG-17", "installed", "NOT VERIFIED"],
        }
        for concept_id, terms in cases.items():
            with self.subTest(concept=concept_id):
                entry = self.by_id[concept_id]
                self.assertEqual(entry["status"], "proposed")
                self.assertIsNone(entry["reviewed_at"])
                doc = (ROOT / entry["path"]).read_text(encoding="utf-8")
                for term in terms:
                    self.assertIn(term, doc)

    def test_context_and_indexes_are_present(self):
        self.assertTrue((ROOT / "archive/planning/icon-interaction-b05-context-2026-11-07.md").is_file())
        for p in ("foundations/README.md", "architecture/README.md", "AGENTS.md"):
            self.assertIn("B05" if p.endswith("README.md") else "Batch 5",
                          (ROOT / p).read_text(encoding="utf-8"))

    def test_registry_unique(self):
        ids = [e["id"] for e in self.entries]
        self.assertEqual(len(ids), len(set(ids)))

if __name__ == "__main__":
    unittest.main()
