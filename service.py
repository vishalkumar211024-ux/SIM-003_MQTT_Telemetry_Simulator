from scenarios import generate_scenario_events


def generate_events(
    battery_id: str,
    scenario: str = "normal",
    count: int = 10,
    delay_seconds: int = 10
):
    """
    Generate telemetry events for a battery
    using the selected scenario.
    """

    if not battery_id:
        raise ValueError("Battery ID is required")

    if count <= 0:
        raise ValueError("Count must be greater than 0")

    if delay_seconds < 0:
        raise ValueError("Delay cannot be negative")

    events = generate_scenario_events(
        battery_id=battery_id,
        scenario=scenario,
        count=count,
        delay_seconds=delay_seconds
    )

    return events