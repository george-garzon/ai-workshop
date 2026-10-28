
"""Package for application-wide configuration.

Purpose: keep shared setup such as environment-backed settings in one place.
The actual settings exercise is in settings.py.

Your task: no executable code is needed here. Import get_settings directly from
app.core.settings when a service needs configuration. Avoid constructing a
global Settings object here, because that can require credentials just to
import unrelated models or run offline checks.

Check: importing app.core should work without an OPENAI_API_KEY.
"""
