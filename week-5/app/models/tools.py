"""Exercise 1C: validate the input to each permitted tool.

Purpose
-------
A ToolCall contains a generic arguments dictionary. These models turn that
dictionary into the particular input a tool accepts. The registry links tool
names to these models, and services/tools.py validates arguments before use.

Build it yourself
-----------------
1. Add the fields listed in each class below.
2. Require nonblank strings and reject unexpected fields with extra="forbid".
   Decide how to strip whitespace without silently changing meaningful content.
3. Add Field descriptions explaining the inputs. Later the registry can obtain
   JSON Schema from model_json_schema() instead of duplicating these definitions.
4. Keep execution out of these classes; they describe data, not database access
   or message sending.

Check your work
---------------
Validate {"account_id": "demo-001"} with LookupAccountArgs.model_validate().
Then try a missing account_id, an unknown extra field, and a blank string.
Each invalid case must fail before the account lookup function can run.
"""

from pydantic import BaseModel


class SearchKnowledgeBaseArgs(BaseModel):
    """TODO: add query, a required nonblank string describing the search text.

    Example: {"query": "refund policy"}. The tool receives this model instance,
    so its implementation will read a named attribute instead of guessing keys.
    """

    pass


class LookupAccountArgs(BaseModel):
    """TODO: add account_id, a required nonblank string identifying an account.

    Example: {"account_id": "demo-001"}. Keep identifiers as strings so leading
    zeros and nonnumeric prefixes are preserved.
    """

    pass


class SendMessageArgs(BaseModel):
    """TODO: add required nonblank recipient, subject, and body strings.

    Use a fake recipient such as learner@example.test for exercises. Valid text
    does not establish permission to send; approval belongs in services/approval.py.
    """

    pass
