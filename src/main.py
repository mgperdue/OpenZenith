import asyncio
import os

from core.config import DEFAULT_SEARCH_RADIUS_KM, LATITUDE, LONGITUDE, USE_MOCK_PROVIDER
from core.flight_data import ADSBExchangeProvider
from core.mock_provider import MockAircraftProvider
from core.tracker import AircraftTracker


async def refresh_loop(tracker: AircraftTracker, provider, refresh_interval=5):
    while True:
        new_data = await provider.fetch_aircraft(
            LATITUDE, LONGITUDE, DEFAULT_SEARCH_RADIUS_KM
        )
        tracker.update_aircraft(new_data)
        tracker.prune_stale_aircraft()
        print_dashboard(tracker)
        if tracker.aircraft:
            print(
                f"Found {len(tracker.aircraft)} aircraft. \
                    Refreshing in {refresh_interval} seconds..."
            )
            await asyncio.sleep(refresh_interval)
        else:
            print("No aircraft found. Retrying in 30 seconds...")
            await asyncio.sleep(30)


def print_dashboard(tracker: AircraftTracker):
    os.system("cls" if os.name == "nt" else "clear")
    print("🛫 OpenZenith: Live Aircraft Tracker\n")
    print(f"Location: {LATITUDE}, {LONGITUDE}")
    print(f"Search Radius: {DEFAULT_SEARCH_RADIUS_KM} km")

    print(f"Timestamp: {tracker.last_update}")

    if not tracker.aircraft:
        print("No aircraft currently tracked.")
        return

    print(
        f"{'CALLSIGN':<10} {'ALTITUDE':>8} {'HEADING':>8} \
          {'LAT':>10} {'LON':>10} {'DISTANCE (KM)':>10}"
    )
    print("-" * 50)

    for data in tracker.aircraft.values():
        print(
            f"{data['callsign']:<10} {data['altitude']:>8} \
                {data['heading']:>8} {data['latitude']:>10.4f} \
                    {data['longitude']:>10.4f} {data['horizontal_distance']:>10.4f}"
        )


async def main():
    if USE_MOCK_PROVIDER:
        provider = MockAircraftProvider()
    else:
        provider = ADSBExchangeProvider()

    tracker = AircraftTracker()
    await refresh_loop(tracker, provider)


if __name__ == "__main__":
    asyncio.run(main())
