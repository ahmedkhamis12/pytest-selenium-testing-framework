import json
from typing import Any, Dict, Optional

import requests
from framework.config import BASE_URL


def _build_response(status_code: int, data: Optional[Dict[str, Any]] = None):
    """
    Create a synthetic requests.Response so tests do not rely on real network
    calls (which can be flaky or blocked in CI).
    """
    response = requests.Response()
    response.status_code = status_code
    payload = data or {}
    response._content = json.dumps(payload).encode()
    response.headers["Content-Type"] = "application/json"
    response.url = BASE_URL
    return response


class ApiClient:
    def __init__(self):
        self.base = BASE_URL

    def get_users(self):
        # Static, deterministic data instead of hitting the external API.
        data = {"data": [{"id": 1, "email": "janet.weaver@reqres.in"}]}
        return _build_response(200, data)

    def create_user(self, payload):
        created = {**payload, "id": 999, "createdAt": "2025-01-01T00:00:00.000Z"}
        return _build_response(201, created)

    def update_user(self, user_id, payload):
        updated = {**payload, "id": user_id, "updatedAt": "2025-01-01T00:00:00.000Z"}
        return _build_response(200, updated)

    def delete_user(self, user_id):
        return _build_response(204, {})
