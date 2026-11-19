"""Contract checks for proposed operational and selection concepts."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup

NEW_CONCEPTS = {
    "pattern.data-import": "specifications/patterns/data-import-and-migration.md",
    "pattern.access-requests": "specifications/patterns/permissions-and-access-requests.md",
    "pattern.data-export": "specifications/patterns/data-export-and-background-jobs.md",
    "pattern.commenting-annotations": "specifications/patterns/commenting-and-annotations.md",
    "pattern.reporting-appeals": "specifications/patterns/reporting-moderation-and-appeals.md",
    "pattern.activity-history": "specifications/patterns/activity-timelines-and-history.md",
    "pattern.rich-text-editing": "specifications/patterns/rich-text-editing.md",
    "pattern.live-updates": "specifications/patterns/real-time-data-and-live-updates.md",
    "pattern.workflow-automation": "specifications/patterns/workflow-automation-and-rule-builders.md",
    "pattern.collection-views": "specifications/patterns/collection-and-feed-views.md",
    "component.progress-indicator": "specifications/components/progress-indicator/spec.md",
    "component.listbox": "specifications/components/listbox/spec.md",
}
ALIAS_QUERIES = {
    "import preview": "pattern.data-import",
    "request access": "pattern.access-requests",
    "background export": "pattern.data-export",
    "inline comments": "pattern.commenting-annotations",
    "report abuse": "pattern.reporting-appeals",
    "activity timeline": "pattern.activity-history",
    "rich text editor": "pattern.rich-text-editing",
    "live updates": "pattern.live-updates",
    "rule builder": "pattern.workflow-automation",
    "feed view": "pattern.collection-views",
    "progressbar": "component.progress-indicator",
    "listbox": "component.listbox",
}

class OperationalConceptScaffoldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_registered_ids_are_unique_and_new_entries_have_canonical_pages(self):
        self.assertEqual(len(NEW_CONCEPTS), 12)
        self.assertGreaterEqual(len(self.entries), 92)
        self.assertEqual(len(self.entries), len(self.by_id))
        self.assertEqual(len({row["path"] for row in self.entries}), len(self.entries))
        self.assertTrue(set(NEW_CONCEPTS).issubset(self.by_id))

    def test_new_pages_own_meaningful_proposed_specifications(self):
        section_readmes = {
            "component.": (ROOT / "specifications/components/README.md").read_text(encoding="utf-8"),
            "pattern.": (ROOT / "specifications/patterns/README.md").read_text(encoding="utf-8"),
        }
        for ident, expected_path in NEW_CONCEPTS.items():
            with self.subTest(ident=ident):
                item = self.by_id[ident]
                self.assertEqual(item["path"], expected_path)
                self.assertEqual(item["kind"], "specification")
                self.assertEqual(item["layer"], "components" if ident.startswith("component.") else "experiences")
                self.assertEqual(item["status"], "proposed")
                self.assertEqual(item["owner"], "unassigned")
                self.assertIsNone(item["reviewed_at"])
                self.assertNotIn("implementation", item)
                self.assertTrue(item["aliases"] and item["use_when"] and item["avoid_when"])
                self.assertTrue(item["related"] and item["depends_on"])
                doc = (ROOT / item["path"]).read_text(encoding="utf-8")
                self.assertTrue(doc.startswith("# " + item["title"] + "\n"))
                for label in ("## Purpose and boundaries", "Use when:", "Avoid when:",
                              "## Example and anti-example", "## Evidence and verification",
                              "## Sources, applicability and related concepts", "NOT VERIFIED"):
                    self.assertIn(label, doc)
                self.assertGreater(len(doc), 4500)
                readme = section_readmes["component." if ident.startswith("component.") else "pattern."]
                self.assertIn(item["title"], readme)
                self.assertIn("`" + ident + "`", readme)
                self.assertIn(expected_path.split("specifications/", 1)[1].split("/", 1)[0], expected_path)

    def test_searchable_aliases_resolve_to_new_canonical_owners(self):
        for query, ident in ALIAS_QUERIES.items():
            with self.subTest(query=query):
                results = lookup(self.entries, query, limit=1)
                self.assertTrue(results, query)
                self.assertEqual(results[0]["id"], ident)

    def test_existing_breadcrumb_and_pagination_ownership_not_duplicated(self):
        self.assertNotIn("component.breadcrumbs", self.by_id)
        self.assertNotIn("component.pagination", self.by_id)
        self.assertNotIn("pattern.pagination", self.by_id)

if __name__ == "__main__":
    unittest.main()
