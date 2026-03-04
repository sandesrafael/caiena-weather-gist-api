from openweather_sdk.models import CurrentWeather, DailyForecast

from app.comment_builder import build_comment


def test_build_comment_with_state():
    current = CurrentWeather(
        city="Osasco", state="São Paulo", temp=26.1, description="nuvens dispersas", date="03/03"
    )
    forecast = [
        DailyForecast(date="04/03", avg_temp=23.9),
        DailyForecast(date="05/03", avg_temp=22.8),
    ]

    result = build_comment(current, forecast)

    assert "Clima em Osasco/São Paulo - 03/03" in result
    assert "26.1°C — Nuvens dispersas" in result
    assert "04/03: 23.9°C" in result
    assert "05/03: 22.8°C" in result


def test_build_comment_without_state():
    current = CurrentWeather(
        city="Rio de Janeiro", state=None, temp=30.0, description="céu limpo", date="03/03"
    )
    forecast = [DailyForecast(date="04/03", avg_temp=28.0)]

    result = build_comment(current, forecast)

    assert "Clima em Rio de Janeiro - 03/03" in result
    assert "30.0°C — Céu limpo" in result


def test_build_comment_five_day_forecast():
    current = CurrentWeather(
        city="São Paulo", state="São Paulo", temp=25.0, description="nublado", date="03/03"
    )
    forecast = [
        DailyForecast(date="04/03", avg_temp=23.9),
        DailyForecast(date="05/03", avg_temp=22.8),
        DailyForecast(date="06/03", avg_temp=23.4),
        DailyForecast(date="07/03", avg_temp=21.9),
        DailyForecast(date="08/03", avg_temp=21.5),
    ]

    result = build_comment(current, forecast)

    assert "Média dos próximos 5 dias:" in result
    for day in forecast:
        assert f"{day.date}: {day.avg_temp}°C" in result
