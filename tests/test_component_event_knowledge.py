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

    def test_no_new_duplicate_component_id(self):
        ids = [e["id"] for e in self.entries]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(sum(e["id"] == "architecture.component-contracts" for e in self.entries), 1)

if __name__ == "__main__":
    unittest.main()
