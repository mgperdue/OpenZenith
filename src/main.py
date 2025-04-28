import asyncio
import os

from core.config import DEFAULT_SEARCH_RADIUS_KM, LATITUDE, LONGITUDE, USE_MOCK_PROVIDER
from core.flight_data import OpenSkyProvider
from core.mock_provider import MockAircraftProvider
from core.tracker import AircraftTracker


async def refresh_loop(tracker: AircraftTracker, provider):
    while True:
        new_data = await provider.fetch_aircraft(
            LATITUDE, LONGITUDE, DEFAULT_SEARCH_RADIUS_KM
        )
        tracker.update_aircraft(new_data)
        tracker.prune_stale_aircraft()
        print_dashboard(tracker)
        await asyncio.sleep(5)


def print_dashboard(tracker: AircraftTracker):
    os.system("cls" if os.name == "nt" else "clear")
    print("🛫 OpenZenith: Live Aircraft Tracker\n")
    if not tracker.aircraft:
        print("No aircraft currently tracked.")
        return

    print(
        f"{'CALLSIGN':<10} {'ALTITUDE':>8} {'HEADING':>8} \
          {'LAT':>10} {'LON':>10}"
    )
    print("-" * 50)

    for data in tracker.aircraft.values():
        print(
            f"{data['callsign']:<10} {data['altitude']:>8} \
                {data['heading']:>8} {data['latitude']:>10.4f} \
                    {data['longitude']:>10.4f}"
        )


async def main():
    provider = MockAircraftProvider() if USE_MOCK_PROVIDER else OpenSkyProvider()
    tracker = AircraftTracker()
    await refresh_loop(tracker, provider)


if __name__ == "__main__":
    asyncio.run(main())
