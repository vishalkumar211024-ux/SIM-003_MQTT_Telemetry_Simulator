import sys
import os

# Add the project root folder to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from generator import generate_battery_data


def test_battery_id():
    battery = generate_battery_data("BAT001")
    assert battery.battery_id == "BAT001"


def test_voltage_range():
    battery = generate_battery_data("BAT001")
    assert 48.0 <= battery.voltage <= 50.0


def test_current_range():
    battery = generate_battery_data("BAT001")
    assert 10.0 <= battery.current <= 20.0


def test_temperature_range():
    battery = generate_battery_data("BAT001")
    assert 25.0 <= battery.temperature <= 40.0


def test_soc_range():
    battery = generate_battery_data("BAT001")
    assert 20 <= battery.soc <= 100


def test_soh_range():
    battery = generate_battery_data("BAT001")
    assert 90 <= battery.soh <= 100


def test_timestamp_exists():
    battery = generate_battery_data("BAT001")
    assert battery.timestamp is not None