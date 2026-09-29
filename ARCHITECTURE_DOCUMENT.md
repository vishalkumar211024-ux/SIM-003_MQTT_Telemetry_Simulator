# SIM-003 MQTT Telemetry Simulator
## Architecture Document

## 1. Project Overview

SIM-003 MQTT Telemetry Simulator is a Python-based simulator for generating simulated EV battery telemetry events.

The system generates normal telemetry and abnormal/security scenarios without requiring real BMS hardware or a real MQTT broker.

## 2. Purpose

The purpose of the simulator is to provide realistic and configurable telemetry streams for development, testing, and cybersecurity scenario validation.

## 3. System Components

### Telemetry Generator
Generates battery telemetry values such as:
- Voltage
- Current
- Temperature
- SOC
- SOH
- Timestamp

### Scenario Engine
Generates different telemetry conditions:
- Normal
- Delayed
- Duplicate
- Out of Range
- Missing Timestamp
- Spoofed ID
- Replay Attack

### Service Layer
Provides a common function for generating scenario-based telemetry events and validates input parameters.

### FastAPI
Provides REST API endpoints for programmatic telemetry generation.

### Streamlit
Provides a user interface for selecting scenarios and viewing generated events.

### Pydantic Models
Validates battery telemetry data structures.

### Pytest
Provides automated unit and API testing.

## 4. High-Level Data Flow

User
  |
  v
Streamlit UI / FastAPI
  |
  v
Service Layer
  |
  v
Scenario Engine
  |
  v
Telemetry Generator
  |
  v
Pydantic Validation
  |
  v
Telemetry Event
  |
  +--> JSON/API Response
  |
  +--> Streamlit Event Table
  |
  +--> CSV Export

## 5. Event Structure

Each generated event can contain:

- event_id
- battery_id
- voltage
- current
- temperature
- soc
- soh
- timestamp
- sequence_number
- topic
- qos
- simulated
- anomaly

Additional fields such as `sent_at` are generated for applicable scenarios.

## 6. API Architecture

### GET /health
Checks whether the API is running.

### GET /scenarios
Returns the supported telemetry scenarios.

### POST /generate-events
Generates telemetry events based on battery ID, scenario, count, and delay configuration.

### GET /sample
Returns a sample telemetry event.

## 7. Scenario Processing

### Normal
Generates valid battery telemetry.

### Delayed
Adds a configurable delay to the event timestamp.

### Duplicate
Generates events with duplicate sequence information.

### Out of Range
Generates abnormal voltage, temperature, and current values.

### Missing Timestamp
Removes the timestamp field.

### Spoofed ID
Generates a different simulated battery identifier.

### Replay Attack
Uses an older timestamp and a current `sent_at` value and marks the event as `REPLAY_DETECTED`.

## 8. Security Architecture

The simulator is designed for safe testing.

Security controls include:
- All events are marked `simulated=true`.
- Attack scenarios are simulated locally.
- No production battery hardware is connected.
- No real MQTT broker traffic is required.
- Spoofed IDs use simulated identifiers.
- Replay scenarios are explicitly marked with anomaly information.

## 9. Architecture Decision Records

### ADR-001: Python
Python was selected because it supports rapid development, data processing, API development, testing, and Streamlit integration.

### ADR-002: Pydantic
Pydantic is used for structured telemetry data validation.

### ADR-003: FastAPI
FastAPI provides a simple REST interface for programmatic event generation.

### ADR-004: Streamlit
Streamlit provides a simple dashboard for scenario selection and telemetry visualization.

### ADR-005: Local Simulation
Local simulation was selected so development and testing can be performed without real BMS hardware or a production MQTT environment.

## 10. Testing Architecture

Testing is performed using pytest.

Current test result:
- 19 tests passed
- 0 tests failed
- 71% code coverage

Testing includes:
- API endpoints
- Normal telemetry
- Replay attack
- Out-of-range scenario
- Invalid input
- Service validation

## 11. Limitations

- No real MQTT broker integration.
- No real BMS hardware integration.
- No physical sensor data.
- Simplified network simulation.
- Advanced anomaly detection is not implemented.

## 12. Future Improvements

- Real MQTT broker integration
- Authentication and authorization
- Secure telemetry communication
- Persistent telemetry storage
- Advanced anomaly detection
- Real-time monitoring improvements

## 13. Conclusion

The architecture provides a modular structure for generating, testing, and visualizing simulated EV battery telemetry and cybersecurity scenarios.