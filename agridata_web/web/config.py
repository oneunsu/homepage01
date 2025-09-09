from pathlib import Path
from pydantic_settings import BaseSettings

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"

class Settings(BaseSettings):
    PUBLIC_DATA_API_KEY: str
    BASE_PUBLIC_DATA_URL: str = "https://apis.data.go.kr"
    AGRI_WEATHER_VERSION: str = "V3"

    model_config = {"env_file": str(ENV_PATH), "extra": "ignore"}

settings = Settings()