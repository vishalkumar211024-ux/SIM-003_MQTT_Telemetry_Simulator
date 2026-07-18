import json
import argparse
from generator import generate_battery_data


def main():
    parser = argparse.ArgumentParser(description="MQTT Telemetry Simulator")
    parser.add_argument(
        "--count",
        type=int,
        default=5,
        help="Number of battery records to generate"
    )

    args = parser.parse_args()

    if args.count <= 0:
        print("Battery count must be greater than 0.")
        return

    print("=" * 50)
    print("MQTT Telemetry Simulator")
    print("=" * 50)

    battery_list = []

    for i in range(args.count):
        battery = generate_battery_data(f"BAT{i+1:03d}")
        battery_list.append(battery)

    print("\nGenerated Battery Data:\n")

    for i, battery in enumerate(battery_list, start=1):
        print(f"Battery {i}")
        print(battery)
        print("-" * 50)

    with open("sample_data/battery_data.json", "w") as file:
        json.dump(
            [battery.model_dump(mode="json") for battery in battery_list],
            file,
            indent=4
        )

    print("\nBattery data saved to sample_data/battery_data.json")


if __name__ == "__main__":
    main()