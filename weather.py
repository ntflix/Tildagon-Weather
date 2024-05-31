from typing import Any
from .weather_object import WeatherInfo
import requests


def FetchWeather():
    print("Fetching weather data")

    # https://openweathermap.org/current
    api_key = open("api_key.txt", "r").read().strip()
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    units = "metric"
    emf_lat_long = (52.039554, -2.378344)

    final_url = (
        base_url
        + "lat="
        + str(emf_lat_long[0])
        + "&lon="
        + str(emf_lat_long[1])
        + "&appid="
        + api_key
        + "&units="
        + units
    )

    current_data: dict[Any, Any] = {}

    response = requests.get(final_url)
    current_data = response.json()

    print(response)
    print(response.json())

    if current_data:
        weather = WeatherInfo.from_json(current_data)
        return weather
    else:
        print("Error fetching weather data")
        raise Exception("Error fetching weather data")
