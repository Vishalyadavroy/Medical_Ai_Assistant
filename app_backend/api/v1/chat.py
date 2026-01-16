from fastapi import APIRouter
from pydantic import BaseModel
from app_backend.schemas.chat import ChatResponse , ChatRequest
from app_backend.services.chat_service import process_chat

router = APIRouter()


# #request body schema
# class ChatRequest(BaseModel):
#     question:str

# #Response schema
# class ChatResponse(BaseModel):
#     answer:str
#     disclaimer:str

@router.post("/chat", response_model=ChatResponse)
def chat_with_medical_ai(request: ChatRequest):
    return process_chat(request)