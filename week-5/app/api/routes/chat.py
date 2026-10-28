"""Exercise 9: translate between HTTP requests and the agent service.

Purpose
-------
These handlers form the API boundary. FastAPI validates incoming JSON using
the request schema; chat hands that validated object to services/agent.py.
main.py will connect the handlers to URLs. Keep the agent loop out of this file.

Build it yourself
-----------------
1. Complete schemas/chat.py and services/agent.py before wiring this handler.
2. In chat, await run_agent(request) and return its AgentRunResponse.
3. Let schema validation handle missing, empty, and whitespace-only input.
   If you choose extra business validation here, give it a clear HTTP error.
4. While learning, you may translate NotImplementedError into HTTP 501 with a
   helpful exercise message. Translate unexpected service errors into a generic
   HTTP 500 response; keep exception details in server logs instead of exposing
   credentials, tool arguments, or provider internals to the caller.
5. Implement health as a small local liveness response, such as {"status": "ok"}.
   It should not call the model, load credentials, or execute tools.

Check your work
---------------
After main.py registers the routes, missing/blank input should fail validation,
a stubbed agent result should serialize correctly, and /health should return
HTTP 200 even without .env. A string "200" in a JSON body is not an HTTP status.
"""

from app.schemas.chat import AgentRunRequest, AgentRunResponse


async def chat(request: AgentRunRequest) -> AgentRunResponse:
    """TODO: delegate to run_agent and translate appropriate errors to HTTP."""
    raise NotImplementedError("Exercise 9: implement the agent request handler.")


def health() -> dict[str, str]:
    """TODO: return a simple liveness payload without calling other services."""
    raise NotImplementedError("Exercise 9: implement the health handler.")
