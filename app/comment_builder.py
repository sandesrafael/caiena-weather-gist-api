from openweather_sdk.models import CurrentWeather, DailyForecast


def build_comment(
    current: CurrentWeather,
    forecast: list[DailyForecast],
) -> str:
    city_label = f"{current.city}/{current.state}" if current.state else current.city

    forecast_lines = "\n".join(
        f"{day.date}: {day.avg_temp}°C" for day in forecast
    )

    return (
        f"Clima em {city_label} - {current.date}\n"
        f"\n"
        f"{current.temp}°C — {current.description.capitalize()}\n"
        f"\n"
        f"Média dos próximos 5 dias:\n"
        f"\n"
        f"{forecast_lines}\n"
    )
