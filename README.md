# Log Insights & Alerting Service

## Overview

The Log Insights & Alerting Service is a comprehensive backend system designed to ingest, parse, store, and analyze server logs. Acting as a lightweight observability platform—similar in concept to the ELK Stack or Datadog—this application transforms raw log files into structured data to facilitate real-time analytics and automated anomaly detection.

This project demonstrates the implementation of an ETL (Extract, Transform, Load) pipeline using Python and FastAPI, handling asynchronous data processing, complex regular expression parsing, and SQL-based aggregations for performance monitoring.

## Key Features

* **Log Ingestion:** Supports high-volume log file uploads via REST API. Ingested files are processed asynchronously to ensure non-blocking API response times.
* **Structured Parsing:** Implements a robust regex-based parser to normalize raw Nginx/Apache log lines into structured database records (Timestamp, Log Level, Status Code, Endpoint, Latency).
* **Analytical Engine:** Provides endpoints for aggregate data analysis, including error rate calculation, traffic volume over time, and identification of high-latency endpoints.
* **Automated Alerting:** Configurable rule-based engine that monitors log patterns in background intervals. Triggers alerts based on defined thresholds (e.g., "500 Internal Server Error count > 50 in 5 minutes").
* **Search & Filtering:** Dynamic query support to filter logs by specific time windows, status codes, log levels, or substring matches.

## Technical Architecture

The system is built on a modular architecture to separate concerns between the API layer, the processing logic, and the data persistence layer.

* **Framework:** FastAPI (Python 3.10+) for high-performance, asynchronous request handling.
* **Database:** PostgreSQL for persistent storage of structured logs and alert history.
* **ORM:** SQLAlchemy (Async) for database interactions.
* **Migrations:** Alembic for database schema version control.
* **Background Tasks:** FastAPI `BackgroundTasks` for decoupling file parsing and alert evaluation from the main request-response cycle.
* **Data Validation:** Pydantic for strict schema enforcement.

## Database Schema

The core data model revolves around the `logs` table, indexed for time-series querying efficiency:

* **id:** Primary Key
* **timestamp:** DateTime (Indexed for range queries)
* **log_level:** Enum (INFO, WARN, ERROR)
* **status_code:** Integer (Indexed)
* **endpoint:** String
* **message:** Text
* **raw_log:** Text (Original log line for audit)

## Installation & Setup

### Prerequisites

* Python 3.10 or higher
* PostgreSQL
* Virtualenv (recommended)

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/log-insights-service.git
   cd log-insights-service
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Linux/Mac
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration:** Create a `.env` file in the root directory:
   ```ini
   DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/log_db
   SECRET_KEY=your_secret_key
   ```

5. **Run Database Migrations:**
   ```bash
   alembic upgrade head
   ```

6. **Start the Server:**
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation

Once the server is running, the interactive Swagger documentation is available at `http://127.0.0.1:8000/docs`.

### Primary Endpoints

#### Ingestion

* **POST /logs/upload:** Upload a `.log` file. The server accepts the file and processes parsing in the background.

#### Queries & Analytics

* **GET /logs:** Retrieve paginated logs with filters (start_date, end_date, level, status_code).
* **GET /analytics/summary:** Returns high-level metrics (Total requests, Error percentage, Top 5 active endpoints).
* **GET /analytics/traffic:** Returns time-series data for charting traffic volume.

#### Alerts

* **POST /alerts/rules:** Define a new alerting rule (e.g., Threshold, Window, Severity).
* **GET /alerts/history:** View a history of triggered alerts.

## Testing

The project includes a suite of unit and integration tests using pytest.

To run the tests:
```bash
pytest
```

## Future Roadmap

* **Queue Management:** Migration from BackgroundTasks to Celery + Redis for distributed task processing and retries.
* **Visualization:** Integration with a frontend dashboard (React/Vue) for visualizing analytics.
* **Stream Processing:** Implementation of WebSocket endpoints for real-time log streaming.

## License

This project is licensed under the MIT License.
