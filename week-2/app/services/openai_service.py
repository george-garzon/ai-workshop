# app/services/openai_service.py

from openai import OpenAI, AsyncOpenAI
from openai.types.responses import ResponseUsage

from app.core.settings import settings

TOOL_REGISTRY = {
    "search_cruises": search_cruises,
    "get_ship": get_ship,
}

async def asyncopenai(
    instructions: str,
    question: str,
    model: str = "gpt-5.5",
    retries: int = 5,
    timeout: float = 20.0,
):
    api_key = settings.openai_api_key
    client = AsyncOpenAI(
        api_key=api_key,
        max_retries=retries,
        timeout=timeout,
    )

    response = await client.responses.create(
        model=model,
        instructions=instructions, # instructions="You are a coding assistant that talks like a pirate.",
        input=question, # input="How do I check if a Python object is an instance of a class?",
        stream=True,
        max_output_tokens=500,
    )

    output = ""
    usage = None

    # Use tools to provide response
    # tool = TOOL_REGISTRY.get(tool_name)
    #
    # if not tool:
    #     raise ValueError(f"Unknown tool: {tool_name}")
    #
    # result = await tool(args)

    async for event in response:
        if event.type == "error":
            raise RuntimeError(event.error.message)

        if event.type == "response.output_text.delta":
            output += event.delta

        if event.type == "response.completed":
            usage = event.response.usage

    return {
        "response": output,
        "usage": usage,
    }



def clientopenai(
    instructions: str,
    question: str,
    model: str = "gpt-5.5",
    retries: int = 5,
    timeout: float= 20.0
) -> str | None:
    """
    :rtype: None
    :param instructions: 
    :param question: 
    :param model: 
    :param retries: 
    :param timeout: 
    """
    api_key = settings.openai_api_key
    client = OpenAI(
        api_key=api_key,
        max_retries=retries,  # default is 2
        timeout=timeout, # 20 seconds (default is 10 minutes)
    )

    response = client.responses.create(
        model=model,
        instructions=instructions, # instructions="You are a coding assistant that talks like a pirate.",
        input=question, # input="How do I check if a Python object is an instance of a class?",
        stream=True,
        max_output_tokens=500,
    )

    for event in response:
        print(event)

    # return response.output_text