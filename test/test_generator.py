import sys
import os

# Add the project root folder to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from generator import generate_battery_data


def test_generate_battery_data():
    battery = generate_battery_data("BAT001")

    # Check Battery ID
    assert battery.battery_id == "BAT001"

    # Check data ranges
    assert 48.0 <= battery.voltage <= 50.0
    assert 10.0 <= battery.current <= 20.0
    assert 25.0 <= battery.temperature <= 40.0
    assert 20 <= battery.soc <= 100
    assert 90 <= battery.soh <= 100

    print("✅ All tests passed successfully!")