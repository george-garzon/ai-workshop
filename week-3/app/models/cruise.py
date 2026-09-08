from pydantic import BaseModel, ConfigDict, Field

class CruiseArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    cruiseline: str = Field(
        default="Royal Caribbean",
        description="Name of Cruiseline"
    )
    cruiseline_id: int | None = Field(
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
    departure_port: str | None = Field(
        default="miami, florida",
        description="Name of Departure Port: City, State"
    )
    embarkation_date: str | None = Field(
        default=None,
        description="Date the cruise starts. Formed like YYYY-MM-DD"
    )
    disembarkation_date: str | None = Field(
        default=None,
        description="Date the cruise ends. Formed like YYYY-MM-DD"
    )
    nights: int | None = Field(
        default=None,
        description="Count of nights sailed"
    )
    interior: str | None = Field(
        default=None,
        description="Cost of an interior stateroom per night, per person"
    )
    oceanview: str | None = Field(
        default=None,
        description="Cost of an oceanview stateroom per night, per person"
    )
    balcony: str | None = Field(
        default=None,
        description="Cost of a balcony stateroom per night, per person"
    )
    suite: str | None = Field(
        default=None,
        description="Cost of a suite stateroom per night, per person"
    )
    staterooms: str | None = Field(
        default=None,
        description="comma separated value of stateroom types: interior,oceanview,balcony,suite",
    )
