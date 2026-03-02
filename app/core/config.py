from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False
    )
    openweather_api_key: str
    github_token: str
    gist_id: str
    api_host: str = "0.0.0.0"
    api_port: int = 8000

settings = Settings()