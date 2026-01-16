from fastapi import FastAPI
from app_backend.api.v1.chat import router as chat_router
from app_backend.api.v1.soap import router  as soap_router

app = FastAPI(
    title="Medical AI Assistant",
    description="Safe Medical education assistant with Soap reports",
    version="1.0.0"
)


app.include_router(chat_router, prefix="/api/v1")
app.include_router(soap_router, prefix="/api/v1")

@app.get("/")
def health_check():
    return{
        "status" : "ok",
        "message" : "Medical Ai Assistant backend is running"
    }