"""B02 knowledge retrieval and contract checks (not runtime UI tests)."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from find_concept import lookup  # noqa: E402

EXPECTED = {
    "component event ownership": "architecture.component-contracts",
    "cross component events": "architecture.component-contracts",
    "composite component anatomy": "architecture.component-contracts",
    "nested interactive controls": "architecture.component-contracts",
    "controlled uncontrolled state": "architecture.component-contracts",
    "component event propagation": "architecture.component-contracts",
    "semantic icon registry": "foundation.icon-semantics",
    "button action": "component.button",
}

class ComponentEventKnowledgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        cls.by_id = {entry["id"]: entry for entry in cls.entries}

    def test_queries_resolve_to_existing_canonical_contract(self):
        for query, expected in EXPECTED.items():
            with self.subTest(query=query):
                result = lookup(self.entries, query, limit=1)
                self.assertTrue(result, f"no results for {query!r}")
                self.assertEqual(result[0]["id"], expected)

    def test_contract_has_all_b02_topics_and_boundaries(self):
        contract = self.by_id["architecture.component-contracts"]
        self.assertEqual(contract["status"], "proposed")
        self.assertIsNone(contract["reviewed_at"])
        page = (ROOT / contract["path"]).read_text(encoding="utf-8")
        for term in (
            "CKG-04", "CKG-06", "CKG-07", "CKG-08",
            "Component event", "Feature/workflow command", "Domain/authoritative outcome",
            "controlled", "nested", "NOT VERIFIED",
        ):
            with self.subTest(term=term):
                self.assertIn(term, page)

    def test_index_and_context_are_discoverable(self):
        self.assertTrue((ROOT / "archive/planning/icon-interaction-b02-context-2026-11-07.md").is_file())
        for file in ("README.md", "architecture/README.md", "components/README.md", "AGENTS.md"):
            with self.subTest(file=file):
                s = (ROOT / file).read_text(encoding="utf-8")
                self.assertIn("component-contracts", s)

    def test_no_new_duplicate_component_id(self):
        ids = [e["id"] for e in self.entries]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(sum(e["id"] == "architecture.component-contracts" for e in self.entries), 1)

if __name__ == "__main__":
    unittest.main()
