from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openweather_api_key: str
    github_token: str
    gist_id: str
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()