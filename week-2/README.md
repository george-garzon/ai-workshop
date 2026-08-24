# Cruise Search Tool Calling

## Goal

Move beyond chat and make an LLM interact safely with application code.

This example allows the LLM to use cruise-search tools to query application data and return matching sailings in a user-friendly response.

## Example Request

### `POST /api/chat`

```json
{
  "instructions": "Help users find cruises. Use the available cruise-search tools when needed.",
  "question": "Find me a Royal Caribbean sailing with a suite stateroom aboard Harmony of the Seas."
}
```

## Example Response

The API returned 18 matching sailings and summarized several options:

| Sailing | Date | Nights | From | Suite From |
| --- | --- | ---: | --- | ---: |
| **Perfect Day Getaway Cruise** | Oct 1, 2026 | 2 | Orlando / Port Canaveral, FL | **$688** |
| **Bahamas & Perfect Day Cruise** | Nov 10, 2026 | 4 | Orlando / Port Canaveral, FL | **$1,610** |
| **Bahamas & Perfect Day Cruise** | Nov 5, 2026 | 5 | Orlando / Port Canaveral, FL | **$1,631** |
| **Perfect Day at CocoCay & Caribbean** | Sep 11, 2026 | 7 | Orlando / Port Canaveral, FL | **$2,000** |
| **Eastern Caribbean & Perfect Day** | Dec 12, 2026 | 7 | Orlando / Port Canaveral, FL | **$2,348** |

**Lowest suite price found:** A 2-night Perfect Day Getaway Cruise departing October 1, 2026, from Orlando / Port Canaveral, Florida, visiting Perfect Day at CocoCay, with suites from **$688**.

## Raw API Response

```json
{
  "response": "I found **18 Royal Caribbean sailings** aboard **Harmony of the Seas** with **Suite** stateroom availability. Here are some good options:\n\n| Sailing | Date | Nights | From | Suite From |\n|---|---:|---:|---|---:|\n| **Perfect Day Getaway Cruise** | Oct 1, 2026 | 2 | Orlando / Port Canaveral, FL | **$688** |\n| **Bahamas & Perfect Day Cruise** | Nov 10, 2026 | 4 | Orlando / Port Canaveral, FL | **$1,610** |\n| **Bahamas & Perfect Day Cruise** | Nov 5, 2026 | 5 | Orlando / Port Canaveral, FL | **$1,631** |\n| **Perfect Day at CocoCay & Caribbean** | Sep 11, 2026 | 7 | Orlando / Port Canaveral, FL | **$2,000** |\n| **Eastern Caribbean & Perfect Day** | Dec 12, 2026 | 7 | Orlando / Port Canaveral, FL | **$2,348** |\n\n**Lowest suite price found:**  \n**2-night Perfect Day Getaway Cruise** departing **Oct 1, 2026** from **Orlando / Port Canaveral, Florida**, visiting **Perfect Day at CocoCay**, with suites from **$688**.\n\nWould you like me to narrow these down by **travel month, trip length, destination, or budget**?",
  "usage": {
    "input_tokens": 7136,
    "cached_tokens": 0,
    "output_tokens": 321,
    "reasoning_tokens": 0,
    "total_tokens": 7457
  }
}
```

## What This Demonstrates

- The LLM recognizes when it needs current application data.
- It calls an available cruise-search tool instead of inventing results.
- It converts the tool output into an easy-to-read response.
- It reports token usage for monitoring and cost analysis.
