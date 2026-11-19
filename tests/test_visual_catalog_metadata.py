"""Document-only registry and catalog metadata compatibility checks."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup
from validate_catalog import validate_concept_metadata

class DocumentationMetadataContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index=json.loads((ROOT/"catalog/index.json").read_text(encoding="utf-8"))
        cls.schema=json.loads((ROOT/"catalog/schema.json").read_text(encoding="utf-8"))

    def test_durable_concept_fields_and_no_executable_registration(self):
        required=set(self.schema["$defs"]["entry"]["required"])
        self.assertTrue({"id","title","path","layer","kind","status","summary",
                         "aliases","domains","use_when","avoid_when","related",
                         "depends_on","owner","reviewed_at"} <= required)
        properties=self.schema["$defs"]["entry"]["properties"]
        self.assertIn("capabilities",properties)
        self.assertNotIn("implementation",properties)
        self.assertFalse(self.schema["$defs"]["entry"]["additionalProperties"])
        self.assertFalse(any("implementation" in e for e in self.index["entries"]))

    def test_concept_capabilities_are_searchable_not_executable(self):
        entries=self.index["entries"]
        core=[e for e in entries if e["id"] in {
            "component.button","component.input","component.select",
            "component.checkbox","component.dialog","component.field"}]
        self.assertEqual(len(core),6)
        for e in core:
            self.assertTrue(e.get("capabilities"))
            self.assertEqual(validate_concept_metadata(e),[])

    def test_invalid_capabilities_and_implementation_metadata_are_rejected(self):
        for value in [["one","ONE"],["","two"],["ok",2],"not-a-list"]:
            self.assertTrue(validate_concept_metadata({"id":"test","capabilities":value}))
        self.assertTrue(validate_concept_metadata({
            "id":"test", "implementation":{"status":"reference"}}))

    def test_existing_retrieval_identity_is_preserved(self):
        for query,expected in {
            "component.button":"component.button",
            "loading button":"component.button",
            "component hierarchy":"architecture.component-model",
            "modal dialog":"component.dialog",
            "settings":"pattern.account-settings-portal",
        }.items():
            with self.subTest(query=query):
                found=lookup(self.index["entries"],query,limit=1)
                self.assertTrue(found)
                self.assertEqual(found[0]["id"],expected)

if __name__=="__main__":
    unittest.main()
