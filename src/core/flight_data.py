from typing import List

import aiohttp

from core.config import OPENSKY_PASSWORD, OPENSKY_USERNAME


class AircraftDataProvider:
    async def fetch_aircraft(
        self, lat: float, lon: float, radius_km: float
    ) -> List[dict]:
        raise NotImplementedError()


class OpenSkyProvider(AircraftDataProvider):
    async def fetch_aircraft(
        self, lat: float, lon: float, radius_km: float
    ) -> List[dict]:
        url = f"https://opensky-network.org/api/states/all?lamin={lat - 1}\
            &lomin={lon - 1}&lamax={lat + 1}&lomax={lon + 1}"

        auth = (
            aiohttp.BasicAuth(OPENSKY_USERNAME, OPENSKY_PASSWORD)
            if OPENSKY_USERNAME
            else None
        )

        async with aiohttp.ClientSession(auth=auth) as session:
            async with session.get(url) as resp:
                data = await resp.json()

        aircraft = []
        if "states" in data:
            for state in data["states"]:
                icao24 = state[0]
                callsign = (state[1] or "").strip()
                latitude = state[6]
                longitude = state[5]
                altitude = state[7]
                heading = state[10]

                if latitude is not None and longitude is not None:
                    aircraft.append(
                        {
                            "icao24": icao24,
                            "callsign": callsign,
                            "latitude": latitude,
                            "longitude": longitude,
                            "altitude": altitude,
                            "heading": heading,
                        }
                    )

        return aircraft


class AviationStackProvider(AircraftDataProvider):
    async def fetch_aircraft(
        self, lat: float, lon: float, radius_km: float
    ) -> List[dict]:
        # Placeholder (for now, focus on OpenSky first)
        return []
