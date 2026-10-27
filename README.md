# AquaTrack
AI-assisted water leak and water-quality monitoring — starter prototype

## Status
This repository contains an **early software demonstration using sample/simulated sensor readings**. It is not connected to physical sensors and does not certify that water is safe to drink.

## Problem
Water leaks and changes in water-quality indicators can go unnoticed when monitoring depends only on periodic manual checks.

## Proposed solution
AquaTrack is designed to combine:
- Vibration/acoustic signals to help flag possible leaks
- TDS and turbidity sensors to track water-quality indicators
- An ESP32 edge device for collecting and processing readings
- A dashboard and alerts for unusual readings

## What this starter demonstrates
The Python script reads `data/sample_data.csv`, applies simple example thresholds, and prints possible leak or water-quality warnings. These are **illustrative rules**, not validated diagnostic models.

## Run locally
Requires Python 3.10 or newer.

```bash
python src/aquatrack.py
```

Run tests:
```bash
python -m unittest discover -s tests -v
```

## Repository structure
```text
AquaTrack/
├── README.md
├── LICENSE
├── data/sample_data.csv
├── docs/architecture.md
├── src/aquatrack.py
└── tests/test_aquatrack.py
```

## Example interpretation
- `vibration_score` and `acoustic_score` are illustrative normalized scores from 0 to 1.
- `tds_ppm` and `turbidity_ntu` are example sensor readings.
- Thresholds in the code are configurable demonstration values, not official safety limits.
- A TDS or turbidity reading alone cannot determine whether water is potable. Use appropriate laboratory testing and applicable local standards for safety decisions.

## Roadmap
1. Replace sample data with readings from calibrated sensors.
2. Connect an ESP32 and document wiring, calibration, and firmware.
3. Add a dashboard and notification service.
4. Validate detection performance against labelled real-world data.
5. Review privacy, reliability, safety, and deployment costs before field use.

## Social impact
The project aims to support earlier leak detection, reduce avoidable water loss, and help communities monitor changes in water-quality indicators.

## Contribution
Contributions and feedback are welcome. Please document whether results come from simulation or physical measurements.
