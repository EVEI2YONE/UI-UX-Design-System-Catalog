"""Concept-only content checks independent of the static website renderer."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from catalog.core.editorial import findings


class EditorialShellTests(unittest.TestCase):
    def test_histories_are_rejected_at_the_source(self):
        for text in ("## Batch 8 extension", "## Phase 6 executable reference",
                     "Added on PR #13", "## CKG-01 — former ticket heading"):
            self.assertTrue(findings(text), text)
        for text in ("## Validation and recovery", "## Application migration strategy",
                     "**Status:** proposed", "## Evidence and review", "## Phase-aware task UI"):
            self.assertFalse(findings(text), text)

    def test_every_canonical_document_is_concept_first(self):
        entries = json.loads((ROOT / "catalog/index.json").read_text(encoding="utf-8"))["entries"]
        for item in entries:
            with self.subTest(id=item["id"]):
                text = (ROOT / item["path"]).read_text(encoding="utf-8")
                self.assertFalse(findings(text), item["id"])
