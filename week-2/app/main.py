from fastapi import FastAPI, APIRouter
from app.api.routes.chat import health as health_endpoint
from app.api.routes.chat import chat as chat_endpoint
from app.schemas import ChatRequest, ChatResponse

app = FastAPI()
api_router = APIRouter(
    prefix="/api",
)
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health():
    return health_endpoint()

@api_router.post("/chat")
async def chat(request: ChatRequest):
    response = await chat_endpoint(request)
    return response
