from core.tracker import AircraftTracker


def test_tracker_update_and_prune():
    tracker = AircraftTracker()

    tracker.update_aircraft(
        [
            {
                "icao24": "abc123",
                "callsign": "DAL123",
                "latitude": 33.0,
                "longitude": -97.0,
                "altitude": 35000,
                "heading": 90,
            }
        ]
    )

    assert "abc123" in tracker.aircraft
    assert tracker.aircraft["abc123"]["callsign"] == "DAL123"

    tracker.prune_stale_aircraft(timeout_seconds=0)
    assert "abc123" not in tracker.aircraft
