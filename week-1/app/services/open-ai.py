import os
from openai import OpenAI

# client = OpenAI(
#     # This is the default and can be omitted
#     api_key=os.environ.get("OPENAI_API_KEY"),
# )
#
# response = client.responses.create(
#     model="gpt-5.5",
#     instructions="You are a coding assistant that talks like a pirate.",
#     input="How do I check if a Python object is an instance of a class?",
# )
#
# print(response.output_text)

def clientopenai(instructions, question, model="gpt-5.5",retries=5, timeout=20.0) -> None:
    """
    :rtype: None
    :param instructions: 
    :param question: 
    :param model: 
    :param retries: 
    :param timeout: 
    """
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        max_retries=retries,  # default is 2
        timeout=timeout, # 20 seconds (default is 10 minutes)
    )

    response = client.responses.create(
        model=model,
        instructions=instructions, # instructions="You are a coding assistant that talks like a pirate.",
        input=question, # input="How do I check if a Python object is an instance of a class?",
    )

    print(response.output_text)