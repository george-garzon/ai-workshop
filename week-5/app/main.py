"""Exercise 10: assemble the HTTP application.

Purpose
-------
This is the entry point that Uvicorn imports. Its job is to create the FastAPI
application and connect URLs to the handlers in api/routes/chat.py. Business
rules belong in services/, so this file should stay small.

Build it yourself
-----------------
1. Keep the FastAPI instance below; it is the only working app setup provided.
2. Complete the request/response schemas and the route handlers first.
3. Create an APIRouter with the prefix /api. Register an async POST /agent
   handler on it, taking AgentRunRequest and declaring AgentRunResponse as its
   response model. Delegate to the chat handler and await its result.
4. Include the router in app AFTER registering its routes. Including an empty
   router and adding routes afterward can leave those routes off the app.
5. Register GET /health and delegate to the health handler. Optionally add a
   GET / route describing this learning project.

Check your work
---------------
Run the server from week-5 (commands in README.md). Initially /docs exists,
but /health and /api/agent return 404 because you have not registered them.
After wiring the routes, /docs should list both. /health should work without
an API key; /api/agent should eventually return a response and a steps list.

Explain to yourself: why does awaiting a service belong in a route handler,
while choosing which tool to run belongs in the agent service?
"""

from fastapi import FastAPI


app = FastAPI(title="Week 5 Agent Fundamentals — Learning Scaffold")

# TODO: Add route wiring here after completing api/routes/chat.py.
