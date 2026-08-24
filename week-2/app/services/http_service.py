from app.core.settings import settings
import httpx
from typing import Any

# Backend API URL
backend_api_url = settings.backend_api_url
backend_api_secret_key = settings.backend_api_secret_key
backend_api_basic_auth = settings.backend_api_basic_auth

async def request(
    base_url: str = backend_api_url,
    endpoint: str = "health",
    method: str = "GET",
    params: dict[str, Any] | None = None,
    data: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
):
    url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"

    request_headers = {
        "X-API-KEY": backend_api_secret_key,
        "Authorization": f"Basic {backend_api_basic_auth}",
        **(headers or {}),
    }

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=method,
            url=url,
            params=params,
            json=data,
            headers=request_headers,
        )

        response.raise_for_status()

        return response.json()