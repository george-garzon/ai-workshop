# app/tools/cruise_search.py

from app.models.cruise import CruiseArgs
from app.services.cruise_service import cruise_search, get_cruiseline_id, get_ship_id

async def fetch_cruise(args: CruiseArgs):
    print("args")
    if not args.cruiseline_id and args.cruiseline:
        args.cruiseline_id = await get_cruiseline_id(args.cruiseline)

    if not args.ship_id and args.ship:
        args.ship_id = await get_ship_id(args.ship)

    cruises = await cruise_search(
        cruiseline_id=args.cruiseline_id,
        ship_id=args.ship_id,
        staterooms=args.staterooms,
    )

    return cruises