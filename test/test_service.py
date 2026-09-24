import pytest
from service import generate_events


def test_normal_events():
    events = generate_events("BAT001", "normal", 3)
    assert len(events) == 3


def test_replay_attack():
    events = generate_events("BAT001", "replay_attack", 2)

    for event in events:
        assert event["anomaly"] == "REPLAY_DETECTED"
        assert event["simulated"] is True


def test_out_of_range():
    events = generate_events("BAT001", "out_of_range", 1)
    event = events[0]

    assert event["anomaly"] == "OUT_OF_RANGE"
    assert event["voltage"] == 65.0
    assert event["current"] == 600.0
    assert event["temperature"] == 75.0


def test_invalid_battery_id():
    with pytest.raises(ValueError):
        generate_events("", "normal", 1)


def test_invalid_count():
    with pytest.raises(ValueError):
        generate_events("BAT001", "normal", 0)


def test_negative_delay():
    with pytest.raises(ValueError):
        generate_events("BAT001", "normal", 1, -1)


def test_invalid_scenario():
    with pytest.raises(ValueError):
        generate_events("BAT001", "wrong_scenario", 1)