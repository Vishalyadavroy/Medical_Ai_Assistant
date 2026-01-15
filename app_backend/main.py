from fastapi import FastAPI
from dotenv import load_dotenv
from app_backend.api.v1.chat import router as chat_router

load_dotenv() #Load environment variables from .env

app = FastAPI(
    title="Medical AI Assistant",
    description="Safe Medical education assistant with Soap reports",
    version="1.0.0"
)


app.include_router(chat_router, prefix="/api/v1")

@app.get("/")
def health_check():
    return{
        "status" : "ok",
        "message" : "Medical Ai Assistant backend is running"

    }