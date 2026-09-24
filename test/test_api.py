import sys
from pathlib import Path

from fastapi.testclient import TestClient

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from api import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_scenarios():
    response = client.get("/scenarios")

    assert response.status_code == 200

    data = response.json()

    assert "scenarios" in data
    assert "normal" in data["scenarios"]
    assert "replay_attack" in data["scenarios"]


def test_sample():
    response = client.get("/sample")

    assert response.status_code == 200

    data = response.json()

    assert "sample" in data
    assert data["sample"]["battery_id"] == "BAT001"
    assert data["sample"]["simulated"] is True


def test_generate_events():
    response = client.post(
        "/generate-events",
        json={
            "battery_id": "BAT001",
            "scenario": "normal",
            "count": 2,
            "delay_seconds": 10
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["battery_id"] == "BAT001"
    assert data["scenario"] == "normal"
    assert data["count"] == 2
    assert len(data["events"]) == 2


def test_replay_attack():
    response = client.post(
        "/generate-events",
        json={
            "battery_id": "BAT001",
            "scenario": "replay_attack",
            "count": 2,
            "delay_seconds": 10
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["scenario"] == "replay_attack"
    assert data["count"] == 2

    for event in data["events"]:
        assert event["anomaly"] == "REPLAY_DETECTED"
        assert event["simulated"] is True
        assert "sent_at" in event