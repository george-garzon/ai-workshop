# app/tools/ship_details.py
from app.models.cruise import CruiseArgs
from app.services.cruise_service import ship_search, ship_amenity_search, get_ship_id

async def fetch_ship(args: CruiseArgs):
    if not args.ship_id and args.ship:
        args.ship_id = await get_ship_id(args.ship)

    ship = await ship_search(
        ship_id=args.ship_id
    )

    return ship

async def fetch_ship_amenities(args: CruiseArgs):
    if not args.ship_id and args.ship:
        args.ship_id = await get_ship_id(args.ship)

    amenities = await ship_amenity_search(
        ship_id = args.ship_id
    )

    return amenities