from fastapi import FastAPI
from app.api.routes.endpoints import health as health_endpoint
from app.api.routes.endpoints import chat as chat_endpoint

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
def chat():
    return chat_endpoint()
@app.get("/health")
def health():
    return health_endpoint()