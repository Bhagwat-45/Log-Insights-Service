import datetime
from pydantic import BaseModel,Field
from app.models.models import LogLevel

class LogCreate(BaseModel):
    status_code : int = Field(gt=99,lt=600)
    timestamp : datetime.datetime
    log_level : LogLevel
    endpoints : str
    message : str
    raw_log: str
    class Config:
        from_attributes = True


