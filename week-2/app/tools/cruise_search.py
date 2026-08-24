# app/tools/cruise_search.py

from app.models.cruise import CruiseArgs
from app.services.cruise_service import cruise_search, ship_search


async def fetch_cruise(args: CruiseArgs):
    cruises = await cruise_search(
        cruiseline=args.cruiseline,
        ship=args.ship,
        embarkation_date=args.embarkation_date,
        nights=args.nights
    )

    return cruises

async def fetch_ship(args: CruiseArgs):
    ship = await ship_search(
        cruiseline=args.cruiseline,
        ship=args.ship
    )

    return ship