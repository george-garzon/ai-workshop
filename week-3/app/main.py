from fastapi import FastAPI, APIRouter, Query
from app.schemas import ChatRequest
from app.api.routes.chat import health as health_endpoint
from app.api.routes.chat import chat as chat_endpoint
from app.api.routes.chat import document_by_id as doc_endpoint
from app.api.routes.chat import document_search


app = FastAPI()
api_router = APIRouter(prefix="/api")
app.include_router(api_router)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@api_router.get("/health")
def health():
    return health_endpoint()

@api_router.post("/chat")
async def chat(request: ChatRequest):
    response = await chat_endpoint(request)
    return response

@api_router.get("/documents/{document_id}")
async def document_file_id(document_id: int):
    response = await doc_endpoint(document_id)
    return response

@api_router.get("/documents")
async def documents():
    response = await document_search()
    return response
