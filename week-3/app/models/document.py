from pydantic import BaseModel, Field, ConfigDict

class DocumentArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    file_id: int = Field(
        description='Internal file id of document saved in database',
    )
    document_name: str | None = Field(
        description='Full name of document'
    )
    file_type: str | None = Field(
        description='Commonly `pdf`'
    )
    status: int | None = Field(
        description='Only values are `1` for active or `0` for inactive'
    )


class DocumentByIdArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    document_id: int = Field(
        description="The record's id field from the document catalog",
    )
    query: str = Field(
        description="The user's question used to retrieve relevant PDF chunks",
    )

class DocumentChunkArgs(BaseModel):
    file_id: int = Field(
        description='Internal file id of document saved in database',
    )
    chunk_index: str | None
    content: str | None
    page_number: int | None
    section_name: str | None
    embedding: str | None

class DocumentStore:
    def __init__(self):
        self.chunks: list[str] = []
        self.embeddings: list[list[float]] = []
        self.document_ids: list[int] = []
