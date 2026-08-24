# app/schemas/cruise.py
from pydantic import BaseModel

class Ship(BaseModel):
    id: int
    name: str
    cruiseline_id: int
    cruiseline: str
    ship_code: str | None = None
    maiden_voyage: str | None = None
    built_at: str | None = None
    total_decks: int | None = None
    guest_decks: int | None = None
    crew_count: int | None = None
    staterooms: int | None = None
    guest_capacity: int | None = None
    double_occupancy_capacity: int | None = None
    gross_tonnage: int | None = None
    length_ft: int | None = None
    width_ft: int | None = None
    draft_ft: int | None = None
    status: int # 1 or 0
    imo: str | None = None
    mmsi: str | None = None

class CruiseDetail(BaseModel):
    id: int | None = None
    destination_code: str
    destination_name: str | None = None
    itinerary_id: str | None = None
    cruise_title: str | None = None
    cruiseline_name: str | None = None
    cruiseline_short: str | None = None
    ship_name: str | None = None
    departure_port: str | None = None
    embarkation_date: str | None = None
    disembarkation_date: str | None = None
    ports: str | None = None
    region: str | None = None
    nights: str | None = None
    deals: str | None = None
    interior: str | None = None
    oceanview: str | None = None
    balcony: str | None = None
    suite: str | None = None
    studio: str | None = None
    cruiseline_id: int | None = None
    ship_id: int | None = None
    port_fees: float | None = None
    currency: str | None = None

class Cruiseline(BaseModel):
    id: int
    cruiseline: str # name
    shortcode: str
    status: int # 1 or 0