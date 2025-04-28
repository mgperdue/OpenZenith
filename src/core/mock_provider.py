from datetime import datetime
from typing import List

from core.flight_data import AircraftDataProvider


class MockAircraftProvider(AircraftDataProvider):
    async def fetch_aircraft(
        self, lat: float, lon: float, radius_km: float
    ) -> List[dict]:
        now = datetime.utcnow()
        return [
            {
                "icao24": "mock1",
                "callsign": "MOCK1",
                "latitude": lat + 0.1,
                "longitude": lon + 0.1,
                "altitude": 30000,
                "heading": 90,
                "last_seen": now,
            },
            {
                "icao24": "mock2",
                "callsign": "MOCK2",
                "latitude": lat - 0.1,
                "longitude": lon - 0.1,
                "altitude": 31000,
                "heading": 270,
                "last_seen": now,
            },
            {
                "icao24": "mock3",
                "callsign": "MOCK3",
                "latitude": lat,
                "longitude": lon,
                "altitude": 32000,
                "heading": 180,
                "last_seen": now,
            },
        ]
