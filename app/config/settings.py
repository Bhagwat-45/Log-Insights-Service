from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()


def parse_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(',')]


@dataclass
class Settings:
    app_name: str = os.getenv("APP_NAME")
    app_version: str = os.getenv("APP_VERSION")
    app_env: str = os.getenv("ENVIRONMENT", "development")

    host: str = os.getenv("HOST")
    port: int = int(os.getenv("PORT", 8000))

    database_url: str = os.getenv("DATABASE_URL")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    log_format: str = os.getenv("LOG_FORMAT", "json")

    alert_level: str = os.getenv("ALERT_MIN_LEVEL", "ERROR")
    alert_weburl: str = os.getenv("ALERT_WEBHOOK_URL")  

    cors_origin: list[str] = None
    cors_methods: list[str] = None

    def __post_init__(self):
        self.cors_origin = parse_list(os.getenv("CORS_ORIGINS", "*"))
        self.cors_methods = parse_list(os.getenv("CORS_METHODS", "*"))

        if not self.database_url:
            raise ValueError("Error: Database URL Not found!!")

        if self.app_env not in ("development", "production", "test"):
            raise ValueError("Error: app_env must be development/production/test")

        if not (1 <= self.port <= 65535):
            raise ValueError("Error: Port must be between 1 and 65535")


settings = Settings()
