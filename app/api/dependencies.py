from ..infrastructure.openweather_adapter import get_weather_sdk
from ..infrastructure.github_gist_adapter import GistPublisher
from ..application.use_cases import WeatherCommentUseCase

def get_use_case() -> WeatherCommentUseCase:
    return WeatherCommentUseCase(
        sdk=get_weather_sdk(),
        gist_publisher=GistPublisher()
    )