# app/services/cruise_service.py

from .http_service import request

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
    ships = await request(
        endpoint="ships",
        method="GET",
    )

    for ship in ships:
        if ship["name"].lower() == ship_name.lower():
            return ship["id"]

    raise ValueError(f"Ship not found: {ship_name}")

async def get_cruiseline_id(cruiseline_name: str) -> int:
    cruiselines = await request(
        endpoint="cruiselines",
        method="GET",
    )

    for cruiseline in cruiselines:
        if cruiseline["name"].lower() == cruiseline_name.lower():
            return cruiseline["id"]

    raise ValueError(
        f"Cruise line not found: {cruiseline_name}"
    )