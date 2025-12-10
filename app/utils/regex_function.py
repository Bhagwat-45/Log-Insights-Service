import re

NGINX_COMBINED_REGEX = re.compile(
    r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '  # Remote IP
    r'(?P<user>-|\w+) '                                # Remote User (often '-')
    r'\[(?P<timestamp>.*?)\] '                         # Timestamp
    r'"(?P<method>\w+) '                               # HTTP Method
    r'(?P<endpoint>.*?) '                             # The Endpoint/Path
    r'HTTP\/\d\.\d" '                                  # HTTP Version
    r'(?P<status_code>\d{3}) '                         # Status Code (Crucial!)
    r'(?P<body_bytes>\d+) '                            # Body Bytes Sent
    r'"(?P<referer>.*?)" '                             # Referer
    r'"(?P<user_agent>.*?)"'                           # User Agent
)

