# SIM-003 MQTT Telemetry Simulator

# Security Report

## 1. Overview

The SIM-003 MQTT Telemetry Simulator is designed for testing telemetry trust and cybersecurity scenarios using simulated battery data.

The simulator does not communicate with a real MQTT broker, real BMS hardware, or real battery sensors.

## 2. Security Objectives

The main security objectives are:

- Simulate common telemetry anomalies.
- Detect replay attack conditions.
- Identify spoofed battery IDs.
- Detect duplicate telemetry events.
- Identify out-of-range telemetry values.
- Support cybersecurity testing without real hardware.
- Clearly mark generated data as simulated.

## 3. Simulated Security Scenarios

The simulator supports the following scenarios:

1. Normal telemetry
2. Delayed telemetry
3. Duplicate telemetry
4. Out-of-range telemetry
5. Missing timestamp
6. Spoofed battery ID
7. Replay attack

## 4. Replay Attack Detection

The replay attack scenario modifies the telemetry timestamp to an older time while generating a current `sent_at` timestamp.

The generated event is marked with:

```text
REPLAY_DETECTED