
"""Package boundary for the HTTP interface.

Purpose: group the web-facing layer separately from business services. Requests
enter through routes/, are parsed as schemas, and then call services/.

Your task: no implementation is needed here. Keep HTTP handlers in routes/chat.py
and application wiring in main.py. Do not put the agent loop in this initializer.

Check: importing this package should not register routes or create an API client;
those actions belong to explicit setup in their respective modules.
"""
