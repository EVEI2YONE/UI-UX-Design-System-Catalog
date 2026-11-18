"""Documentation-only discovery regression checks for Batch 17."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402

QUERIES = [
    "framework aware architecture",
    "Next.js app router structure",
    "Angular feature folders",
    "React Router file routes",
    "route colocation",
]


class FrameworkAwareArchitectureKnowledgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]

    def test_intent_queries_resolve_to_new_canonical_entry(self):
        for query in QUERIES:
            with self.subTest(query=query):
                hits = lookup(self.entries, query, limit=1)
                self.assertTrue(hits)
                self.assertEqual(hits[0]["id"], "architecture.framework-aware")

    def test_new_entry_is_proposed_and_source_files_exist(self):
        entry = next(x for x in self.entries if x["id"] == "architecture.framework-aware")
        self.assertEqual(entry["status"], "proposed")
        for path in [
            entry["path"],
            "archive/planning/application-architecture-batch-17-context-and-gaps.md",
        ]:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file())


if __name__ == "__main__":
    unittest.main()
