from core import config


def test_config_defaults():
    assert config.DEFAULT_SEARCH_RADIUS_KM == 250
    assert isinstance(config.LATITUDE, float)
    assert isinstance(config.LONGITUDE, float)
