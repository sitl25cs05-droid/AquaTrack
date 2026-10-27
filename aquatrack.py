"""AquaTrack sample-data demonstration.

This script uses illustrative rules on sample data. It is not a validated
leak-detection model and does not determine whether water is safe to drink.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "sample_data.csv"

# Demonstration thresholds only; calibrate and validate before real-world use.
VIBRATION_THRESHOLD = 0.70
ACOUSTIC_THRESHOLD = 0.70
TDS_CHANGE_THRESHOLD_PPM = 150
TURBIDITY_CHANGE_THRESHOLD_NTU = 1.0


def classify_reading(row):
    alerts = []
    vibration = float(row["vibration_score"])
    acoustic = float(row["acoustic_score"])
    tds_change = float(row["tds_change_ppm"])
    turbidity_change = float(row["turbidity_change_ntu"])

    if vibration >= VIBRATION_THRESHOLD or acoustic >= ACOUSTIC_THRESHOLD:
        alerts.append("Possible leak pattern — inspect the pipe/system")
    if tds_change >= TDS_CHANGE_THRESHOLD_PPM:
        alerts.append("TDS indicator changed — investigate and test water appropriately")
    if turbidity_change >= TURBIDITY_CHANGE_THRESHOLD_NTU:
        alerts.append("Turbidity indicator changed — investigate and test water appropriately")

    return alerts


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Sample data file not found: {DATA_FILE}")

    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            alerts = classify_reading(row)
            print(f'{row["timestamp"]} | {row["location_id"]}')
            if alerts:
                for alert in alerts:
                    print(f"  ALERT: {alert}")
            else:
                print("  No demonstration threshold triggered.")
            print()


if __name__ == "__main__":
    main()
