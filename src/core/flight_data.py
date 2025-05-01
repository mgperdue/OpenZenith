from math import atan2, cos, radians, sin, sqrt
from typing import List

import aiohttp

from core.config import ADSBEXCHANGE_KEY, OPENSKY_PASSWORD, OPENSKY_USERNAME


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


class ADSBExchangeProvider(AircraftDataProvider):
    async def fetch_aircraft(
        self, lat: float, lon: float, radius_km: float
    ) -> List[dict]:

        radius_nm = radius_km * 0.539957  # Convert km to nautical miles

        # Public ADSB Exchange endpoint (VirtualRadar style)
        base_url = "https://adsbexchange-com1.p.rapidapi.com/v2/"
        url_string = base_url + f"lat/{lat}/lon/{lon}/dist/{radius_nm}/"
        headers_dict = {
            "x-rapidapi-key": ADSBEXCHANGE_KEY,
            "x-rapidapi-host": "adsbexchange-com1.p.rapidapi.com",
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url_string, headers=headers_dict) as resp:
                data = await resp.json()

        aircraft = []
        if "ac" in data:
            for ac in data["ac"]:
                icao24 = ac["hex"]
                callsign = (ac["flight"] or "").strip() if "flight" in ac else "None"
                latitude = ac["lat"]
                longitude = ac["lon"]
                altitude = ac["alt_baro"]
                heading = ac["track"] if "track" in ac else "None"

                # Haversine formula to calculate the distance
                def haversine(lat1, lon1, lat2, lon2):
                    R = 6371.0  # Earth radius in kilometers
                    dlat = radians(lat2 - lat1)
                    dlon = radians(lon2 - lon1)
                    a = (
                        sin(dlat / 2) ** 2
                        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
                    )
                    c = 2 * atan2(sqrt(a), sqrt(1 - a))
                    return R * c

                horizontal_distance = haversine(lat, lon, latitude, longitude)

                if (
                    latitude is not None
                    and longitude is not None
                    and altitude != "ground"
                ):
                    aircraft.append(
                        {
                            "icao24": icao24,
                            "callsign": callsign,
                            "latitude": latitude,
                            "longitude": longitude,
                            "altitude": altitude,
                            "heading": heading,
                            "horizontal_distance": horizontal_distance,
                        }
                    )

        return aircraft


class AviationStackProvider(AircraftDataProvider):
    async def fetch_aircraft(
        self, lat: float, lon: float, radius_km: float
    ) -> List[dict]:
        # Placeholder (for now, focus on OpenSky first)
        return []
