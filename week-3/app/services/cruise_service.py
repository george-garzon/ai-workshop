# app/services/cruise_service.py

import json
from typing import Any

from .http_service import request


def _extract_records(response: Any, *keys: str) -> list[dict[str, Any]]:
    """Extract a record list from either a list or an API response wrapper."""
    if isinstance(response, str):
        response = json.loads(response)

    if isinstance(response, list):
        records = response
    elif isinstance(response, dict):
        records = next(
            (
                response[key]
                for key in keys
                if isinstance(response.get(key), list)
            ),
            None,
        )

        if records is None:
            records = next(
                (value for value in response.values() if isinstance(value, list)),
                None,
            )
    else:
        records = None

    if records is None or not all(isinstance(record, dict) for record in records):
        raise ValueError("Backend API did not return a list of records")

    return records

async def document_search(
        file_id: int,
):
    response = await request(
        endpoint=f"documents/{file_id}",
        method="GET",
        params={
            "file_id": file_id
        },
    )

    return response


async def document_chunk_search(
        file_id: int,
):
    response = await request(
        endpoint=f"documents/{file_id}",
        method="GET",
        params={
            "file_id": file_id
        },
    )

    return response

async def cruise_search(
    cruiseline_id: int | None = None,
    ship_id: int | None = None,
    staterooms: str | None = None,
    page: int = 1,
):
    params = {
        "cruiseline": cruiseline_id,
        "ship": ship_id,
        "staterooms": staterooms,
        "page": page,
    }

    # Avoid transmitting ?ship=None or equivalent.
    params = {key: value for key, value in params.items() if value is not None}

    return await request(
        endpoint="cruise-market",
        method="GET",
        params=params,
    )


async def ship_search(
        ship_id: int,
):
    response = await request(
        endpoint=f"ships/{ship_id}",
        method="GET",
        params={
            "ship_id": ship_id
        },
    )

    return response

async def ship_amenity_search(
    ship_id: int,
):
    response = await request(
        endpoint=f"ships/amenities/{ship_id}",
        method="GET",
    )
    return response

async def get_ship_id(ship_name: str) -> int:
    response = await request(
        endpoint="ships",
        method="GET",
    )
    ships = _extract_records(response, "ships", "ship_details", "data")

    for ship in ships:
        name = ship.get("name") or ship.get("ship_name")
        if isinstance(name, str) and name.lower() == ship_name.lower():
            return ship["id"]

    raise ValueError(f"Ship not found: {ship_name}")

async def get_cruiseline_id(cruiseline_name: str) -> int:
    response = await request(
        endpoint="cruiselines",
        method="GET",
    )
    cruiselines = _extract_records(
        response,
        "cruiselines",
        "cruiseline_details",
        "data",
    )

    for cruiseline in cruiselines:
        name = cruiseline.get("name") or cruiseline.get("cruiseline")
        if isinstance(name, str) and name.lower() == cruiseline_name.lower():
            return cruiseline["id"]

    raise ValueError(
        f"Cruise line not found: {cruiseline_name}"
    )
