"""研究筆記登錄表：真實登錄表要過，常見的錯要被擋下。"""
from copy import deepcopy
import sys
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import check_notes  # noqa: E402


class TestCheckNotes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = yaml.safe_load(check_notes.REGISTRY.read_text(encoding="utf-8"))
        cls.content_ids = check_notes._content_ids()
        cls.question_ids = check_notes._question_ids()

    def _check(self, registry):
        return check_notes.check(registry, self.content_ids, self.question_ids)

    def _first_note(self, registry):
        return registry["notes"][0]

    def test_real_registry_passes(self):
        self.assertEqual([], self._check(self.registry))

    def test_unregistered_file_is_reported(self):
        reg = deepcopy(self.registry)
        dropped = reg["notes"].pop(0)
        errors = self._check(reg)
        self.assertTrue(any("未登錄" in e and Path(dropped["path"]).name in e for e in errors))

    def test_internal_header_summary_rejected(self):
        reg = deepcopy(self.registry)
        self._first_note(reg)["summary_zh"] = "建立日期：2026-04-17"
        self.assertTrue(any("內部頁首" in e for e in self._check(reg)))

    def test_undeclared_theme_and_duplicate_slug(self):
        reg = deepcopy(self.registry)
        reg["notes"][0]["theme"] = "no-such-theme"
        reg["notes"][1]["slug"] = reg["notes"][2]["slug"]
        errors = self._check(reg)
        self.assertTrue(any("未在 groups 宣告" in e for e in errors))
        self.assertTrue(any("slug 重複" in e for e in errors))

    def test_graduated_needs_existing_unit(self):
        reg = deepcopy(self.registry)
        note = self._first_note(reg)
        note["status"] = "graduated"
        self.assertTrue(any("graduated_to 空白" in e for e in self._check(reg)))
        note["graduated_to"] = ["tech.no-such-unit"]
        self.assertTrue(any("不是存在的知識點" in e for e in self._check(reg)))

    def test_bad_certainty_and_missing_question(self):
        reg = deepcopy(self.registry)
        note = self._first_note(reg)
        note["findings"][0]["certainty"] = "綠"
        note["open_questions"] = ["fq.99.9"]
        errors = self._check(reg)
        self.assertTrue(any("certainty" in e for e in errors))
        self.assertTrue(any("fq.99.9" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
