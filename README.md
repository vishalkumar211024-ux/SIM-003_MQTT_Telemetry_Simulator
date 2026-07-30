# MQTT Telemetry Simulator

A Python-based MQTT Telemetry Simulator developed as part of an internship project. This simulator generates realistic battery telemetry data, validates it using Pydantic, and stores it in JSON format for IoT applications.

## Features

- Battery telemetry data generation
- Sequential Battery IDs
- Data validation using Pydantic
- JSON data export
- Command-line support using argparse
- Unit testing using pytest

## Technologies Used

- Python
- Pydantic
- JSON
- argparse
- pytest
- Git
- GitHub

## Project Progress

### Week 1
- Python environment setup
- Project folder structure
- Basic simulator setup
- Initial project execution

### Week 2
- Implemented BatteryData model using Pydantic
- Generated battery telemetry data
- Added sequential Battery IDs
- Saved telemetry data in JSON format
- Added command-line support using argparse
- Implemented unit testing using pytest

### Week 3
- Executed complete QA test suite
- Added comprehensive unit tests (7 test cases)
- Performed positive testing with valid inputs
- Performed negative testing for invalid battery count
- Verified JSON data export functionality
- Reviewed code quality and identified improvements
- Fixed minor issues during testing

## Test Results

- Total Test Cases: 7
- Passed: 7
- Failed: 0
- Test Framework: pytest

### Validation Performed

- Battery ID validation
- Voltage range validation
- Current range validation
- Temperature range validation
- State of Charge (SOC) validation
- State of Health (SOH) validation
- Timestamp validation

## Upcoming Work

### Week 4
- FastAPI Integration
- Streamlit Dashboard
- Live Battery Telemetry Visualization

## Project Structure

```
SIM-003_MQTT_Telemetry_Simulator/
│── main.py
│── generator.py
│── models.py
│── requirements.txt
│── README.md
│── sample_data/
│   └── battery_data.json
│── test/
│   └── test_generator.py
```

## Author

**Vishal Kumar**  
B.Tech – Electronics & Communication Engineering