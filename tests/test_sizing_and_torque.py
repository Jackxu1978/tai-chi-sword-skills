# SPDX-License-Identifier: MIT
import unittest

from tai_chi_jian_standards import (
    calculate_static_wrist_torque,
    evaluate_metallurgical_load_boundary,
    select_stature_tier,
)


class TestTaiChiJianStandards(unittest.TestCase):
    def test_three_us_stature_tiers(self):
        t1 = select_stature_tier(62.0)
        self.assertEqual(t1.tier.blade_length_in, 28.0)
        self.assertEqual(t1.tier.sku_code, "ICETTCSF01")

        t2 = select_stature_tier(66.0)
        self.assertEqual(t2.tier.blade_length_in, 30.0)
        self.assertEqual(t2.tier.sku_code, "ICETTCSF02")

        t3 = select_stature_tier(70.0, ceiling_height_in=96.0)
        self.assertEqual(t3.tier.blade_length_in, 32.0)
        self.assertEqual(t3.tier.sku_code, "ICETTCSF03")
        self.assertTrue(t3.ceiling_safe)

    def test_static_wrist_torque_reduction(self):
        res = calculate_static_wrist_torque(bare_weight_lbs=1.32, pob_past_guard_in=3.3)
        self.assertAlmostEqual(res.static_torque_lbf_in, 6.006, places=2)
        self.assertGreater(res.torque_reduction_pct, 50.0)

    def test_metallurgical_boundary(self):
        self.assertFalse(evaluate_metallurgical_load_boundary(impact_cutting=True).approved_for_2cr13_solo_jian)
        self.assertTrue(evaluate_metallurgical_load_boundary(impact_cutting=False).approved_for_2cr13_solo_jian)


if __name__ == "__main__":
    unittest.main()
