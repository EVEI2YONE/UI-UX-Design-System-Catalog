"""Batch 19: catalog retrieval and non-runtime source evidence checks."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402

QUERIES = [
    "application architecture examples",
    "MVP folder structure example",
    "prototype file structure",
    "enterprise monorepo example",
    "feature-first reference implementation",
    "before and after application refactor",
    "architecture migration example",
]


class ArchitectureReferenceExamplesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.entry = next(e for e in cls.entries if e["id"] == "architecture.reference-examples")

    def test_task_queries_resolve_to_examples(self):
        for query in QUERIES:
            with self.subTest(query=query):
                result = lookup(self.entries, query, limit=1)
                self.assertTrue(result)
                self.assertEqual(result[0]["id"], "architecture.reference-examples")

    def test_page_and_context_exist_and_are_proposed(self):
        self.assertEqual(self.entry["status"], "proposed")
        self.assertEqual(self.entry["kind"], "example")
        for path in [
            self.entry["path"],
            "planning/application-architecture-batch-19-context-and-gaps.md",
        ]:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file())

    def test_example_discloses_evidence_limits_and_boundaries(self):
        content = (ROOT / self.entry["path"]).read_text(encoding="utf-8")
        for marker in [
            "Reference A: prototype", "Reference B: MVP", "Reference C: enterprise",
            "Allowed import", "Disallowed", "NOT VERIFIED", "not runnable standalone",
            "Incremental migration walk-through", "Task → file location exercises",
        ]:
            with self.subTest(marker=marker):
                self.assertIn(marker, content)

    def test_related_canonical_knowledge_exists(self):
        ids = {e["id"] for e in self.entries}
        for referenced in self.entry["related"] + self.entry["depends_on"]:
            self.assertIn(referenced, ids)


if __name__ == "__main__":
    unittest.main()
