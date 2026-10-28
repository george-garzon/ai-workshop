"""Exercise 1A: define the public API's data shapes.

Purpose
-------
Schemas describe the JSON entering and leaving the HTTP API. Pydantic models
validate that data and let FastAPI describe it in /docs. Internal reasoning
state belongs in models/agent.py; the client only needs a useful answer and
a safe record of what happened.

Build it yourself
-----------------
1. Add fields to the three model shells using the contracts below.
2. Use type hints for validation and Field descriptions for API documentation.
3. Strip surrounding whitespace and reject blank request strings. A minimum
   length alone does not reject a string containing only spaces.
4. Use a default_factory for lists so each response gets its own steps list.
5. Decide which tool details are safe to expose. A step is an execution summary,
   not private model reasoning or an unfiltered dump of account information.

Check your work
---------------
Construct a request with instructions and a question, then try missing fields
and whitespace-only text. Construct two responses and append a step to one:
the other response must stay unchanged. Inspect model_dump() to see the JSON
shape. Empty model shells currently accept no defined fields; they are not a
finished validation contract.
"""

from pydantic import BaseModel


class AgentRunRequest(BaseModel):
    """TODO: add two required, nonblank strings.

    instructions: caller-provided guidance about the task. This must never
        override application-owned tool restrictions or approval policy.
    question: the actual task the caller wants the agent to perform.

    Example values: "Use tools when useful" and "Look up account demo-001".
    """

    pass


class AgentStep(BaseModel):
    """TODO: describe one decision attempt in the returned execution trace.

    iteration: integer, starting at 1 for the first decision attempt.
    action: optional string (tool, final, approval_required, or an error label).
    tool_name: optional string identifying a requested tool.
    tool_arguments: optional dictionary of string keys to JSON-compatible values.
    observation: optional JSON-compatible output safe for the caller to see.
    error: optional readable description when this attempt fails.

    Give optional fields a default of None. A nullable type alone does not make
    a field optional to provide. Record failures as well as successful tools.
    """

    pass


class AgentRunResponse(BaseModel):
    """TODO: add response and steps.

    response: required string containing the final answer or a clear stop reason.
    steps: list of AgentStep objects, with a new empty list for each response.

    Example: a lookup followed by a final answer should show both attempts in
    steps. Approval denial and iteration-limit exits should retain prior steps.
    """

    pass
