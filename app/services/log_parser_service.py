import datetime
from app.schemas.schemas import LogCreate
from app.utils.regex_function import NGINX_COMBINED_REGEX

def _infer_log_level(status_code: int) -> str:
    if 500 <= status_code <= 599:
        return "ERROR"
    elif 400 <= status_code <=499:
        return "WARN"
    else:
        return "INFO"
    
async def parse_log_line(raw_log_line: str) -> dict | None:
    match = NGINX_COMBINED_REGEX(raw_log_line)

    if not match:
        return None
    
    try:
        data = match.groupdict()
        status_code = int(data['status_code'])

        log_level = _infer_log_level(status_code)

        timestamp_str = data['timestamp']

        dt_object = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S %z")
        
        structured_log = {
            "timestamp": dt_object,
            "log_level": log_level,
            "status_code": status_code,
            "endpoint": data['endpoint'],
            "message": f"{data['method']} {data['endpoint']}",
            "raw_log": raw_log_line,
        }
        
        return LogCreate(**structured_log)

    except (ValueError, TypeError, KeyError) as e:
        print(f"Error parsing log line: {raw_log_line[:80]}... Error: {e}")
        return None
