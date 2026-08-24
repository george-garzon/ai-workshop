from pydantic import BaseModel, Field

class CruiseArgs(BaseModel):
    cruiseline: str = Field(
        default="Royal Caribbean",
        description="Name of Cruiseline"
    )
    cruiseline_id: int = Field(
        default=1,  # 1 for Royal Caribbean
        description="ID Map of Cruiseline in the database"
    )
    ship: str = Field(
        description="Name of Ship"
    )
    ship_id: int | None = Field(
        default=None,
        description="ID Map of Ship in the database"
    )
    departure_port: str = Field(
        default="miami, florida",
        description="Name of Departure Port: City, State"
    )
    embarkation_date: str | None = Field(
        description="Date the cruise starts. Formed like YYYY-MM-DD"
    )
    disembarkation_date: str | None = Field(
        description="Date the cruise ends. Formed like YYYY-MM-DD"
    )
    nights: int | None = Field(
        description="Count of nights sailed"
    )
    interior: str | None = Field(
        description="Cost of an interior stateroom per night, per person"
    )
    oceanview: str | None = Field(
        description="Cost of an oceanview stateroom per night, per person"
    )
    balcony: str | None = Field(
        description="Cost of a balcony stateroom per night, per person"
    )
    suite: str | None = Field(
        description="Cost of a suite stateroom per night, per person"
    )