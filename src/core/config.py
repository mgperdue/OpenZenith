import os

# Aircraft Data Source Selection
USE_MOCK_PROVIDER = os.getenv("OPENZENITH_USE_MOCK_PROVIDER", "false").lower() == "true"


# OpenSky API Credentials
OPENSKY_USERNAME = os.getenv("OPENSKY_USERNAME", "")
OPENSKY_PASSWORD = os.getenv("OPENSKY_PASSWORD", "")

# AviationStack API Key
AVIATIONSTACK_KEY = os.getenv("AVIATIONSTACK_KEY", "")

# ADSBExchange API Key
ADSBEXCHANGE_KEY = os.getenv(
    "ADSBEXCHANGE_KEY", "832e849060mshd2d7891c956d663p16f91fjsncedfde6924a9"
)

# Default Search Radius
DEFAULT_SEARCH_RADIUS_KM = float(os.getenv("DEFAULT_SEARCH_RADIUS_KM", 24))

# Default User Location
LATITUDE = float(os.getenv("OPENZENITH_LATITUDE", 33.270836))
LONGITUDE = float(os.getenv("OPENZENITH_LONGITUDE", -97.291939))
