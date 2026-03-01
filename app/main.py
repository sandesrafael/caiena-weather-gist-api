from fastapi import FastAPI
from .api.routers import router

app = FastAPI(
    title="Weather Gist API - Desafio Caiena",
    description="Endpoint que publica temperatura no Gist"
)

app.include_router(router)