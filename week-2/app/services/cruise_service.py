# app/services/cruise_service.py

from app.core.settings import settings
import httpx
from typing import Any

# Backend API URL
backend_api_url = settings.backend_api_url

async def request(
    base_url: str = "http://localhost:8080",
    endpoint: str = "health",
    method: str = "GET",
    params: dict[str, Any] | None = None,
    data: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
):
    url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=method,
            url=url,
            params=params,
            json=data,
            headers=headers,
        )

        response.raise_for_status()

        return response.json()

async def cruise_search(
    cruiseline: str,
    ship: str,
    embarkation_date: str | None,
    nights: int | str | None
):
    response = await request(
        endpoint="cruises",
        method="POST",
        params={
            "cruiseline": cruiseline,
            "nights": nights,
            "embarkation_date": embarkation_date,
            "ship": ship
        },
    )

    return response


async def ship_search(
        cruiseline: str,
        ship: str,
):
    response = await request(
        endpoint="cruises",
        method="POST",
        params={
            "cruiseline": cruiseline,
            "ship": ship
        },
    )

    return response