"""Regression tests for proposed application-architecture guidance (Batches 13-16).

This only checks catalog discoverability and documentation. It is not
an application build, an empirical DX evaluation or an accessibility test.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402

QUERIES = {
    "application architecture": "architecture.application-selection",
    "MVP architecture": "architecture.application-selection",
    "prototype architecture": "architecture.application-selection",
    "feature module boundaries": "architecture.module-boundaries",
    "developer navigation": "architecture.module-boundaries",
    "architecture migration": "architecture.evolution",
    "architecture fitness functions": "architecture.evolution",
    "monorepo architecture": "architecture.enterprise-multiapp",
    "microfrontend": "architecture.enterprise-multiapp",
}
EXPECTED = set(QUERIES.values())


class ApplicationArchitectureKnowledgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_task_discovery_resolves_to_intended_canonical_entry(self):
        for query, expected in QUERIES.items():
            with self.subTest(query=query):
                results = lookup(self.entries, query, limit=1)
                self.assertTrue(results)
                self.assertEqual(results[0]["id"], expected)

    def test_all_architecture_entries_are_proposed_and_documents_exist(self):
        for concept_id in EXPECTED:
            with self.subTest(concept=concept_id):
                entry = self.by_id[concept_id]
                self.assertEqual(entry["status"], "proposed")
                path = (ROOT / entry["path"]).resolve()
                self.assertTrue(path.is_relative_to(ROOT))
                self.assertTrue(path.is_file())

    def test_dependency_direction_is_cycle_free_for_new_entries(self):
        def check(node, seen):
            self.assertNotIn(node, seen, f"cycle at {node}")
            for dependency in self.by_id[node]["depends_on"]:
                self.assertIn(dependency, self.by_id)
                check(dependency, seen | {node})
        for concept_id in EXPECTED:
            check(concept_id, set())

    def test_batch_context_ledger_is_present(self):
        self.assertTrue((ROOT / "planning/application-architecture-batches-13-16-context-and-gaps.md").is_file())


if __name__ == "__main__":
    unittest.main()
