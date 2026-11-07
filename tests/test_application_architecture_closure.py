"""Batch 20 closure: task-first discovery and seven-entry architecture coverage.

Tests protect catalog metadata and navigation, not product implementation quality.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402

EXPECTED = {
    "architecture.application-selection": "architecture/application-architecture.md",
    "architecture.module-boundaries": "architecture/module-boundaries-and-developer-navigation.md",
    "architecture.evolution": "architecture/architecture-evolution.md",
    "architecture.enterprise-multiapp": "architecture/enterprise-and-multiapp.md",
    "architecture.framework-aware": "architecture/framework-aware-application-structure.md",
    "architecture.enforcement-ci": "architecture/architecture-enforcement-and-ci.md",
    "architecture.reference-examples": "architecture/application-architecture-reference-examples.md",
}
TASKS = {
    "MVP architecture": "architecture.application-selection",
    "developer navigation": "architecture.module-boundaries",
    "Next.js app router structure": "architecture.framework-aware",
    "monorepo architecture": "architecture.enterprise-multiapp",
    "architecture migration": "architecture.evolution",
    "module boundary lint": "architecture.enforcement-ci",
    "prototype file structure": "architecture.reference-examples",
}
CONTEXT_LEDGERS = [
    "planning/application-architecture-batches-13-16-context-and-gaps.md",
    "planning/application-architecture-batch-17-context-and-gaps.md",
    "planning/application-architecture-batch-18-context-and-gaps.md",
    "planning/application-architecture-batch-19-context-and-gaps.md",
    "planning/application-architecture-batch-20-closure-audit.md",
]


class ApplicationArchitectureClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_all_seven_concepts_have_unique_proposed_canonical_owners(self):
        self.assertEqual(len(EXPECTED), 7)
        self.assertEqual(len(self.entries), len(self.by_id))
        paths = [self.by_id[key]["path"] for key in EXPECTED]
        self.assertEqual(len(paths), len(set(paths)))
        for concept_id, path in EXPECTED.items():
            with self.subTest(concept=concept_id):
                entry = self.by_id[concept_id]
                self.assertEqual(entry["path"], path)
                self.assertEqual(entry["status"], "proposed")
                self.assertEqual(entry["owner"], "unassigned")
                self.assertIsNone(entry["reviewed_at"])
                self.assertTrue((ROOT / path).is_file())

    def test_task_first_index_and_root_links_are_complete(self):
        index = (ROOT / "architecture/README.md").read_text(encoding="utf-8")
        root = (ROOT / "README.md").read_text(encoding="utf-8")
        for concept_id, path in EXPECTED.items():
            with self.subTest(concept=concept_id):
                self.assertIn(concept_id, index)
                self.assertIn(Path(path).name, index)
                self.assertIn(path, root)
        self.assertLess(index.index("Choose a prototype"), index.index("Enforce imports"))
        self.assertLess(root.index("Choose prototype, MVP"), root.index("Enforce feature/module"))

    def test_task_intents_resolve_to_their_owner(self):
        for query, concept_id in TASKS.items():
            with self.subTest(query=query):
                match = lookup(self.entries, query, limit=1)
                self.assertTrue(match)
                self.assertEqual(match[0]["id"], concept_id)

    def test_context_history_and_closure_ledger_exist(self):
        for path in CONTEXT_LEDGERS:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file())
        audit = (ROOT / CONTEXT_LEDGERS[-1]).read_text(encoding="utf-8")
        for item in ["NOT VERIFIED", "No eighth application architecture concept", "remaining", "proposed"]:
            self.assertIn(item, audit)

    def test_dependency_refs_and_cycles(self):
        def visit(concept_id, ancestors):
            self.assertNotIn(concept_id, ancestors, "dependency cycle")
            for dependency in self.by_id[concept_id]["depends_on"]:
                self.assertIn(dependency, self.by_id)
                visit(dependency, ancestors | {concept_id})
        for concept_id in EXPECTED:
            with self.subTest(concept=concept_id):
                visit(concept_id, set())


if __name__ == "__main__":
    unittest.main()
