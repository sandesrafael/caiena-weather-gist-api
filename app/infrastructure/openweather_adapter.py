from openweather_sdk import OpenWeatherSDK
from ..core.config import settings

def get_weather_sdk() -> OpenWeatherSDK:
    return OpenWeatherSDK(settings.openweather_api_key)