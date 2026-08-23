# app/services/openai_service.py

from openai import OpenAI, AsyncOpenAI
from app.core.settings import settings

async def asyncopenai(
    instructions: str,
    question: str,
    model: str = "gpt-5.5",
    retries: int = 5,
    timeout: float = 20.0,
) -> str | None:
    async def main():
        stream = await client.responses.create(
            model="gpt-5.5",
            input="Write a one-sentence bedtime story about a unicorn.",
            stream=True,
        )

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
    )

    async for event in response:
        # Error Handling
        if event.type == 'error':
            print(event.error.type)
            print(event.error.code)
            print(event.error.event_id)
            print(event.error.message)
        # Print everything else normally.
        print(event)

    # asyncio.run(asyncopenai()) # Used in OpenAI GitHub Docs
    # return response



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
    )

    for event in response:
        print(event)

    # return response.output_text