# AquaTrack — Proposed Architecture

## Current demonstration
CSV sample readings → Python rule checks → console warnings.

## Intended system
1. **Sensing layer:** vibration/acoustic sensor plus TDS and turbidity sensors.
2. **Edge layer:** ESP32 samples readings, validates them, and can apply lightweight rules.
3. **Communication layer:** Wi-Fi, GSM, or LoRa depending on site connectivity.
4. **Application layer:** dashboard stores timestamped readings and displays alerts/trends.
5. **Response layer:** a user checks a suspected leak or quality change and arranges appropriate inspection/testing.

```text
[Vibration / Acoustic]   [TDS]   [Turbidity]
          \                |        /
                   [ESP32 edge device]
                            |
                 [Connectivity / gateway]
                            |
                [Dashboard + alert service]
                            |
              [Human inspection / water testing]
```

## Important limitations
- This repository does not yet contain ESP32 firmware or a live dashboard.
- Sample readings are illustrative, not measured field data.
- Thresholds require calibration and validation for the intended installation.
- TDS/turbidity sensors are screening indicators, not a complete test of microbiological or chemical safety.
