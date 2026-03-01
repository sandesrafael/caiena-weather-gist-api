from .entities import WeatherComment

def build_comment(weather: WeatherComment) -> str:
    current = weather.current
    forecast_str = ", ".join(
        f"{day.avg_temp}°C em {day.date}" for day in weather.forecast[:-1]
    )
    if weather.forecast:
        forecast_str += f" e {weather.forecast[-1].avg_temp}°C em {weather.forecast[-1].date}"

    return (
        f"{current.temp}°C e {current.description} em {current.city} em {current.date}. "
        f"Média para os próximos dias: {forecast_str}."
    )