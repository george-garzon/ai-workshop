"""Package for application behavior.

Purpose: services coordinate the agent, model access, tool execution, approval,
and logging. They sit between HTTP handlers and the lower-level data/tool code.

Your task: implement each service's exercise in the README order. Import the
specific module you need, for example app.services.agent, instead of eagerly
importing every service here. This helps avoid circular imports and makes
individual pieces easier to test.

Check: services should work with a fake model and fake tools without a running
HTTP server. Importing this package should not begin an agent run.
"""
