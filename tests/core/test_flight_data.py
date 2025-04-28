import pytest

from core.flight_data import OpenSkyProvider


@pytest.mark.asyncio
async def test_opensky_provider_fake(monkeypatch):
    provider = OpenSkyProvider()

    async def fake_fetch_aircraft(self, lat, lon, radius_km):
        return [{"icao24": "fake1", "latitude": 33.1, "longitude": -97.1}]

    monkeypatch.setattr(OpenSkyProvider, "fetch_aircraft", fake_fetch_aircraft)

    aircraft = await provider.fetch_aircraft(33.0, -97.0, 250)
    assert len(aircraft) == 1
    assert aircraft[0]["icao24"] == "fake1"
