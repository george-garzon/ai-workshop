from fastapi import FastAPI, APIRouter
from app.api.routes.chat import health as health_endpoint
from app.api.routes.chat import chat as chat_endpoint
from app.models.cruise import CruiseArgs
from app.schemas import ChatRequest, ChatResponse
from app.tools import fetch_ship, fetch_cruise

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

@api_router.get("/ship/{ship_id}")
async def ship_by_id(ship_id: int):
    args = CruiseArgs.model_construct(ship_id=ship_id)
    return await fetch_ship(args)

@api_router.get("/sample-cruise-market")
async def sample_cruise_market():
    args = CruiseArgs.model_construct(
        cruiseline_id=1,
        ship_id=1,
        staterooms = "suite",
    )
    return await fetch_cruise(args)
