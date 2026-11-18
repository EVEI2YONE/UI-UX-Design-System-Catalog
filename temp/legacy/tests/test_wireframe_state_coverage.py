"""Regression test for static wireframe state coverage retrieval.

Only tests text/registry discoverability, not prototype behavior, accessibility or outcomes.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402


class WireframeStateCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_state_coverage_lookup_resolves_existing_owner(self):
        for phrase in ("wireframe state coverage", "static wireframe state matrix",
                       "state annotation handoff", "wireframe recovery states",
                       "permission denied wireframe", "unknown outcome state"):
            with self.subTest(phrase=phrase):
                self.assertEqual(lookup(self.entries, phrase, limit=1)[0]["id"],
                                 "pattern.interaction-recovery")

    def test_other_canonical_retrieval_keeps_existing_owner(self):
        expected = {"form validation": "pattern.forms",
                    "feedback messaging": "pattern.feedback",
                    "offline": "pattern.interaction-recovery",
                    "wireframe methodology": "guidance.wireframe-methodology",
                    "task to screen composition": "pattern.task-flows"}
        for phrase, concept_id in expected.items():
            with self.subTest(phrase=phrase):
                self.assertEqual(lookup(self.entries, phrase, limit=1)[0]["id"],
                                 concept_id)

    def test_static_state_contract_and_status(self):
        entry = self.by_id["pattern.interaction-recovery"]
        self.assertEqual(entry["status"], "proposed")
        self.assertIsNone(entry["reviewed_at"])
        self.assertIn("guidance.wireframe-methodology", entry["related"])
        content = (ROOT / entry["path"]).read_text(encoding="utf-8").lower()
        for phrase in ("minimum state inventory", "state-to-screen annotation",
                       "permission denied", "unknown outcome", "not shown",
                       "not verified", "anti-example", "retry"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, content)


if __name__ == "__main__":
    unittest.main()
