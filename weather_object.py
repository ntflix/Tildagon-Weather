from typing import Any


class WeatherType:
    id: int
    main: str
    description: str
    icon: str

    @staticmethod
    def from_json(data: dict[str, Any]):
        weather_type = WeatherType()
        weather_type.id = data["id"]
        weather_type.main = data["main"]
        weather_type.description = data["description"]
        weather_type.icon = data["icon"]
        return weather_type


class WeatherInfo:
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int
    weather: WeatherType

    @staticmethod
    def from_json(data: dict[str, Any]):
        print("WeatherInfo from_json")
        print(data)
        main = data["main"]
        weather_info = WeatherInfo()
        weather_info.temp = main["temp"]
        weather_info.feels_like = main["feels_like"]
        weather_info.temp_min = main["temp_min"]
        weather_info.temp_max = main["temp_max"]
        weather_info.pressure = main["pressure"]
        weather_info.humidity = main["humidity"]
        weather_info.sea_level = main["sea_level"]
        weather_info.grnd_level = main["grnd_level"]
        weather_info.weather = WeatherType.from_json(data["weather"][0])
        return weather_info

    def human_readable(self):
        return f"{self.weather.main}, {round(self.temp, 1)}°C"
