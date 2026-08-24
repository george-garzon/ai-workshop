import httpx


async def fetch_weather(
    city: str,
    state: str | None,
    units: str,
):
    # Normally call a real weather API here.

    return {
        "city": city,
        "state": state,
        "temperature": 87,
        "units": units,
        "condition": "Partly cloudy",
    }