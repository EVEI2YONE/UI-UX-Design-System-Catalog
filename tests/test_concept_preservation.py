"""Protect durable, explicitly noncanonical concept decisions from drift.

The manifest is a documentary inventory. Only catalog/index.json allocates
canonical identities and only a human review can promote candidate concepts.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "docs/visual-catalog-refactor"
LEDGER = FOLDER / "17-concept-inventory-and-decisions.md"
MANIFEST = FOLDER / "concepts/decision-manifest.json"

class ConceptPreservationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.registry = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.registry_ids = {item["id"] for item in cls.registry}
        cls.ledger = LEDGER.read_text(encoding="utf-8")
        cls.plan = (FOLDER / "02-concepts-and-content-plan.md").read_text(encoding="utf-8")

    def test_ten_source_concepts_have_durable_decisions(self):
        items = self.manifest["records"]
        self.assertEqual(len(items), 10)
        self.assertEqual({x["origin_id"] for x in items},
                         {f"F-{i:02d}" for i in range(1, 6)} |
                         {f"C-{i:02d}" for i in range(1, 6)})
        self.assertEqual(len({x["proposed_id"] for x in items}), len(items))
        self.assertEqual(len({x["artifact_path"] for x in items}), len(items))
        self.assertEqual(self.manifest["review_approval"], "not-recorded")
        for row in items:
            with self.subTest(concept=row["origin_id"]):
                self.assertIn(row["origin_id"], self.ledger)
                self.assertTrue((ROOT / row["artifact_path"]).is_file())
                self.assertIn(row["proposed_id"], (ROOT / row["artifact_path"]).read_text(encoding="utf-8"))

    def test_only_the_existing_review_workspace_is_canonical(self):
        self.assertEqual(len(self.registry), 54)
        self.assertEqual(set(self.registry_ids & {x["proposed_id"] for x in self.manifest["records"]}),
                         {"feature.review-workspace"})
        for row in self.manifest["records"]:
            if row["origin_id"] == "F-01":
                self.assertEqual(row["disposition"], "registered-reference")
                self.assertEqual(row["canonical_id"], "feature.review-workspace")
                self.assertEqual(next(e["status"] for e in self.registry if e["id"]==row["canonical_id"]), "proposed")
            else:
                self.assertIn(row["disposition"], {"deferred", "covered-existing"})
                self.assertIsNone(row["canonical_id"])
                self.assertNotIn(row["proposed_id"], self.registry_ids)

    def test_existing_owners_are_real_registry_ids(self):
        for row in self.manifest["records"]:
            with self.subTest(concept=row["origin_id"]):
                self.assertGreater(len(row["existing_owners"]), 0)
                for ref in row["existing_owners"]:
                    self.assertIn(ref, self.registry_ids)

    def test_all_briefs_are_explicitly_unreviewed_noncanonical_records(self):
        for row in self.manifest["records"]:
            if row["origin_id"] == "F-01":
                continue
            with self.subTest(concept=row["origin_id"]):
                doc = (ROOT / row["artifact_path"]).read_text(encoding="utf-8")
                for phrase in ["NOT a canonical catalog specification", "Owner:** unassigned",
                               "Reviewer approval:** not recorded", "Evidence needed for promotion",
                               "Existing canonical knowledge", "Non-goals:"]:
                    self.assertIn(phrase, doc)
                self.assertIn(row["disposition"], doc)

    def test_knowledge_gap_closure_is_explicit_for_every_original_gap(self):
        gaps = set(re.findall(r"\bKG-\d{2}\b", (FOLDER / "03-knowledge-gap-audit.md").read_text(encoding="utf-8")))
        self.assertEqual(gaps, {f"KG-{i:02d}" for i in range(1, 13)})
        self.assertTrue(gaps.issubset(set(re.findall(r"\bKG-\d{2}\b", self.ledger))))

    def test_open_knowledge_work_packages_are_durable_and_not_catalog_entries(self):
        required = {
            "KG-07": "kg07-accessibility-performance.md",
            "KG-08": "kg08-source-readability.md",
            "KG-10": "kg10-release-security-hosting.md",
            "KG-11": "kg11-source-usability.md",
            "KG-12": "kg12-discovery-research.md",
        }
        index = (FOLDER / "19-open-knowledge-work.md").read_text(encoding="utf-8")
        for gap, name in required.items():
            with self.subTest(gap=gap):
                self.assertIn(gap, index)
                self.assertIn(name, index)
                content = (FOLDER / "gap-work" / name).read_text(encoding="utf-8")
                self.assertIn(gap, content)
                self.assertIn("knowledge specification FILLED", content)
                self.assertIn("follow-up OPEN", content)
                self.assertIn("Acceptance evidence required", content)
                self.assertIn("Nonclaims and deferral rule", content)
                self.assertNotIn(name.removesuffix(".md"), self.registry_ids)

    def test_historical_plan_remains_source_of_candidate_intent(self):
        for term in ["F-01", "F-02", "F-03", "F-04", "F-05",
                     "Search/filter collection", "Responsive information dashboard",
                     "Feedback center", "Workspace navigation shell", "Onboarding composition"]:
            self.assertIn(term.lower(), self.plan.lower())

if __name__ == "__main__":
    unittest.main()
