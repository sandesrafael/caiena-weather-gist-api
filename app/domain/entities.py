from dataclasses import dataclass
from openweather_sdk.models import CurrentWeather, DailyForecast

@dataclass
class WeatherComment:
    current: CurrentWeather
    forecast: list[DailyForecast]