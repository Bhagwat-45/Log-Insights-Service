import datetime
from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.database import Base, engine, get_db
from app.config.settings import settings

from app.models import models

Base.metadata.create_all(bind=engine)

from app.routers import alerts_router, analytics_router, log_router


app = FastAPI(
    title="Log Insights API",
    description="A backend platform built with FastAPI that ingests, parses, stores, analyzes, and monitors log data — enabling insights, anomaly detection, and automated alerts."
)


app.include_router(alerts_router.router)
app.include_router(analytics_router.router)
app.include_router(log_router.router)


@app.get("/", tags=["Root"])
def root():
    return {"Message": "Hello"}


@app.get("/health", status_code=status.HTTP_200_OK, tags=["Health"])
def health_check():
    if get_db():
        return {"Status": "Ok"}
    else:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)


@app.post("/test-insert")
def test_insert(db: Session = Depends(get_db)):
    log = models.LogDB(
        timestamp=datetime.datetime.now(datetime.timezone.utc),
        log_level="INFO",
        message="Test Log"
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return {"inserted_id": log.id}


@app.get("/test-get")
def test_get(db: Session = Depends(get_db)):
    return db.query(models.LogDB).all()


@app.get("/dat")
def test_db():
    return {"Using DB": settings.database_url}
