from fastapi import FastAPI
from pydantic import BaseModel

from scenarios import generate_scenario_events, SCENARIOS


app = FastAPI(title="MQTT Telemetry Simulator")


class GenerateRequest(BaseModel):
    battery_id: str
    scenario: str = "normal"
    count: int = 1
    delay_seconds: int = 10


@app.get("/")
def home():
    return {
        "message": "MQTT Telemetry Simulator API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/generate-events")
def generate_events(request: GenerateRequest):

    if request.scenario not in SCENARIOS:
        return {
            "error": f"Invalid scenario. Choose from: {SCENARIOS}"
        }

    events = generate_scenario_events(
        battery_id=request.battery_id,
        scenario=request.scenario,
        count=request.count,
        delay_seconds=request.delay_seconds
    )

    return {
        "battery_id": request.battery_id,
        "scenario": request.scenario,
        "count": len(events),
        "events": events
    }