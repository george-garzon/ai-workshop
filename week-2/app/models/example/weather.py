from pydantic import BaseModel, Field

class WeatherArgs(BaseModel):
    city: str = Field(
        description="City to get the weather for"
    )

    state: str | None = Field(
        default=None,
        description="US state abbreviation, such as FL or NY"
    )

    units: str = Field(
        default="fahrenheit",
        description="Temperature units: fahrenheit or celsius"
    )