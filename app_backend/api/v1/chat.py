from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


#request body schema
class ChatRequest(BaseModel):
    question:str

#Response schema
class ChatResponse(BaseModel):
    answer:str
    disclaimer:str

@router.post("/chat", response_model=ChatResponse)
def chat_with_medical_ai(request: ChatRequest):
    return {
        "answer": "This is a placeholder response. Medical AI logic will be added later.",
        "disclaimer": "This information is for educational purposes only and is not medical advice."
    }