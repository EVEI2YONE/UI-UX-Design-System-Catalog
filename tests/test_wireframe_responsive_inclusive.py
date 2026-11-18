"""Wireframe B4 retrieval and document contract tests; no product conformance claims."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup  # noqa: E402


class WireframeResponsiveInclusiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_task_queries_resolve_to_existing_canonical_owners(self):
        expected = {
            "responsive wireframe composition": "guidance.mobile-adaptive",
            "wireframe viewport matrix": "guidance.mobile-adaptive",
            "wireframe layout reflow": "guidance.mobile-adaptive",
            "inclusive wireframe review": "guidance.accessibility",
            "wireframe focus annotations": "guidance.accessibility",
            "wireframe text expansion": "guidance.internationalization",
            "rtl wireframe layout": "guidance.internationalization",
            "bidi wireframe review": "guidance.internationalization",
            "wireframe methodology": "guidance.wireframe-methodology",
            "task to screen composition": "pattern.task-flows",
            "wireframe state coverage": "pattern.interaction-recovery",
        }
        for query, concept_id in expected.items():
            with self.subTest(query=query):
                hits = lookup(self.entries, query, limit=1)
                self.assertTrue(hits)
                self.assertEqual(hits[0]["id"], concept_id)

    def test_inclusive_entries_keep_proposed_status_and_cross_references(self):
        for concept_id in ("guidance.mobile-adaptive", "guidance.accessibility",
                           "guidance.internationalization"):
            with self.subTest(concept_id=concept_id):
                entry = self.by_id[concept_id]
                self.assertEqual(entry["status"], "proposed")
                self.assertIsNone(entry["reviewed_at"])
                self.assertEqual(entry["owner"], "unassigned")
                self.assertIn("guidance.wireframe-methodology", entry["related"])
                self.assertTrue((ROOT / entry["path"]).is_file())

    def test_wireframe_stress_requirements_and_evidence_boundary(self):
        expected = {
            "guidance.mobile-adaptive": ("responsive wireframe composition contract", "compact",
                "intermediate", "wide", "safe exit", "not verified", "anti-example"),
            "guidance.accessibility": ("inclusive wireframe stress review", "zoom",
                "keyboard", "focus", "not verified", "anti-example"),
            "guidance.internationalization": ("text-expansion and rtl wireframe",
                "mixed direction", "locale", "not verified", "anti-example"),
        }
        for concept_id, words in expected.items():
            content = (ROOT / self.by_id[concept_id]["path"]).read_text(encoding="utf-8").lower()
            for word in words:
                with self.subTest(concept_id=concept_id, word=word):
                    self.assertIn(word, content)

    def test_no_parallel_wireframe_concept_created(self):
        ids = [entry["id"] for entry in self.entries]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual([ident for ident in ids if "wireframe" in ident],
                         ["guidance.wireframe-methodology"])


if __name__ == "__main__":
    unittest.main()
