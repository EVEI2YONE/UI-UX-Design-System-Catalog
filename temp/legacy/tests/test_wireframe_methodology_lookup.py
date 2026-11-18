"""Regression coverage for proposed, tool-neutral wireframe methodology retrieval.

These checks do not establish prototype behavior, accessibility, or generated-image quality.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402


class WireframeMethodologyLookupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_fidelity_and_escalation_queries(self):
        for query in ("wireframe methodology", "low fidelity wireframe", "image based wireframing", "interactive prototype escalation"):
            with self.subTest(query=query):
                matches = lookup(self.entries, query, limit=3)
                self.assertTrue(matches)
                self.assertEqual(matches[0]["id"], "guidance.wireframe-methodology")

    def test_static_guidance_is_proposed_and_discoverable(self):
        entry = self.by_id["guidance.wireframe-methodology"]
        self.assertEqual(entry["status"], "proposed")
        self.assertIsNone(entry["reviewed_at"])
        self.assertEqual(entry["owner"], "unassigned")
        self.assertTrue((ROOT / entry["path"]).is_file())
        self.assertIn("pattern.task-flows", entry["related"])
        content = (ROOT / entry["path"]).read_text(encoding="utf-8")
        for term in ("Low-fidelity", "Mid-fidelity", "High-fidelity", "Interactive prototype", "NOT VERIFIED", "Anti-example"):
            self.assertIn(term.lower(), content.lower())

    def test_exact_existing_task_queries_keep_existing_owner(self):
        for query, expected in (("task flow", "pattern.task-flows"), ("visual hierarchy", "principle.visual-hierarchy"), ("error recovery", "pattern.interaction-recovery")):
            with self.subTest(query=query):
                self.assertEqual(lookup(self.entries, query, limit=1)[0]["id"], expected)

if __name__ == "__main__":
    unittest.main()
