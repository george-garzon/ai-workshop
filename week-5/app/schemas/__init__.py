"""Package for public HTTP request and response models.

Purpose: schemas/chat.py is the contract shared by callers and the API. Keeping
it separate from internal state lets you change loop details without exposing
them all to clients.

Your task: complete chat.py; this initializer needs no implementation. The
scaffold uses direct imports from app.schemas.chat. If you later re-export names
here, learn how imports and __all__ work before updating the callers.

Check: reading the three public schemas should be enough to explain the JSON
accepted by POST /api/agent and the answer/steps JSON it returns.
"""
