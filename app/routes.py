import logging

from fastapi import APIRouter, HTTPException, Query, status
from github import GithubException
from openweather_sdk.exceptions import CityNotFoundError, OpenWeatherSDKError

from .weather_service import get_weather_comment

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/weather-comment")
def create_weather_comment(
    city: str = Query(
        ...,
        min_length=2,
        max_length=120,
        description="Nome da cidade",
    ),
    country: str = Query(
        "BR",
        min_length=2,
        max_length=2,
        description="Codigo ISO 3166-1 alpha-2",
    ),
    state: str | None = Query(
        None,
        min_length=2,
        max_length=64,
        description="Sigla/nome do estado",
    ),
):
    try:
        gist_url = get_weather_comment(
            city=city.strip(),
            country=country.upper(),
            state=state.strip() if state else None,
        )
        return {
            "message": "Comentario publicado com sucesso no Gist!",
            "gist_url": gist_url,
        }
    except CityNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc
    except (OpenWeatherSDKError, GithubException) as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)
        ) from exc
    except Exception as exc:
        logger.exception("Erro inesperado")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno inesperado.",
        ) from exc
