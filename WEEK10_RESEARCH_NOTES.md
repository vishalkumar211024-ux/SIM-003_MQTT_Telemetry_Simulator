# Week 10 Research Notes

## Project
SIM-003 MQTT Telemetry Simulator

## Research Summary

The project focuses on generating simulated battery telemetry data for an EV battery monitoring system.

The simulator generates battery parameters such as:
- Voltage
- Current
- Temperature
- SOC
- SOH
- Timestamp

The system also supports abnormal and cybersecurity-related scenarios such as delayed telemetry, duplicate events, out-of-range values, missing timestamps, spoofed battery IDs, and replay attacks.

FastAPI is used to provide API access to the simulator, while Streamlit provides a simple dashboard for generating and monitoring telemetry events.

## Cybersecurity Research

Battery telemetry systems can be affected by incorrect, delayed, duplicated, spoofed, or replayed data.

The simulator helps test how a battery monitoring system can identify these abnormal telemetry conditions before connecting to real battery hardware.

## Potential Innovation Areas

The following areas were identified for further technical investigation:

1. Automated generation of multiple battery telemetry attack scenarios.
2. Detection flags for abnormal telemetry events.
3. Simulation of replay attacks using old timestamps.
4. Simulation of spoofed battery identifiers.
5. Combined API and dashboard based testing of battery telemetry.

## Conclusion

The research helped identify possible areas for improving EV battery telemetry testing and cybersecurity validation.

Further technical review and prior-art checking would be required before considering any concept for patent protection.
