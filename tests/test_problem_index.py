"""問題索引必須通過實際掃檔與關係收集，不能只有 YAML 可讀。"""
from tests.test_validate import FixtureTestBase


class TestProblemRegistration(FixtureTestBase):
    def test_missing_id_is_detected_in_new_file(self):
        self._write_yaml(self.canonical_dir / "instructional/problems.yaml", {
            "problems": [{"title": "抬頭後沉髖"}],
        })
        errors, _, _ = self._run()
        self.assertTrue(errors["E001"])

    def test_both_intervention_paths_check_real_ids(self):
        self._write_yaml(self.canonical_dir / "instructional/problems.yaml", {
            "problems": [{"id": "prob.breast.head-lift", "links": {
                "interventions": ["movement.intervention.missing"],
                "water_interventions": ["movement.intervention.water-missing"],
            }}],
        })
        errors, warnings, _ = self._run()
        self.assertEqual(2, len(errors["E003"]))
        self.assertFalse(warnings["W005"])

    def test_empty_problem_file_does_not_create_entries(self):
        self._write_yaml(self.canonical_dir / "instructional/problems.yaml", {
            "categories": [], "problems": [],
        })
        errors, _, count = self._run()
        self.assertEqual(0, count)
        self.assertFalse(errors["E001"])
