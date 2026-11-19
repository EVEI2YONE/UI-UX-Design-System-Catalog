"""Coverage regression for newly proposed concept scaffolds and discoverability."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup

ADDED = {
    "component.combobox", "component.radio-group", "component.switch",
    "component.tabs", "component.disclosure", "component.textarea",
    "component.menu-button", "component.date-time-input", "component.tooltip",
    "component.popover", "component.slider", "component.tree-view",
    "pattern.onboarding-first-use", "pattern.file-upload",
    "pattern.collaboration-sharing", "pattern.content-publishing",
    "pattern.scheduling-availability", "pattern.checkout",
    "pattern.master-detail", "pattern.comparison-decision",
    "guidance.content-architecture", "guidance.inclusive-design",
    "foundation.responsive-composition", "guidance.ia-validation",
    "guidance.ethical-engagement", "governance.adoption-change",
}
SECTIONS = (
    "specifications/components/README.md", "specifications/patterns/README.md",
    "knowledge/guidance/README.md", "knowledge/foundations/README.md",
    "governance/README.md",
)

class NewConceptScaffoldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_all_new_concepts_registered_once(self):
        self.assertEqual(len(ADDED), 26)
        self.assertTrue(ADDED.issubset(self.by_id))
        self.assertGreaterEqual(len(self.entries), 80)
        self.assertEqual(len({row["path"] for row in self.entries}), len(self.entries))

    def test_proposed_documents_have_contracts_and_are_indexed(self):
        section_contents = {
            p: (ROOT / p).read_text(encoding="utf-8") for p in SECTIONS
        }
        for ident in sorted(ADDED):
            with self.subTest(ident=ident):
                entry = self.by_id[ident]
                doc = (ROOT / entry["path"]).read_text(encoding="utf-8")
                self.assertTrue(doc.startswith("# " + entry["title"] + "\n"))
                for marker in ("## Purpose and", "Use when:", "Avoid when:", "NOT VERIFIED"):
                    self.assertIn(marker, doc)
                self.assertTrue("## Example and anti-example" in doc or
                                "## Example / anti-example" in doc)
                self.assertEqual(entry["status"], "proposed")
                self.assertEqual(entry["owner"], "unassigned")
                self.assertIsNone(entry["reviewed_at"])
                self.assertNotIn("implementation", entry)
                self.assertEqual(lookup(self.entries, ident, limit=1)[0]["id"], ident)
                self.assertTrue(any(entry["title"] in content for content in section_contents.values()))

    def test_synthetic_retrieval_phrases_resolve(self):
        cases = {
            "radio buttons": "component.radio-group",
            "autocomplete": "component.combobox",
            "onboarding": "pattern.onboarding-first-use",
            "file upload": "pattern.file-upload",
            "content architecture": "guidance.content-architecture",
            "ethical engagement": "guidance.ethical-engagement",
            "change management": "governance.adoption-change",
        }
        for query, owner in cases.items():
            with self.subTest(query=query):
                self.assertEqual(lookup(self.entries, query, limit=1)[0]["id"], owner)

if __name__ == "__main__":
    unittest.main()
