"""Phase 9: deterministic human/agent discovery and source provenance regression tests."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
sys.path.insert(0,str(ROOT/"site"))
from find_concept import lookup
import build as site_build

class Phase9DiscoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries=json.loads((ROOT/"catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.cases=json.loads((ROOT/"tests/fixtures/phase9_retrieval_cases.json").read_text(encoding="utf-8"))
        cls.by_id={entry["id"]:entry for entry in cls.entries}
        cls.out=tempfile.TemporaryDirectory()
        cls.generated=Path(cls.out.name)/"site"
        site_build.build(cls.generated)

    @classmethod
    def tearDownClass(cls):
        cls.out.cleanup()

    def test_positive_queries_resolve_expected_first_owner(self):
        for case in self.cases["positive"]:
            with self.subTest(query=case["query"]):
                results=lookup(self.entries,case["query"])
                self.assertTrue(results,"no result for "+case["query"])
                self.assertEqual(results[0]["id"],case["expected_id"])

    def test_known_no_result_queries_are_explicitly_documented(self):
        for case in self.cases["negative"]:
            with self.subTest(query=case["query"]):
                self.assertEqual(lookup(self.entries,case["query"]),[],case["reason"])

    def test_ambiguous_queries_are_not_forced_to_one_concept(self):
        for case in self.cases["ambiguous"]:
            results={x["id"] for x in lookup(self.entries,case["query"])}
            self.assertIn(case["expected_contains"],results)

    def test_canonical_documents_and_relationships_resolve(self):
        self.assertEqual(len(self.by_id),len(self.entries))
        for entry in self.entries:
            with self.subTest(entry=entry["id"]):
                self.assertTrue((ROOT/entry["path"]).is_file())
                for rel in entry["related"]+entry["depends_on"]:
                    self.assertIn(rel,self.by_id)
                    self.assertNotEqual(rel,entry["id"])
                url=site_build.route(entry)
                page=self.generated/url.lstrip("/")/"index.html"
                self.assertTrue(page.is_file(),url)
                html=page.read_text(encoding="utf-8")
                self.assertIn(entry["id"],html)
                self.assertIn("View Markdown source",html)

    def test_reference_provenance_matches_actual_generated_source(self):
        for entry in self.entries:
            detail=(self.generated/site_build.route(entry).lstrip("/")/"index.html").read_text(encoding="utf-8")
            implementation=entry.get("implementation")
            if not implementation:
                self.assertIn("Specification only",detail)
                continue
            with self.subTest(entry=entry["id"]):
                self.assertIn("Inspect implementation source",detail)
                self.assertIn('sandbox="allow-scripts"',detail)
                self.assertNotIn("allow-same-origin",detail)
                source=ROOT/implementation["source_path"]
                scenario=ROOT/implementation["scenario_manifest"]
                self.assertTrue(source.is_file())
                self.assertTrue(scenario.is_file())
                bundled=self.generated/"reference"/entry["id"]
                self.assertEqual(source.read_bytes(),(bundled/"source.js").read_bytes())
                self.assertEqual(scenario.read_bytes(),(bundled/"scenarios.js").read_bytes())
                self.assertEqual(implementation["preview_path"]+"/",site_build.route(entry))
                self.assertEqual(entry["status"],"proposed")
                self.assertEqual(implementation["status"],"reference")

    def test_safe_source_ref_links_support_reviewed_branch_and_sha(self):
        branch = site_build.source_repo_url("docs/visual-catalog-refactor-blueprint")
        sha = site_build.source_repo_url("3b933abea778122dece31af7496f409028ed6198")
        self.assertIn("/blob/docs/visual-catalog-refactor-blueprint/", branch)
        self.assertIn("/blob/3b933abea778122dece31af7496f409028ed6198/", sha)
        for bad in ("", "../main", "/main", ".hidden", "main?x=1", "main#fragment", "https://other"):
            with self.subTest(ref=bad):
                with self.assertRaises(ValueError):
                    site_build.source_repo_url(bad)

    def test_website_search_export_is_derived_and_matches_all_entries(self):
        data=json.loads((self.generated/"catalog-search.json").read_text(encoding="utf-8"))
        self.assertEqual(len(data),len(self.entries))
        self.assertEqual({row["id"] for row in data},set(self.by_id))
        for row in data:
            with self.subTest(entry=row["id"]):
                entry=self.by_id[row["id"]]
                self.assertEqual(row["path"],entry["path"])
                self.assertEqual(row["title"],entry["title"])
                self.assertEqual(row["url"],site_build.route(entry))
                self.assertEqual(row["status"],entry["status"])

if __name__=="__main__":
    unittest.main()
