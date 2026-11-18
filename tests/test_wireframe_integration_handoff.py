"""B7 cumulative documentation handoff regression; no product/browser/image checks."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402

HANDOFF = ROOT / "archive/planning/wireframe-integration-handoff-2026-11-07.md"
BANK = ROOT / "archive/planning/wireframe-synthetic-example-bank-2026-11-07.md"
TRACKER = ROOT / "archive/planning/wireframe-knowledge-batches-2026-11-07.md"

OWNER_QUERIES = {
    "wireframe methodology": "guidance.wireframe-methodology",
    "task to screen composition": "pattern.task-flows",
    "wireframe state coverage": "pattern.interaction-recovery",
    "wireframe viewport matrix": "guidance.mobile-adaptive",
    "inclusive wireframe review": "guidance.accessibility",
    "wireframe text expansion": "guidance.internationalization",
    "wireframe visual QA": "governance.quality",
}

class WireframeIntegrationHandoffTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_cumulative_lookup_and_canonical_path(self):
        for query, expected in OWNER_QUERIES.items():
            with self.subTest(query=query):
                hits = lookup(self.entries, query, limit=1)
                self.assertTrue(hits)
                self.assertEqual(hits[0]["id"], expected)
                self.assertTrue((ROOT / hits[0]["path"]).is_file())

    def test_new_concept_and_existing_owners_are_proposed(self):
        # Validate unique catalog identities/paths without freezing global size.
        self.assertEqual(len(self.entries), len(self.by_id))
        self.assertEqual(len(self.entries), len({x["path"] for x in self.entries}))
        self.assertEqual([e["id"] for e in self.entries if "wireframe" in e["id"]],
                         ["guidance.wireframe-methodology"])
        for entry in self.entries:
            with self.subTest(id=entry["id"]):
                self.assertEqual(entry["status"], "proposed")
                self.assertEqual(entry["owner"], "unassigned")
                self.assertIsNone(entry["reviewed_at"])
                for related_id in entry["related"] + entry["depends_on"]:
                    self.assertIn(related_id, self.by_id)

    def test_handoff_is_discoverable_and_noncanonical(self):
        self.assertTrue(HANDOFF.is_file())
        self.assertTrue(BANK.is_file())
        self.assertTrue(TRACKER.is_file())
        body = HANDOFF.read_text(encoding="utf-8")
        for text in ("B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7",
                     "REUSE", "EXTEND", "CREATE", "DEFER",
                     "NOT VERIFIED", "NOT SHOWN", "ILLUSTRATIVE",
                     "guidance.wireframe-methodology", "governance.quality",
                     "tests/test_wireframe_examples_retrieval.py"):
            with self.subTest(term=text):
                self.assertIn(text, body)
        registered = {entry["path"] for entry in self.entries}
        self.assertNotIn(str(HANDOFF.relative_to(ROOT)), registered)
        self.assertNotIn(str(BANK.relative_to(ROOT)), registered)

    def test_root_and_agent_discovery(self):
        agent = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        root = (ROOT / "README.md").read_text(encoding="utf-8")
        catalog = (ROOT / "catalog/README.md").read_text(encoding="utf-8")
        self.assertIn("wireframe-integration-handoff-2026-11-07.md", agent)
        self.assertIn("wireframe-integration-handoff-2026-11-07.md", root)
        self.assertIn("wireframe-integration-handoff-2026-11-07.md", catalog)
        self.assertIn("catalog/index.json", agent)
        self.assertIn("NOT VERIFIED", root)

if __name__ == "__main__":
    unittest.main()
