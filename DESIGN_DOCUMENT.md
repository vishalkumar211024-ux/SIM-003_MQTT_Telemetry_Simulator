# SIM-003 MQTT Telemetry Simulator
## Design Document

## 1. Objective

The design provides a modular simulator for generating battery telemetry events and testing abnormal and cybersecurity-related scenarios.

The simulator works locally and does not require real BMS hardware or a real MQTT broker.

## 2. Technology Stack

- Python 3.10+
- Pydantic v2
- FastAPI
- Uvicorn
- Streamlit
- Pandas
- Pytest

## 3. Module Design

### models.py

Defines the `BatteryData` Pydantic model.

Main fields:
- battery_id
- voltage
- current
- temperature
- soc
- soh
- timestamp

Purpose:
To validate and structure battery telemetry data.

### generator.py

Generates simulated battery telemetry values.

Responsibilities:
- Generate battery measurements.
- Generate timestamps.
- Create battery telemetry records.

### scenarios.py

Implements the seven supported scenarios.

Responsibilities:
- Generate scenario-specific events.
- Add event metadata.
- Add anomaly information.
- Generate simulated attack conditions.

Supported scenarios:
1. normal
2. delayed
3. duplicate
4. out_of_range
5. missing_timestamp
6. spoofed_id
7. replay_attack

### service.py

Provides the main service function for event generation.

Responsibilities:
- Validate battery ID.
- Validate event count.
- Validate delay.
- Call the scenario generation layer.
- Return generated events.

### api.py

Provides the FastAPI interface.

Endpoints:
- `/`
- `/health`
- `/scenarios`
- `/generate-events`
- `/sample`

### app.py

Provides the Streamlit dashboard.

Features:
- Battery ID input
- Scenario selection
- Event count selection
- Delay configuration
- Telemetry event table
- Anomaly count
- CSV download

### main.py

Provides command-line telemetry generation.

It can generate telemetry records using command-line arguments and save sample data.

### test/

Contains automated tests for the project.

## 4. Event Design

A telemetry event contains battery measurement and metadata information.

Example:

```json
{
  "battery_id": "BAT001",
  "voltage": 48.5,
  "current": 120.2,
  "temperature": 32.5,
  "soc": 78.5,
  "soh": 96.2,
  "timestamp": "2026-01-01T10:00:00",
  "event_id": "EVT-001",
  "sequence_number": 1,
  "topic": "battery/telemetry/BAT001",
  "qos": 1,
  "simulated": true,
  "anomaly": null
}