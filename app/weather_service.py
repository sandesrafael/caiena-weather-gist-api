from openweather_sdk import OpenWeatherSDK

from .config import settings
from .comment_builder import build_comment
from .gist_publisher import publish_to_gist


def get_weather_comment(city: str, country: str = "BR", state: str | None = None) -> str:
    sdk = OpenWeatherSDK(settings.openweather_api_key)

    current = sdk.get_current(city, country, state)
    forecast = sdk.get_five_day_daily_forecast(city, country, state)

    comment = build_comment(current, forecast)
    return publish_to_gist(comment)
