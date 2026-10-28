
"""Package for internal data contracts.

Purpose: agent.py describes decisions/state/results; tools.py describes each
tool's validated inputs. These are Pydantic data models, not database tables.
Public HTTP request and response shapes live separately in app/schemas/.

Your task: complete the model classes in those two files. Keep this initializer
minimal and use direct imports while learning so dependencies stay visible.
Optional re-exports can come later if you prefer shorter import paths.

Check: models should be usable in a small local script without starting FastAPI
or constructing a model-provider client.
"""
from .agent import ToolCall, AgentDecision, AgentState, ToolExecutionResult
from .tools import SearchKnowledgeBaseArgs, LookupAccountArgs, SendMessageArgs

__all__ = [
    'ToolCall',
    'AgentDecision',
    'AgentState',
    'ToolExecutionResult',
    'SearchKnowledgeBaseArgs',
    'LookupAccountArgs',
    'SendMessageArgs'
]