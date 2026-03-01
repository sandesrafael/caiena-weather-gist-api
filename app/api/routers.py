from fastapi import APIRouter, Depends, HTTPException
from .schemas import WeatherCommentResponse
from ..application.use_cases import WeatherCommentUseCase
from ..core.exceptions import WeatherAPIException
from .dependencies import get_use_case

router = APIRouter()

@router.get("/weather-comment", response_model=WeatherCommentResponse)
def create_weather_comment(
    city: str,
    country: str = "BR",
    use_case: WeatherCommentUseCase = Depends(get_use_case)
):
    try:
        comment_url = use_case.execute(city, country)
        return WeatherCommentResponse(
            message="Comentário publicado com sucesso no Gist!",
            comment_url=comment_url
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))