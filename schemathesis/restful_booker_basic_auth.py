import base64
import os
import schemathesis
from pathlib import Path
import sys

# Try to import from config
try:
    project_root = Path(__file__).parent.parent
    sys.path.insert(0, str(project_root))
    from config import API_USERNAME, API_PASSWORD
    DEFAULT_USERNAME = API_USERNAME
    DEFAULT_PASSWORD = API_PASSWORD
except ImportError:
    DEFAULT_USERNAME = os.getenv("API_USERNAME", "admin")
    DEFAULT_PASSWORD = os.getenv("API_PASSWORD", "password123")


def _generate_auth_header(username: str = None, password: str = None) -> str:
    """Generate Basic Authentication header value."""
    username = username or DEFAULT_USERNAME
    password = password or DEFAULT_PASSWORD
    creds = f"{username}:{password}".encode()
    return "Basic " + base64.b64encode(creds).decode("ascii")


@schemathesis.auth(refresh_interval=300)
class RestfulBookerBasicAuth:
    def __init__(self):
        self.auth_value = None  

    def get(self, case, ctx):
        if not self.auth_value:
            self.auth_value = _generate_auth_header()
        return self.auth_value

    def set(self, case, data, ctx):
        """Attach Authorization and default headers to the request."""
        case.headers = case.headers or {}
        case.headers["Authorization"] = data
        case.headers.setdefault("Accept", "application/json")
        if case.body is not None:
            case.headers.setdefault("Content-Type", "application/json")


# CLI hook fallback (when SCHEMATHESIS_HOOKS points to this module)
def before_call(context, case):
    """Hook to add Basic Authorization before each request (CLI)."""
    case.headers = case.headers or {}
    case.headers["Authorization"] = _generate_auth_header()
    case.headers.setdefault("Accept", "application/json")
    if case.body is not None:
        case.headers.setdefault("Content-Type", "application/json")
