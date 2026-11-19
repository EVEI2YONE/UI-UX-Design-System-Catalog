"""Source-level acceptance for the nine-concept quality pass.

Checks *written* contracts and examples only; does not certify product behavior,
independent human review, accessibility conformance or usability outcomes.
"""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CONCEPTS = {
    "architecture.component-model": ("## Reuse decision: one canonical route", "## Component inventory to canonical contract mapping"),
    "foundation.visual-craftsmanship": ("## Select a visual direction in five decisions", "## Art-direction research, exploration and selection"),
    "foundation.design-tokens": ("## Choose the owner before editing values", "## Token authoring, interchange and release contract"),
    "foundation.practical-styling": ("## Recipe chooser — context before CSS", "## Utility-first styling ownership reference"),
    "principle.visual-hierarchy": ("## One-minute screen hierarchy contract", "## Operational review rubric"),
    "architecture.reference-examples": ("## Choosing the right reference", "## Acceptance experiment: detect the wrong owner"),
    "architecture.enterprise-multiapp": ("## Topology chooser", "## Enterprise example: changing a cross-app Dialog contract"),
    "foundation.icon-semantics": ("## Decide the role before selecting a glyph", "## Icon-only action state and geometry contract"),
    "guidance.ux-measurement": ("## Measurement decision — specify before collecting events", "## Catalog discoverability and source-trust study protocol"),
}


class FullQualityBatchSourceContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = {e["id"]: e for e in json.loads((ROOT / "catalog/index.json").read_text())["entries"]}
        cls.scorecard = {e["id"]: e for e in json.loads((ROOT / "catalog/concept-scorecard.json").read_text())["concepts"]}

    def source(self, identifier):
        return (ROOT / self.index[identifier]["path"]).read_text(encoding="utf-8")

    def test_decision_precedes_reference_detail_and_mentions_evidence(self):
        for identifier, (entry, detail) in CONCEPTS.items():
            with self.subTest(identifier=identifier):
                text = self.source(identifier)
                self.assertIn(entry, text)
                self.assertIn(detail, text)
                self.assertLess(text.index(entry), text.index(detail))
                self.assertIn("NOT VERIFIED", text.upper())
                self.assertGreaterEqual(len(re.findall(r"https://[^\s)]+", text)), 2)
                self.assertEqual(len(re.findall(r"^```", text, re.M)) % 2, 0)
                self.assertEqual(self.index[identifier]["status"], "proposed")
                self.assertIsNone(self.index[identifier]["reviewed_at"])
                self.assertEqual(self.scorecard[identifier]["evidence_level"], "E0")

    def test_dtcg_example_is_self_contained_valid_json(self):
        src = self.source("foundation.design-tokens")
        block = src.split("## Token authoring, interchange and release contract", 1)[1]
        match = re.search(r"```json\n(.*?)\n```", block, re.S)
        self.assertIsNotNone(match)
        tokens = json.loads(match.group(1))
        self.assertEqual(tokens["spacing"]["$type"], "dimension")
        self.assertEqual(tokens["spacing"]["compact"]["$value"], {"value": 8, "unit": "px"})
        self.assertEqual(tokens["spacing"]["comfortable"]["$value"], {"value": 16, "unit": "px"})

    def test_illustrative_typescript_signature_and_architecture_negative_fixture(self):
        styling = self.source("foundation.practical-styling")
        self.assertIn("onSave: () => void", styling)
        self.assertNotIn("onSave: => void", styling)
        architecture = self.source("architecture.reference-examples")
        for required in ("shared/ui/Dialog", "features/projects/projectApi", "REJECT", "ALLOW",
                         "not runnable standalone"):
            self.assertIn(required.casefold(), architecture.casefold())

    def test_editorial_dimensions_are_formula_consistent_and_separate_from_evidence(self):
        doc = json.loads((ROOT / "catalog/concept-scorecard.json").read_text())
        keys = ("purpose", "actionability", "coverage", "research",
                "discoverability", "verification", "signal_to_noise")
        self.assertEqual(sum(doc["weights_percent"].values()), 100)
        self.assertEqual(set(self.index), set(self.scorecard))
        for identifier in CONCEPTS:
            with self.subTest(identifier=identifier):
                e = self.scorecard[identifier]
                self.assertEqual(set(e["dimensions"]), set(keys))
                score = sum(doc["weights_percent"][k] * e["dimensions"][k] / 4 for k in keys)
                self.assertEqual(e["score"], int(score + 0.5))
                self.assertGreaterEqual(len(e["next_action"]), 25)


if __name__ == "__main__":
    unittest.main()
