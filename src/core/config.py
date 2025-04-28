import os

# Aircraft Data Source Selection
USE_MOCK_PROVIDER = os.getenv("OPENZENITH_USE_MOCK_PROVIDER", "true").lower() == "true"


# OpenSky API Credentials
OPENSKY_USERNAME = os.getenv("OPENSKY_USERNAME", "")
OPENSKY_PASSWORD = os.getenv("OPENSKY_PASSWORD", "")

# AviationStack API Key
AVIATIONSTACK_KEY = os.getenv("AVIATIONSTACK_KEY", "")

# Default Search Radius
DEFAULT_SEARCH_RADIUS_KM = float(os.getenv("DEFAULT_SEARCH_RADIUS_KM", 250))

# Default User Location
LATITUDE = float(os.getenv("OPENZENITH_LATITUDE", 33.2148))
LONGITUDE = float(os.getenv("OPENZENITH_LONGITUDE", -97.1331))
