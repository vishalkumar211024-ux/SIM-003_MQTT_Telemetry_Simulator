# Week 10 Presentation
## SIM-003 MQTT Telemetry Simulator

### Slide 1 – Project Overview
- Simulated EV battery telemetry system
- Generates battery monitoring data
- Supports normal and abnormal scenarios
- FastAPI API + Streamlit dashboard

### Slide 2 – Battery Telemetry
The simulator generates:
- Voltage
- Current
- Temperature
- SOC
- SOH
- Timestamp

### Slide 3 – Supported Scenarios
- Normal
- Delayed
- Duplicate
- Out of Range
- Missing Timestamp
- Spoofed ID
- Replay Attack

### Slide 4 – Cybersecurity Testing
The simulator helps test:
- Replay attacks
- Spoofed battery IDs
- Duplicate data
- Delayed telemetry
- Invalid sensor values

### Slide 5 – FastAPI
FastAPI provides:
- Health check
- Scenario list
- Telemetry event generation
- Sample telemetry endpoint

### Slide 6 – Streamlit Dashboard
The dashboard provides:
- Battery ID selection
- Scenario selection
- Event generation
- Telemetry table
- Anomaly count
- CSV download

### Slide 7 – Testing
- 19 automated tests passed
- 0 tests failed
- 71% code coverage
- API and dashboard tested

### Slide 8 – Future Improvements
- Real MQTT broker integration
- Authentication
- Digital signatures
- Persistent telemetry storage
- Advanced anomaly detection

### Slide 9 – Conclusion
The project provides a controlled environment for testing EV battery telemetry and cybersecurity scenarios without requiring real battery hardware.