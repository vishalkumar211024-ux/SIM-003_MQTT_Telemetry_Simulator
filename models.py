from pydantic import BaseModel
from datetime import datetime


class BatteryData(BaseModel):
    battery_id: str
    voltage: float
    current: float
    temperature: float
    soc: int
    soh: int
    timestamp: datetime
