# MQTT Telemetry Simulator

A Python-based MQTT Telemetry Simulator developed as part of an internship project. The simulator generates realistic battery telemetry data, validates it using Pydantic, and supports configurable telemetry anomaly and attack scenarios through a FastAPI interface.

## Features

* Battery telemetry data generation

* Sequential Battery IDs

* Data validation using Pydantic

* JSON data export

* Command-line support using argparse

* Unit testing using pytest

* Scenario-based telemetry generation

* Delayed telemetry simulation

* Duplicate packet simulation

* Out-of-range value simulation

* Missing timestamp simulation

* Spoofed battery ID simulation

* Replay attack simulation

* FastAPI REST API for telemetry event generation

* MQTT topic and QoS information

* Anomaly flags for simulated events

* Simulation tagging using `simulated=true`

## Technologies Used

* Python

* Pydantic

* FastAPI

* JSON

* argparse

* pytest

* Git

* GitHub

## Project Progress

### Week 1

* Python environment setup

* Project folder structure

* Basic simulator setup

* Initial project execution

### Week 2

* Implemented BatteryData model using Pydantic

* Generated battery telemetry data

* Added sequential Battery IDs

* Saved telemetry data in JSON format

* Added command-line support using argparse

* Implemented unit testing using pytest

### Week 3

* Executed complete QA test suite

* Added comprehensive unit tests

* Performed positive testing with valid inputs

* Performed negative testing for invalid battery count

* Verified JSON data export functionality

* Reviewed code quality and identified improvements

* Fixed minor issues during testing

### Week 4 – Product POC Development

* Implemented scenario-based telemetry generation

* Created `scenarios.py` for configurable telemetry scenarios

* Integrated the simulator with FastAPI

* Implemented `POST /generate-events` endpoint

* Implemented `GET /health` endpoint

* Added normal telemetry scenario

* Added delayed telemetry scenario

* Added duplicate packet scenario

* Added out-of-range telemetry scenario

* Added missing timestamp scenario

* Added spoofed battery ID scenario

* Added replay attack scenario

* Added anomaly flags for simulated events

* Added MQTT topic and QoS information

* Added configurable event count and delay

* Tagged generated events with `simulated=true`

* Updated the project implementation and pushed changes to GitHub

### Week 5 – Architecture & Design

* Designed the formal system architecture

* Defined the main system components and their responsibilities

* Created the component architecture and data flow

* Defined API request and response contracts

* Created sequence flow for telemetry generation

* Documented security controls and threat mitigations

* Prepared Architecture Decision Records (ADRs)

* Prepared the Week 5 Architecture & Design Document

* Completed the architecture and design phase

### Week 6 – Product Development Phase 1

* Implemented backend APIs using FastAPI

* Added `GET /scenarios` endpoint

* Added `GET /sample` endpoint

* Improved `POST /generate-events` endpoint

* Created `service.py` for core business logic

* Integrated FastAPI with the telemetry simulator

* Added API integration tests

* Tested normal telemetry generation through API

* Tested replay attack scenario through API

* Successfully passed 12 automated tests

* Maintained Week 6 work in a separate feature branch

* Pushed Week 6 changes to GitHub

## Implemented Telemetry Scenarios

| Scenario | Description |
| ------------------- | ---------------------------------------------------------- |
| `normal` | Generates valid battery telemetry |
| `delayed` | Simulates delayed telemetry |
| `duplicate` | Simulates duplicate packets |
| `out_of_range` | Generates abnormal voltage, current and temperature values |
| `missing_timestamp` | Generates an event without a timestamp |
| `spoofed_id` | Simulates a spoofed battery identity |
| `replay_attack` | Simulates retransmission of an older telemetry event |

## Test Results

* Total Test Cases: 7

* Passed: 7

* Failed: 0

* Test Framework: pytest

### Validation Performed

* Battery ID validation

* Voltage range validation

* Current range validation

* Temperature range validation

* State of Charge (SOC) validation

* State of Health (SOH) validation

* Timestamp validation

## API

### POST `/generate-events`

Generates telemetry events based on the selected scenario.

Example request:

```json
{
  "battery_id": "BAT001",
  "scenario": "normal",
  "count": 3,
  "delay_seconds": 10
}