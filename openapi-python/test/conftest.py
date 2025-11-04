"""
Shared pytest configuration and fixtures for all test files.
Used by both OpenAPI Generator tests and Schemathesis generated tests.
"""

import pytest
from base64 import b64encode
import os
from pathlib import Path

# Try to import from config, fallback to defaults
try:
    import sys
    project_root = Path(__file__).parent.parent.parent.parent
    sys.path.insert(0, str(project_root))
    from config import API_BASE_URL, API_USERNAME, API_PASSWORD
    BASE_URL = API_BASE_URL
    DEFAULT_USERNAME = API_USERNAME
    DEFAULT_PASSWORD = API_PASSWORD
except ImportError:
    # Fallback defaults
    BASE_URL = os.getenv("API_BASE_URL", "https://restful-booker.herokuapp.com")
    DEFAULT_USERNAME = os.getenv("API_USERNAME", "admin")
    DEFAULT_PASSWORD = os.getenv("API_PASSWORD", "password123")


def get_auth_basic_header(username: str = None, password: str = None) -> str:
    """Generate Basic Authentication header value."""
    username = username or DEFAULT_USERNAME
    password = password or DEFAULT_PASSWORD
    creds = f"{username}:{password}".encode()
    return "Basic " + b64encode(creds).decode("ascii")


@pytest.fixture(scope="session")
def base_url():
    """Base URL for API under test."""
    return BASE_URL


@pytest.fixture(scope="session")
def auth_username():
    """Default authentication username."""
    return DEFAULT_USERNAME


@pytest.fixture(scope="session")
def auth_password():
    """Default authentication password."""
    return DEFAULT_PASSWORD


@pytest.fixture(scope="session")
def auth_basic_header():
    """Basic Authentication header value (fixture)."""
    return get_auth_basic_header()

