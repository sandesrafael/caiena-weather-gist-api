from fastapi import FastAPI

from .routes import router

app = FastAPI(
    title="Weather Gist API - Desafio Caiena",
    description="Publica temperatura atual e previsao de 5 dias em um Gist",
)

app.include_router(router)