from datetime import datetime, timedelta

from generator import generate_battery_data


SCENARIOS = [
    "normal",
    "delayed",
    "duplicate",
    "out_of_range",
    "missing_timestamp",
    "spoofed_id",
    "replay_attack",
]


def generate_scenario_events(battery_id, scenario, count=1, delay_seconds=10):
    events = []

    for i in range(count):
        battery_data = generate_battery_data(battery_id)
        event = battery_data.model_dump()

        event["event_id"] = f"EVT-{i + 1:03d}"
        event["sequence_number"] = i + 1
        event["topic"] = f"battery/telemetry/{battery_id}"
        event["qos"] = 1
        event["simulated"] = True
        event["anomaly"] = None

        if scenario == "normal":
            pass

        elif scenario == "delayed":
            original_time = datetime.fromisoformat(event["timestamp"])
            delayed_time = original_time + timedelta(seconds=delay_seconds)
            event["sent_at"] = delayed_time.isoformat()
            event["anomaly"] = "DELAYED"

        elif scenario == "duplicate":
            event["sequence_number"] = 1
            event["anomaly"] = "DUPLICATE"

        elif scenario == "out_of_range":
            event["voltage"] = 65.0
            event["temperature"] = 75.0
            event["current"] = 600.0
            event["anomaly"] = "OUT_OF_RANGE"

        elif scenario == "missing_timestamp":
            event.pop("timestamp", None)
            event["anomaly"] = "MISSING_TIMESTAMP"

        elif scenario == "spoofed_id":
            event["battery_id"] = f"SIM-SPOOF-{i + 1:03d}"
            event["topic"] = f"battery/telemetry/{event['battery_id']}"
            event["anomaly"] = "SPOOFED_ID"

        elif scenario == "replay_attack":
            original_time = datetime.fromisoformat(event["timestamp"])
            old_time = original_time - timedelta(seconds=300)

            event["timestamp"] = old_time.isoformat()
            event["sent_at"] = datetime.now().isoformat()
            event["anomaly"] = "REPLAY_DETECTED"

        else:
            raise ValueError(
                f"Unknown scenario: {scenario}"
            )

        events.append(event)

    return events