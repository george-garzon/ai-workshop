"""Exercise 4: validate and dispatch a tool proposal.

Purpose
-------
The model produces a generic ToolCall. This service checks its name against the
allowlist, validates its arguments with the correct model, then invokes the
registered Python function. The tool implementations do their specific jobs;
this service handles the shared mechanics and a consistent result shape.

Build it yourself
-----------------
1. Implement validate_tool_call using TOOL_REGISTRY and TOOL_ARGUMENT_MODELS.
   Reject a name missing from either mapping; never evaluate model-generated
   code or dynamically import a module named by the model.
2. Validate the dictionary with the registered Pydantic model and return that
   model instance. Unknown names and invalid arguments should raise clear errors.
3. In execute_tool, validate before invoking anything, retrieve the registered
   handler, and await it with the validated model as its single argument.
4. Wrap a successful output in ToolExecutionResult. Convert expected validation
   and handler failures into its error field so the loop can record them. Keep
   details useful without exposing secrets or entire external responses.
5. During development, allow NotImplementedError to remain visible rather than
   swallowing every unfinished exercise in a generic error handler.

Approval contract
-----------------
run_agent is responsible for gating sensitive actions BEFORE it calls this
service. This function's signature has no approval token and does not establish
permission by itself. Keep it internal and use simulated tools for the exercise.
If you later expose execution elsewhere, design an explicit authorization check
at that boundary too.

Check your work
---------------
A known tool with good arguments should be awaited once. Unknown names, extra
fields, and missing required fields should invoke no handler. A failing handler
should produce an error result rather than a fake success. Test with a local
async fake; none of these checks need an LLM or an external account.
"""

from pydantic import BaseModel

from app.models.agent import ToolCall, ToolExecutionResult


def validate_tool_call(tool_call: ToolCall) -> BaseModel:
    """TODO: return the argument model instance for a permitted, valid call."""
    raise NotImplementedError("Exercise 4: validate the tool name and arguments.")


async def execute_tool(tool_call: ToolCall) -> ToolExecutionResult:
    """TODO: validate, await the handler, and normalize its output or error."""
    raise NotImplementedError("Exercise 4: implement controlled tool dispatch.")
