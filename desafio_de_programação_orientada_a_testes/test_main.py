from unittest.mock import patch
import pytest
from main import get_temperature

expected = 16
temperature = 62

def test_get_temperature_by_lat_lng():
    lat = -14.235004
    lng = -51.92528

    result = get_temperature(lat, lng)

    if result != expected:
       return "Failed"

