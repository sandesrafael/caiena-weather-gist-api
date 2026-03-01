from openweather_sdk import OpenWeatherSDK
from ..domain.entities import WeatherComment
from ..domain.comment_builder import build_comment
from ..infrastructure.github_gist_adapter import GistPublisher

class WeatherCommentUseCase:
    def __init__(self, sdk: OpenWeatherSDK, gist_publisher: GistPublisher):
        self.sdk = sdk
        self.gist_publisher = gist_publisher

    def execute(self, city: str, country: str = "BR") -> str:
        current = self.sdk.get_current(city, country)
        forecast = self.sdk.get_five_day_daily_forecast(city, country)

        weather = WeatherComment(current=current, forecast=forecast)
        comment_text = build_comment(weather)

        comment_url = self.gist_publisher.publish(comment_text)
        return comment_url