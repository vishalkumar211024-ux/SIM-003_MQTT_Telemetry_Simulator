# Week 9 Demo Evidence

## Project
SIM-003 MQTT Telemetry Simulator

## Demo Objective
To demonstrate the working MQTT telemetry simulator, FastAPI endpoints, anomaly scenarios, and Streamlit dashboard.

## Features Demonstrated

### 1. FastAPI Health Check
The `/health` endpoint was tested successfully and returned:

```json
{
  "status": "healthy"
}
```

### 2. Scenario List
The `/scenarios` endpoint was tested and displayed all 7 supported scenarios:

- normal
- delayed
- duplicate
- out_of_range
- missing_timestamp
- spoofed_id
- replay_attack

### 3. Normal Telemetry
Normal battery telemetry events were generated successfully using the `/generate-events` API.

### 4. Replay Attack
The replay attack scenario was tested successfully.

The generated events showed:
- Older timestamp
- Current `sent_at`
- `anomaly: REPLAY_DETECTED`
- `simulated: true`

### 5. Streamlit Dashboard
The Streamlit dashboard was tested successfully.

The dashboard demonstrated:
- Battery ID selection
- Scenario selection
- Event count
- Telemetry event table
- Anomaly count
- CSV download

### 6. Automated Testing
The project test suite was executed successfully.

- Tests passed: 19
- Tests failed: 0
- Code coverage: 71%

## Demo Recording

A screen recording was created demonstrating the FastAPI and Streamlit functionality.

## Status

Week 9 demo preparation and demonstration completed.
