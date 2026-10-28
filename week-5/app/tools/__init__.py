"""Package for concrete capabilities and their registry.

Purpose: sample_tools.py implements the actions; registry.py declares which
actions the agent may request. services/tools.py validates and dispatches them.
These are three different responsibilities even though all concern tools.

Your task: leave this initializer minimal. Implement local tools first, then
register them. Use direct imports from app.tools.registry when wiring services.
Do not run tools or construct external service clients during package import.

Check: you should be able to explain how a string tool name becomes a validated
model instance and then a call to one specific Python function.
"""
