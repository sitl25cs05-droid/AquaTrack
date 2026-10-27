import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from aquatrack import classify_reading


class AquaTrackTests(unittest.TestCase):
    def test_normal_reading_no_alert(self):
        row = {
            "vibration_score": "0.2",
            "acoustic_score": "0.3",
            "tds_change_ppm": "20",
            "turbidity_change_ntu": "0.2",
        }
        self.assertEqual(classify_reading(row), [])

    def test_possible_leak_alert(self):
        row = {
            "vibration_score": "0.8",
            "acoustic_score": "0.2",
            "tds_change_ppm": "20",
            "turbidity_change_ntu": "0.2",
        }
        self.assertTrue(any("Possible leak pattern" in x for x in classify_reading(row)))

    def test_quality_indicator_alerts(self):
        row = {
            "vibration_score": "0.2",
            "acoustic_score": "0.2",
            "tds_change_ppm": "200",
            "turbidity_change_ntu": "1.2",
        }
        alerts = classify_reading(row)
        self.assertEqual(len(alerts), 2)


if __name__ == "__main__":
    unittest.main()
