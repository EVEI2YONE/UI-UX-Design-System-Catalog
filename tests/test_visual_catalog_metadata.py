"""Phase 2 optional visual metadata acceptance tests; no UI runtime claimed."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from find_concept import lookup
from validate_catalog import validate_visual_metadata


class VisualMetadataContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))
        cls.schema = json.loads((ROOT / "catalog/schema.json").read_text(encoding="utf-8"))

    def test_required_legacy_fields_remain(self):
        required = set(self.schema["$defs"]["entry"]["required"])
        self.assertTrue({"id", "title", "path", "layer", "kind", "status", "summary", "aliases",
                         "domains", "use_when", "avoid_when", "related", "depends_on",
                         "owner", "reviewed_at"} <= required)
        self.assertFalse({"implementation", "capabilities"} & required)
        self.assertFalse(self.schema["$defs"]["entry"]["additionalProperties"])

    def test_six_existing_controls_are_enriched_without_implementations(self):
        controls = [x for x in self.index["entries"] if x["id"].startswith("component.")]
        self.assertEqual(len(controls), 6)
        for entry in controls:
            self.assertTrue(entry["capabilities"])
            self.assertNotIn("implementation", entry)
            self.assertEqual(validate_visual_metadata(entry, ROOT), [])

    def test_existing_lookup_order_remains(self):
        for query, expected in {
            "component.button": "component.button",
            "loading button": "component.button",
            "component hierarchy": "architecture.component-model",
            "modal dialog": "component.dialog",
            "settings": "pattern.account-settings-portal"
        }.items():
            with self.subTest(query=query):
                found = lookup(self.index["entries"], query, limit=1)
                self.assertTrue(found)
                self.assertEqual(found[0]["id"], expected)

    def test_invalid_capability_types_and_duplicates_fail(self):
        for value in [["one", "ONE"], ["", "two"], ["ok", 2], "not-a-list"]:
            self.assertTrue(validate_visual_metadata({"id": "test", "capabilities": value}, ROOT))

    def test_reference_requires_existing_local_source_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            base = root / "site/src/implementations/components/button"
            base.mkdir(parents=True)
            (base / "Button.tsx").write_text("export function Button() {}", encoding="utf-8")
            (base / "scenarios.ts").write_text("export const scenarios = []", encoding="utf-8")
            entry = {"id": "component.button",
                     "implementation": {
                         "status": "reference",
                         "source_path": "site/src/implementations/components/button/Button.tsx",
                         "scenario_manifest": "site/src/implementations/components/button/scenarios.ts",
                         "preview_path": "/catalog/components/button"
                     }}
            self.assertEqual(validate_visual_metadata(entry, root), [])
            entry["implementation"]["source_path"] = "site/src/implementations/../../secret.tsx"
            self.assertTrue(validate_visual_metadata(entry, root))

    def test_verified_requires_evidence(self):
        entry = {"id": "component.button", "implementation": {
            "status": "verified",
            "source_path": "site/src/implementations/components/button/Button.tsx",
            "scenario_manifest": "site/src/implementations/components/button/scenarios.ts",
            "preview_path": "/catalog/components/button"
        }}
        self.assertTrue(any("evidence_path" in x for x in validate_visual_metadata(entry, ROOT)))


if __name__ == "__main__":
    unittest.main()
