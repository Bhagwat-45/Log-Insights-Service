from fastapi import FastAPI,status,HTTPException
from app.db.check_connection import check_db_connection


app = FastAPI(
    title= "Log Insights API",
    description="A backend platform built with FastAPI that ingests, parses, stores, analyzes, and monitors log data — enabling insights, anomaly detection, and automated alerts."
)

@app.get("/")
def root():
    return {
        "Message" : "Hello"
    }

@app.get("/health",status_code=status.HTTP_200_OK)
def health_check():
    if check_db_connection():
        return {
            "Status" : "Ok"
        }
    else:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)