from unittest.mock import patch, MagicMock

from fastapi.testclient import TestClient
from openweather_sdk.models import CurrentWeather, DailyForecast
from openweather_sdk.exceptions import CityNotFoundError

from app.main import app

client = TestClient(app)


@patch("app.weather_service.publish_to_gist")
@patch("app.weather_service.OpenWeatherSDK")
def test_endpoint_success(mock_sdk_class, mock_publish):
    mock_sdk = MagicMock()
    mock_sdk_class.return_value = mock_sdk
    mock_sdk.get_current.return_value = CurrentWeather(
        city="Rio de Janeiro", state="Rio de Janeiro", temp=28.5, description="nublado", date="03/03"
    )
    mock_sdk.get_five_day_daily_forecast.return_value = [
        DailyForecast(date="04/03", avg_temp=27.0),
    ]
    mock_publish.return_value = "https://gist.github.com/test"

    response = client.get("/weather-comment?city=Rio de Janeiro")

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Comentario publicado com sucesso no Gist!"
    assert "gist.github.com" in data["gist_url"]


@patch("app.weather_service.OpenWeatherSDK")
def test_endpoint_city_not_found(mock_sdk_class):
    mock_sdk = MagicMock()
    mock_sdk_class.return_value = mock_sdk
    mock_sdk.get_current.side_effect = CityNotFoundError(
        "Cidade 'CidadeInexistente' nao encontrada para o pais 'BR'"
    )

    response = client.get("/weather-comment?city=CidadeInexistente")

    assert response.status_code == 404
    detail = response.json()["detail"]
    assert "CidadeInexistente" in detail
    assert "BR" in detail


def test_endpoint_validates_min_city_length():
    response = client.get("/weather-comment?city=R")
    assert response.status_code == 422
