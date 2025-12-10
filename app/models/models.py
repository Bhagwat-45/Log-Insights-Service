from app.db.database import Base
from sqlalchemy import Text,Column,Integer,String,DateTime,ForeignKey, Enum as SqlEnum, null
from enum import Enum


class LogLevel(str,Enum):
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"


class LogDB(Base):
    __tablename__ = "Logs"
    id  = Column(Integer,primary_key=True,index=True)
    timestamp = Column(DateTime,index=True)
    log_level = Column(SqlEnum(LogLevel),nullable=False)
    status_code = Column(Integer,index=True)
    endpoints = Column(String)
    message = Column(Text)
    raw_log = Column(Text)