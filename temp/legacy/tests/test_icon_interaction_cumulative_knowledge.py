"""B06: cross-batch catalog discovery and verification boundaries.

These tests check canonical metadata, retrieval and documented acceptance, NOT
live application accessibility, interaction behavior or user outcomes.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402

TASK_OWNERS = {
    "icon consistency audit": "foundation.icon-semantics",
    "icon intent collision review": "foundation.icon-semantics",
    "semantic icon registry": "foundation.icon-semantics",
    "icon-only button": "foundation.icon-semantics",
    "component event ownership": "architecture.component-contracts",
    "nested interactive controls": "architecture.component-contracts",
    "pending confirmed icon": "pattern.interaction-recovery",
    "focus after item removal": "pattern.interaction-recovery",
    "sequential task controller": "pattern.task-flows",
    "stable action region": "pattern.task-flows",
    "split button safety": "pattern.advanced-interactions",
    "action consolidation decision matrix": "pattern.advanced-interactions",
    "pointer travel distance": "guidance.ux-measurement",
    "time to next action": "guidance.ux-measurement",
    "utility-first styling ownership": "foundation.practical-styling",
    "visual redundancy enforcement": "architecture.enforcement-ci",
    "component inventory to contract mapping": "architecture.component-model",
    "interaction state test matrix": "governance.quality",
    "catalog retrieval regression": "governance.quality",
}

class IconInteractionCumulativeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_cumulative_task_to_canonical_owner_lookup(self):
        for query, canonical_id in TASK_OWNERS.items():
            with self.subTest(query=query):
                found = lookup(self.entries, query, limit=1)
                self.assertTrue(found, f"No concept found for {query!r}")
                self.assertEqual(found[0]["id"], canonical_id)

    def test_nonoverlapping_legacy_and_new_owners(self):
        # Icon semantics, button activation and QA evidence remain distinct.
        self.assertEqual(lookup(self.entries, "button action", limit=1)[0]["id"], "component.button")
        self.assertEqual(lookup(self.entries, "semantic icon registry", limit=1)[0]["id"], "foundation.icon-semantics")
        self.assertEqual(lookup(self.entries, "catalog validation", limit=1)[0]["id"], "governance.quality")
        ids = [entry["id"] for entry in self.entries]
        self.assertEqual(len(ids), len(set(ids)))

    def test_new_b06_material_is_proposed_and_unverified(self):
        for concept_id, phrases in {
            "foundation.icon-semantics": ["CKG-05", "consistency", "NOT VERIFIED"],
            "governance.quality": ["CKG-18/19", "interaction-state", "NOT VERIFIED"],
        }.items():
            with self.subTest(concept=concept_id):
                entry = self.by_id[concept_id]
                self.assertEqual(entry["status"], "proposed")
                self.assertIsNone(entry["reviewed_at"])
                content = (ROOT / entry["path"]).read_text(encoding="utf-8")
                for phrase in phrases:
                    self.assertIn(phrase, content)

    def test_each_batch_has_context_and_canonical_owner(self):
        for batch in range(2, 7):
            path = ROOT / "archive" / "planning" / f"icon-interaction-b{batch:02d}-context-2026-11-07.md"
            with self.subTest(batch=batch):
                self.assertTrue(path.is_file())
        ledger = (ROOT / "archive/planning/icon-interaction-batches-progress-2026-11-07.md").read_text(encoding="utf-8")
        for batch in range(1, 7):
            self.assertIn(f"B{batch:02d}", ledger)
        for section in ("README.md", "foundations/README.md", "governance/README.md", "AGENTS.md"):
            with self.subTest(section=section):
                text = (ROOT / section).read_text(encoding="utf-8")
                self.assertIn("Batch 6" if section in ("README.md", "AGENTS.md") else "B06", text)

if __name__ == "__main__":
    unittest.main()
