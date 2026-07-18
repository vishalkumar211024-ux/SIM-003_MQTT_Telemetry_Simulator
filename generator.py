import random
from datetime import datetime
from models import BatteryData


def generate_battery_data(battery_id):
    return BatteryData(
        battery_id=battery_id,
        voltage=round(random.uniform(48.0, 50.0), 2),
        current=round(random.uniform(10.0, 20.0), 2),
        temperature=round(random.uniform(25.0, 40.0), 2),
        soc=random.randint(20, 100),
        soh=random.randint(90, 100),
        timestamp=datetime.now()
    )