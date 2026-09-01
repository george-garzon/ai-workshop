from pydantic import BaseModel, Field, ConfigDict

class Document(BaseModel):
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

class DocumentChunk(BaseModel):
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
        self.embeddings: None
