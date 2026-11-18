"""Negative tests for malformed catalog inputs. No UI conformance is asserted."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_catalog


class ValidatorDefensiveTests(unittest.TestCase):
    def validate_payload(self, payload):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "catalog").mkdir()
            (root / "catalog/index.json").write_text(json.dumps(payload), encoding="utf-8")
            (root / "catalog/schema.json").write_text(
                (ROOT / "catalog/schema.json").read_text(encoding="utf-8"), encoding="utf-8")
            stream = io.StringIO()
            with patch.object(validate_catalog, "ROOT", root), patch.object(
                validate_catalog, "INDEX", root / "catalog/index.json"
            ), contextlib.redirect_stdout(stream):
                result = validate_catalog.main()
            return result, stream.getvalue()

    def test_non_array_entries_fail_with_diagnostic(self):
        result, output = self.validate_payload({"entries": {}, "status_model": []})
        self.assertEqual(result, 1)
        self.assertIn("entries must be an array", output)

    def test_missing_fields_fail_without_exception(self):
        result, output = self.validate_payload({
            "entries": [{"id": "bad.entry"}],
            "status_model": ["proposed", "experimental", "stable", "deprecated", "removed"],
        })
        self.assertEqual(result, 1)
        self.assertIn("missing", output)

    def test_non_object_entries_fail_without_exception(self):
        result, output = self.validate_payload({
            "entries": [None],
            "status_model": ["proposed", "experimental", "stable", "deprecated", "removed"],
        })
        self.assertEqual(result, 1)
        self.assertIn("must be an object", output)


if __name__ == "__main__":
    unittest.main()
