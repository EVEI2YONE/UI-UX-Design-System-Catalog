"""B03 catalog retrieval and documentation tests; not product interaction verification."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402

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
                r = lookup(self.entries, query, limit=1)
                self.assertTrue(r)
                self.assertEqual(r[0]["id"], expected)

    def test_b03_scope_remains_existing_canonical_ids(self):
        self.assertEqual(len([e for e in self.entries if e["id"] == "pattern.task-flows"]), 1)
        self.assertEqual(len([e for e in self.entries if e["id"] == "pattern.interaction-recovery"]), 1)
        for ident, phrases in {
            "pattern.task-flows": ("CKG-11/12", "next eligible", "NOT VERIFIED", "permission"),
            "pattern.interaction-recovery": ("CKG-09/10", "icon", "focus", "NOT VERIFIED"),
        }.items():
            with self.subTest(concept=ident):
                e = self.index[ident]
                self.assertEqual(e["status"], "proposed")
                self.assertIsNone(e["reviewed_at"])
                content = (ROOT / e["path"]).read_text(encoding="utf-8")
                for phrase in phrases:
                    self.assertIn(phrase, content)

    def test_context_and_discovery_present(self):
        self.assertTrue((ROOT / "archive/planning/icon-interaction-b03-context-2026-11-07.md").is_file())
        for path in ("README.md", "patterns/README.md", "AGENTS.md"):
            with self.subTest(path=path):
                text = (ROOT / path).read_text(encoding="utf-8")
                self.assertIn("B03" if path == "patterns/README.md" else "Batch 3", text)

if __name__ == "__main__":
    unittest.main()
