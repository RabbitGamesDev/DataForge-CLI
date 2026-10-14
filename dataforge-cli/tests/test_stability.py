import json
import os
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import patch

import dataforge.core as core
import main


class CoreSafetyTests(unittest.TestCase):
    def test_scanner_respects_gitignore_and_sensitive_filenames(self):
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            (root_path / ".gitignore").write_text("private/\n*.local.json\n", encoding="utf-8")
            (root_path / "app.py").write_text("print('ok')", encoding="utf-8")
            (root_path / ".env").write_text("API_KEY=not-a-real-key", encoding="utf-8")
            (root_path / "config.local.json").write_text("{}", encoding="utf-8")
            (root_path / "private").mkdir()
            (root_path / "private" / "secret.py").write_text("secret", encoding="utf-8")

            found = {Path(p).relative_to(root_path).as_posix() for p in core.get_all_files(root)}
            self.assertEqual(found, {"app.py"})

    def test_large_file_read_is_truncated(self):
        with tempfile.TemporaryDirectory() as root:
            file_path = Path(root) / "large.py"
            file_path.write_text("x" * 100, encoding="utf-8")
            result = core.read_file_content(str(file_path), max_bytes=10)
            self.assertTrue(result.startswith("x" * 10))
            self.assertIn("truncated", result)
            self.assertLess(len(result), 100)


class ExportSafetyTests(unittest.TestCase):
    def test_html_export_escapes_report_markup(self):
        with tempfile.TemporaryDirectory() as root:
            report_dir = Path(root) / "dataforge-reports"
            report_dir.mkdir()
            (report_dir / "report.txt").write_text("<script>alert('x')</script>", encoding="utf-8")
            with patch.object(main, "is_pro_active", return_value=True):
                main.run_export(root, "--html")
            html_path = report_dir / "report.html"
            exported = html_path.read_text(encoding="utf-8")
            self.assertIn("&lt;script&gt;", exported)
            self.assertNotIn("<script>", exported)


class LicenseGraceTests(unittest.TestCase):
    def _write_license(self, path, last_checked=None):
        payload = {"active": True, "key": "test-key", "tier": "pro"}
        if last_checked is not None:
            payload["last_checked"] = last_checked
        path.write_text(json.dumps(payload), encoding="utf-8")

    def test_offline_without_prior_successful_check_is_denied(self):
        with tempfile.TemporaryDirectory() as root:
            license_path = Path(root) / "license.json"
            self._write_license(license_path)
            with patch.object(main, "LICENSE_FILE", str(license_path)), patch.object(
                main.urllib.request, "urlopen", side_effect=OSError("offline")
            ):
                self.assertFalse(main.verify_license_hybrid())

    def test_offline_with_recent_successful_check_is_allowed(self):
        with tempfile.TemporaryDirectory() as root:
            license_path = Path(root) / "license.json"
            recent = (datetime.now() - timedelta(days=2)).isoformat()
            self._write_license(license_path, recent)
            with patch.object(main, "LICENSE_FILE", str(license_path)), patch.object(
                main.urllib.request, "urlopen", side_effect=OSError("offline")
            ):
                self.assertTrue(main.verify_license_hybrid())

    def test_offline_with_stale_successful_check_is_denied(self):
        with tempfile.TemporaryDirectory() as root:
            license_path = Path(root) / "license.json"
            stale = (datetime.now() - timedelta(days=9)).isoformat()
            self._write_license(license_path, stale)
            with patch.object(main, "LICENSE_FILE", str(license_path)), patch.object(
                main.urllib.request, "urlopen", side_effect=OSError("offline")
            ):
                self.assertFalse(main.verify_license_hybrid())


if __name__ == "__main__":
    unittest.main()
