# SIM-003 MQTT Telemetry Simulator

# Release Notes

## Version 1.0.0

### Release Status

Final development release for the SIM-003 MQTT Telemetry Simulator.

## 1. Project Overview

The SIM-003 MQTT Telemetry Simulator generates simulated EV battery telemetry and provides cybersecurity testing scenarios.

The project includes:

- Battery telemetry generation
- Seven telemetry scenarios
- FastAPI REST API
- Streamlit dashboard
- Automated testing
- Security scenario testing
- CSV telemetry export

## 2. Implemented Features

### Telemetry Generation

The simulator generates battery parameters including:

- Voltage
- Current
- Temperature
- SOC
- SOH
- Timestamp

### Supported Scenarios

1. Normal
2. Delayed
3. Duplicate
4. Out-of-range
5. Missing timestamp
6. Spoofed ID
7. Replay attack

### FastAPI

Implemented endpoints:

- `GET /`
- `GET /health`
- `GET /scenarios`
- `POST /generate-events`
- `GET /sample`

### Streamlit Dashboard

The dashboard provides:

- Battery ID selection
- Scenario selection
- Event count selection
- Delay configuration
- Telemetry event table
- Anomaly count
- CSV download

## 3. Testing

Automated testing was performed using pytest.

Current result:

```text
19 passed
0 failed
71% coverage