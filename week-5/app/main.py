from fastapi import APIRouter, FastAPI

from app.api.routes.chat import chat as chat_endpoint
from app.api.routes.chat import health as health_endpoint
from app.schemas import AgentRunRequest


app = FastAPI()
api_router = APIRouter(prefix="/api")
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health():
    return health_endpoint()


@api_router.post("/agent")
async def agent(request: AgentRunRequest):
    return await chat_endpoint(request)
