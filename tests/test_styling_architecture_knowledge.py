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

    def test_registry_unique(self):
        ids = [e["id"] for e in self.entries]
        self.assertEqual(len(ids), len(set(ids)))

if __name__ == "__main__":
    unittest.main()
