from pydantic import BaseModel, ConfigDict, Field


class SearchKnowledgeBaseArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str = Field(description="The search query.")


class LookupAccountArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    account_id: str = Field(description="The account id to inspect.")


class SendMessageArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    recipient: str = Field(description="The message recipient.")
    subject: str = Field(description="The message subject.")
    body: str = Field(description="The message body.")
