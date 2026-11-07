"""Regression tests for discoverability of Little Wins-derived catalog guidance.

These tests exercise catalog retrieval and document existence only.
They do not verify application UX, accessibility, platform identity, or security.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from find_concept import lookup  # noqa: E402


QUERIES = {
    "hosted authentication": "pattern.authentication-lifecycle",
    "workspace membership": "pattern.role-aware-workspaces",
    "human approval workflow": "pattern.interaction-recovery",
    "feature flags": "pattern.task-flows",
    "privacy retention": "guidance.privacy-trust",
    "export data": "guidance.privacy-trust",
    "data migration": "pattern.offline-sync",
    "clickable row": "pattern.data-tables",
    "dialog focus return": "component.dialog",
    "global CSS": "foundation.design-tokens",
    "component migration": "architecture.component-model",
    "knowledge coverage audit": "governance.quality",
}


class LittleWinsKnowledgeCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_task_queries_find_intended_existing_concepts_first(self):
        for query, concept_id in QUERIES.items():
            with self.subTest(query=query):
                result = lookup(self.entries, query, limit=1)
                self.assertTrue(result, f"no guidance retrieved for {query!r}")
                self.assertEqual(result[0]["id"], concept_id)

    def test_intended_guidance_pages_exist_and_remain_proposed(self):
        for concept_id in set(QUERIES.values()):
            with self.subTest(concept=concept_id):
                entry = self.by_id[concept_id]
                self.assertEqual(entry["status"], "proposed")
                path = (ROOT / entry["path"]).resolve()
                self.assertTrue(path.is_relative_to(ROOT))
                self.assertTrue(path.is_file())

    def test_batch_evidence_ledgers_exist(self):
        for n in range(6, 11):
            with self.subTest(batch=n):
                path = ROOT / "planning" / f"little-wins-batch-{n}-context-and-gap-ledger.md"
                self.assertTrue(path.is_file(), f"missing context audit for Batch {n}")

    def test_coverage_does_not_introduce_duplicate_canonical_ids(self):
        ids = [entry["id"] for entry in self.entries]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(ids), 40)


if __name__ == "__main__":
    unittest.main()
