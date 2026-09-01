import json
from typing import Any

from openai import AsyncOpenAI

from app.core.settings import settings
from app.models.cruise import CruiseArgs
from app.tools import fetch_cruise, fetch_ship

# 1. Send tool schemas to OpenAI.
# 2. Detect function_call outputs.
# 3. Validate arguments with CruiseArgs.
# 4. await the registered function.
# 5. Return its result using function_call_output.
# 6. Ask the model for its final answer.

TOOL_REGISTRY = {
    "search_cruises": fetch_cruise,
    "get_ship": fetch_ship,
}

TOOLS = [
    {
        "type": "function",
        "name": "search_cruises",
        "description": "Search for cruises matching the user's requirements.",
        "parameters": CruiseArgs.model_json_schema(),
        "strict": False,
    },
    {
        "type": "function",
        "name": "get_ship",
        "description": "Get details about a cruise ship.",
        "parameters": CruiseArgs.model_json_schema(),
        "strict": False,
    },
]


async def execute_tool(tool_call) -> dict[str, Any]:
    tool = TOOL_REGISTRY.get(tool_call.name)

    if tool is None:
        raise ValueError(f"Unknown tool: {tool_call.name}")

    raw_arguments = json.loads(tool_call.arguments)
    arguments = CruiseArgs.model_validate(raw_arguments)

    result = await tool(arguments)

    return {
        "type": "function_call_output",
        "call_id": tool_call.call_id,
        "output": json.dumps(result, default=str),
    }


async def asyncopenai(
    instructions: str,
    question: str,
    model: str = "gpt-5.5",
    retries: int = 5,
    timeout: float = 20.0,
):
    async with AsyncOpenAI(
        api_key=settings.openai_api_key,
        max_retries=retries,
        timeout=timeout,
    ) as client:
        response = await client.responses.create(
            model=model,
            instructions=instructions,
            input=question,
            tools=TOOLS,
            max_output_tokens=500,
        )

        # Continue until the model no longer requests tools.
        while True:
            tool_calls = [
                item
                for item in response.output
                if item.type == "function_call"
            ]

            if not tool_calls:
                return {
                    "response": response.output_text,
                    "usage": response.usage,
                }

            tool_outputs = [
                await execute_tool(tool_call)
                for tool_call in tool_calls
            ]

            response = await client.responses.create(
                model=model,
                instructions=instructions,
                previous_response_id=response.id,
                input=tool_outputs,
                tools=TOOLS,
                max_output_tokens=500,
            )
