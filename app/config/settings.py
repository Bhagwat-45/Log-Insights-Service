from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()

@dataclass
class Settings:
    app_name:str  = os.getenv("APP_NAME")
    app_version:str  = os.getenv("APP_VERSION")
    app_env:str = os.getenv("ENVIRONMENT","development")

    host:str = os.getenv("HOST")
    port:int = int(os.getenv("PORT"))

    database_url:str = os.getenv("DATABASE_URL")
    log_level:str = os.getenv("LOG_LEVEL","INFO")
    log_format:str = os.getenv("LOG_FORMAT","json")

    alert_level:str = os.getenv("ALERT_MIN_LEVEL","ERROR")
    alert_weburl:str = os.getenv("ALERT_WEB_URL",None)

    cors_origin: list[str]= os.getenv("CORS_ORIGINS")
    cors_methods: list[str] = os.getenv("CORS_METHODS")

    def __post_init__(self):
        if not self.database_url:
            raise ValueError("Error : Database URL Not found!!")
        if self.app_env not in ["development","production","test"]:
            raise ValueError("Error app_env set!")
        if self.port not in (1,65535):
            raise ValueError("Error The Port number is not set")
        
        

settings = Settings()

