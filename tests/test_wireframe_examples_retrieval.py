"""B6 synthetic wireframe retrieval regression: metadata/docs, NOT visual quality."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup, score  # noqa: E402

BANK = ROOT / "archive/planning/wireframe-synthetic-example-bank-2026-11-07.md"

QUERIES = {
    "wireframe methodology": "guidance.wireframe-methodology",
    "interactive prototype escalation": "guidance.wireframe-methodology",
    "task to screen composition": "pattern.task-flows",
    "structural wireframe alternatives": "pattern.task-flows",
    "primary action hierarchy": "principle.visual-hierarchy",
    "static wireframe state matrix": "pattern.interaction-recovery",
    "unknown outcome state": "pattern.interaction-recovery",
    "wireframe viewport matrix": "guidance.mobile-adaptive",
    "inclusive wireframe review": "guidance.accessibility",
    "wireframe text expansion": "guidance.internationalization",
    "rtl wireframe layout": "guidance.internationalization",
    "wireframe visual QA": "governance.quality",
    "generated wireframe copy fidelity": "governance.quality",
}


class WireframeExampleRetrievalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_synthetic_case_queries_find_intended_owners(self):
        for query, concept_id in QUERIES.items():
            with self.subTest(query=query):
                result = lookup(self.entries, query, limit=1)
                self.assertTrue(result)
                self.assertEqual(result[0]["id"], concept_id)

    def test_exact_id_and_alias_outweigh_generic_partial(self):
        for term, concept_id in (
            ("guidance.wireframe-methodology", "guidance.wireframe-methodology"),
            ("wireframe visual QA", "governance.quality"),
            ("structural wireframe alternatives", "pattern.task-flows"),
        ):
            with self.subTest(term=term):
                results = lookup(self.entries, term, limit=3)
                self.assertEqual(results[0]["id"], concept_id)

    def test_avoid_when_only_not_used_as_positive_match(self):
        entry = {
            "id": "test.synthetic", "title": "Synthetic positive subject",
            "summary": "Neutral fixture", "aliases": ["positive subject"],
            "domains": ["fixture"], "use_when": ["finding a positive topic"],
            "avoid_when": ["pretend backend completed charge", "fictitious invisible keyboard test"],
        }
        for negative in entry["avoid_when"]:
            with self.subTest(negative=negative):
                self.assertEqual(score(entry, negative), -1)
                self.assertEqual(lookup([entry], negative), [])

    def test_covered_entry_paths_status_and_ownership(self):
        for concept_id in set(QUERIES.values()):
            with self.subTest(concept_id=concept_id):
                e = self.by_id[concept_id]
                self.assertEqual(e["status"], "proposed")
                self.assertEqual(e["owner"], "unassigned")
                self.assertIsNone(e["reviewed_at"])
                self.assertTrue((ROOT / e["path"]).is_file())
                for related_id in e["related"] + e["depends_on"]:
                    self.assertIn(related_id, self.by_id)

    def test_example_bank_has_positive_negative_and_evidence_boundary(self):
        self.assertTrue(BANK.is_file())
        body = BANK.read_text(encoding="utf-8")
        for label in ("WRF-01", "WRF-02", "WRF-03", "WRF-04", "WRF-05",
                      "WRF-06", "Anti-example", "Positive review",
                      "NOT VERIFIED", "ILLUSTRATIVE", "NOT SHOWN"):
            with self.subTest(label=label):
                self.assertIn(label.lower(), body.lower())

    def test_no_parallel_wireframe_canonical_concepts(self):
        ids = [e["id"] for e in self.entries]
        self.assertEqual(len(ids), len(set(ids)))
        # New unrelated catalog entries must not break wireframe ownership.
        self.assertEqual([e["id"] for e in self.entries if "wireframe" in e["id"]],
                         ["guidance.wireframe-methodology"])


if __name__ == "__main__":
    unittest.main()
