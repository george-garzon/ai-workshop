"""Exercise 3B: define the small set of capabilities your agent can request.

Purpose
-------
This registry connects a public tool name to its Python handler, argument model,
description, and approval policy. The executor uses the mappings; the decision
service uses the catalog to explain available choices to the model.

Build it yourself
-----------------
1. Finish models/tools.py and the local tools in sample_tools.py first.
2. Fill TOOL_REGISTRY with the three names below and their function objects.
   Store functions without calling them: registration must not execute a tool.
3. Fill TOOL_ARGUMENT_MODELS with those same names and the matching model classes.
4. Add send_message to SENSITIVE_TOOLS before enabling it for the agent.
5. Build TOOL_SCHEMAS as a list of descriptions: each entry needs a name,
   description, and parameters obtained from the argument model's JSON Schema.
   Mention that send_message is simulated and requires approval. This is a local
   catalog for the structured-decision exercise, not automatically a valid
   provider-specific tools payload; adapt it if you later use native tool calls.
6. Keep names synchronized across all collections. A small consistency check
   should catch a described tool with no handler or an unvalidated handler.

Connections to make
-------------------
search_knowledge_base -> search_knowledge_base function -> SearchKnowledgeBaseArgs
lookup_account       -> lookup_account function       -> LookupAccountArgs
send_message         -> send_message function         -> SendMessageArgs

Check your work
---------------
The handler and model mappings should have identical keys. Catalog names should
match them without duplicates; sensitive names must be a subset of registered
names. No tool should execute while importing this file. The empty collections
below are deliberate exercise placeholders, not a configured working registry.
"""

from typing import Any, Awaitable, Callable

from pydantic import BaseModel


# A handler takes one validated argument-model instance and returns an awaitable.
# Any keeps this starter alias simple; you can explore more precise typing later.
ToolHandler = Callable[[Any], Awaitable[Any]]

# TODO: associate allowed names with async functions from sample_tools.py.
TOOL_REGISTRY: dict[str, ToolHandler] = {}

# TODO: associate the same names with model CLASSES, not model instances.
TOOL_ARGUMENT_MODELS: dict[str, type[BaseModel]] = {}

# TODO: declare sensitive names as application policy, independent of the model.
SENSITIVE_TOOLS: set[str] = set()

# TODO: describe registered tools and derive parameter shapes from their models.
TOOL_SCHEMAS: list[dict[str, Any]] = []
