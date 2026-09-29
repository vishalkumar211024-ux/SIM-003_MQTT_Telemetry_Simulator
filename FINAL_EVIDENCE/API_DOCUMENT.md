# SIM-003 MQTT Telemetry Simulator
## API Documentation

## 1. API Overview

The SIM-003 MQTT Telemetry Simulator provides a FastAPI-based REST interface for generating and checking simulated battery telemetry.

Base URL:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs

## 2. GET /

Checks whether the simulator API is running.

### Response

```json
{
  "message": "MQTT Telemetry Simulator API is running"
}
## 3. GET /health

Checks the health of the API.

### Response

```json
{
  "status": "healthy"
}
## 4. GET /scenarios

Returns the supported telemetry scenarios.

### Response

```json
{
  "scenarios": [
    "normal",
    "delayed",
    "duplicate",
    "out_of_range",
    "missing_timestamp",
    "spoofed_id",
    "replay_attack"
  ]
}
## 5. POST /generate-events

Generates simulated telemetry events.

### Request Body

```json
{
  "battery_id": "BAT001",
  "scenario": "normal",
  "count": 2,
  "delay_seconds": 10
}
### Parameters

| Parameter | Type | Description |
|---|---|---|
| battery_id | string | Battery identifier |
| scenario | string | Telemetry scenario |
| count | integer | Number of events |
| delay_seconds | integer | Delay for delayed scenario |

### Response

```json
{
  "battery_id": "BAT001",
  "scenario": "normal",
  "count": 2,
  "events": []
}
## 6. GET /sample

Generates one sample normal telemetry event.

### Response

```json
{
  "sample": {
    "battery_id": "BAT001",
    "event_id": "EVT-001",
    "sequence_number": 1,
    "topic": "battery/telemetry/BAT001",
    "qos": 1,
    "simulated": true
  }
}
## 7. Supported Scenarios

The simulator supports seven scenarios:

1. normal
2. delayed
3. duplicate
4. out_of_range
5. missing_timestamp
6. spoofed_id
7. replay_attack

## 8. Replay Attack

The replay attack scenario uses an older telemetry timestamp and a current `sent_at` value.

The generated event is marked:

```text
REPLAY_DETECTED
## 9. MQTT-Style Metadata

Generated events contain:

```text
topic: battery/telemetry/{battery_id}
qos: 1
simulated: true
The simulator does not require a real MQTT broker.

## 10. Error Handling

The API validates:

- Battery ID
- Event count
- Delay
- Scenario

Invalid inputs are rejected instead of generating invalid requests.

## 11. Running the API

Run from the project folder:

```powershell
python -m uvicorn api:app --reload
