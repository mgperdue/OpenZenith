import asyncio
from datetime import datetime
from typing import Dict

from core.config import DEFAULT_SEARCH_RADIUS_KM, LATITUDE, LONGITUDE


class AircraftTracker:
    def __init__(self):
        self.aircraft: Dict[str, dict] = {}
        self.last_update: datetime = datetime.utcnow()

    def update_aircraft(self, new_data: list):
        now = datetime.utcnow()
        self.last_update = now
        for plane in new_data:
            self.aircraft[plane["icao24"]] = {
                **plane,
                "last_seen": now,
                "trail": self.aircraft.get(plane["icao24"], {}).get("trail", []),
            }
            self.update_trail(plane["icao24"], plane["latitude"], plane["longitude"])

    def prune_stale_aircraft(self, timeout_seconds=300):
        now = datetime.utcnow()
        to_remove = [
            icao
            for icao, data in self.aircraft.items()
            if (now - data["last_seen"]).total_seconds() > timeout_seconds
        ]
        for icao in to_remove:
            del self.aircraft[icao]

    def update_trail(self, icao24, lat, lon):
        now = datetime.utcnow()
        trail = self.aircraft[icao24].setdefault("trail", [])
        trail.append((now, lat, lon))
        # Keep only last 5 minutes of trail history
        cutoff = now.timestamp() - 300
        self.aircraft[icao24]["trail"] = [
            (t, lat, lon) for t, lat, lon in trail if t.timestamp() > cutoff
        ]


async def refresh_loop(tracker: AircraftTracker, provider):
    while True:
        new_data = await provider.fetch_aircraft(
            LATITUDE, LONGITUDE, DEFAULT_SEARCH_RADIUS_KM
        )
        tracker.update_aircraft(new_data)
        tracker.prune_stale_aircraft()
        await asyncio.sleep(5)
