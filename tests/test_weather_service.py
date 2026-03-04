from unittest.mock import patch, MagicMock

from openweather_sdk.models import CurrentWeather, DailyForecast

from app.weather_service import get_weather_comment


@patch("app.weather_service.publish_to_gist")
@patch("app.weather_service.OpenWeatherSDK")
def test_get_weather_comment_calls_current_and_forecast(mock_sdk_class, mock_publish):
    mock_sdk = MagicMock()
    mock_sdk_class.return_value = mock_sdk
    mock_sdk.get_current.return_value = CurrentWeather(
        city="Osasco", state="São Paulo", temp=26.1, description="nuvens dispersas", date="03/03"
    )
    mock_sdk.get_five_day_daily_forecast.return_value = [
        DailyForecast(date="04/03", avg_temp=23.9),
    ]
    mock_publish.return_value = "https://gist.github.com/test"

    result = get_weather_comment("Osasco", "BR", "SP")

    assert result == "https://gist.github.com/test"
    mock_sdk.get_current.assert_called_once_with("Osasco", "BR", "SP")
    mock_sdk.get_five_day_daily_forecast.assert_called_once_with("Osasco", "BR", "SP")
    mock_publish.assert_called_once()


@patch("app.weather_service.publish_to_gist")
@patch("app.weather_service.OpenWeatherSDK")
def test_get_weather_comment_without_state(mock_sdk_class, mock_publish):
    mock_sdk = MagicMock()
    mock_sdk_class.return_value = mock_sdk
    mock_sdk.get_current.return_value = CurrentWeather(
        city="Rio de Janeiro", state="Rio de Janeiro", temp=30.0, description="céu limpo", date="03/03"
    )
    mock_sdk.get_five_day_daily_forecast.return_value = [
        DailyForecast(date="04/03", avg_temp=28.0),
    ]
    mock_publish.return_value = "https://gist.github.com/test"

    get_weather_comment("Rio de Janeiro", "BR")

    mock_sdk.get_current.assert_called_once_with("Rio de Janeiro", "BR", None)
    mock_sdk.get_five_day_daily_forecast.assert_called_once_with("Rio de Janeiro", "BR", None)


@patch("app.weather_service.publish_to_gist")
@patch("app.weather_service.OpenWeatherSDK")
def test_comment_text_is_passed_to_gist(mock_sdk_class, mock_publish):
    mock_sdk = MagicMock()
    mock_sdk_class.return_value = mock_sdk
    mock_sdk.get_current.return_value = CurrentWeather(
        city="Osasco", state="São Paulo", temp=26.1, description="nuvens dispersas", date="03/03"
    )
    mock_sdk.get_five_day_daily_forecast.return_value = [
        DailyForecast(date="04/03", avg_temp=23.9),
    ]
    mock_publish.return_value = "https://gist.github.com/test"

    get_weather_comment("Osasco", "BR", "SP")

    published_text = mock_publish.call_args[0][0]
    assert "Clima em Osasco/São Paulo - 03/03" in published_text
    assert "26.1°C" in published_text
    assert "04/03: 23.9°C" in published_text
